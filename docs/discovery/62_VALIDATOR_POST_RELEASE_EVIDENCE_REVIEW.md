# 62 — Framework Validator Post-Release Evidence Review

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Review date | 2026-11-14 |
| Phase | Discovery — bounded, repository-internal technical verification |
| Baseline | Published tag `v0.10.0` versus current `main`, as inspected on 2026-11-14 |
| Candidate release / Sprint / milestone | **None selected or committed** |
| Independent UX-02 participants | **Unavailable — UX-02 remains `Prepared — Not Executed`** |
| Consumer impact | **None; no consumer mutations or Application/Integration** |

This is a source and existing-CI-evidence review. It is **not** an independent user study, a newly run test suite, release certification, or approval of a new capability.

## 1. Reason for this review

[Discovery #61](61_NEXT_INCREMENT_EVIDENCE_PRIORITIZATION.md) identifies independent first-time UX validation as the first evidence-gathering priority *when participants are available*. Since none are currently available, internal work should not be labeled UX-02 or treated as proof that new developers can follow the Framework.

A separate, immediately inspectable question is whether the **already-integrated, Unreleased Validator changes** have a traceable technical baseline and CI evidence, and which claims would still require further verification before considering a new release.

## 2. Published baseline to current repository delta

The GitHub compare endpoint for `v0.10.0...main` returned **629 commits ahead**, zero behind and **76 changed file entries** when inspected. This is a **repository-wide post-release diff** containing substantial documentation and the completed Only Film Assessment, **not 629 Validator-specific changes** or a statement of release readiness.

The returned file list includes the following Validator-related changes:

| Path | Observed compare additions | Observed compare deletions |
| --- | ---: | ---: |
| [`.github/workflows/framework-validator.yml`](../../.github/workflows/framework-validator.yml) | 56 | 0 |
| [`scripts/framework_validator/__main__.py`](../../scripts/framework_validator/__main__.py) | 265 | 22 |
| [`scripts/framework_validator/ci_summary.py`](../../scripts/framework_validator/ci_summary.py) | 142 | 0 |
| [`scripts/framework_validator/discovery.py`](../../scripts/framework_validator/discovery.py) | 6 | 3 |
| [`tests/framework_validator/test_ci_summary.py`](../../tests/framework_validator/test_ci_summary.py) | 372 | 0 |
| [`tests/framework_validator/test_cli.py`](../../tests/framework_validator/test_cli.py) | 917 | 2 |

These are **Git compare change statistics**, not manually measured functional contribution counts or exhaustive attribution to individual PRs. The diff is large enough that a future release scope should not be inferred from the aggregate `v0.10.0...main` commit count alone.

## 3. Current Validator contract: static inspection

The checked [CLI entry point](../../scripts/framework_validator/__main__.py), [test suite](../../tests/framework_validator/test_cli.py), [CI summary module](../../scripts/framework_validator/ci_summary.py) and [workflow](../../.github/workflows/framework-validator.yml) support these bounded observations:

- The default CLI root targets **GitHub Framework's own `framework/components` library**. An explicit `--components-root` points to a compatible Component-library directory; it is **not** a semantic Assessment of an arbitrary consumer repository.
- The normal Validator path discovers Components and checks metadata, identity, uniqueness, maturity, dependencies and supported Workflow-specific rules. It can emit reports in JSON.
- `--family` and `--component` enable **filtered scopes**. Passing a partial scope does not establish that all library Components are valid; the public README states this explicitly.
- `--list-components --format json --details` yields a **catalog with metadata loading status** (including `missing` or `invalid`). It is **not semantic validation**, and the [public README](../../README.md) already makes this distinction. A catalog entry or successful listing alone is therefore not evidence of validation success.
- The CI workflow triggers on **pull requests** and pushes to `main`, runs on **Ubuntu and Windows with Python 3.11**, executes Python unittest discovery and runs Validator checks; it uploads JSON reports and emits summaries/annotations.

These observations are grounded in source, tests and workflow definitions. They do **not** demonstrate usability for an unfamiliar developer, automatic template materialization, new semantic Adoption decisions or correctness for every possible input.

## 4. Existing cross-platform CI evidence

For the already merged [PR #307](https://github.com/fran-eliot/github-framework/pull/307), the GitHub workflow-run lookup of its **PR head SHA** returned **Framework Validator run [43646424380](https://github.com/fran-eliot/github-framework/actions/runs/43646424380)** with completed `success` conclusion.

The same run's reported jobs were:

| Job | Recorded conclusion | Selected successful steps |
| --- | --- | --- |
| `Component validation (windows-latest, Python 3.11)` | `success` | Install dependency, Run Validator test suite, Validate Framework Components, Upload report, Summarize results, Annotate errors |
| `Component validation (ubuntu-latest, Python 3.11)` | `success` | Install dependency, Run Validator test suite, Validate Framework Components, Upload report, Summarize results, Annotate errors |

This is **existing CI evidence associated with that PR head**, not a test run initiated by this review or proof that an arbitrary future release commit has passed its release checks. The actual report contents, detailed logs, code coverage, all edge cases, artifact retention after seven days and deployment/release procedures were **not independently rechecked** in this review. A successful workflow is not evidence that the Framework is independently usable by newcomers.

## 5. Findings and evidence gaps

| Finding | Evidence | Limitation |
| --- | --- | --- |
| **VAL-01** — There is an actual post-`v0.10.0` Validator code/workflow/test diff. | Compare `v0.10.0...main` and the six paths above. | Total delta mixes unrelated documentation and consumer Assessment work; a release scope has not been selected. |
| **VAL-02** — The CLI's catalog-versus-validation boundary is already described in user-facing docs and covered by source/tests. | `__main__.py`, `test_cli.py`, `README.md`. | Static contract review and existing tests, not independent comprehension evidence. |
| **VAL-03** — The PR #307 Validator workflow has successful Windows and Ubuntu jobs. | GitHub workflow run 43646424380 and its reported job steps. | Specific PR head only; not a fresh release-tag verification or exhaustive test suite. |
| **VAL-04** — The current CI workflow includes JSON artifact reporting and bounded annotations. | Workflow YAML and `ci_summary.py`. | Artifact contents and downstream consumer value not audited here. |
| **VAL-05** — No new Validator feature is justified by this review alone. | VAL-01 through VAL-04 plus Discovery #58/#61. | Additional user need or a concrete reproducible defect would change the prioritization. |

## 6. Disposition and next evidence gate

**Result: bounded technical evidence consolidated; no new functionality selected.** The existing Validator behavior and documentation already address the basic catalog-versus-validation distinction. Do **not** invent a feature gap or claim UX-02 occurred.

Possible next **internal** verification, subject to a separate, limited decision, is a **release-scope inventory** that identifies the precise post-tag Validator changes and checks current `main` (or a later pinned candidate commit) against the documented test and report contracts. This may support a future release discussion but **does not itself approve a release**.

If independent participants become available later, follow [UX-02 protocol #54](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md) as a **separate actual study**. Until then the status stays `Prepared — Not Executed`.

No consumer changes, branch, Application, Integration, new Component, semantic automation, Solution Shaping, Delivery Scope, Sprint, milestone, target version or release are authorized by this Discovery review.
