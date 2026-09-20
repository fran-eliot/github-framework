
"""Integration tests for the Framework Validator CLI."""

import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from scripts.framework_validator import __main__ as validator_cli


VALID_METADATA = """\
schema_version: "1.0"
id: DOC-ARCHITECTURE
name: Architecture
family: Documentation
version: "0.1.0"
status: Experimental
priority: Recommended
description: Architecture documentation Component.
"""


class FrameworkValidatorCLITests(unittest.TestCase):
    """Exercise main() against isolated Component directories."""

    def run_validator(self, root: Path) -> tuple[int, str]:
        output = io.StringIO()

        with (
            patch.object(validator_cli, "COMPONENTS_ROOT", root),
            redirect_stdout(output),
        ):
            exit_code = validator_cli.main()

        return exit_code, output.getvalue()

    def create_component(self, root: Path) -> Path:
        component = root / "documentation" / "architecture"
        component.mkdir(parents=True)
        return component

    def test_valid_component(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA, encoding="utf-8"
            )

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 0)
            self.assertIn("Components discovered: 1", output)
            self.assertIn("Validation passed:", output)

    def test_empty_components_root(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("Components discovered: 0", output)
            self.assertIn("no Components discovered", output)
            self.assertIn("Validation failed:", output)

    def test_missing_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self.create_component(root)

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("missing metadata.yml", output)
            self.assertIn("Validation failed:", output)

    def test_invalid_yaml(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                "family: [unclosed", encoding="utf-8"
            )

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("unable to load metadata:", output)
            self.assertIn("metadata.yml", output)

    def test_invalid_common_core(self) -> None:
        with TemporaryDirectory() as directory:
            root = Path(directory)
            component = self.create_component(root)
            (component / "metadata.yml").write_text(
                VALID_METADATA.replace(
                    "status: Experimental",
                    "status: Unknown",
                ),
                encoding="utf-8",
            )

            exit_code, output = self.run_validator(root)

            self.assertEqual(exit_code, 1)
            self.assertIn("metadata.yml", output)
            self.assertIn("status:", output)
            self.assertIn("Validation failed:", output)
