# Repository Generation Core — Implementation Plan

Date: 2026-11-19  
Status: **Proposed — scope and implementation approval pending**  
Baseline: `a61dcd8b8e08558d299ea6b7b6c8e37bdb8d928d`  
Scope: [Delivery Scope, GEN-01–GEN-16](repository-generation-core-delivery-scope.md)  
Evidence: [Feasibility Synthesis](experiments/repository-generation-feasibility/SYNTHESIS.md).

PR #401 is integrated, its remote branch removed; [main CI 44505079150](https://github.com/fran-eliot/github-framework/actions/runs/44505079150) succeeded. Integrating the proposed scope did not constitute formal approval. This plan is prepared for joint review, not an authorization to implement.

## 1. Proposed rendering decision

Inspect all eight required canonical artifacts, not just the three experimental selections.

| Artifact | Needed operation |
| --- | --- |
| README-HERO | HTML-escaped scalars, nested if/else and badge blocks; visual inputs disabled in this profile but syntax/references still audited |
| README-OVERVIEW | Literal Markdown substitution |
| README-FEATURES | Ordered each/this of explicit list |
| README-TECH-STACK | List converted to deterministic Markdown bullets before substitution |
| README-QUICK-START | Three literal Markdown substitutions |
| README-DOCUMENTATION | Ordered each/this of explicit list |
| README-FOOTER | Literal Markdown substitution |
| DOC-CHANGELOG | Explicit initialization projection of canonical headings, no historical release sample |

| Approach | Assessment |
| --- | --- |
| Native Handlebars / compatible engine | Attractive for existing block syntax and this; introduces a runtime or library and still needs strict static audit, list formatting and changelog policy. No native engine was executed in feasibility. |
| Jinja2 via translation | Both experimental replays passed; non-native syntax still needs a bounded parser/translation and escaping decisions. Adds production dependencies if adopted. |
| Bounded Python adapter | Supports the small inspected grammar and explicit profile policies, with no new dependency beyond existing PyYAML. Own parser/evaluator must be maintained and tested; no general Handlebars compatibility claim. |
| Normalize canonical assets to a new common syntax | Could simplify a future renderer, but changes canonical contracts and requires migration/version review; disproportionate now. |

**Recommend the bounded Python adapter**, independently implemented from the approved contracts, not promotion of experimental scripts. Support only simple scoped names, the current if/else and each blocks and this scalar items. Reject helpers, arbitrary expressions, unknown names in inactive blocks, foreign syntax, unbalanced blocks and unsupported per-Component constructs. Audit the disabled Hero branches against an explicit internal visual reference allowlist; never accept visual input from users. Escape Hero scalars for HTML, substitute trusted Markdown as literal data without recursive rendering. Use canonical source text for all fixed sections; no duplicate skeleton library. Do not globally collapse blank lines inside user Markdown. A canonical change outside the supported profile fails closed, and does not silently fall back to a generic renderer. No changes to canonical assets are proposed.

This is a candidate decision, based on inspection and bounded experiment evidence, not a benchmark or native-engine compatibility test. Approval of this plan selects this bounded approach only.

## 2. Candidate CLI contract

Run from a Framework checkout on Python 3.11, with existing PyYAML 6.0.2 available. Standalone module; no integration into existing Validator or Preview CLI.

```bash
python -B -m scripts.repository_generation --help
python -B -m scripts.repository_generation plan TPL-BACKEND --template-version 0.1.0 --input project.json --output-parent /path/to/existing/parent --name sample-backend
python -B -m scripts.repository_generation generate TPL-BACKEND --template-version 0.1.0 --input project.json --output-parent /path/to/existing/parent --name sample-backend
```

Paths above are illustrative; the parent must already exist outside the Framework source tree. Both modes perform the same full preflight and build the two intended artifacts in memory; plan performs no writes. Report Template ID/version, each reference in order with outcome and selection, selected metadata/artifact paths and versions, named dependency limitation, output paths and SHA-256 digests of intended bytes. No timestamps in artifacts. Generate repeats all checks and renders anew; no persisted plan or stale approval. On success generate reports actual output location and digests. Exit 0 for successful plan/generate (or help), 2 for argument/input/source/contract errors, 1 for destination/write/verification errors; actionable stderr, no success message on any failure. Human-readable report only; no machine-readable output stability promise yet.

## 3. Candidate project input contract

Strict UTF-8 JSON object, exact key names, reject duplicate keys at every depth, unknown fields, null for non-null fields, malformed input, nonstandard numeric constants and types not in contract. No inferred project content. Example:

```json
{
  "project_name": "Sample Backend",
  "tagline": "A documented sample backend project.",
  "overview": "This sample backend is a planned service used to demonstrate a reproducible repository documentation structure.",
  "features": ["Planned API endpoints"],
  "technologies": ["Backend: Python"],
  "prerequisites": "Python 3.11 is the intended runtime.",
  "installation": "Installation instructions will be supplied after implementation.",
  "execution": "The service is not implemented yet.",
  "documents": ["CHANGELOG.md — change history"],
  "footer": "This repository is a documentation seed."
}
```

| Field | Rule |
| --- | --- |
| project_name | Required single-line nonblank string, 2–60 characters |
| tagline | Required single-line nonblank string, 10–100 characters |
| overview | Required nonblank Markdown string, 80–1200 characters |
| features, technologies, documents | Required nonempty ordered arrays of nonblank single-line strings; no automatic link or technology invention |
| prerequisites, installation, execution, footer | Required nonblank Markdown strings; explicit honest planned/unavailable text allowed |
| short_description | Optional single-line string, default empty, maximum 240 characters |
| alignment | Optional left or center, default center |
| unreleased_changes | Optional object, default empty; keys Added, Changed, Deprecated, Removed, Fixed, Security; values nonempty ordered lists of nonblank single-line strings |

Normalize CRLF/CR to LF in Markdown values, preserve intentional interior whitespace, reject NUL/control characters except LF/tab where appropriate, reject whitespace-only required fields. Reject author content that would introduce extra document H1s under the supported structural checks; no general Markdown parser or sanitization guarantee. Treat supplied placeholder-like text as literal data; do not substitute it a second time. Audit unresolved template tokens structurally before interpolation rather than confusing literal user content with unresolved source syntax. Reject banner/badges as unsupported keys. Format technology strings as bullets; changelog uses canonical heading projection, category order above, no empty categories or invented versions. User-supplied commands are documentation only and are never run.

## 4. Proposed architecture and safety

- `scripts/repository_generation/`: separate orchestration, strict input/profile validation, canonical source/selection checks, bounded rendering/assembly, destination handling and CLI. Exact internal filenames may evolve within approved boundaries.
- Reuse the existing load_template, load_registry, discover_physical and resolve_composition implementation; do not parse textual preview output or change its outcomes. Require exactly the approved required identities and versions (seven README Components 1.0.0 and DOC-CHANGELOG 0.1.0); all composition conflicts block the operation. Confirm canonical selected metadata and artifact paths; missing/unreadable/linked sources fail. Inspect declared required dependencies, fail on unresolvable dependencies except the named VCL-HERO conceptual limitation in this text-only profile; report recommended conceptual visual dependencies separately. No claim of exhaustive transitive conformance.
- A Component-specific render policy maps the canonical fragments to README and changelog. Preflight validates every template branch and intended outputs in memory. Verify structural expectations and provenance, not runtime correctness or semantic adequacy of user content.
- The output parent must be an existing local directory outside the Framework checkout. Reject linked/reparse-point traversed ancestors, non-directory parents and unsafe names; use a portable lower-case ASCII child name (letters, digits, hyphens; start with letter, no trailing hyphen, 1–63 characters; reject Windows reserved device names). Reject existing child including dangling links. Do not create parents. Before writes, complete all preflight; create child exclusively, then fixed README.md and CHANGELOG.md with exclusive binary creation; verify written bytes. No overwrite/update. If a write fails after directory creation, report failure and the newly owned incomplete path for manual inspection/removal; deliberately do not auto-delete anything. Test partial-write failure and preservation of pre-existing data. No system-wide atomicity, race-proof sandbox or recovery transaction claim. No network, Git operations, or execution of supplied content.

## 5. Implementation units (candidate)

| Unit | Deliverable | Criteria principally addressed |
| --- | --- | --- |
| A — Input and composition contracts | Profile, strict JSON loader, source/selection/dependency preflight and focused positive/negative tests | GEN-02–GEN-05; GEN-14 regression |
| B — Rendering and assembly | Bounded syntax audit/evaluator, eight canonical materialization policies, in-memory two-file output, deterministic and adversarial fixture tests | GEN-06–GEN-08, GEN-10 |
| C — CLI and safe local output | Plan/generate/help, reports/exit codes, destination checks and injected I/O failure behavior, subprocess tests | GEN-01, GEN-09–GEN-12 |
| D — Integration and user verification | Real-checkout tests in current Ubuntu/Windows Python 3.11 matrix; reproducible walkthrough, measured maintainer-run first-use replay and evidence matrix | GEN-13–GEN-16; final regression across GEN-01–GEN-12 |

Keep each unit reviewable in one or more thematic branches/PRs. Integrate and verify each baseline before starting the next. Preserve experiment artifacts as historical evidence and do not make their Jinja2 dependencies production requirements. Unit D may extend the existing CI to run new production tests using the existing dependency; any broader workflow change is separately reviewed. No independent users or user study assumed. The acceptance matrix must distinguish test assertions, actual platform execution, and maintainer approval. Completion and publication are separate decisions.

## 6. Approval boundary

Request explicit approval of the Delivery Scope (GEN-01–GEN-16, including the named VCL-HERO limitation), this plan, bounded adapter and commencement of Unit A only. Subsequent units follow the agreed gated review model. No implementation is authorized by merging this proposal. No change to Only Film, UX-02, Template lifecycle, released version, tag, Sprint, milestone or committed Roadmap.
