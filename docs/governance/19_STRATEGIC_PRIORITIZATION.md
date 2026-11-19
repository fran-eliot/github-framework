# 19 — Strategic Prioritization and Experiment Definition

Date: 2026-11-19  
Status: Proposed — decision pending  
Baseline: [f8ea292f44d1c28f46aa509b355a47ace669cff4](https://github.com/fran-eliot/github-framework/commit/f8ea292f44d1c28f46aa509b355a47ace669cff4)

## Context

The [Global Strategic Review](17_GLOBAL_STRATEGIC_REVIEW.md) and [Capability Map](18_STRATEGIC_CAPABILITIES_AND_LANDSCAPE.md) identify an end-to-end creation journey and reduced manual adoption effort as candidate high-value outcomes. PR #395 is merged; its branch was removed and [main CI 44483797262](https://github.com/fran-eliot/github-framework/actions/runs/44483797262) succeeded. Latest release remains v0.12.0; Composition Preview is Complete — Unreleased.

## Decision matrix

Scores are maintainer-reviewable strategic hypotheses on a 1–5 scale (5 favorable); no measured demand, cost estimates or user study. Weighted sum divided by 100.

| Alternative | User value 30% | Differentiation 20% | Reuse 20% | Feasibility 15% | Maintainability 10% | Verifiability 5% | Weighted score |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| A — Repository Generation | 5 | 4 | 5 | 3 | 3 | 5 | 4.30 |
| B — Automated Evidence Collection | 5 | 5 | 4 | 3 | 3 | 4 | 4.25 |
| C — Developer Experience and Distribution | 4 | 3 | 4 | 4 | 4 | 5 | 3.85 |
| D — Consolidation only | 2 | 2 | 3 | 5 | 5 | 5 | 3.10 |

A builds directly on Composition Preview; B has potentially stronger differentiation and remains a close alternative. C improves access but does not by itself close a missing end-to-end journey; D reduces maintenance risk but leaves the primary gaps open. The 0.05 difference between A and B is not robust: increasing the differentiation weight by 5 percentage points at the expense of reuse would reverse their order. Prefer A for sequencing and bounded learning, not numerical superiority. If feasibility is poor, reconsider B or C rather than forcing implementation.

## Concrete materialization gaps

Pinned source observations:

- [TPL-BACKEND 0.1.0](../../framework/templates/repositories/backend/metadata.yml) declares eight required responsibilities, seven recommended and thirteen optional. The experiment must account for all references but need not render all of them.
- [README-HERO](../../framework/components/readme/hero/template.md) uses conditional blocks, nested values and iteration in Handlebars-like notation.
- [DOC-CHANGELOG](../../framework/components/documentation/changelog/template.md) uses angle-bracket editorial placeholders and a historical release example. Blind substitution could invent a release or leave misleading content.
- [Composition Preview](../implementation/repository-template-composition-preview.md) resolves references but does not validate renderability or generate artifacts. Preserve its existing outcome semantics.
- Input contracts, renderer selection, destination ownership, ordered assembly, preflight and generated output verification remain open. A Resolved reference is not a materialization guarantee.

## Proposed experiment: Repository Generation Feasibility

Question: Can a bounded composition of existing canonical Backend Components produce a useful, deterministic local repository documentation seed without changing canonical assets or real consumers?

Candidate scope: one synthetic Backend project, TPL-BACKEND 0.1.0 pinned to the baseline; README-HERO and README-OVERVIEW as assembled sections, DOC-CHANGELOG as a separate artifact. Record every unselected or conceptual reference and do not label the result a complete TPL-BACKEND implementation. Use explicit synthetic input, no fabricated runtime or release claims. Compare reuse of an existing renderer with a narrowly scoped adapter and manual baseline; record dependency and escaping trade-offs before recommending one. No production generator or new public CLI contract.

## Proposed experiment acceptance gates

| ID | Observable condition |
| --- | --- |
| EXP-01 | Record source SHA, Template version, selected Component IDs and versions, input fixture, and commands used. |
| EXP-02 | Account for the full Template reference inventory; distinguish selected, unselected and conceptual items and fail on unresolved conflicts in the selected set. |
| EXP-03 | Produce a README with the selected sections in declared order and one H1; produce a separate changelog with no invented released version. |
| EXP-04 | Required missing or invalid inputs and unsupported syntax fail explicitly; no silently retained unresolved generation placeholders in selected output. |
| EXP-05 | Identical pinned inputs yield byte-identical artifacts in two fresh isolated destinations; record hashes, exact environment and any platform limits. |
| EXP-06 | Reject pre-existing target files, unsafe output paths and collisions without changing them; fixtures only, no writes to canonical sources or real consumers. |
| EXP-07 | Compare at least two rendering approaches against the actual selected syntax and a manual reference output; record limitations, dependency cost and verification results, including failures. |
| EXP-08 | Report PASS / PARTIAL / FAIL with evidence per gate and a recommendation to proceed, refine or defer. No production-readiness assertion. |

An experiment PASS requires evidence for every gate; a documented failure is a valid discovery result. The scope intentionally does not establish full template coverage, runtime correctness, security certification, adoption conformance or a universal renderer. No remote repository creation, Git operations in consumer destinations, automatic overwrite, publishing or deployment. No changes to Only Film; UX-02 remains Prepared — Not Executed.

## Decision boundary

Recommend A for the next experiment only. Selection of a rendering approach, production delivery scope, implementation plan, release, Sprint or milestone requires separate decisions. This document is a proposal, not experiment execution evidence. If approved, conduct the bounded experiment and record actual results before selecting further work. Keep the alternative B available and reassess priorities after the experiment.
