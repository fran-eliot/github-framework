"""Deterministic human-readable rendering of composition evidence."""

from .registry import REGISTRY_PATH
from .resolution import CompositionResolution, OUTCOMES


def _counts(counts: dict[str, int]) -> str:
    return f"Total={sum(counts.values())}; " + "; ".join(
        f"{outcome}={counts[outcome]}" for outcome in OUTCOMES
    )


def render_report(result: CompositionResolution) -> str:
    """Render a complete preview without performing further source reads."""
    lines = [
        "Repository Template Composition Preview",
        f"Template: {result.template.id}",
        f"Version: {result.template.version}",
        f"Template metadata: {result.template.path}",
        f"Component Catalog: {REGISTRY_PATH}",
        "Physical Component library: framework/components (readme, documentation, workflow)",
    ]
    for group in result.groups:
        lines.extend(("", f"[{group.level}]"))
        for reference in group.references:
            classification = reference.registry.classification if reference.registry else "Not registered"
            lines.append(f"- {reference.id} | {classification} | {reference.outcome}")
            lines.append(f"  Reason: {reference.reason}")
            if reference.registry:
                lines.append(f"  Registry: {reference.registry.path} :: {reference.registry.section}")
            else:
                lines.append("  Registry: no entry")
            if reference.physical:
                for match in reference.physical:
                    lines.append(
                        f"  Metadata: {match.path} | version={match.version} | status={match.status}"
                    )
            else:
                lines.append("  Metadata: no physical match")
        lines.append(f"Counts: {_counts(group.counts)}")
    lines.extend((
        "",
        f"Overall: {_counts(result.counts)}",
        "",
        "Resolved means metadata identity/location evidence only, not valid materialization,",
        "successful Validator execution or consumer responsibility satisfaction.",
        "Registry structure is checked; completeness is not guaranteed.",
        "Source reads are not an atomic snapshot. No consumer is assessed.",
    ))
    return "\n".join(lines) + "\n"
