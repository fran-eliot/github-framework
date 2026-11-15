"""End-to-end CLI coverage for a relocated, three-family Component library.

Copies one real tracked Component per family into an isolated temporary root.
This is not a consumer application or an Existing Repository Adoption test.
"""

import json
import shutil
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[2]
FAMILIES = ("readme", "documentation", "workflow")
SOURCE_LIBRARY = ROOT / "framework" / "components"


class RelocatedComponentLibraryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.library = Path(self.temp.name) / "external-library" / "components"
        self.library.mkdir(parents=True)
        self.paths = []
        self.source_checks = {}

        for family in FAMILIES:
            candidates = sorted(
                path for path in (SOURCE_LIBRARY / family).iterdir()
                if path.is_dir() and (path / "metadata.yml").is_file()
            )
            self.assertTrue(candidates, f"No tracked Component in {family}")
            source = candidates[0]
            target = self.library / family / source.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, target)
            self.paths.append(f"{family}/{source.name}")
            self.source_checks[source / "metadata.yml"] = (
                source / "metadata.yml"
            ).read_bytes()

    def run_cli(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(self.library), *args,
            ],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )

    def test_relocated_three_family_catalog_and_full_validation(self) -> None:
        listing = self.run_cli(
            "--list-components", "--format", "json", "--details",
            "--catalog-metadata-sha256", "--catalog-content-sha256",
        )
        self.assertEqual(listing.returncode, 0, listing.stderr)
        catalog = json.loads(listing.stdout)
        self.assertEqual(catalog["components"], sorted(self.paths))
        self.assertEqual(catalog["count"], 3)
        self.assertEqual(
            [detail["path"] for detail in catalog["details"]],
            sorted(self.paths),
        )
        for detail in catalog["details"]:
            self.assertEqual(len(detail["metadata_sha256"]), 64)
            self.assertEqual(len(detail["content_sha256"]), 64)

        full = self.run_cli("--format", "json")
        self.assertEqual(full.returncode, 0, full.stderr)
        report = json.loads(full.stdout)
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["components_discovered"], 3)
        self.assertEqual(
            {item["relative_path"] for item in report["components"]},
            set(self.paths),
        )

    def test_saved_selection_verifies_only_selected_family(self) -> None:
        selection = Path(self.temp.name) / "selected.json"
        export = self.run_cli(
            "--list-components", "--format", "json",
            "--family", "workflow", "--details",
            "--catalog-metadata-sha256", "--catalog-content-sha256",
            "--output", str(selection),
        )
        self.assertEqual(export.returncode, 0, export.stderr)
        self.assertEqual(export.stdout, "")
        catalog = json.loads(selection.read_text(encoding="utf-8"))
        self.assertEqual(catalog["components"], [self.paths[2]])

        targeted = self.run_cli(
            "--catalog-input", str(selection), "--catalog-verify-details",
            "--catalog-verify-sha256", "--catalog-verify-content-sha256",
            "--format", "json",
        )
        self.assertEqual(targeted.returncode, 0, targeted.stderr)
        report = json.loads(targeted.stdout)
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["components_discovered"], 1)
        self.assertEqual(report["scope"]["component_paths"], [self.paths[2]])
        self.assertTrue(report["scope"]["filtered"])
        self.assertEqual(
            [item["relative_path"] for item in report["components"]],
            [self.paths[2]],
        )
        for source, before in self.source_checks.items():
            self.assertEqual(source.read_bytes(), before)

    def test_verified_selection_ignores_unselected_changes_and_rejects_selected(self) -> None:
        selection = Path(self.temp.name) / "workflow-selection.json"
        exported = self.run_cli(
            "--list-components", "--format", "json", "--family", "workflow",
            "--details", "--catalog-metadata-sha256",
            "--catalog-content-sha256", "--output", str(selection),
        )
        self.assertEqual(exported.returncode, 0, exported.stderr)
        saved = selection.read_bytes()

        verify_args = (
            "--catalog-input", str(selection), "--catalog-verify-details",
            "--catalog-verify-sha256", "--catalog-verify-content-sha256",
            "--format", "json",
        )
        baseline = self.run_cli(*verify_args)
        self.assertEqual(baseline.returncode, 0, baseline.stderr)

        # A README-family change must not invalidate a Workflow-only selection.
        unrelated = self.library / self.paths[0] / "scope-probe.txt"
        unrelated.write_bytes(b"independent change\n")
        unchanged = self.run_cli(*verify_args)
        self.assertEqual(unchanged.returncode, 0, unchanged.stderr)
        self.assertEqual(
            json.loads(unchanged.stdout)["scope"]["component_paths"],
            [self.paths[2]],
        )

        # Changing a selected Component must reject the saved content snapshot.
        selected = self.library / self.paths[2] / "scope-probe.txt"
        selected.write_bytes(b"stale selected content\n")
        stale = self.run_cli(*verify_args)
        self.assertEqual(stale.returncode, 2)
        self.assertEqual(stale.stdout, "")
        self.assertIn(
            "--catalog-verify-content-sha256 stale Component content",
            stale.stderr,
        )
        self.assertEqual(selection.read_bytes(), saved)
        for source, before in self.source_checks.items():
            self.assertEqual(source.read_bytes(), before)



if __name__ == "__main__":
    unittest.main()
