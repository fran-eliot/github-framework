"""Validate the Common Core of Framework Component metadata."""

import re
from pathlib import Path
from typing import Any

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


MATURITY_LEVELS = {"L1", "L2", "L3", "L4"}
MATURITY_FIELDS = {"minimum", "recommended", "supported"}


def validate_maturity(metadata: dict[str, Any]) -> list[str]:
    """Validate the optional root-level maturity declaration."""
    errors: list[str] = []

    if "maturity" not in metadata:
        return errors

    maturity = metadata["maturity"]

    if isinstance(maturity, str):
        if maturity not in MATURITY_LEVELS:
            errors.append(
                "maturity: expected one of [L1, L2, L3, L4]"
            )
        return errors

    if not isinstance(maturity, dict):
        return ["maturity: expected a level or mapping"]

    for field in maturity:
        if field not in MATURITY_FIELDS:
            errors.append(f"maturity.{field}: unknown property")

    for field in ("minimum", "recommended"):
        if field not in maturity:
            continue

        if (
            not isinstance(maturity[field], str)
            or maturity[field] not in MATURITY_LEVELS
        ):
            errors.append(
                f"maturity.{field}: expected one of [L1, L2, L3, L4]"
            )

    if "supported" in maturity:
        supported = maturity["supported"]

        if not isinstance(supported, list) or not supported:
            errors.append(
                "maturity.supported: expected a non-empty list"
            )
        else:
            seen: set[str] = set()

            for index, level in enumerate(supported):
                if not isinstance(level, str) or level not in MATURITY_LEVELS:
                    errors.append(
                        f"maturity.supported[{index}]: invalid level"
                    )
                    continue

                if level in seen:
                    errors.append(
                        f"maturity.supported[{index}]: duplicate '{level}'"
                    )

                seen.add(level)

            for field in ("minimum", "recommended"):
                level = maturity.get(field)

                if (
                    isinstance(level, str)
                    and level in MATURITY_LEVELS
                    and level not in seen
                ):
                    errors.append(
                        f"maturity.{field}: '{level}' is not in supported"
                    )

    return errors



DEPENDENCY_CATEGORIES = ("required", "recommended", "optional")
DEPENDENCY_ID = re.compile(r"^(?:README|DOC|WCL|VCL)-[A-Z0-9]+(?:-[A-Z0-9]+)*$")


def validate_dependencies(metadata: dict[str, Any]) -> list[str]:
    """Validate the optional root-level Component dependencies."""
    errors: list[str] = []

    if "dependencies" not in metadata:
        return errors

    dependencies = metadata["dependencies"]

    if isinstance(dependencies, list):
        groups = [("dependencies", dependencies)]
    elif isinstance(dependencies, dict):
        groups = []

        for category in dependencies:
            if category not in DEPENDENCY_CATEGORIES:
                errors.append(
                    f"dependencies.{category}: unknown category"
                )

        for category in DEPENDENCY_CATEGORIES:
            if category not in dependencies:
                continue

            value = dependencies[category]

            if not isinstance(value, list):
                errors.append(
                    f"dependencies.{category}: expected a list"
                )
                continue

            groups.append((f"dependencies.{category}", value))
    else:
        return ["dependencies: expected a list or classified mapping"]

    seen: dict[str, str] = {}

    for group_path, entries in groups:
        for index, entry in enumerate(entries):
            entry_path = f"{group_path}[{index}]"

            if isinstance(entry, str):
                dependency_id = entry

            elif isinstance(entry, dict):
                unknown_fields = set(entry) - {"id", "minimum_version"}

                for field in sorted(unknown_fields):
                    errors.append(
                        f"{entry_path}.{field}: unknown property"
                    )

                if "id" not in entry:
                    errors.append(
                        f"{entry_path}.id: required field is missing"
                    )
                    continue

                dependency_id = entry["id"]

                if "minimum_version" in entry:
                    minimum_version = entry["minimum_version"]

                    if (
                        not isinstance(minimum_version, str)
                        or SEMANTIC_VERSION.fullmatch(minimum_version) is None
                    ):
                        errors.append(
                            f"{entry_path}.minimum_version: "
                            "expected a MAJOR.MINOR.PATCH string"
                        )

            else:
                errors.append(
                    f"{entry_path}: expected an ID or dependency mapping"
                )
                continue

            if (
                not isinstance(dependency_id, str)
                or DEPENDENCY_ID.fullmatch(dependency_id) is None
            ):
                errors.append(
                    f"{entry_path}.id: invalid Component ID"
                )
                continue

            if dependency_id in seen:
                errors.append(
                    f"{entry_path}.id: duplicate '{dependency_id}'; "
                    f"first declared at {seen[dependency_id]}"
                )
            else:
                seen[dependency_id] = entry_path

    return errors



def validate_optional_common_fields(metadata: dict[str, Any]) -> list[str]:
    """Validate optional Common Core owner and audience fields."""
    errors: list[str] = []

    if "owner" in metadata:
        owner = metadata["owner"]

        if not isinstance(owner, str) or not owner.strip():
            errors.append("owner: expected a non-empty string")

    if "audience" in metadata:
        audience = metadata["audience"]

        if not isinstance(audience, list) or not audience:
            errors.append("audience: expected a non-empty list")
        else:
            seen: set[str] = set()

            for index, member in enumerate(audience):
                if not isinstance(member, str) or not member.strip():
                    errors.append(
                        f"audience[{index}]: expected a non-empty string"
                    )
                    continue

                if member in seen:
                    errors.append(
                        f"audience[{index}]: duplicate '{member}'"
                    )
                else:
                    seen.add(member)

    return errors