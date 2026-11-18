"""Pure resolution of declared Template references against source evidence."""

from dataclasses import dataclass
from typing import Mapping

from .registry import RegistrySource
from .sources import PhysicalSource, TemplateSource

OUTCOMES = ("Resolved", "Conceptual", "Unknown", "Inconsistent", "Ambiguous")
CONFLICT_OUTCOMES = frozenset(("Unknown", "Inconsistent", "Ambiguous"))


@dataclass(frozen=True)
class ReferenceResolution:
    id: str
    level: str
    outcome: str
    reason: str
    registry: RegistrySource | None
    physical: tuple[PhysicalSource, ...]


@dataclass(frozen=True)
class RequirementResolution:
    level: str
    references: tuple[ReferenceResolution, ...]

    @property
    def counts(self) -> dict[str, int]:
        return count_outcomes(self.references)


@dataclass(frozen=True)
class CompositionResolution:
    template: TemplateSource
    groups: tuple[RequirementResolution, ...]

    @property
    def counts(self) -> dict[str, int]:
        return count_outcomes(
            tuple(reference for group in self.groups for reference in group.references)
        )

    @property
    def has_conflicts(self) -> bool:
        return any(self.counts[outcome] for outcome in CONFLICT_OUTCOMES)


def count_outcomes(references: tuple[ReferenceResolution, ...]) -> dict[str, int]:
    """Include zero-valued outcomes in a fixed order."""
    counts = dict.fromkeys(OUTCOMES, 0)
    for reference in references:
        counts[reference.outcome] += 1
    return counts


def resolve_reference(
    identity: str,
    level: str,
    registry: RegistrySource | None,
    physical: tuple[PhysicalSource, ...],
) -> ReferenceResolution:
    """Resolve validated source records without reading files or choosing a duplicate."""
    matches = tuple(sorted(physical, key=lambda record: record.path))
    classification = registry.classification if registry is not None else None
    if len(matches) > 1:
        outcome, reason = "Ambiguous", "Multiple physical metadata identities"
    elif classification == "Implemented":
        if matches:
            outcome, reason = "Resolved", "Matching physical metadata identity"
        else:
            outcome, reason = "Inconsistent", "Missing implementation evidence"
    elif classification == "Conceptual":
        if matches:
            outcome, reason = "Inconsistent", "Classification and implementation disagree"
        else:
            outcome, reason = "Conceptual", "Explicit Conceptual classification; no physical match"
    elif matches:
        outcome, reason = "Inconsistent", "Missing registry entry"
    else:
        outcome, reason = "Unknown", "No registry or physical evidence"
    return ReferenceResolution(identity, level, outcome, reason, registry, matches)


def resolve_composition(
    template: TemplateSource,
    registry: Mapping[str, RegistrySource],
    physical: Mapping[str, tuple[PhysicalSource, ...]],
) -> CompositionResolution:
    """Join validated sources by exact ID, preserving declared levels and order."""
    groups = tuple(
        RequirementResolution(
            level,
            tuple(
                resolve_reference(identity, level, registry.get(identity), physical.get(identity, ()))
                for identity in identities
            ),
        )
        for level, identities in template.references
    )
    return CompositionResolution(template, groups)
