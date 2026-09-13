# WCL-BRANCH

## Component Metadata

| Field | Value |
| --- | --- |
| **ID** | `WCL-BRANCH` |
| **Family** | Workflow |
| **Type** | Framework Component |
| **Status** | Implemented |
| **Primary Materialization** | Convention |
| **Lifecycle** | Experimental |

---

## 1. Purpose

`WCL-BRANCH` define la responsabilidad reusable para organizar el trabajo mediante ramas de Git.

Su objetivo consiste en proporcionar convenciones suficientemente claras para aislar cambios, mantener trazabilidad y facilitar integración sin imponer un branching model innecesariamente complejo.

```text
Change
    ↓
Branch
    ↓
Commits
    ↓
Pull Request
    ↓
Integration
```

El Component define principios y convenciones reutilizables.

La estrategia concreta puede especializarse según el repositorio consumidor.

---

## 2. Responsibility

`WCL-BRANCH` es responsable de proporcionar criterios reutilizables para:

- creación de ramas;
- nomenclatura;
- propósito de cada rama;
- duración;
- integración;
- eliminación tras integración;
- relación con Issues y Pull Requests.

---

## 3. Scope

El alcance incluye:

```text
Branch purpose
Branch naming
Branch lifecycle
Integration model
Traceability
Temporary branches
Protected branches
```

La implementación Core favorece modelos simples y adaptables.

---

## 4. Out of Scope

`WCL-BRANCH` no es responsable de:

- definir commits;
- estructurar Pull Requests;
- realizar code review;
- ejecutar CI;
- definir releases completas;
- configurar permisos concretos;
- establecer reglas universales de branch protection.

Estas responsabilidades pertenecen a otros Components o al consumidor.

---

## 5. Materialization

`WCL-BRANCH` se materializa principalmente mediante:

```text
Convention
```

No requiere necesariamente un artefacto adicional.

Su definición canónica está formada por:

```text
README.md
    +
metadata.yml
```

Por tanto:

```text
Implemented
        ≠
Template File Required
```

La ausencia de `templates/` no implica que el Component sea conceptual.

---

## 6. Branching Principle

El branching model DEBERÍA ser tan simple como permita el contexto del proyecto.

Principio:

```text
Minimum Necessary Branching
```

No deben introducirse ramas permanentes, niveles intermedios o flujos adicionales sin una necesidad concreta.

---

## 7. Primary Branch

El repositorio DEBERÍA mantener una rama principal claramente identificable.

Ejemplo habitual:

```text
main
```

La rama principal representa normalmente el estado integrado del proyecto.

Su nombre concreto pertenece al consumidor.

---

## 8. Working Branches

Los cambios que requieran aislamiento PUEDEN desarrollarse mediante ramas temporales.

Ejemplos de categorías:

```text
feature/
fix/
docs/
refactor/
chore/
```

El conjunto concreto no constituye un requisito universal.

El consumidor debería mantener únicamente categorías que aporten significado real.

---

## 9. Feature Branches

Una rama de feature representa trabajo asociado a una nueva capacidad o mejora.

Patrón conceptual:

```text
feature/<short-description>
```

Ejemplos:

```text
feature/workflow-components
feature/repository-templates
```

El nombre debería comunicar el propósito sin convertirse en una descripción excesivamente larga.

---

## 10. Fix Branches

Los cambios correctivos PUEDEN utilizar:

```text
fix/<short-description>
```

cuando distinguirlos de nuevas capacidades resulte útil.

Ejemplo:

```text
fix/broken-reference
```

---

## 11. Documentation Branches

Los cambios exclusivamente documentales PUEDEN utilizar:

```text
docs/<short-description>
```

si el repositorio diferencia explícitamente este tipo de trabajo.

No es necesario crear una categoría específica cuando el branching model del consumidor sea más simple.

---

## 12. Release Branches

Los repositorios que necesiten estabilización previa a una release PUEDEN utilizar:

```text
release/<version>
```

Ejemplo:

```text
release/1.2.0
```

Las release branches no constituyen un requisito de `WCL-BRANCH`.

Solo deben utilizarse cuando exista una necesidad real de estabilización o coordinación.

---

## 13. Hotfix Branches

Los proyectos que necesiten correcciones urgentes sobre una versión publicada PUEDEN utilizar:

```text
hotfix/<short-description>
```

Su adopción depende del release model del consumidor.

No deberían incorporarse por defecto en proyectos que no las necesiten.

---

## 14. Naming

Los nombres de ramas DEBERÍAN:

- ser breves;
- describir el propósito;
- utilizar una convención consistente;
- evitar información sensible;
- evitar nombres personales como única descripción;
- evitar identificadores innecesarios.

Cuando exista una Issue relacionada, el consumidor PUEDE incorporar su identificador.

Ejemplo:

```text
feature/123-workflow-components
```

---

## 15. Traceability

Una rama PUEDE mantener relación con:

```text
Issue
    ↓
Branch
    ↓
Pull Request
```

La trazabilidad no depende necesariamente del nombre de la rama.

Puede mantenerse mediante la Pull Request y los mecanismos del proveedor.

---

## 16. Lifecycle

Las working branches DEBERÍAN ser temporales.

Modelo:

```text
Create
    ↓
Develop
    ↓
Validate
    ↓
Integrate
    ↓
Delete
```

Las ramas integradas que ya no tengan utilidad deberían eliminarse para reducir ruido.

---

## 17. Long-Lived Branches

Las ramas permanentes adicionales a la principal solo deberían existir cuando representen una responsabilidad real del delivery model.

Ejemplos posibles:

```text
develop
maintenance/*
supported-version branches
```

No deben introducirse únicamente porque formen parte de un branching model conocido.

---

## 18. Integration

La integración puede producirse mediante:

- Pull Request;
- merge;
- squash;
- rebase;
- mecanismos equivalentes.

`WCL-BRANCH` no prescribe una estrategia universal.

La elección debe ser coherente con:

- collaboration model;
- commit strategy;
- release model;
- audit requirements.

---

## 19. Branch Protection

El consumidor PUEDE proteger ramas relevantes.

Las protecciones pueden incluir:

```text
Pull Request required
Review required
Status checks required
Restricted direct pushes
```

Estas políticas pertenecen a la configuración del consumidor y pueden componerse con otros Workflow Components.

---

## 20. Composition

`WCL-BRANCH` se relaciona especialmente con:

```text
WCL-ISSUE
WCL-COMMIT
WCL-PULL-REQUEST
WCL-CODE-REVIEW
WCL-CI
WCL-RELEASE
WCL-HOTFIX
```

Ejemplo:

```text
WCL-ISSUE
    ↓
WCL-BRANCH
    ↓
WCL-COMMIT
    ↓
WCL-PULL-REQUEST
    ↓
WCL-CODE-REVIEW
```

Cada Component conserva su responsabilidad independiente.

---

## 21. Repository Template Integration

Un Repository Template puede declarar `WCL-BRANCH` como:

```text
required
recommended
optional
```

El Template puede además proporcionar una especialización apropiada para su tipo de repositorio.

Ejemplo:

```text
TPL-BACKEND
        ↓
WCL-BRANCH
        ↓
feature / fix / release conventions
```

El requirement level pertenece al Template.

---

## 22. Adoption

Adoptar `WCL-BRANCH` consiste principalmente en seleccionar y documentar las convenciones aplicables.

El consumidor DEBERÍA decidir explícitamente:

```text
Primary branch
Working branch strategy
Naming convention
Integration strategy
Cleanup policy
```

No es necesario adoptar todas las variantes descritas por el Component.

---

## 23. Specialization

La especialización puede depender de:

- tamaño del equipo;
- frecuencia de releases;
- deployment model;
- mantenimiento de múltiples versiones;
- regulación;
- contribution model.

La especialización debería reducir o adaptar el modelo.

No duplicar innecesariamente su responsabilidad.

---

## 24. Validation

Una adopción DEBERÍA comprobar:

- existencia de una rama principal clara;
- convención comprensible;
- ausencia de categorías innecesarias;
- coherencia con Pull Requests;
- coherencia con releases;
- lifecycle de ramas temporales;
- ausencia de documentación contradictoria.

La validación puede realizarse mediante inspección del repositorio y su documentación.

---

## 25. Dogfooding

GitHub Framework utiliza ramas temporales para desarrollar cambios antes de integrarlos en `main`.

Esta práctica proporciona una implementación real para validar la responsabilidad.

El Component generaliza dicha práctica sin convertir las decisiones particulares del Framework en requisitos universales.

```text
Framework Practice
        ↓
Generalization
        ↓
WCL-BRANCH
```

---

## 26. Portability

La responsabilidad se basa principalmente en Git y no depende de una funcionalidad exclusiva de GitHub.

Las capacidades de branch protection sí pueden depender del proveedor.

Por tanto:

```text
Branch Convention
        ≠
Provider Configuration
```

El núcleo del Component debe mantenerse portable.

---

## 27. Evolution

`WCL-BRANCH` puede evolucionar para incorporar:

- reusable branch policies;
- validation rules;
- naming validators;
- Repository Template specializations;
- integration with automation.

Estas capacidades deberán añadirse únicamente cuando exista una necesidad reusable demostrada.

---

## 28. Related Components

| Component | Relationship |
| --- | --- |
| `WCL-ISSUE` | Origen potencial del trabajo |
| `WCL-COMMIT` | Historial dentro de la rama |
| `WCL-PULL-REQUEST` | Integración del cambio |
| `WCL-CODE-REVIEW` | Revisión antes de integración |
| `WCL-CI` | Validación automática |
| `WCL-RELEASE` | Branching asociado a releases |
| `WCL-HOTFIX` | Correcciones urgentes |

---

## 29. Related Documentation

- `docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md`
- `docs/design-system/09_COMPONENT_CATALOG.md`
- `docs/standards/07_GITHUB_REPOSITORY_STANDARDS.md`
- `docs/governance/15_WORKING_AGREEMENTS.md`

---

## 30. Status

```text
ID: WCL-BRANCH
Family: Workflow
Status: Implemented
Primary Materialization: Convention
Validation: Reference Implementation Validated
```
