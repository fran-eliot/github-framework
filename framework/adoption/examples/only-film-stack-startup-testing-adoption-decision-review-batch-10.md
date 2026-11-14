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

## Pinned generic Maven test-command scope — source reconciliation (2026-11-14)

The following **static, pinned-SHA** observations refine the `README-TESTING` documentation-sufficiency decision. The examined Only Film reference is `28d75a50e0a178954dd46acc23300d9dd327843c`; no Maven, browser, Docker, database or CI job was executed by this review.

| Pinned source | Verified static fact | Meaning for README readers |
| --- | --- | --- |
| [README — Pruebas y CI](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) | Lists `./mvnw test` before narrower `-Dtest='*ServiceTest'`, `'*ControllerTest'` and `'*RepositoryTest'` examples, and warns some tests need external services, a graphical/headless environment or additional configuration. | The caveat is useful, but the generic command does not identify **which source test classes** need separate prerequisites. This does not prove that the command passes or fails. |
| [`PostgresPersistenceIntegrationTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/repository/PostgresPersistenceIntegrationTest.java) | Uses `@SpringBootTest` with `@ActiveProfiles("postgres")` and explicitly requires a real PostgreSQL service; its filename ends in `Test`. | An unfiltered ordinary Maven/Surefire test invocation may encounter a test needing PostgreSQL environment variables and a live service. `postgres-migration.yml` instead runs this test in a dedicated service-backed job. |
| [`BaseSeleniumTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/ui/BaseSeleniumTest.java) and [`MovieSeleniumTest.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/test/java/com/demo/ui/MovieSeleniumTest.java) | Concrete Selenium tests extend a base class that starts `ChromeDriver`; Chrome headless arguments are added when `CI` is set. | Selenium tests have browser/driver needs distinct from isolated H2 tests. A list of test families does not automatically guarantee generic local execution. |
| [`tests.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml) | Repository/controller/service/security jobs are `workflow_dispatch`-only. The Selenium job is not guarded by that condition; the `pull_request` trigger is limited to changes to `.github/workflows/tests.yml`. | Broad/manual suite and narrowly triggered Selenium PR validation are distinct; neither is proven successful at this SHA merely by its workflow definition. |
| [`postgres-migration.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) | H2 regression runs an explicit `-Dtest` selection; a separate `postgres-integration` job provisions PostgreSQL and selects `PostgresPersistenceIntegrationTest`. | The previously verified 329 selected H2 tests and separate PostgreSQL jobs do **not** imply a successful `./mvnw test`, complete Selenium test run or unified suite pass. |

### Evidence-qualified adoption option

**Consider `README-TESTING = ADAPT`**, strictly for a **future bounded README documentation clarification** separating quick local H2 selections, dedicated PostgreSQL prerequisites, browser-dependent Selenium runs, and the exact manual versus PR workflow triggers. The intent is to help readers interpret existing commands and avoid implying that all test families have identical prerequisites or CI cadence. Neither a failing generic test command nor a passing full suite is inferred.

The already approved `README-TESTING: Partial / Applicable` classification remains unchanged. **Formal Adoption Decision: `Needs Further Evaluation / —`**, pending explicit maintainer approval. This candidate does **not** require or authorize Maven/Surefire changes, exclusion rules, CI workflow edits, Selenium installation, test execution, new coverage metrics or a Quality Gate claim. Assessment **`In Progress`**, **23/28 formally resolved**, **5 pending**, Only Film strictly read-only.

## Pinned Quick Start readiness and configurable-port interpretation — 2026-11-14

A targeted read-only comparison of the pinned Only Film README, `compose.yaml`, `.env.example`, `docs/POSTGRESQL_SETUP.md` and the `compose-smoke.yml` workflow at `28d75a50e0a178954dd46acc23300d9dd327843c` refines the **documentary** acceptance threshold for `README-QUICK-START` without executing Compose.

| Pinned source | Direct evidence | Scope and limitation |
| --- | --- | --- |
| [README Quick Start](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md#L47-L75) | Instructs `docker compose up --build -d` followed by `docker compose ps`, then directs the reader to `http://localhost:8080/movies`. It already mentions configurable `APP_PORT` and `POSTGRES_PORT`, loopback-only binding, empty default PostgreSQL demo content and destructive `down -v`. | `ps` provides container-state visibility but is **not the same as an explicit HTTP application-readiness assertion**. The displayed URL is the default-port example; a changed host `APP_PORT` changes the URL a reader must visit. These are usability clarifications, **not observed startup defects**. |
| [`compose.yaml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) and [`.env.example`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.env.example) | The application maps `127.0.0.1:${APP_PORT:-8080}:8080`; PostgreSQL uses `127.0.0.1:${POSTGRES_PORT:-5432}:5432`; the application depends on **PostgreSQL health**, not on a separately configured application HTTP healthcheck. | Static Compose semantics only, not a completed container build, verified health at the pinned SHA, or assurance about port availability on the user's host. |
| [`compose-smoke.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) | Defines `docker compose config --quiet`, `docker compose up --build --wait -d`, and an explicit **HTTP 200 check** on `http://127.0.0.1:8080/movies`, with repeated checks after container restart/recreation. | A defined smoke procedure indicates an intended readiness criterion, but **does not establish that a successful Compose smoke execution occurred** for this immutable assessed commit. |
| [PostgreSQL local guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) | Distinguishes complete Compose startup from running the database alone with an external Java process, and explicitly warns about empty PostgreSQL seed data and destructive volume cleanup. | An existing specialist guide supplies detail; the README need not duplicate its entire procedure. |

### Adoption decision candidate

**Consider `README-QUICK-START = ADAPT`**, limited to a **future, separately authorized documentary clarification** of the application-ready check versus container listing, the default URL when `APP_PORT` is overridden, and where to find the existing more detailed local troubleshooting/setup guidance. The already approved `Partial / Applicable` values and the original positive/negative **Compose execution evidence gap** remain unchanged.

`README-QUICK-START` stays formally **`Needs Further Evaluation / —`** until explicit maintainer approval. This review does **not** conclude that the existing Quick Start fails, that a clean Compose run succeeds, or that a workflow definition verifies real execution. No runtime test, container change, deletion of volumes, secret manipulation, new healthcheck, consumer edit, or Application/Integration is authorized.

The Only Film Assessment remains **`In Progress`** with all 28/28 State/Applicability approvals unchanged and **23/28 formally resolved Adoption Decisions** (13 `PRESERVE`, 3 `OMIT`, 5 `ADAPT`, 2 `ADD`); **5 pending**.


## Formal README-QUICK-START and README-TESTING Adoption Decisions — 2026-11-14

The Only Film maintainer expressly approved **`README-QUICK-START = ADAPT`**, strictly for future documentary clarification of an HTTP application-readiness check versus container listing, the effect of configurable host `APP_PORT` on the example URL, and navigation to the existing local startup guide. There is **no verified passing or failing clean pinned-SHA Compose run** in the assessed evidence. No container, environment, volume or deployment operation is authorized.

The maintainer independently approved **`README-TESTING = ADAPT`**, strictly for future documentation distinguishing H2-selected tests, PostgreSQL service prerequisites, Selenium browser requirements and the actual manual versus PR CI triggers. The evidence does not establish a full Maven/Selenium/Compose suite outcome, coverage percentage or passed historical Sonar Quality Gate. No Maven, test selection, workflow or application change is authorized.

Both decisions supersede the earlier deferrals while preserving the approved `Partial / Applicable` evaluations and all evidence gaps. **28/28 Adoption Decisions resolved** (14 `PRESERVE`, 3 `OMIT`, 9 `ADAPT`, 2 `ADD`), 0 pending; 28 approved State/Applicability pairs. Assessment **`In Progress`** and no Only Film change or Application/Integration authorization.
