# Only Film — README presentation: human review batch 1

## Review contract

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned consumer SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-HERO`, `README-OVERVIEW`, `README-TECH-STACK` |
| Review status | **Recommendations for maintainer decision; none of these three approved here** |
| Consumer mutation | **NONE** |
| Assessment status | `In Progress` |

This batch compares the **actual pinned sources** against the relevant Framework Components; it does not infer missing requirements from non-canonical headings and does not authorize edits to Only Film. The main [Assessment](only-film-assessment.md) retains the currently recorded `Partial / Applicable` proposals for all three entries until the maintainer expressly accepts or revises them.

## Evaluation alternatives

| Responsibility | Current working State | Recommended for maintainer review | Applicability | Evidence interpretation |
| --- | --- | --- | --- | --- |
| `README-HERO` | `Partial` (unapproved) | **`Satisfied` candidate** | `Applicable` (proposal) | A single project H1, short functional introduction and five relevant badges provide identity without requiring a banner |
| `README-OVERVIEW` | `Partial` (unapproved) | **`Satisfied` candidate** | `Applicable` (proposal) | The opening paragraphs identify the application, its user-facing purpose, cinema tasks and original project context without requiring a separate Overview heading |
| `README-TECH-STACK` | `Partial` (unapproved) | **Retain `Partial` pending verification** | `Applicable` (proposal) | Categorized stack coverage is present and major versions are corroborated, but the full inventory was not audited |

`Satisfied` for Hero or Overview is an **alternative reviewer-facing judgment**, not a recorded change to their State. The absence of a decorative banner or of a literal `Overview` heading is not, by itself, a failure of a Responsibility.

## 1. README-HERO

**Source observations, pinned SHA:**

- [README.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) opens with `# 🎬 Only Film` and a concise description naming Java 25, Spring Boot, Spring MVC, Spring Security and Thymeleaf.
- The introduction explicitly identifies movie listings, screenings, seat selection, ticket purchases and role-based cinema administration.
- Five badge image links represent Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway and Docker Compose.
- [README-HERO Component](../../components/readme/hero/README.md) specifies a project name, tagline and major badges; a banner is **optional**. No mandatory graphic header or separate `Tagline` heading is established.

**Evaluation judgment:** the role of the Hero appears substantively covered. `Satisfied / Applicable` is reasonable **if the maintainer accepts the opening prose as an adequate tagline**. `Partial` should be retained only if a specific communication deficiency is demonstrated, not simply because the heading differs from an example.

**Remaining bounds:** no rendered mobile/dark-theme readability review; do not claim that all five badge images resolve or display correctly.

## 2. README-OVERVIEW

**Source observations, pinned SHA:**

- The same [README introduction](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) states that Only Film is a cinema-management web application and explains its main user tasks.
- The next paragraph distinguishes its original academic collaboration from the later technical evolution.
- The [README-OVERVIEW Component](../../components/readme/overview/README.md) asks for purpose, problem and clarity, with no requirement that an existing-repository adoption must create a duplicate `## Overview` section.

**Evaluation judgment:** `Satisfied / Applicable` is a reasonable semantic interpretation of the existing introduction if the reader can understand the project's purpose without a separate heading. The content can serve both Hero and Overview, provided it is readable and not misleading. A stricter editorial separation would support retaining `Partial`, but must be justified explicitly.

**Remaining bounds:** no documented user-reading/usability session; no copy or navigation change authorized.

## 3. README-TECH-STACK

**Source observations, pinned SHA:**

- The [README's `Tecnologías y arquitectura` table](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) groups backend, security, frontend, local persistence, PostgreSQL persistence, testing and infrastructure technologies.
- The [pinned POM](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) declares the Spring Boot parent version `4.0.5` and `java.version=25`.
- The [pinned Compose](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) defines `app` and `postgres` services, with `postgres:17-alpine`. This is **static configuration evidence**, not proof of successful startup or deployment.
- The [README-TECH-STACK Component](../../components/readme/tech-stack/README.md) recommends technology grouping; its list of categories is guidance, not a requirement to invent Cloud infrastructure.

**Evaluation judgment:** retain `Partial / Applicable` as a conservative **unapproved** assessment until less directly checked technologies/dependencies are corroborated or the reviewer accepts the README table's documentary threshold. It is **not** evidence that the table is broken, nor a requirement to add Cloud technology.

**Remaining bounds:** no exhaustive dependency classification, runtime verification or complete link/badge health check.

## Maintainer review gate

For each of the three Responsibilities, confirm or revise its **State and Applicability** independently:

1. `README-HERO`: accept `Satisfied / Applicable`, retain `Partial / Applicable`, or provide a grounded alternative.
2. `README-OVERVIEW`: accept `Satisfied / Applicable`, retain `Partial / Applicable`, or provide a grounded alternative.
3. `README-TECH-STACK`: retain `Partial / Applicable`, approve `Satisfied / Applicable` if the documentary threshold is deemed met, or provide a grounded alternative.

Record the maintainer's explicit selection and date **in a later Assessment PR**; merging this preparation batch is **not approval**. Continue `Decision Status: Needs Further Evaluation` and `Adoption Decision: —` until the separate adoption-disposition review.

## Evidence and authorization limits

The assessment still evaluates consumer SHA `28d75a50e0a178954dd46acc23300d9dd327843c`. Current repository state, CI outcomes or future changes are **not** silently substituted for the pinned baseline. Source inspection confirms the words and configuration shown, not user-experience quality, every runtime dependency or production readiness. This batch introduces **no consumer modifications**, no approved States, and no resolved Adoption Decisions.
