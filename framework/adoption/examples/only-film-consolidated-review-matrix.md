# Only Film — Consolidated Assessment Human Review Matrix

## 1. Context, purpose, and distinctions

The [Only Film Assessment working record](only-film-assessment.md) now contains twenty structured, **unapproved** Responsibility records: eighteen with a proposed State, and two (`README-CONTRIBUTING`, `DOC-API`) with State intentionally unselected and Applicability `Uncertain` pending review. This is incomplete assessment coverage, not twenty approved evaluations. This matrix continues to track the remaining proposals and review gates; it is not the completed Assessment.

This matrix **consolidates** the 28 existing E3 proposals for `TPL-BACKEND` 0.1.0 in a single human-review entry point. It is based on the individual evidence records **without promoting hypotheses to evaluated States or recording human approval**. It identifies missing evidence, assigns concrete review gates, and supports subsequent completion of the [Assessment Template](../assessment-template.md).

| Field | Value |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Proposals consolidated | `28/28` — **not approved** |
| Human-reviewed States and Applicability | **0 approved in these records** |
| Resolved Adoption Decisions | `0` |
| Assessment Status | `In Progress` |
| Consumer Mutation | `NONE` |

**Legend:**

- `Proposed State` and `Proposed Applicability` are **reviewer-facing hypotheses**, not approved Assessment fields. `Missing / Partial` identifies alternatives not yet discriminated; it is **not** a contractual `State`. `Uncertain` for Applicability preserves an unresolved question rather than claiming `Not Applicable`.
- `P1/P2/P3` prioritize **evidence review**, not confirmed defects, security severity, or mandatory changes to Only Film.
- Each `E3` link opens the underlying record with Detected Facts, Evidence, Evaluation Rationale, Uncertainty, and Decision Status. Original proposals retain `Needs Further Evaluation` and `Adoption Decision: —`.
- Row order and Requirement Levels follow the [canonical Template metadata](../../templates/repositories/backend/metadata.yml), not Component-level priorities.

## 2. Consolidated proposals and next review gates

| Responsibility | Level | Proposed State | Proposed Applicability | Review Priority | Evidence record | Specific review gate |
| --- | --- | --- | --- | --- | --- | --- |
| `README-HERO` | Required | `Partial` | `Applicable` | **P3** | [E3](only-film-required-identity-semantic-review.md) | Check heading, badges, and readability; decide whether identity is conveyed sufficiently. |
| `README-OVERVIEW` | Required | `Partial` | `Applicable` | **P3** | [E3](only-film-required-identity-semantic-review.md) | Evaluate clarity of purpose and distinction from Hero. |
| `README-FEATURES` | Required | `Partial` | `Applicable` | **P2** | [E3](only-film-required-identity-semantic-review.md) | Validate capability claims and distinguish them from implementation details. |
| `README-TECH-STACK` | Required | `Partial` | `Applicable` | **P3** | [E3](only-film-required-final-semantic-review.md) | Cross-check key technologies and use contexts against POM/Compose. |
| `README-QUICK-START` | Required | `Partial` | `Applicable` | **P1** | [E3](only-film-required-semantic-review.md) | Reproduce Compose from a clean clone or justify a documentary threshold; gates Q1–Q8. |
| `README-DOCUMENTATION` | Required | `Partial` | `Applicable` | **P2** | [E3](only-film-required-final-semantic-review.md) | Check key links and discoverability of useful documentation. |
| `README-FOOTER` | Required | `Partial` | `Applicable` | **P2** | [E3](only-film-required-final-semantic-review.md) | Evaluate attribution and license notices without asserting legal permissions. |
| `DOC-CHANGELOG` | Required | `Missing` *(proposed; not approved)* | `Applicable` | **P1** | [E3](only-film-required-semantic-review.md) | Maintainer confirms no tags/releases (2026-11-13); review any equivalent change record and approve or revise `Missing` in the formal Assessment. |
| `README-STATUS` | Recommended | `Partial` | `Applicable` | **P2** | [E3](only-film-recommended-readme-semantic-review.md) | Establish repository maturity at the pinned SHA; do not confuse technology badges with status. |
| `README-ARCHITECTURE` | Recommended | `Partial` | `Applicable` | **P2** | [E3](only-film-recommended-readme-semantic-review.md) | Reconcile MVC/JPA overview with code and dated audit material. |
| `README-REPOSITORY-STRUCTURE` | Recommended | `Partial` | `Applicable` | **P3** | [E3](only-film-recommended-readme-semantic-review.md) | Check tree accuracy and navigability. |
| `README-TESTING` | Recommended | `Partial` | `Applicable` | **P1** | [E3](only-film-testing-semantic-review.md) | Reconcile local commands and CI; distinguish H2, PostgreSQL, Selenium, and JaCoCo. |
| `DOC-ARCHITECTURE` | Recommended | `Partial` | `Applicable` | **P2** | [E3](only-film-recommended-docs-semantic-review.md) | Identify the current architecture; do not treat historical audit findings as automatically current. |
| `DOC-PROJECT-STATUS` | Recommended | `Partial` | `Applicable` | **P2** | [E3](only-film-recommended-docs-semantic-review.md) | Reconstruct milestones and status by area using dated references. |
| `DOC-TESTING` | Recommended | `Partial` | `Applicable` | **P1** | [E3](only-film-testing-semantic-review.md) | Assess guidance, Surefire CI evidence, coverage, and Sonar limitations. |
| `README-ROADMAP` | Optional | `Partial` | `Applicable` | **P3** | [E3](only-film-optional-governance-semantic-review.md) | Check currency of F3 proposals and whether a concise summary suffices. |
| `README-CONTRIBUTING` | Optional | `Missing / Partial` | `Uncertain` | **P2** | [E3](only-film-optional-governance-semantic-review.md) | Determine collaboration policy and sources; decide Applicability and State. |
| `README-DEMO` | Optional | `Partial` | `Applicable` | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Check screenshot representativeness and whether reproducible demo access is needed. |
| `README-AUTHOR` | Optional | `Partial` | `Applicable` | **P2** | [E3](only-film-optional-governance-semantic-review.md) | Review team attribution and later development without presuming ownership rights. |
| `README-HIGHLIGHTS` | Optional | `Partial` | `Applicable` | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Evaluate editorial value of highlights without duplicating Features. |
| `README-LICENSE` | Optional | `Partial` | `Applicable` | **P1** | [E3](only-film-optional-governance-semantic-review.md) | Clarify rights/use from appropriate sources without granting a license. |
| `DOC-ADR` | Optional | `Partial` | `Applicable` | **P3** | [E3](only-film-optional-final-semantic-review.md) | Evaluate documented decisions and the value of an ADR log versus redundancy. |
| `DOC-API` | Optional | `Missing / Partial` | `Uncertain` | **P2** | [E3](only-film-optional-final-semantic-review.md) | Check for a public API contract; do not conflate MVC with REST. |
| `DOC-DATABASE` | Optional | `Partial` | `Applicable` | **P2** | [E3](only-film-optional-final-semantic-review.md) | Evaluate data model, invariants, and migrations against pinned sources. |
| `DOC-DEPLOYMENT` | Optional | `Partial` | `Applicable` | **P2** | [E3](only-film-optional-final-semantic-review.md) | Delimit local use; clarify uploads guidance and Compose evidence. |
| `DOC-SECURITY` | Optional | `Partial` | `Applicable` | **P1** | [E3](only-film-security-semantic-review.md) | Review current security guidance and controls; 329 tests do not establish full security assurance. |
| `DOC-DIAGRAMS` | Optional | `Missing / Partial` | `Uncertain` | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Search for embedded diagrams and evaluate applicability before recommending additions. |
| `DOC-REFERENCES` | Optional | `Partial` | `Uncertain` | **P3** | [E3](only-film-optional-final-semantic-review.md) | Decide whether distributed references suffice or an index adds value. |

**Hypothesis counts** — do **not** copy these as approved assessment results:

| Measure | Count |
| --- | ---: |
| E3 proposals referenced | **28/28** |
| `Partial` as the sole State hypothesis | **24** |
| `Missing` as the preferred State hypothesis (`DOC-CHANGELOG`) | **1** |
| Undiscriminated `Missing / Partial` State | **3** |
| `Applicable` as proposed Applicability | **24** |
| Pending / `Uncertain` Applicability | **4** |
| Formally approved States | **0 recorded** |
| Resolved Adoption Decisions | **0 recorded** |

The absence of recorded approvals refers to **this Assessment**, not to possible external reviews absent from these records.

## 3. Consolidated evidence-quality findings

### E0/E1 — Inventory and documentary exploration

- All **28/28 Template Responsibilities** have been enumerated and associated with reviewed sources or explicit evidence limits. This does **not** establish compliance.
- At the consumer SHA, [GitHub Actions run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) recorded three successful checks. The `h2-regression` log establishes **329 tests, 0 failures, 0 errors, 0 skipped**, including relevant security test classes. Historical JaCoCo report creation/upload and Sonar scanner `ANALYSIS SUCCESSFUL` were observed, **not** a coverage percentage or Quality Gate approval. [E2 source](only-film-verified-surefire-sonar-logs.md).
- The `postgres-schema` check runs a JAR against CI PostgreSQL; it **does not run the README's Docker Compose flow**. No `compose-smoke` check tied directly to the pinned SHA was found in the reviewed results. [Quick Start evidence](only-film-compose-evidence-gap.md).
- Architecture, security, maturity, and roadmap audits use **different base commits**. Their findings cannot automatically be applied to the pinned SHA.
- The [targeted changelog/release review](only-film-changelog-evidence-review.md) favors `Missing` as an **unapproved** `DOC-CHANGELOG` hypothesis. The maintainer confirms no tags/releases as of 2026-11-13; **independent tag inventory was not run**. Formal State approval and equivalent-source review remain open.
- The [README license notice](only-film-optional-governance-semantic-review.md) does not itself grant reuse permissions or establish ownership of the academic collaboration.
- Some `TPL-BACKEND` Responsibilities lack independently located Components in the inspected library. This is a **Framework definition issue**, not automatically a consumer defect.

### E2/E3 — Outstanding review work

1. **P1 — Material gates:** `README-QUICK-START` (Compose reproducibility), `DOC-CHANGELOG` (tags, releases, and equivalents), `README-TESTING` and `DOC-TESTING` (coverage and evidence limits), `DOC-SECURITY` (current documentation versus historical findings), and `README-LICENSE` (legal clarity without invented rights).
2. **P2 — Accuracy and context:** API contract or non-applicability, contribution policy, current architecture/status, database documentation, local operations, and navigation.
3. **P3 — Editorial sufficiency:** presentation, demos, highlights, diagrams, ADRs, and references, without requiring additional documents when existing equivalents serve the same function.

These are **review priorities**, not a declaration that every P1 Responsibility is `Partial` or requires an `ADD` decision.

## 4. Procedure for approving the matrix without fabricating decisions

1. **Set reviewer, date, and reference.** Name the approving reviewer and confirm the pinned SHA. To assess a newer consumer `main`, refresh evidence rather than reusing the old snapshot as current.
2. **Resolve remaining alternatives.** Use the maintainer confirmation of no tags/releases to review the proposed `Missing` on `DOC-CHANGELOG`, checking any specific equivalent source before approval. Distinguish `Missing / Partial` for `README-CONTRIBUTING`, `DOC-API`, and `DOC-DIAGRAMS`; decide Applicability for `DOC-REFERENCES`. `Uncertain` is a supported Applicability value; `Missing / Partial` is not a valid final State.
3. **Evaluate evidence sufficiency.** Ensure each record supports the selected `State` and does not default to `Partial` merely from caution. A documentation Responsibility does not require rerunning every system test, but any operational claim must be scoped accurately.
4. **Record formal Assessment results.** For each Responsibility, enter `State: Satisfied / Partial / Missing`, `Applicability: Applicable / Not Applicable / Uncertain`, `Evidence`, `Evaluation Rationale`, `Uncertainty`, and `Decision Status`. Do not treat proposals as approved facts.
5. **Resolve decisions only when justified.** `Decision Status: Resolved` requires a valid Adoption Decision and rationale. Otherwise keep `Needs Further Evaluation`, `Adoption Decision: —`, and an explicit unresolved question.
6. **Apply the Assessment Template completion check.** The Assessment can become `Complete` even with unresolved decisions, but only after all required fields are recorded and reviewed. Completion does **not** automatically authorize Application or Integration.

## 5. Human reviewer session register

| Field | Value |
| --- | --- |
| Reviewer | Not assigned |
| Accepted Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` (proposed) |
| Approval date and scope | Pending |
| Responsibilities with proposed E3 records | `28` |
| Responsibilities with approved evaluations | `0` recorded |
| First recommended set | P1: Quick Start, Changelog, Testing, Security, and License |
| Required next output | Update a genuine [Assessment Template](../assessment-template.md) record with reviewer-approved State, Applicability, and rationale |
| Assessment Status | `In Progress` |

**Outcome:** the matrix reduces evidence fragmentation and makes review priorities explicit. It **does not replace human Assessment**, constitute an Adoption Decision, or modify the consumer.
