<h1 align="center">
  GitHub Framework
</h1>

🇬🇧 **English** | 🇪🇸 [Español](README_es.md)

<p align="center">
  <strong>Build repositories with the same discipline used to build software.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v0.7.0-blue" alt="Version" />
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
- Existing Repository Adoption Assessment Core
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

Run the automated test suite with:

```bash
python -m unittest discover -s tests/framework_validator -p "test_*.py"
```

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

This capability does not modify consumer repositories and does not introduce automatic remediation or automatic adoption decisions.

---

## 🗺️ Roadmap

GitHub Framework evolves through incremental releases.

Current milestones include:

- **v0.2.0** — Open Source Readiness
- **v0.3.0** — Documentation Framework
- **v0.4.0** — Repository Templates
- **v0.5.0** — Workflow Framework
- **v0.6.0** — Framework Automation
- **v0.7.0** — Existing Repository Adoption
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

**v0.7.0 — Existing Repository Adoption**

The Existing Repository Adoption Assessment Core is implemented, verified, integrated and published.

The next Framework increment has not yet been committed to a release.

---

> **Design once. Reuse everywhere.**
