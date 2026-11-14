# 69 — Framework Validator GitHub Actions Node.js 24 Verification

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Review date | 2026-11-14 |
| Phase | Discovery — bounded verification of integrated CI maintenance |
| Change | [PR #315](https://github.com/fran-eliot/github-framework/pull/315) — merged |
| Inspected `main` SHA | [`51b98aaf7f59a68fbdeee52176cf1375272ea440`](https://github.com/fran-eliot/github-framework/commit/51b98aaf7f59a68fbdeee52176cf1375272ea440) |
| Published version | `v0.10.0`; CI changes remain **Unreleased** |
| Consumer changes | None |
| Release approval | Not given |

## 1. Change included in `main`

The [Framework Validator workflow](../../.github/workflows/framework-validator.yml) now uses:

| Action | Previous | Integrated |
| --- | --- | --- |
| Checkout | `actions/checkout@v4` | `actions/checkout@v5` |
| Python setup | `actions/setup-python@v5` | `actions/setup-python@v6` |
| Artifact upload | `actions/upload-artifact@v4` | `actions/upload-artifact@v6` |

The workflow continues to use GitHub-hosted `ubuntu-latest` and `windows-latest` with Python 3.11, pinned `PyYAML==6.0.2`, read-only contents permissions, test discovery, full-library Validator execution, JSON report uploads, job summaries and annotations.

## 2. PR checks and exact-merge verification

Two independent workflow runs were inspected:

| Evidence | Run | Reference | Windows | Ubuntu |
| --- | --- | --- | --- | --- |
| PR check | [43650256475](https://github.com/fran-eliot/github-framework/actions/runs/43650256475) | PR #315 head `67af29b09ac377004a7f2ca8c378379da642f98d` | `success` — 161 tests / OK | `success` — 161 tests / OK |
| Post-merge `main` push | [43650381451](https://github.com/fran-eliot/github-framework/actions/runs/43650381451) | Merge commit `51b98aaf7f59a68fbdeee52176cf1375272ea440` | `success` — 161 tests / OK | `success` — 161 tests / OK |

The GitHub job listings also show that checkout, Python setup, full-library validation, report upload, summary and annotation steps succeeded in both jobs. Both post-merge runners reported version **2.338.2** in their logs.

The previous warning about the deprecated Node.js 20 action runtime and forced use of Node.js 24 was **not present** in the inspected PR or post-merge Windows/Ubuntu job logs. This is an observation for those particular runs, not a permanent compatibility guarantee for future runner or action versions.

## 3. Actual post-merge JSON reports

The two uploaded ZIP archives from **run 43650381451** were downloaded, opened, and their `validator-report.json` payloads parsed:

| Field | Windows | Ubuntu |
| --- | --- | --- |
| Artifact ID | [14135788566](https://github.com/fran-eliot/github-framework/actions/runs/43650381451/artifacts/14135788566) | [14135199689](https://github.com/fran-eliot/github-framework/actions/runs/43650381451/artifacts/14135199689) |
| `status` | `passed` | `passed` |
| `components_discovered` | 21 | 21 |
| `summary.passed_components` | 21 | 21 |
| `summary.failed_components` | 0 | 0 |
| `summary.error_count` | 0 | 0 |
| `scope.filtered` | `false` | `false` |

All 21 Component records had `status: passed` and empty `errors` arrays. The complete parsed reports matched across platforms after excluding **only** the platform-specific absolute `path` field in Component records. Component IDs, relative paths, statuses, errors, scope and summary values were equal.

Artifact retention remains seven days; the GitHub artifact listings recorded expiry on **2026-11-21 UTC**. Future reviewers must not assume these archives will remain downloadable indefinitely.

## 4. Limits and next decision

**Observed result:** the three-action compatibility update is integrated, and the reviewed PR and post-merge runs passed. The previously observed Node.js runtime warning did not recur in those logs. This substantiates the CI maintenance item in the [Unreleased Changelog](../../CHANGELOG.md).

This record **does not** establish complete coverage, certify external consumers, run independent first-time usability sessions, or approve the Option A full-repository release. Before any release, a new candidate SHA and the complete included documentary scope still require explicit review, together with the applicable verification and release-documentation gates.

UX-02 remains `Prepared — Not Executed` without independent participants. No new release version, Sprint, milestone, tag, GitHub Release, Only Film Application or Integration is authorized or created by this review.
