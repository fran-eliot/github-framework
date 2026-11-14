# Only Film — Adoption Decision review batch 10: Technology Stack, Quick Start and Testing

## Assessment baseline and decision boundary

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable source reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Framework Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-TECH-STACK` (Required); `README-QUICK-START` (Required); `README-TESTING` (Recommended) |
| Previously approved State / Applicability | `28/28` pairs; unchanged |
| Formally resolved Adoption Decisions after explicit maintainer review | `16/28`: 13 `PRESERVE`, 3 `OMIT` |
| Remaining unresolved Adoption Decisions | `12/28`, including `README-QUICK-START` and `README-TESTING` |
| Assessment | `In Progress` |
| Only Film changes | `NONE` |

This packet prepares reviewer-facing choices only. **No formal Adoption Decision is conferred** by preparing or merging it. An explicit, separately dated maintainer approval is required to mark a choice `Resolved`. A documentary `PRESERVE` decision can retain an already useful partial implementation **without converting `State: Partial` to `Satisfied`**, asserting an exhaustive dependency inventory, or validating startup and tests. Only Film remains strictly read-only.

## Formal maintainer Adoption Decision outcome — 2026-11-14

The Only Film maintainer **expressly approved `README-TECH-STACK = PRESERVE`** and **expressly retained** the other two responsibilities as unresolved:

| Responsibility | Decision Status | Adoption Decision | Evidence-constrained rationale |
| --- | --- | --- | --- |
| `README-TECH-STACK` | `Resolved` | `PRESERVE` | Retain only the **existing categorized reader-facing stack overview**, with the POM, Dockerfile, Compose and workflow definitions corroborating selected configured versions and paths; no exhaustive technology use, runtime success or cloud deployment is claimed |
| `README-QUICK-START` | `Needs Further Evaluation` | `—` | Clean Docker Compose build/start for the pinned source was not verified; the absence of that check is neither evidence of success nor evidence of failure |
| `README-TESTING` | `Needs Further Evaluation` | `—` | 329 **selected** passing H2 tests and separately successful PostgreSQL jobs do not establish a complete general Maven suite, Selenium/Compose runs, consolidated coverage or passed historical Quality Gate |

**Human approval date:** 2026-11-14. **Immutable consumer evidence baseline:** `28d75a50e0a178954dd46acc23300d9dd327843c`. All 28 formally approved State / Applicability pairs remain unchanged; in particular all three retain `Partial / Applicable`. The prior proposed options below are retained as **historical preparation**, not as the current formal decision outcome.

**Authorization boundary:** Assessment `In Progress`, **16/28 decisions formally resolved** (13 `PRESERVE`, 3 `OMIT`) and **12 unresolved**. No Only Film source, documentation, build, tool, CI, workflow, tests, runtime, deployment, infrastructure or integration may be modified or executed by this decision.

## Review candidates

| Responsibility | Approved State / Applicability | Suggested decision | Critical evidence boundary |
| --- | --- | --- | --- |
| `README-TECH-STACK` | `Partial / Applicable` | **Consider narrowly `PRESERVE`** of the existing categorized technology overview | Selected versions/configuration are corroborated in POM, Dockerfile, Compose and workflows; not every listed runtime/test tool or deployment behavior was exhaustively verified |
| `README-QUICK-START` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —`** | A clean pinned-SHA `docker compose up --build -d` start was **not independently verified**; JAR-on-PostgreSQL CI cannot substitute for it |
| `README-TESTING` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —`** | Selected H2 and PostgreSQL CI passed, but broad Maven, Selenium, manual and Compose test paths were **not all reproduced** for the pinned SHA |

## 1. README-TECH-STACK — bounded preservation of useful categorized documentation

### Pinned sources checked

- The directly re-fetched [Only Film README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) has `Tecnologías y arquitectura`, organized by **Backend, Security, Frontend, fast local persistence, persistent database, Testing and Infrastructure**. It lists Java 25, Spring Boot 4.0.5, Spring MVC, Spring Data JPA/Hibernate, Spring Security/BCrypt/CSRF, Thymeleaf/Bootstrap, H2, PostgreSQL 17/Flyway, JUnit/Mockito/MockMvc/Selenium, and Docker/Actions/JaCoCo.
- The directly re-fetched [`pom.xml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) declares `java.version=25` and parent Spring Boot `4.0.5`; it includes Selenium dependency configuration. Declaration supports **configured technology use**, not every feature exercised at runtime.
- The directly re-fetched [Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile) uses Maven 3.9 with Temurin 25 to build and a Temurin 25 JRE image for runtime. This is a **static image recipe**, not a successful Docker build at the pinned reference.
- The directly re-fetched [`compose.yaml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) declares `app` and `postgres:17-alpine`, a PostgreSQL health check, local bind ports and two named volumes; this corroborates local configuration without validating a clean deployed instance.
- The directly re-fetched [PostgreSQL CI workflow](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) includes H2 and PostgreSQL selections and Java 25 setup. The [manual/Selenium workflow](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml) distinguishes broad/manual and conditional tests from ordinary PR jobs.
- The [Framework README-TECH-STACK Component](../../components/readme/tech-stack/README.md) suggests category grouping; it does **not** require adding a fictitious Cloud category to a repository without a verified cloud environment.

### Decision posture

**Consider `Resolved / PRESERVE`**, expressly limited to the **existing useful, categorized reader-facing stack inventory**. Its choice is to retain the explanation, **not** to certify every dependency or actual technology path. The previously approved `Partial / Applicable` evaluation stays intact, including unverified tools/usage and actual Compose startup.

`ADAPT` would need a **specific version contradiction, unsupported stack claim or demonstrated navigation problem** at the immutable assessed SHA. A generic desire for template category uniformity, or the unverified existence of cloud infrastructure, does not suffice to justify changes.

A future audit may cross-check each technology against actual source/dependencies, but this review **does not claim** that exhaustive audit or authorize source/documentation changes in Only Film.

## 2. README-QUICK-START — explicit instructions, operational evidence still missing

### Pinned sources checked

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) instructs developers to clone, copy `.env.example` to `.env`, set a private `POSTGRES_PASSWORD`, execute `docker compose up --build -d`, inspect `docker compose ps`, and open `http://localhost:8080/movies`. The URL denotes **local** service access only.
- The directly re-fetched [`.env.example`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.env.example) exposes database/app port and sample password variables. Both `compose.yaml` and the Dockerfile support that startup arrangement **statically**.
- The README distinguishes temporary H2 and PostgreSQL profiles, explains empty default PostgreSQL demo content, names local-only port binding and warns that `docker compose down -v` destroys data volumes.
- The [README-QUICK-START Component](../../components/readme/quick-start/README.md) asks what a developer needs, how to install and how to run; the pinned README addresses those questions **documentarily**, not necessarily operationally.
- The [pinned CI verification](only-film-pinned-quickstart-ci-verification.md) and [Compose execution gap](only-film-compose-evidence-gap.md) identify GitHub Actions run [39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) with successful H2 and PostgreSQL jobs at the pinned SHA. The `postgres-schema` job runs a **Java JAR against CI PostgreSQL**, rather than the documented full Compose environment. No pinned-SHA `compose-smoke` success was confirmed by the earlier check inventory.
- [`compose-smoke.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) specifies a CI procedure for stack startup, HTTP checks, Flyway state and persistence. A workflow **definition** cannot replace an actual identified successful run.

### Decision posture

**Default `Needs Further Evaluation / —`.** A future `PRESERVE` would need an explicit maintainer judgment that the clear, static onboarding path is sufficient despite no verified clean-run record, or a separately authorized disposable test producing traceable pinned-SHA execution evidence. A future `ADAPT` needs actual reproduction failure or a specific demonstrably misleading instruction, not mere absence of a CI check.

If execution is later authorized, follow the [Q1–Q8 criteria](only-film-compose-evidence-gap.md), avoid using existing local volumes and do not place secrets in a repository. The Assessment does **not** authorize running Docker Compose, changing workflows or deleting data.

**Do not claim startup failed** based on missing check evidence; **do not claim startup passed** based on JAR-on-PostgreSQL CI success.

## 3. README-TESTING — selected regression evidence is not the full test suite

### Pinned sources checked

- The pinned README contains `Pruebas y CI`, `./mvnw test`, filtered `-Dtest` examples, a workflow table, and a description separating ordinary PR checks from manual tests and Selenium coverage.
- The directly re-fetched [`postgres-migration.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) defines a **selected** H2 test expression and PostgreSQL jobs. The earlier [verified Surefire evidence](only-film-verified-surefire-sonar-logs.md) records **329 selected H2 tests with 0 failures, 0 errors and 0 skipped** in the relevant successful run; that is **not** the total number of all possible test cases.
- The directly re-fetched [`tests.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml) marks the broad test suite as manually dispatched; conditional Selenium PR coverage is **not** the same as a successful full E2E test run at this pinned source.
- The prior [pinned verification](only-film-pinned-quickstart-ci-verification.md) records successful selected PostgreSQL jobs associated with [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407), but not a general `./mvnw test` reproduction from a clean checkout, complete Selenium/manual workflow completion or a clean Compose smoke run.

### Decision posture

**Default `Needs Further Evaluation / —`.** A conditional `PRESERVE` could retain the README's currently helpful overview if the maintainer explicitly accepts its **documentary** scope and the verified subset/test-selection caveat. `ADAPT` would require a concrete, checked inaccurate trigger/command or audience-relevant documentation gap, not the unsupported assumption that `./mvnw test` failed.

The previously resolved `DOC-TESTING = PRESERVE` applies to **specialist testing documentation**, not an automatic approval of this separate README Testing Responsibility or any test execution.

Do not infer a complete test-suite result, Selenium success, a current coverage percentage, historical Sonar Quality Gate approval or production readiness.

## Formal decision gate

The maintainer must approve or decline each decision independently. Recommended review bundle:

- `README-TECH-STACK = PRESERVE` **narrowly**, preserving the existing categorized overview without claiming complete technology verification.
- `README-QUICK-START = Needs Further Evaluation / —`, pending an agreed documentation-versus-execution acceptance threshold.
- `README-TESTING = Needs Further Evaluation / —`, pending an explicit testing-guide sufficiency and reproducibility threshold.

After **express formal approval**, use a **separate PR** to update the canonical [Assessment](only-film-assessment.md), the [consolidated matrix](only-film-consolidated-review-matrix.md) and this packet, with independently justified rationale and unchanged evidence constraints.

**Postapproval status:** All 28 State / Applicability pairs remain formally approved and unchanged. Sixteen Adoption Decisions resolved (13 `PRESERVE`, 3 `OMIT`); twelve unresolved. Assessment `In Progress`; Only Film read-only. The earlier preparation PR did not itself approve the new decision; express maintainer approval on 2026-11-14 did.
