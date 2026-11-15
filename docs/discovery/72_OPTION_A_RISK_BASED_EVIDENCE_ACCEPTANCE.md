# 72 — Option A: Risk-Based Evidence and Release-Claims Review

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Review date | 2026-11-15 |
| Stage | Discovery — targeted documentary acceptance, not a release authorization |
| Inspected Framework commit | [`abb97eac3ea139eecb0eee76c13b7f987d004e7c`](https://github.com/fran-eliot/github-framework/commit/abb97eac3ea139eecb0eee76c13b7f987d004e7c) (post-PR #319) |
| Immutable Only Film reference | [`28d75a50e0a178954dd46acc23300d9dd327843c`](https://github.com/fran-eliot/only_film/commit/28d75a50e0a178954dd46acc23300d9dd327843c) |
| Current Framework published version | `v0.10.0` |
| Release candidate, version and authorization | **Not selected or approved** |
| Consumer operation | **None** |

> This review is deliberately **risk-based, not a comprehensive audit of all fifty historical Only Film evidence documents**. It confirms the scope and limitations of selected high-consequence claims; it neither grants rights to source material nor certifies consumer runtime, security or compliance.

## 1. Inspected sources and evidence hierarchy

The following exact source contents were reopened for this review rather than relying only on earlier reports:

- Framework [canonical Assessment](../../framework/adoption/examples/only-film-assessment.md), [consolidated review matrix](../../framework/adoption/examples/only-film-consolidated-review-matrix.md), [completion record](../../framework/adoption/examples/only-film-assessment-completion-readiness.md), [security/testing reconciliation](../../framework/adoption/examples/only-film-security-testing-reconciliation.md), [verified Surefire/Sonar logs](../../framework/adoption/examples/only-film-verified-surefire-sonar-logs.md), [Quick Start/CI verification](../../framework/adoption/examples/only-film-pinned-quickstart-ci-verification.md) and [optional governance semantic review](../../framework/adoption/examples/only-film-optional-governance-semantic-review.md).
- Pinned Only Film [README](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/README.md), [pom.xml](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/pom.xml), [historical security hardening audit](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SECURITY_HARDENING_AUDIT.md), [demo-credential note](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/DEMO_CREDENTIALS_SECURITY.md), [Compose smoke workflow](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/.github/workflows/compose-smoke.yml) and [Sonar CI guide](https://github.com/fran-eliot/only_film/blob/28d75a50e0a178954dd46acc23300d9dd327843c/docs/SONARCLOUD_PR_CI.md).
- GitHub's complete **275-entry** pinned consumer tree (`truncated: false`) was inspected for root license filenames. [Run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407), matching the pinned SHA, had already been inspected directly for job outcomes and logs in the prior [canonical-source review](71_OPTION_A_ONLY_FILM_CANONICAL_SOURCE_VERIFICATION.md).

**Evidence levels are not interchangeable:** a pinned file exists; a historical document reports a finding; a job log confirms a specific execution; an approved documentary Adoption Decision records the maintainer's judgment. None, alone or combined, establishes full product certification or a license grant.

## 2. Four high-consequence release-claim boundaries

| Area | Source-backed finding | Unverified / inappropriate claim | Option A treatment |
| --- | --- | --- | --- |
| **Ownership, attribution and licensing** | The pinned README identifies academic collaborative origin, credits the source [`certidevs/g1_testing`](https://github.com/certidevs/g1_testing), distinguishes subsequent evolution, and explicitly says its license note grants no additional license. The pinned root tree contains **no root `LICENSE`, `LICENCE` or `COPYING` file**; `pom.xml` includes an empty `<licenses><license/></licenses>` entry. | That all collaborators granted redistribution rights, that repository visibility is a license, or that the Framework can relicense the Only Film source. No legal determination was performed. | Framework release may contain **source-referencing documentary Assessment records**, but must not claim rights, ownership certification, transfer of code, or a verified license. **Licensing/provenance acceptance remains open** if publication requires such a determination. |
| **Security review** | The pinned `docs/SECURITY_HARDENING_AUDIT.md` is dated **2026-10-10** and explicitly references an **earlier `main` baseline after PR #12 (`0a7e03a0`)**. The source itself says static inspection is not a pentest; the later Framework reconciliation reviews selected code/configuration against the pinned consumer SHA. The pinned demo-credential note distinguishes generated secrets from credentials already persisted or present in Git history. | Treating every historical audit finding as a current exploitable vulnerability, or saying the consumer passed a comprehensive security audit or has no remaining security issues. | Preserve the dated original findings and later bounded reconciliation; describe security checks as historical and scoped, without promoting them to present-day certification or defect claims. |
| **Runtime / deployment / tests** | The pinned README documents `docker compose up --build -d`, and the pinned `compose-smoke.yml` contains config, build, launch, HTTP and persistence checks. The observed pinned consumer [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) has three successful jobs; its `h2-regression` log reports **329 tests, 0 failures, 0 errors, 0 skipped**. | A clean checkout Compose stack was started successfully or failed; Selenium passed; every Maven test/configuration was exercised; or a production environment was validated. The existence of a workflow definition is not evidence of its execution at this reference. | State the known job/test subset and retain the missing independent Compose/Selenium/complete-suite evidence. |
| **Sonar / quality gate** | The inspected `h2-regression` log contains JaCoCo report generation/upload and Sonar scanner **`ANALYSIS SUCCESSFUL`**; the pinned Sonar guide says a green job may omit the scanner without `SONAR_TOKEN`. In this particular observed run, the scanner did execute. | That `Quality Gate: Passed`, coverage percentages, absence of vulnerabilities, or current dashboard status follows from successful scanner submission. | Explicitly separate **analysis accepted/submitted** from **server-side Quality Gate outcome**, which remains unverified in this evidence. |

## 3. Documentary status and permitted release narrative

The [canonical Only Film Assessment](../../framework/adoption/examples/only-film-assessment.md) is formally **`Complete` for documentary Assessment only**, with all **28/28** State/Applicability pairs and **28/28** Adoption Decisions approved on 2026-11-14 against `TPL-BACKEND 0.1.0` and the fixed consumer SHA.

**No approved decision is reopened or changed by this review.** In particular, `README-LICENSE = PRESERVE` preserves the **existing cautious non-grant wording**, not a grant of rights; deployment/testing/security `ADAPT` decisions concern bounded **future documentation**, not authorization to operate or modify the consumer.

A future release may accurately describe the Framework snapshot as containing **a completed, evidence-qualified documentary Assessment case study** and post-`v0.10.0` **Validator CI/CLI improvements**, provided its full repository contents and candidate verification are reviewed. It must not describe Only Film as migrated, production-ready, independently UX-tested, security-certified, licensed for redistribution, or verified end-to-end on Compose.

### Candidate release-note language — illustrative, not approved

> The repository includes an evidence-qualified documentary Adoption Assessment of Only Film at a pinned consumer commit, with 28 approved classifications and Adoption Decisions. Assessment completion does not imply consumer Application/Integration or runtime, security, licensing or quality-gate certification. The Framework Validator has accumulated improved cross-platform CI, JSON reports and scoped Component discovery/validation since v0.10.0; these changes remain Unreleased pending separate version and scope approval.

This paragraph is an **illustrative limitation statement**, not published notes, a version name or an authorization to release.

## 4. Targeted acceptance disposition

| Review aspect | Disposition |
| --- | --- |
| Canonical external link path existence | Previous [#71](71_OPTION_A_ONLY_FILM_CANONICAL_SOURCE_VERIFICATION.md): **21/21 present** at pinned consumer SHA |
| High-consequence evidence attribution | **Reviewed and bounded** in the four categories above |
| Documentary approval chronology | **No discrepancy requiring a further Assessment decision** in this subset |
| All fifty historical evidence files and external URLs | **Not exhaustively audited** |
| All source claims, licenses, provenance and legal permissions | **Not certified**; further assurance needed if required by publication policy |
| Candidate-SHA CI, version selection and complete repository release scope | **Not approved**; prior [Validator evidence](69_VALIDATOR_ACTIONS_NODE24_VERIFICATION.md) remains specific to its inspected commits |
| UX-02 independent usability | **`Prepared — Not Executed`**; no independent participants |

**Conclusion:** A bounded risk-based review supports the **possibility of documenting a complete-tree Option A release with explicit caveats**, but it does not close full publication acceptance or establish an automatic `GO` decision. No consumer change, code mutation, release candidate, Sprint, milestone, version, tag or GitHub Release is authorized or created by this record.
