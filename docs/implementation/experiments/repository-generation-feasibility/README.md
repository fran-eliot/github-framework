# Repository Generation Feasibility — Experiment I

Date: 2026-11-19  
Outcome: **PARTIAL — bounded materialization demonstrated; refine before delivery scope**  
Proposal: [EXP-01–EXP-08](../../../governance/19_STRATEGIC_PRIORITIZATION.md)  
Canonical source baseline: `f8ea292f44d1c28f46aa509b355a47ace669cff4`  
Experiment branch base: `0cc80579319561e176560871d56617b5d9d8456f` ([successful main CI](https://github.com/fran-eliot/github-framework/actions/runs/44496332571)).

## Question and method

Can three canonical Components produce a deterministic documentation seed without changing the Framework library or a real consumer? Compare a bounded direct evaluator and a translation to an existing rendering engine against a hand-authored expected output. Both evaluation paths deliberately share a small parser and the same input/assembly rules, so agreement is not independent verification of the grammar.

The [probe](probe.py) is an experimental artifact, not a production generator, public CLI, supported renderer or additional Framework dependency. The exact tested probe Git blob is `add420286160b6c3f170f11390cd3d649687bc19`. No full checkout or application runtime was executed in the local experiment.

## Sources and selection

TPL-BACKEND 0.1.0 (Experimental) was inspected at the canonical source baseline. The 28 declared references were compared with the registry classifications and the top-level IDs of all 21 physical Component metadata files in the non-truncated Git tree. This is a separate pinned inventory inspection, not a new execution of the Composition Preview CLI.

| Level | Selected (Implemented) | Unselected (Implemented) | Unselected (Conceptual) |
| --- | --- | --- | --- |
| Required | README-HERO, README-OVERVIEW, DOC-CHANGELOG | README-FEATURES, README-TECH-STACK, README-QUICK-START, README-DOCUMENTATION, README-FOOTER | None |
| Recommended | None | README-STATUS, README-ARCHITECTURE, README-TESTING, DOC-ARCHITECTURE, DOC-PROJECT-STATUS | README-REPOSITORY-STRUCTURE, DOC-TESTING |
| Optional | None | README-ROADMAP, README-AUTHOR, DOC-REFERENCES | README-CONTRIBUTING, README-DEMO, README-HIGHLIGHTS, README-LICENSE, DOC-ADR, DOC-API, DOC-DATABASE, DOC-DEPLOYMENT, DOC-SECURITY, DOC-DIAGRAMS |
| Total | 3 | 13 | 12 |

Each selected ID has one physical metadata match and an Implemented registry classification. The other 25 references are not rendered, including five required references; the seed must not be described as a complete TPL-BACKEND implementation.

| Selected Component | Version | Source artifact Git blob |
| --- | --- | --- |
| README-HERO | 1.0.0 | `ab9ce2d2dc9587be8641773c654673eac82dedbc` |
| README-OVERVIEW | 1.0.0 | `baace9693255174158a35d63b42beeae4a268ca3` |
| DOC-CHANGELOG | 0.1.0 | `390a025ff9b71ecce3855021841912f1438a6b62` |

The three template texts were reconstructed from GitHub-retrieved contents in an isolated source fixture at their canonical relative paths. The probe verified exact Git blob hashes before and after use. No complete repository filesystem audit or atomic read guarantee follows from that check.

## Execution

Actual environment: Linux, Python 3.13.5, Jinja2 3.1.6 (already installed in the experimental environment). No Windows or Python 3.11 execution was performed. The probe imports Jinja2 for comparison only; it is not added to production installation or CI.

Reproduce with the three byte-exact sources from the pinned revision, in a disposable directory or pinned checkout with no newline conversion. In an isolated environment with Jinja2 3.1.6, run from this experiment directory:

```bash
python -B probe.py /path/to/pinned-source-root
```

The actual local command was `python -B /tmp/gf-exp/experiment.py /tmp/gf-exp/checkout` with the same probe bytes. It runs without optimization, uses temporary destinations that are removed at exit, and prints the evidence JSON. The fixture (including the optional banner/badge branch variants) is embedded in the probe. No dependency download, network request or Git operation is performed by the probe.

Both approaches render the Hero and Overview fragments in declared relative order, strip the initial Hero authoring comment, normalize runs of blank lines, and assemble one README. The changelog is an explicit editorial projection of the canonical title and Unreleased heading with synthetic Added content; the historical-release example and authoring placeholders are omitted rather than treated as real version data. This is not a general changelog renderer.

During initial execution the shared parser incorrectly rejected the existing double-brace block syntax as foreign syntax. The check was narrowed and the subsequent run passed all scripted assertions. The recorded probe is the corrected version.

## Observed results

The direct and Jinja2 approaches matched the manually authored minimal reference. Each generated the two files in two fresh temporary destinations. All four destination pairs returned the same SHA-256 values:

| Artifact | SHA-256 |
| --- | --- |
| README.md | `76fdbac91226ed9475846f937c04c8fa79bc921893d0c46056bed6ea40167f02` |
| CHANGELOG.md | `92a499cb2fdc0dd320ee1f10f88ab679beda944f4433381353b1da1996a91cdb` |

README contains one H1, a tagline and an Overview. CHANGELOG contains only Unreleased and a synthetic Added entry. No release or running service is asserted. The optional fixture exercised nested conditions, linked/unlinked banners, two badges, and HTML ampersand escaping; it was a rendering comparison, not validation of linked assets.

Both approaches rejected each missing required scalar input, selected invalid lengths, invalid alignment, missing banner alt, seven badges, placeholder-shaped project name, unsupported block syntax (including in an inactive branch), unclosed block and an evaluated unknown variable. Existing destination directories and files were rejected with original bytes unchanged. Traversal in destination and artifact names, and duplicate output names were rejected without creating new destinations. This was an isolated fixed-name exercise, not arbitrary filesystem safety verification; no linked-directory, race, partial-write or permission fault injection was performed.

Additional interactive checks after the successful probe identified two real limitations in both approaches: an unknown identifier inside an inactive conditional produced an empty result, and a non-string optional banner link (123) was rendered as an href. These are negative findings, not passing input-contract tests.

## Rendering comparison

| Approach | Demonstrated | Limit |
| --- | --- | --- |
| Bounded direct evaluation | Selected variables, conditions and badge iteration; same output as reference | Own evaluation/escaping logic, restricted grammar and maintenance burden |
| Jinja2 translation | Selected grammar translated and evaluated with StrictUndefined; same output | Still requires the shared parser/adapter; adds Jinja2 and its dependency; not native Handlebars compatibility |
| Manual reference | Independent expected minimal artifact bytes | Not a repeatable general generation mechanism |

Both renderers share incomplete input checks and a syntax parser, so their agreement cannot establish complete contract coverage. No native Handlebars implementation, Cookiecutter, Copier, performance benchmark or security audit was executed. Do not choose a production engine from this comparison alone.

## Acceptance gates

| Gate | Status | Evidence / remaining work |
| --- | --- | --- |
| EXP-01 | PASS | Pinned sources, versions, exact probe blob, fixture, environment and command recorded |
| EXP-02 | PARTIAL | Full inventory reconciled and selected IDs unambiguous; actual resolver integration and explicit selected-conflict failure not exercised |
| EXP-03 | PASS | Ordered README fragments and separate Unreleased-only changelog match manual reference; one H1 |
| EXP-04 | PARTIAL | Required scalar and syntax rejection demonstrated; inactive unknown identifier and non-string optional link remain accepted |
| EXP-05 | PASS | Two fresh destinations per approach, identical hashes on Linux/Python 3.13.5 only |
| EXP-06 | PASS (bounded) | Existing destination preservation, traversal and collision rejection in fixed-name temporary fixtures; no general safety/atomicity claim |
| EXP-07 | PASS (bounded) | Two evaluation approaches and manual reference compared, including initial failure and limitations |
| EXP-08 | PASS | Per-gate evidence and a refinement recommendation recorded |

Overall result: **PARTIAL**, not full acceptance of the proposed experiment and not authorization to deliver Repository Generation.

## Recommendation

Refine rather than proceed directly to production. Close the selected-reference preflight gap using the existing resolution model and define explicit input/materialization rules that reject inactive unknown references and invalid optional values before writing. Treat fragment assembly and standalone document initialization as distinct policies. Evaluate the benefit of a native renderer or canonical contract normalization after the preflight work, without silently changing Component metadata or templates.

The next decision should be based on a small executable refinement and evidence, including Python 3.11 compatibility where practical. No new version, tag, Sprint, milestone, public CLI or production dependency is proposed or authorized. Only Film remains unchanged; UX-02 remains Prepared — Not Executed.
