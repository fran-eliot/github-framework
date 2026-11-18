# Repository Template Composition Preview — Acceptance Verification

**Status:** Unit D verification candidate; final CI evidence and maintainer acceptance pending  
**Baseline:** `6247a34e348b6b4c0f9efe3d16c139f6cf69b34d` (PR #390 merged)  
**Date:** 2026-11-18

The [approved scope](repository-template-composition-preview-delivery-scope.md) defines AC-01–AC-17. Units A–C are integrated. [PR #390 CI](https://github.com/fran-eliot/github-framework/actions/runs/44404005246) completed successfully; it predates the new Unit D assertions. The following matrix identifies test evidence to review, not a declaration of final acceptance.

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
