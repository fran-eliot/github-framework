# Only Film — ADR, database and local deployment: human review batch

## Scope and review contract

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable consumer baseline | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `DOC-ADR`, `DOC-DATABASE`, `DOC-DEPLOYMENT` |
| Human State / Applicability approval | **All three explicitly approved by the Only Film maintainer on 2026-11-14; dated record below** |
| Formal approvals after review | `26/28` |
| Assessment | `In Progress` |
| Adoption Decisions | `0` resolved |
| Consumer mutation | `NONE` |

This preparation packet reopens exact consumer Markdown guides, Compose and Dockerfile, and the Compose smoke workflow at the pinned SHA, plus earlier Framework review evidence. It establishes **documentary claims and review choices only**; a defined workflow is not proof of its execution, and a local Compose arrangement is not production readiness. This packet does **not** approve any Assessment values or authorize consumer changes.

## Formal maintainer approval outcome — 2026-11-14

The Only Film maintainer **expressly approved** the following independent State and Applicability classifications:

| Responsibility | Approved State | Approved Applicability |
| --- | --- | --- |
| `DOC-ADR` | `Partial` | `Applicable` |
| `DOC-DATABASE` | `Partial` | `Applicable` |
| `DOC-DEPLOYMENT` | `Partial` | `Applicable` — **local, nonproduction Docker Compose only** |

Evidence limits remain: the project-wide accepted architectural-decision inventory and complete database relationships/invariants have not been verified; the pinned Compose smoke execution was not confirmed; and the local upload-volume documentation must still be distinguished from production-grade durability and backups. No failing Compose execution or data-loss defect is inferred.

**Authorization:** the Assessment remains `In Progress`; all Adoption Decisions remain `—` with `Needs Further Evaluation`. No deployment, migration, additional documentation or modifications to Only Film are authorized. The provisional recommendations below remain as **historical preapproval preparation**, not as unapproved current values.

## Evaluation candidates

| Responsibility | Current unapproved State / Applicability | Human-review recommendation | Scope and limitation |
| --- | --- | --- | --- |
| `DOC-ADR` | `Partial / Applicable` | **Retain `Partial / Applicable`** | The project records important technical tradeoffs and operational decisions in specialized guides, but a maintained current decision register with consistent context/status has not been verified |
| `DOC-DATABASE` | `Partial / Applicable` | **Retain `Partial / Applicable`** | PostgreSQL profiles and a specific Flyway integrity constraint are documented; a navigable high-level relational model and all material current invariants were not demonstrated |
| `DOC-DEPLOYMENT` | `Partial / Applicable` (local environment) | **Retain `Partial / Applicable`** | Substantial local Compose guidance exists and a bounded upload-persistence wording inconsistency merits review; successful full Compose execution at this SHA remains unverified |

These are **Optional Responsibilities**. A separate ADR directory, an ER diagram or production deployment instructions must not be imposed simply because a Component identifier exists. `Applicable` for deployment is scoped exclusively to **local, nonproduction Docker Compose**.

## 1. DOC-ADR — decision explanations without a verified active decision register

### Direct evidence

- [Pinned `docs/FLYWAY_V2_SEAT_UNIQUENESS.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) explains why `UNIQUE(session_id, fila, seat)` is introduced through V2 while preserving migration V1, its `NULL` limitations, a duplicate-data preflight query, and functional approval rather than destructive automatic repair for collisions.
- [Pinned `docs/DEPENDENCY_MAINTENANCE.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md) documents review policy: weekly Dependabot proposals, `major` changes separated from `minor/patch`, no automatic merges, and checks to inspect before approving upgrades. The guide also names an **outstanding possible CI-overlap optimization**, not an accepted decision to remove tests.
- An earlier [architecture maintainability audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) is dated 2026-10-10 against an older baseline and therefore cannot be promoted into a current adopted-decision inventory.
- The earlier [Optional technical semantic review](only-film-optional-final-semantic-review.md) did not identify a dedicated ADR index in a bounded source sample. No comprehensive source/decision inventory was newly executed here. `DOC-ADR` appears in Template metadata; the earlier Framework catalog review did not identify an independently specified Component for it.

### Interpretation

The guides give concrete, valuable records of **selected technical rationale**, not simply end-user instructions. `Partial / Applicable` is a defensible documentary candidate because it is unclear how durable architectural choices, alternatives, consequences and *current acceptance status* are discovered consistently. It is not a finding that decisions are undocumented or that an ADR system is compulsory.

**Reviewer question:** Are these thematic explanations sufficient for the portfolio's current audience? `Satisfied` could be supported if the reviewer judges the existing distributed decision rationale complete enough; `Partial` should reflect a named navigation/currentness gap, not an absent `adr/` folder.

**Unverified:** full project-wide decision inventory, whether historical audit recommendations were adopted, and completeness of context/alternative/consequence records. No new ADR process or architecture changes are authorized.

## 2. DOC-DATABASE — focused guides, but incomplete verified conceptual coverage

### Direct evidence

- [Pinned `docs/POSTGRESQL_SETUP.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) distinguishes H2 default and local `dev`, `postgres` and `postgres,demo` profiles. It describes `DB_URL`, `DB_USERNAME`, `DB_PASSWORD`, Flyway and Hibernate schema validation; the `demo` option is explicitly **local-only** and needs special care with known sample credentials.
- [Pinned `docs/FLYWAY_V2_SEAT_UNIQUENESS.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) explains the key uniqueness rule, its limitation for incomplete seat coordinates, the preflight duplicate SQL, and the prohibition against modifying historical V1 or automatically deleting colliding business records.
- The pinned README enumerates major domain entities `Movie`, `Room`, `Session`, `Ticket`, `Review`, `User`, and distinguishes H2 vs PostgreSQL persistence.
- Earlier [pinned PostgreSQL job evidence](only-film-verified-surefire-sonar-logs.md) establishes specific successful H2/PostgreSQL checks. Those jobs do not establish full documentary model coverage or every data invariant.
- The detailed migration SQL and JPA entity relationships were **not re-inventoried exhaustively** in this batch. Consequently, neither a full schema model nor all constraints are asserted here.

### Interpretation

`Partial / Applicable` remains a conservative **review candidate** because specialized database setup and integrity guides are useful but do not necessarily give an accessible end-to-end explanation of entity relationships, lifecycle and materially important invariants. It does **not** signify failing migrations or invalid database design.

**Reviewer question:** Is the current distributed schema/setup guidance enough for the project's intended contributor? If so, `Satisfied / Applicable` could be defensible without requiring a new ER diagram. Any claim about current schema correctness must be separately source-validated.

**Unverified:** exhaustive schema/JPA inventory, complete entity relationships, data lifecycle, and all constraints. No migration, database, or data-repair action authorized.

## 3. DOC-DEPLOYMENT — explicitly local Compose, not production

### Direct evidence

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) and [`docs/POSTGRESQL_SETUP.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) describe preparing a private `.env`, `docker compose up --build -d`, local `http://localhost:8080/movies`, and the important difference between `docker compose down` and **destructive** `down -v`.
- The [pinned `compose.yaml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) defines `app` and `postgres`, a PostgreSQL health check, `postgres_data` and `uploads_data` named volumes, and loopback-only `127.0.0.1` port publishing. The app mounts `uploads_data:/app/uploads` and sets `ONLYFILM_UPLOAD_DIR=/app/uploads`.
- The [pinned Dockerfile](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/Dockerfile) builds using Java 25/Maven and runs a Java 25 JRE image as UID `10001`; these are static configuration facts, **not proof of successful runtime security or startup**.
- The [pinned `compose-smoke.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) **defines** Compose configuration/build, an HTTP `/movies` 200 assertion, Flyway V1 check, database persistence after restart, and upload-file persistence after app recreation. The earlier [Compose evidence gap](only-film-compose-evidence-gap.md) found no confirmed positive `compose-smoke` check directly associated with the evaluated SHA in its inspected check set. Do not substitute JAR-on-PostgreSQL job success or infer that Compose fails.
- **Specific source-language question:** `docs/POSTGRESQL_SETUP.md` explicitly says `postgres_data` and `uploads_data` persist local DB/upload content and maps uploads to `/app/uploads`, while its later **“Seguridad y límites”** section says the app does not yet have a definitive persistence strategy for container-uploaded files. The latter warning may mean **production-grade backup/durability** rather than the already configured local volume; the distinction is **not explicitly resolved in that sentence**.

### Interpretation

`Partial / Applicable` is a defensible **documentary recommendation** because the deployment guide's upload-persistence warning can be misunderstood as contradicting the described local named volume, and a full pinned-SHA Compose run has not been independently verified. This is not a known data-loss bug or evidence of Compose failure.

The reviewer should judge the Documentation Responsibility against the **supported local development/demo environment**, not production deployment that the README explicitly disclaims. A reviewer could instead approve `Satisfied / Applicable` if static guidance and clear scope are enough despite missing execution evidence, provided the ambiguous warning is accepted or clarified.

**Unverified:** end-to-end pinned Compose smoke pass, reliable production backup/recovery, public deployment, production hardening and disaster recovery. No deployment, backup operation, CI change, production claim or README/guide edit is authorized.

## Formal human-review gate

Proposed independently for maintainer confirmation:

1. `DOC-ADR = Partial / Applicable` — decision rationale exists, but maintained decision lifecycle/coverage has not been shown.
2. `DOC-DATABASE = Partial / Applicable` — valuable setup and Flyway guidance, but full conceptual model documentation not demonstrated.
3. `DOC-DEPLOYMENT = Partial / Applicable` **for local Compose only** — relevant instructions exist, with named-volume vs production-durability wording to distinguish.

The maintainer must explicitly accept or revise the **State and Applicability for each**. An approval is **separate** from merging this preparation PR and **separate** from any later Adoption Decision (including `PRESERVE`, `ADAPT` or `ADD`). No consumer edits, CI runs, data migration or production operations follow from the classifications.

The Assessment remains `In Progress` with `23/28` approved and **5** still requiring formal review. `Decision Status: Needs Further Evaluation` and `Adoption Decision: —` remain on all three. `DOC-API` and `DOC-REFERENCES` are **not included** in this packet because their independent State and Applicability interpretations need a separate focused contract-scope review.
