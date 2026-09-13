# Workflow Components

## Purpose

Este directorio contiene las implementaciones canónicas de los **Workflow Components (`WCL-*`)** de GitHub Framework.

Los Workflow Components representan responsabilidades reutilizables relacionadas con procesos de ingeniería, colaboración, gobierno y automatización del ciclo de vida de un repositorio.

Su objetivo es permitir que distintos repositorios adopten prácticas coherentes sin duplicar innecesariamente definiciones, convenciones, configuraciones o artefactos.

---

## Architectural Context

Los Workflow Components forman una de las familias principales de Framework Components definidas por el **Repository Design System (RDS)**.

```text
Framework Components
        │
        ├── README Components
        ├── Documentation Components
        ├── Workflow Components
        └── Visual Components
```

La arquitectura, lifecycle, reglas de composición y criterios generales de implementación se definen en:

```text
docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md
```

El registro oficial de Components se mantiene en:

```text
docs/design-system/09_COMPONENT_CATALOG.md
```

---

## Component Prefix

Todos los Workflow Components utilizan el prefijo:

```text
WCL-
```

Ejemplos:

```text
WCL-ISSUE
WCL-PULL-REQUEST
WCL-CODE-REVIEW
WCL-BRANCH
WCL-COMMIT
```

El identificador representa una responsabilidad reusable del Framework.

No representa necesariamente un archivo, una GitHub Action o un mecanismo de automatización concreto.

---

## Materialization Model

Un Workflow Component puede materializarse mediante distintos mecanismos dependiendo de la responsabilidad que representa.

Entre ellos:

- Convention;
- Community File;
- Configuration;
- Executable Workflow;
- Composite Materialization.

Por tanto:

```text
Workflow Component
        ≠
GitHub Actions Workflow
```

y:

```text
Implemented
        ≠
Executable
```

Un Component basado en convenciones puede considerarse implementado cuando dispone de una definición canónica suficientemente completa y reutilizable, aunque no necesite un artefacto ejecutable.

---

## Current Core Implementations

La primera biblioteca Core de Workflow Components está formada por:

| Component | Responsibility | Primary Materialization |
| --- | --- | --- |
| `WCL-ISSUE` | Gestión estructurada de Issues | Community File / Configuration |
| `WCL-PULL-REQUEST` | Estructuración de Pull Requests | Community File |
| `WCL-CODE-REVIEW` | Revisión y ownership de cambios | Convention / Configuration |
| `WCL-BRANCH` | Gestión y nomenclatura de ramas | Convention |
| `WCL-COMMIT` | Convención y estructura de commits | Convention |

Estos Components constituyen la primera implementación física de la familia Workflow.

Otros Workflow Components reconocidos por el RDS permanecen conceptuales hasta disponer de una implementación canónica validada.

---

## Directory Structure

La estructura inicial de la biblioteca es:

```text
framework/components/workflow/
│
├── README.md
│
├── issue/
│   ├── README.md
│   └── metadata.yml
│
├── pull-request/
│   ├── README.md
│   └── metadata.yml
│
├── code-review/
│   ├── README.md
│   └── metadata.yml
│
├── branch/
│   ├── README.md
│   └── metadata.yml
│
└── commit/
    ├── README.md
    └── metadata.yml
```

La estructura interna de cada Component puede ampliarse cuando su mecanismo de materialización requiera artefactos adicionales.

No deben crearse directorios o archivos vacíos únicamente para mantener simetría entre Components.

---

## Canonical Component Structure

Cada Workflow Component implementado debe disponer como mínimo de:

```text
<component>/
├── README.md
└── metadata.yml
```

### `README.md`

Define la especificación canónica del Component.

Debe describir, cuando resulte aplicable:

- purpose;
- responsibility;
- scope;
- materialization;
- adoption;
- configuration;
- composition;
- validation;
- lifecycle considerations.

### `metadata.yml`

Proporciona metadata estructurada para identificar y clasificar el Component.

La especificación y la metadata forman conjuntamente su definición canónica.

```text
README.md
    +
metadata.yml
    ↓
Canonical Component Definition
```

---

## Additional Artifacts

Un Workflow Component puede contener artefactos adicionales cuando sean necesarios para materializar su responsabilidad.

Ejemplos:

```text
templates/
configuration/
workflow/
examples/
```

Su existencia depende del Component.

No constituyen requisitos universales.

Por ejemplo:

```text
WCL-ISSUE
        ↓
puede necesitar templates y configuration

WCL-BRANCH
        ↓
puede materializarse únicamente mediante Convention
```

La materialización debe responder a una necesidad real y no a una estructura filesystem predeterminada.

---

## Composition

Los Workflow Components pueden utilizarse:

- individualmente;
- junto con otros Workflow Components;
- como parte de Repository Templates;
- junto con README Components;
- junto con Documentation Components;
- junto con Visual Components.

Ejemplo:

```text
Repository Template
        │
        ├── WCL-ISSUE
        ├── WCL-PULL-REQUEST
        ├── WCL-CODE-REVIEW
        └── README-CONTRIBUTING
```

La composición debe mantener separadas las responsabilidades canónicas de cada Component.

---

## Repository Templates

Los Repository Templates pueden declarar Workflow Components como:

```text
required
recommended
optional
```

El requirement level pertenece al contrato del Template consumidor.

No forma parte de la identidad intrínseca del Workflow Component.

Por tanto:

```text
Component Availability
        ≠
Template Requirement Level
```

---

## Consumer Adoption

Un repositorio consumidor puede adoptar un Workflow Component mediante:

- copia controlada de artefactos;
- configuración;
- aplicación de convenciones;
- integración con Repository Templates;
- automatización futura;
- combinación de varios mecanismos.

La adopción puede requerir especialización contextual.

Sin embargo, dicha especialización no debe alterar la responsabilidad canónica del Component.

---

## Dogfooding

GitHub Framework utiliza su propio repositorio como entorno principal de validación.

Cuando una práctica existente del proyecto se generaliza como Workflow Component:

```text
Existing Practice
        ↓
Component Extraction
        ↓
Canonical Definition
        ↓
Framework Adoption
        ↓
Validation
        ↓
Refinement
```

Este proceso permite comprobar que el Component representa una responsabilidad real y reutilizable antes de promover su uso general.

---

## Implementation Status

La existencia de una responsabilidad en el Component Catalog no implica que exista una implementación física.

Los estados principales son:

```text
Conceptual
Implemented
```

Un Component pasa a `Implemented` únicamente cuando existe una definición canónica reutilizable y suficientemente completa.

La clasificación oficial debe mantenerse sincronizada con:

```text
docs/design-system/09_COMPONENT_CATALOG.md
```

---

## Design Principles

La biblioteca Workflow sigue estos principios:

```text
Responsibility before artifact

Reuse before duplication

Convention before unnecessary automation

Portability before provider coupling

Composition before monolithic workflows

Implementation before declaration of availability

Validation before generalization

Simplicity before filesystem symmetry
```

---

## Current Scope

La implementación inicial se centra en responsabilidades fundamentales del flujo de colaboración:

```text
Issue
Pull Request
Code Review
Branch
Commit
```

La automatización ejecutable, CI/CD, releases, dependency management, security workflows y otras capacidades reconocidas por el RDS evolucionarán incrementalmente.

---

## Related Documentation

- `docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md`
- `docs/design-system/09_COMPONENT_CATALOG.md`
- `docs/standards/07_GITHUB_REPOSITORY_STANDARDS.md`
- `docs/governance/15_WORKING_AGREEMENTS.md`
- `framework/templates/repositories/`

---

## Status

```text
Family: Workflow Components
Prefix: WCL-
Lifecycle: Experimental
Implementation: Incremental
Validation: Pending Reference Implementation
```
