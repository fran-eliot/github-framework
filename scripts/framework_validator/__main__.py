"""Command-line entry point for the Framework Validator."""

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path

import yaml

from .discovery import discover_components, load_metadata

from .validation import (
    validate_common_core,
    validate_component_identity,
    validate_unique_ids,
    validate_maturity,
    validate_dependencies,
    validate_optional_common_fields,
    validate_workflow_materialization,
    validate_workflow_artifacts,
    validate_workflow_artifact_files,
    validate_workflow_adoption,
    validate_workflow_validation
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
COMPONENTS_ROOT = REPOSITORY_ROOT / "framework" / "components"


def main(output_format: str = "text", output_path: Path | None = None) -> int:
    """Discover Components and check that their metadata can be loaded."""
    if output_format == "text":
        print("GitHub Framework Validator")
        print()

    component_dirs = discover_components(COMPONENTS_ROOT)
    errors: list[str] = []

    if not component_dirs:
        errors.append(
            f"{COMPONENTS_ROOT}: no Components discovered"
        )

    if output_format == "text":
        print(f"Components discovered: {len(component_dirs)}")

    loaded_components: list[tuple[Path, dict]] = []

    for component_dir in component_dirs:
        metadata_path = component_dir / "metadata.yml"

        if not metadata_path.is_file():
            errors.append(
                f"{component_dir}: missing metadata.yml"
            )
            continue

        try:
            metadata = load_metadata(metadata_path)
        except (OSError, yaml.YAMLError, ValueError) as exc:
            errors.append(
                f"{metadata_path}: unable to load metadata: {exc}"
            )
            continue

        loaded_components.append((metadata_path, metadata))
        component_id = metadata.get("id", "<missing id>")

        for error in validate_common_core(metadata):
            errors.append(f"{metadata_path}: {error}")

        identity_errors = validate_component_identity(
            metadata,
            family_directory=component_dir.parent.name,
            component_directory=component_dir.name,
        )

        for error in identity_errors:
            errors.append(f"{metadata_path}: {error}")

        for error in validate_maturity(metadata):
            errors.append(f"{metadata_path}: {error}")

        for error in validate_dependencies(metadata):
            errors.append(f"{metadata_path}: {error}")

        for error in validate_optional_common_fields(metadata):
            errors.append(f"{metadata_path}: {error}")

        for error in validate_workflow_materialization(metadata):
            errors.append(f"{metadata_path}: {error}")

        for error in validate_workflow_artifacts(metadata):
            errors.append(f"{metadata_path}: {error}")

        for error in validate_workflow_artifact_files(metadata, component_dir):
            errors.append(f"{metadata_path}: {error}")

        for error in validate_workflow_adoption(metadata):
            errors.append(f"{metadata_path}: {error}")

        for error in validate_workflow_validation(metadata):
            errors.append(f"{metadata_path}: {error}")

        if output_format == "text":
            print(f"  {component_id}: {component_dir.name}")

    errors.extend(validate_unique_ids(loaded_components))

    if output_format == "json":
        metadata_by_path = dict(loaded_components)
        component_results = []

        for component_dir in component_dirs:
            metadata_path = component_dir / "metadata.yml"
            component_errors = [
                error
                for error in errors
                if error.startswith(f"{metadata_path}:")
                or error.startswith(f"{component_dir}:")
                or (
                    "id: duplicate " in error
                    and f"first declared in {metadata_path}" in error
                )
            ]
            component_results.append(
                {
                    "path": str(component_dir),
                    "id": metadata_by_path.get(metadata_path, {}).get("id"),
                    "status": "failed" if component_errors else "passed",
                    "errors": component_errors,
                }
            )

        report = json.dumps(
            {
                "status": "failed" if errors else "passed",
                "components_discovered": len(component_dirs),
                "component_ids": [
                    metadata.get("id")
                    for _, metadata in loaded_components
                ],
                "errors": errors,
                "components": component_results,
                "summary": {
                    "passed_components": sum(
                        item["status"] == "passed" for item in component_results
                    ),
                    "failed_components": sum(
                        item["status"] == "failed" for item in component_results
                    ),
                    "error_count": len(errors),
                },
            },
            indent=2,
        )
        if output_path is None:
            print(report)
        else:
            temporary_path = None
            try:
                with tempfile.NamedTemporaryFile(
                    mode="w",
                    encoding="utf-8",
                    newline="\n",
                    dir=output_path.parent,
                    prefix=f".{output_path.name}.",
                    suffix=".tmp",
                    delete=False,
                ) as temporary_file:
                    temporary_path = Path(temporary_file.name)
                    temporary_file.write(report + "\n")
                os.replace(temporary_path, output_path)
            except OSError as exc:
                print(
                    f"Unable to write JSON report to {output_path}: {exc}",
                    file=sys.stderr,
                )
                return 2
            finally:
                if temporary_path is not None:
                    temporary_path.unlink(missing_ok=True)
    else:
        print()
        if errors:
            print(f"Validation failed: {len(errors)} error(s)")
            for error in errors:
                print(f"  ERROR: {error}")
        else:
            print(
                "Validation passed: discovery, metadata loading, Common Core, "
                "identity, uniqueness, maturity, dependencies and Workflow extensions."
            )

    return 1 if errors else 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Framework Component metadata.")
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format (default: text).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        metavar="PATH",
        help="Write the JSON report to PATH (requires --format json).",
    )
    arguments = parser.parse_args()
    if arguments.output is not None and arguments.format != "json":
        parser.error("--output requires --format json")
    raise SystemExit(main(output_format=arguments.format, output_path=arguments.output))