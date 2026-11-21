# Repository Generation Guided Experience — UX-C Verification

Date: 2026-11-21  
Status: **UX-C implemented and integrated; automated verification passed — formal technical closure pending maintainer approval**  
Integrated main: `307febd65e28175e7745ffe094c28d9489bae579`  
Main CI: [44934603680](https://github.com/fran-eliot/github-framework/actions/runs/44934603680) — **success**, Ubuntu, Windows, Component catalog parity and generated-document byte parity.  
Implementation: [PR #430](https://github.com/fran-eliot/github-framework/pull/430) (merged); PR checks [44933749360](https://github.com/fran-eliot/github-framework/actions/runs/44933749360) — success.  
Scope: [Guided Experience Delivery Scope](repository-generation-core-guided-experience-delivery-scope.md); [Implementation Plan](repository-generation-core-guided-experience-implementation-plan.md).

## Authorization and intent

The maintainer formally accepted UX-B's technical closure and authorized UX-C only, retaining UX-D as pending and v0.13.0 as a candidate without publication. UX-C addresses the maintainer-observed excess blank lines in generated README Hero, Features and Documentation. No additional Templates, consumer mutations, release, tag, Sprint or milestone have been authorized.

## Implementation evidence

- `scripts/repository_generation/rendering.py` implements exact-shape handling for the two known, canonical list loops in **README-FEATURES** and **README-DOCUMENTATION**. It removes template-owned blank lines around each list iteration without normalizing or trimming the author-supplied list entries.
- For **README-HERO**, the renderer collapses runs of blank lines left by disabled visual/optional blocks. Current Hero fields are single-line and HTML-escaped; author-supplied multiline Markdown is not processed by this compacting routine.
- Unknown or changed canonical list-loop formatting fails explicitly rather than undergoing an unsafe general-purpose Markdown reformatter.
- `tests/repository_generation/test_rendering.py` adds cases for compact order-preserving list output, canonical source drift, Hero with/without optional short description, literal syntax and preservation of intentional author whitespace.
- `tests/repository_generation/test_assembly.py` adds an assembled README regression covering exact section list spacing, preservation of a triple-LF author footer, fixed document identities, and LF output.
- Canonical `framework/components/**/template.md` files were not changed. Original `plan`, `generate`, `--summary` and `guide` UX remain in scope and are covered by the established regression workflow.

## Integrated CI and acceptance mapping

| Gate | Evidence | Disposition |
| --- | --- | --- |
| UXG-01 and UXG-06 | Existing programmatic CLI, guided integration and canonical resolver/writer tests under the successful workflow | Regression PASS within tested coverage |
| UXG-04 | Added tests preserve author markdown including literal template-like markers and intentional multi-line blank spacing | PASS for tested inputs |
| UXG-09 | Exact merged main workflow 44934603680: both platform validation jobs successful; both parity jobs successful | PASS for integrated matrix |
| UXG-10 | Known renderer-owned blank line patterns corrected; drift rejection and assembled README assertions added | **Technical PASS** for the bounded cleanup |
| UXG-11 | No new maintainer first-use walkthrough yet | Pending UX-D |
| UXG-12 / GEN-15 / GEN-16 | Complete acceptance reconciliation and user evaluation outstanding | Pending UX-D and formal decision |

The CI parity job verifies generated-document bytes between the tested Windows/Ubuntu environments. The new output intentionally differs from the earlier artifact hashes; **historical hashes are not new expected fixtures**. This verification does not claim an independently recorded new hash value or broader CommonMark normalization.

## Remaining work and limits

1. Maintainer reviews and merges this evidence PR; verify exact `main` CI afterwards.
2. Obtain explicit maintainer acceptance of UX-C technical closure and **separate authorization to start UX-D**.
3. UX-D requires a fresh, real maintainer-guided walkthrough, including understanding, cancellation/error recovery, generated-document readability and only actually observed friction/timing.
4. Do not mark GEN-15 or GEN-16 complete on automated evidence alone. The next release candidate **v0.13.0** remains conditional: no tag or GitHub Release without a separately approved final scope and exact commit.

Only Film and UX-02 stay unchanged.
