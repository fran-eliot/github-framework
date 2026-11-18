# Repository Template Composition Preview — Discovery Synthesis

**Status:** Discovery consolidated; candidate ready for Delivery Scope Definition, not implementation  
**Date:** 2026-11-18  
**Synthesis baseline:** [`73b43d367c5e44ab801e5d6768b53320cea6a253`](https://github.com/fran-eliot/github-framework/commit/73b43d367c5e44ab801e5d6768b53320cea6a253) (PR #383 merged)  
**Published Framework:** v0.12.0

## 1. Evidence chain

| Stage | Evidence | Conclusion |
| --- | --- | --- |
| Discovery — [PR #381](https://github.com/fran-eliot/github-framework/pull/381) | [Use case and pinned inventory](repository-template-composition-preview-discovery.md) | A developer needs to join Template references, classification and available implementations before using a Template |
| Solution Shaping — [PR #382](https://github.com/fran-eliot/github-framework/pull/382) | [Alternatives and resolution model](repository-template-composition-preview-solution-shaping.md) | A bounded adapter for the existing registry is the recommended candidate; no second authoritative registry |
| Repeatability — [PR #383](https://github.com/fran-eliot/github-framework/pull/383) | [Experimental evidence and limits](repository-template-composition-preview-repeatability.md) | MODEL HOLDS for documentary and in-memory replay, not executable delivery |

The [PR #383 Validator CI run](https://github.com/fran-eliot/github-framework/actions/runs/44394945513) completed successfully. This confirms the existing workflow for that PR, not execution of a production Composition Preview.

## 2. Consolidated need and candidate capability

A Repository Template declares contextual Responsibilities using stable Component IDs grouped into required, recommended and optional references. The Component Catalog records implementation classification; physical metadata provides identity, version and location evidence. These sources serve different purposes.

The proposed capability answers: **What does a selected Repository Template declare, and what reusable implementation evidence is available for each reference?**

The answer must not become a consumer Assessment, a validation certificate, an automatic recommendation to implement every Conceptual Component, or a repository generation plan.

The use case remains grounded in the Framework's three existing Templates; no independent participant or consumer usability result has been established.

## 3. Evidence ledger

The experiment read the four family tables twice with matching ordered results: 62 entries, of which 21 are Implemented and 41 Conceptual. A separate simplified replay used the unchanged physical ID inventory and the three Template metadata files.

| Template (0.1.0) | Resolved | Conceptual | Total |
| --- | ---: | ---: | ---: |
| TPL-BACKEND | 16 | 12 | 28 |
| TPL-FULLSTACK | 16 | 12 | 28 |
| TPL-DOCUMENTATION | 11 | 10 | 21 |
| **Reference occurrences** | **43** | **34** | **77** |

These are reference occurrences across Templates, not counts of unique Components. All 14 distinct nonphysical IDs referenced by the Templates were classified Conceptual in the Discovery evidence. There were no Unknown, Ambiguous or Inconsistent real replay outcomes.

The required README-LICENSE reference in TPL-DOCUMENTATION demonstrates why availability must not be used as a pass/fail criterion for a Template or consumer.

Nine synthetic resolution combinations matched expectations. Four modified registry examples were rejected (missing heading, duplicate heading, unsupported classification, duplicate ID row).

### Evidence not established

The temporary routines did not form an integrated production pipeline: the physical inventory was reused after verifying source paths were unchanged; Template parsing was line-based; and the replay lookup was separate from the bounded registry reader. No executable experiment artifact, full YAML semantics, actual local filesystem traversal, no-write assertion, CLI contract, cross-platform preview execution or independent consumer test was established. CI for the existing Validator cannot close these gaps.

## 4. Recommended technical direction

Recommend Alternative A for delivery-scope evaluation: a narrowly bounded adapter reading the existing four Component registry tables, joined by stable ID with canonical Template metadata and local physical metadata. Alternative B (canonical structured registry migration) remains deferred. Alternative C (physical metadata alone) cannot distinguish Conceptual and unknown entries.

The adapter must not treat arbitrary Markdown as a stable schema. Missing or duplicate registry sections, malformed rows, unexpected table structure and unreadable or malformed metadata must produce explicit source errors. A structurally valid table with a deleted row cannot be guaranteed detectable from syntax alone; distinguish structural validation from registry completeness, and address this limitation explicitly in the delivery scope.

Do not add a parallel authoritative list of IDs. Preserve the Catalog as classifier and local metadata as physical evidence. Treat a change in source format as requiring adapter review rather than silently guessing.

## 5. Resolution vocabulary proposed for delivery

| Outcome | Interpretation |
| --- | --- |
| Resolved | Implemented registry entry and exactly one matching physical metadata identity |
| Conceptual | Explicit Conceptual classification and no matching physical metadata |
| Unknown | Neither registry entry nor physical match |
| Inconsistent | Registry and physical evidence disagree, or physical match lacks registry registration |
| Ambiguous | Multiple physical matches for the reference; do not select a winner |

A source error is separate from a reference outcome. It must not be converted to Conceptual or Unknown. Ambiguity takes precedence over classification when multiple matches exist. A Resolved entry is a location/identity observation, not proof of valid materialization.

Keep requirement level, implementation classification, resolution outcome and lifecycle status distinct. The stable requirement order and source order within each level must survive rendering.

## 6. Candidate delivery boundaries

The next gate should define a minimal, local, read-only preview for one of the three current canonical Templates by stable ID, returning its independent version and ordered references with evidence and separate per-level outcome counts. A human-readable report is the minimum proposed interface; CLI naming, JSON, exit codes, source discovery and strict loading details are delivery decisions, not established contracts.

The following verification areas must become observable acceptance criteria before implementation:

- Real Template replay matching the pinned 77 reference outcomes, including the required Conceptual reference.
- Source structure and metadata validation, duplicate reference handling and all resolution combinations.
- Deterministic ordering, explicit source provenance and clear distinction between errors and valid Conceptual results.
- Local filesystem read-only behavior and regression coverage for unchanged Validator contracts.
- Cross-platform preview execution, with proof scoped to the tested revision.

Do not promise universal Markdown/YAML validation, a complete registry audit, or an atomic filesystem snapshot. Scope must state which source errors are covered and which completeness claims are unsupported.

## 7. Discovery exit assessment

| Gate | Assessment |
| --- | --- |
| Concrete Framework use case | Supported by existing artifacts |
| Alternative and model | Recommended, not formally selected for implementation |
| Repeatability | MODEL HOLDS within the documented experimental boundary |
| Production feasibility | Candidate; further executable verification required |
| Delivery Scope Definition | Ready to prepare |
| Implementation authorization | Pending |

**Recommendation:** proceed to Delivery Scope Definition for Alternative A. The synthesis does not approve implementation or commit a release, Sprint or milestone. Automatic generation, external consumer inspection or mutation, Adoption Decisions, Template promotion, registry migration and new Component materialization remain out of scope.

The Only Film Assessment and UX-02 status are unchanged.
