
"""Integration tests for the Framework Validator CLI."""

import io
import json
import subprocess
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts.framework_validator import __main__ as validator_cli


VALID_METADATA = """\
schema_version: "1.0"
id: DOC-ARCHITECTURE
name: Architecture
family: Documentation
version: "0.1.0"
status: Experimental
priority: Recommended
description: Architecture documentation Component.
"""

VALID_WORKFLOW_METADATA = """\
schema_version: "1.0"
id: WCL-ISSUE
name: Issue
family: Workflow
version: "0.1.0"
status: Experimental
priority: Required
description: Issue Workflow Component.
materialization:
  primary:
    - Community File
  executable: false
artifacts:
  specification: README.md
  templates:
    - templates/bug_report.yml
adoption:
  target: .github/ISSUE_TEMPLATE/
  specialization: Allowed
validation:
  dogfooding: true
  reference_implementation: Validated
"""

class FrameworkValidatorCLITests(unittest.TestCase):
    """Exercise main() against isolated Component directories."""

    def run_validator(self, root: Path) -> tuple[int, str]:
        output = io.StringIO()

        with (
            patch.object(validator_cli, "COMPONENTS_ROOT", root),
            redirect_stdout(output),
        ):
            exit_code = validator_cli.main()

        return exit_code, output.getvalue()

    def run_validator_json(self, root: Path) -> tuple[int, dict]:
        output = io.StringIO()

        with (
            patch.object(validator_cli, "COMPONENTS_ROOT", root),
            redirect_stdout(output),
        ):
            exit_code = validator_cli.main(output_format="json")

        return exit_code, json.loads(output.getvalue())

    def create_component(self, root: Path) -> Path:
        component = root / "documentation" / "architecture"
        component.mkdir(parents=True)
        return component

    def test_valid_component(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 0)
            self.assertIn("Components discovered: 1", output)
            self.assertIn("Validation passed:", output)

    def test_empty_components_root(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("Components discovered: 0", output)
            self.assertIn("no Components discovered", output)
            self.assertIn("Validation failed:", output)

    def test_missing_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_component(root)

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("missing metadata.yml", output)
            self.assertIn("Validation failed:", output)

    def test_invalid_yaml(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                "family: [unclosed", encoding="utf-8"
            )

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("unable to load metadata:", output)
            self.assertIn("metadata.yml", output)

    def test_invalid_common_core(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA.replace(
                    "status: Experimental",
                    "status: Unknown",
                ),
                encoding="utf-8",
            )

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("metadata.yml", output)
            self.assertIn("status:", output)
            self.assertIn("Validation failed:", output)

    def test_missing_workflow_artifact(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = root / "workflow" / "issue"
            component.mkdir(parents=True)

            (component / "metadata.yml").write_text(
                VALID_WORKFLOW_METADATA,
                encoding="utf-8",
            )
            (component / "README.md").write_text(
                "# Issue\n",
                encoding="utf-8",
            )

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("WCL-ISSUE", output)
            self.assertIn("artifacts.templates[0]", output)
            self.assertIn("file does not exist", output)
            self.assertIn("Validation failed:", output)

    def test_duplicate_component_id(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)

            first_component = root / "documentation" / "architecture"
            first_component.mkdir(parents=True)
            (first_component / "metadata.yml").write_text(
                VALID_METADATA,
                encoding="utf-8",
            )

            second_component = root / "documentation" / "references"
            second_component.mkdir(parents=True)
            (second_component / "metadata.yml").write_text(
                VALID_METADATA,
                encoding="utf-8",
            )

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("Components discovered: 2", output)
            self.assertIn("duplicate 'DOC-ARCHITECTURE'", output)
            self.assertIn("first declared in", output)
            self.assertIn("Validation failed:", output)
    def test_json_output_valid_component(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )

            exit_code, result = self.run_validator_json(root)

            self.assertEqual(exit_code, 0)
            self.assertEqual(result["status"], "passed")
            self.assertEqual(result["components_discovered"], 1)
            self.assertEqual(result["component_ids"], ["DOC-ARCHITECTURE"])
            self.assertEqual(result["scope"], {
                "families": ["readme", "documentation", "workflow"],
                "filtered": False,
            })
            self.assertEqual(result["errors"], [])
            self.assertEqual(result["summary"], {
                "passed_components": 1,
                "failed_components": 0,
                "error_count": 0,
            })
            self.assertEqual(len(result["components"]), 1)
            self.assertEqual(result["components"][0]["id"], "DOC-ARCHITECTURE")
            self.assertEqual(
                result["components"][0]["relative_path"],
                "documentation/architecture",
            )
            self.assertEqual(result["components"][0]["status"], "passed")
            self.assertEqual(result["components"][0]["errors"], [])
            self.assertTrue(result["components"][0]["path"].endswith("architecture"))

    def test_json_output_missing_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_component(root)

            exit_code, result = self.run_validator_json(root)

            self.assertEqual(exit_code, 1)
            self.assertEqual(result["status"], "failed")
            self.assertEqual(result["components_discovered"], 1)
            self.assertEqual(result["component_ids"], [])
            self.assertEqual(len(result["errors"]), 1)
            self.assertIn("missing metadata.yml", result["errors"][0])
            self.assertEqual(result["summary"], {
                "passed_components": 0,
                "failed_components": 1,
                "error_count": 1,
            })
            self.assertEqual(len(result["components"]), 1)
            self.assertIsNone(result["components"][0]["id"])
            self.assertEqual(
                result["components"][0]["relative_path"],
                "documentation/architecture",
            )
            self.assertEqual(result["components"][0]["status"], "failed")
            self.assertEqual(result["components"][0]["errors"], result["errors"])

    def test_json_output_empty_components_root(self) -> None:
        with TemporaryDirectory() as directory:
            exit_code, result = self.run_validator_json(Path(directory))

            self.assertEqual(exit_code, 1)
            self.assertEqual(result["status"], "failed")
            self.assertEqual(result["components_discovered"], 0)
            self.assertEqual(result["component_ids"], [])
            self.assertEqual(result["components"], [])
            self.assertEqual(result["summary"], {
                "passed_components": 0,
                "failed_components": 0,
                "error_count": 1,
            })
            self.assertTrue(
                any("no Components discovered" in error for error in result["errors"])
            )

    def test_json_output_invalid_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA.replace("status: Experimental", "status: Unknown"),
                encoding="utf-8",
            )

            exit_code, result = self.run_validator_json(root)

            self.assertEqual(exit_code, 1)
            self.assertEqual(result["status"], "failed")
            self.assertEqual(result["component_ids"], ["DOC-ARCHITECTURE"])
            self.assertEqual(len(result["components"]), 1)
            self.assertEqual(result["components"][0]["status"], "failed")
            self.assertTrue(
                any("status:" in error for error in result["components"][0]["errors"])
            )

    def test_json_output_duplicate_component_id(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("architecture", "references"):
                component = root / "documentation" / name
                component.mkdir(parents=True)
                (component / "metadata.yml").write_text(
                    VALID_METADATA, encoding="utf-8"
                )

            exit_code, result = self.run_validator_json(root)

            self.assertEqual(exit_code, 1)
            self.assertEqual(result["status"], "failed")
            self.assertEqual(result["components_discovered"], 2)
            self.assertEqual(len(result["components"]), 2)
            self.assertTrue(
                all(component["status"] == "failed" for component in result["components"])
            )
            self.assertTrue(
                all(
                    any("id: duplicate" in error for error in component["errors"])
                    for component in result["components"]
                )
            )
            self.assertEqual(len(result["errors"]), 1)
            self.assertEqual(result["summary"], {
                "passed_components": 0,
                "failed_components": 2,
                "error_count": 1,
            })

    def test_json_output_mixed_valid_and_missing_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            valid_component = self.create_component(root)
            (valid_component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            missing_component = root / "documentation" / "references"
            missing_component.mkdir(parents=True)

            exit_code, result = self.run_validator_json(root)

            self.assertEqual(exit_code, 1)
            self.assertEqual(result["components_discovered"], 2)
            self.assertEqual(result["component_ids"], ["DOC-ARCHITECTURE"])
            self.assertEqual(len(result["errors"]), 1)
            components = {
                Path(component["path"]).name: component
                for component in result["components"]
            }
            self.assertEqual(components["architecture"]["status"], "passed")
            self.assertEqual(components["architecture"]["errors"], [])
            self.assertEqual(components["references"]["status"], "failed")
            self.assertEqual(
                components["references"]["relative_path"],
                "documentation/references",
            )
            self.assertIsNone(components["references"]["id"])
            self.assertEqual(components["references"]["errors"], result["errors"])
            self.assertEqual(result["summary"], {
                "passed_components": 1,
                "failed_components": 1,
                "error_count": 1,
            })

    def test_json_report_file_on_success(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            destination = root / "report.json"
            stdout = io.StringIO()

            with (
                patch.object(validator_cli, "COMPONENTS_ROOT", root),
                redirect_stdout(stdout),
            ):
                exit_code = validator_cli.main(
                    output_format="json", output_path=destination
                )

            self.assertEqual(exit_code, 0)
            self.assertEqual(stdout.getvalue(), "")
            result = json.loads(destination.read_text(encoding="utf-8"))
            self.assertEqual(result["status"], "passed")
            self.assertEqual(result["component_ids"], ["DOC-ARCHITECTURE"])
            self.assertEqual(result["errors"], [])

    def test_json_report_file_on_validation_failure(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_component(root)
            destination = root / "report.json"
            stdout = io.StringIO()

            with (
                patch.object(validator_cli, "COMPONENTS_ROOT", root),
                redirect_stdout(stdout),
            ):
                exit_code = validator_cli.main(
                    output_format="json", output_path=destination
                )

            self.assertEqual(exit_code, 1)
            self.assertEqual(stdout.getvalue(), "")
            result = json.loads(destination.read_text(encoding="utf-8"))
            self.assertEqual(result["status"], "failed")
            self.assertIn("missing metadata.yml", result["errors"][0])
            self.assertEqual(result["components"][0]["status"], "failed")

    def test_json_report_file_write_failure(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            stdout = io.StringIO()
            stderr = io.StringIO()

            with (
                patch.object(validator_cli, "COMPONENTS_ROOT", root),
                redirect_stdout(stdout),
                redirect_stderr(stderr),
            ):
                exit_code = validator_cli.main(
                    output_format="json", output_path=root
                )

            self.assertEqual(exit_code, 2)
            self.assertEqual(stdout.getvalue(), "")
            self.assertIn("Unable to write JSON report", stderr.getvalue())

    def test_json_report_replaces_existing_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            destination = root / "report.json"
            destination.write_text("previous report", encoding="utf-8")

            with patch.object(validator_cli, "COMPONENTS_ROOT", root):
                exit_code = validator_cli.main(
                    output_format="json", output_path=destination
                )

            self.assertEqual(exit_code, 0)
            report = json.loads(destination.read_text(encoding="utf-8"))
            self.assertEqual(report["status"], "passed")
            self.assertEqual(list(root.glob(".report.json.*.tmp")), [])

    def test_json_report_replace_failure_preserves_existing_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            destination = root / "report.json"
            previous_report = '{"status": "previous"}\n'
            destination.write_text(previous_report, encoding="utf-8")
            stdout = io.StringIO()
            stderr = io.StringIO()

            with (
                patch.object(validator_cli, "COMPONENTS_ROOT", root),
                patch.object(
                    validator_cli.os,
                    "replace",
                    side_effect=OSError("simulated replace failure"),
                ),
                redirect_stdout(stdout),
                redirect_stderr(stderr),
            ):
                exit_code = validator_cli.main(
                    output_format="json", output_path=destination
                )

            self.assertEqual(exit_code, 2)
            self.assertEqual(stdout.getvalue(), "")
            self.assertIn("Unable to write JSON report", stderr.getvalue())
            self.assertEqual(destination.read_text(encoding="utf-8"), previous_report)
            self.assertEqual(list(root.glob(".report.json.*.tmp")), [])

    def test_json_relative_paths_across_component_families(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            doc_component = self.create_component(root)
            (doc_component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            workflow_component = root / "workflow" / "issue"
            workflow_component.mkdir(parents=True)
            (workflow_component / "metadata.yml").write_text(
                VALID_WORKFLOW_METADATA, encoding="utf-8"
            )
            (workflow_component / "README.md").write_text(
                "# Issue\n", encoding="utf-8"
            )

            exit_code, result = self.run_validator_json(root)

            self.assertEqual(exit_code, 1)
            self.assertEqual(
                {component["relative_path"] for component in result["components"]},
                {"documentation/architecture", "workflow/issue"},
            )
            self.assertTrue(
                all(
                    component["path"] == str(root / component["relative_path"])
                    for component in result["components"]
                )
            )

    def test_explicit_components_root_json(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory) / "custom-components"
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            output = io.StringIO()

            with redirect_stdout(output):
                exit_code = validator_cli.main(
                    output_format="json", components_root=root
                )

            result = json.loads(output.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(result["components_discovered"], 1)
            self.assertEqual(result["components"][0]["relative_path"], "documentation/architecture")
            self.assertEqual(result["components"][0]["path"], str(component))

    def test_explicit_components_root_text_with_missing_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory) / "custom-components"
            self.create_component(root)
            output = io.StringIO()

            with redirect_stdout(output):
                exit_code = validator_cli.main(components_root=root)

            self.assertEqual(exit_code, 1)
            self.assertIn(str(root), output.getvalue())
            self.assertIn("missing metadata.yml", output.getvalue())

    def test_cli_components_root_argument_and_invalid_path(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory) / "custom-components"
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            command = [
                sys.executable, "-m", "scripts.framework_validator",
                "--format", "json", "--components-root", str(root),
            ]
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                cwd=validator_cli.REPOSITORY_ROOT,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["components_discovered"], 1)

            invalid = subprocess.run(
                command[:-1] + [str(root / "missing")],
                capture_output=True,
                text=True,
                check=False,
                cwd=validator_cli.REPOSITORY_ROOT,
            )
            self.assertEqual(invalid.returncode, 2)
            self.assertIn("--components-root must be an existing directory", invalid.stderr)

    def test_json_filter_one_component_family(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            documentation = self.create_component(root)
            (documentation / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            workflow = root / "workflow" / "issue"
            workflow.mkdir(parents=True)
            (workflow / "metadata.yml").write_text(
                VALID_WORKFLOW_METADATA, encoding="utf-8"
            )
            output = io.StringIO()
            with redirect_stdout(output):
                exit_code = validator_cli.main(
                    output_format="json",
                    components_root=root,
                    families=("documentation",),
                )

            result = json.loads(output.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(result["components_discovered"], 1)
            self.assertEqual(
                result["components"][0]["relative_path"], "documentation/architecture"
            )
            self.assertEqual(result["summary"]["passed_components"], 1)
            self.assertEqual(result["scope"], {
                "families": ["documentation"],
                "filtered": True,
            })

    def test_json_filter_multiple_component_families(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            documentation = self.create_component(root)
            (documentation / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            workflow = root / "workflow" / "issue"
            workflow.mkdir(parents=True)
            (workflow / "metadata.yml").write_text(
                VALID_WORKFLOW_METADATA, encoding="utf-8"
            )
            output = io.StringIO()
            with redirect_stdout(output):
                exit_code = validator_cli.main(
                    output_format="json",
                    components_root=root,
                    families=("documentation", "workflow"),
                )

            result = json.loads(output.getvalue())
            self.assertEqual(exit_code, 1)
            self.assertEqual(result["components_discovered"], 2)
            self.assertEqual(
                {item["relative_path"] for item in result["components"]},
                {"documentation/architecture", "workflow/issue"},
            )

    def test_family_filter_scopes_duplicate_ids(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            documentation = self.create_component(root)
            (documentation / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            readme = root / "readme" / "architecture"
            readme.mkdir(parents=True)
            (readme / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            output = io.StringIO()
            with redirect_stdout(output):
                exit_code = validator_cli.main(
                    output_format="json",
                    components_root=root,
                    families=("documentation",),
                )

            result = json.loads(output.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(result["summary"]["error_count"], 0)
            self.assertEqual(result["components_discovered"], 1)
            self.assertEqual(result["scope"]["filtered"], True)

    def test_cli_family_argument_rejects_unknown_family(self) -> None:
        result = subprocess.run(
            [
                sys.executable, "-m", "scripts.framework_validator",
                "--family", "unknown",
            ],
            capture_output=True,
            text=True,
            check=False,
            cwd=validator_cli.REPOSITORY_ROOT,
        )

        self.assertEqual(result.returncode, 2)
        self.assertIn("invalid choice", result.stderr)

    def test_cli_repeated_family_filter(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            documentation = self.create_component(root)
            (documentation / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            command = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root),
                "--format", "json",
                "--family", "documentation",
                "--family", "documentation",
            ]
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                cwd=validator_cli.REPOSITORY_ROOT,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["components_discovered"], 1)

    def test_json_explicit_all_families_is_unfiltered(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            output = io.StringIO()
            with redirect_stdout(output):
                exit_code = validator_cli.main(
                    output_format="json",
                    components_root=root,
                    families=("workflow", "documentation", "readme"),
                )

            result = json.loads(output.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(result["scope"], {
                "families": ["readme", "documentation", "workflow"],
                "filtered": False,
            })

    def test_json_scope_repeated_family_appears_once(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            command = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root),
                "--format", "json",
                "--family", "documentation",
                "--family", "documentation",
            ]
            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                check=False,
                cwd=validator_cli.REPOSITORY_ROOT,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["scope"], {
                "families": ["documentation"],
                "filtered": True,
            })
