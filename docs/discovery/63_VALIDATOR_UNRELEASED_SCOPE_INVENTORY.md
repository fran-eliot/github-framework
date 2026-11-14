# 63 — Framework Validator Unreleased Scope Inventory

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Date | 2026-11-14 |
| Phase | Discovery — source-backed Unreleased scope inventory |
| Published baseline | Git tag `v0.10.0` (base SHA `3c4b21a26e4e85eeef705fefd48323ffd918e681`) |
| Comparison target | `main` inspected on 2026-11-14 |
| Release planning | **Not authorized; no target version, Sprint or milestone** |
| Independent UX-02 participants | **None available; `Prepared — Not Executed`** |
| Consumer changes | **None** |

This inventory identifies implementation already merged after `v0.10.0`, corresponding closed Issues, and candidate verification gates. It does **not** designate a release candidate or authorize publishing a new version. Compare results cover the inspected references, not future `main` changes.

## 1. Source of truth and history

The [Product Backlog](../governance/14_BACKLOG.md), [Roadmap](../../ROADMAP.md) and [Unreleased Changelog](../../CHANGELOG.md) classify the current Framework Validator enhancements as **integrated into `main` after `v0.10.0`, not released**. The [prior technical review](62_VALIDATOR_POST_RELEASE_EVIDENCE_REVIEW.md) records bounded code and CI observations.

The GitHub comparison `v0.10.0...main` at this review returned **631 commits ahead**, zero behind and a listed set of **76 changed files**. These represent the **whole repository**, including research, assessment and governance records. They must **not** be relabeled as 631 Validator commits or a ready-to-publish release payload. The compare base SHA is `3c4b21a26e4e85eeef705fefd48323ffd918e681`. No candidate head SHA is fixed by this research and no release diff is approved.

## 2. Cohesive implemented capability groups

### A. CI execution, reporting and diagnosis — seven closed Issues

| Issue | Implemented feature / supported repository evidence |
| --- | --- |
| [#135](https://github.com/fran-eliot/github-framework/issues/135) | Run Validator tests and self-validation in GitHub Actions |
| [#137](https://github.com/fran-eliot/github-framework/issues/137) | Upload JSON reports as workflow artifacts |
| [#139](https://github.com/fran-eliot/github-framework/issues/139) | Publish results in GitHub Actions job summary |
| [#141](https://github.com/fran-eliot/github-framework/issues/141) | List failed Components in summaries |
| [#143](https://github.com/fran-eliot/github-framework/issues/143) | Include a bounded first diagnostic per failed Component |
| [#145](https://github.com/fran-eliot/github-framework/issues/145) | Run the Validator on Ubuntu and Windows |
| [#147](https://github.com/fran-eliot/github-framework/issues/147) | Emit file-linked GitHub Actions error annotations |

**Current implementation surfaces:** [workflow YAML](../../.github/workflows/framework-validator.yml), [CI summary and annotations](../../scripts/framework_validator/ci_summary.py), [summary tests](../../tests/framework_validator/test_ci_summary.py) and related CLI JSON/report support. The listed Issues were independently checked on GitHub and each was **closed** at the time of review.

**Bounded contract:** workflow triggers for pull requests and pushes to `main`; two operating systems with Python 3.11; `unittest`, Validator report, upload, job summary and annotations. Artifacts have configured retention, not indefinite archival.

### B. Scoped local validation and Component inventory — four closed Issues

| Issue | Implemented feature / supported repository evidence |
| --- | --- |
| [#149](https://github.com/fran-eliot/github-framework/issues/149) | Repeatable `--component FAMILY/NAME` targeted validation |
| [#151](https://github.com/fran-eliot/github-framework/issues/151) | `--list-components` read-only path inventory |
| [#153](https://github.com/fran-eliot/github-framework/issues/153) | JSON Component catalog output |
| [#155](https://github.com/fran-eliot/github-framework/issues/155) | Optional `--details` inventory of basic metadata loading fields |

**Current implementation surfaces:** [CLI](../../scripts/framework_validator/__main__.py), [Component discovery](../../scripts/framework_validator/discovery.py), [CLI tests](../../tests/framework_validator/test_cli.py), [English README](../../README.md) and [Spanish README](../../README_es.md). Each linked Issue was checked as **closed**.

**Bounded contract:** the catalog lists Component paths and optional metadata identity/reading status; catalog success is **not** semantic or structural Component validation. `--component` validates a selected subset, not the entire library. `--components-root` points at a compatible Framework Component-library layout, **not** automatically at an arbitrary external consumer for semantic Adoption assessment.

### C. Supporting JSON output and test hardening

The [current CLI](../../scripts/framework_validator/__main__.py) also provides JSON aggregate/per-Component results, portable relative paths, explicit scope reporting and controlled file output. The [Unreleased Changelog](../../CHANGELOG.md) records these as **Changed**, not a separate newly authorized product.

The post-tag file comparison included six Validator-relevant paths:

| Path | Compare additions | Compare deletions |
| --- | ---: | ---: |
| `.github/workflows/framework-validator.yml` | 56 | 0 |
| `scripts/framework_validator/__main__.py` | 265 | 22 |
| `scripts/framework_validator/ci_summary.py` | 142 | 0 |
| `scripts/framework_validator/discovery.py` | 6 | 3 |
| `tests/framework_validator/test_ci_summary.py` | 372 | 0 |
| `tests/framework_validator/test_cli.py` | 917 | 2 |

These are GitHub compare line-change statistics, not individual Issue attribution, a complete dependency review or a guarantee that changes outside these paths are irrelevant to a possible release.

## 3. Baseline and current test inventory

Direct source inspection of test definitions at tag `v0.10.0` versus current `main`:

| Test module | `v0.10.0` definitions | Current definitions |
| --- | ---: | ---: |
| `tests/framework_validator/test_validation.py` | 102 | 102 |
| `tests/framework_validator/test_cli.py` | 7 | 43 |
| `tests/framework_validator/test_ci_summary.py` | 0 (file absent in tag diff) | 16 |
| **Total** | **109** | **161** |

This is a **static count of `test_*` method definitions** in the inspected source files. It is not itself an execution result. The corresponding [Framework Validator CI run #43646424380](https://github.com/fran-eliot/github-framework/actions/runs/43646424380), associated with the **PR #307 head**, has both Windows and Ubuntu jobs marked successful. The inspected Ubuntu job log explicitly records **`Ran 161 tests`** followed by **`OK`**. This supports that particular run, not a freshly tested future release candidate or a claim of full branch/code coverage.

## 4. Candidate future release boundaries (not a selection)

The two groups appear suitable for **consideration together** as one bounded Framework Validator maintenance increment: CI observability + scoped Component development workflows, with their report formats, documentation and tests. This is a **candidate classification**, not a selection or approval of a version.

A separate release-scope decision must resolve:

1. **What exactly is included?** Pin a candidate commit; identify the complete file set and whether the numerous post-tag Discovery/Governance/Only Film documents are carried forward in a repository-wide release or deliberately separated. Do not equate the six Validator source/test paths with the full `v0.10.0...main` diff.
2. **What is the compatible public contract?** Reconcile CLI switches, JSON output fields, exit codes, filtering caveats and `--details` behavior against both READMEs and the Changelog, with explicit compatibility expectations.
3. **What are release acceptance gates?** Run/recheck test suite, full-library validation and target-scope checks on the **pinned proposed release reference**, on both supported CI platforms; inspect JSON reports and annotations, not just a generic green badge.
4. **What is the risk of packaging and release?** Review branch freshness, prior-release baseline, dependencies (including pinned PyYAML in CI), permission configuration, artifact retention, release notes, rollback/recovery expectations and downstream compatibility appropriate to a documentation/CLI Framework release.
5. **What remains deliberately excluded?** External-consumer semantic Assessment automation, automatic Adoption Decisions, generation/mutation of consumers, new untested Component families, a new user-study claim, and an implied `v1.0.0` stability declaration.

The observed **161-test successful PR-head run** satisfies only one bounded evidence gate. It does not close these release-specific checks by itself.

## 5. Disposition

**Inventory outcome: two coherent, already-integrated Unreleased Validator feature groups, plus supporting report/test changes.** A small future release-scope proposal might be defensible for maintainer review, **but no release is authorized or scheduled** by this document.

With no independent participants available, [UX-02](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md) remains **`Prepared — Not Executed`**. Do not represent this source/CI inventory as independent usability evidence.

Only GitHub Framework Discovery documentation is changed here. No consumer modification, Only Film Application/Integration, code mutation, new Issue, Sprint, milestone, target version, tag or GitHub Release is created.
