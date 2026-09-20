"""Command-line entry point for the Framework Validator."""

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
)


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
COMPONENTS_ROOT = REPOSITORY_ROOT / "framework" / "components"


def main() -> int:
    """Discover Components and check that their metadata can be loaded."""
    print("GitHub Framework Validator")
    print()

    component_dirs = discover_components(COMPONENTS_ROOT)
    errors: list[str] = []

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

        print(f"  {component_id}: {component_dir.name}")

    errors.extend(validate_unique_ids(loaded_components))
    print()

    if errors:
        print(f"Validation failed: {len(errors)} error(s)")

        for error in errors:
            print(f"  ERROR: {error}")

        return 1

    print(
        "Discovery, metadata loading, Common Core, identity, "
        "uniqueness, maturity and dependencies validation passed."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())