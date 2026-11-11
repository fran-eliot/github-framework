"""Build a concise GitHub Actions summary from a Validator JSON report."""

import argparse
import json
import os
from pathlib import Path


def _markdown_cell(value: str) -> str:
    """Escape a value so it remains in one Markdown table cell."""
    return (
        value.replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("\r", " ")
        .replace("\n", " ")
    )


def render_summary(report: dict) -> str:
    """Render aggregate results and a bounded list of failed Components."""
    summary = report["summary"]
    scope = report["scope"]
    families = ", ".join(scope["families"])
    scope_label = "Partial" if scope["filtered"] else "Full"
    status = "Passed" if report["status"] == "passed" else "Failed"

    result = (
        "## Framework Validator\n\n"
        "| Result | Value |\n"
        "| --- | --- |\n"
        f"| Validation | {status} |\n"
        f"| Scope | {scope_label} ({families}) |\n"
        f"| Passed Components | {summary['passed_components']} |\n"
        f"| Failed Components | {summary['failed_components']} |\n"
        f"| Validation errors | {summary['error_count']} |\n"
    )

    failed_components = [
        component
        for component in report.get("components", [])
        if component["status"] == "failed"
    ]
    if failed_components:
        result += (
            "\n### Failed Components\n\n"
            "| Component | Errors | First diagnostic |\n"
            "| --- | ---: | --- |\n"
        )
        for component in failed_components[:10]:
            # Evitar que el contenido del informe altere la tabla Markdown.
            path = _markdown_cell(str(component["relative_path"]))
            diagnostic = (
                _markdown_cell(str(component["errors"][0]))
                if component["errors"]
                else "No diagnostic available"
            )
            if len(diagnostic) > 160:
                diagnostic = diagnostic[:157] + "..."
            result += f"| {path} | {len(component['errors'])} | {diagnostic} |\n"
        if len(failed_components) > 10:
            result += (
                f"\n{len(failed_components) - 10} more failed Component(s) "
                "are listed in the JSON artifact.\n"
            )

    return result + "\nThe full JSON report is available in the workflow artifacts.\n"


def _workflow_escape(value: str, property_value: bool = False) -> str:
    """Encode content for GitHub Actions workflow commands."""
    escaped = (
        value.replace("%", "%25")
        .replace("\r", "%0D")
        .replace("\n", "%0A")
    )
    if property_value:
        escaped = escaped.replace(":", "%3A").replace(",", "%2C")
    return escaped


def render_annotations(report: dict, limit: int = 25) -> str:
    """Emit bounded file-linked errors from a Validator JSON report."""
    diagnostics: list[tuple[str | None, str]] = []
    for component in report.get("components", []):
        if component["status"] != "failed":
            continue
        path = "framework/components/" + component["relative_path"] + "/metadata.yml"
        for error in component["errors"]:
            diagnostics.append((path, str(error)))

    if not diagnostics and report.get("status") == "failed":
        diagnostics.extend((None, str(error)) for error in report.get("errors", []))

    commands = []
    for path, message in diagnostics[:limit]:
        detail = _workflow_escape(message[:500])
        properties = (
            " file=" + _workflow_escape(path, property_value=True) + ",title=Component validation"
            if path is not None
            else " title=Component validation"
        )
        commands.append(f"::error{properties}::{detail}")

    remaining = len(diagnostics) - limit
    if remaining > 0:
        commands.append(
            f"::notice::{remaining} additional validation errors are in the JSON artifact."
        )
    return "\n".join(commands) + ("\n" if commands else "")


def main() -> None:
    """Append a report summary to the file provided by GitHub Actions."""
    parser = argparse.ArgumentParser(description="Summarize a Validator JSON report.")
    parser.add_argument("report_path", type=Path)
    parser.add_argument(
        "--annotations", action="store_true",
        help="Print GitHub Actions error annotations instead of a job summary.",
    )
    arguments = parser.parse_args()

    if arguments.annotations:
        if arguments.report_path.is_file():
            report = json.loads(arguments.report_path.read_text(encoding="utf-8"))
            print(render_annotations(report), end="")
        return

    destination = Path(os.environ["GITHUB_STEP_SUMMARY"])
    if arguments.report_path.is_file():
        report = json.loads(arguments.report_path.read_text(encoding="utf-8"))
        message = render_summary(report)
    else:
        message = (
            "## Framework Validator\n\n"
            "No JSON report was produced; inspect the preceding workflow steps.\n"
        )
    with destination.open("a", encoding="utf-8") as summary_file:
        summary_file.write(message)


if __name__ == "__main__":
    main()
