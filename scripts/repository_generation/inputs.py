"""Strict JSON project input for the approved text-only profile."""
from dataclasses import dataclass
import json
from pathlib import Path
import unicodedata

from . import GenerationError
from .profile import CATEGORIES

_REQUIRED = frozenset((
    "project_name", "tagline", "overview", "features", "technologies",
    "prerequisites", "installation", "execution", "documents", "footer",
))
_OPTIONAL = frozenset(("short_description", "alignment", "unreleased_changes"))


@dataclass(frozen=True)
class ProjectInput:
    project_name: str
    tagline: str
    overview: str
    features: tuple[str, ...]
    technologies: tuple[str, ...]
    prerequisites: str
    installation: str
    execution: str
    documents: tuple[str, ...]
    footer: str
    short_description: str
    alignment: str
    unreleased_changes: tuple[tuple[str, tuple[str, ...]], ...]


def _unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise GenerationError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def _constant(value):
    raise GenerationError(f"invalid JSON constant: {value}")


def _string(value, field, *, markdown=False, minimum=1, maximum=None, empty=False):
    if not isinstance(value, str):
        raise GenerationError(f"{field}: expected string")
    if markdown:
        value = value.replace("\r\n", "\n").replace("\r", "\n")
    allowed = "\n\t" if markdown else ""
    if any(unicodedata.category(c) in ("Cc", "Cs") and c not in allowed for c in value):
        raise GenerationError(f"{field}: forbidden control or surrogate character")
    if not markdown and any(c in value for c in "\u2028\u2029"):
        raise GenerationError(f"{field}: expected single line")
    if empty and value == "":
        return value
    if not value.strip() or len(value) < minimum or (maximum is not None and len(value) > maximum):
        raise GenerationError(f"{field}: invalid content or length")
    return value


def _items(value, field):
    if not isinstance(value, list) or not value:
        raise GenerationError(f"{field}: expected nonempty array")
    return tuple(_string(item, f"{field}[{index}]") for index, item in enumerate(value))


def parse_project_input(text: str) -> ProjectInput:
    """Parse JSON without coercing or inventing project content."""
    try:
        data = json.loads(text, object_pairs_hook=_unique, parse_constant=_constant)
    except (json.JSONDecodeError, RecursionError) as exc:
        raise GenerationError("invalid project JSON") from exc
    if not isinstance(data, dict):
        raise GenerationError("expected project JSON object")
    missing = _REQUIRED - data.keys()
    unknown = data.keys() - _REQUIRED - _OPTIONAL
    if missing:
        raise GenerationError("missing fields: " + ", ".join(sorted(missing)))
    if unknown:
        raise GenerationError("unknown fields: " + ", ".join(sorted(unknown)))
    alignment = data.get("alignment", "center")
    if alignment not in ("left", "center"):
        raise GenerationError("alignment: expected left or center")
    changes = data.get("unreleased_changes", {})
    if not isinstance(changes, dict) or changes.keys() - set(CATEGORIES):
        raise GenerationError("unreleased_changes: invalid categories")
    return ProjectInput(
        project_name=_string(data["project_name"], "project_name", minimum=2, maximum=60),
        tagline=_string(data["tagline"], "tagline", minimum=10, maximum=100),
        overview=_string(data["overview"], "overview", markdown=True, minimum=80, maximum=1200),
        features=_items(data["features"], "features"),
        technologies=_items(data["technologies"], "technologies"),
        prerequisites=_string(data["prerequisites"], "prerequisites", markdown=True),
        installation=_string(data["installation"], "installation", markdown=True),
        execution=_string(data["execution"], "execution", markdown=True),
        documents=_items(data["documents"], "documents"),
        footer=_string(data["footer"], "footer", markdown=True),
        short_description=_string(data.get("short_description", ""), "short_description", maximum=240, empty=True),
        alignment=alignment,
        unreleased_changes=tuple((key, _items(changes[key], f"unreleased_changes.{key}"))
                                 for key in CATEGORIES if key in changes),
    )


def load_project_input(path: Path) -> ProjectInput:
    try:
        text = path.read_bytes().decode("utf-8")
    except (OSError, UnicodeError) as exc:
        raise GenerationError(f"unreadable UTF-8 project input: {path}") from exc
    return parse_project_input(text)
