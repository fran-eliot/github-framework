# Only Film — Adoption Decision review batch 7: Optional technical documentation

## Scope and review boundaries

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable consumer source | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `DOC-ADR`, `DOC-DATABASE`, `DOC-DEPLOYMENT`, `DOC-SECURITY` |
| Approved State / Applicability | `28/28`, unchanged |
| Formally resolved Adoption Decisions | `12/28`: eleven `PRESERVE`, one `OMIT` (including `DOC-ADR`, approved 2026-11-14) |
| Unresolved Adoption Decisions | `16/28`, including `DOC-DATABASE`, `DOC-DEPLOYMENT` and `DOC-SECURITY` in this batch |
| Assessment status | `In Progress` |
| Consumer modifications | `NONE` |

This **preparation packet** does not grant a formal Adoption Decision. `State` and `Applicability` have already been formally approved for all 28 Responsibilities; a new `Resolved` status requires an independent, express maintainer choice and evidence-specific rationale. Documentation sufficiency is not the same as full runtime validation. No tests, workflows, migrations, settings, files or deployments may be changed in Only Film.

## Formal maintainer Adoption Decision outcome — 2026-11-14

The Only Film maintainer **expressly approved `DOC-ADR = PRESERVE`**, limited to the documented decisions in the Flyway V2 and Dependabot guides, and expressly retained the other three as unresolved:

| Responsibility | Decision Status | Adoption Decision | Rationale / preserved evidence limits |
| --- | --- | --- | --- |
| `DOC-ADR` | `Resolved` | `PRESERVE` | Preserve useful distributed technical decision explanations, **not** a comprehensive ADR catalog or endorsement of earlier architecture audit proposals |
| `DOC-DATABASE` | `Needs Further Evaluation` | `—` | Database profile and migration guidance does not verify complete entity relationships, all invariants or a full current data-model inventory |
| `DOC-DEPLOYMENT` | `Needs Further Evaluation` | `—` | Applicability remains **local, nonproduction Docker Compose only**; no independently confirmed passing Compose run for the pinned SHA or production-level backup/durability assurance |
| `DOC-SECURITY` | `Needs Further Evaluation` | `—` | Earlier audits are historical, not established current vulnerabilities; bounded security tests and scanner submission do not prove a comprehensive audit or passed historical Quality Gate |

**Human decision date:** 2026-11-14. **Immutable assessed consumer SHA:** `28d75a50e0a178954dd46acc23300d9dd327843c` (distinct from the maintainer decision date). All 28 previously approved State / Applicability pairs remain unchanged, including `DOC-ADR = Partial / Applicable` and `DOC-DEPLOYMENT = Partial / Applicable` strictly in the local Compose scope.

**Authorization boundary:** Assessment `In Progress`; **12/28 formally resolved (11 `PRESERVE`, 1 `OMIT`), 16 unresolved**. No change to Only Film, migration, database model, deployment, CI, settings, security controls, test execution, new ADR process, Application or Integration is authorized.

The reviewer-facing proposals below are retained as **historical preparation material**, not current formal decision status.

## Reviewer-facing decision candidates

| Responsibility | Approved State / Applicability | Recommended posture | Remaining decision gate |
| --- | --- | --- | --- |
| `DOC-ADR` | `Partial / Applicable` | **Consider `PRESERVE`, limited to distributed technical decision records** | Decide whether current focused explanations are useful without a formal ADR register; historical audit recommendations must not be relabeled adopted architectural decisions |
| `DOC-DATABASE` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Determine whether existing profile/migration guides provide adequate conceptual data relationships and constraints for the intended reader |
| `DOC-DEPLOYMENT` | `Partial / Applicable`, **local Compose only** | **Keep `Needs Further Evaluation / —` by default** | Clarify local uploads-volume semantics vs production backup/durability and whether pinned Compose execution evidence is needed |
| `DOC-SECURITY` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Determine appropriate security documentation, vulnerability contact/secret-handling expectations, and avoid presenting historical audit findings or CI checks as current assurance |

The lack of a separately located Framework Component specification for some Optional IDs does not create a consumer defect or justify mandatory extra documents. An approved `Partial` documentary classification can coexist with a narrow `PRESERVE` decision; conversely `Applicable` does not authorize deployment or security changes.

## 1. DOC-ADR — existing focused records, not an adopted ADR registry

### Source-backed evidence

- The directly re-fetched [Flyway V2 seat uniqueness guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) explains the `UNIQUE(session_id, fila, seat)` invariant, why the existing V1 migration must remain untouched, how to inspect data conflicts and `NULL` records, and why collisions must not be destructively removed automatically.
- The directly re-fetched [Dependency Maintenance guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md) records weekly Dependabot grouping, separate major-version PRs, human checks and no automatic merging; the guidance explicitly separates these updates from handling vulnerability alerts.
- The [historical architecture/maintainability audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) was written against an earlier commit (`b6cf52c9`), and its proposed improvements must not be represented as present-day accepted ADRs or unresolved current defects.
- The [Optional Technical semantic review](only-film-optional-final-semantic-review.md) documents the bounded absence of a discovered formal ADR directory/catalog, not the absence of architecture decisions in all forms.

### Decision alternatives

**Consider `Resolved / PRESERVE`** for the **existing task-specific decision explanations** as a useful, distributed record of selected migration and maintenance choices. The `Partial / Applicable` classification stays unchanged: a maintained project-wide inventory of architectural alternatives, decision dates, status and consequences has **not** been established. Preservation should not imply that historical architecture audit recommendations were accepted.

`ADAPT` requires a clear, current problem of discoverability, provenance or missing consequence documentation, plus an evidence-backed, maintainable scope. `ADD` (new ADR register) cannot be presumed necessary solely because no `adr/` directory was found. `Needs Further Evaluation / —` remains valid if current decision history is a required acceptance threshold.

**No source-code, migration, CI or repository process change is authorized.**

## 2. DOC-DATABASE — conceptual model versus specialized setup guidance

### Source-backed evidence

- The directly re-fetched [PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) distinguishes temporary H2, local `dev`, persistent `postgres` and local demo profiles, Docker Compose variables and Flyway with Hibernate `validate`.
- The [Flyway V2 document](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) explains a **specific** ticket-seat uniqueness constraint, its `NULL` limitation and collision handling, not the entirety of the domain model.
- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) lists the principal `Movie`, `Room`, `Session`, `Ticket`, `Review` and `User` entities. This orientation does not independently inventory all entity relationships, lifecycle rules, JPA mappings, indexes or invariants.
- The prior [pinned PostgreSQL check evidence](https://github.com/fran-eliot/only_film/actions/runs/39283862407) supports selected schema/integration CI paths, not comprehensive database-documentation verification.

### Decision alternatives

**Default `Needs Further Evaluation / —`.** `PRESERVE` might be appropriate if the intended audience needs primarily **operational PostgreSQL/Flyway instructions**, and a full conceptual schema summary would duplicate readily accessible current source. `ADAPT` requires identifying an actual material model explanation or contributor-navigation gap, grounded in the pinned schema/JPA code. Do not demand an ER diagram simply for formality.

**Not established:** a complete current JPA/data relationship map, every SQL constraint, production data operation guarantees or exhaustive schema consistency. No migration or database edit is authorized.

## 3. DOC-DEPLOYMENT — strictly local Docker Compose, not production hosting

### Source-backed evidence

- The directly re-fetched [pinned `compose.yaml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) defines `app` and `postgres`, the `postgres_data` and `uploads_data` named volumes, PostgreSQL health check, and both mapped ports bound to **`127.0.0.1`**. It defines **local operational configuration**, not internet-facing production hosting.
- The [pinned PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) explains `.env`, Docker Compose, local ports, profiles, and the impact of `docker compose down -v`. Its upload persistence warning must be read alongside the named **local** `uploads_data` volume and distinguished from incomplete **production backup/recovery** arrangements.
- The directly re-fetched [Compose smoke workflow definition](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) specifies build/start, HTTP 200, migration state, restart and database/upload persistence probes. A workflow **definition is not a successful pinned-SHA execution**; the [Compose evidence gap](only-film-compose-evidence-gap.md) did not establish a passing run for that exact SHA.
- The README explicitly cautions against using this local-only Compose configuration as hardened production deployment.

### Decision alternatives

**Default `Needs Further Evaluation / —`.** A possible `PRESERVE` would be limited to clearly documented **local, nonproduction** usage; it must not be described as production deployment or independent proof that the complete Compose startup works at the pinned reference. Consider `ADAPT` only if a concrete contradiction between local volume persistence and the guide's text is substantiated and its user impact is understood.

**Not established:** clean pinned Compose smoke success, public deployment, secrets strategy, remote volumes, external backups, rollback, disaster recovery or production safety. No deployment or workflow execution is authorized.

## 4. DOC-SECURITY — useful guidance, with dated audit and bounded CI

### Source-backed evidence

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) states role restrictions, BCrypt, CSRF, image validation, demo checkout without real payment, and production-exposure limitations.
- The directly re-fetched [2026-10-10 Security Hardening Audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md) identifies source baseline `0a7e03a0` after PR #12 and expressly says the static audit is **not a penetration test**. Findings about controllers, CSRF and configuration at that baseline **must not be asserted as active vulnerabilities** at the later pinned SHA.
- The [Demo Credentials Security guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md) describes randomly generated credentials by default, explicitly configured local demo credentials, warnings for publicly accessible environments and limitations of merely removing historic secrets from code.
- The [existing security reconciliation](only-film-security-testing-reconciliation.md), [negative security tests](only-film-negative-security-test-evidence.md) and [Surefire/Sonar logs](only-film-verified-surefire-sonar-logs.md) record bounded implementation observations and 329 selected passing H2 tests, including 40 security-related cases. These do **not** prove all endpoints secure, vulnerability freedom, a full security review, penetration test, production hardening or a passed historical server-side Sonar Quality Gate.

### Decision alternatives

**Default `Needs Further Evaluation / —`.** `PRESERVE` could retain existing README/credential/security guide coverage as **partial documentary guidance**, if this is demonstrably enough for the consumer's personal, local-project audience. `ADAPT` should require a specific factual conflict, security contact/disclosure requirement, or current secret/configuration instruction gap supported by the pinned source and explicit maintainer policy.

**No license, safe-deployment, secure-by-default, Quality Gate, threat-model or penetration-testing certification follows from this review.** No consumer security change or new audit execution is authorized.

## Formal maintainer review gate

An independent, express maintainer decision is required for each Responsibility. The initial recommended review posture is:

1. `DOC-ADR = PRESERVE` **conditionally**, limited to the two identified distributed technical decision guides.
2. `DOC-DATABASE = Needs Further Evaluation / —`, pending an agreed useful conceptual schema threshold.
3. `DOC-DEPLOYMENT = Needs Further Evaluation / —`, pending clarification of local upload persistence and required execution evidence.
4. `DOC-SECURITY = Needs Further Evaluation / —`, pending an audience-appropriate security documentation sufficiency check.

If expressly approved, a later **separate approval PR** should update the canonical [Assessment](only-film-assessment.md), the [consolidated review matrix](only-film-consolidated-review-matrix.md), and this packet with approval date, individual rationale and unchanged source limitations. Merging this preparation packet does **not** count as approval.

**Postapproval status:** All 28 State / Applicability approvals unchanged; 12 decisions resolved (11 `PRESERVE`, 1 `OMIT`), 16 unresolved. Assessment remains `In Progress`; Only Film remains strictly read-only. The earlier preparation suggestions above are not themselves an approval.
