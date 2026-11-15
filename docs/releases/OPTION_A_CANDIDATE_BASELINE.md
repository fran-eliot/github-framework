# Option A — Full-Snapshot Candidate Baseline

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Prepared | 2026-11-15 |
| Maintainer scope decision | **Option A approved** — complete-repository scope and preparation of a candidate; publication not approved |
| Snapshot branch | [`candidate/option-a-snapshot-20261115`](https://github.com/fran-eliot/github-framework/tree/candidate/option-a-snapshot-20261115) |
| **Current candidate commit** | [`3409568ea3735915a2ab88892be66c4a768c1224`](https://github.com/fran-eliot/github-framework/commit/3409568ea3735915a2ab88892be66c4a768c1224) — fast-forwarded after PR #326 |
| Published comparison base | `v0.10.0` — `3c4b21a26e4e85eeef705fefd48323ffd918e681` |
| New release version / date / tag | **Not selected or authorized** |
| Release status | **Candidate baseline updated and verified; publication approval pending** |
| Consumer boundary | Only Film repository unchanged; Application/Integration not authorized |
| UX-02 | `Prepared — Not Executed` |

## 1. Approved scope and candidate handling

The maintainer explicitly approved adopting **Option A** on 2026-11-15 following the consolidated [release-readiness decision brief](../discovery/73_OPTION_A_RELEASE_READINESS_DECISION_BRIEF.md). This approval permits preparing a **complete repository-tree release candidate**, including all post-`v0.10.0` documentation and historical Only Film Assessment material, with their source-qualified limitations.

The dedicated [candidate branch](https://github.com/fran-eliot/github-framework/tree/candidate/option-a-snapshot-20261115) was initially created at `9f317350b25bad39c438fd0e5ac09fe33f5b5ed7`. After PR #323 was merged and exact-main CI passed, it was **fast-forwarded**, with an expected-head safety check, to the current candidate SHA **`56a24418c63e097a01db00472b31f80ed641f789`**. The initial SHA remains historical evidence, **not** the current branch head. After merged PR #326, the candidate branch was fast-forwarded a second time, using the expected previous SHA `56a24418c63e097a01db00472b31f80ed641f789`, to **`3409568ea3735915a2ab88892be66c4a768c1224`**. This is the **current** candidate reference, verified against its own push workflow. Keep this candidate branch until a subsequent explicit decision; every later move requires a newly pinned SHA and refreshed validation. This PR's own documentary edit is **not** part of the frozen candidate until separately incorporated.

**Separate permissions remain distinct:** (1) the maintainer approved Option A scope and candidate preparation; (2) on 2026-11-15 the maintainer **also approved `v0.11.0 — Framework Validator CLI and CI` and the release-note content**; (3) the final SHA/date, tagging and GitHub Release publication still require a separate explicit decision.

## 2. Exact snapshot inventory

The GitHub comparison [`v0.10.0...3409568ea3735915a2ab88892be66c4a768c1224`](https://github.com/fran-eliot/github-framework/compare/v0.10.0...3409568ea3735915a2ab88892be66c4a768c1224) reported **676 repository-wide commits ahead, zero behind, and 91 changed-file paths**. The GitHub recursive tree for this candidate commit returned **286 entries** with `truncated: false`.

| Change area | Paths | What the approved complete-tree scope includes |
| --- | ---: | --- |
| Framework Validator code, tests, and CI | **7** | CLI scoped Component selection/inventory, JSON reporting and cross-platform GitHub Actions |
| Only Film documentary Assessment and supporting evidence | **50** | Full historical evidence trail and formally completed documentary Assessment, not Only Film source code or Application/Integration |
| Discovery records | **21** | Research findings, historical protocols, test/source verification and Option A decision preparation |
| Governance documents | **3** | Project status, backlog and continuity |
| Root public documentation | **5** | English/Spanish README, CHANGELOG, ROADMAP and CONTRIBUTING |
| Other Adoption material | **3** | Adoption Guide and general Assessment/repeatability examples |
| Release-preparation documentation | **2** | Candidate provenance, proposed release notes and remaining authorization boundaries |
| **Total** | **91** | All tracked files at the SHA, not just the changed paths |

This tally describes the difference from the last published tag; a snapshot release would contain the **whole tracked candidate tree**, including unchanged files. The exact compare link is the authoritative per-path manifest. It does not imply 665 Validator code commits.

## 3. Direct evidence on this exact baseline commit

GitHub [Framework Validator push run 43705884458](https://github.com/fran-eliot/github-framework/actions/runs/43705884458) has `head_sha=3409568ea3735915a2ab88892be66c4a768c1224`, `event=push`, and `conclusion=success`. Its jobs ran on GitHub-hosted Ubuntu and Windows with Python 3.11:

| Check | Ubuntu | Windows |
| --- | --- | --- |
| Job / unit tests | **success; 161 tests / OK** | **success; 161 tests / OK** |
| **Real-library CLI smoke test** | **passed; 21 catalog entries and 21 metadata details** | **passed; 21 catalog entries and 21 metadata details** |
| Whole-library Validator | Successful step | Successful step |
| JSON artifact upload | Successful step | Successful step |
| Summary / annotation steps | Successful steps | Successful steps |
| Legacy Node.js runtime deprecation warning in inspected log | **Not observed** | **Not observed** |

**The actual JSON ZIP artifacts of this run were retrieved and parsed**:

| Property | Ubuntu | Windows |
| --- | --- | --- |
| Artifact ID | [14158447004](https://github.com/fran-eliot/github-framework/actions/runs/43705884458/artifacts/14158447004) | [14157814558](https://github.com/fran-eliot/github-framework/actions/runs/43705884458/artifacts/14157814558) |
| Report `status` | `passed` | `passed` |
| `components_discovered` | **21** | **21** |
| `summary.passed_components` | **21** | **21** |
| `summary.failed_components` / `summary.error_count` | **0 / 0** | **0 / 0** |
| `scope.filtered` | `false` | `false` |

The 21 individual Component records all have `passed` status. After excluding platform-dependent absolute `path` values from Component records, the parsed reports are **equal** (including ordered IDs, relative paths, statuses, errors, scope and summaries). These artifacts are subject to finite GitHub retention; their URLs are not permanent audit storage.

This provides **direct evidence of tests, full-library validation and targeted/catalog CLI smoke execution on the updated pinned candidate**. It is not a complete documentary audit or approval to publish.

## 4. Candidate acceptance checklist

| Gate | Evidence / current status | Action before publication |
| --- | --- | --- |
| **A. Full-tree publication scope** | **Approved by maintainer** on 2026-11-15; includes historical Discovery and 50 Only Film documentary files | Preserve this scope and all evidence caveats |
| **B. Immutable source identity** | **Pinned** to `3409568ea3735915a2ab88892be66c4a768c1224` on the dedicated candidate branch; complete **91-path** diff available | Re-pin and revalidate if any candidate content changes |
| **C. Cross-platform unit tests and full Validator JSON** | **Passed / directly verified** on updated pinned SHA: 161 tests per OS; 21/21 Components; 0 errors; normalized Ubuntu/Windows JSON payloads equal | Re-run if candidate SHA changes or CI results become unsuitable |
| **D. Scoped/catalog CLI smoke outputs** | **Passed on this exact candidate SHA** via the new [real-library smoke step](https://github.com/fran-eliot/github-framework/actions/runs/43705884458): 21 catalog entries and 21 loaded metadata records; all three families, selective validation of three representative components, JSON scope, and rejection of invalid argument combination | Preserve these CI logs as candidate evidence; revalidate if the candidate SHA changes |
| **E. Documentary evidence and source limitations** | Internal path checks, canonical Only Film links and high-risk historical/license/security/test caveats reviewed in [#70](../discovery/70_OPTION_A_MARKDOWN_PATH_INTEGRITY.md), [#71](../discovery/71_OPTION_A_ONLY_FILM_CANONICAL_SOURCE_VERIFICATION.md), [#72](../discovery/72_OPTION_A_RISK_BASED_EVIDENCE_ACCEPTANCE.md) | Complete and knowingly accept candidate-specific public claims; do not imply independent first-time UX, consumer operation or third-party rights |
| **F. Version and publication docs** | `v0.11.0 — Framework Validator CLI and CI` and release-note substance **approved 2026-11-15**; CHANGELOG remains `[Unreleased]` and README badges still show **published v0.10.0** | Agree final date/SHA and publication GO before marking the release published |
| **G. Explicit publication approval** | **Not given** | Obtain separate maintainer approval for candidate SHA, version, notes, and actual tag/GitHub Release creation |

A full source audit of third-party ownership/licensing was **not** performed. Whether documentary links/attribution are adequate for publication depends on their content and applicable rights; this baseline does not imply permissions that have not been verified. Do not import or redistribute Only Film consumer source as part of a Framework release.

## 5. Draft release narrative — unversioned, for later review

**Potential headline:** Framework Validator usability, cross-platform checks and structured reporting.

**Substance:** the Framework Validator gains selective Component validation, read-only inventory, machine-readable validation reports and GitHub Actions support on Ubuntu and Windows. The full Framework snapshot also includes Adoption documentation, a completed **documentary** Assessment of Only Film with 28 approved Responsibility classifications and Adoption Decisions, and historical Discovery/governance records. The historical case study does **not** represent completed consumer Application/Integration, clean-clone Compose/Selenium verification, an established Sonar Quality Gate, independent UX testing, legal rights certification, or a security guarantee.

This paragraph is a **summary** of the separately approved `v0.11.0` release-note content. A release date, milestone, Sprint, release tag and publication action have **not** been authorized; `v1.0.0` remains outside this release.

## 6. Candidate disposition

**Option A adopted. Updated candidate baseline fast-forwarded and validated, including the real-library CLI smoke checks. Final release authorization remains open.** The next release-specific step is to verify/re-pin any changes following this approval record and then request **separate final authorization** for the exact SHA, publication date, tag and GitHub Release.

No changes are made to Only Film. UX-02 remains `Prepared — Not Executed`.
