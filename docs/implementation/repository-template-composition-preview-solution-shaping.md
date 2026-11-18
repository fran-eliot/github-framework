# Repository Template Composition Preview — Solution Shaping

**Status:** Proposed design; implementation not authorized  
**Date:** 2026-11-18  
**Source baseline:** [`0470ed45146a0d810126e18c67435a2724f8da22`](https://github.com/fran-eliot/github-framework/commit/0470ed45146a0d810126e18c67435a2724f8da22) (PR #381 merged)

This proposal follows [Composition Preview Discovery](repository-template-composition-preview-discovery.md). It retains the separation of Component availability, Template requirement level, lifecycle status and consumer conformance.

## 1. Representation alternatives

| Alternative | Advantage | Trade-off |
| --- | --- | --- |
| A — bounded adapter for the current Component Catalog registry tables | Uses the existing classification source; no duplicated registry or migration | Coupled to an explicitly delimited Markdown structure; requires fail-closed parsing and tests |
| B — migrate registry classifications into canonical structured data and derive human-readable tables | Stronger machine-readable contract and long-term reuse | Requires a governance and source-of-truth migration beyond the first preview |
| C — physical metadata only | Simple; builds on existing Validator metadata | Cannot distinguish Conceptual entries from unknown or missing implementations |

**Recommended candidate: A**, as a narrow experimental adapter, not a general Markdown parser. B remains a future decision if real usage warrants it. C alone does not satisfy the discovered classification need.

## 2. Source authority and adapter boundary

The three Template `metadata.yml` files remain authoritative for contextual requirement levels and declared order. Physical Component metadata remains authoritative for ID, version and location evidence. [Component Catalog 1.2.0](../design-system/09_COMPONENT_CATALOG.md) explicitly classifies implementation availability; it does not replace the canonical specification or metadata.

The proposed adapter reads only the four existing family registry tables in sections **40 (README), 57 (Documentation), 93 (Workflow), 112 (Visual)**. The exact source baseline contains headers `ID | Responsibility | Implementation`, backticked IDs and implementation values `Conceptual` or `Implemented`. Other tables, examples, summary counts and prose are not classifier input.

Require each target heading and table exactly once, expected header and valid rows, correct family prefix, nonempty responsibility and unique IDs; reject ambiguous or malformed source structure rather than guess. Section markers and grammar constitute an explicit internal adapter contract, not a stable public schema. Fail closed when the source contract changes; opt-in future migration must preserve classification authority and traceability. Do not hardcode the current list of Conceptual IDs into production code.

## 3. Proposed resolution model

For each declared Component reference, preserve its Template requirement level independently from availability. Join exact stable IDs, never inferred directory names. Candidate outcomes:

| Registry record | Physical metadata match | Outcome |
| --- | --- | --- |
| Implemented | Exactly one | Resolved; report path and metadata version |
| Conceptual | None | Conceptual; report registry evidence, no physical path |
| Implemented | None | Inconsistent; implementation missing |
| Conceptual | One | Inconsistent; classification and physical evidence disagree |
| No record | None | Unknown reference |
| No record | One | Inconsistent; missing registry entry |
| Any | Multiple | Ambiguous; do not select a match |

Unreadable or malformed source metadata, duplicate Template references across levels and incomplete registry parsing are source errors; do not emit misleading availability conclusions. A unique physical metadata match is evidence of location, not proof of valid materialization or passing Component validation.

## 4. Candidate output

A deterministic preview should record the Template ID and version, source paths, ordered required/recommended/optional entries, resolution outcome, and available metadata details. Summaries count outcomes separately per level; they are not coverage or conformance scores. A human-readable report is the minimum candidate; JSON and command naming require review. No files are written by default. Do not add a versioned schema or public compatibility promise during this design phase.

## 5. Verification strategy

- Replay the three real Template compositions from the Discovery study, including the required Conceptual README-LICENSE in TPL-DOCUMENTATION.
- Use isolated fixtures for unknown, ambiguous and inconsistent IDs and malformed tables or metadata; ensure registry source failures cannot masquerade as Conceptual or unknown references.
- Verify repeated source reads yield deterministic results and preserve Template order.
- Confirm no input file changes and no consumer inspection or generation.
- Confirm the published Validator CLI and cross-platform CI behavior remain unchanged.

No replay or executable implementation has been performed by this document.

## 6. Decision and exclusions

Request review of alternative A before defining a delivery scope. Automatic generation, consumer conformance, changes to Only Film, schema migration, new Component implementation, Template promotion, new release version, Sprint and milestone remain excluded or separately governed.