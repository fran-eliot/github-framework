# WCL-CODE-REVIEW

## Component Metadata

| Field | Value |
| --- | --- |
| **ID** | `WCL-CODE-REVIEW` |
| **Family** | Workflow |
| **Type** | Framework Component |
| **Status** | Implemented |
| **Primary Materialization** | Convention / Configuration |
| **Lifecycle** | Experimental |

---

## 1. Purpose

`WCL-CODE-REVIEW` define la responsabilidad reusable para revisar cambios antes de su integración.

Su objetivo consiste en proporcionar criterios y mecanismos suficientes para evaluar:

- corrección;
- claridad;
- mantenibilidad;
- impacto;
- calidad;
- seguridad;
- coherencia con el repositorio.

Modelo:

```text
Proposed Change
    ↓
Review Context
    ↓
Technical Evaluation
    ↓
Feedback
    ↓
Approval / Rework
```

El Component representa la responsabilidad de revisión.

No representa únicamente una configuración de ownership.

---

## 2. Responsibility

`WCL-CODE-REVIEW` es responsable de proporcionar prácticas reutilizables para:

- revisar cambios;
- identificar responsables de revisión cuando corresponda;
- comprobar coherencia técnica;
- detectar riesgos;
- verificar evidencia;
- facilitar feedback;
- apoyar decisiones de integración.

La revisión debe aportar juicio técnico.

No debe reducirse a una aprobación mecánica.

---

## 3. Scope

El alcance puede incluir:

```text
Review criteria
Ownership
Approval guidance
Review checklist
CODEOWNERS
Change risk evaluation
Feedback expectations
```

La profundidad dependerá de:

- project type;
- collaboration model;
- maturity;
- risk;
- número de maintainers.

---

## 4. Out of Scope

`WCL-CODE-REVIEW` no es responsable de:

- estructurar la Pull Request;
- ejecutar CI;
- definir branch strategy;
- gestionar Issues;
- implementar releases;
- decidir automáticamente si un cambio es correcto;
- sustituir pruebas;
- sustituir análisis de seguridad especializado.

Estas responsabilidades pertenecen a otros Components o al contexto del consumidor.

---

## 5. Materialization

La materialización Core combina:

```text
Convention
+
Configuration
```

Estructura potencial:

```text
code-review/
├── README.md
├── metadata.yml
└── templates/
    └── CODEOWNERS
```

`README.md` define los criterios y responsabilidades de revisión.

`CODEOWNERS` puede proporcionar ownership automático cuando resulte útil.

Por tanto:

```text
WCL-CODE-REVIEW
        ≠
CODEOWNERS
```

`CODEOWNERS` constituye una posible materialización parcial.

---

## 6. Review Principles

Una revisión DEBERÍA favorecer:

- comprensión del cambio;
- revisión del propósito antes del detalle;
- detección de duplicación;
- coherencia arquitectónica;
- simplicidad;
- mantenibilidad;
- testability;
- seguridad cuando corresponda;
- documentación suficiente;
- feedback accionable.

La revisión no debería centrarse únicamente en:

- formato;
- preferencias personales;
- estilo sin impacto;
- diferencias cosméticas ya cubiertas por herramientas automáticas.

---

## 7. Review Areas

Según el cambio podrán revisarse áreas como:

```text
Correctness
Architecture
Naming
Complexity
Tests
Documentation
Security
Dependencies
Backward Compatibility
Operational Impact
```

No todas las áreas son aplicables a todas las Pull Requests.

El reviewer debe aplicar juicio contextual.

---

## 8. Correctness

La revisión DEBERÍA comprobar si el cambio:

- satisface el objetivo;
- introduce comportamiento incorrecto;
- omite casos relevantes;
- rompe comportamiento existente;
- introduce inconsistencias.

Cuando exista una Issue relacionada, la revisión puede utilizarla como contexto.

---

## 9. Architecture

Los cambios con impacto arquitectónico DEBERÍAN evaluarse respecto a:

- responsabilidades existentes;
- layering;
- coupling;
- duplication;
- extensibility;
- canonical patterns;
- ADR cuando corresponda.

La revisión no debe exigir abstracciones adicionales sin necesidad demostrada.

---

## 10. Simplicity

Se favorecerá:

```text
Simple
    >
Clever
```

cuando ambas soluciones satisfagan correctamente la responsabilidad.

La revisión DEBERÍA detectar:

- complejidad accidental;
- generalización prematura;
- duplicación;
- abstracciones innecesarias;
- configuración excesiva.

---

## 11. Testing

Cuando el cambio requiera pruebas, la revisión DEBERÍA comprobar:

- existencia de tests adecuados;
- coherencia con la estrategia de testing;
- casos relevantes;
- evidencia de ejecución;
- ausencia de tests puramente cosméticos.

La revisión de testing puede complementarse con:

```text
DOC-TESTING
WCL-CI
```

cuando estén aplicables.

---

## 12. Documentation

La revisión DEBERÍA comprobar si el cambio requiere actualizar:

- README;
- Architecture;
- API documentation;
- Project Status;
- Changelog;
- Standards;
- Repository Templates;
- Component Catalog.

No todos los cambios requieren documentación.

Debe actualizarse cuando el comportamiento, contrato o estado del proyecto cambien de forma relevante.

---

## 13. Security

Cuando exista riesgo de seguridad, la revisión DEBERÍA considerar:

- permisos;
- secrets;
- dependency changes;
- input validation;
- authentication;
- authorization;
- exposure of information;
- external actions;
- supply chain.

Los cambios de seguridad relevantes pueden requerir revisión adicional especializada.

---

## 14. Feedback

El feedback DEBERÍA ser:

- específico;
- comprensible;
- accionable;
- relacionado con el cambio;
- proporcional al impacto.

Se debería distinguir entre:

```text
Required Change
Suggestion
Question
Optional Improvement
```

cuando ello facilite comprensión.

---

## 15. Approval

Una aprobación representa que el reviewer considera que el cambio puede integrarse dentro del scope evaluado.

No implica garantía absoluta.

El número de approvals dependerá del consumidor.

GitHub Framework no establece mediante este Component una cantidad universal de reviewers.

---

## 16. Ownership

El ownership permite identificar responsables naturales de determinadas áreas.

Puede utilizarse para:

- solicitar reviewers;
- distribuir responsabilidad;
- reducir cambios sin supervisión adecuada;
- clarificar mantenimiento.

La definición concreta del ownership pertenece al consumidor.

---

## 17. CODEOWNERS

GitHub permite materializar ownership mediante:

```text
.github/CODEOWNERS
```

El Component puede proporcionar un artefacto reusable como punto de partida:

```text
templates/CODEOWNERS
```

Sin embargo, los owners concretos son necesariamente información del consumidor.

Por tanto, un Template reusable NO DEBE incluir:

- usernames reales;
- teams reales;
- organizaciones específicas;
- rutas inexistentes presentadas como universales.

---

## 18. Canonical CODEOWNERS Strategy

El artefacto Core debe actuar como estructura reusable.

Ejemplo conceptual:

```text
* @OWNER

/docs/ @DOCS_OWNER
/.github/ @MAINTAINER
```

Los placeholders deberán sustituirse durante la adopción.

El artefacto no deberá presentarse directamente como configuración final del consumidor.

---

## 19. Pull Request Relationship

`WCL-CODE-REVIEW` se utiliza habitualmente junto a:

```text
WCL-PULL-REQUEST
```

Modelo:

```text
Pull Request
    ↓
Review Context
    ↓
Code Review
```

Pero ambas responsabilidades permanecen separadas.

`WCL-PULL-REQUEST` estructura el cambio.

`WCL-CODE-REVIEW` establece cómo evaluarlo.

---

## 20. CI Relationship

La revisión humana puede complementarse con validación automática.

```text
Human Review
        +
Automated Validation
        ↓
Higher Confidence
```

CI no sustituye juicio técnico.

Code Review tampoco debería repetir controles que la automatización ya puede verificar de forma fiable.

---

## 21. Adoption

La adopción puede consistir en:

- aplicar los criterios de revisión;
- configurar CODEOWNERS;
- definir approval rules;
- integrar branch protection;
- adaptar checklists;
- establecer reviewers.

No todos estos mecanismos son obligatorios.

La materialización debe ser proporcional al contexto del consumidor.

---

## 22. Small or Solo Projects

Un proyecto individual puede adoptar `WCL-CODE-REVIEW` sin mantener un proceso formal de múltiples reviewers.

En ese contexto puede materializarse mediante:

- self-review;
- Pull Request review before merge;
- checklist;
- diff inspection;
- automated validation.

Por tanto:

```text
Code Review
        ≠
Multiple Maintainers
```

---

## 23. Repository Template Integration

Un Repository Template puede declarar `WCL-CODE-REVIEW` como:

```text
required
recommended
optional
```

La selección dependerá del tipo de repositorio y sus necesidades.

El requirement level no pertenece al Component.

---

## 24. Validation

Una adopción DEBERÍA verificar:

- criterios de revisión comprensibles;
- ownership válido cuando se utilice;
- ausencia de owners inexistentes;
- ausencia de reglas que bloqueen innecesariamente el flujo;
- coherencia con Pull Requests;
- coherencia con branch protection;
- separación entre revisión humana y controles automáticos;
- proporcionalidad respecto al proyecto.

---

## 25. Dogfooding

GitHub Framework utiliza:

```text
.github/CODEOWNERS
```

junto con Pull Requests y revisión manual.

Esta práctica proporciona evidencia inicial para extraer el Component reusable.

El proceso deberá distinguir:

```text
Framework-specific ownership
        ≠
Canonical reusable ownership structure
```

La implementación canónica no debe incluir identidad específica del propio Framework.

---

## 26. Evolution

`WCL-CODE-REVIEW` puede evolucionar para incorporar:

- review checklists reutilizables;
- risk-based review;
- CODEOWNERS variants;
- branch protection guidance;
- automated reviewer assignment;
- policy validation.

Estas capacidades deberán añadirse solo cuando exista evidencia de necesidad reusable.

---

## 27. Related Components

| Component | Relationship |
| --- | --- |
| `WCL-PULL-REQUEST` | Contexto principal de revisión |
| `WCL-BRANCH` | Integración y protección |
| `WCL-COMMIT` | Historial evaluado |
| `WCL-CI` | Validación automática |
| `WCL-SECURITY` | Revisión de seguridad |
| `WCL-DOCUMENTATION-UPDATE` | Comprobación documental |

---

## 28. Related Documentation

- `docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md`
- `docs/design-system/09_COMPONENT_CATALOG.md`
- `docs/standards/07_GITHUB_REPOSITORY_STANDARDS.md`
- `.github/CODEOWNERS`
- `.github/PULL_REQUEST_TEMPLATE.md`

---

## 29. Status

```text
ID: WCL-CODE-REVIEW
Family: Workflow
Status: Implemented
Primary Materialization: Convention / Configuration
Validation: Pending Reference Implementation
```
