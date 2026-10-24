# Changelog

## [Unreleased]

### Added

* Existing Repository Adoption discovery using `TPL-BACKEND` against external consumer repositories.
* Provisional adoption model separating detected facts, evidence, responsibility state, applicability, implementation characteristics, uncertainty, evaluation rationale and adoption decisions.
* Manual Adoption Assessment experiment demonstrating the operational feasibility and traceability of the provisional model.
* Repeatability Experiment validating reuse of the minimal adoption assessment representation against `dental-back-spring`.
* `Minimal Adoption Guide — Version 0` and `Structured Markdown Assessment Template — Version 0` as the frozen representation used during the experiment.
* Complete assessment of all 28 `TPL-BACKEND v0.1.0` Responsibilities on an additional real backend consumer.
* Discovery Synthesis consolidating the Existing Repository Adoption evidence, Requirement Candidates, Solution Hypotheses, refinements and Delivery Readiness boundary.
* `Existing Repository Adoption — Assessment Core` identified as ready for Delivery Scope Definition.
* Delivery Scope Definition for `Existing Repository Adoption — Assessment Core`.
* Delivery Scope Acceptance Criteria covering capability, representation, traceability, integration and scope boundaries.
* Hybrid integration model separating reusable adoption artifacts from historical Discovery evidence.
* Delivery Scope defining the planned reusable adoption artifacts:
  * `framework/adoption/README.md` — reusable Adoption Guide.
  * `framework/adoption/assessment-template.md` — reusable Structured Markdown Assessment Template.
* `Decision Status` introduced to distinguish resolved Adoption Decisions from Responsibilities requiring further evaluation.
* Implementation Plan for `Existing Repository Adoption — Assessment Core`, defining:
  * three implementation units;
  * GitHub Issue decomposition;
  * dependency flow;
  * Acceptance Criteria allocation;
  * relative effort;
  * single-Sprint suitability;
  * Definition of Ready and Definition of Done.
* Discovery and implementation planning documentation:
  * `23_BACKEND_ADOPTION_DISCOVERY.md`
  * `24_ADOPTION_MODEL_DISCOVERY.md`
  * `25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md`
  * `26_ADOPTION_SOLUTION_SHAPING_DISCOVERY.md`
  * `27_ADOPTION_REPEATABILITY_EXPERIMENT.md`
  * `28_ADOPTION_DISCOVERY_SYNTHESIS.md`
  * `29_ADOPTION_DELIVERY_SCOPE.md`
  * `30_ADOPTION_IMPLEMENTATION_PLAN.md`

### Changed

* Refined the understanding of Existing Repository Adoption from generation toward reconciliation of existing consumer responsibilities with Repository Template expectations.
* Refined the boundary between deterministic evidence collection, semantic assessment, adoption decisions and future repository modification.
* Compared Markdown Guide, Markdown Assessment, Tabular Assessment, Generated Report and Structured Data Representation as candidate representations for Existing Repository Adoption.
* Identified `Markdown Guide + Structured Markdown Assessment` as the minimal representation with sufficient evidence to proceed toward Delivery Scope Definition.
* Validated that `Markdown Guide + Structured Markdown Assessment` can support a complete additional consumer assessment without material redesign.
* Refined Responsibility Applicability as distinct from canonical artifact necessity.
* Confirmed that documentation presence does not imply Responsibility Satisfaction.
* Consolidated `PRESERVE`, `ADAPT`, `ADD`, `ACCEPT` and `OMIT` as the stable Adoption Decision vocabulary for the first Assessment Core delivery.
* Replaced `EVALUATE` as a stable Adoption Decision with:
  * `Decision Status: Resolved`
  * `Decision Status: Needs Further Evaluation`
* Removed `JUSTIFY` from the stable Adoption Decision vocabulary for the first delivery; justification remains represented through `Evaluation Rationale` and `Decision Rationale`.
* Kept Implementation Characteristics as provisional descriptive vocabulary rather than a closed contract.
* Consolidated the supported assessment process as `ANALYZE → ASSESS → REVIEW → DECIDE → REPORT`.
* Defined the Assessment Core as a manual, human-readable, human-editable and human-reviewed capability.
* Defined the initial integration boundary as reusable Framework artifacts under `framework/adoption/`, while preserving experimental and historical evidence under `docs/discovery/`.
* Confirmed that the first delivery does not require a new Component family, Component metadata, Component Catalog changes or Framework Validator integration.
* Deferred `APPLY`, `VERIFY`, repository modification, automatic remediation, Structured Data, Adoption Manifest, Adoption CLI, Framework Validator integration, GitHub Actions integration, generated report tooling, continuous reassessment and drift detection.
* Advanced Existing Repository Adoption from Delivery Scope Definition to planned implementation decomposition for the Assessment Core.
* Defined the implementation sequence as Adoption Guide → Assessment Template → Verification and Integration.
* Confirmed that the Assessment Core is suitable for a single Sprint while keeping Sprint, milestone and target version unassigned pending Issue creation and release planning.

---

## [0.6.0] - 2026-09-21

### Added

* Component Metadata Standard defining a shared Common Core and family-specific metadata extensions.
* Framework Validator with deterministic checks for:

  * Component discovery and metadata loading.
  * Common Core fields and controlled vocabularies.
  * Component identity and ID uniqueness.
  * Maturity and dependency declarations.
  * Workflow-specific metadata and local artifacts.
* Minimal validator CLI through `python -m scripts.framework_validator`.
* Human-readable validation reports and deterministic exit codes (`0` for success, `1` for validation failure).
* Automation Reference Implementation documenting Framework dogfooding, validation evidence, findings and limitations.
* Automated tests covering valid metadata and representative failures, including missing Workflow artifacts and duplicate Component IDs.

### Changed

* Normalized the metadata of all 21 implemented Components across the README, Documentation and Workflow families.
* Aligned the Framework Validator with the established metadata and Workflow Component standards.
* Preserved family-specific metadata semantics within the normalized contract.

### Validation

* Successfully validated all 21 implemented Components through Framework dogfooding.
* Passed 109 automated tests.
* Verified the validator CLI success exit code (`0`) and representative failure exit code (`1`).

---

## [0.5.0] - 2026-09-14

### Added

- Workflow Component Architecture.
- Core Workflow Components:
  - `WCL-ISSUE`.
  - `WCL-BRANCH`.
  - `WCL-COMMIT`.
  - `WCL-PULL-REQUEST`.
  - `WCL-CODE-REVIEW`.
- Workflow Reference Implementation.
- Workflow Component Standards.

### Changed

- Repository Design System extended with the Workflow Component model and implementation boundary.
- Component Catalog extended with the first implemented Workflow Components.
- Workflow Component Library validated through Framework dogfooding.
- Physical and convention-based Workflow Component materializations validated through the Reference Implementation.
- Consumer specialization rules validated for reusable Workflow Components.
- Implementation classification, lifecycle and validation state explicitly separated for Workflow Components.
- Project governance synchronized with the Workflow Framework lifecycle.

---

## [0.4.0] - 2026-08-18

### Added

- Repository Template Architecture.
- Core Repository Templates:
  - `TPL-BACKEND`.
  - `TPL-FULLSTACK`.
  - `TPL-DOCUMENTATION`.
- Repository Template Reference Implementation.
- Repository Template Standards.

### Changed

- Repository Design System extended with the Repository Template model.
- Component Catalog extended to cover Repository Templates and refined Component availability classification.
- Repository Template Library validated through Framework dogfooding.
- Repository Template composition rules refined through the Reference Implementation.
- Component availability and consumer conformance explicitly separated.
- Project governance synchronized with the Repository Templates lifecycle.

---

## [0.3.0] - 2026-08-13

### Added

- Documentation Component Architecture.
- Core Documentation Components:
  - `DOC-ARCHITECTURE`.
  - `DOC-PROJECT-STATUS`.
  - `DOC-CHANGELOG`.
  - `DOC-REFERENCES`.
- Documentation Reference Implementation.
- Documentation Writing Standards.

### Changed

- Repository Design System metadata aligned with GitHub Framework.
- Component Catalog metadata aligned with GitHub Framework.
- Project Status aligned with the reusable `DOC-PROJECT-STATUS` component.
- Documentation governance refined through Framework dogfooding.
- Documentation language policy aligned across contribution and component documentation.
- Documentation Component Library linked to the official Documentation Writing Standards.

---

## [0.2.0] - 2026-08-09

### Added

- Official Framework README.
- Spanish README localization.
- MIT License.
- GitHub Community Files.
- CODEOWNERS.
- Pull Request template.
- Bug Report Issue Form.
- Feature Request Issue Form.
- Contribution Guide (`CONTRIBUTING.md`).

### Changed

- Repository prepared for Open Source collaboration.
- README converted into the official reference implementation.
- Documentation governance refined after the first implementation sprint.

---

## [0.1.0] - 2026-08-06

### Added

- Arquitectura inicial del GitHub Framework.
- GitHub Repository Standards (GRS).
- Repository Design System (RDS).
- Component Catalog.
- Primera biblioteca de componentes README.
- Estructura inicial del Framework.
