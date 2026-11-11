# 54 — First-Time Usability Validation Protocol

| Field | Value |
|---|---|
| Project | GitHub Framework |
| Preparation date | 2026-11-11 |
| Status | Prepared — Not Executed |
| Experiment | UX-02 — First-Time Usability Validation |
| Framework reference | `main` after PR #90; pin a commit SHA at execution time |
| Previous Discovery | [53_FIRST_TIME_USER_EXPERIENCE_DISCOVERY.md](53_FIRST_TIME_USER_EXPERIENCE_DISCOVERY.md) |
| Proposed consumer | [fran-eliot/seniormeet](https://github.com/fran-eliot/seniormeet) |
| Consumer reference | `b84b0de246d459caf594a5cdacbe8fccfa68698a` |
| Template baseline | `TPL-BACKEND v0.1.0` (`Experimental`, `L2`) |

> This document defines a **research protocol**, not the results of testing with participants. It does not commit a Delivery Scope, Sprint, milestone, version, or consumer modification.

---

## 1. Context and Previous Evidence

UX-01 identified an insufficiently explicit entry path connecting the README, the Repository Template Library, and the Assessment Template. It also confirmed that the Templates and their canonical metadata exist.

PR #90 added links and orientation to both public READMEs and the Adoption Guide. UX-02 aims to **check the user journey after that change**, without assuming that the friction has disappeared for newcomers.

Primary references:

- [README (EN)](../../README.md) and [README (ES)](../../README_es.md)
- [Repository Template Library](../../framework/templates/repositories/README.md)
- [Existing Repository Adoption Guide](../../framework/adoption/README.md)
- [Assessment Template](../../framework/adoption/assessment-template.md)
- [TPL-BACKEND README](../../framework/templates/repositories/backend/README.md)
- [TPL-BACKEND metadata](../../framework/templates/repositories/backend/metadata.yml)
- [UX-01 Discovery](53_FIRST_TIME_USER_EXPERIENCE_DISCOVERY.md)

## 2. Research Questions

**RQ-01 — Discovery.** Can a newcomer distinguish between creating a repository and assessing an existing one?

**RQ-02 — Navigation.** Can they find the Template Library and the path to Existing Repository Adoption without facilitator hints?

**RQ-03 — Selection.** Can they choose a Repository Template with a justification and obtain its version from canonical metadata?

**RQ-04 — Preparation.** Can they correctly start the Assessment Context using a reproducible consumer reference?

**RQ-05 — Comprehension.** Can they distinguish Detected Facts, Evidence, Evaluated State, and Adoption Decision?

**RQ-06 — Effort.** What questions, backtracking, or requests for assistance actually arise during the journey?

## 3. Study Design and Boundaries

### 3.1 Method

An individual, moderated observational study with tasks based on a practical case. Participants navigate GitHub and explain what they are trying to do; the facilitator observes without revealing paths, answers, or filenames before the tasks are completed.

**Proposed exploratory sample:** 2–3 developers with general GitHub repository experience but no previous involvement in GitHub Framework. One participant can provide qualitative Evidence; this small sample cannot estimate population-level rates or demonstrate the absence of usability problems.

If independent participants are unavailable, the experiment remains **Not Executed**. An author simulation, document inspection, or guided session must not be recorded as independent user-study results.

### 3.2 Preparation

- Pin the commit SHA of `github-framework/main` at the start of each session so subsequent changes do not alter the observed journey.
- Use the same public README and Adoption Guide versions for all participants in a given round.
- Give participants the root URL `https://github.com/fran-eliot/github-framework` and the consumer URL; **do not** provide the path to the Template, its ID, version, or the Assessment Template.
- Keep `seniormeet` read-only, pinned to commit `b84b0de246d459caf594a5cdacbe8fccfa68698a`.
- Avoid granting write access to the consumer. If context must be recorded, use a private temporary copy or session notes, not commits.
- Obtain consent for note-taking before participation, and separate consent if recording is requested. Do not publish names, personal information, or recordings in the public repository.

### 3.3 Exclusions

Do not assess all 28 Responsibilities, perform Application or Integration, or run the Framework Validator as a substitute for an Assessment. Do not measure the consumer's overall quality. Do not modify SeniorMeet's code, dependencies, README, or configuration.

## 4. Facilitator Script

### Context Provided to the Participant

> You want to use GitHub Framework to understand how to improve an existing backend repository, without modifying it yet. The repository you will examine is SeniorMeet. You start from the GitHub Framework homepage. Use only the public documentation to identify where to begin and prepare the context for an initial assessment.

Do not mention `TPL-BACKEND`, `metadata.yml`, or the paths that participants are expected to discover beforehand.

### Tasks

| ID | Participant Task | Evidence of Success |
|---|---|---|
| T1 | Identify the appropriate path for an existing repository. | Distinguishes Adoption from the new-repository path. |
| T2 | Find the Repository Template options and choose one for SeniorMeet. | Locates the Library and justifies the backend type using Template criteria. |
| T3 | State the ID and version of the selected Template and show their source. | Consults canonical metadata; does not infer the version from the overall Framework release. |
| T4 | Find the artifact for recording an assessment and describe its initial fields. | Locates the Assessment Template and identifies its context fields. |
| T5 | Record the consumer and a reproducible reference in session notes. | Uses the repository and commit SHA without changing the consumer. |
| T6 | Formulate two verifiable observations about the consumer without deciding what to change. | Separates facts/Evidence from State, Applicability, and Adoption Decision. |

Tasks may be marked completed, completed with assistance, incomplete, or not applicable due to an earlier blocker. Avoid embedding answers in the task instructions.

### Facilitator Intervention

- Allow questions clarifying the objective without giving away paths.
- If a participant becomes blocked, first record the difficulty and the help requested.
- If a hint is essential, record exactly when and what assistance was provided; mark the remainder of the session as **assisted**.
- Do not silently correct responses; ask what source supports each answer.
- At the end, ask which step was most confusing and what documentation was missing, without suggesting specific solutions.

## 5. Evidence Capture Matrix

Repeat for each session without publishing identifying information:

| Field | Session Value |
|---|---|
| Participant code | `P01` / `P02` / `P03` |
| Date / language | Pending |
| Framework commit SHA | Pending |
| GitHub experience | General, non-identifying description |
| Previous Framework experience | Must be none |
| Consent for notes | Pending |
| Recorded? | No by default |
| Overall result | Pending |

| Task | Status (unassisted / assisted / blocked / N/A) | Observed path and Evidence | Question / Backtracking | Exact Assistance | Comments |
|---|---|---|---|---|---|
| T1 | Pending | — | — | — | — |
| T2 | Pending | — | — | — | — |
| T3 | Pending | — | — | — | — |
| T4 | Pending | — | — | — | — |
| T5 | Pending | — | — | — | — |
| T6 | Pending | — | — | — | — |

Record short quotations only if they were actually spoken. Never invent participant testimony, timings, or participants. Click counts or elapsed minutes may be recorded if observed, but must not be inferred or turned into a universal success threshold.

## 6. Interpretation Criteria

### 6.1 Observation Classification

- **Navigation:** cannot find a resource or chooses an incorrect path.
- **Terminology:** confuses Framework concepts or boundaries.
- **Task support:** understands the objective but does not know what to do next.
- **Artifact comprehension:** locates a file but incorrectly interprets its purpose.
- **No issue observed:** completes the task without observable difficulty; this is not a usability guarantee.

Each observation must include the task, Evidence, context, facilitator intervention, and degree of uncertainty.

### 6.2 Separation of Outcomes

```text
Observed behavior
    ≠
Interpretation
    ≠
Validated need
    ≠
Selected solution
    ≠
Committed delivery
```

One individual's difficulty may justify further investigation. Recurrence across sessions strengthens a hypothesis, but does not automatically turn a documentation or code change into an approved requirement.

### 6.3 Comparison with UX-01

Compare UX-F01, UX-F02, UX-F03, UX-F05, and UX-F10 in particular. UX-F08 was resolved when the canonical Template definition was verified; do not reopen it without new Evidence. PR #90 addresses the observed **documentation link**, but does not by itself demonstrate independent user comprehension.

## 7. Template for Subsequent Synthesis (Empty)

**Execution status:** `Not Executed`

**Sessions completed:** `0`

**Available Evidence:** protocol and historical UX-01 findings; no observations of new users.

| Question | Result | Evidence | Confidence |
|---|---|---|---|
| RQ-01 | Pending | — | — |
| RQ-02 | Pending | — | — |
| RQ-03 | Pending | — | — |
| RQ-04 | Pending | — | — |
| RQ-05 | Pending | — | — |
| RQ-06 | Pending | — | — |

**New findings:** Pending.

**Validated / unvalidated / uncertain needs:** Pending.

**Subsequent decision:** Pending; do not select solutions before observing results.

## 8. Closing and Next Decision

This protocol enables a small, reproducible study without expanding GitHub Framework's technical scope. Actual execution requires real participants and retained Evidence; the document alone **does not validate the user experience**.

If participants are unavailable, an internal document review may be conducted separately and labeled as such, but must not be presented as UX-02 execution.

This protocol does not open a Sprint, milestone, release, or Delivery Scope.
