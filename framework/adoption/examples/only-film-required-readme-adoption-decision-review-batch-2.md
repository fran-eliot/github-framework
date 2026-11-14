# Only Film — Adoption Decision review batch 2: Remaining Required README sections

## Scope, review baseline and current status

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable consumer reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Framework Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-TECH-STACK`, `README-QUICK-START`, `README-DOCUMENTATION`, `README-FOOTER` |
| Formal State / Applicability approval | **28/28 approved (unchanged)** |
| Adoption Decisions resolved | **3/28** (`README-HERO`, `README-OVERVIEW`, `README-FEATURES` — `PRESERVE`) |
| Other Adoption Decisions | **25/28 unresolved**, including all four in this packet |
| Assessment | `In Progress` |
| Consumer modifications | `NONE` |

This packet is **preparation for separate maintainer authorization**, not an approval of any Adoption Decision. The source documents below were directly re-fetched at the pinned consumer SHA or, where specified, retained as bounded previously recorded Framework evidence. The existing formally approved `State` and `Applicability` pairs remain unchanged. The [Assessment Template](../assessment-template.md) requires an explicit `Decision Rationale` for every `Resolved` Adoption Decision; `Needs Further Evaluation / —` remains valid when the decision evidence is insufficient.

## Decision candidates

| Responsibility | Approved State / Applicability | Recommended candidate | Remaining reviewer gate |
| --- | --- | --- | --- |
| `README-TECH-STACK` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Determine whether the unverified full tool inventory justifies a documented `PRESERVE`, or whether a **specific source-backed inaccuracy** merits `ADAPT` |
| `README-QUICK-START` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Decide documentary sufficiency threshold versus a clean pinned-SHA Docker Compose reproduction; avoid inferring Compose failure from a missing associated check |
| `README-DOCUMENTATION` | `Partial / Applicable` | **Consider `PRESERVE`** | Is task-oriented README navigation sufficient for intended readers, despite no exhaustive link/guide inventory? Use `ADAPT` only for a demonstrated discovery or accuracy gap |
| `README-FOOTER` | `Partial / Applicable` | **Consider `PRESERVE` strictly for the current cautious wording** | Confirm that retaining existing collaborative attribution and the no-new-license notice is desirable without making ownership, permission or legal sufficiency claims |

A `Partial` documentary State alone does **not** require `ADAPT`. Conversely `PRESERVE` does not turn a partial evaluation into `Satisfied`, prove runtime correctness, verify every link, or resolve a copyright uncertainty. `PRESERVE`/ `ADAPT` choices remain proposals until the maintainer **explicitly** approves each Adoption Decision separately from merging this packet.

## 1. README-TECH-STACK — keep unresolved pending a specific rationale

### Direct evidence

- The [pinned README technology table](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) lists Java 25, Spring Boot 4.0.5, Spring MVC/JPA/Hibernate, Spring Security/BCrypt, Thymeleaf/Bootstrap, H2, PostgreSQL 17/Flyway, JUnit/Mockito/MockMvc/Selenium and Docker/GitHub Actions/JaCoCo, grouped by purpose.
- The [pinned POM](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) explicitly sets the parent Spring Boot version `4.0.5` and `java.version=25` and includes Selenium and Sonar/JaCoCo settings. These confirm **selected declarations**, not every runtime invocation or workflow's actual completion.
- The [pinned Compose file](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) uses `postgres:17-alpine` and two services; its static definition does not establish successful deployment or production readiness.
- The [Framework Tech Stack Component](../../components/readme/tech-stack/README.md) recommends meaningful grouping but does not require an artificial Cloud category.

### Recommended decision posture

**Remain `Needs Further Evaluation / —` unless the maintainer affirmatively accepts `PRESERVE` with a bounded documentary rationale.** Any `ADAPT` should identify an exact unsupported claim or concrete reader-facing improvement and the needed source evidence. Do not propose new technologies or label an unverified tool as absent.

**Evidence still missing:** exhaustive dependency/tool usage cross-check, runtime execution evidence for the full declared stack, and a demonstrated reason to rewrite the table. A later review of source-specific statements can settle the choice without requiring an unrelated deployment.

## 2. README-QUICK-START — distinguish configured instructions from a reproduced start

### Direct and retained evidence

- The pinned README gives a command sequence to clone, create `.env` from `.env.example`, set a private `POSTGRES_PASSWORD`, build/start with `docker compose up --build -d`, inspect `docker compose ps` and open a **local** `http://localhost:8080/movies`.
- The directly re-fetched [pinned `.env.example`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.env.example) provides placeholders and local ports; [`compose.yaml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) uses loopback bindings, two named volumes, a PostgreSQL health check and an app dependency on healthy PostgreSQL.
- The README warns about `docker compose down -v` (destructive to the volumes), unknown public production suitability and the absence of automatic PostgreSQL demo data. These are genuine onboarding conditions.
- The previously recorded [pinned Compose evidence gap](only-film-compose-evidence-gap.md) identifies three successful H2/PostgreSQL CI checks on the pinned SHA, but **no verified positive Compose smoke check directly associated with that same SHA** in the inspected check set. The successful `postgres-schema` job starts the JAR on CI PostgreSQL, not via the advertised Compose route. The defined Compose smoke workflow is not a positive execution result.

### Recommended decision posture

**Remain `Needs Further Evaluation / —` until the maintainer explicitly chooses the decision threshold:**

- `PRESERVE`: existing command and safety guidance sufficiently serves the intended README reader, despite no independently verified complete pinned-SHA Compose startup. This is a **documentary decision**, not successful runtime reproduction.
- `ADAPT`: a specific misleading instruction, prerequisite, security caveat, or missing procedural explanation is identified. Document that concrete delta and its source evidence.
- `Needs Further Evaluation / —`: a clean pinned-SHA reproduction or equivalent bounded verification is required for the intended usage, but has not yet been observed. If requested, use the existing [Q1–Q8 reproducibility gates](only-film-compose-evidence-gap.md), disposable data, and never destroy real volumes.

Do **not** treat a localhost URL as public deployment, nor missing run evidence as a failed workflow. No Compose execution is authorized by this review.

## 3. README-DOCUMENTATION — consider preservation of existing navigation

### Direct evidence

- The pinned README includes task-oriented links to [PostgreSQL setup](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md), [PostgreSQL JPA integration tests](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md), a security audit and GitHub Actions workflows. The README also documents the repository's main `src/`, `docs/`, `.github/workflows/`, `Dockerfile`, `compose.yaml` and environment files.
- The [Framework README-DOCUMENTATION Component](../../components/readme/documentation/README.md) asks for important project documents to be grouped in a way readers can locate, using example subject categories rather than mandatory headings.
- The original Assessment approved `Partial / Applicable` because a complete README-document link liveness, comprehensive document inventory and navigability study were **not** performed. The presence of named guides was previously checked directly at the pinned reference, but not every link was verified for freshness or health.

### Recommended decision posture

**Consider `PRESERVE`** if the maintainer accepts the current task-oriented README navigation as sufficient for a portfolio/contributor audience. The absence of `## Documentation` alone is not a defect, and a duplicated index can increase maintenance cost.

Consider `ADAPT` only after identifying a particular important unlinked document, broken route or navigation problem with a clear audience effect. No new documentation index, contents page or consumer edit is authorized.

## 4. README-FOOTER — consider preservation without legal inference

### Direct evidence

- The pinned README attributes original academic collaboration to named team members and to [`certidevs/g1_testing`](https://github.com/certidevs/g1_testing), while describing later technical evolution separately and **not asserting exclusive original authorship**.
- Its final line says the project has an academic origin and that the README **does not establish an additional license by itself**; future REST API, real payments, observability and deployment automation remain explicitly prospective rather than claimed current features.
- The [Framework README-FOOTER Component](../../components/readme/footer/README.md) lists license, acknowledgments, related links and contact as possible elements, not mandatory all-at-once obligations.
- Contributor ownership, original-source reuse permissions, license grants, full credit completeness and external link liveness were **not independently verified**.

### Recommended decision posture

**Consider `PRESERVE` only for the current cautious, non-granting footer and academic contributor attribution**. This does **not** settle the separate `README-LICENSE` Responsibility, copyright or distribution rights. If the maintainer finds the closing order confusing or identifies an evidenced credit/wording issue, `ADAPT` may be reconsidered **without inventing legal claims**.

`PRESERVE` is not a substitute for a legal review, contributor permission, adding an unverified license, or modifying the consumer.

## Human review and follow-on

| Required confirmation | Expected output |
| --- | --- |
| `README-TECH-STACK` | `Resolved / PRESERVE`, `Resolved / ADAPT`, or `Needs Further Evaluation / —`, with evidence and explanation |
| `README-QUICK-START` | Independently choose the documentary/operational verification threshold and the decision; never assert a passing smoke run without evidence |
| `README-DOCUMENTATION` | Approve `PRESERVE` or supported `ADAPT`, or leave unresolved |
| `README-FOOTER` | Approve `PRESERVE` of cautious wording or supported `ADAPT`, or leave unresolved; copyright/licensing questions remain separate |

After express maintainer approval, record each approved `Resolved` decision and its rationale in a **separate PR** updating the canonical Assessment, review packet and consolidated matrix. Keep unresolved rows `Needs Further Evaluation / —`. Leave all **28 approved State/Applicability pairs unchanged**, the Assessment `In Progress`, and Only Film read-only.

**Merging this preparation packet is not formal Adoption Decision approval**, execution authority, a deployment permission or a decision to edit Only Film.
