"""Command-line entry point for the Framework Validator."""

import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path

import yaml

from .discovery import COMPONENT_FAMILIES, discover_components, load_metadata

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


def main(
    output_format: str = "text",
    output_path: Path | None = None,
    components_root: Path | None = None,
    families: tuple[str, ...] | None = None,
    component_paths: tuple[str, ...] | None = None,
) -> int:
    """Discover Components and check that their metadata can be loaded."""
    root = COMPONENTS_ROOT if components_root is None else components_root
    if output_format == "text":
        print("GitHub Framework Validator")
        print()

    component_dirs = discover_components(root, families=families)
    if component_paths is not None:
        selected = set(component_paths)
        component_dirs = [
            component for component in component_dirs
            if component.relative_to(root).as_posix() in selected
        ]
    errors: list[str] = []

    if not component_dirs:
        errors.append(
            f"{root}: no Components discovered"
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
                    "relative_path": component_dir.relative_to(root).as_posix(),
                    "id": metadata_by_path.get(metadata_path, {}).get("id"),
                    "status": "failed" if component_errors else "passed",
                    "errors": component_errors,
                }
            )

        selected_families = [
            family for family in COMPONENT_FAMILIES
            if (
                (component_paths is None and (families is None or family in families))
                or (component_paths is not None and any(
                    path.startswith(f"{family}/") for path in component_paths
                ))
            )
        ]
        scope = {
            "families": selected_families,
            "filtered": (
                component_paths is not None
                or len(selected_families) != len(COMPONENT_FAMILIES)
            ),
        }
        if component_paths is not None:
            scope["component_paths"] = sorted(set(component_paths))
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
                "scope": scope,
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
    parser.add_argument(
        "--components-root",
        type=Path,
        metavar="PATH",
        help="Component library directory (default: repository framework/components).",
    )
    parser.add_argument(
        "--family",
        action="append",
        choices=COMPONENT_FAMILIES,
        metavar="{readme,documentation,workflow}",
        help="Validate only this Component family (repeatable; default: all).",
    )
    parser.add_argument(
        "--list-components",
        action="store_true",
        help="List available family/name Component paths without validation.",
    )
    parser.add_argument(
        "--details",
        action="store_true",
        help="Include basic metadata in the JSON Component catalog.",
    )
    parser.add_argument(
        "--component",
        action="append",
        metavar="FAMILY/NAME",
        help="Validate only this Component (repeatable; cannot combine with --family).",
    )
    arguments = parser.parse_args()
    if arguments.details and (
        not arguments.list_components or arguments.format != "json"
    ):
        parser.error("--details requires --list-components --format json")
    if arguments.list_components:
        if arguments.component:
            parser.error("--list-components cannot be combined with --component")
        if arguments.output is not None:
            parser.error("--list-components does not support --output")
    if arguments.component and arguments.family:
        parser.error("--component cannot be combined with --family")
    if arguments.output is not None and arguments.format != "json":
        parser.error("--output requires --format json")
    if arguments.components_root is not None and not arguments.components_root.is_dir():
        parser.error("--components-root must be an existing directory")
    if arguments.component:
        root = arguments.components_root or COMPONENTS_ROOT
        for component_path in arguments.component:
            parts = component_path.split("/")
            if (
                len(parts) != 2
                or parts[0] not in COMPONENT_FAMILIES
                or not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]*", parts[1])
            ):
                parser.error("--component must use FAMILY/NAME with a known family")
            if not (root / parts[0] / parts[1]).is_dir():
                parser.error(f"--component directory does not exist: {component_path}")
    if arguments.list_components:
        root = arguments.components_root or COMPONENTS_ROOT
        family_filter = (
            tuple(dict.fromkeys(arguments.family)) if arguments.family else None
        )
        available = discover_components(root, families=family_filter)
        if not available:
            print("No Components discovered.", file=sys.stderr)
            raise SystemExit(1)
        paths = [component.relative_to(root).as_posix() for component in available]
        if arguments.format == "json":
            families = [
                family for family in COMPONENT_FAMILIES
                if family_filter is None or family in family_filter
            ]
            catalog: dict = {
                "components": paths,
                "count": len(paths),
                "scope": {"families": families},
            }
            if arguments.details:
                entries = []
                for component in available:
                    metadata_path = component / "metadata.yml"
                    entry = {
                        "path": component.relative_to(root).as_posix(),
                        "id": None,
                        "name": None,
                        "version": None,
                        "status": None,
                        "metadata_status": "missing",
                    }
                    if metadata_path.is_file():
                        try:
                            metadata = load_metadata(metadata_path)
                        except (OSError, yaml.YAMLError, ValueError):
                            entry["metadata_status"] = "invalid"
                        else:
                            entry["metadata_status"] = "loaded"
                            for field in ("id", "name", "version", "status"):
                                value = metadata.get(field)
                                entry[field] = value if isinstance(value, str) else None
                    entries.append(entry)
                catalog["details"] = entries
            print(json.dumps(catalog, indent=2))
        else:
            for path in paths:
                print(path)
        raise SystemExit(0)
    raise SystemExit(
        main(
            output_format=arguments.format,
            output_path=arguments.output,
            components_root=arguments.components_root,
            families=tuple(dict.fromkeys(arguments.family)) if arguments.family else None,
            component_paths=(
                tuple(dict.fromkeys(arguments.component)) if arguments.component else None
            ),
        )
    )