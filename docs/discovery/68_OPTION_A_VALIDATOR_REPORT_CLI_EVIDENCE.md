# 68 — Option A: Validator JSON Report and CLI Evidence

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Review date | 2026-11-14 |
| Stage | Discovery — read-only artifact inspection and existing CLI test verification |
| Published baseline | `v0.10.0` |
| **Exact inspected `main` commit** | [`d3dbd4665a9c9e48aaebd7dca54f5b8ada3e5fc4`](https://github.com/fran-eliot/github-framework/commit/d3dbd4665a9c9e48aaebd7dca54f5b8ada3e5fc4) |
| Workflow | [Framework Validator push run 43649322843](https://github.com/fran-eliot/github-framework/actions/runs/43649322843) — **completed / success** |
| Release candidate | **Not selected or approved** |
| UX-02 | `Prepared — Not Executed` (no independent participants) |
| Consumer mutations | **None** |

> This report distinguishes **direct observation of two real CI JSON files**, **CI execution of existing CLI tests**, and **CLI command examples not separately executed**. Its findings belong to one immutable `main` commit, not an approved release candidate or a claim of semantic Adoption validation.

## 1. Source identity and actual CI run

After PR #313 was merged, GitHub showed `main` at `d3dbd4665a9c9e48aaebd7dca54f5b8ada3e5fc4`. The comparison `v0.10.0...d3dbd4665a9c9e48aaebd7dca54f5b8ada3e5fc4` contained **642 repository-wide commits ahead**, zero behind, and **82 changed-file entries**. The additional Discovery files reflect the research being merged, not new Validator features.

The GitHub Actions workflow-run collection showed a **`push` to `main`** at exactly that SHA with `completed / success`. Its two jobs were:

| Job | CI conclusion | Log evidence |
| --- | --- | --- |
| Windows / Python 3.11 | `success` | `Ran 161 tests in 2.439s`, `OK`; Validator and artifact upload steps successful |
| Ubuntu / Python 3.11 | `success` | `Ran 161 tests in 1.271s`, `OK`; Validator and artifact upload steps successful |

This establishes the tests' executed outcome at the **same code revision** as the downloaded reports. The CI workflow runs the normal full-library validation. It does **not** itself run an independent external-consumer semantic Assessment or manually execute all CLI combinations.

## 2. Downloaded JSON artifact inspection

Both **actual uploaded ZIP archives** were retrieved from the run, opened, and the embedded `validator-report.json` parsed and compared:

| Property | Ubuntu | Windows |
| --- | --- | --- |
| Artifact ID | [14134564872](https://github.com/fran-eliot/github-framework/actions/runs/43649322843/artifacts/14134564872) | [14135126874](https://github.com/fran-eliot/github-framework/actions/runs/43649322843/artifacts/14135126874) |
| JSON `status` | `passed` | `passed` |
| `components_discovered` | **21** | **21** |
| `summary.passed_components` | **21** | **21** |
| `summary.failed_components` | **0** | **0** |
| `summary.error_count` | **0** | **0** |
| Top-level `errors` | Empty | Empty |
| `scope.families` | `readme`, `documentation`, `workflow` | Same |
| `scope.filtered` | `false` | `false` |
| Each Component's status/errors | All `passed` / empty | Same |

The JSONs contain the following **seven top-level keys**: `status`, `components_discovered`, `component_ids`, `errors`, `components`, `scope`, `summary`.

**Cross-platform comparison:** The top-level content, ordered 21 Component IDs, and ordered Component records are identical **after removing only each record's machine-specific absolute `path` field**. Relative Component paths, IDs, statuses and error arrays match exactly. Raw artifact ZIP hashes differ, and **absolute paths** differ in Windows (`D:\\a\\...`) versus Ubuntu (`/home/runner/work/...`); this is expected platform-specific representation, not evidence of a result mismatch.

All 21 Component records have `status: passed` and empty `errors`. The report confirms **full-scope metadata/component validation as implemented by the Framework Validator**. It does **not** certify templates against every consumer, verify all file links, measure code coverage or establish an Adoption Decision.

The artifacts have a **seven-day retention window** configured by the workflow and were listed as not expired during inspection; their reported expiration is 2026-11-21 UTC. Future reviewers should not assume the download links will work indefinitely.

## 3. CLI functionality exercised through the passing test suite

At the inspected SHA, [`tests/framework_validator/test_cli.py`](../../tests/framework_validator/test_cli.py) contains **43 `test_*` methods** and was included in the 161-test passing CI run on both operating systems. Direct inspection of the test source confirms these bounded scenarios:

| Behavior | Representative existing tests | Evidence classification |
| --- | --- | --- |
| Target one Component and report filtered scope | `test_component_filter_selects_only_requested_directory` | Test source inspected; executed as part of both successful CI jobs |
| Validate missing metadata in targeted scope | `test_component_filter_detects_missing_metadata` | Same; negative-case validation |
| Repeat `--component` across families, reject invalid/missing selections | `test_cli_component_filter_repeated_and_cross_family`, `test_cli_component_filter_rejects_invalid_or_missing_paths` | Same; subprocess test paths included |
| List paths without requiring valid metadata | `test_cli_list_components_without_loading_metadata` | Same; read-only discovery behavior |
| Return JSON Component catalog | `test_cli_list_components_json_catalog` | Same |
| Return `--details`, including missing or invalid metadata | `test_cli_detailed_catalog_includes_metadata_and_missing_files`, `test_cli_detailed_catalog_handles_invalid_yaml` | Same; metadata loading state is not structural validation |
| Reject `--details` without JSON catalog mode | `test_cli_details_requires_json_catalog` | Same; invalid argument combinations |
| Write JSON report on successful and failed validation | `test_json_report_file_on_success`, `test_json_report_file_on_validation_failure` | Same; file output paths |

**Important distinction:** The test suite's subprocess cases use **isolated temporary Component directories** to test contract behavior. This review did **not** invoke each CLI command independently against the full `main` Component library in a local checkout. The real workflow **did** execute full-scope validation in both operating systems, producing the actual reports inspected in Section 2. Thus **full-scope JSON validation is directly observed**; **selected CLI modes are supported by source-inspected, CI-executed tests**, not by separately saved manual CLI outputs.

## 4. Reproducible follow-up commands — not executed here

The following examples describe **what to run later** on a fixed checkout if a maintainer wants a separate CLI smoke record:

```bash
python -m scripts.framework_validator --format json --output validator-report.json
python -m scripts.framework_validator --component documentation/architecture --format json
python -m scripts.framework_validator --list-components --format json
python -m scripts.framework_validator --list-components --format json --details
python -m scripts.framework_validator --list-components --family documentation
```

These commands are **examples**, not observed additional executions or a release acceptance sign-off. The `--component` result is **partial**; the catalog listing, even with metadata details, is **discovery rather than semantic or structural validation**. A future candidate-specific smoke run should capture output and exit codes, not infer them from these examples.

## 5. Outstanding release gates and technical observations

| Gate | Status at this inspected SHA |
| --- | --- |
| Cross-platform test execution | **Observed PASS**: 161 tests each on Windows/Ubuntu |
| Whole-library JSON report content | **Observed PASS**: 21/21 Components, no errors, scope unfiltered; normalized reports agree |
| Selected CLI contract cases | **Covered by passing tests**; no additional standalone candidate-level CLI transcript |
| Workflow actions compatibility | **Warning remains**: `actions/checkout@v4`, `actions/setup-python@v5`, `actions/upload-artifact@v4` target deprecated Node.js 20 and runners force Node.js 24; both jobs passed |
| Full repository snapshot acceptance | **Open** — large historical documentary payload has not received exhaustive publication-level approval |
| Explicit release candidate, version and publication decision | **Not given** |
| Independent first-time usability | **Not executed** |

The warning was observed in both job logs. It did not fail the checks; an action-version compatibility upgrade must be evaluated and tested separately, not assumed safe.

## 6. Conclusion

**New evidence materially strengthens Option A's technical case:** exact-`main` cross-platform CI results are supported by direct inspection of the uploaded JSON, including **21/21 passed Component records** and agreement across platforms after normalizing absolute paths. The CLI's key filtered and catalog scenarios are covered by the same successful 161-test suite, with the evidence limits stated above.

**No release GO is declared.** A future immutable candidate, accepted full snapshot scope, separately reviewed compatibility concerns and explicit release approval remain prerequisites. UX-02 stays `Prepared — Not Executed`. No GitHub Framework production code, consumer repository, Only Film Application/Integration, Sprint, milestone, tag, version or release is changed or authorized by this Discovery report.
