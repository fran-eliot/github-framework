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

## DOC-DEPLOYMENT — verified local upload-persistence wording discrepancy (2026-11-14)

A targeted static comparison at immutable Only Film commit `28d75a50e0a178954dd46acc23300d9dd327843c` establishes a **specific documentation inconsistency**, rather than an inferred Docker or data-loss failure:

| Pinned source | Direct observation | Boundary |
| --- | --- | --- |
| [`compose.yaml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) | `app` mounts `uploads_data:/app/uploads`, sets `ONLYFILM_UPLOAD_DIR=/app/uploads`; a separate `postgres_data` volume stores database files. The published application and database ports bind to `127.0.0.1`. | Static configuration of **local** persistence; no execution, backup, recovery or production durability is verified. |
| [`docs/POSTGRESQL_SETUP.md`, line 44](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md#L44) | Explicitly states `docker compose down` preserves both named volumes and uploaded images across container recreation; warns that `down -v` removes both. | Documentary claim, independently consistent with the Compose volume configuration, not a successful end-to-end persistence test. |
| [`docs/POSTGRESQL_SETUP.md`, line 50](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md#L50) | Warns that a definitive strategy for uploaded-file persistence in the container is still absent. | As written, ambiguous against the local named-volume configuration. It may intend to warn that **production-grade backup, durability and recovery** are not designed. |

**Evidence-backed candidate: `ADAPT`**, restricted to a **future, separately authorized documentation clarification** distinguishing local named-volume persistence from production storage, backup and recovery guarantees. This does not authorize changing the Compose configuration, Dockerfile, volume contents, workflows or consumer documents now. No pinned-SHA Compose success, failure, storage durability or production deployment is asserted.

The existing formal `DOC-DEPLOYMENT: Partial / Applicable` classification remains unchanged, with `Applicable` limited to **local nonproduction Compose**. **The Adoption Decision remains `Needs Further Evaluation / —` until express maintainer approval.** Assessment `In Progress`; overall formal totals at this review: **19/28 resolved** (13 `PRESERVE`, 3 `OMIT`, 3 `ADAPT`), **9 pending**; consumer mutations `NONE`.



## Formal DOC-DEPLOYMENT Adoption Decision — 2026-11-14

The Only Film maintainer expressly approved **`DOC-DEPLOYMENT = ADAPT`** for a **future, bounded documentation-only clarification** of local upload persistence through Docker Compose named volumes versus production durability, backups and recovery. The existing `Partial / Applicable` classification remains unchanged, and applicability is **strictly local, nonproduction Compose only**. The preceding static evidence review establishes a documentary ambiguity, **not** a runtime failure, data-loss bug, successful pinned-SHA Compose execution or production assurance.

This formal approval supersedes the earlier pending recommendation for `DOC-DEPLOYMENT` only; `DOC-DATABASE` and `DOC-SECURITY` remain unresolved. No Only Film configuration, volume, documentation, CI, test or application file is modified. No Application/Integration is authorized. Assessment `In Progress`, **21/28 resolved** (13 `PRESERVE`, 3 `OMIT`, 4 `ADAPT`, 1 `ADD`), **7 pending**; all 28 previously approved State/Applicability pairs unchanged.

## Pinned database-schema and JPA relationship reconciliation — 2026-11-14

This targeted **read-only source inspection** follows the approved `DOC-DATABASE: Partial / Applicable` classification at immutable Only Film SHA `28d75a50e0a178954dd46acc23300d9dd327843c`. Unlike the earlier review based mainly on the README and specialized guides, this check directly inspected **both Flyway migrations and all six classes in `src/main/java/com/demo/model/`**. It does not validate runtime migration results or exhaustively examine repositories, queries, lifecycle behavior or all domain invariants.

| Pinned source | Direct observations | Documentary implication |
| --- | --- | --- |
| [`V1__initial_schema.sql`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/resources/db/migration/V1__initial_schema.sql) | Defines six tables: `movies`, `salas`, `users`, `sessions`, `tickets`, `reviews`. Foreign keys: `sessions.movie_id → movies.id`, `sessions.room_id → salas.id`; `tickets.user_id → users.id`, `tickets.session_id → sessions.id`; `reviews.movie_id → movies.id`, `reviews.user_id → users.id`. V1 also creates six indexes on those foreign-key columns, and unique email and username constraints. | The current *declared relational topology* can be explained without inferring unseen entities or inventing constraints. Some FK columns are nullable in the migration; an FK is not proof that a relationship is mandatory in every record. |
| [`V2__unique_ticket_seats.sql`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/resources/db/migration/V2__unique_ticket_seats.sql) | Adds `uq_tickets_session_row_seat` as `UNIQUE (session_id, fila, seat)`. The accompanying SQL comments and [V2 guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) caution about historical duplicates and nullable coordinates. | A specific database uniqueness rule, not an all-purpose claim that every seat coordinate is populated, that all concurrent operations are correct, or that a migration was executed successfully here. |
| [`Movie`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/model/Movie.java), [`Room`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/model/Room.java), [`User`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/model/User.java) | Three primary entities map to `movies`, `salas` and `users`. `Room` uses the Spanish database table name `salas`. | Schema naming and application naming are not identical; readers benefit from explicitly relating them. |
| [`Session`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/model/Session.java), [`Ticket`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/model/Ticket.java), [`Review`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/model/Review.java) | Each declares two `@ManyToOne` references consistent with the V1 foreign keys: Session → Movie/Room, Ticket → User/Session, Review → Movie/User. | This is a bounded JPA-to-schema correspondence, **not** evidence that every persistence relationship, fetch path, validation or deletion behavior has been audited. |

### Assessment decision gate

The source-level review establishes a **specific documentation opportunity**: the PostgreSQL setup and Flyway V2 guides teach environment setup and one integrity decision, but do not by themselves present the six-table relationship topology above as a concise, reader-facing domain overview. A separately approved **`DOC-DATABASE = ADAPT`** could clarify major entities, relationship direction, `salas` naming, and the distinction between configured schema constraints and business-layer lifecycle rules. It should not duplicate SQL or mandate an ER diagram; `DOC-DIAGRAMS` remains an independent decision.

**Formal status remains `Needs Further Evaluation / —` for `DOC-DATABASE`** until the maintainer expressly selects an Adoption Decision. All 28 State/Applicability evaluations remain approved. Overall Assessment: **21/28 resolved** (13 `PRESERVE`, 3 `OMIT`, 4 `ADAPT`, 1 `ADD`), **7 pending**, `In Progress`. No changes, database operations, tests, migration execution, refactoring, or Application/Integration are authorized in Only Film.



## Formal DOC-DATABASE Adoption Decision — 2026-11-14

Following the pinned V1/V2 and six-entity JPA reconciliation above, the Only Film maintainer **formally approved `DOC-DATABASE = ADAPT`** for a **future, bounded, source-verified conceptual-model documentation improvement only**. The approved `Partial / Applicable` classification remains unchanged, and the inspection is not an exhaustive model audit. No changes to SQL migrations, JPA entities, data, workflows or consumer documents are authorized. No diagram is required by this decision; `DOC-DIAGRAMS` was independently approved as `ADD` for future maintained diagrams prioritizing the data model.

**Current Assessment outcome:** 28/28 approved State/Applicability pairs unchanged; **23/28 Adoption Decisions resolved** (13 `PRESERVE`, 3 `OMIT`, 5 `ADAPT`, 2 `ADD`), **5 pending**; Assessment `In Progress`. Only Film read-only; Application/Integration not authorized.

## Pinned security-documentation currency reconciliation — 2026-11-14

A targeted read-only review contrasts Only Film's **current-at-the-pinned-SHA** security overview and code with its explicitly **historical** hardening audit. The fixed consumer evidence baseline is `28d75a50e0a178954dd46acc23300d9dd327843c`; this is not a vulnerability assessment, operational penetration test or an up-to-date certification.

| Pinned source | Direct finding | Review boundary |
| --- | --- | --- |
| [README security section, lines 104–117](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md#L104-L117) | Describes role-based access, BCrypt, CSRF, negative authorization controls, image validation, profile restrictions and no real payment gateway or production hardening. It links the technical consolidation audit for context. | The linked audit is **not explicitly labeled historical in the README link text**; the reader can confuse its earlier prioritized observations with findings verified at the pinned state. |
| [`SECURITY_HARDENING_AUDIT.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md) | Dated **2026-10-10**, explicitly based on earlier commit `0a7e03a0` after PR #12. It lists then-proposed security remediation work and states that its static review is **not a pentest**. | Neither its original risk severities nor proposed issues can automatically be asserted as *current, unresolved vulnerabilities* at later SHA `28d75a50…`. |
| [`SecurityConfig.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/config/SecurityConfig.java) | Declares BCrypt encoding, role restrictions, authenticated routes and an H2 console CSRF/frame exception limited by the **explicit local `dev` profile**, enabled console property and loopback server address. | Static control configuration does **not** verify every endpoint, authorization branch or security outcome dynamically. |
| [`DEMO_CREDENTIALS_SECURITY.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md) and [`DataInitializer.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/config/DataInitializer.java#L49-L74) | The guide documents **random demo passwords by default** and an optional explicitly supplied local override. Pinned `demoPassword()` implements this distinction. | Historical audit references to known embedded demo passwords must not be presented as a verified current default-secret defect. Whether all historical exposed secrets were rotated is not established. |
| [Conventional `.github/SECURITY.md` path](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c/.github) | Direct lookup of the exact path returned **Not Found** at the pinned SHA. | Absence of this path **does not** establish that no security reporting or disclosure guidance exists elsewhere, and does not justify inventing a policy, contact or reporting procedure. |

### Evidence-qualified decision option

**Consider `DOC-SECURITY = ADAPT`** for a **future bounded documentation-only clarification** that labels the dated hardening audit as historical when linked from the README, differentiates current-at-pinned implementation descriptions from historical recommendations, and makes the existing demo-credential guide easier to discover where relevant. An independent security disclosure/contact policy could only be added following a separately verified maintainer policy and appropriate authorization; this review does not propose one.

The previously approved `DOC-SECURITY: Partial / Applicable` remains unchanged, along with security-test and CI evidence limitations. A `README-DEMO` clarification remains a **separate pending Adoption Decision**; this candidate does not authorize code or README edits. Static comparison does **not** certify vulnerability absence, complete security coverage, security hardening, a passed historical Sonar Quality Gate or production readiness.

**Formal Adoption Decision remains `Needs Further Evaluation / —` until express maintainer approval.** Assessment **`In Progress`**, 28/28 approved State/Applicability pairs, **23/28 formally resolved Adoption Decisions** (13 `PRESERVE`, 3 `OMIT`, 5 `ADAPT`, 2 `ADD`), **5 pending**. Only Film strictly read-only; no Application/Integration authorization.


## Formal DOC-SECURITY Adoption Decision — 2026-11-14

The Only Film maintainer expressly approved **`DOC-SECURITY = ADAPT`**, exclusively for a **future, bounded documentation-only clarification** of the 2026-10-10 historical audit's earlier SHA versus the pinned consumer state and contextual discoverability of existing demo-credential guidance. This decision does **not** establish that historical findings remain current, certify absence of vulnerabilities, verify a passed historical Quality Gate or authorize a new security disclosure policy. The formal `Partial / Applicable` evaluation and evidence limits remain unchanged. No security implementation, test, secret, configuration, README or other Only Film change is authorized.

**28/28 Adoption Decisions resolved** (14 `PRESERVE`, 3 `OMIT`, 9 `ADAPT`, 2 `ADD`), 0 pending; 28 State/Applicability pairs approved. Assessment **`In Progress`** and no Application/Integration authorization.
