# Changelog

## [Unreleased]

### Added

* Existing Repository Adoption discovery using `TPL-BACKEND` against external consumer repositories.
* Provisional adoption model separating detected facts, evidence, responsibility state, applicability, implementation characteristics, uncertainty, evaluation rationale and adoption decisions.
* Manual Adoption Assessment experiment demonstrating the operational feasibility and traceability of the provisional model.
* Discovery documentation:
  * `23_BACKEND_ADOPTION_DISCOVERY.md`
  * `24_ADOPTION_MODEL_DISCOVERY.md`
  * `25_MANUAL_ADOPTION_ASSESSMENT_DISCOVERY.md`

### Changed

* Refined the understanding of Existing Repository Adoption from generation toward reconciliation of existing consumer responsibilities with Repository Template expectations.
* Refined the boundary between deterministic evidence collection, semantic assessment, adoption decisions and future repository modification.

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