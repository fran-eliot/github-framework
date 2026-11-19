# 18 — Strategic Capabilities and Competitive Landscape

Date: 2026-11-19  
Status: Proposed — discovery  
Baseline: `200b3dcd86dc2d0ed8ab06f50129e8acda8989c7`  
Related: [Global Strategic Review](17_GLOBAL_STRATEGIC_REVIEW.md)

## Product vision hypothesis

A technology-agnostic repository engineering framework enabling developers and organizations to create, adopt, validate and evolve professional repositories using reusable components, standards and progressive automation.

## Capability map

| Area | Available | Gap |
| --- | --- | --- |
| Foundation | Standards, design system, component contracts, governance | Avoid duplication |
| Create | Component Library, three Templates; Composition Preview in main only | Executable materialization and customization |
| Adopt | Assessment, Application, Integration and Assisted Analysis documented cores | Executable evidence collection and complete consumer journeys |
| Validate | Component Validator, catalog, integrity, CI | Consumer-specific checks with explicit scope |
| Maintain | Manual governance and Integration guidance | Repeatable drift and update workflows |
| Distribute | Execution from source checkout | Installation and onboarding |

Preview resolution does not prove materializability. Validator does not certify consumers. Only Film remains a documentary Assessment; UX-02 remains Prepared — Not Executed.

## User hypotheses and journeys

| Persona hypothesis | Desired outcome | Journey |
| --- | --- | --- |
| Independent developer | Start a professional repository without repetitive setup | CREATE |
| Open source maintainer | Improve an existing repository while preserving choices | ADOPT / MAINTAIN |
| Tech lead | Establish consistent repository conventions | CREATE / ADOPT |
| Student | Learn reproducible engineering practices | CREATE |
| Platform engineer | Reuse and enforce organization policies | MAINTAIN (later) |

These are hypotheses, not participant findings or market demand measurements.

- CREATE: select, customize, preview, materialize, verify. Selection and customization have documentary guidance; preview is executable in main; materialization is missing.
- ADOPT: collect Evidence, assess, review decisions, optionally apply and integrate. Published documentary cores support these stages; no automated semantic decision engine.
- MAINTAIN: detect drift, evaluate updates, review proposals and verify changes. Continuous automation is deferred.

## Competitive landscape

Desk research of official source documentation, accessed 2026-11-19; no installation, benchmark or exhaustive market survey.

| Tool | Documented capability | Implication |
| --- | --- | --- |
| [GitHub template repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository) | Reuse directory structure and files | Native baseline for simple creation; avoid duplicating hosting |
| [Cookiecutter](https://cookiecutter.readthedocs.io/) | Parameterized project scaffolding | Evaluate reuse rather than inventing a general rendering engine |
| [Copier](https://github.com/copier-org/copier) | Template rendering and updating generated projects | Compare update and conflict semantics before designing lifecycle tooling |
| [projen](https://projen.io/docs/introduction/) | Configuration synthesis from typed definitions | Consider declarative management trade-offs; do not copy its ownership model by default |
| [Backstage](https://backstage.io/docs/features/software-templates/) | Software scaffolding and publishing inside a developer platform | Potential future integration; avoid platform-scale scope now |
| [OpenSSF Scorecard](https://scorecard.dev/) | Automated security risk heuristics | Complement existing security tools; do not recreate or claim security certification |
| [GitHub community health files](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file) and [rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/creating-rulesets-for-a-repository) | Native shared defaults and repository policy controls | Reuse native capabilities where sufficient |

## Positioning hypothesis

The candidate differentiator is the connection between composable repository responsibilities, transparent evidence, human-reviewed adoption and lifecycle evolution. This is not a claim of uniqueness or superior performance. Generation alone is a crowded capability. Prefer interoperability and reuse where existing tools meet requirements.

## Candidate experiments

| Alternative | Observable result | Main uncertainty |
| --- | --- | --- |
| A — Creation feasibility | Isolated materialization of a bounded Backend composition with explicit unresolved inputs and verification | Artifact contracts, ownership and rendering |
| B — Adoption evidence | Repeatable read-only collection of selected facts compared with a manual baseline | Accuracy, scope and reduction of effort |
| C — Onboarding and distribution | Reproducible first useful outcome from a clean environment | Packaging and documentation friction |
| D — Consolidate only | Existing paths remain usable without new capabilities | Whether maintenance alone meets user needs |

No experiment is approved here. Compare alternatives by value, evidence, effort, risk and maintenance; consider using an existing renderer versus a minimal bounded implementation. No consumer modification, automatic decisions, release, Sprint or milestone. Next: gap analysis and a single recommended experiment with explicit success/failure criteria.
