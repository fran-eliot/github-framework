# 57 — Documentation Consumer License Responsibility Case Study

| Field | Value |
|---|---|
| Project | GitHub Framework |
| Date | 2026-11-11 |
| Status | Discovery — bounded evidence review |
| Previous experiment | [56 — Documentation Template Materialization Reality Check](56_DOCUMENTATION_TEMPLATE_MATERIALIZATION_REALITY_CHECK.md) |
| Consumer | [github/docs](https://github.com/github/docs) |
| Consumer Reference | `2b4f2c7398e04ee8d02adca7440e4286d20c78b9` (`main`) |
| Repository Template | `TPL-DOCUMENTATION` |
| Template Version | `0.1.0` |
| Responsibility examined | `README-LICENSE` (`Required`) |
| Assessment coverage | One Responsibility; not a complete Assessment |
| Consumer mutation | None |

> The results of this case apply only to the Evidence observed at the pinned reference. The consumer is used as an independent documentation example; there is no claim that it has formally adopted GitHub Framework.

---

## 1. Objective and Research Question

Continue the research from #56 using Evidence from a repository whose primary product is documentation and which was not explicitly built to satisfy GitHub Framework contracts.

Question:

> Can a real documentation consumer implement the `README-LICENSE` Responsibility independently even though the Framework Component remains classified as `Conceptual`?

This review does not attempt to determine the consumer's overall conformance, coverage of the Template's other 20 Responsibilities, or legal compliance with license obligations.

## 2. Selection Criteria

[github/docs](https://github.com/github/docs), GitHub's public documentation repository, was selected because:

- Its [README](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md) explicitly identifies the repository as documentation open to contributions.
- Its root structure includes `content/`, `data/`, and `assets/`, as well as publishing code under `src/`.
- It is a **documentation-first** case, although not exclusively documentation: the presence of tooling and code makes that distinction important.
- Its licensing information is observable for both documentation and code.

Selection is based on the repository's purpose and published artifacts. It does not formally assign the Template to the consumer.

## 3. Baselines and Contract

The consumer reference is the immutable commit:

```text
github/docs
2b4f2c7398e04ee8d02adca7440e4286d20c78b9
```

The comparison contract is `TPL-DOCUMENTATION v0.1.0`:

- [Canonical metadata](../../framework/templates/repositories/documentation/metadata.yml).
- [Canonical README](../../framework/templates/repositories/documentation/README.md).
- [Conceptual definition of README-LICENSE](../design-system/09_COMPONENT_CATALOG.md), section 48.

The Template metadata declares `README-LICENSE` among its nine `Required` Components. The Catalog classifies it as `Conceptual`; the recognized Responsibility is **communicating the project's applicable license from its README**.

## 4. Detected Facts and Evidence

| ID | Detected Fact | Pinned Evidence |
|---|---|---|
| E-01 | The README presents the repository as GitHub documentation open to contributions. | [`README.md`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md), introduction |
| E-02 | The README includes a `License` section. | [`README.md`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md), final section |
| E-03 | The `License` section distinguishes Creative Commons Attribution 4.0 for documentation/content from MIT for code. | [`README.md`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md), `License` section |
| E-04 | The README explicitly links to `LICENSE` and `LICENSE-CODE`. | [`README.md`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/README.md), relative links |
| E-05 | `LICENSE` contains the Creative Commons Attribution 4.0 International text. | [`LICENSE`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/LICENSE), heading |
| E-06 | `LICENSE-CODE` contains the MIT License text. | [`LICENSE-CODE`](https://github.com/github/docs/blob/2b4f2c7398e04ee8d02adca7440e4286d20c78b9/LICENSE-CODE), heading |

The license texts are not reproduced; the links provide reviewable sources.

## 5. Bounded Responsibility Evaluation

| Field | Case Evaluation |
|---|---|
| Responsibility | `README-LICENSE` |
| Requirement Level | `Required` |
| Applicability | `Applicable` |
| Provisional State | `Satisfied` — only for communicating licenses from the README |
| Implementation Characteristics | `Own`, `Specialized`, `Distributed` (descriptive) |
| Decision Status | `Needs Further Evaluation` |
| Adoption Decision | `—` |
| Framework Component availability | `Conceptual` |
| Full Template conformance | **Not evaluated** |

### Evaluation Rationale

The README explicitly communicates the applicable licenses for two sets of artifacts and links to their respective sources. For the bounded `README-LICENSE` purpose described in the Catalog, this Evidence **supports a provisional `Satisfied` evaluation**, despite the absence of a reusable canonical Framework Component.

`Applicable` is recorded because the consumer declares the distribution of content and code under explicit licenses. The implementation is `Own` because it is defined in the consumer, `Specialized` because it distinguishes artifact types, and `Distributed` because it separates license communication and license texts across README and license files.

The evaluation concerns **documentation, not legal compliance**: it does not exhaustively verify ownership, third-party resource licenses, or the legal sufficiency of each declaration.

### Uncertainty and Review

- No formal human review has been conducted within a complete Assessment.
- Additional licensing information mechanisms in the consumer have not been examined.
- Not all `TPL-DOCUMENTATION` conditions have been assessed.
- Descriptive characteristics do not constitute a closed contractual classification.
- There is no evidence of a decision by the `github/docs` team to adopt GitHub Framework.

For these reasons, **neither `PRESERVE`, `ACCEPT`, nor any other Adoption Decision is selected**. This case's Evidence must not be used to authorize changes to the consumer repository.

## 6. Hypothesis Comparison

| Hypothesis from #56 | Case Result | Limitation |
|---|---|---|
| A consumer can cover `README-LICENSE` through its own implementation. | **Supported** by concrete README license-communication Evidence. | One Responsibility and one consumer were reviewed. |
| A `Conceptual` classification implies `Missing` for every consumer. | **Not supported**: the case shows observable documentation coverage. | This does not replace the consumer Assessment. |
| The canonical Component must now be materialized. | **Not demonstrated**. | No user attempting to adopt this Template was observed. |
| The `README-LICENSE` requirement level should be downgraded. | **Not demonstrated**. | Communicating licenses has observable value; changing the requirement level needs its own Evidence. |
| The canonical gap makes the Template unusable. | **Not demonstrated**. | This case examines one Responsibility, not complete adoption. |

## 7. Findings

**LC-F01 — Responsibility coverage does not depend exclusively on the materialized Component library.** The case demonstrates the consumer's own differentiated license communication in its README.

**LC-F02 — The observed implementation may be distributed and specialized.** README, `LICENSE`, and `LICENSE-CODE` perform different, complementary functions.

**LC-F03 — Component availability and consumer State are independent dimensions.** The Evidence is compatible with `Conceptual` at the Framework level and provisional `Satisfied` at the consumer level.

**LC-F04 — No adoption friction was observed.** Document inspection can demonstrate that an implementation exists; it does not measure the difficulty of using or creating it through the Framework.

## 8. Discovery Decision and Next Steps

Keep the current contract:

```text
TPL-DOCUMENTATION v0.1.0
    README-LICENSE: Required
    Component classification: Conceptual
```

This case does not automatically justify creating `README-LICENSE`, reclassifying it, changing the Template, or announcing a new release.

**Useful next check:** investigate how a `TPL-DOCUMENTATION` user interprets the coexistence of `Required` and `Conceptual`, or review a second documentation consumer if a specific uncertainty arises. The absence of a canonical implementation becomes a product need only with Evidence of friction, repeatability, or reuse benefits.

Neither `github/docs` nor the Framework outside this document is modified. No Sprint or version is committed.

## 9. Conclusion

For `github/docs`, observable Evidence in its README and two license files **provisionally** supports coverage of `README-LICENSE` through an own, specialized, distributed implementation.

This separates **consumer conformance** from **canonical materialization availability in GitHub Framework**, avoiding the assumption that a Catalog gap automatically requires development.

**Result:** Evidence from a real documentation consumer, bounded to one Responsibility, with no implementation decision.
