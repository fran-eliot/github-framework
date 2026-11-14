# Only Film — Adoption Decision review batch 8: API, Diagrams and References

## Scope and controlled baseline

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable consumer reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `DOC-API`, `DOC-DIAGRAMS`, `DOC-REFERENCES` |
| Formally approved State / Applicability pairs | `28/28`, unchanged |
| Formally resolved Adoption Decisions | `14/28` (11 `PRESERVE`, 3 `OMIT`; API and References approved 2026-11-14) |
| Unresolved Adoption Decisions | `14/28`, including `DOC-DIAGRAMS` |
| Assessment | `In Progress` |
| Only Film mutations | `NONE` |

This is a **preapproval decision-review packet**, not an Adoption Decision, application request, integration plan or change to Only Film. The independent maintainer-approved `State / Applicability` pairs have already been recorded; a separate **explicit human approval** is required for each `Decision Status: Resolved` and associated Adoption Decision. Merging this review packet or replying with `go` does not constitute that approval.

## Formal maintainer Adoption Decision outcome — 2026-11-14

The Only Film maintainer **expressly approved `DOC-API = OMIT` and `DOC-REFERENCES = OMIT`**, and expressly retained `DOC-DIAGRAMS = Needs Further Evaluation / —`:

| Responsibility | Decision Status | Adoption Decision | Precise approved scope and surviving uncertainty |
| --- | --- | --- | --- |
| `DOC-API` | `Resolved` | `OMIT` | Documentation of a **currently supported public/programmatic API contract only**; bounded controller review does not prove the absence of every HTTP or internal programmatic route |
| `DOC-DIAGRAMS` | `Needs Further Evaluation` | `—` | Maintainer interest in future diagrams is real, but artifact inventory is not exhaustive and the diagram type, reader benefit, evidence and acceptance criteria are unselected; no diagram is authorized |
| `DOC-REFERENCES` | `Resolved` | `OMIT` | A **standalone centralized external-technical-reference catalog only**; contextual links, their usefulness, authority, accuracy and maintenance remain relevant, and link health has not been audited |

**Approval date:** 2026-11-14. **Pinned consumer source:** `28d75a50e0a178954dd46acc23300d9dd327843c` (independent of the maintainer's approval date). The 28 individually approved State / Applicability classification pairs are unchanged, including `DOC-API: Missing / Not Applicable`, `DOC-DIAGRAMS: Missing / Applicable`, and `DOC-REFERENCES: Partial / Not Applicable`.

**Authorization boundary:** `Assessment: In Progress`, **14/28 Adoption Decisions formally resolved** (11 `PRESERVE`, 3 `OMIT`), **14 unresolved**. `OMIT` does not remove any consumer route, source, citation or file; diagram generation and any other Application/Integration work remain unauthorized. **Only Film is read-only**.

The candidate language below is the historical **preapproval review**, superseded as to decision status by the dated express maintainer outcome above.

## Candidate decision comparison

| Responsibility | Approved State / Applicability | Reviewer-facing candidate | Strict interpretation |
| --- | --- | --- | --- |
| `DOC-API` | `Missing / Not Applicable` | **Consider `Resolved / OMIT`** | Omit documentation for a **currently supported public/programmatic API contract** only, not all HTTP routes or any future REST API capability |
| `DOC-DIAGRAMS` | `Missing / Applicable` | **Keep `Needs Further Evaluation / —` by default** | Maintainer-confirmed future value does not identify a verified current diagram, diagram subject, audience, acceptance checks or a current authorization to create it |
| `DOC-REFERENCES` | `Partial / Not Applicable` | **Consider `Resolved / OMIT`** | Omit a **standalone centralized external-technical-reference catalog** only; preserve usefulness and maintenance of in-context references |

`OMIT` would be a formally approved **scope choice not to add the specified inapplicable deliverable**, not a deletion or waiver for broader concerns. `ADD` for diagrams is a potential later action, **not** a consequence of `State: Missing` or `Applicability: Applicable` alone.

## 1. DOC-API — external contract, not every MVC route

### Pinned-source evidence and approval scope

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) describes an interactive Spring MVC/Thymeleaf web application and places a REST API among **possible future extensions**, not among confirmed current public features.
- The previously reviewed [API and References contract-scope batch](only-film-api-references-contract-review-batch.md) inspected **seven MVC controller paths**, including re-fetching `MovieController.java` and `ReviewController.java`. Neither of those two files declared `@RestController`, `@ResponseBody` or `ResponseEntity` in the reviewed content; this is **not** an exhaustive pinned-repository programmatic-interface audit.
- Spring `@Controller` routes that serve HTML or authenticate session-based users are HTTP interfaces, **but not by themselves a published integration contract**. A filename search without OpenAPI/Swagger files cannot prove that no API or other programmatic route exists elsewhere.
- On **2026-11-14**, the maintainer **formally approved `Missing / Not Applicable`**, expressly limiting `Not Applicable` to documentation for a **currently supported public/programmatic API contract**. This approval did not label all HTTP routes absent and did not resolve an Adoption Decision.

### Decision choices

**Consider `Resolved / OMIT`** to intentionally **not introduce public API-contract documentation for this evidenced, currently server-rendered consumer scope**. The precise rationale must retain the sampled-source caveat: this is not a claim that every source-level JSON route, HTTP contract, filter or external client was exhaustively inventoried. It does not remove web-controller guidance or commit the project against future REST work.

`Needs Further Evaluation / —` is appropriate if the maintainer needs a complete public-interface inventory before accepting this narrow scope. `ADD` would require **independent evidence of an actual supported contract and a new explicit decision**; it cannot be inferred from the roadmap's proposed REST feature. `OMIT` should be reconsidered if a public/programmatic contract is introduced later.

No endpoint, Swagger/OpenAPI specification, backend functionality or consumer documentation will be created by this assessment.

## 2. DOC-DIAGRAMS — useful future artifact, decision still unscoped

### Pinned-source evidence and maintainer intent

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) explains the nominal `MVC Controller → Service → JPA Repository → Database` architecture **textually**. UI screenshots illustrate pages, not a technical architecture, domain or execution diagram.
- The previous [targeted optional-contract spot-check](only-film-optional-contract-spotcheck.md) examined **nine named pinned Markdown documents** for recognizable Mermaid, PlantUML, draw.io and technical-diagram markers; none was identified in that **bounded sample**. This is not an exhaustive asset or embedded-diagram inventory.
- The [Framework Architecture Component](../../components/documentation/architecture/README.md) treats diagrams as useful where they clarify real relationships and current architecture, not as mandatory decoration. The prior Framework catalog inspection did not locate a separate `DOC-DIAGRAMS` Component specification; no unstated component requirements apply here.
- On **2026-11-14**, the maintainer confirmed that a future technical diagram **would be useful** and **formally approved `Missing / Applicable`** with evidence limits. That expressed interest is **not** approval of an `ADD` Adoption Decision, a specific diagram, or permission to modify Only Film.

### Decision choices

**Default `Needs Further Evaluation / —`.** Before an `ADD` decision, identify the actual reader question, one diagram's scope and acceptance evidence:

- **Architecture overview:** represent the principal Spring MVC/Thymeleaf → service → JPA → H2/PostgreSQL/Flyway context, after checking actual layer dependencies at the pinned SHA; do not certify universal strict layering.
- **Domain relationships:** show `Movie`, `Room`, `Session`, `Ticket`, `Review` and `User` only after verifying entity relations, multiplicities and constraints in pinned JPA/SQL.
- **Checkout/seat concurrency:** document only the source-validated lock and transaction flow, distinguishing checkout simulation from real payment processing.

These are **alternatives**, not a mandated three-diagram bundle. `ADD` becomes defensible only after explicitly choosing one focused, maintainable artifact and defining its evidence/acceptance gate. `PRESERVE` would require identifying a substantive existing diagram that was missed in the bounded sample. No diagram is generated in this packet.

## 3. DOC-REFERENCES — contextual sources versus a redundant index

### Pinned-source evidence and approval scope

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) links the original collaborative repository, supporting project documentation and CI/workflow resources; specialized [PostgreSQL setup](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/POSTGRESQL_SETUP.md) and [dependency maintenance](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEPENDENCY_MAINTENANCE.md) guides supply additional context.
- The directly re-fetched [DOC-REFERENCES Component](../../components/documentation/references/README.md) describes useful authoritative source references, but **explicitly says a separate index may be unnecessary** when there are few references or meaningful links are better kept alongside relevant content.
- The previously approved [API and References scope review](only-film-api-references-contract-review-batch.md) distinguished the **standalone centralized external-technical-reference catalog** from contextual links, source attribution and link maintenance. The review had **not** audited all reference URLs or checked freshness/health.
- On **2026-11-14**, the maintainer **formally approved `Partial / Not Applicable`**, with `Not Applicable` limited **only** to a standalone centralized technical references catalog. This is not a finding that project citations are unnecessary.

### Decision choices

**Consider `Resolved / OMIT`** for the **separate centralized reference catalog** under the approved no-standalone-catalog scope. This preserves all existing contextual references and their obligations for accuracy, link integrity, appropriate authority and attribution; none of these is waived or declared fully verified.

`PRESERVE` would be less precise for an inapplicable separate catalog and could imply a fully satisfied standalone deliverable; the preapproved State remains `Partial`. `ADD` would require an independently justified need for a central reference corpus. Remain `Needs Further Evaluation / —` if evidence of current link use or audience needs is insufficient to settle the narrow choice.

No reference list, external link, citation, README section or consumer file is removed or modified.

## Formal review gate

The maintainer may expressly approve each decision independently or keep it open. Recommended separate approval bundle:

1. `DOC-API = OMIT`, **strictly scoped to a currently supported public/programmatic API-contract document**.
2. `DOC-DIAGRAMS = Needs Further Evaluation / —`, pending one chosen diagram purpose, current-source evidence and acceptance checks.
3. `DOC-REFERENCES = OMIT`, **strictly scoped to a standalone centralized external-technical-reference catalog**, without affecting in-context referencing.

A **later, separate approval-record PR** may update the canonical [Assessment](only-film-assessment.md), [consolidated matrix](only-film-consolidated-review-matrix.md), and this packet only after express maintainer approval and individual decision rationale. Merging this preparation PR is not approval.

**Postapproval status:** All 28 State / Applicability pairs unchanged; 14 Adoption Decisions now resolved (11 `PRESERVE`, 3 `OMIT`), 14 remain unresolved; Assessment `In Progress`; Only Film strictly read-only. Merging the earlier preparation PR did not itself approve these decisions; the formal decisions were expressly granted separately by the maintainer on 2026-11-14.
