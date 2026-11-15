"""Contract tests for the cross-platform CI Component catalog comparison."""

import json
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.framework_validator.ci_catalog_parity import (
    compare_catalogs,
    read_catalog,
)


def catalog() -> dict:
    return {
        "components": ["documentation/example"],
        "count": 1,
        "scope": {"families": ["readme", "documentation", "workflow"]},
        "details": [{
            "path": "documentation/example",
            "id": "DOC-EXAMPLE",
            "name": "Example",
            "version": "0.1.0",
            "status": "Experimental",
            "metadata_status": "loaded",
            "metadata_sha256": "1" * 64,
            "content_sha256": "2" * 64,
        }],
    }


class CatalogParityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        root = Path(self.temp.name)
        self.ubuntu = root / "ubuntu.json"
        self.windows = root / "windows.json"

    def save(self, ubuntu: dict, windows: dict) -> None:
        self.ubuntu.write_text(json.dumps(ubuntu), encoding="utf-8")
        self.windows.write_text(json.dumps(windows), encoding="utf-8")

    def test_matching_complete_catalogs_pass(self) -> None:
        current = catalog()
        self.save(current, current)
        self.assertEqual(compare_catalogs(self.ubuntu, self.windows), 0)
        self.assertEqual(read_catalog(self.ubuntu), current)

    def test_different_content_digest_fails(self) -> None:
        linux, windows = catalog(), catalog()
        windows["details"][0]["content_sha256"] = "3" * 64
        self.save(linux, windows)
        self.assertEqual(compare_catalogs(self.ubuntu, self.windows), 1)

    def test_different_metadata_digest_fails(self) -> None:
        linux, windows = catalog(), catalog()
        windows["details"][0]["metadata_sha256"] = "3" * 64
        self.save(linux, windows)
        self.assertEqual(compare_catalogs(self.ubuntu, self.windows), 1)

    def test_different_metadata_fields_fail(self) -> None:
        linux, windows = catalog(), catalog()
        windows["details"][0]["version"] = "0.2.0"
        self.save(linux, windows)
        self.assertEqual(compare_catalogs(self.ubuntu, self.windows), 1)

    def test_malformed_or_partial_snapshots_are_rejected(self) -> None:
        for update in (
            lambda value: value.update(count=2),
            lambda value: value.pop("details"),
            lambda value: value["details"][0].pop("content_sha256"),
            lambda value: value.update(pagination={"total": 1}),
            lambda value: value["components"].append("documentation/other"),
            lambda value: value["details"][0].update(path="documentation/other"),
        ):
            with self.subTest(update=update):
                left, right = catalog(), catalog()
                update(right)
                self.save(left, right)
                self.assertEqual(compare_catalogs(self.ubuntu, self.windows), 2)

    def test_missing_artifact_is_rejected(self) -> None:
        self.ubuntu.write_text(json.dumps(catalog()), encoding="utf-8")
        self.assertEqual(compare_catalogs(self.ubuntu, self.windows), 2)


if __name__ == "__main__":
    unittest.main()
