# Option A — Full-Snapshot Candidate Baseline

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Prepared | 2026-11-15 |
| Maintainer scope decision | **Option A approved** — complete-repository scope and preparation of a candidate; publication not approved |
| Snapshot branch | [`candidate/option-a-snapshot-20261115`](https://github.com/fran-eliot/github-framework/tree/candidate/option-a-snapshot-20261115) |
| **Immutable candidate baseline commit** | [`9f317350b25bad39c438fd0e5ac09fe33f5b5ed7`](https://github.com/fran-eliot/github-framework/commit/9f317350b25bad39c438fd0e5ac09fe33f5b5ed7) |
| Published comparison base | `v0.10.0` — `3c4b21a26e4e85eeef705fefd48323ffd918e681` |
| New release version / date / tag | **Not selected or authorized** |
| Release status | **Candidate baseline created; not ready to tag or publish** |
| Consumer boundary | Only Film repository unchanged; Application/Integration not authorized |
| UX-02 | `Prepared — Not Executed` |

## 1. Approved scope and candidate handling

The maintainer explicitly approved adopting **Option A** on 2026-11-15 following the consolidated [release-readiness decision brief](../discovery/73_OPTION_A_RELEASE_READINESS_DECISION_BRIEF.md). This approval permits preparing a **complete repository-tree release candidate**, including all post-`v0.10.0` documentation and historical Only Film Assessment material, with their source-qualified limitations.

The dedicated [candidate branch](https://github.com/fran-eliot/github-framework/tree/candidate/option-a-snapshot-20261115) was created directly from `9f317350b25bad39c438fd0e5ac09fe33f5b5ed7` and contains **no code or documentation modifications beyond that baseline commit**. Its purpose is to preserve the review reference while release-specific documentation and acceptance are prepared elsewhere. **Do not delete or advance it casually**; if an approved correction must enter the release candidate, establish a **new exact candidate SHA** and repeat the comparison and applicable checks. The planning/documentation PR that adds this record is **not part of the pinned candidate** unless explicitly carried into a later candidate revision.

**Two separate permissions remain distinct:** (1) the maintainer has now accepted the full-tree **scope and candidate preparation**; (2) the maintainer has **not** selected a release version, approved final release notes, authorized tagging, or authorized GitHub Release publication.

## 2. Exact snapshot inventory

The GitHub comparison [`v0.10.0...9f317350b25bad39c438fd0e5ac09fe33f5b5ed7`](https://github.com/fran-eliot/github-framework/compare/v0.10.0...9f317350b25bad39c438fd0e5ac09fe33f5b5ed7) reported **660 repository-wide commits ahead, zero behind, and 88 changed-file paths**. The GitHub recursive tree for the candidate commit returned **282 entries** with `truncated: false`.

| Change area | Paths | What the approved complete-tree scope includes |
| --- | ---: | --- |
| Framework Validator code, tests, and CI | **6** | CLI scoped Component selection/inventory, JSON reporting and cross-platform GitHub Actions |
| Only Film documentary Assessment and supporting evidence | **50** | Full historical evidence trail and formally completed documentary Assessment, not Only Film source code or Application/Integration |
| Discovery records | **21** | Research findings, historical protocols, test/source verification and Option A decision preparation |
| Governance documents | **3** | Project status, backlog and continuity |
| Root public documentation | **5** | English/Spanish README, CHANGELOG, ROADMAP and CONTRIBUTING |
| Other Adoption material | **3** | Adoption Guide and general Assessment/repeatability examples |
| **Total** | **88** | All tracked files at the SHA, not just the changed paths |

This tally describes the difference from the last published tag; a snapshot release would contain the **whole tracked candidate tree**, including unchanged files. The exact compare link is the authoritative per-path manifest. It does not imply 660 Validator code commits.

## 3. Direct evidence on this exact baseline commit

GitHub [Framework Validator push run 43701840091](https://github.com/fran-eliot/github-framework/actions/runs/43701840091) has `head_sha=9f317350b25bad39c438fd0e5ac09fe33f5b5ed7`, `event=push`, and `conclusion=success`. Its jobs ran on GitHub-hosted Ubuntu and Windows with Python 3.11:

| Check | Ubuntu | Windows |
| --- | --- | --- |
| Job / unit tests | **success; 161 tests / OK** | **success; 161 tests / OK** |
| Whole-library Validator | Successful step | Successful step |
| JSON artifact upload | Successful step | Successful step |
| Summary / annotation steps | Successful steps | Successful steps |
| Legacy Node.js runtime deprecation warning in inspected log | **Not observed** | **Not observed** |

**The actual JSON ZIP artifacts of this run were retrieved and parsed**:

| Property | Ubuntu | Windows |
| --- | --- | --- |
| Artifact ID | [14157076410](https://github.com/fran-eliot/github-framework/actions/runs/43701840091/artifacts/14157076410) | [14157385195](https://github.com/fran-eliot/github-framework/actions/runs/43701840091/artifacts/14157385195) |
| Report `status` | `passed` | `passed` |
| `components_discovered` | **21** | **21** |
| `summary.passed_components` | **21** | **21** |
| `summary.failed_components` / `summary.error_count` | **0 / 0** | **0 / 0** |
| `scope.filtered` | `false` | `false` |

The 21 individual Component records all have `passed` status. After excluding platform-dependent absolute `path` values from Component records, the parsed reports are **equal** (including ordered IDs, relative paths, statuses, errors, scope and summaries). These artifacts are subject to finite GitHub retention; their URLs are not permanent audit storage.

This is **strong evidence of the Validator tests and unfiltered Component validation on the pinned baseline**, not a substitute for targeted CLI smoke verification, a full documentation audit or approval to publish.

## 4. Candidate acceptance checklist

| Gate | Evidence / current status | Action before publication |
| --- | --- | --- |
| **A. Full-tree publication scope** | **Approved by maintainer** on 2026-11-15; includes historical Discovery and 50 Only Film documentary files | Preserve this scope and all evidence caveats |
| **B. Immutable source identity** | **Pinned** to `9f317350b25bad39c438fd0e5ac09fe33f5b5ed7` on dedicated candidate branch; complete 88-path diff available | Re-pin and revalidate if any candidate content changes |
| **C. Cross-platform unit tests and full Validator JSON** | **Passed / directly verified** on pinned SHA: 161/161 tests and 21/21 Components on Ubuntu/Windows | Re-run only if candidate SHA changes or CI results become unsuitable |
| **D. Scoped/catalog CLI smoke outputs** | Existing CI suite covers CLI behavior; **standalone commands on this candidate not independently recorded** | Capture representative `--component`, `--list-components`, `--details` command results and exit codes, or explicitly accept test-suite coverage at the final gate |
| **E. Documentary evidence and source limitations** | Internal path checks, canonical Only Film links and high-risk historical/license/security/test caveats reviewed in [#70](../discovery/70_OPTION_A_MARKDOWN_PATH_INTEGRITY.md), [#71](../discovery/71_OPTION_A_ONLY_FILM_CANONICAL_SOURCE_VERIFICATION.md), [#72](../discovery/72_OPTION_A_RISK_BASED_EVIDENCE_ACCEPTANCE.md) | Complete and knowingly accept candidate-specific public claims; do not imply independent first-time UX, consumer operation or third-party rights |
| **F. Version and publication docs** | `CHANGELOG.md` remains `[Unreleased]`; both README versions still reflect **published v0.10.0** | Select a release version and date; prepare notes and update documentation on a **revised exact candidate** before any tag |
| **G. Explicit publication approval** | **Not given** | Obtain separate maintainer approval for candidate SHA, version, notes, and actual tag/GitHub Release creation |

A full source audit of third-party ownership/licensing was **not** performed. Whether documentary links/attribution are adequate for publication depends on their content and applicable rights; this baseline does not imply permissions that have not been verified. Do not import or redistribute Only Film consumer source as part of a Framework release.

## 5. Draft release narrative — unversioned, for later review

**Potential headline:** Framework Validator usability, cross-platform checks and structured reporting.

**Substance:** the Framework Validator gains selective Component validation, read-only inventory, machine-readable validation reports and GitHub Actions support on Ubuntu and Windows. The full Framework snapshot also includes Adoption documentation, a completed **documentary** Assessment of Only Film with 28 approved Responsibility classifications and Adoption Decisions, and historical Discovery/governance records. The historical case study does **not** represent completed consumer Application/Integration, clean-clone Compose/Selenium verification, an established Sonar Quality Gate, independent UX testing, legal rights certification, or a security guarantee.

This paragraph is **draft narrative**, not approved release notes. No target version (including `v1.0.0`), milestone, Sprint, release tag or date has been selected.

## 6. Candidate disposition

**Option A adopted. Baseline candidate preserved and technically verified for its existing CI workflow. Final release authorization remains open.** The next release-specific step is to complete the scoped CLI and publication-document checks, choose a suitable version **with the maintainer**, produce the updated candidate SHA, and request a separate final approval before tagging or publishing.

No changes are made to Only Film. UX-02 remains `Prepared — Not Executed`.
