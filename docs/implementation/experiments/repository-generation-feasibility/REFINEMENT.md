# Repository Generation Feasibility — Experiment II

Date: 2026-11-19  
Status: **PASS — bounded isolated replay; checkout confirmation pending**  
Baseline: [45c42ef2b6b872d833543f412fc9824c98cda654](https://github.com/fran-eliot/github-framework/commit/45c42ef2b6b872d833543f412fc9824c98cda654)  
Prior evidence: [Experiment I](README.md) and [EXP-01–EXP-08](../../../governance/19_STRATEGIC_PRIORITIZATION.md).

## Scope and method

Refine EXP-02 and EXP-04 without editing the original probe, canonical assets, Validator or Composition Preview. [refinement.py](refinement.py) imports the existing source readers and resolver and the original probe. The three selected identities, their versions and their metadata paths are fixed for this experiment. This is not a production materialization contract.

The local environment could not clone the repository (DNS unavailable). The isolated source fixture was reconstructed from GitHub reads at the baseline:
- Four exact Composition Preview module blobs: init `0f81193aed63b07bee498bc99c81ae07829410b3`, sources `723b7d9fea8f68f2b0c5a248577b6cea90846660`, registry `f8e70d4262d2a418b7ddc9c11662391f65ae87a6`, resolution `42b113c68cb56018ebeab6ad5b9fdaa6ea137842`.
- Exact Backend metadata blob `cc4620d9e82f2a410d40a8ff07c3e332e66757f2`, the three template blobs documented in Experiment I, and original probe blob `add420286160b6c3f170f11390cd3d649687bc19`.
- A reduced catalog containing the four registry sections with independently retrieved IDs and classifications (62 records); reduced YAML metadata files of all 21 physical Components with the five top-level fields used by the reader. These reductions are fixtures, not byte-exact copies of the complete catalog or full metadata files. No complete checkout or other repository files were exercised.
- The tested refinement blob is `bc4cde7f8b12b03bf750b393df19e8dc9f3fc2ef`; its committed identity was checked against the Git tree.

Actual local commands: `python -B /tmp/gf-exp/probe.py /tmp/gf-exp/checkout` and `python -B /tmp/gf-exp/refinement.py /tmp/gf-exp/checkout`. Linux, Python 3.13.5, PyYAML 6.0.3, Jinja2 3.1.6. In a pinned, disposable checkout containing both experimental files and byte-exact templates (no automatic newline conversion), these scripts can be replayed from the repository root:

```bash
python -B docs/implementation/experiments/repository-generation-feasibility/probe.py .
python -B docs/implementation/experiments/repository-generation-feasibility/refinement.py .
```

Use a disposable Python environment with PyYAML and Jinja2. Existing workflow and dependencies are unchanged; no Python 3.11, Windows or full-checkout execution has yet been observed for the refinement.

## EXP-02 — Composition preflight

The actual source-reader and pure resolution functions executed against the isolated fixture. Counts: 16 Resolved, 12 Conceptual, zero Unknown, Inconsistent or Ambiguous (28 references); 21 physical IDs, 62 registry records. All three selected Components resolved in declared relative order and matched the expected artifact paths and versions. The remaining 25 references retain their accounted-for status from Experiment I; not a full Backend materialization.

Four mutations of resolver input records simulated Conceptual, Unknown, Inconsistent and Ambiguous for a selected identity. Both rendering paths rejected every scenario with the expected outcome in the error message, before creating a destination. Mutations were in memory, not edits to the canonical catalog.

## EXP-04 — Rendering preflight

The experimental input policy rejects undeclared root/nested fields, missing or non-string required values, invalid optional link types, and links outside the explicit HTTP(S) scheme/netloc rule; the original length, alignment and badge count checks remain. It also rejects placeholder-shaped values in the checked fields. This is a bounded fixture policy, not an exhaustive validator of canonical metadata contracts, URL safety, Markdown content or referenced assets.

The static traversal audits both conditional branches and iteration bodies, even when inactive, with Component-specific names and a badge scope. The original parser and both rendering approaches remain in use. Five synthetic altered templates test unknown references in inactive conditional/empty iteration, nested unknown condition, out-of-scope badge reference and cross-Component reference.

| Negative scenarios | Per approach | Across both |
| --- | ---: | ---: |
| Selected resolution outcomes | 4 | 8 |
| Invalid input fixtures | 7 | 14 |
| Invalid template fixtures | 5 | 10 |
| Total | 16 | 32 |

All 32 rejected with expected diagnostic substring and no destination created. A valid optional fixture and original minimal fixture passed for each approach. This does not prove arbitrary grammar, context-sensitive escaping, URL/asset validation or all possible malformed inputs.

## Reproducibility and regression

Original probe rerun successfully. Both refined rendering approaches produced identical original output in two fresh temporary destinations per approach:

| Artifact | SHA-256 |
| --- | --- |
| README.md | `76fdbac91226ed9475846f937c04c8fa79bc921893d0c46056bed6ea40167f02` |
| CHANGELOG.md | `92a499cb2fdc0dd320ee1f10f88ab679beda944f4433381353b1da1996a91cdb` |

Template bytes were rechecked after execution. The original probe rechecked existing destination preservation, traversal and collisions in its isolated fixtures. No generalized write atomicity, filesystem audit or application certification is claimed.

## Assessment and decision boundary

EXP-02 and EXP-04 now have passing bounded experimental evidence for their previously identified gaps, in addition to the six passing criteria recorded in Experiment I. Do not silently promote this to unrestricted validation or production readiness. Full-checkout confirmation under the supported Python 3.11 environment remains a discrete verification gap.

Recommendation: use a single full-checkout replay to confirm the bounded feasibility result; then synthesize the findings and decide a generation delivery scope instead of growing this experimental adapter indefinitely. No engine selection, new public CLI, canonical contract change, production dependency, release, Sprint or milestone is authorized. The Composition Preview remains Complete — Unreleased; Only Film and UX-02 retain their existing limits.
