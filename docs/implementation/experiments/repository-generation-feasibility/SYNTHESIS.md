# Repository Generation Feasibility — Discovery Synthesis

Date: 2026-11-19  
Status: **Verified — bounded experiment; maintainer decision pending**  
Integrated baseline: `f4ee63b150619b363e55ec4abb2e313ef6a78ccb`  
Related: [Strategic Prioritization](../../../governance/19_STRATEGIC_PRIORITIZATION.md), [Experiment I](README.md), [Experiment II](REFINEMENT.md).

## Verification

PR #399 integrated the separate experimental workflow; its branch was removed. [Main Validator run 44501203765](https://github.com/fran-eliot/github-framework/actions/runs/44501203765) completed successfully at the integrated baseline. [Experimental run 44501027184](https://github.com/fran-eliot/github-framework/actions/runs/44501027184) ran both probes on the exact PR head `1f59b21c478dcd044d96965456f83f953bf1e1b1` (confirmed by checkout and rev-parse logs), not the merge commit. Only the experimental workflow was added by that PR. Both job logs and step conclusions were inspected.

| Evidence | [Ubuntu](https://github.com/fran-eliot/github-framework/actions/runs/44501027184/job/135480522782) | [Windows](https://github.com/fran-eliot/github-framework/actions/runs/44501027184/job/135480522166) |
| --- | --- | --- |
| Python | 3.11.18 | 3.11.9 |
| PyYAML / Jinja2 | 6.0.2 / 3.1.6 | 6.0.2 / 3.1.6 |
| Full working-tree checkout (shallow history) | PASS | PASS |
| Experiment I | PASS | PASS |
| Experiment II | PASS (bounded) | PASS (bounded) |
| Registry / physical IDs | 62 / 21 | 62 / 21 |
| Backend outcomes | 16 Resolved, 12 Conceptual, 0 conflicts | Same |
| Refinement negative checks | 32 (16 per approach) | 32 (16 per approach) |

All 64 refinement negative check executions across platforms are repetitions of 16 scenarios in two rendering paths, not 64 unique scenarios. Both paths in both environments returned the exact original README SHA-256 `76fdbac91226ed9475846f937c04c8fa79bc921893d0c46056bed6ea40167f02` and CHANGELOG SHA-256 `92a499cb2fdc0dd320ee1f10f88ab679beda944f4433381353b1da1996a91cdb`. The full-checkout gap in Experiment II is closed for this PR head and these runners. Existing Validator CI is separate evidence, not a substitute for replay.

## Gate assessment

| Gate | Result | Boundary |
| --- | --- | --- |
| EXP-01 | PASS | Pinned source and probe identities, fixture, commands and exact environments |
| EXP-02 | PASS | Full canonical inventory through existing resolver, selected conflicts rejected; no full materialization |
| EXP-03 | PASS | Two files, selected order, one H1, Unreleased-only changelog |
| EXP-04 | PASS | Identified gaps and bounded input/static audit cases; not complete contract validation |
| EXP-05 | PASS | Repeated output hashes across both approaches and runners |
| EXP-06 | PASS | Fixed isolated destinations and tested collision/traversal/existing-file cases; not atomicity or arbitrary filesystem safety |
| EXP-07 | PASS | Direct and Jinja2 translation compared against manual reference; shared parser and editorial projection |
| EXP-08 | PASS | Evidence, negative findings and recommendation recorded |

Overall **PASS — bounded feasibility**, subject to maintainer acceptance. No independent user study, real consumer modification, application generation, native Handlebars test, generalized security or full Template conformance is established.

## Findings and product direction

Composition Preview can serve as the resolution layer without altering its behavior. Resolution and renderability are distinct. Materialization requires explicit input contracts, scoped reference auditing, ordered fragment assembly, destination ownership, and standalone document policies. README-HERO/README-OVERVIEW and DOC-CHANGELOG expose different needs. The latter uses an editorial projection rather than generic rendering. Five other required Backend responsibilities were not materialized.

| Candidate next direction | Value | Risk |
| --- | --- | --- |
| A — Bounded local repository documentation generation core | Delivers a first usable creation outcome, building on the proven architecture | Must close required coverage and define precise output/safety contracts before claiming full Template support |
| B — General-purpose generator and renderer | Wider possible coverage | Premature grammar, dependency and ownership commitments |
| C — Defer generation and prioritize automated adoption evidence | Valuable alternative if creation scope proves excessive | Leaves creation journey incomplete despite favorable feasibility |

Recommend A for delivery-scope discovery, not immediate implementation. Start by defining the first useful output and required coverage; distinguish a partial documentation seed from a complete Template instance. Compare renderer reuse, contract normalization and a deliberately bounded adapter against actual canonical assets before choosing a production dependency. Do not simply promote experimental code into production. A usable first-run experience and failure behavior should be explicit acceptance criteria. Reassess B and C if the resulting scope is disproportionate.

## Decision boundary and follow-up

Request formal acceptance of the bounded feasibility result and authorization to define a delivery scope for A. This does not authorize implementation, a release, tag, Sprint or milestone. Existing experimental workflow remains path-filtered and manually dispatchable; retention or removal is a separate later decision, because pinned probe hashes intentionally fail when sources drift. No changes to Only Film; UX-02 remains Prepared — Not Executed; Composition Preview remains Complete — Unreleased; published version remains v0.12.0.
