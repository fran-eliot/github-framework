# 09 - COMPONENT CATALOG

| Field        | Value                     |
| ------------ | ------------------------- |
| **Project**  | GitHub Framework          |
| **Document** | Component Catalog         |
| **Version**  | 1.0.1                     |
| **Status**   | Stable                    |
| **Owner**    | Fran Ramirez              |

---

# Part 1/4

# Registry Foundations

---

# 1. Purpose

El **Component Catalog (CC)** constituye el registro maestro de todos los componentes oficiales del GitHub Framework.

Su función consiste en proporcionar una referencia única para identificar, clasificar, localizar y reutilizar cualquier componente definido en el ecosistema.

Mientras el **Repository Design System (RDS)** define la filosofía y el comportamiento de los componentes, el Component Catalog mantiene su inventario oficial.

---

# 2. Vision

El catálogo deberá convertirse en la referencia principal para cualquier nuevo repositorio.

Antes de crear una solución nueva, deberá consultarse este documento para comprobar si ya existe un componente reutilizable.

---

# 3. Relationship with Other Documents

| Document                 | Responsibility           |
| ------------------------ | ------------------------ |
| Repository Design System | Define los componentes   |
| Component Catalog        | Registra los componentes |
| Repository Templates     | Seleccionan componentes  |
| Repository Standards     | Definen reglas           |
| README Implementation    | Implementa componentes   |

El catálogo nunca duplicará especificaciones completas.

Siempre enlazará a ellas.

---

# 4. Component Registry Philosophy

Cada componente deberá existir una única vez.

No podrán coexistir dos componentes distintos con el mismo propósito.

Cuando aparezca una necesidad nueva deberá evaluarse primero si:

* existe un componente equivalente;
* puede ampliarse uno existente;
* puede parametrizarse;
* realmente es necesaria una nueva definición.

---

# 5. Registry Architecture

El catálogo se organiza mediante familias.

```text id="cc001"
README

↓

Documentation

↓

Workflow

↓

Visual

↓

Template

↓

Profile
```

Cada componente pertenecerá exactamente a una familia principal.

---

# 6. Component Identifier

Todo componente dispondrá de un identificador único.

Formato.

```text id="cc002"
PREFIX-NAME
```

Ejemplos.

```text id="cc003"
README-HERO

DOC-ADR

WCL-CI

VCL-BANNER

TPL-BACKEND

PROFILE-SOLO
```

Los identificadores serán permanentes.

---

# 7. Naming Rules

Los identificadores deberán cumplir:

* inglés;
* mayúsculas;
* guiones;
* sin abreviaturas ambiguas;
* estables entre versiones.

Nunca deberán reutilizarse para otro componente.

---

# 8. Component Metadata

Cada componente tendrá una ficha mínima.

| Field        | Description              |
| ------------ | ------------------------ |
| ID           | Identificador            |
| Name         | Nombre                   |
| Family       | Familia                  |
| Version      | Versión                  |
| Status       | Estado                   |
| Owner        | Responsable              |
| Dependencies | Componentes relacionados |
| Used By      | Plantillas donde aparece |

---

# 9. Component States

Todo componente tendrá un estado.

| State        | Meaning         |
| ------------ | --------------- |
| Draft        | Diseño inicial  |
| Experimental | Validación      |
| Stable       | Uso recomendado |
| Deprecated   | Sustituido      |
| Retired      | Eliminado       |

Los estados deberán comunicarse claramente.

---

# 10. Component Versioning

Cada componente seguirá Semantic Versioning.

Ejemplos.

```text id="cc004"
README-HERO

1.0.0
```

```text id="cc005"
VCL-BANNER

2.1.0
```

La evolución de un componente no implica la actualización inmediata del resto del sistema.

---

# 11. Component Families

El catálogo oficial define inicialmente seis familias.

| Prefix  | Family                   |
| ------- | ------------------------ |
| README  | README Components        |
| DOC     | Documentation Components |
| WCL     | Workflow Components      |
| VCL     | Visual Components        |
| TPL     | Repository Templates     |
| PROFILE | Repository Profiles      |

La incorporación de nuevas familias requerirá una revisión del RDS.

---

# 12. Component Hierarchy

Los componentes podrán depender de otros.

Ejemplo.

```text id="cc006"
README-ARCHITECTURE

↓

DOC-ARCHITECTURE

↓

DOC-ADR
```

Las dependencias deberán declararse explícitamente.

---

# 13. Component Dependency Types

Se distinguen tres tipos.

## Required

Necesario para funcionar.

---

## Recommended

Mejora el componente.

---

## Optional

Añade capacidades sin dependencia funcional.

---

# 14. Component Consumers

Un componente podrá utilizarse por:

* README;
* documentación;
* repositorios;
* GitHub Profile;
* GitHub Pages;
* scripts;
* plantillas.

---

# 15. Component Reuse

El mismo componente podrá aparecer en múltiples proyectos.

Ejemplo.

```text id="cc007"
README-QUICK-START
```

utilizado por:

* NovaCoquinaria;
* OnlyFilm;
* Aula Robótica;
* Cognitiva AI.

El componente seguirá siendo único.

---

# 16. Component Ownership

Cada componente tendrá un responsable.

Actualmente.

```text id="cc008"
Fran Ramirez
```

En proyectos colaborativos podrán existir varios mantenedores.

---

# 17. Component Lifecycle

Todo componente seguirá.

```text id="cc009"
Idea

↓

Specification

↓

Registry

↓

Template

↓

Implementation

↓

Maintenance

↓

Retirement
```

La inclusión en el catálogo implica que el componente existe oficialmente.

---

# 18. Registry Categories

Los componentes se agrupan además por criticidad.

## Core

Fundamentales para el Framework.

---

## Standard

Uso habitual.

---

## Optional

Especializados.

---

## Legacy

Conservados por compatibilidad.

---

# 19. Registry Attributes

Además de la metadata básica, podrán registrarse.

* prioridad;
* audiencia;
* nivel de madurez;
* complejidad;
* reutilización esperada;
* fecha de creación;
* última revisión.

---

# 20. Audience Classification

Cada componente indicará su audiencia principal.

| Audience    | Purpose            |
| ----------- | ------------------ |
| Recruiter   | Perfil profesional |
| Developer   | Ingeniería         |
| Contributor | Colaboración       |
| Maintainer  | Mantenimiento      |
| All         | Uso general        |

Esta clasificación facilitará la composición automática de README y plantillas.

---

# 21. Priority Levels

Los componentes se clasificarán como:

| Priority    | Meaning         |
| ----------- | --------------- |
| Required    | Obligatorio     |
| Recommended | Muy recomendado |
| Optional    | Contextual      |

No todos los proyectos utilizarán los mismos componentes.

---

# 22. Maturity Mapping

Cada componente indicará el nivel mínimo recomendado.

| Level | Description  |
| ----- | ------------ |
| L1    | Experimental |
| L2    | Public Basic |
| L3    | Supporting   |
| L4    | Strategic    |

---

# 23. Registry Navigation

El catálogo deberá permitir localizar un componente mediante:

* identificador;
* familia;
* nivel;
* audiencia;
* prioridad;
* plantilla;
* proyecto.

---

# 24. Registry Principles

El catálogo seguirá estos principios.

* una única fuente de verdad;
* nomenclatura estable;
* sin duplicados;
* documentación enlazada;
* evolución controlada.

---

# 25. Anti-Patterns

No deberán aparecer.

* identificadores repetidos;
* familias ambiguas;
* componentes sin propietario;
* dependencias ocultas;
* componentes sin documentación;
* versiones incompatibles sin registrar.

---

# 26. Quality Gates

Antes de registrar un nuevo componente deberán verificarse.

* [ ] Identificador único.
* [ ] Familia asignada.
* [ ] Metadata completa.
* [ ] Estado definido.
* [ ] Dependencias documentadas.
* [ ] Nivel de prioridad.
* [ ] Audiencia.
* [ ] Referencia al documento de especificación.

---

# 27. Long-Term Vision

El Component Catalog deberá convertirse en el equivalente a la documentación de una biblioteca de componentes.

Todo el ecosistema GitHub podrá construirse consultando este registro.

Los componentes dejarán de ser elementos dispersos para convertirse en activos reutilizables y gobernados.

---

# 28. Part 1 Conclusions

El **Component Catalog** constituye el inventario oficial del GitHub Framework.

Gracias a él, cada componente tendrá una identidad permanente, una clasificación clara y una relación explícita con el resto del sistema.

Este registro permitirá que el Framework evolucione de forma ordenada, manteniendo la coherencia entre estándares, plantillas e implementaciones.

---

# 29. Revision History

| Version | Date       | Description                                                                  |
| ------- | ---------- | ---------------------------------------------------------------------------- |
| 1.0.0   | 2026-08-05 | Primera definición del registro maestro de componentes del GitHub Framework. |

---

# 09 - COMPONENT CATALOG

# Part 2/4

# README & Documentation Components Registry

---

# 30. Purpose

Esta sección constituye el registro oficial de todos los componentes pertenecientes a las familias:

* README Components (`README-*`)
* Documentation Components (`DOC-*`)

Su objetivo es proporcionar una referencia unificada para la construcción de README y sistemas documentales.

---

# 31. README Component Family

## Prefix

```text id="cc010"
README
```

---

## Purpose

Construir README modulares, reutilizables y consistentes.

---

## Consumer

* GitHub Repository
* GitHub Profile
* GitHub Pages
* Documentation Landing Pages

---

## Dependencies

Puede depender de:

* DOC
* VCL

Nunca dependerá directamente de WCL.

---

# 32. README Component Registry

| ID                          | Name                 | Priority    | Audience    | Maturity |
| --------------------------- | -------------------- | ----------- | ----------- | -------- |
| README-HERO                 | Hero Section         | Required    | All         | L1       |
| README-STATUS               | Project Status       | Required    | All         | L2       |
| README-OVERVIEW             | Project Overview     | Required    | All         | L1       |
| README-HIGHLIGHTS           | Highlights           | Recommended | Recruiter   | L2       |
| README-FEATURES             | Features             | Required    | All         | L2       |
| README-ARCHITECTURE         | Architecture         | Recommended | Developer   | L3       |
| README-TECH-STACK           | Tech Stack           | Required    | All         | L2       |
| README-REPOSITORY-STRUCTURE | Repository Structure | Recommended | Developer   | L3       |
| README-QUICK-START          | Quick Start          | Required    | Developer   | L2       |
| README-DOCUMENTATION        | Documentation        | Required    | Developer   | L2       |
| README-DEMO                 | Demo                 | Optional    | Recruiter   | L2       |
| README-TESTING              | Testing              | Recommended | Developer   | L3       |
| README-ROADMAP              | Roadmap              | Recommended | Maintainer  | L3       |
| README-CONTRIBUTING         | Contributing         | Optional    | Contributor | L3       |
| README-LICENSE              | License              | Required    | All         | L2       |
| README-AUTHOR               | Author               | Recommended | Recruiter   | L2       |
| README-FOOTER               | Footer               | Required    | All         | L1       |

---

# 33. README Core Components

Constituyen el mínimo obligatorio para un repositorio estratégico.

```text id="cc011"
README-HERO

README-STATUS

README-OVERVIEW

README-FEATURES

README-TECH-STACK

README-QUICK-START

README-DOCUMENTATION

README-LICENSE

README-FOOTER
```

---

# 34. README Extended Components

Aportan profundidad técnica.

```text id="cc012"
README-ARCHITECTURE

README-TESTING

README-ROADMAP

README-HIGHLIGHTS

README-AUTHOR

README-REPOSITORY-STRUCTURE
```

---

# 35. README Optional Components

Solo deberán utilizarse cuando exista una necesidad clara.

```text id="cc013"
README-DEMO

README-CONTRIBUTING
```

---

# 36. README Dependency Graph

```text id="cc014"
README-HERO

↓

README-OVERVIEW

↓

README-FEATURES

↓

README-ARCHITECTURE

↓

README-DOCUMENTATION

↓

DOC-ARCHITECTURE
```

La profundidad siempre aumentará progresivamente.

---

# 37. Documentation Component Family

## Prefix

```text id="cc015"
DOC
```

---

## Purpose

Construir sistemas documentales completos.

---

## Consumer

* Documentation
* MkDocs
* GitHub Wiki
* GitHub Pages

---

# 38. Documentation Component Registry

| ID                 | Name                         | Priority    | Audience   | Maturity |
| ------------------ | ---------------------------- | ----------- | ---------- | -------- |
| DOC-ARCHITECTURE   | Architecture                 | Required    | Developer  | L3       |
| DOC-ADR            | Architecture Decision Record | Recommended | Developer  | L3       |
| DOC-ROADMAP        | Roadmap                      | Recommended | Maintainer | L3       |
| DOC-PROJECT-STATUS | Project Status               | Required    | Maintainer | L2       |
| DOC-KNOWN-ISSUES   | Known Issues                 | Recommended | Maintainer | L3       |
| DOC-CHANGELOG      | Changelog                    | Required    | All        | L2       |
| DOC-RELEASE-NOTES  | Release Notes                | Recommended | All        | L3       |
| DOC-API            | API Documentation            | Optional    | Developer  | L3       |
| DOC-DATABASE       | Database Documentation       | Optional    | Developer  | L3       |
| DOC-DEPLOYMENT     | Deployment Guide             | Optional    | Developer  | L3       |
| DOC-TESTING        | Testing Strategy             | Recommended | Developer  | L3       |
| DOC-SECURITY       | Security                     | Recommended | Developer  | L3       |
| DOC-DIAGRAMS       | Diagrams                     | Recommended | Developer  | L3       |
| DOC-GLOSSARY       | Glossary                     | Optional    | All        | L4       |
| DOC-REFERENCES     | References                   | Recommended | All        | L2       |

---

# 39. Documentation Core Components

```text id="cc016"
DOC-ARCHITECTURE

DOC-PROJECT-STATUS

DOC-CHANGELOG

DOC-REFERENCES
```

---

# 40. Documentation Extended Components

```text id="cc017"
DOC-ADR

DOC-ROADMAP

DOC-KNOWN-ISSUES

DOC-RELEASE-NOTES

DOC-TESTING

DOC-SECURITY

DOC-DIAGRAMS
```

---

# 41. Documentation Specialized Components

```text id="cc018"
DOC-API

DOC-DATABASE

DOC-DEPLOYMENT

DOC-GLOSSARY
```

Estos componentes dependerán del tipo de proyecto.

---

# 42. Documentation Dependency Graph

```text id="cc019"
DOC-ARCHITECTURE

↓

DOC-ADR

↓

DOC-DIAGRAMS

↓

DOC-REFERENCES
```

---

# 43. Repository Mapping

## Backend

```text id="cc020"
DOC-API

DOC-DATABASE

DOC-DEPLOYMENT

DOC-TESTING
```

---

## AI

```text id="cc021"
DOC-ARCHITECTURE

DOC-DIAGRAMS

DOC-REFERENCES
```

---

## Documentation

```text id="cc022"
DOC-ARCHITECTURE

DOC-ADR

DOC-GLOSSARY

DOC-REFERENCES
```

---

## Full Stack

```text id="cc023"
Todos excepto los específicos no aplicables.
```

---

# 44. Reuse Matrix

| Component         | README | Docs | GitHub Profile | Templates |
| ----------------- | :----: | :--: | :------------: | :-------: |
| README-HERO       |    ✓   |      |        ✓       |     ✓     |
| README-TECH-STACK |    ✓   |      |        ✓       |     ✓     |
| README-ROADMAP    |    ✓   |      |                |     ✓     |
| DOC-ARCHITECTURE  |        |   ✓  |                |     ✓     |
| DOC-ADR           |        |   ✓  |                |     ✓     |
| DOC-CHANGELOG     |        |   ✓  |                |     ✓     |
| DOC-DIAGRAMS      |        |   ✓  |                |     ✓     |

---

# 45. Lifecycle

Todos los componentes de estas familias seguirán el mismo ciclo.

```text id="cc024"
Draft

↓

Stable

↓

Deprecated

↓

Retired
```

---

# 46. Registry Evolution Rules

Un nuevo componente README o DOC solo podrá añadirse cuando:

* no exista uno equivalente;
* aporte una responsabilidad nueva;
* pueda reutilizarse;
* esté documentado;
* tenga un caso de uso claro.

---

# 47. Anti-Patterns

No deberán existir:

* dos componentes para la misma finalidad;
* README que replique documentación extensa;
* documentos técnicos duplicados;
* dependencias circulares entre README y DOC.

---

# 48. Quality Gates

Antes de registrar un componente deberán verificarse.

* [ ] Identificador único.
* [ ] Nombre consistente.
* [ ] Prioridad asignada.
* [ ] Audiencia definida.
* [ ] Nivel mínimo de madurez.
* [ ] Dependencias documentadas.
* [ ] Documento de especificación existente.

---

# 49. Long-Term Vision

Las familias README y DOC constituirán el núcleo documental del GitHub Framework.

Todos los proyectos del ecosistema compartirán estos componentes, garantizando consistencia, reutilización y facilidad de mantenimiento.

Con el tiempo, será posible generar automáticamente README y documentación seleccionando únicamente los componentes necesarios.

---

# 50. Part 2 Conclusions

El registro oficial de componentes **README** y **Documentation** proporciona un vocabulario común para todo el ecosistema.

Cada sección del README y cada documento técnico pasan a formar parte de un catálogo gobernado, con una identidad propia, un nivel de madurez y una audiencia definida.

Esto permitirá construir repositorios consistentes sin volver a diseñar la documentación en cada proyecto.

---

# 51. Revision History

| Version | Date       | Description                                             |
| ------- | ---------- | ------------------------------------------------------- |
| 1.0.0   | 2026-08-05 | Registro inicial de componentes README y Documentation. |

---

# 09 - COMPONENT CATALOG

# Part 3/4

# Workflow & Visual Components Registry

---

# 52. Purpose

Esta sección registra oficialmente las familias:

* Workflow Components (`WCL-*`)
* Visual Components (`VCL-*`)

Estas familias constituyen la capa operativa y visual del GitHub Framework.

Mientras los componentes README y DOC explican un proyecto, los componentes WCL y VCL definen cómo se desarrolla y cómo se presenta.

---

# 53. Workflow Component Family

## Prefix

```text id="cc025"
WCL
```

---

## Purpose

Definir procesos reutilizables para el desarrollo, revisión, publicación y mantenimiento de repositorios.

---

## Consumer

* GitHub
* GitHub Actions
* Project Boards
* Pull Requests
* Releases

---

## Dependencies

Puede utilizar:

* README
* DOC
* VCL

---

# 54. Workflow Component Registry

| ID                       | Name                   | Priority    | Audience   | Maturity |
| ------------------------ | ---------------------- | ----------- | ---------- | -------- |
| WCL-ISSUE                | Issue Template         | Required    | Maintainer | L2       |
| WCL-LABEL                | Labels                 | Required    | Maintainer | L2       |
| WCL-PROJECT              | Project Board          | Recommended | Maintainer | L3       |
| WCL-BRANCH               | Branch Strategy        | Required    | Developer  | L2       |
| WCL-COMMIT               | Commit Convention      | Required    | Developer  | L2       |
| WCL-PULL-REQUEST         | Pull Request           | Required    | Developer  | L2       |
| WCL-CODE-REVIEW          | Code Review            | Recommended | Developer  | L3       |
| WCL-CI                   | Continuous Integration | Recommended | Developer  | L3       |
| WCL-CD                   | Continuous Delivery    | Optional    | Maintainer | L4       |
| WCL-DEPENDABOT           | Dependency Updates     | Recommended | Maintainer | L3       |
| WCL-SECURITY             | Security Workflow      | Recommended | Developer  | L3       |
| WCL-RELEASE              | Release Workflow       | Recommended | Maintainer | L3       |
| WCL-HOTFIX               | Hotfix Workflow        | Optional    | Developer  | L3       |
| WCL-DOCUMENTATION-UPDATE | Documentation Sync     | Recommended | Maintainer | L3       |
| WCL-ASSESSMENT           | GRS Assessment         | Required    | Maintainer | L4       |
| WCL-MAINTENANCE          | Maintenance Cycle      | Recommended | Maintainer | L3       |

---

# 55. Workflow Core Components

```text id="cc026"
WCL-ISSUE

WCL-LABEL

WCL-BRANCH

WCL-COMMIT

WCL-PULL-REQUEST

WCL-ASSESSMENT
```

---

# 56. Workflow Extended Components

```text id="cc027"
WCL-CODE-REVIEW

WCL-CI

WCL-DEPENDABOT

WCL-RELEASE

WCL-DOCUMENTATION-UPDATE

WCL-MAINTENANCE
```

---

# 57. Workflow Specialized Components

```text id="cc028"
WCL-CD

WCL-HOTFIX

WCL-SECURITY

WCL-PROJECT
```

Su utilización dependerá del tipo de proyecto.

---

# 58. Workflow Dependency Graph

```text id="cc029"
WCL-ISSUE

↓

WCL-BRANCH

↓

WCL-COMMIT

↓

WCL-PULL-REQUEST

↓

WCL-CODE-REVIEW

↓

WCL-CI

↓

WCL-RELEASE

↓

WCL-MAINTENANCE
```

---

# 59. Workflow Capability Mapping

| Component        | Primary Capability        |
| ---------------- | ------------------------- |
| WCL-BRANCH       | Git Strategy              |
| WCL-COMMIT       | Version Control           |
| WCL-PULL-REQUEST | Collaborative Development |
| WCL-CODE-REVIEW  | Code Quality              |
| WCL-CI           | Continuous Integration    |
| WCL-CD           | DevOps                    |
| WCL-SECURITY     | Secure Development        |
| WCL-RELEASE      | Release Management        |
| WCL-ASSESSMENT   | Engineering Governance    |

---

# 60. Visual Component Family

## Prefix

```text id="cc030"
VCL
```

---

## Purpose

Construir una identidad visual consistente para todos los repositorios del ecosistema.

---

## Consumer

* README
* GitHub Profile
* GitHub Pages
* Portfolio

---

## Dependencies

No depende funcionalmente de WCL.

Puede complementar componentes README.

---

# 61. Visual Component Registry

| ID                       | Name                 | Priority    | Audience  | Maturity |
| ------------------------ | -------------------- | ----------- | --------- | -------- |
| VCL-BANNER               | Repository Banner    | Recommended | Recruiter | L3       |
| VCL-SOCIAL-PREVIEW       | Social Preview       | Recommended | Recruiter | L3       |
| VCL-HERO                 | Hero Layout          | Required    | All       | L2       |
| VCL-BADGES               | Badge Group          | Required    | All       | L2       |
| VCL-SKILL-ICONS          | Skill Icons          | Required    | Recruiter | L2       |
| VCL-PROJECT-CARD         | Project Card         | Recommended | Recruiter | L3       |
| VCL-STATS                | GitHub Stats         | Optional    | Recruiter | L2       |
| VCL-CONTRIBUTION-GRAPH   | Contribution Graph   | Optional    | Recruiter | L2       |
| VCL-TYPING-BANNER        | Typing Animation     | Optional    | Recruiter | L2       |
| VCL-ARCHITECTURE-DIAGRAM | Architecture Diagram | Recommended | Developer | L3       |
| VCL-WORKFLOW-DIAGRAM     | Workflow Diagram     | Recommended | Developer | L3       |
| VCL-FOLDER-DIAGRAM       | Repository Tree      | Recommended | Developer | L2       |
| VCL-NAVIGATION-CARD      | Navigation Card      | Recommended | All       | L3       |
| VCL-CALL-OUT             | GitHub Callouts      | Required    | All       | L2       |

---

# 62. Visual Core Components

```text id="cc031"
VCL-HERO

VCL-BADGES

VCL-SKILL-ICONS

VCL-CALL-OUT
```

---

# 63. Visual Extended Components

```text id="cc032"
VCL-BANNER

VCL-SOCIAL-PREVIEW

VCL-PROJECT-CARD

VCL-ARCHITECTURE-DIAGRAM

VCL-WORKFLOW-DIAGRAM

VCL-NAVIGATION-CARD
```

---

# 64. Visual Optional Components

```text id="cc033"
VCL-STATS

VCL-CONTRIBUTION-GRAPH

VCL-TYPING-BANNER
```

Estos componentes estarán reservados principalmente para el GitHub Profile.

---

# 65. Visual Dependency Graph

```text id="cc034"
VCL-BANNER

↓

VCL-HERO

↓

VCL-BADGES

↓

VCL-SKILL-ICONS

↓

VCL-PROJECT-CARD
```

---

# 66. Visual Capability Mapping

| Component                | Primary Capability       |
| ------------------------ | ------------------------ |
| VCL-BANNER               | Brand Identity           |
| VCL-HERO                 | Information Architecture |
| VCL-BADGES               | Project Status           |
| VCL-SKILL-ICONS          | Technology Communication |
| VCL-PROJECT-CARD         | Portfolio Presentation   |
| VCL-ARCHITECTURE-DIAGRAM | Software Architecture    |
| VCL-WORKFLOW-DIAGRAM     | Process Design           |

---

# 67. Cross-Family Relationships

Las familias comienzan a interactuar.

Ejemplo.

```text id="cc035"
README-HERO

↓

VCL-HERO

↓

VCL-BANNER

↓

VCL-BADGES
```

Otro ejemplo.

```text id="cc036"
README-DOCUMENTATION

↓

DOC-ARCHITECTURE

↓

VCL-NAVIGATION-CARD
```

---

# 68. Reuse Matrix

| Component Family | README | Docs | GitHub Profile | Templates |
| ---------------- | :----: | :--: | :------------: | :-------: |
| WCL              |        |   ✓  |                |     ✓     |
| VCL              |    ✓   |   ✓  |        ✓       |     ✓     |

---

# 69. Registry Evolution Rules

Los componentes WCL y VCL solo podrán ampliarse cuando:

* exista una necesidad recurrente;
* el componente sea reutilizable;
* no incremente innecesariamente la complejidad del Framework;
* exista una especificación previa en el RDS.

---

# 70. Anti-Patterns

No deberán registrarse:

* workflows específicos de un único proyecto;
* componentes visuales puramente decorativos;
* automatizaciones sin mantenimiento;
* variantes del mismo componente con pequeñas diferencias.

---

# 71. Quality Gates

Antes de registrar un componente WCL o VCL deberán verificarse.

* [ ] Identificador único.
* [ ] Flujo o elemento visual claramente definido.
* [ ] Responsabilidad única.
* [ ] Audiencia identificada.
* [ ] Prioridad asignada.
* [ ] Nivel mínimo de madurez.
* [ ] Relaciones documentadas.

---

# 72. Long-Term Vision

Las familias WCL y VCL permitirán que todos los repositorios compartan la misma forma de trabajar y el mismo lenguaje visual.

Los proyectos podrán diferenciarse por su dominio funcional sin perder coherencia operativa ni identidad gráfica.

---

# 73. Part 3 Conclusions

El registro oficial de componentes **Workflow** y **Visual** completa el catálogo operativo del GitHub Framework.

Los procesos de desarrollo y los elementos gráficos dejan de ser decisiones aisladas para convertirse en componentes gobernados, reutilizables y alineados con el resto del ecosistema.

Esto permitirá aplicar la misma experiencia de desarrollo y presentación a cualquier repositorio futuro.

---

# 74. Revision History

| Version | Date       | Description                                        |
| ------- | ---------- | -------------------------------------------------- |
| 1.0.0   | 2026-08-05 | Registro inicial de componentes Workflow y Visual. |

---

# 09 - COMPONENT CATALOG

# Part 4/4

# Repository Templates, Profiles & Framework Governance

---

# 75. Purpose

Esta sección completa el **Component Catalog** incorporando las dos últimas familias del GitHub Framework:

* Repository Templates (`TPL-*`)
* Repository Profiles (`PROFILE-*`)

Asimismo, define la relación entre todas las familias de componentes y establece las reglas de gobernanza del catálogo.

---

# 76. Repository Template Family

## Prefix

```text id="cc037"
TPL
```

---

## Purpose

Las plantillas representan configuraciones reutilizables del Framework.

No contienen componentes nuevos.

Seleccionan componentes existentes.

---

## Consumer

* Nuevos repositorios
* Scripts de generación
* Framework Bootstrap
* Repository Wizard

---

# 77. Template Registry

| ID                | Name                     | Project Type  | Maturity |
| ----------------- | ------------------------ | ------------- | -------- |
| TPL-BACKEND       | Backend Repository       | Backend       | L2-L4    |
| TPL-FULLSTACK     | Full Stack Repository    | Full Stack    | L2-L4    |
| TPL-AI            | AI Repository            | AI            | L2-L4    |
| TPL-DOCUMENTATION | Documentation Repository | Documentation | L2-L4    |
| TPL-LIBRARY       | Library Repository       | Library       | L2-L4    |
| TPL-WEBSITE       | Website Repository       | Website       | L2-L4    |

---

# 78. Maturity Templates

Las plantillas también podrán clasificarse por nivel.

| Template | Description  |
| -------- | ------------ |
| TPL-L1   | Experimental |
| TPL-L2   | Public Basic |
| TPL-L3   | Supporting   |
| TPL-L4   | Strategic    |

Estas plantillas podrán combinarse con cualquier tipo de proyecto.

---

# 79. Repository Profiles

## Prefix

```text id="cc038"
PROFILE
```

---

## Purpose

Los perfiles determinan cómo se utilizará un repositorio.

No modifican el contenido.

Modifican el comportamiento del Framework.

---

# 80. Profile Registry

| ID                  | Name             | Purpose               |
| ------------------- | ---------------- | --------------------- |
| PROFILE-SOLO        | Solo Developer   | Proyectos personales  |
| PROFILE-TEAM        | Team Development | Equipos pequeños      |
| PROFILE-OPEN-SOURCE | Open Source      | Comunidad             |
| PROFILE-RESEARCH    | Research         | IA y experimentación  |
| PROFILE-ENTERPRISE  | Enterprise       | Organización compleja |

---

# 81. Template Composition

Una plantilla siempre se construye combinando:

```text id="cc039"
Repository Type

+

Maturity

+

Profile
```

Ejemplo.

```text id="cc040"
TPL-BACKEND

+

TPL-L4

+

PROFILE-SOLO
```

---

# 82. Framework Composition

Todo repositorio podrá representarse mediante el siguiente modelo.

```text id="cc041"
README

+

Documentation

+

Workflow

+

Visual

+

Template

+

Profile
```

El Framework completo surge de la composición de estas seis familias.

---

# 83. Framework Dependency Graph

```text id="cc042"
README

↓

Documentation

↓

Workflow

↓

Visual

↓

Template

↓

Profile
```

Las dependencias deberán mantenerse acíclicas.

---

# 84. Framework Component Matrix

| Family        | Prefix  | Registry | Components |
| ------------- | ------- | -------- | ---------: |
| README        | README  | ✓        |         17 |
| Documentation | DOC     | ✓        |         15 |
| Workflow      | WCL     | ✓        |         16 |
| Visual        | VCL     | ✓        |         14 |
| Templates     | TPL     | ✓        |         10 |
| Profiles      | PROFILE | ✓        |          5 |

---

# 85. Framework Relationships

| Family  | Depends On            |
| ------- | --------------------- |
| README  | VCL, DOC              |
| DOC     | —                     |
| WCL     | DOC                   |
| VCL     | README                |
| TPL     | README, DOC, WCL, VCL |
| PROFILE | TPL                   |

Estas relaciones representan dependencias conceptuales, no dependencias técnicas.

---

# 86. Component Selection Strategy

Al crear un nuevo repositorio.

```text id="cc043"
Choose Template

↓

Choose Profile

↓

Select Components

↓

Generate Repository

↓

Customize

↓

Publish
```

---

# 87. Framework Layers

```text id="cc044"
Brand Layer

↓

Repository Layer

↓

Documentation Layer

↓

Workflow Layer

↓

Visual Layer

↓

Governance Layer
```

Cada capa incorpora nuevas capacidades.

---

# 88. Component Traceability

Todo componente deberá poder responder.

* ¿Dónde está definido?
* ¿Qué plantillas lo utilizan?
* ¿Qué perfiles lo activan?
* ¿Qué repositorios lo implementan?
* ¿Cuál es su versión?
* ¿Quién es su responsable?

---

# 89. Component Registry Fields

La ficha completa de un componente incluirá.

| Field          | Description                       |
| -------------- | --------------------------------- |
| ID             | Identificador único               |
| Name           | Nombre                            |
| Family         | Familia                           |
| Version        | Semantic Version                  |
| Status         | Estado                            |
| Owner          | Responsable                       |
| Priority       | Required / Recommended / Optional |
| Audience       | Público objetivo                  |
| Maturity       | L1-L4                             |
| Dependencies   | Relaciones                        |
| Used By        | Plantillas                        |
| Implemented In | Repositorios                      |
| Last Review    | Última revisión                   |

---

# 90. Framework Governance

El catálogo será el único lugar autorizado para registrar nuevos componentes.

Todo nuevo componente deberá:

* disponer de especificación;
* aparecer en el catálogo;
* tener identificador único;
* indicar dependencias;
* mantener compatibilidad.

---

# 91. Repository Bootstrap Process

Todo nuevo repositorio seguirá.

```text id="cc045"
Framework

↓

Template

↓

Profile

↓

Components

↓

Repository

↓

Assessment
```

---

# 92. Evolution Strategy

La evolución del Framework seguirá.

```text id="cc046"
Need

↓

Proposal

↓

Specification

↓

Registry

↓

Template

↓

Implementation

↓

Adoption
```

---

# 93. Anti-Patterns

No deberán existir.

* plantillas incompatibles;
* perfiles duplicados;
* componentes no registrados;
* dependencias circulares;
* componentes sin implementación prevista;
* repositorios fuera del Framework.

---

# 94. Quality Gates

Antes de aprobar una nueva versión del catálogo deberán verificarse.

* [ ] Todas las familias actualizadas.
* [ ] Componentes registrados.
* [ ] Matrices sincronizadas.
* [ ] Dependencias revisadas.
* [ ] Plantillas verificadas.
* [ ] Perfiles documentados.

---

# 95. Framework Roadmap

## Phase 1

Component Catalog.

---

## Phase 2

Templates.

---

## Phase 3

Examples.

---

## Phase 4

Automation.

---

## Phase 5

Repository Generator.

---

## Phase 6

Framework Dashboard.

---

# 96. Long-Term Vision

El Component Catalog será el núcleo del GitHub Framework.

Permitirá construir, mantener y evolucionar cualquier repositorio mediante un conjunto gobernado de componentes reutilizables.

El Framework podrá crecer durante años incorporando nuevas familias, plantillas y automatizaciones sin perder consistencia.

---

# 97. Final Conclusions

El **Component Catalog** completa la arquitectura lógica del GitHub Framework.

Cada componente posee ahora:

* una identidad permanente;
* una familia claramente definida;
* un propósito específico;
* una relación explícita con el resto del sistema.

El catálogo se convierte en la fuente oficial de verdad para el ecosistema y en el punto de unión entre los estándares (GRS), el Repository Design System (RDS), las plantillas y la futura implementación.

A partir de este momento, cualquier nuevo repositorio podrá construirse seleccionando componentes ya definidos en lugar de diseñarse desde cero.

---

# 98. Revision History

| Version | Date       | Description |
| ------- | ---------- | ----------- |
| 1.0.0   | 2026-08-05 | Primera versión del Component Catalog. |
| 1.0.1   | 2026-08-11 | Metadata alineada con GitHub Framework durante la implementación de referencia del Documentation Framework. |
