# Framework Validator — Candidate Release Notes (Unreleased Draft)

> **Historical preparation artifact — superseded by the published [v0.12.0 GitHub Release](https://github.com/fran-eliot/github-framework/releases/tag/v0.12.0).** The tag was published on 2026-11-15 at `8fc0a036489a60f72c2ee66185bbd5e53b3a89c1`. This document preserves the **pre-publication draft and gates as historical context**; its statements that approval/publication is pending are no longer the current state. See [CHANGELOG](../../CHANGELOG.md) and the official GitHub Release for the published scope.

> **Draft for maintainer review only — NOT approved for publication.**
>
> No release version, release date, tag, GitHub Release, Sprint or milestone is assigned by this document. Do not copy these notes to a published Release until an exact candidate commit, accompanying CI evidence, release scope and maintainer authorization have been confirmed.

**Published baseline:** [v0.11.0](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0), commit `55680b388b0fd8256c95e15866e53d21cc9a5033`  
**Draft source baseline:** `main` at [`5890237d4513404bc99d144f7cb33b4d7ea42d17`](https://github.com/fran-eliot/github-framework/commit/5890237d4513404bc99d144f7cb33b4d7ea42d17), following merged [PR #370](https://github.com/fran-eliot/github-framework/pull/370)  
**Preparation date:** 2026-11-15  
**Preparation direction:** Option A selected by the maintainer on 2026-11-15; `v0.12.0` is proposed, not approved as a tag or publication. The final candidate SHA and approval of these notes remain outstanding.
**Status:** `Unreleased — Draft`

For explicit choices and outstanding authorization checks, consult the [publication decision proposal](framework-validator-publication-decision-proposal-20261115.md). This draft remains unpublished regardless of whether that proposal is merged.

This draft groups user-visible behavior recorded in [CHANGELOG.md > Unreleased](../../CHANGELOG.md), linked implementation guides and merged PRs. It deliberately excludes older v0.11.0 capabilities that are already published. It is not an exhaustive commit-by-commit ledger.

---

## Proposed public-facing release notes

### Component catalog: discover, select and export

The Framework Validator now supports more flexible **read-only catalog exploration** across README, Documentation and Workflow Component libraries.

- Filter by Component paths with `--match` / `--exclude`, family with `--family`, metadata load status, declared Component status and metadata ID, name or version.
- Sort catalogs by path or supported metadata fields, with ascending/descending order and deterministic handling of missing metadata.
- Page selected results using `--limit` and `--offset`, including next/previous offsets in JSON output.
- Request optional family, metadata-loading and declared-status summaries.
- Export JSON catalogs to a file, preserving a pre-existing output when export fails.

The ordinary `--list-components` behavior stays available without the new optional fields. See the [CLI/JSON compatibility contract](../implementation/validator-compatibility-contract.md) for explicitly tested guarantees and limits.

### Export a saved selection and validate it later

A JSON catalog can be reused as a **targeted validation selection** using `--catalog-input PATH` or read from stdin with `--catalog-input -`. Only the selected Component paths are validated; a filtered or paginated selection does **not** prove that the full library passes.

Optional preflight checks compare the saved catalog with local metadata details, raw `metadata.yml` SHA-256 digests and regular-file-tree content SHA-256 digests. Changed, removed or added files can cause the imported selection to be rejected before validation. Symlink protections and file-read consistency checks reduce unsafe or stale snapshots.

These SHA-256 checks show **local consistency with a supplied snapshot**, not a trusted publisher signature or atomic filesystem snapshot. Consult the [practical catalog workflow](../implementation/validator-catalog-workflow.md) for executable examples and exit codes.

### CI evidence and cross-platform reproducibility

Framework Validator CI on Ubuntu and Windows now exports a detailed, verifiable Component catalog and its targeted validation report as downloadable GitHub Actions artifacts, retained for seven days.

A separate parity job downloads both catalogs **from the same workflow run** and fails if their inventories, metadata or content SHA-256 digests differ. Checkout conversion is disabled before hashing to avoid spurious Unix/Windows line-ending differences. When parity fails, its diagnostics identify mismatching fields and limit output size.

The existing ordinary validation report and its CI diagnostics remain separate from catalog evidence. These artifacts are not signed attestations.

### Regression tests and practical documentation

The post-v0.11.0 tests cover catalog filtering, sorting, pagination, snapshot integrity, import and verification, output safety, CLI/JSON compatibility and cross-platform parity.

A new practical guide demonstrates selection → export → verified validation using real Framework Components and a temporary Component copy in smoke tests. A read-only scope study clarifies why **validating a Framework Component library is not equivalent to validating an arbitrary application repository**; it does not claim that a consumer application was executed or certified.

### Scope and compatibility notes

- These features operate on **Framework Component libraries**, not generic application structures.
- Existing Repository Adoption remains a separate, human-reviewed process. **No automatic Assessment decisions, Application or Integration are introduced here.**
- JSON and CLI regression tests protect documented scenarios, but do not establish a versioned public schema or universal backward compatibility for all optional flag combinations.
- No changes to the Only Film consumer or its pinned documentary Assessment are included.
- Release consumers should review the [compatibility contract](../implementation/validator-compatibility-contract.md) before relying on optional JSON fields and local integrity checks.

---

## Maintainer-only verification before publication

The notes above are **proposed text**, not current release claims. Verify each item against the final immutable candidate, then edit this draft as necessary.

| Gate | Evidence at draft time | Required before publishing |
| --- | --- | --- |
| Compare published tag against candidate | [Pinned historical delta](framework-validator-v0110-to-main-delta-20261115.md) records 246 commits ahead, 0 behind and 21 changed paths **at an earlier SHA** after PR #368 | Re-run diff at the exact future candidate SHA, including #369–#370 and this draft if merged |
| Ubuntu/Windows regression and smoke | [PR #370 workflow](https://github.com/fran-eliot/github-framework/actions/runs/43759208158) completed successfully | Confirm a CI run at the selected release candidate SHA |
| Cross-platform catalog parity | Same PR workflow completed successfully | Confirm parity at candidate SHA and inspect associated catalog artifacts |
| CLI/JSON consumer compatibility | [Bounded contract](../implementation/validator-compatibility-contract.md) and regression coverage | Review any additional consumer-relevant guarantees/limitations; document deliberate breaking changes, if any |
| Consumer application interoperability | [Read-only scope study](../implementation/aula-robotica-validator-consumer-boundary-20261115.md) and synthetic fixture tests | Do **not** assert real consumer validation; independently authorize and scope any further exercise |
| Version, release scope and release notes | Draft text only | Obtain explicit maintainer approval of the version, exact tag SHA and publication text |
| Release publication | None | Publish only following separate authorization |

**Current recommendation:** use this draft to evaluate scope and readiness. Do **not** assign a version or publish from the draft alone.

## Evidence and traceability

- [Unreleased CHANGELOG](../../CHANGELOG.md) — detailed change log
- [Pinned tag-to-main comparison](framework-validator-v0110-to-main-delta-20261115.md) — historical file-level audit
- [Unreleased delivery readiness review](framework-validator-unreleased-readiness-20261115.md) — evidence limits and gates
- [Practical Component catalog workflow](../implementation/validator-catalog-workflow.md)
- [Framework Validator CLI/JSON compatibility contract](../implementation/validator-compatibility-contract.md)
- [Read-only consumer boundary study](../implementation/aula-robotica-validator-consumer-boundary-20261115.md)

This document does not approve, perform or imply modifications to Only Film or Aula Robótica, nor a new Adoption Assessment, Application or Integration.
