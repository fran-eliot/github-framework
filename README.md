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

For a complete, reproducible catalog-to-validation example (including integrity checks and the difference between stale content and failed validation), see the [Component Catalog Workflow Guide](docs/implementation/validator-catalog-workflow.md).


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

To summarize declared Component statuses across the selected catalog, use `--component-status-summary` with JSON output:

```bash
python -m scripts.framework_validator --list-components --format json --component-status-summary
```

The optional `component_status_summary` object contains `by_status` counts keyed by declared status (sorted alphabetically) and a separate `missing` count for absent or non-string statuses, including unreadable metadata. These counts total the catalog `count` after all filters. Unlike `--metadata-summary`, this summarizes the Component's declared status rather than YAML loading outcomes. It requires `--list-components --format json`, composes with catalog filters, other summaries, `--details` and JSON export, and leaves the default catalog unchanged.

Validate a selection previously exported from a Component catalog by passing its JSON file to `--catalog-input`. This connects read-only discovery to the existing targeted Validator without requiring manual `--component` arguments:

```bash
python -m scripts.framework_validator --list-components --format json --family documentation --limit 5 --output selected-components.json
python -m scripts.framework_validator --catalog-input selected-components.json --format json
```

To detect changes anywhere in a Component (including templates, examples, README, metadata, and newly added or removed files), export an optional **complete Component file-tree digest**:

```bash
python -m scripts.framework_validator --list-components --format json --details --catalog-content-sha256 --output selected-components.json
python -m scripts.framework_validator --catalog-input selected-components.json --catalog-verify-content-sha256 --format json
```

The `content_sha256` digest is deterministic: it hashes each regular file's portable relative path, byte length and raw content, in sorted path order. Nested files are included; directory-only changes without file changes are not. Symbolic links are rejected rather than followed, including symlinked Component root directories and links to files outside the library. Renamed or removed files also change the digest. A missing digest, changed file tree, unreadable file, or file detected changing while its hash is computed prevents validation (argument error `2`). The hash checks file size and modification time around each read; simultaneous same-size edits that evade filesystem timestamps are not guaranteed to be detected. Both options are opt-in, require a detailed JSON catalog for export and can be combined with existing metadata checks. **This compares local Component bytes**, not the authenticity of a catalog supplied by an untrusted party or any external consumer files; default JSON and validation behavior remain unchanged.

For a stronger raw-file consistency check, include SHA-256 digests in a detailed catalog and verify them before targeted validation:

```bash
python -m scripts.framework_validator --list-components --format json --details --catalog-metadata-sha256 --output selected-components.json
python -m scripts.framework_validator --catalog-input selected-components.json --catalog-verify-sha256 --format json
```

The opt-in `metadata_sha256` property is computed from the **exact bytes** of each `metadata.yml` (not only the fields shown in `--details`). `--catalog-metadata-sha256` requires a detailed JSON listing; `--catalog-verify-sha256` requires an imported catalog with matching digests, and can be combined with `--catalog-verify-details`. A changed file or missing digest causes argument error `2` before validation. The metadata digest check rejects symlinked `metadata.yml` files and symlinked Component roots rather than following them, including links to files outside the selected library. This verifies metadata file consistency, **not** other Component files or authenticity against a trusted signer. The default JSON schema remains unchanged.

To detect **stale exported metadata** before validating, generate the catalog with `--details` and supply `--catalog-verify-details` when importing it:

```bash
python -m scripts.framework_validator --list-components --format json --details --family documentation --output selected-components.json
python -m scripts.framework_validator --catalog-input selected-components.json --catalog-verify-details --format json
```

This optional preflight compares each selected Component's exported `id`, `name`, `version`, `status` and metadata loading state with the current library. Missing/mismatched detail entries or changed metadata produce argument error `2` before validation; the default import behavior is unchanged without the flag. This is a consistency check of catalog metadata fields, **not** a cryptographic integrity check or verification of Component content. It also works with catalog input from stdin.

For automated workflows, use `--catalog-input -` to read the catalog directly from standard input, avoiding an intermediate file:

```bash
python -m scripts.framework_validator --list-components --format json --family documentation | python -m scripts.framework_validator --catalog-input - --format json
```

The same selection, path-safety checks, report format and exit codes apply to file and stdin input. The input stream is read only once; this does not modify Components.

The input must be a JSON catalog object with a non-empty `components` array of unique `FAMILY/NAME` paths from the **current Component library**. Pagination is supported: only the paths present in the exported page are validated. Use `--components-root` on both commands when working with a custom library; the input does not authorize access outside that root. The option cannot be combined with `--list-components`, `--component`, or `--family`. Invalid or missing catalogs, unsafe paths and missing Component directories cause argument error `2` before validation. Component validation errors retain exit code `1` and the normal text/JSON report, including its filtered scope. No Component files are modified.

Page a Component catalog after applying all filters and sorting, using `--limit N` (positive integer) and/or `--offset N` (non-negative integer):

```bash
python -m scripts.framework_validator --list-components --format json --sort-by name --limit 10 --offset 10 --details
```

Both options require `--list-components` and work with text, JSON, metadata filtering, summaries and atomic export. When requested, JSON adds `pagination` with `total` (matching Components **before** pagination), `offset`, `limit` (null if omitted), `has_next` (boolean), `next_offset` (integer for the next page or null at the end), `has_previous` (boolean), and `previous_offset` (integer for the preceding page or null on the first page). Follow `next_offset` or `previous_offset` with the same filters and sort options. With a limit, the previous offset is `max(0, offset - limit)`; with offset-only pagination, the previous offset is `0`. `count`, `components`, `details`, and all summaries describe the **current page**. An empty page exits with code `1` and does not overwrite existing output. Without pagination flags the output schema and ordering are unchanged.

Control the direction of an explicit catalog sort using `--sort-order asc|desc` (ascending by default):

```bash
python -m scripts.framework_validator --list-components --sort-by path --sort-order desc
python -m scripts.framework_validator --list-components --format json --sort-by status --sort-order desc --details
```

Descending metadata sorts keep missing or non-string values **last**, and keep portable paths ascending as deterministic tie-breakers. `--sort-order` requires `--sort-by` and applies after filtering in text listings or JSON exports. `scope.sort_order` is included only when the direction is specified, so existing output remains unchanged.

Sort by the declared Component status using `--sort-by status` in text or JSON catalogs:

```bash
python -m scripts.framework_validator --list-components --format json --sort-by status --details
```

Status ordering is case-sensitive and lexicographical. Missing, invalid or non-string statuses appear last; portable Component paths break ties. This works with all existing catalog filters, summaries and JSON export, while leaving the default path order unchanged.

Filter the declared Component `status` field with repeatable, case-sensitive `--component-status` glob patterns. Unlike `--metadata-status`, which selects YAML loading states (`loaded`, `missing`, `invalid`), this option matches the actual `status` string in `metadata.yml`:

```bash
python -m scripts.framework_validator --list-components --component-status "Experimental" --format json --details
```

Multiple patterns form a union and combine with other catalog filters, ordering, summaries and JSON export. Missing, invalid or non-string status fields do not match. The JSON scope includes `component_status` only when requested; an empty selection exits with code `1` without replacing an existing export.

Filter catalog entries by metadata loading state using repeatable `--metadata-status loaded|missing|invalid` (combined as a union). This loads metadata only when the status filter or `--details` requires it; it does not perform semantic validation:

```bash
python -m scripts.framework_validator --list-components --metadata-status missing --metadata-status invalid --format json --details
```

This also works with `--family`, `--match`, `--exclude` and JSON `--output`. The JSON catalog includes `scope.metadata_status` in the order `loaded`, `missing`, `invalid` when this filter is present. An empty selection exits with code `1` without overwriting an output file.

Order catalog output by path (the default), metadata ID, or metadata version with `--sort-by path|id|version`:

```bash
python -m scripts.framework_validator --list-components --sort-by id
python -m scripts.framework_validator --list-components --format json --sort-by version --details
```

Metadata sorting is case-sensitive and lexicographical (version sorting does **not** interpret SemVer precedence). Missing or non-string values appear last, with portable Component paths breaking ties. Sorting applies after filters, preserves alignment between `components` and `details`, and adds `scope.sort_by` only when explicitly requested. It supports text listings, JSON catalogs, summaries and JSON export, but not validation mode.

Filter by the `version` string from `metadata.yml` using repeatable case-sensitive `--metadata-version` glob patterns. This is a string pattern filter rather than a Semantic Versioning range resolver. Components with missing, invalid, or non-string versions are excluded:

```bash
python -m scripts.framework_validator --list-components --metadata-version "0.1.*" --format json --details
```

Combine it with ID, path, family and loading-status filters, optional summaries, and JSON `--output`. `scope.metadata_version` appears only when requested; no matches return code `1` without overwriting an existing export.

Search the human-readable `name` field in Component metadata with repeatable, case-sensitive `--metadata-name` glob patterns, or order results by name with `--sort-by name`:

```bash
python -m scripts.framework_validator --list-components --metadata-name "*Architecture*" --format json --details
python -m scripts.framework_validator --list-components --sort-by name --format json
```

Name filters match any selected glob pattern and compose with existing catalog filters, summaries and JSON export. Missing, unreadable or non-string names cannot match and sort last; ties use the Component path. JSON catalogs include `scope.metadata_name` only when filtering by name. An empty selection returns exit code `1` without changing an existing export.

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
