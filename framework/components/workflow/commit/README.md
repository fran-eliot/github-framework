# WCL-COMMIT

## Component Metadata

| Field | Value |
| --- | --- |
| **ID** | `WCL-COMMIT` |
| **Family** | Workflow |
| **Type** | Framework Component |
| **Status** | Implemented |
| **Primary Materialization** | Convention |
| **Lifecycle** | Experimental |

---

## 1. Purpose

`WCL-COMMIT` define la responsabilidad reusable para crear commits comprensibles, trazables y mantenibles.

Su objetivo consiste en proporcionar una convención suficientemente clara para que el historial Git comunique la evolución del proyecto sin imponer complejidad innecesaria.

```text
Change
    ↓
Commit
    ↓
Repository History
    ↓
Review / Traceability
```

Un commit debe representar una unidad coherente de cambio.

---

## 2. Responsibility

`WCL-COMMIT` es responsable de proporcionar criterios reutilizables para:

- estructura de mensajes;
- propósito del commit;
- granularidad;
- legibilidad;
- trazabilidad;
- consistencia;
- relación con el workflow del repositorio.

---

## 3. Scope

El alcance incluye:

```text
Commit purpose
Commit message structure
Commit types
Commit scope
Commit granularity
Traceability
Repository history
```

La implementación Core utiliza una convención inspirada en Conventional Commits sin exigir necesariamente toda su especificación.

---

## 4. Out of Scope

`WCL-COMMIT` no es responsable de:

- definir branch strategy;
- estructurar Pull Requests;
- establecer code review;
- ejecutar CI;
- definir release strategy;
- imponer una herramienta concreta;
- determinar automáticamente la granularidad correcta de cada cambio.

Estas responsabilidades pertenecen a otros Components o al consumidor.

---

## 5. Materialization

`WCL-COMMIT` se materializa principalmente mediante:

```text
Convention
```

Su definición canónica está formada por:

```text
README.md
    +
metadata.yml
```

No necesita un template físico para considerarse implementado.

```text
Implemented
        ≠
Template Required
```

---

## 6. Core Principle

Un commit DEBERÍA representar una unidad coherente de cambio.

Principio:

```text
One coherent purpose
        ↓
One understandable commit
```

Esto no implica que cada archivo o modificación deba producir un commit independiente.

La granularidad debe favorecer comprensión y mantenimiento.

---

## 7. Commit Message Structure

La forma recomendada es:

```text
<type>(<scope>): <description>
```

El `scope` es opcional:

```text
<type>: <description>
```

Ejemplos:

```text
feat(workflows): add issue component

docs: update repository standards

fix(templates): correct component reference
```

---

## 8. Type

El `type` comunica la naturaleza principal del cambio.

Tipos Core recomendados:

```text
feat
fix
docs
refactor
test
chore
```

El consumidor PUEDE utilizar tipos adicionales cuando aporten significado real.

No deberían añadirse categorías únicamente para aumentar precisión aparente.

---

## 9. `feat`

Utilizar:

```text
feat
```

para cambios que introducen una nueva capacidad o comportamiento relevante.

Ejemplo:

```text
feat(workflows): add pull request component
```

---

## 10. `fix`

Utilizar:

```text
fix
```

para correcciones de comportamiento o defectos.

Ejemplo:

```text
fix(catalog): correct component status
```

---

## 11. `docs`

Utilizar:

```text
docs
```

para cambios exclusivamente documentales.

Ejemplo:

```text
docs: update contribution guidelines
```

Si el cambio documental forma parte inseparable de una nueva feature, no es necesario crear un commit `docs` separado únicamente para clasificar archivos.

---

## 12. `refactor`

Utilizar:

```text
refactor
```

cuando se modifica la estructura interna sin introducir intencionadamente una nueva capacidad ni corregir un defecto observable.

Ejemplo:

```text
refactor(templates): simplify repository composition
```

---

## 13. `test`

Utilizar:

```text
test
```

para cambios centrados en pruebas.

Ejemplo:

```text
test(validation): add metadata checks
```

No es obligatorio separar tests del cambio funcional cuando forman parte de la misma unidad coherente.

---

## 14. `chore`

Utilizar:

```text
chore
```

para mantenimiento que no encaje mejor en otro tipo.

Ejemplos:

```text
chore: prepare release

chore(deps): update development dependency
```

`chore` no debería convertirse en una categoría genérica para evitar clasificar correctamente los cambios.

---

## 15. Scope

El scope PUEDE utilizarse para identificar el área principal afectada.

Ejemplos:

```text
workflows
templates
catalog
docs
release
```

El scope debe:

- aportar contexto;
- mantenerse breve;
- representar una responsabilidad reconocible;
- evitar granularidad innecesaria.

No es obligatorio.

---

## 16. Description

La descripción DEBERÍA:

- comenzar de forma concisa;
- describir el cambio;
- evitar información redundante;
- ser comprensible sin inspeccionar inmediatamente el diff;
- evitar mensajes genéricos.

Ejemplos recomendados:

```text
feat(workflows): add core workflow components

fix(catalog): align workflow component status
```

Ejemplos no recomendados:

```text
update files

changes

fix stuff

work
```

---

## 17. Imperative Style

Cuando resulte natural, la descripción PUEDE utilizar estilo imperativo:

```text
add
update
remove
fix
refactor
```

Ejemplo:

```text
feat(workflows): add branch component
```

La consistencia es más importante que imponer reglas lingüísticas innecesariamente estrictas.

---

## 18. Commit Granularity

Los commits DEBERÍAN ser suficientemente pequeños para comprenderse y suficientemente completos para representar una unidad coherente.

Debe evitarse:

```text
Unrelated changes
        ↓
Single commit
```

pero también:

```text
Artificial fragmentation
        ↓
Many meaningless commits
```

El objetivo es producir un historial útil.

---

## 19. Atomicity

Un commit PUEDE considerarse suficientemente atómico cuando:

- representa un propósito identificable;
- no mezcla cambios independientes sin necesidad;
- mantiene coherencia interna;
- puede revisarse razonablemente;
- deja el repositorio en un estado válido cuando sea viable.

Atomicidad no significa necesariamente modificar un único archivo.

---

## 20. Temporary Commits

Durante desarrollo local pueden existir commits provisionales.

Ejemplos:

```text
WIP
checkpoint
experiment
```

Antes de integrar una rama, el consumidor PUEDE:

- squash;
- rebase;
- reorganizar;
- conservarlos;

según su estrategia de integración.

`WCL-COMMIT` no prescribe una política universal.

---

## 21. Traceability

Cuando resulte útil, un commit PUEDE mantener referencias hacia:

```text
Issue
Pull Request
ADR
Release
```

La trazabilidad no debería convertir el subject en una colección de identificadores.

La Pull Request puede proporcionar contexto adicional.

---

## 22. Breaking Changes

Los proyectos que necesiten identificar breaking changes PUEDEN utilizar convenciones compatibles con Conventional Commits.

Ejemplo:

```text
feat(api)!: change authentication contract
```

o información adicional en el cuerpo del commit.

Esta capacidad no es necesaria para todos los consumidores.

---

## 23. Commit Body

Un commit PUEDE incluir body cuando el subject no proporcione contexto suficiente.

El body puede explicar:

- motivación;
- decisiones relevantes;
- consecuencias;
- restricciones.

No debería duplicar información fácilmente visible en el diff.

---

## 24. Commit Footer

El footer PUEDE utilizarse para:

- referencias;
- breaking changes;
- metadata compatible con tooling.

Su uso depende de las necesidades del consumidor.

---

## 25. Composition

`WCL-COMMIT` se relaciona especialmente con:

```text
WCL-BRANCH
WCL-PULL-REQUEST
WCL-CODE-REVIEW
WCL-CI
WCL-RELEASE
DOC-CHANGELOG
```

Modelo:

```text
Branch
    ↓
Commit
    ↓
Pull Request
    ↓
Review
    ↓
Integration
```

Cada Component conserva su responsabilidad.

---

## 26. Pull Request Relationship

Los commits proporcionan el historial del cambio.

La Pull Request proporciona contexto de integración.

Por tanto:

```text
Commit Message
        ≠
Pull Request Description
```

No es necesario duplicar toda la información entre ambos mecanismos.

---

## 27. Release Relationship

Una convención consistente puede facilitar:

- generación de changelog;
- release notes;
- semantic versioning;
- clasificación automática de cambios.

Sin embargo, `WCL-COMMIT` no requiere automatización de releases.

---

## 28. Repository Template Integration

Un Repository Template puede declarar `WCL-COMMIT` como:

```text
required
recommended
optional
```

También puede especializar:

- tipos;
- scopes;
- referencias;
- reglas adicionales.

El requirement level pertenece al Template.

---

## 29. Adoption

Adoptar `WCL-COMMIT` consiste principalmente en establecer una convención explícita y aplicarla de forma consistente.

El consumidor DEBERÍA decidir:

```text
Message structure
Accepted types
Scope usage
Granularity expectations
Integration strategy
```

No necesita implementar tooling adicional.

---

## 30. Validation

La adopción puede validarse mediante:

- inspección del historial;
- revisión durante Pull Requests;
- commit hooks;
- CI;
- commit message linters.

La automatización es opcional.

La convención debe poder utilizarse correctamente incluso sin tooling adicional.

---

## 31. Dogfooding

GitHub Framework utiliza mensajes estructurados como:

```text
feat: ...
fix: ...
docs: ...
chore: ...
```

y variantes con scope cuando aportan contexto.

Esta práctica proporciona evidencia real para generalizar `WCL-COMMIT`.

```text
Existing Commit Practice
        ↓
Generalization
        ↓
Canonical Convention
        ↓
Framework Re-adoption
```

---

## 32. Portability

La convención se basa en Git y no depende de GitHub.

Por tanto:

```text
WCL-COMMIT
        ↓
High Portability
```

Puede adoptarse en repositorios alojados en distintos proveedores.

---

## 33. Evolution

`WCL-COMMIT` puede evolucionar para incorporar:

- commit linting;
- reusable configurations;
- hooks;
- release automation integration;
- changelog generation;
- specialized conventions.

Estas capacidades deberán incorporarse únicamente cuando exista una necesidad reusable.

---

## 34. Related Components

| Component | Relationship |
| --- | --- |
| `WCL-BRANCH` | Contexto del cambio |
| `WCL-PULL-REQUEST` | Integración |
| `WCL-CODE-REVIEW` | Revisión |
| `WCL-CI` | Validación automatizada |
| `WCL-RELEASE` | Clasificación para releases |
| `DOC-CHANGELOG` | Historial publicado cuando exista |

---

## 35. Related Documentation

- `docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md`
- `docs/design-system/09_COMPONENT_CATALOG.md`
- `docs/standards/07_GITHUB_REPOSITORY_STANDARDS.md`
- `docs/governance/15_WORKING_AGREEMENTS.md`

---

## 36. Status

```text
ID: WCL-COMMIT
Family: Workflow
Status: Implemented
Primary Materialization: Convention
Validation: Reference Implementation Validated
```
