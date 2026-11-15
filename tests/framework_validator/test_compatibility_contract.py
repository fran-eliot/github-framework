"""Compatibility contracts for the public Validator CLI/JSON workflows.

These isolated subprocess tests protect consumer-facing defaults without
requiring a golden snapshot of absolute paths or operating-system details.
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]

METADATA = """\
schema_version: "1.0"
id: DOC-ARCHITECTURE
name: Architecture
family: Documentation
version: "0.1.0"
status: Experimental
priority: Recommended
description: Architecture documentation Component.
"""


class ValidatorCompatibilityContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "components"
        self.component = self.root / "documentation" / "architecture"
        self.component.mkdir(parents=True)
        (self.component / "metadata.yml").write_text(METADATA, encoding="utf-8")

    def invoke(self, *options: str, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(self.root), *options,
            ],
            cwd=REPOSITORY_ROOT, input=input_text, capture_output=True,
            text=True, check=False,
        )

    def test_default_catalog_json_preserves_minimal_shape(self) -> None:
        result = self.invoke("--list-components", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        catalog = json.loads(result.stdout)
        self.assertEqual(set(catalog), {"components", "count", "scope"})
        self.assertEqual(catalog["components"], ["documentation/architecture"])
        self.assertEqual(catalog["count"], 1)
        self.assertEqual(
            catalog["scope"]["families"],
            ["readme", "documentation", "workflow"],
        )
        self.assertNotIn("details", catalog)
        self.assertNotIn("pagination", catalog)

    def test_optional_catalog_fields_do_not_change_default_contract(self) -> None:
        original = json.loads(self.invoke("--list-components", "--format", "json").stdout)
        expanded = self.invoke(
            "--list-components", "--format", "json", "--details",
            "--catalog-metadata-sha256", "--catalog-content-sha256",
            "--family-summary", "--metadata-summary",
        )
        self.assertEqual(expanded.returncode, 0, expanded.stderr)
        catalog = json.loads(expanded.stdout)
        self.assertEqual(catalog["components"], original["components"])
        self.assertEqual(catalog["count"], original["count"])
        self.assertEqual(catalog["scope"], original["scope"])
        self.assertEqual(len(catalog["details"]), 1)
        for field in ("path", "id", "name", "version", "status", "metadata_status"):
            self.assertIn(field, catalog["details"][0])
        for field in ("metadata_sha256", "content_sha256"):
            self.assertRegex(catalog["details"][0][field], r"^[a-f0-9]{64}$")
        self.assertIn("family_summary", catalog)
        self.assertIn("metadata_summary", catalog)
        repeat = json.loads(self.invoke("--list-components", "--format", "json").stdout)
        self.assertEqual(repeat, original)

    def test_plain_and_imported_targeted_validation_keep_result_schema(self) -> None:
        unfiltered = self.invoke("--format", "json")
        selected = self.invoke("--format", "json", "--component", "documentation/architecture")
        self.assertEqual(unfiltered.returncode, 0, unfiltered.stderr)
        self.assertEqual(selected.returncode, 0, selected.stderr)
        a, b = json.loads(unfiltered.stdout), json.loads(selected.stdout)
        expected = {
            "status", "components_discovered", "component_ids",
            "errors", "components", "scope", "summary",
        }
        self.assertEqual(set(a), expected)
        self.assertEqual(set(b), expected)
        self.assertEqual(a["status"], "passed")
        self.assertEqual(b["status"], "passed")
        self.assertEqual(a["components_discovered"], 1)
        self.assertEqual(b["components_discovered"], 1)
        self.assertFalse(a["scope"]["filtered"])
        self.assertTrue(b["scope"]["filtered"])
        self.assertEqual(
            b["scope"]["component_paths"], ["documentation/architecture"],
        )
        for result in (a, b):
            self.assertEqual(result["summary"]["failed_components"], 0)
            self.assertEqual(result["summary"]["error_count"], 0)
            self.assertEqual(
                result["components"][0]["relative_path"], "documentation/architecture",
            )
        catalog = self.invoke("--list-components", "--format", "json")
        imported = self.invoke(
            "--catalog-input", "-", "--format", "json", input_text=catalog.stdout,
        )
        self.assertEqual(imported.returncode, 0, imported.stderr)
        self.assertEqual(json.loads(imported.stdout), b)

    def test_export_and_stale_preflight_preserve_existing_output(self) -> None:
        destination = Path(self.temp.name) / "catalog.json"
        export = self.invoke(
            "--list-components", "--format", "json", "--details",
            "--catalog-metadata-sha256", "--catalog-content-sha256",
            "--output", str(destination),
        )
        self.assertEqual(export.returncode, 0, export.stderr)
        self.assertEqual(export.stdout, "")
        saved_bytes = destination.read_bytes()
        self.assertTrue(saved_bytes.endswith(b"\n"))
        check = self.invoke(
            "--catalog-input", str(destination),
            "--catalog-verify-details", "--catalog-verify-sha256",
            "--catalog-verify-content-sha256", "--format", "json",
        )
        self.assertEqual(check.returncode, 0, check.stderr)
        (self.component / "README.md").write_text("New file", encoding="utf-8")
        stale = self.invoke(
            "--catalog-input", str(destination),
            "--catalog-verify-content-sha256", "--format", "json",
        )
        self.assertEqual(stale.returncode, 2)
        self.assertEqual(stale.stdout, "")
        self.assertIn("stale Component content", stale.stderr)
        self.assertEqual(destination.read_bytes(), saved_bytes)
        no_match = self.invoke(
            "--list-components", "--format", "json",
            "--match", "workflow/*", "--output", str(destination),
        )
        self.assertEqual(no_match.returncode, 1)
        self.assertEqual(no_match.stdout, "")
        self.assertEqual(destination.read_bytes(), saved_bytes)


    def test_failed_validation_keeps_json_schema_and_component_diagnostics(self) -> None:
        metadata = self.component / "metadata.yml"
        metadata.write_text(
            METADATA.replace("status: Experimental", "status: Unknown"),
            encoding="utf-8",
        )
        result = self.invoke("--format", "json")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertEqual(result.stderr, "")
        report = json.loads(result.stdout)
        self.assertEqual(set(report), {
            "status", "components_discovered", "component_ids",
            "errors", "components", "scope", "summary",
        })
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["components_discovered"], 1)
        self.assertGreater(report["summary"]["error_count"], 0)
        self.assertEqual(report["summary"]["failed_components"], 1)
        self.assertEqual(report["summary"]["passed_components"], 0)
        self.assertEqual(report["components"][0]["status"], "failed")
        self.assertEqual(
            report["components"][0]["relative_path"], "documentation/architecture",
        )
        self.assertTrue(report["components"][0]["errors"])
        self.assertEqual(report["summary"]["error_count"], len(report["errors"]))

    def test_json_export_matches_stdout_for_catalog_and_successful_validation(self) -> None:
        destination = Path(self.temp.name) / "output.json"
        scenarios = (
            ("--list-components", "--format", "json", "--details"),
            ("--format", "json"),
        )
        for options in scenarios:
            with self.subTest(options=options):
                stdout = self.invoke(*options)
                exported = self.invoke(*options, "--output", str(destination))
                self.assertEqual(stdout.returncode, 0, stdout.stderr)
                self.assertEqual(exported.returncode, stdout.returncode, exported.stderr)
                self.assertEqual(exported.stdout, "")
                self.assertEqual(json.loads(destination.read_text(encoding="utf-8")),
                                 json.loads(stdout.stdout))
                self.assertTrue(destination.read_bytes().endswith(b"\n"))

    def test_failed_validation_still_exports_json_report_with_failure_code(self) -> None:
        (self.component / "metadata.yml").write_text(
            METADATA.replace("status: Experimental", "status: Unknown"),
            encoding="utf-8",
        )
        destination = Path(self.temp.name) / "failed-report.json"
        stdout = self.invoke("--format", "json")
        exported = self.invoke("--format", "json", "--output", str(destination))
        self.assertEqual(stdout.returncode, 1)
        self.assertEqual(exported.returncode, 1)
        self.assertEqual(exported.stdout, "")
        self.assertEqual(json.loads(destination.read_text(encoding="utf-8")),
                         json.loads(stdout.stdout))
        self.assertEqual(json.loads(stdout.stdout)["status"], "failed")

    def test_invalid_arguments_do_not_overwrite_existing_json(self) -> None:
        destination = Path(self.temp.name) / "existing.json"
        destination.write_text("previous contents", encoding="utf-8")
        result = self.invoke(
            "--list-components", "--details", "--format", "json",
            "--output", str(destination),
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        previous = destination.read_bytes()
        invalid = self.invoke(
            "--list-components", "--format", "json",
            "--catalog-verify-sha256", "--output", str(destination),
        )
        self.assertEqual(invalid.returncode, 2)
        self.assertEqual(invalid.stdout, "")
        self.assertEqual(destination.read_bytes(), previous)


if __name__ == "__main__":
    unittest.main()
