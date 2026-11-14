# Only Film — Adoption Decision review batch 9: Roadmap, Diagrams and Database Model

## Immutable assessment scope

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned consumer source | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-ROADMAP`, `DOC-DIAGRAMS`, `DOC-DATABASE` |
| Previously approved State / Applicability | `28/28` pairs, unchanged |
| Formal Adoption Decisions after explicit maintainer review | `15/28`: 12 `PRESERVE`, 3 `OMIT` (Roadmap approved 2026-11-14) |
| Open Adoption Decisions | `13/28`, including `DOC-DIAGRAMS` and `DOC-DATABASE` |
| Assessment status | `In Progress` |
| Consumer changes | `NONE` |

This is **decision preparation**, not formal approval or implementation. A separate, express maintainer decision is required to resolve any of these Responsibilities. The immutable pinned snapshot is evidence, whereas the maintainer's 2026-11-14 interest in diagrams is **current preference**, not a property proven at that commit. Merging this packet does not approve `PRESERVE`, `ADD`, or any consumer change.

## Formal maintainer Adoption Decision outcome — 2026-11-14

The Only Film maintainer **expressly approved `README-ROADMAP = PRESERVE`** and expressly retained `DOC-DIAGRAMS` and `DOC-DATABASE` unresolved:

| Responsibility | Decision Status | Adoption Decision | Approved scope / evidence limitations |
| --- | --- | --- | --- |
| `README-ROADMAP` | `Resolved` | `PRESERVE` | Retain **only the existing qualified possible-future-work overview** in the pinned README. It is **not** current milestones, delivery dates, priorities, completed functionality or a binding roadmap; the earlier F3 initiatives were not individually reconciled with the pinned SHA |
| `DOC-DIAGRAMS` | `Needs Further Evaluation` | `—` | The diagram inventory remains **nonexhaustive** and no diagram type, purpose, implementation or accuracy gate has been approved; no diagrams are authorized |
| `DOC-DATABASE` | `Needs Further Evaluation` | `—` | There is no exhaustively verified current JPA relationship model, cardinality inventory or SQL invariant list, and no model diagram or database change is authorized |

**Express maintainer approval date:** 2026-11-14; **immutable consumer evidence reference:** `28d75a50e0a178954dd46acc23300d9dd327843c`. All 28 previously approved State / Applicability pairs remain unchanged: in particular `README-ROADMAP = Partial / Applicable`, `DOC-DIAGRAMS = Missing / Applicable` and `DOC-DATABASE = Partial / Applicable`.

**Authorization boundary:** Assessment `In Progress`; **15/28 Adoption Decisions resolved** (12 `PRESERVE`, 3 `OMIT`) and **13 unresolved**. No Only Film code, documentation, diagram, database model, migration, issue, milestone, release, configuration, test, deployment, Application or Integration change is authorized.

The candidate language below is **historical preparation material** and does not override the maintainer-approved decision status above.

## Proposed decision posture

| Responsibility | Already approved State / Applicability | Reviewer-facing recommendation | Essential distinction |
| --- | --- | --- | --- |
| `README-ROADMAP` | `Partial / Applicable` | **Consider `PRESERVE`** strictly for the existing **nonbinding future-ideas overview** | Do not relabel it a verified milestone plan or assert F3 initiatives are still open or committed |
| `DOC-DIAGRAMS` | `Missing / Applicable` | **Retain `Needs Further Evaluation / —`**; `ADD` is conditional | Confirm the single highest-value visualization, diagram-specific source and acceptance criteria before authorizing addition |
| `DOC-DATABASE` | `Partial / Applicable` | **Retain `Needs Further Evaluation / —`** | PostgreSQL/Flyway instructions and domain entity names are not a verified, complete relationship/invariant model |

`PRESERVE` for the README does **not** change its `Partial` State. `ADD` for a diagram would be a subsequent adoption choice, not a present task to create an image or edit Only Film.

## 1. README-ROADMAP — narrow existing future-ideas purpose

### Source-backed findings

- The directly re-fetched [pinned Only Film README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contains `Próximas líneas de evolución`, which names possible **REST API**, **real payment provider**, **observability**, **deployment automation** and **maintainability improvements**. The text expressly says these are **possible expansions, not implemented capabilities**.
- The directly re-fetched [F3 Functional Audit and Roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) identifies its own earlier baseline as `df63353564485eb6d2d60c982032e5d3c4facbf2` from October 2026, and proposes F3.002–F3.008 initiatives. Neither its presence in a later pinned tree nor its earlier observations prove which initiatives are currently open, completed, reprioritized or committed.
- The directly re-fetched [README-ROADMAP Component](../../components/readme/roadmap/README.md) says it briefly summarizes future phases, **not** that it replaces a dedicated `ROADMAP.md`. It does not require fabricated milestones, owner assignments, delivery dates or a separate planning document.
- The maintainer previously approved `Partial / Applicable` because the README already offers a reader-facing future direction but not demonstrated current priorities, committed next phases or reconciled F3 status.

### Decision alternatives

**Consider `Resolved / PRESERVE`** **only** to keep the **honestly qualified future-ideas overview currently in the README**. This is a deliberately narrow scope choice: the existing ideas are not a guaranteed plan, a versioned release forecast, evidence of completed technical features, or a current status report. Preserving this documentary purpose can coexist with `Partial / Applicable` because detailed phase prioritization is still unverified.

Alternatively, **keep `Needs Further Evaluation / —`** if the maintainer believes `README-ROADMAP` must describe a **current ordered next-phase plan** rather than potential evolution directions. Choosing `ADAPT` requires a verified mismatch or actual current commitments to communicate, not the existence of a dated historical planning file alone.

**No F3 issue closure, new feature commitment, timetable, README update or Only Film edit is approved by this packet.**

## 2. DOC-DIAGRAMS — decide what a diagram must explain first

### Source-backed findings

- The pinned README describes a **nominal** `MVC controller → service → JPA repository → database` architecture in prose, not a maintained technical diagram. A description of the nominal flow must not be treated as evidence that **every** controller respects strict service boundaries; the [historical Architecture Maintainability Audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) refers to a different, **older** SHA `b6cf52c9`.
- The earlier [targeted diagram spot-check](only-film-optional-contract-spotcheck.md) examined nine named pinned Markdown files and selected artifact filenames; it did not establish a maintained diagram in that **bounded sample**, but it was **not an exhaustive search of every embedded image or Markdown diagram**.
- The [Framework Architecture Component](../../components/documentation/architecture/README.md) treats diagrams as optional, useful where they explain real current dependencies and flows. A dedicated `DOC-DIAGRAMS` Component specification was not identified during the prior catalog check; no unobserved mandatory diagram format can be imposed.
- The maintainer separately confirmed on **2026-11-14** that a future diagram would be valuable and approved `Missing / Applicable` with the sampled-evidence caveat. This is not an `ADD` decision or authorization to create a diagram.

### Decision alternatives and proposed first scope

**Default `Needs Further Evaluation / —`.** If a future `ADD` is chosen, the most narrowly useful first candidate is **one high-level current architecture orientation diagram**, not a trio of diagrams or a claim that all code respects a theoretical layering standard.

Minimum approval gate for such a future diagram:

1. **Audience/question:** identify what a portfolio reader or maintainer cannot understand efficiently from the current textual architecture and repository tree.
2. **Pinned source checks:** recheck actual controllers, services, repositories and configuration at `28d75a50e0a178954dd46acc23300d9dd327843c`; distinguish nominal layers from code-level exceptions and show H2/PostgreSQL/Flyway only where verified.
3. **Artifact specification:** decide diagram form (for example Mermaid in a maintained Markdown document), owning document/location and how to keep it updated; the Framework currently supplies no verified DOC-DIAGRAMS-specific format mandate.
4. **Accuracy and limits:** represent supported dependencies, not unsupported formal architecture, deployed topology, live services or production guarantees. Define review and updating responsibility.

**Alternative candidates:** a domain/entity relationship view is linked to the still-unresolved `DOC-DATABASE` model inventory, while a checkout/seat-concurrency view requires current flow/transaction verification. These are **future choices**, not approved additions.

**No diagram is generated and no Only Film files are created or changed.**

## 3. DOC-DATABASE — relationship information and model completeness remain uncertain

### Source-backed findings

- The pinned [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) names domain entities `Movie`, `Room`, `Session`, `Ticket`, `Review` and `User` and distinguishes default H2 from persistent PostgreSQL with Flyway.
- The previously verified [PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) explains database profiles, Compose environment variables, Hibernate validation and migration operation.
- The [Flyway V2 seat uniqueness guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) documents a particular `UNIQUE(session_id, fila, seat)` constraint and its collision and `NULL` considerations, **not every relationship, index, JPA mapping or data lifecycle invariant**.
- Selected successful PostgreSQL integration jobs observed in [the earlier pinned CI review](only-film-pinned-quickstart-ci-verification.md) are bounded execution evidence; they neither prove complete conceptual documentation nor justify extrapolation about every schema invariant.

### Decision alternatives

**Default `Needs Further Evaluation / —`.** An eventual `PRESERVE` may be suitable if the portfolio audience only needs the existing **operational database instructions**. A narrowly defined `ADAPT` could be considered if a current, confirmed navigation gap justifies a conceptual summary of core entities and relationships. Neither choice requires a speculative ER diagram.

Before committing to **any** new entity diagram, verify entity fields, multiplicities, optional relationships and database constraints against pinned classes and SQL; do not infer relationship cardinality from names alone. This is a documentation decision, not a JPA/database migration authorization.

## Formal maintainer decision gate

Recommended post-merge review bundle, to be approved or declined **separately and explicitly**:

- `README-ROADMAP = PRESERVE` **only** for its existing **nonbinding, clearly prospective** ideas list, not a current phase/milestone commitment.
- `DOC-DIAGRAMS = Needs Further Evaluation / —` until **one** diagram subject, source/accuracy checks and acceptance criteria are approved.
- `DOC-DATABASE = Needs Further Evaluation / —` until reader need and pinned model completeness are evaluated.

If expressly approved, a later **separate PR** should update the canonical [Assessment](only-film-assessment.md), [consolidated review matrix](only-film-consolidated-review-matrix.md) and this review packet, recording formal reviewer/date, evidence-limited rationale, and the exact selected allowed decision token.

**Postapproval status:** All 28 State / Applicability pairs unchanged; 15 Adoption Decisions formally resolved (12 `PRESERVE`, 3 `OMIT`), 13 unresolved. Assessment `In Progress`. Only Film strictly read-only. The earlier preparation PR did not itself grant these decisions; the separate, express maintainer approval on 2026-11-14 governs the outcome.


## Formal DOC-DATABASE and DOC-DIAGRAMS Adoption Decisions — 2026-11-14

The Only Film maintainer independently **approved `DOC-DATABASE = ADAPT`** and **`DOC-DIAGRAMS = ADD`**, superseding the earlier deferrals in this preparation packet. `DOC-DATABASE` is limited to a future explanation of the **pinned, source-verified relational model** without changes to schema, JPA or migrations. `DOC-DIAGRAMS` is limited to **future maintainable, evidence-backed technical diagrams**, prioritizing the data model. The approval does not require a diagram immediately, specify its final rendering, or guarantee that the bounded earlier inventory exhaustively excluded existing diagrams.

The independently approved `DOC-DATABASE: Partial / Applicable` and `DOC-DIAGRAMS: Missing / Applicable` classifications and all evidence limitations remain unchanged. `README-ROADMAP = PRESERVE` remains unchanged. **23/28 decisions resolved** (13 `PRESERVE`, 3 `OMIT`, 5 `ADAPT`, 2 `ADD`), **5 pending**. Assessment **`In Progress`**; Only Film strictly unmodified; no Application/Integration authorization.
