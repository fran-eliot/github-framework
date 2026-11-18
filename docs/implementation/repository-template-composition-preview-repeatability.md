# Repository Template Composition Preview — Repeatability Experiment

**Status:** Model holds for the bounded documentary replay; executable delivery remains unverified  
**Date:** 2026-11-18  
**Pinned baseline:** [`6ddcd56da8acb6b3cfe62fe6cddc3c66453be603`](https://github.com/fran-eliot/github-framework/commit/6ddcd56da8acb6b3cfe62fe6cddc3c66453be603) (PR #382 merged)

## 1. Purpose and method

Evaluate the candidate resolution model in [Solution Shaping](repository-template-composition-preview-solution-shaping.md) before defining delivery scope. This was a read-only experimental evaluation using temporary JavaScript routines, not the proposed production Python implementation or a new Validator feature.

Source evidence: [pinned Component Catalog](https://github.com/fran-eliot/github-framework/blob/6ddcd56da8acb6b3cfe62fe6cddc3c66453be603/docs/design-system/09_COMPONENT_CATALOG.md), the three canonical Template metadata files under [repositories](https://github.com/fran-eliot/github-framework/tree/6ddcd56da8acb6b3cfe62fe6cddc3c66453be603/framework/templates/repositories), and the 21 physical Component IDs recorded by the [Discovery study](repository-template-composition-preview-discovery.md). The GitHub comparison between the Discovery baseline and this baseline showed only README, governance and Discovery/Solution Shaping document changes; no Component, Template or registry source paths changed. The physical ID inventory was consequently reused, not rediscovered by a filesystem scanner.

The experiment independently exercised two routines: a section-bounded registry reader (repeated twice on the same document) and a simplified line-based Template reference replay and ID join. The replay obtained classifications from matching registry-format rows in the unchanged real document; it did not exercise an integrated strict parser pipeline. No inputs were written or consumers inspected.

## 2. Registry experiment

| Registry family | Implemented | Conceptual | Total |
| --- | ---: | ---: | ---: |
| README | 12 | 5 | 17 |
| Documentation | 4 | 11 | 15 |
| Workflow | 5 | 11 | 16 |
| Visual | 0 | 14 | 14 |
| **Total** | **21** | **41** | **62** |

Two passes over the four specified registry sections produced the same ordered ID/classification sequence. The experimental reader required unique headings, the expected header/separator, valid rows, family prefixes and unique IDs.

Four synthetic modifications of the registry source were actually rejected: missing section heading, duplicate section heading, unsupported classification value, and duplicate ID row. This is bounded negative evidence, not proof against every malformed Markdown structure. In particular, arbitrary missing rows, unexpected text within a table, duplicate YAML keys and filesystem read failures require dedicated delivery tests.

## 3. Real Template replay

The three pinned Template files were inspected in declared requirement order, and the simplified resolver joined the references with the unchanged physical ID inventory and registry classifications.

| Template (0.1.0) | Required R/C | Recommended R/C | Optional R/C | Total R/C |
| --- | ---: | ---: | ---: | ---: |
| TPL-BACKEND | 8/0 | 5/2 | 3/10 | 16/12 |
| TPL-FULLSTACK | 9/0 | 4/4 | 3/8 | 16/12 |
| TPL-DOCUMENTATION | 8/1 | 2/5 | 1/4 | 11/10 |

R = Resolved; C = Conceptual. All 77 declared references resolved to one of these two outcomes. No Unknown, Ambiguous or Inconsistent outcome was observed in the real replay. The required README-LICENSE reference in TPL-DOCUMENTATION remains Conceptual, not an invalid Template or failed responsibility. Results match the earlier independent documentary counts.

## 4. Synthetic resolution matrix

All nine combinations below were executed against the experimental pure resolution function and matched their expected outcomes.

| Registry classification | Physical match count | Observed |
| --- | ---: | --- |
| Implemented | 1 | Resolved |
| Conceptual | 0 | Conceptual |
| Implemented | 0 | Inconsistent |
| Conceptual | 1 | Inconsistent |
| Absent | 0 | Unknown |
| Absent | 1 | Inconsistent |
| Implemented | 2 | Ambiguous |
| Conceptual | 2 | Ambiguous |
| Absent | 2 | Ambiguous |

Multiple physical matches take precedence over classification and cannot select an arbitrary implementation.

## 5. Result and limitations

**MODEL HOLDS — bounded documentary and in-memory replay.** The proposed outcomes distinguish availability from requirement level and consumer conformity, and the existing registry structure provides a viable initial classification source.

Not verified: production parser, real filesystem discovery on the current checkout, robust YAML loading, duplicate reference rejection under full YAML semantics, integrated end-to-end repeatability, complete malformed-source handling, no-write filesystem assertions, CLI/JSON output, cross-platform execution of a preview or consumer behavior. The existing Validator CI at PR #382 was successful; this is not evidence that a preview implementation passed. No production code or executable experiment artifact is introduced by this record.

## 6. Next gate

Review the findings in Discovery Synthesis and derive explicit acceptance criteria and delivery boundaries before implementation. The bounded adapter remains a recommendation, not an approved schema migration, public CLI contract, new release, Sprint or milestone. No consumer changes or Adoption decisions are authorized.
