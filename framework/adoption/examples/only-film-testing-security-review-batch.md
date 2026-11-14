# Only Film — Testing and Security: human review batch

## Review context

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned consumer SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-TESTING`, `DOC-TESTING`, `DOC-SECURITY` |
| Review status | **Three evaluations formally approved by the Only Film maintainer on 2026-11-14; see decision record below** |
| Approved evaluations after maintainer review | `13/28` |
| Assessment status | `In Progress` |
| Consumer mutation | `NONE` |

This packet verifies **pinned, directly fetched** source documents and separates documentary completeness from test outcomes or security assurance. It uses the Assessment's prior run-log evidence for historical outcomes; **no GitHub Actions log was freshly downloaded or reverified in this packet**. Merging this packet is not human approval of the proposed States/Applicability, nor permission to modify Only Film.

## Formal maintainer review outcome — 2026-11-14

The Only Film maintainer **explicitly approved** the following three independent documentary evaluations:

| Responsibility | Approved State | Approved Applicability |
| --- | --- | --- |
| `README-TESTING` | `Partial` | `Applicable` |
| `DOC-TESTING` | `Partial` | `Applicable` |
| `DOC-SECURITY` | `Partial` | `Applicable` |

The approvals **preserve all evidence limitations**, including the distinction between the selected H2 regression and full test execution, unverified JaCoCo coverage and historical Sonar Quality Gate, the documented local/CI named-test selection difference, and the 2026-10-10 security audit's older reference. Neither test failure nor current security vulnerability is inferred.

All three entries retain `Decision Status: Needs Further Evaluation` and `Adoption Decision: —`; the overall Assessment remains `In Progress`. No modification to Only Film or security assurance is authorized.

The following evaluation alternatives and reviewer gates are preserved as the **pre-approval preparation record**; their historical references to pending review do not supersede the dated decision above.

## Recommendation table

| Responsibility | Current working State | Maintainer review recommendation | Applicability |
| --- | --- | --- | --- |
| `README-TESTING` | `Partial` (unapproved) | **Retain `Partial`** until the broad command and workflow selection guidance meet an agreed sufficiency threshold | `Applicable` (proposed) |
| `DOC-TESTING` | `Partial` (unapproved) | **Retain `Partial`**; specialized guides exist but their complete reproducibility and navigation are not established | `Applicable` (proposed) |
| `DOC-SECURITY` | `Partial` (unapproved) | **Retain `Partial`**; current README and credentials guidance exist, but historical audit scope and reporting guidance require discrimination | `Applicable` (proposed) |

These are **documentary** evaluations. None of them asserts a test failure, exploitable vulnerability, unsuccessful security scan, or deficient legal/security certification.

## 1. README-TESTING

### Direct pinned evidence

- The [pinned README's `Pruebas y CI` section](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) documents `./mvnw test`, selected `-Dtest` variants, a workflow table, and an explicit warning that `tests.yml` is manually triggered and Selenium E2E tests are not equivalent to PR regressions.
- The pinned [`postgres-migration.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) defines a **specific filtered** `h2-regression` command and separate PostgreSQL jobs. It does not execute the unfiltered README command as evidence of a clean local run.
- The pinned [`tests.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml) defines a `workflow_dispatch` path for its main suite and a narrower pull-request path to test Selenium/workflow configuration.
- The prior [verified Surefire/Sonar run-log record](only-film-verified-surefire-sonar-logs.md) attributes **329 passing H2 regression tests with zero failures/errors/skips**, plus successful PostgreSQL jobs, to run `39283862407` at the evaluated reference. These historical results were **not independently reproduced here**.

### Evaluation

The README meaningfully describes where and how to run tests; a noncanonical section name is not a deficiency. However, success of one **filtered** CI selection does not prove that the full README `./mvnw test` path succeeds, and no complete Selenium or Compose execution at the pinned SHA was verified in the prior record. `Partial / Applicable` is a defensible documentary proposal pending approval. A maintainer could instead approve `Satisfied` for a documentation-only threshold if supported by the guidance, while explicitly excluding any test-suite-wide success claim.

**Evidence gates:** accurate prerequisites, local command coverage, workflow triggers, discoverability and clarity about which suites are conditional/manual. No new workflow changes authorized.

## 2. DOC-TESTING

### Direct pinned evidence

- [`docs/POSTGRESQL_INTEGRATION_TESTS.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md) describes the PostgreSQL 17 JPA/concurrency tests, the dedicated Maven command, profile behavior, test-database variables, and the warning that integration fixtures **create rows not automatically cleaned up**. The test must run on a **disposable** PostgreSQL database.
- [`docs/JACOCO_COVERAGE_BASELINE.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/JACOCO_COVERAGE_BASELINE.md) explains H2-selected coverage, the 14-day `jacoco-h2-regression` artifact retention period, HTML/XML report paths and how to inspect a report. It explicitly warns against interpreting this as full-suite project coverage.
- The **documented local JaCoCo selected-test command** in that guide and the directly fetched current `h2-regression` workflow do **not contain identical named-test selections**. This is a **specific potential synchronization concern**, not evidence that either command fails or that the numbers are wrong; a later editorial review may decide whether parity is necessary.
- [`docs/SONARCLOUD_PR_CI.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md) distinguishes PR/main analysis, manual Sonar workflow, scanner availability depending on `SONAR_TOKEN`, and imported JaCoCo H2 selection.
- The prior [historical log-review record](only-film-verified-surefire-sonar-logs.md) observed a JaCoCo report upload and Sonar scanner `ANALYSIS SUCCESSFUL`, but **did not inspect a numerical coverage percentage or verify final Quality Gate status**.

### Evaluation

Testing documentation is substantive and specialized; splitting it between guides is not inherently a defect. The selection mismatch deserves a **targeted accuracy review** rather than immediate changes. `Partial / Applicable` is supported as a conservative proposal for the documentary gaps/limitations around reproduction, navigation and selection parity. No test count can be converted into a coverage percentage; scanner submission is not evidence of a passing Quality Gate.

**Evidence gates:** contributor repeatability, local/CI selection parity where meaningful, bounded artifacts, current Sonar guidance, and discoverability. No artifact retrieval or CI execution is authorized by this review packet.

## 3. DOC-SECURITY

### Direct pinned evidence

- The [pinned README's `Seguridad y límites actuales` section](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describes BCrypt, authenticated sessions and roles, CSRF, ticket/review authorization, image content validation, local development configuration, and demonstration checkout. It explicitly avoids claiming a complete security audit or production-hardened deployment.
- [`docs/DEMO_CREDENTIALS_SECURITY.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md) documents randomized demo passwords, a local-only optional password variable and the warning not to reuse known/shared demo credentials in public environments. This is an existing **specialized handling guide**, not proof that every secret is safe.
- [`docs/SECURITY_HARDENING_AUDIT.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md) is **dated 2026-10-10**, explicitly tied to an **earlier SHA** (`0a7e03a0`), and describes historical risks and proposals. It cannot be treated as a security assessment of the pinned November SHA or as a list of still-open vulnerabilities.
- The main Assessment's existing [security reconciliation](only-film-security-testing-reconciliation.md), [negative-test review](only-film-negative-security-test-evidence.md) and [run-log record](only-film-verified-surefire-sonar-logs.md) include bounded security-relevant test evidence. A prior 329-test H2 success, including 40 tests in five named security-relevant classes, does **not** amount to complete endpoint coverage, security certification or verified Sonar Quality Gate success.

### Evaluation

`DOC-SECURITY` is Optional in the Template but applies to an app with authenticated accounts, user data, uploads and checkout demonstration. Existing README and credential guidance clearly mean `Missing` would be unsupported by these inspected materials. `Partial / Applicable` is a reasonable documentary proposal while the maintainer decides whether vulnerability reporting, secret-handling navigation, threat-model scope and reference freshness are sufficiently covered.

**Evidence gates:** intended users and deployment assumptions, documentation currency, disclosure/reporting route if needed, credential guidelines and historical/current separation. No claim of insecure software, open historical defects, pentest result, or required `SECURITY.md` follows.

## Maintainer acceptance gate

The maintainer may explicitly approve the recommended **three independent `Partial / Applicable` evaluations** with the limitations above, or request a narrower documentary threshold and different allowed State for one or more entries. `Satisfied` must not be understood to certify runtime correctness or safety, and `Partial` does not imply failed tests.

Any approval requires the maintainer's express State and Applicability choices, recorded with the actual date in the [Assessment](only-film-assessment.md) and [review matrix](only-film-consolidated-review-matrix.md). Merging this evidence packet alone does not approve the values.

**Assessment Status:** `In Progress`. **Decision Status:** `Needs Further Evaluation` for each of the three. **Adoption Decision:** `—` for each. **Consumer mutation:** `NONE`.

## Sources and authorization boundary

All directly fetched consumer documents were examined at immutable commit `28d75a50e0a178954dd46acc23300d9dd327843c`. Historical run results and implementation checks are quoted from the linked Framework review records, **not freshly established by this packet**. This is a documentary assessment of the current pinned snapshot, not an independent live security audit, complete runtime test run, legal determination, or infrastructure remediation. No code, CI, secrets, security policy, repository files, or volume data in Only Film may be changed as part of this review.
