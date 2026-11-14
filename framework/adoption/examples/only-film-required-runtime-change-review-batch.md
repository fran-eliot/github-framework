# Only Film — Required Quick Start and Changelog: human review batch

## Review scope

| Field | Value |
| --- | --- |
| Consumer repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned consumer commit | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-QUICK-START`, `DOC-CHANGELOG` (both Required in Template) |
| Review status | **Unapproved proposals for maintainer evaluation** |
| Existing approved evaluations | **8/28** |
| Assessment status | `In Progress` |
| Consumer mutation | `NONE` |

This packet reopens direct pinned content and checks the applicable Framework Components. Neither a successful CI run of a **different startup path** nor a lack of version tags may be used to fabricate evidence or mandatory implementation work. The [Assessment](only-film-assessment.md) keeps both working State/Applicability proposals unchanged until the maintainer explicitly approves or revises them.

## Recommended review alternatives

| Responsibility | Existing unapproved State / Applicability | Recommended review outcome | Rationale |
| --- | --- | --- | --- |
| `README-QUICK-START` | `Partial / Applicable` | **Retain `Partial / Applicable`**, or approve `Satisfied / Applicable` for documentary sufficiency alone | Prerequisites, environment preparation, Compose startup and target URL are documented; a clean Compose execution at this SHA was not verified |
| `DOC-CHANGELOG` | `Missing / Applicable` | **Retain `Missing / Applicable` as documentary observation** if change-history coverage is expected at the assessed scope | No curated change log has been identified; maintainer previously reported no tags or Releases; Component permits exceptions for projects without published versions |

**Important contract distinction:** `Requirement Level: Required` is Template metadata. The [DOC-CHANGELOG Component](../../components/documentation/changelog/README.md) nevertheless recognizes that a standalone Changelog may add little value for short-lived experiments or projects without releases. A reviewer must distinguish **current documentary coverage** (`State`) from whether the Responsibility is **needed** (`Applicability`). No `ADD` Adoption Decision is implied by `Missing`.

## 1. README-QUICK-START — pinned documentary verification

### Source findings

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) includes `Inicio rápido: aplicación y PostgreSQL con Docker`: Docker Engine/Compose as prerequisites, `git clone`, `cp .env.example .env`, password customization, `docker compose up --build -d`, `docker compose ps`, and `http://localhost:8080/movies`.
- The [pinned `.env.example`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.env.example) defines `POSTGRES_DB`, `POSTGRES_USER`, placeholder `POSTGRES_PASSWORD`, `POSTGRES_PORT`, and `APP_PORT`. The placeholder must be changed; its existence is not a production secret or a verified runtime configuration.
- The [pinned Compose file](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) defines `app` and `postgres` services, `postgres:17-alpine`, health-conditioned startup, localhost-bound ports, and named volumes.
- The [pinned Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile) uses `maven:3.9-eclipse-temurin-25` for the build and `eclipse-temurin:25-jre` for runtime. The [pinned POM](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) declares `java.version=25` and Spring Boot parent `4.0.5`.
- The README distinguishes local `dev`/H2 from `postgres` and `postgres,demo` profiles, warns that `docker compose down -v` destroys volume data, and explicitly says the Compose configuration is intended for **local development**, not exposed production.
- The [README-QUICK-START Component](../../components/readme/quick-start/README.md) asks what is needed, how to install and how to run. These three documentary questions have explicit responses at the pinned reference.

### Limits to the finding

No clean-clone Docker Compose execution is demonstrated for the exact pinned commit. The previously recorded [Compose evidence-gap review](only-film-compose-evidence-gap.md) distinguishes a successful JAR-on-PostgreSQL CI job from an actual Compose build/start. Source presence and configuration consistency must **not** be called a passing Compose smoke test.

A user on Windows may need to adapt `cp` to PowerShell/CMD; the README separately provides Windows-specific commands for the Maven startup path. That is a **possible onboarding friction point**, not a validated failure.

### Recommended evaluation

- **Conservative**: `State: Partial`, `Applicability: Applicable`, with verified documentary coverage and unverified reproducibility explicitly stated.
- **Documentation-only threshold**: `State: Satisfied`, `Applicability: Applicable`, **only if** the maintainer accepts that complete, coherent instructions fulfill this Component even though execution has not been independently demonstrated.
- If reproducible operation is essential to the user's accepted threshold, keep `Partial` pending an independently verified disposable Compose run; do not mark a test as failing merely because evidence is unavailable.

**No instruction to execute** `docker compose down -v` on existing data, run deployment, or modify the consumer is authorized.

## 2. DOC-CHANGELOG — pinned documentary verification

### Source findings

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describes collaborative origins and subsequent changes, but **does not maintain a chronological release/version change log**.
- The [pinned POM](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) declares `0.0.1-SNAPSHOT`. This is a Maven project version, **not proof of a published release**.
- The prior [Changelog evidence review](only-film-changelog-evidence-review.md) records a direct `CHANGELOG.md` lookup that returned 404 at one path; the absence of one filename does not exclude equivalent sources elsewhere.
- The maintainer **reported no GitHub Releases and no tags on 2026-11-13**. This is maintainer-supplied history, not a direct tag inventory at the pinned commit. An earlier Releases lookup returned no entries at the time of the check.
- The [DOC-CHANGELOG Component](../../components/documentation/changelog/README.md) defines a curated user-facing record of changes between published versions. It explicitly advises against formalistic changelog catalogs when a project is experimental, has no differentiated releases, or the information provides no real value.

### Limits to the finding

No exhaustive repository-wide search for all alternative changelog filenames, external release notes, or all tag history was performed in this pass. Raw commits and PR lists show individual change attribution but are **not** automatically a curated release record. Do not infer licensing, production maturity, or publication from the POM version.

### Recommended evaluation

- **Documentary-coverage interpretation**: keep proposed `State: Missing` because no equivalent curated changelog was found in the bounded evidence. `Applicability: Applicable` remains the working proposal because this is a Required Template Responsibility. **It does not imply that a new changelog must be created now.**
- **Scope alternative for maintainer review**: the Component's explicit no-releases exception could justify `Applicability: Not Applicable` for the current unversioned consumer **if the maintainer confirms** that a curated record is not useful at this stage. State must still be independently selected according to the Assessment Template.
- **Evidence alternative**: if an actual curated record is identified elsewhere, reassess whether `Partial` or `Satisfied` is warranted rather than accepting `Missing`.

The choice of `Missing / Applicable` versus `Missing / Not Applicable` requires explicit reviewer scope judgment. Neither choice automatically resolves `ADD`, `ACCEPT`, `OMIT` or another Adoption Decision.

## Maintainer review gate

- **Quick Start:** decide `Partial / Applicable` versus `Satisfied / Applicable` using a declared documentary-only or documentary-plus-runtime evidence threshold.
- **Changelog:** decide `Missing / Applicable` versus `Missing / Not Applicable`, taking into account the absence of published versions reported by the maintainer and the Component's exception; provide any alternative curated change source if one exists.

Record the maintainer's explicit selections and approval date **in a later Assessment PR**; merging this review packet **is not approval** of either entry. Both stay `Decision Status: Needs Further Evaluation`, `Adoption Decision: —`. All evidence qualifications remain intact.

## Authorization boundary

Only Film at SHA `28d75a50e0a178954dd46acc23300d9dd327843c` remains **read-only** throughout the Framework adoption assessment. This packet neither authorizes creating a changelog nor changing the README, Maven/Compose setup, GitHub tags, GitHub Releases, workflows, deployment, data volumes or project licensing. The overall Assessment remains `In Progress` and retains **8/28 formally approved evaluations** at the time of this preparation.
