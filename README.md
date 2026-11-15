<h1 align="center">
  GitHub Framework
</h1>

🇬🇧 **English** | 🇪🇸 [Español](README_es.md)

<p align="center">
  <strong>Build repositories with the same discipline used to build software.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v0.11.0-blue" alt="Version" />
  <img src="https://img.shields.io/badge/status-active-success" alt="Status" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License" />
</p>

<p align="center">
  Engineering framework for designing, building and maintaining professional GitHub repositories.
</p>

## 📖 Overview

GitHub Framework is an opinionated engineering framework for designing, building and maintaining professional GitHub repositories.

Instead of treating repositories as collections of files that evolve through isolated decisions, the Framework applies software engineering principles to repository structure, documentation and long-term maintenance.

It provides a common engineering foundation through standards, reusable components, repository templates and reference implementations.

The goal is to reduce repetitive decisions while allowing each project to remain adapted to its own domain.

> Repositories are software assets. They deserve software engineering.

## ✨ Features

- Engineering standards
- Repository Design System
- Reusable documentation components
- Repository templates
- Reusable workflow components
- Common component metadata contract
- Deterministic Framework Validator
- Existing Repository Adoption Assessment, Application and Integration Cores
- Assisted Analysis Core for read-only, human-reviewed Evidence collection
- Reference implementations and dogfooding
- Framework evolution

---

## 🏗️ Framework Architecture

```text
                    GitHub Framework
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   Standards         Components         Templates
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
              Reference Implementations
```

GitHub Framework is built around a small set of engineering building blocks.

Standards define common engineering practices.

Components provide reusable documentation and repository building blocks.

Templates assemble components into reusable repository structures.

Reference implementations validate the Framework through real-world usage.

Existing Repository Adoption complements these building blocks with a human-reviewed way to reconcile an existing repository with Repository Template Responsibilities without forcing canonical files or automatic repository modification.

For a complete architectural description, see the [Architecture documentation](docs/architecture/).

---

## 🚀 Getting Started

Start by exploring the official reference implementation of GitHub Framework.

We recommend the following path:

1. Read this README.
2. Explore the documentation.
3. Discover the reusable components.
4. Review the architecture.
5. Follow the roadmap.

If you want to use the Framework, choose a starting point:

- **New repository:** explore the [Repository Template Library](framework/templates/repositories/README.md) and choose a composition appropriate to your project. Templates are not automatic repository generators.
- **Existing repository:** follow the [Existing Repository Adoption Guide](framework/adoption/README.md), select a Repository Template from the [library](framework/templates/repositories/README.md), confirm its version in the template's `metadata.yml`, and use the [first Assessment walkthrough](framework/adoption/README.md#your-first-assessment-minimal-walkthrough) to start with the [Assessment Template](framework/adoption/assessment-template.md).

---

## 🔗 Quick Links

- 📚 [Documentation](docs/)
- 🔄 [Existing Repository Adoption](framework/adoption/README.md)
- 🗺️ [Roadmap](ROADMAP.md)
- 🤝 [Contributing](CONTRIBUTING.md)
- 📄 [License](LICENSE)

---

## 📚 Documentation

Project documentation is organized into focused areas.

| Area | Description |
|------|-------------|
| [`architecture/`](docs/architecture/) | Framework architecture and design decisions. |
| [`standards/`](docs/standards/) | Engineering standards and conventions. |
| [`design-system/`](docs/design-system/) | Repository Design System and component catalog. |
| [`implementation/`](docs/implementation/) | Reference implementations and implementation guides. |
| [`governance/`](docs/governance/) | Project governance and planning documents. |
| [`framework/adoption/`](framework/adoption/) | Reusable Existing Repository Adoption Assessment Core. |

For detailed information, explore the `docs/` directory and the reusable Framework artifacts under `framework/`.

---

## ✅ Framework Validation

GitHub Framework includes a deterministic validator for its implemented Components.

The validator discovers Components, loads their metadata, and checks the Common Core, identity, uniqueness, maturity, dependencies, and applicable Workflow extensions.

Run it from the repository root:

```bash
python -m scripts.framework_validator
```

The CLI produces a human-readable report and returns exit code `0` on success or `1` when validation fails.

For machine-readable output, use:

```bash
python -m scripts.framework_validator --format json
```

To save the JSON report as a UTF-8 file (including when validation fails):

```bash
python -m scripts.framework_validator --format json --output validation-report.json
```

To validate a different Framework Component library directory, specify its root (containing the Component family directories):

```bash
python -m scripts.framework_validator --components-root path/to/framework/components
```

The option also works with `--format json` and `--output`. An explicitly selected root must be an existing directory.

To validate only selected Component families, repeat `--family` as needed:

```bash
python -m scripts.framework_validator --family documentation --family workflow
```

Available families are `readme`, `documentation`, and `workflow`. With no filter, all are validated. A filtered run checks only the selected Components, including uniqueness among those selected; it is not a full-library validation.

To discover the available Component paths without running validation (even for directories missing `metadata.yml`):

```bash
python -m scripts.framework_validator --list-components
python -m scripts.framework_validator --list-components --family documentation
```

Filter catalog paths with repeatable, case-sensitive `--match` glob patterns. Matches are combined as a sorted union; combine with `--family` to narrow the scope:

```bash
python -m scripts.framework_validator --list-components --match "documentation/*" --match "*/architecture"
```

Patterns match portable `family/name` paths using shell-style wildcards; quote them to prevent shell expansion. Use `--match` only with `--list-components`. JSON catalogs include `scope.match` when patterns are supplied. No match returns exit code `1` without overwriting an existing `--output` file.

Exclude paths from the catalog with repeatable `--exclude` glob patterns. Exclusions are applied **after** family and inclusion filtering, and remove every matching path:

```bash
python -m scripts.framework_validator --list-components --match "documentation/*" --exclude "*/architecture" --format json
```

`--exclude` requires `--list-components` and can be combined with `--match`, `--family`, `--details`, or JSON `--output`. JSON catalogs include `scope.exclude` only when exclusion patterns were supplied. Excluding all Components returns code `1` without overwriting an existing output file.

Filter catalog entries by metadata loading state using repeatable `--metadata-status loaded|missing|invalid` (combined as a union). This loads metadata only when the status filter or `--details` requires it; it does not perform semantic validation:

```bash
python -m scripts.framework_validator --list-components --metadata-status missing --metadata-status invalid --format json --details
```

This also works with `--family`, `--match`, `--exclude` and JSON `--output`. The JSON catalog includes `scope.metadata_status` in the order `loaded`, `missing`, `invalid` when this filter is present. An empty selection exits with code `1` without overwriting an output file.

Filter by the `version` string from `metadata.yml` using repeatable case-sensitive `--metadata-version` glob patterns. This is a string pattern filter rather than a Semantic Versioning range resolver. Components with missing, invalid, or non-string versions are excluded:

```bash
python -m scripts.framework_validator --list-components --metadata-version "0.1.*" --format json --details
```

Combine it with ID, path, family and loading-status filters, optional summaries, and JSON `--output`. `scope.metadata_version` appears only when requested; no matches return code `1` without overwriting an existing export.

Filter the catalog by the `id` declared in `metadata.yml` with repeatable, case-sensitive `--metadata-id` glob patterns (a union of matches). Unlike `--match`, this selects metadata IDs rather than Component paths; Components with missing, unreadable, or non-string IDs cannot match:

```bash
python -m scripts.framework_validator --list-components --metadata-id "DOC-*" --format json --details
```

Combine it with path/family filters, `--metadata-status`, `--metadata-summary`, and JSON `--output`. JSON catalogs add `scope.metadata_id` only when selected. An empty result exits with code `1` and preserves an existing export file.

To summarize the number of selected Components per family without loading metadata, add `--family-summary` to the JSON catalog:

```bash
python -m scripts.framework_validator --list-components --format json --family-summary
```

The optional `family_summary` object contains counts for `readme`, `documentation`, and `workflow` in stable order (including zero counts). Counts reflect the final selection after all filters, and sum to `count`. The option requires `--list-components --format json`, composes with `--metadata-summary`, and supports JSON `--output`.

For a compact inventory health check, add `--metadata-summary` to a JSON Component catalog to count `loaded`, `missing`, and `invalid` metadata entries after all selected filters, without including full Component details:

```bash
python -m scripts.framework_validator --list-components --format json --metadata-summary
python -m scripts.framework_validator --list-components --format json --metadata-status missing --metadata-summary
```

This option requires `--list-components --format json` and adds `metadata_summary` only when requested. It works with `--family`, `--match`, `--exclude`, `--metadata-status`, `--details`, and JSON `--output`; an empty selection keeps the existing exit code `1` behavior.

The default listing prints one portable path per line. For scripts, use `--list-components --format json` to get an object with sorted `components`, `count`, and `scope.families`:

```bash
python -m scripts.framework_validator --list-components --format json
```

For a basic inventory that also includes each Component's ID, name, version, status, and metadata loading state, add `--details`:

```bash
python -m scripts.framework_validator --list-components --format json --details
```

To export the catalog as UTF-8 JSON without printing it to stdout, use `--output` (also supports `--details`, `--family`, and `--components-root`):

```bash
python -m scripts.framework_validator --list-components --format json --details --output component-catalog.json
```

The file is written atomically, replacing an existing destination only after a successful write. A write failure returns exit code `2`; a missing destination directory is not created automatically.

The original `components` list remains unchanged; detailed entries appear under `details`. Missing or unreadable/invalid metadata is reported as `missing` or `invalid`, without running semantic validation. Both listing modes support `--family` and `--components-root`. Listing cannot be combined with `--component`. Catalog export requires `--format json`. An empty catalog returns exit code 1.

For a single Component, use its relative `family/name` path (repeat `--component` to select several):

```bash
python -m scripts.framework_validator --component documentation/architecture --format json
```

Component selection cannot be combined with `--family`; the selected directories must exist. A Component-targeted JSON report includes `scope.component_paths` and sets `scope.filtered` to `true`, even when all families are represented. Other Components are not validated. JSON reports include `scope.families` (selected families in canonical order) and `scope.filtered` (`true` for partial-family validation), so CI can distinguish partial results from full-library checks.

JSON output includes validation status, discovered Component count, loaded Component IDs, global errors, and a `components` array with each Component's path, ID, status, and related errors. The `summary` object provides counts of passed and failed Components and total validation errors. Each Component also includes a portable `relative_path` (for example, `documentation/architecture`) alongside its existing filesystem `path`. The validation scope and exit codes remain unchanged.

Run the automated test suite with:

```bash
python -m unittest discover -s tests/framework_validator -p "test_*.py"
```

GitHub Actions also runs the Validator test suite and checks the repository Components on pull requests and pushes to `main` via `.github/workflows/framework-validator.yml`, on both Ubuntu and Windows (Python 3.11). Each operating-system job uploads a separate `framework-validator-report-<os>` JSON artifact (retained for 7 days), including when the checks fail. The job summary also displays validation status, selected families, and aggregate Component/error counts. If Components fail, it lists up to ten affected relative paths, their error counts, and a truncated first diagnostic per Component; the complete report remains in the JSON artifact. When Component validation fails, GitHub Actions also emits file-linked error annotations (limited to 25) for quicker PR review.

The v0.6.0 reference implementation validates 21 Components and includes 109 automated tests.

For details, see the [Component Metadata Standard](docs/standards/21_COMPONENT_METADATA_STANDARD.md) and [Automation Reference Implementation](docs/implementation/22_AUTOMATION_REFERENCE_IMPLEMENTATION.md).

The validator checks deterministic rules; it does not replace architectural review or generate repository content.

---

## 🔄 Existing Repository Adoption

GitHub Framework includes a reusable **Existing Repository Adoption Assessment Core** for evaluating an existing repository against the Responsibilities defined by a Repository Template.

The supported process is:

```text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
```

The Assessment Core is:

```text
manual
human-readable
human-editable
human-reviewed
non-destructive
```

It supports non-canonical, equivalent and distributed implementations and keeps Evidence, evaluation and Adoption Decisions explicitly separated.

The reusable artifacts are:

- [Adoption Guide](framework/adoption/README.md)
- [Assessment Template](framework/adoption/assessment-template.md)
- [Application Guide](framework/adoption/application/README.md)
- [Integration Guide](framework/adoption/integration/README.md)
- [Assisted Analysis Guide](framework/adoption/assisted-analysis/README.md)
- [Evidence Snapshot Template](framework/adoption/assisted-analysis/evidence-snapshot-template.md)

This capability does not modify consumer repositories and does not introduce automatic remediation or automatic adoption decisions.

---

## 🗺️ Roadmap

GitHub Framework evolves through incremental releases.

Published milestones include:

- **v0.2.0** — Open Source Readiness
- **v0.3.0** — Documentation Framework
- **v0.4.0** — Repository Templates
- **v0.5.0** — Workflow Framework
- **v0.6.0** — Framework Automation
- **v0.7.0** — Existing Repository Adoption Assessment Core
- **v0.8.0** — Existing Repository Adoption Application Core
- **v0.9.0** — Existing Repository Adoption Integration Core
- **v0.10.0** — Existing Repository Adoption Assisted Analysis Core
- **v0.11.0** — Framework Validator CLI and CI
- **v1.0.0** — Stable Release

For the complete roadmap, see [ROADMAP.md](ROADMAP.md).

---

## 🤝 Contributing

Contributions of any size are welcome.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an Issue or Pull Request.

---

## 📄 License

This project is released under the MIT License.

---

## ⭐ Project Status

GitHub Framework is currently evolving through incremental releases.

The latest published release is:

**v0.11.0 — Framework Validator CLI and CI** ([GitHub Release](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0))

Assessment, Application, Integration and Assisted Analysis Cores are implemented, verified, integrated and published. Assisted Analysis collects bounded, source-traceable Evidence through a read-only, human-reviewed process; it does not automate adoption decisions or modify consumer repositories.

**Published on 2026-11-15:** [v0.11.0 — Framework Validator CLI and CI](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0). This Option A full-tree snapshot includes Validator CI/CLI improvements and the completed, evidence-qualified **documentary** Only Film Assessment; it does not imply consumer migration, runtime/security certification or independent usability testing.

---

> **Design once. Reuse everywhere.**
