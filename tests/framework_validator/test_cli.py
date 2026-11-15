
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
            self.assertEqual(len(result["errors"]), 2)
            self.assertTrue(
                any("id: expected" in error for error in result["errors"])
            )
            self.assertTrue(
                any("id: duplicate" in error for error in result["errors"])
            )
            self.assertEqual(result["summary"], {
                "passed_components": 0,
                "failed_components": 2,
                "error_count": 2,
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

    def test_component_filter_selects_only_requested_directory(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            documentation = self.create_component(root)
            (documentation / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            other = root / "documentation" / "references"
            other.mkdir(parents=True)
            output = io.StringIO()
            with redirect_stdout(output):
                exit_code = validator_cli.main(
                    output_format="json",
                    components_root=root,
                    component_paths=("documentation/architecture",),
                )
            result = json.loads(output.getvalue())
            self.assertEqual(exit_code, 0)
            self.assertEqual(result["components_discovered"], 1)
            self.assertEqual(
                result["components"][0]["relative_path"], "documentation/architecture"
            )
            self.assertEqual(result["scope"], {
                "families": ["documentation"],
                "filtered": True,
                "component_paths": ["documentation/architecture"],
            })

    def test_component_filter_detects_missing_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            missing = root / "documentation" / "references"
            missing.mkdir(parents=True)
            output = io.StringIO()
            with redirect_stdout(output):
                exit_code = validator_cli.main(
                    output_format="json",
                    components_root=root,
                    component_paths=("documentation/references",),
                )
            result = json.loads(output.getvalue())
            self.assertEqual(exit_code, 1)
            self.assertEqual(result["components_discovered"], 1)
            self.assertEqual(result["components"][0]["status"], "failed")
            self.assertTrue(any(
                "missing metadata.yml" in error
                for error in result["components"][0]["errors"]
            ))

    def test_cli_component_filter_repeated_and_cross_family(self) -> None:
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
            args = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--format", "json",
                "--component", "workflow/issue",
                "--component", "documentation/architecture",
                "--component", "workflow/issue",
            ]
            result = subprocess.run(
                args, cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 1)
            report = json.loads(result.stdout)
            self.assertEqual(report["components_discovered"], 2)
            self.assertEqual(report["scope"], {
                "families": ["documentation", "workflow"],
                "filtered": True,
                "component_paths": [
                    "documentation/architecture", "workflow/issue",
                ],
            })

    def test_cli_component_filter_rejects_invalid_or_missing_paths(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "documentation").mkdir()
            common = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root),
            ]
            for selection, message in (
                ("../outside", "must use FAMILY/NAME"),
                ("documentation/../outside", "must use FAMILY/NAME"),
                ("unknown/example", "must use FAMILY/NAME"),
                ("documentation/missing", "directory does not exist"),
            ):
                with self.subTest(selection=selection):
                    result = subprocess.run(
                        common + ["--component", selection],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(message, result.stderr)

            conflict = subprocess.run(
                common + [
                    "--component", "documentation/architecture",
                    "--family", "documentation",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(conflict.returncode, 2)
            self.assertIn("cannot be combined", conflict.stderr)

    def test_cli_list_components_without_loading_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for family, name in (
                ("workflow", "issue"),
                ("documentation", "architecture"),
                ("readme", "author"),
            ):
                (root / family / name).mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), [
                "documentation/architecture",
                "readme/author",
                "workflow/issue",
            ])

    def test_cli_list_components_with_family_filter(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "documentation" / "architecture").mkdir(parents=True)
            (root / "workflow" / "issue").mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root),
                    "--list-components", "--family", "workflow",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), ["workflow/issue"])

    def test_cli_list_components_empty_directory(self) -> None:
        with TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(Path(directory)), "--list-components",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("No Components discovered", result.stderr)

    def test_cli_list_components_rejects_incompatible_arguments(self) -> None:
        with TemporaryDirectory() as directory:
            common = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(Path(directory)),
                "--list-components",
            ]
            for options in (
                ["--component", "documentation/architecture"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        common + options,
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("--list-components", result.stderr)

    def test_cli_catalog_match_text_union_and_case_sensitive(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for family, name in (
                ("documentation", "architecture"),
                ("documentation", "references"),
                ("readme", "architecture"),
                ("workflow", "issue"),
            ):
                (root / family / name).mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--match", "documentation/a*",
                    "--match", "*/architecture",
                    "--match", "documentation/a*",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), [
                "documentation/architecture",
                "readme/architecture",
            ])
            case_result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--match", "Documentation/*",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(case_result.returncode, 1)
            self.assertEqual(case_result.stdout, "")
            self.assertIn("No Components match", case_result.stderr)

    def test_cli_catalog_match_json_family_details_and_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            (root / "workflow" / "issue").mkdir(parents=True)
            output = root / "matched.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--family", "documentation",
                    "--match", "documentation/a*", "--match", "*/architecture",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(catalog["count"], 1)
            self.assertEqual(catalog["components"], ["documentation/architecture"])
            self.assertEqual(catalog["scope"], {
                "families": ["documentation"],
                "match": ["documentation/a*", "*/architecture"],
            })
            self.assertEqual(catalog["details"][0]["id"], "DOC-ARCHITECTURE")
            self.assertEqual(catalog["details"][0]["metadata_status"], "loaded")

    def test_cli_catalog_match_no_results_does_not_replace_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "workflow" / "issue").mkdir(parents=True)
            output = root / "catalog.json"
            output.write_text("existing", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--match", "readme/*",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, "")
            self.assertIn("No Components match", result.stderr)
            self.assertEqual(output.read_text(encoding="utf-8"), "existing")

    def test_cli_catalog_match_rejected_without_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--match", "readme/*"],
                ["--format", "json", "--match", "readme/*"],
                ["--component", "readme/author", "--match", "readme/*"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("--match and --exclude require --list-components", result.stderr)


    def test_cli_catalog_exclude_text_and_case_sensitive(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for family, name in (
                ("documentation", "architecture"),
                ("documentation", "references"),
                ("readme", "architecture"),
                ("workflow", "issue"),
            ):
                (root / family / name).mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--exclude", "documentation/*",
                    "--exclude", "*/architecture",
                    "--exclude", "documentation/*",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), ["workflow/issue"])

            case_result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--exclude", "Documentation/*",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(case_result.returncode, 0, case_result.stderr)
            self.assertIn("documentation/architecture", case_result.stdout)

    def test_cli_catalog_exclude_json_match_family_details_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            (root / "workflow" / "issue").mkdir(parents=True)
            output = root / "filtered.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--family", "documentation",
                    "--match", "documentation/*", "--match", "*/architecture",
                    "--exclude", "*/references", "--exclude", "*/references",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], ["documentation/architecture"])
            self.assertEqual(catalog["count"], 1)
            self.assertEqual(catalog["scope"], {
                "families": ["documentation"],
                "match": ["documentation/*", "*/architecture"],
                "exclude": ["*/references"],
            })
            self.assertEqual(catalog["details"][0]["id"], "DOC-ARCHITECTURE")

    def test_cli_catalog_exclude_empty_result_preserves_output(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "workflow" / "issue").mkdir(parents=True)
            output = root / "catalog.json"
            output.write_text("previous", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--exclude", "workflow/*",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, "")
            self.assertIn("No Components match", result.stderr)
            self.assertEqual(output.read_text(encoding="utf-8"), "previous")

    def test_cli_catalog_exclude_requires_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--exclude", "readme/*"],
                ["--format", "json", "--exclude", "readme/*"],
                ["--component", "readme/author", "--exclude", "readme/*"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("require --list-components", result.stderr)


    def test_cli_catalog_sort_by_id_orders_metadata_and_missing_last(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            architecture = self.create_component(root)
            (architecture / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "Z-ARCH"),
                encoding="utf-8",
            )
            references = root / "documentation" / "references"
            references.mkdir(parents=True)
            (references / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "A-REF"),
                encoding="utf-8",
            )
            (root / "readme" / "author").mkdir(parents=True)
            command = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--list-components",
                "--sort-by", "id",
            ]
            result = subprocess.run(
                command,
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), [
                "documentation/references", "documentation/architecture",
                "readme/author",
            ])
            json_result = subprocess.run(
                command + ["--format", "json", "--details"],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(json_result.returncode, 0, json_result.stderr)
            catalog = json.loads(json_result.stdout)
            self.assertEqual(catalog["components"], result.stdout.splitlines())
            self.assertEqual(catalog["scope"]["sort_by"], "id")
            self.assertEqual(
                [item["id"] for item in catalog["details"]],
                ["A-REF", "Z-ARCH", None],
            )

    def test_cli_catalog_sort_by_version_with_filter_and_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            architecture = self.create_component(root)
            (architecture / "metadata.yml").write_text(
                VALID_METADATA.replace('version: "0.1.0"', 'version: "2.0.0"'),
                encoding="utf-8",
            )
            references = root / "documentation" / "references"
            references.mkdir(parents=True)
            (references / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "DOC-REFERENCES")
                .replace('version: "0.1.0"', 'version: "1.0.0"'),
                encoding="utf-8",
            )
            output = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--family", "documentation", "--format", "json",
                    "--sort-by", "version", "--details", "--family-summary",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], [
                "documentation/references", "documentation/architecture",
            ])
            self.assertEqual(catalog["scope"]["sort_by"], "version")
            self.assertEqual(catalog["family_summary"]["documentation"], 2)
            self.assertEqual(
                [item["version"] for item in catalog["details"]],
                ["1.0.0", "2.0.0"],
            )

    def test_cli_catalog_sort_by_path_preserves_default_order(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "workflow" / "issue").mkdir(parents=True)
            (root / "documentation" / "architecture").mkdir(parents=True)
            command = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--list-components", "--format", "json",
            ]
            implicit = subprocess.run(
                command, cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            explicit = subprocess.run(
                command + ["--sort-by", "path"], cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(implicit.returncode, 0, implicit.stderr)
            self.assertEqual(explicit.returncode, 0, explicit.stderr)
            default_catalog = json.loads(implicit.stdout)
            sorted_catalog = json.loads(explicit.stdout)
            self.assertNotIn("sort_by", default_catalog["scope"])
            self.assertEqual(sorted_catalog["scope"]["sort_by"], "path")
            self.assertEqual(
                default_catalog["components"], sorted_catalog["components"]
            )

    def test_cli_catalog_sort_by_requires_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options, expected in (
                (["--sort-by", "id"], "--sort-by requires --list-components"),
                (["--format", "json", "--sort-by", "version"],
                 "--sort-by requires --list-components"),
                (["--list-components", "--sort-by", "unknown"], "invalid choice"),
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(expected, result.stderr)

    def test_cli_catalog_metadata_version_filters_and_exports(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            stable = self.create_component(root)
            (stable / "metadata.yml").write_text(
                VALID_METADATA.replace('version: "0.1.0"', 'version: "1.2.0"'),
                encoding="utf-8",
            )
            preview = root / "documentation" / "references"
            preview.mkdir(parents=True)
            (preview / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "DOC-REFERENCES")
                .replace('version: "0.1.0"', 'version: "0.2.0"'),
                encoding="utf-8",
            )
            (root / "readme" / "author").mkdir(parents=True)
            destination = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--metadata-summary",
                    "--family-summary", "--family", "documentation",
                    "--metadata-version", "1.*", "--metadata-version", "0.2.*",
                    "--metadata-version", "1.*", "--output", str(destination),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(destination.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], [
                "documentation/architecture", "documentation/references",
            ])
            self.assertEqual(catalog["scope"]["metadata_version"], [
                "1.*", "0.2.*",
            ])
            self.assertEqual(
                [item["version"] for item in catalog["details"]],
                ["1.2.0", "0.2.0"],
            )
            self.assertEqual(catalog["family_summary"]["documentation"], 2)
            self.assertEqual(catalog["metadata_summary"]["loaded"], 2)

    def test_cli_catalog_metadata_version_text_and_empty_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            loaded = self.create_component(root)
            (loaded / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            missing = root / "documentation" / "references"
            missing.mkdir(parents=True)
            invalid = root / "readme" / "author"
            invalid.mkdir(parents=True)
            (invalid / "metadata.yml").write_text(
                "family: [bad", encoding="utf-8"
            )
            common = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--list-components",
            ]
            matched = subprocess.run(
                common + ["--metadata-version", "0.1.*"],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(matched.returncode, 0, matched.stderr)
            self.assertEqual(matched.stdout.splitlines(), [
                "documentation/architecture",
            ])
            destination = root / "catalog.json"
            destination.write_text("previous", encoding="utf-8")
            empty = subprocess.run(
                common + [
                    "--format", "json", "--metadata-version", "9.*",
                    "--output", str(destination),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(empty.returncode, 1)
            self.assertIn("No Components match", empty.stderr)
            self.assertEqual(empty.stdout, "")
            self.assertEqual(destination.read_text(encoding="utf-8"), "previous")

    def test_cli_catalog_metadata_version_requires_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--metadata-version", "0.*"],
                ["--format", "json", "--metadata-version", "0.*"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(
                        "--metadata-version requires --list-components",
                        result.stderr,
                    )

    def test_cli_catalog_descending_by_status_keeps_missing_last(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            cases = (
                ("documentation", "architecture", "Experimental"),
                ("documentation", "references", "Stable"),
                ("workflow", "issue", "Stable"),
            )
            for family, name, status in cases:
                component = root / family / name
                component.mkdir(parents=True)
                (component / "metadata.yml").write_text(
                    VALID_METADATA.replace("status: Experimental", f"status: {status}"),
                    encoding="utf-8",
                )
            (root / "readme" / "author").mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--sort-by", "status",
                    "--sort-order", "desc", "--component-status-summary",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["components"], [
                "documentation/references", "workflow/issue",
                "documentation/architecture", "readme/author",
            ])
            self.assertEqual(
                [entry["status"] for entry in catalog["details"]],
                ["Stable", "Stable", "Experimental", None],
            )
            self.assertEqual(catalog["scope"]["sort_order"], "desc")
            self.assertEqual(catalog["component_status_summary"], {
                "by_status": {"Experimental": 1, "Stable": 2}, "missing": 1,
            })

    def test_cli_catalog_descending_path_and_explicit_ascending(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for family, name in (
                ("workflow", "issue"), ("documentation", "architecture"),
                ("readme", "author"),
            ):
                (root / family / name).mkdir(parents=True)
            base = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--list-components",
                "--format", "json", "--sort-by", "path",
            ]
            implicit = subprocess.run(
                base, cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            ascending = subprocess.run(
                base + ["--sort-order", "asc"], cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            descending = subprocess.run(
                base + ["--sort-order", "desc"], cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            for result in (implicit, ascending, descending):
                self.assertEqual(result.returncode, 0, result.stderr)
            before = json.loads(implicit.stdout)
            asc = json.loads(ascending.stdout)
            desc = json.loads(descending.stdout)
            self.assertNotIn("sort_order", before["scope"])
            self.assertEqual(asc["scope"]["sort_order"], "asc")
            self.assertEqual(asc["components"], before["components"])
            self.assertEqual(desc["scope"]["sort_order"], "desc")
            self.assertEqual(desc["components"], list(reversed(before["components"])))

    def test_cli_catalog_descending_metadata_name_and_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for name, metadata_name in (
                ("architecture", "Zulu"), ("references", "Alpha"),
            ):
                component = root / "documentation" / name
                component.mkdir(parents=True)
                (component / "metadata.yml").write_text(
                    VALID_METADATA.replace("name: Architecture", f"name: {metadata_name}"),
                    encoding="utf-8",
                )
            (root / "readme" / "author").mkdir(parents=True)
            output = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--sort-by", "name",
                    "--sort-order", "desc", "--metadata-summary",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], [
                "documentation/architecture", "documentation/references",
                "readme/author",
            ])
            self.assertEqual(
                [entry["name"] for entry in catalog["details"]],
                ["Zulu", "Alpha", None],
            )
            self.assertEqual(catalog["metadata_summary"], {
                "loaded": 2, "missing": 1, "invalid": 0,
            })

    def test_cli_catalog_sort_order_requires_sort_by(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options, expected in (
                (["--sort-order", "desc"], "--sort-order requires --sort-by"),
                (["--list-components", "--sort-order", "desc"],
                 "--sort-order requires --sort-by"),
                (["--list-components", "--sort-by", "path",
                  "--sort-order", "backwards"], "invalid choice"),
                (["--sort-by", "path", "--sort-order", "desc"],
                 "--sort-by requires --list-components"),
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(expected, result.stderr)

    def test_cli_catalog_sort_by_status_places_missing_last(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experimental = self.create_component(root)
            (experimental / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            stable = root / "documentation" / "references"
            stable.mkdir(parents=True)
            (stable / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "DOC-REFERENCES")
                .replace("status: Experimental", "status: Stable"),
                encoding="utf-8",
            )
            (root / "readme" / "author").mkdir(parents=True)
            command = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--list-components",
                "--format", "json", "--details", "--sort-by", "status",
                "--component-status-summary",
            ]
            result = subprocess.run(
                command, cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["components"], [
                "documentation/architecture", "documentation/references",
                "readme/author",
            ])
            self.assertEqual(
                [entry["status"] for entry in catalog["details"]],
                ["Experimental", "Stable", None],
            )
            self.assertEqual(catalog["scope"]["sort_by"], "status")
            self.assertEqual(catalog["component_status_summary"], {
                "by_status": {"Experimental": 1, "Stable": 1}, "missing": 1,
            })

    def test_cli_catalog_sort_by_status_with_filters_and_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experimental = self.create_component(root)
            (experimental / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            stable = root / "documentation" / "references"
            stable.mkdir(parents=True)
            (stable / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "DOC-REFERENCES")
                .replace("status: Experimental", "status: Stable"),
                encoding="utf-8",
            )
            output = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--sort-by", "status",
                    "--component-status", "Sta*", "--metadata-summary",
                    "--component-status-summary", "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], ["documentation/references"])
            self.assertEqual(catalog["scope"]["sort_by"], "status")
            self.assertEqual(catalog["metadata_summary"]["loaded"], 1)
            self.assertEqual(catalog["component_status_summary"], {
                "by_status": {"Stable": 1}, "missing": 0,
            })

    def test_cli_catalog_sort_by_status_text_tie_breaks_by_path(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for name in ("references", "architecture"):
                component = root / "documentation" / name
                component.mkdir(parents=True)
                (component / "metadata.yml").write_text(
                    VALID_METADATA, encoding="utf-8"
                )
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--sort-by", "status",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), [
                "documentation/architecture", "documentation/references",
            ])

    def test_cli_catalog_component_status_summary_counts_declared_and_missing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experimental = self.create_component(root)
            (experimental / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            stable = root / "documentation" / "references"
            stable.mkdir(parents=True)
            (stable / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "DOC-REFERENCES")
                .replace("status: Experimental", "status: Stable"),
                encoding="utf-8",
            )
            invalid = root / "readme" / "author"
            invalid.mkdir(parents=True)
            (invalid / "metadata.yml").write_text(
                "status: [invalid", encoding="utf-8"
            )
            (root / "workflow" / "issue").mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--component-status-summary",
                    "--metadata-summary", "--family-summary",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["count"], 4)
            self.assertEqual(catalog["component_status_summary"], {
                "by_status": {"Experimental": 1, "Stable": 1},
                "missing": 2,
            })
            self.assertEqual(catalog["metadata_summary"], {
                "loaded": 2, "missing": 1, "invalid": 1,
            })
            self.assertNotIn("details", catalog)
            self.assertEqual(
                sum(catalog["component_status_summary"]["by_status"].values())
                + catalog["component_status_summary"]["missing"],
                catalog["count"],
            )

    def test_cli_catalog_component_status_summary_respects_filters_and_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experimental = self.create_component(root)
            (experimental / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            stable = root / "documentation" / "references"
            stable.mkdir(parents=True)
            (stable / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "DOC-REFERENCES")
                .replace("status: Experimental", "status: Stable"),
                encoding="utf-8",
            )
            (root / "readme" / "author").mkdir(parents=True)
            output = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--component-status-summary",
                    "--family", "documentation", "--component-status", "Sta*",
                    "--metadata-status", "loaded", "--details",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], ["documentation/references"])
            self.assertEqual(catalog["component_status_summary"], {
                "by_status": {"Stable": 1}, "missing": 0,
            })
            self.assertEqual(catalog["details"][0]["status"], "Stable")

    def test_cli_catalog_component_status_summary_requires_json_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--component-status-summary"],
                ["--format", "json", "--component-status-summary"],
                ["--list-components", "--component-status-summary"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(
                        "--component-status-summary requires --list-components --format json",
                        result.stderr,
                    )

    def test_cli_catalog_component_status_filters_declared_status(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            experimental = self.create_component(root)
            (experimental / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            stable = root / "documentation" / "references"
            stable.mkdir(parents=True)
            (stable / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "DOC-REFERENCES")
                .replace("status: Experimental", "status: Stable"),
                encoding="utf-8",
            )
            invalid = root / "readme" / "author"
            invalid.mkdir(parents=True)
            (invalid / "metadata.yml").write_text(
                "status: [broken", encoding="utf-8"
            )
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--metadata-summary",
                    "--component-status", "Sta*", "--component-status", "Exp*",
                    "--component-status", "Sta*", "--sort-by", "name",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["components"], [
                "documentation/architecture", "documentation/references",
            ])
            self.assertEqual(catalog["scope"]["component_status"], [
                "Sta*", "Exp*",
            ])
            self.assertEqual(
                [entry["status"] for entry in catalog["details"]],
                ["Experimental", "Stable"],
            )
            self.assertEqual(catalog["metadata_summary"], {
                "loaded": 2, "missing": 0, "invalid": 0,
            })

    def test_cli_catalog_component_status_text_and_safe_empty_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            base = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--list-components",
            ]
            selected = subprocess.run(
                base + ["--component-status", "Experimental"],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(selected.returncode, 0, selected.stderr)
            self.assertEqual(selected.stdout.splitlines(), [
                "documentation/architecture",
            ])
            output = root / "catalog.json"
            output.write_text("previous", encoding="utf-8")
            empty = subprocess.run(
                base + [
                    "--format", "json", "--component-status", "Stable",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(empty.returncode, 1)
            self.assertIn("No Components match", empty.stderr)
            self.assertEqual(empty.stdout, "")
            self.assertEqual(output.read_text(encoding="utf-8"), "previous")

    def test_cli_catalog_component_status_requires_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--component-status", "Experimental"],
                ["--format", "json", "--component-status", "Stable"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(
                        "--component-status requires --list-components",
                        result.stderr,
                    )

    def test_cli_catalog_metadata_name_filter_and_sort(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            architecture = self.create_component(root)
            (architecture / "metadata.yml").write_text(
                VALID_METADATA.replace("name: Architecture", "name: Zebra Design"),
                encoding="utf-8",
            )
            references = root / "documentation" / "references"
            references.mkdir(parents=True)
            (references / "metadata.yml").write_text(
                VALID_METADATA.replace("DOC-ARCHITECTURE", "DOC-REFERENCES")
                .replace("name: Architecture", "name: Alpha Design"),
                encoding="utf-8",
            )
            (root / "readme" / "author").mkdir(parents=True)
            command = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--list-components",
                "--format", "json", "--details", "--sort-by", "name",
                "--metadata-name", "*Design", "--metadata-name", "Alpha*",
                "--metadata-name", "*Design", "--family-summary",
            ]
            result = subprocess.run(
                command, cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["components"], [
                "documentation/references", "documentation/architecture",
            ])
            self.assertEqual(catalog["scope"]["metadata_name"], [
                "*Design", "Alpha*",
            ])
            self.assertEqual(catalog["scope"]["sort_by"], "name")
            self.assertEqual(
                [item["name"] for item in catalog["details"]],
                ["Alpha Design", "Zebra Design"],
            )
            self.assertEqual(catalog["family_summary"]["documentation"], 2)

    def test_cli_catalog_sort_by_name_missing_last(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            architecture = self.create_component(root)
            (architecture / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            (root / "documentation" / "references").mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--sort-by", "name",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), [
                "documentation/architecture", "documentation/references",
            ])

    def test_cli_catalog_metadata_name_empty_preserves_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )
            destination = root / "catalog.json"
            destination.write_text("previous", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--metadata-name", "Nonexistent*",
                    "--output", str(destination),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, "")
            self.assertIn("No Components match", result.stderr)
            self.assertEqual(destination.read_text(encoding="utf-8"), "previous")

    def test_cli_catalog_metadata_name_requires_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--metadata-name", "*"],
                ["--format", "json", "--metadata-name", "*"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(
                        "--metadata-name requires --list-components",
                        result.stderr,
                    )

    def test_cli_catalog_metadata_id_filters_loaded_ids(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            loaded = self.create_component(root)
            (loaded / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            invalid = root / "readme" / "author"
            invalid.mkdir(parents=True)
            (invalid / "metadata.yml").write_text("family: [bad", encoding="utf-8")
            output = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--metadata-summary",
                    "--metadata-id", "DOC-*", "--metadata-id", "*ARCHITECTURE",
                    "--metadata-id", "DOC-*", "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], ["documentation/architecture"])
            self.assertEqual(catalog["scope"]["metadata_id"], [
                "DOC-*", "*ARCHITECTURE",
            ])
            self.assertEqual(catalog["details"][0]["id"], "DOC-ARCHITECTURE")
            self.assertEqual(catalog["metadata_summary"], {
                "loaded": 1, "missing": 0, "invalid": 0,
            })

    def test_cli_catalog_metadata_id_text_and_empty_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            loaded = self.create_component(root)
            (loaded / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            common = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root), "--list-components",
            ]
            matched = subprocess.run(
                common + ["--metadata-id", "DOC-*"],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(matched.returncode, 0, matched.stderr)
            self.assertEqual(matched.stdout.splitlines(), [
                "documentation/architecture",
            ])
            output = root / "catalog.json"
            output.write_text("previous", encoding="utf-8")
            empty = subprocess.run(
                common + [
                    "--format", "json", "--metadata-id", "WCL-*",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(empty.returncode, 1)
            self.assertIn("No Components match", empty.stderr)
            self.assertEqual(empty.stdout, "")
            self.assertEqual(output.read_text(encoding="utf-8"), "previous")

    def test_cli_catalog_metadata_id_requires_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--metadata-id", "DOC-*"],
                ["--format", "json", "--metadata-id", "DOC-*"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(
                        "--metadata-id requires --list-components", result.stderr
                    )

    def test_cli_catalog_family_summary_counts_all_families(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for family, name in (
                ("documentation", "architecture"),
                ("documentation", "references"),
                ("readme", "author"),
                ("workflow", "issue"),
            ):
                (root / family / name).mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--family-summary",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["count"], 4)
            self.assertEqual(catalog["family_summary"], {
                "readme": 1, "documentation": 2, "workflow": 1,
            })
            self.assertNotIn("details", catalog)
            self.assertNotIn("metadata_summary", catalog)

    def test_cli_catalog_family_summary_composes_with_filters_and_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            doc = self.create_component(root)
            (doc / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            (root / "readme" / "author").mkdir(parents=True)
            destination = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--family-summary",
                    "--metadata-id", "DOC-*",
                    "--metadata-status", "loaded",
                    "--metadata-summary", "--output", str(destination),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(destination.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], ["documentation/architecture"])
            self.assertEqual(catalog["family_summary"], {
                "readme": 0, "documentation": 1, "workflow": 0,
            })
            self.assertEqual(catalog["metadata_summary"], {
                "loaded": 1, "missing": 0, "invalid": 0,
            })
            self.assertEqual(sum(catalog["family_summary"].values()), catalog["count"])

    def test_cli_catalog_family_summary_requires_json_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--family-summary"],
                ["--format", "json", "--family-summary"],
                ["--list-components", "--family-summary"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(
                        "--family-summary requires --list-components --format json",
                        result.stderr,
                    )

    def test_cli_catalog_metadata_summary_counts_all_states(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            loaded = self.create_component(root)
            (loaded / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            invalid = root / "readme" / "author"
            invalid.mkdir(parents=True)
            (invalid / "metadata.yml").write_text("family: [bad", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--metadata-summary",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["count"], 3)
            self.assertEqual(catalog["metadata_summary"], {
                "loaded": 1, "missing": 1, "invalid": 1,
            })
            self.assertNotIn("details", catalog)

    def test_cli_catalog_metadata_summary_respects_all_filters(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            loaded = self.create_component(root)
            (loaded / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            invalid = root / "documentation" / "database"
            invalid.mkdir(parents=True)
            (invalid / "metadata.yml").write_text("family: [bad", encoding="utf-8")
            output = root / "summary.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--metadata-summary",
                    "--family", "documentation", "--match", "documentation/*",
                    "--exclude", "*/database", "--metadata-status", "missing",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            catalog = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(catalog["components"], ["documentation/references"])
            self.assertEqual(catalog["metadata_summary"], {
                "loaded": 0, "missing": 1, "invalid": 0,
            })

    def test_cli_catalog_metadata_summary_requires_json_listing(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options in (
                ["--metadata-summary"],
                ["--format", "json", "--metadata-summary"],
                ["--list-components", "--metadata-summary"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(
                        "--metadata-summary requires --list-components --format json",
                        result.stderr,
                    )

    def test_cli_catalog_metadata_status_filters_text(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            loaded = self.create_component(root)
            (loaded / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            invalid = root / "readme" / "author"
            invalid.mkdir(parents=True)
            (invalid / "metadata.yml").write_text("family: [bad", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--metadata-status", "missing",
                    "--metadata-status", "invalid",
                    "--metadata-status", "missing",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.splitlines(), [
                "documentation/references", "readme/author",
            ])

    def test_cli_catalog_metadata_status_json_filter_and_export(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            loaded = self.create_component(root)
            (loaded / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            invalid = root / "documentation" / "database"
            invalid.mkdir(parents=True)
            (invalid / "metadata.yml").write_text("family: [bad", encoding="utf-8")
            output = root / "selected.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--family", "documentation",
                    "--match", "documentation/*", "--exclude", "*/database",
                    "--metadata-status", "loaded",
                    "--metadata-status", "missing",
                    "--metadata-status", "loaded",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            result_json = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(result_json["components"], [
                "documentation/architecture", "documentation/references",
            ])
            self.assertEqual(result_json["scope"], {
                "families": ["documentation"],
                "match": ["documentation/*"],
                "exclude": ["*/database"],
                "metadata_status": ["loaded", "missing"],
            })
            self.assertEqual(
                [entry["metadata_status"] for entry in result_json["details"]],
                ["loaded", "missing"],
            )

    def test_cli_catalog_metadata_status_empty_result_preserves_output(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            loaded = self.create_component(root)
            (loaded / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            output = root / "catalog.json"
            output.write_text("unchanged", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--metadata-status", "invalid",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("No Components match", result.stderr)
            self.assertEqual(result.stdout, "")
            self.assertEqual(output.read_text(encoding="utf-8"), "unchanged")

    def test_cli_catalog_metadata_status_requires_list_and_known_value(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            for options, fragment in (
                (["--metadata-status", "loaded"], "requires --list-components"),
                (["--format", "json", "--metadata-status", "missing"], "requires --list-components"),
                (["--list-components", "--metadata-status", "broken"], "invalid choice"),
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        [
                            sys.executable, "-m", "scripts.framework_validator",
                            "--components-root", str(root), *options,
                        ],
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn(fragment, result.stderr)


    def test_cli_list_components_json_catalog(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for family, name in (
                ("workflow", "issue"),
                ("documentation", "architecture"),
                ("readme", "author"),
            ):
                (root / family / name).mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root),
                    "--list-components", "--format", "json",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout), {
                "components": [
                    "documentation/architecture",
                    "readme/author",
                    "workflow/issue",
                ],
                "count": 3,
                "scope": {"families": ["readme", "documentation", "workflow"]},
            })

    def test_cli_list_components_json_scoped_catalog(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "documentation" / "architecture").mkdir(parents=True)
            (root / "workflow" / "issue").mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--family", "workflow",
                    "--family", "workflow",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout), {
                "components": ["workflow/issue"],
                "count": 1,
                "scope": {"families": ["workflow"]},
            })

    def test_cli_list_components_json_empty_directory_fails(self) -> None:
        with TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(Path(directory)),
                    "--list-components", "--format", "json",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, "")
            self.assertIn("No Components discovered", result.stderr)

    def test_cli_detailed_catalog_includes_metadata_and_missing_files(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            valid = self.create_component(root)
            (valid / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "documentation" / "references").mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["count"], 2)
            self.assertEqual(catalog["components"], [
                "documentation/architecture", "documentation/references",
            ])
            self.assertEqual(catalog["details"], [
                {
                    "path": "documentation/architecture",
                    "id": "DOC-ARCHITECTURE",
                    "name": "Architecture",
                    "version": "0.1.0",
                    "status": "Experimental",
                    "metadata_status": "loaded",
                },
                {
                    "path": "documentation/references",
                    "id": None, "name": None, "version": None, "status": None,
                    "metadata_status": "missing",
                },
            ])

    def test_cli_detailed_catalog_handles_invalid_yaml(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                "family: [unclosed", encoding="utf-8"
            )
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details", "--family", "documentation",
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            catalog = json.loads(result.stdout)
            self.assertEqual(catalog["details"][0]["metadata_status"], "invalid")
            self.assertIsNone(catalog["details"][0]["id"])

    def test_cli_json_catalog_export_with_metadata_and_family_filter(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(VALID_METADATA, encoding="utf-8")
            (root / "workflow" / "issue").mkdir(parents=True)
            output = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--family", "documentation",
                    "--details", "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            self.assertEqual(json.loads(output.read_text(encoding="utf-8")), {
                "components": ["documentation/architecture"],
                "count": 1,
                "scope": {"families": ["documentation"]},
                "details": [{
                    "path": "documentation/architecture",
                    "id": "DOC-ARCHITECTURE",
                    "name": "Architecture",
                    "version": "0.1.0",
                    "status": "Experimental",
                    "metadata_status": "loaded",
                }],
            })
            self.assertTrue(output.read_bytes().endswith(b"\n"))

    def test_cli_json_catalog_export_replaces_existing_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            output = root / "catalog.json"
            output.write_text("outdated", encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root),
                    "--list-components", "--format", "json",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["count"], 1)
            self.assertEqual(list(root.glob(".catalog.json.*.tmp")), [])

    def test_cli_json_catalog_export_reports_write_error(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            destination = root / "missing-parent" / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--output", str(destination),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")
            self.assertIn("Unable to write JSON catalog", result.stderr)
            self.assertFalse(destination.exists())

    def test_cli_json_catalog_export_replace_failure_preserves_existing_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            output = root / "catalog.json"
            old_catalog = '{"components": ["previous"]}\n'
            output.write_text(old_catalog, encoding="utf-8")
            stdout = io.StringIO()
            stderr = io.StringIO()

            with (
                patch.object(
                    validator_cli.os,
                    "replace",
                    side_effect=OSError("simulated replace failure"),
                ),
                redirect_stdout(stdout),
                redirect_stderr(stderr),
            ):
                written = validator_cli.write_json_output(
                    '{"components": ["readme/author"]}',
                    output,
                    label="catalog",
                )

            self.assertFalse(written)
            self.assertEqual(stdout.getvalue(), "")
            self.assertIn("Unable to write JSON catalog", stderr.getvalue())
            self.assertEqual(output.read_text(encoding="utf-8"), old_catalog)
            self.assertEqual(list(root.glob(".catalog.json.*.tmp")), [])

    def test_cli_json_catalog_export_with_invalid_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                "family: [unclosed", encoding="utf-8"
            )
            output = root / "catalog.json"
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--format", "json", "--details",
                    "--output", str(output),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")
            report = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(report["count"], 1)
            self.assertEqual(report["details"][0]["metadata_status"], "invalid")
            self.assertIsNone(report["details"][0]["id"])


    def test_cli_catalog_text_output_argument_rejected(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "readme" / "author").mkdir(parents=True)
            result = subprocess.run(
                [
                    sys.executable, "-m", "scripts.framework_validator",
                    "--components-root", str(root), "--list-components",
                    "--output", str(root / "catalog.json"),
                ],
                cwd=validator_cli.REPOSITORY_ROOT,
                capture_output=True, text=True, check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("--output requires --format json", result.stderr)


    def test_cli_details_requires_json_catalog(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            common = [
                sys.executable, "-m", "scripts.framework_validator",
                "--components-root", str(root),
            ]
            for options in (
                ["--details"],
                ["--list-components", "--details"],
                ["--format", "json", "--details"],
            ):
                with self.subTest(options=options):
                    result = subprocess.run(
                        common + options,
                        cwd=validator_cli.REPOSITORY_ROOT,
                        capture_output=True, text=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("--details requires", result.stderr)
