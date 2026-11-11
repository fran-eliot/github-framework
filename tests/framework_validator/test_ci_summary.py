"""Tests for the Framework Validator GitHub Actions summary."""

import json
import os
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.framework_validator.ci_summary import render_annotations, render_summary
from scripts.framework_validator.__main__ import REPOSITORY_ROOT


class FrameworkValidatorSummaryTests(unittest.TestCase):
    def test_full_success_summary(self) -> None:
        report = {
            "status": "passed",
            "scope": {
                "families": ["readme", "documentation", "workflow"],
                "filtered": False,
            },
            "summary": {
                "passed_components": 21,
                "failed_components": 0,
                "error_count": 0,
            },
        }
        summary = render_summary(report)
        self.assertIn("| Validation | Passed |", summary)
        self.assertIn("| Scope | Full (readme, documentation, workflow) |", summary)
        self.assertIn("| Passed Components | 21 |", summary)
        self.assertIn("| Validation errors | 0 |", summary)

    def test_partial_failure_summary(self) -> None:
        report = {
            "status": "failed",
            "scope": {"families": ["workflow"], "filtered": True},
            "summary": {
                "passed_components": 2,
                "failed_components": 1,
                "error_count": 3,
            },
        }
        summary = render_summary(report)
        self.assertIn("| Validation | Failed |", summary)
        self.assertIn("| Scope | Partial (workflow) |", summary)
        self.assertIn("| Failed Components | 1 |", summary)
        self.assertIn("| Validation errors | 3 |", summary)

    def test_cli_appends_summary_from_json_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "validator-report.json"
            target = root / "summary.md"
            target.write_text("Earlier step\n", encoding="utf-8")
            source.write_text(
                json.dumps({
                    "status": "passed",
                    "scope": {"families": ["documentation"], "filtered": True},
                    "summary": {
                        "passed_components": 1,
                        "failed_components": 0,
                        "error_count": 0,
                    },
                }),
                encoding="utf-8",
            )
            result = subprocess.run(
                [
                    sys.executable, "-m",
                    "scripts.framework_validator.ci_summary", str(source),
                ],
                cwd=REPOSITORY_ROOT,
                env={**os.environ, "GITHUB_STEP_SUMMARY": str(target)},
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            output = target.read_text(encoding="utf-8")
            self.assertTrue(output.startswith("Earlier step\n"))
            self.assertIn("| Scope | Partial (documentation) |", output)

    def test_cli_missing_report_records_diagnostic(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "summary.md"
            result = subprocess.run(
                [
                    sys.executable, "-m",
                    "scripts.framework_validator.ci_summary",
                    str(root / "missing.json"),
                ],
                cwd=REPOSITORY_ROOT,
                env={**os.environ, "GITHUB_STEP_SUMMARY": str(target)},
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn(
                "No JSON report was produced",
                target.read_text(encoding="utf-8"),
            )

    def test_failed_components_are_listed_with_error_counts(self) -> None:
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 1,
                "failed_components": 2,
                "error_count": 3,
            },
            "components": [
                {
                    "relative_path": "documentation/architecture",
                    "status": "passed",
                    "errors": [],
                },
                {
                    "relative_path": "documentation/references",
                    "status": "failed",
                    "errors": ["missing metadata.yml"],
                },
                {
                    "relative_path": "documentation/samples",
                    "status": "failed",
                    "errors": ["error one", "error two"],
                },
            ],
        }
        result = render_summary(report)
        self.assertIn("### Failed Components", result)
        self.assertIn("| documentation/references | 1 | missing metadata.yml |", result)
        self.assertIn("| documentation/samples | 2 | error one |", result)
        self.assertNotIn("| documentation/architecture |", result)

    def test_success_summary_does_not_include_failed_table(self) -> None:
        report = {
            "status": "passed",
            "scope": {"families": ["workflow"], "filtered": True},
            "summary": {
                "passed_components": 1,
                "failed_components": 0,
                "error_count": 0,
            },
            "components": [
                {
                    "relative_path": "workflow/issue",
                    "status": "passed",
                    "errors": [],
                },
            ],
        }
        self.assertNotIn("### Failed Components", render_summary(report))

    def test_failed_components_list_is_limited_to_ten(self) -> None:
        components = [
            {
                "relative_path": f"documentation/component-{i:02}",
                "status": "failed",
                "errors": ["invalid metadata"],
            }
            for i in range(12)
        ]
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 0,
                "failed_components": 12,
                "error_count": 12,
            },
            "components": components,
        }
        result = render_summary(report)
        self.assertIn("| documentation/component-09 | 1 | invalid metadata |", result)
        self.assertNotIn("| documentation/component-10 | 1 | invalid metadata |", result)
        self.assertIn("2 more failed Component(s)", result)

    def test_failed_component_paths_are_escaped(self) -> None:
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 0,
                "failed_components": 1,
                "error_count": 1,
            },
            "components": [
                {
                    "relative_path": "documentation/invalid|line\nbreak",
                    "status": "failed",
                    "errors": ["invalid metadata"],
                },
            ],
        }
        result = render_summary(report)
        self.assertIn(r"| documentation/invalid\|line break | 1 | invalid metadata |", result)

    def test_first_diagnostic_is_escaped(self) -> None:
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 0,
                "failed_components": 1,
                "error_count": 1,
            },
            "components": [
                {
                    "relative_path": "documentation/references",
                    "status": "failed",
                    "errors": ["field|value\non next line\\detail"],
                },
            ],
        }
        result = render_summary(report)
        self.assertIn(
            r"| documentation/references | 1 | field\|value on next line\\detail |",
            result,
        )

    def test_first_diagnostic_is_truncated(self) -> None:
        diagnostic = "x" * 200
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 0,
                "failed_components": 1,
                "error_count": 1,
            },
            "components": [
                {
                    "relative_path": "documentation/references",
                    "status": "failed",
                    "errors": [diagnostic],
                },
            ],
        }
        result = render_summary(report)
        self.assertIn(f"| 1 | {'x' * 157}... |", result)
        self.assertNotIn(diagnostic, result)

    def test_failed_component_without_diagnostics_has_fallback(self) -> None:
        report = {
            "status": "failed",
            "scope": {"families": ["documentation"], "filtered": True},
            "summary": {
                "passed_components": 0,
                "failed_components": 1,
                "error_count": 0,
            },
            "components": [
                {
                    "relative_path": "documentation/references",
                    "status": "failed",
                    "errors": [],
                },
            ],
        }
        self.assertIn(
            "| documentation/references | 0 | No diagnostic available |",
            render_summary(report),
        )

    def test_annotations_include_component_file_and_escape_diagnostics(self) -> None:
        report = {
            "status": "failed",
            "components": [
                {
                    "status": "passed",
                    "relative_path": "documentation/architecture",
                    "errors": [],
                },
                {
                    "status": "failed",
                    "relative_path": "documentation/odd,name:section",
                    "errors": ["Unexpected 100% \n::warning::injection\r", "second error"],
                },
            ],
        }
        commands = render_annotations(report)
        self.assertIn(
            "::error file=framework/components/documentation/odd%2Cname%3Asection/"
            "metadata.yml,title=Component validation::"
            "Unexpected 100%25 %0A::warning::injection%0D",
            commands,
        )
        self.assertEqual(commands.count("::error "), 2)
        self.assertNotIn("\n::warning::injection", commands)

    def test_annotations_are_bounded_and_report_remaining_count(self) -> None:
        report = {
            "status": "failed",
            "components": [{
                "status": "failed",
                "relative_path": "workflow/issue",
                "errors": [f"failure-{i}" for i in range(4)],
            }],
        }
        commands = render_annotations(report, limit=2)
        self.assertEqual(commands.count("::error "), 2)
        self.assertIn("::notice::2 additional validation errors", commands)
        self.assertNotIn("failure-2", commands)

    def test_annotations_for_global_discovery_failure(self) -> None:
        report = {
            "status": "failed",
            "components": [],
            "errors": ["no Components discovered"],
        }
        self.assertEqual(
            render_annotations(report),
            "::error title=Component validation::no Components discovered\n",
        )

    def test_annotations_success_and_missing_report(self) -> None:
        self.assertEqual(
            render_annotations({"status": "passed", "components": [], "errors": []}),
            "",
        )
        with TemporaryDirectory() as directory:
            root = Path(directory)
            result = subprocess.run(
                [
                    sys.executable, "-m",
                    "scripts.framework_validator.ci_summary",
                    str(root / "missing.json"), "--annotations",
                ],
                cwd=REPOSITORY_ROOT,
                env={key: value for key, value in os.environ.items()
                     if key != "GITHUB_STEP_SUMMARY"},
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout, "")

    def test_annotations_cli_prints_commands_only(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "validator-report.json"
            source.write_text(json.dumps({
                "status": "failed",
                "components": [{
                    "status": "failed",
                    "relative_path": "documentation/references",
                    "errors": ["missing metadata.yml"],
                }],
            }), encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-m",
                    "scripts.framework_validator.ci_summary",
                    str(source), "--annotations",
                ],
                cwd=REPOSITORY_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(
                result.stdout,
                "::error file=framework/components/documentation/references/"
                "metadata.yml,title=Component validation::missing metadata.yml\n",
            )
