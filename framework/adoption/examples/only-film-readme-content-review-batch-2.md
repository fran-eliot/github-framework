# Only Film — README content: human review batch 2

## Review context

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned consumer SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Repository Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-FEATURES`, `README-DOCUMENTATION`, `README-FOOTER` |
| Review status | **Recommendation only — no approval recorded for these three Responsibilities** |
| Consumer mutation | `NONE` |
| Overall Assessment | `In Progress` |

This document is a bounded, directly sourced **human review preparation record**. It does not change the current [Assessment](only-film-assessment.md) State/Applicability values, waive evidence limitations, or authorize changes to Only Film. The [consolidated review matrix](only-film-consolidated-review-matrix.md) links this batch; only explicit maintainer decisions can approve the three evaluations.

## Review proposals

| Responsibility | Current working State | Recommended maintainer review outcome | Applicability | Reason |
| --- | --- | --- | --- | --- |
| `README-FEATURES` | `Partial` (unapproved) | **`Satisfied` candidate** | `Applicable` | Role-based capabilities are directly visible and comprehensible; real payments are explicitly excluded elsewhere in the README |
| `README-DOCUMENTATION` | `Partial` (unapproved) | **Retain `Partial` pending navigation review** | `Applicable` | Links to operational guides and CI are real at pinned SHA, but important guides may be omitted from task-oriented README navigation |
| `README-FOOTER` | `Partial` (unapproved) | **Retain `Partial` pending final editorial/legal-context review** | `Applicable` | Credits, project history and cautious license notice exist, but legal permission is not established and the section arrangement may warrant clarification |

The recommendation is about **coverage of each documentary Responsibility**, not whether Only Film is feature-complete, production-ready or legally licensed. Neither missing canonical English headings nor an absent separate documentation index automatically constitute defects.

## 1. README-FEATURES

**Direct evidence at pinned SHA:**

- The [README's `Funcionalidades` section](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) groups key functions by **visitors**, **registered users**, and **administrators**. It names movie/session browsing, registration, login, ticket purchase/reservation, QR tickets, reviews, and administrative operations.
- The same section includes a paragraph on database transactions and locking to guard seat availability. The [README-FEATURES Component](../../components/readme/features/README.md) prioritizes main capabilities rather than implementation detail. This technical sentence is a **possible editorial improvement**, not proof of missing feature coverage.
- In `Seguridad y límites actuales`, the README explicitly says there is **no integrated real payment gateway** and that checkout is a **demonstration purchase flow**. Treating the feature list as evidence of real payment processing would be incorrect.
- The prior [required identity/features semantic review](only-film-required-identity-semantic-review.md) and [Assessment detail](only-film-assessment.md) note that CI is limited evidence rather than end-to-end confirmation of every advertised feature.

**Review interpretation:** `Satisfied / Applicable` is a reasonable **candidate** if the maintainer accepts a concise role-based summary as meeting the Framework responsibility, including the separate demonstration-payment caveat. `Partial / Applicable` remains defensible if the maintainer considers the ambiguous purchase wording or the locking paragraph a material clarity issue.

**Not verified:** no exhaustive feature-by-feature behavioral acceptance; no separate payment-provider integration; no decision to move implementation detail or rewrite a capability claim.

## 2. README-DOCUMENTATION

**Direct evidence at pinned SHA:**

- The README links the [PostgreSQL setup guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md), [PostgreSQL integration-testing guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md), and [security hardening audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md); all **three files were directly fetched at the pinned SHA**.
- The README links `docs/screenshots/` and names six GitHub Actions workflows; the `ticket-regression.yml` and `compose-smoke.yml` workflow **files were directly fetched** at the pinned SHA. File existence is not a successful workflow execution.
- `Organización del repositorio` explains `src/main`, `src/test`, `docs/`, `.github/workflows/` and Docker-related files.
- The [README-DOCUMENTATION Component](../../components/readme/documentation/README.md) states that important documents should be grouped, with example categories Architecture, ADR, Roadmap, API, and Deployment. These examples are not a mandatory exhaustive list for the consumer.

**Review interpretation:** the existing navigation **partly fulfills** the Responsibility through useful contextual links; a separate `## Documentation` index is not automatically required. Keep `Partial / Applicable` as a conservative proposal unless a reviewer concludes the existing distributed pathways are sufficiently clear and complete for the intended audience. If `Satisfied` is selected, that judgment should not imply an exhaustive internal-link health audit.

**Not verified:** link-by-link target validation throughout the README, all potentially important docs in the consumer tree, freshness of each guide, and a user journey test. A separate documentation index is **not authorized**.

## 3. README-FOOTER

**Direct evidence at pinned SHA:**

- `Origen, créditos y evolución` in the [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) credits four original contributors, links the [academic source project](https://github.com/certidevs/g1_testing), and distinguishes subsequent maintenance in `fran-eliot/only_film` from sole authorship of the original work.
- The `Próximas líneas de evolución` section lists future work — REST API, real payment-provider integration, observability, deployment automation, maintainability — **as possible future enhancements**, not implemented functionality.
- A final bold `Licencia` notice explicitly says the README **does not establish an additional license**. This preserves legal uncertainty rather than granting reuse permission.
- The [README-FOOTER Component](../../components/readme/footer/README.md) permits license, acknowledgments, related links and contact information; it does **not** require every optional element.

**Review interpretation:** the original credits, external-source attribution and license caveat all serve Footer purposes. `Partial / Applicable` remains a prudent working recommendation where the maintainer has not approved clarity/completeness of the ending section structure or reviewed legal context. `Satisfied / Applicable` is a reasonable alternative only if the existing closing material is judged adequate for the project's purpose **without asserting legal permission**.

**Not verified:** external contributor intellectual-property permissions, legal license status, attribution completeness beyond the directly visible README, external link liveness. No new license or rights claim should be inferred.

## Maintainer acceptance gate

For each responsibility, the maintainer must **explicitly approve** both State and Applicability. Recommended default options:

1. `README-FEATURES = Satisfied / Applicable` — only if role-based feature summary and payment caveat are accepted as adequate; otherwise retain `Partial / Applicable`.
2. `README-DOCUMENTATION = Partial / Applicable` — retaining scope and link-inventory uncertainty, or approve `Satisfied / Applicable` with a concrete documentary threshold.
3. `README-FOOTER = Partial / Applicable` — keeping attribution and license clarity as open qualifications, or approve `Satisfied / Applicable` if the present closing text is considered sufficiently informative.

**Merging a PR containing this packet does not approve these entries.** Record any explicit maintainer decision in the main Assessment and consolidated matrix in a separate review PR with its actual approval date. Until then, the working values remain `Partial / Applicable` for all three; keep `Decision Status: Needs Further Evaluation`, `Adoption Decision: —` and overall `Assessment: In Progress`.

## Scope and evidence boundary

The immutable consumer baseline remains `28d75a50e0a178954dd46acc23300d9dd327843c`. The limited source fetches above establish content/file presence, **not** browser UX, correct operation of every feature, successful workflow runs, full repository link validity or legal reuse rights. No proposed change to the Only Film consumer, release, CI settings, workflows, licenses or repository access policy is authorized.
