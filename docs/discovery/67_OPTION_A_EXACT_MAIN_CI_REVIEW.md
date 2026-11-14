# 67 — Option A Exact-Main CI Evidence and Release Gates

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Review date | 2026-11-14 |
| Phase | Discovery — exact-commit CI inspection for Option A |
| Published baseline | `v0.10.0` at `3c4b21a26e4e85eeef705fefd48323ffd918e681` |
| Inspected `main` commit | [`2a9e12d1bf84fc8c0245e43f324ba14ae2c0ca91`](https://github.com/fran-eliot/github-framework/commit/2a9e12d1bf84fc8c0245e43f324ba14ae2c0ca91) (post-PR #312 merge) |
| Workflow | [Framework Validator run 43648960987](https://github.com/fran-eliot/github-framework/actions/runs/43648960987) — **push to `main`, completed / success** |
| Release candidate designation | **None** — this is a fixed inspection reference |
| UX-02 | `Prepared — Not Executed`; no independent participants |
| Consumer changes | **None** |

> This record improves on earlier PR-head CI evidence by checking a workflow whose `head_sha` is exactly the merged `main` commit above. It does **not** certify a future release candidate, verify every JSON field, test unrelated consumer code, or approve any release.

## 1. Current snapshot and inclusion boundary

The GitHub comparison `v0.10.0...2a9e12d1bf84fc8c0245e43f324ba14ae2c0ca91` returned **640 commits ahead, zero behind and 81 changed-file entries**. This includes the merged [Option A file inventory #65](65_OPTION_A_FULL_SNAPSHOT_REVIEW.md), [content review #66](66_OPTION_A_SNAPSHOT_CONTENT_REVIEW.md) and the bounded Only Film consolidated matrix wording reconciliation. The comparison is **repository-wide**, and these statistics must not be described as Validator-specific commit counts.

A Git tag on this commit would include the complete tracked tree, including current documentation and consumer Assessment evidence. The complete snapshot has **not** been approved for publication; the inspected SHA is a fixed research reference, **not** an accepted release candidate.

## 2. Same-SHA CI evidence (inspected through GitHub Actions)

The repository's workflow-run collection reported:

| Attribute | Observed |
| --- | --- |
| Workflow name | Framework Validator |
| Run ID | [43648960987](https://github.com/fran-eliot/github-framework/actions/runs/43648960987) |
| Trigger | `push` on `main` |
| Head SHA | `2a9e12d1bf84fc8c0245e43f324ba14ae2c0ca91` |
| Run state and conclusion | `completed` / `success` |
| Operating systems | `ubuntu-latest`, `windows-latest`; both with Python 3.11 |

The job listing and downloaded job-log **text** directly confirmed:

| Job | GitHub conclusion | Test log | Report and summary steps |
| --- | --- | --- | --- |
| Windows, Python 3.11 | `success` | `Ran 161 tests in 2.435s`; `OK` | Validate Framework Components, Upload Validator report, Summarize Validator results, Annotate Validator errors: **successful steps** |
| Ubuntu, Python 3.11 | `success` | `Ran 161 tests in 1.304s`; `OK` | Validate Framework Components, Upload Validator report, Summarize Validator results, Annotate Validator errors: **successful steps** |

The source workflow includes a **full-library** Validator invocation with JSON file output. Successful steps support that this invocation finished successfully at the inspected SHA. **Separate targeted/filtered CLI invocations were not observed in this particular workflow.** Nor was code coverage measured or a complete user-experience study performed.

## 3. Uploaded report artifacts

The same workflow's artifact list exposed these two uploads:

| Platform | Artifact | Artifact ID | Reported archive size | Reported expiry |
| --- | --- | --- | ---: | --- |
| Ubuntu | `framework-validator-report-ubuntu-latest` | `14135940085` | 944 bytes | 2026-11-21 22:36 UTC |
| Windows | `framework-validator-report-windows-latest` | `14135132223` | 954 bytes | 2026-11-21 22:36 UTC |

The artifacts were listed as **not expired at inspection**. The logs record successful upload/finalization. The report archive bytes were **not decoded or semantically inspected** in this review; therefore it does **not** independently assert the JSON's exact `summary`, `components`, `scope` or `error_count` values, nor does it compare report payloads across operating systems. The published report links and expiry represent **transient evidence**, so future release verification should preserve or regenerate them on an approved candidate.

## 4. CI deprecation warnings observed on both operating systems

Both job logs contained a warning:

> Node.js 20 is deprecated. The following actions target Node.js 20 but are being forced to run on Node.js 24: actions/checkout@v4, actions/setup-python@v5, actions/upload-artifact@v4.

The [workflow source](../../.github/workflows/framework-validator.yml) uses those three major-version actions. The warning is **nonblocking in this observed run**, not a failed check. However, relying on forced runtime migration creates a reasonable **future compatibility-maintenance question**. Before a release decision, review supported newer action versions and their behavior on both platforms; if an upgrade is justified, treat it as a **separately reviewed code/CI change**, not an automatic correction made by this research.

This review does not claim the newer versions are compatible without testing or select any update.

## 5. What improved and what remains unverified

| Option A gate | New verified evidence | Remaining limitation |
| --- | --- | --- |
| Exact source identity | GitHub `push` workflow `head_sha` matches pinned merged `main` commit. | Not explicitly selected or approved as a **release candidate**; new merges would require a fresh SHA. |
| Cross-platform tests | **161 tests / `OK`** in both job logs on that SHA. | No code/branch coverage measurement, dependency audit or later candidate replay. |
| Full-library Validator | Both jobs marked `Validate Framework Components` successful. | JSON report **contents not independently examined**; partial-selection examples not exercised in this workflow. |
| Reporting and diagnostic chain | JSON artifacts uploaded and job summary/annotation steps completed successfully. | No decoded report review; no negative-case CI demonstration or retention beyond listed expiry. |
| CI runtime compatibility | Both jobs successful despite Node.js deprecation warning. | Workflow actions compatibility warning still merits review; no changes authorized here. |
| Full snapshot documentary acceptance | [#65](65_OPTION_A_FULL_SNAPSHOT_REVIEW.md) and [#66](66_OPTION_A_SNAPSHOT_CONTENT_REVIEW.md) provide file inventory and bounded content review. | All 81 changed paths and included documentary claims have **not** been exhaustively approved as a release payload. |
| Public release decision | `v0.10.0` remains the published version. | Version, release scope, tag, milestone, release notes and publication approval are **not given**. |

## 6. Recommended decision boundary

**Outcome: exact-`main` cross-platform CI gate has encouraging, specifically attributable evidence; Option A remains under review.** This result should not be reported as a `GO` decision for publication.

The next bounded technical checks, if separately authorized, are to inspect the actual uploaded JSON report payloads, exercise representative filtered CLI and catalog scenarios on a pinned candidate, and evaluate the GitHub Actions Node.js compatibility warning. The documentary check still requires acceptance of the **entire** included Framework snapshot, not merely the Validator features.

No new version, Issue, Sprint, milestone, branch designated as a release candidate, tag, GitHub Release, consumer mutation, Only Film Application/Integration or UX-02 study is initiated or authorized by this evidence record.
