# Repository Template Composition Preview — Acceptance Verification

**Status:** Complete — Unreleased (formally accepted by maintainer)  
**Baseline:** `6247a34e348b6b4c0f9efe3d16c139f6cf69b34d` (PR #390 merged)  
**Date:** 2026-11-18

The [approved scope](repository-template-composition-preview-delivery-scope.md) defines AC-01–AC-17. Units A–C are integrated. [PR #390 CI](https://github.com/fran-eliot/github-framework/actions/runs/44404005246) completed successfully; it predates the new Unit D assertions. The following matrix maps the approved criteria to verification evidence. The integrated revision and CI results are recorded below; the formal maintainer decision is recorded below.

| Criterion | Verification location |
| --- | --- |
| AC-01 | test_cli: real Template IDs, help |
| AC-02 | test_cli: invalid argument subprocesses |
| AC-03 | test_sources, test_resolution, test_report, test_cli: levels, order, empty groups |
| AC-04 | test_cli: baseline counts and repeatability |
| AC-05 | test_cli: required README-LICENSE, Conceptual evidence |
| AC-06 | test_resolution: nine combinations |
| AC-07 | test_cli: complete conflicting report, exit 1 |
| AC-08 | test_registry: bounded parsing and malformed fixtures; test_cli: source error |
| AC-09 | test_sources: invalid YAML and references; test_cli: duplicate key |
| AC-10 | test_sources: missing, denied, linked and unsupported sources; test_cli: missing metadata |
| AC-11 | test_sources: runtime identity and duplicate matches |
| AC-12 | test_report and test_cli: evidence, counts and reconciliation |
| AC-13 | test_cli: repeated subprocesses, different working directory, success/conflict/error |
| AC-14 | test_cli: fixture tree paths and bytes unchanged with -B |
| AC-15 | Existing Validator tests, smoke and parity workflow |
| AC-16 | Existing Ubuntu/Windows Python 3.11 matrix, expanded preview suite |
| AC-17 | Usage guide and README EN/ES navigation |

## Expected baseline

| Template | Required R/C | Recommended R/C | Optional R/C |
| --- | --- | --- | --- |
| TPL-BACKEND | 8/0 | 5/2 | 3/10 |
| TPL-FULLSTACK | 9/0 | 4/4 | 3/8 |
| TPL-DOCUMENTATION | 8/1 | 2/5 | 1/4 |

These expectations derive from the approved Discovery baseline; production resolution does not hardcode them. Tests execute actual CLI subprocesses in the platform matrix.

## Reproduction

```bash
python -B -m unittest discover -s tests/template_composition_preview -p "test_*.py"
```

The tests snapshot isolated fixture trees, including directory paths and regular file bytes. They do not constitute a system-wide filesystem or network audit. The command has no consumer input or network retrieval path. Permissions are simulated in a targeted test; symlink checks may be skipped on unsupported platforms. Source reads are not atomic snapshots. Registry completeness and consumer conformance are not certified.

Final verification must record the exact tested revision and CI outcome, identify any skipped checks or unavailable evidence, and receive maintainer review before marking delivery complete. No version, Sprint, milestone or consumer change follows automatically.

## Core verification evidence

**Integrated revision:** [`3bc48973dfca8b596e02cc0936c88b88e16b1184`](https://github.com/fran-eliot/github-framework/commit/3bc48973dfca8b596e02cc0936c88b88e16b1184) (PR #391 merged). The PR branch was removed. The [PR CI run 44405148104](https://github.com/fran-eliot/github-framework/actions/runs/44405148104) and [push-to-main run 44406140362](https://github.com/fran-eliot/github-framework/actions/runs/44406140362) both completed successfully. The second run's head SHA is exactly the integrated revision above.

| Evidence on integrated revision | Ubuntu | Windows |
| --- | --- | --- |
| Validator unit/regression suite | 282 tests, OK | 282 tests, OK |
| Composition Preview suite | 24 tests, OK | 24 tests, OK |
| Validator real-library CLI smoke | Success | Success |
| Cross-platform catalog parity | Success (shared job) | Success (shared job) |

Counts and absence of reported skips were checked in the platform job logs, not inferred solely from the workflow status. The same test totals were observed in PR CI. The CLI subprocess assertions compare the reference rows and per-level and aggregate counts for all three canonical Templates, including the required Conceptual README-LICENSE, without embedding those counts in production code. The verified baseline therefore contains 77 reference occurrences (43 Resolved, 34 Conceptual), not 77 distinct Components.

| AC | Core verification assessment |
| --- | --- |
| AC-01–AC-02 | Supported by CLI help, canonical selection and argument error tests |
| AC-03–AC-05 | Supported by ordered groups, zero counts, real baseline replay and required Conceptual evidence |
| AC-06–AC-07 | Supported by nine-case matrix and complete conflict reports |
| AC-08–AC-11 | Supported by bounded registry and strict source fixtures, source-error subprocesses and runtime identity discovery |
| AC-12–AC-13 | Supported by report evidence, count reconciliation and repeated subprocesses |
| AC-14 | Supported within isolated fixture scope by byte/path snapshots for exits 0/1/2 with -B; network and consumer exclusion assessed by code scope, not a system-wide access trace |
| AC-15–AC-16 | Supported by exact integrated-revision CI, both platform test suites, real CLI subprocesses, smoke and parity |
| AC-17 | Supported by the usage guide and English/Spanish README navigation |

No skips were reported by either platform's unittest summaries; the permission-denial fixture simulates an exception, rather than proving all operating-system permission configurations. Registry structural checks cannot prove completeness. No independent user study, consumer conformance test, atomic source snapshot or system-wide filesystem/network audit was performed.

**Recommendation:** accept the four implementation units and AC-01–AC-17 for the bounded approved scope, with the stated evidence limitations. This verification is not itself formal maintainer acceptance, a release candidate or an authorization to publish. The capability remains Unreleased after v0.12.0; no change to Only Film, UX-02, Sprint or milestone.

## Formal delivery acceptance — 2026-11-18

The maintainer formally accepted Repository Template Composition Preview as **Complete — Unreleased**, including all four implementation units and the bounded evidence for AC-01–AC-17. Core verification documentation was integrated through [PR #392](https://github.com/fran-eliot/github-framework/pull/392) at `9896d7ea84df72d73856e6487ecb9ac599f065f9`; its [CI run 44406655239](https://github.com/fran-eliot/github-framework/actions/runs/44406655239) succeeded. The tested implementation baseline and all limitations above remain unchanged. No new release is authorized; v0.12.0 remains the published version. No consumer changes, Sprint or milestone are authorized by this decision.
