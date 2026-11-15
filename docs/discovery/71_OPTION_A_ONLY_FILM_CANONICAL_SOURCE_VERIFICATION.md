# 71 — Option A: Only Film Canonical Assessment External-Source Verification

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Review date | 2026-11-15 |
| Phase | Discovery — pinned external-source references |
| Framework inspection SHA | [`3fb2716bd21c7627999088231a00f96a255b8061`](https://github.com/fran-eliot/github-framework/commit/3fb2716bd21c7627999088231a00f96a255b8061) (after PR #318) |
| Canonical Assessment | [`framework/adoption/examples/only-film-assessment.md`](../../framework/adoption/examples/only-film-assessment.md) |
| Immutable Only Film consumer SHA | [`28d75a50e0a178954dd46acc23300d9dd327843c`](https://github.com/fran-eliot/only_film/commit/28d75a50e0a178954dd46acc23300d9dd327843c) |
| Assessment status | **`Complete` — documentary only**, 28/28 classifications and 28/28 approved Adoption Decisions |
| Release / candidate | **None selected or authorized** |

> Link accessibility and path identity are **not** evidence of operational correctness, semantic conformity, permission to redistribute code, complete third-party provenance, security, or full consumer validation. Only Film is not changed by this research.

## 1. Scope and source extraction

The canonical [Only Film Assessment](../../framework/adoption/examples/only-film-assessment.md) was fetched directly from Framework at the fixed inspection commit, rather than inferred from a title or prior summary. Its conventional inline Markdown external links produced:

| Measure | Observed |
| --- | ---: |
| External Markdown link occurrences in the canonical Assessment | **88** |
| Distinct external URLs | **27** |
| Distinct pinned consumer `blob`/`tree` paths | **21** |
| Pinned consumer `blob`/`tree` paths present in exact SHA tree | **21/21** |
| Missing exact-SHA paths in that set | **0** |
| Other URLs | **6** (repository, action run, external origin repo, commit listing, root tree, job deep link) |

This is an **exact-SHA source-path inventory of the canonical Assessment**, not a scan of every link in all fifty supporting Only Film review documents. The 27 URLs are deduplicated: repeated references within the Assessment are not counted as independently verified source files.

## 2. Direct verification of the 21 pinned content targets

The GitHub Git-tree endpoint for [Only Film `28d75a50e0a178954dd46acc23300d9dd327843c`](https://github.com/fran-eliot/only_film/tree/28d75a50e0a178954dd46acc23300d9dd327843c) returned a complete recursive tree with **275** entries and `truncated: false`. Each of the canonical Assessment's **21** distinct pinned `blob`/`tree` URLs was parsed into its immutable SHA and consumer-relative path and checked for an exact path in that tree.

All **21/21** target paths were present. They cover README and build/runtime configuration, workflows, technical guides/audits, screenshots directory and selected Java controller directories. Selected important sources were additionally reopened as full GitHub file content, including `README.md`, `pom.xml` and `compose.yaml`.

**Scope limits:** Path presence establishes that the cited material exists **at that commit**. It does not prove that every claim citing a path is correct, that every intra-file anchor is valid, that a particular workflow command was executed or that an external license grants reuse.

## 3. Other canonical external URLs

The six other distinct URLs were treated by URL type, not incorrectly compared to the Git file tree:

| Reference type | Result |
| --- | --- |
| Only Film repository root | GitHub repository resource fetched successfully |
| [GitHub Actions run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) | GitHub run resource fetched; `head_sha` matches the exact `28d75a50e0a178954dd46acc23300d9dd327843c`; `completed / success` |
| [Source/origin repository `certidevs/g1_testing`](https://github.com/certidevs/g1_testing) | GitHub repository resource fetched successfully — existence does **not** determine licensing or ownership rights |
| Only Film historical commits URL at pinned SHA | GitHub resource fetched successfully |
| Only Film root `tree` URL at pinned SHA | GitHub resource fetched successfully |
| Actions job deep link `.../job/118164215980` | The generic GitHub resource fetch did **not** support this URL form. Separately, the linked job ID **118164215980** was returned by the supported GitHub workflow-jobs lookup with name `h2-regression` and conclusion `success`; log text was available through GitHub's job-log endpoint. Do **not** report the unsupported page fetch as a broken URL. |

Thus every distinct canonical link was **accounted for**, but the job deep-link itself was not opened through the generic page fetch and not all links received the same kind of verification. There is no claim of comprehensive general-web liveness monitoring.

## 4. Consumer CI evidence, properly bounded

For the exact pinned Only Film commit, [run 39283862407](https://github.com/fran-eliot/only_film/actions/runs/39283862407) reports three successful jobs:

- `PostgreSQL JPA and concurrent checkout`;
- `postgres-schema`;
- `h2-regression` (job ID `118164215980`).

The inspected `h2-regression` job log records **`Tests run: 329, Failures: 0, Errors: 0, Skipped: 0`** and `BUILD SUCCESS`. It shows a JaCoCo report task and upload in that historical run, and Sonar scanner `ANALYSIS SUCCESSFUL`. These statements describe **that bounded workflow run**, not the outcome of an independently rerun clean-checkout Maven suite, Selenium, Docker Compose, a completed Sonar Quality Gate, current vulnerability status, penetration testing or production readiness.

The [canonical Assessment](../../framework/adoption/examples/only-film-assessment.md) and [consolidated matrix](../../framework/adoption/examples/only-film-consolidated-review-matrix.md) retain these evidence limitations; completing the documentary Assessment did not authorize consumer Application/Integration or any changes to Only Film.

## 5. Option A release implication and open evidence

**Result:** the highest-priority canonical Only Film source pointers are retrievable and the **21 exact-SHA paths exist**; the specific historical CI run matches the pinned consumer SHA and its selected test count is independently visible in the job log. No broken pinned consumer path was found **in the canonical Assessment link subset**.

This reduces a **bounded source-traceability risk**, not the broader publication acceptance obligation. The following remain outside this review: links in the other 49 Only Film supporting files, third-party URLs outside the inspected source, full heading-anchor checks, factual audit of each historical claim, copyright/license permission verification, independent usability sessions, consumer runtime verification, and approval of the entire Option A snapshot.

**No version, release-candidate commit, Sprint, milestone, tag, GitHub Release or consumer mutation is authorized by this Discovery.** `v0.10.0` remains the latest published Framework release, and UX-02 remains `Prepared — Not Executed`.
