# 56 — Documentation Template Materialization Reality Check

| Field | Value |
|---|---|
| Project | GitHub Framework |
| Date | 2026-11-11 |
| Status | Discovery — bounded reality check |
| Framework baseline | v0.10.0 |
| Template | `TPL-DOCUMENTATION v0.1.0` |
| Template status / maturity | `Experimental` / `L2` |
| Previous reference | [55 — Framework Functional Maturity Discovery](55_FRAMEWORK_FUNCTIONAL_MATURITY_DISCOVERY.md) |
| Delivery / Sprint / milestone | None committed |

> This document examines the distinction between canonical Component availability and a consumer's coverage of Responsibilities. It is not a complete conformance Assessment, a Delivery Scope, or authorization to change the Template or materialize Components.

---

## 1. Research Question

The functional analysis in #55 identified a gap in `TPL-DOCUMENTATION`: one of its nine `Required` Components is classified as `Conceptual`. The question is:

> Does the conceptual status of `README-LICENSE` actually prevent use of `TPL-DOCUMENTATION` in an existing documentation repository, or does it only limit reuse of a canonical Framework implementation?

**Hypothesis:** the gap concerns availability of a canonical Component, not necessarily whether any particular consumer can satisfy the Responsibility.

## 2. Sources Reviewed

- [TPL-DOCUMENTATION metadata](../../framework/templates/repositories/documentation/metadata.yml) — canonical contract source.
- [TPL-DOCUMENTATION README](../../framework/templates/repositories/documentation/README.md) — scope, availability, and boundaries.
- [Repository Template Library](../../framework/templates/repositories/README.md) — classification, version, and conformance.
- [Component Catalog](../design-system/09_COMPONENT_CATALOG.md), sections 19 and 48 — conceptual distinction and definition of `README-LICENSE`.
- [Framework README](../../README.md), `License` section, and [LICENSE](../../LICENSE) — observable example within the Framework itself.
- [Adoption Assessment Guide](../../framework/adoption/README.md) — `Responsibility over File` and human-review principles.

These findings come from **document inspection of published artifacts**, not from executing the Framework Validator or an external Assessment.

## 3. Canonical TPL-DOCUMENTATION Contract

The metadata declares:

```yaml
id: TPL-DOCUMENTATION
version: 0.1.0
status: Experimental
project_type: Documentation
maturity: L2
```

Its composition contains **9 Required, 7 Recommended, and 5 Optional** Components (21 referenced Responsibilities / Components). Its README availability section records:

| Requirement level | Implemented | Declared |
|---|---:|---:|
| Required | 8 | 9 |
| Recommended | 2 | 7 |
| Optional | 1 | 5 |
| **Total** | **11** | **21** |

The only identified gap among Required Components is:

```text
README-LICENSE → Conceptual
```

This classification does not automatically change the `Required` requirement level. Nor does it mean the entire Template is absent or unusable as a basis for reasoning about Responsibilities.

## 4. Meaning of README-LICENSE

The Catalog defines `README-LICENSE` as the **Responsibility to communicate the project's applicable license from the README**.

Its published classification is:

```text
Family: README
Implementation: Conceptual
```

The Catalog clarifies that a consumer's `LICENSE` file covers a related Responsibility, but **does not by itself constitute a reusable canonical implementation** of the `README-LICENSE` Component.

The following statements must not be treated as equivalent:

```text
LICENSE file exists
    ≠
README communicates applicable license
    ≠
Framework provides a canonical reusable README-LICENSE Component
```

The `TPL-DOCUMENTATION` contract requires the corresponding Responsibility; availability of a physical reusable Component is a separate dimension.

## 5. Observable Case: GitHub Framework Itself

The `fran-eliot/github-framework` repository includes:

- A `## 📄 License` section in its [README](../../README.md), stating that the project is distributed under the MIT license.
- A [LICENSE](../../LICENSE) file containing the MIT license text and copyright notice.

These are **Detected Facts** drawn directly from documentation. They support the hypothesis that a consumer can communicate its license without first materializing `README-LICENSE` as a Framework Component.

### Limitations of the Example

- `github-framework` is not claimed to be a formal `TPL-DOCUMENTATION` consumer; the repository combines documentation and executable tooling.
- No `README-LICENSE` Responsibility Assessment has been completed on an independent documentation consumer.
- A license section and a `LICENSE` file constitute Evidence, not an automatic `Satisfied` State or an `Adoption Decision`.
- The example does not demonstrate that the observed implementation should become the canonical content of a new Component.

## 6. Confirmed Architectural Distinction

The Component Catalog and Template Library maintain the rule:

```text
Component availability
    ≠
Consumer conformance
```

A consumer may satisfy a Responsibility through an own, distributed, or equivalent implementation while the Framework Component remains `Conceptual`.

Consequently, both of the following statements can be true at the same time:

1. `TPL-DOCUMENTATION` **cannot be fully materialized using only the Framework's currently implemented canonical Components**.
2. A consumer **may satisfy the license-communication Responsibility** through its own artifacts without waiting for a canonical Component to exist.

Actual conformance requires evaluation against the Responsibility, Evidence, and human review. It cannot be inferred from the mere presence of an individual file.

## 7. Alternatives Reviewed, Without a Solution Decision

| Alternative | What It Would Address | What Still Needs to Be Demonstrated |
|---|---|---|
| A. Preserve the contract and classification | Retains the current model and permits consumer-specific implementations | That the availability limitation is acceptable for real documentation consumers |
| B. Materialize `README-LICENSE` as a Component | Provides a reusable canonical implementation and could close the Required materialization gap | Real need, contract definition, minimal composition, license variability, and maintenance costs |
| C. Review the requirement level of `README-LICENSE` | Changes the minimum `TPL-DOCUMENTATION` contract | Evidence that license communication should not be Required for this repository type; implementation absence alone is insufficient |
| D. Document a consumer-specific composition path | Clarifies options when a Responsibility exists without a canonical Component | Observed user confusion and lack of equivalent information in current guides |

No alternative is selected here. In particular, **a materialization gap does not justify downgrading a Requirement Level**.

## 8. Findings Register

| ID | Finding | Status |
|---|---|---|
| TM-F01 | `TPL-DOCUMENTATION v0.1.0` references `README-LICENSE` as Required and Conceptual. | Confirmed |
| TM-F02 | The Component Catalog explicitly distinguishes communicating license information in README from having a LICENSE file. | Confirmed |
| TM-F03 | The Framework itself communicates its license in README and contains a LICENSE file. | Confirmed as observable case |
| TM-F04 | `Conceptual` limits canonical availability but does not automatically determine consumer conformance. | Confirmed in published contracts |
| TM-F05 | The lack of a canonical Component creates a substantial barrier for real documentation consumers. | **Not demonstrated** |
| TM-F06 | `README-LICENSE` must be materialized or its requirement level changed. | **Not demonstrated** |

## 9. Outstanding Research

Before Solution Shaping or Product Backlog work:

1. Select a **documentation-first repository** with an immutable identity and reference, not deliberately built to satisfy this Template's contract.
2. Record only the Evidence needed for `README-LICENSE` (README section, license link or text, related file, clarifications, and context), without inferring conformance from a filename.
3. Classify Responsibility coverage through human review, preserving explicit uncertainties.
4. Check whether the absence of the canonical Component creates actual adoption friction, independently of the observed coverage.
5. Repeat or compare with another consumer only if the first case cannot distinguish the hypotheses.

If no repeatable need appears, **do not materialize or reclassify by default**.

## 10. Result and Decision Boundary

**Reality Check result:** a **canonical materialization** gap was confirmed, not a universal inability to use the Template or a proven defect in the `TPL-DOCUMENTATION` contract.

The next investigation requires evidence from a specific documentation consumer. Templates, Components, Validator, and consumers have not been modified. No complete Assessment was run and the Template was not promoted to `Stable`.

**Decision:** keep the alternatives open and continue Discovery without committing an implementation, Sprint, milestone, or release.
