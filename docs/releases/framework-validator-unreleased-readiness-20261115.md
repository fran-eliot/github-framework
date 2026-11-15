# Framework Validator — Unreleased Delivery Readiness Review

**Review date:** 2026-11-15  
**Evidence baseline:** `main` commit [`f8464b4a5307620d1db281945207aead154c6ca0`](https://github.com/fran-eliot/github-framework/commit/f8464b4a5307620d1db281945207aead154c6ca0) (merged PR #363).  
**Published baseline:** [`v0.11.0`](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0), fixed at `55680b388b0fd8256c95e15866e53d21cc9a5033`.  
**Decision state:** **Review prepared — release not authorized**. No version, release date, Sprint, milestone or tag is assigned.

This is a **snapshot of documented evidence**, not a release approval or a guarantee that the current branch will remain identical to the reviewed commit. Check GitHub again before any release proposal.

## 1. Why this review exists

The first Framework Validator CI and CLI delivery shipped in v0.11.0. Since that immutable tag, independent PRs have substantially expanded catalog discovery, filtered selection, metadata integrity and CI reproducibility. The purpose of this review is to separate **implemented and tested behavior** from **unverified claims** and provide observable criteria for a future maintainer decision.

The [Unreleased CHANGELOG](../../CHANGELOG.md) is the feature ledger; the [Project Status](../governance/12_PROJECT_STATUS.md) and [Backlog](../governance/14_BACKLOG.md) remain the governance records. This review does **not** revise either the released tag or the historical v0.11.0 release notes.

## 2. Delivery inventory — present on the reviewed `main`, not on the published tag

| Capability | Traceability | Contract / use |
| --- | --- | --- |
| Catalog discovery and export | [PRs #330–#349](https://github.com/fran-eliot/github-framework/pull/349), Unreleased CHANGELOG | Read-only catalog; atomic JSON export, composable filters, summary statistics, sorting and pagination. A page is not the whole library |
| Saved selection → targeted validation | [#351](https://github.com/fran-eliot/github-framework/pull/351), [#352](https://github.com/fran-eliot/github-framework/pull/352) | Import JSON from file or stdin; check Component path constraints; validate only selected paths |
| Metadata and content snapshot preflight | [#353](https://github.com/fran-eliot/github-framework/pull/353)–[#357](https://github.com/fran-eliot/github-framework/pull/357) | Optional detailed field checks and SHA-256 of raw metadata and complete regular-file trees, including symlink rejection |
| Integrity maintainability | [#359](https://github.com/fran-eliot/github-framework/pull/359), [#360](https://github.com/fran-eliot/github-framework/pull/360) | Dedicated integrity helpers, direct unit tests, and detection of some file changes during hashing |
| Practical example and evidence outputs | [#361](https://github.com/fran-eliot/github-framework/pull/361), [#362](https://github.com/fran-eliot/github-framework/pull/362) | End-to-end read-only workflow and per-platform JSON catalog/report artifacts retained seven days |
| Ubuntu/Windows reproducibility gate | [#363](https://github.com/fran-eliot/github-framework/pull/363) | Third CI job compares complete inventories and hashes; Git checkout byte conversion is explicitly disabled before checkout |

These increments were merged into `main` after publication of v0.11.0. **Do not describe them as released in v0.11.0**.

## 3. Evidence reviewed

| Check | Observed result | Boundary |
| --- | --- | --- |
| [PR #363 CI run 43748589509](https://github.com/fran-eliot/github-framework/actions/runs/43748589509) | **Success:** Ubuntu Component validation, Windows Component validation, and cross-platform catalog parity all completed successfully | The passing run is tied to a PR commit, not proof of a hypothetical future release commit |
| Earlier [PR #362 run 43746866040](https://github.com/fran-eliot/github-framework/actions/runs/43746866040) | **Success:** both platforms exported the verifiable catalog/report artifacts | Artifact retention is seven days; a downloaded catalog is not a signed attestation |
| [Practical catalog workflow](../implementation/validator-catalog-workflow.md) and [smoke test](../../scripts/framework_validator/smoke.py) | End-to-end selection, export, verified targeted validation and stale-digest rejection using a temporary copy of a tracked Component are exercised by CI | This is Framework-library validation, **not** an application or consumer integration test |
| [Unit tests](../../tests/framework_validator/) and [Workflow](../../.github/workflows/framework-validator.yml) | Automated regression suite runs on Python 3.11 for Ubuntu and Windows | A green suite establishes the tested cases only; it does not demonstrate exhaustive environment or dependency coverage |

**Important observation:** the first PR #363 parity attempt (run [43747497334](https://github.com/fran-eliot/github-framework/actions/runs/43747497334)) failed on byte-level catalog differences. The workflow was corrected by disabling Git automatic CRLF conversion **before checkout**, and run 43748589509 passed all three jobs. Preserve this regression story in future release assessment; do not silently count the first attempt as success.

## 4. Boundaries, uncertainties and release risks

1. **Snapshot trust:** digest verification compares files with an imported local catalog. It does not authenticate the catalog, prove the origin of bytes, or provide signed supply-chain provenance.
2. **Filesystem concurrency:** content hashing checks size and timestamps during file reads, but is not an atomic snapshot and cannot guarantee detection of every concurrent or same-size edit.
3. **Scope:** listing or validating selected Components is not a whole-library validation. Catalog checks do not decide semantic Existing Repository Adoption responsibilities.
4. **Platform behavior:** parity is proven for the reviewed runner/checkout configuration and tracked Component inventory. Toolchain or Git checkout-policy changes require renewed testing.
5. **Consumer evidence:** no documented proof here that an external consumer applies the catalog pipeline, deploys, passes its runtime tests or meets its Quality Gate.
6. **Documentation compatibility:** the growing set of optional CLI flags and JSON shapes merits a consolidated compatibility audit before release notes claim stable consumer-facing behavior.
7. **Independent usability:** the adoption study's UX-02 remains **Prepared — Not Executed**; this review must not attribute results to independent participants.

## 5. Readiness criteria for a subsequent proposal

| Criterion | Current documented state | Action before approval |
| --- | --- | --- |
| Bounded list of changes since released tag | **Documented** in Unreleased and section 2 | Confirm actual diff at the final candidate commit |
| Unit, integration and real-library smoke tests | **Green** at the cited PR run | Re-run at the exact proposed candidate SHA |
| Cross-platform catalog parity | **Green** at the cited PR run | Re-run and inspect third parity job for candidate SHA |
| Downloadable artifacts and reports | **Observed** for the prior workflow | Verify they correspond to the candidate commit and retention is suitable |
| CLI and JSON compatibility | **Partially evidenced** by regression tests and defaults | Review consumer-facing flags, JSON schema, errors and backward compatibility explicitly |
| Consumer usage / external interoperability | **Not demonstrated** in this review | Propose a narrowly scoped read-only consumer evaluation separately, if required |
| Release documentation and naming | **Not prepared or approved** | Draft candidate-specific notes and proposed version only after scope review |
| Maintainer authorization | **Not granted** | Obtain explicit approval of scope, candidate SHA, tag and publication |

**Overall outcome:** **evidence suitable for scoping discussion; not ready for an automatic release decision**. The testing evidence is encouraging, but a new published version is a separate governance action.

## 6. Suggested next action (proposal only)

Consolidate a small, reproducible CLI/JSON **compatibility contract** that compares existing defaults and common filtered/unfiltered workflows, then reassess the remaining gaps in section 5. This is preferable to adding further unrelated command-line flags. A read-only consumer exercise can be planned independently without modifying the consumer.

No Application or Integration work on Only Film is authorized. Its completed Assessment remains strictly documentary, pinned to `28d75a50e0a178954dd46acc23300d9dd327843c` against `TPL-BACKEND 0.1.0`; it does not certify Docker Compose, Maven, Selenium, security checks, licensing or deployment.

---

**Maintenance note:** when updating this review, add a new dated snapshot or explicitly update its evidence baseline. Do not retroactively imply that the results of a later PR applied to an earlier SHA.
