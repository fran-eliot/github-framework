# 07 - GITHUB METADATA

| Field        | Value                             |
| ------------ | --------------------------------- |
| **Project**  | GitHub Professional Profile       |
| **Document** | GitHub Repository Standards (GRS) |
| **Version**  | 1.0.0 (Draft)                     |
| **Status**   | In Progress                       |
| **Owner**    | Fran Ramirez                      |

---

# Part 1/8

# GitHub Metadata Philosophy

---

# 1. Purpose

Este documento define los estándares oficiales que deberán cumplir todos los repositorios públicos del ecosistema GitHub de Fran Ramirez.

No pretende documentar únicamente la configuración de GitHub.

Define un conjunto de normas de calidad para garantizar que todos los repositorios transmitan una imagen profesional, coherente y mantenible.

Estos estándares constituyen el **GitHub Repository Standard (GRS)**.

---

# 2. Vision

Cada repositorio deberá considerarse un producto.

No un simple contenedor de código.

Un visitante deberá percibir inmediatamente que:

* existe una arquitectura;
* existe documentación;
* existe mantenimiento;
* existe criterio.

La calidad del repositorio deberá reflejar la calidad del software.

---

# 3. Mission

Los estándares GRS tienen cuatro objetivos principales.

* Homogeneizar todos los repositorios.
* Facilitar la navegación.
* Reducir el mantenimiento.
* Reforzar la identidad profesional.

---

# 4. Repository Philosophy

Cada repositorio representa una parte de la identidad profesional.

Por tanto:

* deberá ser comprensible;
* deberá ser navegable;
* deberá ser reutilizable;
* deberá mantenerse actualizado.

Un repositorio abandonado perjudica más que un repositorio privado.

---

# 5. Engineering Principles

Los estándares GRS se apoyan en los mismos principios definidos para el resto del ecosistema.

* Simplicidad.
* Consistencia.
* Documentación.
* Calidad.
* Evolución sostenible.

---

# 6. Repository as a Product

Todo repositorio estratégico deberá responder afirmativamente a las siguientes preguntas.

* ¿Puede entenderse sin ayuda externa?
* ¿Puede instalarse?
* ¿Puede ejecutarse?
* ¿Puede mantenerse?
* ¿Puede evolucionar?

Si alguna respuesta es negativa, el repositorio no estará preparado para formar parte del portfolio.

---

# 7. User Experience

El visitante ideal seguirá un recorrido sencillo.

```text id="grs001"
Repository

↓

Description

↓

README

↓

Architecture

↓

Code

↓

Releases
```

No deberá perderse buscando información.

---

# 8. Repository Identity

Todos los proyectos compartirán una identidad común.

Esto implica consistencia en:

* nombres;
* descripciones;
* estructura;
* documentación;
* banners;
* enlaces;
* navegación.

---

# 9. Metadata Philosophy

Los metadatos no son un detalle menor.

Constituyen la primera información que GitHub muestra sobre un proyecto.

Por tanto deberán recibir el mismo nivel de cuidado que el código fuente.

---

# 10. First Impression

Antes de abrir un README, el visitante ya ha visto:

* nombre;
* descripción;
* topics;
* imagen social.

Esos cuatro elementos deberán comunicar inmediatamente:

```text id="grs002"
Qué es.

↓

Qué hace.

↓

Por qué merece la pena abrirlo.
```

---

# 11. Quality over Quantity

El objetivo no consiste en publicar muchos repositorios.

Consiste en mantener pocos proyectos con un estándar elevado.

La calidad será siempre prioritaria frente al volumen.

---

# 12. Public Repository Criteria

Un repositorio solo deberá hacerse público cuando:

* aporte valor al portfolio;
* esté razonablemente documentado;
* no contenga información sensible;
* represente correctamente el nivel técnico actual.

---

# 13. Private Repository Criteria

Permanecerán privados aquellos proyectos que:

* sean experimentales;
* estén incompletos;
* contengan pruebas temporales;
* no aporten una capacidad nueva.

---

# 14. Repository Lifecycle

Todos los proyectos seguirán un ciclo de vida común.

```text id="grs003"
Prototype

↓

Development

↓

Public Release

↓

Maintenance

↓

Archive
```

Cada estado tendrá implicaciones distintas en cuanto a visibilidad y mantenimiento.

---

# 15. Metadata Consistency

Los metadatos deberán mantenerse sincronizados entre:

* GitHub;
* README;
* LinkedIn;
* CV;
* documentación.

Nunca deberán transmitir mensajes diferentes.

---

# 16. Editorial Consistency

Todos los textos visibles en GitHub deberán compartir el mismo estilo.

El tono será:

* técnico;
* claro;
* internacional;
* preciso;
* profesional.

Nunca:

* excesivamente comercial;
* informal;
* ambiguo.

---

# 17. Repository Standards (GRS)

El ecosistema adoptará oficialmente los siguientes estándares.

| ID      | Standard               |
| ------- | ---------------------- |
| GRS-001 | Repository Naming      |
| GRS-002 | Repository Description |
| GRS-003 | About Section          |
| GRS-004 | Topics                 |
| GRS-005 | README                 |
| GRS-006 | Documentation          |
| GRS-007 | Releases               |
| GRS-008 | Branch Strategy        |
| GRS-009 | Repository Lifecycle   |
| GRS-010 | Portfolio Governance   |

Las siguientes partes desarrollarán cada uno de estos estándares.

---

# 18. Scope

Los estándares GRS serán obligatorios para:

* GitHub Profile
* NovaCoquinaria
* OnlyFilm
* Aula Robótica
* Cognitiva AI
* Dental Clinic
* futuros proyectos estratégicos.

Podrán aplicarse parcialmente a proyectos secundarios.

---

# 19. Long-Term Objective

El sistema GRS deberá mantenerse vigente durante varios años.

Las modificaciones serán incrementales.

No deberán requerir rediseños completos del ecosistema.

---

# 20. Success Criteria

El sistema de metadatos será exitoso cuando:

* todos los repositorios transmitan una identidad coherente;
* cualquier visitante pueda orientarse rápidamente;
* el mantenimiento sea sencillo;
* la calidad percibida sea homogénea en todo el portfolio.

---

# 21. Part 1 Conclusions

Los metadatos de GitHub no son información administrativa.

Forman parte de la experiencia de usuario y de la marca profesional.

El sistema **GitHub Repository Standards (GRS)** convierte esos elementos en un conjunto de normas reutilizables que permitirán mantener un ecosistema consistente, profesional y preparado para evolucionar durante los próximos años.

---

# 07 - GITHUB METADATA

# Part 2/8

# GRS-001 Repository Naming Standard

---

# 22. Purpose

El estándar **GRS-001** define las reglas oficiales para nombrar todos los repositorios del ecosistema GitHub de Fran Ramirez.

El objetivo consiste en garantizar que cualquier repositorio sea:

* fácilmente identificable;
* coherente con el resto del portfolio;
* estable a largo plazo;
* comprensible para una audiencia internacional.

El nombre de un repositorio constituye parte de la marca profesional.

---

# 23. Naming Philosophy

El nombre de un repositorio deberá responder a una única pregunta.

```text id="naming001"
¿Qué es este proyecto?
```

No:

```text id="naming002"
¿Quién lo hizo?

¿Para qué curso era?

¿En qué empresa nació?
```

El nombre debe describir el producto.

No el contexto.

---

# 24. General Principles

Todo nombre deberá cumplir los siguientes principios.

* Corto.
* Memorables.
* Internacional.
* Estable.
* Sin ambigüedades.

---

# 25. Official Language

Todos los nombres utilizarán:

```text id="naming003"
English
```

Se evitarán nombres en español salvo cuando constituyan una marca propia.

Ejemplo.

```text id="naming004"
NovaCoquinaria
```

es válido porque constituye el nombre oficial del proyecto.

---

# 26. Naming Strategy

Los proyectos utilizarán nombres de producto.

No nombres descriptivos.

Correcto.

```text id="naming005"
NovaCoquinaria
OnlyFilm
```

Incorrecto.

```text id="naming006"
java-final-project

spring-practice

backend-course

dam-project
```

---

# 27. Repository Identity

Cada nombre deberá representar una identidad propia.

No una tecnología.

Las tecnologías cambian.

Los nombres permanecen.

---

# 28. Length

Longitud recomendada.

```text id="naming007"
8–20 caracteres
```

Longitud máxima.

```text id="naming008"
30 caracteres
```

---

# 29. Readability

Los nombres deberán ser fácilmente pronunciables.

Incluso para personas cuya lengua materna no sea el español.

---

# 30. Capitalization

Para proyectos con nombre propio se utilizará:

```text id="naming009"
PascalCase
```

Ejemplos.

```text id="naming010"
NovaCoquinaria

OnlyFilm
```

Cuando el nombre oficial sea una combinación de palabras separadas por guiones (por razones de marca, herramientas o URLs), se respetará esa convención.

---

# 31. Kebab Case

El uso de:

```text id="naming011"
kebab-case
```

quedará reservado para:

* utilidades;
* librerías;
* herramientas internas;
* scripts.

Ejemplos.

```text id="naming012"
github-profile

banner-generator

knowledge-tools
```

---

# 32. Snake Case

```text id="naming013"
snake_case
```

queda descartado.

No forma parte de la identidad visual del ecosistema.

---

# 33. Prefixes

No se utilizarán prefijos como:

```text id="naming014"
java-

spring-

python-

angular-

my-
```

Las tecnologías pertenecen a los metadatos.

No al nombre.

---

# 34. Suffixes

También quedan descartados sufijos como:

```text id="naming015"
-final

-v2

-new

-test

-demo

-copy
```

Las versiones se gestionarán mediante Git y Releases.

Nunca mediante el nombre.

---

# 35. Academic Naming

No aparecerán referencias a:

* universidad;
* bootcamp;
* curso;
* asignatura;
* práctica.

Ejemplos incorrectos.

```text id="naming016"
ironhack-final

dam-project

spring-exercise
```

El repositorio deberá sobrevivir al contexto académico.

---

# 36. Company Naming

Los proyectos personales nunca incorporarán nombres de empresas donde se hayan desarrollado conocimientos o inspiración.

La identidad pertenece al producto.

---

# 37. Acronyms

Las siglas solo se utilizarán cuando:

* sean ampliamente reconocidas;
* formen parte del nombre oficial.

En caso contrario se preferirán nombres completos.

---

# 38. Numeric Identifiers

No se utilizarán números salvo que formen parte de la identidad del producto.

Incorrecto.

```text id="naming017"
project2

backend2026

spring01
```

---

# 39. Temporary Repositories

Los repositorios temporales deberán permanecer privados.

Nunca se publicarán con nombres provisionales.

---

# 40. Repository Families

Cuando varios repositorios pertenezcan al mismo ecosistema se utilizará una convención consistente.

Ejemplo.

```text id="naming018"
NovaCoquinaria

NovaCoquinaria-Docs

NovaCoquinaria-Site
```

Solo cuando exista una necesidad real de dividir el proyecto.

---

# 41. Reserved Names

Se evitarán nombres excesivamente genéricos.

Ejemplos.

```text id="naming019"
Backend

Portfolio

Website

Project
```

No son suficientemente distintivos.

---

# 42. Brand Protection

Antes de adoptar un nombre deberá comprobarse:

* disponibilidad en GitHub;
* ausencia de conflictos evidentes con proyectos conocidos;
* facilidad de búsqueda.

No se pretende registrar una marca, pero sí evitar confusiones innecesarias.

---

# 43. Rename Policy

Renombrar un repositorio será una excepción.

Solo se aceptará cuando:

* mejore significativamente la claridad;
* unifique el ecosistema;
* elimine un nombre provisional.

No se realizarán cambios por motivos estéticos.

---

# 44. Repository Classification

Cada nombre deberá pertenecer a una de estas categorías.

| Category      | Convention   |
| ------------- | ------------ |
| Product       | PascalCase   |
| Tool          | kebab-case   |
| Documentation | Product-Docs |
| Website       | Product-Site |
| Library       | kebab-case   |
| Template      | kebab-case   |

Esta clasificación facilitará la navegación.

---

# 45. Future Projects

Todo proyecto nuevo deberá superar la siguiente revisión antes de crear el repositorio.

* [ ] ¿El nombre representa el producto?
* [ ] ¿Es internacional?
* [ ] ¿Es fácil de recordar?
* [ ] ¿Puede mantenerse durante años?
* [ ] ¿Es coherente con el ecosistema?

---

# 46. Anti-Patterns

No utilizar:

* nombres excesivamente largos;
* nombres académicos;
* nombres tecnológicos;
* fechas;
* versiones;
* prefijos innecesarios;
* sufijos temporales.

---

# 47. Quality Gates

Antes de aprobar un nombre deberán verificarse:

* [ ] Longitud adecuada.
* [ ] Pronunciable.
* [ ] Internacional.
* [ ] Coherente con la marca.
* [ ] Sin referencias temporales.
* [ ] Sin tecnologías incrustadas.
* [ ] Sin contexto académico.

---

# 48. Examples

## Correct

```text id="naming020"
NovaCoquinaria

OnlyFilm

CognitivaAI

github-profile

banner-generator
```

---

## Incorrect

```text id="naming021"
spring-final-project

backend-java-2026

dam-practice

ironhack-capstone

project-final-v3
```

---

# 49. Long-Term Vision

Los nombres deberán mantenerse estables durante toda la vida del proyecto.

El repositorio podrá evolucionar técnicamente.

Su identidad no deberá hacerlo.

---

# 50. Part 2 Conclusions

El nombre de un repositorio constituye el primer elemento de su identidad.

El estándar **GRS-001** garantiza que todos los proyectos del ecosistema compartan una convención coherente, internacional y preparada para mantenerse vigente durante muchos años.

El objetivo no es únicamente facilitar la organización del código.

Es construir una **marca técnica consistente**, donde cada nombre represente un producto y no una circunstancia temporal.

---

# 07 - GITHUB METADATA

# Part 3/8

# GRS-002 Repository About Standard

---

# 51. Purpose

El estándar **GRS-002** define la configuración oficial del apartado **About** de todos los repositorios del ecosistema GitHub.

Incluye:

* Description
* Website
* Topics
* Social Preview
* Pinned Repositories

Su objetivo consiste en garantizar una primera impresión clara, profesional y coherente.

---

# 52. Philosophy

La sección **About** deberá responder tres preguntas.

```text id="aboutstd001"
¿Qué es?

↓

¿Qué hace?

↓

¿Por qué debería abrirlo?
```

Todo lo demás pertenece al README.

---

# 53. Components

Todo repositorio estratégico deberá configurar los siguientes elementos.

| Component      | Required      |
| -------------- | ------------- |
| Description    | Sí            |
| Website        | Cuando exista |
| Topics         | Sí            |
| Social Preview | Sí            |
| License        | Sí            |
| README         | Sí            |

---

# 54. Repository Description

La descripción constituye el elemento más importante del apartado About.

Deberá resumir el proyecto en una única frase.

---

# 55. Description Principles

Toda descripción deberá ser:

* breve;
* técnica;
* internacional;
* precisa;
* orientada al propósito.

Nunca:

* comercial;
* publicitaria;
* excesivamente genérica.

---

# 56. Description Length

Longitud recomendada.

```text id="aboutstd002"
70–110 caracteres
```

Máximo aproximado.

```text id="aboutstd003"
120 caracteres
```

El objetivo es evitar cortes en la interfaz de GitHub.

---

# 57. Description Structure

Formato recomendado.

```text id="aboutstd004"
Product Type + Main Purpose + Key Technology (opcional)
```

Ejemplos.

```text id="aboutstd005"
Knowledge Engineering Platform for structured culinary documentation.

Spring Boot backend for cinema ticket management.

FastAPI collaboration platform for university robotics projects.

Machine Learning project for cognitive impairment screening.
```

---

# 58. Forbidden Terms

No utilizar:

* Awesome
* Amazing
* Best
* Ultimate
* Final Project
* Personal Project
* Practice
* Learning
* Exercise

La calidad deberá deducirse del proyecto.

No afirmarse explícitamente.

---

# 59. Website Field

El campo Website tendrá prioridad según el siguiente orden.

1. GitHub Pages
2. Proyecto desplegado
3. Documentación pública
4. Sitio web oficial

Nunca se enlazará una página inacabada.

---

# 60. Website Policy

Si no existe un destino útil.

El campo permanecerá vacío.

Es preferible no mostrar un enlace que enlazar contenido poco cuidado.

---

# 61. Topics Purpose

Los Topics cumplen dos funciones.

* Clasificación.
* Descubrimiento.

Por ello deberán elegirse cuidadosamente.

---

# 62. Topics Principles

Los Topics deberán describir:

* dominio;
* tecnologías principales;
* arquitectura;
* metodología.

No simplemente todas las herramientas utilizadas.

---

# 63. Topics Categories

Los Topics pertenecerán a cuatro grupos.

### Domain

Ejemplo.

```text id="aboutstd006"
knowledge-management

healthcare

robotics

cinema

artificial-intelligence
```

---

### Technology

Ejemplo.

```text id="aboutstd007"
spring-boot

fastapi

python

java

angular
```

---

### Architecture

Ejemplo.

```text id="aboutstd008"
clean-architecture

rest-api

documentation-first

microservices

knowledge-graph
```

---

### Engineering

Ejemplo.

```text id="aboutstd009"
testing

ci-cd

docker

automation
```

---

# 64. Topics Limit

Número recomendado.

```text id="aboutstd010"
8–12 Topics
```

Nunca más de:

```text id="aboutstd011"
15
```

---

# 65. Topics Ordering

Los Topics seguirán el siguiente orden.

```text id="aboutstd012"
Domain

↓

Technology

↓

Architecture

↓

Engineering
```

El orden será consistente en todos los repositorios.

---

# 66. Social Preview

Todos los proyectos estratégicos dispondrán de:

* imagen personalizada;
* coherente con el sistema visual;
* generada desde el mismo Design System.

No se utilizarán capturas de pantalla.

---

# 67. Social Preview Philosophy

La imagen Social Preview deberá:

* identificar el proyecto;
* reforzar la marca;
* mantener coherencia visual.

No deberá explicar el proyecto.

---

# 68. Pinned Repositories

El perfil GitHub mostrará únicamente repositorios estratégicos.

Orden recomendado.

1. NovaCoquinaria
2. OnlyFilm
3. Aula Robótica
4. Cognitiva AI
5. Dental Clinic
6. Proyecto estratégico más reciente

---

# 69. Pinning Rules

Un repositorio podrá fijarse cuando:

* represente una capacidad principal;
* tenga documentación madura;
* refleje el posicionamiento profesional actual.

---

# 70. Unpinning Rules

Se retirará un repositorio fijado cuando:

* exista otro claramente superior;
* deje de representar la dirección profesional;
* permanezca archivado.

---

# 71. Description Consistency

La Description deberá estar alineada con:

* README;
* Social Preview;
* Topics;
* Banner.

Nunca deberán transmitir mensajes distintos.

---

# 72. SEO Philosophy

GitHub actúa como un buscador.

Por tanto:

* los Topics;
* la Description;
* el nombre;

constituyen el SEO interno del repositorio.

No deberán desaprovecharse.

---

# 73. International Audience

Todos los metadatos se redactarán en inglés.

El README podrá ofrecer versión española.

Pero la configuración GitHub será internacional.

---

# 74. Accessibility

Las imágenes Social Preview deberán:

* ser legibles;
* mantener buen contraste;
* funcionar en miniatura;
* no depender exclusivamente del color.

---

# 75. Quality Gates

Antes de publicar un repositorio deberán verificarse:

* [ ] Description clara.
* [ ] Website válido (si existe).
* [ ] Topics revisados.
* [ ] Social Preview actualizado.
* [ ] README coherente.
* [ ] License visible.

---

# 76. Repository Metadata Matrix

Cada proyecto dispondrá de una ficha de metadatos.

| Field          | Example                                                               |
| -------------- | --------------------------------------------------------------------- |
| Name           | NovaCoquinaria                                                        |
| Description    | Knowledge Engineering Platform for structured culinary documentation. |
| Website        | GitHub Pages                                                          |
| Topics         | knowledge-management, documentation-first, python, markdown           |
| Social Preview | Banner oficial                                                        |

Esta ficha servirá como referencia para el mantenimiento.

---

# 77. Long-Term Maintenance

Los metadatos deberán revisarse:

* cuando cambie el posicionamiento del proyecto;
* cuando se publique una versión importante;
* al menos una vez al año.

---

# 78. Anti-Patterns

No utilizar:

* descripciones vacías;
* Topics irrelevantes;
* Topics duplicados;
* imágenes genéricas;
* capturas de pantalla como Social Preview;
* enlaces rotos.

---

# 79. Success Criteria

La sección About será exitosa cuando:

* el visitante entienda el proyecto antes de abrir el README;
* los Topics faciliten el descubrimiento;
* la identidad visual sea consistente;
* los repositorios fijados representen fielmente el portfolio.

---

# 80. Part 3 Conclusions

El estándar **GRS-002** transforma la sección **About** en un componente estratégico del ecosistema GitHub.

Description, Topics, Website y Social Preview dejarán de ser simples metadatos para convertirse en herramientas de comunicación técnica.

El resultado será una primera impresión coherente, internacional y alineada con la identidad profesional definida para todo el portfolio.

---

# 07 - GITHUB METADATA

# Part 4/8

# GRS-003 Repository Structure & Documentation Standard

---

# 81. Purpose

El estándar **GRS-003** define la estructura oficial que deberán seguir todos los repositorios estratégicos del ecosistema GitHub.

Su objetivo consiste en garantizar que cualquier proyecto sea:

* fácil de entender;
* sencillo de navegar;
* mantenible;
* escalable;
* coherente con el resto del portfolio.

La estructura del repositorio deberá reflejar la calidad de la ingeniería.

---

# 82. Repository Philosophy

Un repositorio no es únicamente una colección de archivos.

Es un producto técnico.

Su organización deberá facilitar:

* la comprensión;
* el mantenimiento;
* la colaboración futura.

---

# 83. Standard Repository Layout

Todo repositorio estratégico seguirá una estructura similar a la siguiente.

```text id="repo001"
Repository

├── README.md
├── README.es.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md (opcional)
├── SECURITY.md (cuando proceda)
├── ROADMAP.md
├── PROJECT_STATUS.md
├── docs/
├── assets/
├── .github/
└── source code
```

La estructura podrá ampliarse, pero no simplificarse en proyectos principales.

---

# 84. README Standard

Todo repositorio público deberá disponer de un README profesional.

El README constituye la puerta de entrada al proyecto.

Nunca será opcional.

---

# 85. README Responsibilities

El README responderá, como mínimo, a las siguientes preguntas.

```text id="repo002"
¿Qué es?

↓

¿Por qué existe?

↓

¿Cómo funciona?

↓

¿Cómo se instala?

↓

¿Cómo se utiliza?
```

No deberá contener documentación técnica exhaustiva.

Para ello existirá la carpeta `docs/`.

---

# 86. README Languages

Los proyectos estratégicos tendrán dos versiones oficiales.

```text id="repo003"
README.md

README.es.md
```

El inglés será siempre la versión principal.

---

# 87. Documentation Strategy

El README será una visión general.

La documentación detallada se organizará dentro de:

```text id="repo004"
docs/
```

El README nunca crecerá indefinidamente.

---

# 88. docs/ Directory

La carpeta `docs/` contendrá toda la documentación técnica.

Ejemplos.

```text id="repo005"
docs/

architecture/

adr/

management/

api/

deployment/

testing/

diagrams/
```

La estructura concreta dependerá del proyecto.

---

# 89. ADR Policy

Cuando el proyecto lo justifique, las decisiones importantes deberán documentarse mediante ADR (Architecture Decision Records).

No todas las aplicaciones necesitarán ADRs.

Pero todos los proyectos arquitectónicamente relevantes deberán contemplarlos.

---

# 90. Assets Directory

Toda imagen utilizada por el README deberá almacenarse en:

```text id="repo006"
assets/
```

Nunca se enlazarán imágenes externas salvo necesidad justificada.

---

# 91. LICENSE

Todo repositorio público deberá incluir una licencia.

La licencia elegida dependerá del tipo de proyecto.

La ausencia de licencia no será aceptable en repositorios estratégicos.

---

# 92. CHANGELOG

Los proyectos maduros deberán mantener un historial de versiones.

Formato recomendado.

```text id="repo007"
Keep a Changelog
```

La estructura será consistente en todos los proyectos.

---

# 93. CONTRIBUTING

El archivo `CONTRIBUTING.md` será obligatorio únicamente cuando:

* el proyecto acepte contribuciones externas;
* exista interés real en la colaboración.

En proyectos personales podrá omitirse inicialmente.

---

# 94. SECURITY

`SECURITY.md` será recomendable para proyectos con despliegues públicos o aplicaciones susceptibles de recibir reportes de seguridad.

En proyectos puramente académicos no será necesario.

---

# 95. ROADMAP

Todo proyecto estratégico dispondrá de un roadmap.

El roadmap deberá responder:

```text id="repo008"
¿Qué viene después?
```

No deberá convertirse en una lista infinita de ideas.

---

# 96. PROJECT_STATUS

Cada proyecto mantendrá un archivo de estado.

Ejemplo.

```text id="repo009"
Stable

Active Development

Maintenance

Archived
```

Este documento facilitará el seguimiento del proyecto.

---

# 97. .github Directory

La carpeta `.github/` contendrá toda la configuración específica de GitHub.

Ejemplos.

```text id="repo010"
ISSUE_TEMPLATE/

PULL_REQUEST_TEMPLATE.md

workflows/

FUNDING.yml (si algún día fuera necesario)
```

La organización será consistente.

---

# 98. Documentation Principles

Toda documentación deberá ser:

* precisa;
* actualizada;
* navegable;
* reutilizable.

Nunca:

* redundante;
* contradictoria;
* desactualizada.

---

# 99. Documentation Depth

El nivel de documentación dependerá del tipo de proyecto.

| Repository Type   | Documentation Level |
| ----------------- | ------------------- |
| Strategic Product | Muy alta            |
| Technical Demo    | Media               |
| Utility           | Ligera              |
| Prototype         | Mínima              |

No todos los proyectos requieren el mismo esfuerzo documental.

---

# 100. Navigation

Todo README deberá enlazar a la documentación relevante.

Ejemplo.

```text id="repo011"
Architecture

API

Roadmap

Releases

License
```

La navegación deberá ser evidente.

---

# 101. Repository Templates

Con el tiempo se desarrollarán plantillas reutilizables para:

* README;
* CHANGELOG;
* ROADMAP;
* PROJECT_STATUS;
* CONTRIBUTING.

Esto reducirá significativamente el esfuerzo al crear nuevos proyectos.

---

# 102. Documentation Synchronization

Toda modificación importante del software deberá reflejarse en la documentación correspondiente.

El código y la documentación evolucionarán conjuntamente.

---

# 103. Anti-Patterns

No utilizar:

* documentación duplicada;
* README excesivamente largos;
* imágenes dispersas por el repositorio;
* archivos sin propósito claro;
* estructuras diferentes para proyectos similares.

---

# 104. Quality Gates

Antes de publicar un repositorio deberán verificarse:

* [ ] README completo.
* [ ] Documentación organizada.
* [ ] Licencia incluida.
* [ ] Assets centralizados.
* [ ] Navegación clara.
* [ ] Estado del proyecto actualizado.
* [ ] Roadmap disponible (si procede).

---

# 105. Repository Maturity Levels

Se definen cuatro niveles de madurez.

| Level | Description                                              |
| ----- | -------------------------------------------------------- |
| L1    | Código únicamente                                        |
| L2    | Código + README                                          |
| L3    | Documentación estructurada                               |
| L4    | Ecosistema completo (ADR, Roadmap, Releases, Governance) |

Los proyectos fijados en el perfil deberán aspirar al nivel **L4**.

---

# 106. Long-Term Vision

Con el crecimiento del portfolio, todos los repositorios estratégicos compartirán una estructura reconocible.

Un visitante que conozca un proyecto podrá orientarse inmediatamente en cualquier otro.

Esta consistencia reducirá el esfuerzo de mantenimiento y reforzará la identidad profesional.

---

# 107. Part 4 Conclusions

El estándar **GRS-003** transforma la organización de los repositorios en un sistema de ingeniería.

La estructura deja de depender de cada proyecto individual y pasa a formar parte de una arquitectura común.

El resultado será un ecosistema donde código, documentación y configuración compartan los mismos principios de claridad, consistencia y mantenibilidad, transmitiendo una imagen profesional y preparada para evolucionar durante muchos años.

---

# 07 - GITHUB METADATA

# Part 5/8

# GRS-004 Git Strategy, Branching & Release Standard

---

# 108. Purpose

El estándar **GRS-004** define la estrategia oficial de control de versiones para todos los repositorios del ecosistema GitHub.

Su objetivo consiste en garantizar:

* desarrollo ordenado;
* historial comprensible;
* releases reproducibles;
* evolución controlada;
* consistencia entre proyectos.

Git deja de ser únicamente una herramienta de versionado.

Pasa a formar parte de la arquitectura de ingeniería.

---

# 109. Philosophy

La estrategia Git deberá ser:

* sencilla;
* consistente;
* escalable;
* apropiada para proyectos personales.

No intentará reproducir procesos corporativos complejos cuando no aporten valor.

---

# 110. Branching Model

Modelo oficial.

```text id="git001"
main

↓

develop

↓

feature/*
```

Se añadirán ramas adicionales únicamente cuando el proyecto lo requiera.

---

# 111. Main Branch

La rama:

```text id="git002"
main
```

representa siempre el estado estable del proyecto.

Reglas.

* Código funcional.
* Documentación sincronizada.
* Releases publicadas.
* Sin trabajo experimental.

Nunca se desarrollará directamente sobre `main`, salvo correcciones excepcionales y justificadas.

---

# 112. Develop Branch

La rama:

```text id="git003"
develop
```

representa la integración continua del proyecto.

Todo desarrollo nuevo deberá incorporarse primero a `develop`.

Una vez estabilizado pasará a `main`.

---

# 113. Feature Branches

Toda funcionalidad nueva utilizará una rama específica.

Formato.

```text id="git004"
feature/<nombre>
```

Ejemplos.

```text id="git005"
feature/authentication

feature/banner-system

feature/knowledge-graph

feature/project-dashboard
```

---

# 114. Naming Rules

Los nombres de rama deberán:

* utilizar inglés;
* ser descriptivos;
* emplear kebab-case.

No utilizar:

```text id="git006"
feature/test

feature/new

feature/update2

feature/final
```

---

# 115. Release Branches

Cuando el proyecto tenga suficiente madurez podrá utilizar:

```text id="git007"
release/x.y.z
```

Ejemplo.

```text id="git008"
release/2.0.0
```

La rama de release se utilizará únicamente para estabilización y preparación de la publicación.

---

# 116. Hotfix Branches

Las correcciones urgentes podrán desarrollarse mediante:

```text id="git009"
hotfix/<nombre>
```

Ejemplo.

```text id="git010"
hotfix/security-patch

hotfix/login-error
```

Tras la corrección deberán fusionarse tanto en `main` como en `develop`.

---

# 117. Experimental Branches

Las pruebas de investigación podrán utilizar:

```text id="git011"
experiment/<topic>
```

Estas ramas no formarán parte del flujo habitual y podrán eliminarse una vez finalizada la exploración.

---

# 118. Semantic Versioning

Todos los proyectos estratégicos utilizarán:

```text id="git012"
MAJOR.MINOR.PATCH
```

Ejemplos.

```text id="git013"
1.0.0

1.1.0

1.2.3

2.0.0
```

---

# 119. Versioning Rules

## Major

Cambios incompatibles.

---

## Minor

Nuevas funcionalidades compatibles.

---

## Patch

Correcciones y mejoras menores.

---

# 120. Git Tags

Cada Release publicada deberá tener un tag.

Formato.

```text id="git014"
v1.0.0
```

Siempre con prefijo:

```text id="git015"
v
```

---

# 121. GitHub Releases

Todo proyecto estratégico publicará Releases.

Cada Release incluirá:

* versión;
* fecha;
* resumen;
* principales cambios;
* enlaces relevantes cuando proceda.

---

# 122. Release Notes

Las notas seguirán una estructura uniforme.

```text id="git016"
Highlights

New Features

Improvements

Fixes

Known Issues
```

Esto facilitará la lectura y comparación entre versiones.

---

# 123. Commit Philosophy

Los commits deberán ser:

* pequeños;
* atómicos;
* descriptivos.

Cada commit deberá representar una única intención de cambio.

---

# 124. Commit Language

Todos los mensajes se escribirán en:

```text id="git017"
English
```

El inglés facilita la colaboración y mantiene coherencia con el resto del ecosistema.

---

# 125. Commit Style

Se adoptará una convención inspirada en **Conventional Commits**.

Ejemplos.

```text id="git018"
feat:

fix:

docs:

refactor:

test:

build:

ci:

chore:
```

No será necesario seguir el estándar al pie de la letra, pero sí mantener consistencia.

---

# 126. Pull Requests

Todo cambio relevante deberá integrarse mediante Pull Request, incluso en proyectos personales cuando exista una rama `develop`.

La Pull Request actuará como punto de revisión y documentación del cambio.

---

# 127. Pull Request Structure

Toda Pull Request incluirá:

* objetivo;
* cambios principales;
* impacto;
* checklist;
* referencias (cuando proceda).

Esto facilitará futuras revisiones del historial.

---

# 128. Merge Strategy

Método recomendado.

```text id="git019"
Squash and Merge
```

Ventajas.

* historial limpio;
* un commit representativo por funcionalidad;
* menor ruido.

Excepciones podrán justificarse cuando el historial detallado aporte valor.

---

# 129. Branch Protection

En proyectos maduros se recomienda proteger la rama `main`.

Reglas sugeridas.

* impedir pushes directos;
* requerir Pull Request;
* exigir checks automáticos cuando existan.

En proyectos personales esta protección será opcional, pero recomendable.

---

# 130. CI/CD Integration

Cuando el proyecto disponga de integración continua:

* los tests deberán ejecutarse automáticamente;
* el análisis estático formará parte del pipeline;
* las Releases deberán publicarse únicamente tras superar los controles definidos.

---

# 131. Changelog Synchronization

Cada Release deberá reflejarse en:

* CHANGELOG.md;
* GitHub Releases;
* PROJECT_STATUS (si procede).

Nunca deberán existir versiones inconsistentes.

---

# 132. Repository Maturity

La estrategia Git dependerá del nivel del proyecto.

| Level | Branches                                          |
| ----- | ------------------------------------------------- |
| L1    | main                                              |
| L2    | main + feature/*                                  |
| L3    | main + develop + feature/*                        |
| L4    | main + develop + feature/* + release/* + hotfix/* |

No todos los proyectos requieren el máximo nivel.

---

# 133. Anti-Patterns

No utilizar:

* commits gigantes;
* mensajes como "update", "changes", "fix";
* ramas con nombres ambiguos;
* versiones sin tags;
* releases sin documentación.

---

# 134. Quality Gates

Antes de crear una Release deberán verificarse:

* [ ] Tests superados.
* [ ] Documentación actualizada.
* [ ] CHANGELOG sincronizado.
* [ ] Tag creado.
* [ ] Release publicada.
* [ ] Rama principal estable.

---

# 135. Long-Term Vision

Todos los proyectos estratégicos compartirán la misma estrategia Git.

Esto permitirá que cualquier colaborador o recruiter comprenda inmediatamente el flujo de trabajo utilizado, independientemente del repositorio.

---

# 136. Part 5 Conclusions

El estándar **GRS-004** transforma Git en una parte esencial de la calidad del proyecto.

La estrategia de ramas, commits y releases deja de depender de decisiones puntuales y pasa a formar parte de un proceso uniforme, mantenible y alineado con prácticas profesionales.

El resultado será un historial claro, una evolución trazable y una experiencia consistente en todo el ecosistema GitHub.

---

# 07 - GITHUB METADATA

# Part 6/8

# GRS-005 Repository Configuration, Automation & Security Standard

---

# 137. Purpose

El estándar **GRS-005** define la configuración oficial de GitHub para los repositorios del ecosistema profesional de Fran Ramirez.

Incluye:

* Issues;
* Pull Requests;
* Labels;
* Discussions;
* Wiki;
* GitHub Projects;
* GitHub Pages;
* GitHub Actions;
* Dependabot;
* Code Scanning;
* Secret Scanning;
* Branch Protection;
* Repository Rulesets;
* configuraciones de seguridad.

Su objetivo consiste en garantizar que cada funcionalidad de GitHub se habilite únicamente cuando aporte valor real al proyecto.

La configuración no deberá responder a una lista de funcionalidades disponibles.

Deberá responder a las necesidades concretas del repositorio.

---

# 138. Configuration Philosophy

GitHub ofrece numerosas funcionalidades.

No todas deberán activarse.

El principio general será:

```text id="config001"
Enable only what the project can maintain.
```

Una funcionalidad activada y abandonada transmite menor calidad que una funcionalidad deshabilitada deliberadamente.

---

# 139. Native GitHub First

Siempre que GitHub ofrezca una funcionalidad nativa suficientemente adecuada, se priorizará frente a soluciones externas.

Orden de preferencia:

```text id="config002"
Native GitHub Feature

↓

Versioned Repository Configuration

↓

Stable External Service

↓

Custom Tooling
```

Las soluciones personalizadas deberán justificarse por una necesidad que GitHub no cubra correctamente.

---

# 140. Configuration by Repository Maturity

La configuración dependerá del nivel de madurez establecido en `GRS-003`.

| Feature           |       L1 |          L2 |          L3 |                      L4 |
| ----------------- | -------: | ----------: | ----------: | ----------------------: |
| Issues            | Optional | Recommended |    Required |                Required |
| Pull Requests     | Optional | Recommended |    Required |                Required |
| Issue Templates   |       No |    Optional | Recommended |                Required |
| PR Template       |       No |    Optional |    Required |                Required |
| Labels            |    Basic |       Basic |    Standard |                Standard |
| Discussions       |       No |          No |    Optional |       Context-dependent |
| Wiki              |       No |          No |          No |             Exceptional |
| Projects          |       No |    Optional | Recommended |             Recommended |
| Pages             |       No |    Optional | Recommended |             Recommended |
| Actions           | Optional | Recommended |    Required |                Required |
| Dependabot        |       No | Recommended |    Required |                Required |
| Branch Protection |       No |    Optional | Recommended |                Required |
| Security Policy   |       No |    Optional | Recommended |  Required when relevant |
| Code Scanning     |       No |    Optional | Recommended | Required when supported |

El nivel superior no implica activar automáticamente todas las funcionalidades.

Cada una deberá mantener un propósito claro.

---

# 141. Issues

Las Issues se utilizarán como unidad principal para registrar trabajo, incidencias, deuda técnica y decisiones operativas.

---

## 141.1 Issue Objectives

Las Issues deberán servir para:

* describir un problema;
* proponer una mejora;
* registrar deuda técnica;
* documentar investigación;
* definir trabajo futuro;
* relacionar commits y pull requests;
* mantener trazabilidad.

No deberán convertirse en notas personales incomprensibles para terceros.

---

## 141.2 Issue Types

Categorías recomendadas:

```text id="config003"
Feature

Bug

Documentation

Technical Debt

Research

Maintenance

Security
```

No todos los proyectos necesitarán todas las categorías.

---

## 141.3 Issue Structure

Una Issue profesional deberá incluir, cuando proceda:

```text id="config004"
Context

Problem or Opportunity

Expected Outcome

Acceptance Criteria

Technical Notes

Related Work
```

Las Issues pequeñas podrán utilizar una estructura simplificada.

---

## 141.4 Acceptance Criteria

Los criterios deberán:

* ser verificables;
* describir resultados;
* evitar decisiones técnicas prematuras;
* permitir determinar cuándo el trabajo está terminado.

Ejemplo:

```text id="config005"
- [ ] The API returns paginated results.
- [ ] Invalid page values are rejected.
- [ ] Unit and integration tests cover the new behavior.
- [ ] Documentation is updated.
```

---

## 141.5 Issue Restrictions

No se utilizarán títulos como:

```text id="config006"
Fix stuff

Improve project

Changes

Pending

Review later
```

Se preferirán títulos concretos:

```text id="config007"
Add semantic validation for duplicated document identifiers

Document refresh-token rotation strategy

Remove generated coverage artifacts from version control
```

---

# 142. Issue Templates

Los repositorios L3 y L4 deberán valorar plantillas de Issues.

---

## 142.1 Recommended Templates

```text id="config008"
bug-report.yml

feature-request.yml

documentation.yml

technical-debt.yml
```

Las plantillas basadas en formularios YAML serán preferibles cuando simplifiquen la captura de información.

---

## 142.2 Template Principles

Cada plantilla deberá:

* solicitar únicamente información necesaria;
* evitar formularios excesivamente largos;
* proporcionar ejemplos;
* aplicar labels cuando resulte útil;
* mantener un tono profesional.

---

## 142.3 Blank Issues

Las Issues en blanco podrán deshabilitarse cuando el proyecto acepte colaboración externa y necesite mantener una entrada estructurada.

En proyectos personales podrán permanecer disponibles para trabajo interno.

---

# 143. Pull Request Template

Los proyectos estratégicos deberán incluir:

```text id="config009"
.github/PULL_REQUEST_TEMPLATE.md
```

La plantilla deberá ayudar a revisar el cambio.

No deberá convertirse en burocracia.

---

## 143.1 Canonical Pull Request Structure

```markdown id="config010"
## Summary

Briefly describe the purpose of this pull request.

## Changes

- Change one
- Change two

## Validation

- [ ] Tests pass locally
- [ ] Documentation is updated
- [ ] No sensitive information is included
- [ ] The change has been reviewed in GitHub

## Screenshots or Evidence

Add visual or technical evidence when relevant.

## Related Issues

Closes #
```

Las secciones sin contenido podrán omitirse en pull requests pequeñas.

---

## 143.2 Pull Request Evidence

Se incluirá evidencia cuando el cambio afecte a:

* interfaces;
* documentación visual;
* pipelines;
* arquitectura;
* cobertura;
* resultados de modelos;
* comportamiento reproducible.

La evidencia deberá ayudar a revisar.

No decorar la Pull Request.

---

## 143.3 Self-Review

Antes de solicitar o realizar el merge, incluso trabajando en solitario, deberá efectuarse una revisión final:

* diff completo;
* archivos añadidos;
* archivos eliminados;
* comentarios temporales;
* secretos;
* documentación;
* tests;
* alcance real.

La Pull Request funcionará como espacio de reflexión antes de integrar el cambio.

---

# 144. Labels

Las labels deberán mantener un vocabulario controlado.

---

## 144.1 Label Categories

Se recomienda agruparlas por función.

### Type

```text id="config011"
type: feature
type: bug
type: documentation
type: refactor
type: research
type: maintenance
```

### Priority

```text id="config012"
priority: critical
priority: high
priority: medium
priority: low
```

### Status

```text id="config013"
status: blocked
status: in progress
status: ready
status: needs review
```

### Area

Ejemplos:

```text id="config014"
area: backend
area: frontend
area: ai
area: documentation
area: infrastructure
```

---

## 144.2 Label Naming

Las labels utilizarán:

```text id="config015"
category: value
```

Ventajas:

* agrupación visual;
* orden alfabético;
* menor ambigüedad;
* reutilización entre proyectos.

---

## 144.3 Label Colors

Los colores deberán seguir una lógica común:

| Category | Color Intent            |
| -------- | ----------------------- |
| Type     | Neutral or domain-based |
| Priority | Red to gray scale       |
| Status   | Semantic                |
| Area     | Project accent palette  |

El texto de la label continuará siendo la fuente principal de significado.

---

## 144.4 Label Restrictions

Se evitarán:

* labels duplicadas;
* sinónimos;
* colores sin lógica;
* labels sin uso;
* estados contradictorios;
* más categorías de las necesarias.

---

# 145. GitHub Projects

GitHub Projects podrá utilizarse para planificación visible y seguimiento.

No será obligatorio en todos los repositorios.

---

## 145.1 Valid Uses

* roadmap operativo;
* backlog;
* planificación de releases;
* seguimiento de módulos;
* visualización de estado;
* coordinación entre varios repositorios.

---

## 145.2 Project Scope

Cuando varios repositorios pertenezcan al mismo producto, se preferirá un proyecto a nivel de usuario u organización frente a varios tableros aislados.

Ejemplo:

```text id="config016"
Dental Clinic

├── dental-front
├── dental-back
└── dental-back-spring
```

podría gestionarse mediante un único Project.

---

## 145.3 Recommended Views

```text id="config017"
Backlog

Current Iteration

Roadmap

By Priority

By Repository
```

No deberán crearse vistas sin un uso real.

---

## 145.4 Project Maintenance

Un Project abandonado deberá:

* actualizarse;
* cerrarse;
* eliminarse;
* o marcarse claramente como histórico.

No deberá permanecer mostrando trabajo obsoleto como si continuara activo.

---

# 146. Discussions

GitHub Discussions solo se habilitará cuando exista una comunidad o una necesidad de conversación asíncrona distinta a las Issues.

---

## 146.1 Valid Uses

* preguntas y respuestas;
* ideas abiertas;
* anuncios;
* feedback;
* comunidad;
* soporte no asociado a un bug concreto.

---

## 146.2 Initial Policy

Para la primera versión del ecosistema:

```text id="config018"
GitHub Discussions disabled by default
```

Motivos:

* proyectos mantenidos principalmente por una persona;
* contribuciones externas limitadas;
* riesgo de secciones vacías;
* coste adicional de moderación.

---

## 146.3 NovaCoquinaria

NovaCoquinaria permanecerá inicialmente con Discussions deshabilitado mientras no se acepten contribuciones externas.

Podrá reevaluarse cuando:

* la documentación sea estable;
* exista interés externo;
* se abra una comunidad;
* puedan atenderse consultas.

---

# 147. Wiki

La Wiki permanecerá deshabilitada por defecto.

---

## 147.1 Rationale

La documentación deberá:

* versionarse junto al código;
* revisarse mediante Git;
* incluirse en `docs/`;
* poder desplegarse con MkDocs o GitHub Pages.

La Wiki introduce una segunda fuente de verdad y dificulta la sincronización.

---

## 147.2 Exception

Solo podrá habilitarse cuando:

* exista una comunidad que necesite editar contenido sin modificar el repositorio;
* la información no pertenezca al producto versionado;
* exista una estrategia explícita de gobernanza.

---

# 148. GitHub Pages

GitHub Pages se utilizará cuando mejore significativamente el acceso a documentación o demos estáticas.

---

## 148.1 Valid Uses

* documentación MkDocs;
* Javadoc;
* informes de cobertura seleccionados;
* demos frontend estáticas;
* documentación de APIs;
* páginas de proyecto;
* visualizaciones estáticas.

---

## 148.2 Invalid Uses

No se utilizará para:

* publicar contenido incompleto;
* mantener una segunda versión manual del README;
* exponer archivos generados sin contexto;
* simular una demo funcional cuando no lo sea.

---

## 148.3 Deployment

La publicación deberá automatizarse mediante GitHub Actions cuando resulte viable.

El contenido publicado deberá proceder de una fuente versionada.

---

## 148.4 NovaCoquinaria Priority

NovaCoquinaria es un candidato prioritario para GitHub Pages mediante MkDocs porque:

* ya dispone de documentación estructurada;
* la navegación web mejora la comprensión;
* el resultado representa una parte esencial del producto;
* permite mostrar el sistema de conocimiento sin exigir clonar el repositorio.

---

# 149. GitHub Actions

GitHub Actions será el sistema de automatización preferente para repositorios alojados en GitHub.

---

## 149.1 Workflow Objectives

Los workflows podrán cubrir:

* tests;
* linting;
* build;
* análisis estático;
* validación documental;
* generación de documentación;
* despliegue;
* releases;
* security scanning;
* validación de enlaces.

---

## 149.2 Workflow Principles

Cada workflow deberá:

* tener un nombre descriptivo;
* ejecutar una responsabilidad principal;
* utilizar versiones explícitas de acciones;
* evitar permisos innecesarios;
* fallar de forma comprensible;
* ser reproducible;
* mantenerse actualizado.

---

## 149.3 Workflow Naming

Ejemplos:

```text id="config019"
CI

Documentation Validation

Security Scan

Release

Deploy Documentation
```

Nombres de archivos:

```text id="config020"
ci.yml

documentation.yml

security.yml

release.yml

deploy-docs.yml
```

---

## 149.4 Trigger Strategy

Los triggers deberán limitarse al trabajo necesario.

Ejemplo:

```text id="config021"
pull_request:
  branches:
    - develop
    - main

push:
  branches:
    - main
```

Se utilizarán filtros de rutas cuando reduzcan ejecuciones innecesarias.

---

## 149.5 Permissions

Los workflows utilizarán el principio de mínimo privilegio.

Ejemplo:

```yaml id="config022"
permissions:
  contents: read
```

Los permisos de escritura solo se habilitarán para workflows que realmente necesiten publicar o crear releases.

---

## 149.6 Action Pinning

Las acciones deberán referenciar:

* versiones mayores o menores mantenidas;
* o commits concretos en entornos de mayor seguridad.

No se utilizará una referencia flotante no controlada cuando exista riesgo de cambios incompatibles.

---

## 149.7 Secrets

Los secretos deberán almacenarse exclusivamente en:

* GitHub Actions Secrets;
* Environments;
* variables protegidas.

Nunca en:

* workflows;
* README;
* `.env` versionados;
* ejemplos reales;
* capturas.

---

# 150. Continuous Integration Baseline

Todo proyecto estratégico deberá aspirar a un workflow básico de integración continua.

---

## 150.1 Java Baseline

```text id="config023"
Checkout

↓

Configure JDK

↓

Resolve Dependencies

↓

Compile

↓

Run Tests

↓

Generate Coverage

↓

Static Analysis
```

---

## 150.2 Python Baseline

```text id="config024"
Checkout

↓

Configure Python

↓

Install Dependencies

↓

Lint

↓

Run Tests

↓

Generate Coverage

↓

Project-Specific Validation
```

---

## 150.3 Documentation Baseline

```text id="config025"
Markdown Validation

↓

Link Validation

↓

Metadata Validation

↓

Build Documentation
```

NovaCoquinaria deberá aplicar una variante avanzada de este flujo.

---

# 151. Dependabot

Dependabot deberá habilitarse en repositorios estratégicos con dependencias mantenidas.

---

## 151.1 Supported Ecosystems

Podrá configurarse para:

* Maven;
* npm;
* pip;
* GitHub Actions;
* Docker.

---

## 151.2 Update Frequency

Frecuencia recomendada:

```text id="config026"
weekly
```

Una frecuencia diaria generaría ruido innecesario en proyectos personales.

---

## 151.3 Pull Request Limits

Se limitará el número de Pull Requests simultáneas para evitar saturar el repositorio.

Ejemplo:

```text id="config027"
open-pull-requests-limit: 5
```

---

## 151.4 Grouped Updates

Cuando resulte posible, las actualizaciones menores compatibles podrán agruparse.

Las dependencias críticas o de seguridad deberán mantenerse separadas cuando facilite su revisión.

---

## 151.5 Dependabot Maintenance

Activar Dependabot implica:

* revisar alertas;
* atender actualizaciones;
* cerrar PR obsoletas;
* resolver incompatibilidades;
* no acumular decenas de propuestas sin gestionar.

Si no puede mantenerse, deberá ajustarse su frecuencia o alcance.

---

# 152. Security Features

Los repositorios públicos deberán aprovechar las funcionalidades de seguridad disponibles de forma proporcional al riesgo.

---

## 152.1 Security Baseline

Todo repositorio estratégico deberá considerar:

* Dependabot alerts;
* dependency graph;
* secret scanning;
* push protection;
* code scanning;
* `SECURITY.md`;
* branch protection;
* revisión de permisos de workflows.

---

## 152.2 Secret Scanning

Secret scanning deberá habilitarse cuando esté disponible.

Push protection deberá utilizarse para reducir el riesgo de publicar credenciales accidentalmente.

---

## 152.3 Code Scanning

GitHub CodeQL podrá habilitarse cuando:

* el lenguaje sea compatible;
* el repositorio tenga una base de código relevante;
* pueda mantenerse;
* los resultados se revisen.

No deberá activarse únicamente para mostrar un badge.

---

## 152.4 Security Policy

`SECURITY.md` será requerido para proyectos estratégicos que:

* gestionen autenticación;
* procesen datos personales;
* expongan APIs;
* se desplieguen públicamente;
* incluyan modelos sanitarios;
* acepten reportes externos.

---

## 152.5 Medical and AI Projects

Cognitiva AI deberá incluir además:

* disclaimer de investigación;
* limitaciones de uso;
* información sobre datos;
* riesgos de interpretación;
* ausencia de finalidad diagnóstica;
* procedimiento de reporte cuando corresponda.

---

# 153. Branch Protection and Rulesets

Los repositorios L3 y L4 deberán utilizar protección de ramas o Rulesets cuando resulte viable.

---

## 153.1 Main Protection

Reglas recomendadas para `main`:

* require a pull request;
* require status checks;
* require conversation resolution;
* prevent force pushes;
* prevent deletion;
* restrict direct pushes when practical.

---

## 153.2 Develop Protection

`develop` podrá exigir:

* status checks;
* Pull Request;
* conversación resuelta.

La configuración podrá ser menos estricta que `main`.

---

## 153.3 Solo Maintainer Adaptation

En proyectos personales deberá evitarse una configuración que bloquee el trabajo por ausencia de revisores externos.

No se exigirá necesariamente:

```text id="config028"
Required approving reviews: 1
```

si el único mantenedor es Fran.

Sí podrá exigirse:

* Pull Request;
* checks;
* resolución de conversaciones;
* no force push.

---

## 153.4 Ruleset Priority

Los Rulesets serán preferibles cuando permitan aplicar reglas consistentes a varias ramas o repositorios.

La configuración deberá documentarse para evitar reglas invisibles o difíciles de reproducir.

---

# 154. Environments

Los GitHub Environments se utilizarán cuando existan despliegues diferenciados.

Ejemplos:

```text id="config029"
development

staging

production

documentation
```

---

## 154.1 Environment Protection

Podrán utilizarse:

* secrets específicos;
* approval gates;
* deployment branches;
* variables;
* historial de despliegues.

En proyectos personales no se añadirá aprobación manual sin una necesidad real.

---

# 155. Repository Variables and Secrets

Se diferenciarán claramente:

### Variables

Configuración no sensible.

### Secrets

Información confidencial.

---

## 155.1 Naming

Se utilizarán nombres en mayúsculas y snake case:

```text id="config030"
DATABASE_URL

DEPLOYMENT_TOKEN

SONAR_TOKEN

DOCS_BASE_URL
```

Esta convención se limita a variables de entorno y no contradice `GRS-001`.

---

## 155.2 Secret Rotation

Los secretos deberán:

* tener un propietario;
* poder revocarse;
* renovarse cuando exista exposición;
* no reutilizarse innecesariamente entre proyectos.

---

# 156. Repository Permissions

Los permisos deberán seguir el principio de mínimo privilegio.

---

## 156.1 Collaborators

Solo se mantendrán colaboradores que:

* participen activamente;
* necesiten acceso;
* tengan un nivel de permiso adecuado.

Los accesos antiguos deberán revisarse y retirarse cuando dejen de ser necesarios.

---

## 156.2 External Applications

Las GitHub Apps y OAuth Apps deberán revisarse periódicamente.

No se mantendrán integraciones sin uso o con permisos excesivos.

---

# 157. Notifications

Las notificaciones deberán configurarse para facilitar mantenimiento sin generar ruido.

Prioridades:

* fallos de workflows;
* alertas de seguridad;
* Pull Requests;
* Issues relevantes;
* releases.

No será necesario seguir cada evento de cada repositorio.

---

# 158. Feature Decision Matrix

Antes de habilitar una funcionalidad deberá evaluarse:

| Question                                               | Required Answer |
| ------------------------------------------------------ | --------------- |
| ¿Resuelve una necesidad real?                          | Sí              |
| ¿Puede mantenerse?                                     | Sí              |
| ¿Evita duplicar otra herramienta?                      | Sí              |
| ¿Mejora la experiencia del visitante o mantenedor?     | Sí              |
| ¿Existe un propietario claro?                          | Sí              |
| ¿Puede deshabilitarse sin perder información esencial? | Preferiblemente |

Si varias respuestas son negativas, la funcionalidad no deberá habilitarse.

---

# 159. Project Configuration Profiles

Se definen perfiles iniciales para los proyectos estratégicos.

---

## 159.1 NovaCoquinaria

```text id="config031"
Issues: Enabled
Issue Templates: Recommended
Pull Requests: Enabled
Discussions: Disabled initially
Wiki: Disabled
Projects: Recommended
Pages: High priority
Actions: Required
Dependabot: Python + GitHub Actions
Security: Secret scanning + workflow review
```

---

## 159.2 OnlyFilm

```text id="config032"
Issues: Enabled
Pull Requests: Enabled
Projects: Optional
Pages: Optional
Actions: Required
Dependabot: Maven + GitHub Actions + Docker
Code Scanning: Recommended
Security Policy: Recommended
```

---

## 159.3 Aula Robótica

```text id="config033"
Issues: Enabled
Issue Templates: Required
Pull Requests: Enabled
Projects: Recommended
Pages: Documentation candidate
Actions: Required
Dependabot: pip + GitHub Actions + Docker
Code Scanning: Recommended
Security Policy: Required
```

---

## 159.4 Cognitiva AI

```text id="config034"
Issues: Enabled
Pull Requests: Enabled
Projects: Recommended for research backlog
Pages: Optional documentation site
Actions: Validation and reproducibility
Dependabot: pip + GitHub Actions
Code Scanning: Recommended
Security Policy: Required
Discussions: Disabled initially
```

---

## 159.5 Dental Clinic

```text id="config035"
Issues: Enabled
Pull Requests: Enabled
Project: Shared across repositories
Actions: Required
Dependabot: npm + Maven or npm + npm
Pages: Optional
Security Policy: Required
Branch Rules: Coordinated across repositories
```

---

## 159.6 Vanguard A/B Test

```text id="config036"
Issues: Optional
Pull Requests: Enabled
Projects: Not required
Pages: Optional dashboard summary
Actions: Reproducibility validation
Dependabot: pip + GitHub Actions
Security Policy: Not required unless data risks justify it
```

---

# 160. Configuration Anti-Patterns

No deberán utilizarse:

* Discussions vacías;
* Wiki desactualizada;
* GitHub Projects abandonados;
* Actions sin mantener;
* Dependabot con decenas de PR ignoradas;
* workflows con permisos globales;
* secretos compartidos sin necesidad;
* branch protection que bloquee al único mantenedor;
* plantillas extensas para cambios triviales;
* badges de seguridad sin procesos reales detrás.

---

# 161. Configuration Quality Gates

Antes de considerar correctamente configurado un repositorio estratégico deberá verificarse:

## Collaboration

* [ ] Issues configuradas de acuerdo con el proyecto.
* [ ] PR template disponible.
* [ ] Labels normalizadas.
* [ ] Projects habilitado solo cuando aporta valor.
* [ ] Discussions y Wiki tienen una decisión explícita.

## Automation

* [ ] Workflow de CI disponible.
* [ ] Tests o validadores se ejecutan.
* [ ] Workflows utilizan permisos mínimos.
* [ ] Secrets no están versionados.
* [ ] Dependabot está configurado y mantenido.

## Security

* [ ] Dependency graph habilitado.
* [ ] Alertas de seguridad revisadas.
* [ ] Secret scanning habilitado cuando esté disponible.
* [ ] Code scanning evaluado.
* [ ] `SECURITY.md` presente cuando procede.

## Governance

* [ ] `main` representa un estado estable.
* [ ] Rulesets o branch protection están documentados.
* [ ] Los permisos de colaboradores están revisados.
* [ ] Las integraciones externas siguen siendo necesarias.

---

# 162. Configuration Review Cadence

## Monthly

Solo cuando exista actividad:

* workflows fallidos;
* alertas;
* Dependabot;
* Issues bloqueadas.

## Quarterly

* Actions;
* permisos;
* secrets;
* branch rules;
* Projects;
* integraciones.

## Annual

* revisión completa de configuración;
* funcionalidades habilitadas;
* colaboradores;
* seguridad;
* automatización;
* documentación del estándar.

---

# 163. Configuration Definition of Done

Un repositorio se considerará configurado profesionalmente cuando:

* las funcionalidades activas tengan un propósito;
* la automatización proteja la calidad;
* la seguridad básica esté habilitada;
* la configuración no introduzca burocracia innecesaria;
* el mantenimiento pueda realizarse con un esfuerzo sostenible;
* cualquier visitante o colaborador comprenda cómo interactuar con el proyecto.

---

# 164. Part 6 Conclusions

El estándar **GRS-005** garantiza que las funcionalidades de GitHub se utilicen como herramientas de ingeniería y no como elementos decorativos.

Issues, Pull Requests, Actions, Pages, Dependabot y las funciones de seguridad deberán responder siempre a una necesidad real.

La calidad de la configuración no se medirá por el número de funcionalidades activadas.

Se medirá por la capacidad del repositorio para:

* mantener trazabilidad;
* proteger el código;
* automatizar validaciones;
* reducir riesgos;
* facilitar su evolución.

El resultado será un ecosistema con configuración profesional, pero adaptada a la realidad de proyectos mantenidos principalmente por una sola persona.

---

# 07 - GITHUB METADATA

# Part 7/8

# GRS-006 Portfolio Governance & Repository Lifecycle Standard

---

# 165. Purpose

El estándar **GRS-006** define cómo se gobierna el conjunto completo de repositorios del ecosistema GitHub de Fran Ramirez.

Su objetivo consiste en establecer criterios claros para decidir:

* qué repositorios deben ser públicos;
* cuáles deben permanecer privados;
* cuáles pueden formar parte del portfolio;
* cuáles deben fijarse;
* cuáles deben archivarse;
* cuáles deben retirarse;
* cómo gestionar forks;
* cómo presentar proyectos colaborativos;
* cómo mantener una narrativa profesional coherente.

La gobernanza del portfolio no consiste en acumular repositorios.

Consiste en seleccionar, mantener y evolucionar un conjunto limitado de evidencias técnicas.

---

# 166. Portfolio Philosophy

El portfolio deberá tratarse como un sistema curado.

No como un historial exhaustivo.

Cada repositorio público deberá tener una función reconocible dentro del ecosistema.

Un proyecto podrá existir sin formar parte del portfolio principal.

Un repositorio podrá ser técnicamente correcto y, aun así, no aportar valor suficiente a la narrativa profesional.

---

# 167. Governance Principles

La gobernanza seguirá los siguientes principios:

* calidad sobre cantidad;
* evidencia sobre claims;
* claridad sobre exhaustividad;
* mantenimiento sobre acumulación;
* honestidad sobre apariencia;
* evolución sobre permanencia artificial.

---

# 168. Repository Portfolio Roles

Todo repositorio deberá clasificarse dentro de uno de los siguientes roles.

---

## 168.1 Strategic

Representa directamente una capacidad central del posicionamiento profesional.

Características:

* forma parte del Engineering Portfolio;
* puede aparecer fijado;
* recibe mantenimiento prioritario;
* debe alcanzar madurez L4;
* requiere identidad visual y documental completa.

Ejemplos:

```text
NovaCoquinaria
OnlyFilm
Aula Robótica
Cognitiva AI
Dental Clinic
```

---

## 168.2 Supporting

Demuestra una capacidad secundaria o complementaria.

Características:

* es público;
* dispone de README suficiente;
* puede alcanzar madurez L3;
* no necesita ocupar un pin;
* puede enlazarse desde LinkedIn, CV o una candidatura concreta.

Ejemplo:

```text
vanguard-ab-test
```

---

## 168.3 Learning

Documenta aprendizaje, prácticas o exploraciones.

Características:

* puede permanecer público si aporta contexto;
* debe identificarse claramente como educativo;
* no deberá confundirse con producto estable;
* no aparecerá en el portfolio principal;
* puede mantenerse en madurez L2 o L3.

---

## 168.4 Experimental

Explora una idea, tecnología o hipótesis.

Características:

* normalmente permanecerá privado;
* puede contener ramas o código no estabilizado;
* no requiere una identidad completa;
* podrá promocionarse si alcanza suficiente madurez.

---

## 168.5 Historical

Representa una etapa anterior con valor documental o profesional.

Características:

* puede permanecer público;
* deberá comunicar que no representa el nivel técnico actual;
* no recibirá mantenimiento activo;
* no deberá ocupar posiciones destacadas.

---

## 168.6 Archived

Ha finalizado su ciclo de vida.

Características:

* no se espera desarrollo adicional;
* permanece disponible por trazabilidad;
* GitHub deberá marcarlo como archivado;
* el README deberá indicar su estado;
* no formará parte del portfolio activo.

---

## 168.7 Private

No debe exponerse públicamente.

Motivos habituales:

* información sensible;
* código incompleto;
* experimento temporal;
* falta de derechos de publicación;
* escaso valor profesional;
* contenido corporativo;
* credenciales o datos personales;
* riesgo reputacional.

---

# 169. Repository Lifecycle

Todo repositorio seguirá un ciclo de vida explícito.

```text
Idea
↓
Private Experiment
↓
Active Development
↓
Public Candidate
↓
Public Release
↓
Strategic or Supporting
↓
Maintenance
↓
Historical
↓
Archived
```

No todos los repositorios recorrerán todas las etapas.

Muchos proyectos experimentales podrán finalizar sin hacerse públicos.

---

# 170. Lifecycle States

Se definen los siguientes estados canónicos.

| State              | Meaning                          |
| ------------------ | -------------------------------- |
| Concept            | Idea sin implementación estable  |
| Experimental       | Exploración técnica              |
| Active Development | Desarrollo principal en curso    |
| Public Preview     | Público, pero todavía no estable |
| Stable             | Versión funcional y documentada  |
| Maintenance        | Evolución limitada               |
| Historical         | Conservado por contexto          |
| Archived           | Cerrado y no mantenido           |

Estos estados deberán utilizarse de forma consistente en `PROJECT_STATUS.md`, README y Releases.

---

# 171. Public Repository Gate

Un repositorio solo podrá hacerse público cuando supere las siguientes comprobaciones.

## Legal and Ownership

* [ ] Existe derecho a publicar el contenido.
* [ ] La autoría está correctamente representada.
* [ ] Las dependencias y recursos permiten su publicación.
* [ ] La licencia está decidida o la ausencia está explicada.

## Security

* [ ] No contiene secretos.
* [ ] No contiene credenciales.
* [ ] No contiene datos personales.
* [ ] No contiene URLs internas.
* [ ] El historial Git ha sido revisado.

## Content

* [ ] Existe README.
* [ ] El propósito se comprende.
* [ ] El estado está comunicado.
* [ ] Las limitaciones están documentadas.
* [ ] La estructura es navegable.

## Professional Value

* [ ] Aporta evidencia útil.
* [ ] No perjudica la percepción del perfil.
* [ ] No duplica innecesariamente otro repositorio.
* [ ] Representa correctamente el nivel actual o su contexto histórico.

---

# 172. Public Preview Policy

Un proyecto podrá hacerse público antes de alcanzar estabilidad cuando exista valor en mostrar su evolución.

En ese caso deberá utilizar:

```text
Public Preview
```

y comunicar claramente:

* funcionalidades disponibles;
* limitaciones;
* roadmap;
* ausencia de garantías;
* estado experimental.

No se utilizará:

```text
Stable
```

ni:

```text
Production Ready
```

sin evidencia suficiente.

---

# 173. Private Repository Policy

Permanecerán privados los repositorios que:

* no puedan explicarse todavía;
* contengan pruebas desordenadas;
* estén sujetos a confidencialidad;
* incluyan material de terceros no publicable;
* no tengan una historia profesional clara;
* requieran una limpieza extensa;
* sean simples borradores.

La privacidad no deberá interpretarse como una carencia.

Es una decisión de gobernanza.

---

# 174. Promotion to Supporting

Un proyecto podrá promocionarse a `Supporting` cuando:

* sea público;
* tenga README profesional;
* demuestre una capacidad concreta;
* sea reproducible;
* no contenga riesgos;
* mantenga una presentación coherente;
* alcance al menos madurez L3.

---

# 175. Promotion to Strategic

Un proyecto podrá promocionarse a `Strategic` cuando:

* refuerce una capacidad central;
* represente el nivel técnico actual;
* tenga una narrativa diferenciada;
* alcance madurez L4;
* disponga de documentación completa;
* tenga estado y roadmap;
* tenga identidad visual;
* sea suficientemente estable;
* pueda mantenerse durante varios años.

---

# 176. Strategic Admission Questions

Antes de incorporar un proyecto al Engineering Portfolio deberá responderse:

1. ¿Qué capacidad demuestra?
2. ¿Existe otro proyecto que la demuestre mejor?
3. ¿Aporta una historia distinta?
4. ¿Está listo para una revisión técnica?
5. ¿El README permite comprenderlo rápidamente?
6. ¿Puede defenderse en una entrevista?
7. ¿Puede mantenerse?
8. ¿Representa el posicionamiento futuro?

Si varias respuestas son negativas, el proyecto no deberá promocionarse.

---

# 177. Portfolio Capacity

El Engineering Portfolio principal mostrará:

```text
5 proyectos
```

Máximo:

```text
6 proyectos
```

La limitación es deliberada.

Obliga a priorizar.

---

# 178. Pinned Repository Capacity

GitHub permite fijar hasta seis repositorios o gists.

La configuración recomendada será:

```text
5 strategic repositories
+
1 flexible slot
```

El sexto espacio podrá utilizarse para:

* proyecto estratégico nuevo;
* proyecto supporting relevante;
* proyecto temporal de especial interés;
* futuro sistema distribuido o de IA generativa.

---

# 179. Pin Eligibility

Un repositorio solo podrá fijarse cuando:

* sea estratégico;
* esté público;
* tenga metadata completa;
* tenga social preview;
* tenga README suficiente;
* comunique estado;
* no contenga problemas críticos;
* aporte una capacidad distinta.

---

# 180. Pin Ordering

El orden deberá responder a una narrativa profesional.

Configuración inicial recomendada:

```text
1. NovaCoquinaria
2. OnlyFilm
3. Aula Robótica
4. Cognitiva AI
5. Dental Clinic
6. Vanguard A/B Test or future strategic project
```

El orden podrá cambiar únicamente por evolución estratégica.

---

# 181. Unpin Policy

Un repositorio deberá retirarse de los pins cuando:

* exista un proyecto claramente superior;
* deje de representar el nivel actual;
* pase a mantenimiento sin relevancia estratégica;
* sea archivado;
* tenga problemas de calidad;
* duplique capacidades.

Retirar un pin no implica archivar el repositorio.

---

# 182. Portfolio Replacement Rule

Un proyecto nuevo no se añadirá simplemente por novedad.

Deberá:

* ocupar un espacio libre;
* o sustituir a otro.

La sustitución deberá justificarse mediante:

* mayor profundidad;
* mayor actualidad;
* mejor alineación;
* mejor documentación;
* nueva capacidad;
* menor redundancia.

---

# 183. Portfolio Balance

El conjunto deberá mantener cobertura equilibrada.

| Capability              | Expected Evidence       |
| ----------------------- | ----------------------- |
| Architecture            | NovaCoquinaria          |
| Java Backend            | OnlyFilm                |
| Python Backend          | Aula Robótica           |
| Artificial Intelligence | Cognitiva AI            |
| Full Stack              | Dental Clinic           |
| Data Analytics          | Vanguard or future slot |

La matriz se revisará cuando aparezcan proyectos nuevos.

---

# 184. Repository Degradation

Un proyecto podrá degradarse de `Strategic` a `Supporting` cuando:

* exista otro mejor;
* pierda relevancia;
* quede tecnológicamente obsoleto;
* no pueda mantenerse;
* su narrativa se vuelva redundante.

Podrá degradarse de `Supporting` a `Historical` cuando:

* deje de representar capacidades actuales;
* solo conserve valor formativo;
* no requiera más evolución.

---

# 185. Archive Policy

Un repositorio deberá archivarse cuando:

* haya concluido;
* no vaya a mantenerse;
* haya sido sustituido;
* conserve valor histórico;
* deba permanecer accesible en modo solo lectura.

Antes de archivarlo deberá:

* actualizarse el README;
* comunicar el motivo;
* indicar la alternativa si existe;
* cerrar o transferir Issues;
* publicar una release final cuando proceda;
* revisar enlaces externos.

---

## 185.1 Archive Notice

Ejemplo:

```markdown
> [!IMPORTANT]
> This repository is archived and no longer actively maintained.
> It is preserved for historical and educational purposes.
```

Cuando exista sustituto:

```markdown
> [!IMPORTANT]
> This repository has been superseded by [Project Name](URL).
```

---

# 186. Delete Policy

La eliminación será excepcional.

Solo deberá utilizarse cuando:

* exista información sensible;
* el repositorio se haya creado por error;
* no exista valor histórico;
* duplique completamente otro proyecto;
* haya problemas legales;
* pueda perjudicar seriamente el perfil.

En la mayoría de casos será preferible:

* privatizar;
* archivar;
* o limpiar.

---

# 187. Repository Transfer Policy

Un repositorio podrá transferirse cuando:

* pertenezca realmente a una organización;
* exista un nuevo propietario;
* un proyecto colaborativo deba independizarse;
* se cree una organización específica.

Antes de transferirlo deberá revisarse:

* visibilidad;
* permisos;
* enlaces;
* acciones;
* secrets;
* Pages;
* packages;
* ownership;
* atribución.

---

# 188. Fork Governance

Los forks requieren una política específica.

Un fork no deberá presentarse como trabajo completamente original.

---

## 188.1 Fork Classification

Un fork podrá clasificarse como:

### Reference Fork

Se conserva para consulta.

No forma parte del portfolio.

### Contribution Fork

Existe para contribuir al proyecto original.

No se presenta como producto propio.

### Evolution Fork

Ha recibido una evolución sustancial.

Puede formar parte del portfolio si documenta correctamente:

* origen;
* contribuciones propias;
* diferencias;
* estado;
* licencia;
* relación con el proyecto inicial.

---

# 189. Fork Portfolio Gate

Un fork solo podrá formar parte del Engineering Portfolio cuando:

* exista trabajo propio significativo;
* las mejoras estén documentadas;
* la atribución sea visible;
* la licencia lo permita;
* la narrativa sea honesta;
* el valor técnico sea demostrable;
* no exista una alternativa original mejor.

---

# 190. OnlyFilm Governance

OnlyFilm se clasificará como:

```text
Evolution Fork
```

Su incorporación al portfolio requerirá:

* explicar el origen;
* describir el estado recibido;
* listar las mejoras propias;
* documentar tests añadidos;
* documentar CI/CD;
* documentar refactorizaciones;
* mantener atribución;
* verificar licencia;
* evitar claims de autoría total.

---

# 191. Collaborative Project Governance

Los proyectos realizados en equipo deberán presentar la autoría de forma transparente.

---

## 191.1 Required Information

Deberán explicar:

* contexto colaborativo;
* integrantes;
* alcance del proyecto;
* responsabilidades propias;
* contribuciones posteriores;
* mantenimiento actual.

---

## 191.2 Personal Contribution

El README o la documentación deberá diferenciar entre:

```text
Team Work
```

y:

```text
My Contributions
```

Esto permite demostrar colaboración sin apropiarse del trabajo ajeno.

---

# 192. Dental Clinic Governance

Clínica Dental deberá presentarse como un producto colaborativo compuesto por varios repositorios.

La estrategia deberá definir:

* backend canónico;
* frontend canónico;
* backend alternativo;
* contribuciones propias;
* estado de cada componente;
* repositorio agregador futuro;
* mantenimiento.

No deberán ocupar tres posiciones fijadas.

---

# 193. Educational Project Governance

Un proyecto educativo podrá permanecer público cuando:

* tenga contenido propio relevante;
* documente el contexto;
* no se presente como producto comercial;
* muestre aprendizaje o evolución;
* mantenga atribución;
* no contenga material protegido.

---

## 193.1 Educational Notice

Podrá utilizarse:

```markdown
> [!NOTE]
> This project was originally developed in an educational context and has been preserved or extended as part of my engineering portfolio.
```

---

# 194. Repositories with Multiple Authors

Cuando existan varios autores se deberá revisar:

* CONTRIBUTORS;
* commits;
* README;
* licencia;
* atribución;
* About;
* descripción del portfolio.

No se utilizará la primera persona singular para describir trabajo colectivo sin matices.

---

# 195. Confidentiality Governance

Los proyectos profesionales sujetos a confidencialidad no deberán publicarse.

La experiencia adquirida podrá reflejarse mediante:

* descripción general en LinkedIn;
* CV;
* About del perfil;
* skills;
* proyectos personales equivalentes.

Nunca mediante:

* código interno;
* nombres de servicios;
* tickets;
* capturas;
* endpoints;
* configuraciones;
* datos.

---

# 196. Portfolio Audit Cadence

La revisión global se realizará:

## Quarterly

* pins;
* proyectos activos;
* enlaces;
* estado.

## Semiannual

* clasificación;
* portfolio;
* supporting projects;
* proyectos candidatos.

## Annual

* auditoría completa;
* repositorios públicos;
* privados;
* archived;
* forks;
* metadata;
* coherencia con carrera profesional.

---

# 197. Repository Health Signals

Durante la auditoría se evaluarán:

* última actividad;
* estado;
* issues abiertas;
* workflows;
* dependencias;
* documentación;
* release;
* seguridad;
* links;
* archivos generados;
* coherencia.

La fecha del último commit no será el único indicador.

Un proyecto estable puede no necesitar commits frecuentes.

---

# 198. Repository Governance Matrix

| Role         |     Public |          Portfolio |       Pin | Target Maturity |       Maintenance |
| ------------ | ---------: | -----------------: | --------: | --------------: | ----------------: |
| Strategic    |        Yes |                Yes |  Eligible |              L4 |              High |
| Supporting   |        Yes | Optional secondary | Temporary |              L3 |            Medium |
| Learning     |   Optional |                 No |        No |           L2–L3 |               Low |
| Experimental | Usually no |                 No |        No |           L1–L2 |         Temporary |
| Historical   |        Yes |                 No |        No |        Existing |           Minimal |
| Archived     |        Yes |                 No |        No |          Frozen |              None |
| Private      |         No |                 No |        No |             Any | Context-dependent |

---

# 199. Portfolio Decision Record

Los cambios importantes deberán documentarse.

Ejemplo:

```text
Decision:
Replace Vanguard A/B Test with EventDrivenPlatform.

Reason:
The new project better demonstrates distributed backend engineering and current career direction.

Impact:
Vanguard remains public as a supporting data project.
```

Podrá registrarse en:

* `REPOSITORY_AUDIT.md`;
* `PROJECT_STATUS.md`;
* pull request;
* historial de revisiones.

---

# 200. Governance Anti-Patterns

No deberán aplicarse prácticas como:

* fijar proyectos únicamente por antigüedad;
* publicar todo por defecto;
* ocultar autoría colaborativa;
* mantener forks sin explicar;
* conservar repositorios rotos por número;
* usar actividad artificial para aparentar mantenimiento;
* declarar estable un prototipo;
* eliminar sin revisar valor histórico;
* mantener proyectos públicos con secretos;
* confundir cantidad con experiencia.

---

# 201. Governance Quality Gates

La gobernanza se considerará correcta cuando:

## Classification

* [ ] Todo repositorio público tiene una función.
* [ ] Los estratégicos están identificados.
* [ ] Los supporting están diferenciados.
* [ ] Los históricos y archived comunican su estado.

## Portfolio

* [ ] Existen entre cinco y seis proyectos.
* [ ] Cada uno aporta una capacidad distinta.
* [ ] El orden es estratégico.
* [ ] Los pins coinciden con la narrativa.

## Ownership

* [ ] Los forks están atribuidos.
* [ ] Los proyectos colaborativos distinguen contribuciones.
* [ ] No existen claims engañosos.

## Lifecycle

* [ ] Los proyectos tienen estado.
* [ ] Los proyectos obsoletos se degradan o archivan.
* [ ] Los repositorios privados permanecen privados por decisión consciente.

## Maintenance

* [ ] El portfolio puede mantenerse con esfuerzo sostenible.
* [ ] No existen repositorios públicos críticos abandonados.
* [ ] Las auditorías se realizan periódicamente.

---

# 202. Governance Definition of Done

El portfolio se considerará gobernado profesionalmente cuando:

* cada repositorio tenga un rol explícito;
* la visibilidad responda a criterios definidos;
* los proyectos estratégicos estén curados;
* los pins representen el posicionamiento actual;
* los forks y colaboraciones se presenten con transparencia;
* los proyectos obsoletos no compitan con el trabajo actual;
* la evolución futura disponga de reglas claras;
* el ecosistema pueda crecer sin perder coherencia.

---

# 203. Part 7 Conclusions

El estándar **GRS-006** convierte el portfolio en un sistema gobernado.

La calidad del GitHub de Fran Ramirez no dependerá del número de repositorios acumulados, sino de la capacidad para:

* seleccionar;
* clasificar;
* mantener;
* promocionar;
* degradar;
* archivar;
* atribuir correctamente.

El resultado será un ecosistema honesto, sostenible y alineado con la evolución profesional.

Cada repositorio tendrá una razón para existir públicamente.

Cada proyecto destacado tendrá una función específica.

Y cada cambio en el portfolio responderá a una decisión estratégica, no a una preferencia momentánea.

---

# 07 - GITHUB METADATA

# Part 8/8

# GRS-007 Repository Assessment, Implementation & Maintenance Standard

---

# 204. Purpose

El estándar **GRS-007** define cómo evaluar, implantar y mantener los estándares de repositorio establecidos en este documento.

Su objetivo consiste en transformar los principios GRS en un sistema operativo que permita:

* medir la preparación de un repositorio;
* detectar carencias;
* priorizar mejoras;
* decidir si un proyecto está preparado para el portfolio;
* mantener la coherencia a largo plazo;
* incorporar nuevos repositorios sin improvisación.

El sistema de evaluación no pretende convertir la calidad de ingeniería en una cifra absoluta.

Su función será facilitar decisiones consistentes.

---

# 205. Assessment Philosophy

La evaluación deberá responder a cuatro preguntas:

```text
¿El repositorio se entiende?

¿El repositorio demuestra calidad técnica?

¿El repositorio puede mantenerse?

¿El repositorio representa correctamente el perfil profesional?
```

Una puntuación alta no compensará:

* información sensible;
* atribución incorrecta;
* enlaces rotos;
* documentación engañosa;
* ausencia de derechos de publicación.

Estos elementos funcionarán como bloqueos absolutos.

---

# 206. Assessment Dimensions

Cada repositorio se evaluará en ocho dimensiones.

| ID | Dimension                          |
| -- | ---------------------------------- |
| A1 | Identity and Metadata              |
| A2 | Documentation                      |
| A3 | Architecture and Code Organization |
| A4 | Testing and Quality                |
| A5 | Automation and Delivery            |
| A6 | Security and Legal                 |
| A7 | Maintenance and Lifecycle          |
| A8 | Portfolio Value                    |

---

# 207. Scoring Scale

Cada dimensión recibirá una puntuación entre 0 y 5.

| Score | Meaning           |
| ----: | ----------------- |
|     0 | Ausente o crítico |
|     1 | Muy insuficiente  |
|     2 | Parcial           |
|     3 | Aceptable         |
|     4 | Sólido            |
|     5 | Excelente         |

La puntuación deberá basarse en evidencia observable.

No en intención futura.

---

# 208. Dimension A1 — Identity and Metadata

Evalúa:

* nombre;
* descripción;
* topics;
* website;
* social preview;
* idioma;
* coherencia visual;
* estado visible.

## Score Guidance

### 0

No existe descripción ni metadata básica.

### 1

Metadata incompleta o confusa.

### 2

Nombre y descripción presentes, pero topics o imagen ausentes.

### 3

Metadata suficiente y comprensible.

### 4

Metadata completa, coherente y bien mantenida.

### 5

Identidad profesional plenamente integrada con el ecosistema.

---

# 209. Dimension A2 — Documentation

Evalúa:

* README;
* instalación;
* uso;
* arquitectura;
* documentación adicional;
* idiomas;
* navegación;
* reproducibilidad.

## Score Guidance

### 0

No existe documentación útil.

### 1

README mínimo o desactualizado.

### 2

Existe información básica, pero faltan pasos esenciales.

### 3

README suficiente para comprender y ejecutar.

### 4

Documentación estructurada y navegable.

### 5

Documentación madura, sincronizada y tratada como parte del producto.

---

# 210. Dimension A3 — Architecture and Code Organization

Evalúa:

* estructura del repositorio;
* separación de responsabilidades;
* modularidad;
* claridad del dominio;
* decisiones documentadas;
* ausencia de archivos basura;
* capacidad de evolución.

## Score Guidance

### 0

Estructura caótica o código no evaluable.

### 1

Organización mínima y difícil de comprender.

### 2

Estructura funcional con inconsistencias relevantes.

### 3

Organización clara y mantenible.

### 4

Arquitectura sólida y documentada.

### 5

Arquitectura diferencial, extensible y ampliamente explicada.

---

# 211. Dimension A4 — Testing and Quality

Evalúa:

* tests;
* cobertura;
* linting;
* análisis estático;
* quality gates;
* validaciones;
* tratamiento de errores;
* reproducibilidad de resultados.

## Score Guidance

### 0

No existe evidencia de calidad.

### 1

Comprobaciones manuales o tests testimoniales.

### 2

Tests parciales sin estrategia clara.

### 3

Cobertura razonable de comportamientos principales.

### 4

Estrategia de calidad automatizada y documentada.

### 5

Calidad integrada en arquitectura, CI y mantenimiento.

---

# 212. Dimension A5 — Automation and Delivery

Evalúa:

* GitHub Actions;
* build;
* CI;
* releases;
* Docker;
* despliegue;
* generación documental;
* validaciones automáticas;
* versionado semántico.

## Score Guidance

### 0

Todo el proceso es manual y no está documentado.

### 1

Existen scripts aislados o incompletos.

### 2

Automatización parcial.

### 3

CI o proceso de release funcional.

### 4

Pipeline sólido y mantenible.

### 5

Automatización integral, reproducible y coherente con el sistema.

---

# 213. Dimension A6 — Security and Legal

Evalúa:

* secretos;
* dependencias;
* licencia;
* atribución;
* autoría;
* tratamiento de datos;
* política de seguridad;
* cumplimiento del contexto del proyecto.

## Score Guidance

### 0

Existe un riesgo crítico o bloqueo legal.

### 1

Licencia o propiedad poco clara.

### 2

Requisitos básicos incompletos.

### 3

Seguridad y licencia suficientemente definidas.

### 4

Controles y documentación adecuados al riesgo.

### 5

Gobernanza legal y de seguridad especialmente madura.

---

# 214. Dimension A7 — Maintenance and Lifecycle

Evalúa:

* estado;
* roadmap;
* changelog;
* issues;
* dependencias;
* limpieza;
* actividad;
* sostenibilidad;
* archivado cuando procede.

## Score Guidance

### 0

Repositorio abandonado y sin contexto.

### 1

Estado desconocido.

### 2

Mantenimiento irregular o no documentado.

### 3

Estado y evolución razonablemente claros.

### 4

Mantenimiento consistente y gobernado.

### 5

Lifecycle completo, trazable y sostenible.

---

# 215. Dimension A8 — Portfolio Value

Evalúa:

* alineación profesional;
* diferenciación;
* profundidad;
* relevancia para recruiters;
* utilidad para Tech Leads;
* complementariedad;
* capacidad de defensa en entrevista.

## Score Guidance

### 0

No aporta valor al portfolio.

### 1

Valor profesional muy limitado.

### 2

Demuestra aprendizaje o una capacidad secundaria.

### 3

Aporta evidencia profesional clara.

### 4

Representa una competencia estratégica.

### 5

Proyecto insignia o altamente diferencial.

---

# 216. Weighting Model

Las dimensiones tendrán los siguientes pesos.

| Dimension                          |   Weight |
| ---------------------------------- | -------: |
| Identity and Metadata              |      10% |
| Documentation                      |      15% |
| Architecture and Code Organization |      15% |
| Testing and Quality                |      15% |
| Automation and Delivery            |      10% |
| Security and Legal                 |      10% |
| Maintenance and Lifecycle          |      10% |
| Portfolio Value                    |      15% |
| **Total**                          | **100%** |

La puntuación ponderada se expresará sobre 100.

---

# 217. Readiness Levels

A partir de la puntuación se definen cinco niveles.

|  Score | Level | Interpretation      |
| -----: | ----- | ------------------- |
|   0–39 | R0    | Not Ready           |
|  40–59 | R1    | Public with Caution |
|  60–74 | R2    | Public Ready        |
|  75–89 | R3    | Portfolio Ready     |
| 90–100 | R4    | Flagship Ready      |

---

## 217.1 R0 — Not Ready

El proyecto deberá permanecer privado, limpiarse o archivarse.

---

## 217.2 R1 — Public with Caution

Puede ser público por contexto educativo o histórico, pero no debe destacarse.

---

## 217.3 R2 — Public Ready

Es comprensible, seguro y suficientemente documentado.

No está preparado todavía para ser fijado.

---

## 217.4 R3 — Portfolio Ready

Puede formar parte del Engineering Portfolio y ser evaluado por recruiters o Tech Leads.

---

## 217.5 R4 — Flagship Ready

Representa de forma excepcional el nivel actual y puede ocupar las primeras posiciones.

---

# 218. Mandatory Blockers

Aunque la puntuación sea alta, un repositorio no podrá alcanzar R2 o superior si existe alguno de estos bloqueos:

* secretos o credenciales;
* datos personales;
* ausencia de derechos de publicación;
* licencia incompatible;
* atribución engañosa;
* malware o dependencias peligrosas;
* instrucciones críticas incorrectas;
* enlaces principales rotos;
* contenido corporativo confidencial;
* claims sanitarios o de seguridad irresponsables.

Los bloqueos deberán resolverse antes de continuar la evaluación.

---

# 219. Maturity and Readiness Relationship

La madurez documental y la preparación del portfolio son conceptos relacionados, pero distintos.

| Maturity | Typical Readiness |
| -------- | ----------------- |
| L1       | R0–R1             |
| L2       | R1–R2             |
| L3       | R2–R3             |
| L4       | R3–R4             |

Un repositorio L4 no será automáticamente R4.

También deberá tener valor estratégico y diferenciación.

---

# 220. Repository Assessment Card

Cada auditoría deberá producir una ficha como esta:

```text
Repository:
Role:
Lifecycle State:
Maturity Level:
Readiness Level:
Weighted Score:
Mandatory Blockers:
Primary Strength:
Primary Risk:
Next Promotion Condition:
```

Ejemplo conceptual:

```text
Repository: NovaCoquinaria
Role: Strategic
Lifecycle State: Active Development
Maturity Level: L4
Readiness Level: R3
Weighted Score: 88
Mandatory Blockers: None
Primary Strength: Knowledge architecture and documentation automation
Primary Risk: Complex onboarding for first-time visitors
Next Promotion Condition: Public documentation site and clearer quick start
```

---

# 221. Audit Evidence

La puntuación deberá respaldarse mediante referencias concretas.

Ejemplos:

* archivo README;
* pipeline;
* tests;
* release;
* documentación;
* licencia;
* issue;
* captura;
* configuración;
* diagrama;
* estado.

No se puntuará una capacidad que solo figure como intención en el roadmap.

---

# 222. Initial Ecosystem Targets

Objetivos recomendados para la primera fase:

| Repository            | Role                | Target Maturity | Target Readiness |
| --------------------- | ------------------- | --------------: | ---------------: |
| NovaCoquinaria        | Strategic           |              L4 |               R4 |
| OnlyFilm              | Strategic           |              L4 |               R3 |
| Aula Robótica         | Strategic           |              L4 |               R4 |
| Cognitiva AI          | Strategic           |              L4 |               R3 |
| Dental Clinic         | Strategic ecosystem |              L4 |               R3 |
| Vanguard A/B Test     | Supporting          |              L3 |            R2–R3 |
| Learning repositories | Learning            |              L2 |            R1–R2 |
| Experiments           | Experimental        |           L1–L2 |            R0–R1 |

---

# 223. Implementation Strategy

Los estándares GRS se implantarán progresivamente.

No se intentará transformar todos los repositorios de forma simultánea.

---

## Phase 1 — Standards Consolidation

Objetivos:

* finalizar `07_GITHUB_METADATA.md`;
* estabilizar identificadores GRS;
* corregir numeración;
* crear checklists reutilizables;
* aprobar el vocabulario oficial.

Entregables:

```text
07_GITHUB_METADATA.md
TOPICS_CATALOG.md
REPOSITORY_ASSESSMENT_TEMPLATE.md
```

---

## Phase 2 — Profile Repository

Objetivos:

* aplicar naming y metadata;
* crear README inglés y español;
* incorporar banner;
* configurar social preview;
* establecer reglas mínimas;
* publicar primera release del perfil.

---

## Phase 3 — NovaCoquinaria

Objetivos:

* completar metadata;
* revisar licencia;
* publicar documentación;
* aplicar social preview;
* configurar CI;
* definir contribution policy;
* alcanzar R4.

---

## Phase 4 — Java Portfolio

Objetivos:

* mejorar OnlyFilm;
* documentar condición de fork;
* corregir instrucciones;
* validar tests;
* publicar release;
* alcanzar R3.

---

## Phase 5 — Python Platform

Objetivos:

* limpiar Aula Robótica;
* revisar artifacts;
* añadir licencia;
* simplificar README;
* publicar documentación;
* alcanzar R4.

---

## Phase 6 — AI Portfolio

Objetivos:

* reorganizar Cognitiva AI;
* limpiar raíz;
* documentar modelo final;
* añadir model card;
* añadir data card;
* mejorar reproducibilidad;
* alcanzar R3.

---

## Phase 7 — Full Stack Ecosystem

Objetivos:

* definir backend canónico;
* coordinar repositorios;
* crear landing repository;
* documentar contribuciones;
* implantar CI;
* alcanzar R3.

---

## Phase 8 — Supporting Repositories

Objetivos:

* revisar Vanguard;
* clasificar learning repositories;
* privatizar experimentos;
* archivar históricos;
* reducir ruido público.

---

# 224. Rollout Priority

El orden inicial de ejecución será:

```text
1. GitHub Profile
2. NovaCoquinaria
3. OnlyFilm
4. Aula Robótica
5. Cognitiva AI
6. Dental Clinic
7. Vanguard
8. Repository cleanup
```

Este orden equilibra:

* visibilidad inmediata;
* posicionamiento Java;
* diferenciación;
* esfuerzo;
* valor profesional.

---

# 225. Minimum Viable Standard

Mientras se ejecuta la migración completa, todo repositorio público deberá cumplir al menos:

* nombre comprensible;
* descripción;
* README;
* estado;
* licencia o aclaración;
* ausencia de secretos;
* atribución correcta.

Este conjunto constituye el `GRS Minimum Public Baseline`.

---

# 226. Strategic Repository Baseline

Todo repositorio estratégico deberá cumplir:

* metadata completa;
* social preview;
* README inglés;
* versión española cuando se haya decidido mantenerla;
* arquitectura;
* Quick Start;
* testing;
* CI;
* licencia;
* roadmap;
* changelog;
* releases;
* lifecycle;
* configuración de seguridad proporcional.

---

# 227. Audit Workflow

La auditoría seguirá este proceso:

```text
Inventory
↓
Classification
↓
Blocker Review
↓
Dimension Scoring
↓
Readiness Level
↓
Backlog
↓
Implementation
↓
Reassessment
```

---

# 228. Reassessment Rules

Un repositorio deberá reevaluarse cuando:

* se publique una versión mayor;
* cambie de rol;
* se proponga como pin;
* se archive;
* se produzca una migración tecnológica;
* aparezca un riesgo;
* cambie su licencia;
* se abra a contribuciones.

---

# 229. Maintenance Cadence

## Monthly

Cuando exista actividad:

* alertas;
* pipelines;
* Dependabot;
* issues críticas;
* enlaces principales.

## Quarterly

* pins;
* Current Focus;
* proyectos estratégicos;
* metadata;
* workflows;
* seguridad.

## Semiannual

* scoring GRS;
* clasificación;
* portfolio;
* topics;
* licencias;
* readiness.

## Annual

* auditoría completa del ecosistema;
* repositorios privados;
* históricos;
* archivados;
* estándares;
* roadmap.

---

# 230. GRS Change Management

El estándar también deberá versionarse.

---

## 230.1 Patch Change

Correcciones editoriales o aclaraciones.

```text
1.0.0 → 1.0.1
```

---

## 230.2 Minor Change

Nuevo estándar compatible, checklist o criterio.

```text
1.0.0 → 1.1.0
```

---

## 230.3 Major Change

Cambio incompatible en niveles, scoring o gobernanza.

```text
1.0.0 → 2.0.0
```

---

# 231. Standard Identifiers

Los identificadores GRS deberán mantenerse estables.

No deberán reutilizarse para otros conceptos.

La versión consolidada deberá incluir un índice oficial.

Propuesta final:

| ID      | Standard                                   |
| ------- | ------------------------------------------ |
| GRS-001 | Repository Naming                          |
| GRS-002 | Repository About and Metadata              |
| GRS-003 | Repository Structure and Documentation     |
| GRS-004 | Git Strategy and Releases                  |
| GRS-005 | Configuration, Automation and Security     |
| GRS-006 | Portfolio Governance and Lifecycle         |
| GRS-007 | Assessment, Implementation and Maintenance |

Los estándares futuros comenzarán en `GRS-008`.

---

# 232. Global Audit Checklist

## Identity

* [ ] Nombre coherente.
* [ ] Description en inglés.
* [ ] Topics controlados.
* [ ] Website válido.
* [ ] Social Preview.

## Documentation

* [ ] README.
* [ ] Quick Start.
* [ ] Arquitectura.
* [ ] Roadmap.
* [ ] Estado.
* [ ] Documentación navegable.

## Engineering

* [ ] Estructura limpia.
* [ ] Tests.
* [ ] Linting.
* [ ] CI.
* [ ] Releases.
* [ ] Versionado.

## Security and Legal

* [ ] Secrets revisados.
* [ ] Licencia.
* [ ] Atribución.
* [ ] Dependencias.
* [ ] Datos.
* [ ] Security policy cuando procede.

## Governance

* [ ] Rol.
* [ ] Lifecycle.
* [ ] Maturity.
* [ ] Readiness.
* [ ] Pin eligibility.
* [ ] Maintenance owner.

---

# 233. Strategic Repository Definition of Done

Un repositorio estratégico se considerará completado cuando:

* alcance al menos R3;
* no tenga blockers;
* cumpla L4;
* pueda instalarse o comprenderse de forma reproducible;
* tenga metadata completa;
* tenga identidad visual;
* mantenga licencia y atribución;
* disponga de una release estable;
* muestre evidencias técnicas;
* pueda defenderse en una entrevista;
* tenga una estrategia de mantenimiento.

---

# 234. Ecosystem Definition of Done

El ecosistema GitHub se considerará gobernado profesionalmente cuando:

* todos los repositorios públicos estén clasificados;
* los estratégicos alcancen R3 o R4;
* los pins representen la narrativa profesional;
* los experimentos innecesarios permanezcan privados;
* los históricos comuniquen su contexto;
* los archivados estén correctamente cerrados;
* los forks mantengan atribución;
* las colaboraciones distingan autoría;
* la metadata utilice estándares comunes;
* la configuración sea mantenible;
* el sistema pueda crecer sin perder coherencia.

---

# 235. Initial Backlog

## Critical

* [ ] Consolidar `07_GITHUB_METADATA.md`.
* [ ] Corregir el índice GRS definitivo.
* [ ] Crear el catálogo de topics.
* [ ] Crear plantilla de assessment.
* [ ] Aplicar baseline al perfil.
* [ ] Revisar metadata de NovaCoquinaria.

## High

* [ ] Actualizar pins.
* [ ] Auditar licencias.
* [ ] Crear social previews.
* [ ] Revisar OnlyFilm como fork.
* [ ] Limpiar Aula Robótica.
* [ ] Reestructurar Cognitiva AI.

## Medium

* [ ] Diseñar labels.
* [ ] Crear templates de Issues.
* [ ] Crear template de Pull Request.
* [ ] Configurar Dependabot.
* [ ] Aplicar branch rules.
* [ ] Revisar repositorios secundarios.

## Low

* [ ] Evaluar organización propia.
* [ ] Evaluar generador de metadata.
* [ ] Automatizar assessment.
* [ ] Crear dashboard GRS.

---

# 236. Future Extensions

El sistema podrá ampliarse con:

```text
GRS-008 Topic Vocabulary
GRS-009 README Component Standard
GRS-010 Documentation Architecture
GRS-011 Security Baseline
GRS-012 AI and Data Project Standard
GRS-013 Open Source Contribution Standard
```

Solo se crearán nuevos estándares cuando exista una necesidad estable y reutilizable.

---

# 237. Success Metrics

El éxito del estándar no se medirá por la cantidad de archivos creados.

Se evaluará mediante:

* rapidez para comprender un repositorio;
* número reducido de problemas críticos;
* coherencia de metadata;
* reproducibilidad;
* calidad de los pins;
* facilidad de mantenimiento;
* capacidad de incorporar nuevos proyectos;
* referencias a proyectos durante procesos de selección.

---

# 238. Strategic Principles

El sistema GRS deberá recordar siempre:

* publicar es una decisión;
* documentar forma parte de desarrollar;
* automatizar debe reducir riesgo;
* configurar no significa activar todo;
* archivar es mejor que abandonar;
* atribuir correctamente genera credibilidad;
* un repositorio profesional debe poder explicarse solo;
* el portfolio debe mostrar el presente, no todo el pasado.

---

# 239. Final Conclusions

El sistema **GitHub Repository Standards** convierte el ecosistema de repositorios de Fran Ramirez en una plataforma profesional gobernada.

Los estándares definidos cubren:

* identidad;
* metadata;
* estructura;
* documentación;
* Git;
* releases;
* automatización;
* seguridad;
* lifecycle;
* portfolio;
* auditoría;
* mantenimiento.

A partir de este momento, un repositorio no se considerará preparado únicamente porque su código funcione.

Deberá también:

* explicarse;
* demostrarse;
* protegerse;
* versionarse;
* mantenerse;
* ocupar una función clara dentro del portfolio.

El resultado será un GitHub coherente, honesto y técnicamente sólido, preparado para evolucionar durante los próximos años sin convertirse de nuevo en una colección desordenada de repositorios.

---

# 240. Revision History

| Version | Date       | Description                                              |
| ------- | ---------- | -------------------------------------------------------- |
| 1.0.0   | 2026-08-05 | Primera versión completa de GitHub Repository Standards. |
