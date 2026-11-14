# Only Film — Adoption Decision review batch 3: Recommended README status, architecture, structure and testing

## Scope and decision boundaries

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable consumer reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-STATUS`, `README-ARCHITECTURE`, `README-REPOSITORY-STRUCTURE`, `README-TESTING` |
| Formally approved State / Applicability | `28/28`, unchanged |
| Formally resolved Adoption Decisions | `5/28` (all existing `PRESERVE`; unchanged) |
| Unresolved Adoption Decisions | `23/28`, including all four reviewed below |
| Assessment | `In Progress` |
| Consumer modifications | `NONE` |

This is a **maintainer-review preparation packet**, not a formal Adoption Decision, an Application plan or a consumer mutation. The [Assessment Template](../assessment-template.md) requires an explicit `Decision Rationale` when a decision moves to `Resolved`; the `Needs Further Evaluation / —` combination remains valid for the others. Existing State/Applicability approvals and source limitations cannot be replaced with presumed functional or operational assurance.

## Summary of decision candidates

| Responsibility | Approved State / Applicability | Decision candidate | Distinguishing gate |
| --- | --- | --- | --- |
| `README-STATUS` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Determine what verifiable current status/maturity statement would help the intended reader, without promoting a historical audit or passing tests to present-day production-readiness evidence |
| `README-ARCHITECTURE` | `Satisfied / Applicable` | **Consider `PRESERVE`** | Existing principal MVC/service/JPA flow is a high-level illustration, not a guarantee that all controllers follow it; consider `ADAPT` only if the current wording materially misleads |
| `README-REPOSITORY-STRUCTURE` | `Satisfied / Applicable` | **Consider `PRESERVE`** | Main project paths are summarized; the nonexhaustive overview should not be forced into a complete file inventory |
| `README-TESTING` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Distinguish verified selected H2/PostgreSQL jobs from unverified broad `./mvnw test`, Selenium, manually triggered suite, and Compose execution |

A `Satisfied` documentary State does **not** force `PRESERVE`, and a `Partial` documentary State does **not** force `ADAPT`. Each `PRESERVE` candidate requires a separate, explicit maintainer choice and rationale; merging this preparation document is **not approval**.

## 1. README-STATUS — proposed unresolved decision

### Evidence

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) shows Java, Spring Boot, PostgreSQL, Flyway and Docker badges, testing/CI information, local Compose-only guidance and a forward-looking evolution list. Technology versions and workflow definitions are **not** a validated current project-status or maturity statement.
- The directly re-fetched [`TECHNICAL_MATURITY_ASSESSMENT.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md) explicitly dates its static evaluation **2026-10-10** and names a different analyzed reference, `9f2a31e927df105d14e3d30d4d8277fa61883deb`. Its academic/portfolio and not-public-production-ready context **must not be promoted as an independently verified status at the newer pinned SHA**.
- The [Framework README-STATUS Component](../../components/readme/status/README.md) calls for meaningful `project_status` and `maturity` information after Hero. It does not authorize inventing a label.
- The earlier [pinned successful H2/PostgreSQL checks](only-film-verified-surefire-sonar-logs.md) have bounded testing significance; they do not establish maintenance cadence, supported deployments, project phase or current maturity.

### Decision threshold

**Default: `Needs Further Evaluation / —`.** `ADAPT` might be worth considering if the maintainer chooses a verifiable, reader-useful status/maturity description with an explicit reference and date. `PRESERVE` could instead be justified by a deliberate acceptance of the existing distributed project-context wording, but that would not create the missing current status claim or silently promote the State from `Partial`.

**Human question:** What status/maturity message, if any, is currently supportable and genuinely useful? The answer must distinguish local demonstration from production readiness, and may remain unresolved pending evidence. **No README status addition is approved here.**

## 2. README-ARCHITECTURE — conditional `PRESERVE`

### Evidence

- The pinned README's `Tecnologías y arquitectura` section describes a **principal** `MVC controller → business service → JPA repository → database` flow and the major domain entities.
- The [Framework README-ARCHITECTURE Component](../../components/readme/architecture/README.md) requests a concise general architecture summary, not a comprehensive codebase dependency map.
- The pinned [historical architecture-maintainability audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) discusses controller/repository boundaries at an earlier reference; the Assessment did not independently establish that any particular exception still exists at the pinned SHA. That older finding is neither a current refactoring mandate nor an exhaustive architecture audit.

### Decision threshold

**Consider `PRESERVE`** if the maintainer accepts the existing principal-flow explanation as a truthful **orientation**, not a categorical assertion that *every* route passes through every layer. `ADAPT` would require a concrete source-backed misleading claim, an audience navigation problem, or a clear readability gain. No new diagram, code refactor or enforcement of a uniform layering pattern is authorized.

**Limits:** no current exhaustive controller-to-repository inventory or all runtime paths checked; the earlier audit's relevance to the pinned SHA is unconfirmed.

## 3. README-REPOSITORY-STRUCTURE — conditional `PRESERVE`

### Evidence

- The pinned README's `Organización del repositorio` tree summarizes `src/main/java/com/demo`, templates/static assets, Flyway migrations, `src/test`, `docs`, `.github/workflows`, `Dockerfile`, `compose.yaml`, and `.env.example`.
- The earlier [Recommended README semantic review](only-film-recommended-readme-semantic-review.md) checked the main pinned paths, but no exhaustive directory-by-directory source inventory was documented in the current review.
- `README-REPOSITORY-STRUCTURE` is `Recommended` in the [Template metadata](../../templates/repositories/backend/metadata.yml); an independently documented Framework Component was not previously established. Missing Component-level documentation in the Framework is **not** a defect in Only Film.

### Decision threshold

**Consider `PRESERVE`** if the maintainer accepts the annotated tree as adequate for repository orientation. It is not supposed to list all files. `ADAPT` is appropriate only after identifying an important missing or misleading path whose presence materially helps a new reader. This review does not create directories, restructure modules or declare full tree accuracy.

**Limits:** file inventory is intentionally simplified, previous checks sampled principal paths and no reader usability validation was performed.

## 4. README-TESTING — proposed unresolved decision

### Evidence

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) includes `./mvnw test`, selected Maven `-Dtest` examples and a workflow table, and **explicitly notes that `tests.yml` is largely manual** and Selenium is not equivalent to the regression jobs run for every PR.
- Direct inspection of pinned [`.github/workflows/tests.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/tests.yml) confirms the suite runs by `workflow_dispatch` and a constrained PR path trigger used to validate Selenium-related workflow configuration; it should not be presented as an unconditional all-PR suite.
- Direct inspection of pinned [`.github/workflows/postgres-migration.yml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/postgres-migration.yml) confirms explicit H2-regression and PostgreSQL job definitions, distinct from the broad local Maven invocation. Earlier [pinned logs](only-film-verified-surefire-sonar-logs.md) report **329 passing tests in the selected H2 job**, plus two successful PostgreSQL jobs; those results do **not** establish a passing complete generic Maven test run, Selenium E2E, or Compose smoke check at the same SHA.
- The approved `Partial / Applicable` evaluation concerns the clarity and sufficiency of documented testing instructions, not a known failed test or a calculated recent overall coverage percentage.

### Decision threshold

**Default: `Needs Further Evaluation / —`.** `PRESERVE` may be accepted as a documentary decision if the maintainer considers the stated workflow differences and caveats sufficient without broader verification. `ADAPT` should be selected only for a specific misleading prerequisite, inaccurate trigger/command description or important reader guidance gap confirmed by source.

**Limits:** clean-checkout `./mvnw test`, Selenium, Compose smoke and other selected paths were not comprehensively executed or independently accepted for this pinned SHA. This review does not request or perform test execution or modify CI.

## Formal maintainer review gate

Each Responsibility needs an independently approved `Decision Status`, `Adoption Decision` and, if `Resolved`, an exact `Decision Rationale`. Proposed reviewer choices are:

1. `README-STATUS`: default **`Needs Further Evaluation / —`** until the intended project-status message is evidenced.
2. `README-ARCHITECTURE`: **consider `Resolved / PRESERVE`**, maintaining the distinction between a principal high-level flow and an exhaustive architecture claim.
3. `README-REPOSITORY-STRUCTURE`: **consider `Resolved / PRESERVE`**, treating the tree as deliberately selective.
4. `README-TESTING`: default **`Needs Further Evaluation / —`** until the maintainer chooses a documented testing-sufficiency criterion.

Once the maintainer **expressly approves** one or more outcomes, a separate approval-record PR may update the Assessment and this packet. Do not infer approvals from merging this preparation PR or an unqualified `go`. All 28 State/Applicability pairs remain approved, all five prior Adoption Decisions remain `PRESERVE`, Assessment remains `In Progress`, and **Only Film is read-only**.
