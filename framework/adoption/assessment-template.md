# Existing Repository Adoption Assessment

> Reusable Structured Markdown Assessment Template for GitHub Framework Existing Repository Adoption.
>
> Guidance for completing this assessment is available in `framework/adoption/README.md`.

---

## 1. Assessment Context

| Field | Value |
|---|---|
| Consumer Repository | `<repository>` |
| Consumer Reference | `<branch / commit SHA / tag>` |
| Repository Template | `<template>` |
| Template Version | `<version>` |
| Assessment Date | `<YYYY-MM-DD>` |
| Assessment Status | `In Progress` |

Supported Assessment Status values:

```text
In Progress
Complete
```

---

## 2. Assessment Summary

| Responsibility | Requirement Level | State | Applicability | Decision Status | Adoption Decision |
|---|---|---|---|---|---|
| `<Responsibility>` | `<level>` | `<Satisfied / Partial / Missing>` | `<Applicable / Not Applicable / Uncertain>` | `<Resolved / Needs Further Evaluation>` | `<PRESERVE / ADAPT / ADD / ACCEPT / OMIT / —>` |

Add one row for every Responsibility included in the selected Repository Template.

When:

```text
Decision Status
    Needs Further Evaluation
```

the Adoption Decision may remain unresolved and may be represented as:

```text
—
```

---

## 3. Responsibility Details

Duplicate the following block for each Responsibility.

---

### `<Responsibility>`

**Requirement Level**

`<requirement level>`

**State**

`<Satisfied / Partial / Missing>`

**Applicability**

`<Applicable / Not Applicable / Uncertain>`

**Implementation Characteristics**

`<none / one or more descriptive characteristics>`

The provisional descriptive vocabulary observed during Discovery includes:

```text
Canonical
Own
Equivalent
Specialized
Distributed
```

This vocabulary is not a closed taxonomy.

**Uncertainty**

```text
<what is unknown, why it cannot currently be resolved, and what evidence would help resolve it>

Use "None identified" when no material uncertainty remains.
```

**Detected Facts**

- `<verifiable observation>`
- `<verifiable observation>`

**Evidence**

- `<minimal sufficient reference to file, repository section, configuration, source code, generated documentation, or repository structure>`
- `<additional evidence when necessary>`

**Evaluation Rationale**

```text
<explain why the Evidence supports the recorded State, Applicability and interpretation>
```

**Decision Status**

`<Resolved / Needs Further Evaluation>`

**Adoption Decision**

`<PRESERVE / ADAPT / ADD / ACCEPT / OMIT / —>`

If:

```text
Decision Status
    Resolved
```

record one stable Adoption Decision.

If:

```text
Decision Status
    Needs Further Evaluation
```

the Adoption Decision may remain:

```text
—
```

**Decision Rationale**

```text
<when resolved, explain why the Adoption Decision is appropriate given the assessment>

<when unresolved, explain why a final decision cannot yet be made>
```

---

## 4. Assessment Conclusion

### Assessment Status

`<In Progress / Complete>`

### Major Findings

- `<major finding>`
- `<major finding>`

### Open Uncertainties

- `<open uncertainty>`
- `<open uncertainty>`

Use:

```text
None identified
```

when no material uncertainty remains.

### Recommended Next Review

```text
<describe any review that would be useful after new evidence, context or repository changes become available>

Use "None currently required" when no follow-up review is needed.
```

---

## 5. Optional Aggregate Counts

This section is optional.

### State Totals

| State | Count |
|---|---:|
| Satisfied | `<count>` |
| Partial | `<count>` |
| Missing | `<count>` |

### Applicability Totals

| Applicability | Count |
|---|---:|
| Applicable | `<count>` |
| Not Applicable | `<count>` |
| Uncertain | `<count>` |

### Decision Totals

| Adoption Decision | Count |
|---|---:|
| PRESERVE | `<count>` |
| ADAPT | `<count>` |
| ADD | `<count>` |
| ACCEPT | `<count>` |
| OMIT | `<count>` |
| Needs Further Evaluation | `<count>` |

The aggregate counts are informational only and are not required for a valid assessment.

---

## Completion Check

An assessment may be marked:

```text
Complete
```

when every Responsibility in scope has been assessed.

Each Responsibility must record:

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

also record:

```text
Adoption Decision
Decision Rationale
```

When:

```text
Decision Status
    Needs Further Evaluation
```

preserve:

```text
Uncertainty
rationale explaining why the decision remains unresolved
```

Therefore:

```text
Assessment Complete
    ≠
All Adoption Decisions Resolved
```

---

## Template Boundaries

This template is:

```text
human-readable
human-editable
Markdown-based
```

It is not:

```text
machine-readable metadata
schema
parser input contract
automation hook
implementation backlog
application plan
automatic conformance certification
```

It does not define:

```text
consumer storage policy
mandatory completed-assessment filename
```

The assessment records human-reviewed evaluation and decisions. It does not modify the consumer repository.
