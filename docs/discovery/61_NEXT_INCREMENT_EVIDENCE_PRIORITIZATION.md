# 61 — Next Increment Evidence Prioritization

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Date | 2026-11-14 |
| Phase | Discovery — evidence-informed priority proposal |
| Last published release | `v0.10.0` |
| Active Sprint / milestone / target release | **None committed** |
| Consumer modifications | **None** |
| Solution Shaping / Delivery Scope | **Not opened by this review** |
| Decision authority | Maintainer review required for any future commitment |

> This proposal identifies the next **question worth validating**. It is not a new implementation plan, an approved user study, a consumer Application authorization or a commitment to deliver a release.

## 1. Sources and current evidence

| Source | What it establishes | What it does not establish |
| --- | --- | --- |
| [Product Backlog](../governance/14_BACKLOG.md) | Practical use by consumers remains a proposed, uncommitted priority; post-`v0.10.0` Validator changes are Unreleased. | An approved next Sprint, release or feature scope. |
| [Functional Maturity synthesis #58](58_FUNCTIONAL_MATURITY_DISCOVERY_SYNTHESIS.md) | Template responsibilities, Component availability and consumer coverage are distinct; the single `README-LICENSE` materialization gap is not enough to prioritize a new canonical Component. | User harm, repeated demand or a justified Validator/generator extension. |
| [First-Time Experience #53](53_FIRST_TIME_USER_EXPERIENCE_DISCOVERY.md) | A **document-inspection / internal walkthrough** identified navigation questions and preserved the Fact / Evidence / Evaluation / Decision boundary. | Behavior, task success, time or difficulty of unfamiliar real participants. |
| [UX-02 protocol #54](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md) | A ready observational protocol for a proposed **2–3 independent developers**, with tasks and evidence capture. Its status is **Prepared — Not Executed**. | Any actual session, participant result, measured difficulty or validation success. |
| [End-to-End feasibility #59](59_ADOPTION_END_TO_END_FEASIBILITY_CHECK.md) | A one-Responsibility SeniorMeet review stops safely before Application while its Adoption Decision is unresolved. | A completed SeniorMeet Assessment, consumer change or end-to-end run. |
| [End-to-End reconciliation #60](60_ADOPTION_END_TO_END_EVIDENCE_RECONCILIATION.md) | Two historical `dental-back-spring` Application/Integration cases have **merged PRs**; their scope and historical verification provenance are documented. | A newly executed flow, independent usability evidence or a universal efficiency claim. |
| [Only Film completed Assessment](../../framework/adoption/examples/only-film-assessment.md) | Formal documentary completion for 28/28 approved classifications and 28/28 resolved decisions. | Consumer Application or Integration authorization, production certification or full operational test evidence. |

**Completed documentary consumer case:** the [Only Film Assessment](../../framework/adoption/examples/only-film-assessment.md) was formally approved `Complete` on 2026-11-14 for `fran-eliot/only_film` at `28d75a50e0a178954dd46acc23300d9dd327843c` against `TPL-BACKEND 0.1.0`. It has **28/28 classified Responsibilities and 28/28 resolved Adoption Decisions**, with all evidence limits retained. Only Film was not modified or authorized for Application/Integration.

## 2. Candidate next priorities

| Candidate | Supporting evidence | Missing evidence / readiness | Proposed disposition |
| --- | --- | --- | --- |
| **A. Independent first-time Assessment usability, UX-02** | #53 identifies navigation/comprehension questions; #54 supplies a reproducible, bounded protocol. | Independent participants, observed task notes and explicit findings are unavailable. | **First evidence-gathering priority when participants are available**; remain `Prepared — Not Executed` until then. |
| **B. Independent Assessment → Application → Integration usability and effort** | #60 confirms historical merged `MODIFY` and `CREATE` consumer cases; Only Film provides a complete documentary Assessment with resolved choices. | Independent participant, separately authorized consumer/change boundaries, verified candidate and stable-state review. | **Second research candidate, subject to distinct authorization**. No consumer or write permission is selected here. |
| **C. Canonical `README-LICENSE` Component materialization** | #58 documents one `TPL-DOCUMENTATION` required/Conceptual gap. | Repeated actual consumer friction or independently observed difficulty. | **Defer implementation** until the #58 reopening criteria are met. |
| **D. Additional Validator functionality or automatic semantic adoption** | The Validator has useful post-release deterministic additions recorded in the backlog. | Demonstrated, repeatable user need for another extension and a bounded contract. | **No new tooling scope selected**; automatic semantic decisions remain excluded. |
| **E. Additional Only Film `ADAPT`/`ADD` execution** | Only Film has 9 `ADAPT` and 2 `ADD` decisions, limited to future justified documentation. | Independent Application authorization, current consumer baseline, Evidence Refresh, a reviewed Change Set and verification plan. | **Not selected**; Assessment completion is not permission to implement. |

## 3. Recommended evidence-first sequence

**Proposed next research question:** Can a developer who has not previously used GitHub Framework find the Repository Template and Assessment entry point, create a bounded evidence-based starting record, and explain the distinction between facts, evidence, State and Adoption Decision without direct path hints?

1. **Keep UX-02 `Prepared — Not Executed`** unless real independent participants are available. Follow the already published [protocol #54](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md); do not substitute internal walkthrough notes for external sessions.
2. If sessions occur under a **separate study decision**, record observed tasks, blockers, assistance and quotations actually given, without inventing metrics or generalizing a small sample.
3. Review the findings **before** selecting a documentation navigation change, new Component, CLI extension, assisted workflow or Solution Shaping scope. `NO CHANGE` is a legitimate outcome.
4. Evaluate a distinct end-to-end, participant-observed case **only if explicitly authorized**, with approved Assessment/Decision, a bounded Application Plan, candidate verification, and an Integration review under consumer governance.
5. If participants are not available, leave UX-02 pending and select a **different demonstrable need**. Do not treat another internal documentary replay as a substitute for independent usability evidence.

## 4. Decision gates and boundaries

**This document proposes a research priority, not an approved execution.** The following are not authorized or implied:

- Recruiting, scheduling or claiming participants were observed;
- Starting or completing UX-02;
- Opening Solution Shaping, Delivery Scope, Sprint, milestone, target version or release;
- Changing `TPL-DOCUMENTATION`, creating a `README-LICENSE` Component, extending Validator behavior or automating semantic assessment;
- Any modification, test execution, deployment, Application or Integration in Only Film, SeniorMeet, `dental-back-spring` or another consumer.

Maintainer review should separately determine whether to seek independent UX-02 participants, choose another bounded technical question, or postpone new research. **No next increment is committed by merging this proposal.**
