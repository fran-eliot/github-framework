# Proposed Release — v0.11.0: Framework Validator CLI and CI

> **DRAFT — PROPOSAL ONLY.** This is a proposed next version and draft release announcement for maintainer review. The version, release title, publication date, release notes, tag and GitHub Release have **not** been approved or published. The latest published GitHub Framework version remains **v0.10.0**.

| Field | Proposed value or verified reference |
| --- | --- |
| Release title | **v0.11.0 — Framework Validator CLI and CI** *(proposed)* |
| Publication date | **To be decided** |
| Current published baseline | `v0.10.0` (`3c4b21a26e4e85eeef705fefd48323ffd918e681`) |
| Option A | **Maintainer-approved complete-repository snapshot scope**, not Validator-only changes |
| Inspected candidate branch | [`candidate/option-a-snapshot-20261115`](https://github.com/fran-eliot/github-framework/tree/candidate/option-a-snapshot-20261115) |
| Candidate snapshot commit reviewed for this proposal | [`56a24418c63e097a01db00472b31f80ed641f789`](https://github.com/fran-eliot/github-framework/commit/56a24418c63e097a01db00472b31f80ed641f789) |
| Exact-SHA CI evidence | [Run 43703461574](https://github.com/fran-eliot/github-framework/actions/runs/43703461574) — success, Ubuntu and Windows |
| Consumer changes | **None** — Only Film source not modified |
| Final release approval | **Not yet provided** |

## 1. Version rationale

**Recommendation: v0.11.0**, a pre-1.0 minor increment following v0.10.0. The observable capabilities are improved **Framework Validator developer experience and CI**, together with substantial documentation and a completed *documentary* Adoption Assessment case study.

This is **not** a v1.0.0 stability release: the roadmap still lists v1.0.0 as planned, independent UX-02 evaluation remains `Prepared — Not Executed`, and automatic consumer Adoption decisions, repository mutation and full end-to-end consumer Application/Integration have **not** been delivered by this increment.

The version and name are **options for maintainer approval**, not committed repository metadata. A final release may select a different version/title and should not be inferred from the draft filename.

## 2. Draft GitHub Release description (English)

### Highlights

This proposed release strengthens the GitHub Framework Validator with repeatable cross-platform verification, more useful machine-readable diagnostics, and focused inspection or validation of individual Components.

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

At inspected candidate commit [`56a24418c63e097a01db00472b31f80ed641f789`](https://github.com/fran-eliot/github-framework/commit/56a24418c63e097a01db00472b31f80ed641f789), [GitHub Actions run 43703461574](https://github.com/fran-eliot/github-framework/actions/runs/43703461574) completed successfully on Ubuntu and Windows:

- **161 unit tests passed** per operating system.
- The real-library CLI smoke check passed on both operating systems and reported **21 Component catalog entries**, **21 metadata entries loaded**, three checked Component families and three targeted Component validations.
- The full-library JSON reports, downloaded and reviewed separately, reported **21 Components passed, zero failed and zero errors** per operating system; normalized results matched.

These results apply to the **specified candidate commit**. If release documentation or other changes enter the candidate, obtain and review validation evidence for the **new exact release SHA** before publication.

### Scope and limitations

**Option A is a complete tracked-repository snapshot**, not a narrow Validator-only release. The candidate diff from `v0.10.0` contains **90 changed paths**, including **50 Only Film documentary evidence files**, **21 Discovery documents**, and project-governance material. Their inclusion must be acknowledged rather than silently presented as Validator functionality.

The Only Film case study is a **completed documentary Assessment**, using the immutable consumer SHA `28d75a50e0a178954dd46acc23300d9dd327843c` and `TPL-BACKEND 0.1.0`. It does **not** mean that Only Film was modified, migrated, integrated, security-certified or independently verified end-to-end. Historical CI evidence includes a bounded **329-test H2 job**, but a clean-clone Compose startup, Selenium execution, complete Maven suite, historical Sonar Quality Gate outcome and third-party reuse rights are **not established** by that evidence. The Framework repository's MIT license must not be represented as granting licenses over the external Only Film project's source.

Independent first-time UX-02 validation remains `Prepared — Not Executed`. No automatic Adoption decisions, consumer modifications, release automation or v1.0.0 stability certification are claimed.

### Useful links

- [Published v0.10.0 baseline](https://github.com/fran-eliot/github-framework/releases/tag/v0.10.0)
- [Proposed snapshot comparison](https://github.com/fran-eliot/github-framework/compare/v0.10.0...56a24418c63e097a01db00472b31f80ed641f789)
- [Option A candidate evidence](OPTION_A_CANDIDATE_BASELINE.md)
- [Validator and UI documentation in English](../../README.md)
- [Validator and UI documentation in Spanish](../../README_es.md)
- [Only Film documentary Assessment](../../framework/adoption/examples/only-film-assessment.md)

## 3. Pending public documentation synchronization

**Do not perform these edits until the maintainer approves the target version and release plan.** Once approved, draft a single controlled, reviewable release-preparation change set that:

1. Moves agreed Unreleased work to the **approved version/date** in `CHANGELOG.md`, while retaining a new Unreleased section.
2. Updates **both** README version badges and the published-release sections in English/Spanish without implying that the release is already live before tag publication.
3. Reconciles `ROADMAP.md`, `docs/governance/12_PROJECT_STATUS.md` and related release-status language so “proposed,” “ready,” and “published” are not confused.
4. Reconciles the candidate record and compares the new complete release tree with v0.10.0.
5. Runs full CI and real-library CLI smoke checks on the **exact new candidate SHA**, reviews both JSON reports, and obtains express final approval for the SHA, notes and publication act.

The potential tag `v0.11.0` is **not created** by this document or by approving its draft PR. The existing branch `candidate/option-a-snapshot-20261115` must remain available for candidate review; any change to its head must be separately verified.

## 4. Current decision state

| Question | State |
| --- | --- |
| Option A complete-tree release scope | **Approved** |
| Version `v0.11.0` and title | **Proposed, pending maintainer selection** |
| Final notes and release date | **Draft, not approved** |
| Publication-document changes | **Not yet applied** |
| Final exact release SHA | **Not yet approved** |
| Create tag, GitHub Release or milestone | **Not authorized** |

**Next decision:** approve or change the proposed `v0.11.0` version and scope of the draft notes. That approval would permit publication-document preparation, **not automatic tag creation or release publication**.
