"""Tests for Framework Component metadata validation."""

from typing import Any
import unittest
from pathlib import Path

from scripts.framework_validator.validation import (
    validate_common_core,
    validate_component_identity,
    validate_unique_ids,
)


def valid_metadata() -> dict:
    """Build a valid Common Core metadata example."""
    return {
        "schema_version": "1.0",
        "id": "README-TEST",
        "name": "Test Component",
        "family": "README",
        "version": "1.0.0",
        "status": "Stable",
        "priority": "Required",
        "description": "A test Component.",
    }


class CommonCoreValidationTests(unittest.TestCase):
    """Verify Common Core validation rules."""

    def test_valid_metadata(self) -> None:
        metadata = valid_metadata()

        self.assertEqual(validate_common_core(metadata), [])

    def test_missing_required_field(self) -> None:
        metadata = valid_metadata()
        del metadata["name"]

        errors = validate_common_core(metadata)

        self.assertEqual(
            errors,
            ["name: required field is missing"],
        )

    def test_invalid_version(self) -> None:
        metadata = valid_metadata()
        metadata["version"] = "invalid"

        errors = validate_common_core(metadata)

        self.assertEqual(
            errors,
            ["version: expected a MAJOR.MINOR.PATCH string"],
        )

    def test_invalid_status(self) -> None:
        metadata = valid_metadata()
        metadata["status"] = "Unknown"

        errors = validate_common_core(metadata)

        self.assertEqual(len(errors), 1)
        self.assertIn("status: expected one of", errors[0])

    def test_multiple_errors(self) -> None:
        metadata = valid_metadata()
        del metadata["name"]
        metadata["version"] = "invalid"
        metadata["status"] = "Unknown"

        errors = validate_common_core(metadata)

        self.assertEqual(len(errors), 3)

    def test_schema_version_must_be_string(self) -> None:
        metadata = valid_metadata()
        metadata["schema_version"] = 1.0

        errors = validate_common_core(metadata)

        self.assertEqual(
            errors,
            ["schema_version: expected string '1.0'"],
        )

    def test_invalid_family(self) -> None:
        metadata = valid_metadata()
        metadata["family"] = "readme"

        errors = validate_common_core(metadata)

        self.assertEqual(len(errors), 1)
        self.assertIn("family: expected one of", errors[0])

    
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


class ComponentIdentityTests(unittest.TestCase):
    """Verify canonical Component identities."""

    def test_valid_readme_identity(self) -> None:
        metadata = valid_metadata()

        errors = validate_component_identity(
            metadata, "readme", "test"
        )

        self.assertEqual(errors, [])

    def test_valid_workflow_identity(self) -> None:
        metadata = valid_metadata()
        metadata["id"] = "WCL-CODE-REVIEW"
        metadata["family"] = "Workflow"

        errors = validate_component_identity(
            metadata, "workflow", "code-review"
        )

        self.assertEqual(errors, [])

    def test_incorrect_id(self) -> None:
        metadata = valid_metadata()
        metadata["id"] = "README-OTHER"

        errors = validate_component_identity(
            metadata, "readme", "test"
        )

        self.assertEqual(len(errors), 1)
        self.assertIn("id: expected 'README-TEST'", errors[0])

    def test_incorrect_family(self) -> None:
        metadata = valid_metadata()
        metadata["family"] = "Documentation"

        errors = validate_component_identity(
            metadata, "readme", "test"
        )

        self.assertEqual(len(errors), 1)
        self.assertIn("family: expected 'README'", errors[0])



class UniqueIdValidationTests(unittest.TestCase):
    """Verify uniqueness of Component IDs."""

    def test_unique_ids(self) -> None:
        first = valid_metadata()
        second = valid_metadata()
        second["id"] = "README-OTHER"

        components = [
            (Path("readme/test/metadata.yml"), first),
            (Path("readme/other/metadata.yml"), second),
        ]

        self.assertEqual(validate_unique_ids(components), [])

    def test_duplicate_id(self) -> None:
        first = valid_metadata()
        second = valid_metadata()

        components = [
            (Path("readme/test/metadata.yml"), first),
            (Path("readme/other/metadata.yml"), second),
        ]

        errors = validate_unique_ids(components)

        self.assertEqual(len(errors), 1)
        self.assertIn("duplicate 'README-TEST'", errors[0])
        self.assertIn(
            Path("readme/test/metadata.yml").as_posix(),
            errors[0].replace("\\", "/"),
        )

    def test_missing_id_is_handled_by_common_core(self) -> None:
        metadata = valid_metadata()
        del metadata["id"]

        components = [
            (Path("readme/test/metadata.yml"), metadata),
        ]

        self.assertEqual(validate_unique_ids(components), [])


if __name__ == "__main__":
    unittest.main()