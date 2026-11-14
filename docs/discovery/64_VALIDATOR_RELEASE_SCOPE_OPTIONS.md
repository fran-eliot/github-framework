# 64 — Framework Validator Release Scope Options

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Date | 2026-11-14 |
| Stage | Discovery — release-scope decision preparation |
| Published baseline | `v0.10.0` (`3c4b21a26e4e85eeef705fefd48323ffd918e681`) |
| Reviewed branch | `main` at the time of this investigation; **no release candidate SHA pinned** |
| Release / version / milestone / Sprint | **Not selected, approved or opened** |
| UX-02 | `Prepared — Not Executed` (no independent participants available) |
| Consumer operations | **None** |

> This is a decision-support document. It does not approve release scope, select a version, initiate a release procedure or authorize consumer Application/Integration.

## 1. Problem and confirmed baseline

The [Validator inventory #63](63_VALIDATOR_UNRELEASED_SCOPE_INVENTORY.md) identifies **eleven closed enhancement Issues**, grouped as CI reporting/diagnostics (seven) and targeted validation/Component inventory (four). The [Unreleased Changelog](../../CHANGELOG.md) describes these changes without a release assignment; the [Roadmap](../../ROADMAP.md) likewise records them as integrated but Unreleased.

The inspected GitHub comparison `v0.10.0...main` returned **633 commits ahead, zero behind, and 78 changed-file entries**. This is a **repository-wide** comparison, incorporating the completed Only Film documentary Assessment and Discovery/governance documentation. These aggregate figures will change whenever `main` advances and **must not** be interpreted as Validator-only release scope. A release candidate has not been fixed, and this review does not assert that all unrelated documents have been individually audited.

The Validator-related paths identified by #63 are:

- `.github/workflows/framework-validator.yml`
- `scripts/framework_validator/__main__.py`
- `scripts/framework_validator/ci_summary.py`
- `scripts/framework_validator/discovery.py`
- `tests/framework_validator/test_ci_summary.py`
- `tests/framework_validator/test_cli.py`

Existing `tests/framework_validator/test_validation.py` remains part of the suite although its content was not changed in the compared inventory. CLI usage documentation lives in [README.md](../../README.md) and [README_es.md](../../README_es.md); the Unreleased notes are in [CHANGELOG.md](../../CHANGELOG.md). **The six modified source/CI/test paths are not, by themselves, a complete isolated release bill of materials.**

## 2. Candidate release choices — not approved

| Option | Proposed release unit | Strength | Risk / unresolved work | Disposition |
| --- | --- | --- | --- | --- |
| **A — Publish a reviewed complete repository snapshot** | Select and pin one commit after inspecting the **entire** `v0.10.0...candidate` diff, including the many post-release Adoption, governance and discovery documents | Straightforward source ancestry and reproducible single-state release | Requires accepting and describing all included changes accurately, not only Validator features; must not imply the completed Only Film Assessment is an Application or certified consumer | **Candidate for review**, not yet authorized |
| **B — Prepare a dedicated, bounded release candidate** | Explicitly separate the desired Validator changes and necessary tests/docs from unrelated post-tag work in a reviewed candidate branch | Smaller conceptual change set and potentially narrower release notes | Nontrivial dependency/merge/rebase and maintenance risk; needs proof that CLI, CI, tests and both READMEs remain coherent; cannot simply tag `main` and pretend excluded files are absent | **Conditional fallback** if the full snapshot cannot be accepted |
| **C — Keep the Validator changes Unreleased** | No release candidate, tag or version assignment yet | Avoids premature packaging; allows further focused evidence | Users of the published tag do not receive the post-tag improvements | **Valid default pending an express release-scope decision** |

The primary technical distinction is **what Git commit actually contains**. A tag on a reviewed `main` commit includes **all tracked files in that snapshot**, even if release notes emphasize the Validator. Omitting other modifications from the narrative does not omit them from a Git release. Option B therefore requires a **genuinely distinct candidate tree**, not merely a shorter Changelog.

## 3. Minimum acceptance gates before choosing an executable release plan

| Gate | Required evidence for a later approval | Current finding |
| --- | --- | --- |
| **G1 — Candidate identity** | An exact candidate SHA and ancestry from `v0.10.0`; compare file list at that SHA | **Open** — current `main` is mutable |
| **G2 — Full included scope** | Review of **every** changed file against the published tag, classifying Validator product changes, required docs/tests, other integrated docs/governance and any unintended change | **Open** — #63 focused on Validator-related paths |
| **G3 — CLI / JSON compatibility** | Explicit check of `--component`, `--family`, `--list-components`, `--details`, `--components-root`, report paths, schema/keys and exit-code behavior against both READMEs and tests | **Partially supported** by code/tests; no candidate-wide compatibility sign-off |
| **G4 — Candidate CI and Validator self-check** | Windows + Ubuntu CI on the **candidate SHA**, test results, full-library validation, representative partial-scope runs, report contents and artifact/annotation checks | **Open on candidate**; earlier PR #307 run 43646424380 reported 161 tests passing in Ubuntu and successful jobs on both OS |
| **G5 — Documentation and release notes** | Reconcile [Unreleased Changelog](../../CHANGELOG.md), [Roadmap](../../ROADMAP.md), [Project Status](../governance/12_PROJECT_STATUS.md), [Backlog](../governance/14_BACKLOG.md) and public docs with the **actual** release tree | **Not authorized**; existing documents still say Unreleased |
| **G6 — Safety and compatibility boundaries** | Review Python/PyYAML assumptions, GitHub Actions permissions/artifact retention, cross-platform paths and handling of malformed metadata; preserve semantic-vs-deterministic boundary | **Partially supported** by existing code and CI, not an exhaustive release audit |
| **G7 — Maintainer release authorization** | Explicit decision on selected option, target version, branch/commit, acceptance conditions and publication responsibility, separate from simply merging this Discovery | **Not given** |

The observed **161 passing tests** in an earlier PR-head CI run are useful historical evidence but do **not** by themselves satisfy G4 for an as-yet-unselected release candidate. No release checks are being presented as executed by this document.

## 4. What the existing evidence does and does not justify

**Supported:** the post-tag Validator additions form two coherent groups; the 11 associated Issues were reported closed; both public README versions describe the CLI; the CI pipeline reports successful Linux/Windows jobs on an inspected PR; a bounded release-scope review is a meaningful next engineering decision.

**Not yet supported:** a fixed releasable snapshot, a clean isolated code-only patch, acceptance of all repository-wide post-release content, full release test evidence, semantic Adoption automation, a stable `v1.0.0` maturity claim, or independent usability outcomes.

The [completed Only Film Assessment](../../framework/adoption/examples/only-film-assessment.md) remains a source-qualified **documentary** result. Its 28 approved classifications and 28 decisions do **not** authorize changes to Only Film or consumer Application/Integration. The unavailable independent participants do not convert internal review into [UX-02](54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md) execution.

## 5. Proposed decision sequence

1. Maintain **Option C** until the maintainer explicitly selects **A** or **B**, or another scoped alternative.
2. If **A** is preferred, pin a candidate commit and build a **complete release manifest** from that exact tree. Confirm that documentation/Discovery changes are an acceptable part of that snapshot, even if Validator changes are the release headline.
3. If **B** is preferred, first design a truly separate candidate tree with all transitive code, tests, workflow and documentation requirements; then inspect the resulting full diff and repeat acceptance checks. Avoid unreviewed cherry-picks or misleading release notes.
4. Define the version and release process **only after** scope and gates are accepted. A potential maintenance increment must not be silently labeled `v1.0.0` or assigned another version by this Discovery.
5. Check all candidate CI results at the selected SHA before any tag or GitHub Release; record failures, missing artifacts and unverified conditions rather than treating a previous green PR as sufficient.

## 6. Outcome

**Discovery conclusion: release-scope options identified; no release path selected.**

No implementation, Application, Integration, test execution, branch for release, issue, milestone, Sprint, target version, tag or publication is authorized here. Merging this document accepts only a **record of the choice and prerequisites**, not the decision to publish.
