# Only Film — Adoption Decision review batch 11: Status and Architecture

## Assessed scope and decision boundary

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable assessed SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Framework Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-STATUS`, `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS` |
| Approved State / Applicability pairs | `28/28`, unchanged |
| Prior formal Adoption Decisions | `16/28`: 13 `PRESERVE`, 3 `OMIT` |
| Unresolved Adoption Decisions | `12/28`, including all three |
| Assessment Status | `In Progress` |
| Consumer mutations | `NONE` |

This packet is a **review proposal**, not a formal Adoption Decision or authorization to update Only Film. Its purpose is to distinguish useful **historical evidence** from the **current-source evidence** that a maintained status or architecture document would require. Merging the packet does not grant a decision, set project maturity, establish current milestones or authorize execution or edits.

## Reviewer-facing options

| Responsibility | Approved State / Applicability | Suggested review posture | Key decision gate |
| --- | --- | --- | --- |
| `README-STATUS` | `Partial / Applicable` | **Retain `Needs Further Evaluation / —`**; consider a later narrowly scoped `ADAPT` | An explicit current `project_status` and `maturity` statement would need a maintainer-selected, source-backed meaning, date and scope |
| `DOC-ARCHITECTURE` | `Partial / Applicable` | **Retain `Needs Further Evaluation / —`**; consider a later bounded `ADAPT` or `PRESERVE` | Reconcile current components and layer exceptions against pinned code before claiming a maintained system-level architecture description |
| `DOC-PROJECT-STATUS` | `Partial / Applicable` | **Retain `Needs Further Evaluation / —`**; consider a later bounded `ADAPT` | Reconstruct actual active work, area progress, next milestone and immediate priorities without projecting historical F3 proposals forward |

The three descriptions serve different purposes: **README-STATUS** gives a quick current public signal, **DOC-ARCHITECTURE** explains the actual system design, and **DOC-PROJECT-STATUS** is an operational progress snapshot. One historical maturity document does not automatically fulfill all three.

## 1. README-STATUS — status and maturity need distinct current evidence

### Source-backed observations

- The directly re-fetched [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) displays badges for **Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway and Docker Compose**. These describe technologies, not maintained project status, current activity, CI health or maturity.
- The directly re-fetched [Framework README-STATUS Component](../../components/readme/status/README.md) identifies `project_status` and `maturity` and positions the content after `README-HERO`. Neither property can be inferred from a successful single CI workflow.
- The directly re-fetched [Technical Maturity Assessment](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md) is dated **2026-10-10** with **different source SHA** `9f2a31e927df105d14e3d30d4d8277fa61883deb`. It describes the then-current evolved academic/portfolio state and a need for additional validation before public production, but **its diagnoses are not a verified current assessment of the pinned SHA**.
- The previously identified successful [GitHub Actions run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) covers bounded selected H2/PostgreSQL checks, not the consumer's ongoing development activity, up-to-date maturity, supported SLA or public deployment readiness.

### Review disposition and alternatives

**Default `Needs Further Evaluation / —`**. A possible future **`ADAPT`** would add or improve a **short, dated, maintainer-confirmed status and maturity statement** in the correct README position, distinguishing academic/portfolio intent from public-production claims. Before selecting it, define the actual relevant state (for example, maintained portfolio project, development phase, or local-only demonstration), the meaning of maturity within the Framework, who verifies it, and how it remains current.

`PRESERVE` could be considered only if the maintainer specifically accepts existing distributed cues as enough for the intended audience, without confusing a technology badge or older assessment with a current status label. **Do not populate speculative project_status/maturity values**, and do not change README under this review PR.

## 2. DOC-ARCHITECTURE — current architecture versus dated audit observations

### Source-backed observations

- The pinned README gives the **nominal** `MVC controller → service/business rules → JPA repository → database` flow and principal domain entities. This provides useful high-level navigation but is not an exhaustive current dependency or control-flow map.
- The directly re-fetched [Framework DOC-ARCHITECTURE Component](../../components/documentation/architecture/README.md) asks for the **current** architecture, major responsibilities, relationships, significant flows and constraints. It allows avoiding a separate document when that would duplicate a sufficiently clear README, and does not prescribe a diagram solely for formality.
- The directly re-fetched [Architecture Maintainability Audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) is dated **2026-10-10**, referencing prior SHA `b6cf52c9` after PR #23. Its examples of controller-to-repository access, entity form binding and rollback risks were observations **on that older baseline**. They cannot be relabeled as unresolved present defects at `28d75a50e0a178954dd46acc23300d9dd327843c` without current code/test verification.
- The directly re-fetched [F3 Functional Audit and Roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) explicitly references another earlier SHA `df63353564485eb6d2d60c982032e5d3c4facbf2` and records historical reconciliations of some earlier findings, demonstrating why snapshots from different baselines must not be merged as a current defect inventory.
- The previous `README-ARCHITECTURE = PRESERVE` approval applies to its **high-level descriptive orientation only**. It does not automatically resolve the separate `DOC-ARCHITECTURE` responsibility for a maintained system-level account.

### Review disposition and alternatives

**Default `Needs Further Evaluation / —`**. A future **`ADAPT`** could reconcile a concise architecture guide to the pinned SHA, but only after source checks establish actual controller/service/repository boundaries and noteworthy exceptions, data/persistence profile roles, authorization responsibilities and the real transaction/checkout constraints. The guide should distinguish observed current behavior from **historical** proposals. This is a **documentation** choice; it does not authorize layer refactoring or correcting an older finding without independent evidence.

`PRESERVE` could be defensible if the current README plus clearly dated specialist references are adequate for the target audience and no maintained architecture guide is needed. That is a separate evidence- and audience-based judgment. `DOC-DIAGRAMS` remains independently unresolved and must not be triggered by this packet.

## 3. DOC-PROJECT-STATUS — next milestone cannot be reconstructed from old plans alone

### Source-backed observations

- The directly re-fetched [Framework DOC-PROJECT-STATUS Component](../../components/documentation/project-status/README.md) aims to maintain a **dated operational snapshot**: general state, progress by area, active work, next milestone, immediate goals and material risks, at a suitable level of detail. It is not interchangeable with a roadmap, backlog or changelog.
- The pinned [Technical Maturity Assessment](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md) refers to `9f2a31e927df105d14e3d30d4d8277fa61883deb`, and the pinned-tree [F3 Functional Audit and Roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) refers to `df63353564485eb6d2d60c982032e5d3c4facbf2`, **both earlier than the assessed consumer SHA**.
- The F3 document lists proposal identifiers and planned investigations, but no current pinned-SHA reconciliation of F3 item status, active contributors, next milestone or remaining committed work was established. Presence of a roadmap file is **not** proof of ongoing or completed work.
- The README lists possible REST API, real payment integration, observability, deployment automation and maintainability improvements as **nonbinding options**. The separate `README-ROADMAP = PRESERVE` decision explicitly did **not** convert them into project-status facts.
- Successful selected CI jobs at the pinned SHA do not determine current project phase, issue state or upcoming milestone.

### Review disposition and alternatives

**Default `Needs Further Evaluation / —`**. A possible future **`ADAPT`** would require a current, explicitly dated project-area overview based on actual maintained sources: issue/PR disposition, verified finished work, open objectives, blockers and the maintainer's next milestone. A project status page should avoid copying every issue or promising delivery dates that are not approved.

`PRESERVE` could be argued only if the intended audience needs no richer status than the existing clearly dated portfolio/maturity context. That choice would preserve **historical context as historical**, rather than claim it is the present operational picture. No current milestone or maturity is inferred here.

## Supplementary live-repository status check — 2026-11-14

This limited check supplements the **pinned-source** review above with separately identified **mutable GitHub repository observations**; it does not change the immutable Assessment baseline or establish a maintainer-approved project phase.

| Check | Observation | Evidence boundary |
| --- | --- | --- |
| Consumer `main` head | At this check, GitHub's latest commit listing placed `28d75a50e0a178954dd46acc23300d9dd327843c` first (merge PR #493, F3.003b occupancy/ranking). | A checked point in time, **not** a promise that the branch will remain at this SHA. |
| Open issues | [#248 — SonarCloud October 2026 follow-up](https://github.com/fran-eliot/only_film/issues/248) and [#427 — Thymeleaf fallback HTML titles](https://github.com/fran-eliot/only_film/issues/427) appeared in the GitHub open-issue search. | These record maintenance topics; their issue descriptions are not independently revalidated defect findings, quality metrics or an exhaustive work plan. |
| Open pull requests | The GitHub open-PR search returned no results for `fran-eliot/only_film`. | This does **not** establish that development is inactive or that all historical F3 work is complete. |
| Next milestone and accountable project phase | Not established by these checks. | Requires an authoritative current source or explicit maintainer confirmation. |

**Implications for the existing Batch 11 gates:**

- `README-STATUS`: a live open-issue snapshot provides no contractually approved `project_status` or `maturity` values; do not infer production readiness or a status label.
- `DOC-ARCHITECTURE`: the confirmed F3.003b merge establishes a code-history anchor, but no new pinned-SHA controller/service/repository audit was performed in this check; do not infer the entire current dependency graph.
- `DOC-PROJECT-STATUS`: the two observed open issues are concrete candidate inputs for a **dated** operational snapshot. They are insufficient to classify all areas of progress, past F3 dispositions, active ownership or the next milestone.

**Review outcome:** retain all three `Needs Further Evaluation / —`. The 28 approved State/Applicability pairs and the 16 formally resolved Adoption Decisions are unchanged. No consumer mutation or Application/Integration authorization is implied.

## Pinned-source architecture reconciliation — 2026-11-14

The following **targeted static code review** uses Only Film commit `28d75a50e0a178954dd46acc23300d9dd327843c` directly. It distinguishes surviving architectural patterns from older audit claims; it is **not** a comprehensive application audit or runtime verification.

| Area | Observed at pinned SHA | Significance for `DOC-ARCHITECTURE` |
| --- | --- | --- |
| Administrative ticket editing | [`TicketController.saveTicket`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/TicketController.java) accepts `@Valid TicketAdminForm`, not a full `Ticket` entity. It delegates to [`TicketService.updateAdminDiscount`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/service/TicketService.java), which checks a free seat, constrains the discount and uses the checkout lock inside `@Transactional`. | The older October 10 maturity report's direct entity-binding finding **must not be repeated as a verified present condition**. These source-level safeguards do not amount to a complete security certification. |
| Review management | [`ReviewController`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/ReviewController.java) directly injects `ReviewRepository`, `MovieRepository` and `TicketRepository` for reads, eligibility checks and persistence; its edit flow binds a `ReviewFormDTO`, verifies owner/admin permission, and copies selected fields into the persisted review. | A strictly universal `controller → service → repository` claim would be inaccurate. Direct repository access is demonstrably present, but this alone is not proof of an exploitable defect. |
| Session management | [`SessionController`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/SessionController.java) accesses session, movie, room and ticket repositories for selected reads, while delegating save/deactivation to [`SessionManagementService`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/service/SessionManagementService.java). The service uses `@Transactional`, validates changes and coordinates deactivation with inventory locking. | Document the **mixed controller query / service-managed mutation** pattern instead of presenting all operations as passing through a service. |
| Reporting | [`DashboardMetricsService`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/service/DashboardMetricsService.java) provides `@Transactional(readOnly = true)` sales, occupancy and movie-ranking aggregation methods via `TicketRepository`. | A concrete example of service-backed reporting, not a basis for generalizing the entire application topology. |

**Evidence boundary and next decision gate.** This targeted review materially narrows uncertainty about two historical concerns and identifies mixed architecture boundaries, but it does not exhaustively reconcile all eight controllers, security configuration, JPA relationships, profiles, transactions or runtime paths. The older audit and maturity report remain **dated evidence about earlier SHAs**, not a current defect list. Before choosing `PRESERVE` or `ADAPT`, determine whether a concise, source-verified description of the real architecture is needed beyond the existing README and specialist documents. Keep `DOC-ARCHITECTURE = Needs Further Evaluation / —` until explicit maintainer approval.

## Reviewer approval gate

The most evidence-conservative recommendation is to **leave all three decisions unresolved** until the precise informational audience and current-source checks are agreed. Reviewer alternatives remain:

- `README-STATUS`: keep pending; optionally later `ADAPT` with explicitly approved current `project_status` / `maturity` values.
- `DOC-ARCHITECTURE`: keep pending; later `PRESERVE` the evidence-qualified distributed context or `ADAPT` a verified current architecture explanation, depending on audience needs.
- `DOC-PROJECT-STATUS`: keep pending; optionally later `ADAPT` a bounded current milestone and area-progress record after verified issue/PR reconstruction.

A **formal maintainer approval** is required before a new PR may mark any entry `Resolved`. In all scenarios, all 28 independent State and Applicability approvals stay intact.

**No Adoption Decision is resolved by this document. Existing totals stay 16/28 resolved (13 `PRESERVE`, 3 `OMIT`), 12 pending; Assessment `In Progress`; Only Film strictly read-only.**


## Formal maintainer decision — 2026-11-14

After the preparation and pinned-source reconciliation above, the Only Film maintainer **formally approved `DOC-ARCHITECTURE = ADAPT`**, strictly for a **future, bounded documentation-only adaptation**. Its approved `Partial / Applicable` classification stays unchanged. The decision authorizes neither an immediate document addition nor any consumer modification; future Application scope and source-backed wording require separate approval. The approval does **not** make historical audit observations current defects, require a new diagram, authorize refactoring or override `README-ARCHITECTURE = PRESERVE`.

`README-STATUS` and `DOC-PROJECT-STATUS` remain `Needs Further Evaluation / —`. This is the **postreview outcome** superseding the earlier recommendation to keep all three pending: **17/28 Adoption Decisions resolved** (13 `PRESERVE`, 3 `OMIT`, 1 `ADAPT`), **11 pending**. All 28 approved State/Applicability pairs remain unchanged. Assessment **`In Progress`**; Only Film **read-only, no mutations**.


## Formal maintainer decisions — README-STATUS and DOC-PROJECT-STATUS (2026-11-14)

The maintainer formally approved both `README-STATUS = ADAPT` and `DOC-PROJECT-STATUS = ADAPT`, superseding their prior deferrals. Both retain their independently approved `Partial / Applicable` classifications. The first concerns only a future bounded, dated and evidenced operational status/maturity statement; the second only a future dated operational progress and objectives summary supported by current authoritative sources. No maturity value, phase, milestone, F3 disposition, complete test run or production-readiness claim is approved or inferred.

These Assessment decisions do not authorize changes to Only Film or any Application/Integration execution. All 28 State/Applicability pairs remain unchanged. **19/28 decisions resolved** (13 `PRESERVE`, 3 `OMIT`, 3 `ADAPT`), **9 pending**. Assessment **`In Progress`**, consumer mutations **`NONE`**.
