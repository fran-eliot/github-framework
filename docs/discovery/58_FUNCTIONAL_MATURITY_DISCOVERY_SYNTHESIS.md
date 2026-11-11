# 58 — Functional Maturity Discovery Synthesis

| Field | Value |
|---|---|
| Project | GitHub Framework |
| Date | 2026-11-11 |
| Status | Discovery Synthesis — Concluded for current evidence |
| Published version | `v0.10.0` |
| Scope | Functional maturity / Template materialization / `README-LICENSE` |
| Primary sources | [55 — Functional Maturity](55_FRAMEWORK_FUNCTIONAL_MATURITY_DISCOVERY.md), [56 — Materialization Reality Check](56_DOCUMENTATION_TEMPLATE_MATERIALIZATION_REALITY_CHECK.md), [57 — Documentation Consumer Case](57_DOCUMENTATION_LICENSE_CONSUMER_CASE_STUDY.md) |
| Solution Shaping | Not started |
| Delivery Scope | Not defined |
| Sprint / milestone / target version | None committed |

> This synthesis concludes the bounded investigation based on currently available evidence. Closing Discovery does not turn findings into implementation requirements or imply that all functional maturity concerns have been resolved.

---

## 1. Objective

Consolidate what has been learned about the differences between:

- contracts and Responsibilities defined by GitHub Framework;
- Canonical Components that are actually available;
- a consumer's ability to satisfy Responsibilities using its own implementations;
- executable automation versus manual, reviewable processes.

The decision question is:

> Is there sufficient evidence to prioritize materializing `README-LICENSE`, changing `TPL-DOCUMENTATION`, or extending Framework tooling as the next increment?

## 2. Synthesized Evidence

### 2.1 Functional Maturity (Discovery #55)

- **Repository Templates:** the library contains versioned compositions `TPL-BACKEND`, `TPL-FULLSTACK`, and `TPL-DOCUMENTATION`. These are declarative contracts, not automatic repository generators.
- **Framework Validator:** its Python entry point discovers and validates `metadata.yml` within the Framework's own `framework/components/` directory. It does not independently perform a semantic Assessment of external consumers.
- **Existing Repository Adoption:** Assessment, Application, and Integration provide Guides and Markdown records for human, reviewable operations. Assisted Analysis provides read-only, source-traceable Evidence support through a Guide and Snapshot Template. These artifacts do not deliver an automated adoption engine.

Prior release verification documents support the boundaries and deliverables of these capabilities. This synthesis does not reproduce those executions or claim that tests were rerun.

### 2.2 TPL-DOCUMENTATION Contract (Discovery #56)

According to the canonical definition of `TPL-DOCUMENTATION v0.1.0`, with status `Experimental` and maturity `L2`:

| Requirement Level | Declared | Implemented according to canonical README |
|---|---:|---:|
| Required | 9 | 8 |
| Recommended | 7 | 2 |
| Optional | 5 | 1 |
| **Total** | **21** | **11** |

`README-LICENSE` is the only `Required` Component classified as `Conceptual`.

The absence of its canonical materialization means that **the complete minimum contract cannot be materialized exclusively from implemented Components**. It does not mean that every documentation consumer fails to communicate its license.

The library and Component Catalog distinguish:

```text
Component availability
    ≠
Consumer responsibility coverage
    ≠
Consumer Adoption Decision
```

### 2.3 External Documentation Consumer (Discovery #57)

The `github/docs` case, pinned to commit `2b4f2c7398e04ee8d02adca7440e4286d20c78b9`, shows:

- a `License` section in the README;
- distinct license communication for documentation/content under CC BY 4.0 and code under MIT;
- links to `LICENSE` and `LICENSE-CODE`, which contain the corresponding license texts.

For the `README-LICENSE` Responsibility, understood as communicating the applicable license from the README, the case recorded **provisional `Satisfied`** coverage, with Applicability `Applicable`, implementation characteristics `Own / Specialized / Distributed`, and `Decision Status: Needs Further Evaluation`.

This evaluation is **partial and document-based**. No complete `TPL-DOCUMENTATION` Assessment was performed, no formal consumer review took place, legal license compliance was not verified, and no Adoption Decision was selected.

## 3. Final Findings

| ID | Conclusion | Evidence strength | Implication |
|---|---|---|---|
| FM-S01 | Declarative contracts and actual Component availability are distinct. | Confirmed in canonical artifacts | Keep this distinction when describing maturity |
| FM-S02 | `TPL-DOCUMENTATION` has a canonical materialization gap in `README-LICENSE`. | Confirmed | Do not present the Template as fully materializable from the catalog alone |
| FM-S03 | A documentation consumer can communicate licensing without a canonical Framework Component. | Supported by one external case | Do not infer `Missing` from `Conceptual` |
| FM-S04 | The gap creates a significant adoption obstacle for real users. | Not demonstrated | Requires targeted observation |
| FM-S05 | Materializing `README-LICENSE` is the next highest-value investment. | Not demonstrated | Do not open Delivery Scope by default |
| FM-S06 | Downgrading `README-LICENSE` from Required would be appropriate. | Not demonstrated | Preserve the contract until contrary evidence is available |
| FM-S07 | The Framework Validator must be extended or a generator created to address this case. | Not demonstrated | Do not expand tooling without a bounded, repeatable need |

## 4. Discovery Decision

**Proposed decision:** conclude the current investigation and **do not promote** the `README-LICENSE` gap to Solution Shaping or the Product Backlog based on existing evidence.

Preserve:

```text
TPL-DOCUMENTATION v0.1.0
    README-LICENSE
        Requirement Level: Required
        Framework Component Availability: Conceptual
```

No new Components are created, metadata is not changed, the Validator is not modified, and the examined consumers remain unchanged.

This decision is **reversible**. Concluding the experiment does not prohibit future implementation of the Component; it means that such work is not yet authorized.

## 5. Criteria for Reopening the Investigation

Reopen the topic if at least one of the following forms of verifiable evidence emerges:

1. A documentation consumer encounters a specific difficulty applying the contract because the canonical `README-LICENSE` Component is unavailable.
2. Multiple consumers repeatedly need to solve the same problem, revealing a reusable pattern with clear boundaries.
3. A usability test shows recurring confusion among `Required`, `Conceptual`, and `Satisfied`.
4. A representative implementation case demonstrates that materializing `README-LICENSE` delivers greater value than keeping a consumer-specific solution.
5. Design evidence provides a justified reason to question the current requirement level, **independently** of Component availability.

If so, begin **Solution Shaping** explicitly and compare alternatives before committing a Delivery Scope.

## 6. Recommended Priority for Project Evolution

Given the bounded findings of this investigation, the next effort should seek evidence of **actual Framework usage value**, rather than automatically expanding the documentation catalog.

Potential research directions, without a committed implementation order:

| Area | Concrete question | Potential evidence |
|---|---|---|
| Adoption end-to-end | Can a consumer complete Assessment and, where appropriate, Application and Integration using traceable records at reasonable cost? | Observable walkthrough on a small case; explicit human decisions |
| Templates in practice | What manual work must a user repeat when starting from an existing composition? | Actual steps, blockers, repetition, and artifacts used |
| Validator expectations | Do users understand what the CLI validates and which repository it applies to? | Entry-point inspection, controlled execution, and comprehension tasks |
| Pending UX-02 | Does the initial navigation after PR #90 work for new users? | Real participant sessions following protocol #54 |

UX-02 remains **Prepared — Not Executed** until independent participants are available. This need not prevent separate technical investigations.

## 7. Closing Status

| Item | Status |
|---|---|
| Discovery #55 — Functional maturity baseline | Completed |
| Discovery #56 — Materialization reality check | Completed |
| Discovery #57 — External consumer license case | Completed, bounded to one Responsibility |
| Discovery #58 — Synthesis and decision boundary | Completed |
| `README-LICENSE` materialization | Not committed |
| `TPL-DOCUMENTATION` contract changes | Not committed |
| New Product Backlog item | Not created |
| Sprint / milestone / release | None opened for this work |

**Final result:** the evidence supports maintaining the distinction between Component availability and Responsibility coverage, but **does not yet justify any functional modification**. Future work should provide direct evidence of a user need before selecting a solution.

This document is a Discovery synthesis and decision boundary; **it is not a Delivery Scope, implementation plan, code verification, or release approval**.
