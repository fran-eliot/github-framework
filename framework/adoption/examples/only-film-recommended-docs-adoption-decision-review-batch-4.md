# Only Film — Adoption Decision review batch 4: Recommended technical documentation

## Scope and controlled baseline

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable consumer reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS`, `DOC-TESTING` |
| Approved State / Applicability pairs | `28/28` — maintained |
| Formally resolved Adoption Decisions | `7/28` — existing `PRESERVE` approvals only |
| Unresolved Adoption Decisions | `21/28` — includes all three in this packet |
| Assessment status | `In Progress` |
| Consumer changes | `NONE` |

This document **prepares** a separate maintainer decision. It does not approve `PRESERVE`, `ADAPT`, `ADD`, `ACCEPT`, or `OMIT`, and it does not start optional Application or Integration. The [Assessment Template](../assessment-template.md) permits `Needs Further Evaluation / —` when evidence or the intended decision has not been accepted. The previous approval of a documentary `State / Applicability` pair does not determine its Adoption Decision.

## Initial decision comparison

| Responsibility | Maintainer-approved classification | Reviewer-facing candidate | Distinguishing evidence gate |
| --- | --- | --- | --- |
| `DOC-ARCHITECTURE` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Determine whether the README plus historical audit is adequate as maintained architecture guidance or a targeted, current architecture description is needed; do not carry older code findings forward unverified |
| `DOC-PROJECT-STATUS` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Identify a present-day verifiable progress-by-area summary, next milestone and ownership; historical F3 planning and past maturity are not current execution status |
| `DOC-TESTING` | `Partial / Applicable` | **Consider documentary `PRESERVE`, conditionally** | Accept the existing specialized guides as sufficient at their stated scope, or identify a specific mismatch or missing reproducibility instruction warranting `ADAPT` |

None of these candidates is a resolved decision. `Partial` does **not** independently mandate a new document or a change. `PRESERVE` is permissible with acknowledged evidence limits but does not promote `Partial` to `Satisfied`, establish successful execution, or waive later corrections.

## 1. DOC-ARCHITECTURE — current description versus historical analysis

### Source-backed observations

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) presents the **principal** Controller MVC → Service/Rules → JPA Repository → Database flow and names the principal domain entities; this was considered sufficient for the *separate* `README-ARCHITECTURE` responsibility, which is already `PRESERVE`.
- The directly re-fetched [`ARCHITECTURE_MAINTAINABILITY_AUDIT.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) says **2026-10-10** and explicitly references `main` after PR #23, `b6cf52c9`. It notes controller-to-repository paths and proposes improvements **at that older reference**. The present audit does **not** recheck the asserted paths throughout the pinned SHA.
- The directly re-fetched [F3 functional audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) is based on `df63353564485eb6d2d60c982032e5d3c4facbf2`, also earlier than the assessed reference; it is planning/evidence history, not a current architectural finding.
- The [Framework Architecture Component](../../components/documentation/architecture/README.md) asks for a useful description of context, components, relationships, flows, decisions and constraints. It explicitly notes that a smaller project can keep an adequate explanation in the README instead of creating a redundant architecture document.

### Decision alternatives and threshold

**Default: leave `Needs Further Evaluation / —`.** The maintainer should first decide whether contributors need a more current explanation of component relationships and constraints than the README currently supplies.

- `PRESERVE`: if the current overview plus explicitly dated audit is accepted as sufficiently useful for this project, without presenting historic audit findings as current defects.
- `ADAPT`: if a **specific** current architectural relationship, constraint or reader need is missing or inaccurate, and a bounded source-backed change can be described. No new document should be created automatically.
- Remain `—`: if the current architecture cannot be distinguished reliably from historical descriptions or the reader requirement remains unclear.

**Limit:** no complete pinned controller/service dependency inventory, runtime architecture verification, refactor, diagram or consumer edit was performed.

## 2. DOC-PROJECT-STATUS — status must match an actual reference

### Source-backed observations

- The [Framework Project Status Component](../../components/documentation/project-status/README.md) describes a **dated operational snapshot**: overall status, progress by area, work in progress, next milestone, risks and immediate objectives. It explicitly notes that a separate page may be unnecessary if a concise README already communicates this sufficiently.
- The directly re-fetched [`TECHNICAL_MATURITY_ASSESSMENT.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md) records the date **2026-10-10**, baseline `9f2a31e927df105d14e3d30d4d8277fa61883deb` and a static maturity assessment **for that reference**. It is not current status evidence at the later pinned SHA.
- The [F3 functional audit and roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) is tied to `df63353564485eb6d2d60c982032e5d3c4facbf2`. Its planned work does not verify which F3 issues have been completed, canceled, superseded or remain open at the pinned reference.
- The pinned README distinguishes *possible future improvements* such as REST, payment integration, observability and deployment automation. These do **not** establish a current milestone or a live workstream status. Historical successful CI checks similarly do not establish current project management state.

### Decision alternatives and threshold

**Default: leave `Needs Further Evaluation / —`.** Neither `PRESERVE` nor `ADAPT` should be selected by treating an earlier plan as today's backlog.

- `PRESERVE`: only if the maintainer deliberately judges the present distributed, explicitly historical descriptions sufficient for the intended consumer audience, with no falsely current milestone.
- `ADAPT` or `ADD`: only after checking real current scope and milestone against appropriate source references and agreeing on a maintainable form. A new page must not be created simply to mirror the Framework.
- Remain `—`: pending a verified current progress summary and reader use case.

**Limit:** no current F3 issue status, up-to-date milestone, roadmap progress, maintenance schedule, or new project status fact was established by this packet.

## 3. DOC-TESTING — conditional preservation of specialized guidance

### Source-backed observations

- The directly re-fetched [PostgreSQL integration test guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md) describes PostgreSQL 17 testing, concurrent checkout, the isolated CI job and local environment prerequisites. These are **documented paths**, not a claim that the entire suite was rerun in this review.
- The [JaCoCo coverage baseline guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/JACOCO_COVERAGE_BASELINE.md) explicitly limits the report to the H2 regression selection and gives artifact/reproduction instructions. It does not provide a verified global coverage figure.
- The [SonarCloud PR/CI guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md) describes scanner integration and selected H2 coverage import. It does not itself establish a passed historical Quality Gate.
- Prior [verified Surefire/Sonar evidence](only-film-verified-surefire-sonar-logs.md) records **329 passing selected H2 tests**, artifact creation/upload and a scanner message `ANALYSIS SUCCESSFUL`, but the JaCoCo XML/HTML percentage and the historic server-side Quality Gate outcome were **not independently retrieved or confirmed**.
- The [formally approved Assessment](only-film-assessment.md) notes a **difference between the local JaCoCo test-selection instruction and the H2 workflow's selected tests**. This is a documentation-parity question, **not** a confirmed test failure. `DOC-TESTING` already has approved `Partial / Applicable` coverage and remains decision-unresolved.

### Decision alternatives and threshold

**Consider `PRESERVE` only if the maintainer accepts these existing specialist guides as useful within their **bounded** scope**, without implying full test reproducibility, comprehensive coverage or a passed Quality Gate.

- `PRESERVE`: retain current PostgreSQL, JaCoCo and Sonar documentation with explicit limits, acknowledging any unverified test-selection parity or historical artifacts.
- `ADAPT`: identify a **specific** misleading command, mismatch in selected test sets, missing prerequisite, or reader-discovery weakness and show the exact evidence-backed correction. This would be a separate subsequent action, never an edit under this packet.
- Remain `—`: if accurate reproducibility and guide/workflow selection parity are essential preconditions to a decision and have not been resolved.

**Limit:** this is not a numerical coverage review or verification of Sonar server processing. A successful scanner submission must not be represented as a successful Quality Gate; neither scanner logs nor a transient artifact upload prove the final numbers.

## Reviewer approval and follow-on

A reviewer may approve three decisions independently, with an allowed token and dated reason for each, or preserve `Needs Further Evaluation / —`. A hypothetical default review outcome would leave `DOC-ARCHITECTURE` and `DOC-PROJECT-STATUS` pending while considering `PRESERVE` for `DOC-TESTING` strictly at the above documentary scope. It **is not an authorization**.

On a future **explicit** maintainer approval, record approved `Decision Status`, `Adoption Decision`, `Decision Rationale`, reviewer/date and unchanged evidence boundaries in a **separate PR** to the canonical Assessment, consolidated matrix and this packet. A merge of this preparation PR or a bare `go` does not approve the candidates.

**All 28 State / Applicability pairs remain approved; only 7 previously approved `PRESERVE` decisions are resolved; 21 remain open; Assessment is `In Progress`; Only Film remains strictly read-only.**
