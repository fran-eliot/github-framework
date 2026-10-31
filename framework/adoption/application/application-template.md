# Existing Repository Adoption — Application Record

Este template registra una Application concreta del **Existing Repository Adoption — Application Core**.

Debe utilizarse después de un Assessment con:

```text
Decision Status
    Resolved
```

La representación es deliberadamente:

```text
Markdown
human-readable
human-editable
Git-reviewable
usable without tooling
```

No constituye un schema, manifest ni machine contract.

---

## 1. Application Context

**Consumer Repository:**  
<!-- Repository name or URL -->

**Consumer Reference:**  
<!-- Branch, tag, commit SHA or equivalent reference -->

**Repository Template:**  
<!-- Example: TPL-BACKEND -->

**Repository Template Version:**  
<!-- Template version used by the source Assessment -->

**Assessment Reference:**  
<!-- Path, link or stable reference to the source Assessment -->

**Application Date:**  
<!-- YYYY-MM-DD -->

**Application Scope:**  
<!-- Short description of the selected Application scope -->

---

## 2. Selected Responsibility

**Responsibility:**  

**Requirement Level:**  

**State:**  
<!-- Satisfied / Partial / Missing -->

**Applicability:**  
<!-- Applicable / Not Applicable / Uncertain -->

**Implementation Characteristics:**  
<!-- Optional; preserve source Assessment wording when relevant -->

**Decision Status:**  
<!-- Must normally be Resolved before Application -->

**Adoption Decision:**  
<!-- PRESERVE / ADAPT / ADD / ACCEPT / OMIT -->

**Decision Rationale:**

> 

---

## 3. Current Assessment Outcome

Summarize only the Assessment information needed to understand this Application.

**Assessment Evidence Summary:**

- 
- 

**Assessment Conclusion:**

> 

Do not silently reinterpret the complete Assessment here.

If current Evidence materially contradicts the Assessment, record it in **Evidence Refresh** and use `REPLAN` when appropriate.

---

## 4. Evidence Refresh

Refresh the Evidence needed for the selected Responsibility before any mutation.

### Current Facts

- 
- 

### Current Evidence

| Evidence | Location / Reference | Observation |
| --- | --- | --- |
|  |  |  |
|  |  |  |

### Differences from Assessment

- None observed.

### Evidence Freshness Result

Candidate descriptive values:

```text
CURRENT
STALE
INSUFFICIENT
```

**Result:**  

**Rationale:**

> 

Current consumer state takes precedence over stale assumptions.

Do not invent missing facts.

---

## 5. Application Intent

Describe the semantic outcome this Application should produce.

> 

The Intent should explain the desired result, not only the physical edit.

Example:

```text
Align backend execution documentation
with current runtime configuration
while preserving valid README content.
```

Avoid:

```text
Edit README.md
```

---

## 6. Application Readiness

Application Readiness is descriptive and provisional.

**Readiness:**  
<!-- READY / NOT READY / DEFERRED -->

**Rationale:**

> 

A resolved Adoption Decision does not automatically imply that mutation is currently justified.

---

## 7. Candidate Change Set

Complete this section when mutation is planned.

If no mutation is justified, record:

```text
Change Set
    NONE
```

### Change Set

| Change ID | Target | Operation | Expected Change |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

Supported operations:

```text
CREATE
MODIFY
```

Unsupported as stable operations:

```text
DELETE
MOVE
RENAME
```

### Change Set Boundary

**What may change:**

- 
- 

**What must not change:**

- 
- 

---

## 8. Preservation Scope

Record valid consumer state that must remain preserved.

### Content / Implementation Preservation

- 
- 

### Repository Structure Preservation

- 
- 

### Consumer Convention Notes

Examples:

```text
language
terminology
naming
documentation style
repository-local organization
```

- 
- 

Preservation Scope must not protect the exact state that Application Intent needs to change.

---

## 9. Risk / Conflict Notes

| Risk / Conflict | Evidence | Impact | Planned Response |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

Examples:

```text
stale assumptions
target changed since Assessment
equivalent implementation appeared
unsupported historical information
consumer convention mismatch
overlapping Change Set
```

Automatic semantic conflict resolution is outside the current Application Core.

---

## 10. Verification Plan

Define verification before APPLY.

### Expected Changes

- 
- 

### Expected Preservation

- 
- 

### Intent Verification

- 
- 

### PASS Evidence

- 
- 

### REFINE Conditions

- 
- 

### FAIL Conditions

- 
- 

---

## 11. Plan Review

### Review Checklist

- [ ] Selected Responsibility is explicit.
- [ ] Decision Status is `Resolved`.
- [ ] Evidence Refresh is current enough for this Application.
- [ ] Application Intent is explicit.
- [ ] Candidate Change Set is bounded, or no Change Set is justified.
- [ ] Preservation Scope is explicit.
- [ ] Unsupported facts have not been invented.
- [ ] Risks / Conflicts are understood.
- [ ] Verification Plan is feasible.
- [ ] Unsupported operations are not required.

### Plan Review Result

Select one:

```text
PROCEED
NO CHANGE
REPLAN
DEFER
REJECTED
```

**Result:**  

**Review Rationale:**

> 

Only `PROCEED` moves to APPLY.

---

## 12. Application Result

Select one:

```text
APPLIED
NO CHANGE
REPLAN
DEFER
REJECTED
```

**Application Result:**  

**Result Rationale:**

> 

### Non-Mutation Outcome

Complete when the result is `NO CHANGE`, `REPLAN`, `DEFER` or `REJECTED`.

**Why no mutation was performed:**

> 

**Recommended next action:**

> 

`NO CHANGE` is a valid Application outcome and does not imply failure.

---

## 13. Applied Change Evidence

Complete only when:

```text
Application Result
    APPLIED
```

### Candidate State

**Isolation Mechanism:**  

**Candidate Reference:**  

### Changed Artifacts

| Artifact | Change ID | Operation | Result |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |

### Diff Summary

> 

### Unexpected Changes

- None observed.

APPLIED does not imply VERIFIED.

---

## 14. Verification Result

Complete after APPLY.

### Physical Verification

**Result:**  
<!-- PASS / REFINE / FAIL -->

**Evidence:**

- 
- 

### Intent Verification

**Result:**  
<!-- PASS / REFINE / FAIL -->

**Evidence:**

- 
- 

### Preservation Verification

**Result:**  
<!-- PASS / REFINE / FAIL -->

**Evidence:**

- 
- 

### Semantic Verification

**Previous State:**  

**Candidate State:**  

**Rationale:**

> 

### Overall Verification Result

Select one:

```text
PASS
REFINE
FAIL
```

**Result:**  

**Verification Rationale:**

> 

---

## 15. Refinement Notes

Complete when:

```text
Verification Result
    REFINE
```

### Refinement Reason

> 

### Bounded Refinement

| Change ID | Target | Adjustment | Why it remains within Intent |
| --- | --- | --- | --- |
|  |  |  |  |

### Re-Verification

**Physical Verification:**  

**Intent Verification:**  

**Preservation Verification:**  

**Overall Result:**  
<!-- PASS / REFINE / FAIL -->

Do not create a new Adoption Decision unless new Evidence materially changes the original problem.

---

## 16. Final Candidate State

Select one:

```text
VERIFIED
DISCARDED
DEFERRED
REPLAN REQUIRED
```

**Final Candidate State:**  

**Candidate Reference:**  

**Rationale:**

> 

This state describes the candidate Application outcome.

It does not mean the change has been integrated into stable consumer state.

---

## 17. Conclusion

### Application Summary

**Responsibility:**  

**Adoption Decision:**  

**Application Intent:**  

**Application Result:**  

**Verification Result:**  
<!-- Leave not applicable for non-mutation outcomes when no VERIFY occurred -->

**Final Candidate State:**  

### Preservation Summary

> 

### Remaining Risks / Uncertainty

- 
- 

### Next Step

> 

Possible next steps:

```text
preserve verified candidate for review
discard candidate
replan
defer
return to Assessment
```

`INTEGRATE` is outside the current Application Core.

---

# Completion Rules

An Application Record is complete when the sections required by its actual outcome are filled.

## Always Required

```text
Application Context
Selected Responsibility
Current Assessment Outcome
Evidence Refresh
Application Intent
Preservation Scope
Risk / Conflict Notes
Verification Plan
Plan Review
Application Result
Conclusion
```

## Required when Mutation is Planned

```text
Candidate Change Set
```

## Required when Application Result = APPLIED

```text
Applied Change Evidence
Verification Result
Final Candidate State
```

## Required when Verification Result = REFINE

```text
Refinement Notes
Re-Verification
```

## Valid without Mutation

The same template supports:

```text
NO CHANGE
REPLAN
DEFER
REJECTED
```

without requiring a fictitious Change Set, commit or Verification Result.

---

# Supported Representation Scenarios

## Scenario A — ADAPT / MODIFY

```text
Decision
    ADAPT

Operation
    MODIFY

Application Result
    APPLIED

Verification Result
    PASS

Final Candidate State
    VERIFIED
```

## Scenario B — ADD / CREATE / REFINE

```text
Decision
    ADD

Operation
    CREATE

Application Result
    APPLIED

Verification Result
    REFINE
        ↓
bounded adjustment
        ↓
VERIFY AGAIN
        ↓
PASS

Final Candidate State
    VERIFIED
```

## Scenario C — ADAPT / NO CHANGE or REPLAN

```text
Decision
    ADAPT

Evidence Refresh
    insufficient for justified mutation

Change Set
    NONE

Application Result
    NO CHANGE
        or
    REPLAN

Final Candidate State
    REPLAN REQUIRED
        or
    DEFERRED
```

---

# Scope Boundaries

This template does not define or require:

```text
INTEGRATE
automatic merge
automatic remediation
automatic conflict resolution
DELETE
MOVE
RENAME
CLI
GitHub Actions
parser
schema
Structured Data contract
Application Manifest
post-integration rollback
```

It records a human-reviewed Application up to a verified or safely stopped candidate state.

---

# References

Application process and boundaries:

```text
framework/adoption/application/README.md
```

Delivery Scope and Implementation Plan:

```text
docs/discovery/35_APPLICATION_DELIVERY_SCOPE.md
docs/discovery/36_APPLICATION_IMPLEMENTATION_PLAN.md
```

Assessment artifacts:

```text
framework/adoption/README.md
framework/adoption/assessment-template.md
```
