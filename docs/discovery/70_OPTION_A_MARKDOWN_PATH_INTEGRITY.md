# 70 — Option A: Markdown Internal Path Integrity Review

| Field | Value |
| --- | --- |
| Project | GitHub Framework |
| Review date | 2026-11-15 |
| Phase | Discovery — bounded Markdown path-integrity verification |
| Published baseline | `v0.10.0` |
| **Exact inspected `main` commit** | [`6e444664d26fad028913a533bef6a477c4ee0011`](https://github.com/fran-eliot/github-framework/commit/6e444664d26fad028913a533bef6a477c4ee0011) |
| Comparison | [`v0.10.0...6e444664d26f`](https://github.com/fran-eliot/github-framework/compare/v0.10.0...6e444664d26fad028913a533bef6a477c4ee0011) |
| Release candidate | **Not selected or authorized** |
| UX-02 | `Prepared — Not Executed` — no independent participants |
| Consumer repositories | **Not modified** |

> This is a **path-existence inspection**, not an exhaustive publication review, a Markdown rendering audit, a live URL check, a copyright/license determination, a CI test run, or release authorization.

## 1. Exact reviewed population

The pinned GitHub comparison `v0.10.0...6e444664d26fad028913a533bef6a477c4ee0011` reported **649 commits ahead**, zero behind and **84 changed-file entries**. The complete changed-file population comprised **78 Markdown documents** and **6 Validator implementation/CI/test files**. These are whole-repository counts, not Validator-only commits.

The 78 Markdown files were grouped and inspected as follows:

| Reviewed Markdown population | Files | Markdown link occurrences | Relative targets resolved against the repository tree | Missing relative paths |
| --- | ---: | ---: | ---: | ---: |
| `framework/adoption/examples/only-film-*.md` | **50** | 1,208 | **563** | **0** |
| `docs/discovery/53_*.md` through `69_*.md` | **17** | 214 | **146** | **0** |
| Public root docs and the three changed governance records (inspected as one batch) | **8** | **75** | **74** | **0** |
| Other Adoption documents: main Guide, first Assessment example and cross-consumer replay | **3** | 65 | **50** | **0** |

The **root-plus-governance group was inspected together** and contained **75 link occurrences / 74 relative targets** in aggregate; separate per-group counts were not collected. Accordingly, no individual counts are asserted for the two subgroups in the table above. The **aggregate checked total is 78 documents, 1,562 Markdown link occurrences and 833 relative targets**.

## 2. Inspection method

The review used the GitHub connector to fetch the **recursive Git tree** for the pinned SHA. The tree listing was complete (`truncated: false`) and contained **278** tree entries, including files and directories.

For each of the **78 changed Markdown files**, the same pinned revision was fetched and scanned for conventional inline Markdown links of the form `[label](target)` (also accepting image-link prefixes). For links with relative targets:

1. Omit external protocols (`https:`, `http:`, `mailto:`, `tel:`, `data:`) and same-page fragment-only references.
2. Remove optional target fragments/queries and normalize relative `.` and `..` path segments against the referring document's directory.
3. Resolve the remaining repository-relative file or directory against the **same pinned commit tree**.
4. Report targets with no corresponding file or directory entry.

**Observed result: zero missing relative paths across 833 parsed, qualifying relative link occurrences.** This is a direct read-only inspection result, not a newly added executable checker or test fixture.

## 3. Explicit limits and false-negative boundaries

This inspection did **not**:

- Check the existence of named heading/HTML anchors after `#`, even for valid file paths;
- Request external HTTPS links, pinned third-party URLs, CI logs, screenshots or GitHub source targets to establish liveness;
- Fully parse every Markdown dialect, multiline reference-style definition, HTML anchor, escaped delimiter or embedded documentation snippet;
- Verify that each path points to the **right** content, or that historical assessment statements and external evidence are factually current;
- Validate all third-party permissions, academic source authorship, copyright/license grant, security posture, full Maven/Selenium/Compose execution or Sonar Quality Gates;
- Run tests on a new release candidate, or exercise external consumer Application/Integration.

The internal Markdown `[label](target)` scanner checks only the **link forms it recognizes**. Zero missing paths is not a guarantee that every possible link is correct or every document is release-ready.

## 4. Implication for Option A

**One bounded documentary release gate has stronger evidence:** the changed Markdown corpus contains no missing paths among its 833 conventional relative links, when resolved against the pinned Framework snapshot. This supplements the [file-level manifest](65_OPTION_A_FULL_SNAPSHOT_REVIEW.md), [content reconciliation](66_OPTION_A_SNAPSHOT_CONTENT_REVIEW.md), [real JSON/CLI evidence](68_OPTION_A_VALIDATOR_REPORT_CLI_EVIDENCE.md), and [Node.js 24 CI verification](69_VALIDATOR_ACTIONS_NODE24_VERIFICATION.md).

It does **not** settle the remaining acceptance of the entire documentary corpus, the external links, historical/source claims, license/provenance questions or future release notes. An immutable approved candidate will require its **own** final acceptance checks, especially if further PRs change the repository tree.

No code, workflow, consumer repository, Only Film Application/Integration, version, Sprint, milestone, release tag or GitHub Release is authorized or created by this record. The latest published version remains `v0.10.0`.
