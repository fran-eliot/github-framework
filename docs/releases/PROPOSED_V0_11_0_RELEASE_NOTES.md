# Approved Release Notes — v0.11.0: Framework Validator CLI and CI

> **VERSION AND RELEASE-NOTE CONTENT APPROVED — NOT PUBLISHED.** On 2026-11-15 the maintainer explicitly approved `v0.11.0 — Framework Validator CLI and CI` and these release notes. The final publication date, exact final release commit, tag creation and GitHub Release publication require **separate explicit approval**. The latest published version remains **v0.10.0**.

| Field | Approved choice or inspected evidence |
| --- | --- |
| Release title | **v0.11.0 — Framework Validator CLI and CI** — maintainer-approved 2026-11-15 |
| Publication date | **To be decided** |
| Current published baseline | `v0.10.0` (`3c4b21a26e4e85eeef705fefd48323ffd918e681`) |
| Option A | **Maintainer-approved complete-repository snapshot scope**, not Validator-only changes |
| Inspected candidate branch | [`candidate/option-a-snapshot-20261115`](https://github.com/fran-eliot/github-framework/tree/candidate/option-a-snapshot-20261115) |
| Inspected candidate commit (before this PR) | [`0df4704dad80871044e31bdfeebb29449bf17b0a`](https://github.com/fran-eliot/github-framework/commit/0df4704dad80871044e31bdfeebb29449bf17b0a) |
| Exact-SHA CI evidence | [Run 43706322266](https://github.com/fran-eliot/github-framework/actions/runs/43706322266) — success, Ubuntu and Windows |
| Consumer changes | **None** — Only Film source not modified |
| Version and notes | **Approved 2026-11-15**; publication approval **not provided** |

## 1. Version rationale

**Approved choice: v0.11.0**, a pre-1.0 minor increment following v0.10.0. The observable capabilities are improved **Framework Validator developer experience and CI**, together with substantial documentation and a completed *documentary* Adoption Assessment case study.

This is **not** a v1.0.0 stability release: the roadmap still lists v1.0.0 as planned, independent UX-02 evaluation remains `Prepared — Not Executed`, and automatic consumer Adoption decisions, repository mutation and full end-to-end consumer Application/Integration have **not** been delivered by this increment.

The maintainer approved this version and title on 2026-11-15. The legacy `PROPOSED_` filename records the document's origin and is **not** a claim that the approval is pending. The version is **not yet published**; the final commit, publication date and tag require separate approval.

## 2. Draft GitHub Release description (English)

### Highlights

This release strengthens the GitHub Framework Validator with repeatable cross-platform verification, more useful machine-readable diagnostics, and focused inspection or validation of individual Components.

The complete Framework snapshot also includes expanded Existing Repository Adoption guidance, historical Discovery and governance records, and a formally completed documentary Assessment of the external Only Film project at a pinned consumer commit.

### Added

- Automated **Framework Validator** tests and complete-library Component validation on GitHub Actions pull requests and pushes to `main`, covering **Ubuntu and Windows (Python 3.11)**.
- Downloadable per-platform **JSON validation reports**, GitHub Actions job summaries and file-linked error annotations.
- Targeted validation of individual Components through repeatable `--component FAMILY/NAME` arguments.
- Read-only Component catalog through `--list-components`, with family filtering, text/JSON output and optional `--details` metadata inventory.
- Automated **real-library CLI smoke checks**, including discovery of 21 Components, detailed metadata loading, family-restricted reports, targeted selection and rejection of an incompatible argument combination.
- Extensive documentary adoption evidence, including an explicitly approved **Only Film documentary Assessment** with **28/28** State/Applicability classifications and **28/28** Adoption Decisions resolved.

### Changed

- More detailed Validator JSON output, including individual Component statuses and errors, aggregate summary counts, portable relative paths and a clear distinction between full-library and filtered validation.
- Improved CLI output and JSON report writing for local use.
- Updated GitHub Actions dependencies to Node.js 24-compatible majors: `actions/checkout@v5`, `actions/setup-python@v6` and `actions/upload-artifact@v6`.
- Additional Adoption Guide, example, Discovery, project-governance and release-candidate documentation.

### Verification evidence

At inspected candidate commit [`0df4704dad80871044e31bdfeebb29449bf17b0a`](https://github.com/fran-eliot/github-framework/commit/0df4704dad80871044e31bdfeebb29449bf17b0a), [GitHub Actions run 43706322266](https://github.com/fran-eliot/github-framework/actions/runs/43706322266) completed successfully on Ubuntu and Windows:

- **161 unit tests passed** per operating system.
- The real-library CLI smoke check passed on both operating systems and reported **21 Component catalog entries**, **21 metadata entries loaded**, three checked Component families and three targeted Component validations.
- The full-library JSON reports, downloaded and reviewed separately, reported **21 Components passed, zero failed and zero errors** per operating system; normalized results matched.

These results apply to the **specified candidate commit**. If release documentation or other changes enter the candidate, obtain and review validation evidence for the **new exact release SHA** before publication.

### Scope and limitations

**Option A is a complete tracked-repository snapshot**, not a narrow Validator-only release. The candidate diff from `v0.10.0` contains **91 changed paths**, including **50 Only Film documentary evidence files**, **21 Discovery documents**, and project-governance material. Their inclusion must be acknowledged rather than silently presented as Validator functionality.

The Only Film case study is a **completed documentary Assessment**, using the immutable consumer SHA `28d75a50e0a178954dd46acc23300d9dd327843c` and `TPL-BACKEND 0.1.0`. It does **not** mean that Only Film was modified, migrated, integrated, security-certified or independently verified end-to-end. Historical CI evidence includes a bounded **329-test H2 job**, but a clean-clone Compose startup, Selenium execution, complete Maven suite, historical Sonar Quality Gate outcome and third-party reuse rights are **not established** by that evidence. The Framework repository's MIT license must not be represented as granting licenses over the external Only Film project's source.

Independent first-time UX-02 validation remains `Prepared — Not Executed`. No automatic Adoption decisions, consumer modifications, release automation or v1.0.0 stability certification are claimed.

### Useful links

- [Published v0.10.0 baseline](https://github.com/fran-eliot/github-framework/releases/tag/v0.10.0)
- [Inspected snapshot comparison](https://github.com/fran-eliot/github-framework/compare/v0.10.0...0df4704dad80871044e31bdfeebb29449bf17b0a)
- [Option A candidate evidence](OPTION_A_CANDIDATE_BASELINE.md)
- [Validator and UI documentation in English](../../README.md)
- [Validator and UI documentation in Spanish](../../README_es.md)
- [Only Film documentary Assessment](../../framework/adoption/examples/only-film-assessment.md)

## 3. Publication preparation and outstanding controls

**The maintainer approved the version/title and substance of these notes on 2026-11-15.** The five public documentation updates were integrated in PR #326: `CHANGELOG.md` remains **[Unreleased]**, both README version badges correctly continue to show **v0.10.0** (latest published), and ROADMAP/governance distinguish preparation from publication.

The confirmed candidate branch at the time of this approval is [`candidate/option-a-snapshot-20261115`](https://github.com/fran-eliot/github-framework/tree/candidate/option-a-snapshot-20261115), inspected at `0df4704dad80871044e31bdfeebb29449bf17b0a`. This approval-record change is **not yet included** in that pinned candidate; if it is to be published in Option A, the branch must be fast-forwarded to a newly reviewed commit and its exact-SHA CI/report evidence rechecked.

Before any tag or GitHub Release:

1. Confirm the exact final candidate SHA and complete Option A snapshot scope, including all documentary evidence and its limitations.
2. Check the final candidate's Ubuntu/Windows CI and smoke-test results and review the JSON validation reports at that SHA.
3. Obtain a distinct, explicit maintainer approval to **create the `v0.11.0` tag and publish the GitHub Release at the named SHA**, including the final release date and notes.
4. Synchronize release-published metadata (CHANGELOG version/date, README badges, roadmap/status), through a reviewed change if needed; do not mark publication completed beforehand.

The approved narrative **does not** authorize Only Film mutation, consumer Application/Integration, automatic Adoption decisions, a security/quality-gate certification, a new Sprint/milestone, or stable `v1.0.0` status.

## 4. Current decision state

| Question | State |
| --- | --- |
| Option A complete-tree release scope | **Approved** |
| Version `v0.11.0` and title | **Approved by maintainer, 2026-11-15** |
| Release-note content | **Approved by maintainer, 2026-11-15** |
| Public documentation preparation | **Integrated in PR #326**; not marked published |
| Current inspected candidate SHA | `0df4704dad80871044e31bdfeebb29449bf17b0a`; subject to final post-change revalidation |
| Final release date, final SHA and publication action | **Not yet authorized** |
| Create tag or GitHub Release | **Not authorized** |

**Next decision:** once the final candidate is verified, obtain the maintainer's express release GO for the exact SHA, date, tag and publication act.
