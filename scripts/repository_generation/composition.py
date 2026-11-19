"""Read-only composition and direct dependency preflight for generation."""
from dataclasses import dataclass
from pathlib import Path
import re

from scripts.template_composition_preview import SourceError
from scripts.template_composition_preview.registry import load_registry
from scripts.template_composition_preview.resolution import (
    CompositionResolution, resolve_composition, resolve_reference,
)
from scripts.template_composition_preview.sources import (
    COMPONENT_ID, discover_physical, load_mapping, load_template, read_text,
)

from . import GenerationError
from .profile import REQUIRED, VISUAL_LIMITATION, require_profile

_LEVELS = ("required", "recommended", "optional")
_VERSION = re.compile(r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)")


@dataclass(frozen=True)
class SelectedComponent:
    id: str
    version: str
    metadata_path: str
    artifact_path: str
    template: str


@dataclass(frozen=True)
class DependencyFinding:
    owner: str
    id: str
    level: str
    minimum_version: str
    outcome: str
    note: str


@dataclass(frozen=True)
class GenerationComposition:
    resolution: CompositionResolution
    selected: tuple[SelectedComponent, ...]
    dependencies: tuple[DependencyFinding, ...]


def _version(value, context):
    if not isinstance(value, str) or not _VERSION.fullmatch(value):
        raise GenerationError(f"{context}: unsupported dependency version")
    return tuple(int(part) for part in value.split("."))


def _declarations(metadata, owner):
    declarations = metadata.get("dependencies", [])
    if declarations == []:
        return
    if not isinstance(declarations, dict) or declarations.keys() - set(_LEVELS):
        raise GenerationError(f"{owner}: unsupported dependency declarations")
    seen = set()
    for level in _LEVELS:
        entries = declarations.get(level, [])
        if not isinstance(entries, list):
            raise GenerationError(f"{owner}: invalid {level} dependencies")
        for entry in entries:
            if not isinstance(entry, dict) or set(entry) != {"id", "minimum_version"}:
                raise GenerationError(f"{owner}: invalid dependency entry")
            identity, minimum = entry["id"], entry["minimum_version"]
            if not isinstance(identity, str) or not COMPONENT_ID.fullmatch(identity):
                raise GenerationError(f"{owner}: invalid dependency identity")
            if identity == owner or identity in seen:
                raise GenerationError(f"{owner}: self or duplicate dependency {identity}")
            seen.add(identity)
            _version(minimum, f"{owner}/{identity}")
            yield level, identity, minimum


def _find_dependencies(owner, metadata, registry, physical):
    for level, identity, minimum in _declarations(metadata, owner):
        result = resolve_reference(identity, level, registry.get(identity), physical.get(identity, ()))
        outcome, note = result.outcome, result.reason
        if outcome == "Resolved":
            actual = result.physical[0].version
            if _version(actual, f"{owner}/{identity}") < _version(minimum, f"{owner}/{identity}"):
                outcome, note = "VersionMismatch", f"{actual} is below {minimum}"
            else:
                note = f"Library version {actual}; not a transitive materialization claim"
        allowed = (owner, identity, level, minimum, outcome) == (
            "README-HERO", "VCL-HERO", "required", "1.0.0", "Conceptual",
        )
        if allowed:
            note = VISUAL_LIMITATION
        elif level == "required" and outcome != "Resolved":
            raise GenerationError(f"{owner}: required dependency {identity}: {outcome} ({note})")
        yield DependencyFinding(owner, identity, level, minimum, outcome, note)


def load_composition(root: Path, template_id: str, version: str) -> GenerationComposition:
    """Resolve the bounded profile, then capture selected text and direct dependency findings."""
    require_profile(template_id, version)
    try:
        template = load_template(root, template_id)
        require_profile(template.id, template.version)
        registry = load_registry(root)
        physical = discover_physical(root)
        resolution = resolve_composition(template, registry, physical)
        if resolution.has_conflicts:
            conflicts = ", ".join(
                f"{ref.id}: {ref.outcome}"
                for group in resolution.groups for ref in group.references
                if ref.outcome in ("Unknown", "Inconsistent", "Ambiguous")
            )
            raise GenerationError("composition conflicts: " + conflicts)
        required = next(group.references for group in resolution.groups if group.level == "required")
        if tuple(ref.id for ref in required) != tuple(row[0] for row in REQUIRED):
            raise GenerationError("required composition differs from supported profile")
        selected, dependencies = [], []
        for ref, (identity, expected_version, directory) in zip(required, REQUIRED):
            if ref.outcome != "Resolved" or len(ref.physical) != 1:
                raise GenerationError(f"{identity}: selected reference is {ref.outcome}")
            base = "framework/components/" + directory
            metadata_path, artifact_path = base + "/metadata.yml", base + "/template.md"
            info = ref.physical[0]
            if (info.path, info.version) != (metadata_path, expected_version):
                raise GenerationError(f"{identity}: unsupported selected path or version")
            metadata = load_mapping(root, metadata_path)
            if (metadata.get("id"), metadata.get("version")) != (identity, expected_version):
                raise GenerationError(f"{identity}: selected metadata identity/version mismatch")
            text = read_text(root, artifact_path)
            if not text.strip():
                raise GenerationError(f"{identity}: empty canonical artifact")
            selected.append(SelectedComponent(identity, expected_version, metadata_path, artifact_path, text))
            dependencies.extend(_find_dependencies(identity, metadata, registry, physical))
        if not any(
            (finding.owner, finding.id, finding.level, finding.minimum_version, finding.outcome)
            == ("README-HERO", "VCL-HERO", "required", "1.0.0", "Conceptual")
            for finding in dependencies
        ):
            raise GenerationError("named VCL-HERO limitation differs from supported profile")
        return GenerationComposition(resolution, tuple(selected), tuple(dependencies))
    except SourceError as exc:
        raise GenerationError(f"composition source error: {exc}") from exc
