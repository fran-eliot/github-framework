# 55 — Framework Functional Maturity Discovery

| Field | Value |
|---|---|
| Project | GitHub Framework |
| Date | 2026-11-11 |
| Published baseline version | `v0.10.0` |
| Status | Discovery — documentation and code baseline, not Delivery Scope |
| Focus | Repository Templates, Framework Validator, and Existing Repository Adoption |
| Previous investigation | [54 — First-Time Usability Validation Protocol](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md) |
| Implementation decision | None |
| Sprint / milestone / new version | None committed |

> This document examines **capabilities observable in published artifacts**, distinguishing them from conceptual contracts and future options. Code review is static: neither the test suite nor the CLI was executed during this investigation.

---

## 1. Objective

Establish a verifiable baseline to answer:

> What can an external developer actually use in GitHub Framework v0.10.0, what requires human involvement, and what remains a conceptual contract?

The three areas examined are:

1. Repository Templates and actual Component availability.
2. Framework Validator, its coverage, and execution boundaries.
3. Existing Repository Adoption from Assessment to Integration, with Assisted Analysis support.

The review does not assume that an adoption CLI, generator, new Template, manifest, or remediation system should be created.

## 2. Method and Sources

Public files from `main` after PR #91 were examined, including:

- [Repository Template Library](../../framework/templates/repositories/README.md).
- [Backend Template](../../framework/templates/repositories/backend/README.md) and its [metadata](../../framework/templates/repositories/backend/metadata.yml).
- [FullStack Template](../../framework/templates/repositories/fullstack/README.md) and its [metadata](../../framework/templates/repositories/fullstack/metadata.yml).
- [Documentation Template](../../framework/templates/repositories/documentation/README.md) and its [metadata](../../framework/templates/repositories/documentation/metadata.yml).
- [Framework Validator entry point](../../scripts/framework_validator/__main__.py).
- [Automation Reference Implementation](../implementation/22_AUTOMATION_REFERENCE_IMPLEMENTATION.md).
- [Assessment Guide](../../framework/adoption/README.md) and [Assessment Template](../../framework/adoption/assessment-template.md).
- [Application Guide](../../framework/adoption/application/README.md) and [Application Record](../../framework/adoption/application/application-template.md).
- [Integration Guide](../../framework/adoption/integration/README.md) and [Integration Record](../../framework/adoption/integration/integration-template.md).
- [Assisted Analysis Guide](../../framework/adoption/assisted-analysis/README.md) and [Evidence Snapshot Template](../../framework/adoption/assisted-analysis/evidence-snapshot-template.md).
- [Assisted Analysis Core Verification](../implementation/52_ASSISTED_ANALYSIS_CORE_VERIFICATION.md).

**Verification scope:** the listed artifacts exist and were read. Historical test and replay results are cited as previously documented Evidence, not as executions performed during this review.

## 3. Repository Templates: Capabilities and Boundaries

### 3.1 Confirmed Availability

The canonical library is located at `framework/templates/repositories/` and defines three Templates:

```text
TPL-BACKEND
TPL-FULLSTACK
TPL-DOCUMENTATION
```

Each provides a `README.md` and `metadata.yml`. Metadata identifies the Template, version, status, project type, maturity, and Components classified as `required`, `recommended`, and `optional`.

Templates are **declarative Component compositions**, not completed repositories or executable generators. The physical `template/` directory is optional and should not be created when the Template has no specific artifacts requiring it.

### 3.2 Reported Material Availability

| Template | Required implemented | Recommended implemented | Optional implemented | Total implemented |
|---|---:|---:|---:|---:|
| `TPL-BACKEND` | 8/8 | 5/7 | 3/13 | 16/28 |
| `TPL-FULLSTACK` | 9/9 | 4/8 | 3/11 | 16/28 |
| `TPL-DOCUMENTATION` | 8/9 | 2/7 | 1/5 | 11/21 |

**Source:** availability sections in the respective canonical Template READMEs. These figures do not constitute current Validator execution or an independent inventory-wide count.

`TPL-DOCUMENTATION` explicitly identifies `README-LICENSE` as a Required Component that remains `Conceptual`. Its minimum contract cannot be fully materialized using only implemented Components. The `Required`, `Recommended`, and `Optional` requirement levels must not be confused with the physical `Implemented` / `Conceptual` classification.

### 3.3 Usable Value and Limitations

**Available:** manual composition selection by project type, consultation of versioned contracts, and Responsibility references for assessment or deliberate construction.

**Not implemented as tooling:** automatic scaffolding generation, guided instantiation, or automatic parameterization. This review also found no executable validator specifically for Repository Template conformance.

**Maturity question:** is a declarative composition sufficient for the current target audience, or is there a repeatable need for more direct materialization or adoption? No decision is made yet.

## 4. Framework Validator: Capabilities and Boundaries

### 4.1 Behavior Verifiable from Code

The `scripts/framework_validator/__main__.py` entry point defines:

```text
REPOSITORY_ROOT = path of this Framework checkout
COMPONENTS_ROOT = REPOSITORY_ROOT / "framework" / "components"
```

Its `main()` function discovers Component directories, reads `metadata.yml`, and validates:

- Common Core and optional fields;
- Component ID identity and uniqueness;
- maturity and dependencies;
- Workflow extensions: materialization, artifacts, artifact files, adoption, and validation.

The CLI prints results and returns `0` when no errors are found, or `1` when errors are found. It is invoked from the Framework root with `python -m scripts.framework_validator`.

The v0.6.0 Reference Implementation documents **21 physical Components**: 4 Documentation, 12 README, and 5 Workflow, together with isolated tests and historical dogfooding.

### 4.2 Structural Boundary

The hard-coded `COMPONENTS_ROOT` points to the GitHub Framework checkout itself. This entry point does not accept an arbitrary consumer repository as the assessment target and **does not** automatically determine semantic Responsibility coverage for a consumer.

It also does not generate content, apply Adoption changes, or validate Evidence Snapshots. The last boundary is confirmed by the Assisted Analysis Core verification document.

**Do not infer** that the Validator is defective because it does not perform functions outside its defined scope. It is an implemented consistency tool for the Framework catalog, not an automated adoption advisor.

## 5. Existing Repository Adoption: Capabilities and Boundaries

| Capability | Primary artifact | Supported work | Boundary |
|---|---|---|---|
| Assessment Core | Guide + Structured Markdown Assessment Template | ANALYZE → ASSESS → REVIEW → DECIDE → REPORT | Persistent result without consumer modification |
| Application Core | Guide + Application Record | SELECT, refresh Evidence, plan, review, apply in isolation, and verify | Ends at verified candidate state; bounded, human-directed change |
| Integration Core | Guide + Integration Record | Refresh stable base, drift, governance checks, review, integrate, verify stable state | Verified stable state or safe-stop/recovery-required state |
| Assisted Analysis Core | Guide + Evidence Snapshot Template | Deterministic, bounded, source-traceable, read-only Evidence for the other three capabilities | Does not perform semantic evaluation or make decisions |

### 5.1 Implementation Status

Implementation and verification documentation identifies all four Cores as delivered in published versions, including Assisted Analysis Core in v0.10.0. Earlier verification records A/B/C replays and AC-01…AC-73 as `PASS`.

**Nature of the deliverables:** reusable Markdown guides and representations. These artifacts do not demonstrate an execution engine for Assessment, Application, or Integration. A human practitioner must collect Evidence, interpret it, and perform permitted operations under each Guide's conditions.

`Application` may include material changes **performed by people under review** and must not be described as necessarily read-only. `Assisted Analysis` is explicitly read-only.

### 5.2 Value and Potential Friction

**Current value:** a traceable, reviewable model that is non-destructive by default, supports non-canonical implementations, preserves human decisions, and respects consumer governance.

**Potential, unvalidated friction:** navigating between four Guides and their records may require significant effort for a first adoption. UX-01 covered only the entry point; UX-02 has an approved protocol but has not been executed with independent participants.

**Do not assume** that Guide length alone demonstrates a usability defect or justifies an automated engine.

## 6. Observable Maturity Map

| Area | Documented contract | Reusable artifact | Dedicated automated execution | Usage Evidence |
|---|---|---|---|---|
| Repository Templates | Yes | Yes (metadata and README) | Not documented for instantiation | Previous Reference Implementations / Discovery |
| Framework Validator | Yes | Yes (Python code) | Yes, validation of Framework Components | Documented v0.6.0 tests and dogfooding |
| Assessment | Yes | Yes (Guide + Template) | No; human evaluation | v0.7.0 experiments and verification |
| Application | Yes | Yes (Guide + Record) | No; human application in isolation | v0.8.0 verification |
| Integration | Yes | Yes (Guide + Record) | No; integration under human governance | v0.9.0 verification |
| Assisted Analysis | Yes | Yes (Guide + Snapshot) | No; documented human collection | v0.10.0 replays and verification |

This map describes the implementation **as examined in the sources**, not an end-to-end execution certification for every capability against arbitrary external repositories.

## 7. Preliminary Findings

### FM-F01 — Composition and Materialization Are Distinct Dimensions

All three Repository Templates are specified, but not all their Components are available. `TPL-DOCUMENTATION` has a material gap among Required Components. That does not automatically imply non-conformance for a consumer with its own or an equivalent implementation.

### FM-F02 — The Validator Has a Deliberately Limited Target

The CLI inspects metadata in this project's `framework/components/`, not Responsibilities in an arbitrary consumer. Any extension would require justification of its use case, contract, and semantic boundary rather than using the Validator's name to imply automatic conformance.

### FM-F03 — Adoption Is Reusable Without Automatic Execution

The Assessment → Application → Integration chain is documented, and Assisted Analysis can supply Evidence. Current value lies in the practices and reviewable records; automation is not part of the published delivery.

### FM-F04 — Architectural Verification Does Not Establish Autonomous Adoption

Historical verifications demonstrate the boundaries and criteria of their respective deliveries. On their own, they do not show that a new user can complete the entire workflow without guidance. UX-02 has yet to be executed.

## 8. Prioritized Research Hypotheses

| Research order | Hypothesis | Evidence needed before Solution Shaping |
|---|---|---|
| 1 | Incomplete Component availability in some Templates affects initial use. | Real `TPL-DOCUMENTATION` scenarios distinguishing canonical and equivalent implementations |
| 2 | The manual Adoption workflow has repeatable friction points between records. | Observation of a consumer and traceability across Assessment, Application, Integration, and Evidence Snapshot |
| 3 | Users misinterpret the scope of the Framework Validator. | Tasks or documentation exposing actual expectations about what it validates and which repository |
| 4 | A need may exist to automate specific deterministic tasks. | Repeated operations, observed cost, and semantic boundaries; not preferences alone |

This is an order **for investigation**, not implementation, and does not select the next product increment, release, or backlog item.

## 9. Recommended Next Check

Before building features, perform a bounded **Template Materialization Reality Check**:

1. Review `TPL-DOCUMENTATION` and its `README-LICENSE` gap.
2. Distinguish which part of the gap affects the Framework and which can be satisfied by a consumer-specific implementation.
3. Examine Evidence from previously documented real cases to avoid repeating experiments.
4. Determine whether a reproducible need arises for a new Component, a requirement-level change, or no change.

The investigation should remain read-only regarding consumers and explicitly record uncertainty. If Evidence supports a change, begin Solution Shaping separately before defining Delivery Scope.

## 10. Conclusion

GitHub Framework v0.10.0 provides structured Templates, an executable Validator focused on its own catalog, and a complete Adoption model with reviewable Markdown artifacts. The lack of automatic execution in certain capabilities is a **scope boundary**, not necessarily a defect.

The next maturity question with tangible Evidence concerns the difference between conceptual contracts and actual Component availability, particularly in `TPL-DOCUMENTATION`.

**Status:** initial Discovery completed; no solution approved, Sprint opened, or release committed.
