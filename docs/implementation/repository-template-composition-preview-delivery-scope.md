# Repository Template Composition Preview — Delivery Scope

**Status:** Proposed delivery scope; maintainer approval required before implementation  
**Date:** 2026-11-18  
**Baseline:** [`18c5dbfc1aa4dbd6d60fa0683d83ccd0c0545eca`](https://github.com/fran-eliot/github-framework/commit/18c5dbfc1aa4dbd6d60fa0683d83ccd0c0545eca) (PR #384 merged)  
**Published Framework:** v0.12.0

## 1. Objective and decision

Deliver a minimal local read-only preview of a canonical Repository Template. Follow the [Discovery Synthesis](repository-template-composition-preview-synthesis.md) and recommend Alternative A: read the existing registry tables and reconcile their classifications with Template and physical Component metadata. This scope proposes the first executable delivery, not an approval of the alternative, a release commitment or a completed implementation.

## 2. Proposed public entry point

From a Framework checkout with Python 3.11 and the existing PyYAML dependency:

```bash
python -m scripts.template_composition_preview TPL-BACKEND
python -m scripts.template_composition_preview TPL-FULLSTACK
python -m scripts.template_composition_preview TPL-DOCUMENTATION
```

Exactly one case-sensitive stable Template ID is required. The first delivery provides a deterministic human-readable stdout report only. Standard help is available; invalid arguments yield a usage diagnostic. Resolve fixed Framework source locations from the installed module's checkout, not the current working directory. Do not accept arbitrary consumer paths, custom registry paths, remote URLs, output files, JSON, or changes to the existing Validator CLI. This is a separate entry point to preserve that CLI's contract. The name and interface are proposed for approval.

## 3. Source boundary and loading

- Read the three canonical Template metadata locations under `framework/templates/repositories/`; verify selected identity rather than guessing from the directory name.
- Read `docs/design-system/09_COMPONENT_CATALOG.md` as the classification source. Use only the four explicitly bounded family registry sections (40, 57, 93 and 112), not summary tables, examples or other prose. Require each section and expected table exactly once, an expected header and separator, nonempty rows, exact recognized classification values, correct family prefix and globally unique registered IDs.
- Discover immediate physical Component directories in the current implemented families `readme`, `documentation`, and `workflow` under `framework/components/`. The Visual registry is included, but no physical Visual discovery is supported by this bounded first delivery. An unexpected physical Visual family must be reported as unsupported rather than silently used to certify absence.
- Read YAML using a safe loader with explicit duplicate mapping-key rejection, not a line-based parser. For Template metadata check usable ID, version and the three reference lists; require valid nonempty stable IDs and no repeated reference across or within levels. Empty lists are allowed. For physical metadata check usable ID, version, name, status and family/location consistency; do not infer identity from folder names. Do not require validation of unrelated metadata fields.
- Reject missing expected source roots, unreadable inputs, missing or malformed metadata for discovered Component directories, symbolic links in the traversed source paths and unsupported registry structures. Do not skip a failed physical read and then infer absence. Retain all valid duplicate physical ID matches for diagnosis rather than taking the first match.
- Structural registry validation is not a completeness proof. A valid row removed from a table may go undetected. An unregistered reference without a match is Unknown; with a match it is Inconsistent. No hardcoded ID allowlist or secondary authoritative registry is introduced.

## 4. Report and resolution contract

Report Template ID/version, relative Framework-root source references, then required, recommended and optional groups in that order, retaining the source list order. Each row exposes Component ID, registry classification (or not registered), resolution outcome, a concise reason and available evidence: registry section when present, relative metadata path(s), version and lifecycle status when present. Multiple physical matches are listed deterministically, without choosing one. A Conceptual or Unknown reference has no invented physical path. Display per-level and overall counts by outcome, including zero-valued outcomes.

| Registry | Physical matches | Outcome | Reason |
| --- | ---: | --- | --- |
| Implemented | 1 | Resolved | Matching identity |
| Conceptual | 0 | Conceptual | Explicit registry classification; no match |
| Implemented | 0 | Inconsistent | Missing implementation evidence |
| Conceptual | 1 | Inconsistent | Classification and implementation disagree |
| Not registered | 0 | Unknown | No registry or physical evidence |
| Not registered | 1 | Inconsistent | Missing registry entry |
| Any | 2 or more | Ambiguous | Multiple physical identities |

A source error is not a reference outcome. On source errors, emit a clear stderr diagnostic, no partial preview report and a nonzero exit code. Proposed exit codes: **0** = complete preview, all outcomes Resolved or Conceptual; **1** = complete preview with at least one Unknown, Inconsistent or Ambiguous reference; **2** = argument or source error preventing a reliable preview. A required Conceptual reference alone does not cause failure. These codes describe preview resolution only, never Template validity or consumer conformance.

The report must state that Resolved is metadata identity/location evidence, not proof of valid materialization, successful Validator execution or satisfaction of a Responsibility by a consumer. Paths are portable relative POSIX paths; no absolute machine-specific locations in successful stdout. No timestamps or nondeterministic ordering. Source reads are not atomic snapshots.

## 5. Acceptance criteria

| ID | Observable acceptance criterion |
| --- | --- |
| AC-01 | The three documented commands select the correct canonical ID and independent Template version; --help succeeds. |
| AC-02 | Missing, extra or unknown ID arguments fail with exit 2, clear stderr and no preview stdout. |
| AC-03 | The three requirement levels and source order are preserved; empty lists produce explicit zero counts. |
| AC-04 | Real baseline replay: Backend 8/0, 5/2, 3/10; Full Stack 9/0, 4/4, 3/8; Documentation 8/1, 2/5, 1/4 (Resolved/Conceptual by level). All three exit 0. |
| AC-05 | Documentation's required README-LICENSE is Conceptual, with registry evidence and no physical path. |
| AC-06 | All nine synthetic registry classification / physical match combinations reproduce the Solution Shaping matrix, including ambiguity precedence. |
| AC-07 | Unknown, Inconsistent or Ambiguous references remain in a complete report, with reasons and exit 1; no arbitrary winner. |
| AC-08 | Four registry sections parse independently; unrelated matching rows outside those sections are ignored. Missing/duplicate sections, malformed rows, invalid classifications/prefixes, duplicate IDs, invalid or repeated headers, empty tables and unexpected content within a table fail closed. |
| AC-09 | Malformed YAML, duplicate mapping keys, invalid required metadata fields, missing/non-list requirement levels, invalid IDs and duplicate Template references yield source errors. |
| AC-10 | Missing/unreadable input, missing metadata in discovered Component directories, symbolic links and unsupported physical Visual discovery fail explicitly, not as absence. Platform-dependent symlink tests document skips. |
| AC-11 | Physical matches are discovered from the actual library at runtime using metadata IDs, not hardcoded inventory or directory-derived IDs. |
| AC-12 | Output includes traceable relative source references, evidence and counts by level and overall; all counts reconcile with individual rows. |
| AC-13 | Identical repeated executions over unchanged sources produce identical stdout, stderr and exit codes; isolated fixtures cover changed classifications and duplicate physical matches. |
| AC-14 | Snapshot fixture file bytes and paths before/after success and failure; no changes, generated files, consumer access or network requests. Account for normal Python bytecode cache behavior by disabling bytecode writes for the no-write verification and documenting the invocation. |
| AC-15 | Existing Validator CLI/JSON regression tests and real-library smoke test continue to pass; no change to its output or flags. |
| AC-16 | Preview tests and real Template commands execute successfully on Ubuntu and Windows using Python 3.11 in CI; results and tested revision are recorded. |
| AC-17 | Documentation explains invocation, output, exit codes, structural adapter limits, absence of registry completeness guarantee and distinction from consumer Assessment. |

Baseline counts come from the prior bounded replay, not from already-executed acceptance tests. If legitimate source evolution changes the counts, review and explicitly update the baseline evidence rather than hardcoding a production result.

## 6. Delivery exclusions and completion gate

Excluded: repository generation or materialization, copying templates into consumers, consumer inspection or mutation, automatic Adoption Decisions, Template or Component lifecycle promotion, schema/registry migration, additional Component implementations, JSON export, public schema promises, network retrieval, release orchestration, arbitrary root inputs, and implicit integration with the Validator CLI.

Implementation planning may decompose the scope into source readers, resolver/report and verification/documentation. Delivery is complete only when the scoped implementation and AC-01–AC-17 have evidence, the existing workflow remains green, and the maintainer reviews the result. No new Sprint, milestone or target release is committed. Only Film remains a completed documentary Assessment at its pinned reference and UX-02 remains Prepared — Not Executed.

**Next gate:** review and approve the proposed scope, then prepare implementation planning with dependencies and acceptance-criteria allocation.
