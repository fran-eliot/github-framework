"""Build a concise GitHub Actions summary from a Validator JSON report."""

import argparse
import json
import os
from pathlib import Path


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
            "| Component | Errors |\n"
            "| --- | ---: |\n"
        )
        for component in failed_components[:10]:
            # Evitar que las rutas alteren las columnas de la tabla Markdown.
            path = str(component["relative_path"]).replace("\\", "\\\\")
            path = path.replace("|", "\\|").replace("\n", " ").replace("\r", " ")
            result += f"| {path} | {len(component['errors'])} |\n"
        if len(failed_components) > 10:
            result += (
                f"\n{len(failed_components) - 10} more failed Component(s) "
                "are listed in the JSON artifact.\n"
            )

    return result + "\nThe full JSON report is available in the workflow artifacts.\n"


def main() -> None:
    """Append a report summary to the file provided by GitHub Actions."""
    parser = argparse.ArgumentParser(description="Summarize a Validator JSON report.")
    parser.add_argument("report_path", type=Path)
    arguments = parser.parse_args()

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
