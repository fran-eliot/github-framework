# Only Film — Pinned Changelog and Release Evidence Review

## 1. Context and objective

This **E2 evidence-quality review** concerns `DOC-CHANGELOG`, a `Required` Responsibility of `TPL-BACKEND` 0.1.0. It does not constitute an approved semantic classification or an Adoption Decision.

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Responsibility | `DOC-CHANGELOG` (`Required`) |
| Method | Read-only inspection of the Git tree, README, POM, accessible commits, and GitHub Releases |
| Assessment Status | `In Progress` |
| Consumer Mutation | `NONE` |

**Question:** Is there a source documenting changes *published between versions* that fulfills the `DOC-CHANGELOG` Responsibility, even if it is not named `CHANGELOG.md`?

The [DOC-CHANGELOG Component](../../components/documentation/changelog/README.md) distinguishes a changelog from exhaustive Git history, pull requests, issues, release notes, and project status. A canonical filename is neither mandatory nor sufficient evidence of Responsibility satisfaction.

## 2. Checks performed and sources

| Check | Observation | Scope and limitations |
| --- | --- | --- |
| Git tree at the pinned SHA | No paths were identified with names containing `changelog`, `changes`, `history`, or `release` | Filename inspection, not a complete semantic audit of document contents |
| README at the pinned SHA | Explains technical evolution, academic origins, and future work; points to Git history and PRs for change attribution | No version-by-version list of published changes in the inspected sections |
| POM at the pinned SHA | Project version `0.0.1-SNAPSHOT`; Spring Boot parent `4.0.5` | Neither a development artifact version nor a dependency version establishes a release history |
| Functional audit | `docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md` contains roadmap information and historical findings | Not shown to be the official record of published changes |
| Git history up to the SHA | Feature and test commits and merged PRs, including #493, #491, and #489, appeared among 30 recent commits inspected | Development activity does not prove version publication |
| GitHub Releases | An earlier review obtained an empty list from the releases endpoint | This is a time-dependent endpoint result, not proof that no releases ever existed |
| Tags | **Not verified:** the prior tag query was rejected by available access restrictions | Do **not** conclude that tags are absent |

**Sources pinned to the consumer commit:**

- [README.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Functional audit and roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [Repository tree at the pinned SHA](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [Git history up to the pinned SHA](https://github.com/fran-eliot/only_film/commits/28d75a50e0a178954dd46acc23300d9dd327843c/)
- [Current GitHub Releases page](https://github.com/fran-eliot/only_film/releases) — a **mutable** resource, not evidence pinned to the consumer SHA

## 3. Bounded interpretation

The versioned files, Git history, and PRs **do** enable tracing individual development changes. However, the inspected sources have **not identified** a consolidated, user-facing record explaining which relevant changes were published in each version.

This does **not**, by itself, establish an approved `State: Missing`, because two questions remain:

1. **Alternative sources:** tags, external release notes, equivalent documentation, or a versioning policy might exist outside the reviewed material.
2. **Suitability and applicability:** the reviewer must establish the consumer's audience and the level of change communication needed for a `Required` Responsibility.

Do not reconstruct release notes from commits and misrepresent them as officially published versions. Likewise, do not automatically prescribe a new `CHANGELOG.md` before examining existing equivalents.

## 4. Checks required for semantic review

| Gate | Review action | Observable acceptance criterion |
| --- | --- | --- |
| C1 — Tags | Inspect tags reachable from the pinned commit, including reference destinations and dates | Verifiable record with explicit historical/snapshot scope |
| C2 — Releases | Recheck publications and release notes, separating current API state from history at the pinned SHA | Versions, dates, contents, and commit association where available |
| C3 — Equivalent source | Look for curated change records beyond raw Git history and PR listings | Evidence of a source recording relevant versioned changes, or an explicit scoped finding that none was identified |
| C4 — Version policy | Examine whether `0.0.1-SNAPSHOT` represents development only or whether a formal publication process exists | Evidence-backed interpretation, with no inferred releases |
| C5 — Consumer context | Identify users, maintainers, and change-communication requirements | Rationale for Applicability and the Responsibility's expected scope |
| C6 — Individual assessment | Record `State`, `Applicability`, `Evidence`, `Evaluation Rationale`, `Uncertainty`, and `Decision Status` in the Assessment | Named reviewer and traceable reasoning; Adoption Decision only when justified |

Record the verification date and reference before using any newly discovered tags, releases, or equivalent documents in the assessment.

The [provisional E3 review](only-film-required-semantic-review.md) now prefers `Missing` as an **unapproved hypothesis**, while preserving the open tag check.

## 5. Assessment implications

| Field | Result |
| --- | --- |
| Requirement Level | `Required` under TPL-BACKEND 0.1.0 |
| Canonical Changelog file | Not identified among inspected paths |
| Technical change history | Available through accessible commits and PRs |
| Version-published changes | Not established in inspected sources |
| GitHub Releases | Earlier endpoint query returned an empty list |
| Tags | Not verified |
| Proposed State | `Missing` — **unapproved E3 hypothesis** |
| Proposed Applicability | `Applicable` — pending human review |
| Decision Status | `Needs Further Evaluation` |
| Adoption Decision | `—` |
| Assessment Status | `In Progress` |

**Outcome:** the evidence narrows the alternatives but does not close the Responsibility, authorize consumer changes, or make the overall Assessment `Complete`.

## 6. Targeted DOC-CHANGELOG review — 2026-11-12

This update revisits the sources **without changing the pinned consumer reference** (`28d75a50e0a178954dd46acc23300d9dd327843c`). Observations, access limitations, and semantic judgment remain separate.

| Source / gate | Observation and limitation |
| --- | --- |
| `CHANGELOG.md` at the pinned SHA | Direct file lookup returned `404 Not Found`; this establishes absence of **that exact path only** |
| Pinned README | The "Origin, credits and evolution" section refers to commits and PRs for attribution, but does not list **published changes grouped by version** |
| GitHub Releases | The earlier E2 review recorded an empty endpoint response. An independent recheck on 2026-11-12 could not be completed with available tools; the earlier observation is **not** presented as a fresh result |
| Tags (C1) | **Still unverified:** public-access and remote Git attempts did not return a usable tag inventory. **Do not claim that no tags exist** |
| Git history and `0.0.1-SNAPSHOT` | Show development activity and an artifact version; neither replaces a curated change record nor proves published releases |

### Bounded semantic proposal

- **Proposed State: `Missing`** (**E3 hypothesis**, not an approved `State`). No version-oriented changelog or equivalent distributed implementation was identified in the sources inspected. `Partial` would require an actual source recording at least some versioned changes, not merely a commit or PR list.
- **Proposed Applicability: `Applicable`** (human review pending), given the Template's `Required` Responsibility and the benefit of explaining the project's evolution. This does not mandate a release schedule.
- **Decision Status: `Needs Further Evaluation`**; **Adoption Decision: `—`**. Do not prescribe creating `CHANGELOG.md` until equivalent sources and the consumer's needs have been reviewed.

**Final approval gate:** the reviewer must inspect [tags](https://github.com/fran-eliot/only_film/tags), [releases](https://github.com/fran-eliot/only_film/releases), and any alternative versioned-change source. Record the date, reference, and findings. If a substantive source exists, reconsider `Missing` against `Partial` and `Satisfied`. Otherwise, `Missing` remains the best-supported proposal. This is a **Responsibility review**, not a modification to Only Film.
