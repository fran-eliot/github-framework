"""Strict local source acquisition for Repository Template composition."""

from dataclasses import dataclass
from pathlib import Path
import re
import stat

import yaml

from . import SourceError

TEMPLATES = {
    "TPL-BACKEND": "backend",
    "TPL-FULLSTACK": "fullstack",
    "TPL-DOCUMENTATION": "documentation",
}
LEVELS = ("required", "recommended", "optional")
FAMILIES = {
    "readme": ("README", "README"),
    "documentation": ("Documentation", "DOC"),
    "workflow": ("Workflow", "WCL"),
}
COMPONENT_ID = re.compile(r"(?:README|DOC|WCL|VCL)-[A-Z0-9]+(?:-[A-Z0-9]+)*")


@dataclass(frozen=True)
class TemplateSource:
    id: str
    version: str
    path: str
    references: tuple[tuple[str, tuple[str, ...]], ...]


@dataclass(frozen=True)
class PhysicalSource:
    id: str
    name: str
    version: str
    status: str
    path: str


class _UniqueLoader(yaml.SafeLoader):
    """Safe YAML loading without silently overwriting duplicate keys."""

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                if key in result:
                    raise SourceError(f"duplicate YAML key: {key!r}")
                result[key] = self.construct_object(value_node, deep=deep)
            except TypeError as exc:
                raise SourceError("invalid YAML mapping key") from exc
        return result


def checked_path(root: Path, relative: str, *, directory: bool) -> Path:
    """Check each traversed path component without following symbolic links."""
    current = root.absolute()
    parts = Path(relative).parts
    for index, part in enumerate(("", *parts)):
        if part:
            current = current / part
        try:
            info = current.lstat()
        except OSError as exc:
            raise SourceError(f"unavailable source: {current}") from exc
        if stat.S_ISLNK(info.st_mode) or (
            getattr(info, "st_file_attributes", 0)
            & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
        ):
            raise SourceError(f"linked source path: {current}")
        expected_directory = index < len(parts) or directory
        if not (stat.S_ISDIR(info.st_mode) if expected_directory else stat.S_ISREG(info.st_mode)):
            raise SourceError(f"unexpected source type: {current}")
    return current


def read_text(root: Path, relative: str) -> str:
    path = checked_path(root, relative, directory=False)
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise SourceError(f"unreadable source: {relative}") from exc


def load_mapping(root: Path, relative: str) -> dict:
    try:
        data = yaml.load(read_text(root, relative), Loader=_UniqueLoader)
    except (yaml.YAMLError, SourceError, RecursionError) as exc:
        raise SourceError(f"{relative}: {exc}") from exc
    if not isinstance(data, dict):
        raise SourceError(f"{relative}: expected YAML mapping")
    return data


def _text(data: dict, field: str, path: str) -> str:
    value = data.get(field)
    if not isinstance(value, str) or not value.strip() or value != value.strip() or not value.isprintable():
        raise SourceError(f"{path}: invalid {field}")
    return value


def load_template(root: Path, template_id: str) -> TemplateSource:
    if template_id not in TEMPLATES:
        raise SourceError(f"unknown Template ID: {template_id}")
    path = f"framework/templates/repositories/{TEMPLATES[template_id]}/metadata.yml"
    data = load_mapping(root, path)
    if _text(data, "id", path) != template_id:
        raise SourceError(f"{path}: Template identity mismatch")
    version = _text(data, "version", path)
    groups = data.get("components")
    if not isinstance(groups, dict) or set(groups) != set(LEVELS):
        raise SourceError(f"{path}: expected exactly the three requirement levels")
    seen = set()
    references = []
    for level in LEVELS:
        values = groups[level]
        if not isinstance(values, list):
            raise SourceError(f"{path}: {level} must be a list")
        for value in values:
            if not isinstance(value, str) or not COMPONENT_ID.fullmatch(value):
                raise SourceError(f"{path}: invalid Component ID in {level}")
            if value in seen:
                raise SourceError(f"{path}: duplicate Template reference {value}")
            seen.add(value)
        references.append((level, tuple(values)))
    return TemplateSource(template_id, version, path, tuple(references))


def discover_physical(root: Path) -> dict[str, tuple[PhysicalSource, ...]]:
    base = "framework/components"
    library = checked_path(root, base, directory=True)
    try:
        (library / "visual").lstat()
    except FileNotFoundError:
        pass
    except OSError as exc:
        raise SourceError("unable to inspect physical Visual family") from exc
    else:
        raise SourceError("unsupported physical Visual family")
    matches: dict[str, list[PhysicalSource]] = {}
    for family, (label, prefix) in FAMILIES.items():
        relative = f"{base}/{family}"
        directory = checked_path(root, relative, directory=True)
        try:
            entries = sorted(directory.iterdir(), key=lambda item: item.name)
            for entry in entries:
                info = entry.lstat()
                if stat.S_ISLNK(info.st_mode) or (
                    getattr(info, "st_file_attributes", 0)
                    & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
                ):
                    raise SourceError(f"linked Component entry: {entry}")
                if not stat.S_ISDIR(info.st_mode):
                    continue
                path = f"{relative}/{entry.name}/metadata.yml"
                data = load_mapping(root, path)
                identity = _text(data, "id", path)
                if not COMPONENT_ID.fullmatch(identity) or not identity.startswith(prefix + "-"):
                    raise SourceError(f"{path}: invalid Component family identity")
                if _text(data, "family", path) != label:
                    raise SourceError(f"{path}: Component family/location mismatch")
                record = PhysicalSource(
                    identity, _text(data, "name", path), _text(data, "version", path),
                    _text(data, "status", path), path,
                )
                matches.setdefault(identity, []).append(record)
        except OSError as exc:
            raise SourceError(f"unable to discover Components: {relative}") from exc
    return {identity: tuple(sorted(records, key=lambda record: record.path))
            for identity, records in sorted(matches.items())}
