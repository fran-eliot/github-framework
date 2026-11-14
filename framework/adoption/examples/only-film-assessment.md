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
| `README-HERO` | Required | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-OVERVIEW` | Required | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-FEATURES` | Required | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-TECH-STACK` | Required | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-QUICK-START` | Required | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-DOCUMENTATION` | Required | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-FOOTER` | Required | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-CHANGELOG` | Required | `Missing` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-STATUS` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-ARCHITECTURE` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-REPOSITORY-STRUCTURE` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-TESTING` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-ARCHITECTURE` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-PROJECT-STATUS` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-TESTING` | Recommended | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-ROADMAP` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-CONTRIBUTING` | Optional | **Unselected** (`Missing` / `Partial`; pending review) | `Uncertain` | `Needs Further Evaluation` | `—` |
| `README-DEMO` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-AUTHOR` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-HIGHLIGHTS` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `README-LICENSE` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-ADR` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-API` | Optional | **Unselected** (`Missing` / `Partial`; pending review) | `Uncertain` | `Needs Further Evaluation` | `—` |
| `DOC-DATABASE` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-DEPLOYMENT` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(local environment; proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-SECURITY` | Optional | `Partial` *(proposed; pending human approval)* | `Applicable` *(proposed)* | `Needs Further Evaluation` | `—` |
| `DOC-DIAGRAMS` | Optional | **Unselected** (`Missing` / `Partial`; pending review) | `Uncertain` | `Needs Further Evaluation` | `—` |
| `DOC-REFERENCES` | Optional | `Partial` *(proposed; pending human approval)* | `Uncertain` *(applicability pending review)* | `Needs Further Evaluation` | `—` |

**Coverage:** twenty-five Responsibilities have selected **proposed States** (including one with Applicability `Uncertain`); three additional Responsibilities have structured entries with State **not selected** and Applicability `Uncertain`. All **28/28** Responsibilities now have structured working entries, but the three unresolved States and outstanding human review prevent completion. The [28-Responsibility review matrix](only-film-consolidated-review-matrix.md) contains hypotheses and review priorities for the remaining items, **not approved assessment results**. The summary and Responsibility Details now follow the Template's canonical order; human review and completion requirements are still outstanding.

The `State` and `Applicability` cells above are technically recommended contractual values; their *approval status* is separate from the values themselves. Their inclusion does not imply formal human sign-off.

---

## 3. Responsibility Details

### README-HERO

**Requirement Level**

`Required`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Canonical` in the functional sense: the README opens with an explicit project heading, short introductory description, and a limited group of technology badges.

**Uncertainty**

- Whether the opening introduction is sufficiently distinct from the later overview and adequately conveys the project identity and intended audience.
- Whether the badges and heading remain legible and visually coherent on the intended screen sizes and light/dark themes; no responsive rendering review is recorded.
- Whether the headline technology versions are current at the pinned SHA beyond those already checked against POM and Compose.

**Detected Facts**

- The pinned README begins with `# 🎬 Only Film`, followed by a brief description identifying the project and its principal technologies.
- An additional paragraph introduces the academic collaboration from which the project originated and its subsequent technical development.
- Five badges identify Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway, and Docker Compose.
- The [README-HERO Component](../../components/readme/hero/README.md) describes clear naming, tagline, structure, and restrained badge use. A decorative banner is **optional**, and the absence of one is not a defect.
- Java, Spring Boot, and PostgreSQL versions have supporting pinned configuration evidence; the prior semantic review did not verify every visual rendering context.

**Evidence**

- [Pinned README — heading, introduction, badges](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [README-HERO Component](../../components/readme/hero/README.md)
- [Required identity and overview E3 semantic review](only-film-required-identity-semantic-review.md)
- [Pinned pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Pinned compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml)

**Evaluation Rationale**

The main heading, short introduction, and five badges visibly serve the Hero Responsibility; a banner or a separately titled tagline is not a mandatory prerequisite. The remaining questions are editorial distinction from Overview, reader clarity, and display compatibility, which were not reviewed as completed. `Partial` remains a **proposed editorial hypothesis**, not a documented visual failure or absent identity. A human reviewer can select `Satisfied` if the present introduction is sufficiently clear and readable.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The reviewer must decide whether `PRESERVE` or a bounded `ADAPT` is appropriate once the actual README appearance and clarity are considered. No change to the consumer is authorized.

---

---

### README-OVERVIEW

**Requirement Level**

`Required`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — the project's functional overview is integrated into the introductory README paragraphs rather than a separately titled `Overview` section.

**Uncertainty**

- Whether the introduction clearly explains the problem solved and value to visitors, users, and maintainers beyond describing functions.
- Whether the current mix of product summary, technology stack, and academic origins keeps the Overview understandable and distinct from Hero.
- Whether a separate heading would improve navigation or simply duplicate a sufficiently clear existing introduction.

**Detected Facts**

- The pinned README introduces Only Film as a cinema-management web application and outlines movie listings, screenings, seat selection, ticketing, and role-based administration.
- A following paragraph explains the academic collaboration and subsequent technical development of the repository.
- The [README-OVERVIEW Component](../../components/readme/overview/README.md) expects a clear description of the project, its purpose, and the problem it addresses, without turning the overview into installation or detailed implementation guidance.
- The README introduction already fulfills a recognizable overview function; the absence of a literal `## Overview` heading does not demonstrate that the Responsibility is missing.

**Evidence**

- [Pinned Only Film README — introductory overview](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [README-OVERVIEW Component](../../components/readme/overview/README.md)
- [Required Hero, Overview, and Features E3 semantic review](only-film-required-identity-semantic-review.md)

**Evaluation Rationale**

The introductory paragraphs convey the nature and scope of the application, so a `Missing` State is not supported. The remaining questions concern the separation of product purpose from technical description and history, and the reader's ability to identify the project's benefit without duplicative text. `Partial` is a **conservative proposed editorial judgment**, not proof of a defective overview. A reviewer may reasonably approve `Satisfied` if the existing introduction meets the Component's documentary purpose without a separate section title.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Whether to `PRESERVE` the existing introduction or `ADAPT` its organization requires human review of the communication goals. This record does not authorize changes to Only Film.

---

---

### README-FEATURES

**Requirement Level**

`Required`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Equivalent` — a role-grouped `Funcionalidades` section fulfills the feature-summary function without the canonical English heading.

**Uncertainty**

- Whether every capability listed for visitors, registered users, and administrators accurately represents the pinned consumer commit.
- Whether demonstration ticket purchase/checkout is clearly distinguishable from integration with a real payment provider.
- Whether the paragraph on database transactions and seat-locking is appropriate in a feature summary or should be linked from architecture documentation.

**Detected Facts**

- The pinned README has a `Funcionalidades` section organized by visitor, user, and administrator roles. It describes movie and session browsing, registration/login, seat and ticket operations, reviews, and management capabilities.
- The feature description refers to simulated purchasing, not a verified production payment integration.
- An additional paragraph describes transactional controls and database locking to prevent duplicate seat sales; this is an implementation characteristic rather than solely an end-user capability.
- The Framework's `README-FEATURES` Component focuses on concise main capabilities instead of extensive implementation detail.
- The pinned H2/PostgreSQL CI checks provide bounded regression evidence but do **not** establish independent functional acceptance of every advertised feature.

**Evidence**

- [Pinned Only Film README — Funcionalidades](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [README-FEATURES Component](../../components/readme/features/README.md)
- [Required identity/overview/features semantic review](only-film-required-identity-semantic-review.md)
- [Pinned CI run](https://github.com/fran-eliot/only_film/actions/runs/39283862407)

**Evaluation Rationale**

The consumer has an explicit, audience-oriented feature summary, so `Missing` would misrepresent the inspected README. The roles and capabilities are recognizable, but the assessment has not established feature-by-feature accuracy or whether the technical transaction paragraph obscures the user-facing overview. `Partial` is a **provisional editorial hypothesis**, not a confirmed functionality gap or failed acceptance test. The reviewer can approve `Satisfied` if the current wording accurately communicates the main functions at the level expected for this Required Responsibility.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The maintainer must confirm feature accuracy and select `PRESERVE` or `ADAPT` only when documentary changes are justified. Nothing in this working assessment authorizes edits to the Only Film consumer.

---

---

### README-TECH-STACK

**Requirement Level**

`Required`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Canonical` in the documentary sense: a project-specific `Tecnologías y arquitectura` section groups technologies by functional layer, rather than mechanically reproducing the Framework Component's suggested categories.

**Uncertainty**

- Whether every technology listed is actually used in the described runtime, development, or test context at the pinned consumer commit.
- Whether the technological inventory and architecture summary remain sufficiently easy to navigate without forcing generic Cloud categories onto a consumer with no verified cloud deployment.
- Whether additional evidence is needed for the less directly inspected dependencies and tools beyond the already corroborated Java, Spring Boot, and PostgreSQL versions.

**Detected Facts**

- The pinned README's technology table distinguishes backend, security, frontend, local persistence, durable persistence, testing, and infrastructure.
- It identifies Java 25, Spring Boot 4.0.5, Spring MVC, Spring Data JPA, Hibernate, Spring Security, BCrypt, Thymeleaf, Bootstrap 5, H2, PostgreSQL 17, Flyway, JUnit 5, Mockito, MockMvc, Selenium, Docker Compose, GitHub Actions, and JaCoCo.
- The pinned `pom.xml` declares `java.version=25` and Spring Boot parent version `4.0.5`, corroborating the prominent Java and Spring Boot version claims.
- The pinned `compose.yaml` uses `postgres:17-alpine` and defines `app` and `postgres` services, corroborating PostgreSQL 17 and Docker Compose configuration **statically**, not demonstrating successful deployment.
- The [README-TECH-STACK Component](../../components/readme/tech-stack/README.md) suggests categories for orientation but does not require every possible environment category.

**Evidence**

- [Pinned Only Film README — technology and architecture table](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Pinned compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml)
- [README-TECH-STACK Component](../../components/readme/tech-stack/README.md)
- [Tech Stack, Documentation, and Footer E3 semantic review](only-film-required-final-semantic-review.md)

**Evaluation Rationale**

A clearly identified, categorized technology table exists, and the most salient version claims were cross-checked against versioned POM and Compose configuration. Consequently, absence of a specific suggested category or a differently named heading would not justify `Missing`. `Partial` is a **conservative proposed judgment** about complete inventory accuracy and editorial sufficiency; no comprehensive audit of all dependencies and uses has been performed. Human review may reasonably confirm `Satisfied` if the table is accurate and adequate for the README's audience, without demanding a Cloud section unrelated to this application.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The reviewer must determine whether the table warrants `PRESERVE` or a specific `ADAPT` for inaccurate or confusing entries. This proposed record does not authorize new infrastructure or revisions to Only Film.

---

---

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

**P1 Reviewer Disposition**

**Pending — no acceptance or rejection recorded.** The following alternatives are **decision criteria**, not approved States:

- **Documentation-only review:** inspect the pinned instructions, `.env.example`, Dockerfile, `compose.yaml`, and PostgreSQL guide for a complete, coherent local onboarding path. The existing static review supports readability and consistency, **not demonstrated execution**. If this is the accepted scope for a README documentation Responsibility, the reviewer may approve `Satisfied` with that limitation stated.
- **Operational reproduction required:** review the [Q1–Q8 gates](only-film-compose-evidence-gap.md) using a disposable environment and synthetic secrets. In the inspected checks for pinned run [39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407), JAR-on-PostgreSQL success **cannot substitute** for a Compose build/start. A missing run is an evidence gap, not a failing test.
- **Retain or revise `Partial`:** identify a **specific** material documentation problem or accepted evidence threshold not met. Do not use `Partial` exclusively as a precaution.

**Acceptance record:** Reviewer: *unassigned*; reference: `28d75a50e0a178954dd46acc23300d9dd327843c`; chosen documentary/operational threshold: *pending*; evidence disposition: *pending*; approved State and date: *none recorded*; Adoption Decision: `—`.
**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

No downstream `PRESERVE`, `ADAPT`, or other Adoption Decision is approved. The reviewer must determine the sufficiency threshold and whether to request a reproducible Compose smoke run using the recorded Q1–Q8 gates. Any operational reproduction must use disposable data and avoid destructive cleanup of existing volumes.

---

---

### README-DOCUMENTATION

**Requirement Level**

`Required`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — the README links to relevant project documentation in task-oriented sections rather than providing a standalone documentation index.

**Uncertainty**

- Whether important source documents are discoverable by new contributors from the README's dispersed links.
- Whether any critical links are stale, important documents lack entry points, or existing navigation creates material duplication; a comprehensive link audit has not been performed.
- Whether a documentation index would add measurable value or the current task-oriented layout already meets the Component's purpose.

**Detected Facts**

- The pinned README links to `docs/screenshots/`, `docs/POSTGRESQL_SETUP.md`, `docs/SECURITY_HARDENING_AUDIT.md`, `docs/POSTGRESQL_INTEGRATION_TESTS.md`, and project GitHub Actions workflows.
- Its `Organización del repositorio` section outlines `src/main`, `src/test`, `docs/`, `.github/workflows/`, and key Docker and configuration files.
- The PostgreSQL setup and integration-testing documents were observed at the pinned consumer SHA. Their existence does not guarantee that every documentation link remains current.
- The Framework's [README-DOCUMENTATION Component](../../components/readme/documentation/README.md) encourages grouping important resources. Architecture, ADR, Roadmap, API, and Deployment are examples; this does not mandate every documentation category for every consumer.
- There is no literal `## Documentation` heading in the inspected README. The Responsibility can nevertheless be fulfilled through distributed links, so absence of that heading is **not** proof of `Missing`.

**Evidence**

- [Pinned README — linked documentation and repository organization](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [Pinned PostgreSQL integration testing guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md)
- [README-DOCUMENTATION Component](../../components/readme/documentation/README.md)
- [Required Tech Stack, Documentation, and Footer E3 review](only-film-required-final-semantic-review.md)

**Evaluation Rationale**

The README offers concrete navigation to important project resources. Therefore the documentation Responsibility is not absent merely because there is no canonical index heading. The question is whether the distributed organization is discoverable, complete enough for the intended audience, and consistent with the repository at the pinned SHA. `Partial` remains a **conservative, unapproved navigation-sufficiency hypothesis**, not a verified broken-link finding. A human reviewer may select `Satisfied` if the task-based references are demonstrably useful without an extra index.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The reviewer must establish whether to `PRESERVE` the distributed navigation or `ADAPT` any concrete gaps, based on link validation and audience needs. This record does not authorize a new documentation index or consumer edits.

---

---

### README-FOOTER

**Requirement Level**

`Required`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Equivalent` — concluding attribution and license-context material appears in the final README sections instead of a separate canonical Footer block.

**Uncertainty**

- Whether the credit statement comprehensively and accurately represents the original collaborators and subsequent maintainers.
- Whether the final license notice is clearly understandable without implying reuse permission that has not been legally established.
- Whether the concluding section arrangement communicates an effective close to the README, given that future-work material follows the origin/credits section.
- Whether additional related links or contact information would serve the audience; the Component does not require every optional Footer element.

**Detected Facts**

- The pinned README includes `Origen, créditos y evolución`, attributing the academic origins to multiple contributors and linking the original [certidevs/g1_testing](https://github.com/certidevs/g1_testing) repository.
- The text distinguishes later work on `fran-eliot/only_film` from exclusive authorship of the original collaborative project.
- `Próximas líneas de evolución` follows, listing potential future improvements rather than implemented features.
- The final README line contains a `Licencia` note referring to the academic origin and the original repository; it explicitly does **not** establish an additional license through the README itself.
- The Framework [README-FOOTER Component](../../components/readme/footer/README.md) allows license, acknowledgments, related links, and contact information but does not require all of them.
- The existence of a credit and license notice is **documentary evidence**, not a verified legal determination of rights, ownership, or permitted reuse.

**Evidence**

- [Pinned README — credits, evolution, and license notice](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [README-FOOTER Component](../../components/readme/footer/README.md)
- [Required Tech Stack, Documentation, and Footer E3 review](only-film-required-final-semantic-review.md)
- [Original academic repository, linked as background](https://github.com/certidevs/g1_testing)

**Evaluation Rationale**

The README already contains attribution, project history, and cautious license information, satisfying identifiable Footer functions. The remaining review concerns editorial composition and clarity, not whether the document has a literal Footer heading or a specific contact block. `Partial` is a **provisional assessment of documentary suitability**, not a finding that credit is incorrect or a statement that the project is licensed for reuse. If the present closing text is clear and appropriate for the consumer's audience, a reviewer may justify `Satisfied`.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

A human reviewer must determine whether to `PRESERVE` the current closing material or `ADAPT` its organization or wording without introducing unauthorized legal or ownership claims. No modifications to Only Film are approved.

---

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

**P1 Reviewer Disposition**

**Pending — no formal State approval recorded.** The proposed `Missing` is supported by the inspected versioned documentation, but the reviewer should apply the following discrimination criteria:

- **Approve proposed `Missing` only if** the reviewer accepts the documented scope of the pinned README/tree/POM/commits, the reported absence of tags and Releases, and no substantive curated versioned-change record or equivalent is identified. The absence of `CHANGELOG.md` at one path is insufficient on its own.
- **Reconsider `Partial` or `Satisfied` if** an actual consumer-facing, maintained record of changes is identified and its scope is assessed. Raw commits, PR lists, `0.0.1-SNAPSHOT`, and the academic origin narrative are not automatically such a record.
- **Record provenance separately:** tag and Release absence was **maintainer-reported on 2026-11-13**; independent tag inventory was not executed. Earlier GitHub Releases API observations were empty but are time-dependent. Any later search must record date and its relation to the pinned commit.

**Acceptance record:** Reviewer: *unassigned*; reference: `28d75a50e0a178954dd46acc23300d9dd327843c`; equivalent-source determination: *pending*; confirmed State and date: *none recorded*; Adoption Decision: `—`.
**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The recommended `State` can be assessed without selecting an implementation action. The maintainer must review the proposal and determine whether the right downstream decision is `ADD`, `ADAPT`, `ACCEPT`, or another permitted value after considering audience, existing equivalent sources, and maintenance scope. No change to Only Film is authorized by this record.

---

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

---

### README-REPOSITORY-STRUCTURE

**Requirement Level**

`Recommended`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Canonical` in a descriptive sense: the README includes an explicit directory tree, but the Framework review did not identify a standalone Component specification for this Responsibility.

**Uncertainty**

- Whether the concise tree is accurate and sufficiently navigable for a new contributor at the pinned consumer SHA.
- Whether omitted paths are genuinely important for orientation rather than intentionally excluded implementation detail.
- The absence of a separately identified `README-REPOSITORY-STRUCTURE` Component in the inspected Framework catalog is a Framework coverage question, **not** proof of a defect in Only Film.

**Detected Facts**

- The pinned README contains `Organización del repositorio`, summarizing `src/main/java/com/demo`, template/static resources, `db/migration`, tests, `docs/`, `.github/workflows/`, `Dockerfile`, `compose.yaml` and `.env.example`.
- The earlier pinned-tree review confirmed the principal referenced paths. The README tree is intentionally an overview and does not claim to list every file.
- `README-REPOSITORY-STRUCTURE` is `Recommended` in `TPL-BACKEND` 0.1.0 metadata, regardless of whether an independently documented Component exists.

**Evidence**

- [Pinned README — repository organization](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned consumer repository tree](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [Canonical TPL-BACKEND metadata](../../templates/repositories/backend/metadata.yml)
- [Recommended README semantic review](only-film-recommended-readme-semantic-review.md)

**Evaluation Rationale**

The README already gives readers an intelligible map of the project's major source, resource, migration, documentation, and automation paths. Therefore the Responsibility is not `Missing`. The `Partial` proposal is a **conservative, unapproved hypothesis about currency and usability**, not an assertion that the directory tree is wrong or insufficient merely because it is abbreviated. The reviewer may confirm `Satisfied` if the displayed layout is accurate and adequately supports navigation.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

No rewrite or new Component is authorized. The reviewer must evaluate whether to `PRESERVE` the existing overview or `ADAPT` any genuinely misleading or missing navigation information.

---

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

**P1 Reviewer Disposition**

**Pending — the proposed `Partial` State has not been approved.** Review the README as an **onboarding and test-selection guide**, separate from asserting complete test success:

- **Scope of commands:** `./mvnw test` is a documented general local command; the pinned CI `h2-regression` executes a selected test set. A passing filtered CI job does not demonstrate that a clean-clone invocation of the general command works.
- **Scope of execution:** [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) supports 329 H2 regression tests with zero failures, errors or skips, and two successful PostgreSQL jobs. It does **not** establish successful Selenium, manual-suite or Compose execution at the pinned SHA.
- **Documentation acceptance threshold:** confirm that prerequisites, appropriate local commands, workflow trigger conditions, test boundaries and limitations are discoverable without presenting optional/manual jobs as obligatory PR checks. If the README already meets that purpose, the reviewer may justify `Satisfied` even though not every suite has been executed. Retain `Partial` only for a concrete material guidance gap.

**Acceptance record:** Reviewer: *unassigned*; pinned SHA: `28d75a50e0a178954dd46acc23300d9dd327843c`; command/trigger accuracy: *pending*; documentary sufficiency decision: *pending*; approved State and review date: *none recorded*; Adoption Decision: `—`.
**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Whether to `PRESERVE` the README guidance or `ADAPT` its clarity and prerequisites remains subject to the maintainer's review. Neither code nor workflow changes are approved by this assessment record.

---

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

**P1 Reviewer Disposition**

**Pending — the proposed `Partial` State has not been approved.** Review the specialized guides as a **maintainable, discoverable testing reference**, with evidence claims explicitly bounded:

- **Protocol and reproducibility:** confirm the PostgreSQL, JaCoCo and SonarCloud guides describe supported prerequisites, command selection, CI triggers, artifact inspection, and expected limits. A distributed collection is not automatically defective if it is navigable and accurate.
- **JaCoCo evidence:** the pinned run log confirms `jacoco:report` and a historically successful artifact upload (`jacoco-h2-regression`, ID `12201642997`). Later artifact listing returned no copies; report XML/HTML and any coverage percentage were **not verified**. Do not calculate coverage from 329 Surefire tests or imply whole-project coverage.
- **Sonar evidence:** the scanner log shows `ANALYSIS SUCCESSFUL` and JaCoCo import. The historical CE task `AaFU8vS6n_jCCWP5LQvY` did not yield a verified final processing status, `analysisId`, or Quality Gate. The present `main` dashboard is not a substitute for that historical result.
- **Verdict threshold:** the reviewer should approve `Satisfied` if the documents accurately meet the testing-documentation purpose even with a historical coverage/Quality Gate caveat, or justify `Partial` with a specific usability or accuracy deficiency. Do not treat unavailable metrics as evidence of test failure.

**Acceptance record:** Reviewer: *unassigned*; pinned SHA: `28d75a50e0a178954dd46acc23300d9dd327843c`; guide coverage and navigation: *pending*; JaCoCo/Quality Gate evidence threshold: *pending*; approved State and review date: *none recorded*; Adoption Decision: `—`.
**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

A human review must determine whether to `PRESERVE` the specialized guidance, `ADAPT` discoverability or reproducibility instructions, or choose another supported action. No new test run, coverage figure, Quality Gate determination, or consumer modification is authorized.

---

---

### README-ROADMAP

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — the README summarizes possible evolution, and a separate, historically pinned F3 functional audit and roadmap records more detailed initiatives.

**Uncertainty**

- Whether the future-work items in the README still reflect real priorities at the pinned consumer SHA.
- Which initiatives F3.002–F3.008 in the older audit were implemented, revised, or superseded by the pinned reference; this has not been independently reconciled.
- Whether a brief future-work summary suffices for the audience or should link to an up-to-date planning source.

**Detected Facts**

- The pinned README has a `Próximas líneas de evolución` section mentioning possible REST API, real payment integration, observability, and deployment automation; these are framed as **potential future work**, not completed capabilities.
- The pinned repository contains `docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md`, listing initiatives F3.002–F3.008 from an **earlier** baseline `df63353564485eb6d2d60c982032e5d3c4facbf2`.
- The existing F3 document cannot establish, solely by its presence in the later tree, which initiatives remain open or have already been completed at the assessed commit.
- The Framework's [README-ROADMAP Component](../../components/readme/roadmap/README.md) supports a concise overview of upcoming phases, not a duplicated detailed planning document.

**Evidence**

- [Pinned README — future development](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned historical F3 audit and roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md)
- [README-ROADMAP Component](../../components/readme/roadmap/README.md)
- [Optional README governance semantic review](only-film-optional-governance-semantic-review.md)

**Evaluation Rationale**

The README already communicates possible future directions, so a canonical roadmap heading or extra document is not automatically necessary. However, the historical planning document is tied to another commit and cannot be treated as proof of the current backlog. `Partial` is a **proposed assessment of currency and editorial usefulness**, not a finding that every F3 initiative is outstanding. The reviewer may approve `Satisfied` if a concise forward-looking summary is all the Optional Responsibility needs for this portfolio consumer.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

A `PRESERVE` or `ADAPT` decision requires verifying that the future-work descriptions remain accurate and valuable to the consumer's intended audience. No new roadmap promises or modifications to Only Film are authorized.

---

---

### README-CONTRIBUTING

**Requirement Level**

`Optional`

**State**

**Not selected** — `Missing` or `Partial` are the documentary hypotheses requiring discrimination. This is explicitly an **incomplete Assessment field**, not a third contractual State and not a declaration of `Missing`.

**Applicability**

`Uncertain` — no verified policy or confirmed intention to accept external contributions at the pinned consumer reference.

**Implementation Characteristics**

`Distributed` is a **possible** characteristic of the existing development instructions; no independently verified contribution governance or acceptance procedure has been established.

**Uncertainty**

- Whether the maintainer intends the repository to accept external contributions and, if so, under what policy and review process.
- Whether contribution rules exist outside the inspected README and tree, for example in GitHub repository settings, PR templates, project-level guidance, or other maintained sources.
- Whether technical setup/test guidance constitutes a partial contribution entry point or a distinct contributing policy is necessary for the intended audience.
- An inspected Framework Component catalog did not locate a standalone `README-CONTRIBUTING` Component despite this Responsibility appearing in Template metadata. That is a **Framework-side specification question**, not evidence that Only Film is deficient.

**Detected Facts**

- The pinned README provides development prerequisites, test commands, CI descriptions, and source-code orientation that may support technical onboarding.
- The earlier pinned-tree inspection did not find a `CONTRIBUTING.md` file; absence of that filename does not rule out an equivalent policy.
- The prior semantic review did not verify rules for external collaborators, PR submission, acceptance/review, or commit conventions.
- `README-CONTRIBUTING` is `Optional` in `TPL-BACKEND` 0.1.0; optionality alone does **not** establish `Not Applicable`.

**Evidence**

- [Pinned README — development and testing guidance](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned consumer tree](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [TPL-BACKEND metadata](../../templates/repositories/backend/metadata.yml)
- [Optional governance E3 semantic review](only-film-optional-governance-semantic-review.md)

**Evaluation Rationale**

The README contains actionable technical onboarding information, but those instructions are not automatically a policy on who may contribute, how changes are proposed and reviewed, and how contributions are accepted. `Partial` would require treating technical onboarding as an adequate subset of the intended Responsibility; `Missing` would require establishing that no substantive contributing guidance is present. Neither conclusion has been human-reviewed, and whether the Responsibility is applicable to this consumer's collaboration model is unresolved. Recording `Uncertain` Applicability and leaving State unselected is more traceable than manufacturing a contractual answer.

**Reviewer Discrimination Gate — State and Applicability**

**Open; no State or Applicability approval recorded.** Decide the intended contribution model first. Technical setup, tests and CI instructions in the pinned README support onboarding but do not themselves establish who may propose changes, review expectations or acceptance policy.

- **If the repository accepts contributions:** inspect maintained contribution policy or equivalent repository/project guidance. Choose `Partial` only if the existing guidance demonstrably fulfills a meaningful subset of that applicable purpose; choose `Missing` if no substantive contributing guidance meets it. `Satisfied` also requires sufficient evidence, not just an expected filename.
- **If external contributions are not intended:** document the audience and whether this Optional Responsibility is `Not Applicable`; do not infer that solely from the absence of `CONTRIBUTING.md` or from the Template's Optional level.
- **Evidence needed:** maintainer's current contribution policy, the pinned README, any equivalent instructions or GitHub collaboration settings, and an explicit review of which obligations are in scope.

**Disposition record:** Accepted contribution model: *pending*; equivalent governance evidence: *unverified*; proposed contractual State: *unselected*; Applicability: `Uncertain`; reviewer/date: *not recorded*. `Needs Further Evaluation` and `Adoption Decision: —` remain unchanged.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

First establish the intended contribution model and any existing policy. Then approve a contractual State and Applicability and decide, if justified, between `PRESERVE`, `ADAPT`, `ADD`, `ACCEPT`, or `OMIT`. No contribution policy is created or authorized here.

---

---

### README-DEMO

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — screenshots embedded in the README and a documented local startup path, rather than an independently verified public demo.

**Uncertainty**

- Whether the screenshots accurately represent the behavior and appearance at the pinned consumer SHA; image presence was checked, but visual fidelity and freshness were not.
- Whether screenshots satisfy the portfolio audience or a reproducible local demonstration is also needed.
- Whether demo-data prerequisites and the absence of an online demo are communicated sufficiently; no public demo is established by a localhost URL.
- Whether Docker Compose startup can be reproduced at the pinned SHA; a passing Compose smoke execution linked to that reference was not verified.

**Detected Facts**

- The pinned README includes `Capturas de la aplicación` with images of the movie listing, movie details, seat selection, and a QR ticket.
- Other versioned interface screenshots appear in `docs/screenshots/`; their quality and representativeness were not visually audited in the prior semantic review.
- The README describes Docker Compose startup and `http://localhost:8080/movies`, which is a **local address**, not a hosted demonstration.
- A Compose smoke workflow definition exists, but the previously reviewed CI checks did not establish successful execution of that workflow for the pinned commit.

**Evidence**

- [Pinned README — screenshots and local startup](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned screenshots directory](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/docs/screenshots)
- [Optional Demo, Highlights and Diagrams E3 semantic review](only-film-optional-showcase-semantic-review.md)
- [Compose smoke evidence gap](only-film-compose-evidence-gap.md)

**Evaluation Rationale**

The repository already shows the application through documented screenshots, so the Responsibility is not automatically `Missing` merely because no public live demo was verified. `Partial` is a **provisional judgment of demo clarity and reproducibility** rather than an observed broken workflow or an obligation to deploy the project publicly. The reviewer may find the existing visual examples sufficient for this Optional Responsibility.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Decide whether to `PRESERVE` the current screenshot-based presentation or `ADAPT` its explanation after validating the screenshots and audience needs. No demo deployment or consumer edit is authorized.

---

---

### README-AUTHOR

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Equivalent` — attribution and credits are embedded in `Origen, créditos y evolución`, not in a separately titled Author block.

**Uncertainty**

- Whether all material original contributors and later maintainers are credited accurately and with an appropriate distinction of roles.
- Whether an additional author/contact link would improve clarity, without implying exclusive authorship of academic group work.
- Whether any licensing or intellectual-property rights can be substantiated; attribution does **not** independently verify code ownership or permissions.

**Detected Facts**

- At the pinned SHA, the README credits four members of the academic collaboration and links their profiles and the original `certidevs/g1_testing` repository.
- The narrative distinguishes the original collaborative creation from subsequent evolution under `fran-eliot/only_film`, without representing the entire initial project as one person's exclusive work.
- The [README-AUTHOR Component](../../components/readme/author/README.md) permits an author or team to be identified through names and links; a literal `Author` heading is not required.

**Evidence**

- [Pinned README — origins and credits](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [README-AUTHOR Component](../../components/readme/author/README.md)
- [Original academic repository](https://github.com/certidevs/g1_testing)
- [Optional README governance E3 semantic review](only-film-optional-governance-semantic-review.md)

**Evaluation Rationale**

Authorship and project-origin attribution are already present and directly relevant to the Responsibility; the lack of an exact heading does not make the section `Missing`. `Partial` is a **conservative editorial hypothesis** until the clarity and completeness of original and later contributions are reviewed. This is not a legal judgment or an inference of ownership. A reviewer may justify `Satisfied` if the existing credits fulfill the Component's communication purpose.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The maintainer must assess whether to `PRESERVE` the existing balanced attribution or `ADAPT` specific wording/links with verified facts. No retroactive attribution change or license claim is authorized.

---

---

### README-HIGHLIGHTS

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — notable implementation choices are already described within `Funcionalidades` and `Seguridad y límites actuales`, without a distinct Highlights section.

**Uncertainty**

- Whether a small selection of highlights would materially clarify this portfolio project's differentiators instead of repeating Features.
- Which of the stated technical qualities are sufficiently supported at the pinned commit and should be presented prominently.
- Whether the README already balances domain features, security limitations and implementation details for its audience.

**Detected Facts**

- The pinned README describes measures against duplicate seat sales, transactional checkout, role-based access, review authorization, image validation, and PostgreSQL/Flyway migration support.
- `Funcionalidades` describes visitor, user and administrator capabilities; `Seguridad y límites actuales` explicitly qualifies the checkout as simulated, not a real payment gateway.
- [GitHub Actions run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) records 329 successful H2 tests and three successful checks for the pinned SHA, providing **bounded** regression support rather than complete validation of every feature or user experience.
- No literal `Highlights` heading appears in the inspected README; that absence alone is not a failure of this Optional Responsibility.

**Evidence**

- [Pinned README — Features and security limitations](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Verified Surefire and Sonar log evidence](only-film-verified-surefire-sonar-logs.md)
- [Optional showcase E3 semantic review](only-film-optional-showcase-semantic-review.md)

**Evaluation Rationale**

Differentiating qualities are communicated through existing sections and some claims have bounded technical support. A dedicated Highlights block may improve portfolio readability, but could also duplicate Features without adding information. `Partial` is a **provisional editorial interpretation**, not proof that the current README lacks compelling highlights or that a dedicated block is required. A reviewer can approve `Satisfied` if the distributed presentation already meets the consumer's needs.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

A future `PRESERVE` or `ADAPT` choice should follow an editorial review of actual value, factual support and duplication, not a requirement to manufacture showcase text.

---

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

**P1 Reviewer Disposition**

**Pending — the proposed `Partial` State is not approved.** Assess the **accuracy of license-status communication** independently from ownership and permission to distribute or relicense original contributions.

- **Observed documentary notice:** the pinned README identifies collaborative academic origins, points toward the original source, and expressly avoids granting an additional license. The inspected root paths did not identify `LICENSE`, `LICENCE` or `COPYING`, and the POM's `<licenses><license/></licenses>` entry has no terms. These observations **do not establish legal permission or prohibit use** by themselves.
- **Rights and attribution boundary:** original academic collaboration involved multiple contributors, while later evolution occurred in the maintained fork. Neither GitHub hosting, subsequent technical work, repository visibility, nor a README notice proves sole ownership or authority to grant a license over the entire codebase.
- **Documentation acceptance threshold:** decide whether the current cautionary notice accurately communicates the **unverified** terms to readers without suggesting an implied open-source license. `Satisfied` may be defensible if that disclosure meets the Optional documentary purpose; `Partial` requires a specific clarity gap. This is separate from the legally supported rights position, which remains unresolved here.
- **Downstream boundary:** do not select a license, assert permission, replace attribution, or add `LICENSE` as an automatic consequence of this Assessment. Obtain authoritative rights information or appropriate advice before any stronger licensing statement.

**Acceptance record:** Reviewer: *unassigned*; consumer SHA: `28d75a50e0a178954dd46acc23300d9dd327843c`; communication adequacy: *pending*; rights evidence: *not verified*; approved State/date: *not recorded*; Adoption Decision: `—`.
**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Before choosing `PRESERVE`, `ADAPT`, `ADD`, or another valid action, the maintainer must establish the intended audience and obtain appropriate rights information if stronger permission statements are contemplated. This working record neither creates nor recommends a specific license grant.

---

---

### DOC-ADR

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Distributed` — technical decisions and operational constraints are explained within specialized documents, but a consolidated ADR convention or inventory was not established in the bounded earlier review.

**Uncertainty**

- Whether important, durable architectural decisions are sufficiently documented with context, alternatives, decision, consequences, and present validity.
- Whether a formal ADR index would add useful traceability, or simply duplicate existing, task-specific documents.
- Which recommendations in earlier architecture audits still correspond to current, accepted decisions at the pinned SHA.

**Detected Facts**

- The pinned `docs/FLYWAY_V2_SEAT_UNIQUENESS.md` explains `UNIQUE(session_id, fila, seat)`, preservation of existing V1 migration history, duplicate-data checks, `NULL` considerations, and careful non-destructive handling of collisions.
- The pinned `docs/DEPENDENCY_MAINTENANCE.md` explains weekly Dependabot updates, review of major versions separately, and avoidance of unattended auto-merge.
- The pinned `docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md` contains historical options and risks. It uses a different baseline and must not be read as a current approved ADR inventory.
- The earlier inspected tree did not identify an `adr/` directory or `ADR-*` filenames; this does **not** establish the absence of documented decisions in other forms.
- The prior Framework catalog review did not identify a separate `DOC-ADR` Component specification. The Template metadata does include the `Optional` Responsibility; no absent Component rule is imposed on the consumer.

**Evidence**

- [Pinned Flyway V2 seat uniqueness document](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md)
- [Pinned dependency maintenance document](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md)
- [Historical architecture audit in pinned tree](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md)
- [Canonical Template metadata](../../templates/repositories/backend/metadata.yml)
- [Optional technical E3 semantic review](only-film-optional-final-semantic-review.md)

**Evaluation Rationale**

The consumer already documents reasons and operational consequences of meaningful technical choices. Therefore the Responsibility is not necessarily `Missing` merely because there is no folder named `adr`. The existing documents do not yet demonstrate a maintained, comparable record of the main architectural decisions and their current status. `Partial` is a **conservative proposed documentary interpretation**, not proof that an ADR register must be introduced. The reviewer should assess whether an optional formal register is valuable given the project's size and existing documentation.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The maintainer must decide whether to `PRESERVE` the existing decision explanations or `ADAPT` their organization after considering value and duplication. No new ADR process or consumer edit is authorized.

---

---

### DOC-API

**Requirement Level**

`Optional`

**State**

**Not selected** — `Missing` or `Partial` are the current hypotheses, contingent on an agreed scope for API documentation. This entry is **not yet a completed contractual State evaluation**.

**Applicability**

`Uncertain` — no independently confirmed public REST/JSON API contract, but an interface-documentation need has not been categorically ruled out.

**Implementation Characteristics**

No public API contract implementation was verified in the prior evidence. Spring MVC page controllers and session-authenticated routes are web interfaces, **not automatically an external REST API**.

**Uncertainty**

- Whether any public JSON/REST endpoints or consumer-facing HTTP contracts exist at the pinned SHA beyond the examined MVC controllers.
- Whether the project's audience needs a documented programmatic API, a bounded internal HTTP contract, or simply web navigation and developer guidance.
- Whether an `OpenAPI`/`Swagger` specification or other equivalent API document exists outside the filename/path checks already performed.
- Whether `DOC-API` is in scope for this server-rendered application today, rather than only for a prospective REST API feature.

**Detected Facts**

- The pinned README describes a Spring MVC/Thymeleaf application with server-rendered pages, authenticated web routes, and session-based interaction.
- The README mentions an `API REST` under `Próximas líneas de evolución` as a **possible future extension**, not an implemented feature at the pinned SHA.
- Source inspection located Spring MVC controllers, but the presence of HTTP endpoints does not establish a documented public API for integration clients.
- The previous file/path review did not identify filenames containing `openapi` or `swagger`; this is a **bounded name-based observation**, not exhaustive proof of API absence.
- `DOC-API` is `Optional` in the Template; that classification does not itself settle Applicability.

**Evidence**

- [Pinned README — architecture and potential REST API](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned Spring MVC controller directory](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller)
- [TPL-BACKEND metadata](../../templates/repositories/backend/metadata.yml)
- [Optional technical E3 semantic review](only-film-optional-final-semantic-review.md)

**Evaluation Rationale**

An API documentation Responsibility should be evaluated against an actual interface and its consumers, not a generic expectation that every backend publishes REST endpoints. The README treats REST as future work, and the currently reviewed routes relate to server-rendered MVC. `Missing` would need a confirmed applicable API-documentation requirement that is unmet; `Partial` would need demonstrable partial coverage of that requirement. Neither is established by the available bounded review. The State is intentionally unselected and Applicability `Uncertain` pending a decision on scope and further endpoint evidence.

**Evidence-Based Applicability Recommendation**

**Provisional recommendation: `Not Applicable` for a standalone public/programmatic API contract at the pinned commit — subject to maintainer review. This recommendation does not overwrite the working `Applicability: Uncertain` or select a contractual State.**

At `28d75a50e0a178954dd46acc23300d9dd327843c`, direct inspection of seven controller files — `MovieController.java`, `RoomController.java`, `SessionController.java`, `TicketController.java`, `UserController.java`, `AuthController.java`, and `ReviewController.java` — found Spring `@Controller` classes with view/redirect-returning handlers. **None of those seven files declares `@RestController`, `@ResponseBody`, or `ResponseEntity`.** The pinned README separately and explicitly describes `API REST` as a *possible future extension*, not an implemented feature.

These positive observations are stronger than filename or mutable-branch code searches, but **the complete pinned Java tree and other possible routing/integration mechanisms have not been inventoried**. Do not turn a seven-file sample into a proof that no programmatic endpoint exists.

**Conditional reviewer outcomes:**

- **If no currently supported programmatic interface is identified and the intended consumers only use MVC pages:** prefer `Applicability: Not Applicable` for *public API-contract documentation*, with rationale describing the bounded verification and the user-facing scope. The reviewer must still select a valid `State` under the Assessment Template and justify its interpretation; `Not Applicable` is **not** a substitute State.
- **If an actual integration/JSON contract is identified:** prefer `Applicability: Applicable`, then assess the real source-backed documentation as `Satisfied`, `Partial`, or `Missing`.
- **If a meaningful scope question remains after review:** `Applicability: Uncertain` is allowed if its uncertainty and next evidence gate are recorded. The State nevertheless cannot remain unselected in a completed Assessment.

**Remaining evidence and sign-off:** inventory any additional pinned entry points; clarify whether the project promises a programmatic integration surface; record the maintainer's accepted scope, reviewer identity, date, contractual State, and rationale. **No approval or adoption action is recorded in this proposal.**

**Reviewer Discrimination Gate — State and Applicability**

**Open; no State or Applicability approval recorded.** A server-rendered Spring MVC controller is not automatically a public REST API, and the pinned README lists an API REST as **possible future work**.

- **Determine the contract and audience:** inspect the pinned controllers for consumer-facing JSON, programmatic HTTP contracts, or integrations. Decide whether documentation of any actual interface is materially needed for the intended consumer; do not classify a prospective feature as already implemented.
- **If an applicable interface exists:** identify concrete endpoints and existing contractual documentation before judging `Satisfied`, `Partial` or `Missing`. A lack of OpenAPI/Swagger filenames alone does not demonstrate absence.
- **If no API documentation purpose applies today:** explain `Not Applicable` based on the project's present supported interfaces and users. Optionality by itself does not settle the issue.

**Disposition record:** Supported interface contract: *unverified beyond bounded MVC inspection*; consumer need: *pending*; proposed contractual State: *unselected*; Applicability: `Uncertain`; reviewer/date: *not recorded*. No API specification, new endpoint, or adoption action is authorized.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Review the actual supported interfaces and intended consumers. If API documentation is not needed for this application's present scope, the reviewer can justify `Not Applicable` and then complete State under the Template's rules; otherwise identify concrete applicable contracts and select State on evidence. No speculative REST API documentation or consumer changes follow from this record.

---

---

### DOC-DATABASE

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed; human review pending**

**Implementation Characteristics**

`Own`, `Specialized`, `Distributed` — PostgreSQL setup instructions, a focused Flyway V2 integrity document, versioned SQL migration sources, and the README's domain overview.

**Uncertainty**

- Whether a new contributor can understand the essential entity relationships, data lifecycle, constraints, and supported profile differences without reconstructing them from JPA classes and SQL.
- Whether the migration documentation accurately describes the current V1/V2 relationship and constraints at the pinned consumer SHA.
- Whether a conceptual data-model summary is needed or the existing focused guides sufficiently serve this portfolio application's audience; an ER diagram is not automatically mandatory.

**Detected Facts**

- The pinned `docs/POSTGRESQL_SETUP.md` distinguishes quick H2 development, `dev`, `postgres`, and `postgres,demo` profiles, database environment variables, Flyway migrations, and Hibernate `ddl-auto=validate`.
- The pinned `docs/FLYWAY_V2_SEAT_UNIQUENESS.md` describes `UNIQUE(session_id, fila, seat)`, the decision to preserve V1, preflight collision checking, `NULL` considerations, and non-destructive handling of existing duplicates.
- The README identifies domain entities such as `Movie`, `Room`, `Session`, `Ticket`, `Review`, and `User`, and distinguishes H2 from PostgreSQL persistence.
- At the pinned SHA, [GitHub Actions run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) reports successful `postgres-schema` and `PostgreSQL JPA and concurrent checkout` jobs. These confirm bounded CI checks, **not** completeness of database documentation or every schema invariant.

**Evidence**

- [Pinned PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [Pinned Flyway V2 seat uniqueness document](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md)
- [Pinned README — domain entities and persistence](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned PostgreSQL CI run](https://github.com/fran-eliot/only_film/actions/runs/39283862407)
- [Optional technical E3 semantic review](only-film-optional-final-semantic-review.md)

**Evaluation Rationale**

Database-specific operational and schema-integrity documentation exists, so `Missing` would not reflect the available evidence. These sources explain profiles, migration procedures, and at least one important uniqueness constraint, but the prior review has not demonstrated a sufficiently accessible conceptual model of all material relationships and invariants. `Partial` is a **conservative, unapproved documentary-sufficiency proposal**; it does not mean migrations or schema are defective. The reviewer may accept `Satisfied` if focused documentation sufficiently meets the intended user's needs without extra diagrams.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The reviewer should establish the data-model documentation threshold and choose `PRESERVE` or a bounded `ADAPT` only if a material navigation or explanation gap is confirmed. No migration changes or data-model refactoring are authorized.

---

---

### DOC-DEPLOYMENT

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Applicable` — **proposed for the documented local Compose development environment only; no production deployment is asserted**

**Implementation Characteristics**

`Own`, `Specialized`, `Distributed` — local startup and operation instructions in the README and PostgreSQL guide, plus the pinned Dockerfile and Compose configuration.

**Uncertainty**

- Whether the README and PostgreSQL guide consistently describe the intended persistence of uploaded files. The guide contains a warning suggesting the absence of a definitive upload-persistence strategy even though it also describes a named `uploads_data` volume; local volume persistence is not equivalent to production backup/durability.
- Whether the documented Docker Compose route has been successfully reproduced at the pinned SHA; the earlier checks did **not** establish an associated successful Compose smoke run.
- Whether the consumer supports only local development or a separate deployed demo, and what startup, verification, backup, recovery, and operational guidance is appropriate for that actual supported scope.
- No evidence of production readiness, public exposure, disaster recovery, or production rollback is claimed.

**Detected Facts**

- The pinned README and `docs/POSTGRESQL_SETUP.md` describe preparing private `.env` settings, running `docker compose up --build -d`, connecting to PostgreSQL, accessing the local web application, and avoiding inadvertent data loss with `docker compose down -v`.
- The pinned `compose.yaml` defines `app` and `postgres`, PostgreSQL health checks, `postgres_data` and `uploads_data` volumes, and application/DB ports bound to `127.0.0.1`.
- The README explicitly warns that its Compose setup is not production deployment configuration for exposure to the Internet.
- The pinned `compose-smoke.yml` **defines** build/start, web, migrations, and persistence checks. A successful execution of that workflow **for the same pinned SHA was not identified** in the earlier reviewed check set.
- The PostgreSQL guide contains potentially inconsistent descriptions of uploads persistence; the difference may be between local operational persistence and the lack of a complete production file-storage strategy, and requires review instead of assuming a confirmed runtime bug.

**Evidence**

- [Pinned README — local Compose startup and limitations](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [Pinned compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml)
- [Pinned Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile)
- [Pinned Compose smoke workflow definition](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml)
- [Compose smoke execution evidence gap](only-film-compose-evidence-gap.md)
- [Optional technical E3 semantic review](only-film-optional-final-semantic-review.md)

**Evaluation Rationale**

The consumer has a documented operational route for a **local** Compose deployment and provides explicit safeguards and limitations, so the Responsibility is not absent. The semantic assessment must match the environment the project actually supports rather than imposing production requirements it does not claim to meet. The unverified Compose execution and potentially inconsistent uploads warning leave real documentation questions. `Partial` is a **proposed documentary assessment**, not proof that the Compose stack fails or that production deployment is expected. The reviewer should decide whether `Satisfied` is appropriate for local-only guidance or whether specific clarification is needed.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Review local operational scope, the uploads warning, and the threshold for reproduction evidence before choosing `PRESERVE` or `ADAPT`. No workflow trigger, deployed service, production plan, or change to Only Film is authorized.

---

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

**P1 Reviewer Disposition**

**Pending — the proposed `Partial` State is not approved.** The reviewer should evaluate the **accuracy, currency and discoverability of security documentation**, not certify the application's security posture.

- **Current versus historical baseline:** `docs/SECURITY_HARDENING_AUDIT.md` is dated 2026-10-10 and refers to an older commit. The risk descriptions cannot be restated as unresolved defects at the pinned `28d75a50e0a178954dd46acc23300d9dd327843c` without contemporary supporting evidence. The current README, demo-credentials guide and source/test reconciliation are distinct sources.
- **Bounded implementation/test evidence:** the inspected security-relevant tests include authorization, CSRF, image validation and environment hardening; the pinned CI run records 329 passing selected H2 tests, including 40 tests from five named security-relevant classes. This **does not** demonstrate that all endpoints, upload threats, dependencies, or deployment configurations are safe. Sonar `ANALYSIS SUCCESSFUL` does not establish a passed Quality Gate.
- **Documentation acceptance threshold:** decide whether the README and specialist documents appropriately inform users about credentials/secrets, supported local-only deployment, exposure constraints, relevant security practices and how to report issues. Evaluate whether a separate disclosure policy or index is **needed for the audience**, rather than automatically requiring `SECURITY.md` or a pentest.
- **State discrimination:** the existing material supports a non-`Missing` assessment. Approve `Satisfied` if it meets the agreed documentary purpose, or `Partial` only with specific, current documentation gaps. Do not interpret either State as a security assurance.

**Acceptance record:** Reviewer: *unassigned*; consumer SHA: `28d75a50e0a178954dd46acc23300d9dd327843c`; historical/current evidence separation: *pending review*; documentary threshold and threat-model scope: *pending*; approved State/date: *not recorded*; Adoption Decision: `—`.
**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The reviewer must determine whether `PRESERVE` or `ADAPT` the existing documentation is appropriate, and whether any additional documentation is justified by the consumer's audience and deployment assumptions. No security certification, change to Only Film, or downstream adoption action follows from this proposed record.

---

---

### DOC-DIAGRAMS

**Requirement Level**

`Optional`

**State**

**Not selected** — `Missing` or `Partial` remain hypotheses requiring evidence and reviewer judgment. This is an **incomplete contractual State**, not an approved finding.

**Applicability**

`Uncertain` — whether diagrams provide necessary or worthwhile technical explanation for this consumer is not yet established.

**Implementation Characteristics**

No maintained technical diagram artifact was confirmed in the bounded prior inspection. The README provides a **textual** architecture flow; interface screenshots and decorative SVG assets do not automatically constitute architecture, data-model, or deployment diagrams.

**Uncertainty**

- Whether diagrams are embedded in the pinned Markdown documents but were missed by the earlier filename/path inspection.
- Whether important entity relationships, checkout flows, or local deployment topology would be materially clearer with a version-controlled diagram.
- Whether the existing textual explanation is sufficient for the project's scope, so that diagrams would merely duplicate information.
- The earlier Framework catalog check did not locate a standalone `DOC-DIAGRAMS` Component. The [DOC-ARCHITECTURE Component](../../components/documentation/architecture/README.md) states that diagrams are optional to architectural explanation; no nonexistent Component contract is imposed here.

**Detected Facts**

- The pinned README gives the textual flow `MVC controller → service / business rules → JPA repository → database`, not an explicit architecture or data diagram.
- The pinned repository contains interface screenshots in `docs/screenshots/` and an avatar SVG asset; neither filename confirms technical diagram documentation.
- Prior path inspection did not identify `.drawio`, `.puml`, named Mermaid artifacts, or obviously diagram-specific filenames; **embedded diagrams in Markdown were not exhaustively checked**.
- The Template lists `DOC-DIAGRAMS` as `Optional`, and the documentation architecture Component cautions that diagrams should have a specific purpose, represent current architecture and remain maintainable.

**Evidence**

- [Pinned README — textual architecture description](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned consumer tree](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c)
- [DOC-ARCHITECTURE Component](../../components/documentation/architecture/README.md)
- [Optional showcase E3 semantic review](only-film-optional-showcase-semantic-review.md)

**Evaluation Rationale**

The available evidence does not establish a maintained technical diagram, but neither does it show that diagrams are needed for the consumer's actual purpose. Absence of a diagram-named file is not proof that all diagrams are missing, and a high-level textual flow can be sufficient for a relatively simple explanation. `Missing` versus `Partial` cannot be selected without clarifying the required documentary scope and searching for embedded artifacts; `Not Applicable` must also be evaluated on the merits, not inferred from Optional level. This record deliberately leaves State unselected and Applicability `Uncertain`.

**Reviewer Discrimination Gate — State and Applicability**

**Open; no State or Applicability approval recorded.** The pinned README describes an MVC → service → JPA → database flow **in text**. The previous filename inspection did not establish a maintained technical diagram, but did not exhaustively search Markdown for embedded Mermaid or image references.

- **Verify actual evidence:** inspect relevant pinned Markdown and assets for existing architecture, entity or deployment diagrams. Screenshots and decorative SVG files do not automatically fulfill this Responsibility.
- **Determine usefulness:** identify one or more real comprehension problems that a maintained diagram would solve. The Framework's architecture guidance treats diagrams as optional, and a clear textual flow may already be appropriate.
- **If applicable:** select the final State based on any substantive existing visualization (`Satisfied`/`Partial`) or verified absence (`Missing`), not a filename convention. If not useful to the consumer, justify `Not Applicable` rather than creating diagrams for formal compliance.

**Disposition record:** Embedded-diagram search: *not completed*; user need: *pending*; proposed contractual State: *unselected*; Applicability: `Uncertain`; reviewer/date: *not recorded*. No diagram generation is authorized.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

Confirm whether diagrams already exist, decide whether any are useful, then select the contractual State and Applicability with human review. No diagram generation or change to Only Film is authorized.

---

---

### DOC-REFERENCES

**Requirement Level**

`Optional`

**State**

`Partial` — **proposed; human review pending**

**Applicability**

`Uncertain` — whether a consolidated references Responsibility is useful for this consumer remains unresolved; this is **not** a decision of `Not Applicable`.

**Implementation Characteristics**

`Own`, `Distributed` — references to the academic source repository, internal guides, and development tools appear in context rather than as a separately maintained references catalog.

**Uncertainty**

- Whether stable external technical standards or authoritative sources are needed for readers beyond the existing contextual links.
- Whether meaningful links are out of date, repeated, or difficult to discover. A comprehensive reference URL audit has not been performed.
- Whether a central References document would improve the user journey or create redundant maintenance; the Framework Component explicitly permits contextual linking.
- If the reviewer determines the Responsibility is `Not Applicable`, the proposed `State` must be reconciled with the Template's contractual rules before declaring this entry complete.

**Detected Facts**

- The pinned README links to the original academic repository, selected technical documentation, and GitHub Actions workflows.
- Specialized guides mention PostgreSQL, Flyway, Maven, SonarCloud, and Dependabot; their mention does **not** establish that authoritative external reference URLs for each are provided or required.
- The Framework [DOC-REFERENCES Component](../../components/documentation/references/README.md) recommends primary sources with clear purpose and context and explicitly allows no standalone references catalog where contextual links are easier to use.
- The earlier filename/path review did not identify a separate `REFERENCES` document. Absence of that filename alone is not a finding of deficient referencing.

**Evidence**

- [Pinned Only Film README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)
- [Pinned dependency maintenance guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md)
- [DOC-REFERENCES Component](../../components/documentation/references/README.md)
- [Optional technical E3 semantic review](only-film-optional-final-semantic-review.md)

**Evaluation Rationale**

Contextual links already exist, and a standalone index is not required by the References Component. Whether the existing collection adequately addresses the intended reader's need for external source traceability has not been assessed exhaustively. `Partial` is a **proposed documentary State conditional on an applicable references scope**; Applicability remains `Uncertain` and may prove `Not Applicable` following human review. It is not a claim that a new References file is mandatory or that existing links are broken.

**Reviewer Discrimination Gate — Applicability**

**Open; proposed `Partial` State remains unapproved and Applicability remains `Uncertain`.** Existing contextual references are acknowledged, and the Framework Component does **not** require a standalone reference index where in-place links are clearer.

- **Inspect purpose and quality:** review whether the pinned README and specialist guides link the few authoritative sources actually needed by readers, whether important links are stale, and whether duplication or discoverability is a material problem.
- **If a separate references responsibility is applicable:** justify whether contextual linking is already `Satisfied` or `Partial` for the intended audience, without requiring a new index by default.
- **If centralization adds no value:** evaluate `Not Applicable` for a standalone reference catalog or clarify the scope of `DOC-REFERENCES`; reconcile the conditional proposed State with the final Applicability under the Template contract.

**Disposition record:** Reference inventory and need: *pending*; proposed State: `Partial` (not approved); Applicability: `Uncertain`; reviewer/date: *not recorded*. No reference index is authorized.

**Decision Status**

`Needs Further Evaluation`

**Adoption Decision**

`—`

**Decision Rationale**

The reviewer should determine whether references need consolidation or can remain contextual, then confirm Applicability and State under the Template's allowed values. No addition of a References index, external citations, or consumer changes is authorized.

---

## 4. Assessment Conclusion

### Assessment Status

`In Progress`

### Major Findings

- All 28 Template Responsibilities have preliminary E3 review proposals, and all twenty-eight have structured entries in this Assessment working record (including three with State deliberately unselected): `README-HERO`, `README-OVERVIEW`, `README-FEATURES`, `README-TECH-STACK`, `README-QUICK-START`, `README-DOCUMENTATION`, `README-FOOTER`, `DOC-CHANGELOG`, `README-STATUS`, `README-ARCHITECTURE`, `README-REPOSITORY-STRUCTURE`, `README-TESTING`, `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS`, `DOC-TESTING`, `README-ROADMAP`, `README-CONTRIBUTING`, `DOC-API`, `DOC-DATABASE`, `DOC-DEPLOYMENT`, `DOC-ADR`, `DOC-REFERENCES`, `README-DEMO`, `README-AUTHOR`, `README-HIGHLIGHTS`, `DOC-DIAGRAMS`, `README-LICENSE`, and `DOC-SECURITY`.
- `DOC-CHANGELOG` has a recommended `Missing` State supported by reviewed documentation and maintainer confirmation of no tags or Releases.
- `README-QUICK-START` has a proposed `Partial` State, grounded in documentation and CI evidence but bounded by the missing pinned-Compose execution evidence. **No formal human approval is claimed for either State.**

### Open Uncertainties

- Human sign-off on all twenty-eight structured entries, including contractual State selection for the three unresolved entries, including `DOC-CHANGELOG` alternatives and the Testing documentation sufficiency threshold.
- Contractual State selection for `README-CONTRIBUTING`, `DOC-API`, and `DOC-DIAGRAMS`, Applicability review for these three plus `DOC-REFERENCES`, and human review of Quick Start Compose verification, security-documentation adequacy, license-status communication, architecture freshness, and actual project milestone.
- The historical JaCoCo coverage percentage and Sonar Quality Gate outcome are not established; whether either is necessary for documentary acceptance remains a reviewer question.
- Rights and permissions associated with the original academic contributions remain unverified; the Assessment does not grant a license.
- Adoption Decisions and rationales where warranted.

### Recommended Next Review

Review the full 28-Responsibility working Assessment against Template metadata, first resolving the three unselected States and four open Applicability judgments. Then validate proposed States, rationale, and P1 evidence gates with human sign-off before selecting Adoption Decisions or authorizing consumer changes.

---

## Completion Check

- **Assessment `Complete`: NO.**
- **Responsibility coverage in this working artifact:** `28/28` structured entries (`25` with proposed State, one of those with Applicability `Uncertain`; `3` with State unselected), `0/28` not entered.
- **Formally approved States in this record:** `0`.
- **Resolved Adoption Decisions:** `0`.
- **Consumer mutations:** `NONE`.

This Markdown record follows the Assessment Template's field structure for all twenty-eight Responsibilities; the three entries with unselected State remain incomplete. Its summary intentionally remains **partial** rather than filling missing entries with unsupported `State` values. It does not establish compliance or authorize Application/Integration.
