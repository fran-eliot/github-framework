# Framework Validator — Publication Decision Packet (Proposal Only)

**Prepared:** 2026-11-15  
**Decision status:** **Pending maintainer review — NOT approved**  
**Published baseline:** [v0.11.0](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0), commit `55680b388b0fd8256c95e15866e53d21cc9a5033`  
**Candidate for review (not selected/approved):** `85cfd9e18c7f13277ad323b7e744ad405809519a`, the `main` merge of [PR #371](https://github.com/fran-eliot/github-framework/pull/371)  
**Potential next identifier:** `v0.12.0` **only if expressly approved**. No tag, release, milestone, Sprint or publication action has been authorized.

This packet offers a bounded decision to the maintainer. It does **not** designate the current branch tip or any later `main` commit as an approved candidate. The candidate is a concrete commit for verification, not an automatic consequence of preparing release notes.

## 1. Scope proposed for evaluation

The [unpublished release-notes draft](framework-validator-candidate-release-notes-unreleased.md) groups post-v0.11.0 improvements:

| Scope | Evidence | Proposed treatment |
| --- | --- | --- |
| Component discovery and catalog operations | Filter/sort/page, summaries, atomic JSON export in [Unreleased CHANGELOG](../../CHANGELOG.md) | Consider for publication as opt-in CLI functionality |
| Saved catalog selection and integrity checks | `--catalog-input`, metadata/file-tree digests, stale snapshot preflight; [practical workflow](../implementation/validator-catalog-workflow.md) | Present as local consistency checking, **not** an authenticated source attestation |
| Framework Validator CI reproducibility | Platform artifacts and strict Ubuntu/Windows catalog parity with bounded diagnostic output | Present as CI evidence for checked-out revisions only |
| Compatibility and safety regression coverage | [CLI/JSON contract](../implementation/validator-compatibility-contract.md), automated tests and smoke | Describe tested guarantees and known compatibility limits |
| Consumer scope study | [Aula Robótica boundary](../implementation/aula-robotica-validator-consumer-boundary-20261115.md) | Include only as a clarification of Validator boundaries, **not** external consumer validation |

**Explicit exclusions:** generic application validation, automatic Existing Repository Adoption decisions, Application/Integration of Only Film or other consumers, signed attestations, atomic filesystem snapshots, universal API/schema compatibility, independent UX-02 evidence, consumer deployment or security certification.

## 2. Verifiable commit-to-commit evidence

An actual GitHub comparison from published-tag commit `55680b388b0fd8256c95e15866e53d21cc9a5033` to the review commit `85cfd9e18c7f13277ad323b7e744ad405809519a` reports:

| Observation | Result |
| --- | --- |
| Comparison | `ahead` |
| Commits ahead | **262** |
| Commits behind | **0** |
| Changed paths | **23** |
| Current publication status | **Unreleased** |

[Open this exact comparison](https://github.com/fran-eliot/github-framework/compare/55680b388b0fd8256c95e15866e53d21cc9a5033...85cfd9e18c7f13277ad323b7e744ad405809519a)

These figures are a commit-level inventory, **not** counts of features or successful tests. The earlier [delta review](framework-validator-v0110-to-main-delta-20261115.md) is an immutable historical comparison at PR #368 (246 commits, 21 paths); it must not be silently replaced or cited as the current candidate comparison.

## 3. CI evidence and what remains open

The [PR #371 run 43759738664](https://github.com/fran-eliot/github-framework/actions/runs/43759738664) completed successfully with:

- Component validation on Ubuntu (Python 3.11): **success**
- Component validation on Windows (Python 3.11): **success**
- Cross-platform Component catalog parity: **success**

**Precision:** this workflow ran for the PR head `d9c1d8adc84675f1fbcc73a46f8b32cc71d5e4aa`, not as proof of tests on the later merge commit `85cfd9e18c7f13277ad323b7e744ad405809519a`. The precise merge candidate requires separately confirmed successful tests for that SHA (for example, a matching push-to-main run), not inference from a prior PR run. This review has not confirmed such a run.

| Gate | Status | Required action |
| --- | --- | --- |
| Scope described and bounded | **Prepared** | Confirm final inclusion/exclusion and compatibility caveats |
| Tag-to-candidate change inventory | **Observed at the review SHA** | Repeat if any different SHA is selected |
| PR test suite and parity | **Passed for the linked PR run** | Verify corresponding exact candidate SHA |
| CI catalog/report artifacts | **Available in the PR workflow subject to retention** | Review candidate-SHA artifacts and provenance limits |
| API/CLI/JSON contract | **Bounded regression coverage** | Decide whether current guarantees meet release expectations |
| Independent external consumer validation | **Not demonstrated** | Decide whether to defer separately; do not assert it was done |
| Publication authorization | **Pending** | Approve version, exact tag target SHA, publication scope and notes explicitly |

## 4. Alternatives for a maintainer decision

**Option A — Authorize a bounded next Validator release, conditionally.**  
Consider `v0.12.0` for the completed **Framework Component Validator** enhancements. Require a confirmed CI pass and artifacts for the approved exact SHA, final review of the release-notes text, and an explicit follow-up authorization **before creating the tag or publishing**. This does not convert any consumer study into Adoption completion.

**Option B — Defer publication and collect additional evidence.**  
Keep all changes Unreleased, with no target version. Prioritize a separately authorized, reproducible read-only exercise using a real **Framework Component library** and check remaining CLI/JSON compatibility risks. Do not change or classify an external consumer without a new, explicitly defined Assessment scope.

**Recommendation for decision-making:** Option A is a reasonable **proposal for review** only if the maintainer accepts the explicitly bounded scope and confirms candidate-specific CI. Option B remains appropriate if external interoperability is required as a release gate. Neither option is silently selected by the existence or merge of this document.

## 5. Approval boundaries

The maintainer must explicitly specify, in a separate decision:

1. **Whether to publish** now, or defer;
2. **Which precise commit SHA** is approved as the tag target;
3. **Which release version** (if any), with `v0.12.0` only a suggestion;
4. **Which final notes** may be published;
5. **Whether to create the tag and GitHub Release**.

Until then, do **not** create tags, releases, milestones, Sprints or automated follow-on publication actions. A merged PR containing this proposal **is not publication approval**.

**Only Film remains unchanged:** documentary Assessment `Complete` only for pinned consumer commit `28d75a50e0a178954dd46acc23300d9dd327843c` against `TPL-BACKEND 0.1.0`. UX-02 remains `Prepared — Not Executed`.

---

**Source discipline:** recheck `main`, open PRs, exact commit CI and release status at the time of any later decision. This document preserves its dated, pinned review baseline instead of asserting that the current `main` always equals the candidate.
