# Only Film — TPL-BACKEND Assessment (Working Record)

> Partial, human-reviewable Assessment record based on the [Existing Repository Adoption Assessment Template](../assessment-template.md).
> This document is the **Assessment working artifact**, not an additional discovery report or an approval of all 28 Responsibilities.

---

## 1. Assessment Context

| Field | Value |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Repository Template | `TPL-BACKEND` |
| Template Version | `0.1.0` |
| Assessment Record Started | `2026-11-13` |
| Assessment Status | `In Progress` |
| Human Review | Pending for the individual recorded State and Applicability |
| Consumer Mutation | `NONE` |

This pinned consumer reference is the evaluation baseline. Repository-wide facts outside the commit, such as the existence of GitHub tags and Releases, have separately identified provenance and verification limits.

## 2. Assessment Summary — Partial Record

| Responsibility | Requirement Level | State | Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-QUICK-START` | Required | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-CHANGELOG` | Required | `Missing` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-TESTING` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-TESTING` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-ARCHITECTURE` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-PROJECT-STATUS` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-STATUS` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-ARCHITECTURE` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-LICENSE` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-SECURITY` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |

**Coverage:** ten Responsibilities have completed **proposed assessment entries**; the other **18/28** have not been formally recorded in this working artifact. The [28-Responsibility review matrix](only-film-consolidated-review-matrix.md) contains hypotheses and review priorities for the remaining items, **not approved assessment results**. Before declaring `Complete`, add and review every Responsibility in the Template's canonical order.

The `State` and `Applicability` cells above are technically recommended contractual values; their *approval status* is separate from the values themselves. Their inclusion does not imply formal human sign-off.

---

## 3. Responsibility Details

### README-QUICK-START

**Requirement Level**

`Required`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — the consumer's own README instructions, supported by PostgreSQL and Docker documentation. These are descriptions of implementation shape, not an automatic satisfaction judgment.

**Uncertainty**

- The documented Docker Compose Quick Start has not been demonstrated from a clean checkout of the pinned consumer SHA.
- No positive Compose smoke check directly associated with that SHA was found among the previously inspected checks; a run on another SHA must not be treated as equivalent without verification.
- The documentary sufficiency threshold and potential onboarding friction (port overrides, sample credentials, absence of default demo data) still require reviewer judgment.

**Detected Facts**

- The pinned README gives a concrete onboarding sequence: clone, create `.env` from `.env.example`, replace the sample database password, run `docker compose up --build -d`, inspect `docker compose ps`, and visit `http://localhost:8080/movies`.
- The pinned `Dockerfile` uses Java 25 build/runtime images; `pom.xml` specifies Java 25 and Spring Boot parent 4.0.5.
- The pinned `compose.yaml` declares the application and PostgreSQL 17, database health dependency, volumes for PostgreSQL and uploaded images, and localhost-bound published ports. The `postgres` Spring profile uses database environment variables and Flyway schema migration.
- The README explains local-only operation, alternative Maven startup, port overrides and the lack of default PostgreSQL demo data. It warns that `docker compose down -v` deletes volumes.
- [GitHub Actions run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) completed successfully at the pinned SHA, including the `postgres-schema` job. That job starts the **JAR against CI PostgreSQL**, not the documented Docker Compose stack.
- `compose-smoke.yml` describes Compose configuration, build/start, HTTP, migration and persistence checks, but the previous review **did not find a successful Compose check tied directly to the pinned SHA**. This does **not** prove that Compose fails or was never run elsewhere.

**Evidence**

- [Pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile)
- [Pinned Compose configuration](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml)
- [Pinned environment example](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.env.example)
- [Pinned PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [Static configuration and CI evidence review](only-film-pinned-quickstart-ci-verification.md)
- [Compose execution gap and Q1–Q8 reproduction gates](only-film-compose-evidence-gap.md)
- [Provisional semantic review](only-film-required-semantic-review.md)

**Evaluation Rationale**

`README-QUICK-START` is `Required` by the pinned Template and clearly applicable to a project whose README presents two documented startup paths. The README contains a coherent sequence, and the previously examined Docker, Java, Compose and Spring parameters are internally consistent. Therefore, `Missing` would not reflect the available documentation. However, no direct Compose run for the pinned SHA has been verified and the review has not established that the documented procedure is sufficient for a new user. `Partial` is a **conservative proposed interpretation of documentary and operational sufficiency**, not evidence that Docker startup fails. A reviewer may choose `Satisfied` if the documentation Responsibility's criteria are met without a separate full runtime demonstration, but must document that judgment rather than treating an unrun workflow as passed.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

No downstream `PRESERVE`, `ADAPT`, or other Adoption Decision is approved. The reviewer must determine the sufficiency threshold and whether to request a reproducible Compose smoke run using the recorded Q1–Q8 gates. Any operational reproduction must use disposable data and avoid destructive cleanup of existing volumes.

---

### README-TESTING

**Requirement Level**

`Recommended`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — the README's testing overview points to project-specific GitHub Actions workflows and specialist guides.

**Uncertainty**

- The general `./mvnw test` command has not been reproduced from a clean checkout of the pinned commit, and it is not equivalent to the specific H2 test selection executed by CI.
- Full Selenium, manual workflows, and Docker Compose testing have not been demonstrated for the pinned SHA in the inspected evidence.
- A human reviewer must judge whether the README adequately explains test prerequisites, CI triggers, scope differences, and the limits of its testing claims.

**Detected Facts**

- The pinned README contains a `Pruebas y CI` section with `./mvnw test`, selected `-Dtest` examples, a table of workflows, and an explanation that the broad `tests.yml` suite is manual rather than necessarily required for each PR.
- `postgres-migration.yml` defines H2 regression, PostgreSQL schema/runtime checks, and PostgreSQL JPA/concurrent checkout; `tests.yml` includes manual suites and conditional Selenium workflow coverage.
- The pinned [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) records `h2-regression` with **329 tests, 0 failures, 0 errors, 0 skipped**, and `BUILD SUCCESS`.
- Five specifically reviewed classes account for **40** of those tests, including Review, CSRF, Ticket Security, environment hardening, and file-service tests; that subtotal is not the entire 329-test run.
- The other two jobs in the same run, `postgres-schema` and `PostgreSQL JPA and concurrent checkout`, completed successfully, but they do not prove Selenium or Compose smoke test success.

**Evidence**

- [Pinned README — testing and CI](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned tests.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml)
- [Pinned postgres-migration.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml)
- [Verified Surefire and Sonar log evidence](only-film-verified-surefire-sonar-logs.md)
- [Pinned Quick Start and CI verification](only-film-pinned-quickstart-ci-verification.md)
- [Testing E3 semantic proposal](only-film-testing-semantic-review.md)

**Evaluation Rationale**

The README offers useful, discoverable testing instructions, links to the relevant CI workflows, and distinguishes common PR checks from manual testing. Execution evidence confirms that a substantial selected H2 regression ran successfully on the pinned SHA. Nevertheless, the README's broad local test command has not been independently reproduced here, and some workflow paths are conditional or manual. `Partial` is therefore a conservative **proposed assessment of the clarity and completeness of testing guidance**, not a conclusion that the tests themselves are deficient. A reviewer may instead approve `Satisfied` if the documentation Responsibility's scope is sufficiently met.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Whether to `PRESERVE` the README guidance or `ADAPT` its clarity and prerequisites remains subject to the maintainer's review. Neither code nor workflow changes are approved by this assessment record.

---

### DOC-TESTING

**Requirement Level**

`Recommended`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Specialized`, `Distributed` — specialized project documentation covers PostgreSQL integration tests, JaCoCo reporting, and SonarCloud/CI.

**Uncertainty**

- Whether the distributed documentation is sufficient and current for a contributor to reproduce relevant PostgreSQL, Selenium, Compose, and optional analysis paths.
- The historical JaCoCo report was produced and uploaded, but its XML/HTML contents were not retrieved; **no measured coverage percentage** is available from the inspected evidence.
- The Sonar scanner reported successful submission, but the **historical Quality Gate result was not verified**. Test execution and documentation quality must be evaluated separately.

**Detected Facts**

- The pinned `docs/POSTGRESQL_INTEGRATION_TESTS.md` describes the PostgreSQL integration-test environment.
- The pinned `docs/JACOCO_COVERAGE_BASELINE.md` distinguishes selected H2 regression coverage from any project-wide coverage claim and explains report inspection.
- The pinned `docs/SONARCLOUD_PR_CI.md` describes CI/SonarCloud integration and the availability requirement for `SONAR_TOKEN`.
- The historical `h2-regression` log records JaCoCo report generation and successful upload of `jacoco-h2-regression` (artifact ID `12201642997`); a subsequent artifact listing was empty. The report's percentage has **not** been inspected.
- The same run's scanner logs show `ANALYSIS SUCCESSFUL` and JaCoCo import. This demonstrates submission/analysis by the scanner, **not a passed Quality Gate**. The historical CE task ID `AaFU8vS6n_jCCWP5LQvY` is recorded in the specialist review, but its final processing and Quality Gate status were not obtained.
- The H2 job's 329 passing tests, although useful, do **not** establish total test-suite coverage or complete documentation sufficiency.

**Evidence**

- [Pinned PostgreSQL integration testing guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md)
- [Pinned JaCoCo coverage baseline](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/JACOCO_COVERAGE_BASELINE.md)
- [Pinned SonarCloud PR CI guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md)
- [Pinned H2 regression run](https://github.com/fran-eliot/only_film/actions/runs/39283862407/job/118164215980)
- [Verified Surefire, JaCoCo, and Sonar logs](only-film-verified-surefire-sonar-logs.md)
- [Testing semantic review and historical Sonar CE task](only-film-testing-semantic-review.md)

**Evaluation Rationale**

The consumer has substantive specialized documentation and independently identified execution evidence. The guides provide context for PostgreSQL tests, selected JaCoCo reports, and SonarCloud CI. However, those materials are distributed across different files and were not validated as a complete, current, reproducible contributor workflow. `Partial` is an **unapproved documentary sufficiency hypothesis**; it does not mean that the project lacks tests or that SonarCloud failed. A reviewer must decide whether these documents satisfy the Responsibility without requiring a single consolidated guide or full suite execution.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

A human review must determine whether to `PRESERVE` the specialized guidance, `ADAPT` discoverability or reproducibility instructions, or choose another supported action. No new test run, coverage figure, Quality Gate determination, or consumer modification is authorized.

---

### README-LICENSE

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Equivalent` **as a documentary notice only**. The existing README notice does not constitute a license grant or establish intellectual-property ownership.

**Uncertainty**

- Actual copyright and reuse permissions for the original academic collaboration have not been verified.
- The reviewer must determine whether the current non-grant notice sufficiently informs readers or whether it requires a clearer explanation supported by authoritative rights information.
- Whether a license file or a more detailed notice can lawfully be added depends on the relevant rights holders; **no license selection is implied**.

**Detected Facts**

- The pinned consumer README ends with a license-related note identifying the academic origins, directing readers to the original project and project documentation for terms, and expressly stating that the README does not grant an additional license.
- The prior pinned-tree inspection did not identify a root `LICENSE`, `LICENCE`, or `COPYING` file. That filename observation is not a complete legal rights review.
- The pinned `pom.xml` contains an empty `<licenses><license/></licenses>` entry; it does not specify reuse terms.
- The original project is attributed to multiple collaborators in the README. The subsequent maintenance of `fran-eliot/only_film` does not establish unilateral authority to license all original contributions.

**Evidence**

- [Pinned README — origin, credits, and license notice](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned POM](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Pinned consumer tree](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [Original academic repository](https://github.com/certidevs/g1_testing)
- [Optional README governance semantic review](only-film-optional-governance-semantic-review.md)

**Evaluation Rationale**

A license-status notice exists and deliberately avoids asserting permissions that have not been established, so `Missing` would overlook real documentary content. However, the note does not explain a verified license or clearly specify reuse permissions. The proposed `Partial` evaluates **the clarity and completeness of license-related communication**, not whether a particular open-source license should be granted. It is not a legal determination. A reviewer may find the notice sufficient for the project's actual context, but that judgment must remain distinct from ownership and authorization.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Before choosing `PRESERVE`, `ADAPT`, `ADD`, or another valid action, the maintainer must establish the intended audience and obtain appropriate rights information if stronger permission statements are contemplated. This working record neither creates nor recommends a specific license grant.

---

### DOC-SECURITY

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Specialized`, `Distributed` — security guidance and qualifications are spread across the README, a historical hardening audit, demo-credentials guidance, configuration, and CI records.

**Uncertainty**

- The historical `SECURITY_HARDENING_AUDIT.md` evaluates a **different earlier baseline**; its findings must not be presented as current defects at the pinned SHA.
- The review has not established whether documentation adequately covers the intended threat model, secret handling, local-only deployment, vulnerability reporting, and user-data expectations.
- Tests and scanner submission do not prove complete endpoint coverage, dependency safety, security certification, a successful Quality Gate, or production readiness.
- The reviewer must decide whether a distributed set of guides is sufficient or a more focused security-documentation entry point would help maintainers.

**Detected Facts**

- The pinned README includes `Seguridad y límites actuales`, describing role restrictions, BCrypt, CSRF protection, image validation, a demonstration checkout without a real payment gateway, and explicit limitations on production deployment.
- The `docs/SECURITY_HARDENING_AUDIT.md` document is dated **2026-10-10** and states an older project baseline. It captures historical risks and recommendations, **not** an independently current audit of the assessed commit.
- At the pinned SHA, reviewed `ReviewController.java` and related tests provide evidence of authorization checks on review edits, including a negative POST test expecting HTTP 403.
- `MutationCsrfSecurityTest.java` exercises protection against GET mutations, missing CSRF tokens, and unauthorized session disabling. `FileService.java` and `FileServiceTest.java` provide bounded image-content and size validation evidence.
- Configuration and `EnvironmentHardeningTest.java` address restrictions on H2 console/SQL logging and demo configuration. `docs/DEMO_CREDENTIALS_SECURITY.md` warns about credential handling.
- The verified `h2-regression` log on [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) shows **329 tests, 0 failures, 0 errors, 0 skipped**; five cited security-relevant test classes account for **40** tests within that result.
- The run's Sonar scanner reported `ANALYSIS SUCCESSFUL`; **the historical Quality Gate result remains unverified**. No pentest or exhaustive security review is established.

**Evidence**

- [Pinned README — security section](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Historical hardening audit at the pinned tree](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md)
- [Demo credentials security guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md)
- [Security implementation and historical-audit reconciliation](only-film-security-testing-reconciliation.md)
- [Negative security-test evidence](only-film-negative-security-test-evidence.md)
- [Verified Surefire and Sonar log evidence](only-film-verified-surefire-sonar-logs.md)
- [DOC-SECURITY E3 semantic review](only-film-security-semantic-review.md)

**Evaluation Rationale**

`DOC-SECURITY` is `Optional` under the Template yet relevant to a consumer that authenticates users, handles uploads and user records, and supports demonstration purchases. The reviewed evidence demonstrates substantive security-related documentation and bounded tests, so absence of a standalone `SECURITY.md` must not trigger `Missing`. `Partial` is a **provisional judgment about the adequacy and currency of the documentary coverage**, particularly the distinction between a historical audit and current controls. It is **not** an assertion that the application is insecure or that lacking a pentest automatically makes security documentation partial. Human review must establish the actual documentary acceptance criteria.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The reviewer must determine whether `PRESERVE` or `ADAPT` the existing documentation is appropriate, and whether any additional documentation is justified by the consumer's audience and deployment assumptions. No security certification, change to Only Film, or downstream adoption action follows from this proposed record.

---

### DOC-ARCHITECTURE

**Requirement Level**

`Recommended`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Specialized`, `Distributed` — the README summarizes the MVC/JPA structure while historical architecture and maintainability documentation provides additional context, but not a verified consolidated architecture snapshot for the pinned commit.

**Uncertainty**

- Which boundaries, dependencies, critical flows, and architectural exceptions are present at the pinned SHA, beyond the nominal README diagram-like description?
- Whether the existing overview and supporting documents adequately describe the **current** architecture for contributors without recasting historical issues as unresolved defects.
- Whether a more consolidated architecture overview is warranted or the existing sources meet the Component's level of detail.

**Detected Facts**

- The pinned README describes a primary `MVC controller → service / business rules → JPA repository → database` flow and names domain entities including `Movie`, `Room`, `Session`, `Ticket`, `Review`, and `User`.
- The Framework's `DOC-ARCHITECTURE` Component expects a maintained description of architectural purpose, context, key components, relationships, and constraints; it does not prescribe exhaustive class-by-class documentation or a diagram solely for formality.
- The pinned repository contains `docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md`, dated **2026-10-10** and explicitly based on an earlier `main` after PR #23 (`b6cf52c9`). It describes some direct controller-to-repository access and proposed improvements **for that historical reference**.
- The functional audit `docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md` uses another historical baseline (`df63353564485eb6d2d60c982032e5d3c4facbf2`) and cautions against reopening findings automatically after later changes.
- The existing sources convey a nominal architecture and selected historical concerns; no complete architecture-description reconciliation to the pinned SHA was established by the prior reviews.

**Evidence**

- [DOC-ARCHITECTURE Component](../../components/documentation/architecture/README.md)
- [Pinned consumer README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Historical architecture audit in the pinned tree](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md)
- [Historical F3 functional audit in the pinned tree](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [DOC-ARCHITECTURE E3 semantic review](only-film-recommended-docs-semantic-review.md)
- [README-ARCHITECTURE E3 semantic review](only-film-recommended-readme-semantic-review.md)

**Evaluation Rationale**

Documentation relevant to the architectural Responsibility exists, so `Missing` is not established simply by the lack of a canonical architecture snapshot. The README's high-level flow provides a useful entry point, but a historical maintainability audit is not necessarily a maintained explanation of current components, relationships, and constraints. `Partial` is a **proposed documentary sufficiency judgment**, rather than an assertion that earlier direct repository access still exists or that the pinned architecture is defective. Human review should verify the expected scope and decide whether the distributed sources sufficiently support the selected Template.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Whether to `PRESERVE` the existing documentation or `ADAPT` its architectural overview requires human review and a bounded reference check. No refactoring or consumer-documentation change is authorized by this record.

---

### DOC-PROJECT-STATUS

**Requirement Level**

`Recommended`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Specialized`, `Distributed` — the README outlines possible next steps, while a maturity assessment and functional roadmap describe the project's development history from different reference points.

**Uncertainty**

- The actual status of F3 initiatives (completed, open, revised, or superseded) at the pinned SHA has not been reconstructed from current evidence.
- The latest verifiable milestone, current status by area, and immediate next objective are not established as one maintained, consumer-facing operational snapshot.
- Whether the project's portfolio context calls for a compact maintained status page or existing descriptions suffice requires reviewer judgment.

**Detected Facts**

- The Framework's `DOC-PROJECT-STATUS` Component calls for an overview, progress by area, a next milestone and immediate goals, distinct from a backlog, roadmap, or changelog.
- The consumer's `docs/TECHNICAL_MATURITY_ASSESSMENT.md` is dated **2026-10-10** and names historical reference `9f2a31e927df105d14e3d30d4d8277fa61883deb`; it describes a technically evolved academic/portfolio project with production-readiness limitations **at that baseline**.
- The `docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md` document is tied to `df63353564485eb6d2d60c982032e5d3c4facbf2` and describes F3.002–F3.008 initiatives. Their present completion status at the pinned SHA has not been verified.
- The pinned README's future work section mentions potential REST API, real payment integration, observability, and deployment automation, explicitly **not** implemented feature claims.
- [Run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) confirms successful checks at the pinned SHA, including an H2 regression job with 329 tests; isolated successful checks do **not** establish the overall project milestone or operational maturity.

**Evidence**

- [DOC-PROJECT-STATUS Component](../../components/documentation/project-status/README.md)
- [Historical technical maturity assessment in pinned tree](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md)
- [Historical F3 audit and roadmap in pinned tree](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [Pinned consumer README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned CI run](https://github.com/fran-eliot/only_film/actions/runs/39283862407)
- [DOC-PROJECT-STATUS E3 semantic review](only-film-recommended-docs-semantic-review.md)

**Evaluation Rationale**

Status-related material exists, but the Component's purpose is a maintained **operational snapshot** showing current progress, milestone and next steps. Historical maturity findings and a roadmap cannot safely be treated as an up-to-date account at the pinned SHA. `Partial` is a **conservative proposed evaluation of the documentary coverage and freshness**, not a conclusion that every F3 item remains open or that any historical risk still applies. A reviewer should decide whether the distributed sources meet the project's actual communication needs or need a scoped update.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The maintainer must establish the relevant reporting audience and verify present milestones before selecting `PRESERVE`, `ADAPT`, or another valid Adoption Decision. No changes to Only Film or new project status claims are authorized.

---

### README-STATUS

**Requirement Level**

`Recommended`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — the README communicates technologies, testing approaches and future possibilities; a separate historical maturity assessment supplies contextual information. No integrated, current `project_status` and `maturity` declaration was identified in the inspected README.

**Uncertainty**

- Who maintains and validates a concise status/maturity statement for the consumer, and against which dated reference?
- Whether the intended audience needs explicit distinctions such as `portfolio/demo`, active development, and production readiness, and what evidence supports those descriptors.
- Whether an updated README statement or an accessible equivalent source would be sufficient without requiring a new standalone status document.

**Detected Facts**

- At the pinned commit, README badges identify **technology versions** (Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway and Docker Compose), not CI health, active project status or a maturity level.
- The README's testing/CI section distinguishes GitHub Actions workflows and manual test paths, while the future-work section explicitly describes potential enhancements rather than completed features.
- The historical `docs/TECHNICAL_MATURITY_ASSESSMENT.md` is dated **2026-10-10** and tied to `9f2a31e927df105d14e3d30d4d8277fa61883deb`. It describes a technically evolving academic/portfolio backend with production limitations **at that earlier reference**, not necessarily at the assessed SHA.
- The Framework [README-STATUS Component](../../components/readme/status/README.md) concerns operational status and maturity (`project_status` and `maturity`), which are different from a technology badge.
- A [successful CI run on the pinned commit](https://github.com/fran-eliot/only_film/actions/runs/39283862407) includes 329 passing selected H2 tests but does **not** establish overall maintenance status, deployment readiness or maturity.

**Evidence**

- [Pinned Only Film README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Historical technical maturity assessment in the pinned tree](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md)
- [README-STATUS Component](../../components/readme/status/README.md)
- [Verified Surefire and Sonar log evidence](only-film-verified-surefire-sonar-logs.md)
- [Provisional README status/architecture semantic review](only-film-recommended-readme-semantic-review.md)

**Evaluation Rationale**

The README and supporting documents contain useful information about the project and its evolution. However, a technology/version badge is not a status or maturity indicator, and an older technical audit cannot simply be copied forward as the current state. `Partial` is a **proposed semantic evaluation of the clarity and currency of the status information**, not a claim that the project is currently unhealthy or that a particular visual badge is mandatory. The reviewer must decide what a useful status declaration means for this consumer and whether existing equivalent sources suffice.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

No `PRESERVE`, `ADAPT` or `ADD` decision is authorized. The maintainer must assess the consumer's intended audience and verify any status or maturity statement before selecting a documentation action.

---

### README-ARCHITECTURE

**Requirement Level**

`Recommended`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — a concise architecture/technology overview is already present in the README, with more detailed but historically scoped technical notes elsewhere in the repository.

**Uncertainty**

- Whether the nominal MVC/JPA flow remains a sufficiently accurate **high-level overview** of the pinned commit, including relevant exceptions.
- Whether direct controller-to-repository access noted in an **earlier** architecture audit still exists at the assessed SHA; it has not been revalidated across all controllers.
- Whether the README's succinct description is sufficient for the Responsibility's purpose or should better distinguish a representative flow from an exhaustive architecture contract.

**Detected Facts**

- The pinned README describes the principal `MVC controller → service / business logic → JPA repository → database` flow and identifies core domain entities including `Movie`, `Room`, `Session`, `Ticket`, `Review` and `User`.
- The Framework's [README-ARCHITECTURE Component](../../components/readme/architecture/README.md) expects a high-level architecture summary, not a detailed replication of the technical documentation.
- The `docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md` file, dated **2026-10-10**, concerns an earlier reference after PR #23 (`b6cf52c9`) and describes some direct controller-to-repository access at that point. That finding has not been comprehensively retested at the pinned SHA.
- A historical technical maturity assessment also concerns a different reference; the existence of multiple dated audits does not, by itself, establish the actual architecture at the assessed commit.

**Evidence**

- [Pinned README — technology and architecture section](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [README-ARCHITECTURE Component](../../components/readme/architecture/README.md)
- [Historical architecture maintainability audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md)
- [Historical technical maturity assessment](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md)
- [Provisional README status/architecture semantic review](only-film-recommended-readme-semantic-review.md)

**Evaluation Rationale**

The consumer already has a readable, appropriately concise architectural flow, so the Responsibility is not `Missing`. The line is explicitly a **principal flow**, not necessarily a guarantee that every request follows the same layers; historical reports suggest an older implementation was more nuanced. `Partial` is a **conservative, unapproved assessment hypothesis** reflecting the need to verify explanatory sufficiency and avoid overstating architecture uniformity. A human reviewer could reasonably select `Satisfied` if the overview meets the documented Component's high-level purpose, without requiring a full architecture audit or diagram.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The maintainer must decide whether to `PRESERVE` the existing overview or `ADAPT` wording for accuracy and navigability. No architecture refactoring, new diagram, or consumer change follows automatically from this proposed evaluation.

---

### DOC-CHANGELOG

**Requirement Level**

`Required`

**State**

`Missing` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Distributed` change attribution through commits and PRs exists, but no equivalent curated changelog implementation has been identified. This characteristic describes the evidence, not satisfaction of the Responsibility.

**Uncertainty**

- Whether any external or otherwise uninspected, substantive change record fulfills this Responsibility for the pinned consumer.
- Whether the consumer should maintain an `Unreleased` log before any formal version is published.
- Which bounded improvement, if any, the maintainer wishes to authorize after the semantic review; no Application decision is implied.

**Detected Facts**

- The pinned consumer README describes the project's academic origin and technical evolution, and points to Git history and PRs for attribution, but does not present a curated version-by-version change log.
- A direct lookup of `CHANGELOG.md` at the pinned SHA returned `404 Not Found`; this is an observation about **one path**, not proof that no equivalent document exists anywhere.
- The POM declares `0.0.1-SNAPSHOT`, which is an artifact version and not evidence of a published release.
- Historical commits and PRs record individual changes; this does not automatically make them release notes or a changelog.
- On **2026-11-13**, the consumer maintainer explicitly confirmed **no GitHub Releases and no tags**. This is **maintainer testimony**, not an independently executed tag inventory. An earlier GitHub Releases endpoint query also returned an empty list.

**Evidence**

- [Pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Pinned Git history](https://github.com/fran-eliot/only_film/commits/28d75a50e0a178954dd46acc23300d9dd327843c/)
- [Changelog evidence review, including maintainer confirmation](only-film-changelog-evidence-review.md)
- [Provisional Required semantic review](only-film-required-semantic-review.md)
- [Canonical Template metadata](../../templates/repositories/backend/metadata.yml)

**Evaluation Rationale**

`DOC-CHANGELOG` is `Required` by `TPL-BACKEND` 0.1.0. The relevant question is whether the consumer communicates meaningful changes in a changelog-like form, not whether a file has a prescribed name. The reviewed README, POM, and documentation did not establish such a record; the maintainer further confirmed the absence of tags and GitHub Releases. Raw commit/PR history supports attribution but is not a curated record of changes for readers. On this bounded evidence, `Missing` is more defensible than `Partial`: assigning `Partial` would require an identified partially satisfying change record. This remains **a proposed semantic assessment**, subject to human review of any alternative source.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The recommended `State` can be assessed without selecting an implementation action. The maintainer must review the proposal and determine whether the right downstream decision is `ADD`, `ADAPT`, `ACCEPT`, or another permitted value after considering audience, existing equivalent sources, and maintenance scope. No change to Only Film is authorized by this record.

---

## 4. Assessment Conclusion

### Assessment Status

`In Progress`

### Major Findings

- All 28 Template Responsibilities have preliminary E3 review proposals, and ten are now transcribed into this Assessment working record: `README-QUICK-START`, `DOC-CHANGELOG`, `README-STATUS`, `README-ARCHITECTURE`, `README-TESTING`, `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS`, `DOC-TESTING`, `README-LICENSE`, and `DOC-SECURITY`.
- `DOC-CHANGELOG` has a recommended `Missing` State supported by reviewed documentation and maintainer confirmation of no tags or Releases.
- `README-QUICK-START` has a proposed `Partial` State, grounded in documentation and CI evidence but bounded by the missing pinned-Compose execution evidence. **No formal human approval is claimed for either State.**

### Open Uncertainties

- Human sign-off on all ten proposed evaluation entries, including `DOC-CHANGELOG` alternatives and the Testing documentation sufficiency threshold.
- Formal Assessment entries for the other 18 Responsibilities, plus human review of Quick Start Compose verification, security-documentation adequacy, license-status communication, architecture freshness, and actual project milestone.
- The historical JaCoCo coverage percentage and Sonar Quality Gate outcome are not established; whether either is necessary for documentary acceptance remains a reviewer question.
- Rights and permissions associated with the original academic contributions remain unverified; the Assessment does not grant a license.
- Adoption Decisions and rationales where warranted.

### Recommended Next Review

Review the ten structured entries, including `README-STATUS` and `README-ARCHITECTURE`, for approval or correction. Then progressively incorporate other Responsibilities from the consolidated review matrix, prioritizing existing P1 gates rather than generating another exploratory document.

---

## Completion Check

- **Assessment `Complete`: NO.**
- **Responsibility coverage in this working artifact:** `10/28` proposed, `18/28` not yet entered.
- **Formally approved States in this record:** `0`.
- **Resolved Adoption Decisions:** `0`.
- **Consumer mutations:** `NONE`.

This Markdown record follows the Assessment Template's field structure for the first ten Responsibilities. Its summary intentionally remains **partial** rather than filling missing entries with unsupported `State` values. It does not establish compliance or authorize Application/Integration.
