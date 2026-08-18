# Repository Template Reference Implementation

| Field | Value |
|---|---|
| **Project** | GitHub Framework |
| **Document** | Repository Template Reference Implementation |
| **Template** | `TPL-DOCUMENTATION` |
| **Template Version** | `0.1.0` |
| **Status** | Validated |
| **Validation Method** | Dogfooding |

---

## 1. Propósito

Este documento registra la primera Reference Implementation de la Repository Template Library de GitHub Framework.

La validación utiliza el propio repositorio **GitHub Framework** como implementación real de:

```text
TPL-DOCUMENTATION
```

El objetivo no es adaptar artificialmente el repositorio al Template.

El objetivo es comprobar si la composición definida por `TPL-DOCUMENTATION` representa adecuadamente las necesidades de un repositorio documental real y utilizar los resultados para refinar el Framework.

---

## 2. Alcance

La Reference Implementation valida:

- composición del Repository Template;
- requirement levels;
- disponibilidad de Components;
- relación entre README Components y Documentation Components;
- arquitectura documental;
- personalización;
- omisiones justificadas;
- gaps del repositorio consumidor;
- posibles defectos del Template.

Quedan fuera de esta validación:

- generación automática;
- CLI;
- schema validation;
- migraciones;
- Template inheritance.

---

## 3. Repository Template

Template validado:

```text
TPL-DOCUMENTATION
```

Características:

```text
family: Repository
version: 0.1.0
status: Experimental
project_type: Documentation
maturity: L2
```

GitHub Framework constituye un candidato adecuado porque la documentación, los estándares, los Components y las especificaciones forman parte principal del producto mantenido por el repositorio.

---

## 4. Método de Validación

La validación sigue este flujo:

```text
TPL-DOCUMENTATION
        │
        ▼
GitHub Framework
        │
        ▼
Conformance Analysis
        │
        ├── Template satisfied
        ├── Consumer gap
        └── Template flaw
```

Un gap no implica automáticamente que el repositorio deba modificarse.

Cada desviación deberá clasificarse antes de realizar cambios.

---

### Disponibilidad vs Conformidad

La disponibilidad de un Framework Component y la satisfacción de una responsabilidad por parte del repositorio consumidor son dimensiones diferentes.

```text
Framework Component availability
              ≠
Consumer requirement satisfaction
```

Un Component puede permanecer clasificado como `Conceptual` dentro del Framework mientras un repositorio real satisface correctamente esa responsabilidad mediante una implementación propia o equivalente.

La Reference Implementation evalúa por tanto dos dimensiones:

```text
Component availability
        +
Consumer conformance
```

La ausencia de una implementación reutilizable del Component no implica automáticamente una falta de conformidad del consumer.

---

## 5. Required Components

| Component | Framework Availability | Consumer Evidence | Conformance | Assessment |
|---|---|---|---|---|
| `README-HERO` | Implemented | `README.md` | ✅ | Conforme |
| `README-STATUS` | Implemented | `README.md` | ✅ | Conforme |
| `README-OVERVIEW` | Implemented | `README.md` | ✅ | Conforme |
| `README-DOCUMENTATION` | Implemented | `README.md` | ✅ | Conforme |
| `README-LICENSE` | Conceptual | `README.md` + `LICENSE` | ✅ | Responsabilidad satisfecha mediante implementación propia |
| `README-FOOTER` | Implemented | `README.md` | ✅ | Conforme |
| `DOC-ARCHITECTURE` | Implemented | `08_REPOSITORY_DESIGN_SYSTEM.md` + `09_COMPONENT_CATALOG.md` | ✅ | Specialized / Distributed |
| `DOC-PROJECT-STATUS` | Implemented | `docs/governance/12_PROJECT_STATUS.md` | ✅ | Conforme |
| `DOC-CHANGELOG` | Implemented | `CHANGELOG.md` | ✅ | Conforme |

---

## 6. README Components

### README-HERO

El README identifica claramente GitHub Framework y comunica su propuesta principal.

Resultado:

```text
Conforme
```

### README-STATUS

La sección `Project Status` refleja el estado actual del proyecto y se encuentra sincronizada con la versión publicada y el milestone activo.

Resultado:

```text
Conforme
```

### README-OVERVIEW

El README explica:

- qué es GitHub Framework;
- qué problema aborda;
- qué principios aplica;
- cuál es su objetivo.

Resultado:

```text
Conforme
```

### README-DOCUMENTATION

El README proporciona acceso explícito a:

```text
docs/
architecture/
standards/
design-system/
implementation/
governance/
```

Resultado:

```text
Conforme
```

### README-LICENSE

La licencia MIT está visible desde el README y existe un archivo `LICENSE` en la raíz.

El Framework Component `README-LICENSE` permanece actualmente clasificado como `Conceptual`, pero GitHub Framework satisface la responsabilidad mediante su implementación propia.

Clasificación:

```text
Framework availability: Conceptual
Consumer requirement: Satisfied
```

Resultado:

```text
Conforme
```

Este caso demuestra que la disponibilidad material de un Framework Component y la conformidad de un consumer deben evaluarse de forma independiente.

### README-FOOTER

El README dispone de cierre explícito.

Resultado:

```text
Conforme
```

---

## 7. Documentation Components

### DOC-ARCHITECTURE

GitHub Framework implementa `DOC-ARCHITECTURE` mediante una adopción especializada y distribuida.

La responsabilidad arquitectónica se encuentra principalmente en:

```text
docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md
docs/design-system/09_COMPONENT_CATALOG.md
```

El Repository Design System define la arquitectura general, capas, principios, componentes, documentación y reglas de composición del Framework.

El Component Catalog materializa el vocabulario, familias, relaciones, dependencias y registro de los elementos reutilizables.

Ambos documentos actúan conjuntamente como implementación de la responsabilidad definida por `DOC-ARCHITECTURE`.

Clasificación:

```text
Component satisfied
Adoption: Specialized / Distributed
```

No se crea un documento arquitectónico adicional porque duplicaría responsabilidades ya cubiertas por documentos existentes.

La Reference Implementation valida la responsabilidad conceptual del Component y no exige reproducir literalmente su `template.md`.

### DOC-PROJECT-STATUS

Existe:

```text
docs/governance/12_PROJECT_STATUS.md
```

La estructura satisface la responsabilidad del Component y su contenido se encuentra sincronizado con el estado actual de Sprint 6.

Clasificación:

```text
Conforme
```

### DOC-CHANGELOG

Existe:

```text
CHANGELOG.md
```

El documento mantiene historial versionado y sección `Unreleased`.

Clasificación:

```text
Conforme
```

---

## 8. Recommended Components

La ausencia de un Component `recommended` no invalida la implementación.

| Component | Framework Availability | Current Evidence | Assessment |
|---|---|---|---|
| `README-ROADMAP` | Implemented | `README.md` + `ROADMAP.md` | Conforme |
| `README-REPOSITORY-STRUCTURE` | Conceptual | No identificado como sección explícita | Omitido |
| `DOC-ADR` | Conceptual | No existe instancia específica | Omitido |
| `DOC-ROADMAP` | Conceptual | `ROADMAP.md` | Conforme conceptualmente |
| `DOC-GLOSSARY` | Conceptual | No existe instancia específica | Omitido |
| `DOC-DIAGRAMS` | Conceptual | Diagramas distribuidos en documentación | Parcial |
| `DOC-REFERENCES` | Implemented | Referencias distribuidas | Omitido como documento independiente |

Las omisiones deberán evaluarse por necesidad real y no incorporarse únicamente para maximizar conformidad.

---

## 9. Optional Components

| Component | Framework Availability | Current Evidence | Assessment |
|---|---|---|---|
| `README-CONTRIBUTING` | Conceptual | `README.md` + `CONTRIBUTING.md` | Presente mediante implementación propia |
| `README-AUTHOR` | Implemented | No requerido | Omitido |
| `README-HIGHLIGHTS` | Conceptual | No requerido | Omitido |
| `DOC-TESTING` | Conceptual | No requerido actualmente | Omitido |
| `DOC-SECURITY` | Conceptual | No requerido actualmente | Omitido |

La ausencia de estos Components no afecta al contrato mínimo de `TPL-DOCUMENTATION`.

---

## 10. Dogfooding Findings

### Finding 1 — README-STATUS

La implementación real demuestra que el estado resumido del proyecto forma parte natural del punto de entrada de un repositorio documental mantenido.

Decisión:

```text
README-STATUS
→ Required
```

### Finding 2 — README-LICENSE

La implementación real demuestra que un repositorio documental público mantenido necesita hacer visible su licencia.

Decisión:

```text
README-LICENSE
→ Required
```

### Finding 3 — DOC-REFERENCES

GitHub Framework mantiene referencias dentro de los documentos que las necesitan sin requerir una instancia independiente.

Decisión:

```text
DOC-REFERENCES
Required → Recommended
```

### Finding 4 — Optional Physical Template

Los Core Repository Templates implementados no necesitan actualmente artefactos físicos específicos.

Decisión:

```text
template/
→ optional
```

No deberán crearse directorios vacíos para satisfacer una convención.

### Finding 5 — Maturity Is Not a Template

La implementación demuestra que la madurez funciona como propiedad del Repository Template:

```text
TPL-DOCUMENTATION
maturity: L2
```

No resulta necesario modelar:

```text
TPL-DOCUMENTATION + TPL-L2
```

La documentación arquitectónica anterior que represente los niveles de madurez como Templates deberá sincronizarse con el modelo implementado.

### Finding 6 — Component Availability vs Consumer Conformance

La Reference Implementation demuestra que la disponibilidad de un Framework Component no determina por sí sola la conformidad de un repositorio consumidor.

Casos observados:

```text
README-LICENSE
Framework → Conceptual
Consumer  → Satisfied

DOC-ROADMAP
Framework → Conceptual
Consumer  → Satisfied conceptually

README-CONTRIBUTING
Framework → Conceptual
Consumer  → Present
```

Decisión:

```text
Component availability
≠
Consumer conformance
```

Los Repository Templates definen responsabilidades y requirement levels.

La conformidad deberá evaluarse por la satisfacción efectiva de esas responsabilidades, mientras que `Implemented / Conceptual` describe la disponibilidad de implementaciones reutilizables dentro del Framework.

---

# 11. Consumer Gaps

Los consumer gaps detectados durante el dogfooding han sido resueltos.

### Gap 1 — README status/version synchronization

Estado:

```text
Resolved
```

El README principal ha sido sincronizado con el estado actual del proyecto:

- versión publicada actual: `v0.3.0`;
- milestone actual: `v0.4.0` — Repository Templates;
- evolución del Framework descrita mediante implementación incremental, validación y dogfooding.

La versión española del README se ha sincronizado con el mismo estado.

### Gap 2 — PROJECT_STATUS synchronization

Estado:

```text
Resolved
```

`docs/governance/12_PROJECT_STATUS.md` ha sido actualizado para reflejar:

- Sprint 6 — Repository Templates;
- Repository Template Architecture completada;
- Core Repository Templates implementados;
- Reference Implementation en validación;
- Component Catalog sincronizado con las implementaciones físicas;
- `v0.4.0 — Repository Templates` como próximo hito.

Resultado:

```text
Consumer gaps
      ↓
0 unresolved
```

---

## 12. Template Gaps

El dogfooding detectó los siguientes Template gaps, posteriormente corregidos durante la evolución de `TPL-DOCUMENTATION`:

```text
README-STATUS requirement level
README-LICENSE requirement level
DOC-REFERENCES requirement level
template/ physical structure requirement
```

Estos findings refinan `TPL-DOCUMENTATION` y la Repository Template Architecture.

Adicionalmente, la validación ha producido un refinamiento semántico transversal:

```text
Component availability
≠
Consumer conformance
```

Este refinamiento no modifica la composición de `TPL-DOCUMENTATION`, pero clarifica cómo debe evaluarse la conformidad de cualquier Repository Template frente a un repositorio consumidor.

---

## 13. Conformance Status

Estado:

```text
CONFORMANT
```

La Reference Implementation alcanza conformidad estructural con `TPL-DOCUMENTATION`.

Razones:

- las 9 responsabilidades `required` están identificadas y satisfechas por el consumer;
- `README-LICENSE` demuestra conformidad mediante implementación propia aunque su Framework Component permanezca `Conceptual`;
- los consumer gaps detectados durante el dogfooding han sido resueltos;
- la composición del Template ha sido contrastada con las implementaciones físicas reales;
- el Component Catalog y la Repository Template Library han sido sincronizados con los findings de la validación.

```text
TPL-DOCUMENTATION
        ↓
Required Responsibilities
        ↓
9 / 9 satisfied
        ↓
Structural Conformance ✅
        ↓
CONFORMANT
```

Importante: **`CONFORMANT` no significa que `TPL-DOCUMENTATION` pase a `Stable`**. Solo significa que este consumer satisface su contrato.


---

## 14. Próximos Pasos

1. Formalizar Repository Template Standards (#14).
2. Ejecutar la validación final del Sprint 6.
3. Incorporar los findings de la Reference Implementation a la evolución futura del Framework cuando corresponda.
4. Preparar el cierre de `v0.4.0 — Repository Templates`.

---

## 15. Criterio de Finalización

La Reference Implementation estará completada cuando:

- [x] todos los gaps del Template estén resueltos o documentados;
- [x] todas las responsabilidades `required` estén satisfechas por el consumer;
- [x] la documentación arquitectónica esté sincronizada;
- [x] la documentación de gobierno relevante esté sincronizada;
- [x] el resultado del dogfooding esté documentado;
- [ ] la validación final del Sprint esté completada.

---

## 16. Estado

```text
Status: Validated
```

La Reference Implementation ha sido validada mediante dogfooding sobre el propio repositorio GitHub Framework.

La validación confirma la conformidad estructural del consumer con `TPL-DOCUMENTATION` y ha producido refinamientos incorporados a la Repository Template Architecture, al Component Catalog y a la Repository Template Library.

La validación final del Sprint permanece como actividad independiente del cierre de esta Reference Implementation.