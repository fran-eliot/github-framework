# 73 — Option A: Consolidated Release-Readiness Decision Brief

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Decision date | 2026-11-15 |
| Status | **Recommendation prepared — maintainer decision outstanding** |
| Option under review | **A — publish a complete, reviewed Framework repository snapshot** |
| Baseline | `v0.10.0` — `3c4b21a26e4e85eeef705fefd48323ffd918e681` |
| Inspected `main` reference | [`665ef635f20d5fb3b3efc3d6433279c4765f672d`](https://github.com/fran-eliot/github-framework/commit/665ef635f20d5fb3b3efc3d6433279c4765f672d) |
| Current published version | **`v0.10.0`** |
| Candidate commit / target version / release date | **None authorized or selected** |
| Consumer boundary | Only Film remains unmodified; Application/Integration not authorized |
| UX-02 | `Prepared — Not Executed` (no independent participants) |

## 1. Decision requested

**Proposed direction: proceed with Option A to a separately authorized, bounded release-candidate preparation stage. Do not publish yet.** This would accept that the snapshot includes **the complete Git tree**, not only Validator enhancements.

The maintainer has authorized **studying** Option A, not explicitly accepted its full publication scope, approved a candidate commit, selected a version, or authorized any release. Merging this brief merely records the recommendation and factual readiness: it **must not be construed as approval to tag or publish**.

**Material question for the maintainer:** Is a future GitHub Framework release permitted to include the entire post-`v0.10.0` repository tree, **including historical Discovery/governance records and the 50 Only Film documentary Assessment files**, with bounded evidence claims rather than technical/rights certification? An explicit affirmative answer is required before release-candidate preparation is committed to.

## 2. Snapshot reviewed — all areas included

The fixed GitHub comparison [`v0.10.0...665ef635f20d`](https://github.com/fran-eliot/github-framework/compare/v0.10.0...665ef635f20d5fb3b3efc3d6433279c4765f672d) returned **658 commits ahead, zero behind and 87 changed file entries**. These are whole-repository numbers, not Validator-only changes.

| Area | Changed files | Scope consequence |
| --- | ---: | --- |
| Validator implementation, tests, CI | **6** | Selective CLI and inventory capabilities, structured JSON diagnostics, cross-platform verification and Node.js 24-compatible workflow |
| Only Film documentary Assessment/evidence | **50** | Source-bound historical case study, **not** consumer code or a claim that Application/Integration occurred |
| Discovery | **20** | Research, usability protocol and evidence/release-scope reviews, **not** committed production features |
| Governance | **3** | Current and historical status, backlog and continuity |
| Root public documents | **5** | README EN/ES, CHANGELOG, ROADMAP, CONTRIBUTING; some require version-specific synchronization if approved |
| Other Adoption documents | **3** | Guide and general example/repeatability materials |
| **Total** | **87** | A tag would include **all tracked files at the selected SHA**, including unchanged files |

The original [79-path inspection](65_OPTION_A_FULL_SNAPSHOT_REVIEW.md) is historical and was incrementally superseded by subsequent merged research. **87 is the snapshot count at this brief's inspected commit, not a permanent release manifest**; a candidate prepared after this PR must be re-pinned and re-compared.

## 3. Consolidated evidence, not repeated Discovery

| Verification area | Present evidence | What it actually establishes | Remaining condition |
| --- | --- | --- | --- |
| Validator tests, Ubuntu/Windows | [Exact-`main` verification](67_OPTION_A_EXACT_MAIN_CI_REVIEW.md), [Node 24 compatibility](69_VALIDATOR_ACTIONS_NODE24_VERIFICATION.md), and latest [run 43701153414](https://github.com/fran-eliot/github-framework/actions/runs/43701153414) at inspected `665ef635f20d5fb3b3efc3d6433279c4765f672d` | Latest push run **success** on both OS; **161 tests / OK** in both job logs; JSON report upload jobs succeeded; no `##[warning]` in either inspected log | Verify the **actual candidate SHA**, not a previous `main` state |
| Validator JSON results | [Real reports #68](68_OPTION_A_VALIDATOR_REPORT_CLI_EVIDENCE.md), [post-upgrade reports #69](69_VALIDATOR_ACTIONS_NODE24_VERIFICATION.md) | At previously pinned SHAs, downloaded Ubuntu/Windows reports each had **21/21 passed**, zero validation errors, and matching normalized records | Candidate reports must be retained/inspected if the candidate SHA changes |
| Filtered CLI and component catalog | [Existing passing tests and API distinctions #68](68_OPTION_A_VALIDATOR_REPORT_CLI_EVIDENCE.md) | Test suite covers selective `--component`, `--list-components`, `--details`, JSON and invalid-input scenarios | Capture candidate-specific filtered/catalog smoke output and exit codes for additional release confidence |
| Internal Markdown paths | [Read-only inspection #70](70_OPTION_A_MARKDOWN_PATH_INTEGRITY.md) | **78 changed Markdown files**, **833 conventional relative links** checked against a then-pinned full Git tree, **zero missing paths** | Repeat/spot-check for candidate drift; anchors, reference-style links and external URL liveness were not established |
| Only Film canonical source pointers | [Exact-SHA lookup #71](71_OPTION_A_ONLY_FILM_CANONICAL_SOURCE_VERIFICATION.md) | **21/21** canonical pinned source paths exist at consumer SHA `28d75a50...`; cited consumer CI run matches that SHA | Not a full semantic/third-party audit of 50 evidence documents |
| High-impact release claims | [Risk review #72](72_OPTION_A_RISK_BASED_EVIDENCE_ACCEPTANCE.md) and [content review #66](66_OPTION_A_SNAPSHOT_CONTENT_REVIEW.md) | Licensing/attribution, historical security, H2/Compose/Selenium, and Sonar analysis-versus-Quality-Gate boundaries explicitly documented; matrix chronology reconciled | Maintainer accepts publication of a documentation case study with stated caveats; no assertion of unverified rights |
| Independent first-time UX | [UX-02 validation protocol](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md) | Protocol exists; **no independent participants** and no study completed | **Not a prerequisite for a bounded Validator maintenance release unless that release claims independent usability**; do not claim UX results |

**What changed since the original options review:** the formerly open CI deprecation concern was **addressed in code** in merged PR #315 and verified after merge. The JSON reports were genuinely downloaded/inspected in #68 and #69. The latest exact-`main` run adds fresh CI support, but it is **not** a formally selected release candidate.

## 4. Requirements classified by impact

### Blocking **before candidate preparation**

1. **Explicit Option A scope acceptance:** the maintainer must accept the **complete-tree snapshot approach**, including all fifty Only Film evidence records and Discovery/governance history. The assistant may not infer this from approval to study Option A.
2. **Boundary on claims and rights:** agree that the case study is a **linked, documentary Assessment**, not proof of consumer licensing or a right to relicense/reuse third-party code. If permissions for publishing **the Framework's own documentary text** are uncertain, resolve that independently before release publication.

### Required **on the candidate before tag or publication**

1. **Freeze identity:** choose a candidate Git SHA and compare it with `v0.10.0`; refresh the complete changed-file manifest and review any changes after this inspected snapshot.
2. **Candidate-specific CI:** Ubuntu and Windows Python 3.11 tests, full-library validation, inspect JSON summaries and artifact status. Capture representative targeted and catalog CLI smoke outputs and exit codes.
3. **Content and contract acceptance:** verify README EN/ES and CLI options, failure semantics, JSON result distinctions, relative paths, workflow permissions/action versions and known evidence limitations. Do a focused link/claim review of any documents added/modified after the inspected reference.
4. **Release documentation:** draft notes that fairly describe **Validator improvements plus the broad documentation payload**; synchronize CHANGELOG, badges and root documentation only when an explicit version/date is authorized. Do not silently claim `v1.0.0` or new product maturity.
5. **Maintainer release GO:** obtain distinct affirmative approval for the **candidate SHA, version, release notes and act of publication**; only then create any tag or GitHub Release.

### Not automatically blocking a **bounded maintenance release**

- Independent UX-02 sessions that have **not** been run — **provided** the release does not claim validated first-time usability or a mature `v1.0.0` experience.
- Full clean-clone Only Film Compose/Selenium execution, penetration tests, historical Sonar Quality Gate or legally certified third-party ownership — **provided** the release makes **none** of those claims, contains no unauthorized transfer of consumer source, and acknowledges evidence limits.
- Exhaustive external-link uptime checks for every historical supporting page — **provided** the high-value source references and scope descriptions are reviewed, known defects are addressed, and the maintainer knowingly accepts remaining documentary risk.

These are **risk-based recommendations** for release-scoping, **not waivers** of applicable legal obligations, security controls or a maintainer's higher standards.

## 5. Release message boundaries

**Safe, subject to final review:** “The Framework Validator gains cross-platform automated checks, machine-readable reports and focused Component inventory and validation. The Framework also includes a formally completed, source-qualified **documentary** Only Film Assessment with 28 approved Responsibility classifications and 28 approved Adoption Decisions.”

**Do not claim:** “Only Film is integrated/migrated”, “Docker Compose or Selenium was verified at the pinned SHA”, “Sonar Quality Gate passed”, “the original academic collaborators granted redistribution licenses”, “independent first-time usability was validated”, or “the Framework is production-certified/stable v1.0.0”. These claims are **not supported** by the reviewed sources.

No release notes are published by this brief.

## 6. Recommendation and explicit decision state

| Question | Position |
| --- | --- |
| Is Option A technically worth pursuing? | **Yes — recommend bounded candidate preparation**, based on passing exact-`main` Validator CI and narrowly defined evidence limits |
| Is the full repository documentation payload accepted for a release? | **Not yet explicitly accepted** |
| Is a release candidate selected/frozen? | **No** |
| Is a target version/milestone/Sprint authorized? | **No** |
| Can a tag or GitHub Release be published now? | **No** |
| What decision would unlock candidate preparation? | **Maintainer explicitly accepts Option A's complete-tree scope and authorizes preparing a candidate for subsequent review, without publication** |

**Disposition: READY FOR A SCOPE DECISION — NOT READY TO PUBLISH.** The next action is the maintainer's explicit scope decision, followed, only if accepted, by a bounded candidate-preparation change. Continue to treat `v0.10.0` as the last published release and UX-02 as `Prepared — Not Executed`. No Only Film mutation, Application/Integration, new version, release candidate, milestone, Sprint, tag or publication is authorized by merging this document.
