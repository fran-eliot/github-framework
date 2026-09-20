"""Validate the Common Core of Framework Component metadata."""

import re
from typing import Any
from pathlib import Path

REQUIRED_FIELDS = (
    "schema_version",
    "id",
    "name",
    "family",
    "version",
    "status",
    "priority",
    "description",
)

FAMILIES = {"README", "Documentation", "Workflow"}
STATUSES = {"Draft", "Experimental", "Stable", "Deprecated", "Retired"}
PRIORITIES = {"Required", "Recommended", "Optional"}

SEMANTIC_VERSION = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")


def validate_common_core(metadata: dict[str, Any]) -> list[str]:
    """Return Common Core validation errors for one Component."""
    errors: list[str] = []

    missing_fields = set(REQUIRED_FIELDS) - metadata.keys()

    for field in REQUIRED_FIELDS:
        if field in missing_fields:
            errors.append(f"{field}: required field is missing")

    if (
        "schema_version" not in missing_fields
        and metadata["schema_version"] != "1.0"
    ):
        errors.append("schema_version: expected string '1.0'")

    for field in ("id", "name", "description"):
        if field in missing_fields:
            continue

        value = metadata[field]

        if not isinstance(value, str) or not value.strip():
            errors.append(f"{field}: expected a non-empty string")

    if "version" not in missing_fields:
        version = metadata["version"]

        if (
            not isinstance(version, str)
            or SEMANTIC_VERSION.fullmatch(version) is None
        ):
            errors.append("version: expected a MAJOR.MINOR.PATCH string")

    for field, allowed_values in (
        ("family", FAMILIES),
        ("status", STATUSES),
        ("priority", PRIORITIES),
    ):
        if field in missing_fields:
            continue

        value = metadata[field]

        if not isinstance(value, str) or value not in allowed_values:
            allowed = ", ".join(sorted(allowed_values))
            errors.append(f"{field}: expected one of [{allowed}]")

    return errors


FAMILY_PREFIXES = {
    "README": "README",
    "Documentation": "DOC",
    "Workflow": "WCL",
}


def validate_component_identity(
    metadata: dict[str, Any],
    family_directory: str,
    component_directory: str,
) -> list[str]:
    """Validate the canonical ID and its physical family."""
    errors: list[str] = []

    directory_families = {
        "readme": "README",
        "documentation": "Documentation",
        "workflow": "Workflow",
    }

    expected_family = directory_families.get(family_directory)

    if expected_family is None:
        errors.append(
            f"family: unrecognized directory '{family_directory}'"
        )
        return errors

    family = metadata.get("family")

    if family != expected_family:
        errors.append(
            f"family: expected '{expected_family}' for directory "
            f"'{family_directory}'"
        )

    expected_id = (
        f"{FAMILY_PREFIXES[expected_family]}-"
        f"{component_directory.upper()}"
    )

    component_id = metadata.get("id")

    if component_id != expected_id:
        errors.append(
            f"id: expected '{expected_id}' for directory "
            f"'{family_directory}/{component_directory}'"
        )

    return errors



def validate_unique_ids(
    components: list[tuple[Path, dict[str, Any]]],
) -> list[str]:
    """Detect duplicate Component IDs across metadata files."""
    errors: list[str] = []
    first_occurrence: dict[str, Path] = {}

    for metadata_path, metadata in components:
        component_id = metadata.get("id")

        # Missing or invalid IDs are handled by Common Core validation.
        if not isinstance(component_id, str) or not component_id.strip():
            continue

        if component_id in first_occurrence:
            errors.append(
                f"{metadata_path}: id: duplicate '{component_id}'; "
                f"first declared in {first_occurrence[component_id]}"
            )
        else:
            first_occurrence[component_id] = metadata_path

    return errors