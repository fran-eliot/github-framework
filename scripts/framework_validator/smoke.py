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

    excluded = run_cli(
        "--list-components", "--format", "json",
        "--match", "documentation/*", "--exclude", examples[0],
    )
    assert excluded["components"] == examples[1:]
    assert excluded["count"] == len(examples) - 1
    assert excluded["scope"]["match"] == ["documentation/*"]
    assert excluded["scope"]["exclude"] == [examples[0]]

    loaded_catalog = run_cli(
        "--list-components", "--format", "json", "--details",
        "--metadata-status", "loaded",
    )
    assert loaded_catalog["components"] == paths
    assert loaded_catalog["details"] == details["details"]
    assert loaded_catalog["scope"]["metadata_status"] == ["loaded"]
    missing_catalog = run_cli(
        "--list-components", "--format", "json",
        "--metadata-status", "missing", success=False,
    )
    assert missing_catalog.returncode == 1 and not missing_catalog.stdout

    # Check newer catalog contracts against the real metadata, not test fixtures.
    metadata = {entry["path"]: entry for entry in details["details"]}
    assert all(isinstance(entry["name"], str) for entry in metadata.values())
    assert all(isinstance(entry["version"], str) for entry in metadata.values())

    family_summary = run_cli(
        "--list-components", "--format", "json", "--family-summary",
    )
    expected_families = {
        family: sum(path.startswith(f"{family}/") for path in paths)
        for family in FAMILIES
    }
    assert family_summary["components"] == paths
    assert family_summary["family_summary"] == expected_families
    assert sum(family_summary["family_summary"].values()) == len(paths)

    metadata_summary = run_cli(
        "--list-components", "--format", "json", "--metadata-summary",
    )
    assert metadata_summary["components"] == paths
    assert metadata_summary["metadata_summary"] == {
        "loaded": len(paths), "missing": 0, "invalid": 0,
    }

    first = details["details"][0]
    for option, field in (
        ("--metadata-id", "id"),
        ("--metadata-name", "name"),
        ("--metadata-version", "version"),
    ):
        value = first[field]
        assert isinstance(value, str)
        selected = [path for path in paths if metadata[path][field] == value]
        filtered = run_cli(
            "--list-components", "--format", "json", option, value,
            "--family-summary", "--metadata-summary",
        )
        assert filtered["components"] == selected
        assert filtered["scope"][option.removeprefix("--").replace("-", "_")] == [value]
        assert filtered["metadata_summary"] == {
            "loaded": len(selected), "missing": 0, "invalid": 0,
        }
        assert sum(filtered["family_summary"].values()) == len(selected)

    for field in ("id", "name", "version"):
        ordered = run_cli(
            "--list-components", "--format", "json",
            "--sort-by", field, "--details",
        )
        expected = sorted(paths, key=lambda path: (metadata[path][field], path))
        assert ordered["components"] == expected
        assert [entry["path"] for entry in ordered["details"]] == expected
        assert ordered["scope"]["sort_by"] == field

    # Combined filtering, ordering, summaries and atomic output must agree.
    sample_family = first["path"].split("/", 1)[0]
    expected = sorted(
        [path for path in paths if path.startswith(f"{sample_family}/")],
        key=lambda path: (metadata[path]["name"], path),
    )
    with TemporaryDirectory() as directory:
        destination = Path(directory) / "selected-catalog.json"
        command = [
            sys.executable, "-m", "scripts.framework_validator",
            "--list-components", "--format", "json",
            "--family", sample_family, "--metadata-status", "loaded",
            "--sort-by", "name", "--details", "--family-summary",
            "--metadata-summary", "--output", str(destination),
        ]
        exported = subprocess.run(
            command, cwd=ROOT, capture_output=True, text=True, check=False,
        )
        assert exported.returncode == 0, exported.stderr
        assert not exported.stdout
        selected = json.loads(destination.read_text(encoding="utf-8"))
        assert selected["components"] == expected
        assert [item["path"] for item in selected["details"]] == expected
        assert selected["family_summary"][sample_family] == len(expected)
        assert selected["metadata_summary"]["loaded"] == len(expected)
        original = destination.read_bytes()

        no_match = subprocess.run(
            [
                sys.executable, "-m", "scripts.framework_validator",
                "--list-components", "--format", "json",
                "--metadata-id", "NONEXISTENT-ID-FOR-SMOKE-*",
                "--output", str(destination),
            ],
            cwd=ROOT, capture_output=True, text=True, check=False,
        )
        assert no_match.returncode == 1 and not no_match.stdout
        assert destination.read_bytes() == original

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
        "catalog_exclusion_verified": True,
        "catalog_metadata_status_verified": True,
        "catalog_metadata_queries_verified": True,
        "catalog_metadata_sorting_verified": True,
        "catalog_summaries_verified": True,
        "catalog_combined_export_verified": True,
        "families_checked": list(FAMILIES),
        "targeted_components": representatives,
        "invalid_combination_rejected": True,
    }, indent=2))


if __name__ == "__main__":
    main()
