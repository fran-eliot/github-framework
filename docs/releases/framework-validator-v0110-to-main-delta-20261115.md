# Framework Validator — Published Tag to Main Delta Evidence

**Review date:** 2026-11-15  
**Published baseline:** [v0.11.0](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0) at `55680b388b0fd8256c95e15866e53d21cc9a5033`  
**Reviewed main:** [`78742038065c8feb9ebf081132d132b4cf7115d9`](https://github.com/fran-eliot/github-framework/commit/78742038065c8feb9ebf081132d132b4cf7115d9) (after [PR #368](https://github.com/fran-eliot/github-framework/pull/368))  
**Method:** GitHub compare endpoint, **published tag commit → pinned main commit**. This is a repository change inventory, not a new release decision.

[Inspect the exact comparison](https://github.com/fran-eliot/github-framework/compare/55680b388b0fd8256c95e15866e53d21cc9a5033...78742038065c8feb9ebf081132d132b4cf7115d9)

## 1. Exact recorded comparison

| Measure | Observed |
| --- | --- |
| Compare status | `ahead` |
| Commits ahead of published tag | **246** |
| Commits behind published tag | **0** |
| Files returned by comparison | **21** |
| Diffed target | Current `main` at the pinned SHA above, **not** the future release candidate |
| Publication status | All post-tag changes remain **Unreleased** |

The 246 value counts Git commits between the refs, including workflow commits such as merges. It is **not** a count of independent features, PRs, user-facing changes, or tests. File counts and statuses describe the final diff between two commits, not every intermediate edit.

## 2. Changed-path classification

The GitHub comparison returned 21 changed files. Grouping below is based on file paths and recorded changes, not a claim that all changes in a group are semantically equivalent.

| Area | Changed paths | Count |
| --- | --- | --- |
| Validator implementation | `scripts/framework_validator/__main__.py` (modified); `integrity.py`, `ci_catalog_parity.py` (added) | **3** |
| Automated tests and smoke coverage | `scripts/framework_validator/smoke.py` (modified); `tests/framework_validator/test_cli.py` (modified); `test_integrity.py`, `test_ci_catalog_parity.py`, `test_compatibility_contract.py`, `test_consumer_boundary.py` (added) | **6** |
| CI workflow | `.github/workflows/framework-validator.yml` (modified) | **1** |
| User-facing documentation | `README.md`, `README_es.md` (modified) | **2** |
| Roadmap and history | `CHANGELOG.md`, `ROADMAP.md` (modified) | **2** |
| Governance | `docs/governance/12_PROJECT_STATUS.md`, `14_BACKLOG.md`, `16_CONTINUITY_KIT.md` (modified) | **3** |
| Guides and evidence | `docs/implementation/validator-catalog-workflow.md`, `validator-compatibility-contract.md`, `aula-robotica-validator-consumer-boundary-20261115.md` and `docs/releases/framework-validator-unreleased-readiness-20261115.md` (added) | **4** |
| **Total** | | **21** |

This comparison does not by itself show an external consumer integration, an application deployment, a new Framework Component, or new Repository Template versions.

## 3. Functional and evidence cross-check

These statements rely on the merged changes and the linked documentation; they are **not** independent execution claims made by this comparison:

- **Component catalog CLI:** filtering, sorting, summaries, pagination, atomic JSON export and saved selections; see [README](../../README.md) and [Unreleased changelog](../../CHANGELOG.md).
- **Optional consistency checking:** `metadata_sha256` and `content_sha256` catalog fields with imported-selection preflight; they check local bytes against an imported snapshot, not provenance.
- **CI reproducibility:** two platform validation jobs, catalog/report artifacts and a third catalog parity job; the original [PR #363 parity failure](https://github.com/fran-eliot/github-framework/actions/runs/43747497334) was followed by the corrected [three-job successful run](https://github.com/fran-eliot/github-framework/actions/runs/43748589509).
- **Backward-compatibility guards:** [CLI/JSON compatibility contract](../implementation/validator-compatibility-contract.md) covers specific default, optional, failure and file-export behaviors, not every CLI permutation.
- **Consumer boundary:** [Aula Robótica scope study](../implementation/aula-robotica-validator-consumer-boundary-20261115.md) inspected two files pinned to the external consumer and ran **synthetic fixture tests**. It neither tested the consumer application nor completed an Adoption Assessment.
- **Latest merged PR at the comparison target:** [#368](https://github.com/fran-eliot/github-framework/pull/368); its [CI run 43758239153](https://github.com/fran-eliot/github-framework/actions/runs/43758239153) completed successfully.

## 4. Evidence gaps before any release proposal

1. **Candidate identity:** a later change to `main` invalidates this diff as an exact release-candidate inventory. Recompare the published tag against the proposed **immutable candidate SHA**.
2. **Candidate-specific CI:** require successful Ubuntu, Windows and parity jobs for that exact candidate, not merely a successful earlier PR run.
3. **Contract review:** explicitly inspect all intended consumer-visible CLI/JSON behavior and breaking-change risks; current regression tests cover bounded contracts only.
4. **Release notes:** derive a concise, grouped description from verified changes. Do not claim a complete consumer adoption workflow or signed artifact attestation.
5. **Independent consumer evidence:** absent for a real application using the Framework Component Validator in its proper library scope. Documentary Only Film Assessment is not Application or Integration.
6. **Maintainer decision:** propose scope, candidate SHA and potential version separately. No tag, release, Sprint or milestone is implied or authorized by this report.

**Outcome:** a reproducible, source-grounded scope inventory is available for release planning, but **release readiness remains conditional**. The published version is still `v0.11.0`.

## 5. Repeatable audit procedure

1. Resolve the published `v0.11.0` tag to its fixed commit, without moving it.
2. Record the exact proposed `main` or candidate SHA.
3. Compare the two commits in GitHub; record ahead/behind counts, changed paths and file statuses.
4. Verify GitHub Actions results at the candidate SHA and download its platform catalogs while available.
5. Reconcile the diff with `CHANGELOG.md > Unreleased`, compatibility tests and governance records.
6. Only after an explicit maintainer decision, prepare candidate-specific release notes, a version and publication.

This study is **read-only**. It does not modify Only Film, Aula Robótica or any other consumer.
