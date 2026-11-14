# Only Film — Consolidated Assessment Human Review Matrix

## 1. Context, purpose, and distinctions

The [Only Film Assessment working record](only-film-assessment.md) now contains all twenty-eight structured Responsibility records: **twenty-eight formally approved** by the maintainer on 2026-11-14 (`README-HERO`, `README-OVERVIEW`, `README-FEATURES`, `README-TECH-STACK`, `README-QUICK-START`, `README-DOCUMENTATION`, `README-FOOTER`, `DOC-CHANGELOG`, `README-STATUS`, `README-ARCHITECTURE`, `README-REPOSITORY-STRUCTURE`, `README-TESTING`, `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS`, `DOC-TESTING`, `DOC-ADR`, `DOC-API`, `DOC-DATABASE`, `DOC-DEPLOYMENT`, `README-ROADMAP`, `README-DEMO`, `README-AUTHOR`, `README-HIGHLIGHTS`, `README-LICENSE`, `DOC-SECURITY`, `README-CONTRIBUTING`, `DOC-DIAGRAMS`, `DOC-REFERENCES`) and **0 still proposed/unapproved**. All twenty-eight have allowed State values, including `Missing` for those two approved records and the approved scoped `DOC-API` classification. `README-CONTRIBUTING` has approved `Not Applicable` based on the confirmed contribution policy, `DOC-DIAGRAMS` has approved `Applicable` based on future diagram interest, and `DOC-API` has approved scoped `Not Applicable` for a current public/programmatic API contract, bounded by the seven-controller review. Full structural coverage does not constitute an approved or completed Assessment. The working Assessment's summary and detail blocks follow canonical `TPL-BACKEND` metadata order for reviewer comparison. This matrix tracks completed State/Applicability approvals and the remaining **Adoption Decision and evidence gates**; it is not a completed Assessment.

This matrix **consolidates** the 28 existing E3 proposals for `TPL-BACKEND` 0.1.0 in a single human-review entry point. It is based on the individual evidence records **without treating those approvals as Adoption Decisions; twenty-eight explicit maintainer approvals are now recorded**. It identifies missing evidence, assigns concrete review gates, and supports subsequent completion of the [Assessment Template](../assessment-template.md).

| Field | Value |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Responsibilities consolidated | `28/28` — **28 approved / 0 proposals** |
| Human-reviewed States and Applicability | **28 approved on 2026-11-14**, 0 pending |
| Resolved Adoption Decisions | `5` (`PRESERVE` for Hero, Overview, Features, Documentation and Footer; 23 unresolved) |
| Assessment Status | `In Progress` |
| Consumer Mutation | `NONE` |

**Legend:**

- All 28 State and Applicability pairs are maintainer-approved on 2026-11-14. Earlier E3 source proposals and alternatives are historical evidence, not unsigned Assessment classifications. `Uncertain` remains an allowed contractual Applicability value if new evidence requires reassessment, but no current approved summary value uses it.
- `P1/P2/P3` prioritize **evidence review**, not confirmed defects, security severity, or mandatory changes to Only Film.
- Each `E3` link opens the underlying record with Detected Facts, Evidence, Evaluation Rationale, Uncertainty, and Decision Status. Original proposals retain `Needs Further Evaluation` and `Adoption Decision: —`.
- Row order and Requirement Levels follow the [canonical Template metadata](../../templates/repositories/backend/metadata.yml), not Component-level priorities.

**First README presentation review batch:** [README presentation — human review batch 1](only-film-readme-presentation-review-batch-1.md) rechecks the pinned README, POM and Compose against the Hero, Overview and Tech Stack Components. Its recommendations were **explicitly approved by the maintainer on 2026-11-14**: `README-HERO: Satisfied / Applicable`, `README-OVERVIEW: Satisfied / Applicable`, and `README-TECH-STACK: Partial / Applicable`. Their documentary limitations remain, and no Adoption Decision was authorized. The preparation packet's original wording is retained as an evidence trail; this matrix and the Assessment record the subsequent approvals.

**Second README content review batch:** [README content — human review batch 2](only-film-readme-content-review-batch-2.md) directly inspects the pinned README, linked technical guides and selected workflows against the Features, Documentation and Footer Components. Its recommendations were **expressly approved by the maintainer on 2026-11-14**: `README-FEATURES: Satisfied / Applicable`, `README-DOCUMENTATION: Partial / Applicable`, and `README-FOOTER: Partial / Applicable`. The review-batch file records the subsequent decision separately from its original preparation notes. Evidence limitations and unresolved Adoption Decisions are retained.

**Required runtime/change-history review batch:** [Quick Start and Changelog — human review batch](only-film-required-runtime-change-review-batch.md) rechecks pinned README, Compose, Dockerfile, environment example and Maven configuration and applies the two Framework Components. Its `README-QUICK-START: Partial / Applicable` and `DOC-CHANGELOG: Missing / Applicable` recommendations were **expressly approved by the Only Film maintainer on 2026-11-14**, with bounded source and unverified Compose-run evidence retained. The original review packet records pre-approval alternatives as history; no consumer action or Adoption Decision follows.

**Testing and security review batch:** [Testing and Security — human review batch](only-film-testing-security-review-batch.md) directly rechecks pinned README, test workflows, PostgreSQL testing, JaCoCo and SonarCloud guides, demo-credential guidance and the earlier historical security audit. The maintainer **explicitly approved `Partial / Applicable` for all three** (`README-TESTING`, `DOC-TESTING`, `DOC-SECURITY`) on 2026-11-14. The source boundaries and the JaCoCo guide/workflow selection discrepancy remain recorded, **not** as failing-test or security findings. No consumer edit is authorized.

**Architecture, status and license review batch:** [Architecture, Project Status and License — human review batch](only-film-architecture-status-license-review-batch.md) compares the pinned README, POM and earlier architecture/functional/maturity audits against the Framework's architecture and project status components. The maintainer **explicitly approved `README-ARCHITECTURE: Satisfied / Applicable` and `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS`, `README-LICENSE: Partial / Applicable` on 2026-11-14**. Historical findings remain separate from current architecture/status; licensing rights remain unverified. The review packet preserves earlier alternatives as its pre-approval evidence record. No Adoption Decision or consumer edit was authorized.

**README status, structure and roadmap review batch:** [README Status, Repository Structure and Roadmap — human review batch](only-film-readme-status-structure-roadmap-review-batch.md) directly checks the pinned README, `TPL-BACKEND` metadata and applicable Status/Roadmap Components, while bounding two historical planning/maturity sources. The maintainer **expressly approved `README-STATUS: Partial / Applicable`, `README-REPOSITORY-STRUCTURE: Satisfied / Applicable` and `README-ROADMAP: Partial / Applicable` on 2026-11-14**. The original preparation alternatives remain in the batch for traceability; historical status and F3 planning are not promoted to current facts, and no Adoption Decision or consumer edit is authorized.

**Demo, author and highlights review batch:** [Demo, Author and Highlights — human review batch](only-film-demo-author-highlights-review-batch.md) revisits directly inspected pinned README content and Framework documentary expectations. The maintainer **expressly approved `README-DEMO: Partial / Applicable`, `README-AUTHOR: Satisfied / Applicable`, and `README-HIGHLIGHTS: Satisfied / Applicable` on 2026-11-14**. Screenshot pixels were not independently inspected, Compose startup was not rerun, academic credits do not establish ownership or licensing rights, and selective test evidence is not complete feature assurance. The review packet retains the preapproval proposals as historical context; no Adoption Decision or consumer edit follows.

**ADR, database and local deployment review batch:** [ADR, Database and Local Deployment — human review batch](only-film-adr-database-deployment-review-batch.md) directly checks pinned Flyway/Dependabot/PostgreSQL guides, Compose/Dockerfile, and the defined Compose smoke workflow. The maintainer **expressly approved `Partial / Applicable` for `DOC-ADR`, `DOC-DATABASE` and `DOC-DEPLOYMENT` on 2026-11-14**, the latter solely for **local, nonproduction Docker Compose**. The upload-volume versus production-durability wording remains an unresolved documentary question, not a confirmed data-loss bug or failed CI. Only `DOC-API` and `DOC-REFERENCES` remain awaiting State/Applicability review. No Adoption Decision or consumer modification is authorized.

**API and references contract-scope review batch:** [API and References — human review batch](only-film-api-references-contract-review-batch.md) rechecks the pinned README, selected MVC controllers and two technical guides against the Framework References Component and earlier bounded source samples. The maintainer **expressly approved `DOC-API: Missing / Not Applicable` and `DOC-REFERENCES: Partial / Not Applicable` on 2026-11-14**, separately approving State and Applicability for each. `DOC-API` is restricted to a **currently supported public/programmatic API contract**; `DOC-REFERENCES` is restricted to a **standalone centralized external-technical-reference catalog**, without excluding contextual source attribution or link maintenance. Neither finding proves repository-wide absence. The preparation alternatives remain available as historical evidence; the Assessment has **28/28 classification pairs approved** but stays `In Progress` with zero Adoption Decisions resolved.

**Required README Adoption Decision review batch 1:** [Hero, Overview, Features and Tech Stack — decision review](only-film-required-readme-adoption-decision-review-batch-1.md) prepared individual options before formal maintainer review. On **2026-11-14**, the maintainer expressly **resolved `README-HERO`, `README-OVERVIEW` and `README-FEATURES` as `PRESERVE`**, while explicitly **retaining `README-TECH-STACK` as `Needs Further Evaluation / —`**. The three `PRESERVE` resolutions concern the documented presentation only, do not verify all runtime/visual behavior and do not authorize changes to Only Film. The batch document retains its preapproval alternatives as historical review provenance.

**Required README Adoption Decision review batch 2:** [Tech Stack, Quick Start, Documentation and Footer — decision review](only-film-required-readme-adoption-decision-review-batch-2.md) was formally reviewed by the maintainer on **2026-11-14**. The maintainer **expressly resolved `README-DOCUMENTATION` and `README-FOOTER` as `PRESERVE`**, while **retaining `README-TECH-STACK` and `README-QUICK-START` as `Needs Further Evaluation / —`**. Documentation navigation was not exhaustively link-checked; Footer preservation does not establish intellectual-property rights or license permissions; a successful pinned-SHA Compose start was not verified. The preparation record retains original candidate language as historical provenance. No consumer change follows.

**Recommended README Adoption Decision review batch 3:** [Status, Architecture, Repository Structure and Testing — decision review](only-film-recommended-readme-adoption-decision-review-batch-1.md) uses the approved classifications and bounded pinned-source evidence. `README-ARCHITECTURE` and `README-REPOSITORY-STRUCTURE` have conditional `PRESERVE` candidates for high-level reader orientation; `README-STATUS` and `README-TESTING` are recommended to remain `Needs Further Evaluation / —` until status/maturity and testing-evidence thresholds are resolved. **The five already approved `PRESERVE` decisions remain the only resolved decisions; no new Adoption Decision is authorized by this preparation packet.**

## 2. Consolidated proposals and next review gates

| Responsibility | Level | Proposed State | Proposed Applicability | Review Priority | Evidence record | Specific review gate |
| --- | --- | --- | --- | --- | --- | --- |
| `README-HERO` | Required | `Satisfied` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-required-identity-semantic-review.md) | Approved from bounded pinned sources; retain evidence limits and unresolved Adoption Decision. |
| `README-OVERVIEW` | Required | `Satisfied` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-required-identity-semantic-review.md) | Approved from bounded pinned sources; retain evidence limits and unresolved Adoption Decision. |
| `README-FEATURES` | Required | `Satisfied` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-required-identity-semantic-review.md) | Approved from pinned documentary evidence; retain stated limitations and unresolved Adoption Decision. |
| `README-TECH-STACK` | Required | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-required-final-semantic-review.md) | Approved from bounded pinned sources; retain evidence limits and unresolved Adoption Decision. |
| `README-QUICK-START` | Required | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P1** | [E3](only-film-required-semantic-review.md) | Maintainer-approved from bounded evidence; retain documented limitations; Adoption Decision unresolved. |
| `README-DOCUMENTATION` | Required | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-required-final-semantic-review.md) | Approved from pinned documentary evidence; retain stated limitations and unresolved Adoption Decision. |
| `README-FOOTER` | Required | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-required-final-semantic-review.md) | Approved from pinned documentary evidence; retain stated limitations and unresolved Adoption Decision. |
| `DOC-CHANGELOG` | Required | `Missing` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P1** | [E3](only-film-required-semantic-review.md) | Maintainer-approved from bounded evidence; retain documented limitations; Adoption Decision unresolved. |
| `README-STATUS` | Recommended | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-recommended-readme-semantic-review.md) | Approved Partial for status/maturity communication; older maturity reference is not current. Adoption Decision unresolved. |
| `README-ARCHITECTURE` | Recommended | `Satisfied` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-recommended-readme-semantic-review.md) | Maintainer-approved high-level principal-flow summary; no complete architecture-conformance claim. Adoption Decision unresolved. |
| `README-REPOSITORY-STRUCTURE` | Recommended | `Satisfied` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-recommended-readme-semantic-review.md) | Approved Satisfied for a useful nonexhaustive directory overview. Adoption Decision unresolved. |
| `README-TESTING` | Recommended | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P1** | [E3](only-film-testing-semantic-review.md) | Maintainer-approved documentary Partial; retain bounded evidence and unresolved Adoption Decision. |
| `DOC-ARCHITECTURE` | Recommended | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-recommended-docs-semantic-review.md) | Maintainer-approved partial current-architecture documentation; earlier audit findings are not current defects. Adoption Decision unresolved. |
| `DOC-PROJECT-STATUS` | Recommended | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-recommended-docs-semantic-review.md) | Maintainer-approved partial status documentation; historical roadmap is not a verified current milestone. Adoption Decision unresolved. |
| `DOC-TESTING` | Recommended | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P1** | [E3](only-film-testing-semantic-review.md) | Maintainer-approved documentary Partial; retain bounded evidence and unresolved Adoption Decision. |
| `README-ROADMAP` | Optional | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-optional-governance-semantic-review.md) | Approved Partial for potential future directions without a verified current phase plan. Adoption Decision unresolved. |
| `README-CONTRIBUTING` | Optional | `Missing` *(approved 2026-11-14)* | `Not Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-optional-governance-semantic-review.md) | Approved for personal/no-external-contribution scope; no consumer mutation. |
| `README-DEMO` | Optional | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Approved Partial: screenshot links and local path exist; visual freshness/Compose demonstration unverified. Adoption Decision unresolved. |
| `README-AUTHOR` | Optional | `Satisfied` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-optional-governance-semantic-review.md) | Approved Satisfied for balanced project-origin/team attribution, not intellectual-property rights. Adoption Decision unresolved. |
| `README-HIGHLIGHTS` | Optional | `Satisfied` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Approved Satisfied for existing distributed feature highlights with simulated-payment and security qualifications. Adoption Decision unresolved. |
| `README-LICENSE` | Optional | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P1** | [E3](only-film-optional-governance-semantic-review.md) | Maintainer-approved partial license-status notice only; copyright and reuse rights remain unverified. Adoption Decision unresolved. |
| `DOC-ADR` | Optional | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-optional-final-semantic-review.md) | Approved documentary `Partial`; current ADR inventory not verified. Adoption Decision unresolved. |
| `DOC-API` | Optional | `Missing` *(approved 2026-11-14)* | `Not Applicable` *(approved 2026-11-14; current public API only)* | **P2** | [E3](only-film-optional-final-semantic-review.md) | Formal approval is limited to documentation of a currently supported public/programmatic API contract; bounded evidence and unresolved Adoption Decision retained. |
| `DOC-DATABASE` | Optional | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P2** | [E3](only-film-optional-final-semantic-review.md) | Approved documentary `Partial`; full schema/model inventory not verified. Adoption Decision unresolved. |
| `DOC-DEPLOYMENT` | Optional | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14; local Compose only)* | **P2** | [E3](only-film-optional-final-semantic-review.md) | Approved documentary `Partial`; local-only scope and smoke/persistence evidence limits. Adoption Decision unresolved. |
| `DOC-SECURITY` | Optional | `Partial` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P1** | [E3](only-film-security-semantic-review.md) | Maintainer-approved documentary Partial; retain bounded evidence and unresolved Adoption Decision. |
| `DOC-DIAGRAMS` | Optional | `Missing` *(approved 2026-11-14)* | `Applicable` *(approved 2026-11-14)* | **P3** | [E3](only-film-optional-showcase-semantic-review.md) | Approved with bounded evidence; future diagram design and source inventory remain separate. |
| `DOC-REFERENCES` | Optional | `Partial` *(approved 2026-11-14)* | `Not Applicable` *(approved 2026-11-14; standalone catalog only)* | **P3** | [E3](only-film-optional-final-semantic-review.md) | Formal approval is limited to a standalone centralized external-technical-reference catalog; bounded evidence and unresolved Adoption Decision retained. |

**Working assessment value counts** — All 28 of the following evaluations are formally approved, with 0 remaining State/Applicability proposals:

| Measure | Count |
| --- | ---: |
| Responsibilities with structured entries | **28/28** |
| `Satisfied` State (approved: Hero, Overview, Features, README Architecture, Repository Structure, Author, Highlights) | **7** |
| `Partial` State (approved or proposed, including approved README Status, Roadmap, Demo, DOC Architecture, Project Status and README License) | **17** |
| `Missing` State (approved: Changelog, Contributing, API, Diagrams) | **4** |
| `Applicable` Applicability (approved or proposed) | **25** |
| `Not Applicable` Applicability (three approved; API and References narrowly scoped) | **3** |
| `Uncertain` Applicability in current working entries | **0** |
| Formally approved State and Applicability evaluations | **28** |
| Still awaiting formal evaluation approval | **0** |
| Resolved Adoption Decisions | **5** (`PRESERVE`; 23 remain open) |

These are **working Assessment counts** rather than conformance scores. Scoped `Not Applicable` for `DOC-API` and `DOC-REFERENCES` is formally approved as separate Applicability values, with the specific documentary scope and source limitations retained.

## 3. Consolidated evidence-quality findings

### E0/E1 — Inventory and documentary exploration

- All **28/28 Template Responsibilities** have been enumerated and associated with reviewed sources or explicit evidence limits. This does **not** establish compliance.
- At the consumer SHA, [GitHub Actions run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) recorded three successful checks. The `h2-regression` log establishes **329 tests, 0 failures, 0 errors, 0 skipped**, including relevant security test classes. Historical JaCoCo report creation/upload and Sonar scanner `ANALYSIS SUCCESSFUL` were observed, **not** a coverage percentage or Quality Gate approval. [E2 source](only-film-verified-surefire-sonar-logs.md).
- The `postgres-schema` check runs a JAR against CI PostgreSQL; it **does not run the README's Docker Compose flow**. No `compose-smoke` check tied directly to the pinned SHA was found in the reviewed results. [Quick Start evidence](only-film-compose-evidence-gap.md).
- Architecture, security, maturity, and roadmap audits use **different base commits**. Their findings cannot automatically be applied to the pinned SHA.
- The [targeted changelog/release review](only-film-changelog-evidence-review.md) supports the **maintainer-approved `Missing / Applicable` `DOC-CHANGELOG` evaluation** based on bounded evidence. The maintainer confirms no tags/releases as of 2026-11-13; **independent tag inventory was not run**. The maintainer approved `Missing / Applicable` on 2026-11-14, with the nonexhaustive equivalent-source and tag-inventory limitations explicitly retained; no Adoption Decision was made.
- The [README license notice](only-film-optional-governance-semantic-review.md) does not itself grant reuse permissions or establish ownership of the academic collaboration.
- Some `TPL-BACKEND` Responsibilities lack independently located Components in the inspected library. This is a **Framework definition issue**, not automatically a consumer defect.

### E2/E3 — Outstanding review work

1. **P1 — Material gates:** `README-QUICK-START` (Compose reproducibility), `DOC-CHANGELOG` (tags, releases, and equivalents), `README-TESTING` and `DOC-TESTING` (coverage and evidence limits), `DOC-SECURITY` (current documentation versus historical findings), and `README-LICENSE` (legal clarity without invented rights).
2. **P2 — Accuracy and context:** API contract or non-applicability, contribution policy, current architecture/status, database documentation, local operations, and navigation.
3. **P3 — Editorial sufficiency:** presentation, demos, highlights, diagrams, ADRs, and references, without requiring additional documents when existing equivalents serve the same function.

These are **review priorities**, not a declaration that every P1 Responsibility is `Partial` or requires an `ADD` decision.

## 4. Procedure for approving the matrix without fabricating decisions

1. **Set reviewer, date, and reference.** Name the approving reviewer and confirm the pinned SHA. To assess a newer consumer `main`, refresh evidence rather than reusing the old snapshot as current.
2. **Resolve remaining alternatives.** Retain the maintainer-approved `Missing / Applicable` on `DOC-CHANGELOG` with its bounded equivalent-source and tag-history limitations; any later source evidence may justify a reassessment. Preserve the approved `Missing` States for `README-CONTRIBUTING` and `DOC-DIAGRAMS`; preserve the approved `DOC-API: Missing / Not Applicable` (present-day public/programmatic contract only) and `DOC-REFERENCES: Partial / Not Applicable` (standalone catalog only) with their evidence limits. `Uncertain` is a supported Applicability value; `Missing / Partial` is not a valid final State.
3. **Evaluate evidence sufficiency.** Ensure each record supports the selected `State` and does not default to `Partial` merely from caution. A documentation Responsibility does not require rerunning every system test, but any operational claim must be scoped accurately.
4. **Record formal Assessment results.** For each Responsibility, enter `State: Satisfied / Partial / Missing`, `Applicability: Applicable / Not Applicable / Uncertain`, `Evidence`, `Evaluation Rationale`, `Uncertainty`, and `Decision Status`. Do not treat proposals as approved facts.
5. **Resolve decisions only when justified.** `Decision Status: Resolved` requires a valid Adoption Decision and rationale. Otherwise keep `Needs Further Evaluation`, `Adoption Decision: —`, and an explicit unresolved question.
6. **Apply the Assessment Template completion check.** The Assessment can become `Complete` even with unresolved decisions, but only after all required fields are recorded and reviewed. Completion does **not** automatically authorize Application or Integration.

## 5. Human reviewer session register

| Field | Value |
| --- | --- |
| Reviewer | Only Film maintainer for all twenty-eight approved State/Applicability entries; Adoption Decisions pending |
| Assessed Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Approval date and scope | 2026-11-14 — twenty-eight explicit State/Applicability approvals; 0 pending |
| Responsibilities with proposed E3 records | `28` |
| Responsibilities with approved evaluations | `28` recorded |
| First recommended set | P1: Quick Start, Changelog, Testing, Security, and License |
| Required next output | Review the 23 unresolved Adoption Decisions separately without authorizing consumer mutations |
| Assessment Status | `In Progress` |

**Outcome:** the matrix reduces evidence fragmentation and makes review priorities explicit. It **does not replace human Assessment**, constitute an Adoption Decision, or modify the consumer.


## 6. Review readiness and handoff gates

The working Assessment has **28/28 structural entries**, but **28/28 contractual State values** (28 approved, 0 proposals) and **28 explicit maintainer approvals**. The tables below describe **questions to decide**, not decisions taken. Approval of State/Applicability is already recorded; a merged PR **does not resolve an Adoption Decision** or authorize changes to the consumer.

### 6.1 Contract and evidence checkpoints

| Checkpoint | Expected review outcome | Current status |
| --- | --- | --- |
| Canonical responsibility coverage | Exactly 8 Required, 7 Recommended, and 13 Optional entries, in Template metadata order | Structured: 28/28; 28 approved and 0 unapproved |
| State contract | Each of 28 entries has an allowed `Satisfied / Partial / Missing` value | **28 approved / 0 proposed** |
| Applicability contract | `Applicable / Not Applicable / Uncertain` with justified scope | All 28 approved; 0 `Uncertain` in current Summary; two carefully scoped `Not Applicable` results |
| Evidence and rationale | Bounded source citation, interpretation, and uncertainty per Responsibility | Approved documentary evaluations retain named source limitations and independent technical questions |
| Decision handling | `Needs Further Evaluation` may retain `Adoption Decision: —`; `Resolved` must have rationale | 5 formally resolved `PRESERVE` with individual rationales; 23 unresolved |
| Reviewer attribution | Named reviewer, reference confirmation, review scope and date | Only Film maintainer, 2026-11-14; immutable consumer SHA recorded |
| Completion | Apply [Assessment Template Completion Check](../assessment-template.md) to reviewed contractual fields | `In Progress` |

### 6.2 Approved State and Applicability outcomes with unresolved evidence gates

| Responsibility | Current working record | Evidence or policy question for reviewer |
| --- | --- | --- |
| `README-CONTRIBUTING` | `Missing / Not Applicable` **maintainer-approved 2026-11-14** | Preserve bounded evidence and no-external-contributions scope; no contribution file or consumer change authorized |
| `DOC-API` | `Missing / Not Applicable` **maintainer-approved 2026-11-14** for current public/programmatic API documentation only | Entry-point inventory remains bounded; revisit if a supported integration contract is identified |
| `DOC-DIAGRAMS` | `Missing / Applicable` **maintainer-approved 2026-11-14** | Preserve nonexhaustive diagram evidence; future scope and any implementation remain separate |
| `DOC-REFERENCES` | `Partial / Not Applicable` **maintainer-approved 2026-11-14** for a standalone external-reference catalog only | In-place sources, link validity and attribution remain relevant; no full URL audit |

The three formerly unselected States have approved `Missing` classifications, with the separate applicability findings and their evidence limits recorded. All 28 State/Applicability pairs have explicit approval, but **no Adoption Decision is resolved**. The Template allows `Uncertain` Applicability if newly discovered facts require reopening a finding; do not infer certainty from sampled negative evidence.

### 6.3 P1 evidence acceptance sequence

| Review sequence | Responsibility | Evidence and acceptance question | Disposition |
| --- | --- | --- | --- |
| 1 | `README-QUICK-START` | [Compose evidence gap](only-film-compose-evidence-gap.md): decide whether static documentary sufficiency is enough, or Q1–Q8 reproduction on the pinned SHA is required | Pending reviewer |
| 2 | `DOC-CHANGELOG` | [Changelog evidence review](only-film-changelog-evidence-review.md): examine equivalence of change records, distinguish Git history from curated change communication, and preserve the maintainer-report versus independent-verification distinction | Pending reviewer |
| 3 | `README-TESTING` / `DOC-TESTING` | [Testing semantic review](only-film-testing-semantic-review.md) and [verified Surefire/JaCoCo/Sonar logs](only-film-verified-surefire-sonar-logs.md): general vs selected commands, workflow triggers and historical artifact/Quality Gate evidence limits | **Maintainer-approved `Partial / Applicable` for both on 2026-11-14; evidence gaps retained** |
| 4 | `DOC-SECURITY` | [Security E3 review](only-film-security-semantic-review.md): current README/credentials documentation, historical audit and bounded controls without a security certification | **Maintainer-approved `Partial / Applicable` on 2026-11-14; evidence gaps retained** |
| 5 | `README-LICENSE` | [Optional governance E3 review](only-film-optional-governance-semantic-review.md): distinguish notice clarity from legal permission, collaborative authorship, and authority to grant reuse rights | Pending reviewer |

**Quick Start review record:** The pinned README, Dockerfile, Compose, `.env.example` and PostgreSQL guide have been reviewed for static consistency. The checked run [39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) establishes three successful checks, including JAR-on-PostgreSQL, **not** a Compose smoke execution for the pinned reference. The reviewer must choose and state the documentary or operational acceptance threshold. If execution is required, use disposable resources, synthetic secrets and the existing **Q1–Q8** protocol. If documentation alone suffices, state the basis for `Satisfied` or describe the specific gap supporting `Partial`.

**Changelog review record:** The pinned README/tree/POM and inspected history do not identify a curated versioned-change record. `CHANGELOG.md` absence at a single path, lack of a Git tag inventory and the earlier empty Releases query have distinct evidence boundaries. The maintainer reported **no tags or Releases on 2026-11-13**; this is not independently verified tag history. `Missing` is the preferred unapproved hypothesis unless a substantive equivalent source is identified; the reviewer must explicitly accept or revise that interpretation.

| Reviewer sign-off item | `README-QUICK-START` | `DOC-CHANGELOG` |
| --- | --- | --- |
| Assessed consumer reference | Pinned SHA; reviewer confirmation pending | Pinned SHA; reviewer confirmation pending |
| Evidence acceptance threshold | Documentation-only vs Q1–Q8 reproduction: **unselected** | Equivalent record and scope: **unconfirmed by reviewer** |
| Proposed State | `Partial`, not approved | `Missing`, not approved |
| Reviewer and review date | Not recorded | Not recorded |
| Formal State approval | **No** | **No** |
| Decision Status / Adoption Decision | `Needs Further Evaluation` / `—` | `Needs Further Evaluation` / `—` |

A documentation Responsibility can be evaluated on documentary evidence without asserting every runtime path was executed. Conversely, if reproducibility is the agreed acceptance criterion, do not replace the required Compose evidence with an unrelated successful job. These gates may be accepted, revised, or deferred only with rationale; a merged PR **does not approve** either State or authorize consumer changes.

### 6.4 Testing evidence and reviewer sign-off

| Evidence dimension | Verified for pinned SHA | Not established by the reviewed evidence |
| --- | --- | --- |
| H2 Surefire regression | `329 tests, 0 failures, 0 errors, 0 skipped` in job `h2-regression` of [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) | Full suite execution or reproduction of generic `./mvnw test` from a clean clone |
| PostgreSQL CI | `postgres-schema` and `PostgreSQL JPA and concurrent checkout` jobs succeeded | Selenium, manual workflow or Docker Compose smoke success at the same SHA |
| JaCoCo | Report generation and historical upload of artifact `jacoco-h2-regression` (ID `12201642997`) appear in logs | XML/HTML contents, numeric coverage percentage, global project coverage |
| SonarCloud | Scanner `ANALYSIS SUCCESSFUL` and JaCoCo import documented; CE task `AaFU8vS6n_jCCWP5LQvY` captured | CE task final status, historical `analysisId`, Quality Gate result |
| Documentary suitability | README and specialized guides exist with scope descriptions | Reviewer acceptance of guidance clarity, correct prerequisites and sufficient navigation |

These observations are from the [Testing E3 review](only-film-testing-semantic-review.md) and [verified run log report](only-film-verified-surefire-sonar-logs.md). A scanner's successful submission is not a passed Quality Gate, and successful selected tests are not a statement that every available suite ran.

| Reviewer sign-off item | `README-TESTING` | `DOC-TESTING` |
| --- | --- | --- |
| Consumer reference | Pinned SHA `28d75a50e0a178954dd46acc23300d9dd327843c` | Pinned SHA `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Review focus | General vs selected commands, manual workflows and bounded run evidence | Specialist PostgreSQL/JaCoCo/Sonar guidance; artifact and Quality Gate gaps |
| Approved State | `Partial` | `Partial` |
| Approved Applicability | `Applicable` | `Applicable` |
| Documentary evidence scope | Incomplete full-suite and clean local reproduction | Unverified coverage percentage/Quality Gate; local vs workflow selection difference |
| Reviewer and date | Only Film maintainer / **2026-11-14** | Only Film maintainer / **2026-11-14** |
| Formal evaluation approval | **Yes** | **Yes** |
| Decision Status / Adoption Decision | `Needs Further Evaluation` / `—` | `Needs Further Evaluation` / `—` |

A reviewer may accept a documentation Responsibility without demanding all tests or metrics, but must record the basis. Unverified Selenium, coverage and Quality Gate results must remain **unknown**, not be converted to passing or failing results.

### 6.5 Security and license evidence acceptance

| Review dimension | Source-supported observation | Boundary or unanswered question |
| --- | --- | --- |
| Current security documentation | Pinned README describes roles, BCrypt, CSRF, image validation, simulated checkout and local deployment limitations; demo-credentials guide discusses secrets | Does this cover the actual user/deployment context and vulnerability reporting expectations? |
| Historical security audit | `SECURITY_HARDENING_AUDIT.md` is dated **2026-10-10**, and states an older baseline | Historical findings cannot automatically be assigned as outstanding defects at the assessed SHA |
| Implemented controls and test evidence | Pinned source review describes authorization, CSRF, upload validation and environment hardening; run [39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) reports 329 selected H2 tests passing, including 40 in five security-relevant classes | No pentest, exhaustive endpoint/third-party dependency audit, full security guarantee or verified Sonar Quality Gate |
| License-status notice | Pinned README acknowledges the academic origin and does not purport to grant an additional license | Whether the notice is sufficient for readers is a **documentary** judgment, not proof of permissions |
| License and ownership provenance | No root `LICENSE`/`LICENCE`/`COPYING` identified in the bounded tree review; POM license fields empty; credits name original collaborators | Rights holders, grant terms and unilateral authority to relicense original contributions **not verified** |

**Security review:** Use the [E3 security review](only-film-security-semantic-review.md), [historical/current reconciliation](only-film-security-testing-reconciliation.md) and [negative test evidence](only-film-negative-security-test-evidence.md) to distinguish the documentary burden from the technical assurance burden. The absence of a standalone `SECURITY.md` or pentest does not alone make the documentation `Partial`. If a vulnerability-reporting path or secrets guidance is materially required but undocumented, record the exact gap, intended audience, and evidence before changing the proposed State.

**License review:** Use the [Optional governance E3 review](only-film-optional-governance-semantic-review.md) and pinned consumer README/POM. Judge whether the existing cautionary note is sufficiently clear. Do not convert `README-LICENSE: Satisfied` into a legal opinion, a confirmed open-source grant, or approval to add a license file. Rights and collaborative attribution require separate authoritative verification.

| Reviewer sign-off item | `DOC-SECURITY` | `README-LICENSE` |
| --- | --- | --- |
| Assessed reference | Pinned SHA; approved with bounded evidence | Pinned SHA; approved with bounded rights evidence |
| State | `Partial` (**approved**) | `Partial` (**approved**) |
| Applicability | `Applicable` (**approved**) | `Applicable` (**approved**) |
| Main acceptance threshold | Partial documentary scope, distinguishing historical and current evidence | Cautious communication of unverified reuse status, **not a legal grant** |
| Specific remaining evidence questions | Historical audit scope, reporting/disclosure guidance, nonexhaustive test evidence | Original collaborators' rights, grant terms and authority to license remain **unverified** |
| Reviewer/date | Only Film maintainer / **2026-11-14** | Only Film maintainer / **2026-11-14** |
| Formal evaluation approval | **Yes** | **Yes** |
| Decision Status / Adoption Decision | `Needs Further Evaluation` / `—` | `Needs Further Evaluation` / `—` |

These are the final two **P1 evidence-disposition gates**. All six P1 Responsibilities have a reviewer-facing evidence gate. `README-QUICK-START`, `DOC-CHANGELOG`, `README-TESTING`, `DOC-TESTING` and `DOC-SECURITY` now have formal maintainer evaluation approval. `README-LICENSE` also received a formal documentary evaluation approval on 2026-11-14, **without any legal license grant or adoption action**.

### 6.6 Optional applicability and State discrimination — reviewer session

**Pinned source spot check:** [Targeted Optional Responsibility Source Spot Check](only-film-optional-contract-spotcheck.md) records three exact CONTRIBUTING/PR-template path lookups, **seven pinned MVC controller files** inspected for controller/response annotations and view-return patterns, four sampled pinned documents checked for diagram markers, and bounded contextual-reference observations. These are **limited evidence checks**, not repository-wide absence findings or approval of any State/Applicability value. No recursive inventory of the pinned controller directory has been established, so no global absence of an API contract is claimed.

This is a **review preparation gate**, not an approval. The prior E3 reviews support only bounded facts: onboarding instructions without a confirmed collaboration policy, MVC interfaces without a confirmed public REST contract, a textual architecture flow without exhaustive embedded-diagram inspection, and references present in context without a confirmed need for an index. Do not infer `Not Applicable` merely because an item is Optional.

| Priority | Responsibility | Evidence to establish | Conditional reviewer conclusion | Status |
| --- | --- | --- | --- | --- |
| P2 | `README-CONTRIBUTING` | Maintainer confirmed personal project without external contributions; pinned evidence describes onboarding, not contributor policy | **Approved `Missing / Not Applicable`** as separate State and Applicability; no contribution file or consumer mutation | **Maintainer-approved 2026-11-14**; Adoption Decision unresolved |
| P2 | `DOC-API` | Seven pinned MVC view controllers inspected; README places REST API in future work. Other routes/consumers not fully inventoried | **Approved `Missing / Not Applicable`** for present-day supported public/programmatic API documentation **only** | **Maintainer-approved 2026-11-14**; no API absence certification; Adoption Decision unresolved |
| P3 | `DOC-DIAGRAMS` | Maintainer confirms future value; nine pinned Markdown documents sampled, with no identified technical diagrams | **Approved `Missing / Applicable`**, expressly bounded by nonexhaustive inspection; future diagram choice remains open | **Maintainer-approved 2026-11-14**; Adoption Decision unresolved |
| P3 | `DOC-REFERENCES` | [Seven-file pinned link inventory](only-film-optional-contract-spotcheck.md): contextual links, no demonstrated need for centralized external-reference catalog in sample | **Approved `Partial / Not Applicable`** only for a standalone centralized external-reference catalog, never in-place sources | **Maintainer-approved 2026-11-14**; link validation and Adoption Decision unresolved |

**DOC-API approved evidence boundary:** On 2026-11-14, the maintainer approved `Missing / Not Applicable` for current public/programmatic API-contract documentation, **not** as a claim that all programmatic interfaces are absent. The seven-controller MVC sample and future-REST README wording are bounded evidence; a later supported API contract warrants reassessment. No OpenAPI document or endpoint is authorized. [Pinned controller evidence](only-film-optional-contract-spotcheck.md).

**Evidence-led Optional recommendations:** The maintainer confirmed on 2026-11-14 that Only Film is personal and does not accept external contributions. The maintainer **formally approved `README-CONTRIBUTING: Missing / Not Applicable` on 2026-11-14** as separate State/Applicability values. The maintainer also confirmed interest in future technical diagrams, and **formally approved `DOC-DIAGRAMS: Missing / Applicable` on 2026-11-14**, expressly retaining the nonexhaustive diagram-source limitation. These **two evaluations are approved**, like all remaining State/Applicability classifications; no Adoption Decision or consumer edit is authorized. See [source details](only-film-optional-contract-spotcheck.md).

**DOC-REFERENCES approved evidence boundary:** On 2026-11-14, the maintainer approved `Partial / Not Applicable` **only for a standalone centralized technical-reference catalog**. The Component permits contextual references and does not waive their relevance, accuracy, attribution or maintenance. Seven-file sampling does not establish the full external link inventory; no catalog is authorized. [Detailed inventory](only-film-optional-contract-spotcheck.md).

**Acceptance protocol:** Record the exact pinned reference, evidence checked, intended reader/use case, chosen allowed `State` (`Satisfied`, `Partial`, or `Missing`), supported `Applicability` (`Applicable`, `Not Applicable`, or `Uncertain`), rationale, reviewer and date. `Uncertain` is a supported final Applicability **when justified**; leaving State unselected is **not** sufficient for a completed Assessment. Resolving these fields must not be confused with authorizing `ADD`, `ADAPT`, `PRESERVE`, `ACCEPT` or `OMIT`.

| Reviewer sign-off | `README-CONTRIBUTING` | `DOC-API` | `DOC-DIAGRAMS` | `DOC-REFERENCES` |
| --- | --- | --- | --- | --- |
| Evidence scope | Personal project contribution policy; bounded docs | Current public/programmatic contract, not full routing audit | Bounded technical-diagram inventory | Standalone catalog, not contextual source maintenance |
| State | `Missing` (**approved**) | `Missing` (**approved**) | `Missing` (**approved**) | `Partial` (**approved**) |
| Applicability | `Not Applicable` (**approved**) | `Not Applicable` (**approved; scoped**) | `Applicable` (**approved**) | `Not Applicable` (**approved; scoped**) |
| Reviewer/date | Only Film maintainer / 2026-11-14 | Only Film maintainer / 2026-11-14 | Only Film maintainer / 2026-11-14 | Only Film maintainer / 2026-11-14 |
| Adoption Decision | `—` | `—` | `—` | `—` |

### 6.7 Review recording protocol

For each Responsibility, a reviewer should confirm the pinned reference, inspect the minimum linked evidence, and **explicitly approve or revise** State, Applicability, and Evaluation Rationale. Record the reviewer and date on the Assessment (or a directly linked review record) before counting an evaluation as approved. Leave `Decision Status: Needs Further Evaluation` and `Adoption Decision: —` when no adoption action has been authorized.

All 28 State and Applicability pairs have formally approved values. A future `Complete` status must be judged separately under the [Completion Check](../assessment-template.md); **23 Adoption Decisions remain unresolved** and none is authorized by this approval. That status does not authorize modifications to Only Film or imply conformance certification.
