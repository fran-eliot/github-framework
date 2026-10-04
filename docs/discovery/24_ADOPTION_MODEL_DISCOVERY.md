# 24 — Adoption Model Discovery

## 1. Propósito

Este documento consolida los hallazgos obtenidos durante la investigación del proceso de adopción de GitHub Framework sobre repositorios existentes.

Su objetivo es comprender qué modelo mínimo necesita el Framework para analizar un repositorio consumidor, comparar su estado con las responsabilidades definidas por un Repository Template y representar de forma explícita las decisiones necesarias para su adopción.

La investigación parte de una pregunta central:

> ¿Qué necesita GitHub Framework para reconciliar de forma segura un Repository Template con un repositorio existente sin asumir que adoptar significa generar o sustituir archivos?

Este documento no define todavía una solución técnica ni una nueva funcionalidad del Framework.

Su propósito es consolidar evidencia suficiente para comprender el problema antes de seleccionar una solución.

---

## 2. Contexto

GitHub Framework dispone actualmente de un modelo declarativo formado por:

~~~text
Standards
    ↓
Components
    ↓
Repository Templates
~~~

Los Repository Templates permiten expresar qué responsabilidades son:

- Required;
- Recommended;
- Optional.

El Framework también reconoce que un consumer puede satisfacer una responsabilidad mediante:

- una implementación canónica;
- una implementación propia;
- una especialización compatible;
- una implementación equivalente;
- una implementación distribuida entre varios artefactos.

Por tanto, la conformidad no depende de reproducir literalmente una estructura de archivos determinada.

La primera investigación de adopción mostró que esta capacidad declarativa no resuelve por sí sola el proceso mediante el cual un repositorio existente puede adoptar el Framework.

Entre:

~~~text
Repository Template
~~~

y:

~~~text
Consumer Repository
~~~

es necesario comprender un proceso de reconciliación capaz de responder preguntas como:

~~~text
¿Qué existe ya?

¿Qué responsabilidad satisface?

¿La satisface completamente?

¿Es aplicable a este consumer?

¿Debe conservarse?

¿Debe adaptarse?

¿Debe añadirse algo?

¿Puede aceptarse una implementación equivalente?

¿Puede omitirse justificadamente?
~~~

Esta necesidad dio lugar a la investigación de un modelo mínimo de adopción.

---

## 3. Relación con `23_BACKEND_ADOPTION_DISCOVERY`

Este documento continúa la investigación iniciada en:

~~~text
docs/discovery/23_BACKEND_ADOPTION_DISCOVERY.md
~~~

El documento `23_BACKEND_ADOPTION_DISCOVERY` utilizó `TPL-BACKEND` sobre un repositorio existente para observar por primera vez el proceso real de adopción.

Ese experimento permitió identificar, entre otros, los siguientes hallazgos:

- adoptar un Template sobre un repositorio existente es principalmente un problema de reconciliación;
- la unidad de análisis debe ser la responsabilidad y no el archivo;
- presencia física y satisfacción de una responsabilidad son conceptos diferentes;
- el estado de una responsabilidad y la acción de adopción son conceptos diferentes;
- la detección determinista no sustituye a la evaluación semántica;
- una implementación equivalente puede satisfacer una responsabilidad;
- el nivel de requisito influye en la decisión de adopción;
- análisis y aplicación deben permanecer separados;
- la evidencia y las decisiones necesitan trazabilidad.

A partir de estos hallazgos surgieron Requirement Candidates y diferentes Solution Hypotheses.

Sin embargo, un único consumer no proporciona evidencia suficiente para convertir esas observaciones en un modelo general.

El presente documento amplía la investigación mediante consumers adicionales con características técnicas y documentales diferentes.

Su finalidad no es repetir el primer experimento, sino intentar:

~~~text
confirmar
refinar
contradecir
o falsificar
~~~

el modelo emergente.

Por tanto:

~~~text
23_BACKEND_ADOPTION_DISCOVERY
        ↓
Problem Discovery
        ↓
Initial Adoption Model
        ↓
Additional Consumer Experiments
        ↓
24_ADOPTION_MODEL_DISCOVERY
        ↓
Model Consolidation
~~~

---

## 4. Alcance y límites

### 4.1 Incluido

Esta investigación incluye:

- adopción de `TPL-BACKEND`;
- repositorios existentes;
- evaluación por responsabilidades;
- análisis de evidencia;
- estados de responsabilidad;
- applicability;
- formas o características de implementación;
- niveles Required, Recommended y Optional;
- decisiones de adopción;
- trazabilidad entre evidencia, evaluación y decisión;
- comparación entre varios consumers;
- identificación de límites de automatización;
- refinamiento del modelo mínimo de adopción.

### 4.2 Fuera de alcance

Esta investigación no pretende:

- modificar los repositorios utilizados como consumers;
- generar archivos;
- corregir automáticamente documentación;
- definir un formato YAML o JSON de adopción;
- introducir un `github-framework.yml`;
- diseñar una CLI;
- implementar un analyzer;
- extender el Framework Validator;
- integrar GitHub Actions;
- definir un repository generator;
- automatizar decisiones semánticas;
- definir todavía el proceso de aplicación de cambios;
- diseñar rollback;
- resolver el flujo de inicialización de repositorios nuevos;
- seleccionar funcionalidades para una próxima release;
- crear un Sprint;
- crear una milestone;
- asignar una versión.

Las posibles soluciones técnicas permanecerán como hipótesis hasta que la investigación proporcione evidencia suficiente para seleccionarlas.

### 4.3 Principio de trabajo

La investigación mantiene la siguiente separación:

~~~text
Detected Fact
      ≠
Evidence
      ≠
Evaluated State
      ≠
Adoption Decision
      ≠
Applied Change
~~~

El objetivo de Discovery es comprender las relaciones entre estos conceptos antes de automatizarlos.

### 4.4 Criterio de prudencia

Ningún hallazgo aislado se considerará automáticamente una regla general del Framework.

Los patrones observados deberán contrastarse entre varios consumers antes de promoverse a:

~~~text
Discovery Finding
        ↓
Requirement
        ↓
Standard
        ↓
Implementation
~~~

Del mismo modo, una Solution Hypothesis no constituye una decisión de implementación.

La investigación debe permitir que la evidencia determine la solución, y no utilizar los experimentos para justificar una solución elegida previamente.

---

## 5. Preguntas de contraste derivadas del Experimento #1

El Experimento #1 permitió identificar un modelo inicial de Existing Repository Adoption y varios aspectos que requerían contraste adicional.

Los Experimentos #2 y #3 no fueron diseñados a partir de un protocolo formal previamente registrado.

Por tanto, las siguientes preguntas no deben interpretarse como hipótesis experimentales definidas ex ante.

Representan una reconstrucción explícita de las principales cuestiones que emergieron del primer experimento y que posteriormente fueron contrastadas mediante consumers adicionales.

Su función es proporcionar una estructura común para interpretar la evidencia acumulada sin atribuir al proceso un grado de formalización que no tuvo originalmente.

---

### 5.1 Representación de consumers diferentes

Primera pregunta de contraste:

> ¿Puede el modelo emergente representar consumers tecnológicamente y documentalmente diferentes sin necesitar nuevos estados fundamentales, nuevas acciones de adopción o reglas específicas para cada tecnología?

El Experimento #1 había producido provisionalmente:

~~~text
Responsibility State

    Satisfied
    Partial
    Missing
~~~

y:

~~~text
Adoption Action

    PRESERVE
    ADAPT
    ADD
    ACCEPT
    EVALUATE
    JUSTIFY
    OMIT
~~~

Los siguientes consumers permiten observar si estas categorías continúan siendo útiles cuando cambia la forma real del repositorio.

---

### 5.2 Separación entre estado, implementación, evidencia y decisión

Segunda pregunta de contraste:

> ¿Es suficiente representar una responsabilidad mediante su estado y su acción, o los consumers adicionales muestran que deben distinguirse otras dimensiones?

El primer experimento ya había sugerido:

~~~text
Detected Fact
        ≠
Evaluated State
        ≠
Adoption Decision
        ≠
Applied Change
~~~

Los siguientes experimentos permiten comprobar especialmente el papel de:

~~~text
Evidence

Reason / Rationale

Implementation Characteristics

Uncertainty
~~~

y determinar si alguno de estos conceptos debe permanecer separado de `State`.

---

### 5.3 Requirement Level, applicability y contexto

Tercera pregunta de contraste:

> ¿Puede una decisión de adopción derivarse únicamente de `State` y `Requirement Level`, o necesita considerar también applicability y contexto del consumer?

El modelo inicial podía expresarse de forma simplificada como:

~~~text
STATE
+
REQUIREMENT LEVEL
+
CONTEXT
    ↓
ACTION
~~~

Los siguientes consumers permiten observar si esta relación necesita mayor precisión.

---

### 5.4 Carácter provisional de las preguntas

Estas preguntas sirven como instrumentos de contraste y consolidación.

No constituyen:

- hipótesis estadísticas;
- criterios de aceptación de una feature;
- un protocolo experimental pre-registrado;
- requisitos normativos del Framework.

Su utilidad consiste en hacer explícitas las cuestiones que emergieron durante Discovery y comprobar cómo evolucionan al introducir nuevos consumers.

Por tanto, el resultado esperado no es simplemente:

~~~text
confirm
or
reject
~~~

sino también:

~~~text
reinforce

refine

contradict

leave unresolved
~~~

según la evidencia disponible.

---

## 6. Método de contraste

### 6.1 Estrategia

Para ampliar la evidencia del Experimento #1 se mantiene constante:

~~~text
Repository Template
    TPL-BACKEND v0.1.0

Adoption Mode
    Existing Repository Adoption
~~~

y se modifica el consumer.

Esto permite observar cómo responde el modelo emergente ante repositorios con tecnologías y perfiles documentales diferentes.

Los consumers utilizados son:

| Experiment | Consumer | Main Technology |
|---|---|---|
| #1 | Only Film | Java / Spring Boot |
| #2 | dental-back | TypeScript / NestJS |
| #3 | aula-robotica-platform | Python / FastAPI |

La comparación no pretende demostrar representatividad estadística.

Su objetivo es buscar evidencia capaz de:

- reforzar conceptos emergentes;
- obligar a refinarlos;
- revelar contradicciones;
- descubrir dimensiones no consideradas;
- identificar límites de la investigación.

---

### 6.2 Unidad de assessment

La unidad principal continúa siendo:

~~~text
Responsibility
~~~

y no:

~~~text
File
~~~

Cada responsabilidad del Repository Template debe evaluarse según la evidencia disponible en el consumer.

Un archivo puede proporcionar evidencia para una o varias responsabilidades.

Una responsabilidad puede estar distribuida entre varios artefactos.

---

### 6.3 Fuentes de evidencia

La evidencia puede proceder de:

- README;
- documentación;
- código;
- configuración;
- tests;
- workflows;
- diagramas;
- especificaciones;
- estructura versionada;
- otros artefactos relevantes.

La existencia de un artefacto constituye evidencia potencial.

No determina automáticamente el estado de una responsabilidad.

---

### 6.4 Cadena de razonamiento

Durante el contraste se mantiene explícita la separación:

~~~text
Detected Fact
        ↓
Evidence
        ↓
Evaluation
        ↓
Responsibility State
        ↓
Adoption Decision
~~~

La investigación puede añadir qualifiers o rationale cuando sean necesarios para explicar la evaluación.

No se asume que todos estos elementos deban convertirse posteriormente en campos persistentes de una implementación.

---

### 6.5 Responsibility State

Se utiliza provisionalmente:

~~~text
Satisfied
Partial
Missing
~~~

como taxonomía mínima de estado.

Uno de los objetivos del contraste es observar si aparecen situaciones que no puedan representarse adecuadamente mediante estos tres estados.

Conceptos como:

~~~text
Equivalent
Specialized
Distributed
Not Applicable
Uncertain
Omissible
~~~

no se incorporan automáticamente como nuevos estados.

Su naturaleza se determina a partir de la evidencia.

---

### 6.6 Applicability

Se observa de forma independiente si una responsabilidad resulta:

~~~text
Applicable
Not Applicable
Uncertain
~~~

para el contexto concreto del consumer.

Esta dimensión se mantiene separada tanto de:

~~~text
Requirement Level
~~~

como de:

~~~text
Responsibility State
~~~

mientras la evidencia permita sostener esa separación.

---

### 6.7 Características de implementación

Los experimentos observan también cómo se materializa una responsabilidad.

Entre las características identificadas inicialmente aparecen:

~~~text
Canonical
Own
Equivalent
Specialized
Distributed
~~~

Estas categorías permanecen provisionales.

En particular, no se presupone que sean mutuamente excluyentes.

Los consumers adicionales pueden mostrar que una implementación necesita varias características simultáneamente o que la taxonomía debe reorganizarse.

---

### 6.8 Adoption Decision

Las decisiones provisionales procedentes del primer experimento son:

~~~text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
~~~

Los experimentos posteriores permiten observar:

- si estas decisiones continúan siendo suficientes;
- si diferentes estados pueden conducir a decisiones diferentes;
- si una misma decisión puede derivarse de razones distintas;
- qué información adicional interviene en la decisión.

No se presupone una correspondencia automática:

~~~text
State → Action
~~~

---

### 6.9 Analysis frente a Application

Los experimentos se limitan a:

~~~text
analyze
assess
review
reason
record findings
~~~

No modifican los consumers.

Por tanto, la investigación puede aportar evidencia directa sobre assessment y adoption decision, pero no sobre la seguridad de una futura fase de aplicación.

En particular, no valida:

~~~text
generation
patching
merge
rollback
idempotency
automatic correction
~~~

---

### 6.10 Búsqueda de contradicciones y refinamientos

El contraste no pretende demostrar que el modelo inicial sea correcto.

Para cada nuevo consumer se busca especialmente:

- una responsabilidad que no pueda representarse mediante los estados existentes;
- una decisión que no pueda expresarse mediante las acciones existentes;
- una implementación que contradiga la separación entre responsabilidad y archivo;
- una situación donde applicability no pueda mantenerse separada;
- una pérdida relevante de información en el modelo;
- una nueva etapa necesaria en el proceso;
- evidencia que contradiga un Requirement Candidate anterior.

La ausencia de contradicción no se interpreta como prueba de universalidad.

---

### 6.11 Interpretación de los resultados

Durante la consolidación de los experimentos resulta útil distinguir tres tipos generales de resultado:

~~~text
MODEL HOLDS

El consumer puede representarse mediante
los conceptos existentes sin cambios relevantes.
~~~

~~~text
REFINEMENT NEEDED

Los fundamentos continúan siendo útiles,
pero la evidencia exige separar, precisar
o ampliar alguna dimensión.
~~~

~~~text
MODEL CONTRADICTION

El consumer presenta una situación que
los fundamentos existentes no pueden
representar adecuadamente.
~~~

Estas categorías son una herramienta retrospectiva de interpretación.

No constituyen criterios de resultado pre-registrados antes de ejecutar los experimentos.

Tampoco representan estados normativos del Framework.

Su función es facilitar la comparación de lo observado y hacer explícito cuándo la evidencia conserva, refina o contradice el modelo emergente.

---

### 6.12 Límites metodológicos

Los resultados deben interpretarse dentro de los límites de esta investigación.

Los tres consumers:

- utilizan el mismo Repository Template;
- pertenecen al dominio backend;
- son repositorios existentes;
- proceden de un conjunto limitado de proyectos;
- no representan todos los posibles estilos de repositorio;
- no prueban Repository Initialization;
- no prueban Application;
- no prueban otros Repository Templates.

Por tanto:

~~~text
repeated evidence
        ≠
universal rule
~~~

Cualquier generalización posterior deberá conservar estos límites.

---

## 7. Experimento #2 — `dental-back`

### 7.1 Objetivo

El segundo experimento utiliza un nuevo consumer manteniendo constantes:

~~~text
Repository Template
    TPL-BACKEND v0.1.0

Adoption Mode
    Existing Repository Adoption
~~~

El objetivo no es realizar una segunda demostración del primer experimento.

Su propósito es comprobar si el modelo emergente puede explicar un backend tecnológicamente diferente y detectar posibles dependencias accidentales respecto al consumer utilizado inicialmente.

En particular, el experimento pretende comprobar:

- si `Satisfied`, `Partial` y `Missing` continúan siendo suficientes como estados fundamentales;
- si el estado puede mantenerse separado de la razón que lo produce;
- si existen implementaciones equivalentes o propias que no deben confundirse con ausencia;
- si `Applicability` necesita tratarse independientemente;
- si las acciones de adopción identificadas siguen siendo suficientes;
- si la evidencia necesita conservarse explícitamente para explicar la evaluación.

---

### 7.2 Consumer

Consumer:

~~~text
fran-eliot/dental-back
~~~

Contexto tecnológico principal:

~~~text
TypeScript
NestJS
MySQL
TypeORM
JWT
Swagger
~~~

El repositorio implementa el backend de una aplicación de gestión para una clínica dental.

Entre las capacidades descritas por el propio proyecto se encuentran:

- autenticación mediante JWT;
- autorización mediante roles;
- gestión relacionada con citas y entidades del dominio;
- persistencia mediante MySQL y TypeORM;
- documentación de API mediante Swagger.

El consumer representa un contraste útil con el primer experimento porque concentra una parte importante de su documentación en el README y dispone de una estructura documental independiente mucho más reducida.

---

### 7.3 Baseline estructural

El inventario de archivos versionados mostró, entre otros, los siguientes elementos:

~~~text
.gitignore
.prettierrc
README.md
docs/DER clinica_dental.png
eslint.config.mjs
nest-cli.json
package.json
package-lock.json
prueba.ts
src/
test/
tsconfig.build.json
tsconfig.json
~~~

También se observaron módulos y código correspondientes a las diferentes responsabilidades funcionales del backend.

En el baseline no se identificaron:

~~~text
CHANGELOG.md
LICENSE
CONTRIBUTING.md
.github/
~~~

Estas ausencias constituyen hechos estructurales.

No deben convertirse automáticamente en conclusiones sobre todas las responsabilidades asociadas.

Por ejemplo:

~~~text
LICENSE absent
        ≠
README-LICENSE necessarily Missing
~~~

porque el README puede contener información relacionada con la licencia aunque no exista un archivo `LICENSE`.

---

### 7.4 Baseline documental

El README presenta una cantidad considerable de información sobre el proyecto.

Entre sus elementos se identificaron:

- título y descripción del backend;
- badges tecnológicos y de estado;
- descripción funcional;
- tecnologías utilizadas;
- autenticación y autorización;
- endpoints y Swagger;
- estructura del proyecto;
- relación con `dental-front`;
- mejoras futuras;
- autores;
- información sobre licencia;
- instrucciones de instalación y ejecución;
- modelo de datos;
- entidades, relaciones y enums.

El repositorio dispone además de:

~~~text
docs/DER clinica_dental.png
~~~

como evidencia gráfica del modelo de datos.

Este baseline resulta especialmente útil para comprobar si una responsabilidad puede estar implementada mediante contenido integrado en el README o mediante artefactos distintos de un documento Markdown dedicado.

---

## 8. Resultados del Experimento #2

### 8.1 Responsabilidades Required

La evaluación de las ocho responsabilidades Required de `TPL-BACKEND` produjo el siguiente resultado:

| Responsibility | State | Evidence / Rationale |
|---|---|---|
| `README-HERO` | Satisfied | El README identifica claramente el proyecto y proporciona una presentación inicial mediante título, descripción y badges. |
| `README-OVERVIEW` | Satisfied | Existe una explicación del propósito y contexto funcional del backend. |
| `README-FEATURES` | Satisfied | Las capacidades principales están descritas explícitamente. |
| `README-TECH-STACK` | Satisfied | El stack tecnológico se encuentra identificado y explicado. |
| `README-QUICK-START` | Partial | Existen instrucciones de instalación y ejecución, pero el comando de clonación conserva el placeholder `tuusuario/backend-clinica-dental.git`. |
| `README-DOCUMENTATION` | Partial | Existe documentación técnica relevante dentro del README y evidencia documental adicional, pero la responsabilidad de acceso/navegación hacia documentación extensa no queda completamente resuelta. |
| `README-FOOTER` | Satisfied | El cierre del README contiene información final del proyecto y autoría. |
| `DOC-CHANGELOG` | Missing | No se identificó un changelog ni evidencia equivalente suficiente para considerar satisfecha esta responsabilidad. |

Resultado:

~~~text
Satisfied    5
Partial      2
Missing      1
~~~

El resultado cuantitativo coincide con el obtenido en el primer consumer.

Sin embargo, esta coincidencia no implica que ambos repositorios presenten los mismos problemas.

---

### 8.2 Mismo estado, diferente evidencia

El contraste más claro aparece en `README-QUICK-START`.

En Only Film la responsabilidad fue evaluada como `Partial` porque las instrucciones conservaban referencias heredadas del repositorio original.

En `dental-back`, la misma responsabilidad también resulta `Partial`, pero por una razón diferente:

~~~text
Only Film
    inherited repository reference
            ↓
         Partial

dental-back
    generic repository placeholder
            ↓
         Partial
~~~

Por tanto:

~~~text
Responsibility State
        ≠
Reason for State
~~~

Guardar únicamente:

~~~text
README-QUICK-START = Partial
~~~

eliminaría información necesaria para comprender qué ocurre realmente en cada consumer.

El experimento refuerza así la necesidad de conservar tanto la evidencia como el razonamiento de evaluación.

---

### 8.3 Presencia no equivale a satisfacción

`README-QUICK-START` proporciona también un segundo resultado relevante.

La sección existe.

Las instrucciones existen.

El repositorio contiene los elementos necesarios para ejecutar el proyecto.

Sin embargo, un dato incorrectamente personalizado impide considerar completamente satisfecha la responsabilidad.

Por tanto:

~~~text
Section Present
        ≠
Responsibility Satisfied
~~~

Esto refuerza el límite identificado en el primer experimento respecto a una futura detección puramente estructural.

Un analyzer podría detectar determinísticamente que existe una sección de instalación.

Determinar que el enlace de clonación contiene un placeholder requiere una evaluación adicional.

---

### 8.4 Evidencia fuera de documentos canónicos

El consumer aporta también evidencia relevante mediante:

~~~text
docs/DER clinica_dental.png
~~~

El diagrama constituye información real sobre el modelo de datos aunque no adopte la forma de un documento Markdown canónico del Framework.

Esto refuerza:

~~~text
Responsibility
        ≠
Canonical Artifact
~~~

y demuestra que la evidencia de una responsabilidad puede adoptar formatos diferentes.

La evaluación debe poder reconocer esa evidencia antes de decidir si satisface total o parcialmente la responsabilidad correspondiente.

---

### 8.5 Recommended

El análisis de las responsabilidades Recommended mostró un consumer con información relevante distribuida principalmente entre el README, el código y los artefactos existentes.

Se identificó evidencia especialmente clara para:

- estado del proyecto;
- estructura del repositorio;
- aspectos arquitectónicos;
- modelo de datos;
- testing.

Sin embargo, el experimento mostró también que detectar esa evidencia no basta para convertir automáticamente cada responsabilidad documental en `Satisfied`.

Por ejemplo:

~~~text
tests present
        ≠
DOC-TESTING automatically Satisfied
~~~

y:

~~~text
architecture information present in README
        ≠
dedicated architecture responsibility
automatically Satisfied
~~~

La evaluación Recommended reforzó por tanto la necesidad de distinguir:

~~~text
Artifact Detection
        ↓
Semantic Evidence
        ↓
Responsibility Assessment
~~~

sin introducir un nuevo estado fundamental.

---

### 8.6 Optional y Applicability

Las responsabilidades Optional proporcionaron un segundo tipo de challenge.

Algunas responsabilidades disponían de evidencia claramente relacionada con el consumer, mientras que otras no podían evaluarse correctamente mediante una simple búsqueda de archivos.

Un ejemplo especialmente significativo es la documentación API.

`dental-back` implementa una API real y utiliza Swagger.

Por tanto, `DOC-API` tiene una aplicabilidad diferente a la observada en Only Film, donde la API figuraba como una posibilidad futura del proyecto.

Esto refuerza que:

~~~text
Applicability
        ≠
State
~~~

y que el mismo Repository Template puede contener responsabilidades cuya aplicabilidad cambia según el consumer.

La ausencia de un artefacto asociado a una responsabilidad Optional no debe transformarse automáticamente en una acción `ADD`.

Antes debe determinarse si la responsabilidad es aplicable.

---

### 8.7 Evaluación del modelo inicial

El segundo consumer pudo analizarse sin introducir:

- un nuevo estado fundamental;
- una nueva acción fundamental;
- una nueva etapa fundamental del proceso.

Los estados:

~~~text
Satisfied
Partial
Missing
~~~

continuaron siendo suficientes para representar el grado de satisfacción observado.

Las acciones provisionales:

~~~text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
~~~

también continuaron siendo capaces de representar las decisiones consideradas durante el análisis.

Sin embargo, el experimento mostró que el modelo necesitaba mayor precisión para representar por qué una responsabilidad recibe determinado estado y cómo está implementada.

---

### 8.8 Contraste con las preguntas derivadas del Experimento #1

#### Representación de consumers diferentes

**Evidencia que refuerza el modelo.**

El modelo pudo aplicarse a un backend NestJS/TypeScript sin introducir estados o acciones específicos de esa tecnología.

Esto aporta evidencia favorable a que las categorías emergentes del primer experimento pueden utilizarse sobre un consumer tecnológicamente diferente.

#### Separación entre estado, implementación, evidencia y decisión

**Evidencia que refuerza y precisa la separación.**

El contraste entre los dos `README-QUICK-START` demuestra que dos responsabilidades pueden compartir estado y eventual acción mientras mantienen evidencia y razones diferentes.

El diagrama de datos refuerza además la existencia de implementaciones y evidencias no limitadas a archivos canónicos.

Por tanto, el segundo consumer no solo conserva la separación inicial, sino que muestra que `State` no contiene información suficiente para explicar por sí solo el assessment.

#### Requirement Level, applicability y contexto

**Evidencia que refuerza la necesidad de considerar dimensiones separadas.**

La diferencia de applicability de responsabilidades como `DOC-API` entre los dos consumers muestra que el Template por sí solo no determina todas las decisiones de adopción.

El contexto del consumer continúa siendo necesario para interpretar la responsabilidad.

---

### 8.9 Impacto sobre los Requirement Candidates

El segundo experimento no refutó ninguno de los Requirement Candidates surgidos del primero.

La evidencia reforzó especialmente:

~~~text
RC-01  Analyze existing consumer against Template

RC-02  Distinguish responsibility state

RC-03  Separate state and adoption action

RC-06  Recognize equivalent, specialized
       or distributed implementations

RC-07  Consider requirement level and applicability

RC-09  Preserve traceability between
       evidence, evaluation and decision

RC-10  Separate analysis from application

RC-11  Distinguish deterministic detection
       from semantic evaluation

RC-12  Represent uncertainty
~~~

RC-04, RC-05 y RC-08 continuaron siendo compatibles con la evidencia relativa a preservar, adaptar y justificar decisiones.

RC-13 y parte de RC-14 no fueron sometidos a una validación directa suficiente porque el experimento no modificó el consumer ni evaluó el flujo de inicialización.

RC-15 quedó reforzado por el propio experimento: utilizar un consumer externo al Framework volvió a revelar propiedades del modelo que el dogfooding por sí solo no había hecho explícitas.

---

### 8.10 Refinamiento emergente

El principal refinamiento producido por el segundo experimento puede expresarse como:

~~~text
Evidence
    ↓
Evaluation
    ↓
State + Qualifiers
    ↓
Adoption Decision
    ↓
Rationale
~~~

El estado deja de ser suficiente como representación completa del assessment.

También emerge con mayor claridad la necesidad de distinguir dimensiones que inicialmente aparecían mezcladas:

~~~text
State

Applicability

Implementation Characteristics

Evidence / Reason
~~~

Este refinamiento no modifica todavía formalmente el modelo.

Se convierte en una hipótesis que deberá ser sometida al tercer consumer.

---

### 8.11 Interpretación del challenge

La interpretación retrospectiva del segundo experimento es:

~~~text
REFINEMENT NEEDED
~~~

El consumer no proporciona una contradicción fundamental del modelo inicial.

Sin embargo, demuestra que una representación basada únicamente en:

~~~text
Responsibility
+
State
+
Action
~~~

pierde información relevante.

En particular, la evidencia muestra la necesidad de representar mejor:

- la evidencia que fundamenta el assessment;
- la razón concreta del estado;
- la applicability;
- las características de la implementación;
- la trazabilidad hasta la decisión de adopción.

Por tanto, el Experimento #2 conserva los fundamentos principales surgidos del primero, pero obliga a refinarlos.

Este resultado se utiliza como base para someter el modelo refinado a un tercer consumer con mayor riqueza documental y mayor distribución de responsabilidades.

La categoría `REFINEMENT NEEDED` se utiliza aquí como instrumento retrospectivo de interpretación y no como un resultado definido previamente a la ejecución del experimento.

---

## 9. Experimento #3 — `aula-robotica-platform`

### 9.1 Objetivo

El tercer experimento somete el modelo refinado tras los dos primeros consumers a un escenario documentalmente más rico y estructuralmente más distribuido.

Se mantienen constantes:

~~~text
Repository Template
    TPL-BACKEND v0.1.0

Adoption Mode
    Existing Repository Adoption
~~~

y se modifica nuevamente el consumer.

El objetivo principal es intentar encontrar situaciones que el modelo refinado no pueda representar adecuadamente.

En particular, el experimento pretende comprobar:

- si una responsabilidad puede estar distribuida entre múltiples artefactos;
- si una implementación puede presentar varias características simultáneamente;
- si la ausencia de una ubicación canónica sigue siendo irrelevante cuando existe evidencia equivalente;
- si la presencia de un artefacto nominalmente coincidente garantiza o no la satisfacción semántica;
- si `Applicability` continúa siendo independiente de `State`;
- si los tres estados fundamentales siguen siendo suficientes;
- si las acciones de adopción existentes continúan siendo suficientes;
- si aparece alguna nueva dimensión fundamental.

---

### 9.2 Consumer

Consumer:

~~~text
fran-eliot/aula-robotica-platform
~~~

Contexto tecnológico principal:

~~~text
Python
FastAPI
MariaDB
Docker
Nginx
WebSockets
GitHub Actions
SonarCloud
Pytest
~~~

El proyecto representa una plataforma colaborativa de robótica educativa que ha evolucionado desde un entorno académico local hacia una aplicación desplegada sobre infraestructura Linux mediante contenedores.

El consumer resulta especialmente útil para este challenge porque combina:

- backend modular;
- IAM y autorización contextual;
- persistencia;
- comunicación realtime;
- infraestructura Docker;
- CI/CD;
- testing automatizado;
- documentación técnica extensa;
- diagramas;
- especificación OpenAPI;
- documentación de operaciones;
- documentación de decisiones;
- documentación de estado.

A diferencia de los dos consumers anteriores, muchas responsabilidades potenciales no se concentran en un único README o documento.

---

### 9.3 Baseline documental

El README contiene, entre otros:

- descripción del proyecto;
- funcionalidades;
- arquitectura;
- infraestructura cloud;
- stack tecnológico;
- seguridad e IAM;
- realtime;
- calidad software;
- Docker y deployment;
- instalación local;
- estructura del proyecto;
- documentación técnica;
- estado actual;
- roadmap;
- autoría.

También declara herramientas y prácticas como:

~~~text
Pytest
Ruff
SonarCloud
GitHub Actions
Coverage
~~~

y describe un conjunto amplio de tests automatizados.

El Quick Start utiliza la URL real del consumer y proporciona instrucciones tanto para despliegue Docker como para ejecución local.

Esto introduce un contraste directo con los dos experimentos anteriores, cuyos Quick Starts contenían problemas diferentes de personalización.

---

### 9.4 Baseline estructural

El inventario versionado revela una estructura documental extensa.

Entre otros artefactos aparecen responsabilidades relacionadas con:

~~~text
Architecture
Security
Backend
Realtime
Database
Operations
DevOps
Testing
Product
Engineering Guidelines
Architectural Decisions
Project Status
Project History
~~~

Existen además:

- especificación OpenAPI;
- scripts SQL;
- diagramas de arquitectura;
- diagramas de autenticación;
- diagramas de base de datos;
- diagramas RBAC;
- diagramas realtime;
- informes de CI;
- informes de calidad;
- informes de cobertura.

La estructura incluye también un changelog en:

~~~text
docs/14_STATUS/55_CHANGELOG.md
~~~

Este elemento proporciona un challenge directo al principio:

~~~text
Responsibility
        ≠
Canonical Path
~~~

porque no existe necesariamente un `CHANGELOG.md` en la raíz para que exista evidencia de `DOC-CHANGELOG`.

Sin embargo, la existencia del artefacto tampoco determina por sí sola el estado de la responsabilidad.

---

## 10. Resultados del Experimento #3

### 10.1 Responsabilidades Required

Las responsabilidades README muestran un nivel de cobertura superior al observado en los dos primeros consumers.

| Responsibility | State | Evidence / Rationale |
|---|---|---|
| `README-HERO` | Satisfied | El README identifica y posiciona claramente el proyecto mediante título, descripción inicial y badges. |
| `README-OVERVIEW` | Satisfied | La descripción proporciona propósito y contexto suficiente para comprender el proyecto. |
| `README-FEATURES` | Satisfied | Las principales capacidades están documentadas explícitamente. |
| `README-TECH-STACK` | Satisfied | El stack tecnológico y la infraestructura se describen con amplitud. |
| `README-QUICK-START` | Satisfied | Existen instrucciones concretas de clonación, configuración y ejecución con referencias correctas al consumer. |
| `README-DOCUMENTATION` | Partial | El README identifica la documentación técnica y sus principales áreas, pero la navegación hacia documentos concretos no queda completamente resuelta. |
| `README-FOOTER` | Satisfied | El documento dispone de cierre y autoría suficientes para cubrir la responsabilidad. |
| `DOC-CHANGELOG` | Partial | Existe un changelog técnico real y mantiene `Unreleased`, pero no mantiene todavía el historial de releases versionadas y fechadas requerido por la responsabilidad. |

Resultado:

~~~text
Satisfied    6
Partial      2
Missing      0
~~~

Este resultado corrige una posible interpretación puramente estructural:

~~~text
docs/14_STATUS/55_CHANGELOG.md exists
        ↓
DOC-CHANGELOG = Satisfied
~~~

no es una inferencia válida.

La evaluación semántica del contenido modifica el resultado.

---

### 10.2 Challenge de `DOC-CHANGELOG`

`DOC-CHANGELOG` constituye uno de los resultados metodológicos más claros del experimento.

La detección estructural puede establecer:

~~~text
Detected Fact

docs/14_STATUS/55_CHANGELOG.md exists
~~~

La lectura del documento añade evidencia semántica:

~~~text
Evidence

- declara explícitamente propósito de changelog;
- registra evolución técnica;
- utiliza categorías de cambios;
- adopta una sección [Unreleased];
- se inspira en Keep a Changelog;
- referencia Semantic Versioning.
~~~

Sin embargo, la responsabilidad definida por el Framework exige mantener un historial comprensible de cambios publicados y distinguir `Unreleased` de releases identificadas.

El artefacto observado no mantiene todavía esa secuencia de releases versionadas y fechadas.

Por tanto:

~~~text
Detected Artifact
        ↓
Semantic Evidence
        ↓
Evaluation
        ↓
DOC-CHANGELOG = Partial
~~~

Este caso demuestra simultáneamente dos propiedades:

~~~text
Non-canonical path
        ≠
Missing responsibility
~~~

y:

~~~text
Matching artifact name
        ≠
Satisfied responsibility
~~~

La evaluación por responsabilidad necesita por tanto algo más que path matching o detección nominal.

---

### 10.3 `README-DOCUMENTATION` y navegación

El consumer dispone de una cantidad considerable de documentación.

El README identifica áreas como:

~~~text
Architecture
Security IAM
Docker
Cloud Deployment
Realtime
Testing
Data Model
Architectural Decisions
SAML
~~~

y existe evidencia estructural de documentos correspondientes.

Sin embargo:

~~~text
Documentation Exists
        ≠
Documentation Navigation Satisfied
~~~

La responsabilidad `README-DOCUMENTATION` no consiste únicamente en que el repositorio contenga documentación extensa.

También debe proporcionar acceso útil hacia ella desde el README.

Por ello, la responsabilidad se mantiene como `Partial`.

Este resultado refuerza nuevamente la diferencia entre existencia de artefactos y satisfacción de una responsabilidad.

---

### 10.4 Responsabilidades Recommended

El consumer proporciona evidencia abundante para las siete responsabilidades Recommended de `TPL-BACKEND`.

Se identifican implementaciones relacionadas con:

~~~text
README-STATUS

README-ARCHITECTURE

README-REPOSITORY-STRUCTURE

README-TESTING

DOC-ARCHITECTURE

DOC-PROJECT-STATUS

DOC-TESTING
~~~

La evidencia aparece en diferentes niveles.

Parte está integrada directamente en el README.

Otra parte se encuentra distribuida entre documentos especializados, código, tests y artefactos auxiliares.

Esto permite observar una propiedad importante:

~~~text
Responsibility State
        ≠
Implementation Shape
~~~

Una responsabilidad puede estar semánticamente cubierta sin reproducir la implementación canónica del Framework.

No obstante, durante Discovery la existencia de un documento con un nombre relacionado no se utiliza por sí sola para declarar automáticamente `Satisfied`.

El assessment debe considerar su contenido y su relación con la responsabilidad.

---

### 10.5 Responsabilidades Optional

El tercer consumer introduce mucha más evidencia para responsabilidades Optional que los dos anteriores.

El inventario permite detectar artefactos relacionados con:

~~~text
README-ROADMAP
README-AUTHOR
README-HIGHLIGHTS

DOC-ADR
DOC-API
DOC-DATABASE
DOC-DEPLOYMENT
DOC-SECURITY
DOC-DIAGRAMS
~~~

Entre las evidencias estructurales aparecen:

~~~text
docs/13_DECISIONS/52_ARCHITECTURAL_DECISIONS.md

docs/03_BACKEND/12_API_ROUTES.md
docs/assets/openapi.json

docs/06_DATABASE/
docs/assets/*.sql

docs/08_OPERATIONS/35_DEPLOYMENT.md

docs/01_ARCHITECTURE/07_SECURITY_ARCHITECTURE.md
docs/02_SECURITY/

docs/diagrams/
~~~

El experimento muestra que varias responsabilidades pueden estar implementadas mediante conjuntos de artefactos y no mediante una única correspondencia:

~~~text
Responsibility
        ↓
Multiple Evidence Artifacts
~~~

No obstante, detectar estos artefactos no convierte automáticamente todas esas responsabilidades en `Satisfied`.

Cuando el estado dependa del contenido semántico, la evidencia deberá evaluarse antes de cerrar el assessment.

---

### 10.6 Implementaciones distribuidas

Aula Robótica introduce con mucha mayor claridad el concepto de implementación distribuida.

Por ejemplo, una responsabilidad relacionada con seguridad puede disponer de evidencia en:

~~~text
README
+
Architecture Documentation
+
Security Documentation
+
Authentication Documentation
+
RBAC Documentation
+
Runtime Configuration
~~~

Del mismo modo, testing puede estar representado mediante:

~~~text
README
+
Testing Status
+
Testing Strategy
+
Test Suite
+
Coverage Evidence
+
CI
~~~

Esto cuestiona la interpretación de `Implementation Form` como un único valor mutuamente excluyente.

Una implementación podría ser simultáneamente:

~~~text
Own
+
Specialized
+
Distributed
~~~

Por tanto, el experimento sugiere hablar provisionalmente de:

~~~text
Implementation Characteristics
~~~

en lugar de:

~~~text
Implementation Form
~~~

como una enumeración exclusiva.

El experimento no proporciona todavía evidencia suficiente para definir una taxonomía cerrada de esas características.

---

### 10.7 Applicability continúa siendo independiente

El consumer implementa una API real, persistencia, deployment, seguridad y numerosos diagramas.

Responsabilidades como:

~~~text
DOC-API
DOC-DATABASE
DOC-DEPLOYMENT
DOC-SECURITY
DOC-DIAGRAMS
~~~

son claramente relevantes para el contexto del proyecto.

Esto contrasta nuevamente con consumers donde alguna de estas responsabilidades podía no resultar aplicable.

Por tanto:

~~~text
Applicability
        ≠
Requirement Level
        ≠
State
~~~

El Template establece el nivel de requisito.

El consumer aporta el contexto necesario para evaluar aplicabilidad y estado.

---

### 10.8 El modelo de estados sobrevive

A pesar de la mayor complejidad documental del consumer, no aparece un caso que requiera necesariamente un cuarto estado fundamental.

Las situaciones observadas continúan pudiendo expresarse mediante:

~~~text
Satisfied

Partial

Missing
~~~

combinadas con dimensiones adicionales.

Por ejemplo:

~~~text
State
    Satisfied

Implementation Characteristics
    Own
    Specialized
    Distributed
~~~

o:

~~~text
State
    Missing

Requirement Level
    Optional

Applicability
    Uncertain
~~~

Esto refuerza la hipótesis de que conceptos como:

~~~text
Equivalent
Distributed
Not Applicable
Uncertain
Omissible
~~~

no deberían mezclarse dentro de una única taxonomía de estados.

---

### 10.9 El modelo de decisiones también sobrevive

El tercer consumer tampoco demuestra la necesidad de introducir una nueva acción fundamental.

Las decisiones provisionales continúan pudiendo expresarse mediante:

~~~text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
~~~

Sin embargo, el experimento permite precisar una distinción importante.

`PRESERVE` y `ACCEPT` pueden conducir ambos a no modificar el consumer, pero representan razonamientos diferentes.

~~~text
PRESERVE

La implementación existente satisface directamente
la responsabilidad y puede conservarse.
~~~

frente a:

~~~text
ACCEPT

La implementación existente no reproduce necesariamente
la forma canónica, pero se reconoce como equivalente,
especializada o distribuida y válida para la responsabilidad.
~~~

Esta distinción se mantiene provisional durante Discovery.

---

### 10.10 Contraste con las preguntas derivadas del Experimento #1

#### Representación de consumers diferentes

**Evidencia que refuerza el modelo.**

El modelo permite representar un backend Python/FastAPI con una estructura documental considerablemente más extensa sin introducir nuevos estados o acciones fundamentales.

El tercer consumer amplía además la diversidad tecnológica y documental respecto a los dos anteriores.

#### Separación entre estado, implementación, evidencia y decisión

**Evidencia que refuerza y refina significativamente la separación.**

`DOC-CHANGELOG` demuestra que detección estructural y evaluación semántica pueden producir niveles de conocimiento diferentes.

Las responsabilidades distribuidas muestran además que las características de implementación no parecen constituir una dimensión necesariamente exclusiva.

Por tanto, la evidencia favorece mantener separados:

~~~text
Detected Fact
Evidence
Evaluation
State
Implementation Characteristics
Adoption Decision
Rationale
~~~

sin asumir todavía que todos estos conceptos deban convertirse en elementos normativos del Framework.

#### Requirement Level, applicability y contexto

**Evidencia que refuerza la separación de dimensiones.**

La presencia real de API, database, deployment, security y diagrams muestra que la applicability depende del contexto del consumer y debe permanecer conceptualmente separada tanto del estado como del requirement level.

---

### 10.11 Challenge al modelo refinado

El consumer no introduce:

~~~text
New Fundamental State
    NO

New Fundamental Adoption Action
    NO

New Fundamental Process Stage
    NO
~~~

pero sí introduce un refinamiento significativo:

~~~text
Implementation Form
        ↓
Implementation Characteristics
~~~

La razón es que las propiedades observadas no parecen ser necesariamente mutuamente excluyentes.

También refuerza la cadena:

~~~text
Detected Fact
        ↓
Evidence
        ↓
Evaluation
        ↓
State + Qualifiers
        ↓
Adoption Decision
        ↓
Rationale
~~~

El caso `DOC-CHANGELOG` demuestra especialmente por qué no deben omitirse las etapas intermedias.

---

### 10.12 Interpretación del challenge

La interpretación retrospectiva del tercer experimento es:

~~~text
REFINEMENT NEEDED
~~~

El consumer no proporciona una contradicción fundamental de los conceptos utilizados para representar Existing Repository Adoption.

En particular, no aparece evidencia que obligue a introducir:

~~~text
New Fundamental State
    NO

New Fundamental Adoption Action
    NO

New Fundamental Process Stage
    NO
~~~

Sin embargo, la evidencia obliga a refinar la representación de las implementaciones:

~~~text
single Implementation Form
        ↓
potentially multiple Implementation Characteristics
~~~

y refuerza que la evaluación semántica debe permanecer explícitamente separada de la detección estructural.

El resultado no demuestra que el modelo sea universal.

Demuestra únicamente que, frente a tres consumers backend tecnológicamente y documentalmente diferentes, los fundamentos utilizados han continuado siendo útiles mientras algunas dimensiones han necesitado mayor precisión.

La categoría `REFINEMENT NEEDED` se utiliza como instrumento retrospectivo para describir ese resultado y no como criterio de aceptación establecido antes del experimento.

Este nivel de evidencia permite avanzar hacia una consolidación provisional del modelo, pero no hacia una especificación normativa del Framework.

---

## 11. Comparación de los tres consumers

### 11.1 Contextos comparados

Los tres experimentos mantuvieron constantes:

~~~text
Repository Template
    TPL-BACKEND v0.1.0

Adoption Mode
    Existing Repository Adoption
~~~

mientras cambiaron deliberadamente el consumer.

| Experiment | Consumer | Main Technology | Documentation Profile |
|---|---|---|---|
| #1 | Only Film | Java / Spring Boot | README desarrollado y documentación complementaria |
| #2 | dental-back | TypeScript / NestJS | Documentación concentrada principalmente en README |
| #3 | aula-robotica-platform | Python / FastAPI | Documentación extensa, especializada y distribuida |

Esta diversidad permite comparar el comportamiento del modelo frente a distintas tecnologías y formas de documentar un backend.

No pretende constituir una muestra estadísticamente representativa de repositorios software.

Su función es someter el modelo emergente a escenarios progresivamente diferentes.

---

### 11.2 Comparación de responsabilidades Required

Los tres consumers muestran resultados diferentes pese a utilizar el mismo Repository Template.

| Responsibility | Only Film | dental-back | aula-robotica-platform |
|---|---|---|---|
| `README-HERO` | Satisfied | Satisfied | Satisfied |
| `README-OVERVIEW` | Satisfied | Satisfied | Satisfied |
| `README-FEATURES` | Satisfied | Satisfied | Satisfied |
| `README-TECH-STACK` | Satisfied | Satisfied | Satisfied |
| `README-QUICK-START` | Partial | Partial | Satisfied |
| `README-DOCUMENTATION` | Partial | Partial | Partial |
| `README-FOOTER` | Satisfied | Satisfied | Satisfied |
| `DOC-CHANGELOG` | Missing | Missing | Partial |

Resumen:

~~~text
Only Film
    Satisfied    5
    Partial      2
    Missing      1

dental-back
    Satisfied    5
    Partial      2
    Missing      1

aula-robotica-platform
    Satisfied    6
    Partial      2
    Missing      0
~~~

Los valores agregados son útiles para describir el assessment, pero no contienen información suficiente para explicar las diferencias entre consumers.

En particular:

~~~text
same counts
    ≠
same adoption situation
~~~

Only Film y `dental-back` presentan la misma distribución cuantitativa Required, pero las razones concretas de algunos estados son diferentes.

---

### 11.3 Tres comportamientos diferentes de Quick Start

`README-QUICK-START` proporciona una comparación especialmente útil.

~~~text
Only Film
    section exists
    inherited repository reference
        ↓
    Partial

dental-back
    section exists
    generic repository placeholder
        ↓
    Partial

aula-robotica-platform
    section exists
    consumer-specific clone/config/run instructions
        ↓
    Satisfied
~~~

Los dos primeros consumers comparten estado, pero no evidencia ni causa.

El tercero demuestra que la responsabilidad puede satisfacerse sin introducir una nueva forma de modelarla.

Esto refuerza:

~~~text
State alone
    ≠
Complete Assessment
~~~

---

### 11.4 Tres comportamientos documentales

Los consumers muestran también tres estrategias diferentes de materialización documental.

#### Only Film

Combina README y documentación adicional, con determinadas responsabilidades implementadas mediante contenido propio o equivalente.

#### dental-back

Concentra una parte considerable del conocimiento técnico en el README y utiliza pocos artefactos documentales independientes.

#### aula-robotica-platform

Distribuye el conocimiento entre README, documentos especializados, diagramas, especificaciones, tests, configuración y evidencias de calidad.

Por tanto:

~~~text
same Template
        ↓
different valid repository shapes
~~~

El Framework no puede asumir una única topología documental para determinar si una responsabilidad está satisfecha.

---

### 11.5 El caso comparativo de `DOC-CHANGELOG`

`DOC-CHANGELOG` proporciona otra comparación significativa.

~~~text
Only Film
    no sufficient changelog evidence identified
        ↓
    Missing

dental-back
    no sufficient changelog evidence identified
        ↓
    Missing

aula-robotica-platform
    changelog artifact exists
    real change information exists
    Unreleased exists
    published release history incomplete
        ↓
    Partial
~~~

Este contraste demuestra dos límites diferentes.

Primero:

~~~text
canonical root file absent
        ≠
responsibility necessarily Missing
~~~

Segundo:

~~~text
artifact named CHANGELOG present
        ≠
responsibility necessarily Satisfied
~~~

La ubicación y el nombre proporcionan evidencia estructural.

El estado requiere evaluación semántica.

---

### 11.6 Diferencias de Applicability

Los tres consumers muestran que algunas responsabilidades no pueden interpretarse únicamente a partir del Repository Template.

Un caso claro es `DOC-API`.

~~~text
Only Film
    API described as future possibility
        ↓
    applicability differs

dental-back
    actual API + Swagger
        ↓
    applicable

aula-robotica-platform
    actual API + API documentation + OpenAPI artifact
        ↓
    applicable
~~~

La misma responsabilidad Optional puede tener relevancia distinta según el consumer.

Esto confirma que:

~~~text
Requirement Level
        ≠
Applicability
~~~

y también:

~~~text
Applicability
        ≠
State
~~~

---

### 11.7 Diferencias en la forma de implementación

Los primeros experimentos permitían describir algunas implementaciones mediante términos como:

~~~text
Own
Equivalent
Specialized
Distributed
~~~

El tercer consumer muestra con mayor claridad que estos términos no parecen formar necesariamente una enumeración exclusiva.

Por ejemplo, una implementación documental puede ser simultáneamente:

~~~text
Own
+
Specialized
+
Distributed
~~~

Por tanto, la comparación de consumers sugiere abandonar provisionalmente la idea de:

~~~text
Implementation Form
    one value
~~~

en favor de:

~~~text
Implementation Characteristics
    zero or more relevant characteristics
~~~

La estructura interna de esas características permanece abierta.

---

### 11.8 Lo que no cambió entre experiments

Pese a las diferencias entre consumers, determinados elementos sobrevivieron a los tres experimentos.

No fue necesario introducir un nuevo:

~~~text
Fundamental Responsibility State

Fundamental Adoption Action

Fundamental Analysis Unit
~~~

La unidad de assessment continuó siendo:

~~~text
Responsibility
~~~

Los estados fundamentales continuaron siendo:

~~~text
Satisfied
Partial
Missing
~~~

y las decisiones identificadas continuaron pudiendo expresarse mediante:

~~~text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
~~~

Esto no demuestra que estas taxonomías sean universales.

Sí proporciona evidencia suficiente para conservarlas en el modelo provisional.

---

## 12. Findings consolidados

### F-01 — Existing Repository Adoption es un problema de reconciliación

Los tres experimentos refuerzan que adoptar un Repository Template sobre un repositorio existente no consiste principalmente en crear una estructura nueva.

El problema observado es:

~~~text
Existing Repository
        +
Repository Template
        ↓
Reconciliation
~~~

El consumer ya contiene decisiones, documentación, código y estructuras que deben comprenderse antes de proponer cambios.

---

### F-02 — La responsabilidad es la unidad de assessment

Ninguno de los experimentos requirió utilizar el archivo como unidad fundamental.

Por el contrario, múltiples observaciones muestran que:

~~~text
Responsibility
        ≠
File
~~~

Una responsabilidad puede:

- estar implementada en un archivo no canónico;
- estar integrada dentro del README;
- utilizar un formato diferente;
- estar distribuida entre varios artefactos.

Por tanto, filename matching puede proporcionar evidencia, pero no constituye por sí mismo un assessment.

---

### F-03 — Detección estructural y evaluación semántica son diferentes

Los experimentos muestran repetidamente:

~~~text
Detected Fact
        ≠
Evaluated State
~~~

Ejemplos:

~~~text
Quick Start section exists
        ≠
README-QUICK-START Satisfied

CHANGELOG artifact exists
        ≠
DOC-CHANGELOG Satisfied

testing files exist
        ≠
DOC-TESTING Satisfied

docs directory exists
        ≠
README-DOCUMENTATION Satisfied
~~~

Esto establece un límite importante para cualquier futura automatización.

---

### F-04 — `State` necesita permanecer separado de la evidencia

Only Film y `dental-back` muestran que:

~~~text
same State
        ≠
same Reason
~~~

Ambos pueden presentar:

~~~text
README-QUICK-START = Partial
~~~

por razones diferentes.

Por tanto, almacenar únicamente el estado elimina información necesaria para comprender y revisar el assessment.

---

### F-05 — `State` y `Adoption Decision` son conceptos diferentes

Los experimentos continúan apoyando:

~~~text
Responsibility State
        ≠
Adoption Action
~~~

El estado describe el consumer.

La decisión expresa qué hacer respecto a la adopción.

La evaluación debe poder existir antes de tomar una decisión.

---

### F-06 — `Applicability` constituye una dimensión independiente

La comparación entre consumers demuestra que la aplicabilidad de determinadas responsabilidades depende del contexto.

Por tanto:

~~~text
State
Requirement Level
Applicability
~~~

representan preguntas diferentes.

Una responsabilidad puede ser:

~~~text
Missing
+
Optional
+
Not Applicable
~~~

sin representar necesariamente un gap que deba corregirse.

---

### F-07 — Las implementaciones no canónicas pueden ser válidas

Los experimentos proporcionan evidencia de responsabilidades materializadas mediante implementaciones:

- propias;
- equivalentes;
- especializadas;
- distribuidas;
- integradas en otros artefactos.

Por tanto:

~~~text
Canonical Implementation absent
        ≠
Responsibility Missing
~~~

La equivalencia debe evaluarse semánticamente.

---

### F-08 — Las características de implementación pueden coexistir

El tercer consumer muestra que términos como:

~~~text
Own
Specialized
Distributed
~~~

pueden describir simultáneamente una misma implementación.

Esto cuestiona una taxonomía basada en una única `Implementation Form`.

El concepto provisional pasa a ser:

~~~text
Implementation Characteristics
~~~

sin definir todavía una estructura normativa cerrada.

---

### F-09 — La trazabilidad forma parte del problema de adopción

Para comprender una decisión no basta con registrar:

~~~text
Responsibility
State
Action
~~~

Los experimentos muestran la necesidad de preservar una cadena similar a:

~~~text
Evidence
    ↓
Evaluation
    ↓
State + Qualifiers
    ↓
Adoption Decision
    ↓
Rationale
~~~

Esta trazabilidad permite revisar posteriormente por qué se tomó una decisión.

---

### F-10 — `PRESERVE` y `ACCEPT` representan decisiones diferentes

Ambas decisiones pueden producir:

~~~text
no repository modification
~~~

pero expresan razones distintas.

`PRESERVE` describe una implementación existente que satisface directamente la responsabilidad.

`ACCEPT` permite reconocer explícitamente una implementación válida que no reproduce necesariamente la forma canónica y puede ser equivalente, especializada o distribuida.

La diferencia pertenece al razonamiento de adopción, no al estado físico del repositorio.

---

### F-11 — La ausencia Optional no debe convertirse automáticamente en trabajo

Los experimentos muestran que:

~~~text
Optional + Missing
        ≠
ADD
~~~

La decisión puede requerir primero:

~~~text
EVALUATE
~~~

y producir posteriormente:

~~~text
ADD
~~~

o:

~~~text
OMIT
~~~

según applicability y contexto.

El mismo principio resulta relevante para responsabilidades Recommended cuando una omisión pueda estar justificada.

---

### F-12 — Analysis y Application deben permanecer separados

Los tres experimentos se realizaron sin modificar los consumers.

Esto permitió evaluar el repositorio antes de decidir cambios.

La separación:

~~~text
ANALYZE / ASSESS
        ≠
APPLY
~~~

continúa siendo necesaria para evitar que una futura herramienta transforme observaciones incompletas en modificaciones automáticas.

---

### F-13 — La automatización segura comienza por evidencia, no por cambios

Los casos observados permiten automatizar potencialmente determinados hechos:

~~~text
file exists
section detected
workflow exists
test suite exists
OpenAPI artifact exists
~~~

pero no justifican automáticamente automatizar:

~~~text
semantic equivalence
applicability
adoption decision
repository modification
~~~

Por tanto, una dirección prudente sería:

~~~text
Automate Evidence
        before
Automating Decisions
~~~

Esta conclusión define una frontera de automatización, no una decisión sobre una herramienta concreta.

---

### F-14 — External Adoption también valida el Framework

Los consumers no solo son objetos de assessment.

También revelan propiedades y limitaciones del propio Framework.

Durante los experimentos se han refinado:

- la separación entre estado y razón;
- la independencia de applicability;
- el papel de la evidencia;
- la interpretación de implementaciones distribuidas;
- la diferencia entre detección estructural y satisfacción semántica.

Por tanto:

~~~text
Consumer Adoption
        ↓
Framework Learning
~~~

La adopción externa constituye también un mecanismo de validación del diseño del Framework.

---

### F-15 — Tres experiments permiten consolidación provisional, no universalidad

Ninguno de los tres consumers ha producido una contradicción fundamental del modelo.

Sin embargo:

~~~text
3 consumers
        ≠
universal validation
~~~

Los experimentos están concentrados en:

~~~text
TPL-BACKEND
+
Existing Repository Adoption
~~~

No proporcionan evidencia equivalente sobre:

- otros Repository Templates;
- repository initialization;
- automatic application;
- rollback;
- otros dominios de proyecto;
- todos los posibles estilos documentales.

Por tanto, los findings pueden consolidarse como base provisional para continuar Discovery, pero no deben promoverse automáticamente a reglas universales del Framework.

---

## 13. Evolución de los Requirement Candidates

El primer experimento produjo quince Requirement Candidates.

No representan funcionalidades comprometidas.

Representan necesidades candidatas derivadas de observaciones de Discovery y sometidas posteriormente a contraste mediante consumers adicionales.

Los Experimentos #2 y #3 permiten revisar su evolución.

---

### 13.1 RC-01 — Analyze existing consumer against Template

**Estado tras los experimentos: Reinforced**

La adopción necesita comenzar comprendiendo el estado existente del consumer frente a las responsabilidades del Repository Template.

Los tres consumers muestran configuraciones diferentes pese a utilizar el mismo Template.

Por tanto, el proceso necesita producir primero una representación del consumer antes de considerar modificaciones.

~~~text
Consumer
    +
Repository Template
        ↓
Assessment
~~~

El análisis no puede asumir que el repositorio comienza vacío.

---

### 13.2 RC-02 — Distinguish responsibility state

**Estado tras los experimentos: Reinforced + Refined**

Los estados provisionales:

~~~text
Satisfied
Partial
Missing
~~~

han resultado suficientes para los tres consumers.

Sin embargo, los experimentos demuestran que el estado no debe absorber otras dimensiones.

En particular:

~~~text
Equivalent
Specialized
Distributed
Not Applicable
Uncertain
~~~

no describen el mismo concepto que:

~~~text
Satisfied
Partial
Missing
~~~

El candidate se refina por tanto hacia una separación explícita entre `State` y sus posibles qualifiers.

---

### 13.3 RC-03 — Separate state and adoption action

**Estado tras los experimentos: Reinforced**

Ningún experimento ha requerido fusionar ambos conceptos.

El assessment responde:

~~~text
What exists and to what extent
does it satisfy the responsibility?
~~~

La decisión responde:

~~~text
What should be done about it
during adoption?
~~~

Por tanto:

~~~text
State
    ≠
Action
~~~

continúa siendo una separación fundamental.

---

### 13.4 RC-04 — Preserve valid existing implementations

**Estado tras los experimentos: Reinforced**

Los tres consumers contienen implementaciones que no necesitan ser sustituidas para adoptar el Framework.

La adopción debe poder producir:

~~~text
PRESERVE
~~~

cuando una implementación existente satisface directamente la responsabilidad.

Esto evita que adopción se interprete como regeneración del repositorio.

---

### 13.5 RC-05 — Adapt existing content without unnecessary replacement

**Estado tras los experimentos: Reinforced**

Los casos `README-QUICK-START` de Only Film y `dental-back` muestran responsabilidades parcialmente satisfechas donde existe una base útil.

El problema no requiere necesariamente reemplazar el contenido.

Puede requerir:

~~~text
ADAPT
~~~

sobre la implementación existente.

Por tanto:

~~~text
Partial
        ≠
Replace
~~~

---

### 13.6 RC-06 — Recognize equivalent, specialized and distributed implementations

**Estado tras los experimentos: Strongly Reinforced + Refined**

Los tres consumers muestran implementaciones no necesariamente canónicas.

Aula Robótica añade un refinamiento importante: las características observadas pueden coexistir.

Una implementación puede ser simultáneamente:

~~~text
Own
+
Specialized
+
Distributed
~~~

Por ello, el candidate deja de sugerir implícitamente una única `Implementation Form`.

La necesidad emergente es reconocer:

~~~text
Implementation Characteristics
~~~

potencialmente múltiples y no necesariamente exclusivas.

La taxonomía concreta permanece abierta.

---

### 13.7 RC-07 — Consider requirement level and applicability

**Estado tras los experimentos: Strongly Reinforced**

Los experimentos muestran que:

~~~text
Required
Recommended
Optional
~~~

no determinan por sí solos la decisión.

También debe considerarse:

~~~text
Applicability
~~~

El contraste de `DOC-API` entre consumers proporciona evidencia especialmente clara.

Por tanto:

~~~text
State
+
Requirement Level
+
Applicability
+
Context
~~~

participan en el razonamiento de adopción.

---

### 13.8 RC-08 — Allow justified omissions

**Estado tras los experimentos: Reinforced**

La ausencia de una responsabilidad Recommended u Optional no implica automáticamente que deba implementarse.

El modelo necesita poder representar una decisión explícita de no incorporación cuando exista una razón válida.

Las decisiones relacionadas continúan siendo:

~~~text
JUSTIFY
OMIT
~~~

La omisión debe ser una decisión trazable, no una ausencia accidental interpretada retrospectivamente.

---

### 13.9 RC-09 — Trace evidence, evaluation and decision

**Estado tras los experimentos: Strongly Reinforced + Refined**

Este candidate recibe uno de los mayores refuerzos.

Only Film y `dental-back` muestran que el mismo estado puede tener causas diferentes.

Aula Robótica muestra que incluso un artefacto nominalmente coincidente con una responsabilidad puede requerir evaluación semántica antes de determinar el estado.

La trazabilidad provisional evoluciona desde:

~~~text
Evidence
    ↓
State
    ↓
Decision
~~~

hacia:

~~~text
Detected Fact
        ↓
Evidence
        ↓
Evaluation
        ↓
State + Qualifiers
        ↓
Adoption Decision
        ↓
Rationale
~~~

Esta cadena representa conocimiento progresivo, no necesariamente una estructura física de datos definitiva.

---

### 13.10 RC-10 — Separate analysis and application

**Estado tras los experimentos: Reinforced**

Los tres experimentos pudieron realizarse sin modificar los consumers.

Esto demuestra que el assessment tiene valor independiente de la aplicación.

La separación continúa siendo:

~~~text
Understand
    before
Modify
~~~

y:

~~~text
Analysis
    ≠
Application
~~~

La investigación no proporciona todavía evidencia suficiente para definir cómo debería implementarse la fase de aplicación.

---

### 13.11 RC-11 — Distinguish deterministic detection from semantic evaluation

**Estado tras los experimentos: Strongly Reinforced**

Este candidate aparece repetidamente.

Pueden detectarse de forma determinista hechos como:

~~~text
file exists
directory exists
section exists
workflow exists
tests exist
OpenAPI artifact exists
~~~

pero esos hechos no determinan necesariamente:

~~~text
responsibility satisfied
implementation equivalent
responsibility applicable
adoption action
~~~

El caso `DOC-CHANGELOG` de Aula Robótica proporciona la evidencia más clara:

~~~text
CHANGELOG artifact detected
        ↓
semantic evaluation
        ↓
Partial
~~~

Por tanto, cualquier futura automatización deberá preservar esta frontera.

---

### 13.12 RC-12 — Represent uncertainty and need for evaluation

**Estado tras los experimentos: Reinforced + Refined**

Durante los assessments aparecen situaciones donde la evidencia estructural no permite concluir inmediatamente:

- applicability;
- equivalence;
- completeness;
- necesidad de adopción.

La incertidumbre no debe resolverse inventando certeza.

El modelo necesita poder expresar:

~~~text
Uncertain
Needs Evaluation
Insufficient Evidence
~~~

cuando corresponda.

Sin embargo, los experimentos sugieren que estos conceptos no deberían convertirse automáticamente en nuevos `Responsibility States`.

Pueden pertenecer a dimensiones diferentes del assessment.

---

### 13.13 RC-13 — Avoid destructive modifications by default

**Estado tras los experimentos: Supported but not directly validated**

Los experimentos refuerzan conceptualmente la necesidad de preservar implementaciones válidas y adaptar antes que reemplazar.

Sin embargo, ninguno de los tres experiments ejecutó modificaciones sobre los consumers.

Por tanto, no existe evidencia suficiente para afirmar que un mecanismo concreto de aplicación sea seguro.

El candidate permanece válido como necesidad, pero requiere investigación específica durante una futura fase de aplicación.

---

### 13.14 RC-14 — Keep Initialization and Existing Repository Adoption distinguishable

**Estado tras los experimentos: Supported but only partially tested**

Los tres experimentos trabajan exclusivamente con:

~~~text
Existing Repository Adoption
~~~

y muestran que este escenario requiere reconciliar un estado previo.

Esto apoya conceptualmente su separación respecto a:

~~~text
Repository Initialization
~~~

donde no existe necesariamente una implementación previa que preservar, aceptar o adaptar.

Sin embargo, `Initialization` no ha sido probado experimentalmente durante esta investigación.

Por tanto, el candidate permanece abierto a validación adicional.

---

### 13.15 RC-15 — Use external adoption as Template validation

**Estado tras los experimentos: Strongly Reinforced**

Los consumers han revelado propiedades que no resultaban evidentes mediante el diseño declarativo o el dogfooding aislado.

Entre ellas:

- necesidad de separar estado y razón;
- independencia de applicability;
- implementaciones distribuidas;
- coexistencia de características de implementación;
- límites del filename matching;
- límites de la detección estructural;
- necesidad de trazabilidad.

Por tanto:

~~~text
Apply Template to Consumer
        ↓
Observe Friction
        ↓
Learn about Framework
~~~

La adopción constituye también un mecanismo de validación del propio Template y de los conceptos del Framework.

---

## 14. Consolidación de necesidades

Los quince Requirement Candidates pueden agruparse provisionalmente en cinco áreas de necesidad.

Esta agrupación no sustituye a los candidates originales.

Su objetivo es reducir duplicación conceptual y mostrar qué responsabilidades mayores emergen de los experimentos.

---

### 14.1 Responsibility Assessment

Incluye principalmente:

~~~text
RC-02
RC-06
RC-07
RC-11
RC-12
~~~

Pregunta central:

> ¿Cómo puede el Framework comprender correctamente el estado de una responsabilidad dentro de un consumer?

Esta área necesita representar:

- estado;
- applicability;
- características de implementación;
- evidencia;
- incertidumbre;
- diferencia entre detección estructural y evaluación semántica.

Puede resumirse provisionalmente como:

~~~text
Detected Facts
        ↓
Evidence
        ↓
Evaluation
        ↓
Responsibility Assessment
~~~

---

### 14.2 Adoption Analysis

Incluye principalmente:

~~~text
RC-01
RC-03
RC-09
RC-10
~~~

Pregunta central:

> ¿Cómo puede el Framework comparar un consumer existente con un Repository Template sin modificar todavía el repositorio?

Esta área necesita:

- analizar el consumer;
- comparar responsabilidades;
- separar estado y acción;
- conservar trazabilidad;
- mantener analysis separado de application.

Puede resumirse como:

~~~text
Consumer
    +
Repository Template
        ↓
Adoption Analysis
~~~

---

### 14.3 Adoption Decision

Incluye principalmente:

~~~text
RC-04
RC-05
RC-08
~~~

Pregunta central:

> ¿Cómo se representa explícitamente qué debe hacerse con cada responsabilidad durante la adopción?

Las decisiones provisionales continúan siendo:

~~~text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
~~~

La decisión deberá considerar el assessment y el contexto sin quedar implícita en ellos.

---

### 14.4 Safe Application

Incluye principalmente:

~~~text
RC-13
RC-14
~~~

Pregunta central:

> ¿Cómo podrían aplicarse posteriormente decisiones de adopción sin destruir implementaciones válidas ni confundir adopción con inicialización?

Esta área permanece deliberadamente menos validada.

Los experimentos actuales proporcionan evidencia sobre analysis y decision, pero no sobre ejecución de cambios.

Por tanto:

~~~text
Safe Application
    remains
Future Discovery
~~~

No deberá seleccionarse todavía un mecanismo de generación, patching, CLI o modificación automática.

---

### 14.5 Framework Learning

Incluye principalmente:

~~~text
RC-15
~~~

Pregunta central:

> ¿Cómo puede la experiencia de adopción de consumers reales mejorar el propio Framework?

La adopción externa puede revelar:

- responsabilidades mal definidas;
- requirement levels discutibles;
- supuestos canónicos demasiado rígidos;
- Components insuficientemente reutilizables;
- gaps entre Template y realidad;
- oportunidades de mejorar Standards y Components.

Puede expresarse como un feedback loop:

~~~text
Framework
    ↓
Consumer Adoption
    ↓
Observed Evidence
    ↓
Framework Learning
    ↓
Framework Refinement
~~~

---

## 15. Modelo conceptual emergente

Los findings y Requirement Candidates permiten expresar provisionalmente el problema de adopción mediante varias capas.

### 15.1 Repository Template

Define:

~~~text
Responsibilities
+
Requirement Levels
~~~

No determina por sí solo el estado real del consumer.

---

### 15.2 Consumer Evidence

El repositorio proporciona hechos observables:

~~~text
Files
Sections
Documentation
Code
Tests
Workflows
Diagrams
Specifications
Configuration
Other Artifacts
~~~

Estos elementos constituyen fuentes potenciales de evidencia.

---

### 15.3 Responsibility Assessment

La evidencia se interpreta frente a una responsabilidad.

El assessment puede necesitar representar:

~~~text
State
+
Applicability
+
Implementation Characteristics
+
Evidence
+
Evaluation Rationale
+
Uncertainty
~~~

No todas estas dimensiones están necesariamente presentes en todos los casos.

---

### 15.4 Adoption Decision

A partir del assessment y del contexto puede producirse una decisión explícita:

~~~text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
~~~

La decisión no modifica todavía el consumer.

---

### 15.5 Adoption Result

Una adopción completa podría producir eventualmente:

~~~text
Repository Changes
+
Explicit Adoption Decisions
~~~

Sin embargo, los experimentos actuales proporcionan evidencia directa sobre el assessment y sobre la representación explícita de decisiones de adopción, no sobre la ejecución de cambios en el repositorio.

La aplicación de cambios permanece fuera del alcance de esta investigación.

---

### 15.6 Representación provisional

El modelo conceptual puede resumirse como:

~~~text
Repository Template
        │
        │ responsibilities
        │ requirement levels
        ↓
Consumer Repository
        │
        │ detected facts
        ↓
Evidence
        │
        ↓
Evaluation
        │
        ↓
Responsibility Assessment
        │
        │ state
        │ applicability
        │ implementation characteristics
        │ uncertainty
        │ rationale
        ↓
Adoption Decision
        │
        ↓
Explicit Adoption Result

        - - - - - - - - - - -

Future / not validated here:

Adoption Decision
        ↓
Apply Changes
        ↓
Verify
~~~

Esta representación no constituye todavía un schema, formato de archivo, API o arquitectura de implementación.

Es únicamente el modelo conceptual mínimo que emerge de la evidencia disponible.

---

## 16. Fórmula provisional de decisión

El primer experimento produjo inicialmente una relación simplificada:

~~~text
STATE
+
REQUIREMENT LEVEL
+
CONTEXT
    ↓
ACTION
~~~

Los experimentos posteriores muestran que esa representación pierde información relevante.

Una formulación provisional más completa es:

~~~text
STATE
+
REQUIREMENT LEVEL
+
APPLICABILITY / CONTEXT
+
IMPLEMENTATION CHARACTERISTICS
+
EVIDENCE / REASON
        ↓
ADOPTION DECISION
~~~

La fórmula no representa un algoritmo.

No implica que cada dimensión pueda evaluarse automáticamente.

Tampoco implica que una combinación determinada de valores produzca siempre una única acción.

Su función es mostrar qué información ha demostrado ser relevante durante los experimentos.

En particular:

~~~text
Missing + Optional
~~~

no permite inferir automáticamente:

~~~text
ADD
~~~

del mismo modo que:

~~~text
Satisfied
~~~

no permite distinguir automáticamente entre:

~~~text
PRESERVE
~~~

y:

~~~text
ACCEPT
~~~

sin comprender la implementación y el razonamiento correspondiente.

---

## 17. Estado de los Requirement Candidates

Tras los tres experimentos:

~~~text
Refuted
    none

Reinforced
    RC-01
    RC-03
    RC-04
    RC-05
    RC-08
    RC-10

Strongly Reinforced
    RC-07
    RC-11
    RC-15

Reinforced + Refined
    RC-02
    RC-12

Strongly Reinforced + Refined
    RC-06
    RC-09

Supported but not directly validated
    RC-13

Supported but only partially tested
    RC-14
~~~

La ausencia de candidates refutados no demuestra que el modelo sea definitivo.

Indica únicamente que ninguno de los tres consumers utilizados ha proporcionado evidencia suficiente para descartar una de estas necesidades.

Los candidates relacionados con aplicación e inicialización presentan además un nivel de validación inferior porque esos escenarios no han sido ejecutados durante los experimentos.

---

## 18. Modelo mínimo útil provisional

### 18.1 Propósito

Los tres experimentos permiten proponer un modelo mínimo capaz de representar los aspectos de Existing Repository Adoption que han demostrado ser relevantes.

Este modelo tiene carácter provisional y pertenece exclusivamente a Discovery.

Su objetivo no es describir todos los posibles escenarios de adopción.

Su objetivo es identificar el conjunto mínimo de conceptos que, según la evidencia disponible, permite:

- analizar un consumer existente;
- compararlo con un Repository Template;
- evaluar responsabilidades;
- conservar la evidencia utilizada;
- representar incertidumbre;
- distinguir implementaciones no canónicas;
- tomar decisiones explícitas de adopción;
- explicar posteriormente esas decisiones.

El modelo no constituye:

- un Standard;
- un schema;
- un formato YAML o JSON;
- una API;
- una estructura de clases;
- un comando CLI;
- una extensión del Framework Validator;
- un formato de manifest;
- una decisión de implementación.

---

### 18.2 Principio fundamental

El modelo se apoya en la separación observada durante los experimentos:

~~~text
Detected Fact
        ≠
Evidence
        ≠
Evaluated State
        ≠
Adoption Decision
        ≠
Applied Change
~~~

Cada elemento representa un nivel diferente de conocimiento o actuación.

Colapsar estos niveles produciría decisiones que no pueden justificarse adecuadamente a partir de la evidencia disponible.

---

## 19. Elementos mínimos del modelo

### 19.1 Template Responsibility

El punto de partida es una responsabilidad incluida en un Repository Template.

La responsabilidad proporciona al menos:

~~~text
Responsibility Identifier

Requirement Level
~~~

Por ejemplo:

~~~text
README-QUICK-START
Required
~~~

o:

~~~text
DOC-API
Optional
~~~

El Repository Template define qué responsabilidades deben considerarse.

No determina su estado dentro del consumer.

---

### 19.2 Detected Facts

Un `Detected Fact` representa una observación verificable sobre el consumer.

Ejemplos:

~~~text
README.md exists

README contains Quick Start section

docs/14_STATUS/55_CHANGELOG.md exists

docs/assets/openapi.json exists

.github/workflows contains workflows

tests directory contains test files
~~~

Un hecho detectado no contiene todavía una conclusión sobre la responsabilidad.

Por tanto:

~~~text
Detected Fact
        ≠
Responsibility Assessment
~~~

---

### 19.3 Evidence

`Evidence` representa información del consumer relevante para evaluar una responsabilidad.

Puede proceder de uno o múltiples artefactos.

Por ejemplo:

~~~text
Responsibility
    DOC-API

Evidence
    README API description
    docs/03_BACKEND/12_API_ROUTES.md
    docs/assets/openapi.json
~~~

La evidencia puede ser:

- estructural;
- textual;
- documental;
- ejecutable;
- configuracional;
- visual;
- distribuida.

El modelo no presupone que una responsabilidad corresponda a un único artefacto.

---

### 19.4 Evaluation

`Evaluation` representa la interpretación de la evidencia frente a la responsabilidad.

Es el punto donde una observación deja de ser únicamente estructural y pasa a compararse con el significado de la responsabilidad.

Ejemplo:

~~~text
Detected Fact
    CHANGELOG artifact exists

Evidence
    Unreleased section
    categorized changes
    technical evolution

Evaluation
    artifact implements changelog semantics
    but does not maintain published
    versioned and dated release history
~~~

La evaluación permite posteriormente determinar el estado.

---

### 19.5 State

`State` representa el grado en que la responsabilidad está satisfecha en el consumer.

La taxonomía provisional mínima es:

~~~text
Satisfied
Partial
Missing
~~~

#### Satisfied

Existe evidencia suficiente para considerar satisfecha la responsabilidad.

#### Partial

Existe una implementación relevante, pero no satisface completamente la responsabilidad.

#### Missing

No se ha identificado una implementación suficiente para satisfacer la responsabilidad.

Estos estados no representan:

- applicability;
- canonicality;
- equivalence;
- uncertainty;
- adoption action.

---

### 19.6 Applicability

`Applicability` representa si una responsabilidad resulta pertinente para el consumer.

La taxonomía provisional es:

~~~text
Applicable
Not Applicable
Uncertain
~~~

Esta dimensión resulta especialmente relevante para responsabilidades Recommended y Optional.

Ejemplo:

~~~text
DOC-API

Consumer A
    no API
    → Not Applicable

Consumer B
    REST API
    → Applicable
~~~

`Applicability` no modifica el significado de `State`.

Ambas dimensiones pueden coexistir durante el assessment.

---

### 19.7 Implementation Characteristics

`Implementation Characteristics` describe propiedades relevantes de la forma en que el consumer materializa una responsabilidad.

Los experimentos han observado características como:

~~~text
Canonical
Own
Equivalent
Specialized
Distributed
~~~

El tercer experimento muestra que estas propiedades no deben asumirse como mutuamente excluyentes.

Por ejemplo:

~~~text
Own
+
Specialized
+
Distributed
~~~

pueden describir simultáneamente una implementación.

El modelo provisional no define todavía una taxonomía normativa de estas características.

Únicamente conserva la necesidad de poder representarlas cuando resulten relevantes para la evaluación o la decisión.

---

### 19.8 Uncertainty

El modelo necesita preservar explícitamente situaciones donde la evidencia disponible no permita una conclusión suficiente.

La incertidumbre puede afectar a:

~~~text
Applicability

Semantic Equivalence

Completeness

Evidence Sufficiency

Adoption Decision
~~~

La incertidumbre no debe resolverse creando certeza artificial.

Tampoco debe convertirse automáticamente en un nuevo `State`.

Puede expresarse provisionalmente mediante conceptos como:

~~~text
Uncertain

Needs Evaluation

Insufficient Evidence
~~~

La representación definitiva permanece abierta.

---

### 19.9 Evaluation Rationale

El assessment necesita conservar por qué se ha asignado determinado estado.

Por ejemplo:

~~~text
Responsibility
    README-QUICK-START

State
    Partial

Rationale
    clone command still references
    inherited repository URL
~~~

frente a:

~~~text
Responsibility
    README-QUICK-START

State
    Partial

Rationale
    clone command contains
    generic repository placeholder
~~~

El mismo estado no implica la misma razón.

Por ello:

~~~text
State
        ≠
Rationale
~~~

---

### 19.10 Adoption Decision

Una vez realizado el assessment puede registrarse una decisión de adopción.

El conjunto provisional continúa siendo:

~~~text
PRESERVE
ADAPT
ADD
ACCEPT
EVALUATE
JUSTIFY
OMIT
~~~

Estas decisiones describen qué hacer respecto a una responsabilidad.

No describen su estado.

---

### 19.11 Decision Rationale

La decisión debe poder explicarse independientemente del assessment.

Ejemplo:

~~~text
State
    Satisfied

Implementation
    Own + Distributed

Decision
    ACCEPT

Rationale
    existing implementation satisfies
    the responsibility through valid
    non-canonical artifacts
~~~

o:

~~~text
State
    Partial

Decision
    ADAPT

Rationale
    existing implementation is useful
    and only requires targeted correction
~~~

Esto permite revisar posteriormente por qué se decidió preservar, adaptar, aceptar, añadir u omitir una implementación.

---

## 20. Unidad mínima de assessment

El modelo provisional puede representar una evaluación mediante la siguiente estructura conceptual:

~~~text
Responsibility Assessment

    Responsibility
    Requirement Level

    Detected Facts
    Evidence

    Evaluation

        State
        Applicability
        Implementation Characteristics
        Uncertainty

    Evaluation Rationale


Adoption Decision

    Decision
    Decision Rationale
~~~

`Responsibility Assessment` y `Adoption Decision` se mantienen conceptualmente separados.

El assessment representa qué se ha observado y cómo se ha evaluado una responsabilidad frente al Repository Template.

La decisión representa qué debería hacerse respecto a esa responsabilidad durante la adopción.

Una decisión puede apoyarse en un assessment, pero no forma parte del assessment mismo.

No todos los campos conceptuales tienen que producir necesariamente un valor explícito en todos los casos.

La estructura representa información potencialmente necesaria, no un schema obligatorio.

---

## 21. Ejemplos derivados de los experimentos

Las decisiones mostradas en estos ejemplos son representaciones analíticas provisionales derivadas del assessment; no corresponden a cambios aplicados sobre los consumers durante los experimentos.

### 21.1 Only Film — Quick Start

~~~text
Responsibility
    README-QUICK-START

Requirement Level
    Required

Detected Fact
    Quick Start section exists

Evidence
    installation instructions
    clone command

State
    Partial

Applicability
    Applicable

Evaluation Rationale
    repository reference belongs
    to inherited original project

Adoption Decision
    ADAPT

Decision Rationale
    useful implementation already exists;
    targeted personalization is sufficient
~~~

---

### 21.2 dental-back — Quick Start

~~~text
Responsibility
    README-QUICK-START

Requirement Level
    Required

Detected Fact
    Quick Start content exists

Evidence
    installation instructions
    clone command

State
    Partial

Applicability
    Applicable

Evaluation Rationale
    clone command contains
    generic repository placeholder

Adoption Decision
    ADAPT

Decision Rationale
    implementation should be retained
    and personalized rather than replaced
~~~

Los dos ejemplos muestran:

~~~text
same State
+
same Decision
+
different Evidence / Rationale
~~~

---

### 21.3 Aula Robótica — Changelog

~~~text
Responsibility
    DOC-CHANGELOG

Requirement Level
    Required

Detected Fact
    docs/14_STATUS/55_CHANGELOG.md exists

Evidence
    changelog purpose declared
    semantic categories
    Unreleased section
    relevant project changes

Evaluation
    valid changelog implementation exists,
    but published versioned and dated
    release history is incomplete

State
    Partial

Applicability
    Applicable

Implementation Characteristics
    Own

Evaluation Rationale
    responsibility is partially implemented
    in a non-root artifact but does not yet
    satisfy the published release history
    expected by the Component

Adoption Decision
    ADAPT

Decision Rationale
    preserve existing useful changelog
    and complete missing release history
~~~

Este ejemplo demuestra:

~~~text
non-canonical path
        ≠
Missing

and

matching artifact
        ≠
Satisfied
~~~

---

## 22. Relación entre assessment y decisión

Los experimentos muestran que no puede asumirse como regla universal una relación trivial como:

~~~text
Satisfied → PRESERVE

Partial → ADAPT

Missing → ADD
~~~

como regla universal.

Puede resultar útil como heurística inicial en determinados casos, pero pierde dimensiones relevantes.

La relación observada es más próxima a:

~~~text
State
+
Requirement Level
+
Applicability
+
Implementation Characteristics
+
Evidence
+
Context
+
Rationale
        ↓
Adoption Decision
~~~

Ejemplos:

~~~text
Satisfied
+
valid direct implementation
        ↓
PRESERVE
~~~

~~~text
Satisfied
+
valid equivalent implementation
        ↓
ACCEPT
~~~

~~~text
Partial
+
useful existing implementation
        ↓
ADAPT
~~~

~~~text
Missing
+
Required
+
Applicable
        ↓
ADD
~~~

~~~text
Missing
+
Optional
+
Applicability uncertain
        ↓
EVALUATE
~~~

~~~text
Missing
+
Optional
+
Not Applicable
        ↓
OMIT
~~~

~~~text
Missing
+
Recommended
+
valid contextual reason
        ↓
JUSTIFY / OMIT
~~~

Estas relaciones continúan siendo ejemplos derivados de Discovery.

No constituyen todavía reglas ejecutables.

---

## 23. Flujo mínimo de adopción

La evidencia disponible permite representar un flujo mínimo para Existing Repository Adoption:

~~~text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
~~~

### ANALYZE

Observar el consumer y reunir hechos potencialmente relevantes.

### ASSESS

Interpretar la evidencia frente a las responsabilidades del Repository Template.

### REVIEW

Revisar incertidumbre, equivalencias, applicability y evaluaciones que no puedan resolverse de forma determinista.

### DECIDE

Registrar explícitamente la decisión de adopción para cada responsabilidad relevante.

### REPORT

Producir una representación trazable del assessment y de las decisiones.

Este flujo describe únicamente la parte del proceso respaldada por la evidencia obtenida durante los experimentos.

---

## 24. Relación con aplicación futura

Un proceso completo de adopción podría evolucionar posteriormente hacia:

~~~text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
    ↓
APPLY
    ↓
VERIFY
~~~

Sin embargo:

~~~text
APPLY
VERIFY
~~~

no han sido investigados operacionalmente durante los experimentos actuales.

Por tanto, permanecen fuera de la parte del modelo provisional respaldada por la evidencia disponible.

Esto evita utilizar evidencia sobre assessment y adoption decision para justificar prematuramente mecanismos de modificación o verificación del repositorio.

---

## 25. Límites de automatización

### 25.1 Automatización potencialmente determinista

Los experimentos muestran hechos que podrían detectarse mediante automatización con riesgo relativamente bajo.

Ejemplos:

~~~text
file exists

directory exists

README section exists

workflow exists

test files exist

OpenAPI artifact exists

specific configuration exists
~~~

Estos resultados pueden convertirse en evidencia.

No deberían convertirse directamente en decisiones.

---

### 25.2 Evaluación potencialmente asistida

Otros aspectos requieren interpretación.

Ejemplos:

~~~text
Does this content satisfy the responsibility?

Is this artifact semantically equivalent?

Is this responsibility applicable?

Is the documentation sufficiently complete?

Does this distributed implementation
cover the expected responsibility?
~~~

Una futura herramienta podría ayudar a reunir información o presentar evidencia.

Los experimentos no justifican todavía delegar automáticamente estas decisiones.

---

### 25.3 Decisiones que requieren contexto

Las decisiones de adopción incorporan factores que no pueden deducirse únicamente de la estructura del repositorio.

Por ejemplo:

~~~text
PRESERVE or ACCEPT?

ADD or OMIT?

ADAPT?

Is omission justified?

Is an equivalent implementation preferable to the canonical one?
~~~

Estos ejemplos se refieren a decisiones de adopción dentro del modelo provisional.

`REPLACE` no se introduce como una `Adoption Decision`.

La sustitución de un artifact implicaría una estrategia futura de aplicación sobre el consumer y permanece fuera del alcance investigado por esta Discovery.

Por tanto, el modelo mantiene:

~~~text
Human Review
~~~

como frontera provisional cuando exista interpretación semántica o decisión contextual.

---

### 25.4 Aplicación automática

Los experimentos no han evaluado:

- generación de archivos;
- modificación de contenido existente;
- merge de documentación;
- actualización automática de configuración;
- rollback;
- resolución de conflictos;
- idempotencia;
- preservación de customizaciones;
- seguridad de modificaciones.

Por tanto, ninguna conclusión de esta investigación deberá utilizarse para afirmar que:

~~~text
automatic APPLY is safe
~~~

---

## 26. Frontera provisional de automatización

La evidencia permite representar la frontera actual de la siguiente manera:

~~~text
                  DEGREE OF DETERMINISM

Detected Facts          MORE DETERMINISTIC
      │
      ↓
Evidence Collection     PARTLY DETERMINISTIC
      │
      ↓
Semantic Evaluation     CONTEXTUAL
      │
      ↓
Adoption Decision       CONTEXTUAL
      │
      ↓
Repository Changes      NOT EVALUATED HERE
~~~

El grado de determinismo disminuye a medida que el proceso incorpora interpretación semántica y contexto específico del consumer.

Esto no implica que las etapas contextuales no puedan recibir asistencia mediante automatización.

Implica únicamente que la evidencia disponible no permite tratarlas como transformaciones completamente deterministas.

Esto conduce a un principio provisional:

> Automatizar primero la obtención y organización de evidencia; automatizar decisiones o modificaciones únicamente cuando exista evidencia específica que permita hacerlo de forma segura.

Este principio no selecciona ninguna tecnología.

No implica todavía:

- analyzer;
- CLI;
- manifest;
- validator extension;
- GitHub Action;
- generator.

---

## 27. Qué no es el modelo provisional.

El modelo provisional no debe confundirse con una implementación futura.

En particular:

~~~text
Provisional Adoption Model
    ≠
github-framework.yml
~~~

~~~text
Provisional Adoption Model
    ≠
Adoption CLI
~~~

~~~text
Provisional Adoption Model
    ≠
Framework Validator extension
~~~

~~~text
Provisional Adoption Model
    ≠
Repository Generator
~~~

~~~text
Provisional Adoption Model
    ≠
GitHub Action
~~~

~~~text
Provisional Adoption Model
    ≠
AI Analyzer
~~~

Cualquiera de esas opciones podría investigarse posteriormente como Solution Hypothesis.

El modelo conceptual existe antes de seleccionar cómo materializarlo.

---

## 28. Estado del modelo

Tras tres experiments:

~~~text
Model Status
    Provisional

Tested Context
    TPL-BACKEND v0.1.0
    Existing Repository Adoption

Consumers
    Only Film
    dental-back
    aula-robotica-platform

Fundamental States
    Satisfied
    Partial
    Missing

Fundamental Adoption Decisions
    PRESERVE
    ADAPT
    ADD
    ACCEPT
    EVALUATE
    JUSTIFY
    OMIT

Application Model
    Not Validated

Implementation Architecture
    Not Selected

Delivery Scope
    Not Selected
~~~

El modelo dispone de evidencia suficiente para utilizarse como base de la siguiente etapa de Discovery.

No dispone todavía de evidencia suficiente para convertirse directamente en una especificación normativa del Framework.

---

## 29. Impacto sobre las Solution Hypotheses

El primer experimento identificó varias posibles respuestas al problema de adopción.

Estas opciones se registraron como:

~~~text
SH-01  Manual Adoption Guide

SH-02  Adoption Checklist / Assessment

SH-03  Assisted Repository Analyzer

SH-04  Adoption Report

SH-05  Adoption Manifest

SH-06  Framework Validator Extension

SH-07  Adoption CLI

SH-08  Selective Application

SH-09  Repository Generator

SH-10  GitHub Actions Integration

SH-11  Staged Adoption Process
~~~

Los experimentos posteriores permiten reconsiderar estas hipótesis.

Esta revisión no selecciona una solución.

Su propósito es determinar qué relación mantiene cada hipótesis con las necesidades observadas.

---

### 29.1 SH-01 — Manual Adoption Guide

Continúa siendo compatible con la evidencia.

Una guía podría explicar:

- cómo seleccionar un Repository Template;
- cómo analizar un consumer;
- cómo evaluar responsabilidades;
- cómo interpretar requirement levels;
- cómo considerar applicability;
- cómo reconocer implementaciones equivalentes o distribuidas;
- cómo tomar decisiones de adopción.

Su principal ventaja conceptual es que puede representar el proceso sin requerir automatización prematura.

Sin embargo, una guía por sí sola no proporciona necesariamente una representación estructurada del assessment.

~~~text
Status
    Still Plausible
~~~

---

### 29.2 SH-02 — Adoption Checklist / Assessment

Los experimentos refuerzan especialmente la necesidad de algún mecanismo que permita revisar responsabilidades de forma sistemática.

Una representación de assessment podría registrar conceptos como:

~~~text
Responsibility

Requirement Level

Evidence

State

Applicability

Implementation Characteristics

Uncertainty

Rationale
~~~

Esto mantiene una relación directa con el MUM.

No obstante:

~~~text
Assessment Concept
        ≠
specific file format
~~~

La evidencia no determina todavía si debería materializarse como Markdown, tabla, formulario, estructura serializada u otro mecanismo.

~~~text
Status
    Strongly Supported as a Need
    Implementation Undecided
~~~

---

### 29.3 SH-03 — Assisted Repository Analyzer

Los experimentos muestran oportunidades claras para asistencia automatizada en la detección de hechos.

Un analyzer podría potencialmente detectar:

~~~text
files
directories
README sections
workflows
tests
documentation artifacts
OpenAPI artifacts
configuration
~~~

Esto podría reducir trabajo manual durante `ANALYZE`.

Sin embargo, los experimentos muestran también que:

~~~text
Detection
    ≠
Semantic Evaluation
~~~

Por tanto, la evidencia respalda mejor:

~~~text
Assisted Analysis
~~~

que:

~~~text
Automatic Adoption Decision
~~~

~~~text
Status
    Plausible
    Automation Boundary Required
~~~

---

### 29.4 SH-04 — Adoption Report

La necesidad de trazabilidad refuerza la utilidad potencial de un resultado explícito del análisis.

Un report podría comunicar:

~~~text
Template evaluated

Responsibilities evaluated

Evidence found

States

Uncertainty

Decisions

Rationale
~~~

Esto permitiría revisar el assessment sin modificar el consumer.

El concepto se alinea especialmente con:

~~~text
ANALYZE
ASSESS
REVIEW
DECIDE
REPORT
~~~

Sin embargo, los experimentos no determinan todavía si el report debe ser persistente, generado, manual o efímero.

~~~text
Status
    Strongly Supported as an Outcome
    Representation Undecided
~~~

---

### 29.5 SH-05 — Adoption Manifest

Un manifest podría representar de forma estructurada decisiones y metadata de adopción.

Sin embargo, los experimentos no demuestran todavía que el consumer necesite almacenar permanentemente esa información en un archivo dedicado.

Introducir prematuramente algo como:

~~~text
github-framework.yml
~~~

podría convertir un modelo conceptual todavía provisional en un contrato técnico difícil de modificar.

Antes sería necesario comprender:

- qué información merece persistencia;
- quién la mantiene;
- cuándo cambia;
- qué constituye source of truth;
- cómo se versiona;
- cómo interactúa con Template metadata;
- cómo evita duplicar información existente.

~~~text
Status
    Open Hypothesis
    Not Yet Justified
~~~

---

### 29.6 SH-06 — Framework Validator Extension

El validator actual trabaja sobre responsabilidades propias de validación del Framework.

Los experimentos muestran que consumer adoption introduce además evaluación semántica y contextual.

Extender directamente el validator podría mezclar:

~~~text
Framework Structural Validation
        +
Consumer Adoption Assessment
~~~

antes de comprender completamente la frontera entre ambos.

Determinados checks podrían resultar automatizables en el futuro.

Sin embargo, la evidencia actual no justifica convertir el Framework Validator en motor de adopción.

~~~text
Status
    Possible Future Integration
    Premature as Current Solution
~~~

---

### 29.7 SH-07 — Adoption CLI

Una CLI podría eventualmente orquestar partes del proceso:

~~~text
analyze
assess
report
apply
verify
~~~

pero elegir una CLI ahora fijaría una interfaz de usuario antes de estabilizar suficientemente el proceso que debería representar.

Los experimentos proporcionan evidencia que respalda varios conceptos del dominio de adopción.

No validan todavía una interfaz de ejecución.

~~~text
Status
    Open Hypothesis
    Premature
~~~

---

### 29.8 SH-08 — Selective Application

La evidencia favorece conceptualmente una aplicación selectiva frente a una sustitución completa.

Las decisiones:

~~~text
PRESERVE
ADAPT
ADD
ACCEPT
OMIT
~~~

implican que diferentes responsabilidades pueden requerir tratamientos distintos.

Por tanto, si en el futuro existe una fase `APPLY`, debería ser capaz de respetar esas diferencias.

Sin embargo, los experimentos actuales no ejecutaron cambios.

No se han validado todavía:

- merge;
- patching;
- conflict resolution;
- idempotency;
- rollback;
- preservation of customizations.

~~~text
Status
    Conceptually Supported
    Operationally Unvalidated
~~~

---

### 29.9 SH-09 — Repository Generator

Los experimentos proporcionan poca evidencia a favor de utilizar generación como respuesta principal a Existing Repository Adoption.

Los consumers ya contienen implementaciones que deben:

~~~text
PRESERVE
ADAPT
ACCEPT
~~~

Un generator orientado a crear una estructura desde cero no resuelve por sí solo el problema de reconciliación.

Esto no implica que generation carezca de utilidad para:

~~~text
Repository Initialization
~~~

pero ese escenario no ha sido investigado aquí.

~~~text
Status
    Weak Fit for Existing Repository Adoption
    Initialization Not Evaluated
~~~

---

### 29.10 SH-10 — GitHub Actions Integration

GitHub Actions podría eventualmente ejecutar análisis o verificaciones recurrentes.

Sin embargo, integrar adopción en CI antes de estabilizar:

~~~text
what is evaluated
how it is evaluated
what is deterministic
what requires review
~~~

sería prematuro.

Además, los experimentos no han demostrado todavía la necesidad de evaluación continua después de una adopción inicial.

~~~text
Status
    Possible Future Integration
    Not Yet Justified
~~~

---

### 29.11 SH-11 — Staged Adoption Process

Los experimentos proporcionan el mayor soporte conceptual a una adopción por etapas.

La hipótesis inicial puede refinarse, para la parte efectivamente investigada, como:

~~~text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
~~~

Un proceso completo podría incorporar posteriormente:

~~~text
APPLY
    ↓
VERIFY
~~~

pero esas etapas no han sido validadas todavía.

La principal evidencia a favor del staged process es que los experimentos necesitan separar explícitamente:

~~~text
observation
evaluation
decision
application
~~~

~~~text
Status
    Strongly Supported Conceptually
~~~

---

## 30. Comparación de las Solution Hypotheses

La evidencia disponible permite agrupar provisionalmente las hipótesis según su relación con los findings.

| Solution Hypothesis | Discovery Assessment |
|---|---|
| SH-01 Manual Adoption Guide | Still Plausible |
| SH-02 Adoption Checklist / Assessment | Strongly Supported as a Need |
| SH-03 Assisted Repository Analyzer | Plausible; automation boundary required |
| SH-04 Adoption Report | Strongly Supported as an Outcome |
| SH-05 Adoption Manifest | Open; not yet justified |
| SH-06 Validator Extension | Possible future integration; premature |
| SH-07 Adoption CLI | Open; premature |
| SH-08 Selective Application | Conceptually supported; operationally unvalidated |
| SH-09 Repository Generator | Weak fit for existing repository adoption |
| SH-10 GitHub Actions Integration | Possible future integration; not yet justified |
| SH-11 Staged Adoption Process | Strongly supported conceptually |

Esta tabla no constituye un ranking.

Tampoco selecciona una implementación.

Su función es registrar cómo ha cambiado la plausibilidad de las hipótesis después de los experimentos.

---

## 31. Preguntas abiertas

La investigación reduce considerablemente el espacio del problema, pero mantiene preguntas relevantes.

### 31.1 Assessment

Permanece abierto:

- qué información mínima debe persistirse;
- qué qualifiers necesitan representación explícita;
- cómo expresar incertidumbre;
- cómo evaluar equivalencia de forma consistente;
- qué evidence resulta suficiente para cada responsabilidad;
- cuándo una implementación distribuida puede considerarse completa.

---

### 31.2 Applicability

Debe investigarse:

- quién determina applicability;
- si puede inferirse parcialmente del tipo de proyecto;
- cuándo requiere revisión humana;
- cómo documentar una decisión `Not Applicable`;
- cómo interactúa con Required, Recommended y Optional.

Los experimentos no han demostrado todavía si una responsabilidad Required puede legítimamente ser `Not Applicable` dentro de todos los Repository Templates.

---

### 31.3 Implementation Characteristics

Permanece abierta la estructura interna de:

~~~text
Implementation Characteristics
~~~

Los experimentos sugieren que no es una enumeración exclusiva.

Una posible futura investigación podría estudiar dimensiones como:

~~~text
Origin
Relation
Distribution
~~~

pero introducirlas ahora excedería la evidencia disponible.

---

### 31.4 Evidence Model

Debe determinarse si el Framework necesita distinguir formalmente entre:

~~~text
Detected Fact

Evidence

Evaluation
~~~

o si parte de esa distinción puede mantenerse únicamente a nivel conceptual.

También permanece abierto cómo representar evidencia distribuida y qué nivel de detalle resulta útil sin generar burocracia.

---

### 31.5 Persistence

No está resuelto si assessment y decisiones deben:

~~~text
exist only during adoption

or

persist inside consumer repository

or

persist externally

or

combine multiple approaches
~~~

Esta pregunta debe resolverse antes de seleccionar un manifest.

---

### 31.6 Reassessment

No se ha investigado qué ocurre cuando el consumer evoluciona después de la adopción.

Permanece abierto si existe necesidad de:

~~~text
one-time assessment

periodic reassessment

continuous conformance checking
~~~

La respuesta condicionaría posibles integraciones futuras con validator o CI.

---

### 31.7 Application

La mayor área no validada continúa siendo:

~~~text
APPLY
~~~

Antes de automatizar modificaciones será necesario investigar:

- safe modification;
- preservation;
- merge;
- conflict detection;
- idempotency;
- rollback;
- verification;
- user control.

---

### 31.8 Initialization

Los experimentos no investigan:

~~~text
Repository Initialization
~~~

Por tanto, no puede concluirse todavía si:

~~~text
Initialization
+
Existing Repository Adoption
~~~

deben compartir una implementación, compartir únicamente parte del modelo o permanecer como workflows independientes.

---

### 31.9 Other Repository Templates

Toda la investigación utiliza:

~~~text
TPL-BACKEND v0.1.0
~~~

El modelo deberá contrastarse eventualmente con otros Repository Templates para determinar qué elementos son realmente generales.

---

## 32. Conclusiones

### 32.1 Respuesta a la pregunta de Discovery

La pregunta central de esta investigación es:

> ¿Qué limita hoy que GitHub Framework sea realmente útil fuera de su propio repositorio?

Los experimentos permiten responder provisionalmente:

> GitHub Framework ya puede describir mediante Standards, Components y Repository Templates las responsabilidades esperadas de un repositorio, pero todavía carece de un proceso de adopción suficientemente formalizado para analizar un consumer existente, evaluar cómo sus implementaciones satisfacen esas responsabilidades y registrar de forma trazable qué debe preservarse, adaptarse, añadirse, aceptarse, justificarse u omitirse.

La limitación principal observada no es la ausencia de otro Repository Template ni la falta inmediata de un generator.

Es el gap entre:

~~~text
Declarative Repository Model
        ↓
Existing Consumer Reality
~~~

---

### 32.2 Naturaleza del problema

Existing Repository Adoption se comporta principalmente como:

~~~text
Reconciliation
~~~

y no como:

~~~text
Generation
~~~

El consumer ya contiene implementaciones y decisiones.

Por tanto, una adopción segura necesita comprender primero esas implementaciones.

---

### 32.3 Modelo provisional

Los experimentos permiten conservar provisionalmente:

~~~text
State
    Satisfied
    Partial
    Missing
~~~

y:

~~~text
Adoption Decision
    PRESERVE
    ADAPT
    ADD
    ACCEPT
    EVALUATE
    JUSTIFY
    OMIT
~~~

pero muestran que estos elementos necesitan contexto adicional:

~~~text
Evidence

Applicability

Implementation Characteristics

Uncertainty

Rationale
~~~

---

### 32.4 Frontera de automatización

La investigación muestra una frontera consistente:

~~~text
Detected Facts
        ↓
Evidence
        ↓
Semantic Evaluation
        ↓
Adoption Decision
        ↓
Repository Modification
~~~

El grado de determinismo disminuye a medida que el proceso incorpora interpretación semántica y contexto específico del consumer.

Esto sugiere que la automatización directa resulta más adecuada en las etapas con evidencia más determinista, mientras que las etapas de evaluación y decisión requieren preservar explícitamente el contexto y la intervención humana.

Por tanto:

> The Framework needs to understand the adoption process before automating it.

La automatización más segura comienza ayudando a detectar y organizar evidencia, no aplicando automáticamente cambios al consumer.

---

### 32.5 Resultado de los experimentos

Los tres consumers no han producido una refutación fundamental del modelo.

Sí han provocado refinamientos importantes:

- estado separado de razón;
- applicability independiente;
- evidence explícita;
- detección separada de evaluación;
- implementación no limitada a artefactos canónicos;
- características de implementación potencialmente múltiples;
- assessment separado de decision;
- decision separada de application.

Por tanto, el resultado global puede expresarse como:

~~~text
Initial Adoption Model
        ↓
3 Consumer Experiments
        ↓
Refined Provisional Model
~~~

No como:

~~~text
Final Universal Adoption Standard
~~~

---

## 33. Próximos pasos de Discovery

La investigación ha reducido suficientemente el problema para evitar comenzar la siguiente etapa desde una lista abierta de features.

El siguiente paso debería investigar cómo representar y utilizar el assessment mínimo sin comprometer todavía una arquitectura de implementación.

La pregunta siguiente puede formularse como:

> ¿Cuál es la forma mínima, comprensible y trazable de realizar un adoption assessment sobre un consumer real utilizando el modelo provisional?

Esta pregunta permite contrastar conjuntamente:

~~~text
SH-01  Manual Adoption Guide

SH-02  Adoption Checklist / Assessment

SH-04  Adoption Report

SH-11  Staged Adoption Process
~~~

antes de introducir hipótesis de mayor coste o acoplamiento como:

~~~text
Manifest
CLI
Validator Extension
Generator
GitHub Actions
~~~

El objetivo de la siguiente investigación no debería ser seleccionar inmediatamente una herramienta.

Debería comprobar primero si el modelo provisional puede utilizarse de forma repetible por una persona sobre un consumer real.

---

## 34. Estado de Discovery

~~~text
Discovery Topic
    Existing Repository Adoption

Repository Template Tested
    TPL-BACKEND v0.1.0

Consumers Tested
    3

Experiments
    Completed

Problem Understanding
    Substantially Improved

Requirement Candidates
    Consolidated

Adoption Model
    Provisional

Solution Selected
    No

Implementation Architecture Selected
    No

Delivery Scope Selected
    No

Sprint Selected
    No

Milestone Selected
    No

Release Selected
    No
~~~

La investigación puede considerarse suficientemente madura para cerrar esta etapa de problem discovery.

El siguiente paso deberá continuar siendo Discovery hasta validar una forma mínima y repetible de realizar el adoption assessment.

Solo después de esa validación deberá evaluarse si existe evidencia suficiente para convertir alguna Solution Hypothesis en delivery scope.

