# Documentation Components

La **Documentation Component Library** proporciona componentes reutilizables para construir documentación técnica consistente, mantenible y estructurada en repositorios GitHub.

Esta familia implementa los componentes `DOC-*` definidos por el **Repository Design System (RDS)** y registrados oficialmente en el **Component Catalog**.

---

## 1. Propósito

Los Documentation Components estandarizan documentos técnicos recurrentes para evitar que cada proyecto tenga que diseñar nuevamente las mismas estructuras documentales.

Cada componente representa una única responsabilidad documental y debe poder reutilizarse de forma independiente.

La biblioteca sigue los principios generales de GitHub Framework:

- simplicidad antes que complejidad;
- reutilización antes que duplicación;
- componentes antes que soluciones específicas;
- implementación antes que documentación innecesaria;
- evolución incremental mediante casos de uso reales.

---

## 2. Familia de Componentes

Los Documentation Components utilizan el siguiente prefijo:

```text
DOC-
```

Ejemplos:

```text
DOC-ARCHITECTURE
DOC-ADR
DOC-PROJECT-STATUS
DOC-CHANGELOG
```

Los identificadores son permanentes y se encuentran definidos en el Component Catalog.

Los directorios utilizan nombres en minúsculas y `kebab-case`.

Ejemplos:

```text
DOC-ARCHITECTURE   → architecture/
DOC-PROJECT-STATUS → project-status/
DOC-RELEASE-NOTES  → release-notes/
```

---

## 3. Ubicación

La Documentation Component Library se encuentra en:

```text
framework/components/documentation/
```

La estructura prevista es:

```text
documentation/
├── architecture/
├── adr/
├── roadmap/
├── project-status/
├── known-issues/
├── changelog/
├── release-notes/
├── api/
├── database/
├── deployment/
├── testing/
├── security/
├── diagrams/
├── glossary/
└── references/
```

Esta estructura refleja directamente los componentes `DOC-*` registrados oficialmente.

Las clasificaciones conceptuales como `Core`, `Architecture`, `Governance`, `Reference` o `Specialized` no generan niveles adicionales de directorios.

Estas clasificaciones pertenecen a la metadata del componente.

---

## 4. Contrato del Componente

Todos los Documentation Components siguen el mismo contrato base:

```text
component/
├── metadata.yml
├── README.md
├── template.md
└── example.md
```

`example.md` será opcional cuando el propio `template.md` sea suficientemente claro para comprender el uso del componente.

El objetivo es mantener una estructura uniforme sin introducir archivos que no aporten valor.

---

## 5. Responsabilidad de los Archivos

### `metadata.yml`

Contiene la metadata procesable por máquinas que describe el componente.

Permitirá que futuras herramientas puedan descubrir, validar, seleccionar o componer componentes sin necesidad de interpretar su documentación Markdown.

El contrato inicial contempla:

```yaml
id:
name:
family:
version:
status:
priority:
audience:
maturity:
description:
dependencies:
```

Solo se incorporarán nuevos campos cuando una necesidad real de implementación lo justifique.

---

### `README.md`

Contiene la especificación humana del componente.

Debe explicar, cuando resulte aplicable:

- propósito;
- responsabilidad;
- cuándo utilizarlo;
- cuándo no utilizarlo;
- estructura;
- reglas de personalización;
- dependencias;
- consideraciones de mantenimiento.

El README describe el componente reutilizable.

No debe describir una implementación específica de un proyecto concreto.

---

### `template.md`

Contiene la plantilla reutilizable del documento.

Es el artefacto destinado a ser utilizado por repositorios consumidores, Repository Templates y futuras herramientas de generación.

La información específica de cada proyecto deberá representarse mediante placeholders o instrucciones de personalización.

No debe contener información dependiente de un repositorio concreto.

---

### `example.md`

Contiene, cuando sea necesario, una implementación de referencia válida del componente.

Los ejemplos deberán:

- demostrar un uso realista;
- facilitar la comprensión del template;
- evitar dependencias innecesarias de proyectos concretos;
- mantenerse sincronizados con el componente.

No deberá existir un ejemplo cuando no aporte información adicional significativa.

---

## 6. Registro de Documentation Components

La familia inicial está formada por los siguientes componentes:

| Component | Directory | Classification |
|-----------|-----------|----------------|
| `DOC-ARCHITECTURE` | `architecture/` | Core / Architecture |
| `DOC-ADR` | `adr/` | Architecture |
| `DOC-ROADMAP` | `roadmap/` | Governance |
| `DOC-PROJECT-STATUS` | `project-status/` | Core / Governance |
| `DOC-KNOWN-ISSUES` | `known-issues/` | Governance |
| `DOC-CHANGELOG` | `changelog/` | Core / Governance |
| `DOC-RELEASE-NOTES` | `release-notes/` | Governance |
| `DOC-API` | `api/` | Specialized / Reference |
| `DOC-DATABASE` | `database/` | Specialized / Reference |
| `DOC-DEPLOYMENT` | `deployment/` | Specialized / Architecture |
| `DOC-TESTING` | `testing/` | Architecture |
| `DOC-SECURITY` | `security/` | Architecture |
| `DOC-DIAGRAMS` | `diagrams/` | Architecture |
| `DOC-GLOSSARY` | `glossary/` | Specialized / Reference |
| `DOC-REFERENCES` | `references/` | Core / Reference |

El **Component Catalog** continúa siendo la fuente de verdad para los identificadores, prioridad, audiencia, madurez y registro oficial de cada componente.

---

## 7. Clasificación

Los Documentation Components pueden pertenecer a una o varias clasificaciones conceptuales.

### Core

Componentes documentales fundamentales para repositorios estratégicos.

### Architecture

Componentes relacionados con arquitectura, diseño técnico e implementación.

### Governance

Componentes relacionados con gestión, evolución y mantenimiento del proyecto.

### Reference

Componentes destinados principalmente a proporcionar información de consulta.

### Specialized

Componentes necesarios únicamente para determinados tipos de proyecto o dominios.

Estas clasificaciones permiten seleccionar componentes sin introducir jerarquías innecesarias en el filesystem.

---

## 8. Reglas de Dependencias

Los Documentation Components deben permanecer desacoplados y ser reutilizables de forma independiente siempre que sea posible.

Toda dependencia deberá declararse explícitamente.

Las relaciones entre componentes deberán aumentar progresivamente el nivel de detalle documental.

Ejemplo:

```text
README-ARCHITECTURE
        ↓
README-DOCUMENTATION
        ↓
DOC-ARCHITECTURE
        ↓
DOC-ADR
```

Un Documentation Component no deberá depender de la implementación específica del README de un proyecto.

Las referencias entre documentos implementados en un repositorio utilizarán enlaces relativos.

---

## 9. Principios de Diseño

Todo Documentation Component deberá:

- tener una responsabilidad principal;
- resolver una necesidad documental recurrente;
- poder reutilizarse en distintos proyectos;
- evitar duplicar responsabilidades existentes;
- mantenerse comprensible de forma independiente;
- utilizar formatos abiertos y versionables;
- priorizar Markdown cuando sea suficiente;
- admitir evolución incremental;
- evitar dependencias específicas de un único proyecto.

Antes de crear un nuevo componente deberá comprobarse:

1. si ya existe un componente equivalente;
2. si puede ampliarse uno existente;
3. si la nueva responsabilidad es realmente independiente;
4. si existe un caso de uso reutilizable.

---

## 10. Ciclo de Vida

Los Documentation Components siguen el ciclo de vida general definido por GitHub Framework:

```text
Idea

↓

Specification

↓

Template

↓

Implementation

↓

Validation

↓

Reuse

↓

Maintenance
```

Un componente no deberá promoverse para reutilización general hasta haber sido validado mediante una implementación real.

---

## 11. Estados

Los componentes podrán utilizar los siguientes estados:

```text
Draft

Experimental

Stable

Deprecated

Retired
```

### Draft

El componente se encuentra en diseño o implementación inicial.

### Experimental

Existe una implementación funcional y está siendo validada mediante casos de uso reales.

### Stable

El componente ha sido validado y se recomienda para reutilización.

### Deprecated

El componente continúa disponible temporalmente, pero existe una alternativa recomendada.

### Retired

El componente ha sido retirado y no deberá utilizarse en nuevas implementaciones.

---

## 12. Quality Gates

Antes de considerar un Documentation Component preparado para reutilización deberá verificarse:

- [ ] Dispone de un identificador `DOC-*` único.
- [ ] Resuelve una responsabilidad documental claramente definida.
- [ ] Sigue el contrato estándar del componente.
- [ ] Su metadata está completa.
- [ ] Su template es reutilizable.
- [ ] Sus dependencias están declaradas.
- [ ] No duplica otro componente existente.
- [ ] Ha sido validado mediante una implementación real.
- [ ] Su documentación permite que otro maintainer pueda reutilizarlo.

---

## 13. Relación con README Components

Los README Components constituyen la capa de entrada al repositorio.

Los Documentation Components proporcionan niveles superiores de profundidad técnica y documental.

La relación seguirá el principio de **progressive disclosure**:

```text
README

↓

Documentation Entry Point

↓

Documentation Component

↓

Specialized Documentation
```

Los README Components deberán enlazar hacia la documentación detallada en lugar de duplicarla.

---

## 14. Single Source of Truth

Cada responsabilidad documental deberá disponer de una única especificación oficial.

El flujo será:

```text
RDS Specification

↓

Component Catalog

↓

Documentation Component

↓

Repository Template

↓

Project Implementation
```

Las implementaciones de proyectos podrán adaptar el contenido necesario, pero no redefinir el contrato del componente.

---

## 15. Evolución

Un nuevo Documentation Component solo deberá incorporarse cuando:

1. no exista un componente que resuelva la misma necesidad;
2. ampliar uno existente provocaría una mezcla de responsabilidades;
3. represente un patrón documental reutilizable;
4. exista al menos un caso de uso real que justifique su incorporación.

La finalidad de la biblioteca no es maximizar el número de componentes.

Su objetivo es mantener **el conjunto mínimo de componentes necesarios para construir sistemas documentales profesionales y reutilizables**.

---

## 16. Reference Implementation

GitHub Framework actúa como implementación de referencia de la Documentation Component Library.

La validación inicial de los Core Documentation Components utiliza las siguientes implementaciones:

| Component | Reference Implementation | Adoption |
| --------- | ------------------------ | -------- |
| `DOC-ARCHITECTURE` | `docs/design-system/08_REPOSITORY_DESIGN_SYSTEM.md` + `09_COMPONENT_CATALOG.md` | Specialized / Distributed |
| `DOC-PROJECT-STATUS` | `docs/governance/12_PROJECT_STATUS.md` | Direct |
| `DOC-CHANGELOG` | `CHANGELOG.md` | Direct |
| `DOC-REFERENCES` | — | Not instantiated |

`DOC-REFERENCES` pertenece al Core de la biblioteca, pero su prioridad `Recommended` no obliga a todos los repositorios a instanciarlo.

La implementación de referencia valida el contrato conceptual de los componentes, no la reproducción literal de sus templates.

Las especializaciones son válidas cuando preservan la responsabilidad del componente y evitan duplicación documental.

---

## 17. Documentation Writing Standards

La redacción y mantenimiento de los Documentation Components deberá seguir los estándares definidos en:

[`docs/standards/17_DOCUMENTATION_WRITING_STANDARDS.md`](../../../docs/standards/17_DOCUMENTATION_WRITING_STANDARDS.md)

Estos estándares definen, entre otros aspectos:

- política lingüística;
- estilo de redacción;
- jerarquía Markdown;
- uso de listas, tablas y checklists;
- enlaces;
- placeholders;
- Single Source of Truth;
- mantenimiento;
- Quality Gates documentales.

Los componentes individuales podrán añadir reglas específicas cuando su responsabilidad lo requiera, pero no deberán contradecir los estándares generales del Framework.

---

## 18. Estado Actual

La arquitectura de la Documentation Component Library está definida.

Los componentes individuales se implementarán progresivamente y serán validados mediante dogfooding sobre la documentación del propio GitHub Framework.

La implementación de componentes individuales pertenece a la siguiente etapa de desarrollo de la biblioteca.