# Only Film — README status, repository structure and roadmap: human review batch

## Assessment boundary

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned assessment SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-STATUS`, `README-REPOSITORY-STRUCTURE`, `README-ROADMAP` |
| Review status | **Proposals only; the maintainer has not approved these three in this packet** |
| Approved State / Applicability pairs before review | **17/28** |
| Assessment | `In Progress` |
| Resolved Adoption Decisions | `0` |
| Consumer mutation | `NONE` |

This review uses directly fetched files at the immutable consumer SHA and the corresponding Framework guidance. Earlier maturity and F3 reports are considered **historical sources**, not verified present-day status. A merged review packet is not approval and cannot authorize changes to Only Film.

## Review recommendations

| Responsibility | Current unapproved State / Applicability | Recommended maintainer review candidate | Evidence limit |
| --- | --- | --- | --- |
| `README-STATUS` | `Partial / Applicable` | **Retain `Partial / Applicable`** | Version badges and earlier maturity findings are not a current `project_status` / `maturity` declaration |
| `README-REPOSITORY-STRUCTURE` | `Partial / Applicable` | **Consider `Satisfied / Applicable`** | A useful explicit tree identifies principal source, test, resource, automation and Docker paths; not a full file inventory |
| `README-ROADMAP` | `Partial / Applicable` | **Retain `Partial / Applicable`** | Future possibilities are declared accurately as prospective, but no dated set of next phases or verified current planning state was established |

Each State is a **documentary coverage** judgment rather than proof of running features, current project maturity or a requirement to create a new document.

## 1. README-STATUS — `Partial / Applicable` candidate

### Direct pinned evidence

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) has technology/version badges (Java 25, Spring Boot 4.0.5, PostgreSQL 17, Flyway and Docker Compose), which should not be construed as badges for current operational health, maintenance activity or project maturity.
- Its `Pruebas y CI` text describes different automated and manual checks, but individual CI results and described workflow triggers do not establish an overall maintenance status, deployment readiness or maturity assessment.
- The directly fetched [`docs/TECHNICAL_MATURITY_ASSESSMENT.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md) is dated **2026-10-10** and evaluates **earlier commit `9f2a31e927df105d14e3d30d4d8277fa61883deb`**, not the pinned SHA. Its academic/portfolio and production-readiness language cannot be silently carried forward as current.
- The [Framework README-STATUS Component](../../components/readme/status/README.md) requires the concepts `project_status` and `maturity`, and positions the Status block immediately after the Hero. The inspected pinned README does not present a comparable current declaration there.

### Interpretation and reviewer gate

Retaining `Partial / Applicable` is supported as a **review proposal**: status-related context is present, but a current, evidence-backed project-status/maturity statement is not. The reviewer may revise it after identifying a maintained equivalent source and agreeing the scope. The earlier maturity verdict must not be treated as a current defect list, production-readiness certification or proof that development is active/inactive.

**Unverified:** actual current milestone, maturity level at the assessed SHA, maintained status designation and deployment posture. No new status text or badge is authorized.

## 2. README-REPOSITORY-STRUCTURE — `Satisfied / Applicable` candidate

### Direct pinned evidence

- The README has an explicit `Organización del repositorio` tree showing `src/main/java/com/demo`, `src/main/resources/templates`, `src/main/resources/static`, `src/main/resources/db/migration`, `src/test/java/com/demo`, `docs/`, `.github/workflows/`, `Dockerfile`, `compose.yaml` and `.env.example`.
- The text explains these paths' broad functions (controllers, services, repositories, entities, security, Thymeleaf views, static assets, migrations, tests, documentation, CI and Docker configuration).
- [`TPL-BACKEND` `0.1.0` metadata](../../templates/repositories/backend/metadata.yml) classifies `README-REPOSITORY-STRUCTURE` as **Recommended**. In the earlier Assessment record, an independent Component specification for this Responsibility was not identified; this is a Framework catalog coverage issue, not evidence that the consumer layout is wrong.
- This pass directly re-fetched the README's displayed tree but **did not run an exhaustive pinned directory-by-directory tree inventory**. Existing earlier Framework source review confirmed principal paths; that prior check remains the provenance for path existence.

### Interpretation and reviewer gate

A concise orientation tree is an effective fulfillment of the Responsibility. `Satisfied / Applicable` is therefore a reasonable **candidate** if the maintainer accepts that a nonexhaustive but useful map of major folders meets the audience's navigation needs. The present `Partial / Applicable` proposal remains unapproved until then, and may be retained if a specific important omission or misleading path is demonstrated.

**Unverified:** exhaustive directory coverage, file-by-file accuracy and usefulness for every potential contributor. No new Framework Component or consumer restructuring is authorized.

## 3. README-ROADMAP — `Partial / Applicable` candidate

### Direct pinned evidence

- The [pinned README's `Próximas líneas de evolución`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) names potential REST API, real payments, observability, automated deployment and maintainability improvements. It explicitly distinguishes possible future directions from **implemented capabilities**.
- The directly fetched [`docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) has historical base `df63353564485eb6d2d60c982032e5d3c4facbf2` (October 2026) and lists F3 initiatives, but its presence does not establish the remaining priorities or completion states at the later pinned SHA.
- The [README-ROADMAP Component](../../components/readme/roadmap/README.md) asks for a short summary of **upcoming phases**, not duplication of a detailed planning document. The pinned README offers concise future possibilities, but no confirmed ordering, status by initiative or phase dates.

### Interpretation and reviewer gate

`Partial / Applicable` is a defensible documentary review candidate when the desired roadmap communicates prioritized **next phases**, not merely possible ideas. `Satisfied / Applicable` could be defensible if the maintainer judges a short, clearly prospective list sufficient for this portfolio project's Optional Responsibility, without pretending those items have been committed or scheduled.

**Unverified:** current F3 tickets and phase completion, relative priority, delivery schedule and next actual milestone. No feature commitment, public deployment or roadmap modification is authorized.

## Human review gate and nonapproval statement

The maintainer may explicitly approve the proposed `README-STATUS: Partial / Applicable`, `README-REPOSITORY-STRUCTURE: Satisfied / Applicable` and `README-ROADMAP: Partial / Applicable` or revise any State using the documented criteria. Every accepted State and Applicability must be formally recorded with a date **in a separate approval PR**.

**Merging this review batch does not approve any assessment value.** All three remain `Decision Status: Needs Further Evaluation` and `Adoption Decision: —`. The main Assessment remains `In Progress` and the 17 prior formal approvals are unaffected. Only Film must stay read-only until a distinct authorized Adoption Decision.
