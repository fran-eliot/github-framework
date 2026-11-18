# Repository Template Composition Preview — Discovery

**Status:** Discovery proposal; not an implementation commitment  
**Evidence date:** 2026-11-18  
**Framework baseline:** [`f7af289d17d06c176e7a93dd6b804d0f7c300dbd`](https://github.com/fran-eliot/github-framework/commit/f7af289d17d06c176e7a93dd6b804d0f7c300dbd) (after PR #380; latest published release v0.12.0)

## 1. Problem and use case

A developer starting a backend, full-stack or documentation repository needs to identify the Components a Repository Template declares, locate reusable implementations, and understand which responsibilities still require a project-specific approach. Today this requires cross-referencing the Template metadata, the Component Catalog and the physical library. The Validator's catalog lists implemented Component directories; it does not resolve the contextual composition declared by a Repository Template.

The bounded proposal is a **read-only composition preview**, not a repository generator or a consumer Assessment. The existing [Repository Template contract](../../framework/templates/repositories/README.md#29-component-availability) expressly permits Conceptual Components at any requirement level.

## 2. Pinned observations

Sources at the baseline above:

- [Backend metadata](https://github.com/fran-eliot/github-framework/blob/f7af289d17d06c176e7a93dd6b804d0f7c300dbd/framework/templates/repositories/backend/metadata.yml)
- [Full Stack metadata](https://github.com/fran-eliot/github-framework/blob/f7af289d17d06c176e7a93dd6b804d0f7c300dbd/framework/templates/repositories/fullstack/metadata.yml)
- [Documentation metadata](https://github.com/fran-eliot/github-framework/blob/f7af289d17d06c176e7a93dd6b804d0f7c300dbd/framework/templates/repositories/documentation/metadata.yml)
- [Physical library](https://github.com/fran-eliot/github-framework/tree/f7af289d17d06c176e7a93dd6b804d0f7c300dbd/framework/components): 21 metadata files (12 README, 4 Documentation, 5 Workflow); IDs inspected directly.
- [Component Catalog](https://github.com/fran-eliot/github-framework/blob/f7af289d17d06c176e7a93dd6b804d0f7c300dbd/docs/design-system/09_COMPONENT_CATALOG.md): all 14 distinct referenced IDs without physical matches are explicitly registered as Conceptual.

Counts below are **matching physical metadata IDs / declared references**, not validation or conformance scores.

| Template (0.1.0) | Required | Recommended | Optional | Total |
| --- | ---: | ---: | ---: | ---: |
| TPL-BACKEND | 8/8 | 5/7 | 3/13 | 16/28 |
| TPL-FULLSTACK | 9/9 | 4/8 | 3/11 | 16/28 |
| TPL-DOCUMENTATION | 8/9 | 2/7 | 1/5 | 11/21 |

### References without physical metadata matches

| Template | Requirement level | Catalogued Conceptual IDs |
| --- | --- | --- |
| TPL-BACKEND | recommended | README-REPOSITORY-STRUCTURE, DOC-TESTING |
| TPL-BACKEND | optional | README-CONTRIBUTING, README-DEMO, README-HIGHLIGHTS, README-LICENSE, DOC-ADR, DOC-API, DOC-DATABASE, DOC-DEPLOYMENT, DOC-SECURITY, DOC-DIAGRAMS |
| TPL-FULLSTACK | recommended | README-REPOSITORY-STRUCTURE, DOC-TESTING, DOC-DEPLOYMENT, DOC-DIAGRAMS |
| TPL-FULLSTACK | optional | README-CONTRIBUTING, README-DEMO, README-HIGHLIGHTS, README-LICENSE, DOC-ADR, DOC-API, DOC-DATABASE, DOC-SECURITY |
| TPL-DOCUMENTATION | required | README-LICENSE |
| TPL-DOCUMENTATION | recommended | README-REPOSITORY-STRUCTURE, DOC-ADR, DOC-ROADMAP, DOC-GLOSSARY, DOC-DIAGRAMS |
| TPL-DOCUMENTATION | optional | README-CONTRIBUTING, README-HIGHLIGHTS, DOC-TESTING, DOC-SECURITY |

In particular, the Documentation Template intentionally references a Conceptual README-LICENSE as required. Absence of a physical implementation is not an invalid Template or an unsatisfied consumer responsibility. No consumer was inspected or changed for this study.

## 3. Proposed observable behavior

- Select one of the three existing Templates by stable ID and report its independent version.
- Retain each declared requirement level and source order.
- Resolve references by stable Component ID, not directory naming or filename heuristics.
- Show the physical canonical location when a unique metadata match exists; distinguish catalogued Conceptual references from unknown, ambiguous or inconsistent references. Do not infer Conceptual solely from absence.
- Identify malformed metadata or duplicate references explicitly, without silently guessing.
- Report counts per requirement level, with evidence links and limitations; no pass/fail consumer conformance score.

The representation, source resolution mechanism and CLI surface remain open design questions. In particular, the human-readable registry is not yet a guaranteed machine-readable contract: evaluate a bounded, traceable representation of Conceptual IDs before promising automated classification. Do not introduce a second authoritative registry or scrape arbitrary Markdown as though it were a stable schema.

## 4. Candidate acceptance checks

| Case | Expected result |
| --- | --- |
| Backend and Full Stack at the pinned baseline | All required references have matching physical metadata; other levels preserve their declared composition |
| Documentation at the pinned baseline | README-LICENSE remains required and Conceptual, without a false Template failure |
| Unknown reference | Explicit unresolved/unknown result, not invented classification |
| Duplicate physical IDs or inconsistent registry evidence | Explicit ambiguity or conflict, no arbitrary first-match selection |
| Invalid input | Clear diagnostic; no files written |
| Repeated execution at the same source revision | Deterministic composition and ordering |

These are candidate checks, not executed tests. The counts in section 2 are documentary evidence only.

## 5. Boundaries and next decision

Out of scope: materialization, templating engines, automatic generation, network retrieval, automatic migrations, consumer inspection or mutation, Adoption Decisions, Template promotion, implementing missing Components en masse, and automatic release planning.

Next: review the representation and evidence strategy, then decide whether to implement a bounded preview. No next release, Sprint, milestone or delivery scope is committed by this discovery.
