# 23 — Backend Adoption Discovery

## 1. Propósito

Este documento recoge un ejercicio de discovery orientado a evaluar cómo puede adoptarse GitHub Framework desde un repositorio backend existente.

El objetivo no es implementar una solución de adopción ni validar una funcionalidad previamente diseñada, sino observar qué ocurre cuando un repositorio real se contrasta con un Repository Template del Framework.

La pregunta principal que guía el ejercicio es:

> ¿Qué limita hoy que GitHub Framework sea realmente útil fuera de su propio repositorio?

Para responderla se utiliza `TPL-BACKEND` sobre un consumer existente, analizando qué responsabilidades del Template ya están satisfechas, cuáles requieren adaptación, cuáles están ausentes y cuáles pueden estar cubiertas mediante implementaciones equivalentes o especializadas.

El discovery busca producir evidencia que permita distinguir entre:

- problemas reales de adopción;
- capacidades ya presentes en el Framework;
- necesidades todavía no cubiertas;
- decisiones que requieren evaluación humana;
- tareas potencialmente automatizables;
- posibles soluciones técnicas que todavía no deben considerarse comprometidas.

Los resultados podrán utilizarse posteriormente como entrada para arquitectura, estándares, backlog o futuros incrementos del Framework.

Este documento no constituye por sí mismo una especificación, una decisión arquitectónica, una planificación de release ni una implementación.

---

## 2. Contexto

### 2.1 Estado de GitHub Framework

GitHub Framework dispone actualmente de una arquitectura basada en cuatro elementos principales:

```text
Standards
    ↓
Components
    ↓
Templates
    ↓
Reference Implementations
```

Los Standards establecen reglas y convenciones.

Los Components representan responsabilidades reutilizables.

Los Repository Templates componen Components para diferentes tipos de repositorio.

Las Reference Implementations proporcionan evidencia mediante uso real del Framework.

La evolución realizada hasta `v0.6.0` ha permitido disponer de:

- estándares de documentación y repositorio;
- un Repository Design System;
- un catálogo de Components;
- Repository Templates;
- Workflow Components;
- metadata estructurada para Components;
- validación determinista del propio catálogo del Framework.

Sin embargo, la existencia de estos elementos no demuestra por sí sola que un proyecto externo pueda adoptar el Framework de manera clara, gradual y segura.

La experiencia anterior de dogfooding validó principalmente elementos del Framework utilizando el propio repositorio GitHub Framework como consumer.

El presente discovery desplaza la observación hacia un repositorio distinto y ya existente.

### 2.2 Pregunta de discovery

La pregunta de partida es:

> ¿Qué limita hoy que GitHub Framework sea realmente útil fuera de su propio repositorio?

Esta pregunta no presupone cuál debe ser la solución.

En particular, no se asume que la siguiente evolución deba consistir en:

- un repository generator;
- una CLI;
- un manifest;
- una extensión del validator;
- una GitHub Action;
- otro mecanismo concreto de automatización.

Estas posibilidades pueden aparecer como hipótesis durante el discovery, pero deberán derivarse de necesidades observadas y no utilizarse como punto de partida.

### 2.3 Por qué `TPL-BACKEND`

Se selecciona `TPL-BACKEND` porque representa un tipo de repositorio ampliamente aplicable y permite contrastar el Framework con un proyecto software real.

El Template define una composición de Components clasificados como:

```text
Required
Recommended
Optional
```

La evaluación no consiste únicamente en comprobar si los archivos asociados a esos Components existen.

De acuerdo con el modelo de Repository Templates, una responsabilidad puede satisfacerse mediante:

- la implementación canónica del Component;
- una implementación propia;
- una especialización compatible;
- una implementación equivalente;
- una implementación distribuida entre varios artefactos.

Por tanto:

```text
Component availability ≠ Consumer conformance
```

y, de forma equivalente:

```text
File existence ≠ Responsibility satisfaction
```

Este principio resulta especialmente relevante al estudiar repositorios existentes, donde las responsabilidades pueden haberse implementado antes de adoptar GitHub Framework y sin utilizar su estructura o nomenclatura.

### 2.4 Por qué Only Film

Se selecciona **Only Film** como consumer experimental.

Only Film es un proyecto backend Java/Spring Boot existente y no fue creado a partir de `TPL-BACKEND`.

El repositorio utilizado para el ejercicio procede de un fork del proyecto original y no ha experimentado desarrollo posterior significativo.

Esta característica resulta útil para el discovery porque permite estudiar un escenario habitual de adopción:

```text
Existing repository
        +
Existing documentation
        +
Existing project decisions
        ↓
Framework adoption
```

El consumer ya dispone de una estructura de proyecto, README, documentación, tests y automatización propia.

Por tanto, el problema no consiste en crear un repositorio vacío, sino en determinar cómo puede incorporarse el Framework sin destruir, duplicar o sustituir innecesariamente aquello que ya existe.

---

## 3. Alcance del experimento

### 3.1 Consumer

```text
Consumer: Only Film
Repository type: Existing backend repository
Primary technology: Java / Spring Boot
Origin: Existing fork
```

Only Film se utiliza exclusivamente como consumer experimental para obtener evidencia sobre el proceso de adopción.

El ejercicio no pretende evaluar la calidad general del proyecto ni realizar una auditoría técnica de su código.

### 3.2 Template

```text
Template: TPL-BACKEND
Template version: 0.1.0
Maturity: L2
Status: Experimental
```

El Template se utiliza como referencia para identificar responsabilidades aplicables al consumer.

Su estado `Experimental` también es relevante: el ejercicio puede descubrir problemas no solo en el consumer, sino también en la propia composición, reglas o supuestos de `TPL-BACKEND`.

### 3.3 Modo de adopción

El escenario estudiado es:

```text
Adoption mode: Existing Repository
```

No se parte de un repositorio vacío.

El proceso conceptual es:

```text
Existing Repository
        ↓
Analyze
        ↓
Compare with Template
        ↓
Classify existing responsibilities and gaps
        ↓
Identify adoption actions
```

El objetivo es observar qué decisiones serían necesarias para adoptar el Framework conservando el valor existente del consumer.

### 3.4 Restricciones

Durante el discovery:

- Only Film permanece sin modificaciones;
- no se copian Components al consumer;
- no se generan archivos;
- no se corrigen los gaps encontrados;
- no se fuerza la estructura física del Template;
- no se considera un nombre de archivo como prueba suficiente de conformidad;
- no se modifica `TPL-BACKEND` como consecuencia inmediata de una observación;
- no se selecciona anticipadamente ninguna solución técnica.

Toda conclusión debe distinguir entre evidencia observada e interpretación.

### 3.5 Fuera de alcance

Quedan expresamente fuera de este ejercicio:

- modificar Only Film;
- realizar una migración real al Framework;
- generar archivos o documentación;
- corregir las referencias heredadas del fork;
- crear el `CHANGELOG.md` ausente;
- diseñar una CLI;
- diseñar un repository generator;
- definir un adoption manifest;
- extender el Framework Validator;
- implementar GitHub Actions para adopción;
- decidir el alcance de una nueva release;
- crear un Sprint;
- crear un milestone;
- asignar una nueva versión;
- promover automáticamente elementos existentes del Icebox.

Cualquiera de estos elementos podrá aparecer posteriormente como requirement candidate o solution hypothesis, pero no constituye un resultado predeterminado del discovery.

---

## 4. Método de evaluación

### 4.1 Responsabilidades frente a archivos

La unidad principal de evaluación es la **responsabilidad del Component**, no el archivo físico asociado a su implementación canónica.

Por tanto, una evaluación como:

```text
docs/ARCHITECTURE.md does not exist
        ↓
DOC-ARCHITECTURE = Missing
```

no es suficiente.

El proceso correcto es:

```text
Component responsibility
        ↓
Inspect consumer evidence
        ↓
Determine whether the responsibility exists
        ↓
Identify how it is implemented
        ↓
Classify adoption state
```

La evidencia puede encontrarse en:

- README;
- documentación específica;
- varios documentos conjuntamente;
- configuración;
- workflows;
- otros artefactos relevantes del repositorio.

Esto permite respetar implementaciones propias, equivalentes, especializadas o distribuidas.

### 4.2 Estados de adopción

Durante el discovery se utilizará inicialmente el siguiente modelo:

| Estado | Significado | Acción de adopción potencial |
|---|---|---|
| `Satisfied` | La responsabilidad ya está correctamente satisfecha | `PRESERVE` |
| `Partial` | Existe una implementación, pero necesita adaptación | `ADAPT` |
| `Equivalent` | La responsabilidad está satisfecha mediante otra implementación compatible | `ACCEPT` |
| `Missing` | La responsabilidad no está satisfecha | `ADD` cuando resulte necesaria |
| `Omissible` | La ausencia puede estar justificada por contexto o nivel de requisito | `JUSTIFY / IGNORE` |

Estos estados son instrumentos del discovery y no constituyen todavía un estándar formal del Framework.

Tampoco implican automáticamente una clasificación global del consumer como `CONFORMANT` o `NON-CONFORMANT`.

### 4.3 Evidencia

Cada evaluación debe poder relacionarse con evidencia concreta del consumer.

La evidencia se divide inicialmente en dos categorías.

#### Evidencia determinista

Puede identificarse mediante reglas objetivas.

Ejemplos:

```text
README.md exists
CHANGELOG.md does not exist
docs/ exists
.github/workflows/ exists
```

Este tipo de evidencia es potencialmente automatizable.

#### Evidencia semántica

Requiere interpretar el contenido y su relación con la responsabilidad evaluada.

Ejemplos:

```text
Does Quick Start describe the current consumer?

Does existing documentation satisfy DOC-ARCHITECTURE?

Is an existing section equivalent to a Framework Component?

Is omission of a Recommended Component justified?
```

La presencia física de un artefacto no proporciona necesariamente respuesta a estas preguntas.

Esta distinción será utilizada posteriormente para estudiar qué partes del proceso de adopción podrían automatizarse sin reducir la conformidad a comprobaciones superficiales del filesystem.

### 4.4 Límites de la evaluación

Este ejercicio utiliza un único consumer y un único Repository Template.

Por tanto, sus resultados constituyen:

```text
Discovery evidence
```

y no:

```text
Universal framework rules
```

Una observación encontrada en Only Film no debe convertirse automáticamente en un requisito general.

Asimismo, una necesidad observada en este consumer puede deberse a:

- características particulares de Only Film;
- su condición de fork;
- decisiones del proyecto original;
- una limitación de `TPL-BACKEND`;
- una limitación general del modelo de adopción;
- una combinación de los factores anteriores.

Será necesario separar estas posibilidades antes de formalizar nuevos Standards, Components o mecanismos de automatización.

El discovery tampoco pretende medir la calidad general de Only Film.

Un repositorio puede ser técnicamente rico y, al mismo tiempo, no satisfacer determinadas responsabilidades de `TPL-BACKEND`.

Del mismo modo, satisfacer un Template no constituye por sí solo una certificación de calidad técnica del software.

---

## 5. Baseline del consumer

Antes de evaluar `TPL-BACKEND`, se establece una baseline del estado existente de Only Film.

El objetivo de esta baseline no es valorar la calidad del repositorio, sino identificar qué activos existen antes de cualquier hipotética adopción de GitHub Framework.

Esta distinción es necesaria para poder determinar posteriormente qué debería preservarse, adaptarse, aceptarse como equivalente o añadirse.

### 5.1 Estructura existente

Only Film es un proyecto Java / Spring Boot con una estructura de aplicación ya desarrollada.

En la raíz del repositorio existen, entre otros:

```text
README.md
pom.xml
mvnw
mvnw.cmd
compose.sonar.yaml
lombok.config
.github/
docs/
src/
```

También existen artefactos generados o específicos del entorno de desarrollo, como `target/` y `.idea/`.

No existe actualmente:

```text
CHANGELOG.md
```

La ausencia de `CHANGELOG.md` constituye una observación determinista relevante porque `DOC-CHANGELOG` forma parte de los Required Components de `TPL-BACKEND`.

En este punto únicamente se registra la ausencia.

La acción que pudiera derivarse de ella se evaluará posteriormente.

### 5.2 README existente

Only Film dispone de un README amplio que ya cubre numerosas responsabilidades habituales de documentación de un proyecto backend.

Entre sus contenidos se encuentran:

- identificación y presentación del proyecto;
- descripción general;
- funcionalidades;
- arquitectura;
- tecnologías utilizadas;
- modelo de datos;
- seguridad;
- despliegue;
- Quick Start;
- estrategia y ejecución de tests;
- estructura del proyecto;
- credenciales de demostración;
- capturas de la aplicación;
- equipo;
- mejoras futuras;
- información sobre licencia;
- cierre del documento.

Por tanto, el escenario de adopción no parte de:

```text
No README
    ↓
Generate README
```

sino de:

```text
Existing rich README
        ↓
Analyze responsibilities
        ↓
Preserve useful content
        +
Adapt what requires consumer-specific correction
        +
Add only genuinely missing responsibilities
```

La baseline también revela contenido heredado del repositorio original.

En particular, el Quick Start mantiene referencias a:

```text
https://github.com/certidevs/g1_testing.git
cd g1_testing
```

y la sección final del README conserva igualmente una referencia al repositorio original.

Dado que el consumer utilizado es un fork sin desarrollo posterior significativo, estas referencias se consideran contenido heredado pendiente de personalización y no una degradación producida por GitHub Framework.

Este caso resulta relevante para el discovery porque demuestra que:

```text
Section exists
        ≠
Responsibility correctly satisfied
```

La existencia física de una sección `Quick Start` puede detectarse de forma relativamente objetiva.

Determinar si sus instrucciones corresponden realmente al consumer requiere, en cambio, interpretar su contenido y contexto.

### 5.3 Documentación existente

Only Film dispone de un directorio `docs/` con documentación previa a cualquier adopción del Framework.

Entre los artefactos encontrados se incluyen:

```text
docs/DAILY_29_04_2026.md
docs/PROCESO-COMPRA-TICKET.md
docs/PROPUESTA_ORGANIZACION.md
docs/PROYECTO_G1_CINE.md
```

junto con otros documentos de trabajo y diferentes capturas relacionadas con:

- funcionalidades de la aplicación;
- GitHub Actions;
- SonarQube;
- ejecución de tests.

La documentación existente es heterogénea.

Incluye, entre otros tipos de contenido:

- definición funcional del proyecto;
- descripción de entidades y relaciones;
- organización del equipo;
- planificación;
- notas de desarrollo;
- procesos funcionales;
- evidencias visuales.

Por ejemplo, `PROYECTO_G1_CINE.md` describe el dominio del proyecto, sus entidades principales, relaciones, repositorios, controladores y evolución prevista.

`PROCESO-COMPRA-TICKET.md` documenta un flujo funcional concreto relacionado con sesiones, tickets y compra.

`PROPUESTA_ORGANIZACION.md` corresponde principalmente a organización y coordinación del equipo.

La existencia de `docs/` no implica por sí misma que responsabilidades como:

```text
DOC-ARCHITECTURE
DOC-TESTING
DOC-DATABASE
DOC-DEPLOYMENT
DOC-SECURITY
```

estén necesariamente satisfechas.

Del mismo modo, la ausencia de documentos con esos nombres no demuestra que dichas responsabilidades estén ausentes.

Parte de esas responsabilidades puede encontrarse:

- dentro del README;
- distribuida entre varios documentos;
- representada mediante otros artefactos;
- parcialmente cubierta;
- o no resultar necesaria para el consumer.

Esta situación convierte a Only Film en un caso especialmente útil para evaluar adopción basada en responsabilidades en lugar de adopción basada únicamente en estructura física.

También se observa que `docs/` no dispone actualmente de un índice documental explícito que organice y permita navegar sus distintos contenidos.

Esta observación será relevante al evaluar posteriormente `README-DOCUMENTATION`.

### 5.4 Automatización existente

Only Film ya dispone de automatización mediante GitHub Actions.

Se han identificado dos workflows:

```text
.github/workflows/tests.yml
.github/workflows/sonar.yml
```

`tests.yml` organiza la ejecución de diferentes categorías de tests:

```text
Repository tests
Controller tests
Service tests
Security tests
Selenium E2E tests
```

El workflow también conserva artefactos de ejecución para los tests Selenium, incluyendo reportes y capturas en caso de fallo.

`sonar.yml` ejecuta:

```text
Build
    +
Tests
    +
Coverage
    +
SonarCloud analysis
```

utilizando Maven, JaCoCo y SonarCloud.

Los dos workflows utilizan actualmente:

```text
workflow_dispatch
```

por lo que su ejecución es manual.

La propia configuración de `tests.yml` documenta que esta decisión es intencionada para evitar ejecutar la suite automáticamente en cada push.

Por tanto, la baseline de automatización no es:

```text
No automation
```

sino:

```text
Existing consumer-specific automation
```

Esto introduce otra consideración relevante para el discovery.

Una futura adopción de GitHub Framework no debería asumir que un consumer carece de workflows ni sustituir automáticamente automatización existente.

Debería poder distinguir, al menos conceptualmente, entre:

```text
Framework responsibility
        ↓
Existing consumer workflow
        ↓
Compatible / adaptable / conflicting / missing
```

La mera presencia de `.github/workflows/` tampoco demuestra que una determinada responsabilidad del Framework esté satisfecha.

Será necesario evaluar el propósito y comportamiento de cada workflow cuando resulte relevante para el Template.

### 5.5 Resumen de la baseline

La baseline muestra que Only Film no es un repositorio vacío ni un consumer sin prácticas previas.

Dispone de:

```text
✓ README amplio
✓ documentación existente
✓ estructura de proyecto establecida
✓ tests
✓ automatización GitHub Actions
✓ análisis SonarCloud
✓ decisiones propias de organización y desarrollo
```

y también presenta elementos que pueden requerir evaluación o adaptación:

```text
△ referencias heredadas del fork
△ documentación heterogénea
△ ausencia de navegación documental clara
△ responsabilidades distribuidas entre distintos artefactos
✗ CHANGELOG.md ausente
```

Por tanto, el escenario real de adopción observado hasta este punto se aproxima más a:

```text
                 Existing Repository
                         │
                         ▼
                       Analyze
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       Preserve        Adapt         Identify gaps
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                 Framework Adoption
```

que a:

```text
Template
    ↓
Generate files
    ↓
Repository
```

Esta diferencia constituye una primera evidencia relevante del discovery, pero todavía no determina qué solución debería implementar GitHub Framework.

---

## 6. Evaluación de `TPL-BACKEND`

Una vez establecida la baseline del consumer, se contrastan las responsabilidades declaradas por `TPL-BACKEND` con la evidencia existente en Only Film.

La evaluación se realiza sobre responsabilidades y no sobre coincidencias literales de archivos o secciones.

Los resultados representan el estado observado durante este discovery y no modifican la definición formal de los Components ni establecen todavía nuevas reglas de conformidad.

### 6.1 Required Components

`TPL-BACKEND` define ocho Components Required.

| Component | Estado | Evidencia principal | Acción potencial |
|---|---|---|---|
| `README-HERO` | `Satisfied` | Identificación, presentación y badges del proyecto | `PRESERVE` |
| `README-OVERVIEW` | `Satisfied` | Descripción y visión general | `PRESERVE` |
| `README-FEATURES` | `Satisfied` | Funcionalidades documentadas | `PRESERVE` |
| `README-TECH-STACK` | `Satisfied` | Tecnologías y stack técnico | `PRESERVE` |
| `README-QUICK-START` | `Partial` | Existe Quick Start, pero conserva referencias del repositorio original | `ADAPT` |
| `README-DOCUMENTATION` | `Partial` | Existe `docs/` y documentación relacionada, pero falta una navegación documental clara | `ADAPT` |
| `README-FOOTER` | `Satisfied` | Cierre explícito del README | `PRESERVE` |
| `DOC-CHANGELOG` | `Missing` | No existe `CHANGELOG.md` | `ADD` |

Resultado:

```text
Required Components: 8

Satisfied: 5
Partial:   2
Missing:   1
```

#### `README-QUICK-START`

Only Film dispone de instrucciones de instalación y ejecución.

Sin embargo, el contenido mantiene referencias heredadas:

```text
https://github.com/certidevs/g1_testing.git
cd g1_testing
```

La responsabilidad existe estructuralmente, pero no está completamente adaptada al consumer actual.

Por tanto:

```text
Presence: yes
Responsibility: partially satisfied
Adoption action: ADAPT
```

Este caso demuestra que detectar una sección no basta para determinar su estado de adopción.

#### `README-DOCUMENTATION`

El repositorio dispone de un directorio `docs/` con documentación significativa y el README enlaza diferentes recursos y capturas.

Sin embargo, no se observa una navegación documental clara que presente `docs/` como conjunto organizado de documentación del proyecto.

Por tanto:

```text
Documentation exists
        +
Documentation references exist
        +
No clear documentation entry point
        ↓
Partial
```

La adopción no requeriría necesariamente sustituir la documentación existente, sino mejorar su descubribilidad y navegación.

#### `DOC-CHANGELOG`

No existe un `CHANGELOG.md`.

En este caso la evidencia es determinista:

```text
CHANGELOG.md exists = false
```

y no se ha identificado otro artefacto que desempeñe claramente esa responsabilidad.

Por tanto:

```text
DOC-CHANGELOG = Missing
```

Al tratarse de un Required Component, una futura adopción conforme debería resolver esta responsabilidad.

El discovery no determina todavía cómo debe hacerse.

---

### 6.2 Recommended Components

`TPL-BACKEND` define siete Components Recommended.

Su ausencia no implica automáticamente un defecto del consumer.

La evaluación debe determinar si la responsabilidad:

- ya está satisfecha;
- está parcialmente satisfecha;
- dispone de una implementación equivalente;
- o puede omitirse justificadamente.

| Component | Estado | Evidencia principal | Acción potencial |
|---|---|---|---|
| `README-STATUS` | `Partial` | Existen badges e indicadores, pero no un estado explícito y contextual del proyecto | `ADAPT` |
| `README-ARCHITECTURE` | `Satisfied` | El README describe arquitectura, capas y organización técnica | `PRESERVE` |
| `README-REPOSITORY-STRUCTURE` | `Satisfied` | Existe una sección de estructura del proyecto | `PRESERVE` |
| `README-TESTING` | `Satisfied` | Estrategia, categorías y ejecución de tests documentadas | `PRESERVE` |
| `DOC-ARCHITECTURE` | `Partial / Equivalent` | Arquitectura distribuida entre README y documentación existente | `EVALUATE / ACCEPT` |
| `DOC-PROJECT-STATUS` | `Missing / Omissible` | No existe documento específico de estado del proyecto | `JUSTIFY / IGNORE` |
| `DOC-TESTING` | `Partial / Equivalent` | Responsabilidad distribuida entre README, workflows y evidencias existentes | `EVALUATE / ACCEPT` |

#### `README-STATUS`

Los badges proporcionan información técnica sobre determinados estados del proyecto.

Sin embargo, no constituyen necesariamente una declaración explícita sobre:

- madurez;
- estado de desarrollo;
- mantenimiento;
- situación actual del proyecto.

La responsabilidad se considera parcialmente satisfecha.

```text
Indicators exist
        ≠
Explicit project status
```

#### `README-ARCHITECTURE`

El README documenta explícitamente la arquitectura y organización técnica del proyecto.

No se identifica una necesidad inmediata de sustituir esta implementación por una estructura canónica del Framework.

Resultado:

```text
Satisfied → PRESERVE
```

#### `README-REPOSITORY-STRUCTURE`

Existe una sección dedicada a la estructura del proyecto.

Resultado:

```text
Satisfied → PRESERVE
```

#### `README-TESTING`

El README documenta la estrategia de testing, categorías de pruebas y comandos de ejecución.

Además, el repositorio dispone de automatización específica para tests.

La responsabilidad README se considera satisfecha independientemente de que exista o no un documento `DOC-TESTING` separado.

Resultado:

```text
Satisfied → PRESERVE
```

#### `DOC-ARCHITECTURE`

Only Film no dispone de un único documento canónico equivalente a un hipotético `ARCHITECTURE.md`.

Sin embargo, existe información arquitectónica en el README y documentación adicional sobre dominio, entidades, relaciones y organización del proyecto.

La responsabilidad podría estar implementada de forma:

```text
Specialized
    +
Distributed
```

No obstante, la evidencia observada no justifica todavía elevar esta clasificación a `Satisfied` sin matices.

Por tanto se conserva:

```text
Partial / Equivalent
```

La decisión relevante para adopción no sería:

```text
Create ARCHITECTURE.md because it does not exist
```

sino:

```text
Evaluate existing architectural evidence
        ↓
Accept if sufficient
        or
Adapt if responsibility remains incomplete
```

#### `DOC-PROJECT-STATUS`

No se ha identificado un documento que desempeñe explícitamente la responsabilidad de mantener el estado actual del proyecto.

Sin embargo, `DOC-PROJECT-STATUS` es Recommended.

Por tanto:

```text
Missing
    +
Recommended
        ↓
Evaluate necessity
```

La ausencia puede ser razonable para un proyecto académico sin evolución activa posterior.

Resultado:

```text
Missing / Omissible
```

#### `DOC-TESTING`

La responsabilidad de testing aparece distribuida entre:

```text
README
+
.github/workflows/tests.yml
+
.github/workflows/sonar.yml
+
evidencias existentes
```

Existe por tanto evidencia sustancial, pero no necesariamente un documento especializado de testing.

El caso se clasifica provisionalmente como:

```text
Partial / Equivalent
```

y no como `Missing`.

Este caso vuelve a demostrar que:

```text
No canonical documentation file
        ≠
No documentation responsibility
```

---

### 6.3 Optional Components

`TPL-BACKEND` define trece Components Optional.

Su propósito no es maximizar cobertura documental.

Un Optional Component debe incorporarse únicamente cuando aporte valor real al consumer.

Por tanto, la evaluación se centra principalmente en su aplicabilidad.

| Component | Estado observado | Interpretación |
|---|---|---|
| `README-ROADMAP` | `Equivalent` | La sección de mejoras futuras desempeña una función equivalente |
| `README-CONTRIBUTING` | `Not identified` | No se observa necesidad actual suficiente |
| `README-DEMO` | `Equivalent` | Credenciales demo y capturas proporcionan evidencia funcional |
| `README-AUTHOR` | `Equivalent` | El equipo de desarrollo sustituye adecuadamente una autoría individual |
| `README-HIGHLIGHTS` | `Equivalent` | El README ya destaca aspectos técnicos relevantes |
| `README-LICENSE` | `Partial` | Existe sección de licencia, pero no se ha identificado una licencia formal |
| `DOC-ADR` | `Not identified` | No se observa necesidad actual suficiente |
| `DOC-API` | `Not applicable` | La API REST aparece como evolución futura, no como interfaz pública actual |
| `DOC-DATABASE` | `Partial / Equivalent` | Modelo de datos documentado dentro del contenido existente |
| `DOC-DEPLOYMENT` | `Partial / Equivalent` | El README contiene información de despliegue |
| `DOC-SECURITY` | `Equivalent` | El README documenta decisiones relevantes de seguridad |
| `DOC-DIAGRAMS` | `Not identified` | No se observa necesidad actual suficiente |
| `DOC-REFERENCES` | `Not identified` | No se observa necesidad actual suficiente |

Los estados `Not identified` y `Not applicable` se utilizan únicamente para el análisis de Optional Components y no se incorporan todavía al modelo general de estados de adopción.

#### Optional no significa pendiente

La ausencia de un Optional Component no debe convertirse automáticamente en una tarea.

Por ejemplo:

```text
DOC-ADR absent
```

no implica:

```text
ADD DOC-ADR
```

La pregunta correcta es:

```text
Does the consumer have architectural decisions
that require an explicit ADR lifecycle?
```

Si la respuesta no está respaldada por una necesidad real, la ausencia debe conservarse.

#### `README-ROADMAP`

El README dispone de una sección de mejoras futuras.

Aunque no utilice un `ROADMAP.md` independiente, desempeña una responsabilidad equivalente para el contexto actual del proyecto.

Resultado:

```text
Equivalent → ACCEPT
```

#### `README-DEMO`

El proyecto proporciona credenciales de demostración y abundante evidencia visual de funcionalidades.

La implementación no necesita adoptar literalmente una sección denominada `Demo` para satisfacer esa finalidad.

Resultado:

```text
Equivalent → ACCEPT
```

#### `README-AUTHOR`

Only Film es un proyecto de equipo.

La sección dedicada al equipo de desarrollo resulta más adecuada para este consumer que una interpretación individual de autoría.

Resultado:

```text
Equivalent → ACCEPT
```

Este caso muestra que una implementación consumer-specific puede ser más apropiada que reproducir literalmente el Component.

#### `README-LICENSE`

Existe una sección `Licencia` que describe el proyecto como académico y destinado a fines educativos.

Sin embargo, esa declaración no demuestra por sí sola la existencia de una licencia formal que establezca derechos de uso, modificación o redistribución.

Resultado:

```text
Partial
```

Al tratarse de un Optional Component en `TPL-BACKEND`, esta observación no afecta por sí sola a la conformidad Required del Template.

#### `DOC-API`

La documentación disponible presenta una API REST como posible evolución futura.

Por tanto, no existe evidencia suficiente para considerar actualmente necesaria documentación especializada de una interfaz pública de ese tipo.

Resultado:

```text
Not applicable
```

Este caso es especialmente relevante porque demuestra que un Template puede conocer una responsabilidad potencial sin exigir su materialización en todos los consumers.

#### Documentation Components equivalentes

Los casos:

```text
DOC-DATABASE
DOC-DEPLOYMENT
DOC-SECURITY
```

muestran nuevamente que una responsabilidad documental puede estar integrada dentro del README u otros artefactos existentes.

La adopción no debería fragmentar automáticamente documentación coherente únicamente para reproducir la estructura física del Framework.

La pregunta relevante debe seguir siendo:

```text
Is the responsibility adequately satisfied?
```

y no:

```text
Does the canonical file exist?
```

---

### 6.4 Resumen de cobertura

La evaluación completa de `TPL-BACKEND` muestra tres comportamientos diferentes según el nivel de requisito.

#### Required

```text
8 Components

5 Satisfied
2 Partial
1 Missing
```

Existe una base de adopción considerable.

La mayor parte de las responsabilidades Required ya se encuentran presentes antes de aplicar formalmente GitHub Framework.

Las acciones potenciales se concentran en:

```text
PRESERVE existing responsibilities
ADAPT existing but consumer-inaccurate responsibilities
ADD genuinely missing responsibilities
```

#### Recommended

```text
7 Components

3 Satisfied
1 Partial
2 Partial / Equivalent
1 Missing / Omissible
```

Los Recommended introducen una necesidad mayor de evaluación contextual.

En este nivel deja de ser suficiente preguntar si algo existe.

También es necesario determinar:

```text
Is the existing implementation sufficient?

Is an equivalent implementation acceptable?

Does this consumer actually need the responsibility?

Can omission be justified?
```

#### Optional

Los Optional muestran todavía con mayor claridad que cobertura y calidad no son equivalentes.

El consumer ya implementa varias responsabilidades Optional mediante soluciones propias o equivalentes, mientras que otras no presentan una necesidad demostrada.

Por tanto:

```text
More Components
    ≠
Better adoption
```

Una adopción correcta debe ser capaz de preservar una ausencia justificada.

### 6.5 Primera fotografía de adopción

El contraste completo permite representar provisionalmente Only Film de esta forma:

```text
                         TPL-BACKEND
                              │
                              ▼
                         Only Film
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
     Already useful     Needs adaptation      Missing
          │                   │                   │
      PRESERVE              ADAPT                 ADD
          │
          ├── canonical implementation
          ├── equivalent implementation
          ├── specialized implementation
          └── distributed implementation

Recommended / Optional
          │
          ├── ACCEPT equivalent
          ├── EVALUATE necessity
          ├── JUSTIFY omission
          └── IGNORE when not applicable
```

La principal característica del escenario observado es que la adopción de un repositorio existente no comienza con generación.

Comienza con análisis.

De forma provisional:

```text
Existing Repository
        ↓
Analyze
        ↓
Understand existing responsibilities
        ↓
Preserve / Adapt / Accept / Add / Omit
        ↓
Adopt Framework
```

Esto contrasta con un modelo simplificado:

```text
Select Template
        ↓
Generate canonical files
        ↓
Repository conforms
```

La evidencia obtenida hasta este punto no demuestra que la generación carezca de utilidad.

Sí demuestra que, para el escenario `Existing Repository`, la generación sin análisis previo podría:

- sobrescribir contenido válido;
- duplicar responsabilidades ya satisfechas;
- fragmentar documentación existente;
- ignorar implementaciones equivalentes;
- convertir Optional Components en ruido;
- confundir presencia física con conformidad.

Esta diferencia deberá analizarse en las siguientes secciones antes de derivar requirement candidates o solution hypotheses.

---

## 7. Observaciones

Las siguientes observaciones proceden del contraste entre `TPL-BACKEND` y el estado existente de Only Film.

Se registran deliberadamente antes de formular Findings, Requirement Candidates o Solution Hypotheses.

Una observación describe evidencia encontrada durante el experimento.

No constituye por sí misma:

- un problema general del Framework;
- un requisito;
- una decisión arquitectónica;
- una propuesta de implementación;
- una funcionalidad candidata para una futura release.

### 7.1 El consumer ya satisface gran parte del Template

Only Film no fue creado utilizando GitHub Framework.

Sin embargo, antes de cualquier adopción formal ya satisface cinco de las ocho responsabilidades Required de `TPL-BACKEND` y cubre parcial o equivalentemente otras responsabilidades Required, Recommended y Optional.

La situación observada no es:

```text
Template responsibility
        ↓
Absent from consumer
```

para la mayoría de los Components.

Con frecuencia es:

```text
Template responsibility
        ↓
Existing consumer implementation
```

La implementación existente puede encontrarse en el README, en documentación especializada, distribuida entre varios artefactos o expresada mediante una estructura diferente de la implementación canónica del Framework.

### 7.2 Presencia y satisfacción no son equivalentes

`README-QUICK-START` dispone de una implementación claramente identificable dentro del README.

Sin embargo, sus instrucciones conservan referencias al repositorio original del que procede el fork:

```text
https://github.com/certidevs/g1_testing.git
cd g1_testing
```

Por tanto, durante el experimento se han observado simultáneamente estas dos condiciones:

```text
Quick Start exists = true

Quick Start correctly represents current consumer = false
```

La presencia del artefacto y la satisfacción de su responsabilidad producen resultados distintos.

### 7.3 Ausencia física y ausencia de responsabilidad tampoco son equivalentes

Only Film no dispone necesariamente de archivos separados con nombres equivalentes a cada Documentation Component de `TPL-BACKEND`.

Sin embargo, diferentes responsabilidades se encuentran parcial o equivalentemente representadas dentro de:

```text
README.md
docs/
.github/workflows/
```

La arquitectura, testing, modelo de datos, despliegue y seguridad constituyen ejemplos de información que puede encontrarse integrada o distribuida entre artefactos existentes.

Por tanto, durante el análisis se han encontrado casos con la forma:

```text
Canonical file absent
        +
Responsibility evidence present
```

### 7.4 Algunas responsabilidades están distribuidas

No todas las responsabilidades observadas pueden asociarse de forma inequívoca a un único archivo.

El caso de testing combina evidencia procedente de:

```text
README.md
+
.github/workflows/tests.yml
+
.github/workflows/sonar.yml
+
documentation / execution evidence
```

De forma similar, la información arquitectónica se encuentra repartida entre el README y documentación adicional.

La unidad de responsabilidad y la unidad física de almacenamiento no presentan necesariamente una relación uno a uno.

### 7.5 Existen gaps que sí pueden identificarse directamente

No todas las evaluaciones requieren interpretación semántica compleja.

`DOC-CHANGELOG` proporciona un caso diferente.

No existe:

```text
CHANGELOG.md
```

y durante el análisis no se ha identificado otro artefacto que desempeñe claramente esa responsabilidad.

En este caso, la observación puede expresarse de forma directa:

```text
Required responsibility
        +
No identified implementation
        ↓
Missing
```

Esto contrasta con casos como `DOC-ARCHITECTURE` o `DOC-TESTING`, donde la ausencia de un archivo canónico no permite obtener la misma conclusión.

### 7.6 Existen implementaciones que requieren personalización, no sustitución completa

El Quick Start de Only Film contiene estructura y contenido útiles.

El problema observado se concentra en determinadas referencias heredadas del fork.

Por tanto, el estado encontrado no corresponde a:

```text
No implementation
```

sino a:

```text
Existing implementation
        +
Consumer-specific mismatch
```

El mismo patrón puede producirse en otros contenidos de un repositorio existente sin que todo el artefacto resulte inválido.

### 7.7 Existen implementaciones equivalentes

Algunas responsabilidades Optional aparecen satisfechas mediante estructuras distintas de las representaciones canónicas del Framework.

Por ejemplo:

```text
README-ROADMAP
```

encuentra una implementación equivalente en la sección de mejoras futuras.

Asimismo:

```text
README-AUTHOR
```

encuentra una representación contextual mediante la identificación del equipo de desarrollo.

La equivalencia observada no depende de que el consumer utilice el mismo título, estructura o archivo que el Component.

### 7.8 No todos los Components son necesariamente aplicables

Durante la evaluación de Optional Components se han encontrado responsabilidades cuya incorporación no está respaldada actualmente por una necesidad observable del consumer.

Entre ellas se encuentran casos como:

```text
DOC-ADR
DOC-DIAGRAMS
DOC-REFERENCES
```

También se ha observado un caso de no aplicabilidad contextual:

```text
DOC-API
```

La API REST aparece como una posible evolución futura, no como una interfaz pública actual que requiera documentación especializada.

Por tanto, la evaluación de Optional Components ha requerido distinguir entre:

```text
Missing
```

y situaciones como:

```text
Not identified
Not applicable
```

### 7.9 Los Recommended requieren juicio contextual

`DOC-PROJECT-STATUS` no dispone de una implementación claramente identificada.

Sin embargo, su nivel es Recommended y el consumer corresponde a un proyecto académico sin evolución posterior significativa.

Por tanto, durante la evaluación no ha sido suficiente registrar:

```text
DOC-PROJECT-STATUS absent
```

También ha sido necesario considerar:

```text
Does this consumer currently need it?
```

La evaluación de Recommended Components introduce así una dimensión contextual que no aparece en una comprobación puramente estructural.

### 7.10 La documentación existente es heterogénea

El directorio `docs/` contiene documentación de distinta naturaleza.

Se han encontrado contenidos relacionados con:

- definición funcional;
- dominio;
- entidades y relaciones;
- procesos;
- organización del equipo;
- planificación;
- notas de desarrollo;
- evidencias visuales.

La existencia del directorio:

```text
docs/
```

no permite determinar por sí sola qué responsabilidades documentales están satisfechas.

Tampoco existe actualmente un índice documental explícito que represente el conjunto como una estructura navegable.

### 7.11 El consumer ya dispone de automatización propia

Only Film contiene:

```text
.github/workflows/tests.yml
.github/workflows/sonar.yml
```

Estos workflows implementan automatización específica del proyecto para tests y análisis de calidad.

Por tanto, el consumer no presenta el estado:

```text
No workflows
```

sino:

```text
Existing project-specific workflows
```

La existencia de automatización previa forma parte del estado inicial del consumer antes de cualquier adopción del Framework.

### 7.12 La evidencia presenta diferentes grados de determinismo

Durante el experimento se han encontrado observaciones que pueden obtenerse directamente de la estructura del repositorio.

Por ejemplo:

```text
README.md exists
CHANGELOG.md does not exist
docs/ exists
.github/workflows/ exists
```

También se han encontrado evaluaciones que requieren interpretar contenido y contexto:

```text
Does Quick Start represent the current consumer?

Does existing documentation satisfy DOC-ARCHITECTURE?

Is an implementation equivalent to a Component?

Is omission of a Recommended Component justified?
```

Ambos tipos de evidencia intervienen en una misma evaluación de adopción.

### 7.13 El mismo consumer produce diferentes acciones de adopción

El contraste con `TPL-BACKEND` no ha producido una única acción uniforme.

Se han observado al menos los siguientes casos:

```text
Satisfied
    ↓
PRESERVE

Partial
    ↓
ADAPT

Equivalent
    ↓
ACCEPT

Missing Required
    ↓
ADD

Recommended / Optional without demonstrated need
    ↓
EVALUATE / JUSTIFY / OMIT
```

Por tanto, diferentes responsabilidades de un mismo consumer se encuentran en estados de adopción distintos.

### 7.14 La evaluación no ha requerido modificar el consumer

Todas las observaciones anteriores se han obtenido manteniendo Only Film sin modificaciones.

No ha sido necesario:

- copiar Components;
- generar archivos;
- reorganizar documentación;
- modificar workflows;
- corregir el README;
- añadir el CHANGELOG;
- introducir metadata de adopción.

El experimento ha podido separar:

```text
Analyze current state
```

de:

```text
Apply adoption changes
```

### 7.15 El Template también forma parte de lo que se está evaluando

El contraste no proporciona únicamente información sobre Only Film.

`TPL-BACKEND` tiene estado `Experimental`.

Por tanto, cuando una responsabilidad resulta difícil de aplicar, clasificar o interpretar, existen al menos dos posibles fuentes de la dificultad:

```text
Consumer-specific condition
```

o:

```text
Template / Framework model
```

El discovery no atribuye automáticamente cada discrepancia al consumer.

### 7.16 Resumen de observaciones

El experimento muestra una combinación de situaciones:

```text
Existing responsibility
Existing but inaccurate responsibility
Equivalent responsibility
Distributed responsibility
Missing responsibility
Potentially omissible responsibility
Not currently applicable responsibility
```

Estas situaciones aparecen dentro del mismo repositorio y frente al mismo Template.

Hasta este punto, el experimento únicamente establece que dichas situaciones existen.

La interpretación de qué significan para GitHub Framework corresponde a la siguiente fase del discovery.

---

## 8. Findings

Los Findings interpretan las observaciones obtenidas durante el experimento y expresan conocimiento potencialmente relevante para la evolución de GitHub Framework.

La relación utilizada es:

```text
Evidence
    ↓
Observation
    ↓
Finding
```

Un Finding no constituye todavía:

- un Requirement Candidate;
- una solución;
- una decisión arquitectónica;
- una funcionalidad comprometida;
- alcance para una futura release.

Para convertirse posteriormente en requisito, deberá demostrar que representa una necesidad suficientemente general del proceso de adopción y no únicamente una característica particular de Only Film.

### 8.1 La adopción de un repositorio existente es un problema de reconciliación

Only Film ya implementa gran parte de las responsabilidades de `TPL-BACKEND` antes de adoptar formalmente GitHub Framework.

Por tanto, para un repositorio existente, adoptar el Framework no consiste principalmente en transformar:

```text
Nothing
    ↓
Framework implementation
```

sino en reconciliar:

```text
Existing repository state
            +
Template responsibilities
            ↓
Adoption decisions
```

La adopción debe considerar simultáneamente lo que ya existe y lo que el Template espera.

Este escenario es fundamentalmente diferente de inicializar un repositorio nuevo.

### 8.2 Analizar precede a modificar

El experimento ha podido determinar el estado de adopción de numerosas responsabilidades sin realizar ninguna modificación sobre Only Film.

Esto permite separar conceptualmente dos fases:

```text
Analyze
    ↓
Understand current adoption state
```

y:

```text
Apply
    ↓
Perform selected adoption changes
```

El análisis no es simplemente una consecuencia de la modificación.

Es una actividad previa que permite decidir qué modificaciones, si alguna, resultan apropiadas.

### 8.3 La adopción no puede reducirse a generación

Only Film ya contiene:

- un README amplio;
- documentación;
- tests;
- workflows;
- decisiones de arquitectura;
- información de seguridad;
- información de despliegue.

Generar indiscriminadamente implementaciones canónicas para todas las responsabilidades de `TPL-BACKEND` podría producir:

```text
existing responsibility
        +
generated responsibility
        ↓
duplication
```

o:

```text
existing implementation
        ↓
replacement
        ↓
loss of consumer-specific value
```

La generación puede seguir siendo una posible herramienta para determinados escenarios, especialmente cuando una responsabilidad está realmente ausente.

Sin embargo, el experimento no respalda un modelo en el que generación y adopción sean conceptos equivalentes.

### 8.4 La conformidad requiere evaluar responsabilidades, no únicamente artefactos

El experimento confirma en un consumer externo el principio ya establecido por el modelo de Repository Templates:

```text
File existence ≠ Responsibility satisfaction
```

Only Film presenta ambos sentidos del problema.

#### Artefacto presente, responsabilidad incompleta

```text
README-QUICK-START
```

existe, pero conserva referencias heredadas del repositorio original.

#### Artefacto canónico ausente, responsabilidad presente

Responsabilidades como arquitectura o testing aparecen parcial o equivalentemente implementadas mediante contenido distribuido.

Por tanto, una evaluación basada exclusivamente en:

```text
file exists?
section exists?
```

produciría falsos positivos y falsos negativos.

### 8.5 La adopción necesita preservar implementaciones válidas

La evaluación ha identificado numerosas responsabilidades `Satisfied` o `Equivalent`.

En estos casos, adoptar el Framework no requiere crear una nueva implementación.

La acción relevante es:

```text
PRESERVE
```

o:

```text
ACCEPT
```

Esto introduce una propiedad importante del proceso de adopción:

> no modificar también puede ser una decisión válida de adopción.

El valor del Framework no depende de maximizar el número de artefactos que introduce en el consumer.

### 8.6 Adaptar es una operación distinta de añadir

`README-QUICK-START` demuestra que una responsabilidad puede existir y necesitar únicamente personalización.

El estado:

```text
Partial
```

no equivale a:

```text
Missing
```

y las acciones correspondientes tampoco son equivalentes:

```text
Partial → ADAPT

Missing → ADD
```

Esta diferencia evita tratar contenido parcialmente válido como si no existiera.

También permite conservar estructura y conocimiento útil del consumer.

### 8.7 La equivalencia es necesaria para adoptar repositorios heterogéneos

Only Film implementa algunas responsabilidades mediante estructuras diferentes de las representaciones canónicas del Framework.

Si la adopción exigiera coincidencia física estricta:

```text
Canonical representation
        =
Only valid representation
```

sería necesario reestructurar contenido válido únicamente para ajustarlo al Framework.

El experimento proporciona evidencia de un modelo diferente:

```text
Responsibility
      ↓
Canonical implementation
      OR
Equivalent implementation
      OR
Specialized implementation
      OR
Distributed implementation
```

La capacidad de reconocer equivalencia resulta especialmente importante para repositorios creados antes de adoptar GitHub Framework.

### 8.8 La aplicabilidad forma parte de la decisión de adopción

Los Optional Components han mostrado que una responsabilidad puede existir en el catálogo sin ser necesaria para un consumer concreto.

Por tanto, además de preguntar:

```text
Is it implemented?
```

la adopción puede requerir preguntar primero:

```text
Is it applicable?
```

Este Finding es diferente de la conformidad.

Una responsabilidad puede estar ausente porque:

```text
it is missing
```

o porque:

```text
it is not currently applicable
```

Confundir ambos casos produciría adopciones innecesariamente extensas.

### 8.9 El nivel de requisito modifica el significado de la ausencia

La misma observación:

```text
responsibility not identified
```

no tiene necesariamente la misma consecuencia para:

```text
Required
Recommended
Optional
```

En el experimento:

- un Required ausente representa un gap de adopción;
- un Recommended ausente requiere evaluar necesidad y posible justificación;
- un Optional ausente puede no requerir ninguna acción.

Por tanto, el proceso de adopción necesita interpretar conjuntamente:

```text
Responsibility state
        +
Requirement level
        +
Consumer context
```

### 8.10 La adopción combina evidencia determinista y semántica

Parte del análisis puede expresarse mediante hechos objetivos:

```text
README.md exists
CHANGELOG.md does not exist
docs/ exists
workflow exists
```

Otra parte requiere interpretar significado:

```text
Is Quick Start accurate?

Is architecture sufficiently documented?

Is this implementation equivalent?

Is omission justified?
```

Por tanto, el proceso completo no pertenece exclusivamente a uno de estos extremos:

```text
fully deterministic
```

ni:

```text
fully subjective
```

sino que combina ambos.

Esta distinción será relevante al estudiar posteriormente los límites de automatización.

### 8.11 Un resultado automatizable no implica una decisión automatizable

La ausencia de `CHANGELOG.md` puede detectarse automáticamente.

Sin embargo, otros pasos potenciales pueden seguir requiriendo decisiones adicionales.

De forma similar:

```text
docs/ exists
```

es determinista, mientras que:

```text
docs/ adequately satisfies documentation responsibilities
```

no lo es necesariamente.

Por tanto:

```text
Automatable evidence
        ≠
Automatable adoption decision
```

Este Finding evita asumir que todo aquello que puede detectarse mecánicamente puede resolverse correctamente de forma mecánica.

### 8.12 El estado de adopción necesita más expresividad que presente o ausente

El experimento ha necesitado distinguir al menos:

```text
Satisfied
Partial
Equivalent
Missing
Omissible
```

y durante Optional Components han aparecido además conceptos de aplicabilidad como:

```text
Not identified
Not applicable
```

Esto indica que un modelo binario:

```text
Present / Missing
```

no representa adecuadamente la adopción de un repositorio existente.

No obstante, el experimento todavía no demuestra que todos estos términos deban convertirse en estados formales del Framework.

Algunos pueden representar:

- estados;
- calificadores;
- decisiones;
- acciones;
- resultados de aplicabilidad.

La taxonomía deberá refinarse antes de formalizarla.

### 8.13 Estado y acción de adopción son conceptos diferentes

Durante el análisis han aparecido asociaciones como:

```text
Satisfied → PRESERVE
Partial → ADAPT
Equivalent → ACCEPT
Missing → ADD
Omissible → JUSTIFY / OMIT
```

Sin embargo, ambos lados representan conceptos diferentes.

Por ejemplo:

```text
Partial
```

describe el estado observado de una responsabilidad.

Mientras:

```text
ADAPT
```

describe una posible acción derivada.

Por tanto, el modelo emergente debe evitar mezclar:

```text
What exists?
```

con:

```text
What should be done?
```

Esta separación permitirá que una misma situación pueda producir decisiones diferentes según contexto y nivel de requisito.

### 8.14 La adopción puede necesitar registrar decisiones, no solo cambios

Algunas responsabilidades pueden terminar sin producir ninguna modificación física.

Ejemplos:

```text
Equivalent → ACCEPT
Recommended absent → JUSTIFY
Optional not applicable → OMIT
Satisfied → PRESERVE
```

En estos casos existe una decisión de adopción aunque el filesystem permanezca exactamente igual.

Esto sugiere que el resultado conceptual de una adopción puede incluir:

```text
Changes
    +
Decisions
```

y no únicamente:

```text
Generated or modified files
```

Este Finding no determina todavía dónde ni cómo deberían registrarse dichas decisiones.

### 8.15 La adopción de repositorios existentes y la creación de repositorios nuevos son escenarios diferentes

El experimento estudia exclusivamente:

```text
Existing Repository Adoption
```

En este escenario existe un estado previo que debe analizarse y reconciliarse.

Un repositorio nuevo podría presentar un proceso diferente:

```text
New Repository
        ↓
Select Template
        ↓
Instantiate initial structure
```

La evidencia obtenida con Only Film no permite concluir que ambos escenarios deban utilizar exactamente el mismo mecanismo.

Por tanto, conviene distinguir conceptualmente:

```text
Repository Initialization
```

de:

```text
Existing Repository Adoption
```

aunque en el futuro puedan compartir Components, Templates o herramientas.

### 8.16 El consumer puede revelar problemas del Template

`TPL-BACKEND` tiene estado `Experimental`.

Por tanto, una dificultad encontrada durante la adopción no debe atribuirse automáticamente al consumer.

El proceso también puede revelar:

- responsabilidades ambiguas;
- niveles de requisito discutibles;
- solapamientos entre Components;
- criterios de equivalencia insuficientes;
- problemas de aplicabilidad;
- expectativas difíciles de evaluar.

Esto convierte la adopción externa en una fuente de validación del propio Template.

La relación es bidireccional:

```text
Template evaluates Consumer
          +
Consumer tests Template
```

### 8.17 La adopción externa aporta evidencia diferente del dogfooding

El dogfooding anterior permitió comprobar el Framework utilizando su propio repositorio como consumer.

Only Film introduce condiciones diferentes:

```text
Repository created independently
        +
Existing conventions
        +
Existing documentation
        +
Existing automation
        +
Inherited content
```

Estas condiciones hacen visibles problemas que un repositorio construido junto con el Framework puede no revelar.

Por tanto, ambos tipos de evidencia son complementarios:

```text
Dogfooding
    +
External consumer adoption
        ↓
Stronger framework validation
```

### 8.18 Finding principal

El experimento permite formular provisionalmente el siguiente Finding principal:

> La adopción de GitHub Framework sobre un repositorio existente no es principalmente un proceso de generación de artefactos, sino un proceso de análisis y reconciliación entre responsabilidades declaradas por un Template y responsabilidades ya presentes, parciales, equivalentes, ausentes o no aplicables en el consumer.

El proceso observado puede representarse como:

```text
Existing Repository
        +
Repository Template
        ↓
Analyze
        ↓
Classify responsibilities
        ↓
Evaluate context
        ↓
Decide adoption actions
        ↓
Preserve / Adapt / Add / Accept / Omit
```

Este Finding describe el problema observado.

Todavía no determina qué mecanismo debe proporcionar GitHub Framework para resolverlo.

---

## 9. Modelo de adopción emergente

El análisis de Only Film muestra que la adopción de un Repository Template sobre un repositorio existente produce diferentes tipos de decisión.

Estas decisiones no deben confundirse con el estado observado de una responsabilidad.

El experimento distingue provisionalmente dos dimensiones:

```text
Responsibility State
        ↓
What exists?

Adoption Action
        ↓
What should be done?
```

Por ejemplo:

```text
Partial
```

describe el estado de una responsabilidad, mientras que:

```text
ADAPT
```

representa una posible acción de adopción.

La relación entre ambas dimensiones depende también del nivel de requisito y del contexto del consumer.

Por tanto, las siguientes operaciones representan un modelo emergente y no una correspondencia normativa definitiva.

### 9.1 Preserve

`PRESERVE` representa la decisión de conservar una implementación existente cuando ya satisface adecuadamente la responsabilidad evaluada.

Patrón observado:

```text
Responsibility
        ↓
Existing implementation
        ↓
Satisfied
        ↓
PRESERVE
```

Ejemplos encontrados en Only Film incluyen:

```text
README-HERO
README-OVERVIEW
README-FEATURES
README-TECH-STACK
README-FOOTER
README-ARCHITECTURE
README-REPOSITORY-STRUCTURE
README-TESTING
```

En estos casos, adoptar el Framework no requiere necesariamente introducir un nuevo artefacto.

La implementación existente ya aporta valor y puede conservarse.

`PRESERVE` evita un comportamiento de adopción basado en:

```text
Framework has canonical implementation
        ↓
Replace consumer implementation
```

cuando la responsabilidad ya está correctamente satisfecha.

La operación puede representarse como:

```text
Existing valid content
        +
Framework responsibility
        ↓
No replacement required
```

Por tanto, la ausencia de cambios físicos puede constituir un resultado válido del proceso de adopción.

### 9.2 Adapt

`ADAPT` representa la decisión de modificar una implementación existente cuando la responsabilidad está presente pero no completamente satisfecha.

Patrón observado:

```text
Responsibility
        ↓
Existing implementation
        ↓
Partial
        ↓
ADAPT
```

El ejemplo más claro del experimento es:

```text
README-QUICK-START
```

Only Film ya contiene instrucciones de instalación y ejecución, pero conserva referencias heredadas del repositorio original.

La situación no requiere necesariamente:

```text
Delete existing Quick Start
        ↓
Generate new Quick Start
```

sino:

```text
Preserve useful structure
        +
Correct consumer-specific content
```

`ADAPT` reconoce que una implementación parcialmente válida contiene información que puede conservarse.

Esta operación también evita reducir los estados de adopción a:

```text
Present
Missing
```

porque introduce una situación intermedia:

```text
Present but requires change
```

El alcance concreto de una adaptación puede variar.

Puede afectar a:

- referencias;
- nombres;
- enlaces;
- comandos;
- contenido incompleto;
- navegación;
- información específica del consumer.

El discovery no establece todavía reglas generales para determinar automáticamente qué modificaciones deben realizarse.

### 9.3 Add

`ADD` representa la incorporación de una responsabilidad que no dispone de una implementación identificada y cuya presencia resulta necesaria según el Template y el contexto del consumer.

Patrón principal:

```text
Required responsibility
        +
Missing implementation
        ↓
ADD
```

El ejemplo observado es:

```text
DOC-CHANGELOG
```

`TPL-BACKEND` lo declara Required y Only Film no dispone actualmente de un `CHANGELOG.md` ni se ha identificado otro artefacto que desempeñe claramente esa responsabilidad.

Por tanto, la adopción produciría conceptualmente:

```text
Missing Required
        ↓
ADD
```

Sin embargo, `ADD` describe una acción conceptual.

No determina todavía:

- qué archivo debe crearse;
- si debe utilizarse una implementación canónica;
- si debe partirse de un Component;
- si debe generarse automáticamente;
- si debe realizarse manualmente;
- qué contenido inicial debe incluir.

Esas cuestiones pertenecen a fases posteriores de diseño o implementación.

Además:

```text
Missing
        ≠
Always ADD
```

La necesidad de añadir depende también del requirement level y de la aplicabilidad.

### 9.4 Accept

`ACCEPT` representa la decisión de reconocer como válida una implementación existente que satisface una responsabilidad mediante una forma diferente de la representación canónica del Framework.

Patrón observado:

```text
Responsibility
        ↓
Existing non-canonical implementation
        ↓
Equivalent
        ↓
ACCEPT
```

Ejemplos encontrados durante el experimento incluyen casos como:

```text
README-ROADMAP
README-DEMO
README-AUTHOR
```

Only Film no necesita necesariamente reorganizar estas responsabilidades para reproducir literalmente la estructura propuesta por los Components.

La operación reconoce:

```text
Different representation
        ≠
Incorrect implementation
```

`ACCEPT` resulta especialmente relevante para repositorios existentes, porque estos pueden haber desarrollado convenciones válidas antes de adoptar GitHub Framework.

También puede aplicarse a responsabilidades:

```text
specialized
```

o:

```text
distributed
```

si la evidencia disponible demuestra suficientemente que la responsabilidad está cubierta.

La dificultad principal de esta operación es que determinar equivalencia suele requerir más interpretación semántica que comprobar la existencia de un archivo.

### 9.5 Evaluate / Justify / Omit

No todas las responsabilidades ausentes deben terminar en `ADD`.

Los niveles Recommended y Optional introducen decisiones adicionales.

El patrón observado puede representarse como:

```text
Responsibility absent
        ↓
Evaluate applicability
        ↓
Is it necessary for this consumer?
```

A partir de esa evaluación pueden aparecer diferentes acciones.

#### Evaluate

`EVALUATE` representa la necesidad de determinar si una responsabilidad resulta relevante para el consumer antes de decidir una acción.

Ejemplo:

```text
DOC-PROJECT-STATUS
```

Su ausencia puede detectarse, pero su nivel Recommended obliga a considerar si un documento específico de estado aporta valor real al contexto actual del proyecto.

Por tanto:

```text
Missing Recommended
        ↓
EVALUATE
```

no necesariamente:

```text
Missing Recommended
        ↓
ADD
```

#### Justify

`JUSTIFY` representa una decisión consciente de no implementar una responsabilidad cuando su nivel o contexto permite omisión, pero resulta útil conservar la razón de esa decisión.

Conceptualmente:

```text
Responsibility considered
        +
Not implemented
        +
Reason established
        ↓
JUSTIFY
```

El experimento no determina todavía dónde debería registrarse dicha justificación.

Puede tratarse únicamente de una decisión durante el proceso de adopción o, en una evolución futura, de información persistente.

#### Omit

`OMIT` representa la decisión de no incorporar una responsabilidad cuando no resulta necesaria o aplicable al consumer.

Ejemplos potenciales encontrados entre los Optional Components incluyen:

```text
DOC-ADR
DOC-DIAGRAMS
DOC-REFERENCES
```

cuando no existe una necesidad demostrada.

También aparece el caso:

```text
DOC-API
```

cuya responsabilidad no resulta actualmente aplicable al no existir la interfaz pública correspondiente.

El patrón es:

```text
Optional responsibility
        ↓
Not applicable / no demonstrated need
        ↓
OMIT
```

La omisión no representa un fallo de adopción.

Puede constituir una decisión correcta.

### 9.6 Relación entre estados y acciones

El experimento permite construir la siguiente matriz provisional:

| Estado observado | Requirement level | Acción potencial |
|---|---|---|
| `Satisfied` | Any | `PRESERVE` |
| `Partial` | Any | `ADAPT` |
| `Equivalent` | Any | `ACCEPT` |
| `Missing` | Required | `ADD` |
| `Missing` | Recommended | `EVALUATE` → `ADD` / `JUSTIFY` |
| `Missing` | Optional | `EVALUATE` → `ADD` / `OMIT` |
| `Not applicable` | Recommended / Optional | `OMIT` |
| `Omissible` | Recommended | `JUSTIFY` / `OMIT` |

Esta matriz no constituye todavía una regla normativa.

En particular, el experimento se basa en un único consumer y no demuestra que todas las combinaciones posibles estén correctamente representadas.

Su función es hacer explícito el comportamiento observado y proporcionar una base para futuras validaciones.

### 9.7 Flujo conceptual emergente

Combinando los resultados anteriores, el proceso observado puede expresarse provisionalmente como:

```text
Existing Repository
        │
        ▼
Select Repository Template
        │
        ▼
Analyze Consumer
        │
        ▼
Evaluate each responsibility
        │
        ├── Satisfied ───────────────► PRESERVE
        │
        ├── Partial ─────────────────► ADAPT
        │
        ├── Equivalent ──────────────► ACCEPT
        │
        └── Missing
              │
              ▼
       Evaluate requirement level
              │
       ┌──────┼──────────┐
       │      │          │
   Required Recommended Optional
       │      │          │
       ▼      ▼          ▼
      ADD   EVALUATE   EVALUATE
              │          │
          ADD /       ADD /
          JUSTIFY     OMIT
```

El flujo muestra que:

```text
Analyze
```

precede a:

```text
Change
```

y que el resultado del análisis puede ser tanto una modificación como una decisión de conservar, aceptar u omitir.

### 9.8 Resultado conceptual de una adopción

A partir del experimento, una adopción puede conceptualizarse provisionalmente como un conjunto de:

```text
Adoption Result
    │
    ├── Changes
    │     ├── ADD
    │     └── ADAPT
    │
    └── Decisions
          ├── PRESERVE
          ├── ACCEPT
          ├── JUSTIFY
          └── OMIT
```

Esto amplía el modelo simplificado:

```text
Adoption Result = Generated Files
```

hacia:

```text
Adoption Result
    =
Repository Changes
    +
Explicit Adoption Decisions
```

El discovery todavía no establece si estas decisiones necesitan persistirse, en qué formato deberían representarse o qué mecanismo debería gestionarlas.

### 9.9 Límites del modelo emergente

El modelo anterior se deriva de un único experimento:

```text
Consumer: Only Film
Template: TPL-BACKEND
Mode: Existing Repository
```

Por tanto, todavía no se ha demostrado:

- que los estados identificados sean exhaustivos;
- que las acciones sean suficientes para todos los consumers;
- que cada estado produzca siempre la misma acción;
- que `Not applicable` deba formalizarse como estado;
- que `Omissible` sea un estado o una propiedad derivada;
- que las decisiones deban persistirse;
- que el proceso deba implementarse mediante software;
- que el mismo modelo sea adecuado para repositorios nuevos;
- que el modelo sea aplicable sin cambios a otros Repository Templates.

Estas cuestiones deberán validarse con evidencia adicional antes de convertir el modelo en un Standard o contrato formal del Framework.

### 9.10 Modelo provisional

Con las limitaciones anteriores, el discovery produce el siguiente modelo provisional para adopción de repositorios existentes:

```text
Repository Template
        +
Existing Consumer
        ↓
ANALYZE
        ↓
Responsibility State
        +
Requirement Level
        +
Consumer Context
        ↓
DECIDE
        ↓
┌──────────┬──────────┬────────┬────────┬─────────┐
│ PRESERVE │  ADAPT   │  ADD   │ ACCEPT │  OMIT   │
└──────────┴──────────┴────────┴────────┴─────────┘
        ↓
Adoption Result
```

`EVALUATE` y `JUSTIFY` actúan como operaciones de decisión dentro del proceso y no necesariamente como modificaciones del consumer.

Este modelo constituye un resultado del discovery.

No constituye todavía la especificación de un mecanismo de adopción de GitHub Framework.

---

## 10. Límites de automatización

El experimento permite identificar partes del proceso de adopción que presentan distinto grado de automatización potencial.

Esta sección no propone todavía una herramienta concreta.

Su propósito es distinguir entre:

```text
Evidence that can be detected mechanically
```

y:

```text
Decisions that require semantic or contextual evaluation
```

Esta separación resulta necesaria antes de considerar cualquier mecanismo de automatización.

### 10.1 Evidencia determinista

Parte de la información utilizada durante la evaluación de Only Film puede obtenerse mediante reglas objetivas sobre el repositorio.

Ejemplos observados:

```text
README.md exists
CHANGELOG.md does not exist
docs/ exists
.github/workflows/ exists
```

También pueden identificarse estructuralmente determinados elementos como:

- archivos;
- directorios;
- workflows;
- metadata;
- determinados encabezados o secciones;
- referencias o patrones concretos;
- relaciones declaradas por el Repository Template.

Para este tipo de evidencia, el resultado puede expresarse mediante una comprobación reproducible:

```text
Repository
    ↓
Deterministic rule
    ↓
Observable fact
```

Por ejemplo:

```text
Does CHANGELOG.md exist?
        ↓
false
```

Este tipo de análisis presenta características compatibles con automatización:

- resultado reproducible;
- regla explícita;
- baja ambigüedad;
- ausencia de juicio contextual significativo.

Sin embargo, incluso cuando la evidencia es determinista, la decisión de adopción derivada puede no serlo.

Por ejemplo:

```text
File absent
```

no implica universalmente:

```text
ADD file
```

La acción depende de la responsabilidad, su requirement level y el contexto del consumer.

Por tanto:

```text
Deterministic evidence
        ≠
Deterministic adoption action
```

### 10.2 Evidencia semántica

Otra parte de la evaluación requiere comprender el significado del contenido existente.

El caso de `README-QUICK-START` lo demuestra claramente.

Puede detectarse que existe una sección de Quick Start.

Sin embargo, determinar que:

```text
https://github.com/certidevs/g1_testing.git
```

no corresponde al consumer actual requiere relacionar:

```text
Repository identity
        +
README content
        +
Consumer context
```

De forma similar, preguntas como:

```text
Does existing documentation satisfy DOC-ARCHITECTURE?

Is the testing responsibility sufficiently documented?

Is this implementation equivalent to a Framework Component?

Is a Recommended responsibility necessary for this consumer?

Is an omission justified?
```

no pueden resolverse únicamente mediante la existencia de archivos.

El proceso es más próximo a:

```text
Repository evidence
        +
Component responsibility
        +
Template requirement level
        +
Consumer context
        ↓
Semantic evaluation
```

La evaluación semántica puede producir resultados como:

```text
Partial
Equivalent
Omissible
Not applicable
```

que requieren más contexto que una comprobación binaria.

### 10.3 Diferentes niveles de automatización potencial

El experimento permite distinguir provisionalmente varios niveles.

#### Nivel 1 — Detección estructural

Ejemplos:

```text
Does README.md exist?
Does CHANGELOG.md exist?
Does docs/ exist?
Are workflows present?
```

Este nivel presenta alta capacidad de automatización.

#### Nivel 2 — Detección de contenido

Ejemplos:

```text
Does README contain a Quick Start section?
Does README contain testing information?
Does a document reference deployment?
```

Parte de estas comprobaciones puede realizarse mecánicamente.

Sin embargo, encontrar contenido relacionado no demuestra necesariamente que la responsabilidad esté correctamente satisfecha.

#### Nivel 3 — Validación contextual

Ejemplos:

```text
Does Quick Start describe this repository correctly?

Are existing architecture docs sufficient?

Does this content represent an equivalent implementation?
```

Aquí aumenta la necesidad de interpretación.

#### Nivel 4 — Decisión de adopción

Ejemplos:

```text
Should this implementation be preserved?

Should it be adapted?

Should a Recommended responsibility be added?

Is omission justified?
```

Estas decisiones combinan:

```text
evidence
+
requirement level
+
consumer context
+
adoption intent
```

y presentan un grado mayor de juicio.

La clasificación anterior es provisional y no constituye todavía un modelo formal del Framework.

### 10.4 Detección y decisión son responsabilidades diferentes

Una automatización puede detectar:

```text
CHANGELOG.md missing
```

sin necesidad de decidir inmediatamente:

```text
Create CHANGELOG.md
```

De forma similar puede detectar:

```text
Quick Start section found
```

sin afirmar:

```text
README-QUICK-START satisfied
```

Esto permite separar conceptualmente:

```text
Detection
    ↓
Evidence
```

de:

```text
Evaluation
    ↓
Adoption decision
```

La separación es relevante porque permite automatizar tareas de bajo riesgo sin atribuir a la automatización decisiones que la evidencia disponible no permite resolver de forma determinista.

### 10.5 La automatización puede asistir sin decidir

Entre los extremos:

```text
Fully manual
```

y:

```text
Fully automatic
```

existe un espacio intermedio.

Un proceso asistido podría, conceptualmente:

```text
detect evidence
        ↓
present findings
        ↓
request or support evaluation
        ↓
record decision
```

sin realizar automáticamente modificaciones sobre el consumer.

El experimento no determina todavía que este modelo deba implementarse.

Sí demuestra que la separación entre detección y decisión permite representar mejor los casos encontrados que un proceso puramente generativo.

### 10.6 Las acciones presentan diferentes niveles de riesgo

Las operaciones emergentes tampoco tienen el mismo impacto.

Conceptualmente:

```text
PRESERVE
ACCEPT
JUSTIFY
OMIT
```

pueden no requerir modificaciones físicas.

Mientras:

```text
ADAPT
ADD
```

sí pueden producir cambios sobre el consumer.

Además, `ADAPT` presenta un riesgo particular porque actúa sobre contenido existente.

Una modificación incorrecta puede:

- eliminar información útil;
- cambiar intención;
- romper instrucciones;
- sustituir convenciones propias;
- introducir duplicación;
- reducir información específica del proyecto.

Por tanto, detectar que una responsabilidad es `Partial` no proporciona automáticamente información suficiente para modificarla de forma segura.

### 10.7 Riesgo de automatización basada únicamente en archivos

Un mecanismo basado exclusivamente en filesystem podría interpretar:

```text
ARCHITECTURE.md absent
        ↓
DOC-ARCHITECTURE missing
        ↓
Create ARCHITECTURE.md
```

Sin embargo, Only Film proporciona evidencia arquitectónica distribuida.

El resultado podría ser:

```text
Existing architecture documentation
        +
Generated architecture document
        ↓
Duplication / fragmentation
```

De forma similar, un mecanismo basado únicamente en presencia podría interpretar:

```text
Quick Start exists
        ↓
README-QUICK-START satisfied
```

aunque las instrucciones correspondan a otro repositorio.

Por tanto, una automatización puramente estructural puede producir tanto:

```text
False Missing
```

como:

```text
False Satisfied
```

### 10.8 Riesgo de convertir el Template en una estructura física obligatoria

Los Repository Templates expresan una composición de responsabilidades.

Si la automatización asumiera:

```text
Template Component
        ↓
Mandatory canonical artifact
```

el modelo podría transformarse implícitamente en:

```text
Template
        =
Required filesystem layout
```

Esto entraría en tensión con la capacidad ya observada de satisfacer responsabilidades mediante implementaciones:

```text
own
specialized
equivalent
distributed
```

Por tanto, cualquier automatización futura deberá distinguir entre:

```text
Canonical implementation
```

y:

```text
Required implementation form
```

Ambos conceptos no son equivalentes.

### 10.9 Riesgo de maximizar cobertura

La automatización también podría introducir un incentivo incorrecto:

```text
More implemented Components
        =
Better adoption
```

El análisis de Optional Components contradice esa simplificación.

Añadir automáticamente:

```text
DOC-ADR
DOC-DIAGRAMS
DOC-REFERENCES
```

sin una necesidad demostrada aumentaría cobertura física, pero no necesariamente valor.

Por tanto, la automatización no debería convertir Optional Components en obligaciones implícitas.

La omisión puede ser un resultado válido.

### 10.10 Riesgo de ocultar incertidumbre

Algunas evaluaciones realizadas durante el discovery permanecen deliberadamente expresadas como:

```text
Partial / Equivalent
Missing / Omissible
```

Estas clasificaciones reflejan incertidumbre o necesidad de evaluación contextual.

Una automatización que obligara a producir inmediatamente un resultado binario:

```text
PASS
FAIL
```

eliminaría información relevante del proceso.

En determinados casos, una salida como:

```text
Needs evaluation
```

puede representar mejor la evidencia disponible que una decisión automática.

### 10.11 Riesgo de automatización prematura

Los estándares anteriores del Framework ya excluyeron automatizaciones complejas mientras los patrones todavía no estuvieran suficientemente validados.

El presente experimento refuerza esa precaución.

Solo se ha estudiado:

```text
1 Consumer
1 Template
1 Adoption Mode
```

Por tanto, todavía no existe evidencia suficiente para fijar de manera definitiva:

- un workflow universal de adopción;
- una taxonomía completa de estados;
- un formato persistente de decisiones;
- reglas generales de equivalencia;
- reglas automáticas de aplicabilidad;
- un mecanismo universal de modificación;
- una interfaz concreta de adopción.

Automatizar estas decisiones ahora podría convertir conclusiones provisionales en contratos difíciles de cambiar posteriormente.

### 10.12 Frontera provisional de automatización

A partir del experimento puede establecerse una frontera provisional:

```text
                    AUTOMATION CONFIDENCE

High
 │
 │  Repository structure detection
 │  File existence
 │  Directory existence
 │  Workflow existence
 │  Explicit metadata
 │
 │  Section / content detection
 │
 │  --------------------------------
 │
 │  Responsibility interpretation
 │  Equivalence evaluation
 │  Applicability evaluation
 │  Omission justification
 │  Consumer-specific adaptation
 │
Low
```

Esta frontera no implica que las tareas situadas en la parte inferior sean imposibles de asistir mediante software.

Indica únicamente que presentan mayor dependencia de contexto y, por tanto, mayor riesgo si se convierten prematuramente en decisiones automáticas.

### 10.13 Principio provisional

El experimento permite formular el siguiente principio provisional:

> Automatizar primero la obtención de evidencia no implica automatizar inmediatamente las decisiones de adopción.

Conceptualmente:

```text
Detect
    ↓
Evidence
    ↓
Evaluate
    ↓
Decision
    ↓
Apply
```

Las primeras etapas pueden presentar mayor determinismo que las últimas.

Una evolución futura podría automatizar una, varias o todas estas etapas, pero el discovery todavía no proporciona evidencia suficiente para decidirlo.

### 10.14 Resultado

El principal límite identificado no es estrictamente técnico.

Es epistemológico:

```text
What can the Framework know
from repository evidence?
```

frente a:

```text
What still requires
consumer-specific judgment?
```

Only Film demuestra que GitHub Framework puede obtener determinados hechos estructurales de forma objetiva, pero que la adopción completa también requiere interpretar responsabilidades, equivalencia, aplicabilidad y contexto.

Por tanto, cualquier futura automatización deberá preservar explícitamente la diferencia entre:

```text
Detected fact
Evaluated state
Adoption decision
Applied change
```

antes de convertir el proceso de adopción en comportamiento ejecutable.

---

## 11. Requirement Candidates

Los Findings obtenidos durante el experimento permiten formular necesidades potenciales para GitHub Framework.

Estas necesidades se registran como:

```text
Requirement Candidates
```

y no como requisitos aprobados.

Un Requirement Candidate expresa:

```text
What capability may be needed?
```

sin determinar:

```text
How should it be implemented?
```

La relación utilizada en esta sección es:

```text
Observation
    ↓
Finding
    ↓
Demonstrated need
    ↓
Requirement Candidate
```

Un candidato podrá posteriormente:

- validarse;
- refinarse;
- dividirse;
- combinarse con otros;
- descartarse;
- requerir evidencia adicional;
- convertirse en requisito formal.

No implica todavía:

- incorporación al backlog;
- prioridad;
- Sprint;
- milestone;
- versión;
- arquitectura seleccionada;
- implementación comprometida.

### 11.1 RC-01 — Analizar un consumer existente frente a un Repository Template

**Finding relacionado:** la adopción de un repositorio existente es un problema de reconciliación.

GitHub Framework dispone de Repository Templates que declaran responsabilidades, pero el experimento ha requerido realizar manualmente el contraste entre:

```text
Existing Consumer
        +
Repository Template
```

para determinar el estado de adopción.

Requirement Candidate:

> GitHub Framework debería proporcionar un proceso definido para analizar un repositorio existente frente a las responsabilidades declaradas por un Repository Template.

El proceso debería permitir obtener una visión del estado actual antes de aplicar modificaciones.

Este candidato no determina si el análisis debe realizarse mediante:

- documentación;
- checklist;
- tooling;
- CLI;
- validator;
- GitHub Action;
- otro mecanismo.

### 11.2 RC-02 — Distinguir el estado de cada responsabilidad

**Findings relacionados:** presencia y satisfacción no son equivalentes; el modelo binario presente/ausente resulta insuficiente.

El experimento ha necesitado diferenciar situaciones como:

```text
Satisfied
Partial
Equivalent
Missing
```

y considerar además aplicabilidad u omisión en determinados contextos.

Requirement Candidate:

> El proceso de adopción debería poder representar más de un estado para una responsabilidad y evitar reducir su evaluación a una clasificación binaria presente/ausente.

La taxonomía concreta todavía necesita validación adicional.

Por tanto, este candidato no formaliza todavía como estándar los estados utilizados durante el discovery.

### 11.3 RC-03 — Separar estado y acción de adopción

**Finding relacionado:** estado y acción representan conceptos diferentes.

El experimento ha distinguido:

```text
What exists?
```

de:

```text
What should be done?
```

Por ejemplo:

```text
Partial
```

es un estado, mientras:

```text
ADAPT
```

es una posible acción.

Requirement Candidate:

> El modelo de adopción debería representar separadamente el estado observado de una responsabilidad y la acción de adopción decidida para ella.

Esto evita que una detección se convierta automáticamente en una modificación.

### 11.4 RC-04 — Preservar implementaciones existentes válidas

**Finding relacionado:** la adopción necesita preservar implementaciones válidas.

Only Film satisface numerosas responsabilidades antes de adoptar formalmente el Framework.

Requirement Candidate:

> El proceso de adopción debería permitir conservar implementaciones existentes cuando ya satisfacen adecuadamente una responsabilidad del Template.

Conceptualmente:

```text
Satisfied
    ↓
PRESERVE
```

La adopción no debería exigir sustitución únicamente porque exista una implementación canónica del Component.

### 11.5 RC-05 — Adaptar contenido existente sin sustituirlo innecesariamente

**Finding relacionado:** adaptar es diferente de añadir.

`README-QUICK-START` demuestra que una responsabilidad puede estar presente y necesitar únicamente cambios específicos del consumer.

Requirement Candidate:

> El proceso de adopción debería distinguir responsabilidades parcialmente satisfechas de responsabilidades ausentes y permitir que las primeras se traten mediante adaptación en lugar de sustitución completa.

Este candidato no define cómo identificar ni ejecutar automáticamente una adaptación.

### 11.6 RC-06 — Reconocer implementaciones equivalentes, especializadas o distribuidas

**Finding relacionado:** la equivalencia es necesaria para adoptar repositorios heterogéneos.

El consumer puede satisfacer una responsabilidad sin utilizar la representación física canónica del Framework.

Requirement Candidate:

> El proceso de adopción debería permitir reconocer que una responsabilidad puede estar satisfecha mediante una implementación propia, equivalente, especializada o distribuida.

Por tanto:

```text
Canonical artifact absent
```

no debería implicar automáticamente:

```text
Responsibility missing
```

Los criterios generales para demostrar equivalencia todavía requieren validación adicional.

### 11.7 RC-07 — Considerar requirement level y aplicabilidad

**Findings relacionados:** la aplicabilidad forma parte de la adopción y el nivel de requisito modifica el significado de la ausencia.

Requirement Candidate:

> La evaluación de una responsabilidad debería considerar conjuntamente su estado, su requirement level y el contexto del consumer antes de determinar una acción de adopción.

Conceptualmente:

```text
Responsibility State
        +
Requirement Level
        +
Consumer Context
        ↓
Adoption Decision
```

Esto resulta especialmente relevante para Components Recommended y Optional.

### 11.8 RC-08 — Permitir omisiones justificadas

**Finding relacionado:** una adopción puede necesitar registrar decisiones y no únicamente cambios.

No implementar una responsabilidad puede constituir una decisión válida cuando:

- el nivel de requisito lo permite;
- la responsabilidad no resulta aplicable;
- no existe una necesidad demostrada.

Requirement Candidate:

> El proceso de adopción debería poder representar una omisión válida y, cuando resulte necesario, su justificación.

Este candidato no determina:

- si la justificación debe persistirse;
- dónde debería almacenarse;
- qué formato debería utilizar;
- cuándo debería ser obligatoria.

### 11.9 RC-09 — Mantener trazabilidad entre evidencia, evaluación y decisión

**Findings relacionados:** evidencia, estado y decisión son conceptos diferentes.

Durante el experimento se ha seguido conceptualmente:

```text
Evidence
    ↓
Evaluated State
    ↓
Adoption Decision
```

Requirement Candidate:

> El proceso de adopción debería permitir relacionar una evaluación con la evidencia del consumer que la sustenta y distinguir dicha evidencia de la decisión posterior.

Esto permitiría explicar, por ejemplo:

```text
Evidence:
Quick Start contains inherited repository URL

Evaluated State:
Partial

Decision:
ADAPT
```

sin tratar las tres informaciones como una única conclusión.

### 11.10 RC-10 — Separar análisis y aplicación de cambios

**Finding relacionado:** analizar precede a modificar.

El experimento completo se ha realizado sin modificar Only Film.

Requirement Candidate:

> GitHub Framework debería permitir evaluar el estado de adopción de un consumer antes de aplicar cambios sobre él.

Conceptualmente:

```text
ANALYZE
    ↓
DECIDE
    ↓
APPLY
```

en lugar de:

```text
ANALYZE + MODIFY
```

como una única operación inseparable.

Este candidato permite que el resultado del análisis pueda revisarse antes de modificar el repositorio.

### 11.11 RC-11 — Distinguir detección determinista de evaluación semántica

**Finding relacionado:** la adopción combina evidencia determinista y semántica.

Requirement Candidate:

> El proceso de adopción debería distinguir las comprobaciones que pueden resolverse mediante reglas deterministas de aquellas que requieren interpretación contextual o semántica.

Ejemplo:

```text
CHANGELOG.md exists?
```

puede ser determinista.

Mientras:

```text
Does existing documentation sufficiently
satisfy DOC-ARCHITECTURE?
```

puede requerir evaluación adicional.

Esta distinción evita presentar como certeza automática aquello que la evidencia disponible no permite determinar de forma objetiva.

### 11.12 RC-12 — Representar incertidumbre o necesidad de evaluación

**Finding relacionado:** algunas evaluaciones no admiten inmediatamente una respuesta binaria.

Durante el experimento han aparecido estados provisionales como:

```text
Partial / Equivalent
Missing / Omissible
```

Requirement Candidate:

> El proceso de adopción debería poder representar situaciones que necesitan evaluación adicional sin forzarlas prematuramente a un resultado definitivo.

Conceptualmente:

```text
Evidence insufficient for final decision
        ↓
Needs evaluation
```

puede ser un resultado válido.

La representación concreta de esta incertidumbre todavía no está definida.

### 11.13 RC-13 — Evitar modificaciones destructivas por defecto

**Findings relacionados:** preservar implementaciones válidas y distinguir análisis de aplicación.

Requirement Candidate:

> Cualquier proceso de adopción que pueda modificar un consumer debería evitar por defecto sobrescribir o eliminar contenido existente sin que la acción haya sido previamente determinada.

Este candidato se deriva especialmente del escenario `Existing Repository`, donde el consumer ya contiene documentación y automatización propias.

No establece todavía mecanismos concretos de protección, confirmación o rollback.

### 11.14 RC-14 — Mantener Initialization y Existing Repository Adoption como escenarios distinguibles

**Finding relacionado:** creación y adopción de repositorios existentes son escenarios diferentes.

Requirement Candidate:

> GitHub Framework debería distinguir conceptualmente la inicialización de un repositorio nuevo de la adopción del Framework sobre un repositorio existente.

Esto no implica que ambos procesos necesiten herramientas diferentes.

Pueden compartir:

- Standards;
- Components;
- Repository Templates;
- metadata;
- reglas;
- futuras capacidades.

Pero sus condiciones iniciales son diferentes:

```text
New Repository
        ↓
No significant existing implementation
```

frente a:

```text
Existing Repository
        ↓
Existing implementation requiring reconciliation
```

### 11.15 RC-15 — Utilizar adopción externa como mecanismo de validación de Templates

**Finding relacionado:** el consumer también evalúa el Template.

Requirement Candidate:

> La evolución de Repository Templates experimentales debería poder incorporar evidencia procedente de adopciones sobre consumers independientes del repositorio GitHub Framework.

Esto complementaría el dogfooding con escenarios donde existen:

- convenciones previas;
- documentación previa;
- automatización previa;
- implementaciones equivalentes;
- contenido heredado.

Este candidato afecta al proceso de madurez y validación del Framework más que al mecanismo operativo de adopción.

### 11.16 Agrupación provisional

Los candidatos anteriores pueden organizarse provisionalmente en cinco capacidades.

#### A. Analysis

```text
RC-01 Analyze existing consumer
RC-10 Separate analysis from apply
RC-11 Deterministic vs semantic evaluation
RC-12 Represent uncertainty
```

#### B. Responsibility Model

```text
RC-02 Responsibility states
RC-03 State vs action
RC-06 Equivalent implementations
RC-07 Requirement level + applicability
```

#### C. Adoption Decisions

```text
RC-04 Preserve
RC-05 Adapt
RC-08 Justified omission
RC-09 Evidence → evaluation → decision traceability
```

#### D. Safe Application

```text
RC-13 Non-destructive modification
RC-14 Initialization vs existing adoption
```

#### E. Framework Validation

```text
RC-15 External adoption evidence
```

Esta agrupación no representa todavía arquitectura ni backlog.

Su propósito es identificar afinidades entre necesidades descubiertas.

### 11.17 Dependencias conceptuales

Los Requirement Candidates tampoco son completamente independientes.

El experimento sugiere una secuencia conceptual:

```text
Responsibility Model
        ↓
Analysis
        ↓
Adoption Decisions
        ↓
Safe Application
```

Mientras:

```text
External Adoption Evidence
```

retroalimenta la evolución del conjunto.

Representado de forma completa:

```text
              External Consumers
                     │
                     ▼
           Responsibility Model
                     │
                     ▼
                  Analyze
                     │
                     ▼
             Adoption Decisions
                     │
                     ▼
              Safe Application
                     │
                     ▼
               Adopted Consumer
                     │
                     └──────────────┐
                                    ▼
                           Framework Evidence
```

Esta dependencia es relevante porque automatizar `Safe Application` antes de estabilizar suficientemente `Analysis` y `Responsibility Model` podría formalizar decisiones todavía inmaduras.

### 11.18 Candidatos con evidencia más directa

No todos los Requirement Candidates presentan actualmente el mismo grado de evidencia.

El experimento proporciona evidencia especialmente directa para:

```text
RC-01 Analyze existing consumer
RC-02 Represent responsibility state
RC-04 Preserve valid implementations
RC-05 Adapt partial implementations
RC-06 Accept equivalent implementations
RC-07 Consider requirement level and context
RC-10 Separate analysis from changes
RC-11 Separate deterministic and semantic evaluation
```

Otros candidatos, como persistencia de justificaciones, representación de incertidumbre o mecanismos de aplicación segura, necesitan mayor refinamiento o evidencia adicional antes de convertirse en contratos formales.

Por tanto, esta lista no debe interpretarse como:

```text
15 future features
```

sino como:

```text
15 candidate requirements
        ↓
to validate / consolidate / reject
```

### 11.19 Resultado

El discovery ya permite expresar la limitación inicial de GitHub Framework de forma más concreta.

El Framework dispone de:

```text
Standards
Components
Repository Templates
Reference Implementations
Component metadata
Framework validation
```

pero el experimento identifica como espacio todavía no operacionalizado:

```text
Existing Consumer
        +
Repository Template
        ↓
Structured Adoption Process
```

Ese proceso potencial necesitaría comprender:

```text
Analyze
Evaluate
Decide
Apply
```

sin asumir todavía qué herramienta o arquitectura debe proporcionarlo.

Los Requirement Candidates documentados en esta sección constituyen la primera formulación estructurada de ese espacio de necesidad.

---

## 12. Solution Hypotheses

Los Requirement Candidates describen capacidades potencialmente necesarias para operacionalizar la adopción de GitHub Framework sobre repositorios existentes.

Esta sección explora posibles respuestas a esas necesidades.

Cada propuesta se registra como:

```text
Solution Hypothesis
```

y no como:

```text
Selected Solution
```

Una Solution Hypothesis puede:

- cubrir uno o varios Requirement Candidates;
- combinarse con otras hipótesis;
- requerir experimentación;
- resultar innecesaria;
- descartarse;
- posponerse hasta disponer de mayor evidencia.

La relación utilizada es:

```text
Finding
    ↓
Requirement Candidate
    ↓
Solution Hypothesis
```

y no:

```text
Finding
    ↓
Implementation
```

Por tanto, ninguna de las alternativas siguientes constituye todavía alcance de una release.

### 12.1 SH-01 — Manual Adoption Guide

Una primera hipótesis consiste en documentar explícitamente el proceso de adopción sin introducir nueva automatización.

Conceptualmente:

```text
Existing Repository
        +
Repository Template
        ↓
Manual Adoption Guide
        ↓
Analyze
Evaluate
Decide
Apply
```

La guía podría explicar cómo:

- seleccionar un Repository Template;
- recorrer sus responsabilidades;
- localizar evidencia en el consumer;
- distinguir `Satisfied`, `Partial`, `Equivalent` y `Missing`;
- considerar requirement level y aplicabilidad;
- decidir entre `PRESERVE`, `ADAPT`, `ADD`, `ACCEPT` y `OMIT`;
- documentar incertidumbre o justificaciones;
- revisar los cambios antes de aplicarlos.

#### Requirement Candidates relacionados

Principalmente:

```text
RC-01
RC-02
RC-03
RC-04
RC-05
RC-06
RC-07
RC-08
RC-09
RC-10
RC-11
RC-12
RC-14
```

#### Ventajas potenciales

```text
Low implementation cost
Low technical risk
Makes the process explicit
Allows further experimentation
Does not prematurely encode semantic decisions
```

También permitiría probar el modelo con más consumers antes de convertirlo en comportamiento ejecutable.

#### Limitaciones

El análisis continuaría siendo mayoritariamente manual.

Tareas repetitivas como comprobar estructura, localizar archivos o identificar determinados patrones no se beneficiarían de automatización.

La consistencia del resultado dependería en mayor medida de la persona que realice la adopción.

---

### 12.2 SH-02 — Adoption Checklist / Assessment

Una segunda hipótesis consiste en proporcionar una representación estructurada de la evaluación.

Podría adoptar conceptualmente la forma:

```text
Template Responsibility
        ↓
Evidence
        ↓
State
        ↓
Decision
        ↓
Notes / Justification
```

Por ejemplo:

```text
Component: README-QUICK-START
Evidence: README contains inherited clone URL
State: Partial
Decision: ADAPT
Notes: personalize repository URL and directory
```

El objetivo sería hacer reproducible el análisis sin determinar todavía que deba existir una herramienta ejecutable.

#### Requirement Candidates relacionados

Especialmente:

```text
RC-02
RC-03
RC-07
RC-08
RC-09
RC-12
```

#### Ventajas potenciales

Permitiría separar explícitamente:

```text
Evidence
Evaluated State
Adoption Decision
```

También facilitaría comparar resultados entre diferentes consumers y detectar patrones repetidos.

#### Limitaciones

Una checklist no elimina el juicio semántico.

Además, si su estructura se formaliza demasiado pronto, podría estabilizar una taxonomía de estados y decisiones que todavía necesita más evidencia.

---

### 12.3 SH-03 — Assisted Repository Analyzer

Otra hipótesis consiste en automatizar únicamente las partes deterministas del análisis.

Conceptualmente:

```text
Repository
    ↓
Analyzer
    ↓
Detected Evidence
```

El resultado podría incluir hechos como:

```text
README.md ............... found
CHANGELOG.md ............ not found
docs/ ................... found
.github/workflows/ ...... found
Quick Start section ..... detected
Testing section ......... detected
```

sin concluir automáticamente:

```text
README-QUICK-START = Satisfied
DOC-ARCHITECTURE = Missing
```

#### Requirement Candidates relacionados

Principalmente:

```text
RC-01
RC-09
RC-10
RC-11
RC-12
```

#### Ventajas potenciales

Automatizaría trabajo repetitivo de bajo riesgo.

Mantendría separadas:

```text
Detection
```

y:

```text
Evaluation
```

Además, permitiría reutilizar reglas deterministas en futuros mecanismos de adopción.

#### Limitaciones

No resolvería por sí mismo:

- equivalencia;
- aplicabilidad;
- suficiencia documental;
- justificación de omisiones;
- adaptación semántica.

Por tanto, seguiría siendo necesario un nivel posterior de evaluación.

---

### 12.4 SH-04 — Adoption Report

Una hipótesis complementaria consiste en producir un informe estructurado del análisis.

Conceptualmente:

```text
Repository + Template
        ↓
Assessment
        ↓
Adoption Report
```

El informe podría representar:

```text
Required
Recommended
Optional

Evidence
State
Decision
Uncertainty
Notes
```

y proporcionar una fotografía del consumer antes de aplicar cambios.

#### Requirement Candidates relacionados

Especialmente:

```text
RC-02
RC-03
RC-08
RC-09
RC-10
RC-12
RC-15
```

#### Ventajas potenciales

Crearía un artefacto revisable.

También podría proporcionar evidencia para:

- adopción;
- revisión;
- evolución de Templates;
- nuevos experimentos;
- comparación entre consumers.

#### Limitaciones

El experimento actual no demuestra todavía:

- si el informe debería persistirse;
- si debería versionarse;
- cuál debería ser su formato;
- si pertenece al consumer o al proceso de evaluación;
- si debe ser legible por humanos, máquinas o ambos.

---

### 12.5 SH-05 — Adoption Manifest

Otra hipótesis sería persistir determinadas decisiones de adopción en un artefacto estructurado.

Conceptualmente:

```text
Repository
    +
Template
    +
Adoption Decisions
        ↓
Adoption Manifest
```

Podría llegar a representar información como:

```text
Template identity
Template version
Responsibility
Evidence
State
Decision
Justification
```

#### Requirement Candidates relacionados

Potencialmente:

```text
RC-03
RC-06
RC-07
RC-08
RC-09
RC-12
```

#### Ventajas potenciales

Permitirá, si fuera necesario, conservar decisiones como:

```text
Equivalent → ACCEPT
Recommended → JUSTIFY
Optional → OMIT
```

incluso cuando no produzcan cambios físicos.

También podría facilitar reevaluaciones futuras frente a nuevas versiones de un Template.

#### Limitaciones

Actualmente no existe evidencia suficiente para demostrar que estas decisiones necesiten persistencia permanente.

Introducir un manifest demasiado pronto podría:

- formalizar una taxonomía inmadura;
- añadir mantenimiento;
- duplicar información;
- crear problemas de versionado;
- anticipar necesidades todavía no demostradas.

Por tanto, esta hipótesis requiere evidencia adicional antes de considerarse una solución candidata madura.

---

### 12.6 SH-06 — Framework Validator Extension

El Framework Validator existente podría hipotéticamente ampliarse para participar en determinados aspectos de adopción.

Sin embargo, su responsabilidad actual se centra en validaciones deterministas del propio Framework.

Una posible evolución limitada podría consistir en:

```text
Framework Validator
        +
Consumer inspection
        ↓
Deterministic findings
```

#### Requirement Candidates relacionados

Potencialmente:

```text
RC-01
RC-10
RC-11
```

#### Ventajas potenciales

Podría reutilizar:

- infraestructura existente;
- convenciones;
- reglas deterministas;
- mecanismos de reporting;
- testing.

#### Riesgos y limitaciones

Existe un riesgo significativo de ampliar conceptualmente el validator desde:

```text
Validate deterministic Framework rules
```

hacia:

```text
Judge semantic consumer conformance
```

sin disponer todavía de reglas suficientes para hacerlo correctamente.

Esto podría producir:

```text
False Satisfied
False Missing
False Failure
```

Por tanto, cualquier posible extensión debería preservar claramente la frontera entre:

```text
deterministic validation
```

y:

```text
semantic adoption evaluation
```

El discovery actual no demuestra que ampliar el validator sea preferible a introducir una capacidad separada.

---

### 12.7 SH-07 — Adoption CLI

Una CLI podría proporcionar una interfaz para coordinar diferentes etapas del proceso.

Conceptualmente:

```text
CLI
 ├── analyze
 ├── review
 └── apply
```

Esta representación es únicamente ilustrativa y no constituye un diseño de comandos.

#### Requirement Candidates relacionados

Potencialmente podría coordinar gran parte de:

```text
RC-01 → RC-14
```

dependiendo de su alcance.

#### Ventajas potenciales

Una CLI podría:

- proporcionar un punto de entrada coherente;
- ejecutar análisis determinista;
- presentar resultados;
- recoger decisiones;
- aplicar cambios seleccionados;
- generar informes.

#### Limitaciones

Una CLI es principalmente una interfaz.

No resuelve por sí misma los problemas conceptuales de:

- estados;
- equivalencia;
- aplicabilidad;
- incertidumbre;
- reglas de adaptación;
- persistencia de decisiones.

Implementarla antes de estabilizar suficientemente esos conceptos podría producir una interfaz alrededor de un modelo todavía inmaduro.

Por tanto:

```text
Need for adoption process
        ≠
Demonstrated need for CLI
```

---

### 12.8 SH-08 — Selective Component Application

Otra hipótesis consiste en permitir aplicar únicamente Components concretos después del análisis.

Conceptualmente:

```text
Analysis Result
        ↓
Missing Required
        ↓
Select Component
        ↓
Apply canonical starting point
```

Por ejemplo, una responsabilidad realmente ausente podría utilizar su Component como base inicial.

#### Requirement Candidates relacionados

Especialmente:

```text
RC-05
RC-13
```

y parcialmente:

```text
RC-04
RC-10
```

#### Ventajas potenciales

Evitaría generar un Template completo sobre un repositorio que ya satisface gran parte de sus responsabilidades.

El proceso sería selectivo:

```text
Only add what is needed
```

en lugar de:

```text
Generate everything
```

#### Limitaciones

Todavía sería necesario resolver:

- personalización;
- conflictos;
- destino físico;
- merge con contenido existente;
- placeholders;
- revisión previa;
- rollback.

Además, solo aborda la fase `APPLY`, no el análisis que determina qué debe aplicarse.

---

### 12.9 SH-09 — Repository Generator

El Icebox ya contempla conceptualmente un repository generator.

El discovery permite ahora situar esa hipótesis con mayor precisión.

Un generator encaja especialmente bien en:

```text
New Repository Initialization
```

donde el estado inicial puede aproximarse a:

```text
No existing repository structure
        ↓
Instantiate Template
```

También podría resultar útil para determinadas acciones `ADD` sobre consumers existentes.

#### Requirement Candidates relacionados

Principalmente:

```text
RC-13
RC-14
```

y parcialmente algunas acciones derivadas de responsabilidades `Missing`.

#### Ventajas potenciales

Podría reducir trabajo repetitivo en creación de repositorios nuevos y proporcionar implementaciones canónicas como punto de partida.

#### Limitaciones frente al experimento

Por sí solo no resuelve:

```text
RC-01 Analyze consumer
RC-04 Preserve
RC-05 Adapt
RC-06 Equivalent implementations
RC-07 Applicability
RC-09 Traceability
RC-11 Semantic boundary
```

Por tanto, el experimento no respalda:

```text
Repository Generator
        =
Existing Repository Adoption
```

El generator continúa siendo una hipótesis válida, pero parece responder principalmente a un escenario diferente o a una fase posterior del proceso.

---

### 12.10 SH-10 — GitHub Actions Integration

Otra hipótesis existente en el Icebox consiste en integrar capacidades del Framework mediante GitHub Actions.

Una Action podría ejecutar, por ejemplo:

```text
Repository analysis
```

o:

```text
Framework validation
```

dentro del ciclo del repositorio.

#### Ventajas potenciales

Podría proporcionar:

- ejecución reproducible;
- integración con pull requests;
- reporting continuo;
- detección de determinados cambios.

#### Limitaciones frente al experimento

GitHub Actions constituye un mecanismo de ejecución, no el modelo de adopción.

Antes sería necesario determinar:

```text
What should be evaluated?
Which rules are deterministic?
What constitutes failure?
What requires human judgment?
```

El experimento tampoco demuestra todavía que el análisis de adopción necesite ejecutarse continuamente.

Por tanto, GitHub Actions Integration permanece como posible mecanismo futuro, no como solución derivada directamente del discovery.

---

### 12.11 SH-11 — Staged Adoption Process

Los Findings y Requirement Candidates permiten formular una hipótesis de nivel superior que no prescribe todavía una tecnología concreta.

El proceso podría dividirse conceptualmente en etapas:

```text
1. ANALYZE
        ↓
2. REVIEW
        ↓
3. DECIDE
        ↓
4. APPLY
        ↓
5. VERIFY
```

#### Analyze

Obtener evidencia del consumer frente al Template.

#### Review

Examinar resultados deterministas, semánticos e inciertos.

#### Decide

Seleccionar acciones como:

```text
PRESERVE
ADAPT
ADD
ACCEPT
JUSTIFY
OMIT
```

#### Apply

Ejecutar únicamente los cambios aprobados.

#### Verify

Comprobar el resultado después de la adopción.

Esta hipótesis podría combinar mecanismos manuales y automáticos en diferentes etapas.

Por ejemplo:

```text
ANALYZE → partially automated
REVIEW  → human-assisted
DECIDE  → explicit decision
APPLY   → manual or automated
VERIFY  → deterministic + semantic review
```

#### Requirement Candidates relacionados

Esta hipótesis proporciona una posible estructura para prácticamente todos los candidatos:

```text
RC-01 → RC-14
```

sin seleccionar todavía la tecnología utilizada en cada fase.

#### Limitaciones

El modelo necesita validación mediante más experimentos.

En particular, todavía no se ha demostrado:

- si las cinco etapas son necesarias;
- si `REVIEW` y `DECIDE` deben estar separadas;
- cómo funciona `VERIFY`;
- qué información necesita persistirse;
- qué partes deben automatizarse.

---

### 12.12 Comparación provisional de hipótesis

Las hipótesis responden a niveles diferentes del problema.

| Hipótesis | Analysis | Decision support | Apply | Persistence | Principal riesgo |
|---|---:|---:|---:|---:|---|
| Manual Adoption Guide | ✓ | ✓ | Manual | No | Baja repetibilidad |
| Adoption Checklist | ✓ | ✓ | No | Possible | Formalización prematura |
| Repository Analyzer | ✓ | Partial | No | No | Confundir detección con evaluación |
| Adoption Report | ✓ | ✓ | No | Yes | Contrato prematuro |
| Adoption Manifest | Partial | ✓ | No | Yes | Modelo inmaduro |
| Validator Extension | Partial | Limited | No | No | Expandir responsabilidad del validator |
| Adoption CLI | Possible | Possible | Possible | Possible | Interfaz antes que modelo |
| Selective Component Application | No | No | ✓ | No | Cambios sin análisis suficiente |
| Repository Generator | Limited | No | ✓ | No | Orientación excesiva a generación |
| GitHub Actions Integration | Possible | Limited | Possible | No | Automatizar reglas todavía inmaduras |
| Staged Adoption Process | ✓ | ✓ | ✓ | Undefined | Necesita más validación |

La tabla no representa una evaluación competitiva ni selecciona una opción.

Varias hipótesis pueden ser complementarias y operar en niveles diferentes.

### 12.13 Combinaciones posibles

Las hipótesis no son mutuamente excluyentes.

Por ejemplo, una evolución incremental podría conceptualmente combinar:

```text
Adoption Guide
        +
Assessment
        +
Deterministic Analyzer
```

sin introducir todavía:

```text
Automatic Apply
```

Otra evolución posterior podría añadir:

```text
Selective Component Application
```

una vez estabilizado el modelo de análisis.

De forma similar:

```text
CLI
GitHub Actions
```

podrían actuar en el futuro como interfaces o mecanismos de ejecución sobre capacidades definidas previamente.

La secuencia concreta no está decidida.

### 12.14 Hipótesis que requieren mayor precaución

El experimento proporciona menor respaldo directo para comenzar por:

```text
Repository Generator
Adoption Manifest
Full semantic validator
Automatic repository modification
```

No porque estas ideas sean necesariamente incorrectas, sino porque dependen de decisiones todavía no suficientemente validadas.

En particular:

```text
Generator
```

necesita saber qué debe generarse.

```text
Manifest
```

necesita saber qué información merece persistirse.

```text
Semantic Validator
```

necesita reglas suficientemente objetivas.

```text
Automatic Apply
```

necesita decisiones de adopción suficientemente fiables.

Por tanto, estas hipótesis dependen conceptualmente de conocimiento previo sobre el modelo de adopción.

### 12.15 Hipótesis con menor compromiso arquitectónico

Las alternativas con menor compromiso inicial son aquellas que permiten continuar aprendiendo sin fijar prematuramente una arquitectura.

Entre ellas:

```text
Manual Adoption Guide
Adoption Checklist / Assessment
Deterministic Repository Analyzer
Staged Adoption Process
```

Estas hipótesis permiten estudiar:

- nuevos consumers;
- otros Templates;
- estabilidad de los estados;
- estabilidad de las acciones;
- equivalencia;
- aplicabilidad;
- repetición de patrones.

Sin embargo, esta observación no constituye todavía una selección.

### 12.16 Resultado

El discovery no produce una única solución evidente.

En cambio, revela varias capas potenciales:

```text
PROCESS
    Staged Adoption Process

GUIDANCE
    Adoption Guide
    Adoption Checklist

ANALYSIS
    Repository Analyzer

REPRESENTATION
    Adoption Report
    Adoption Manifest

INTERFACE
    CLI

APPLICATION
    Selective Component Application
    Repository Generator

EXECUTION / INTEGRATION
    GitHub Actions

VALIDATION
    Possible Validator Extension
```

Esto permite evitar una decisión prematura basada únicamente en una tecnología.

La pregunta deja de ser:

```text
Should GitHub Framework build a generator or a CLI?
```

y pasa a ser:

```text
Which parts of the adoption process
need to be formalized first,
which need automation,
and which still require
additional evidence?
```

La selección de una solución queda deliberadamente abierta.

---

## 13. Preguntas abiertas

El experimento con Only Film ha permitido identificar un modelo inicial de adopción, Requirement Candidates y diferentes Solution Hypotheses.

Sin embargo, un único consumer no proporciona evidencia suficiente para cerrar determinadas decisiones.

Las siguientes preguntas se mantienen abiertas porque su respuesta podría modificar:

- el modelo de adopción;
- los Requirement Candidates;
- la frontera entre análisis determinista y semántico;
- la arquitectura de una futura solución;
- el alcance de una futura iteración del Framework.

### 13.1 ¿El modelo observado se repite en otros consumers?

Only Film ha producido estados como:

```text
Satisfied
Partial
Equivalent
Missing
Omissible
```

y acciones como:

```text
PRESERVE
ADAPT
ADD
ACCEPT
JUSTIFY
OMIT
```

Debe comprobarse si este modelo sigue siendo suficiente al analizar otros repositorios existentes.

Un nuevo consumer podría revelar:

- estados adicionales;
- acciones adicionales;
- estados innecesarios;
- solapamientos;
- casos ambiguos;
- relaciones diferentes entre estado y acción.

Por tanto, todavía no puede considerarse cerrada la taxonomía.

### 13.2 ¿El modelo funciona con otros Repository Templates?

El experimento se ha realizado exclusivamente con:

```text
TPL-BACKEND
```

No se ha comprobado todavía si el mismo proceso funciona sin modificaciones significativas con:

```text
TPL-DOCUMENTATION
TPL-FULLSTACK
```

Otros Templates pueden introducir:

- diferentes tipos de responsabilidad;
- mayor distribución entre artefactos;
- diferentes criterios de aplicabilidad;
- nuevas relaciones entre Components.

La generalización del modelo necesita evidencia adicional.

### 13.3 ¿Qué constituye evidencia suficiente de equivalencia?

El Framework permite conceptualmente implementaciones:

```text
own
specialized
equivalent
distributed
```

pero el experimento muestra que reconocer equivalencia puede requerir juicio.

Permanece abierta la pregunta:

> ¿Qué evidencia mínima permite afirmar que una implementación consumer-specific satisface suficientemente una responsabilidad del Framework?

Una definición demasiado estricta podría rechazar implementaciones válidas.

Una definición demasiado amplia podría aceptar responsabilidades insuficientemente cubiertas.

### 13.4 ¿Qué estados pertenecen realmente al modelo?

Durante el discovery se han utilizado:

```text
Satisfied
Partial
Equivalent
Missing
Omissible
```

y han aparecido además:

```text
Not applicable
Not identified
Needs evaluation
```

Todavía debe determinarse cuáles de estos conceptos representan:

- estados de responsabilidad;
- propiedades;
- calificadores;
- resultados de aplicabilidad;
- incertidumbre;
- decisiones.

Por ejemplo:

```text
Omissible
```

podría no ser un estado del consumer, sino una consecuencia de:

```text
Requirement Level
        +
Consumer Context
```

De forma similar:

```text
Not applicable
```

podría pertenecer a una dimensión de aplicabilidad independiente.

Formalizar esta taxonomía antes de resolver estas diferencias podría introducir ambigüedad en el modelo.

### 13.5 ¿Qué decisiones necesitan persistirse?

El experimento ha producido decisiones que pueden no modificar archivos:

```text
PRESERVE
ACCEPT
JUSTIFY
OMIT
```

Permanece abierta la cuestión de si estas decisiones deben existir únicamente durante el proceso de adopción o conservarse posteriormente.

Si deben persistirse, sería necesario determinar:

- propósito;
- propietario;
- formato;
- ubicación;
- lifecycle;
- versionado;
- relación con el Template;
- relación con futuras reevaluaciones.

Todavía no existe evidencia suficiente para justificar un Adoption Manifest como solución.

### 13.6 ¿Cuándo termina una adopción?

El modelo emergente identifica:

```text
ANALYZE
REVIEW
DECIDE
APPLY
VERIFY
```

pero todavía no se ha definido qué significa que una adopción esté completa.

Posibles interpretaciones incluyen:

```text
All Required responsibilities resolved
```

o criterios adicionales relacionados con:

```text
Recommended decisions
Explicit omissions
Verification
Unresolved evaluations
```

El experimento actual no necesita resolver esta cuestión, pero una futura formalización del proceso probablemente sí.

### 13.7 ¿Qué significa VERIFY?

`VERIFY` aparece como etapa potencial del Staged Adoption Process.

Sin embargo, todavía no se ha demostrado si representa:

- repetir el análisis;
- validar únicamente cambios aplicados;
- comprobar Required Components;
- revisar decisiones semánticas;
- producir un informe final;
- alguna combinación de las anteriores.

Por tanto, `VERIFY` permanece como parte hipotética del proceso y no como etapa formal.

### 13.8 ¿Cuánto análisis puede automatizarse de forma fiable?

La existencia de archivos y determinadas estructuras presenta alta capacidad de automatización.

La equivalencia y aplicabilidad presentan mayor dependencia semántica.

Entre ambos extremos existen casos intermedios.

Permanece abierta la frontera exacta entre:

```text
Automatically detectable
Human-reviewable
Human-decidable
Automatically actionable
```

La respuesta probablemente dependa también del tipo de Component.

### 13.9 ¿La automatización debe extender el Framework Validator?

El validator actual dispone de una responsabilidad definida sobre reglas deterministas del Framework.

No se ha determinado si el análisis de consumers debería:

```text
extend Framework Validator
```

o:

```text
remain a separate capability
```

La decisión dependerá, entre otros factores, de:

- cuánto comparten ambos dominios;
- qué reglas son deterministas;
- qué semántica necesita el proceso;
- si sus ciclos de evolución son diferentes;
- si compartir implementación introduciría acoplamiento innecesario.

### 13.10 ¿Necesitamos primero proceso, representación o tooling?

Las Solution Hypotheses muestran varias capas:

```text
Process
Guidance
Analysis
Representation
Interface
Application
Integration
Validation
```

Todavía debe determinarse cuál constituye el siguiente nivel mínimo de formalización útil.

Entre las posibilidades se encuentran:

```text
formalize process first
```

```text
formalize assessment representation first
```

```text
automate deterministic analysis first
```

o alguna combinación incremental.

Esta decisión no debería basarse únicamente en facilidad técnica.

Debe depender de qué opción permite validar mejor el modelo con menor compromiso prematuro.

### 13.11 ¿Cuánta evidencia externa es suficiente?

Only Film proporciona la primera evidencia de este discovery sobre un consumer existente independiente del Framework.

Permanece abierta la cuestión de cuántos y qué tipos de consumers deberían analizarse antes de formalizar el modelo.

Podrían resultar relevantes variaciones como:

```text
small / large repository
new / mature repository
high / low documentation
backend / fullstack / documentation
single developer / team
existing automation / no automation
```

No se establece todavía un número mínimo.

La necesidad es obtener diversidad suficiente para distinguir:

```text
Only Film-specific pattern
```

de:

```text
Framework adoption pattern
```

### 13.12 ¿TPL-BACKEND necesita cambios?

El experimento ha utilizado `TPL-BACKEND` como referencia, pero también lo ha sometido indirectamente a validación.

Todavía debe revisarse si alguno de los casos encontrados indica:

- responsabilidades ambiguas;
- niveles Required/Recommended/Optional discutibles;
- solapamiento entre README y Documentation Components;
- criterios de aplicabilidad insuficientes;
- necesidad de mejorar las descripciones de responsabilidades.

No debe asumirse que todo gap pertenece al consumer.

### 13.13 ¿Cómo debe tratarse la personalización heredada?

Only Film contiene referencias heredadas del repositorio original.

Este caso ha permitido clasificar `README-QUICK-START` como `Partial`.

Sin embargo, queda abierta una cuestión más general:

> ¿Hasta qué punto debe el proceso de adopción detectar inconsistencias entre la identidad actual del consumer y contenido heredado?

Esto podría incluir:

- URLs;
- nombres de repositorio;
- paths;
- badges;
- owners;
- referencias documentales.

El experimento demuestra que el problema existe, pero todavía no que deba formar parte de una capacidad general del Framework.

### 13.14 ¿Initialization y Adoption compartirán el mismo modelo?

El discovery distingue:

```text
New Repository Initialization
```

de:

```text
Existing Repository Adoption
```

pero no determina todavía su relación arquitectónica.

Podrían compartir:

```text
Template selection
Components
metadata
application mechanisms
verification
```

mientras difieren en:

```text
analysis
reconciliation
conflict handling
preservation
```

La relación deberá estudiarse antes de diseñar un mecanismo general de repository generation.

### 13.15 ¿Qué debe ocurrir ante incertidumbre?

Un proceso real puede encontrar casos donde la evidencia no permita determinar con confianza:

```text
Satisfied
```

o:

```text
Missing
```

El discovery ha utilizado provisionalmente clasificaciones como:

```text
Partial / Equivalent
```

para conservar esa incertidumbre.

Permanece abierta la cuestión de cómo debería representarse formalmente.

Posibles comportamientos conceptuales incluyen:

```text
Needs Review
Unknown
Unresolved
```

pero ninguno ha sido seleccionado.

### 13.16 Pregunta de decisión para el siguiente paso

Las preguntas anteriores pueden resumirse en una cuestión inmediata:

> ¿Existe ya evidencia suficiente para formalizar una primera capacidad de adopción, o debe realizarse al menos otro experimento con un consumer diferente antes de seleccionar alcance?

Esta pregunta debe resolverse antes de:

- promover Requirement Candidates al backlog;
- seleccionar una Solution Hypothesis;
- crear un Sprint;
- crear un milestone;
- asignar una nueva versión;
- comenzar implementación.

Mantener esta decisión explícita evita que el discovery se convierta automáticamente en planificación.

---

## 14. Conclusiones del discovery

Este discovery partió de una pregunta deliberadamente abierta:

> ¿Qué limita hoy que GitHub Framework sea realmente útil fuera de su propio repositorio?

El experimento con Only Film permite responderla con mayor precisión.

### 14.1 El Framework ya dispone del modelo declarativo

GitHub Framework ya dispone de elementos capaces de describir qué responsabilidades debería considerar un determinado tipo de repositorio:

```text
Standards
    ↓
Components
    ↓
Repository Templates
```

`TPL-BACKEND` proporciona una composición estructurada de responsabilidades clasificadas como:

```text
Required
Recommended
Optional
```

Por tanto, el principal gap observado no consiste en la ausencia de un modelo que describa un repositorio backend.

El Framework ya puede expresar:

```text
What responsibilities should be considered?
```

### 14.2 El gap aparece al aplicar ese modelo sobre un repositorio existente

Only Film fue creado independientemente de GitHub Framework y ya contiene:

- README;
- documentación;
- tests;
- automatización;
- decisiones arquitectónicas;
- convenciones propias;
- contenido específico del proyecto.

Al contrastarlo con `TPL-BACKEND`, las responsabilidades no aparecen únicamente como:

```text
Present
Missing
```

sino mediante situaciones más diversas:

```text
Satisfied
Partial
Equivalent
Missing
Potentially omissible
Not currently applicable
```

Esto obliga a interpretar el estado existente antes de decidir qué hacer.

Por tanto, el gap observado se encuentra entre:

```text
Repository Template
```

y:

```text
Existing Consumer
```

### 14.3 La limitación principal es operacional

El Framework define responsabilidades y dispone de implementaciones reutilizables, pero todavía no proporciona un proceso operacional explícito para responder sistemáticamente:

```text
What already exists?

What responsibility does it satisfy?

Is it sufficient?

Is it equivalent?

Does it need adaptation?

Is something genuinely missing?

Is the responsibility applicable?

What should be preserved?

What should be changed?
```

El proceso utilizado durante este discovery ha tenido que construirse manualmente para realizar esa reconciliación.

La limitación principal identificada puede expresarse por tanto como:

> GitHub Framework dispone de un modelo declarativo de Repository Templates, pero todavía no dispone de un proceso de adopción suficientemente formalizado para reconciliar ese modelo con el estado de un repositorio existente.

### 14.4 Adopción no equivale a generación

El experimento no respalda un modelo simplificado:

```text
Select Template
        ↓
Generate canonical files
        ↓
Repository adopted
```

Only Film ya satisface gran parte de `TPL-BACKEND`.

Una generación indiscriminada podría:

- duplicar documentación;
- sustituir implementaciones válidas;
- fragmentar responsabilidades distribuidas;
- ignorar equivalencias;
- añadir Optional Components sin necesidad;
- sobrescribir contenido específico del consumer.

El proceso observado se aproxima más a:

```text
Existing Repository
        +
Repository Template
        ↓
Analyze
        ↓
Evaluate
        ↓
Decide
        ↓
Apply selected changes
```

Por tanto:

```text
Adoption ≠ Generation
```

aunque la generación pueda formar parte de determinadas acciones futuras.

### 14.5 La adopción comienza por análisis

El experimento completo ha podido realizarse sin modificar Only Film.

Esto demuestra que:

```text
ANALYZE
```

puede existir como etapa independiente de:

```text
APPLY
```

y que el resultado del análisis puede conducir tanto a cambios como a decisiones de no cambiar.

El modelo emergente distingue:

```text
Detected Fact
        ↓
Evaluated State
        ↓
Adoption Decision
        ↓
Applied Change
```

Estas capas no deberían colapsarse prematuramente en una única operación automática.

### 14.6 Preservar forma parte de adoptar

Uno de los resultados más relevantes del experimento es que numerosas responsabilidades ya están correctamente implementadas.

En esos casos:

```text
PRESERVE
```

es una acción válida de adopción.

De forma similar:

```text
ACCEPT
```

puede reconocer una implementación equivalente sin exigir que el consumer adopte la representación canónica del Framework.

Por tanto, el valor de una futura capacidad de adopción no debería medirse por la cantidad de archivos que modifica o genera.

### 14.7 La conformidad sigue siendo semántica

El experimento externo confirma un principio ya presente en el modelo de Repository Templates:

```text
File existence ≠ Responsibility satisfaction
```

Only Film proporciona ejemplos en ambas direcciones:

```text
Artifact exists
        +
Responsibility incomplete
```

y:

```text
Canonical artifact absent
        +
Responsibility evidence present
```

Por tanto, una futura capacidad de adopción o conformance no debería reducir el modelo del Framework a una estructura obligatoria de filesystem.

### 14.8 La automatización tiene una frontera

Parte del análisis presenta alta capacidad de automatización:

```text
file existence
directory existence
workflow existence
explicit metadata
structural patterns
```

Otras decisiones requieren mayor contexto:

```text
equivalence
sufficiency
applicability
justification
consumer-specific adaptation
```

La frontera observada puede resumirse como:

```text
Detect
    ↓
Evidence
    ↓
Evaluate
    ↓
Decision
    ↓
Apply
```

Las primeras etapas presentan actualmente mayor determinismo que las últimas.

Por tanto:

```text
Automatable evidence
        ≠
Automatically safe decision
```

### 14.9 El modelo de adopción todavía es provisional

El experimento ha producido un modelo útil:

```text
Responsibility State
        +
Requirement Level
        +
Consumer Context
        ↓
Adoption Decision
```

y acciones potenciales:

```text
PRESERVE
ADAPT
ADD
ACCEPT
JUSTIFY
OMIT
```

Sin embargo, solo se ha estudiado:

```text
1 Consumer
1 Repository Template
1 Adoption Mode
```

No existe todavía evidencia suficiente para convertir automáticamente esta taxonomía en un Standard estable.

En particular, permanecen abiertas cuestiones sobre:

- equivalencia;
- aplicabilidad;
- incertidumbre;
- persistencia de decisiones;
- finalización de una adopción;
- relación entre Initialization y Existing Repository Adoption.

### 14.10 El discovery ha refinado el espacio de solución

Antes del experimento podían parecer equivalentes ideas como:

```text
Repository Generator
CLI
Validator Extension
GitHub Actions Integration
```

El análisis muestra que pertenecen a capas diferentes.

El espacio potencial puede representarse como:

```text
PROCESS
GUIDANCE
ANALYSIS
REPRESENTATION
INTERFACE
APPLICATION
INTEGRATION
VALIDATION
```

Por tanto, seleccionar una tecnología antes de determinar qué capa necesita formalizarse primero supondría adelantar la solución al problema.

### 14.11 Respuesta a la pregunta inicial

La pregunta inicial era:

> ¿Qué limita hoy que GitHub Framework sea realmente útil fuera de su propio repositorio?

La evidencia obtenida permite formular la siguiente respuesta provisional:

> GitHub Framework ya puede describir mediante Standards, Components y Repository Templates las responsabilidades esperadas de un repositorio, pero todavía carece de un proceso de adopción suficientemente formalizado que permita analizar un consumer existente, reconciliar sus implementaciones con esas responsabilidades y decidir de forma segura qué preservar, adaptar, añadir, aceptar u omitir.

Esta conclusión es más específica que:

```text
The Framework needs more automation
```

y también más específica que:

```text
The Framework needs a repository generator
```

El problema descubierto es anterior a ambas afirmaciones:

```text
The Framework needs to understand
the adoption process before automating it.
```

### 14.12 Resultado del discovery

El experimento ha producido:

```text
✓ External consumer baseline
✓ TPL-BACKEND assessment
✓ Observations
✓ Findings
✓ Emerging adoption model
✓ Automation boundaries
✓ Requirement Candidates
✓ Solution Hypotheses
✓ Open Questions
```

No ha producido:

```text
✗ Selected solution
✗ Approved requirements
✗ Implementation scope
✗ Sprint
✗ Milestone
✗ Release version
```

Esta separación constituye un resultado intencionado del discovery.

---

## 15. Próximos pasos

El siguiente paso no debería ser implementar inmediatamente una de las Solution Hypotheses.

Antes debe decidirse si la evidencia actual es suficiente para formalizar una primera capacidad de adopción o si el modelo necesita validación adicional.

### 15.1 Cerrar formalmente este experimento

El primer paso consiste en considerar Only Film como:

```text
Discovery Experiment #1
```

con:

```text
Consumer: Only Film
Template: TPL-BACKEND
Mode: Existing Repository Adoption
Purpose: Adoption discovery
Consumer changes: None
```

El experimento proporciona evidencia válida, pero no pretende demostrar universalidad.

### 15.2 Revisar los Requirement Candidates

Los Requirement Candidates deberán revisarse para identificar:

```text
Supported by direct evidence
Needs additional evidence
Potentially overlapping
Too implementation-specific
Potentially generalizable
Consumer-specific
```

El objetivo no es priorizarlos todavía, sino reducirlos a un modelo coherente de necesidades.

En particular, deberá comprobarse si los quince candidatos pueden consolidarse alrededor de las capacidades ya identificadas:

```text
Responsibility Model
Analysis
Adoption Decisions
Safe Application
Framework Validation
```

### 15.3 Validar el modelo con evidencia adicional

Antes de considerar la formalización de la taxonomía emergente como Standard, resulta conveniente contrastarla con evidencia adicional obtenida mediante otros escenarios de adopción.

El objetivo del siguiente experimento no sería repetir mecánicamente todo el análisis, sino intentar refutar o ampliar el modelo actual.

Las preguntas principales serían:

```text
Do the same states appear?

Do the same adoption actions appear?

Are new states needed?

Does equivalence remain important?

Does applicability behave similarly?

Does the Analyze → Decide separation still hold?
```

Un segundo consumer debería seleccionarse por su capacidad para aportar evidencia diferente, no únicamente por conveniencia.

### 15.4 Considerar diversidad de escenario

El siguiente experimento podría variar una dimensión relevante respecto a Only Film.

Por ejemplo:

```text
Different Repository Template
```

o:

```text
Different repository maturity
```

o:

```text
Different documentation level
```

o:

```text
Repository with active development
```

La selección deberá maximizar aprendizaje y evitar validar únicamente el mismo patrón con un consumer demasiado similar.

### 15.5 Mantener separadas validación y solución

Durante el siguiente experimento deberían mantenerse abiertas las Solution Hypotheses.

En particular, no debería asumirse todavía que el resultado será:

```text
CLI
Generator
Manifest
Validator Extension
GitHub Action
```

El objetivo debe seguir siendo comprobar el modelo del problema.

Si diferentes consumers producen consistentemente:

```text
Analyze
        ↓
Evaluate
        ↓
Decide
        ↓
Apply
```

existirá mayor evidencia para formalizar ese proceso.

### 15.6 Identificar el Minimum Useful Formalization

Después de validar el modelo deberá determinarse cuál es la formalización mínima que aporta valor real.

La pregunta no debería ser:

```text
What is the most complete adoption system we can build?
```

sino:

```text
What is the smallest capability
that makes adoption meaningfully more usable
while preserving the evidence-based model?
```

Entre las posibilidades actualmente abiertas se encuentran:

```text
Adoption Guide
Assessment model
Deterministic Analyzer
Staged Adoption Process
```

individualmente o mediante una combinación limitada.

### 15.7 Posponer automatización destructiva

Hasta disponer de mayor evidencia deberían mantenerse fuera de una primera formalización aquellas capacidades que impliquen cambios automáticos significativos sobre consumers existentes.

Especialmente:

```text
automatic overwrite
automatic semantic adaptation
full repository regeneration
automatic equivalence decisions
automatic applicability decisions
```

Esto no implica descartarlas.

Implica mantenerlas posteriores a la estabilización del modelo que necesitan ejecutar.

### 15.8 Revisar `TPL-BACKEND`

El experimento también deberá utilizarse para revisar si `TPL-BACKEND` necesita refinamientos.

La revisión debería centrarse en:

- claridad de responsabilidades;
- requirement levels;
- posibles solapamientos;
- criterios de aplicabilidad;
- relación entre README y Documentation Components;
- facilidad de evaluación sobre consumers existentes.

Cualquier cambio deberá justificarse por evidencia y no únicamente por el deseo de hacer que Only Film resulte conforme.

### 15.9 No abrir todavía un nuevo ciclo de delivery

Al cierre de este documento no se propone todavía:

```text
new Sprint
new milestone
new release version
implementation branch
```

El proyecto permanece en discovery.

El siguiente ciclo de delivery debería comenzar únicamente cuando exista suficiente evidencia para responder:

```text
What problem are we solving?

For whom?

What is the minimum useful scope?

What evidence supports it?

What is explicitly out of scope?
```

### 15.10 Criterio para abandonar discovery

El discovery podrá considerarse suficientemente maduro para pasar a planificación cuando:

1. el problema de adopción pueda expresarse de forma estable;
2. los principales Requirement Candidates hayan sido consolidados;
3. se haya contrastado el modelo con evidencia suficiente;
4. exista una frontera clara entre necesidad y solución;
5. pueda definirse un incremento pequeño y verificable;
6. los principales riesgos de automatización estén comprendidos;
7. pueda establecerse un alcance explícito y un fuera de alcance.

Solo entonces debería decidirse:

```text
Backlog
    ↓
Scope
    ↓
Sprint / Milestone
    ↓
Version
    ↓
Implementation
```

### 15.11 Siguiente decisión

El siguiente paso inmediato es revisar el documento completo y decidir entre dos caminos:

```text
A. Evidence sufficient
        ↓
Consolidate requirements
        ↓
Define minimum formalization

B. Evidence insufficient
        ↓
Run Discovery Experiment #2
        ↓
Compare findings
```

Esta decisión deberá tomarse después de revisar el conjunto de evidencia y no como consecuencia automática de haber finalizado este documento.

---

## Estado del documento

```text
Discovery: Backend Adoption
Consumer: Only Film
Template: TPL-BACKEND v0.1.0
Adoption mode: Existing Repository
Consumer modified: No
Experiment status: Completed
Discovery phase: Active
Solution selected: No
Delivery scope selected: No
Sprint created: No
Milestone created: No
Release assigned: No
```

