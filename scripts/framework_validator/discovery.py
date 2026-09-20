"""Discover implemented Framework Components and load their metadata."""

from pathlib import Path
from typing import Any

import yaml


COMPONENT_FAMILIES = ("readme", "documentation", "workflow")


def discover_components(components_root: Path) -> list[Path]:
    """Return the directories of implemented Components."""
    component_dirs: list[Path] = []

    for family in COMPONENT_FAMILIES:
        family_dir = components_root / family

        if not family_dir.is_dir():
            continue

        for component_dir in family_dir.iterdir():
            if component_dir.is_dir():
                component_dirs.append(component_dir)

    return sorted(component_dirs)


def load_metadata(metadata_path: Path) -> dict[str, Any]:
    """Load a Component's YAML metadata."""
    with metadata_path.open(encoding="utf-8") as metadata_file:
        metadata = yaml.safe_load(metadata_file)

    if not isinstance(metadata, dict):
        raise ValueError(
            f"Expected a YAML mapping in {metadata_path}"
        )

    return metadata