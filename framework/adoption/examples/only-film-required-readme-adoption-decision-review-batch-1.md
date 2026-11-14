# Only Film — Adoption Decision review batch 1: Required README identity and stack

## Scope and decision protocol

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned consumer reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Repository Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities in this review | `README-HERO`, `README-OVERVIEW`, `README-FEATURES`, `README-TECH-STACK` |
| Formal State / Applicability approvals | **28/28** (maintainer, 2026-11-14; unchanged) |
| Resolved Adoption Decisions | **3/28** formally resolved after this review (maintainer, 2026-11-14); 25 pending |
| Assessment Status | `In Progress` |
| Consumer mutation | `NONE` |
| Purpose | **Record the initial review alternatives and subsequent separate explicit maintainer decisions, without consumer changes** |

The [Assessment Template](../assessment-template.md) permits `PRESERVE`, `ADAPT`, `ADD`, `ACCEPT`, and `OMIT` for an explicitly resolved Adoption Decision, with a recorded rationale; `Needs Further Evaluation / —` is valid while a decision remains open. A formally approved `State` and `Applicability` pair does **not** automatically determine any Adoption Decision.

The [Framework adoption guide](../README.md) keeps Assessment separate from optional Application and Integration. No consumer edit, evidence refresh to a newer Only Film branch, code change, automatic rollout or consumer authorization is implied by this review.

## Formal maintainer Adoption Decision outcome — 2026-11-14

The Only Film maintainer **explicitly approved** three independently resolved Adoption Decisions and expressly retained the fourth as unresolved:

| Responsibility | Decision Status | Adoption Decision | Approval outcome |
| --- | --- | --- | --- |
| `README-HERO` | `Resolved` | `PRESERVE` | Maintain the pinned H1, concise identity and badges; mobile/dark-mode and remote badge rendering remain unverified |
| `README-OVERVIEW` | `Resolved` | `PRESERVE` | Retain the existing integrated introduction; no separate Overview heading required |
| `README-FEATURES` | `Resolved` | `PRESERVE` | Retain role-organized capabilities with explicit simulated-payment qualification; feature-by-feature acceptance not independently established |
| `README-TECH-STACK` | `Needs Further Evaluation` | `—` | No decision authorized; full tool usage and concrete `PRESERVE` versus `ADAPT` rationale remain to be reviewed |

**Authorization boundary:** The 28 existing `State / Applicability` pairs remain formally approved and unchanged, with their original documentary evidence limits. The pinned consumer reference remains `28d75a50e0a178954dd46acc23300d9dd327843c`, separately from the 2026-11-14 human decision date. `PRESERVE` is an Assessment decision to retain existing documentation; it does **not** authorize modifications, deployments, code changes, or integration in Only Film. **Assessment remains `In Progress`; three decisions resolved, twenty-five unresolved; consumer mutation `NONE`.**

The candidate alternatives and initially pending approval language below are retained as **historical preparation**, not as the current decision status.

## Candidate decision matrix

| Responsibility | Maintainer-approved evaluation (unchanged) | Initial decision candidate | Alternative or unresolved gate |
| --- | --- | --- | --- |
| `README-HERO` | `Satisfied / Applicable` | **Consider `PRESERVE`** for the current H1, concise introduction and five technology badges | `ADAPT` only if a concrete readability, visual or badge-accuracy issue merits change; responsive/dark-mode and remote badge rendering not audited |
| `README-OVERVIEW` | `Satisfied / Applicable` | **Consider `PRESERVE`** for the existing integrated introduction | `ADAPT` only for an identified audience/navigation need; no compulsory duplicate heading |
| `README-FEATURES` | `Satisfied / Applicable` | **Consider `PRESERVE`** for role-grouped features and explicit simulated-checkout limitations | `ADAPT` only for concrete misleading claims or a demonstrated readability benefit; bounded CI is not complete behavior acceptance |
| `README-TECH-STACK` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` as default** pending factual and reader-value checks | `PRESERVE` if existing category coverage is accepted with bounded inventory; `ADAPT` only if a specific unsupported/stale entry or useful correction is established |

**These are reviewer-facing candidates, not approved Adoption Decisions.** A `Satisfied` documentary State can still warrant later adaptation, and a `Partial` documentary State need not trigger an edit. A `PRESERVE` decision would record the deliberate choice to retain existing material; it is not proof of production readiness or a waiver of evidence limitations.

## 1. README-HERO — proposed `PRESERVE` consideration

### Source evidence

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) starts with a single H1, `🎬 Only Film`, two short introduction paragraphs and five badges for Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway and Docker Compose.
- The [Framework README-HERO Component](../../components/readme/hero/README.md) calls for a name, concise identity/tagline and restrained prominent badges. A banner is optional.
- The [formally approved Assessment record](only-film-assessment.md) judges documentary coverage `Satisfied / Applicable`, but explicitly preserves unresolved responsive/dark-mode rendering and remote badge availability questions.

### Decision threshold and recommendation

**Consider `PRESERVE`** if the maintainer confirms that this existing introduction is clear and the nonessential visual checks are not blockers. Do **not** add a banner or separate tagline merely to reproduce a framework template shape. `ADAPT` would require a specifically identified visual, accuracy or audience benefit. The review **does not** independently render the README in mobile or dark mode.

**Required explicit human decision:** `PRESERVE`, `ADAPT`, or remain `Needs Further Evaluation / —`, with rationale. No modifications are approved here.

## 2. README-OVERVIEW — proposed `PRESERVE` consideration

### Source evidence

- The same pinned README describes cinema listings, screening/session management, seat selection, purchasing demo tickets and administrator permissions in its opening prose. It distinguishes the collaborative academic origin from subsequent maintenance.
- The [Framework README-OVERVIEW Component](../../components/readme/overview/README.md) asks for the project purpose and problem, with concise language rather than installation instructions or detailed architecture.
- The formally approved Assessment accepts the existing distributed introductory overview as `Satisfied / Applicable` without requiring an exact English-language `Overview` heading.

### Decision threshold and recommendation

**Consider `PRESERVE`** for the currently concise integrated Hero/Overview if the maintainer finds it comprehensible for the intended portfolio audience. An `ADAPT` should be tied to an actual communication need, not a formalistic extra heading that duplicates the introduction. No independent reader usability study was conducted.

**Required explicit human decision:** `PRESERVE`, `ADAPT`, or leave unresolved with rationale. No consumer edit follows from the candidate.

## 3. README-FEATURES — proposed `PRESERVE` consideration

### Source evidence

- The pinned `Funcionalidades` section groups tasks by Visitors, Users and Administrators; it also mentions transactional seat-availability protection and ticket ownership constraints.
- The pinned `Seguridad y límites actuales` explicitly says checkout is a **demonstration flow without an integrated real payment provider**, and does not present security as a complete audit.
- The [Framework README-FEATURES Component](../../components/readme/features/README.md) asks for primary capabilities, not a lengthy implementation specification. The current Assessment approves `Satisfied / Applicable` for this documentary purpose.
- Earlier [bounded pinned test evidence](only-film-verified-surefire-sonar-logs.md) records a selected H2 regression; it is not independent acceptance of every feature and does not establish real payments.

### Decision threshold and recommendation

**Consider `PRESERVE`** for the useful role-based feature orientation while explicitly retaining the simulated checkout qualification. If the reviewer has source-backed reasons to avoid a misunderstood purchase claim, or to move the transaction-locking explanation to architecture, `ADAPT` may be considered narrowly. This is a content decision, not feature-implementation authorization.

**Required explicit human decision:** `PRESERVE`, `ADAPT`, or unresolved. Do not reframe simulated payments as a live provider integration.

## 4. README-TECH-STACK — preserve the open gate until its rationale is clear

### Source evidence

- The pinned `Tecnologías y arquitectura` table groups Backend, Security, Frontend, local H2, PostgreSQL/Flyway persistence, Testing and Infrastructure.
- The earlier Assessment checked the pinned [POM](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) for Java 25 and Spring Boot 4.0.5, and pinned [Compose configuration](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/compose.yaml) for PostgreSQL 17 and the Compose service definitions.
- The [README-TECH-STACK Component](../../components/readme/tech-stack/README.md) suggests categories such as Backend, Frontend, Database, Cloud, DevOps and Testing, but does **not** demand an invented Cloud deployment category.
- The approved `Partial / Applicable` State retains uncertainty over whether every listed tool/dependency is used at this pinned reference; the static Compose definition is not a successful runtime demonstration.

### Decision threshold and recommendation

**Do not yet propose a resolved decision as the default**. The maintained Assessment's proposed decision alternatives are `PRESERVE` or `ADAPT`:

- **`PRESERVE`:** the maintainer accepts the table as sufficiently helpful for the consumer's README audience, while recognizing that the full tool inventory and all runtime claims were not exhaustively checked. Preserving text does not certify tool use.
- **`ADAPT`:** the maintainer points to a specific incorrect/outdated assertion or concrete improvement (e.g., supported usage of a named tool) and records its evidence and proposed documentary delta. No speculative technology addition or cloud claims.
- **`Needs Further Evaluation / —`:** a claim essential to the choice remains unverified; name the targeted source/test needed. Do not select `ADAPT` merely because the approved documentary State is `Partial`.

### Review boundary

No new dependency audit, Compose smoke run or cross-check of every README technology was completed in this first decision batch. Those gaps were recorded in the earlier Assessment. If a decision implies a material runtime claim, verify its actual pinned-source support before formally resolving it.

## Proposed formal review flow

1. Independently confirm or revise the **Decision Status and Adoption Decision** for each of the four Responsibilities, including the chosen rationale and which evidence limits remain.
2. Keep `Needs Further Evaluation / —` for any unapproved choice. In particular, `README-TECH-STACK` may remain unresolved while the other three are addressed.
3. If the maintainer formally approves any `Resolved` decision, record that approval date, source evidence, `Decision Rationale`, and exact decision in a **separate narrow PR** updating the Assessment and the decision register.
4. Preserve the **28 formally approved State/Applicability pairs unchanged**. Do not conflate a resolved `PRESERVE` with code changes; do not authorize `ADAPT` edits without the separate optional Application/Integration workflow.

**Historical preparation boundary:** Merging the earlier preparation PR was not approval of any Adoption Decision. The later explicit maintainer approval of 2026-11-14 now resolves the three identified `PRESERVE` decisions, while `README-TECH-STACK` and 24 other decisions remain `Needs Further Evaluation / —`. The Assessment remains `In Progress`, and Only Film remains read-only.
