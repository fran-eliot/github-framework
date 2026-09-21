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

    for wrapper in ("component", "classification"):
        if wrapper in metadata:
            errors.append(
                f"{wrapper}: historical root wrapper is not allowed"
            )

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


WORKFLOW_MATERIALIZATION_MECHANISMS = {
    "Convention",
    "Configuration",
    "Community File",
    "Template",
}


def validate_workflow_materialization(
    metadata: dict[str, Any],
) -> list[str]:
    """Validate materialization for a Workflow Component."""
    errors: list[str] = []

    if metadata.get("family") != "Workflow":
        return errors

    if "materialization" not in metadata:
        return ["materialization: required field is missing"]

    materialization = metadata["materialization"]

    if not isinstance(materialization, dict):
        return ["materialization: expected a mapping"]

    if "primary" not in materialization:
        errors.append("materialization.primary: required field is missing")
    else:
        primary = materialization["primary"]

        if not isinstance(primary, list) or not primary:
            errors.append("materialization.primary: expected a non-empty list")
        else:
            seen: set[str] = set()

            for index, mechanism in enumerate(primary):
                path = f"materialization.primary[{index}]"

                if (
                    not isinstance(mechanism, str)
                    or mechanism not in WORKFLOW_MATERIALIZATION_MECHANISMS
                ):
                    errors.append(f"{path}: invalid mechanism")
                    continue

                if mechanism in seen:
                    errors.append(f"{path}: duplicate '{mechanism}'")
                else:
                    seen.add(mechanism)

    if "executable" not in materialization:
        errors.append("materialization.executable: required field is missing")
    elif not isinstance(materialization["executable"], bool):
        errors.append("materialization.executable: expected a boolean")

    return errors


def validate_workflow_artifacts(
    metadata: dict[str, Any],
) -> list[str]:
    """Validate the structure of Workflow artifact declarations."""
    errors: list[str] = []

    if metadata.get("family") != "Workflow":
        return errors

    if "artifacts" not in metadata:
        return ["artifacts: required field is missing"]

    artifacts = metadata["artifacts"]

    if not isinstance(artifacts, dict):
        return ["artifacts: expected a mapping"]

    if "specification" not in artifacts:
        errors.append("artifacts.specification: required field is missing")
    else:
        specification = artifacts["specification"]

        if not isinstance(specification, str) or not specification.strip():
            errors.append(
                "artifacts.specification: expected a non-empty path"
            )

    if "templates" in artifacts:
        templates = artifacts["templates"]

        if not isinstance(templates, list):
            errors.append("artifacts.templates: expected a list")
        else:
            seen: set[str] = set()

            for index, template in enumerate(templates):
                path = f"artifacts.templates[{index}]"

                if not isinstance(template, str) or not template.strip():
                    errors.append(f"{path}: expected a non-empty path")
                    continue

                if template in seen:
                    errors.append(f"{path}: duplicate '{template}'")
                else:
                    seen.add(template)

    return errors


def validate_workflow_artifact_files(
    metadata: dict[str, Any],
    component_dir: Path,
) -> list[str]:
    """Check that declared Workflow artifacts are local, existing files."""
    errors: list[str] = []

    if metadata.get("family") != "Workflow":
        return errors

    artifacts = metadata.get("artifacts")

    # Structural errors are reported by validate_workflow_artifacts.
    if not isinstance(artifacts, dict):
        return errors

    declared_paths: list[tuple[str, str]] = []

    specification = artifacts.get("specification")
    if isinstance(specification, str) and specification.strip():
        declared_paths.append(("artifacts.specification", specification))

    templates = artifacts.get("templates")
    if isinstance(templates, list):
        for index, template in enumerate(templates):
            if isinstance(template, str) and template.strip():
                declared_paths.append(
                    (f"artifacts.templates[{index}]", template)
                )

    root = component_dir.resolve()

    for property_name, declared_path in declared_paths:
        # Artifact paths use repository-style forward slashes.
        # Reject backslashes rather than interpreting them differently
        # on Windows and Unix.
        if "\\" in declared_path:
            errors.append(
                f"{property_name}: expected a forward-slash relative path"
            )
            continue

        relative_path = Path(declared_path)

        if (
            declared_path.startswith("/")
            or relative_path.is_absolute()
            or ":" in declared_path
        ):
            errors.append(
                f"{property_name}: expected a relative path"
            )
            continue

        resolved_path = (root / relative_path).resolve()

        if not resolved_path.is_relative_to(root):
            errors.append(
                f"{property_name}: path escapes the Component directory"
            )
            continue

        if not resolved_path.is_file():
            errors.append(
                f"{property_name}: file does not exist: '{declared_path}'"
            )

    return errors


WORKFLOW_SPECIALIZATIONS = {"Allowed", "Required"}


def validate_workflow_adoption(
    metadata: dict[str, Any],
) -> list[str]:
    """Validate adoption declarations for a Workflow Component."""
    errors: list[str] = []

    if metadata.get("family") != "Workflow":
        return errors

    if "adoption" not in metadata:
        return ["adoption: required field is missing"]

    adoption = metadata["adoption"]

    if not isinstance(adoption, dict):
        return ["adoption: expected a mapping"]

    if "specialization" not in adoption:
        errors.append("adoption.specialization: required field is missing")
    elif adoption["specialization"] not in WORKFLOW_SPECIALIZATIONS:
        errors.append(
            "adoption.specialization: expected 'Allowed' or 'Required'"
        )

    if "target" in adoption:
        target = adoption["target"]

        if not isinstance(target, str) or not target.strip():
            errors.append("adoption.target: expected a non-empty path")
        elif (
            target.startswith("/")
            or "\\" in target
            or ":" in target
            or any(part == ".." for part in target.split("/"))
        ):
            errors.append(
                "adoption.target: expected a relative repository path"
            )

    return errors


WORKFLOW_REFERENCE_IMPLEMENTATION_STATES = {
    "Pending",
    "Validated",
}

def validate_workflow_validation(
    metadata: dict[str, Any],
) -> list[str]:
    """Validate Workflow evidence declarations."""
    errors: list[str] = []

    if metadata.get("family") != "Workflow":
        return errors

    if "validation" not in metadata:
        return ["validation: required field is missing"]

    validation = metadata["validation"]

    if not isinstance(validation, dict):
        return ["validation: expected a mapping"]

    if "dogfooding" not in validation:
        errors.append("validation.dogfooding: required field is missing")
    elif not isinstance(validation["dogfooding"], bool):
        errors.append("validation.dogfooding: expected a boolean")

    if "reference_implementation" not in validation:
        errors.append(
            "validation.reference_implementation: required field is missing"
        )
    else:
        reference_implementation = validation["reference_implementation"]

        if (
            not isinstance(reference_implementation, str)
            or reference_implementation
            not in WORKFLOW_REFERENCE_IMPLEMENTATION_STATES
        ):
            errors.append(
                "validation.reference_implementation: "
                "expected 'Pending' or 'Validated'"
            )

    return errors
