# Only Film — API and references contract-scope review

## Purpose and boundaries

| Field | Value |
| --- | --- |
| Consumer repository | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Assessed pinned reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Framework Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `DOC-API`, `DOC-REFERENCES` |
| Status | **Both State and Applicability pairs explicitly approved by the Only Film maintainer on 2026-11-14; dated outcome below** |
| Formal evaluation approvals after maintainer review | `28/28` |
| Assessment status | `In Progress` |
| Adoption Decisions | `0` resolved |
| Consumer mutation | `NONE` |

This record deliberately **separates the contractual State from Applicability** and scopes a documentation Responsibility to an actual supported reader/consumer use case. A `Not Applicable` proposal does **not** stand in for a missing State, authorize changes, prove repository-wide absence, or automatically mean a documentation gap is a defect.

## Formal maintainer approval outcome — 2026-11-14

The Only Film maintainer **expressly approved each independent State and Applicability classification**:

| Responsibility | Approved State | Approved Applicability and its precise scope |
| --- | --- | --- |
| `DOC-API` | `Missing` | `Not Applicable` — documentation for a **currently supported public/programmatic API contract** only |
| `DOC-REFERENCES` | `Partial` | `Not Applicable` — a **standalone centralized external-technical-reference catalog** only |

All source limitations remain intact: the seven-controller sample does not prove the absence of every programmatic route or integration, and the sampled documentation does not prove there are no other external references. In-context source citations, attribution, validity and maintenance **remain relevant**; no general references exemption is implied. Missing/Partial are independent contractual States, **not** authorizations to create a REST API, OpenAPI artifact or references catalog.

**Boundary:** the Assessment remains `In Progress`; **all 28 Adoption Decisions remain `—`**, all 28 Decision Status values remain `Needs Further Evaluation`, no legal/rights assertions are made, and **no edits to Only Film** are authorized. The preapproval proposals and alternative scope discussions below remain as dated historical preparation, not current unapproved classifications.

## Candidate outcomes and discriminating questions

| Responsibility | Existing unapproved proposal | Candidate for explicit maintainer consideration | Exact scope |
| --- | --- | --- | --- |
| `DOC-API` | `Missing / Not Applicable` | **Retain `Missing / Not Applicable` as separate contractual values** | Documentation of a **currently supported public/programmatic API contract**, not ordinary MVC HTML routes nor a future REST feature |
| `DOC-REFERENCES` | `Partial / Not Applicable` | **Retain `Partial / Not Applicable` as separate contractual values** | A **standalone centralized external-technical-reference catalog**, not the usefulness, validity or maintenance of source links in existing documents |

The paired values are not contradictory: `State` identifies observed coverage of the specifically scoped documentary deliverable; `Applicability` decides whether that deliverable is needed by this consumer **at the pinned commit**. Neither `Missing` nor `Partial` implies a need to implement a nonapplicable deliverable. Because `DOC-REFERENCES` has an explicitly wider component purpose involving meaningful source identification, a maintainer may instead assess its broader contextual-linking Responsibility as `Applicable`.

## 1. DOC-API — proposed `Missing / Not Applicable`, limited to a supported programmatic API

### Direct and previously recorded evidence

- The [pinned Only Film README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describes an MVC/Thymeleaf, server-rendered application and lists an `API REST` among **possible future enhancements**, not as an implemented public interface.
- This pass fetched [`MovieController.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/MovieController.java) and [`ReviewController.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/ReviewController.java) at the pinned reference. Both declare Spring `@Controller`; neither declares `@RestController`, `@ResponseBody` or `ResponseEntity` in the fetched file. An `org.springframework.web.bind.annotation.*` import alone is **not** a declared REST endpoint.
- The earlier [targeted pinned controller spot check](only-film-optional-contract-spotcheck.md) directly inspected **seven** MVC controller paths (`MovieController`, `RoomController`, `SessionController`, `TicketController`, `UserController`, `AuthController`, `ReviewController`); their reviewed mappings returned page views or redirects, without those explicit REST/response-body indicators. The seven-file finding remains **previous review evidence**. This pass re-fetched two of them, **not** the full seven.
- Earlier source/path checks did not identify an OpenAPI/Swagger-named artifact. That is only a filename-bound observation, not a comprehensive API-contract inventory.
- Neither the inspected files nor the README establish **real external API consumers** or an integration contract. An MVC application's HTML routes are HTTP endpoints, but do not automatically require REST/OpenAPI documentation.

### Evaluation

**Candidate State `Missing`:** no maintained public/programmatic API contract documentation was identified **within the inspected evidence**, as distinct from the ordinary web application documentation. This is an absence-of-observed-documentation classification, **not** a claim that no route or integration exists in the entire repository.

**Candidate Applicability `Not Applicable`:** the README presents REST as future work and reviewed controllers are MVC-first. For the **present, supported, external programmatic API documentation purpose** there is no established consumer/contract requiring its adoption. This is not an assertion that the future REST feature will never exist.

**Required maintainer gate:** confirm the intended API consumers. If the pinned project actually offers a supported JSON/REST/integration contract, change Applicability to `Applicable` and reassess documentation coverage using that concrete contract. If uncertainty is material after bounded review, `Uncertain` is an allowed Applicability value and must be accompanied by a targeted remaining-evidence criterion.

**Limits:** no recursive Java tree, all possible filter/functional routes, webhook/integration surface or end-to-end content negotiation inventory was completed. Do not turn a seven-file review into a repository-wide no-API theorem. No REST endpoint, OpenAPI document, or consumer change is authorized.

## 2. DOC-REFERENCES — proposed `Partial / Not Applicable` for a standalone catalog

### Direct and previously recorded evidence

- The [Framework DOC-REFERENCES Component](../../components/documentation/references/README.md) says its primary purpose is to make **relevant external sources** discoverable and useful, especially when several standards, official sources and specifications recur across documents. It explicitly states that **no centralized list is necessary** if there are few sources or links work better at their point of use; no register should be added for formality.
- The pinned [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) directly inspected in this pass contains contextual links to project documentation, GitHub Actions, the original academic source and contributor profiles, among other resources. Many of these are **navigation, provenance or tooling links**, not a bibliography of independent standards. Link presence alone is not a complete external-reference catalog.
- This pass also fetched pinned [`POSTGRESQL_SETUP.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) and [`DEPENDENCY_MAINTENANCE.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md). Both describe primary technologies and operational practices without a Markdown absolute-link `[label](https://...)` in these two files; plain text mentioning PostgreSQL, Maven, Dependabot or SonarCloud does **not** establish an obligation to provide external links for each.
- The earlier [targeted references spot check](only-film-optional-contract-spotcheck.md) examined a **seven-file** pinned Markdown sample. No recurring standards/specifications corpus justifying a new central catalog was established **within that sample**. A complete document and link audit, links' live health, relevance and source authority were not checked.

### Evaluation

**Candidate State `Partial`:** links and project/source attribution exist **in context**, while no comprehensive organized standalone external-reference collection was verified. This is a documentary-coverage observation within the **narrow standalone-catalog scope**, not a finding that source citation is defective or that links are broken.

**Candidate Applicability `Not Applicable`:** a **centralized external-reference catalog** has no demonstrated reader need based on the sampled documents, and the Framework Component explicitly discourages unnecessary duplication. That does **not** make in-place technical source references nonapplicable or dispensable.

**Alternative:** if the maintainer interprets `DOC-REFERENCES` as a **broader obligation to provide relevant sources wherever readers need them**, `Applicable` may be more accurate. The State should then be judged as `Satisfied` or `Partial` from the quality/relevance of **actual in-place references**, not from absence of a `REFERENCES.md` file.

**Required maintainer gate:** explicitly decide whether the scoped Responsibility concerns the centralized catalog (candidate `Not Applicable`) or ongoing reference quality in context (candidate `Applicable`). Consider a sample of authoritative external standards and intended reader needs; do not add a catalog without evidence of value.

**Limits:** full project-wide link inventory, link liveness, external source relevance, duplicate analysis and consumer expectations were not verified. `Partial / Not Applicable` is a provisional, narrow interpretation rather than a general recommendation to stop maintaining technical references. No new references index or edits to Only Film are authorized.

## Final formal-approval gate

For these last two entries, the maintainer must explicitly approve or revise **both** fields, with the chosen **scope**:

1. `DOC-API`: `State: Missing`; `Applicability: Not Applicable` **only for a currently supported public/programmatic API contract**, with nonexhaustive entry-point verification expressly preserved.
2. `DOC-REFERENCES`: `State: Partial`; `Applicability: Not Applicable` **only for a standalone centralized external-technical-reference catalog**, leaving in-context citations and source attribution outside that narrow nonapplicability judgment.

The maintainer's acceptance must record a date and source SHA in the Assessment and matrix by a **separate formal-approval PR**. Merging this preparation record is **not** formal approval. If these two State/Applicability pairs are subsequently approved, the Assessment can show **28/28 formally reviewed evaluations**, but the **overall Assessment remains `In Progress`** until its independent completion criteria and all Adoption Decisions are resolved through the agreed authorization process. The review itself does not select any `PRESERVE`, `ADAPT`, `ADD`, `ACCEPT` or `OMIT` action.

**No consumer modifications, public API invention, reference catalog, deployment, legal assertion or implementation authorization follow from this review.**
