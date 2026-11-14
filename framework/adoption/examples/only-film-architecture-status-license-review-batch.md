# Only Film — Architecture, project status and license: human review batch

## Scope and decision contract

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Pinned SHA | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Framework Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `README-ARCHITECTURE`, `DOC-ARCHITECTURE`, `DOC-PROJECT-STATUS`, `README-LICENSE` |
| Record status | **All four evaluations formally approved by the Only Film maintainer on 2026-11-14; see dated decision below** |
| Approved State/Applicability pairs after review | `17/28` |
| Overall Assessment | `In Progress` |
| Consumer changes | `NONE` |

This is a bounded human-review preparation document. It compares directly inspected consumer files at the **immutable pinned SHA** with the relevant Framework Components and existing Assessment. It does **not** substitute dated historical audits for current implementation evidence, confirm licensing rights, or authorize any change to Only Film.

## Formal maintainer approval outcome — 2026-11-14

The Only Film maintainer **expressly approved** these four separate State and Applicability values:

| Responsibility | Approved State | Approved Applicability |
| --- | --- | --- |
| `README-ARCHITECTURE` | `Satisfied` | `Applicable` |
| `DOC-ARCHITECTURE` | `Partial` | `Applicable` |
| `DOC-PROJECT-STATUS` | `Partial` | `Applicable` |
| `README-LICENSE` | `Partial` | `Applicable` |

This approval keeps **all evidence limitations**: the README's architecture flow is principal rather than exhaustive; dated architecture/functional/maturity audits concern older SHA references; current milestone and all historical issue dispositions remain unverified; and the original academic collaboration's **copyright, licensing rights, reuse permissions and relabeling authority are not established**. A documentary license-status evaluation does **not** authorize any license grant.

The Assessment stays `In Progress`, all four `Decision Status` fields stay `Needs Further Evaluation`, all four `Adoption Decision` fields remain `—`, and Only Film remains read-only.

The proposal and acceptance-gate language below records the **preapproval reviewer preparation** and does not supersede this dated decision.

## Proposed reviewer outcomes

| Responsibility | Existing unapproved State / Applicability | Recommended human-review outcome | Evidence scope |
| --- | --- | --- | --- |
| `README-ARCHITECTURE` | `Partial / Applicable` | **Consider `Satisfied / Applicable`** for the high-level documentary purpose | The README clearly describes a *principal* MVC/service/JPA/data path and main entities; exceptions in earlier source audits are not confirmed for this SHA |
| `DOC-ARCHITECTURE` | `Partial / Applicable` | **Retain `Partial / Applicable`** | A readable high-level overview and historical architecture report exist, but no maintained comprehensive current architecture description was validated |
| `DOC-PROJECT-STATUS` | `Partial / Applicable` | **Retain `Partial / Applicable`** | Historical maturity and functional plans do not establish current area progress, milestone and priorities |
| `README-LICENSE` | `Partial / Applicable` | **Retain `Partial / Applicable`** | The README accurately warns that it does not grant an additional license, but the rights basis and sufficient reuse-status clarity are unverified |

The outcome concerns **documentation coverage**, not architectural correctness, real-time project health, ownership, or a grant of legal rights. Missing a canonical English heading alone is not a reason to fail an existing-repository Responsibility.

## 1. README-ARCHITECTURE — proposed `Satisfied` alternative

**Direct pinned observations**

- The [README's `Tecnologías y arquitectura`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) classifies backend, security, frontend, local/durable persistence, testing and infrastructure. It explicitly calls the path **`Flujo principal`**: `Controlador MVC → servicio / reglas de negocio → repositorio JPA → base de datos`, and names `Movie`, `Room`, `Session`, `Ticket`, `Review`, `User`.
- The [Framework README-ARCHITECTURE Component](../../components/readme/architecture/README.md) only asks for a **general architecture summary** and says it must not replace detailed technical documentation. It does not require an architecture diagram or exhaustive layer-by-layer assertions.
- [`docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) was directly fetched in the pinned tree; it is **dated 2026-10-10 and tied to an earlier commit after PR #23 (`b6cf52c9`)**. It observed selected controller-to-repository paths **at that older reference**. It does not show those paths still existed at the pinned assessment commit.

**Assessment interpretation:** `Satisfied / Applicable` is a reasonable **candidate** if the maintainer accepts this concise *principal* flow as sufficiently accurate for a README-level orientation, despite nonexhaustive code verification. `Partial / Applicable` is equally defensible if the maintainer wants the README to distinguish exceptions more explicitly. Neither verdict asserts perfectly uniform code layers.

**Unverified:** all controller dependencies at the pinned SHA, runtime traces, all exceptions to the principal flow, and architecture diagram rendering. No new diagram or refactoring authorized.

## 2. DOC-ARCHITECTURE — retain `Partial` proposal

**Direct pinned observations**

- The [DOC-ARCHITECTURE Component](../../components/documentation/architecture/README.md) expects a maintained description of the **current** architectural context, components, responsibilities, relationships, flows and constraints. It recognizes an explicit exception for projects small enough to explain wholly in README, discouraging duplicate documents created for formality.
- The README provides a high-level flow and stack categorization, while the pinned [architecture maintainability audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/ARCHITECTURE_MAINTAINABILITY_AUDIT.md) provides historical observations and possible improvements from October, **not** a currently reconciled system design.
- The pinned [F3 functional audit and roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) uses another earlier SHA (`df63353564485eb6d2d60c982032e5d3c4facbf2`), and already warns against automatically reopening older risks. This further demonstrates why dated documents must not silently become a current architecture contract.

**Assessment interpretation:** `Partial / Applicable` remains a **conservative candidate**, because current architectural relationships and important constraints beyond the summary have not been systematically reconciled. The reviewer could reasonably choose `Satisfied / Applicable` if the README and relevant existing sources provide sufficient current orientation for the project's complexity. If the project is small enough that a separate architecture document adds no value, the Component also supports reviewing **Applicability** independently, but `Not Applicable` is **not recommended without an explicit scope judgment**.

**Unverified:** current code-wide boundaries, design constraints, full component links, and which historical audit findings persist. No standalone architecture document is authorized.

## 3. DOC-PROJECT-STATUS — retain `Partial` proposal

**Direct pinned observations**

- The [DOC-PROJECT-STATUS Component](../../components/documentation/project-status/README.md) describes a maintained operational **snapshot**: general state, progress by area, next milestone and immediate objectives. It explicitly distinguishes this from a roadmap, issue tracker or changelog and allows a README-only alternative for smaller projects.
- [`docs/TECHNICAL_MATURITY_ASSESSMENT.md`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/TECHNICAL_MATURITY_ASSESSMENT.md) is dated **2026-10-10**, with explicit source commit `9f2a31e927df105d14e3d30d4d8277fa61883deb`. Its academic/portfolio maturity judgment applies to that **older** reference; it must not be presented as a current certification.
- The pinned [F3 functional audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) describes a plan based on `df63353564485eb6d2d60c982032e5d3c4facbf2`, not a verified live completion table at the assessed SHA.
- The pinned [README's `Próximas líneas de evolución`](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) lists possible REST API, real payment, observability and deployment automation work as **future-only ideas**. That is helpful but does not identify a validated next project milestone or state by workstream.

**Assessment interpretation:** retain `Partial / Applicable` as a bounded proposal. Some status and evolution information is present, but a dated, maintained status summary with current progress and next milestone was not established. This is **not** evidence that the project has stalled or that every F3 item remains outstanding.

**Unverified:** actual F3 ticket completion at the pinned SHA, next milestone, current ownership and work-in-progress. No new status document or milestone assertions authorized.

## 4. README-LICENSE — retain `Partial` proposal

**Direct pinned observations**

- The pinned [README's final `Licencia` notice](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) identifies the academic origins and directs readers to the original source for terms. It explicitly states that the README **does not establish an additional license**.
- The same README identifies four original contributors, links the academic [source repository](https://github.com/certidevs/g1_testing) and distinguishes original collaborative work from later technical changes. This is attribution content, **not proof of rights**.
- The pinned [POM](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) has an empty `<licenses><license/></licenses>` placeholder; it does not provide grant terms.
- Prior bounded source review in the [Assessment](only-film-assessment.md) did not identify root `LICENSE`, `LICENCE` or `COPYING` files. **No new repository-wide rights audit or external source license verification** was performed in this packet.

**Assessment interpretation:** `Partial / Applicable` is a defensible documentary proposal while the maintainer reviews whether the cautionary note is clear enough to readers and whether a precise rights statement can be supported. A future `Satisfied` approval can only mean the **notice communicates the uncertainty well**, never that source code has been licensed or the maintainer has sole authority to grant rights.

**Unverified:** copyright ownership, contributor permissions, valid reuse terms, license status of the source academic repository, external rights-holder consent. No `LICENSE` file, licensing choice or permission statement is authorized or recommended by this review.

## Human acceptance gate

The maintainer should explicitly decide **both State and Applicability** for each:

1. `README-ARCHITECTURE`: candidate `Satisfied / Applicable`, or retain `Partial / Applicable` if the principal-flow explanation requires qualification.
2. `DOC-ARCHITECTURE`: retain `Partial / Applicable`, or revise after determining whether the README plus dated guides suffice for current architecture and if separate documentation is needed.
3. `DOC-PROJECT-STATUS`: retain `Partial / Applicable`, or revise once current status/milestone criteria are accepted.
4. `README-LICENSE`: retain `Partial / Applicable`, or approve `Satisfied / Applicable` **solely for cautious documentary communication**, never as legal authorization.

**Merging this packet is not formal approval.** Record an explicit maintainer decision and date separately in the Assessment and consolidated review matrix. `Decision Status: Needs Further Evaluation`, `Adoption Decision: —` and overall `Assessment: In Progress` remain for all four.

## Evidence and authorization boundary

Consumer evidence is anchored to immutable commit `28d75a50e0a178954dd46acc23300d9dd327843c`. The three historical audits are cited at their own **earlier reference points** and are not used to assert present-day defects or milestones. No code, deployment, ownership decision, licensing action, milestone update, README edit, documentation expansion, or architectural change to Only Film has been authorized. No resolved Adoption Decision is recorded.
