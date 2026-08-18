# 08 - REPOSITORY DESIGN SYSTEM

| Field        | Value                          |
| ------------ | ------------------------------ |
| **Project**  | GitHub Framework               |
| **Document** | Repository Design System (RDS) |
| **Version**  | 1.1.0                          |
| **Status**   | Stable                         |
| **Owner**    | Fran Ramirez                   |

---

# 1. Purpose

El **Repository Design System (RDS)** define el modelo arquitectónico de GitHub Framework para construir, evolucionar y mantener repositorios mediante elementos reutilizables.

Su objetivo consiste en transformar la creación de repositorios desde una actividad artesanal hacia un proceso basado en:

- estándares;
- Framework Components;
- Repository Templates;
- Maturity Profiles;
- reglas de composición;
- validación;
- gobernanza.

El RDS complementa los estándares GRS.

Mientras los GRS definen criterios de calidad y evaluación, el RDS define cómo estructurar y reutilizar las capacidades necesarias para construir repositorios coherentes.

El sistema podrá aplicarse a distintos tipos de proyecto sin imponer una composición idéntica a todos ellos.

---

# 2. Vision

Todo repositorio que adopte GitHub Framework deberá poder reutilizar responsabilidades ya definidas por el sistema cuando resulten aplicables.

La creación de un nuevo proyecto no deberá comenzar necesariamente desde cero.

Cuando exista un Repository Template adecuado, este proporcionará una composición inicial de Framework Components.

El proyecto consumidor podrá adaptar esa composición según sus necesidades sin duplicar responsabilidades canónicas ni incorporar Components innecesarios.

---

# 3. Relationship with Other Standards

El RDS se apoya en los siguientes documentos.

| Document                       | Responsibility                     |
| ------------------------------ | ---------------------------------- |
| 01_BRAND                       | Identidad profesional              |
| 02_VISUAL_IDENTITY             | Lenguaje visual                    |
| 03_PORTFOLIO_ARCHITECTURE      | Arquitectura del portfolio         |
| 04_REPOSITORY_AUDIT            | Estado actual                      |
| 05_PROFILE_README_ARCHITECTURE | Arquitectura del README del perfil |
| 06_VISUAL_DESIGN_SYSTEM        | Sistema visual                     |
| 07_GITHUB_METADATA             | Estándares GRS                     |

El RDS reutiliza todos ellos.

No los sustituye.

---

# 4. Repository as a System

Un repositorio deja de considerarse únicamente un conjunto de archivos.

Pasa a entenderse como un sistema formado por responsabilidades relacionadas.

Ejemplo conceptual:

```text
Repository
    │
    ├── Metadata
    ├── README
    ├── Documentation
    ├── Workflows
    ├── Assets
    └── Governance
```

Estas responsabilidades podrán materializarse mediante uno o varios Framework Components.

Los Components encapsulan responsabilidades reutilizables.

Los Repository Templates determinan qué combinación resulta adecuada para cada tipo de proyecto.

---

# 5. Component Philosophy

Todo Framework Component deberá perseguir cuatro propiedades:

- reutilizable;
- suficientemente desacoplado;
- documentado;
- mantenible.

Un Component deberá representar una responsabilidad generalizable.

Podrá admitir parámetros, variantes o guidance contextual, pero su definición canónica no deberá depender innecesariamente de un único proyecto consumidor.

Cuando una necesidad sea exclusivamente específica de un proyecto y no exista evidencia de reutilización potencial, deberá permanecer en ese proyecto.

---

# 6. Design Principles

El Repository Design System seguirá los principios:

* composición frente a duplicación;
* consistencia frente a personalización excesiva;
* simplicidad frente a complejidad;
* evolución incremental;
* documentación como parte del diseño.

---

# 7. Single Source of Truth

Cada elemento reutilizable del RDS deberá disponer de una fuente canónica identificable.

Para los Framework Components implementados, la definición canónica estará formada por su especificación y metadata correspondientes.

El Component Catalog proporcionará descubrimiento y clasificación global sin sustituir esas definiciones.

Los Repository Templates mantendrán su composición canónica en sus propias especificaciones y metadata.

Las plantillas, ejemplos, documentación y Reference Implementations deberán derivarse de estas fuentes.

No deberán mantenerse definiciones paralelas incompatibles del mismo elemento.

---

# 8. Component Taxonomy

Los Framework Components podrán organizarse en familias según la responsabilidad que representan.

Las familias actualmente definidas por el RDS incluyen:

| Family | Responsibility |
|---|---|
| README Components | Presentación y navegación principal |
| Documentation Components | Documentación técnica y de gobierno |
| Workflow Components | Procesos de desarrollo y mantenimiento |
| Visual Components | Identidad y comunicación visual |
| Governance Components | Responsabilidades de gobierno reutilizables cuando exista implementación |

La existencia conceptual de una familia no implica que todos sus Components estén implementados físicamente.

El Component Catalog mantendrá la visión global de los Components reconocidos por el Framework.

---

# 9. Component Lifecycle

Los Framework Components seguirán el ciclo de vida definido por la gobernanza del RDS.

Conceptualmente:

```text
Idea
    ↓
Specification
    ↓
Implementation
    ↓
Validation
    ↓
Adoption
    ↓
Maintenance
    ↓
Deprecation
    ↓
Retirement
```

Un Component no se considerará suficientemente maduro para adopción general únicamente por disponer de una implementación.

Deberá existir evidencia de validación mediante uso real, Reference Implementation o dogfooding.

La definición detallada de estados y transiciones pertenece a la gobernanza del RDS.

---

# 10. Component Granularity

Los Framework Components deberán ser lo suficientemente pequeños para reutilizarse.

Ejemplos.

Correcto.

* Hero Section
* Quick Start
* Architecture Diagram
* Release Notes

Incorrecto.

* README completo
* Todo el repositorio
* Toda la documentación

---

# 11. Composition Model

Los Framework Components se combinan mediante composición.

Ejemplo conceptual:

```text
Hero
+
Tech Stack
+
Quick Start
+
Architecture
+
Roadmap
```

La composición no será completamente arbitraria.

Deberá respetar:

- la responsabilidad de cada Component;
- sus dependencias cuando existan;
- el Repository Template aplicable;
- las necesidades reales del proyecto consumidor.

No todos los proyectos utilizarán exactamente la misma combinación.

Los Repository Templates proporcionarán composiciones reutilizables sin impedir extensiones justificadas.

---

# 12. Component Requirement Levels

La necesidad de un Framework Component se evaluará dentro del contexto de cada Repository Template.

Los Repository Templates utilizarán tres requirement levels:

## Required

El Component forma parte del contrato mínimo del Template.

## Recommended

El Component aporta valor habitual, pero su necesidad depende del proyecto consumidor.

## Optional

El Component se incorpora únicamente cuando existe una necesidad concreta.

Por tanto:

```text
Component
+
Repository Template Context
        ↓
Requirement Level
```

Un mismo Component podrá tener requirement levels diferentes en Templates distintos.

El requirement level no modifica la prioridad, madurez o definición canónica del Component.

---

# 13. Component Independence

Cada Framework Component deberá poder evolucionar con el menor acoplamiento posible respecto al resto del sistema.

Ejemplo.

Modificar la sección "Quick Start" no deberá obligar a rediseñar el README completo.

---

# 14. Naming Convention

Los elementos reutilizables del RDS deberán utilizar nombres e identificadores estables y suficientemente descriptivos.

Cuando exista un identificador formal deberá seguir la convención definida para su familia.

Ejemplos:

```text
README-HERO
DOC-ARCHITECTURE
WCL-RELEASE
VCL-BANNER
TPL-BACKEND
```

Los nombres deberán representar responsabilidades y evitar ambigüedad.

Los identificadores existentes no deberán modificarse sin evaluar compatibilidad, consumidores y metadata asociada.

---

# 15. Versioning

Los Framework Components podrán mantener versionado independiente del repositorio y de la versión global de GitHub Framework.

Cuando un elemento sea versionable utilizará Semantic Versioning:

```text
Major.Minor.Patch
```

Los Repository Templates podrán mantener igualmente versionado independiente.

Una nueva versión del Framework no obliga automáticamente a modificar la versión de todos sus Components o Templates.

Los cambios incompatibles deberán reflejarse mediante el versionado correspondiente y seguir la política de compatibilidad definida por la gobernanza.

---

# 16. Machine-Readable Identifiers

Los elementos reutilizables del RDS utilizarán identificadores estables cuando necesiten ser referenciados por documentación, metadata, validadores o futuras automatizaciones.

Ejemplos:

```text
README-HERO
DOC-ARCHITECTURE
WCL-RELEASE
VCL-BANNER
TPL-BACKEND
```

Estos identificadores deberán corresponder con la definición canónica del elemento y no constituir una taxonomía paralela.

Las futuras capacidades de automatización deberán consumir estos identificadores y la metadata existente en lugar de introducir nuevos tokens equivalentes.

---

# 17. Documentation First

Todo Framework Component deberá disponer de documentación suficiente para comprender:

- su propósito;
- su responsabilidad;
- su alcance;
- sus límites;
- su forma de utilización.

Cuando corresponda, deberá incluir ejemplos, template o guidance de implementación.

La documentación forma parte de la definición del Component.

La Definition of Done general del RDS se mantiene en la sección de gobernanza.

---

# 18. Component Quality Attributes

Todo Framework Component deberá evaluarse según:

* claridad;
* reutilización;
* independencia;
* mantenibilidad;
* facilidad de comprensión;
* consistencia con el resto del sistema.

---

# 19. Component Consumers

Los Framework Components podrán utilizarse, según corresponda, en:

- repositorios backend;
- proyectos full stack;
- repositorios documentales;
- GitHub Profile;
- proyectos de aprendizaje cuando sus necesidades lo justifiquen;
- futuros tipos de repositorio soportados por el Framework.

No todos los Components serán aplicables a todos los consumidores.

La selección deberá realizarse mediante el Repository Template correspondiente o mediante una necesidad explícitamente justificada.

La madurez del consumidor podrá modificar las expectativas de calidad y mantenimiento, pero no constituye por sí misma un tipo de consumidor.

---

# 20. Repository Design Layers

El diseño completo de un repositorio se dividirá en capas.

```text
Brand Layer

↓

Metadata Layer

↓

Documentation Layer

↓

Engineering Layer

↓

Governance Layer
```

Cada capa agrupa componentes relacionados.

---

# 21. Backward Compatibility

Los cambios en un componente deberán mantener compatibilidad razonable con versiones anteriores.

Solo los cambios mayores justificarán modificaciones incompatibles.

---

# 22. Reuse Strategy

Antes de crear un componente nuevo deberá comprobarse:

* ¿Existe ya uno equivalente?
* ¿Puede ampliarse?
* ¿Puede parametrizarse?
* ¿Es realmente necesario?

El objetivo será minimizar duplicaciones.

---

# 23. Anti-Patterns

No deberán aparecer:

- Components duplicados;
- Repository Templates incompatibles para necesidades equivalentes;
- nombres inconsistentes;
- documentación repetida;
- definiciones canónicas paralelas;
- Components específicos de un único proyecto sin evidencia de reutilización;
- Components incorporados únicamente para aumentar cobertura;
- composiciones rígidas derivadas exclusivamente de la madurez.

---

# 24. Component Quality Gates

Antes de incorporar un Framework Component al RDS deberá verificarse:

- [ ] Tiene un propósito definido.
- [ ] Su responsabilidad y alcance están documentados.
- [ ] Existe evidencia de reutilización potencial.
- [ ] Está suficientemente desacoplado.
- [ ] Mantiene coherencia con el sistema.
- [ ] No duplica una responsabilidad existente.
- [ ] Su fuente canónica está identificada.
- [ ] Incluye guidance, ejemplo o template cuando corresponda.
- [ ] Puede validarse mediante implementación, Reference Implementation o dogfooding.

---

# 25. Long-Term Vision

El Repository Design System constituye el modelo arquitectónico sobre el que GitHub Framework desarrolla una biblioteca reutilizable para construir y evolucionar repositorios.

Su evolución deberá permitir:

- reducir el esfuerzo de creación;
- reutilizar responsabilidades ya resueltas;
- mantener consistencia;
- acelerar la documentación;
- facilitar la evolución de los repositorios;
- validar conformidad;
- soportar progresivamente automatización y generación asistida.

La evolución se realizará a partir de necesidades reales y de evidencia obtenida mediante consumidores, Reference Implementations y dogfooding.

---

# 26. Part 1 Conclusions

El **Repository Design System** proporciona los fundamentos arquitectónicos de GitHub Framework.

Los repositorios se entienden como sistemas formados por responsabilidades reutilizables.

Los Framework Components encapsulan esas responsabilidades.

Los Repository Templates las combinan según tipos de proyecto.

Los Maturity Profiles expresan expectativas de evolución y mantenimiento.

```text
Standards
        ↓
Framework Components
        ↓
Repository Templates
        ↓
Repository Implementations
        ↓
Validation and Evolution
```

El resultado es un sistema orientado a reutilización, consistencia y evolución incremental sin imponer la misma estructura o combinación de Components a todos los proyectos.

---

# 27. Part 1 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.

---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 2/7

# README Component Library

---

# 28. Purpose

La **README Component Library** define componentes reutilizables para construir la capa de presentación y navegación principal de los repositorios que adopten GitHub Framework.

Cada README Component representa una responsabilidad concreta.

Los Repository Templates podrán reutilizar estos Components para definir composiciones adecuadas a distintos tipos de proyecto.

El objetivo no consiste en eliminar toda personalización ni en imponer un README universal.

Consiste en evitar que responsabilidades recurrentes deban diseñarse nuevamente desde cero.

---

# 29. README Philosophy

Todo README deberá perseguir tres objetivos.

```text
Capture Attention

↓

Build Confidence

↓

Enable Action
```

El lector deberá:

* comprender el proyecto;
* confiar en su calidad;
* saber cómo utilizarlo.

---

# 30. Component Architecture

La arquitectura general será:

```text
Hero

↓

Overview

↓

Features

↓

Architecture

↓

Technology Stack

↓

Quick Start

↓

Documentation

↓

Roadmap

↓

Contributing

↓

License

↓

Footer
```

No todos los proyectos necesitarán todos los bloques.

---

# 31. Component Classification

Los README Components se clasifican principalmente por su responsabilidad.

Su necesidad dentro de un repositorio no se define mediante una clasificación global `Core`, `Extended` u `Optional`.

El requirement level pertenece al Repository Template que consume el Component.

Por tanto:

```text
README Component
        ↓
Canonical responsibility

Repository Template
        ↓
Required / Recommended / Optional
```

Un mismo README Component podrá ser `required` en un Template, `recommended` en otro y no formar parte de un tercero.

La prioridad y madurez canónicas del Component se mantienen separadas de su requirement level contextual.

---

# 32. README-HERO

## Identifier

```text
README-HERO
```

---

## Purpose

Presentar el proyecto en menos de cinco segundos.

---

## Contents

* Banner
* Nombre
* Tagline
* Badges principales

---

## Example

```text
Banner

NovaCoquinaria

Knowledge Engineering Platform

Badges
```

---

# 33. README-STATUS

## Identifier

```text
README-STATUS
```

---

## Purpose

Mostrar el estado del proyecto.

---

## Possible Values

```text
Active Development

Stable

Maintenance

Archived

Research
```

---

# 34. README-OVERVIEW

## Identifier

```text
README-OVERVIEW
```

---

## Purpose

Explicar el proyecto.

Debe responder:

```text
Why?

What?

Who?
```

Nunca:

How?

Eso pertenece al Quick Start.

---

## Recommended Length

200–500 palabras.

---

# 35. README-HIGHLIGHTS

## Identifier

```text
README-HIGHLIGHTS
```

---

## Purpose

Mostrar rápidamente las capacidades principales.

---

## Format

Lista breve.

Ejemplo.

```text
Documentation First

Knowledge Graph

Semantic Validation

MkDocs

Automation
```

---

# 36. README-FEATURES

## Identifier

```text
README-FEATURES
```

---

## Purpose

Describir funcionalidades.

No tecnologías.

---

## Example

```text
Recipe Knowledge Graph

Semantic Validation

Automation Pipeline

Documentation Website
```

---

# 37. README-ARCHITECTURE

## Identifier

```text
README-ARCHITECTURE
```

---

## Purpose

Explicar la arquitectura.

---

## Possible Contents

* diagrama;
* módulos;
* capas;
* flujo;
* ADR relacionados.

---

# 38. README-TECH-STACK

## Identifier

```text
README-TECH-STACK
```

---

## Purpose

Mostrar tecnologías.

---

## Preferred Style

Skill Icons.

No listas enormes.

---

## Example

```text
Java

Spring

Python

Docker

PostgreSQL
```

---

# 39. README-REPOSITORY-STRUCTURE

## Identifier

```text
README-REPOSITORY-STRUCTURE
```

---

## Purpose

Explicar la organización.

---

## Example

```text
docs/

assets/

src/

.github/
```

---

# 40. README-QUICK-START

## Identifier

```text
README-QUICK-START
```

---

## Purpose

Permitir comenzar rápidamente.

---

## Maximum Reading Time

Cinco minutos.

---

## Structure

```text
Requirements

↓

Installation

↓

Configuration

↓

Run
```

---

# 41. README-DOCUMENTATION

## Identifier

```text
README-DOCUMENTATION
```

---

## Purpose

Enlazar documentación extensa.

---

## Typical Links

* Architecture
* ADR
* API
* Roadmap
* Status

---

# 42. README-DEMO

## Identifier

```text
README-DEMO
```

---

## Purpose

Mostrar el proyecto funcionando.

---

## Possible Formats

* GIF
* vídeo
* GitHub Pages
* capturas

---

# 43. README-TESTING

## Identifier

```text
README-TESTING
```

---

## Purpose

Explicar estrategia de calidad.

---

## Example

```text
JUnit

PyTest

Coverage

CI
```

---

# 44. README-ROADMAP

## Identifier

```text
README-ROADMAP
```

---

## Purpose

Explicar evolución prevista.

No sustituye al ROADMAP.md.

---

# 45. README-CONTRIBUTING

## Identifier

```text
README-CONTRIBUTING
```

---

## Purpose

Explicar cómo colaborar.

Solo cuando el proyecto acepte contribuciones.

---

# 46. README-LICENSE

## Identifier

```text
README-LICENSE
```

---

## Purpose

Enlazar licencia.

Nunca reproducirla completa.

---

# 47. README-AUTHOR

## Identifier

```text
README-AUTHOR
```

---

## Purpose

Presentar el autor.

Muy breve.

Enlazará al GitHub Profile.

---

# 48. README-FOOTER

## Identifier

```text
README-FOOTER
```

---

## Purpose

Cerrar el documento.

Podrá incluir.

* agradecimientos;
* enlaces;
* navegación.

---

# 49. README Component Catalog

La README Component Library incluye actualmente los siguientes Components definidos por el RDS:

| Component | Identifier | Responsibility |
|---|---|---|
| Hero | `README-HERO` | Presentación inicial |
| Status | `README-STATUS` | Estado del proyecto |
| Overview | `README-OVERVIEW` | Propósito y contexto |
| Highlights | `README-HIGHLIGHTS` | Capacidades destacadas |
| Features | `README-FEATURES` | Funcionalidades principales |
| Architecture | `README-ARCHITECTURE` | Visión arquitectónica |
| Tech Stack | `README-TECH-STACK` | Tecnologías principales |
| Repository Structure | `README-REPOSITORY-STRUCTURE` | Organización del repositorio |
| Quick Start | `README-QUICK-START` | Primer uso |
| Documentation | `README-DOCUMENTATION` | Navegación documental |
| Demo | `README-DEMO` | Evidencia visual o funcional |
| Testing | `README-TESTING` | Estrategia de testing |
| Roadmap | `README-ROADMAP` | Evolución prevista |
| Contributing | `README-CONTRIBUTING` | Participación externa |
| License | `README-LICENSE` | Acceso a la licencia |
| Author | `README-AUTHOR` | Autoría |
| Footer | `README-FOOTER` | Cierre y navegación |

Esta tabla proporciona una vista funcional de la biblioteca.

La definición canónica de cada Component implementado pertenece a su especificación y metadata dentro del Framework.

Los requirement levels no se mantienen en esta matriz.

Se definen contextualmente en cada Repository Template.

---

# 50. Component Dependencies

Algunos README Components podrán mantener relaciones o dependencias con otros Components.

Estas relaciones deberán declararse únicamente cuando sean necesarias para cumplir su responsabilidad.

Ejemplo conceptual:

```text
README-DOCUMENTATION
        ↓
Project Documentation
```

Otros Components podrán ser independientes.

Ejemplo:

```text
README-HERO
```

Las dependencias reales deberán mantenerse en la definición canónica del Component cuando exista implementación.

No deberán inferirse únicamente por el orden visual del README.

---

# 51. Assembly Rules

Los README deberán construirse mediante composición de responsabilidades cuando exista un Repository Template aplicable.

La materialización de un README Component podrá adaptar:

- contenido;
- parámetros;
- enlaces;
- ejemplos;
- información específica del proyecto.

La adaptación no deberá alterar innecesariamente la responsabilidad canónica del Component.

Cuando una necesidad sea reutilizable deberá evaluarse si corresponde:

```text
Configure existing Component
        ↓
Extend Component
        ↓
Create new Component
```

No se duplicará un Component únicamente para introducir variaciones de contenido específicas de un proyecto.

---

# 52. Template Integration

La composición de README Components se determina mediante Repository Templates y necesidades específicas del proyecto.

No existen perfiles README independientes como:

```text
Strategic
Supporting
Learning
Experimental
```

Estos conceptos pertenecen al modelo de madurez cuando corresponda y no definen por sí solos una composición universal del README.

El modelo correcto es:

```text
Project Type
        ↓
Repository Template
        ↓
README Component Composition
        +
Maturity Expectations
```

Dos repositorios con la misma madurez podrán utilizar README Components diferentes.

La composición canónica deberá consultarse en el Repository Template correspondiente.

---

# 53. Anti-Patterns

No utilizar:

- README innecesariamente extensos;
- secciones vacías;
- tecnologías repetidas;
- duplicación de información mantenida canónicamente en `docs/`;
- GIF decorativos;
- badges sin significado;
- Components incorporados sin necesidad;
- requirement levels definidos globalmente fuera de Repository Templates;
- orden rígido cuando no responda a la experiencia de lectura.

---

# 54. README Quality Gates

Antes de aprobar un README deberá verificarse:

- [ ] El propósito del proyecto puede comprenderse rápidamente.
- [ ] Los Required README Components del Repository Template están correctamente materializados.
- [ ] Los Components adicionales responden a necesidades reales.
- [ ] No existen secciones vacías o redundantes.
- [ ] Funcionalidades y tecnologías están diferenciadas cuando corresponda.
- [ ] La navegación hacia documentación es coherente cuando exista documentación adicional.
- [ ] Las instrucciones de uso son suficientes para el tipo de proyecto.
- [ ] Los enlaces son válidos.
- [ ] La composición mantiene coherencia con el resto del repositorio.
- [ ] No se duplica innecesariamente información canónica mantenida en otros documentos.

---

# 55. Long-Term Vision

La README Component Library permitirá construir README reutilizando responsabilidades estandarizadas y validadas.

Los Repository Templates proporcionarán composiciones iniciales adecuadas a diferentes tipos de proyecto.

Cada Component podrá evolucionar independientemente dentro de su contrato y política de compatibilidad.

Con el tiempo, las especificaciones y metadata podrán permitir generación asistida de README a partir de Repository Templates y parámetros del proyecto.

La automatización deberá consumir las fuentes canónicas existentes y no sustituirlas.

---

# 56. Part 2 Conclusions

La **README Component Library** convierte el README en un sistema modular de responsabilidades reutilizables.

Cada README Component dispone de:

- un propósito;
- una responsabilidad;
- reglas de uso;
- relaciones o dependencias cuando correspondan;
- una definición canónica cuando exista implementación.

Los Repository Templates determinan contextualmente qué Components son:

```text
Required
Recommended
Optional
```

Por tanto, la biblioteca no define un README universal.

Proporciona piezas reutilizables que permiten construir README coherentes, mantenibles y adaptados al tipo real de proyecto.

---

# 57. Part 2 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.


---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 3/7

# Documentation Component Library

---

# 58. Purpose

La **Documentation Component Library (DCL)** define responsabilidades documentales reutilizables reconocidas por GitHub Framework.

Mientras la **README Component Library** está orientada principalmente a la presentación y navegación inicial del proyecto, la DCL proporciona Components para documentación técnica, operativa, de gobierno y de referencia.

Los Repository Templates podrán reutilizar estos Components cuando resulten adecuados para el tipo de proyecto.

La existencia de un Documentation Component en el RDS no implica necesariamente que disponga todavía de una implementación física estable dentro del Framework.

El objetivo de la DCL consiste en evitar que responsabilidades documentales recurrentes deban diseñarse nuevamente desde cero, sin imponer un sistema documental idéntico a todos los repositorios.

---

# 59. Documentation Philosophy

La documentación forma parte del producto cuando resulta necesaria para comprender, utilizar, mantener o evolucionar un proyecto.

Cada documento deberá responder a una necesidad concreta.

No deberá existir documentación únicamente "por si acaso".

Cuando una responsabilidad documental sea reutilizable y esté reconocida por el Framework, deberá reutilizarse el Documentation Component correspondiente.

Las necesidades específicas de un proyecto que no justifiquen generalización podrán permanecer como documentación propia del consumidor.

La documentación deberá mantener una fuente canónica identificable y evitar duplicaciones innecesarias.

---

# 60. Documentation Architecture

La documentación de un repositorio podrá organizarse mediante diferentes responsabilidades según su tipo y necesidades.

Modelo conceptual:

```text
README
        ↓
Project Documentation
        ├── Architecture
        ├── Engineering
        ├── Governance
        └── Reference
```

El README actúa como punto de entrada cuando corresponda.

La estructura concreta deberá derivarse del Repository Template y de las necesidades reales del proyecto.

No todos los repositorios necesitarán todas las áreas documentales ni deberán organizarlas físicamente de la misma forma.

---

# 61. Documentation Layers

La documentación puede analizarse mediante diferentes capas funcionales.

| Layer | Purpose |
|---|---|
| Entry | Primera toma de contacto y navegación |
| Functional | Explicación del funcionamiento |
| Technical | Arquitectura e implementación |
| Governance | Gestión y evolución |
| Reference | Información de consulta |

Estas capas proporcionan un modelo conceptual para separar responsabilidades documentales.

Un Documentation Component podrá relacionarse con una o varias de ellas cuando su responsabilidad lo justifique.

Las capas no determinan requirement levels ni una estructura física obligatoria.

---

# 62. Component Classification

Los Documentation Components se clasifican principalmente por la responsabilidad documental que representan.

Podrán relacionarse conceptualmente con áreas como:

- architecture;
- engineering;
- governance;
- reference.

Estas categorías facilitan descubrimiento y organización.

No determinan si un Component es obligatorio.

La necesidad de cada Documentation Component se establece contextualmente mediante el Repository Template correspondiente:

```text
Documentation Component
        ↓
Canonical responsibility

Repository Template
        ↓
Required / Recommended / Optional
```

La clasificación funcional, la prioridad, la madurez y el requirement level son propiedades diferentes y no deberán confundirse.

---

# 63. DOC-ARCHITECTURE

## Identifier

```text
DOC-ARCHITECTURE
```

---

## Purpose

Describir la arquitectura general del proyecto.

---

## Typical Sections

* visión general;
* módulos;
* diagramas;
* dependencias;
* decisiones clave.

---

# 64. DOC-ADR

## Identifier

```text
DOC-ADR
```

---

## Purpose

Registrar decisiones arquitectónicas relevantes.

---

## Structure

```text
Context

Decision

Consequences
```

---

# 65. DOC-ROADMAP

## Identifier

```text
DOC-ROADMAP
```

---

## Purpose

Mostrar la evolución prevista.

---

## Typical Horizons

```text
Current

Next Release

Future

Long Term
```

---

# 66. DOC-PROJECT-STATUS

## Identifier

```text
DOC-PROJECT-STATUS
```

---

## Purpose

Reflejar el estado actual del proyecto.

---

## Possible Information

* versión;
* estabilidad;
* hitos;
* riesgos;
* próximos pasos.

---

# 67. DOC-KNOWN-ISSUES

## Identifier

```text
DOC-KNOWN-ISSUES
```

---

## Purpose

Registrar limitaciones conocidas.

---

## Implementation Status

Responsabilidad documental reconocida por el RDS.

No dispone actualmente de una implementación canónica dentro de:

```text
framework/components/documentation/
```

Su incorporación futura como Framework Component requerirá especificación, metadata, implementación y validación conforme al lifecycle del RDS.

---

## Rules

Nunca ocultar problemas importantes.

La transparencia genera confianza.

---

# 68. DOC-CHANGELOG

## Identifier

```text
DOC-CHANGELOG
```

---

## Purpose

Mantener el historial funcional.

---

## Preferred Format

Keep a Changelog.

---

# 69. DOC-RELEASE-NOTES

## Identifier

```text
DOC-RELEASE-NOTES
```

---

## Purpose

Comunicar los cambios de cada versión.

No sustituye al CHANGELOG.

---

## Implementation Status

Responsabilidad documental reconocida por el RDS.

No dispone actualmente de una implementación canónica dentro de:

```text
framework/components/documentation/
```

Su incorporación futura como Framework Component requerirá especificación, metadata, implementación y validación conforme al lifecycle del RDS.

---

# 70. DOC-API

## Identifier

```text
DOC-API
```

---

## Purpose

Documentar interfaces públicas.

---

## Possible Formats

* OpenAPI;
* Markdown;
* Javadoc;
* MkDocs.

---

# 71. DOC-DATABASE

## Identifier

```text
DOC-DATABASE
```

---

## Purpose

Documentar el modelo de datos.

---

## Possible Contents

* entidades;
* relaciones;
* diagramas ER;
* convenciones.

---

# 72. DOC-DEPLOYMENT

## Identifier

```text
DOC-DEPLOYMENT
```

---

## Purpose

Explicar despliegue.

---

## Possible Sections

* requisitos;
* infraestructura;
* variables;
* Docker;
* Kubernetes.

---

# 73. DOC-TESTING

## Identifier

```text
DOC-TESTING
```

---

## Purpose

Explicar estrategia de calidad.

---

## Possible Contents

* unit tests;
* integration tests;
* coverage;
* CI.

---

# 74. DOC-SECURITY

## Identifier

```text
DOC-SECURITY
```

---

## Purpose

Explicar aspectos de seguridad.

---

## Possible Sections

* autenticación;
* autorización;
* secretos;
* vulnerabilidades conocidas.

---

# 75. DOC-DIAGRAMS

## Identifier

```text
DOC-DIAGRAMS
```

---

## Purpose

Centralizar diagramas.

---

## Preferred Formats

* Mermaid;
* PlantUML;
* SVG.

Evitar diagramas editables no versionados.

---

# 76. DOC-GLOSSARY

## Identifier

```text
DOC-GLOSSARY
```

---

## Purpose

Definir terminología.

Especialmente útil en proyectos de dominio complejo.

---

# 77. DOC-REFERENCES

## Identifier

```text
DOC-REFERENCES
```

---

## Purpose

Centralizar enlaces relevantes.

---

## Possible Targets

* documentación externa;
* estándares;
* RFC;
* papers;
* especificaciones.

---

# 78. Navigation Principles

La documentación deberá permitir al lector comprender su contexto y localizar información relacionada cuando sea necesario.

Según el tipo de documento podrán utilizarse:

- enlaces hacia documentación de nivel superior;
- enlaces hacia información más especializada;
- documentos relacionados;
- índices;
- navegación desde el README;
- referencias cruzadas.

La navegación bidireccional se utilizará cuando aporte valor.

No será necesario introducir enlaces artificiales únicamente para satisfacer una estructura uniforme.

---

# 79. Documentation Hierarchy

Los documentos deberán mantener responsabilidades diferenciadas y evitar duplicar información canónica.

Cuando exista una relación de profundización podrá utilizarse un modelo como:

```text
README
        ↓
Architecture
        ↓
ADR
```

El nivel superior resume y orienta.

El nivel especializado desarrolla el detalle correspondiente.

Las referencias podrán ser bidireccionales cuando mejoren la navegación, pero el contenido canónico deberá mantenerse en el documento responsable de esa información.

---

# 80. Cross References

Las referencias internas entre archivos del repositorio utilizarán preferentemente enlaces relativos.

Esto facilita:

- forks;
- branches;
- reorganizaciones;
- reutilización de Templates.

Las referencias hacia recursos externos utilizarán su URL correspondiente.

Los enlaces deberán apuntar a la fuente canónica siempre que sea posible.

---

# 81. Document Metadata

Los Documentation Components podrán definir metadata cuando sea necesaria para su mantenimiento y gobernanza.

Entre los campos habituales podrán encontrarse:

- título;
- versión;
- estado;
- owner;
- fecha;
- historial.

La metadata requerida dependerá de la responsabilidad del Component y del Repository Template.

No todos los documentos necesitarán necesariamente el mismo bloque de metadata.

Cuando exista una especificación canónica del Component, esta determinará los campos aplicables.

---

# 82. Callout Standards

Se utilizarán los callouts nativos de GitHub.

Ejemplos.

```markdown
> [!NOTE]

> [!TIP]

> [!IMPORTANT]

> [!WARNING]

> [!CAUTION]
```

No se crearán estilos personalizados.

---

# 83. Diagram Standards

Los diagramas deberán:

* mantenerse en Git;
* ser reproducibles;
* utilizar formato abierto;
* actualizarse junto con la documentación.

---

# 84. Documentation Component Catalog

La Documentation Component Library reconoce actualmente las siguientes responsabilidades:

| Component | Identifier | Responsibility | Implementation |
|---|---|---|---|
| Architecture | `DOC-ARCHITECTURE` | Arquitectura general | Implemented |
| ADR | `DOC-ADR` | Decisiones arquitectónicas | Implemented |
| Roadmap | `DOC-ROADMAP` | Evolución prevista | Implemented |
| Project Status | `DOC-PROJECT-STATUS` | Estado operativo | Implemented |
| Known Issues | `DOC-KNOWN-ISSUES` | Limitaciones conocidas | Conceptual |
| Changelog | `DOC-CHANGELOG` | Historial de cambios | Implemented |
| Release Notes | `DOC-RELEASE-NOTES` | Comunicación de releases | Conceptual |
| API | `DOC-API` | Interfaces públicas | Implemented |
| Database | `DOC-DATABASE` | Modelo de datos | Implemented |
| Deployment | `DOC-DEPLOYMENT` | Despliegue | Implemented |
| Testing | `DOC-TESTING` | Estrategia de calidad | Implemented |
| Security | `DOC-SECURITY` | Seguridad | Implemented |
| Diagrams | `DOC-DIAGRAMS` | Representaciones visuales | Implemented |
| Glossary | `DOC-GLOSSARY` | Terminología | Implemented |
| References | `DOC-REFERENCES` | Fuentes y referencias | Implemented |

`Implemented` indica que existe actualmente una definición canónica dentro de:

```text
framework/components/documentation/
```

`Conceptual` indica una responsabilidad reconocida por el RDS que todavía no dispone de implementación canónica dentro del Framework.

La presencia en este catálogo no determina requirement level.

Los Repository Templates establecen contextualmente qué Components son `required`, `recommended` u `optional`.

El Component Catalog global y las definiciones canónicas deberán mantenerse sincronizados con esta evolución.

---

# 85. Template Integration

La composición de Documentation Components pertenece a los Repository Templates.

Un Template podrá seleccionar diferentes responsabilidades documentales según el tipo de proyecto.

Ejemplo conceptual:

```text
Project Type
        ↓
Repository Template
        ↓
Documentation Component Composition
        ↓
Required / Recommended / Optional
```

Los Maturity Profiles podrán incrementar las expectativas de profundidad, mantenimiento o gobernanza documental.

No constituyen, sin embargo, una matriz universal de documentos.

Por tanto:

```text
Same maturity
≠
Same documentation
```

Dos repositorios con la misma madurez podrán requerir sistemas documentales diferentes.

---

# 86. Anti-Patterns

No utilizar:

- documentación duplicada;
- diagramas sin mantener;
- ADR para decisiones triviales;
- enlaces rotos;
- documentos huérfanos sin justificación;
- mezclas innecesarias de idiomas dentro de un mismo documento;
- referencias externas sin contexto;
- Documentation Components incorporados sin necesidad;
- requirement levels definidos globalmente fuera de Repository Templates;
- documentación creada únicamente para aumentar cobertura;
- definiciones paralelas de una misma responsabilidad documental.

---

# 87. Documentation Quality Gates

Antes de aprobar el sistema documental de un repositorio deberá verificarse:

- [ ] Los Required Documentation Components del Repository Template están correctamente materializados.
- [ ] Cada documento responde a una responsabilidad identificable.
- [ ] Los Components adicionales responden a necesidades reales.
- [ ] No existe duplicación innecesaria de información canónica.
- [ ] La navegación permite localizar la información relevante.
- [ ] Los enlaces internos y externos son válidos.
- [ ] La metadata requerida por los Components aplicables está presente.
- [ ] Los diagramas existentes están actualizados y son mantenibles.
- [ ] No existen documentos obsoletos o huérfanos sin justificación.
- [ ] La documentación refleja razonablemente el estado actual del proyecto.

---

# 88. Long-Term Vision

La Documentation Component Library permitirá construir sistemas documentales reutilizando responsabilidades estandarizadas y validadas.

Los Repository Templates proporcionarán composiciones adecuadas a diferentes tipos de proyecto.

Los repositorios podrán compartir responsabilidades, convenciones y patrones de navegación sin necesitar una estructura documental idéntica.

Con el tiempo, las especificaciones y metadata podrán permitir:

- resolución automática de Documentation Components;
- generación asistida de documentación;
- validación de conformidad;
- detección de documentación obsoleta;
- análisis de navegación y referencias.

La automatización deberá consumir las fuentes canónicas existentes y no sustituirlas.

---

# 89. Part 3 Conclusions

La **Documentation Component Library** convierte responsabilidades documentales recurrentes en elementos reutilizables del Framework.

Cada Documentation Component representa una responsabilidad definida.

Cuando existe implementación, su especificación y metadata constituyen su fuente canónica.

El RDS podrá reconocer además responsabilidades conceptuales pendientes de implementación, siempre que su estado quede claramente diferenciado.

Los Repository Templates determinan contextualmente qué Documentation Components son:

```text
Required
Recommended
Optional
```

Por tanto, la DCL no impone un sistema documental universal.

Proporciona responsabilidades reutilizables para construir documentación coherente, mantenible y adaptada a las necesidades reales de cada tipo de proyecto.

---

# 90. Part 3 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.


---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 4/7

# Workflow Component Library

---

# 91. Purpose

La **Workflow Component Library (WCL)** define responsabilidades operativas reutilizables relacionadas con el desarrollo, validación, publicación y mantenimiento de repositorios.

Los Workflow Components permiten reutilizar prácticas y procesos cuando resultan adecuados para el tipo de proyecto y su contexto operativo.

Los Repository Templates podrán incorporar estos Components mediante requirement levels contextuales.

El objetivo consiste en proporcionar patrones reutilizables sin imponer un workflow universal a todos los repositorios.

Diferentes proyectos podrán utilizar composiciones operativas diferentes incluso cuando compartan nivel de madurez.

---

# 92. Workflow Philosophy

Un workflow deberá:

- responder a una necesidad operativa identificable;
- ser comprensible;
- reducir errores;
- facilitar el mantenimiento;
- automatizar tareas repetitivas cuando aporte valor;
- minimizar la burocracia.

Los procesos deberán ayudar al desarrollo y mantenimiento del proyecto.

No deberán incorporarse únicamente para reproducir prácticas habituales de otros repositorios.

La complejidad del workflow deberá ser proporcional a las necesidades reales del consumidor.

---

# 93. Workflow Layers

Los workflows pueden analizarse mediante diferentes capas funcionales.

```text
Planning

↓

Development

↓

Validation

↓

Release

↓

Maintenance
```

Estas capas proporcionan un modelo conceptual para organizar responsabilidades operativas.

Un Workflow Component podrá relacionarse con una o varias capas cuando su responsabilidad lo justifique.

Las capas no determinan requirement levels ni una secuencia universal obligatoria.

---

# 94. Workflow Classification

Los Workflow Components podrán relacionarse con diferentes áreas operativas:

| Area | Purpose |
|---|---|
| Planning | Organización del trabajo |
| Development | Desarrollo e integración |
| Validation | Revisión y calidad |
| Release | Versionado y publicación |
| Maintenance | Evolución posterior |

Estas áreas facilitan clasificación y descubrimiento.

No determinan si un Workflow Component es obligatorio.

La necesidad del Component se establece contextualmente mediante el Repository Template y las necesidades operativas del proyecto.

---

# 95. WCL-ISSUE

## Identifier

```text id="workflow002"
WCL-ISSUE
```

---

## Purpose

Representar una unidad de trabajo.

---

## Structure

```text id="workflow003"
Context

↓

Objective

↓

Acceptance Criteria

↓

Technical Notes

↓

Related Links
```

---

# 96. WCL-LABEL

## Identifier

```text
WCL-LABEL
```

---

## Purpose

Clasificar Issues y Pull Requests.

---

## Possible Categories

```text
type:

priority:

status:

area:
```

Las categorías concretas deberán adaptarse al modelo de trabajo del repositorio.

No todos los consumidores necesitarán el mismo conjunto de labels.

---

# 97. WCL-PROJECT

## Identifier

```text id="workflow006"
WCL-PROJECT
```

---

## Purpose

Organizar el backlog.

---

## Recommended Views

* Backlog
* Sprint
* Roadmap
* Done

---

# 98. WCL-BRANCH

## Identifier

```text
WCL-BRANCH
```

---

## Purpose

Definir una estrategia coherente para organizar ramas cuando el proyecto necesite desarrollo paralelo o aislamiento de cambios.

---

## Possible Strategies

Según el contexto podrán utilizarse estrategias como:

```text
main
+
feature/*
```

o:

```text
main
+
develop
+
feature/*
+
release/*
+
hotfix/*
```

También podrán utilizarse otros modelos compatibles con las necesidades del proyecto.

La estrategia concreta deberá definirse en el Repository Template o en la configuración del consumidor cuando corresponda.

No se impondrá Git Flow como estrategia universal.

---

# 99. WCL-COMMIT

## Identifier

```text id="workflow009"
WCL-COMMIT
```

---

## Purpose

Normalizar commits.

---

## Possible Convention

Podrá utilizarse una convención basada en prefijos como:

```text
feat

fix

docs

test

refactor

build

ci

chore
```

El Repository Template o el proyecto consumidor podrá establecer convenciones adicionales, incluido el idioma, cuando resulte necesario.

La convención deberá mantenerse consistente dentro del repositorio.

---

# 100. WCL-PULL-REQUEST

## Identifier

```text id="workflow011"
WCL-PULL-REQUEST
```

---

## Purpose

Documentar integración.

---

## Typical Sections

```text
Summary

Changes

Validation

Evidence

Related Issues
```

---

# 101. WCL-CODE-REVIEW

## Identifier

```text
WCL-CODE-REVIEW
```

---

## Purpose

Revisar calidad antes del merge.

---

## Possible Review Areas

* arquitectura;
* naming;
* tests;
* documentación;
* seguridad;
* duplicación;
* complejidad.

---

# 102. WCL-CI

## Identifier

```text
WCL-CI
```

---

## Purpose

Validar automáticamente.

---

## Typical Steps

```text id="workflow015"
Checkout

↓

Dependencies

↓

Build

↓

Tests

↓

Coverage

↓

Static Analysis
```

---

# 103. WCL-CD

## Identifier

```text id="workflow016"
WCL-CD
```

---

## Purpose

Automatizar publicación.

---

## Possible Targets

* GitHub Pages
* Docker Registry
* Releases
* Documentation

---

# 104. WCL-DEPENDABOT

## Identifier

```text
WCL-DEPENDABOT
```

---

## Purpose

Mantener dependencias actualizadas.

---

## Update Strategy

La frecuencia y configuración deberán adaptarse al ecosistema tecnológico, actividad y necesidades de mantenimiento del proyecto.

Las actualizaciones automáticas no deberán generar ruido operativo innecesario.

---

# 105. WCL-SECURITY

## Identifier

```text
WCL-SECURITY
```

---

## Purpose

Gestionar aspectos de seguridad.

---

## Possible Capabilities

- Secret Scanning
- Code Scanning
- Security Policy
- Dependabot Alerts

---

# 106. WCL-RELEASE

## Identifier

```text
WCL-RELEASE
```

---

## Purpose

Definir un proceso reproducible para publicar versiones cuando el proyecto mantenga releases.

---

## Possible Responsibilities

Un release podrá implicar, según el proyecto:

- versionado;
- tag;
- release notes;
- GitHub Release;
- actualización de changelog;
- actualización de estado;
- publicación de artefactos;
- despliegue.

La secuencia y responsabilidades concretas deberán derivarse del contexto del proyecto.

No todos los repositorios necesitarán releases formales.

---

# 107. WCL-HOTFIX

## Identifier

```text
WCL-HOTFIX
```

---

## Purpose

Gestionar correcciones urgentes que requieren un tratamiento diferente al flujo ordinario de cambios.

---

## Guidance

La estrategia concreta dependerá del branching model y del release model utilizados por el repositorio.

Un hotfix podrá requerir:

- aislamiento del cambio;
- validación prioritaria;
- publicación acelerada;
- sincronización con ramas activas;
- actualización documental cuando corresponda.

No se presupone una estructura concreta de ramas.

---

# 108. WCL-DOCUMENTATION-UPDATE

## Identifier

```text id="workflow023"
WCL-DOCUMENTATION-UPDATE
```

---

## Purpose

Sincronizar documentación.

---

## Possible Triggers

- cambios de comportamiento;
- cambios arquitectónicos;
- nuevas capacidades;
- releases;
- modificaciones de configuración;
- cambios que invaliden documentación existente.

---

# 109. WCL-ASSESSMENT

## Identifier

```text
WCL-ASSESSMENT
```

---

## Purpose

Ejecutar una evaluación estructurada del repositorio cuando corresponda, incluyendo GRS Assessment cuando forme parte del modelo de evaluación aplicable.

---

## Possible Outputs

- Score;
- Readiness;
- Findings;
- Backlog.

---

# 110. WCL-MAINTENANCE

## Identifier

```text
WCL-MAINTENANCE
```

---

## Purpose

Mantener el repositorio.

---

## Typical Tasks

* actualizar dependencias;
* revisar Issues;
* revisar enlaces;
* actualizar roadmap;
* revisar documentación.

---

# 111. Workflow Relationships

Los Workflow Components podrán mantener relaciones o dependencias cuando su responsabilidad lo requiera.

Ejemplo de composición posible:

```text
Issue
        ↓
Branch
        ↓
Commit
        ↓
Pull Request
        ↓
Review
        ↓
CI
        ↓
Release
```

Esta secuencia representa una composición posible, no un workflow universal.

Otros repositorios podrán utilizar subconjuntos diferentes.

Las dependencias reales deberán declararse en la definición canónica del Workflow Component cuando exista implementación.

No se crearán dependencias artificiales únicamente para mantener una cadena operativa uniforme.

---

# 112. Template Integration

La composición de Workflow Components pertenece a los Repository Templates y a las necesidades operativas del proyecto.

No existen Workflow Profiles independientes como:

```text
Strategic
Supporting
Learning
Experimental
```

Estos conceptos pertenecen al modelo de madurez cuando corresponda.

El modelo correcto es:

```text
Project Type
        ↓
Repository Template
        ↓
Workflow Component Composition
        +
Maturity Expectations
```

Los Maturity Profiles podrán incrementar expectativas de revisión, automatización, seguridad o mantenimiento.

No determinan una matriz universal de Workflow Components.

Por tanto:

```text
Same maturity
≠
Same workflow
```

---

# 113. Automation Policy

Toda tarea repetitiva deberá evaluarse para automatización cuando exista suficiente estabilidad del proceso.

Ejemplos:

- validación Markdown;
- comprobación de enlaces;
- testing;
- releases;
- documentación;
- validación de metadata.

La automatización deberá:

- aportar valor operativo;
- ser comprensible;
- mantenerse observable;
- consumir fuentes canónicas cuando existan;
- evitar duplicar reglas mantenidas en otros lugares.

No se automatizarán decisiones que requieran necesariamente juicio humano.

La automatización no constituye un objetivo por sí misma.

---

# 114. Manual Approval Points

Determinadas decisiones podrán requerir aprobación humana según el riesgo y contexto del proyecto.

Ejemplos:

- publicar una release;
- archivar un repositorio;
- promocionar un proyecto;
- cambiar una licencia;
- modificar una estrategia operativa relevante.

Los approval points deberán utilizarse cuando aporten control real.

No deberán introducirse como burocracia automática en todos los workflows.

---

# 115. Workflow Quality Attributes

Todo workflow deberá ser:

- reproducible;
- documentado;
- simple;
- observable;
- mantenible;
- proporcional a la necesidad.

---

# 116. Anti-Patterns

No utilizar:

- procesos duplicados;
- ramas permanentes innecesarias;
- branching models complejos sin necesidad;
- workflows sin mantenimiento;
- Pull Requests innecesariamente grandes;
- releases formales cuando el proyecto no las necesita;
- automatizaciones opacas;
- Workflow Components incorporados únicamente por madurez;
- requirement levels definidos globalmente fuera de Repository Templates;
- dependencias artificiales entre Workflow Components;
- procesos copiados de otro proyecto sin evaluar su contexto.

---

# 117. Workflow Quality Gates

Antes de aprobar un Workflow Component o una composición operativa deberá verificarse, según corresponda:

- [ ] El objetivo está definido.
- [ ] Responde a una necesidad operativa real.
- [ ] La responsabilidad está claramente delimitada.
- [ ] La automatización está justificada cuando existe.
- [ ] La documentación necesaria está disponible.
- [ ] Las dependencias reales están identificadas.
- [ ] No introduce complejidad innecesaria.
- [ ] Puede mantenerse y observarse.
- [ ] No duplica una responsabilidad existente.
- [ ] Su requirement level procede del Repository Template cuando corresponda.
- [ ] Puede reutilizarse o permanecer específico del consumidor según su naturaleza.

---

# 118. Long-Term Vision

La Workflow Component Library permitirá construir procesos operativos reutilizando responsabilidades estandarizadas y validadas.

Los Repository Templates podrán proporcionar composiciones adecuadas a diferentes tipos de proyecto.

Los repositorios compartirán patrones operativos cuando exista una necesidad común, sin requerir exactamente la misma forma de trabajar.

Con el tiempo, las especificaciones y metadata podrán permitir:

- resolución automática de Workflow Components;
- configuración asistida de workflows;
- validación de dependencias;
- análisis de conformidad;
- generación de automatizaciones;
- detección de procesos obsoletos.

La automatización deberá consumir las fuentes canónicas existentes y no sustituirlas.

---

# 119. Part 4 Conclusions

La **Workflow Component Library** convierte responsabilidades operativas recurrentes en elementos reutilizables del Framework.

Issues, ramas, commits, Pull Requests, revisión, integración continua, releases y mantenimiento podrán modelarse mediante Workflow Components cuando resulten necesarios.

Cada Workflow Component representa una responsabilidad operativa definida.

Los Repository Templates determinan contextualmente qué Workflow Components son:

```text
Required
Recommended
Optional
```

Los Maturity Profiles podrán incrementar las expectativas operativas, pero no definen una composición universal.

Por tanto:

```text
Reusable workflow responsibilities
        +
Repository Template
        +
Project needs
        ↓
Appropriate operational model
```

La WCL no pretende que todos los repositorios trabajen de la misma forma.

Pretende evitar que responsabilidades operativas recurrentes deban diseñarse nuevamente desde cero.

---

# 120. Part 4 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.


---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 5/7

# Visual Component Library

---

# 121. Purpose

La **Visual Component Library (VCL)** define responsabilidades visuales reutilizables reconocidas por GitHub Framework.

Su objetivo consiste en facilitar una presentación visual coherente, profesional y mantenible mediante Components reutilizables cuando exista una necesidad visual identificable.

La VCL complementa el **Visual Design System**, pero no lo sustituye.

El Visual Design System define principios, reglas y convenciones como:

- color;
- tipografía;
- espaciado;
- accesibilidad;
- compatibilidad visual;
- comportamiento responsive.

La VCL define elementos visuales reutilizables que pueden materializar esas reglas.

Por tanto:

```text
Visual Design System
        ↓
Visual rules and constraints

Visual Component Library
        ↓
Reusable visual responsibilities
```

No todo proyecto necesitará Visual Components específicos ni deberá compartir exactamente la misma identidad gráfica.

---

# 122. Visual Philosophy

Todo Visual Component deberá responder a una necesidad identificable.

Podrá contribuir a:

- facilitar la comprensión;
- reforzar la identidad;
- mejorar la navegación;
- comunicar información;
- proporcionar contexto visual.

Los elementos visuales no deberán incorporarse únicamente con fines decorativos.

La complejidad visual deberá ser proporcional al valor que aporta al consumidor.

La coherencia deberá derivarse de las reglas del Visual Design System y no de imponer exactamente los mismos elementos gráficos a todos los repositorios.

---

# 123. Visual Architecture

La experiencia visual de un repositorio puede construirse mediante diferentes responsabilidades.

Modelo conceptual:

```text
Visual Experience
        ├── Identity
        ├── Presentation
        ├── Information
        ├── Navigation
        └── Technical Visualization
```

Los Visual Components podrán relacionarse con una o varias de estas áreas.

No existe una secuencia visual universal que todos los repositorios deban implementar.

La composición deberá derivarse del Repository Template, del contexto del consumidor y de las reglas del Visual Design System.

---

# 124. Visual Classification

Los Visual Components podrán relacionarse con diferentes áreas funcionales:

| Area | Purpose |
|---|---|
| Identity | Identidad visual del proyecto |
| Presentation | Presentación inicial y comunicación visual |
| Information | Comunicación visual de información |
| Navigation | Acceso visual a contenidos relacionados |
| Technical Visualization | Representación de arquitectura, procesos o estructura |

Estas áreas facilitan clasificación y descubrimiento.

No determinan requirement levels.

Un Visual Component podrá utilizarse en diferentes tipos de consumidor cuando su responsabilidad resulte aplicable.

---

# 125. VCL-BANNER

## Identifier

```text id="visual002"
VCL-BANNER
```

---

## Purpose

Presentar visualmente el proyecto.

---

## Recommended Contents

* nombre;
* tagline;
* iconografía;
* fondo minimalista.

---

## Recommended Format

Las dimensiones deberán adaptarse al contexto donde se utilice el banner.

Cuando se necesite un formato horizontal reutilizable podrá utilizarse una relación aproximada:

```text
2:1
```

Las dimensiones concretas podrán definirse mediante guidance o variantes del Component.

---

# 126. VCL-SOCIAL-PREVIEW

## Identifier

```text id="visual004"
VCL-SOCIAL-PREVIEW
```

---

## Purpose

Imagen utilizada por GitHub al compartir el repositorio.

---

## Recommended Principles

* legible en miniatura;
* sin texto excesivo;
* coherente con el banner;
* fácilmente reconocible.

---

# 127. VCL-HERO

## Identifier

```text id="visual005"
VCL-HERO
```

---

## Purpose

Construir la cabecera del README.

---

## Relationship

Puede materializar visualmente responsabilidades definidas por `README-HERO`.

No sustituye al README Component ni duplica su responsabilidad documental.

---

## Typical Structure

```text
Banner

↓

Project Name

↓

Tagline

↓

Primary Badges
```

---

# 128. VCL-BADGES

## Identifier

```text id="visual007"
VCL-BADGES
```

---

## Purpose

Mostrar información rápida.

---

## Possible Categories

* Build
* Version
* License
* Documentation
* Status

---

## Badge Policy

Utilizar únicamente badges útiles.

Evitar colecciones enormes.

---

# 129. VCL-SKILL-ICONS

## Identifier

```text id="visual008"
VCL-SKILL-ICONS
```

---

## Purpose

Representar tecnologías.

---

## Possible Sources

Podrán utilizarse proveedores o assets compatibles con las reglas del Visual Design System.

Entre las opciones actuales puede utilizarse:

```text
skillicons.dev
```

La responsabilidad del Component no dependerá de un proveedor concreto.

---

## Principles

* pocas tecnologías;
* agrupadas por categorías;
* sin duplicados.

---

# 130. VCL-PROJECT-CARD

## Identifier

```text id="visual010"
VCL-PROJECT-CARD
```

---

## Purpose

Representar proyectos relacionados.

---

## Contents

* nombre;
* descripción;
* stack;
* enlace.

---

## Possible Consumers

- GitHub Profile;
- portfolio;
- landing pages;
- documentación que necesite representar proyectos relacionados.



---

# 131. VCL-STATS

## Identifier

```text
VCL-STATS
```

---

## Purpose

Representar visualmente métricas o estadísticas relevantes cuando aporten contexto al consumidor.

---

## Typical Consumer

GitHub Profile.

---

## Guidance

Las estadísticas deberán utilizarse únicamente cuando aporten información útil.

La selección de widgets, proveedores o métricas no forma parte del contrato general del Component.

No deberá asumirse que los repositorios individuales necesitan estadísticas visuales.

---

# 132. VCL-CONTRIBUTION-GRAPH

## Identifier

```text
VCL-CONTRIBUTION-GRAPH
```

---

## Purpose

Representar visualmente actividad o contribuciones cuando esta información resulte relevante.

---

## Typical Consumer

GitHub Profile.

---

## Guidance

Su uso deberá justificarse por el contexto.

No forma parte de la composición visual general de los repositorios.

---

# 133. VCL-TYPING-BANNER

## Identifier

```text
VCL-TYPING-BANNER
```

---

## Purpose

Mostrar contenido textual dinámico cuando aporte valor a la presentación.

---

## Typical Consumer

GitHub Profile.

---

## Guidance

Su uso deberá ser excepcional y responder a una necesidad concreta.

No deberá incorporarse como elemento visual estándar de los repositorios.

---

# 134. VCL-ARCHITECTURE-DIAGRAM

## Identifier

```text
VCL-ARCHITECTURE-DIAGRAM
```

---

## Purpose

Representar la arquitectura.

---

## Recommended Formats

* Mermaid
* PlantUML
* SVG

---

# 135. VCL-WORKFLOW-DIAGRAM

## Identifier

```text
VCL-WORKFLOW-DIAGRAM
```

---

## Purpose

Explicar procesos.

---

## Examples

* CI/CD
* Release Flow
* Knowledge Pipeline

---

# 136. VCL-FOLDER-DIAGRAM

## Identifier

```text
VCL-FOLDER-DIAGRAM
```

---

## Purpose

Explicar estructura.

---

## Possible Formats

- árbol textual;
- Mermaid;
- SVG;
- otras representaciones mantenibles cuando aporten claridad.

Ejemplo:

```text
src/

docs/

assets/

.github/
```

---

# 137. VCL-NAVIGATION-CARD

## Identifier

```text
VCL-NAVIGATION-CARD
```

---

## Purpose

Enlazar documentación relacionada.

---

## Possible Targets

* Architecture
* API
* Roadmap
* ADR

---

# 138. VCL-CALL-OUT

## Identifier

```text
VCL-CALL-OUT
```

---

## Purpose

Resaltar información importante.

---

## Relationship

La representación y sintaxis deberán seguir las reglas definidas por la Documentation Component Library y los estándares documentales aplicables.

Este Component representa la responsabilidad visual de destacar información y no redefine la sintaxis canónica de los callouts.

---

## Current Recommended Style

GitHub Callouts.

```markdown
> [!NOTE]

> [!TIP]

> [!IMPORTANT]

> [!WARNING]
```

---

# 139. Color System

El sistema de color se define mediante el Visual Design System.

Los Visual Components deberán reutilizar sus roles y convenciones cuando corresponda.

No deberán introducir colores arbitrarios que contradigan la identidad visual definida.

Los colores concretos, tokens y variantes pertenecen a la fuente canónica del Visual Design System y no se duplican en la VCL.

---

# 140. Typography

Los Visual Components deberán respetar las reglas tipográficas definidas por el Visual Design System y las capacidades del medio donde se rendericen.

En GitHub se priorizará la tipografía nativa y la legibilidad.

Se evitarán:

- fuentes embebidas innecesarias;
- imágenes utilizadas únicamente para representar texto;
- efectos tipográficos que reduzcan accesibilidad o mantenibilidad.

Las decisiones tipográficas canónicas pertenecen al Visual Design System.

---

# 141. Spacing

Los Visual Components deberán mantener una separación visual coherente con el contexto donde se utilicen.

Se evitarán:

- bloques excesivamente densos;
- encabezados consecutivos sin contenido;
- separación irregular;
- espacios introducidos artificialmente mediante hacks de Markdown o HTML.

Las reglas específicas de espaciado pertenecen al Visual Design System cuando estén definidas.

---

# 142. Iconography

Los Visual Components deberán utilizar iconografía consistente cuando resulte necesaria.

Las fuentes podrán incluir, entre otras:

- Skill Icons;
- Simple Icons;
- GitHub Octicons;
- assets propios mantenidos por el proyecto.

La selección deberá respetar las reglas del Visual Design System.

No deberán mezclarse estilos visuales incompatibles sin justificación.

---

# 143. Image Policy

Las imágenes utilizadas por Visual Components deberán ser mantenibles y formar parte de una estrategia de assets identificable.

Cuando corresponda deberán:

- estar versionadas;
- almacenarse junto al proyecto o en una fuente controlada;
- optimizarse;
- mantenerse actualizadas;
- disponer de texto alternativo cuando sea necesario.

Las dependencias externas deberán utilizarse únicamente cuando aporten una ventaja justificada.

La ubicación física concreta de los assets dependerá de la estructura del Repository Template o del consumidor.

---

# 144. Dark Mode Compatibility

Los Visual Components deberán verificarse en los modos de visualización relevantes del medio donde se utilicen.

Para GitHub deberán considerarse, como mínimo:

- GitHub Dark;
- GitHub Light.

Los Components no deberán depender exclusivamente de un único modo cuando esto comprometa su comprensión.

---

# 145. Responsive Behavior

Los Visual Components deberán conservar su comprensión en los tamaños de pantalla relevantes para su consumidor.

Cuando corresponda deberán evaluarse en:

- escritorio;
- tablet;
- móvil.

La validación deberá prestar especial atención a elementos con dimensiones amplias, texto integrado o información visual densa.

---

# 146. Accessibility

Los Visual Components deberán respetar principios básicos de accesibilidad.

Entre ellos:

- mantener contraste suficiente;
- no depender únicamente del color;
- utilizar texto alternativo cuando proceda;
- evitar imágenes con exceso de información;
- mantener legibilidad en diferentes tamaños;
- evitar movimiento o efectos visuales innecesarios.

Las reglas detalladas deberán mantenerse en el Visual Design System o en estándares especializados cuando existan.

---

# 147. Template Integration

La composición de Visual Components pertenece a los Repository Templates y a las necesidades de presentación del proyecto.

No existen Visual Profiles independientes como:

```text
Strategic
Supporting
Learning
Experimental
```

Estos conceptos pertenecen al modelo de madurez cuando corresponda.

El modelo correcto es:

```text
Project Type
        ↓
Repository Template
        ↓
Visual Component Composition
        +
Maturity Expectations
```

Los Maturity Profiles podrán incrementar expectativas de calidad, consistencia, accesibilidad o presentación.

No determinan una matriz universal de Visual Components.

Por tanto:

```text
Same maturity
≠
Same visual composition
```

---

# 148. Anti-Patterns

No utilizar:

- elementos visuales sin propósito;
- GIF decorativos;
- badges excesivos;
- fondos recargados;
- iconografía inconsistente;
- estadísticas sin valor informativo;
- colores sin criterio;
- tipografías artificiales;
- imágenes de baja calidad;
- Visual Components incorporados únicamente por madurez;
- requirement levels definidos globalmente fuera de Repository Templates;
- reglas del Visual Design System duplicadas dentro de Components;
- dependencias innecesarias de proveedores externos;
- elementos específicos de un consumidor generalizados sin evidencia de reutilización.

---

# 149. Visual Quality Gates

Antes de aprobar la composición visual de un repositorio deberá verificarse, según corresponda:

- [ ] Los Required Visual Components del Repository Template están correctamente materializados.
- [ ] Cada elemento visual responde a una necesidad identificable.
- [ ] Los Components adicionales aportan valor real.
- [ ] La composición respeta las reglas aplicables del Visual Design System.
- [ ] La información visual es legible.
- [ ] La navegación visual es comprensible cuando exista.
- [ ] Los assets son mantenibles.
- [ ] La compatibilidad con los modos de visualización relevantes ha sido revisada.
- [ ] El comportamiento responsive es adecuado cuando corresponde.
- [ ] La accesibilidad ha sido considerada.
- [ ] No existen elementos puramente decorativos que generen ruido innecesario.
- [ ] No se duplican reglas mantenidas canónicamente en el Visual Design System.

---

# 150. Long-Term Vision

La Visual Component Library permitirá reutilizar responsabilidades visuales validadas cuando un repositorio necesite identidad, presentación, navegación o visualización técnica.

Los Repository Templates podrán proporcionar composiciones visuales adecuadas a diferentes tipos de proyecto.

Los repositorios podrán compartir lenguaje visual sin necesitar exactamente los mismos elementos gráficos.

Con el tiempo, las especificaciones, assets y metadata podrán permitir:

- resolución automática de Visual Components;
- generación asistida de assets;
- validación de consistencia visual;
- comprobaciones de accesibilidad;
- detección de assets obsoletos;
- adaptación de variantes.

La automatización deberá consumir las fuentes canónicas del Visual Design System y de los Visual Components sin duplicarlas.

---

# 151. Part 5 Conclusions

La **Visual Component Library** convierte responsabilidades visuales recurrentes en elementos reutilizables del Framework.

Banners, social previews, badges, tarjetas, diagramas y otros elementos podrán modelarse mediante Visual Components cuando exista una necesidad reutilizable.

Las reglas de color, tipografía, espaciado, accesibilidad, responsive behavior y compatibilidad visual pertenecen al Visual Design System y actúan como constraints sobre estos Components.

Los Repository Templates determinan contextualmente qué Visual Components son:

```text
Required
Recommended
Optional
```

Los Maturity Profiles podrán incrementar las expectativas de calidad visual, pero no definen una composición universal.

Por tanto:

```text
Visual Design System
        +
Reusable Visual Components
        +
Repository Template
        +
Project needs
        ↓
Appropriate visual experience
```

La VCL no pretende que todos los repositorios tengan la misma apariencia.

Pretende reutilizar responsabilidades visuales comunes manteniendo coherencia, claridad y capacidad de adaptación.

---

# 152. Part 5 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.
---

# 08 - REPOSITORY DESIGN SYSTEM

# Part 6/7

# Repository Templates & Maturity Profiles

---

# 153. Purpose

La **Repository Template Library (RTL)** define composiciones reutilizables para crear y estructurar repositorios según su tipo de proyecto.

Cada Repository Template establece:

- un tipo de proyecto;
- un nivel mínimo de madurez recomendado;
- una composición de Framework Components;
- reglas de aplicación y personalización.

El objetivo consiste en reducir decisiones repetitivas durante la creación de repositorios y proporcionar una base coherente sin imponer tecnologías, estructuras o Components innecesarios.

---

# 154. Template Philosophy

Los Repository Templates no son repositorios completos ni copias rígidas de una estructura predeterminada.

Son composiciones reutilizables del Framework.

Cada Template selecciona únicamente los Components necesarios para representar un determinado tipo de repositorio y establece su requirement level dentro de esa composición.

Principio:

```text
Components
    ↓
Reusable responsibilities
    ↓
Repository Template
    ↓
Context-specific composition
```

Un Template reutiliza Components.

No redefine sus responsabilidades canónicas.

---

# 155. Template Architecture

Un Repository Template se modela mediante:

```text
Repository Template
├── Project Type
├── Maturity
├── Required Components
├── Recommended Components
├── Optional Components
└── Template-specific guidance
```

El tipo de proyecto determina el contexto principal de la composición.

La madurez representa el nivel mínimo recomendado para utilizar el Template y se registra como metadata.

Los Components se clasifican dentro de cada Template como:

```text
Required
Recommended
Optional
```

El requirement level dentro de un Template es contextual y no modifica la prioridad canónica del Component en el Component Catalog.

---

# 156. Maturity Levels

GitHub Framework mantiene los niveles de madurez definidos por el sistema:

| Level | Description |
|---|---|
| L1 | Experimental |
| L2 | Public Basic |
| L3 | Supporting |
| L4 | Strategic |

La madurez describe el nivel de evolución, mantenimiento y exigencia esperado para un repositorio o Component.

No constituye un Repository Template independiente.

Por tanto:

```text
TPL-DOCUMENTATION
maturity: L2
```

No se modelará mediante:

```text
TPL-DOCUMENTATION
+
TPL-L2
```

La evolución de madurez podrá requerir incorporar nuevos Components o prácticas, pero no implica cambiar el tipo de Repository Template.

---

# 157. L1 — Experimental Maturity Profile

## Purpose

Explorar y validar ideas con una inversión estructural mínima.

## Typical Projects

- pruebas;
- prototipos;
- investigación;
- spikes técnicos.

## Characteristics

- estructura mínima;
- documentación esencial;
- Components limitados a necesidades reales;
- automatización opcional;
- cambios frecuentes permitidos.

L1 no define una estructura física ni un Repository Template específico.

---

# 158. L2 — Public Basic Maturity Profile

## Purpose

Mantener un repositorio público comprensible y utilizable.

## Characteristics

- identidad y propósito claros;
- licencia cuando corresponda;
- documentación de uso suficiente;
- estado visible;
- historial de cambios cuando exista versionado;
- prácticas básicas de mantenimiento.

L2 constituye actualmente el nivel mínimo recomendado para los Repository Templates implementados.

---

# 159. L3 — Supporting Maturity Profile

## Purpose

Mantener proyectos públicos relevantes con mayor profundidad documental y operativa.

## Characteristics

- documentación técnica ampliada;
- testing documentado;
- roadmap cuando exista evolución planificada;
- automatización de calidad;
- procesos de contribución y revisión cuando sean necesarios;
- mayor trazabilidad de decisiones.

L3 amplía las expectativas de mantenimiento sin constituir un Template independiente.

---

# 160. L4 — Strategic Maturity Profile

## Purpose

Mantener repositorios estratégicos con alta exigencia de calidad, gobernanza y continuidad.

## Characteristics

- documentación profunda;
- gobernanza explícita;
- automatización avanzada cuando aporte valor;
- seguridad y mantenimiento continuado;
- trazabilidad de decisiones;
- releases y evolución controlada;
- alta calidad de presentación y experiencia de uso.

L4 representa el nivel de madurez más exigente del Framework.

No obliga a incorporar todos los Components existentes.

---

# 161. Repository Template Catalog

La Repository Template Library se organiza por tipo de proyecto.

Los Repository Templates implementados actualmente son:

| Template | Project Type | Maturity | Status |
|---|---|---:|---|
| `TPL-BACKEND` | Backend | L2 | Experimental |
| `TPL-FULLSTACK` | Full Stack | L2 | Experimental |
| `TPL-DOCUMENTATION` | Documentation | L2 | Experimental |

Estos Templates constituyen las composiciones canónicas disponibles actualmente en:

```text
framework/templates/repositories/
```

Otros tipos de proyecto podrán originar nuevos Repository Templates cuando exista un caso de uso real que justifique su incorporación.

Entre los tipos potenciales se encuentran:

```text
AI
Library
Website
```

Estos tipos no constituyen Templates oficiales mientras no dispongan de una especificación, composición, implementación y validación dentro del Framework.

Principio:

```text
Potential Project Type
        ↓
Real use case
        ↓
Template specification
        ↓
Implementation
        ↓
Validation
        ↓
Official Repository Template
```

La Repository Template Library evoluciona mediante necesidades reales y no mediante la creación anticipada de Templates.

---

# 162. TPL-BACKEND

`TPL-BACKEND` define la composición base para repositorios cuyo producto principal es una aplicación o servicio backend.

Características:

```text
project_type: Backend
maturity: L2
status: Experimental
```

La composición canónica del Template se mantiene en:

```text
framework/templates/repositories/backend/
```

El Template reutiliza Components relacionados con responsabilidades como:

- presentación del proyecto;
- arquitectura;
- API;
- persistencia;
- testing;
- documentación;
- despliegue;
- evolución del proyecto.

La selección exacta y sus requirement levels pertenecen a la especificación canónica del Template y no se duplican en este documento.

---

# 163. Backend Template Guidance

`TPL-BACKEND` no presupone un framework, lenguaje, base de datos o estrategia de despliegue concretos.

Puede aplicarse, entre otros, a proyectos desarrollados con:

- Spring Boot;
- FastAPI;
- Django;
- otros stacks backend equivalentes.

Tecnologías como Docker, Kubernetes, OpenAPI o sistemas de observabilidad deberán incorporarse únicamente cuando respondan a necesidades reales del proyecto.

El Template define responsabilidades.

El proyecto consumidor decide su implementación tecnológica.

---

# 164. TPL-FULLSTACK

`TPL-FULLSTACK` define la composición base para repositorios que integran responsabilidades frontend y backend dentro de un mismo proyecto.

Características:

```text
project_type: Full Stack
maturity: L2
status: Experimental
```

La composición canónica se mantiene en:

```text
framework/templates/repositories/fullstack/
```

El Template puede incorporar responsabilidades relacionadas con:

- presentación;
- arquitectura;
- frontend;
- backend;
- interfaces;
- persistencia;
- testing;
- documentación;
- despliegue.

La composición exacta deberá consultarse siempre en la especificación canónica del Template.

---

# 165. TPL-DOCUMENTATION

`TPL-DOCUMENTATION` define la composición base para repositorios cuyo producto principal es documentación técnica, conocimiento estructurado, estándares o guías.

Características:

```text
project_type: Documentation
maturity: L2
status: Experimental
```

La composición canónica se mantiene en:

```text
framework/templates/repositories/documentation/
```

El Template combina README Components y Documentation Components para proporcionar:

- identidad;
- estado;
- overview;
- navegación documental;
- arquitectura;
- estado operativo;
- historial de cambios;
- licencia;
- cierre y navegación.

GitHub Framework se utiliza como primera Reference Implementation de este Template mediante dogfooding y se encuentra actualmente en proceso de validación.

---

# 166. Future Repository Templates

La arquitectura admite la incorporación futura de nuevos tipos de Repository Template.

Entre los candidatos identificados se encuentran:

- AI;
- Library;
- Website.

Su presencia en esta lista no implica que formen parte actualmente de la Repository Template Library.

Un nuevo Template deberá incorporarse únicamente cuando:

- exista al menos un caso de uso real;
- los Components necesarios estén identificados;
- la composición pueda generalizarse;
- no pueda resolverse adecuadamente mediante un Template existente;
- exista una implementación que permita validarlo.

No se crearán Templates especulativos para cubrir escenarios todavía no utilizados.

---

# 167. Template Requirement Levels

Cada Repository Template clasifica sus Components mediante tres requirement levels.

## Required

Responsabilidades necesarias para satisfacer el contrato mínimo del Template.

La ausencia de uno de estos Components deberá considerarse una desviación y justificarse explícitamente.

## Recommended

Components que aportan valor habitual al tipo de repositorio, pero cuya necesidad depende del proyecto consumidor.

Su ausencia no invalida por sí sola la conformidad.

## Optional

Components aplicables únicamente cuando exista una necesidad concreta.

No deberán incorporarse para aumentar artificialmente la cobertura del Template.

El requirement level es contextual al Repository Template.

No modifica la prioridad, madurez o definición canónica del Component.

---

# 168. Template Composition Model

La composición de un Repository Template sigue el modelo:

```text
Repository Template
        │
        ├── Required
        │
        ├── Recommended
        │
        └── Optional
```

Los Maturity Profiles no mantienen una matriz global rígida de Components.

Dos Templates con la misma madurez pueden necesitar composiciones distintas.

Ejemplo conceptual:

```text
TPL-BACKEND
maturity: L2
        │
        └── Backend-oriented composition
```

```text
TPL-DOCUMENTATION
maturity: L2
        │
        └── Documentation-oriented composition
```

Por tanto:

```text
Same maturity
≠
Same components
```

La composición canónica pertenece siempre a cada Repository Template.

---

# 169. Workflow Composition

Los Repository Templates pueden requerir o recomendar Workflow Components cuando el tipo de proyecto y su contexto operativo lo justifiquen.

La madurez puede incrementar las expectativas de mantenimiento, pero no define por sí sola una matriz universal de workflows.

Principio:

```text
Project Type
+
Repository Needs
+
Maturity Expectations
        ↓
Appropriate Workflow Components
```

Un repositorio documental y un backend pueden compartir nivel L2 y, sin embargo, necesitar workflows diferentes.

Los Workflow Components deberán seleccionarse por responsabilidad y necesidad real.

---

# 170. Maturity Evolution

Un repositorio puede evolucionar progresivamente entre Maturity Profiles.

```text id="template007"
L1

↓

L2

↓

L3

↓

L4
```

Esta evolución no requiere recrear el repositorio ni sustituir necesariamente su Repository Template.

La promoción de madurez puede implicar:

- incorporar nuevos Components;
- reforzar documentación;
- mejorar workflows;
- introducir automatización;
- aumentar controles de calidad;
- formalizar gobernanza.

La evolución deberá responder a necesidades reales y no a la acumulación automática de Components.

---

# 171. Maturity Upgrade Checklist

Antes de promocionar la madurez de un repositorio deberá comprobarse:

- [ ] La necesidad de promoción está justificada.
- [ ] La metadata refleja la madurez objetivo.
- [ ] Los Required Components del Repository Template siguen satisfechos.
- [ ] Los nuevos Components incorporados responden a necesidades reales.
- [ ] La documentación refleja el nuevo nivel operativo.
- [ ] Los workflows necesarios están definidos.
- [ ] Los controles de calidad son adecuados.
- [ ] La gobernanza requerida está disponible.
- [ ] No se ha introducido complejidad únicamente para satisfacer el perfil.

---

# 172. Bootstrap Strategy

Todo nuevo repositorio basado en la RTL seguirá conceptualmente:

```text
Identify Project Type
        ↓
Select Repository Template
        ↓
Review Maturity
        ↓
Apply Required Components
        ↓
Evaluate Recommended Components
        ↓
Add Optional Components when justified
        ↓
Configure Workflows
        ↓
Validate
        ↓
Publish
```

El Template proporciona una base.

No sustituye las decisiones específicas del proyecto.

---

# 173. Automation Vision

La arquitectura de Repository Templates está preparada para soportar automatización futura.

Una herramienta podrá utilizar metadata canónica para:

```text
Select Repository Template
        ↓
Read Template Metadata
        ↓
Resolve Components
        ↓
Collect Parameters
        ↓
Materialize Repository
        ↓
Validate Result
```

La automatización deberá consumir las especificaciones existentes.

No deberá introducir una segunda definición de Templates o Components.

La generación automática no forma parte todavía del contrato de la RTL.

---

# 174. Template Versioning

Cada Repository Template mantiene versionado independiente.

Los cambios deberán reflejar la evolución de su contrato, composición o guidance.

La actualización de un Template no obliga automáticamente a migrar los repositorios consumidores.

Las migraciones deberán evaluarse según:

- impacto;
- compatibilidad;
- valor;
- necesidad real.

---

# 175. Compatibility Rules

Los Repository Templates deberán mantener compatibilidad razonable entre versiones siempre que sea posible.

Un cambio incompatible en el contrato deberá:

- estar justificado;
- documentarse;
- reflejarse en el versionado;
- proporcionar guidance de migración cuando existan consumidores afectados.

La compatibilidad se evaluará sobre responsabilidades y contratos, no sobre una estructura física rígida.

---

# 176. Anti-Patterns

No utilizar:

- Templates gigantes;
- Components innecesarios;
- Templates especulativos sin consumidor real;
- duplicación de especificaciones canónicas;
- matrices universales de Components basadas únicamente en madurez;
- estructuras físicas rígidas sin necesidad;
- requirement levels heredados sin evaluar el contexto;
- Templates distintos para proyectos equivalentes;
- Components creados únicamente para conseguir conformidad.

---

# 177. Quality Gates

Antes de aprobar un Repository Template deberá verificarse:

- [ ] El tipo de proyecto está claramente identificado.
- [ ] La madurez recomendada está definida.
- [ ] Los Components `required` representan el contrato mínimo.
- [ ] Los Components `recommended` aportan valor habitual.
- [ ] Los Components `optional` responden a escenarios reales.
- [ ] No se duplican especificaciones canónicas de Components.
- [ ] La estructura física no se impone sin necesidad.
- [ ] La composición puede reutilizarse en más de un proyecto equivalente.
- [ ] Existe un caso de uso real.
- [ ] El Template puede validarse mediante implementación, Reference Implementation o dogfooding.
- [ ] Las decisiones específicas del Template están documentadas.

---

# 178. Long-Term Vision

La Repository Template Library permitirá iniciar nuevos repositorios reutilizando composiciones validadas del Framework.

Cada Template representará una configuración mantenible de responsabilidades adaptada a un tipo de proyecto.

La evolución futura podrá incorporar:

- nuevos Repository Templates respaldados por casos reales;
- validación automática;
- resolución de Components;
- generación asistida;
- migraciones entre versiones.

La automatización deberá construirse sobre el modelo declarativo existente y no sustituirlo.

---

# 179. Part 6 Conclusions

La **Repository Template Library** transforma la creación de repositorios en un proceso basado en composición.

Los Repository Templates representan tipos de proyecto.

Los Maturity Profiles representan expectativas de evolución y mantenimiento.

Los Components representan responsabilidades reutilizables.

```text
Components
        ↓
Repository Templates
        ↓
Repository Implementation
        ↓
Maturity Evolution
```

Esta separación evita convertir la madurez en una segunda jerarquía de Templates y permite que proyectos diferentes compartan nivel de madurez sin necesitar la misma composición.

La RTL proporciona así una arquitectura extensible, reutilizable y preparada para futuras capacidades de validación y generación.

---

# 180. Part 6 Versioning

El versionado de esta Part se gestiona mediante el Revision History global del Repository Design System.

---

# 181. Purpose

Esta sección define la gobernanza oficial del **Repository Design System (RDS)**.

Su objetivo consiste en garantizar que el sistema:

* permanezca coherente;
* evolucione de forma controlada;
* mantenga compatibilidad;
* pueda aplicarse a futuros proyectos sin rediseños completos.

El RDS deja de ser un conjunto de documentos.

Se convierte en un producto mantenido.

---

# 182. Governance Philosophy

Todo elemento mantenido por el RDS deberá evolucionar siguiendo principios similares al software.

Cambios:

* pequeños;
* revisables;
* documentados;
* versionados;
* compatibles cuando sea posible.

---

# 183. Framework Element Lifecycle

Todo elemento reutilizable mantenido por el RDS deberá evolucionar mediante un ciclo controlado.

```text
Idea
    ↓
Specification
    ↓
Implementation
    ↓
Validation
    ↓
Adoption
    ↓
Maintenance
    ↓
Deprecation
    ↓
Retirement
```

Este ciclo podrá aplicarse, según corresponda, a:

- Framework Components;
- Repository Templates;
- convenciones reutilizables del Design System.

La implementación no implica estabilidad automática.

Un elemento deberá validarse mediante uso real, Reference Implementation o dogfooding antes de considerarse suficientemente maduro para adopción general.

No existirán elementos oficiales permanentes sin mantenimiento.

---

# 184. Framework Element States

Los elementos oficiales del RDS utilizarán, cuando corresponda, estados explícitos de evolución.

| State | Meaning |
|---|---|
| Draft | En diseño |
| Experimental | Implementado y en validación |
| Stable | Validado para uso recomendado |
| Deprecated | Sigue disponible, pero existe una alternativa preferida |
| Retired | Fuera del catálogo activo |

El estado deberá registrarse en la fuente canónica correspondiente.

El paso entre estados deberá estar respaldado por evidencia de implementación, validación o mantenimiento.

Los Repository Templates y Framework Components podrán evolucionar de forma independiente.

---

# 185. Component Registry

El **Component Catalog** constituye el registro central de los Framework Components reconocidos por el sistema.

El catálogo proporciona una vista global de:

- identificadores;
- familias;
- responsabilidades;
- prioridades;
- madurez;
- estado;
- relaciones relevantes.

Las especificaciones y metadata de cada Component constituyen su definición canónica cuando exista una implementación dentro de:

```text
framework/components/
```

Principio:

```text
Component Catalog
        ↓
Global discovery and classification

Component specification + metadata
        ↓
Canonical component definition
```

El catálogo no deberá duplicar en detalle las especificaciones mantenidas por cada Component.

Las diferencias entre catálogo y definición canónica deberán considerarse deuda del Design System y resolverse mediante sincronización.

---

# 186. Versioning Strategy

GitHub Framework utilizará Semantic Versioning para los artefactos versionables del RDS.

```text
Major.Minor.Patch
```

## Major

Cambios incompatibles en responsabilidades, contratos o modelos públicos.

## Minor

Nuevas capacidades compatibles, Components, Repository Templates o ampliaciones relevantes.

## Patch

Correcciones compatibles que no modifican sustancialmente el contrato.

Los Framework Components y Repository Templates podrán mantener versiones independientes de la versión global del proyecto.

Una nueva versión de GitHub Framework no obliga automáticamente a modificar la versión de todos sus elementos.

---

# 187. Compatibility Policy

La evolución del RDS deberá preservar compatibilidad razonable siempre que sea posible.

Los cambios incompatibles deberán:

- estar justificados;
- reflejarse en el versionado correspondiente;
- documentarse;
- identificar los consumidores afectados;
- proporcionar guidance de migración cuando sea necesario.

La compatibilidad se evaluará principalmente sobre responsabilidades y contratos.

No se garantizará compatibilidad con estructuras accidentales que no formen parte de una especificación canónica.

---

# 188. Deprecation Policy

Cuando un Framework Component, Repository Template u otro elemento oficial sea sustituido:

- cambiará su estado a `Deprecated`;
- permanecerá documentado durante un periodo razonable;
- indicará la alternativa recomendada;
- identificará las implicaciones de migración;
- mantendrá compatibilidad temporal cuando sea viable.

La retirada definitiva deberá producirse de forma explícita mediante el estado:

```text
Retired
```

Un elemento no desaparecerá del sistema activo sin una decisión documentada.

---

# 189. Ownership

Todo elemento mantenido por el RDS deberá tener ownership identificable.

Actualmente, el mantenimiento principal del sistema corresponde a:

```text
Owner

Fran Ramirez
```

En el futuro podrán existir varios Maintainers o responsables especializados por familia, Component o Repository Template.

El ownership deberá permitir identificar quién puede:

- mantener la especificación;
- revisar cambios;
- resolver inconsistencias;
- aprobar evolución relevante.

---

# 190. Framework Review

Los elementos del RDS deberán revisarse cuando:

- aparezca una nueva necesidad real;
- se detecte duplicación;
- una Reference Implementation revele un gap;
- el dogfooding contradiga una decisión existente;
- evolucione GitHub o una dependencia relevante;
- cambie la estrategia del Framework;
- aparezca deuda de diseño;
- una especificación diverja de su implementación.

La revisión deberá favorecer:

```text
Reuse
before
Extension
before
New Element
```

No toda necesidad específica deberá originar un nuevo Component o Template.

---

# 191. Repository Bootstrap

Todo nuevo proyecto que adopte el Framework seguirá conceptualmente:

```text
Identify Project Type
        ↓
Select Repository Template
        ↓
Review Template Maturity
        ↓
Apply Required Components
        ↓
Evaluate Recommended Components
        ↓
Add Optional Components when justified
        ↓
Configure Project-specific Needs
        ↓
Validate
        ↓
Publish
```

El Maturity Profile no se selecciona como un Template independiente.

La madurez constituye una propiedad y una expectativa de evolución del repositorio.

El proceso de bootstrap deberá reutilizar las definiciones canónicas existentes y evitar recrear Components manualmente cuando ya exista una especificación aplicable.

---

# 192. Repository Validation

La validación de un repositorio deberá comprobar su conformidad con las responsabilidades y contratos que realmente le correspondan.

Flujo conceptual:

```text
Repository Template
        ↓
Required Components
        ↓
Repository Implementation
        ↓
Conformance Analysis
        ↓
Consumer Gaps / Template Gaps
        ↓
Validation Result
```

La validación podrá incluir, según el contexto:

- conformidad con el Repository Template;
- presencia y correcta materialización de Required Components;
- metadata;
- documentación;
- workflows;
- calidad;
- GRS Assessment cuando corresponda.

La ausencia de un Component `recommended` u `optional` no deberá considerarse automáticamente un defecto.

Las desviaciones deberán clasificarse antes de modificar el repositorio o el Framework.

---

# 193. Continuous Improvement

El sistema deberá mejorar mediante evidencia obtenida de implementaciones reales.

Cada nuevo proyecto podrá revelar:

- oportunidades de reutilización;
- mejoras de Components;
- simplificaciones;
- gaps de Repository Templates;
- necesidades de nuevos Components;
- candidatos a nuevos Templates;
- decisiones específicas que no deban generalizarse.

Principio:

```text
Project-specific need
        ↓
Evaluate
        ├── Existing Component
        ├── Existing Template
        ├── Framework improvement
        └── Keep project-specific
```

No toda variación deberá incorporarse al Framework.

La generalización requerirá evidencia de reutilización potencial.

---

# 194. Design Debt

El propio Design System puede acumular deuda.

Ejemplos:

- Components redundantes;
- Repository Templates obsoletos;
- documentación divergente;
- metadata desincronizada;
- modelos arquitectónicos históricos todavía presentes;
- diagramas antiguos;
- especificaciones que no reflejan la implementación;
- duplicación de fuentes de verdad.

La deuda del Design System deberá gestionarse igual que la deuda técnica:

```text
Detect
    ↓
Classify
    ↓
Prioritize
    ↓
Resolve
    ↓
Validate
```

El dogfooding constituye una fuente principal para detectar esta deuda.

---

# 195. Design Backlog

Las mejoras, gaps y deuda del Design System deberán registrarse mediante los mecanismos de planificación de GitHub Framework.

Las fuentes principales son:

```text
GitHub Issues
+
docs/governance/14_BACKLOG.md
```

Los findings derivados de:

- dogfooding;
- Reference Implementations;
- auditorías;
- implementación de Components;
- implementación de Repository Templates;

deberán convertirse en trabajo trazable cuando requieran actuación.

No se mantendrá un backlog paralelo del RDS que pueda divergir del sistema de gobierno del proyecto.

---

# 196. Repository Migration

Un repositorio existente podrá adoptar GitHub Framework de forma incremental.

La migración seguirá conceptualmente:

```text
Repository Assessment
        ↓
Identify Project Type
        ↓
Select Repository Template
        ↓
Conformance Analysis
        ↓
Gap Classification
        ↓
Migration Plan
        ↓
Implementation
        ↓
Validation
```

Los gaps deberán distinguir, cuando corresponda, entre:

- Consumer Gaps;
- Template Gaps;
- Component Gaps;
- documentación o metadata desactualizada.

La migración no deberá perseguir conformidad mecánica.

Solo se incorporarán Components que respondan al contrato del Template o a necesidades reales del repositorio.

No será necesario recrear un repositorio para adoptar el Framework.

---

# 197. Repository Audit

Los repositorios que adopten GitHub Framework podrán revisarse periódicamente para detectar:

- divergencias respecto a su Repository Template;
- Components desactualizados;
- documentación obsoleta;
- metadata inconsistente;
- deuda de mantenimiento;
- problemas de seguridad;
- oportunidades de simplificación.

La frecuencia dependerá de:

- criticidad;
- actividad;
- madurez;
- ritmo de evolución;
- necesidades de mantenimiento.

Las auditorías también podrán ejecutarse cuando:

- cambie el Repository Template;
- exista una migración;
- se prepare una release relevante;
- aparezcan problemas de conformidad;
- una Reference Implementation revele nueva deuda.

---

# 198. Metrics

El RDS podrá utilizar métricas para evaluar su efectividad.

Entre ellas:

- reutilización de Components;
- adopción de Repository Templates;
- consistencia;
- mantenibilidad;
- tiempo de creación;
- calidad documental;
- gaps detectados mediante dogfooding;
- esfuerzo necesario para migraciones.

Las métricas deberán utilizarse para mejorar decisiones.

No deberán convertirse en objetivos artificiales de cobertura o acumulación de Components.

---

# 199. Repository Health

GitHub Framework podrá incorporar en el futuro mecanismos para evaluar el estado general de un repositorio.

Una evaluación de salud podría considerar:

```text
Template Conformance
+
Maintenance
+
Documentation
+
Quality
+
Security
+
Repository Activity
```

Los niveles, métricas y algoritmos concretos deberán definirse antes de constituir una capacidad oficial del Framework.

Repository Health se considera actualmente una capacidad potencial y no un contrato implementado del RDS.

---

# 200. Automation Roadmap

La evolución del Framework podrá automatizar progresivamente tareas repetitivas basadas en especificaciones canónicas.

Entre ellas:

- resolución de Repository Templates;
- generación asistida de repositorios;
- materialización de Components;
- generación de README;
- validación Markdown;
- validación de metadata;
- comprobación de enlaces;
- análisis de conformidad;
- auditorías;
- soporte a releases.

La automatización deberá consumir Components, Templates y metadata existentes.

No deberá introducir una segunda fuente de verdad.

Las capacidades se implementarán únicamente cuando exista suficiente estabilidad del modelo que automatizan.

---

# 201. Design System Evolution

La evolución del Repository Design System se realizará incrementalmente.

Las capacidades actualmente definidas incluyen:

- README Components;
- Documentation Components;
- Workflow Components;
- Visual Components;
- Repository Templates;
- Maturity Profiles;
- Governance.

La implementación física de estas capacidades podrá avanzar a ritmos diferentes.

Entre las líneas de evolución potencial se encuentran:

- ampliación de Component Libraries;
- nuevos Repository Templates respaldados por casos reales;
- validación automática;
- generación asistida;
- Automation Components;
- AI-assisted generation;
- análisis de Repository Health;
- herramientas de migración.

La planificación concreta se mantendrá en los mecanismos de gobierno del proyecto y no se duplicará en este documento.

---

# 202. Repository Ecosystem

GitHub Framework está diseñado para soportar múltiples repositorios y tipos de proyecto.

El sistema podrá ser consumido por:

- repositorios backend;
- proyectos full stack;
- repositorios documentales;
- GitHub Profile;
- proyectos de aprendizaje;
- futuros tipos de repositorio.

El nivel de madurez de estos consumidores constituye una dimensión independiente de su tipo de proyecto.

---

# 203. Repository Design Principles

El sistema mantendrá como principios operativos:

- reutilizar antes que duplicar;
- extender antes que crear;
- documentar antes que automatizar;
- automatizar antes que repetir;
- validar mediante uso real;
- evolucionar antes que reemplazar;
- mantener una única fuente canónica;
- evitar complejidad sin necesidad.

Estos principios deberán prevalecer sobre la búsqueda de cobertura total o uniformidad artificial.

---

# 204. Anti-Patterns

No deberán aparecer:

- Components duplicados;
- Repository Templates incompatibles para necesidades equivalentes;
- Templates sin mantener;
- Templates especulativos;
- automatizaciones huérfanas;
- documentación divergente;
- metadata desincronizada;
- múltiples fuentes de verdad;
- decisiones arquitectónicas no registradas;
- conformidad conseguida mediante Components innecesarios;
- reglas de madurez utilizadas como composición rígida.

---

# 205. RDS Quality Gates

Antes de aprobar una evolución relevante del Repository Design System deberá verificarse:

- [ ] Los Components afectados están registrados.
- [ ] Los Repository Templates afectados están sincronizados.
- [ ] La metadata refleja la implementación.
- [ ] La compatibilidad ha sido evaluada.
- [ ] La documentación está actualizada.
- [ ] Las fuentes canónicas no se contradicen.
- [ ] Los ejemplos o Reference Implementations siguen siendo válidos.
- [ ] Los gaps detectados están resueltos o registrados.
- [ ] La gobernanza refleja los cambios relevantes.
- [ ] No se ha introducido duplicación innecesaria.

---

# 206. Definition of Done

Una capacidad del Repository Design System se considerará implementada cuando:

## Specification

- [ ] Su responsabilidad esté definida.
- [ ] Su alcance y límites sean claros.
- [ ] La fuente canónica esté identificada.

## Implementation

- [ ] Exista una implementación cuando la capacidad la requiera.
- [ ] La metadata esté sincronizada.
- [ ] No duplique responsabilidades existentes.

## Validation

- [ ] Exista evidencia de uso real, Reference Implementation o dogfooding.
- [ ] Los gaps encontrados estén resueltos o registrados.
- [ ] Los Quality Gates aplicables estén satisfechos.

## Governance

- [ ] El cambio sea trazable.
- [ ] La documentación de gobierno esté actualizada cuando corresponda.
- [ ] El versionado refleje cambios contractuales relevantes.

La existencia de futuras capacidades de automatización no será requisito para considerar implementado el modelo actual.

---

# 207. Long-Term Vision

GitHub Framework deberá proporcionar una base reutilizable para construir, evolucionar y mantener repositorios técnicos.

El Repository Design System constituye su modelo arquitectónico para organizar:

- Components;
- Repository Templates;
- Maturity Profiles;
- reglas de composición;
- validación;
- gobernanza.

El objetivo no consiste únicamente en producir repositorios visualmente atractivos.

Consiste en crear un ecosistema:

- coherente;
- profesional;
- reutilizable;
- mantenible;
- verificable;
- preparado para evolucionar durante muchos años.

La automatización futura deberá ampliar este modelo sin sustituir sus fuentes canónicas.

---

# 208. Final Conclusions

El **Repository Design System** proporciona el modelo arquitectónico de GitHub Framework.

Los estándares definen reglas y criterios.

Los Framework Components encapsulan responsabilidades reutilizables.

Los Repository Templates componen esas responsabilidades según tipos de proyecto.

Los Maturity Profiles expresan expectativas de evolución y mantenimiento.

La gobernanza controla su ciclo de vida.

```text
Standards
        ↓
Framework Components
        ↓
Repository Templates
        ↓
Repository Implementations
        ↓
Validation and Evolution
```

Los repositorios que adopten GitHub Framework no deberán diseñar desde cero responsabilidades ya resueltas por el sistema.

Al mismo tiempo, el Framework no impondrá Components, estructuras o automatizaciones que no respondan a necesidades reales.

El resultado es una arquitectura orientada a reutilización, consistencia, trazabilidad y evolución incremental.

---

# 209. Next Evolution

El Repository Design System ha evolucionado desde una especificación documental hacia una implementación reutilizable dentro de GitHub Framework.

La siguiente etapa consiste en consolidar la correspondencia entre:

```text
Design System
        ↓
Framework Components
        ↓
Repository Templates
        ↓
Reference Implementations
```

Las prioridades de evolución deberán centrarse en:

- completar la implementación física de Components definidos;
- validar Repository Templates mediante consumidores reales;
- resolver gaps detectados mediante dogfooding;
- mantener sincronizados RDS, Component Catalog y metadata;
- ampliar el Framework únicamente a partir de necesidades demostradas;
- preparar progresivamente capacidades de validación y automatización.

GitHub Framework constituye la plataforma reutilizable.

El RDS constituye su modelo arquitectónico.

La evolución futura deberá preservar esta separación.

---

# 210. Revision History

| Version | Date       | Description |
| ------- | ---------- | ----------- |
| 1.0.0   | 2026-08-05 | Primera versión completa del Repository Design System. |
| 1.0.1   | 2026-08-11 | Metadata alineada con GitHub Framework durante la implementación de referencia del Documentation Framework. |
| 1.1.0   | 2026-08-14 | Arquitectura del RDS consolidada alrededor de Framework Components, Repository Templates, requirement levels contextuales, Maturity Profiles independientes y fuentes canónicas sincronizadas con la implementación. |