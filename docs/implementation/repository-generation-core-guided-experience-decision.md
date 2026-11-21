# Repository Generation Core — Guided Experience Decision Proposal

Date: 2026-11-21  
Status: **Proposed — maintainer decision required; no implementation authorized**  
Baseline: `aca19ce4f959bb7f84e5317394a2c4e00b29bf4f`  
Related evidence: [First-Use Walkthrough](repository-generation-core-first-use.md), [Usability Improvement Gate](repository-generation-core-usability-improvement-gate.md), [Generation Guide](../../framework/generation/README.md).  
Release state: v0.12.0 published; Repository Generation Core remains unreleased.

## 1. Problem and target outcome

The first maintainer-run walkthrough verified a safe, deterministic two-document output and collision refusal, but the maintainer explicitly found the workflow **not easy to use** and requested better information, help and interpretation. The current journey requires authoring a 10-required-field JSON document, supplying multiple CLI flags and interpreting 28 registry references and direct dependency classifications before understanding a two-file result. Excess blank lines in generated Markdown were also observed. These are meaningful first-use findings, not independent user statistics.

**Desired user outcome:** A new developer can state what the tool will create, enter their project facts with clear inline guidance, understand a short plan, knowingly confirm generation and inspect the result without learning the internal Component catalog. Keep deep provenance and the strict JSON/CLI path for advanced users and automation.

The desired experience is narrower than a platform, IDE integration, web portal, full scaffolding engine or full Template instance. Do not expand supported Templates or select unresolved assets as part of this improvement.

## 2. Alternatives

| Dimension | A — clearer existing CLI | B — opt-in terminal-guided flow | C — browser/web experience |
| --- | --- | --- | --- |
| First-time project fact entry | Still requires editing full JSON | Prompts with field descriptions, defaults and examples; could optionally import existing JSON | Forms with contextual validation |
| Plan interpretation | Add short human summary; detail optional | Same summary explained during a guided plan/confirm flow | Rich visual preview |
| User effort and accessibility | Low implementation cost; moderate user friction | Moderate implementation cost; fewer command/JSON prerequisites, though terminal familiarity remains | Potentially easiest for nonterminal users; browser/UI/distribution needed |
| Maintenance | Small | Additional interaction and state/error tests, Python-only | Larger UI, dependencies, build/deployment and security surface |
| Existing safety/architecture | Easy to preserve | Preserve by reusing current strict input, composition, rendering and exclusive writer; no parallel generation implementation | Must coordinate UI and backend; larger boundary |
| Evidence today | Existing CLI verified, comprehension difficult | Hypothesis only; no guided prototype tested | Hypothesis only; no web prototype tested |
| Recommendation | Useful foundation and immediate improvement | **Recommended candidate** for a bounded opt-in feasibility and implementation plan | Defer; revisit after evidence of adoption demand |

No numeric prioritization score is claimed; no user preference study or comparative performance benchmark has been conducted.

## 3. Recommended staged approach (subject to approval)

**Stage 0 — report clarity and document polish:** Preserve the full technical report while offering a short user-oriented view showing: profile and text-only limitation; what will be created and where; source conflicts and blocking errors; eight selected and twenty unselected references; specific VCL-HERO exception; SHA-256; and next action. Separate a bounded renderer whitespace cleanup with dedicated regression tests; do not normalize arbitrary author Markdown or silently edit canonical Component assets. Stage 0 itself requires review of any CLI interface changes.

**Stage 1 — Bounded terminal guided experience:** Add a separately invoked, explicitly interactive entry point (illustrative command `guide`, not a committed CLI contract). Do not activate it automatically for existing `plan`/`generate` calls. Guide users through:
1. Explaining the text-only, two-document output and what is excluded.
2. Choosing the supported TPL-BACKEND 0.1.0 profile without pretending other Templates are supported.
3. Entering the ten required project fields, with multiline Markdown support, honest examples, and explicitly chosen optional values. Do not invent facts or infer technologies.
4. Reviewing/editing entries before any output operation.
5. Choosing an existing external parent and a new portable child directory.
6. Running the **same** strict validation, canonical composition resolution and in-memory assembly as the current CLI.
7. Showing a human-readable, read-only plan and a clear decision to proceed or cancel; cancellation writes nothing.
8. Invoking the **same** exclusive destination writer only on explicit confirmation; show file paths and safe next steps.

The guided flow should make success, cancellation and failure distinguishable without weakening current `0/1/2` exit semantics for the existing commands. What (if anything) is saved or exported as a project JSON must be an explicit, separate design decision. No data collection, network operations or automatic writes are assumed.

**Stage 2 — empirical first-use replay:** Repeat a maintainer-run walkthrough using genuinely new project facts and a fresh destination. Assess the ability to complete the flow without assistant-provided commands; explanation of output and unresolved dependencies; clarity and recoverability of errors; number of confusing steps; and elapsed time only if observed. Do not claim broad UX validation from one maintainer session.

## 4. Guardrails and acceptance candidates

A separate Delivery Scope and Implementation Plan must be approved before writing the guided CLI. In particular:

| ID | Proposed observable gate |
| --- | --- |
| UXG-01 | Existing `plan`/`generate` contracts, output safety, and automated use remain supported |
| UXG-02 | Prompting is explicit and opt-in; unattended invocation does not hang or create output |
| UXG-03 | All project facts are user-supplied or explicitly accepted defaults; required fields retain strict validation |
| UXG-04 | Multiline author text survives without accidental splitting, template evaluation, or unrelated whitespace normalization |
| UXG-05 | Before confirmation, no destination files are created; cancellation is clean |
| UXG-06 | Preflight and generation reuse the current canonical resolver/renderer and safe writer; failures do not weaken guards |
| UXG-07 | Human-oriented plan accurately distinguishes selected/unselected, resolved/conceptual, intended/generated and named VCL-HERO gap |
| UXG-08 | Guidance covers destination collision and partial write recovery without automatic deletion |
| UXG-09 | Positive/negative cases run on Ubuntu and Windows, including simulated stdin/EOF/cancellation and real-checkout public example |
| UXG-10 | Maintainer first-use retest records actual usability findings; no inferred independent validation |

These are **candidates**, not approved replacement criteria. GEN-01–GEN-16 and their existing evidence remain authoritative for the bounded generator. Any release decision remains separate.

## 5. Open design choices

- Whether Stage 0 should introduce an explicit `--summary`/`--details` presentation option or retain default verbose output with a clearly labeled summary at the top. Prefer a backwards-compatible report mode, not a silent change to expected output.
- How to enter multiline fields, how to handle correction/review, and how to present default and absent optional fields without fabricated content.
- Whether input is ephemeral or an explicitly saved JSON draft, and how to prevent accidental writes to existing files.
- Whether a separate `guide` subcommand or a distinct module is the clearest supported entry point.
- How to characterize cancellation exit semantics, noninteractive execution, and narrow terminal compatibility.
- Whether excessive template-derived blank lines warrant a bounded post-render normalization and how to keep legitimate author-authored blank lines intact.

## 6. Decision request

**Recommended decision:** Prioritize a bounded guided terminal experience (B), supported by human-first CLI reporting (A), and defer web/UI (C). If accepted, authorize *only* the next Delivery Scope/Implementation Plan and an explicit interface/safety review, **not immediate implementation**. Maintain the original strict programmatic CLI as an advanced and automation pathway.

The maintainers must explicitly approve the selected option and any later implementation scope before modifying the CLI. Until successful retesting, maintain GEN-15 as pending and the Repository Generation Core as Complete Implementation — Usability Acceptance Pending, not delivery-accepted or released. No new release, tag, Sprint, milestone, Only Film change or UX-02 execution is authorized.
