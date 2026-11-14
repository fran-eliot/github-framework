# Only Film — Adoption Decision review batch 5: Changelog and optional README governance

## Review basis and guardrails

| Field | Value |
| --- | --- |
| Consumer | [fran-eliot/only_film](https://github.com/fran-eliot/only_film) |
| Immutable assessed reference | `28d75a50e0a178954dd46acc23300d9dd327843c` |
| Template | `TPL-BACKEND` `0.1.0` |
| Responsibilities | `DOC-CHANGELOG` (Required), `README-CONTRIBUTING` (Optional), `README-ROADMAP` (Optional) |
| Approved State / Applicability pairs | `28/28`, unchanged |
| Previously resolved Adoption Decisions | `8/28`, all `PRESERVE` |
| Unresolved Adoption Decisions | `20/28`, including the three in this packet |
| Assessment | `In Progress` |
| Consumer mutation | `NONE` |

This **preapproval review packet** distinguishes observed documentary `State`, independent `Applicability`, and a possible `Adoption Decision`. Each suggested decision requires **subsequent explicit maintainer approval**; merging this preparation document or saying `go` is not approval. The [Assessment Template](../assessment-template.md) supports `PRESERVE`, `ADAPT`, `ADD`, `ACCEPT`, and `OMIT` for justified resolved decisions, while `Needs Further Evaluation / —` can remain open. Neither a Template requirement level nor a `Missing` State mechanically selects `ADD` or `OMIT`.

## Candidate decision comparison

| Responsibility | Approved State / Applicability | Reviewer-facing candidate | Evidence threshold and scope |
| --- | --- | --- | --- |
| `DOC-CHANGELOG` | `Missing / Applicable` | **Keep `Needs Further Evaluation / —` as default**, with **`ADD` as a conditional, bounded candidate** | Choose whether an `Unreleased` curated record provides genuine value before the first identified release; establish source, audience and maintenance policy, without fabricating tags/releases/version history |
| `README-CONTRIBUTING` | `Missing / Not Applicable` | **Consider `OMIT`** | The maintainer expressly confirmed a **personal project with no external contributions**; keep the technical onboarding content without inventing a contributor acceptance policy or requiring `CONTRIBUTING.md` |
| `README-ROADMAP` | `Partial / Applicable` | **Keep `Needs Further Evaluation / —` as default** | Future ideas in the README are not current commitments; the F3 roadmap's older baseline does not establish which planned issues were completed at the pinned SHA |

**Important:** `OMIT` for `README-CONTRIBUTING` would be an Assessment choice **not to introduce an external contributor policy for the maintainer-confirmed project scope**; it would not delete the already present Maven, CI or local development guidance. `ADD` for `DOC-CHANGELOG` would be a **possible future Application-stage choice**, not an immediate file creation or retrospective release invention.

## 1. DOC-CHANGELOG — Required but no automatic `ADD`

### Source observations

- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) distinguishes academic origins, subsequent technical evolution and future work, but does not itself present curated version-to-version change communication.
- The [pinned POM](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml) declares `0.0.1-SNAPSHOT`. This is **not** evidence of a published version, tag or GitHub Release.
- The earlier [pinned Changelog evidence review](only-film-changelog-evidence-review.md) inspected filenames and sections, found no identified equivalent curated changelog and noted that a fetch of `CHANGELOG.md` at the pinned reference returned 404. Filename/path evidence does **not** prove exhaustive absence of alternatives or independently verify all tags.
- The maintainer **reported on 2026-11-13** that there were no releases or tags; this is separately attributed **maintainer testimony**, not a successful immutable Git tag inventory. A prior mutable Releases endpoint review returned an empty list; do not infer a universal, permanent absence.
- The [Framework Changelog Component](../../components/documentation/changelog/README.md) allows `Unreleased` entries, but also explicitly says a separate changelog may not be necessary in very short-lived projects or where no differentiated releases exist. Commits, PRs, roadmap and project status do not automatically constitute a curated changelog.

### Decision alternatives

- **`Needs Further Evaluation / —` (recommended default):** Before committing to a maintained change log, identify its real audience, useful granularity, prospective maintenance owner, and whether the project is preparing its first public release. Check any maintained alternative change record as needed.
- **`ADD` (conditional):** If the maintainer actively chooses to publish a new curated change record, the scoped downstream application could **start** with an accurately sourced `Unreleased` section, link to relevant evidence, and define an ongoing update policy. This decision must not invent historical releases, claim a complete chronology from raw commits, or imply the file already exists.
- **`ACCEPT` or `PRESERVE` (alternative only with rationale):** The maintainer might deliberately accept the currently missing changelog as adequate for a non-released portfolio project, or identify a genuinely equivalent maintained source. If selecting `ACCEPT`, explicitly describe that this accepts an outstanding `Missing` Responsibility; do **not** silently relabel it `Satisfied`.
- **`ADAPT` (only if warranted):** An identified genuine equivalent change record might require a narrow correction; none is established here.

### Reviewer question

Does maintaining a separate curated `Unreleased` change record serve actual future readers **now**, or should the choice remain pending until a real release strategy and audience exist? The Required classification remains `Missing / Applicable` either way; no file is created in Only Film under this Assessment.

## 2. README-CONTRIBUTING — strong `OMIT` candidate

### Source observations

- The maintainer **expressly confirmed on 2026-11-14** that Only Film is a **personal project that does not accept outside contributions**. This is the direct basis for the already approved `Applicability: Not Applicable`, separately from the previously approved `State: Missing`.
- The [pinned README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md) already provides environment setup, tests, workflow guidance and source orientation. These are useful **technical onboarding** instructions but do not declare outside contributor eligibility, PR acceptance/review criteria, or a contribution governance program.
- The earlier [Optional Responsibility source spot-check](only-film-optional-contract-spotcheck.md) could not find a `CONTRIBUTING.md`, `.github/CONTRIBUTING.md` or `.github/PULL_REQUEST_TEMPLATE.md` at the specific pinned paths. It was a **bounded path-specific inspection** and does not prove all policy alternatives are absent.
- The Framework `TPL-BACKEND` marks this Responsibility `Optional`. Optionality by itself would **not** establish `Not Applicable` or select `OMIT`; here the evidence is the maintainer's explicit contribution model.

### Decision alternatives

**Consider `Resolved / OMIT`** to intentionally **not add** a separate external contributor guidance responsibility under the current personal, no-outside-contributions model. The recorded rationale should say that nothing is being removed from Only Film, that existing technical onboarding stays available, and that the decision would need reconsideration if project policy later welcomes contributors.

`PRESERVE` is less precise because no substantive external contributor policy was evidenced under the approved `State: Missing`. `ADD` would contradict the confirmed project scope unless the maintainer expressly revises that policy. `OMIT` must not be interpreted as a `Not Applicable` State or a deletion instruction.

### Reviewer question

Does the maintainer explicitly select **`OMIT`** for external-contribution policy documentation while continuing to retain the README's technical onboarding guidance?

## 3. README-ROADMAP — future possibilities are not present milestones

### Source observations

- The pinned README's `Próximas líneas de evolución` lists possible REST API, payment-provider integration, observability, deployment automation and maintenance improvements. It explicitly labels these as **potential**, not implemented or scheduled.
- The historical [F3 functional audit and roadmap](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/F3_FUNCTIONAL_AUDIT_AND_ROADMAP.md) is based on `df63353564485eb6d2d60c982032e5d3c4facbf2`. The status of F3.002–F3.008 at the pinned assessed SHA is not reconstructed in this review.
- The [Framework README-ROADMAP Component](../../components/readme/roadmap/README.md) expects a concise outline of upcoming phases, without duplicating a detailed roadmap. It does not create a new delivery commitment or require dates.
- The approved `Partial / Applicable` assessment captures the real future-ideas section while retaining uncertainty about current priority, phase sequencing, milestones and source freshness.

### Decision alternatives

**Default: `Needs Further Evaluation / —`.** A conditional `PRESERVE` could accept the existing explicitly **noncommittal ideas list** as sufficient for the intended portfolio audience, without declaring a maintained roadmap or current phase. A conditional `ADAPT` would require a specific verified stale description or an actual current and maintainable next-phase plan. No historical F3 item should be presumed open or closed.

### Reviewer question

Should the README remain a nonbinding list of future ideas, or is there an independently supported current phase that the maintainer actually wants to communicate? No new dates, priorities or feature guarantees are authorized by this packet.

## Formal review gate and follow-up

The reviewer should approve or decline each candidate **independently**. Recommended initial choices for separate maintainer sign-off:

- `DOC-CHANGELOG = Needs Further Evaluation / —`; `ADD` remains a **conditional** choice if a curated `Unreleased` change record is genuinely desired and supported.
- `README-CONTRIBUTING = OMIT`, limited to external contributor policy under the maintainer-confirmed no-outside-contributions model.
- `README-ROADMAP = Needs Further Evaluation / —` pending an actual planning/audience rationale.

If the maintainer formally approves any decision, record the chosen allowed token, reviewer, date, source-specific rationale and evidence limits in the canonical [Assessment](only-film-assessment.md), [consolidated matrix](only-film-consolidated-review-matrix.md) and this packet through a **subsequent, separate PR**. A resolved `OMIT` decision is a documentary scope choice, not removal of any consumer file.

**Unchanged boundaries:** 28/28 State/Applicability approvals; 8/28 prior resolved `PRESERVE` decisions, 20 still unresolved; Assessment `In Progress`; no consumer file, branch, setting, workflow or other mutation.
