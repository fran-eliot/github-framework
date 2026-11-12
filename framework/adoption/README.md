# Existing Repository Adoption

The **Existing Repository Adoption** capability provides reusable guidance for assessing an existing repository against the Responsibilities defined by a GitHub Framework Repository Template. Optionally, a resolved Adoption Decision can progress to a verified candidate state and then be integrated into the consumer's stable state.

The current release provides three lifecycle capabilities and one optional, cross-cutting Evidence support capability:

```text
Existing Repository Adoption
    Assessment Core
        ↓
    optional Application Core
        ↓
    optional Integration Core

Assisted Analysis
    optional evidence support
    across Assessment / Application / Integration
```

Assessment Core supports analyzing, assessing, reviewing, and documenting Adoption Decisions.

Application Core supports planning, applying bounded changes in isolation, and verifying justified changes.

Integration Core supports reviewing and integrating a verified candidate into the consumer's stable state, following the consumer's governance and verifying the resulting stable state.

Assisted Analysis supports deterministic, bounded, source-traceable, read-only Evidence collection across these stages. It does not replace semantic evaluation or human decisions.

### Your First Assessment: Minimal Walkthrough

To get started with an existing repository **without modifying it**:

1. **Choose a Template.** Explore the [Repository Template Library](../templates/repositories/README.md) and select one that matches the consumer. For example, [TPL-BACKEND](../templates/repositories/backend/README.md) may fit a backend service.
2. **Pin the contract.** Read the Template's guidance and obtain its `id` and `version` from canonical metadata (for example, [TPL-BACKEND metadata](../templates/repositories/backend/metadata.yml)). The Template version is distinct from the Framework's release version.
3. **Pin the consumer.** Record the repository URL and an exact commit SHA. A mutable branch name alone is insufficient for reproducible Evidence.
4. **Create a working record.** Copy the [Assessment Template](assessment-template.md) to your own working file. Fill in `Consumer Repository`, `Consumer Reference`, `Repository Template`, `Template Version`, date, and `Assessment Status: In Progress`.
5. **Start with facts.** Choose one Responsibility declared by the Template, inspect relevant artifacts, and record `Detected Facts` and commit-pinned `Evidence` references. Do not infer a Decision from the presence or absence of a particular filename.
6. **Evaluate explicitly.** Record `State`, `Applicability`, `Implementation Characteristics`, `Uncertainty`, and `Evaluation Rationale`. If Evidence or review is insufficient, keep `Decision Status: Needs Further Evaluation` and `Adoption Decision: —`.
7. **Save the partial result.** Documenting one Responsibility is a **starting point**, not a complete Assessment. Before setting `Complete`, cover and review the Responsibilities required by the selected Template under this Guide's completion rules.

**What's next?** Only a reviewed, resolved Adoption Decision may proceed to [Application](application/README.md), which refreshes Evidence and requires a plan and verification before isolated changes. [Integration](integration/README.md) subsequently requires a verified candidate and stable-base review. [Assisted Analysis](assisted-analysis/README.md) optionally supports read-only Evidence collection, not automated decisions.

**Worked examples:** the [first Assessment example](examples/first-assessment-example.md) covers one Responsibility in SeniorMeet. The [Only Film two-Responsibility walkthrough](examples/only-film-two-responsibilities.md) demonstrates commit-pinned Evidence for Quick Start and Testing in a second consumer. Both remain `In Progress`; neither is a complete Assessment or a validated Adoption Decision.

**Repeatability replay:** the [cross-consumer Assessment comparison](examples/cross-consumer-repeatability-replay.md) applies the same `README-QUICK-START` review structure to both examples, with explicit documentary acceptance checks and outstanding operational verifications. It does not certify either consumer or resolve Adoption Decisions.

**Assessment coverage:** the [Only Film TPL-BACKEND coverage matrix](examples/only-film-assessment-coverage.md) inventories all 28 Template Responsibilities and separates five provisional documentary explorations from 23 not-yet-assessed items. The [first required-README batch](examples/only-film-required-readme-batch-1.md) documents observed facts for Hero, Overview, and Features without resolving semantic decisions. These are planning and review aids, not a complete Assessment.

This walkthrough is guidance only. It does not generate repositories, execute assessments, or replace human review.
---

## 1. Purpose

Existing Repository Adoption addresses a different problem from creating a new repository.

An existing repository may:

- already implement a Responsibility through a canonical artifact;
- satisfy it through an equivalent implementation;
- distribute it across several artifacts;
- cover it only partially;
- not implement it;
- not require it in its specific context.

Existing Repository Adoption therefore emphasizes:

```text
reconciliation
```

rather than:

```text
generation
replacement
automatic remediation
```

Assessment Core aims to produce an evaluation that is:

```text
usable
repeatable
traceable
reviewable
persistent
```

while explicitly retaining human review.

---

## 2. Scope

The supported process is:

```text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
```

The outcome is a persistent Markdown Assessment preserving:

```text
Detected Facts
Evidence
Evaluation
Uncertainty
Adoption Decisions
Rationale
```

Assessment Core does not modify the consumer repository.

Once an Adoption Decision is resolved, Application Core may optionally continue with:

```text
SELECT
    ↓
REFRESH EVIDENCE
    ↓
DEFINE APPLICATION INTENT
    ↓
PLAN
    ↓
REVIEW PLAN
    ↓
APPLY IN ISOLATION
    ↓
VERIFY
    ↓
REVIEW RESULT
```

The Application Core boundary is a verified candidate state.

When a verified candidate state exists, Integration Core may optionally continue with:

```text
REFRESH STABLE BASE
    ↓
EVALUATE DRIFT
    ↓
CHECK INTEGRATION CONDITIONS
    ↓
REVIEW
    ↓
INTEGRATE
    ↓
VERIFY STABLE STATE
    ↓
CONFIRM
```

The Integration Core boundary is a verified stable state or a safe-stop / recovery-required state.

---

## 3. Assessment Inputs

Every Assessment starts with four conceptual inputs:

```text
Existing Consumer Repository

Repository Template

Repository Template Version

Consumer Reference
```

### Existing Consumer Repository

The repository to be assessed.

It serves as the:

```text
evidence source
```

### Repository Template

The Repository Template selected as the Assessment reference.

For selection, consult the [Repository Template Library](../templates/repositories/README.md) and the intended usage criteria of the chosen Template. For example, [TPL-BACKEND](../templates/repositories/backend/README.md) targets backend services and applications. The project type alone does not establish that the Template's Responsibilities have been satisfied.

It serves as the:

```text
assessment baseline
```

### Repository Template Version

Identifies the specific Template version used.

Confirm the ID and version in the selected Template's canonical metadata. For the backend example, see [`TPL-BACKEND/metadata.yml`](../templates/repositories/backend/metadata.yml). The Template version is independent of the published GitHub Framework version.

The Assessment must always be interpreted against that version.

### Consumer Reference

Identifies the exact consumer state being evaluated.

For example:

```text
branch
commit SHA
tag
```

The reference must be precise enough to avoid treating a historical Assessment as automatically valid for any future state of the repository.

---

## 4. Assessment Principles

### 4.1 Evidence before Automation

Assessment Core prioritizes explicit Evidence and human review over any future automation.

```text
Evidence
    before
Automation
```

### 4.2 Responsibility over File

The evaluation unit is:

```text
Responsibility
```

not:

```text
File
```

Therefore:

```text
Canonical Artifact Missing
    ≠
Responsibility Missing
```

A Responsibility may be satisfied by a non-canonical implementation.

### 4.3 Human Review Remains Explicit

The Assessment keeps observation, evaluation, and decision separate:

```text
Detected Fact
    ≠
Evaluated State
    ≠
Adoption Decision
```

A deterministic check may provide Evidence, but it cannot replace semantic evaluation.

### 4.4 Reconciliation over Replacement

Existing Repository Adoption must first interpret what the consumer already does.

The absence of a canonical structure does not, by itself, require replacing an existing solution.

---

## 5. Assessment Model

For each Responsibility, the following dimensions are recorded and evaluated:

```text
Responsibility
Requirement Level
Detected Facts
Evidence
State
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
Decision Status
Adoption Decision
Decision Rationale
```

These dimensions must not be collapsed into one another.

In particular:

```text
State
    ≠
Applicability
    ≠
Adoption Decision
```

---

## 6. Process

### 6.1 ANALYZE

The purpose of ANALYZE is to identify observable information about the consumer.

Record:

```text
Detected Facts
Evidence
```

without deciding which Adoption action is appropriate yet.

Examples of Detected Facts:

```text
README.md exists

docs/ directory is absent

OpenAPI configuration exposes API documentation

repository-level LICENSE file is not present
```

A Detected Fact must be verifiable.

It must not contain a semantic conclusion.

```text
Fact
    ≠
Evaluation
```

### 6.2 ASSESS

The purpose of ASSESS is to interpret Evidence against the Responsibility.

Evaluate:

```text
State
Applicability
Implementation Characteristics
Uncertainty
Evaluation Rationale
```

### 6.3 REVIEW

The purpose of REVIEW is to determine whether the evaluation can be justified.

The review must consider:

```text
evidence sufficiency
semantic interpretation
non-canonical implementations
uncertainty
applicability
```

Review is particularly important when a Responsibility is implemented using structures that differ from those defined canonically by the Template.

### 6.4 DECIDE

The purpose of DECIDE is to record whether a decision can be resolved and, when possible, which disposition is appropriate.

Record:

```text
Decision Status
Adoption Decision
Decision Rationale
```

### 6.5 REPORT

Preserve the completed Assessment as a:

```text
persistent Markdown outcome
```

The same artifact can serve as:

```text
working assessment
+
review artifact
+
persistent report
```

No separate Generated Report is required.

---

## 7. Detected Facts

Detected Facts contain verifiable observations about the consumer.

They must describe:

```text
what exists
what does not exist
what configuration is present
what repository structure is observable
```

They must not express:

```text
whether the Responsibility is satisfied
what should be changed
which Adoption Decision should be selected
```

---

## 8. Evidence

Evidence connects the Assessment to observable consumer material.

It may reference:

```text
file paths
repository sections
configuration
source code
generated documentation
repository structure
```

The general rule is:

```text
minimal sufficient evidence
```

Preserve enough Evidence for another person to review the evaluation without unnecessarily copying large amounts of consumer content.

---

## 9. Responsibility State

State represents only:

```text
current responsibility coverage
```

The stable vocabulary is:

### `Satisfied`

The Responsibility is sufficiently covered in the consumer.

This may be achieved through a canonical or non-canonical implementation.

### `Partial`

The Responsibility is only partially covered.

A relevant implementation may exist, but some required coverage is missing.

### `Missing`

The Responsibility is not covered by the observed Evidence.

State does not represent:

```text
future action
applicability
priority
```

---

## 10. Applicability

Applicability indicates whether a Responsibility is relevant to the specific consumer.

The stable vocabulary is:

### `Applicable`

The Responsibility is relevant to the consumer.

### `Not Applicable`

The Responsibility is not needed in the evaluated context.

### `Uncertain`

There is insufficient Evidence or context to determine applicability yet.

Applicability must be evaluated independently from State.

For example:

```text
State
    Missing

Applicability
    Not Applicable

Decision
    OMIT
```

is a valid outcome.

---

## 11. Implementation Characteristics

Implementation Characteristics describe non-canonical implementations when that information helps interpret a Responsibility correctly.

The provisional vocabulary observed during Discovery is:

```text
Canonical
Own
Equivalent
Specialized
Distributed
```

This vocabulary is:

```text
provisional
descriptive
non-exclusive
```

A Responsibility may have:

```text
zero
one
or several
```

Implementation Characteristics.

These categories help describe how a Responsibility is implemented, especially when its implementation differs from the canonical materialization expected by the Repository Template.

They are not a closed taxonomy or a conformance contract.

Therefore:

```text
Implementation Characteristic
    supports interpretation
```

but does not, on its own, determine:

```text
State
Applicability
Adoption Decision
```

Evidence and Evaluation Rationale must preserve enough context to interpret any Implementation Characteristic used.

---

## 12. Documentation Evaluation

The physical presence of documentation does not, by itself, demonstrate that a Responsibility is satisfied.

The following distinction must be preserved:

```text
Documentation Exists
    ≠
Responsibility Satisfied
```

Depending on the Responsibility, evaluation may require checking:

```text
presence
correctness
coverage
current relevance
```

An existing but incorrect, incomplete, or outdated file may result in a State other than `Satisfied`.

---

## 13. Uncertainty

Where applicable, Uncertainty must record:

```text
what is unknown
why it cannot currently be resolved
what evidence would resolve it
```

Do not use:

```text
confidence score
probability
Low / Medium / High
```

Uncertainty must be expressed through concrete, reviewable information.

---

## 14. Evaluation Rationale

Evaluation Rationale answers:

> Why does the observed Evidence support the recorded State, Applicability, and interpretation?

It must explain the evaluation without anticipating any future action.

Therefore:

```text
Evaluation Rationale
    explains the assessment
```

while:

```text
Decision Rationale
    explains the adoption decision
```

These concepts must remain separate.

---

## 15. Decision Status

Decision Status indicates whether an Adoption Decision can be resolved at the time of the Assessment.

The stable vocabulary is:

### `Resolved`

There is sufficient Evidence and context to record an Adoption Decision.

### `Needs Further Evaluation`

The decision cannot be safely resolved using the available information.

Decision Status:

```text
is not
an Adoption Decision
```

When a Responsibility requires additional evaluation, preserve:

```text
Evidence
Uncertainty
Evaluation Rationale
reason for unresolved decision
```

without forcing an artificial Adoption Decision.

---

## 16. Adoption Decisions

The stable Adoption Decision vocabulary is:

```text
PRESERVE
ADAPT
ADD
ACCEPT
OMIT
```

### `PRESERVE`

Retain the existing implementation because it adequately satisfies the Responsibility and does not require modification for the purpose being assessed.

### `ADAPT`

Modify an existing implementation to cover the Responsibility adequately.

### `ADD`

Add a necessary implementation or artifact because the Responsibility requires additional coverage.

### `ACCEPT`

Consciously accept an existing non-canonical implementation when it is appropriate for the Responsibility and its context.

### `OMIT`

Do not introduce the expected materialization because the Responsibility is not applicable or because there is an explicit, reviewed reason for omitting it.

---

## 17. No Automatic State → Decision Mapping

The same State and Applicability combination may lead to different decisions depending on:

```text
Requirement Level
Implementation Characteristics
Evidence
Context
Rationale
```

Therefore:

```text
State
    +
Requirement Level
    +
Applicability
    +
Implementation Characteristics
    +
Evidence
    +
Context
    +
Rationale
        ↓
Adoption Decision
```

Automatic rules such as:

```text
Satisfied → PRESERVE

Partial → ADAPT

Missing → ADD
```

must not be applied without contextual evaluation.

---

## 18. `EVALUATE`

`EVALUATE` is not part of the stable Adoption Decision vocabulary.

The need it previously represented is expressed through:

```text
Decision Status
    Needs Further Evaluation
```

This allows an evaluated Responsibility to be retained without inventing a final disposition.

---

## 19. `JUSTIFY`

`JUSTIFY` is likewise not part of the stable Adoption Decision vocabulary.

The need to preserve justification is covered by:

```text
Evaluation Rationale
+
Decision Rationale
```

No additional decision type is needed to represent that a conclusion requires justification.

---

## 20. Decision Rationale

Decision Rationale answers:

> Why is this Adoption Decision appropriate given the Assessment?

It must connect the decision with:

```text
State
Applicability
Implementation Characteristics
Evidence
context
```

without turning these dimensions into automatic rules.

Valid examples:

```text
Satisfied
+
Equivalent
+
ACCEPT
```

and:

```text
Missing
+
Not Applicable
+
OMIT
```

---

## 21. Assessment Completion

An Assessment may be marked:

```text
Complete
```

when all Responsibilities defined by the selected Repository Template have been evaluated.

Each Responsibility must include:

```text
State
Applicability
Evidence
Evaluation Rationale
Decision Status
```

When:

```text
Decision Status
    Resolved
```

the following must also be present:

```text
Adoption Decision
Decision Rationale
```

When:

```text
Decision Status
    Needs Further Evaluation
```

the following must be present:

```text
Uncertainty
rationale explaining
why the decision remains unresolved
```

---

## 22. Complete Does Not Mean Fully Resolved

Maintain the distinction:

```text
Assessment Complete
    ≠
All Adoption Decisions Resolved
```

An Assessment may be complete while some Responsibilities remain:

```text
Needs Further Evaluation
```

provided that the uncertainty and the reason for each unresolved decision are adequately documented.

`Complete` indicates that the Assessment has evaluated all expected Responsibilities.

It does not certify that every decision is resolved.

---

## 23. Human Review

Existing Repository Adoption Assessment records a traceable human evaluation.

It is not:

```text
automated certification
```

Review should specifically verify:

- sufficiency of Evidence;
- consistency between Evidence and State;
- independence of State and Applicability;
- recognition of equivalent or distributed implementations;
- unresolved uncertainty;
- consistency between evaluation and Adoption Decision;
- sufficiency of Evaluation Rationale and Decision Rationale.

Future validation may assist with deterministic checks, but cannot replace the semantic review defined by this Assessment Core.

---

## 24. Using the Assessment Template

The reusable artifact for recording an Assessment is:

```text
framework/adoption/assessment-template.md
```

The relationship between the two artifacts is:

```text
Guide
    explains
        how and why

Template
    records
        what was assessed
```

Recommended workflow:

```text
1. Copy the Assessment Template
        ↓
2. Complete Assessment Context
        ↓
3. ANALYZE each Responsibility
        ↓
4. ASSESS State and Applicability
        ↓
5. REVIEW Evidence and interpretation
        ↓
6. DECIDE or mark Needs Further Evaluation
        ↓
7. Complete the Assessment Conclusion
        ↓
8. Preserve the assessment as the reviewable outcome
```

This delivery does not impose a:

```text
consumer storage path
mandatory completed-assessment filename
```

---

## 25. Persistent Outcome

A completed Assessment must preserve sufficient context to remain interpretable later.

At minimum, it must identify:

```text
Consumer Repository
Consumer Reference
Repository Template
Template Version
Assessment Date
Assessment Status
```

The persistent outcome documents:

```text
what was observed
how it was evaluated
what remains uncertain
what decisions were made
why those decisions were made
```

---

### 25.1 Application Core

The reusable Application Core is documented in:

```text
framework/adoption/application/README.md
```

The artifact for recording an individual Application is:

```text
framework/adoption/application/application-template.md
```

The relationship between these two cores is:

```text
Assessment Core
    understands and decides
        ↓
optional Application Core
    plans, applies in isolation and verifies
```

Application consumes an Adoption Decision with:

```text
Decision Status
    Resolved
```

and maintains the following principles:

```text
Evidence before Mutation
Reconciliation over Replacement
Responsibility over Artifact
Bounded Change
Preservation
Human Review
No Mutation is a Valid Outcome
```

Application Core supports:

```text
CREATE
MODIFY
NO CHANGE
REPLAN
DEFER
REJECTED
```

and Verification Results:

```text
PASS
REFINE
FAIL
```

---

### 25.2 Integration Core

The reusable Integration Core is documented in:

```text
framework/adoption/integration/README.md
```

The artifact for recording an individual Integration is:

```text
framework/adoption/integration/integration-template.md
```

The relationship between the three capabilities is:

```text
Assessment Core
    understands and decides
        ↓
optional Application Core
    plans, applies in isolation and verifies
        ↓
optional Integration Core
    accepts into stable state and verifies
```

Integration consumes:

```text
verified candidate state
```

and maintains the following principles:

```text
Verified Candidate before Integration
Refresh Stable Base
Evaluate Drift Impact
Consumer Governance over Framework Merge Preference
Mergeability is not Integration Readiness
Human Review before Stable Integration
Verify Stable State after Integration
Represent Recovery without Automating it
```

Integration Core supports the following decisions:

```text
INTEGRATE
DEFER
REPLAN
REJECT
```

and final states:

```text
INTEGRATED
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

This capability does not configure consumer governance, prescribe a universal merge strategy, or automate recovery.

### 25.3 Assisted Analysis Core

The reusable Assisted Analysis Core is documented in:

```text
framework/adoption/assisted-analysis/README.md
```

The artifact for recording an individual Evidence Snapshot is:

```text
framework/adoption/assisted-analysis/evidence-snapshot-template.md
```

Assisted Analysis is not a fourth lifecycle stage.

Its relationship to Existing Repository Adoption is cross-cutting:

```text
                 Assisted Analysis
                 ┌──────┼──────┐
                 ↓      ↓      ↓
Assessment    Application    Integration
```

It can support:

```text
Assessment
    Detected Facts + Evidence

Application
    Evidence Refresh

Integration
    Stable Base Refresh Evidence
    Integration-condition Evidence
```

It maintains the following principles:

```text
Facts before Evaluation
Evidence before Decision
Read-Only before Mutation
Explicit Collection Scope
Source Traceability
Collection Gaps are Visible
Human Review owns Semantic Meaning
Representation before Tooling
```

The reusable representation is:

```text
Structured Markdown Evidence Snapshot
```

Assisted Analysis does not automatically produce:

```text
Responsibility State
Applicability
Adoption Decision
Application Result
Drift Impact
Integration Review
Integration Decision
Final Integration State
```

Nor does it introduce a CLI, GitHub Actions, consumer mutation, Schema, Manifest, Componentization, or Framework Validator extension.

## 26. Out of Scope

Existing Repository Adoption does not document or implement stable procedures for:

```text
automatic merge
automatic remediation
automatic semantic assessment
automatic Adoption Decisions
automatic semantic conflict resolution

DELETE
MOVE
RENAME

component installation

CLI
parser
schema
Structured Data contract
Adoption Manifest

Framework Validator integration
GitHub Actions integration

repository generation

continuous reassessment
drift detection

automatic post-integration rollback
```

Nor does it turn Existing Repository Adoption into a new Component family.

This delivery does not require:

```text
metadata.yml
Component Catalog integration
mandatory metadata contract
```

Excluded capabilities may return to Discovery if sufficient Evidence emerges to justify including them.

---

## 27. Interpretation Boundaries

Existing Repository Adoption Assessment must avoid the following automatic inferences:

```text
file exists
    ⇒
Responsibility Satisfied
```

```text
canonical file missing
    ⇒
Responsibility Missing
```

```text
State
    ⇒
Adoption Decision
```

```text
assessment complete
    ⇒
all decisions resolved
```

```text
assessment result
    ⇒
automatic conformance certification
```

Every conclusion must remain supported by explicit Evidence and rationale.

---

## 28. Operational Summary

Assessment Core can be summarized as:

```text
Existing Consumer Repository
        +
Repository Template
        ↓
ANALYZE
        ↓
ASSESS
        ↓
REVIEW
        ↓
DECIDE
        ↓
REPORT
        ↓
Persistent Human-Reviewed Assessment
```

The conceptual sequence for each Responsibility is:

```text
Detected Facts
        ↓
Evidence
        ↓
State
+
Applicability
+
Implementation Characteristics
+
Uncertainty
        ↓
Evaluation Rationale
        ↓
Decision Status
        ↓
Adoption Decision
        ↓
Decision Rationale
```

when the decision can be resolved.

If it cannot be resolved:

```text
Decision Status
    Needs Further Evaluation

+
Uncertainty

+
Rationale
```

without forcing an Adoption Decision.

---

## 29. References

Assessment Core definition and planning are documented in:

```text
docs/discovery/29_ADOPTION_DELIVERY_SCOPE.md
docs/implementation/30_ADOPTION_IMPLEMENTATION_PLAN.md
```

Application Core definition and planning are documented in:

```text
docs/discovery/35_APPLICATION_DELIVERY_SCOPE.md
docs/discovery/36_APPLICATION_IMPLEMENTATION_PLAN.md
```

Integration Core definition and planning are documented in:

```text
docs/discovery/41_INTEGRATION_DELIVERY_SCOPE.md
docs/discovery/42_INTEGRATION_IMPLEMENTATION_PLAN.md
```

Assisted Analysis Core definition and planning are documented in:

```text
docs/discovery/50_ASSISTED_ANALYSIS_DELIVERY_SCOPE.md
docs/implementation/51_ASSISTED_ANALYSIS_IMPLEMENTATION_PLAN.md
```

The experimental Evidence supporting this capability remains in:

```text
docs/discovery/
```

Reusable Existing Repository Adoption artifacts are located in:

```text
framework/adoption/
```
