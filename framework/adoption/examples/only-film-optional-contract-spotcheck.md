# Only Film — Targeted Optional Responsibility Source Spot Check

## 1. Scope and provenance

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned consumer SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | [TPL-BACKEND 0.1.0](../../templates/repositories/backend/metadata.yml) |
| Responsibilities | `README-CONTRIBUTING`, `DOC-API`, `DOC-DIAGRAMS`, `DOC-REFERENCES` |
| Method | Read-only GitHub file retrieval **at the pinned commit** plus bounded default-branch code searches |
| Assessment status | `In Progress`; no State or Applicability approval |
| Consumer mutation | `NONE` |

This is an evidence extension to the [28-Responsibility working Assessment](only-film-assessment.md), **not** a complete repository-wide inventory or adoption decision. Path-specific negatives and default-branch search results must not be generalized to all files in the pinned commit.

## 2. README-CONTRIBUTING

The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) includes development, Maven, test/CI and repository-organization instructions. Those support technical onboarding but do **not** establish who may contribute, how a PR is reviewed or whether external contributions are welcomed.

Three exact pinned paths were fetched, and each returned `404 Not Found`:

| Exact path | Result at pinned SHA |
| --- | --- |
| `CONTRIBUTING.md` | Not found |
| `.github/CONTRIBUTING.md` | Not found |
| `.github/PULL_REQUEST_TEMPLATE.md` | Not found |

A code-search query `CONTRIBUTING` on the **mutable default branch** returned no hits. That search is index-dependent and does not independently inventory the pinned Git tree. Alternate policy locations and maintainer practice have not been verified.

**Reviewer still needs:** the actual contribution-acceptance policy and any maintained equivalent documentation. `State` remains **unselected** and `Applicability: Uncertain`.

## 3. DOC-API

The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describes a Spring MVC/Thymeleaf web application and mentions `API REST` only among possible future improvements.

Direct inspection of pinned [`ReviewController.java`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/ReviewController.java) confirms `@Controller`, `@GetMapping`, `@PostMapping`, Spring `Model`, and returned Thymeleaf view names / redirect strings. That file has **no** `@RestController` or `@ResponseBody` declaration. This is evidence about **one controller**, not all consumer endpoints.

Default-branch searches for `@RestController` and `@ResponseBody` returned no indexed hits. These are mutable-branch/index-limited negative checks; they do not establish complete absence of JSON responses, HTTP interfaces, or integration contracts at the pinned commit.

**Reviewer still needs:** a bounded inventory of relevant pinned controllers plus the intended API consumers. Do not treat future REST aspirations as implemented. `State` remains **unselected** and `Applicability: Uncertain`.

## 4. DOC-DIAGRAMS

The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) contains a **textual** architecture sequence: `Controlador MVC → servicio / reglas de negocio → repositorio JPA → base de datos`, alongside **UI screenshots**, not proven technical diagrams.

Four additional pinned Markdown files were fetched and searched for the explicit text indicators `mermaid`, `plantuml`, `draw.io`, and Markdown image references ending in `.png`, `.svg`, `.jpg` or `.jpeg`:

| Sampled document | Selected indicators found |
| --- | --- |
| [POSTGRESQL_SETUP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) | None |
| [F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) | None |
| [SECURITY_HARDENING_AUDIT.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md) | None |
| [DEPENDENCY_MAINTENANCE.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md) | None |

Default-branch code searches for `mermaid`, `drawio`, and `plantuml` returned no hits; these searches have the same indexing and branch limitations. Other pinned Markdown files and assets, alternative markup, links, and generated diagrams were **not exhaustively checked**.

**Reviewer still needs:** assess whether a maintained technical diagram serves a concrete need and, if necessary, inspect other pinned documents. `State` remains **unselected** and `Applicability: Uncertain`.

## 5. DOC-REFERENCES

The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) links workflows, project documentation, the academic source repository and GitHub Actions. The four sampled specialist Markdown documents above contained no external links in the selected **Markdown absolute-link form** `[label](https://...)` or `[label](http://...)`; this does **not** rule out relative links, inline URLs, useful context-specific references or other files.

The [DOC-REFERENCES Component](../../components/documentation/references/README.md) explicitly permits references to remain near their use when a separate index would not help. This spot check did not verify the full external-link inventory, relevance, freshness or authority.

**Reviewer still needs:** decide which external sources the intended audience requires and whether contextual linking suffices. `State: Partial` remains **proposed, unapproved**; `Applicability: Uncertain`.

## 6. Evidence boundaries and handoff

| Responsibility | Confirmed in this bounded check | Not established |
| --- | --- | --- |
| `README-CONTRIBUTING` | Three exact pinned paths absent; README onboarding inspected | Collaboration policy or all equivalent sources |
| `DOC-API` | One pinned MVC view controller inspected; REST described as future work in README | All pinned controllers and actual API consumers |
| `DOC-DIAGRAMS` | Four pinned documents lack selected diagram indicators | All embedded diagrams and whether any are needed |
| `DOC-REFERENCES` | README contains contextual links; four documents sampled for absolute Markdown links | Complete and useful external-reference coverage |

The spot check **does not** resolve the three unselected States, the four open Applicability judgments, or any Adoption Decision. No additional tests, external deployment, security audit, or consumer modification was performed.

## 7. Pinned MVC controller expansion

A follow-up file-by-file inspection fetched the seven controller source paths below **directly from the pinned SHA** `28d75a50e0a178954dd46acc23300d9dd327843c`. Each inspected class declares `@Controller`; the mapped handler methods observed in these classes return `String` view names or redirect targets, and none of these seven files declares `@RestController` or `@ResponseBody`.

| Pinned controller | Selected mapped functions inspected | Finding |
| --- | --- | --- |
| [MovieController.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/MovieController.java) | Home, listing/detail, editing and deactivate handlers | MVC views and redirects |
| [RoomController.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/RoomController.java) | Room listing/detail, create/edit, deactivate | MVC views and redirects |
| [SessionController.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/SessionController.java) | Session listing/detail, create/edit, deactivate | MVC views and redirects |
| [TicketController.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/TicketController.java) | Ticket listing/detail, checkout and purchase handlers | MVC views and redirects |
| [UserController.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/UserController.java) | Administration and profile handlers | MVC views and redirects |
| [AuthController.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/AuthController.java) | Registration/login handlers | MVC views and redirects |
| [ReviewController.java](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/src/main/java/com/demo/controller/ReviewController.java) | Review list/detail/create/edit/delete | MVC views and redirects |

**Scope of negative evidence:** direct `fetch_file` results establish only that these seven inspected source files do not explicitly declare `@RestController` or `@ResponseBody`. No recursive pinned Git tree was enumerated and other controllers, filters, functional routing, content negotiation, webhooks and static resources were not audited. The earlier default-branch searches remain **mutable-branch/index-limited** observations, not pinned repository-wide results.

The README still frames a REST API as a future option. Taken together, the reviewed source supports an **MVC-first consumer interpretation**, not an assertion of a public REST API. An API documentation Responsibility may be `Not Applicable` depending on the intended consumer, but the owner/reviewer must explicitly decide the scope and contractual State; **no values are approved or altered**.

**Potential next verification:** compare the complete pinned Java controller directory against the seven filenames above and inspect any remaining entry points. Then ask whether programmatic integration is an intended supported interface at this revision. Do not recommend an OpenAPI document without an actual, identified contract.

## 8. Expanded pinned documentation sample — contribution guidance and diagrams

The following **nine exact Markdown files** were fetched directly at the pinned SHA and inspected for contribution-policy language and explicit diagram indicators. This expands, but does **not** exhaust, the previous four-document spot check.

| Pinned document | Explicit diagram indicator (Mermaid/PlantUML/draw.io, common diagram syntax, or embedded Markdown image) |
| --- | --- |
| [README.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) | Four embedded `docs/screenshots/` **UI screenshots**, not identified as technical diagrams |
| [POSTGRESQL_SETUP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) | None in the selected checks |
| [POSTGRESQL_INTEGRATION_TESTS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_INTEGRATION_TESTS.md) | None in the selected checks |
| [SONARCLOUD_PR_CI.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md) | None in the selected checks |
| [ARCHITECTURE_MAINTAINABILITY_AUDIT.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) | None in the selected checks |
| [F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) | None in the selected checks |
| [DEMO_CREDENTIALS_SECURITY.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md) | None in the selected checks |
| [FLYWAY_V2_SEAT_UNIQUENESS.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/FLYWAY_V2_SEAT_UNIQUENESS.md) | None in the selected checks |
| [JACOCO_COVERAGE_BASELINE.md](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/JACOCO_COVERAGE_BASELINE.md) | None in the selected checks |

The README uses a textual MVC → service → JPA repository → database sequence. The selected indicators covered literal `mermaid`, `plantuml`, `draw.io`, `graph TD/LR`, `sequenceDiagram` and Markdown image links ending in common `.png`, `.svg` and JPEG extensions. Other notation, assets and unsampled documents may exist. The absence of selected markers in a sample **does not establish that every technical diagram is absent**.

A direct reading of [pinned README lines describing CI and authorship](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) confirms that pull requests to `main` are mentioned as triggering checks, and Git history/PRs are referenced for later change attribution. These statements are **not** a published external-contribution eligibility, review or acceptance policy. The earlier pinned `404` results for three conventional contribution paths remain path-specific only.

### Conditional semantic recommendations — not approved

- **`README-CONTRIBUTING`:** if the maintainer confirms collaboration guidance is relevant for the intended open-source/portfolio audience, **`Applicability: Applicable` and `State: Missing` are the preferred provisional pair** *for contribution policy itself*, unless an equivalent policy is identified. Maven/CI onboarding instructions should not automatically be treated as a partial contribution policy. If the project does not invite contributions, the reviewer may instead justify `Not Applicable`. A valid contractual State is still required for Assessment completion.
- **`DOC-DIAGRAMS`:** if maintainable diagrams would not clarify important domain relationships or operations beyond the current textual explanation, **`Applicability: Not Applicable` is the preferred provisional value**. If diagrams are useful, select `Applicable` and determine `Missing / Partial / Satisfied` against actual diagram evidence. No final State is proposed while that scope decision remains open.

Both recommendations are **conditional** on project purpose and maintainer judgment; neither records human approval. The working Assessment remains `In Progress`, with three States unselected and four Applicability values `Uncertain`, and no consumer changes.

