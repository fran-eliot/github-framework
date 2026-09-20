"""Tests for Framework Component metadata validation."""

from typing import Any
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

from scripts.framework_validator.validation import (
    validate_common_core,
    validate_component_identity,
    validate_dependencies,
    validate_unique_ids,
    validate_maturity,
    validate_optional_common_fields,
    validate_workflow_materialization,
    validate_workflow_artifacts,
    validate_workflow_artifact_files,
    validate_workflow_adoption,
    validate_workflow_validation,
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

    def test_historical_component_wrapper_is_rejected(self) -> None:
        metadata = valid_metadata()
        metadata["component"] = {"id": "README-EXAMPLE"}

        errors = validate_common_core(metadata)

        self.assertIn(
            "component: historical root wrapper is not allowed",
            errors,
        )

    def test_historical_classification_wrapper_is_rejected(self) -> None:
        metadata = valid_metadata()
        metadata["classification"] = {"family": "README"}

        errors = validate_common_core(metadata)

        self.assertIn(
            "classification: historical root wrapper is not allowed",
            errors,
        )

    
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



class WorkflowMaterializationTests(unittest.TestCase):
    """Verify Workflow materialization declarations."""

    def workflow_metadata(self) -> dict:
        metadata = valid_metadata()
        metadata["family"] = "Workflow"
        metadata["materialization"] = {
            "primary": ["Convention"],
            "executable": False,
        }
        return metadata

    def test_valid_convention(self) -> None:
        self.assertEqual(
            validate_workflow_materialization(self.workflow_metadata()),
            [],
        )

    def test_valid_multiple_mechanisms(self) -> None:
        metadata = self.workflow_metadata()
        metadata["materialization"]["primary"] = [
            "Convention",
            "Configuration",
        ]

        self.assertEqual(validate_workflow_materialization(metadata), [])

    def test_non_workflow_is_ignored(self) -> None:
        metadata = valid_metadata()
        metadata["materialization"] = "not applicable"

        self.assertEqual(validate_workflow_materialization(metadata), [])

    def test_missing_materialization(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["materialization"]

        self.assertEqual(
            validate_workflow_materialization(metadata),
            ["materialization: required field is missing"],
        )

    def test_invalid_materialization_type(self) -> None:
        metadata = self.workflow_metadata()
        metadata["materialization"] = []

        self.assertEqual(
            validate_workflow_materialization(metadata),
            ["materialization: expected a mapping"],
        )

    def test_missing_primary(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["materialization"]["primary"]

        self.assertEqual(
            validate_workflow_materialization(metadata),
            ["materialization.primary: required field is missing"],
        )

    def test_empty_primary(self) -> None:
        metadata = self.workflow_metadata()
        metadata["materialization"]["primary"] = []

        self.assertEqual(
            validate_workflow_materialization(metadata),
            ["materialization.primary: expected a non-empty list"],
        )

    def test_invalid_mechanism(self) -> None:
        metadata = self.workflow_metadata()
        metadata["materialization"]["primary"] = ["Unknown"]

        self.assertEqual(
            validate_workflow_materialization(metadata),
            ["materialization.primary[0]: invalid mechanism"],
        )

    def test_duplicate_mechanism(self) -> None:
        metadata = self.workflow_metadata()
        metadata["materialization"]["primary"] = [
            "Convention",
            "Convention",
        ]

        self.assertEqual(
            validate_workflow_materialization(metadata),
            ["materialization.primary[1]: duplicate 'Convention'"],
        )

    def test_missing_executable(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["materialization"]["executable"]

        self.assertEqual(
            validate_workflow_materialization(metadata),
            ["materialization.executable: required field is missing"],
        )

    def test_invalid_executable_type(self) -> None:
        metadata = self.workflow_metadata()
        metadata["materialization"]["executable"] = "false"

        self.assertEqual(
            validate_workflow_materialization(metadata),
            ["materialization.executable: expected a boolean"],
        )

    def test_template_materialization_is_allowed(self) -> None:
        metadata = self.workflow_metadata()
        metadata["materialization"]["primary"] = ["Template"]

        self.assertEqual(validate_workflow_materialization(metadata), [])



class WorkflowArtifactsTests(unittest.TestCase):
    """Verify Workflow artifact declarations."""

    def workflow_metadata(self) -> dict:
        metadata = valid_metadata()
        metadata["family"] = "Workflow"
        metadata["artifacts"] = {
            "specification": "README.md",
            "templates": ["templates/CODEOWNERS"],
        }
        return metadata

    def test_valid_artifacts(self) -> None:
        self.assertEqual(
            validate_workflow_artifacts(self.workflow_metadata()),
            [],
        )

    def test_templates_are_optional(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["artifacts"]["templates"]

        self.assertEqual(validate_workflow_artifacts(metadata), [])

    def test_empty_templates_are_allowed(self) -> None:
        metadata = self.workflow_metadata()
        metadata["artifacts"]["templates"] = []

        self.assertEqual(validate_workflow_artifacts(metadata), [])

    def test_non_workflow_is_ignored(self) -> None:
        metadata = valid_metadata()
        metadata["artifacts"] = "not applicable"

        self.assertEqual(validate_workflow_artifacts(metadata), [])

    def test_missing_artifacts(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["artifacts"]

        self.assertEqual(
            validate_workflow_artifacts(metadata),
            ["artifacts: required field is missing"],
        )

    def test_invalid_artifacts_type(self) -> None:
        metadata = self.workflow_metadata()
        metadata["artifacts"] = []

        self.assertEqual(
            validate_workflow_artifacts(metadata),
            ["artifacts: expected a mapping"],
        )

    def test_missing_specification(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["artifacts"]["specification"]

        self.assertEqual(
            validate_workflow_artifacts(metadata),
            ["artifacts.specification: required field is missing"],
        )

    def test_empty_specification(self) -> None:
        metadata = self.workflow_metadata()
        metadata["artifacts"]["specification"] = " "

        self.assertEqual(
            validate_workflow_artifacts(metadata),
            ["artifacts.specification: expected a non-empty path"],
        )

    def test_invalid_templates_type(self) -> None:
        metadata = self.workflow_metadata()
        metadata["artifacts"]["templates"] = "templates/CODEOWNERS"

        self.assertEqual(
            validate_workflow_artifacts(metadata),
            ["artifacts.templates: expected a list"],
        )

    def test_invalid_template_entry(self) -> None:
        metadata = self.workflow_metadata()
        metadata["artifacts"]["templates"] = [""]

        self.assertEqual(
            validate_workflow_artifacts(metadata),
            ["artifacts.templates[0]: expected a non-empty path"],
        )

    def test_duplicate_template(self) -> None:
        metadata = self.workflow_metadata()
        metadata["artifacts"]["templates"] = [
            "templates/CODEOWNERS",
            "templates/CODEOWNERS",
        ]

        self.assertEqual(
            validate_workflow_artifacts(metadata),
            [
                "artifacts.templates[1]: duplicate "
                "'templates/CODEOWNERS'"
            ],
        )



class WorkflowArtifactFilesTests(unittest.TestCase):
    """Verify local Workflow artifact files and path containment."""

    def workflow_metadata(self) -> dict:
        metadata = valid_metadata()
        metadata["family"] = "Workflow"
        metadata["artifacts"] = {
            "specification": "README.md",
            "templates": ["templates/CODEOWNERS"],
        }
        return metadata

    def test_existing_files(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("Specification", encoding="utf-8")
            (root / "templates").mkdir()
            (root / "templates" / "CODEOWNERS").write_text(
                "* @maintainer", encoding="utf-8"
            )

            self.assertEqual(
                validate_workflow_artifact_files(
                    self.workflow_metadata(), root
                ),
                [],
            )

    def test_missing_specification(self) -> None:
        with TemporaryDirectory() as directory:
            metadata = self.workflow_metadata()
            del metadata["artifacts"]["templates"]

            self.assertEqual(
                validate_workflow_artifact_files(
                    metadata, Path(directory)
                ),
                [
                    "artifacts.specification: "
                    "file does not exist: 'README.md'"
                ],
            )

    def test_missing_template(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("Specification", encoding="utf-8")

            self.assertEqual(
                validate_workflow_artifact_files(
                    self.workflow_metadata(), root
                ),
                [
                    "artifacts.templates[0]: "
                    "file does not exist: 'templates/CODEOWNERS'"
                ],
            )

    def test_parent_directory_escape(self) -> None:
        with TemporaryDirectory() as directory:
            metadata = self.workflow_metadata()
            metadata["artifacts"] = {
                "specification": "../README.md",
            }

            self.assertEqual(
                validate_workflow_artifact_files(
                    metadata, Path(directory)
                ),
                [
                    "artifacts.specification: "
                    "path escapes the Component directory"
                ],
            )

    def test_absolute_path(self) -> None:
        with TemporaryDirectory() as directory:
            metadata = self.workflow_metadata()
            metadata["artifacts"] = {
                "specification": "/tmp/README.md",
            }

            self.assertEqual(
                validate_workflow_artifact_files(
                    metadata, Path(directory)
                ),
                [
                    "artifacts.specification: expected a relative path"
                ],
            )

    def test_windows_style_path(self) -> None:
        with TemporaryDirectory() as directory:
            metadata = self.workflow_metadata()
            metadata["artifacts"] = {
                "specification": r"templates\CODEOWNERS",
            }

            self.assertEqual(
                validate_workflow_artifact_files(
                    metadata, Path(directory)
                ),
                [
                    "artifacts.specification: "
                    "expected a forward-slash relative path"
                ],
            )

    def test_directory_is_not_a_file(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").mkdir()

            metadata = self.workflow_metadata()
            del metadata["artifacts"]["templates"]

            self.assertEqual(
                validate_workflow_artifact_files(metadata, root),
                [
                    "artifacts.specification: "
                    "file does not exist: 'README.md'"
                ],
            )

    def test_non_workflow_is_ignored(self) -> None:
        with TemporaryDirectory() as directory:
            metadata = valid_metadata()
            metadata["artifacts"] = {
                "specification": "missing.md",
            }

            self.assertEqual(
                validate_workflow_artifact_files(
                    metadata, Path(directory)
                ),
                [],
            )



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



class WorkflowAdoptionTests(unittest.TestCase):
    """Verify Workflow adoption declarations."""

    def workflow_metadata(self) -> dict:
        metadata = valid_metadata()
        metadata["family"] = "Workflow"
        metadata["adoption"] = {
            "target": ".github/ISSUE_TEMPLATE/",
            "specialization": "Allowed",
        }
        return metadata

    def test_valid_adoption(self) -> None:
        self.assertEqual(
            validate_workflow_adoption(self.workflow_metadata()),
            [],
        )

    def test_target_is_optional(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["adoption"]["target"]

        self.assertEqual(validate_workflow_adoption(metadata), [])

    def test_required_specialization(self) -> None:
        metadata = self.workflow_metadata()
        metadata["adoption"]["specialization"] = "Required"

        self.assertEqual(validate_workflow_adoption(metadata), [])

    def test_non_workflow_is_ignored(self) -> None:
        metadata = valid_metadata()
        metadata["adoption"] = "not applicable"

        self.assertEqual(validate_workflow_adoption(metadata), [])

    def test_missing_adoption(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["adoption"]

        self.assertEqual(
            validate_workflow_adoption(metadata),
            ["adoption: required field is missing"],
        )

    def test_invalid_adoption_type(self) -> None:
        metadata = self.workflow_metadata()
        metadata["adoption"] = []

        self.assertEqual(
            validate_workflow_adoption(metadata),
            ["adoption: expected a mapping"],
        )

    def test_missing_specialization(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["adoption"]["specialization"]

        self.assertEqual(
            validate_workflow_adoption(metadata),
            ["adoption.specialization: required field is missing"],
        )

    def test_invalid_specialization(self) -> None:
        metadata = self.workflow_metadata()
        metadata["adoption"]["specialization"] = "Custom"

        self.assertEqual(
            validate_workflow_adoption(metadata),
            [
                "adoption.specialization: "
                "expected 'Allowed' or 'Required'"
            ],
        )

    def test_empty_target(self) -> None:
        metadata = self.workflow_metadata()
        metadata["adoption"]["target"] = " "

        self.assertEqual(
            validate_workflow_adoption(metadata),
            ["adoption.target: expected a non-empty path"],
        )

    def test_absolute_target(self) -> None:
        metadata = self.workflow_metadata()
        metadata["adoption"]["target"] = "/etc/config"

        self.assertEqual(
            validate_workflow_adoption(metadata),
            [
                "adoption.target: "
                "expected a relative repository path"
            ],
        )

    def test_parent_directory_target(self) -> None:
        metadata = self.workflow_metadata()
        metadata["adoption"]["target"] = "../outside"

        self.assertEqual(
            validate_workflow_adoption(metadata),
            [
                "adoption.target: "
                "expected a relative repository path"
            ],
        )

    def test_windows_style_target(self) -> None:
        metadata = self.workflow_metadata()
        metadata["adoption"]["target"] = r".github\CODEOWNERS"

        self.assertEqual(
            validate_workflow_adoption(metadata),
            [
                "adoption.target: "
                "expected a relative repository path"
            ],
        )



class WorkflowValidationTests(unittest.TestCase):
    """Verify Workflow validation evidence declarations."""

    def workflow_metadata(self) -> dict:
        metadata = valid_metadata()
        metadata["family"] = "Workflow"
        metadata["validation"] = {
            "dogfooding": True,
            "reference_implementation": "Validated",
        }
        return metadata

    def test_valid_validation(self) -> None:
        self.assertEqual(
            validate_workflow_validation(self.workflow_metadata()),
            [],
        )

    def test_false_dogfooding_is_allowed(self) -> None:
        metadata = self.workflow_metadata()
        metadata["validation"]["dogfooding"] = False

        self.assertEqual(validate_workflow_validation(metadata), [])

    def test_other_nonempty_reference_state_is_allowed(self) -> None:
        metadata = self.workflow_metadata()
        metadata["validation"]["reference_implementation"] = "Pending"

        self.assertEqual(validate_workflow_validation(metadata), [])

    def test_non_workflow_is_ignored(self) -> None:
        metadata = valid_metadata()
        metadata["validation"] = "not applicable"

        self.assertEqual(validate_workflow_validation(metadata), [])

    def test_missing_validation(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["validation"]

        self.assertEqual(
            validate_workflow_validation(metadata),
            ["validation: required field is missing"],
        )

    def test_invalid_validation_type(self) -> None:
        metadata = self.workflow_metadata()
        metadata["validation"] = []

        self.assertEqual(
            validate_workflow_validation(metadata),
            ["validation: expected a mapping"],
        )

    def test_missing_dogfooding(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["validation"]["dogfooding"]

        self.assertEqual(
            validate_workflow_validation(metadata),
            ["validation.dogfooding: required field is missing"],
        )

    def test_invalid_dogfooding_type(self) -> None:
        metadata = self.workflow_metadata()
        metadata["validation"]["dogfooding"] = "true"

        self.assertEqual(
            validate_workflow_validation(metadata),
            ["validation.dogfooding: expected a boolean"],
        )

    def test_missing_reference_implementation(self) -> None:
        metadata = self.workflow_metadata()
        del metadata["validation"]["reference_implementation"]

        self.assertEqual(
            validate_workflow_validation(metadata),
            [
                "validation.reference_implementation: "
                "required field is missing"
            ],
        )

    def test_empty_reference_implementation(self) -> None:
        metadata = self.workflow_metadata()
        metadata["validation"]["reference_implementation"] = " "

        self.assertEqual(
            validate_workflow_validation(metadata),
            [
                "validation.reference_implementation: "
                "expected 'Pending' or 'Validated'"
            ],
        )

    def test_unknown_reference_implementation(self) -> None:
        metadata = self.workflow_metadata()
        metadata["validation"]["reference_implementation"] = "Unknown"

        errors = validate_workflow_validation(metadata)

        self.assertTrue(
            any(
                "validation.reference_implementation:" in error
                for error in errors
            )
        )

    def test_multiple_validation_errors(self) -> None:
        metadata = self.workflow_metadata()
        metadata["validation"] = {
            "dogfooding": "yes",
            "reference_implementation": "",
        }

        self.assertEqual(
            validate_workflow_validation(metadata),
            [
                "validation.dogfooding: expected a boolean",
                "validation.reference_implementation: "
                "expected 'Pending' or 'Validated'",
            ],
        )


if __name__ == "__main__":
    unittest.main()