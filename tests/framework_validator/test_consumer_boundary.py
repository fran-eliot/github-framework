"""Prove that Framework Component validation is not generic application validation.

An isolated fixture models an application repository with ordinary Python
files and no Framework Component family directories. It is not a consumer
Assessment and does not execute or modify the external example repository.
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


FRAMEWORK_ROOT = Path(__file__).resolve().parents[2]
VALID_COMPONENT = """\
schema_version: "1.0"
id: DOC-ARCHITECTURE
name: Architecture
family: Documentation
version: "0.1.0"
status: Experimental
priority: Recommended
description: Architecture documentation Component.
"""


class ConsumerBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.application = Path(self.temp.name) / "application"
        (self.application / "app").mkdir(parents=True)
        (self.application / "tests").mkdir()
        (self.application / "pyproject.toml").write_text(
            '[project]\nname = "example-application"\nrequires-python = ">=3.13"\n',
            encoding="utf-8",
        )
        (self.application / "README.md").write_text(
            "# Example Application\n", encoding="utf-8"
        )
        (self.application / "app" / "main.py").write_text(
            "from __future__ import annotations\n", encoding="utf-8"
        )

    def run_cli(self, root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), *args,
            ],
            cwd=FRAMEWORK_ROOT,
            capture_output=True, text=True, check=False,
        )

    def test_generic_application_is_not_reported_as_validated(self) -> None:
        before = {
            path.relative_to(self.application).as_posix(): path.read_bytes()
            for path in self.application.rglob("*") if path.is_file()
        }
        result = self.run_cli(self.application, "--format", "json")
        self.assertEqual(result.returncode, 1, result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["components_discovered"], 0)
        self.assertGreater(report["summary"]["error_count"], 0)
        self.assertTrue(any("no Components discovered" in error for error in report["errors"]))
        after = {
            path.relative_to(self.application).as_posix(): path.read_bytes()
            for path in self.application.rglob("*") if path.is_file()
        }
        self.assertEqual(after, before)

    def test_application_files_are_not_listed_as_framework_components(self) -> None:
        result = self.run_cli(
            self.application, "--list-components", "--format", "json"
        )
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")

    def test_explicit_component_library_is_a_separate_validation_scope(self) -> None:
        library = self.application / "framework" / "components"
        component = library / "documentation" / "architecture"
        component.mkdir(parents=True)
        (component / "metadata.yml").write_text(VALID_COMPONENT, encoding="utf-8")

        root_result = self.run_cli(self.application, "--format", "json")
        self.assertEqual(root_result.returncode, 1)
        self.assertEqual(json.loads(root_result.stdout)["components_discovered"], 0)

        catalog_result = self.run_cli(
            library, "--list-components", "--format", "json"
        )
        self.assertEqual(catalog_result.returncode, 0, catalog_result.stderr)
        catalog = json.loads(catalog_result.stdout)
        self.assertEqual(catalog["components"], ["documentation/architecture"])

        validation_result = self.run_cli(library, "--format", "json")
        self.assertEqual(validation_result.returncode, 0, validation_result.stderr)
        validated = json.loads(validation_result.stdout)
        self.assertEqual(validated["status"], "passed")
        self.assertEqual(validated["components_discovered"], 1)
        self.assertEqual(
            validated["components"][0]["relative_path"], "documentation/architecture"
        )


if __name__ == "__main__":
    unittest.main()
