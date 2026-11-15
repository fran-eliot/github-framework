# Component Catalog → Targeted Validation: Practical Workflow

This guide demonstrates a **read-only** selection and validation workflow for the implemented GitHub Framework Component library. Commands are run from the **GitHub Framework repository root** with Python 3.11 and PyYAML installed.

It does not assess, apply, or integrate an existing consumer repository. In particular, it does not infer any Adoption Decision, modify Only Film, or establish that a consumer's tools, tests, or deployment run successfully.

## 1. Discover Components

Start with the actual tracked Component library:

```bash
python -m scripts.framework_validator --list-components --format json --family documentation --details
```

The JSON `components` array contains portable `FAMILY/NAME` paths. `details` reports the currently readable metadata for each selected Component. This **catalog listing is not a validation pass**.

## 2. Export a bounded, verifiable selection

Select one Documentation Component after deterministic path sorting:

```bash
python -m scripts.framework_validator --list-components --format json --family documentation --sort-by path --limit 1 --details --catalog-metadata-sha256 --catalog-content-sha256 --output selected-components.json
```

This creates a JSON file in the current directory. Its `components` array identifies the **page**, not the full library. `metadata_sha256` hashes the bytes of `metadata.yml`; `content_sha256` covers regular files within the Component, including their relative paths. Neither digest authenticates who produced the JSON.

For an unpaginated selection, omit `--limit 1`. To select a different family, replace `documentation` with `readme` or `workflow`. The catalog source must remain the same library when checking it later.

## 3. Validate exactly the exported selection

```bash
python -m scripts.framework_validator --catalog-input selected-components.json --catalog-verify-details --catalog-verify-sha256 --catalog-verify-content-sha256 --format json
```

The three optional preflight checks compare the exported metadata fields, raw `metadata.yml` digest and complete Component file-tree digest against the current local library. Only after they pass does the Validator check the selected Components.

A successful JSON report returns `status: "passed"`, `components_discovered: 1` in this one-Component example, and a `scope.component_paths` array equal to the exported selection. The precise Component path depends on the library. The report is **filtered** and is not proof of whole-library validation.

To validate the entire library instead, run separately:

```bash
python -m scripts.framework_validator --format json
```

## 4. Interpret exit status and changes

| Exit code | Interpretation for this workflow |
| --- | --- |
| `0` | The requested validation completed successfully |
| `1` | Validation failed (or a listing had no matching Components) |
| `2` | Invalid arguments, unusable input, failed export, or a rejected/stale digest preflight |

If an exported Component file is edited, renamed, added, or removed before step 3, the `--catalog-verify-content-sha256` preflight rejects the old snapshot. The CLI does not change the Component or repair the mismatch; export a new catalog **only after reviewing the change**.

A file change can leave the ordinary metadata validation passing. **Validation success and content snapshot consistency are different claims.** Rejecting a stale digest says the content differs from the saved snapshot; it does not mean the modified content is invalid.

The SHA-256 checks reject symbolic links, and full-content verification checks file size and modification time around reads. They are not an atomic filesystem snapshot, a signed attestation, or a verification of a consumer repository.

## 5. Use a custom Component library (optional)

The same selection workflow works against an existing folder containing the `readme/`, `documentation/`, and/or `workflow/` Component family directories. Pass the **same** root to both commands:

```bash
python -m scripts.framework_validator --components-root path/to/framework/components --list-components --format json --details --catalog-content-sha256 --output selected-components.json
python -m scripts.framework_validator --components-root path/to/framework/components --catalog-input selected-components.json --catalog-verify-content-sha256 --format json
```

This validates Framework **Component metadata and supported artifacts**, not arbitrary application repositories or their runtime. The selection must contain existing `FAMILY/NAME` Component paths in that library.

### Relocated Component library regression

The automated suite also creates a **separate temporary Component library** with one tracked README, Documentation and Workflow Component copied from this repository. It verifies complete three-family discovery and full-library validation, then exports a Workflow-only catalog with metadata and content SHA-256 and reimports it for scoped validation. This tests the documented `--components-root` behavior without changing the tracked source. It is **not** a consumer application test, a Template assessment or evidence of external interoperability.

## 6. Automated and reproducible coverage

The CI job executes `python -m scripts.framework_validator.smoke` on Ubuntu and Windows. That smoke test also copies a **real tracked Documentation Component** into a temporary library and exercises the entire flow: export both digests, verify the snapshot, change the **temporary copy's README**, confirm a stale-content rejection, and confirm that ordinary targeted validation can still pass. The tracked Component is never changed.

### CI artifacts for inspection

The [Framework Validator workflow](../../.github/workflows/framework-validator.yml) exports an **unfiltered** detailed Component catalog with both SHA-256 fields and immediately runs all three optional verification checks against that catalog. On successful jobs, GitHub Actions provides a downloadable `framework-component-catalog-ubuntu-latest` or `framework-component-catalog-windows-latest` artifact containing `component-catalog.json` and `catalog-verification-report.json` (7-day retention). The verification report is a targeted full-selection Validator result; it does not replace the separate `validator-report.json` artifact from the ordinary full-library validation step. The catalog describes the checked-out revision in that CI run, not necessarily the current tip of `main`.

### Cross-platform parity gate

The CI job explicitly disables Git's automatic CRLF checkout conversion **before checkout** so that the same tracked file bytes are hashed on Ubuntu and Windows. The parity gate compares raw bytes indirectly through SHA-256; normalizing hashes after reading files would conceal actual byte differences.

After both platform validation jobs succeed, a separate CI job downloads the Ubuntu and Windows catalog artifacts and compares their **complete JSON catalogs**, including the Component path inventory, metadata fields, and both SHA-256 digests. The job fails on any catalog difference or invalid/missing artifact; it does not silently ignore platform-specific variations. On a mismatch, its error output identifies the differing Component paths and **field names** (such as `metadata_sha256` or `content_sha256`) plus top-level catalog differences, with a bounded number of entries rather than printing raw file contents or entire digests. The comparison uses the catalogs from the same GitHub Actions run/checked-out commit. A parity pass means the catalog snapshots match between these environments, **not** that either source is cryptographically authenticated or a consumer application has been verified.

The job stops at a failing export or verification, while the separate standard Validator report and its diagnostics still run via `always()`. GitHub's artifact association supports traceability to the workflow run but is not a signed attestation; consumers should independently verify the trusted commit and source.

For the bounded default and opt-in output guarantees covered by isolated regression tests, consult the [Validator CLI/JSON Compatibility Contract](validator-compatibility-contract.md).

See [Framework Validation](../../README.md) for the full CLI reference and [Existing Repository Adoption](../../framework/adoption/README.md) for the distinct, human-reviewed consumer Assessment process.
