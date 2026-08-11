# Contributing to GitHub Framework

Thank you for your interest in contributing to GitHub Framework.

GitHub Framework evolves through small, evidence-driven changes that prioritize simplicity, reuse and maintainability.

Before contributing, please review the principles below.

## Contribution Principles

Contributions should follow these principles:

- Solve a real problem.
- Prefer reuse over duplication.
- Keep solutions as simple as possible.
- Avoid unnecessary architectural changes.
- Reuse existing components and patterns whenever possible.
- Validate changes through real usage.
- Keep documentation aligned with implementation.

## Before Opening an Issue

Before opening an Issue:

1. Check whether a similar Issue already exists.
2. Verify whether an existing component, template or pattern already solves the problem.
3. Describe the problem before proposing a solution.
4. Provide enough context to understand the use case.

Use the appropriate Issue template:

- **Bug report** for reproducible problems.
- **Feature request** for improvements or new capabilities.

Repository maintainers will assign area, priority and milestone during triage.

## Issue Triage

Repository maintainers are responsible for classifying new Issues.

During triage, maintainers may:

- assign labels;
- set priorities;
- assign milestones;
- request additional information;
- close duplicate or out-of-scope Issues.

## Development Workflow

The typical contribution workflow is:

1. Fork or clone the repository.
2. Create a branch for the change.
3. Implement the smallest change that solves the problem.
4. Validate the result.
5. Commit using the project commit conventions.
6. Open a Pull Request.

Example branch names:

```text
feature/documentation-components
fix/broken-reference
docs/update-roadmap
```

## Commit Messages

GitHub Framework follows the Conventional Commits specification.

Examples:
```text
feat(components): add documentation component
docs(readme): improve getting started section
fix(templates): correct invalid repository path
refactor(components): simplify component metadata
```

Commit messages should describe the purpose of the change clearly and concisely.

## Pull Requests

Pull Requests should:

- Address a real project need.
- Be focused on a single coherent change.
- Reference the related Issue when applicable.
- Explain what changed and why.
- Describe how the change was validated.
- Avoid unrelated refactoring.

Use the repository Pull Request template when opening a PR.

## Validation

Before submitting a Pull Request, verify that:

- The change works as intended.
- Existing links remain valid.
- Documentation reflects the implementation.
- Existing components or patterns were reused where appropriate.
- No unnecessary complexity was introduced.

Additional validation requirements may be introduced as automated tooling evolves.

## Architecture Changes

The base architecture of GitHub Framework is considered stable.

Architectural changes should only be proposed when a real implementation demonstrates that the existing architecture cannot solve the problem cleanly.

Before proposing an architectural change, consider whether the problem can be solved through:

- an existing component;
- a new reusable component;
- a template;
- an improvement to an existing pattern.

Repository-wide structural changes should be supported by clear evidence from real implementations.

## Language Policy

GitHub Framework follows a bilingual documentation policy based on the audience and responsibility of the content.

### English

English is used for:

- source code;
- filenames and directory names;
- technical identifiers;
- component IDs;
- metadata keys and canonical metadata values;
- commits and branch names;
- GitHub repository metadata;
- the main public README;
- public-facing content intended primarily for an international audience.

### Spanish

Spanish is used for:

- architecture documentation;
- governance documentation;
- design documentation;
- development documentation;
- internal specifications;
- explanatory content of Documentation Components;
- guidance included in reusable templates when it is not part of the final technical artifact.

Established technical terms may remain in English when translation would reduce clarity.

### Reusable Components

Reusable components keep their technical identity in English while their explanatory documentation may be written in Spanish.

Examples:

```text
DOC-ARCHITECTURE
metadata.yml
Experimental
Recommended
```

while explanatory content such as component README files and template guidance may remain in Spanish.

The complete documentation policy is defined in:

[`docs/standards/17_DOCUMENTATION_WRITING_STANDARDS.md`](docs/standards/17_DOCUMENTATION_WRITING_STANDARDS.md)

## Code of Conduct

GitHub Framework aims to maintain a respectful and constructive collaboration environment.

A formal Code of Conduct may be introduced as the contributor community grows.

## Questions and Discussions

Use GitHub Issues for bugs and concrete improvement proposals.

General discussions or support channels may be introduced in future versions of the Framework.

---

Thank you for helping improve GitHub Framework.