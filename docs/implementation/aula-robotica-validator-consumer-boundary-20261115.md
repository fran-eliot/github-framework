# Read-only Consumer Boundary Study — Aula Robótica Platform

**Study date:** 2026-11-15  
**Consumer:** [fran-eliot/aula-robotica-platform](https://github.com/fran-eliot/aula-robotica-platform)  
**Pinned consumer commit:** [`92db31aabe0d9ea2ec53974b802d617ca9a250fe`](https://github.com/fran-eliot/aula-robotica-platform/commit/92db31aabe0d9ea2ec53974b802d617ca9a250fe)  
**Framework baseline:** `main` at [`86236c20ac7dcf11f18e71cce22bf888c45c353a`](https://github.com/fran-eliot/github-framework/commit/86236c20ac7dcf11f18e71cce22bf888c45c353a), before this study's PR.  
**Study type:** Source inspection plus **isolated local simulation** of CLI scope. **Not** an Existing Repository Adoption Assessment, Application, Integration, deployment test or consumer certification.

## Evidence inspected

The following files were accessed from the **exact pinned consumer commit**:

| Source | Directly observed facts | Evidence boundary |
| --- | --- | --- |
| [README.md](https://github.com/fran-eliot/aula-robotica-platform/blob/92db31aabe0d9ea2ec53974b802d617ca9a250fe/README.md) | Describes an educational robotics collaboration platform with FastAPI, SQLAlchemy, IAM/RBAC, Jinja2, MariaDB, Docker and Nginx; its documented structure includes `app/`, `deploy/`, `docs/`, and `tests/` | These are **README descriptions**, not independently executed or deployment-verified assertions |
| [pyproject.toml](https://github.com/fran-eliot/aula-robotica-platform/blob/92db31aabe0d9ea2ec53974b802d617ca9a250fe/pyproject.toml) | Declares `requires-python = ">=3.13"`, FastAPI and SQLAlchemy dependencies, plus pytest and Ruff in the development dependency group | Project configuration; not proof that dependencies installed or tests passed |

Only the two named source files were examined for this study. **No repository-wide presence/absence audit** was performed. In particular, this study does **not** claim that a `framework/components/` directory does not exist at the pinned consumer commit. Its presence or absence in the full consumer tree remains unverified here.

## Technical question

**Can the existing Framework Validator be pointed at an ordinary application repository root and thereby validate that application's own runtime, structure, security or adoption?**

**Answer from the Validator contract: No.** The Validator's `--components-root` parameter identifies a **Framework Component library root** with supported family directories such as `readme/`, `documentation/` and `workflow/`. It is not an application-repository validator. A selection or successful Component report does not establish adoption of a Repository Template or certify a consumer runtime. See the [CLI/JSON contract](../implementation/validator-compatibility-contract.md) and [adoption guide](../../framework/adoption/README.md).

## Isolated compatibility simulation

Automated tests in [`test_consumer_boundary.py`](../../tests/framework_validator/test_consumer_boundary.py) create a **temporary, simplified application-like fixture**, not a checkout or copy of the consumer. It contains `README.md`, `pyproject.toml`, `app/` and `tests/` with placeholder content.

The tests assert:

1. Running `--components-root` against the fixture's generic application root returns a failed JSON validation (`components_discovered = 0`), instead of implying that the application is validated.
2. The generic application files do not appear as Framework Components in `--list-components` output.
3. A **separately and explicitly selected** fixture library at `framework/components/` can contain a valid Documentation Component and be catalogued/validated on its own terms. This verifies the **Component library** only, not the surrounding application.
4. The application-only test preserves fixture file bytes; it does not write to an external consumer.

Tests run in the existing Ubuntu/Windows Framework CI matrix. The results apply to the synthetic fixture and the documented Validator interface; **do not report them as tests performed on Aula Robótica Platform**.

## Findings and decision boundaries

| Question | Finding |
| --- | --- |
| Is the consumer's declared stack an application stack? | **Yes, in the two inspected source files** |
| Can Validator validate such an application's business logic directly? | **No** — outside the current Component Validator scope |
| Was the consumer's complete directory tree inventoried? | **No** |
| Was a Framework Component library found or ruled out in the consumer? | **Not established** |
| Was the consumer's CI, coverage, runtime, deploy or security verified? | **No** |
| Was an Adoption Assessment initiated or its Decisions altered? | **No** |
| Was any consumer source edited? | **No** |

**Readiness implication:** improving the Framework Validator and its catalog integrity is valuable for Framework **Component libraries**. It should not be advertised as generic consumer compatibility or an automated route through Existing Repository Adoption.

## Possible next step — requires separate scope approval

A genuinely consumer-specific follow-up could perform a **bounded read-only inventory** of the pinned repository and compare observable repository artifacts with the Responsibilities of a **separately chosen and pinned** Repository Template. That would be a new assessment scope with its own evidence and review, not a continuation or transfer of Only Film decisions. Do not assign Adoption classifications, claim completed responsibilities, modify the consumer or start Application/Integration from this study.

**Release boundary:** this study does not clear the consumer-use evidence gap in the [Unreleased readiness review](../releases/framework-validator-unreleased-readiness-20261115.md). It clarifies what evidence would be needed instead.
