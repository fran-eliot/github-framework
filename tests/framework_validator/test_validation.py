"""Tests for Framework Component metadata validation."""

from typing import Any
import unittest
from pathlib import Path

from scripts.framework_validator.validation import (
    validate_common_core,
    validate_component_identity,
    validate_dependencies,
    validate_unique_ids,
    validate_maturity,
    validate_optional_common_fields,
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



class MaturityValidationTests(unittest.TestCase):
    """Verify optional Component maturity declarations."""

    def test_absent_maturity(self) -> None:
        self.assertEqual(validate_maturity(valid_metadata()), [])

    def test_valid_scalar_maturity(self) -> None:
        metadata = valid_metadata()
        metadata["maturity"] = "L2"

        self.assertEqual(validate_maturity(metadata), [])

    def test_invalid_scalar_maturity(self) -> None:
        metadata = valid_metadata()
        metadata["maturity"] = "L5"

        self.assertEqual(
            validate_maturity(metadata),
            ["maturity: expected one of [L1, L2, L3, L4]"],
        )

    def test_valid_partial_mapping(self) -> None:
        metadata = valid_metadata()
        metadata["maturity"] = {"minimum": "L2"}

        self.assertEqual(validate_maturity(metadata), [])

    def test_valid_mapping_with_supported(self) -> None:
        metadata = valid_metadata()
        metadata["maturity"] = {
            "minimum": "L1",
            "recommended": "L2",
            "supported": ["L1", "L2", "L3", "L4"],
        }

        self.assertEqual(validate_maturity(metadata), [])

    def test_invalid_minimum_type(self) -> None:
        metadata = valid_metadata()
        metadata["maturity"] = {"minimum": ["L1"]}

        errors = validate_maturity(metadata)

        self.assertEqual(
            errors,
            ["maturity.minimum: expected one of [L1, L2, L3, L4]"],
        )

    def test_duplicate_supported_level(self) -> None:
        metadata = valid_metadata()
        metadata["maturity"] = {
            "supported": ["L1", "L1"],
        }

        errors = validate_maturity(metadata)

        self.assertEqual(
            errors,
            ["maturity.supported[1]: duplicate 'L1'"],
        )

    def test_minimum_not_supported(self) -> None:
        metadata = valid_metadata()
        metadata["maturity"] = {
            "minimum": "L1",
            "supported": ["L2", "L3"],
        }

        errors = validate_maturity(metadata)

        self.assertEqual(
            errors,
            ["maturity.minimum: 'L1' is not in supported"],
        )

    def test_invalid_supported_type(self) -> None:
        metadata = valid_metadata()
        metadata["maturity"] = {"supported": "L2"}

        self.assertEqual(
            validate_maturity(metadata),
            ["maturity.supported: expected a non-empty list"],
        )

    def test_nested_input_maturity_is_not_root_maturity(self) -> None:
        metadata = valid_metadata()
        metadata["inputs"] = {
            "maturity": {
                "type": "enum",
                "allowed": ["L1", "L2", "L3", "L4"],
            }
        }

        self.assertEqual(validate_maturity(metadata), [])



class DependencyValidationTests(unittest.TestCase):
    """Verify simple and classified Component dependencies."""

    def test_absent_dependencies(self) -> None:
        self.assertEqual(validate_dependencies(valid_metadata()), [])

    def test_empty_dependencies(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = []

        self.assertEqual(validate_dependencies(metadata), [])

    def test_valid_simple_list(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = [
            "README-HERO",
            "DOC-ARCHITECTURE",
            "VCL-BANNER",
        ]

        self.assertEqual(validate_dependencies(metadata), [])

    def test_valid_classified_dependencies(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = {
            "required": ["VCL-HERO"],
            "recommended": [
                {"id": "README-OVERVIEW", "minimum_version": "1.0.0"}
            ],
            "optional": [],
        }

        self.assertEqual(validate_dependencies(metadata), [])

    def test_invalid_dependencies_type(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = "README-HERO"

        self.assertEqual(
            validate_dependencies(metadata),
            ["dependencies: expected a list or classified mapping"],
        )

    def test_invalid_category(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = {"mandatory": ["README-HERO"]}

        self.assertEqual(
            validate_dependencies(metadata),
            ["dependencies.mandatory: unknown category"],
        )

    def test_invalid_category_value(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = {"required": "README-HERO"}

        self.assertEqual(
            validate_dependencies(metadata),
            ["dependencies.required: expected a list"],
        )

    def test_invalid_dependency_id(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = ["readme-hero"]

        self.assertEqual(
            validate_dependencies(metadata),
            ["dependencies[0].id: invalid Component ID"],
        )

    def test_missing_dependency_id(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = [{"minimum_version": "1.0.0"}]

        self.assertEqual(
            validate_dependencies(metadata),
            ["dependencies[0].id: required field is missing"],
        )

    def test_invalid_minimum_version(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = [
            {"id": "README-HERO", "minimum_version": "1.0"}
        ]

        self.assertEqual(
            validate_dependencies(metadata),
            [
                "dependencies[0].minimum_version: "
                "expected a MAJOR.MINOR.PATCH string"
            ],
        )

    def test_duplicate_across_categories(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = {
            "required": ["README-HERO"],
            "optional": ["README-HERO"],
        }

        self.assertEqual(
            validate_dependencies(metadata),
            [
                "dependencies.optional[0].id: duplicate 'README-HERO'; "
                "first declared at dependencies.required[0]"
            ],
        )

    def test_invalid_entry_type(self) -> None:
        metadata = valid_metadata()
        metadata["dependencies"] = [42]

        self.assertEqual(
            validate_dependencies(metadata),
            ["dependencies[0]: expected an ID or dependency mapping"],
        )



class OptionalCommonFieldsTests(unittest.TestCase):
    """Verify optional owner and audience declarations."""

    def test_absent_optional_fields(self) -> None:
        self.assertEqual(
            validate_optional_common_fields(valid_metadata()),
            [],
        )

    def test_valid_owner(self) -> None:
        metadata = valid_metadata()
        metadata["owner"] = "Framework Maintainers"

        self.assertEqual(validate_optional_common_fields(metadata), [])

    def test_invalid_owner(self) -> None:
        metadata = valid_metadata()
        metadata["owner"] = "   "

        self.assertEqual(
            validate_optional_common_fields(metadata),
            ["owner: expected a non-empty string"],
        )

    def test_valid_audience(self) -> None:
        metadata = valid_metadata()
        metadata["audience"] = ["Developer", "Maintainer"]

        self.assertEqual(validate_optional_common_fields(metadata), [])

    def test_custom_audience_is_allowed(self) -> None:
        metadata = valid_metadata()
        metadata["audience"] = ["Security Engineer"]

        self.assertEqual(validate_optional_common_fields(metadata), [])

    def test_empty_audience(self) -> None:
        metadata = valid_metadata()
        metadata["audience"] = []

        self.assertEqual(
            validate_optional_common_fields(metadata),
            ["audience: expected a non-empty list"],
        )

    def test_invalid_audience_type(self) -> None:
        metadata = valid_metadata()
        metadata["audience"] = "Developer"

        self.assertEqual(
            validate_optional_common_fields(metadata),
            ["audience: expected a non-empty list"],
        )

    def test_empty_audience_member(self) -> None:
        metadata = valid_metadata()
        metadata["audience"] = ["Developer", " "]

        self.assertEqual(
            validate_optional_common_fields(metadata),
            ["audience[1]: expected a non-empty string"],
        )

    def test_duplicate_audience_member(self) -> None:
        metadata = valid_metadata()
        metadata["audience"] = ["Developer", "Developer"]

        self.assertEqual(
            validate_optional_common_fields(metadata),
            ["audience[1]: duplicate 'Developer'"],
        )


if __name__ == "__main__":
    unittest.main()