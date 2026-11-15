"""Smoke-test the public Validator CLI against the real Component library.

Unlike the unit tests' temporary fixtures, this uses the tracked repository
Components and verifies the CLI's catalog and filtered validation contracts.
"""

import json
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory


ROOT = Path(__file__).resolve().parents[2]
FAMILIES = ("readme", "documentation", "workflow")


def run_cli(*arguments: str, success: bool = True) -> dict | subprocess.CompletedProcess[str]:
    command = [sys.executable, "-m", "scripts.framework_validator", *arguments]
    result = subprocess.run(
        command, cwd=ROOT, capture_output=True, text=True, check=False
    )
    if success and result.returncode != 0:
        raise AssertionError(
            f"CLI failed with code {result.returncode}: {' '.join(arguments)}\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )
    if not success:
        return result
    try:
        return json.loads(result.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(
            f"CLI did not emit JSON for {' '.join(arguments)}: {result.stdout}"
        ) from exc


def main() -> None:
    catalog = run_cli("--list-components", "--format", "json")
    paths = catalog["components"]
    assert catalog["count"] == len(paths) and len(paths) > 0
    assert len(paths) == len(set(paths)), "Duplicate catalog Component paths"
    assert catalog["scope"]["families"] == list(FAMILIES)

    details = run_cli("--list-components", "--format", "json", "--details")
    assert details["components"] == paths
    assert details["count"] == len(paths)
    assert [entry["path"] for entry in details["details"]] == paths
    assert all(entry["metadata_status"] == "loaded" for entry in details["details"])
    assert all(entry["id"] for entry in details["details"])

    # Exercise the exported catalog with actual tracked Component metadata.
    with TemporaryDirectory() as directory:
        destination = Path(directory) / "component-catalog.json"
        exported = subprocess.run(
            [
                sys.executable, "-m", "scripts.framework_validator",
                "--list-components", "--format", "json", "--details",
                "--output", str(destination),
            ],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        assert exported.returncode == 0, exported.stderr
        assert exported.stdout == "", "Catalog export must not print JSON to stdout"
        assert json.loads(destination.read_text(encoding="utf-8")) == details
        assert destination.read_bytes().endswith(b"\n")
        assert list(Path(directory).glob(".component-catalog.json.*.tmp")) == []

    # Pattern filtering selects a sorted, unique union of portable Component paths.
    examples = [path for path in paths if path.startswith("documentation/")]
    assert examples, "No Documentation Components available for pattern matching"
    matched = run_cli(
        "--list-components", "--format", "json",
        "--match", "documentation/*", "--match", examples[0],
    )
    assert matched["components"] == examples
    assert matched["count"] == len(examples)
    assert matched["scope"]["match"] == ["documentation/*", examples[0]]
    no_match = run_cli(
        "--list-components", "--format", "json",
        "--match", "nonexistent/*", success=False,
    )
    assert no_match.returncode == 1 and not no_match.stdout

    representatives = []
    for family in FAMILIES:
        selected = [path for path in paths if path.startswith(f"{family}/")]
        assert selected, f"No Component in family {family}"
        family_catalog = run_cli(
            "--list-components", "--format", "json", "--family", family
        )
        assert family_catalog["components"] == selected
        assert family_catalog["count"] == len(selected)
        assert family_catalog["scope"]["families"] == [family]
        representatives.append(selected[0])

        family_validation = run_cli("--format", "json", "--family", family)
        assert family_validation["status"] == "passed"
        assert family_validation["components_discovered"] == len(selected)
        assert family_validation["scope"]["filtered"] is True
        assert family_validation["scope"]["families"] == [family]
        assert {item["relative_path"] for item in family_validation["components"]} == set(selected)
        assert family_validation["summary"]["error_count"] == 0

    selections = [arg for path in representatives for arg in ("--component", path)]
    targeted = run_cli("--format", "json", *selections)
    assert targeted["status"] == "passed"
    assert targeted["components_discovered"] == len(representatives)
    assert targeted["scope"]["filtered"] is True
    assert targeted["scope"]["component_paths"] == sorted(representatives)
    assert targeted["scope"]["families"] == list(FAMILIES)
    assert {item["relative_path"] for item in targeted["components"]} == set(representatives)
    assert targeted["summary"]["error_count"] == 0

    rejected = run_cli(
        "--list-components", "--component", representatives[0], success=False
    )
    assert rejected.returncode != 0
    assert "cannot be combined" in rejected.stderr

    print(json.dumps({
        "status": "passed",
        "catalog_components": len(paths),
        "details_metadata_loaded": len(details["details"]),
        "catalog_export_verified": True,
        "catalog_pattern_matching_verified": True,
        "families_checked": list(FAMILIES),
        "targeted_components": representatives,
        "invalid_combination_rejected": True,
    }, indent=2))


if __name__ == "__main__":
    main()
