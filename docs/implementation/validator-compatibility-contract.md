# Framework Validator — CLI/JSON Compatibility Contract

**Status:** Documented regression contract for the current implementation on `main`; not a published version, an immutable JSON schema, or a commitment to indefinite API stability.

This companion to the [practical Component catalog workflow](validator-catalog-workflow.md) records the consumer-visible behavior covered by `tests/framework_validator/test_compatibility_contract.py`. The tests run with a temporary Documentation Component and exercise the CLI through real subprocesses on Ubuntu and Windows in the existing Validator CI matrix.

## Covered behaviors

| Contract | Regression assertion |
| --- | --- |
| Default catalog | `--list-components --format json` emits exactly `components`, `count` and `scope` at the top level; no optional `details` or `pagination` object |
| Opt-in enrichment | `--details`, metadata/content SHA-256 flags, family and metadata summaries add data only when requested; running the default command again preserves the original catalog shape |
| Validation report | Full-library, explicit `--component`, and imported `--catalog-input -` validation expose the existing `status`, `components_discovered`, `component_ids`, `errors`, `components`, `scope`, and `summary` top-level fields |
| Selection scope | An unfiltered full-library validation has `scope.filtered=false`; a one-Component selection reports `scope.filtered=true` and the selected `scope.component_paths` |
| Saved snapshot | Exported JSON is a newline-terminated UTF-8 file; a metadata/content-verified import succeeds with unchanged input |
| Failure safety | Stale content preflight returns code `2` without emitting a validation report; a zero-match catalog returns code `1`; neither overwrites an existing saved catalog |
| Failed validation report | Invalid Component metadata returns code `1` but still emits a structured JSON failure report, including component-level diagnostics and summary counts |
| stdout vs file export | Successful catalog and validation commands serialize equivalent JSON to stdout or `--output`; a failed validation still writes its JSON report and returns `1` |
| Argument-error export safety | An invalid flag combination returns code `2` without clobbering a pre-existing output file |

**Exit codes:** `0` indicates successful requested operation or validation; `1` indicates validation failure or an empty listing; `2` indicates invalid arguments or rejected imported snapshot/export. The same exit code can have different contextual meanings; the caller must also consider which operation was requested.

## Important limitations

- The tests pin the **documented default shapes and selected semantic fields**, not absolute paths, entire serialized JSON documents, key ordering or arbitrary error wording. Local paths and diagnostics can differ between Windows and Ubuntu.
- The one-Component fixture is not a substitute for the real-library smoke test and the CI cross-platform catalog parity gate.
- SHA-256 preflights check consistency against the supplied catalog, not its provenance or the authenticity of the repository.
- A selected Component validation is not a complete repository validation; none of these commands automatically assesses, applies or integrates an external consumer repository.
- This contract is intended as a regression guard for future changes. It is **not** a claim that every CLI option combination or JSON field is externally stable.

## Run the contract tests

From the GitHub Framework repository root, with Python 3.11 and PyYAML installed:

```bash
python -m unittest discover -s tests/framework_validator -p "test_compatibility_contract.py"
```

The usual [Framework Validator CI workflow](../../.github/workflows/framework-validator.yml) also executes these tests as part of its existing suite. Review changes to these assertions alongside any intended CLI/JSON breaking change, and document compatibility implications before proposing a new release.

**Governance:** The [Unreleased delivery readiness review](../releases/framework-validator-unreleased-readiness-20261115.md) remains a pre-release evidence assessment, not release approval. No consumer application, including Only Film, is modified or certified by these checks.
