# 65 — Option A: Full-Repository Snapshot Release Scope Review

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Review date | 2026-11-14 |
| Study | **Option A — complete repository snapshot**, not a release authorization |
| Published baseline | `v0.10.0` — `3c4b21a26e4e85eeef705fefd48323ffd918e681` |
| Exact proposed **inspection** reference | [`10722c83b606a08467ca9b5e08c5c01863542bb4`](https://github.com/fran-eliot/github-framework/commit/10722c83b606a08467ca9b5e08c5c01863542bb4) |
| Reference status | Pinned historical `main` snapshot; **not designated as release candidate** |
| Scope disposition | Research only — **no release, tag, version, Sprint or milestone approved** |
| Consumer boundary | No consumer mutation, Only Film Application or Integration |

> This study records exactly which **paths** differ from the published tag in a fixed inspected Git snapshot. It is a **file-level inventory**, not a line-by-line semantic audit, release verification or sign-off to publish. Later commits to `main` are not included.

## 1. Exact source comparison

The GitHub comparison [`v0.10.0...10722c83b606`](https://github.com/fran-eliot/github-framework/compare/v0.10.0...10722c83b606a08467ca9b5e08c5c01863542bb4) returned **635 commits ahead**, **0 behind**, and **79 changed-file entries**, covering **all of GitHub Framework**, not 635 Validator changes. The base is `3c4b21a26e4e85eeef705fefd48323ffd918e681`; the inspected snapshot is `10722c83b606a08467ca9b5e08c5c01863542bb4`. A future release review must refresh these measurements on **the actual release candidate SHA**.

The file inventory below classifies **each of the 79 returned changed paths exactly once**. A Git tag placed on this snapshot publishes **the entire tracked repository tree at this commit**; it does not merely package the changed paths or the Validator enhancements.

| Area | Changed files | Meaning |
| --- | ---: | --- |
| Validator implementation, tests and CI | **6** | Functional and CI changes; the unchanged validation test suite remains in the snapshot. |
| Public root documentation | **5** | README/CLI explanations, release chronology, roadmap and contribution guidance all travel with the Git tree. |
| Discovery research | **12** | Discovery #53–#64, including unexecuted UX-02 and release-option research, remains historical or proposal evidence, not approved implementation. |
| Governance | **3** | Project status, backlog and continuity state; no new Sprint or release commitment. |
| Other Adoption examples and guide | **3** | Existing Repository Adoption guide changes and general worked examples. |
| Only Film Assessment and evidence | **50** | 50 documented source-bound artifacts; canonical Assessment Complete for pinned Only Film SHA, without consumer mutation or Application authorization. |
| **Total** | **79** | All changed paths from the pinned comparison |

## 2. Complete changed-file manifest

The status and additions/deletions below are **GitHub compare metadata**. They are not a manual source audit, licensing review or a promise that every change is ready to release.

### Validator implementation, tests and CI — 6 path(s)

| Path | Status | + | − |
| --- | --- | ---: | ---: |
| `.github/workflows/framework-validator.yml` | added | 56 | 0 |
| `scripts/framework_validator/__main__.py` | modified | 265 | 22 |
| `scripts/framework_validator/ci_summary.py` | added | 142 | 0 |
| `scripts/framework_validator/discovery.py` | modified | 6 | 3 |
| `tests/framework_validator/test_ci_summary.py` | added | 372 | 0 |
| `tests/framework_validator/test_cli.py` | modified | 917 | 2 |

### Public root documentation — 5 path(s)

| Path | Status | + | − |
| --- | --- | ---: | ---: |
| `CHANGELOG.md` | modified | 19 | 1 |
| `CONTRIBUTING.md` | modified | 8 | 0 |
| `README.md` | modified | 80 | 6 |
| `README_es.md` | modified | 80 | 6 |
| `ROADMAP.md` | modified | 21 | 2 |

### Discovery research — 12 path(s)

| Path | Status | + | − |
| --- | --- | ---: | ---: |
| `docs/discovery/53_FIRST_TIME_USER_EXPERIENCE_DISCOVERY.md` | added | 356 | 0 |
| `docs/discovery/54_FIRST_TIME_USABILITY_VALIDATION_PROTOCOL.md` | added | 188 | 0 |
| `docs/discovery/55_FRAMEWORK_FUNCTIONAL_MATURITY_DISCOVERY.md` | added | 200 | 0 |
| `docs/discovery/56_DOCUMENTATION_TEMPLATE_MATERIALIZATION_REALITY_CHECK.md` | added | 166 | 0 |
| `docs/discovery/57_DOCUMENTATION_LICENSE_CONSUMER_CASE_STUDY.md` | added | 146 | 0 |
| `docs/discovery/58_FUNCTIONAL_MATURITY_DISCOVERY_SYNTHESIS.md` | added | 150 | 0 |
| `docs/discovery/59_ADOPTION_END_TO_END_FEASIBILITY_CHECK.md` | added | 169 | 0 |
| `docs/discovery/60_ADOPTION_END_TO_END_EVIDENCE_RECONCILIATION.md` | added | 148 | 0 |
| `docs/discovery/61_NEXT_INCREMENT_EVIDENCE_PRIORITIZATION.md` | added | 60 | 0 |
| `docs/discovery/62_VALIDATOR_POST_RELEASE_EVIDENCE_REVIEW.md` | added | 81 | 0 |
| `docs/discovery/63_VALIDATOR_UNRELEASED_SCOPE_INVENTORY.md` | added | 103 | 0 |
| `docs/discovery/64_VALIDATOR_RELEASE_SCOPE_OPTIONS.md` | added | 77 | 0 |

### Governance — 3 path(s)

| Path | Status | + | − |
| --- | --- | ---: | ---: |
| `docs/governance/12_PROJECT_STATUS.md` | modified | 40 | 11 |
| `docs/governance/14_BACKLOG.md` | modified | 43 | 6 |
| `docs/governance/16_CONTINUITY_KIT.md` | modified | 36 | 2 |

### Other Adoption examples and guide — 3 path(s)

| Path | Status | + | − |
| --- | --- | ---: | ---: |
| `framework/adoption/README.md` | modified | 288 | 228 |
| `framework/adoption/examples/cross-consumer-repeatability-replay.md` | added | 124 | 0 |
| `framework/adoption/examples/first-assessment-example.md` | added | 99 | 0 |

### Only Film Assessment and evidence — 50 path(s)

| Path | Status | + | − |
| --- | --- | ---: | ---: |
| `framework/adoption/examples/only-film-adr-database-deployment-review-batch.md` | added | 106 | 0 |
| `framework/adoption/examples/only-film-api-diagrams-references-adoption-decision-review-batch-8.md` | added | 115 | 0 |
| `framework/adoption/examples/only-film-api-references-contract-review-batch.md` | added | 91 | 0 |
| `framework/adoption/examples/only-film-architecture-status-license-review-batch.md` | added | 109 | 0 |
| `framework/adoption/examples/only-film-assessment-completion-readiness.md` | added | 63 | 0 |
| `framework/adoption/examples/only-film-assessment-coverage.md` | added | 135 | 0 |
| `framework/adoption/examples/only-film-assessment-review-register.md` | added | 142 | 0 |
| `framework/adoption/examples/only-film-assessment.md` | added | 2388 | 0 |
| `framework/adoption/examples/only-film-changelog-evidence-review.md` | added | 130 | 0 |
| `framework/adoption/examples/only-film-changelog-governance-adoption-decision-review-batch-5.md` | added | 119 | 0 |
| `framework/adoption/examples/only-film-compose-evidence-gap.md` | added | 93 | 0 |
| `framework/adoption/examples/only-film-consolidated-review-matrix.md` | added | 311 | 0 |
| `framework/adoption/examples/only-film-demo-author-highlights-review-batch.md` | added | 99 | 0 |
| `framework/adoption/examples/only-film-negative-security-test-evidence.md` | added | 95 | 0 |
| `framework/adoption/examples/only-film-optional-contract-spotcheck.md` | added | 151 | 0 |
| `framework/adoption/examples/only-film-optional-final-semantic-review.md` | added | 170 | 0 |
| `framework/adoption/examples/only-film-optional-governance-semantic-review.md` | added | 129 | 0 |
| `framework/adoption/examples/only-film-optional-readme-governance.md` | added | 131 | 0 |
| `framework/adoption/examples/only-film-optional-showcase-attribution-adoption-decision-review-batch-6.md` | added | 165 | 0 |
| `framework/adoption/examples/only-film-optional-showcase-diagrams.md` | added | 129 | 0 |
| `framework/adoption/examples/only-film-optional-showcase-semantic-review.md` | added | 109 | 0 |
| `framework/adoption/examples/only-film-optional-technical-adoption-decision-review-batch-7.md` | added | 194 | 0 |
| `framework/adoption/examples/only-film-optional-technical-batch.md` | added | 178 | 0 |
| `framework/adoption/examples/only-film-pinned-quickstart-ci-verification.md` | added | 109 | 0 |
| `framework/adoption/examples/only-film-readme-content-review-batch-2.md` | added | 92 | 0 |
| `framework/adoption/examples/only-film-readme-presentation-review-batch-1.md` | added | 91 | 0 |
| `framework/adoption/examples/only-film-readme-status-structure-roadmap-review-batch.md` | added | 91 | 0 |
| `framework/adoption/examples/only-film-recommended-docs-adoption-decision-review-batch-4.md` | added | 109 | 0 |
| `framework/adoption/examples/only-film-recommended-docs-semantic-review.md` | added | 150 | 0 |
| `framework/adoption/examples/only-film-recommended-documentation-batch.md` | added | 143 | 0 |
| `framework/adoption/examples/only-film-recommended-readme-adoption-decision-review-batch-1.md` | added | 114 | 0 |
| `framework/adoption/examples/only-film-recommended-readme-batch.md` | added | 139 | 0 |
| `framework/adoption/examples/only-film-recommended-readme-semantic-review.md` | added | 159 | 0 |
| `framework/adoption/examples/only-film-required-final-semantic-review.md` | added | 185 | 0 |
| `framework/adoption/examples/only-film-required-identity-semantic-review.md` | added | 130 | 0 |
| `framework/adoption/examples/only-film-required-readme-adoption-decision-review-batch-1.md` | added | 118 | 0 |
| `framework/adoption/examples/only-film-required-readme-adoption-decision-review-batch-2.md` | added | 121 | 0 |
| `framework/adoption/examples/only-film-required-readme-batch-1.md` | added | 113 | 0 |
| `framework/adoption/examples/only-film-required-readme-batch-2.md` | added | 136 | 0 |
| `framework/adoption/examples/only-film-required-runtime-change-review-batch.md` | added | 100 | 0 |
| `framework/adoption/examples/only-film-required-semantic-review.md` | added | 141 | 0 |
| `framework/adoption/examples/only-film-roadmap-diagrams-model-adoption-decision-review-batch-9.md` | added | 118 | 0 |
| `framework/adoption/examples/only-film-security-semantic-review.md` | added | 104 | 0 |
| `framework/adoption/examples/only-film-security-testing-reconciliation.md` | added | 110 | 0 |
| `framework/adoption/examples/only-film-stack-startup-testing-adoption-decision-review-batch-10.md` | added | 152 | 0 |
| `framework/adoption/examples/only-film-status-architecture-adoption-decision-review-batch-11.md` | added | 132 | 0 |
| `framework/adoption/examples/only-film-testing-security-review-batch.md` | added | 100 | 0 |
| `framework/adoption/examples/only-film-testing-semantic-review.md` | added | 159 | 0 |
| `framework/adoption/examples/only-film-two-responsibilities.md` | added | 138 | 0 |
| `framework/adoption/examples/only-film-verified-surefire-sonar-logs.md` | added | 102 | 0 |
## 3. Consequences specific to Option A

**A. Everything in the pinned tree is included.** The tree includes the post-`v0.10.0` deterministic Framework Validator improvements, both public README versions, the Unreleased Changelog, governance and research records, and the **50 Only Film assessment/evidence documents**. The existence of these files in a tagged Framework snapshot would **not** edit the Only Film consumer, confirm its runtime or tests, certify security, grant licenses, or authorize Application/Integration. The Assessment is expressly **documentary `Complete`**.

**B. The release narrative and snapshot are different concepts.** If Validator CI/CLI improvements are the headline, any actual release notes must also accurately acknowledge the material non-Validator documentation and research carried in the same commit. Do not quietly omit or imply that Discovery/Assessment files are not in the release. The `Unreleased` Changelog heading must only be transformed after deciding an actual version, date, scope and publishing process; no such change is authorized here.

**C. No automatic `v1.0.0` promotion.** The prior [release-scope options](64_VALIDATOR_RELEASE_SCOPE_OPTIONS.md) preserve a distinction between a coherent maintenance increment and full Framework product maturity. An Option A snapshot is not an independent usability, consumer adoption or stable-product certification.

**D. Full-tree release obligations remain.** Inclusion of unrelated changes creates a review obligation, even when most are documentation. This inventory does **not** audit the full content of 50 historical evidence files, correctness of every hyperlink, provenance of all third-party material, or licensing permissions. A reviewer should check these matters at the level appropriate to a release.

## 4. Pre-release evidence currently available

- The 11 related [closed Validator Issues](63_VALIDATOR_UNRELEASED_SCOPE_INVENTORY.md) are grouped into CI/reporting and selective validation/catalog workflows. They were previously verified as closed; this is not a reexecution.
- Both public READMEs and the [Unreleased Changelog](../../CHANGELOG.md) document selected CLI/JSON/CI additions. Their complete consistency has not been independently signed off against the entire snapshot.
- For the **PR #310 head** (not the inspected merge commit), [Framework Validator workflow run 43647820652](https://github.com/fran-eliot/github-framework/actions/runs/43647820652) is reported `completed / success`; both `windows-latest` and `ubuntu-latest` Python 3.11 jobs reported success for **Run Validator test suite**, **Validate Framework Components** and **Upload Validator report**. This **does not validate the exact inspected merge SHA as a release candidate**.
- A historical [PR #307 workflow run](https://github.com/fran-eliot/github-framework/actions/runs/43646424380) had 161 tests passing in its Ubuntu log; it is not a newly executed test run for this snapshot.

## 5. Option A go/no-go gates — not yet satisfied

| Gate | Requirement before a release decision | Status at this review |
| --- | --- | --- |
| A1. Pin candidate | Choose an exact release candidate SHA and confirm no unexpected drift from this study | **Open** — inspection SHA is not an approved candidate |
| A2. Accept complete scope | Human review of all 79 changed paths and any material release implications beyond Validator code | **Open** — all paths classified, not individually accepted |
| A3. Contract consistency | CLI flags, relative paths, JSON fields, exit codes, filtered-mode caveats, artifacts and both README languages | **Open** — evidence is partial |
| A4. Candidate validation | Cross-platform tests and full-library self-validation at the **exact candidate SHA**; representative partial-selection checks and JSON/annotation results | **Open** — existing runs refer to previous PR heads |
| A5. Security/dependencies | Check workflow permissions, Python/PyYAML assumptions, unsafe file/output handling, artifact retention, and any release-relevant provenance | **Open** — no exhaustive audit |
| A6. Documentation/release notes | Reconcile CHANGELOG, ROADMAP, status, backlog, documentation dates, exact published contents and release notes | **Open** — no version selected |
| A7. Explicit approval | Maintainer selects Option A, accepts full snapshot scope and separately authorizes release planning/publishing | **Open** — authorized to **study** A only |

The result of this study is **not** `GO` for publication.

## 6. Bounded recommendation

**Option A is technically straightforward but carries a broad documentary payload.** Its repository-level size and concentration of Only Film/Discovery material are now explicit. Before advancing beyond research, the maintainer should decide whether publishing **all** those documents as part of the next Framework snapshot is acceptable, with their limitations clearly disclosed.

If acceptable, a **subsequent and separately authorized** release-candidate preparation may pin a commit, review the full tree and run acceptance gates. If not, reconsider Option B (a genuinely separate candidate tree) or C (keep Unreleased). **This document does not choose A, open release planning, change code, create a release tag or mutate a consumer.**

Independent UX-02 study remains `Prepared — Not Executed` because participants are unavailable. This GitHub inspection is not a substitute.
