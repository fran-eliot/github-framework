# Existing Repository Adoption — Integration Record

> Reusable Structured Markdown Template for reviewing, executing and verifying one Integration from a verified candidate state into stable consumer state.

---

## 1. Integration Context

| Field | Value |
| --- | --- |
| Consumer Repository | |
| Stable Target | |
| Integration Owner / Reviewer | |
| Integration Date | |
| Related Assessment | |
| Related Application Record | |
| Responsibility | |
| Requirement Level | |

### Context Notes

Document the minimum context needed to understand why this Integration exists.

Do not copy the full Assessment or Application history when a reference is sufficient.

---

## 2. Candidate Reference

| Field | Value |
| --- | --- |
| Candidate State | VERIFIED |
| Candidate Branch / Reference | |
| Candidate Commit / Revision | |
| Pull Request / Equivalent | |
| Candidate Artifacts | |

### Candidate Verification Evidence

```text
Verification Result:
Evidence Reference:
Verified At:
```

The Integration Core begins only from a:

```text
verified candidate state
```

If the candidate is not verified:

```text
STOP
    ↓
return to Application
```

---

## 3. Application Outcome

| Field | Value |
| --- | --- |
| Adoption Decision | |
| Application Operation | |
| Application Result | |
| Application Verification | |
| Application Intent | |
| Preservation Scope Reference | |

### Application History

Use this section to record relevant history such as:

```text
direct PASS
```

or:

```text
REFINE → PASS
```

Do not rewrite the Application Record.

---

## 4. Stable Base Reference

| Field | Value |
| --- | --- |
| Stable Branch / Target | |
| Original Stable Base | |
| Current Stable Reference | |
| Stable Reference Captured At | |

### Stable Target Notes

Record the stable target that would receive the candidate if Integration proceeds.

Examples:

```text
main
master
release branch
equivalent stable target
```

No specific branch name is required by the Framework.

---

## 5. Stable Base Refresh

### Refresh Result

| Field | Value |
| --- | --- |
| Base Drift | NONE / PRESENT |
| Relevant Stable Changes | |
| Candidate Target Still Exists | YES / NO / N/A |
| Candidate Still Mergeable / Applicable | YES / NO / UNKNOWN |

### Refresh Evidence

```text
Current Stable Reference:
Compared With:
Relevant Changes:
Evidence:
```

Stable Base Refresh is mandatory before Integration.

A previous verification does not prove current Integration readiness.

---

## 6. Drift Impact

> Complete this section when Base Drift is PRESENT. Otherwise record N/A.

### Drift Evaluation

| Dimension | Result | Evidence / Rationale |
| --- | --- | --- |
| Target Overlap | YES / NO / UNKNOWN | |
| Application Intent Still Valid | YES / NO / UNCERTAIN | |
| Preservation Scope Still Valid | YES / NO / UNCERTAIN | |
| Governance Changed | YES / NO / UNKNOWN | |
| Release Constraints Changed | YES / NO / UNKNOWN | |

### Drift Impact Result

```text
NONE
COMPATIBLE
INVALIDATING
UNCERTAIN
```

Selected result:

```text

```

### Drift Rationale

Explain why current drift does or does not invalidate Integration.

Base drift alone must not automatically trigger REPLAN.

---

## 7. Integration Conditions

Record only conditions relevant to the consumer repository.

| Condition | Required? | Current Result | Evidence |
| --- | :---: | --- | --- |
| Mergeability | | | |
| Required Reviews | | | |
| Required Checks | | | |
| Workflow Runs | | | |
| Branch Protection | | | |
| Base Freshness | | | |
| Release Constraints | | | |
| Other | | | |

### Conditions Summary

```text
SATISFIED
NOT SATISFIED
UNCERTAIN
```

Selected result:

```text

```

Do not invent controls that the consumer repository does not use.

---

## 8. Governance Constraints

> Contextual section. Record only observed repository governance.

Possible constraints include:

```text
required approvals
CODEOWNERS
required checks
linear history
direct push restrictions
merge strategy restrictions
release freeze
release branch policy
```

### Observed Constraints

| Constraint | Evidence | Impact on Integration |
| --- | --- | --- |
| | | |

### Governance Assessment

```text
Consumer Governance
    over
Framework Merge Preference
```

The Integration Core records and respects consumer governance.

It does not configure or override it.

---

## 9. Integration Review

Review the candidate before any stable mutation.

### Review Checklist

| Review Question | Result | Evidence / Rationale |
| --- | --- | --- |
| Candidate remains verified | PASS / FAIL / UNCERTAIN | |
| Stable base was refreshed | PASS / FAIL | |
| Drift impact is understood | PASS / FAIL / N/A | |
| Application Intent remains valid | PASS / FAIL / UNCERTAIN | |
| Preservation Scope remains valid | PASS / FAIL / UNCERTAIN | |
| Integration Conditions are satisfied | PASS / FAIL / UNCERTAIN | |
| Consumer Governance is satisfied | PASS / FAIL / UNCERTAIN | |
| Candidate remains within approved scope | PASS / FAIL | |

### Integration Review Result

```text
PROCEED
DEFER
REPLAN
REJECT
```

Selected result:

```text

```

### Review Rationale

Explain why the selected Review Result is justified.

Only:

```text
PROCEED
```

permits Integration.

---

## 10. Integration Decision

### Decision

```text
INTEGRATE
DEFER
REPLAN
REJECT
```

Selected decision:

```text

```

### Decision Rationale

Explain the decision using current Evidence.

### Safe-Stop Rules

When the decision is:

```text
DEFER
REPLAN
REJECT
```

do not create fictitious:

```text
Integration Method
Integration Evidence
merge reference
stable mutation
```

---

## 11. Integration Method

> Required only when Integration Decision = INTEGRATE.

| Field | Value |
| --- | --- |
| Stable Target | |
| Integration Method | |
| Platform / Mechanism | |
| Integration Reference | |

Examples of methods:

```text
merge commit
squash merge
rebase merge
equivalent platform operation
```

The Framework does not prescribe one universal merge strategy.

---

## 12. Integration Evidence

> Required only when Integration occurred.

| Evidence | Value |
| --- | --- |
| Stable Mutation Reference | |
| Merge Commit / Equivalent | |
| Changed Artifacts | |
| Integration Summary | |
| Integrated At | |

### Evidence Notes

Integration Evidence proves that stable mutation occurred.

It does not prove that the resulting stable state is correct.

```text
Integration Evidence
    ≠
Stable-State Verification
```

---

## 13. Stable-State Verification

Stable-State Verification is required after Integration.

For a safe-stop decision with no stable mutation, record:

```text
NOT APPLICABLE — NO INTEGRATION OCCURRED
```

### Physical Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Expected stable change is present | PASS / FAIL / N/A | |
| Expected artifact state is present | PASS / FAIL / N/A | |
| Unexpected target changes are absent | PASS / FAIL / N/A | |

### Intent Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Application Intent is satisfied in stable state | PASS / FAIL / N/A | |

### Preservation Verification

| Check | Result | Evidence |
| --- | --- | --- |
| Preservation Scope remains intact | PASS / FAIL / N/A | |
| Consumer conventions remain intact | PASS / FAIL / N/A | |
| Previously verified unrelated state remains intact | PASS / FAIL / N/A | |

### Repository Health Verification

> Contextual. Use only when relevant.

| Check | Result | Evidence |
| --- | --- | --- |
| Tests | PASS / FAIL / N/A | |
| Build | PASS / FAIL / N/A | |
| Lint | PASS / FAIL / N/A | |
| Required Checks | PASS / FAIL / N/A | |
| Other | PASS / FAIL / N/A | |

### Stable-State Verification Result

```text
PASS
FAIL
NOT APPLICABLE — NO INTEGRATION OCCURRED
```

Selected result:

```text

```

---

## 14. Recovery Notes

> Required when Stable-State Verification = FAIL or Final Integration State = RECOVERY REQUIRED. Otherwise record N/A.

### Recovery Requirement

```text
YES
NO
N/A
```

Selected result:

```text

```

### Failure Evidence

Describe what failed after Integration.

### Impact

Describe the known impact on stable state.

### Manual Recovery Notes

Possible recovery mechanisms may include:

```text
revert commit
revert merge
follow-up fix
branch reset
release rollback
```

These are observations or manual options only.

The Integration Core does not execute:

```text
automatic revert
automatic rollback
recovery orchestration
```

---

## 15. Final Integration State

Select one:

```text
INTEGRATED
DEFERRED
REPLAN REQUIRED
REJECTED
RECOVERY REQUIRED
```

Selected state:

```text

```

### State Consistency Rules

#### INTEGRATED

Requires:

```text
Integration Decision
    INTEGRATE

Integration occurred

Stable-State Verification
    PASS
```

#### DEFERRED

Requires:

```text
Integration Decision
    DEFER

stable mutation
    NOT EXECUTED
```

#### REPLAN REQUIRED

Requires:

```text
Integration Decision
    REPLAN

stable mutation
    NOT EXECUTED
```

#### REJECTED

Requires:

```text
Integration Decision
    REJECT

stable mutation
    NOT EXECUTED
```

#### RECOVERY REQUIRED

Requires:

```text
Integration occurred

Stable-State Verification
    FAIL
```

---

## 16. Conclusion

### Integration Summary

Summarize:

- what candidate was reviewed;
- whether stable base changed;
- whether Integration Conditions were satisfied;
- what Integration Decision was taken;
- whether stable mutation occurred;
- the Stable-State Verification result;
- the Final Integration State.

### Traceability

Preserve the chain:

```text
Assessment Outcome
    ↓
Application Record
    ↓
Verified Candidate
    ↓
Integration Review
    ↓
Integration Decision
    ↓
Integration Evidence
    ↓
Stable-State Verification
    ↓
Final Integration State
```

### Completion Check

An Integration Record is complete when:

- all mandatory sections are populated;
- conditional sections are populated when applicable;
- no unsupported fact is invented;
- safe-stop outcomes contain no fictitious stable mutation evidence;
- successful Integration includes Integration Evidence;
- successful Integration includes Stable-State Verification;
- failed stable verification produces RECOVERY REQUIRED when applicable;
- final state and conclusion are explicit.

---

# Template Usage Rules

## Mandatory Information

Always required:

```text
Integration Context
Candidate Reference
Application Outcome
Stable Base Reference
Stable Base Refresh
Integration Conditions
Integration Review
Integration Decision
Stable-State Verification
Final Integration State
Conclusion
```

## Conditional Information

Required only when applicable:

```text
Drift Impact
    when drift exists

Integration Method
Integration Evidence
    when Integration occurs

Recovery Notes
    when verification fails
    or recovery is required
```

## Contextual Information

Record only when relevant:

```text
Governance Constraints
Release Constraints
Repository Health Evidence
```

## Representation Boundary

This Template remains:

```text
Markdown
human-readable
human-editable
Git-reviewable
usable without tooling
```

It does not require:

```text
JSON
YAML
Schema
Manifest
parser
typed Integration Plan
machine API
```

## Automation Boundary

This Template does not authorize:

```text
automatic merge
automatic approval
automatic conflict resolution
automatic rollback
release orchestration
branch protection configuration
```
