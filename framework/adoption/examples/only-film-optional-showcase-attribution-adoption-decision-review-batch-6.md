# Only Film — Adoption Decision review batch 6: Optional showcase, attribution and license communication

## Scope and controlled baseline

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable consumer reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-DEMO`, `README-AUTHOR`, `README-HIGHLIGHTS`, `README-LICENSE` |
| Formally approved State / Applicability | `28/28`, unchanged |
| Formally resolved Adoption Decisions | `11/28`: ten `PRESERVE`, one `OMIT`; Author and Highlights approved 2026-11-14 |
| Still unresolved | `17/28`, including `README-DEMO` and `README-LICENSE` in this packet |
| Assessment | `In Progress` |
| Consumer modifications | `NONE` |

This packet is **review preparation only**. It does not approve any new Adoption Decision, change a previously approved State/Applicability classification, establish the legal ownership of the academic code, verify runtime behavior or authorize implementation in Only Film. An explicit, independent maintainer decision and rationale must precede any `Resolved` transition.

## Formal maintainer Adoption Decision outcome — 2026-11-14

The Only Film maintainer **expressly approved `README-AUTHOR = PRESERVE` and `README-HIGHLIGHTS = PRESERVE`** and expressly retained the other two Adoption Decisions unresolved:

| Responsibility | Decision Status | Adoption Decision | Approved rationale / evidence limits |
| --- | --- | --- | --- |
| `README-DEMO` | `Needs Further Evaluation` | `—` | Screenshots have not been independently visually inspected for accuracy/freshness; complete pinned-SHA Docker Compose startup and any public demo are not established |
| `README-AUTHOR` | `Resolved` | `PRESERVE` | Retain balanced academic-team credits and distinguish later maintenance; full contributor attribution, ownership, permissions and licensing rights are **not** established |
| `README-HIGHLIGHTS` | `Resolved` | `PRESERVE` | Retain informative distributed features/security differentiators, explicitly limited to simulated payment and no production security certification; full runtime feature verification is **not** established |
| `README-LICENSE` | `Needs Further Evaluation` | `—` | Existing non-grant notice and empty POM license metadata do not prove source ownership, contributor permissions, reuse rights or an authorized license |

**Formal review date: 2026-11-14.** The immutable consumer evidence baseline remains `28d75a50e0a178954dd46acc23300d9dd327843c`. The original **28 formally approved State / Applicability pairs are unchanged**; no `Partial` or `Satisfied` evaluation is silently revised by the new decisions.

**Authorization boundary:** Assessment remains `In Progress`; **11/28 Adoption Decisions resolved (10 `PRESERVE`, 1 `OMIT`), 17 unresolved**. Only Film remains read-only. No screenshot modification, Compose execution, security certification, attribution alteration, license grant, deployment or other Application/Integration action is authorized.

The original candidate suggestions below are **preapproval review history**, not the current formal decision state.

## Decision candidates

| Responsibility | Approved State / Applicability | Proposed review posture | Principal open boundary |
| --- | --- | --- | --- |
| `README-DEMO` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | The screenshot references are present but their pixel contents and freshness were not independently visually audited, and pinned Docker Compose execution was not verified |
| `README-AUTHOR` | `Satisfied / Applicable` | **Consider `PRESERVE`** | Existing academic team credits and later-maintenance distinction serve attribution; this is **not** a complete contribution or intellectual-property audit |
| `README-HIGHLIGHTS` | `Satisfied / Applicable` | **Consider `PRESERVE`** | Valuable differentiators already appear in Features and Security; no full feature, payment, security or production-readiness guarantee is established |
| `README-LICENSE` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Existing cautious license notice is not a rights determination or an open-source grant; stronger wording or a license file would require appropriate authority |

`Partial` does not automatically mean `ADAPT`; `Satisfied` does not automatically mean `PRESERVE`. A conditional preservation decision would only retain the presently evidenced documentary role, not elevate the existing evaluation or settle unknown facts.

## 1. README-DEMO — screenshots are not a verified hosted or reproducible demo

### Evidence at the pinned reference

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) embeds references to four UI screenshots: movie listing (`cartelera.png`), movie detail (`pelicula.png`), seat selection (`sesion.png`) and purchase/QR ticket (`compra-qr.png`) under `docs/screenshots/`.
- The previous [Optional Showcase semantic review](only-film-optional-showcase-semantic-review.md) confirms the screenshot **paths/presence**, not full visual content inspection, visual freshness, user-facing representativeness or any pixel-level property of those screenshots.
- The README's `http://localhost:8080/movies` is a **local address**, not a public web demonstration. The [pinned Compose evidence review](only-film-compose-evidence-gap.md) records no independently verified clean pinned-SHA Compose smoke run among the inspected checks. Absence of an observed run does **not** mean Compose failed.

### Review choices

**Default `Needs Further Evaluation / —`.** A future `PRESERVE` could approve the existing **screenshot-based** documentary illustration for a portfolio audience, provided that its limited evidence scope is acceptable. An `ADAPT` would require a specific observed misleading screenshot/caption or verified onboarding/demo deficiency, not an inferred requirement for a public deployment.

**Not established:** visual fidelity or recency of screenshots, successful pinned-SHA local Compose demonstration, an online demo, or complete end-to-end behavior. This packet does not publish a demo, run Compose, or modify images.

## 2. README-AUTHOR — conditional `PRESERVE` of balanced attribution

### Evidence at the pinned reference

- The README's `Origen, créditos y evolución` names and links **four academic collaborators**, links [the original certidevs/g1_testing repository](https://github.com/certidevs/g1_testing) and separately describes subsequent technical evolution under `fran-eliot/only_film`.
- The directly fetched [README-AUTHOR Component](../../components/readme/author/README.md) asks for author/team information, potentially including name, GitHub, LinkedIn and website, **without requiring every optional link** or a distinct `Author` heading.
- The README explicitly avoids exclusive authorship of the original collaborative project. No comprehensive review of individual historical contributions, complete credit coverage, reuse permission or ownership has been established by this Assessment.

### Review choices

**Consider `Resolved / PRESERVE`** of the **existing balanced attribution** because it already meets the reader-facing team identification purpose of this Optional Responsibility. This would retain the approved `Satisfied / Applicable` classification and all rights/credit-completeness limitations.

`ADAPT` should require a **specific** verified name, link, factual error or reader need. Neither `PRESERVE` nor any other decision here constitutes intellectual-property ownership verification, permission to relicense or permission to alter the original collaborators' attribution.

## 3. README-HIGHLIGHTS — conditional `PRESERVE` of existing distributed differentiators

### Evidence at the pinned reference

- The README describes transactional ticket checkout, prevention of duplicate seat sales, role-based access, review ownership checks, restricted image handling and PostgreSQL/Flyway support across `Funcionalidades` and `Seguridad y límites actuales`.
- The same README says **payment checkout is simulated**, with **no integrated real payment provider**, and does not claim a complete security audit or hardened production deployment.
- The previous [selected Surefire/Sonar evidence](only-film-verified-surefire-sonar-logs.md) supports a selected H2 regression and other specific CI checks but is **not** a complete live feature walkthrough, penetration test, visual review or production-readiness validation.
- The previous [Optional Showcase semantic review](only-film-optional-showcase-semantic-review.md) found no independently established dedicated `README-HIGHLIGHTS` Component; Template Optional metadata does not alone require a new section or repeated content.

### Review choices

**Consider `Resolved / PRESERVE`** to avoid duplicate showcase prose: Features and Security already communicate meaningful implementation traits with important safety and scope caveats. A new `Highlights` heading is not itself evidence of reader value.

`ADAPT` should identify a concrete factual or navigability problem, supported by an appropriate source. `PRESERVE` does **not** certify actual payment processing, exhaustive functional behavior, robust production security or production deployment.

## 4. README-LICENSE — preserve the uncertainty, not presume legal authorization

### Evidence at the pinned reference

- The README ends with a cautious academic-origin license notice, directs readers toward the original project and project documentation for conditions, and explicitly says **the README does not establish an additional license**.
- The pinned [`pom.xml`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) contains a blank `<licenses><license/></licenses>` entry. That is **not** an affirmative grant, and does not establish distribution terms.
- The earlier [Optional Governance semantic review](only-film-optional-governance-semantic-review.md) and the approved Assessment report that no root `LICENSE`, `LICENCE` or `COPYING` was identified in bounded filename checks; those checks do **not** exhaust legal rights sources or original-contributor permissions.
- The original collaborative contribution and later repository maintenance are different facts. The existence of a GitHub repository, credits, PR history or README does not establish unilateral rights to license or relicense all contributions.
- `README-FOOTER = PRESERVE` was approved earlier **only as cautious documentary footer wording** and does **not** resolve this separate `README-LICENSE` Responsibility.

### Review choices

**Default `Needs Further Evaluation / —`.** A bounded `PRESERVE` could be considered **only** for retaining the existing non-granting, uncertainty-aware notice as written. This would **not** resolve underlying legal status or imply a license grant. `ADAPT`, `ADD` or any stronger permissions statement requires independently sufficient rights evidence and maintainer authorization.

Do not fabricate a license, infer the original project's license terms, conclude that reuse is permitted, or modify Only Film as part of this preparation.

## Formal maintainer review gate

For each Responsibility, the maintainer may expressly approve one valid, reasoned Adoption Decision or retain `Needs Further Evaluation / —`. The initial recommended bundle is:

- `README-DEMO = Needs Further Evaluation / —` (unverified screenshot visuals, pinned Compose behavior and desired demo sufficiency).
- `README-AUTHOR = PRESERVE` (existing balanced academic attribution, **without legal/complete-credit claims**).
- `README-HIGHLIGHTS = PRESERVE` (existing useful differentiators without duplicate section, **without a full-feature/security guarantee**).
- `README-LICENSE = Needs Further Evaluation / —` (legal/reuse uncertainty is not determined by the non-grant notice).

A later **separate PR**, only after express maintainer approval, should update this packet, the [canonical Assessment](only-film-assessment.md), and the [consolidated matrix](only-film-consolidated-review-matrix.md). Approval must distinguish `Decision Status` and `Adoption Decision` from the already formally approved `State / Applicability`.

**Historical preparation boundary:** Merging the preparation PR did not approve these decisions. The later **express maintainer approval on 2026-11-14** formally resolved `README-AUTHOR` and `README-HIGHLIGHTS` as `PRESERVE`. All 28 classification pairs remain approved; eleven Adoption Decisions are now resolved (ten `PRESERVE`, one `OMIT`), seventeen remain unresolved; Assessment remains `In Progress`; Only Film remains read-only.
