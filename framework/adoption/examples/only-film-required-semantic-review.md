# Only Film — Provisional Semantic Review of Required Quick Start and Changelog

## 1. Context

This document prepares E3 semantic proposals for two **Required** Responsibilities of `TPL-BACKEND` 0.1.0, using E2 evidence traceable to the pinned Only Film commit. **It is not a human approval or an Adoption Decision.**

| Field | Value |
| --- | --- |
| Consumer Repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Consumer Reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Scope | `README-QUICK-START` and `DOC-CHANGELOG` |
| Review Status | `Proposal — pending human review` |
| Reviewer / Approval | Not assigned / not approved |
| Assessment Status | `In Progress` |
| Consumer Mutation | `NONE` |

The `Required` level comes from the Template. It does **not** automatically entail `State: Missing` when a canonical file is absent; conversely, file presence does not prove `Satisfied`.

## 2. Proposal summary

| Responsibility | Requirement Level | Proposed State | Proposed Applicability | Decision Status | Adoption Decision |
| --- | --- | --- | --- | --- | --- |
| `README-QUICK-START` | `Required` | `Partial` — provisional | `Applicable` — provisional | `Needs Further Evaluation` | `—` |
| `DOC-CHANGELOG` | `Required` | **`Missing` — preferred E3 hypothesis following targeted evidence review; tags and approval pending** | `Applicable` — provisional | `Needs Further Evaluation` | `—` |

For `DOC-CHANGELOG`, the revised evidence favors `Missing` over the previously undiscriminated `Missing / Partial` alternatives. **No State has been formally approved**; substantive alternative sources must still be checked, especially tags.

## 3. Responsibility — README-QUICK-START

**Requirement Level:** `Required`.

**Proposed State:** `Partial` (initial hypothesis, not confirmed).

**Proposed Applicability:** `Applicable` (provisional).

**Implementation Characteristics (proposed):** `Own`, `Distributed` — proprietary README instructions supported by PostgreSQL and Docker guides.

### Detected Facts

- [README.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) provides `git clone`, `cp .env.example .env`, a private password setup, `docker compose up --build -d`, `docker compose ps`, and the local `/movies` URL.
- [Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile) uses Maven/Temurin 25 for build and Temurin 25 JRE; [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) specifies Java 25 and Spring Boot parent 4.0.5.
- [compose.yaml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) defines `app` and PostgreSQL 17, a `postgres` Spring profile, database/uploads volumes, healthcheck dependency, and localhost-bound ports. [application-postgres.properties](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/resources/application-postgres.properties) uses `DB_URL`, `DB_USERNAME`, and `DB_PASSWORD`.
- [`.env.example`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.env.example) provides port, username, and password variables. The README requires replacing the sample password and limits Compose to local development.
- The `postgres-schema` job in [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) succeeded for the pinned SHA. According to [postgres-migration.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml), it starts the **JAR** against CI PostgreSQL and checks migrations and restart; it does **not** execute the documented Compose Quick Start.
- A [compose-smoke.yml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) workflow exists, with `docker compose config`, build, container startup, HTTP checks, and persistence tests. **No Compose check directly associated with the pinned SHA was found** among the reviewed checks.

### Evidence

- [Pinned Quick Start configuration and CI verification](only-film-pinned-quickstart-ci-verification.md)
- [Compose evidence gap and gates Q1–Q8](only-film-compose-evidence-gap.md)
- [Initial two-Responsibility walkthrough](only-film-two-responsibilities.md)
- [README and PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md)

### Evaluation Rationale — proposal

The examined sources provide an identifiable startup procedure with consistent versions, variables, profiles, and security limits. Starting a JAR in CI provides limited confidence in the code but **does not verify reproducibility of the documented Docker workflow**. The `Partial` proposal keeps open whether the instructions meet the intended audience's needs. There is no demonstrated execution failure.

### Uncertainty

- Does Quick Start work from a clean clone with synthetic credentials and a disposable environment, under gates Q1–Q8?
- Can users verify application readiness and access demo accounts/data if needed?
- Are JDK/Maven alternatives and port overrides sufficiently explained?
- What reproducibility threshold should a **documentation** Responsibility meet to qualify as `Satisfied`?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** before selecting `PRESERVE` or `ADAPT`, the reviewer must evaluate documentary sufficiency and the missing operational evidence. A different CI execution does not settle reproducibility.

## 4. Responsibility — DOC-CHANGELOG

**Requirement Level:** `Required`.

**Proposed State:** **`Missing` (proposed, not approved)**; no version-published changelog was identified in the examined sources. Tag inventory remains unverified, and `Partial` or `Satisfied` would require evidence of a substantive equivalent source.

**Proposed Applicability:** `Applicable` (provisional).

**Implementation Characteristics (proposed):** `Distributed` as a **possible** form of change traceability through commits and PRs. These are not proven equivalent to a version-oriented changelog.

### Detected Facts

- The pinned Git tree inspection did not identify paths **by name** containing Changelog, Changes, History, or Release. This was not a complete semantic content review.
- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describes the project's evolution and points to Git/PR history for attribution. Inspected sections do not present a version-by-version published change list.
- [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) declares `0.0.1-SNAPSHOT`, which does not prove a release.
- Git history reachable from the SHA includes features and PRs such as #489, #491, and #493. Granular commit history is **not automatically** release notes or a changelog.
- An earlier GitHub Releases endpoint query returned an empty list; this does not demonstrate that no release ever existed. The **tags check remains incomplete**; tag absence is **not established**.
- [F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) records findings and plans, not a confirmed publication history.
- A targeted review on 2026-11-12 found no `CHANGELOG.md` **at that exact path** in the pinned tree and could not obtain a usable tag inventory. See [updated changelog evidence review, section 6](only-film-changelog-evidence-review.md).

### Evidence

- [Changelog and release evidence review](only-film-changelog-evidence-review.md)
- [Pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md)
- [Pinned pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml)
- [Git history at the pinned SHA](https://github.com/fran-eliot/only_film/commits/28d75a50e0a178954dd46acc23300d9dd327843c/)
- [Mutable GitHub Releases page](https://github.com/fran-eliot/only_film/releases)

### Evaluation Rationale — proposal

No inspected source establishes a **version-oriented record of published changes** fulfilling `DOC-CHANGELOG`. Absence of a canonical filename alone is insufficient; alternative sources must be examined. A raw Git/PR listing cannot be assigned `Partial` merely as a precaution.

Following the targeted check, **`Missing` is the preferred hypothesis, not an approved State**. Tags and other substantive alternatives remain an explicit reviewer gate. If such a source is found, reconsider `Partial` or `Satisfied`.

### Uncertainty

- Are there tags, release notes, or other accessible official sources summarizing changes per version?
- Does the repository have a publication process, or only development builds?
- What information do its intended users need about relevant changes?
- Does this Required Responsibility warrant an `Unreleased` change log even without formal releases?
- After completing C1–C6, can `Missing` be justified, or is an equivalent `Partial`/`Satisfied` implementation present?

**Decision Status:** `Needs Further Evaluation`.

**Adoption Decision:** `—`.

**Decision Rationale (unresolved):** no Adoption Decision (`ADD`, `ADAPT`, `ACCEPT`, `PRESERVE`, or another valid option) is warranted yet. No changelog or fictitious historical versions have been created.

## 5. Human review gates

| Gate | Criterion | Status |
| --- | --- | --- |
| RQ-1 | Confirm the consumer context and purpose of both Required Responsibilities | Pending |
| RQ-2 | Reproduce Compose Quick Start or justify an equivalent documentation-evidence threshold | Pending |
| RQ-3 | Corroborate versions, variables, and safeguards at the pinned SHA | Static evidence prepared; reviewer pending |
| RQ-4 | Verify tags, releases, and alternative records according to C1–C6 | Pending |
| RQ-5 | Select a valid `State` for each Responsibility, with `Applicability` and rationale | Pending |
| RQ-6 | Keep `Needs Further Evaluation` where material uncertainty remains | Prepared; reviewer pending |
| RQ-7 | Resolve an Adoption Decision only with rationale and human authorization | Pending |

## 6. Conclusion

E3 proposals exist for both Required Responsibilities at the pinned Only Film SHA. `README-QUICK-START` retains a `Partial` hypothesis. `DOC-CHANGELOG` now has a preferred `Missing` hypothesis, **conditional on tag and equivalent-source verification**, before any formal `State` is recorded.

**No E3 semantic assessment has been approved**, no Adoption Decision has been resolved, and the overall Assessment remains `In Progress`. Docker has not been executed, and the consumer has not been modified.
