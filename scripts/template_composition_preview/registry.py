"""Bounded adapter for the four existing Component Catalog registry tables."""

from dataclasses import dataclass
from pathlib import Path
import re

from . import SourceError
from .sources import COMPONENT_ID, read_text

REGISTRY_PATH = "docs/design-system/09_COMPONENT_CATALOG.md"
SECTIONS = (
    ("# 40. README Component Registry", "README"),
    ("# 57. Documentation Component Registry", "DOC"),
    ("# 93. Workflow Component Registry", "WCL"),
    ("# 112. Visual Component Registry", "VCL"),
)
HEADER = "| ID | Responsibility | Implementation |"
SEPARATOR = "| --- | --- | :---: |"
ROW = re.compile(r"\| \x60([A-Z0-9-]+)\x60 \| ([^|]+) \| (Implemented|Conceptual) \|")


@dataclass(frozen=True)
class RegistrySource:
    id: str
    classification: str
    section: str
    path: str = REGISTRY_PATH


def parse_registry(text: str) -> dict[str, RegistrySource]:
    """Parse only the explicitly identified registry sections, not arbitrary tables."""
    lines = text.splitlines()
    records = {}
    for heading, prefix in SECTIONS:
        starts = [i for i, line in enumerate(lines) if line == heading]
        if len(starts) != 1:
            raise SourceError(f"{REGISTRY_PATH}: expected one {heading}")
        start = starts[0] + 1
        end = next((i for i in range(start, len(lines))
                    if lines[i].startswith("# ")), len(lines))
        section = lines[start:end]
        headers = [i for i, line in enumerate(section) if line == HEADER]
        if len(headers) != 1:
            raise SourceError(f"{REGISTRY_PATH}: invalid table header in {heading}")
        index = headers[0]
        if index + 1 >= len(section) or section[index + 1] != SEPARATOR:
            raise SourceError(f"{REGISTRY_PATH}: invalid separator in {heading}")
        # The current section has exactly one contiguous table.
        if any(line.lstrip().startswith("|") for line in section[:index]):
            raise SourceError(f"{REGISTRY_PATH}: unexpected table in {heading}")
        rows = 0
        index += 2
        while index < len(section) and section[index].startswith("|"):
            match = ROW.fullmatch(section[index])
            if not match:
                raise SourceError(f"{REGISTRY_PATH}: malformed row in {heading}")
            identity, responsibility, classification = match.groups()
            if (not COMPONENT_ID.fullmatch(identity)
                    or not identity.startswith(prefix + "-")
                    or not responsibility.strip() or identity in records):
                raise SourceError(f"{REGISTRY_PATH}: invalid or duplicate ID {identity}")
            records[identity] = RegistrySource(identity, classification, heading[2:])
            rows += 1
            index += 1
        if not rows or any(line.lstrip().startswith("|") for line in section[index:]):
            raise SourceError(f"{REGISTRY_PATH}: empty or interrupted table in {heading}")
        # The canonical section ends with blank lines and a thematic break.
        if any(line.strip() not in ("", "---") for line in section[index:]):
            raise SourceError(f"{REGISTRY_PATH}: unexpected content after table in {heading}")
    return records


def load_registry(root: Path) -> dict[str, RegistrySource]:
    return parse_registry(read_text(root, REGISTRY_PATH))
