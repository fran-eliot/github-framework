# WCL-ISSUE

## Component Metadata

| Field | Value |
| --- | --- |
| **ID** | `WCL-ISSUE` |
| **Family** | Workflow |
| **Type** | Framework Component |
| **Status** | Implemented |
| **Primary Materialization** | Community File / Configuration |
| **Lifecycle** | Experimental |

---

## 1. Purpose

`WCL-ISSUE` define la responsabilidad reusable para estructurar la creación y captura de Issues dentro de un repositorio.

Su objetivo es proporcionar un mecanismo coherente para transformar una solicitud no estructurada en información suficientemente clara para su evaluación, clasificación y posterior incorporación al workflow del proyecto.

```text
User Need
    ↓
Structured Issue
    ↓
Evaluation
    ↓
Classification
    ↓
Project Workflow
```

El Component define la responsabilidad y el contrato reusable.

No define por sí mismo la estrategia completa de gestión de Issues de un repositorio consumidor.

---

## 2. Responsibility

`WCL-ISSUE` es responsable de proporcionar mecanismos reutilizables para:

- estructurar la creación de Issues;
- capturar información mínima relevante;
- distinguir diferentes tipos de solicitud cuando resulte necesario;
- reducir Issues incompletas o ambiguas;
- facilitar clasificación y triage;
- proporcionar instrucciones contextuales;
- dirigir solicitudes que no deban convertirse en Issues hacia canales alternativos cuando corresponda.

---

## 3. Scope

El alcance del Component incluye:

```text
Issue creation
Issue Forms
Issue templates
Issue configuration
Submission guidance
Contact links
```

Puede incluir distintas variantes de formularios cuando el repositorio consumidor necesite distinguir responsabilidades diferentes.

Ejemplos:

```text
Bug Report
Feature Request
```

---

## 4. Out of Scope

`WCL-ISSUE` no es responsable de:

- definir el Product Backlog;
- establecer prioridades concretas;
- asignar Issues;
- definir milestones;
- implementar project boards;
- definir una estrategia completa de labels;
- gestionar Pull Requests;
- definir branch strategy;
- ejecutar automatizaciones posteriores al alta del Issue.

Estas responsabilidades pueden pertenecer a otros Workflow Components o al gobierno específico del repositorio consumidor.

---

## 5. Materialization

La materialización primaria de `WCL-ISSUE` utiliza capacidades nativas de GitHub.

Estructura habitual:

```text
.github/
└── ISSUE_TEMPLATE/
    ├── bug_report.yml
    ├── feature_request.yml
    └── config.yml
```

Esta estructura constituye una materialización del Component.

No constituye su identidad.

Por tanto:

```text
WCL-ISSUE
        ≠
bug_report.yml
```

y:

```text
WCL-ISSUE
        ≠
GitHub Issue Forms
```

La responsabilidad puede evolucionar hacia otros mecanismos compatibles sin modificar el ID del Component.

---

## 6. Canonical Artifacts

La implementación Core puede proporcionar artefactos reutilizables bajo:

```text
issue/
├── README.md
├── metadata.yml
└── templates/
    ├── bug_report.yml
    ├── feature_request.yml
    └── config.yml
```

Los archivos contenidos en `templates/` representan materializaciones reutilizables.

El repositorio consumidor los adopta en:

```text
.github/ISSUE_TEMPLATE/
```

---

## 7. Issue Form Principles

Los formularios proporcionados por el Component DEBERÍAN:

- solicitar únicamente información útil;
- utilizar campos comprensibles;
- distinguir claramente información requerida y opcional;
- evitar formularios innecesariamente extensos;
- utilizar placeholders solo cuando aporten orientación;
- evitar imponer detalles técnicos que el usuario no pueda conocer;
- permitir evaluar la solicitud sin requerir conversaciones innecesarias;
- mantenerse suficientemente genéricos para su reutilización.

---

## 8. Bug Report

Una variante de Bug Report DEBERÍA permitir capturar como mínimo:

```text
Problem
Expected behavior
Actual behavior
Reproduction information
Relevant context
```

La implementación concreta PUEDE adaptar estos campos según el tipo de proyecto.

El formulario no debería asumir un stack tecnológico específico salvo especialización explícita.

---

## 9. Feature Request

Una variante de Feature Request DEBERÍA permitir capturar como mínimo:

```text
Problem
Proposed solution
Value
Alternatives considered
```

El objetivo consiste en capturar primero la necesidad y después la solución propuesta.

```text
Problem
    ↓
Value
    ↓
Possible Solution
```

Una Feature Request no debería reducirse únicamente a una descripción de implementación.

---

## 10. Configuration

`config.yml` PUEDE utilizarse para controlar el comportamiento general del sistema de Issues.

Puede definir:

- disponibilidad de blank Issues;
- enlaces de contacto;
- canales alternativos;
- documentación relacionada.

La configuración debe mantenerse alineada con el modelo de contribución del repositorio consumidor.

---

## 11. Blank Issues

La disponibilidad de blank Issues constituye una decisión del repositorio consumidor.

Un repositorio PUEDE deshabilitarlas cuando:

- existan formularios suficientes;
- se quiera favorecer información estructurada;
- las solicitudes no estructuradas generen ambigüedad frecuente.

También PUEDE habilitarlas cuando el dominio del proyecto requiera flexibilidad adicional.

Por tanto:

```text
blank_issues_enabled
        =
Consumer Configuration
```

No forma parte de la identidad de `WCL-ISSUE`.

---

## 12. Contact Links

Los Contact Links permiten redirigir solicitudes que no deberían convertirse en Issues.

Ejemplos:

```text
Security reporting
Support
Documentation
Discussions
Community channels
```

No deben añadirse enlaces únicamente para completar la configuración.

Cada enlace debe representar un canal real y mantenido.

---

## 13. Adoption

La adopción típica consiste en copiar o generar los artefactos seleccionados dentro de:

```text
.github/ISSUE_TEMPLATE/
```

Flujo conceptual:

```text
WCL-ISSUE
    ↓
Select artifacts
    ↓
Consumer specialization
    ↓
.github/ISSUE_TEMPLATE/
    ↓
Validation
```

El consumidor puede modificar:

- títulos;
- descripciones;
- labels;
- campos;
- placeholders;
- validaciones;
- contact links.

Estas modificaciones no deberían destruir la responsabilidad estructural del Component.

---

## 14. Specialization

Repository Templates u otros consumidores pueden especializar `WCL-ISSUE`.

Ejemplo:

```text
TPL-BACKEND
    ↓
WCL-ISSUE
    ↓
Bug Report specialized for backend repositories
```

La especialización puede añadir contexto específico, pero debería preservar la semántica principal de los formularios.

---

## 15. Composition

`WCL-ISSUE` puede componerse especialmente con:

```text
WCL-LABEL
WCL-PROJECT
WCL-BRANCH
WCL-PULL-REQUEST
WCL-DOCUMENTATION-UPDATE
```

Ejemplo:

```text
Issue
    ↓
Classification
    ↓
Branch
    ↓
Pull Request
    ↓
Review
```

La composición no implica que `WCL-ISSUE` asuma las responsabilidades de esos Components.

---

## 16. Repository Template Integration

Un Repository Template puede declarar `WCL-ISSUE` como:

```text
required
recommended
optional
```

Ejemplo conceptual:

```yaml
components:
  required:
    - WCL-ISSUE
```

El requirement level pertenece al contrato del Repository Template.

No pertenece al Component.

---

## 17. Validation

Una adopción de `WCL-ISSUE` DEBERÍA validar al menos:

- existencia de los artefactos declarados;
- sintaxis válida de los Issue Forms;
- coherencia de los campos;
- ausencia de referencias inexistentes;
- coherencia de labels preasignados;
- validez de Contact Links;
- correspondencia entre configuración y comportamiento esperado.

La validación puede ser manual o automatizada.

---

## 18. Dogfooding

GitHub Framework utiliza `WCL-ISSUE` sobre su propio repositorio.

La práctica existente:

```text
.github/ISSUE_TEMPLATE/
├── bug_report.yml
├── feature_request.yml
└── config.yml
```

sirve como primera referencia de implementación.

El proceso de dogfooding permite:

```text
Existing Implementation
        ↓
Extraction
        ↓
Generalization
        ↓
Canonical Component
        ↓
Re-adoption
        ↓
Validation
```

La implementación reusable no debe limitarse a copiar accidentalmente decisiones específicas del repositorio Framework.

---

## 19. Portability

`WCL-ISSUE` utiliza actualmente mecanismos nativos de GitHub para su materialización principal.

Sin embargo, la responsabilidad conceptual debe mantenerse separada del proveedor.

```text
Issue Intake Responsibility
        ≠
Provider
```

Una futura adaptación a otro entorno puede utilizar una materialización diferente conservando la misma responsabilidad conceptual.

---

## 20. Evolution

El Component puede evolucionar para incorporar:

- nuevas variantes de formularios;
- mejores reglas de validación;
- integración con otros Workflow Components;
- generación automática;
- validadores estructurales;
- especializaciones reutilizables.

La evolución debe preservar compatibilidad conceptual siempre que sea posible.

---

## 21. Related Components

| Component | Relationship |
| --- | --- |
| `WCL-LABEL` | Clasificación de Issues |
| `WCL-PROJECT` | Seguimiento del trabajo |
| `WCL-BRANCH` | Inicio del flujo de implementación |
| `WCL-PULL-REQUEST` | Integración de cambios |
| `WCL-DOCUMENTATION-UPDATE` | Sincronización documental |

---

## 22. Related Documentation

- `docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md`
- `docs/design-system/09_COMPONENT_CATALOG.md`
- `docs/standards/07_GITHUB_REPOSITORY_STANDARDS.md`
- `docs/governance/15_WORKING_AGREEMENTS.md`
- `.github/ISSUE_TEMPLATE/`

---

## 23. Status

```text
ID: WCL-ISSUE
Family: Workflow
Status: Implemented
Primary Materialization: Community File / Configuration
Validation: Reference Implementation Validated
```
