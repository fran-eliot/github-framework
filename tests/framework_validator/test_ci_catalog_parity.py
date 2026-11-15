"""Contract tests for the cross-platform CI Component catalog comparison."""

import io
import json
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.framework_validator.ci_catalog_parity import (
    compare_catalogs,
    describe_mismatches,
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

    def test_digest_mismatch_identifies_field_without_printing_digests(self) -> None:
        left, right = catalog(), catalog()
        right["details"][0]["content_sha256"] = "3" * 64
        self.save(left, right)
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            outcome = compare_catalogs(self.ubuntu, self.windows)
        self.assertEqual(outcome, 1)
        message = stderr.getvalue()
        self.assertIn("documentation/example: content_sha256", message)
        self.assertNotIn("3" * 64, message)
        self.assertNotIn("metadata_sha256", message)

    def test_metadata_and_catalog_scope_differences_are_identified(self) -> None:
        left, right = catalog(), catalog()
        right["details"][0]["name"] = "Updated example"
        right["scope"]["families"] = ["documentation"]
        message = describe_mismatches(left, right)
        self.assertIn("documentation/example: name", message)
        self.assertIn("catalog field: scope", message)

    def test_missing_optional_detail_field_differs_from_explicit_null(self) -> None:
        left, right = catalog(), catalog()
        left["details"][0]["description"] = None
        self.save(left, right)
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            outcome = compare_catalogs(self.ubuntu, self.windows)
        self.assertEqual(outcome, 1)
        self.assertIn(
            "documentation/example: description", stderr.getvalue()
        )
        self.assertNotIn("documentation/example: ;", stderr.getvalue())

    def test_missing_top_level_field_differs_from_explicit_null(self) -> None:
        left, right = catalog(), catalog()
        right["metadata_summary"] = None
        self.save(left, right)
        stderr = io.StringIO()
        with redirect_stderr(stderr):
            outcome = compare_catalogs(self.ubuntu, self.windows)
        self.assertEqual(outcome, 1)
        self.assertIn("catalog field: metadata_summary", stderr.getvalue())

    def test_mismatch_diagnostics_are_bounded(self) -> None:
        left, right = catalog(), catalog()
        for i in range(12):
            path = f"documentation/item-{i}"
            left["components"].append(path)
            right["components"].append(path)
            original = dict(left["details"][0], path=path, name="Original")
            changed = dict(original, name="Changed")
            left["details"].append(original)
            right["details"].append(changed)
        left["count"] = right["count"] = 13
        message = describe_mismatches(left, right)
        self.assertIn("... and 2 more differences", message)
        self.assertNotIn("documentation/item-9: name", message)

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

    def test_identically_malformed_catalogs_cannot_pass_parity(self) -> None:
        def invalid_count(value: dict) -> None:
            value["count"] = True  # bool compares equal to integer 1 in Python.

        def missing_scope(value: dict) -> None:
            value.pop("scope")

        def invalid_scope(value: dict) -> None:
            value["scope"] = {"families": "documentation"}

        def duplicate_family(value: dict) -> None:
            value["scope"] = {"families": ["readme", "readme"]}

        def unknown_family(value: dict) -> None:
            value["scope"] = {"families": ["external"]}

        def blank_path(value: dict) -> None:
            value["components"][0] = ""
            value["details"][0]["path"] = ""

        for modify in (
            invalid_count, missing_scope, invalid_scope,
            duplicate_family, unknown_family, blank_path,
        ):
            with self.subTest(modify=modify.__name__):
                malformed = catalog()
                modify(malformed)
                self.save(malformed, malformed)
                stderr = io.StringIO()
                with redirect_stderr(stderr):
                    outcome = compare_catalogs(self.ubuntu, self.windows)
                self.assertEqual(outcome, 2)
                self.assertIn("Unable to compare Component catalogs", stderr.getvalue())

    def test_missing_artifact_is_rejected(self) -> None:
        self.ubuntu.write_text(json.dumps(catalog()), encoding="utf-8")
        self.assertEqual(compare_catalogs(self.ubuntu, self.windows), 2)


if __name__ == "__main__":
    unittest.main()
