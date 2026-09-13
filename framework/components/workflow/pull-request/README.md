# WCL-PULL-REQUEST

## Component Metadata

| Field | Value |
| --- | --- |
| **ID** | `WCL-PULL-REQUEST` |
| **Family** | Workflow |
| **Type** | Framework Component |
| **Status** | Implemented |
| **Primary Materialization** | Community File |
| **Lifecycle** | Experimental |

---

## 1. Purpose

`WCL-PULL-REQUEST` define la responsabilidad reusable para estructurar la integración de cambios mediante Pull Requests.

Su objetivo consiste en proporcionar contexto suficiente para comprender, revisar y validar un cambio antes de integrarlo.

```text
Change
    ↓
Pull Request
    ↓
Review
    ↓
Validation
    ↓
Integration
```

El Component representa la responsabilidad reusable.

No define por sí mismo toda la estrategia de branching, code review o CI del repositorio consumidor.

---

## 2. Responsibility

`WCL-PULL-REQUEST` es responsable de proporcionar una estructura reusable para:

- resumir el propósito del cambio;
- identificar Issues relacionadas;
- describir cambios relevantes;
- documentar cómo se validó;
- registrar evidencia cuando sea necesaria;
- facilitar revisión;
- reducir Pull Requests sin contexto suficiente.

---

## 3. Scope

El alcance incluye:

```text
Pull Request template
Pull Request structure
Change summary
Issue traceability
Validation evidence
Review context
```

Puede utilizarse tanto en:

- proyectos personales;
- repositorios colaborativos;
- proyectos open source;
- repositorios internos.

---

## 4. Out of Scope

`WCL-PULL-REQUEST` no es responsable de:

- definir branch strategy;
- establecer reglas de merge;
- definir número de approvals;
- configurar CODEOWNERS;
- ejecutar CI;
- definir release strategy;
- gestionar Issues;
- decidir qué cambios requieren Pull Request.

Estas responsabilidades pueden pertenecer a otros Workflow Components o a la configuración específica del consumidor.

---

## 5. Materialization

La materialización principal utiliza el community file nativo:

```text
.github/PULL_REQUEST_TEMPLATE.md
```

El artefacto reusable se mantiene canónicamente en:

```text
pull-request/
├── README.md
├── metadata.yml
└── templates/
    └── PULL_REQUEST_TEMPLATE.md
```

El archivo físico representa una materialización del Component.

No constituye su identidad.

```text
WCL-PULL-REQUEST
        ≠
PULL_REQUEST_TEMPLATE.md
```

---

## 6. Canonical Pull Request Structure

La estructura Core DEBERÍA proporcionar, cuando resulte aplicable:

```text
Summary
Related Issue
Changes
Validation
Checklist
```

Estas responsabilidades proporcionan contexto suficiente para la mayoría de cambios sin crear una plantilla excesivamente pesada.

---

## 7. Summary

La sección `Summary` DEBERÍA explicar brevemente:

- qué cambia;
- por qué cambia;
- cuál es el resultado esperado.

No debería convertirse en una reproducción completa de la Issue relacionada.

---

## 8. Related Issue

Cuando exista una Issue relacionada, la Pull Request DEBERÍA mantener trazabilidad hacia ella.

Ejemplo:

```text
Closes #123
```

o:

```text
Related to #123
```

según corresponda.

El formato concreto puede adaptarse al sistema de trabajo del consumidor.

---

## 9. Changes

La sección `Changes` DEBERÍA resumir las modificaciones relevantes.

Puede incluir:

- nuevas capacidades;
- cambios funcionales;
- refactors relevantes;
- cambios de configuración;
- documentación;
- eliminación de comportamiento.

No debería listar cada archivo modificado cuando esa información ya puede obtenerse directamente del diff.

---

## 10. Validation

La sección `Validation` DEBERÍA explicar cómo se comprobó el cambio.

Ejemplos:

```text
Tests
Manual validation
Build
Static analysis
Documentation validation
Workflow execution
```

La profundidad depende del riesgo y naturaleza del cambio.

La ausencia de automatización no impide proporcionar evidencia de validación manual.

---

## 11. Checklist

Un checklist PUEDE utilizarse para recordar verificaciones recurrentes.

Debería mantenerse limitado a criterios suficientemente generales.

Ejemplos:

- el cambio responde a una necesidad real;
- se reutilizaron Components o patrones existentes cuando correspondía;
- la documentación fue actualizada cuando era necesario;
- los enlaces fueron comprobados;
- la Pull Request está preparada para revisión.

No debería convertirse en una lista extensa de controles irrelevantes para la mayoría de cambios.

---

## 12. Small Pull Requests

Las secciones sin contenido relevante PUEDEN omitirse o simplificarse en cambios pequeños.

Principio:

```text
Structure
        ≠
Bureaucracy
```

El objetivo del Component es facilitar revisión.

No aumentar innecesariamente la carga documental.

---

## 13. Adoption

La adopción habitual consiste en materializar:

```text
templates/PULL_REQUEST_TEMPLATE.md
        ↓
.github/PULL_REQUEST_TEMPLATE.md
```

El consumidor puede especializar:

- wording;
- Issue format;
- checklist;
- evidence requirements;
- terminology;
- enlaces.

La especialización no debería eliminar el contexto mínimo necesario para revisar cambios relevantes.

---

## 14. Specialization

Repository Templates o consumidores pueden especializar el Component según:

- project type;
- risk;
- collaboration model;
- maturity;
- contribution model.

Ejemplo:

```text
TPL-BACKEND
        ↓
WCL-PULL-REQUEST
        ↓
additional API or testing evidence
```

La especialización no cambia la identidad del Component.

---

## 15. Composition

`WCL-PULL-REQUEST` puede relacionarse especialmente con:

```text
WCL-ISSUE
WCL-BRANCH
WCL-COMMIT
WCL-CODE-REVIEW
WCL-CI
WCL-DOCUMENTATION-UPDATE
```

Ejemplo:

```text
Issue
    ↓
Branch
    ↓
Commit
    ↓
Pull Request
    ↓
Code Review
    ↓
CI
```

Esta secuencia representa una posible relación operativa.

No una dependencia universal.

---

## 16. Code Review Relationship

`WCL-PULL-REQUEST` proporciona el contexto donde puede producirse code review.

Sin embargo:

```text
WCL-PULL-REQUEST
        ≠
WCL-CODE-REVIEW
```

La Pull Request estructura el cambio.

Code Review define cómo se evalúa.

---

## 17. CI Relationship

Un consumidor PUEDE integrar controles automáticos asociados a la Pull Request.

Ejemplo:

```text
Pull Request
        ↓
WCL-CI
        ↓
Validation Status
```

La existencia de CI no forma parte del contrato mínimo de `WCL-PULL-REQUEST`.

---

## 18. Repository Template Integration

Un Repository Template puede declarar `WCL-PULL-REQUEST` como:

```text
required
recommended
optional
```

El requirement level pertenece al Template.

No al Component.

---

## 19. Validation

Una adopción DEBERÍA comprobar:

- existencia del template cuando se utilice materialización GitHub;
- Markdown válido;
- ausencia de enlaces inexistentes;
- secciones coherentes;
- ausencia de instrucciones específicas del Framework no parametrizadas;
- utilidad real del checklist;
- correspondencia con el modelo de contribución del consumidor.

---

## 20. Dogfooding

GitHub Framework utiliza actualmente:

```text
.github/PULL_REQUEST_TEMPLATE.md
```

como práctica operativa real.

La implementación canónica se extrae de esa experiencia siguiendo:

```text
Existing Practice
        ↓
Generalization
        ↓
Canonical WCL-PULL-REQUEST
        ↓
Consumer Re-adoption
        ↓
Validation
```

La versión reusable no deberá contener decisiones que pertenezcan exclusivamente a GitHub Framework.

---

## 21. Portability

La responsabilidad de estructurar cambios revisables no depende conceptualmente de GitHub.

La materialización Core utiliza Pull Requests porque GitHub es la plataforma principal del Framework.

```text
Change Review Context
        ≠
Provider
```

Una futura adaptación podría utilizar mecanismos equivalentes manteniendo la responsabilidad.

---

## 22. Related Components

| Component | Relationship |
| --- | --- |
| `WCL-ISSUE` | Trazabilidad del cambio |
| `WCL-BRANCH` | Aislamiento del cambio |
| `WCL-COMMIT` | Historial del cambio |
| `WCL-CODE-REVIEW` | Evaluación del cambio |
| `WCL-CI` | Validación automatizada |
| `WCL-DOCUMENTATION-UPDATE` | Sincronización documental |

---

## 23. Related Documentation

- `docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md`
- `docs/design-system/09_COMPONENT_CATALOG.md`
- `docs/standards/07_GITHUB_REPOSITORY_STANDARDS.md`
- `.github/PULL_REQUEST_TEMPLATE.md`

---

## 24. Status

```text
ID: WCL-PULL-REQUEST
Family: Workflow
Status: Implemented
Primary Materialization: Community File
Validation: Reference Implementation Validated
```
