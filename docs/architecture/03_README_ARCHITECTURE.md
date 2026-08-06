# 03 - README ARCHITECTURE

| Field           | Value                       |
| --------------- | --------------------------- |
| **Project**     | GitHub Professional Profile |
| **Document**    | Profile README Architecture |
| **Version**     | 1.0.0 (Draft)               |
| **Status**      | In Progress                 |
| **Owner**       | Fran Ramirez                |
| **Last Update** | 2026-08-05                  |

---

> *El README del perfil no debe funcionar como un currículum completo ni como una colección de widgets. Debe actuar como una página de presentación profesional que permita comprender rápidamente quién es Fran Ramirez, qué construye y qué proyectos representan mejor su trabajo.*

Este documento define la arquitectura de información, la estructura editorial y las reglas de composición del GitHub Profile README de **Fran Ramirez**.

Su objetivo es transformar las decisiones establecidas en [`01_BRAND.md`](./01_BRAND.md) y [`02_VISUAL_IDENTITY.md`](./02_VISUAL_IDENTITY.md) en una estructura concreta, mantenible y preparada para su implementación.

La arquitectura deberá aplicarse de forma sincronizada a:

```text
README.md
README.es.md
```

El inglés será el idioma principal y el español ofrecerá una versión equivalente, no una adaptación simplificada.

---

# 1. Purpose

El GitHub Profile README constituye la página principal de la presencia técnica en GitHub.

Su responsabilidad consiste en ofrecer una visión breve, clara y curada de:

* la identidad profesional;
* el posicionamiento técnico;
* la propuesta de valor;
* la forma de entender la ingeniería;
* los proyectos más representativos;
* las capacidades técnicas principales;
* las vías de contacto profesional.

No deberá intentar contener toda la información disponible.

Su función será orientar al visitante hacia las evidencias más relevantes.

---

# 2. README Role

El README deberá actuar simultáneamente como:

## 2.1 Professional Landing Page

Será el primer punto de entrada para recruiters, Tech Leads, Engineering Managers y otros desarrolladores.

Deberá permitir una comprensión inicial sin necesidad de abrir inmediatamente otros repositorios.

---

## 2.2 Portfolio Index

Presentará una selección reducida de proyectos estratégicos.

No será un catálogo completo de repositorios.

Cada proyecto incluido deberá representar una capacidad concreta y aportar una historia diferente al conjunto.

---

## 2.3 Technical Identity Statement

Comunicará una forma de entender la ingeniería basada en:

* arquitectura;
* mantenibilidad;
* documentación;
* testing;
* escalabilidad;
* aprendizaje continuo.

---

## 2.4 Navigation Layer

Conectará el perfil con:

* repositorios estratégicos;
* documentación;
* LinkedIn;
* correo profesional;
* CV o portfolio futuro;
* versión alternativa del idioma.

---

## 2.5 Living Document

El README deberá evolucionar junto con la carrera profesional sin requerir reconstrucciones frecuentes.

La estructura deberá permanecer estable.

Las actualizaciones habituales afectarán principalmente a:

* proyectos;
* foco actual;
* tecnologías;
* enlaces;
* estadísticas;
* posicionamiento futuro.

---

# 3. Target Audience

El README estará diseñado para varios tipos de visitante.

La arquitectura deberá permitir que cada uno encuentre rápidamente la información que necesita.

---

## 3.1 Technical Recruiters

Necesitan identificar:

* posicionamiento;
* tecnologías principales;
* nivel de experiencia;
* proyectos;
* ubicación;
* contacto;
* coherencia con una vacante.

Tiempo probable de exploración inicial:

```text
15–30 segundos
```

---

## 3.2 Tech Leads

Necesitan evaluar:

* calidad técnica;
* arquitectura;
* documentación;
* testing;
* profundidad de los proyectos;
* capacidad de evolución;
* forma de razonar sobre software.

Tiempo probable de exploración:

```text
1–5 minutos
```

---

## 3.3 Engineering Managers

Necesitan comprender:

* madurez profesional;
* capacidad de comunicación;
* autonomía;
* consistencia;
* orientación a producto;
* potencial de crecimiento;
* experiencia transversal.

---

## 3.4 Software Engineers

Pueden interesarse por:

* código;
* arquitectura;
* documentación;
* herramientas;
* decisiones técnicas;
* colaboración;
* reutilización de conocimiento.

---

## 3.5 Open Source Contributors

Necesitan localizar:

* proyectos activos;
* documentación;
* estado;
* roadmap;
* contributing guidelines;
* issues;
* licencias.

---

# 4. Primary User Questions

La arquitectura deberá responder de forma progresiva a las siguientes preguntas:

1. ¿Quién es Fran Ramirez?
2. ¿Cómo se posiciona profesionalmente?
3. ¿Qué tipo de software desarrolla?
4. ¿Cómo entiende la ingeniería?
5. ¿En qué está trabajando actualmente?
6. ¿Qué proyectos demuestran sus capacidades?
7. ¿Qué tecnologías utiliza?
8. ¿Cómo puede contactarse con él?
9. ¿Dónde puede encontrarse información más detallada?

Cada sección deberá responder principalmente a una de estas preguntas.

---

# 5. Communication Priorities

La información deberá organizarse según el siguiente orden de prioridad.

## Priority 1 — Identity

```text
Fran Ramirez
Backend • Full Stack • AI Developer
```

---

## Priority 2 — Value Proposition

```text
Building scalable applications with Java, Python and AI.
```

---

## Priority 3 — Evidence

Proyectos que demuestran las capacidades comunicadas.

---

## Priority 4 — Technical Capabilities

Tecnologías, dominios y prácticas de ingeniería.

---

## Priority 5 — Context

Foco actual, trayectoria y orientación profesional.

---

## Priority 6 — Contact

Vías de comunicación profesional.

---

## Priority 7 — Supporting Metrics

Estadísticas o indicadores complementarios.

Las métricas nunca deberán aparecer antes que los proyectos.

---

# 6. Information Architecture Principles

## 6.1 Identity Before Detail

El visitante deberá comprender la identidad antes de encontrar tecnologías o métricas.

El README no comenzará con badges, estadísticas ni listas de herramientas.

---

## 6.2 Evidence Before Claims

Toda afirmación relevante deberá estar respaldada por:

* proyectos;
* documentación;
* repositorios;
* resultados;
* experiencia;
* enlaces verificables.

---

## 6.3 Progressive Disclosure

La información se presentará desde lo general hacia lo específico.

```text
Identity
↓
Context
↓
Current Focus
↓
Projects
↓
Technologies
↓
Principles
↓
Metrics
↓
Contact
```

El visitante podrá abandonar la lectura en cualquier punto conservando una comprensión coherente del perfil.

---

## 6.4 Scan Before Read

La arquitectura deberá facilitar una exploración visual rápida.

Se utilizarán:

* títulos descriptivos;
* párrafos breves;
* listas limitadas;
* proyectos claramente diferenciados;
* etiquetas tecnológicas;
* espaciado;
* enlaces reconocibles.

---

## 6.5 Short Profile, Deep Repositories

El README del perfil será breve.

Los repositorios estratégicos contendrán el detalle.

El perfil deberá dirigir hacia ellos, no reproducir su documentación.

---

## 6.6 One Section, One Responsibility

Cada sección tendrá una responsabilidad principal.

No se mezclarán:

* biografía y tecnologías;
* proyectos y estadísticas;
* contacto y posicionamiento;
* foco actual e historial completo;
* principios y claims comerciales.

---

## 6.7 Stable Structure, Flexible Content

La estructura deberá mantenerse estable durante varios años.

El contenido podrá evolucionar sin alterar la arquitectura general.

---

# 7. Reading Modes

El README deberá funcionar en tres niveles de lectura.

---

## 7.1 Ten-Second Scan

El visitante deberá identificar:

* nombre;
* rol;
* tagline;
* ubicación o contexto;
* primeros proyectos.

Elementos clave:

```text
Hero
Primary Links
Engineering Portfolio heading
```

---

## 7.2 One-Minute Review

El visitante deberá comprender:

* forma de trabajar;
* foco actual;
* proyectos;
* stack principal;
* contacto.

Elementos clave:

```text
Hero
About
Current Focus
Engineering Portfolio
Technology Stack
Contact
```

---

## 7.3 Deep Exploration

El visitante deberá poder acceder a:

* repositorios;
* arquitectura;
* documentación;
* demos;
* releases;
* LinkedIn;
* versión alternativa del idioma.

El detalle se ofrecerá mediante enlaces, no mediante bloques excesivamente largos.

---

# 8. Page Length Strategy

La longitud deberá mantenerse controlada.

Objetivo aproximado:

```text
800–1,300 palabras
```

Sin contar:

* nombres tecnológicos;
* alt text;
* código HTML;
* URLs;
* contenido interno de SVG;
* metadatos externos.

La longitud final dependerá de la representación de las tarjetas de proyectos.

---

## 8.1 Maximum Reading Length

La lectura lineal completa no debería superar aproximadamente:

```text
4–6 minutos
```

La mayoría de visitantes no realizará esa lectura completa.

Por ello, la información principal deberá aparecer antes de la mitad del documento.

---

## 8.2 Section Length Guidance

| Section                |              Recommended Length |
| ---------------------- | ------------------------------: |
| Hero                   |                  20–40 palabras |
| About                  |                100–150 palabras |
| Current Focus          |                      3–4 puntos |
| Engineering Portfolio  |                   4–6 proyectos |
| Project Description    |                  30–60 palabras |
| Technology Stack       | 20–35 tecnologías seleccionadas |
| Engineering Principles |                      4–6 puntos |
| Statistics             |                     1–2 widgets |
| Contact                |                      1–3 líneas |

---

# 9. Structural Blueprint

La primera versión utilizará la siguiente arquitectura:

```text
Language Switch
│
├── Hero
│   ├── Banner
│   ├── Name
│   ├── Professional Positioning
│   ├── Tagline
│   └── Primary Links
│
├── About Me
│
├── Current Focus
│
├── Engineering Portfolio
│   ├── Featured Project
│   ├── Project Card
│   ├── Project Card
│   ├── Project Card
│   └── Optional Additional Projects
│
├── Technology Stack
│   ├── Backend
│   ├── Frontend
│   ├── AI & Data
│   ├── Databases
│   ├── Cloud & DevOps
│   └── Testing & Tools
│
├── Engineering Principles
│
├── GitHub Activity
│   └── Maximum Two Widgets
│
├── Let's Connect
│
└── Optional Footer
```

---

# 10. Final Section Order

La primera versión deberá seguir este orden:

1. Language Switch.
2. Hero.
3. About Me.
4. Current Focus.
5. Engineering Portfolio.
6. Technology Stack.
7. Engineering Principles.
8. GitHub Activity.
9. Let's Connect.
10. Optional Footer.

El orden no deberá modificarse durante la primera implementación salvo que una prueba real demuestre una mejora significativa.

---

# 11. Ordering Rationale

## 11.1 Language Switch First

Permite elegir el idioma antes de comenzar la lectura.

Deberá ser discreto y no competir con el Hero.

---

## 11.2 Hero Before Everything Else

La identidad y el posicionamiento deben preceder a cualquier detalle.

---

## 11.3 About Before Technologies

El contexto profesional ayuda a interpretar correctamente el stack.

Sin contexto, una lista de tecnologías puede parecer indiscriminada.

---

## 11.4 Current Focus Before Portfolio

El foco actual conecta la identidad con el trabajo presente.

Prepara al visitante para comprender los proyectos seleccionados.

---

## 11.5 Portfolio Before Stack

Los proyectos constituyen evidencias.

Las tecnologías son herramientas.

La evidencia tendrá prioridad.

---

## 11.6 Principles After Technologies

Los principios explican cómo se utilizan esas herramientas.

Su ubicación posterior evita comenzar el perfil con declaraciones abstractas.

---

## 11.7 Statistics Near the End

Las métricas complementan el trabajo.

No deberán dominar el perfil ni condicionar la primera impresión.

---

## 11.8 Contact as Closing Action

El contacto aparecerá después de que el visitante haya recibido suficiente información para decidir si desea iniciar una conversación.

---

# 12. Optional Sections

Las siguientes secciones no formarán parte obligatoria de la primera versión.

---

## 12.1 Engineering Journey

Podrá explicar la evolución desde gestión de proyectos y comunicación hacia desarrollo de software, backend e IA.

Riesgos:

* alargar el perfil;
* duplicar LinkedIn;
* distraer de los proyectos;
* introducir fechas innecesarias.

Decisión inicial:

```text
Deferred
```

---

## 12.2 Open Source Contributions

Se incorporará cuando exista un volumen suficientemente representativo de contribuciones a proyectos de terceros.

Decisión inicial:

```text
Deferred
```

---

## 12.3 Certifications

No se incluirá inicialmente.

Podrá enlazarse desde LinkedIn o CV.

Decisión inicial:

```text
Excluded
```

---

## 12.4 Education

No se incluirá como sección independiente.

Podrá mencionarse de forma muy breve en About si aporta contexto.

Decisión inicial:

```text
Excluded as standalone section
```

---

## 12.5 Availability

No se incluirá de forma permanente salvo que exista una necesidad profesional concreta.

Decisión inicial:

```text
Context-dependent
```

---

## 12.6 Testimonials

No se incluirán en la primera versión.

GitHub no es el canal principal para recomendaciones profesionales.

Decisión inicial:

```text
Excluded
```

---

## 12.7 Blog or Articles

Podrá incorporarse cuando exista contenido publicado y mantenido.

Decisión inicial:

```text
Future extension
```

---

# 13. Excluded Elements

La arquitectura no incluirá:

* visitor counter;
* contribution snake;
* Spotify widget;
* Discord status;
* GIF decorativo;
* typing animation base;
* tablas de contenido para el Profile README;
* muro de badges;
* lista completa de repositorios;
* historial laboral completo;
* formación exhaustiva;
* certificaciones extensas;
* hobbies sin relación profesional;
* frases motivacionales genéricas;
* estadísticas antes de los proyectos;
* tecnologías sin evidencia.

---

# 14. Navigation Strategy

El Profile README no utilizará inicialmente una tabla de contenidos.

Razones:

* longitud controlada;
* flujo lineal;
* pocas secciones;
* compatibilidad móvil;
* reducción de ruido;
* ausencia de necesidad real.

La navegación se resolverá mediante:

* títulos claros;
* orden estable;
* enlaces contextuales;
* lenguaje visual consistente;
* separación adecuada.

---

# 15. Link Architecture

Los enlaces deberán estar jerarquizados.

---

## 15.1 Primary Links

* LinkedIn.
* Email.
* CV o portfolio futuro.

---

## 15.2 Portfolio Links

Por proyecto:

* Repository.
* Documentation.
* Demo.
* Architecture.

Solo se mostrarán enlaces existentes.

---

## 15.3 Supporting Links

* releases;
* roadmap;
* articles;
* additional documentation.

Se reservarán para los repositorios.

---

## 15.4 Link Rules

Los enlaces deberán:

* utilizar texto descriptivo;
* evitar URLs visibles;
* funcionar;
* apuntar directamente al recurso;
* evitar redirecciones innecesarias;
* mantener coherencia entre idiomas.

No se utilizará:

```text
Click here
More
Link
```

Se preferirá:

```text
View Repository
Read Documentation
Explore Architecture
Open Live Demo
```

---

# 16. Mobile-First Structure

Aunque la implementación se realizará en GitHub, la arquitectura deberá considerar primero las pantallas estrechas.

Principios:

* una columna principal;
* tarjetas que puedan apilarse;
* textos breves;
* iconos de tamaño legible;
* imágenes responsivas;
* ausencia de tablas anchas;
* enlaces fáciles de identificar;
* grupos de badges limitados.

El perfil no deberá depender de una composición horizontal compleja.

---

# 17. Accessibility Architecture

La accesibilidad deberá formar parte de la estructura.

El README deberá:

* utilizar jerarquía correcta de encabezados;
* mantener orden lógico;
* incluir alt text;
* evitar información basada solo en color;
* utilizar enlaces descriptivos;
* mantener texto esencial fuera de imágenes;
* evitar animaciones;
* conservar contraste;
* permitir comprensión sin widgets.

---

# 18. Failure Resilience

La estructura deberá continuar siendo comprensible si fallan:

* Skill Icons;
* GitHub Stats;
* imágenes externas;
* servicios de badges;
* previews remotas.

El contenido esencial deberá permanecer en:

* texto Markdown;
* enlaces;
* encabezados;
* descripciones;
* activos propios versionados.

---

# 19. Architecture Decisions

Quedan establecidas las siguientes decisiones:

1. El README funcionará como landing page profesional.
2. La arquitectura será lineal y de una columna.
3. El Hero aparecerá al inicio.
4. Los proyectos aparecerán antes que las tecnologías.
5. La estructura base tendrá nueve secciones principales.
6. No habrá tabla de contenidos.
7. El perfil mostrará entre cuatro y seis proyectos.
8. El stack estará agrupado por dominios.
9. Las estadísticas aparecerán cerca del final.
10. Se utilizarán como máximo dos widgets estadísticos.
11. El Engineering Journey queda aplazado.
12. Open Source Contributions se añadirá cuando exista evidencia suficiente.
13. Educación y certificaciones no tendrán sección propia.
14. El contenido principal será comprensible sin servicios externos.
15. La versión inglesa y española mantendrán la misma estructura.
16. El contenido prioritario aparecerá antes de la mitad del documento.
17. El perfil no intentará reproducir el CV.
18. Cada sección tendrá una responsabilidad principal.
19. La estructura deberá durar varios años.
20. Las actualizaciones habituales no deberán requerir cambios arquitectónicos.

---

# 20. Architecture Acceptance Criteria

La arquitectura se considerará válida cuando:

* [ ] La identidad se comprende en menos de diez segundos.
* [ ] Los proyectos pueden localizarse rápidamente.
* [ ] El stack no domina la presentación.
* [ ] El perfil puede escanearse sin lectura completa.
* [ ] Cada sección tiene un propósito claro.
* [ ] La estructura funciona en móvil.
* [ ] No depende de una tabla de contenidos.
* [ ] La versión inglesa y española pueden mantenerse sincronizadas.
* [ ] El contenido esencial permanece sin widgets.
* [ ] La longitud resulta controlada.
* [ ] La arquitectura permite añadir o sustituir proyectos.
* [ ] Las tecnologías pueden actualizarse sin rediseño.
* [ ] La información profesional no duplica innecesariamente LinkedIn.
* [ ] El contacto aparece de forma clara y no agresiva.
* [ ] La estructura refleja `01_BRAND.md`.
* [ ] La composición aplica `02_VISUAL_IDENTITY.md`.

---

# 21. Section Specification Framework

Cada sección del Profile README deberá documentarse mediante una especificación común.

La especificación incluirá:

```text
Section
├── Purpose
├── User Question
├── Content
├── Structure
├── Length
├── Maintenance
├── Restrictions
└── Acceptance Criteria
```

Este modelo permitirá evaluar cada bloque de forma independiente y evitará que las secciones acumulen responsabilidades innecesarias.

---

# 22. Language Switch

El componente `Language Switch` permitirá acceder a las versiones inglesa y española del perfil.

---

## 22.1 Purpose

Facilitar la selección de idioma antes de comenzar la lectura sin competir visualmente con el Hero.

---

## 22.2 User Question

> ¿Puedo consultar este perfil en mi idioma preferido?

---

## 22.3 Supported Languages

La primera versión incluirá:

```text
English
Español
```

Archivos asociados:

```text
README.md
README.es.md
```

El inglés será el idioma principal.

La versión española deberá mantener la misma arquitectura, contenido y nivel de calidad.

---

## 22.4 Recommended Structure

En la versión inglesa:

```markdown
<p align="right">
  <strong>English</strong> ·
  <a href="./README.es.md">Español</a>
</p>
```

En la versión española:

```markdown
<p align="right">
  <a href="./README.md">English</a> ·
  <strong>Español</strong>
</p>
```

La solución definitiva podrá utilizar Markdown nativo si ofrece una presentación suficientemente limpia.

---

## 22.5 Placement

El selector aparecerá:

```text
Antes del Hero
```

Deberá ocupar una única línea y mantener un contraste secundario.

---

## 22.6 Language Identification

Los idiomas deberán identificarse mediante texto.

Las banderas podrán utilizarse únicamente como apoyo opcional.

No deberán ser el único indicador, ya que representan países y no idiomas.

---

## 22.7 Maintenance

Cualquier cambio estructural o editorial deberá reflejarse en ambas versiones.

No se considerará completada una actualización hasta que:

* ambas versiones estén sincronizadas;
* los enlaces coincidan;
* los proyectos aparezcan en el mismo orden;
* las fechas y estados sean equivalentes;
* no existan secciones presentes en un idioma y ausentes en el otro.

---

## 22.8 Restrictions

El selector no deberá:

* incluir más idiomas sin una estrategia real de mantenimiento;
* utilizar badges grandes;
* ocupar una sección independiente;
* utilizar iconos ambiguos;
* enlazar a traducciones incompletas.

---

## 22.9 Acceptance Criteria

* [ ] Permite cambiar de idioma con un solo enlace.
* [ ] El idioma activo resulta identificable.
* [ ] La posición coincide en ambas versiones.
* [ ] No compite con el Hero.
* [ ] Funciona en móvil.
* [ ] No utiliza banderas como único indicador.
* [ ] Ambas versiones están sincronizadas.

---

# 23. Hero

El `Hero` será la sección de mayor prioridad visual y semántica del perfil.

---

## 23.1 Purpose

Comunicar durante los primeros segundos:

* identidad;
* posicionamiento;
* propuesta de valor;
* contexto profesional;
* canales principales.

---

## 23.2 User Question

> ¿Quién es Fran Ramirez y qué tipo de software desarrolla?

---

## 23.3 Required Content

El Hero deberá incluir:

```text
Banner
Fran Ramirez
Backend • Full Stack • AI Developer
Building scalable applications with Java, Python and AI.
Primary Professional Links
```

---

## 23.4 Identity Content

Nombre profesional:

```text
Fran Ramirez
```

Posicionamiento:

```text
Backend • Full Stack • AI Developer
```

Tagline:

```text
Building scalable applications with Java, Python and AI.
```

Estas expresiones deberán mantenerse idénticas en los activos gráficos y en el texto público, salvo traducción en `README.es.md`.

---

## 23.5 Spanish Version

Posicionamiento:

```text
Desarrollador Backend • Full Stack • IA
```

Tagline propuesta:

```text
Construyendo aplicaciones escalables con Java, Python e inteligencia artificial.
```

Antes de publicar deberá decidirse si el posicionamiento se traduce o se mantiene en inglés como etiqueta profesional internacional.

La versión inicial recomendada será mantener:

```text
Backend • Full Stack • AI Developer
```

también en español, traduciendo únicamente el tagline y el contenido descriptivo.

---

## 23.6 Banner Integration

El Hero utilizará:

```text
assets/brand/banner-dark.svg
assets/brand/banner-light.svg
```

mediante un elemento `picture`.

Estructura base:

```html
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="./assets/brand/banner-dark.svg"
  >
  <source
    media="(prefers-color-scheme: light)"
    srcset="./assets/brand/banner-light.svg"
  >
  <img
    src="./assets/brand/banner-light.svg"
    alt="Fran Ramirez — Backend, Full Stack and AI Developer"
    width="100%"
  >
</picture>
```

---

## 23.7 Duplication Strategy

El contenido esencial no deberá existir exclusivamente dentro del banner.

Aunque el banner incluya nombre o posicionamiento, deberá existir una representación textual accesible en Markdown o HTML.

La duplicación podrá resolverse reduciendo la jerarquía de uno de los dos bloques.

Posible composición:

```text
Banner visual
↓
Fran Ramirez
Backend • Full Stack • AI Developer
Tagline
↓
Links
```

---

## 23.8 Primary Links

Podrán incluir:

* LinkedIn;
* email;
* ubicación;
* CV futuro;
* portfolio futuro.

Versión inicial recomendada:

```text
Madrid, Spain
LinkedIn
Email
```

La ubicación podrá mostrarse como texto sin enlace.

---

## 23.9 Link Presentation

Opción preferida:

```markdown
Madrid, Spain · [LinkedIn](...) · [Email](mailto:...)
```

También podrán utilizarse dos badges discretos para LinkedIn y email si superan la validación visual.

No se utilizarán simultáneamente enlaces textuales y badges equivalentes.

---

## 23.10 Alignment

El Hero utilizará alineación centrada.

Todo el contenido posterior regresará a la alineación izquierda.

---

## 23.11 Length

Extensión textual máxima recomendada:

```text
40 palabras
```

Sin contar el alt text ni los enlaces.

---

## 23.12 Maintenance

Revisión cuando cambie:

* posicionamiento;
* tagline;
* ubicación;
* canales profesionales;
* identidad gráfica.

No deberá actualizarse por cambios menores de stack.

---

## 23.13 Restrictions

No deberá contener:

* párrafos biográficos;
* estadísticas;
* disponibilidad laboral permanente;
* listas extensas de tecnologías;
* más de cuatro enlaces;
* animaciones;
* múltiples slogans;
* badges técnicos;
* claims no demostrables.

---

## 23.14 Acceptance Criteria

* [ ] El nombre se identifica inmediatamente.
* [ ] El posicionamiento se comprende en menos de diez segundos.
* [ ] El tagline complementa el rol sin repetirlo.
* [ ] El contenido esencial existe fuera de la imagen.
* [ ] Los enlaces principales funcionan.
* [ ] La sección funciona en light y dark mode.
* [ ] Resulta legible en móvil.
* [ ] No ocupa una extensión desproporcionada.
* [ ] No contiene elementos decorativos innecesarios.

---

# 24. About Me

La sección `About Me` ofrecerá contexto humano y profesional.

---

## 24.1 Purpose

Explicar brevemente:

* trayectoria profesional;
* áreas de especialización;
* forma de trabajar;
* valor diferencial;
* dirección de crecimiento.

No deberá reproducir LinkedIn ni el CV.

---

## 24.2 User Question

> ¿Qué experiencia, mentalidad y orientación profesional hay detrás de este perfil?

---

## 24.3 Narrative Objectives

La sección deberá comunicar que Fran:

* desarrolla aplicaciones backend, full stack y de IA;
* trabaja principalmente con Java y Python;
* posee experiencia previa en comunicación y gestión de proyectos;
* valora arquitectura, documentación y mantenibilidad;
* continúa creciendo hacia sistemas más complejos y aplicaciones impulsadas por IA.

---

## 24.4 Narrative Strategy

El texto deberá construirse en tres movimientos.

### Present

Qué hace actualmente.

### Differentiation

Qué aporta su trayectoria transversal y cómo trabaja.

### Direction

Hacia qué áreas técnicas está evolucionando.

---

## 24.5 Recommended Structure

```text
Paragraph 1
Current professional identity and main development areas.

Paragraph 2
Engineering approach and transferable experience.

Paragraph 3
Current growth direction and professional interests.
```

La versión definitiva podrá condensarse en dos párrafos si mejora el ritmo.

---

## 24.6 Content Guidance

El texto podrá incluir de forma natural:

* backend systems;
* full stack applications;
* AI-powered solutions;
* Java;
* Spring Boot;
* Python;
* architecture;
* documentation;
* testing;
* maintainability;
* enterprise environments;
* multidisciplinary background.

No todos los conceptos deberán aparecer necesariamente.

---

## 24.7 Differentiation

La trayectoria anterior en comunicación, dirección y gestión de proyectos deberá presentarse como una capacidad complementaria.

No deberá interpretarse como una justificación defensiva del cambio profesional.

El mensaje deberá transmitir que aporta:

* comunicación;
* comprensión de necesidades;
* coordinación;
* visión de producto;
* documentación;
* trabajo con equipos;
* orientación a objetivos.

---

## 24.8 Tone

El texto estará redactado:

* en primera persona;
* con seguridad;
* sin grandilocuencia;
* con inglés natural;
* evitando exceso de adjetivos;
* priorizando verbos de acción.

---

## 24.9 Length

Extensión recomendada:

```text
100–150 palabras
```

Máximo:

```text
180 palabras
```

---

## 24.10 Links

No deberá incluir más de uno o dos enlaces contextuales.

Los proyectos se enlazarán en el portfolio, no en cada mención del About.

---

## 24.11 Maintenance

Revisión recomendada:

```text
Cada 6–12 meses
```

También deberá revisarse si cambia:

* posicionamiento;
* experiencia profesional;
* dirección de carrera;
* especialización principal.

---

## 24.12 Restrictions

No incluir:

* cronología completa;
* fechas;
* lista de estudios;
* lista de empleadores;
* edad;
* información personal irrelevante;
* explicación extensa del proceso de reconversión;
* frases como “I am passionate about technology”;
* afirmaciones de experto;
* más de tres párrafos.

---

## 24.13 Acceptance Criteria

* [ ] Presenta con claridad la identidad actual.
* [ ] Backend, Full Stack e IA aparecen de forma equilibrada.
* [ ] La experiencia transversal aporta valor al relato.
* [ ] Explica cómo trabaja, no solo qué tecnologías conoce.
* [ ] Mantiene una extensión breve.
* [ ] No duplica el CV.
* [ ] Suena natural en inglés.
* [ ] Puede mantenerse válida durante varios años.

---

# 25. Current Focus

La sección `Current Focus` mostrará las prioridades técnicas actuales.

---

## 25.1 Purpose

Conectar la identidad estable con el trabajo y aprendizaje presentes.

---

## 25.2 User Question

> ¿En qué está trabajando y profundizando actualmente?

---

## 25.3 Content Categories

La sección podrá cubrir:

* desarrollo backend;
* full stack;
* IA aplicada;
* arquitectura;
* cloud;
* sistemas distribuidos;
* testing;
* automatización;
* proyectos open source.

---

## 25.4 Initial Content Direction

La primera versión debería reflejar aproximadamente:

```text
Java and Spring Boot backend development
Maintainable full stack applications
AI-powered applications, LLMs and RAG
Software architecture, testing and delivery
```

El texto definitivo deberá referirse a capacidades reales en desarrollo y no a una lista aspiracional.

---

## 25.5 Structure

Formato recomendado:

```markdown
## Current Focus

- Building backend services with Java and Spring Boot.
- Developing maintainable full stack applications.
- Exploring AI-powered applications, LLMs and retrieval-augmented generation.
- Improving architecture, testing and software delivery practices.
```

---

## 25.6 Number of Items

Mínimo:

```text
3
```

Máximo:

```text
4
```

---

## 25.7 Length

Cada punto deberá ocupar:

```text
Una línea o una frase breve
```

No deberán incluirse sublistas.

---

## 25.8 Maintenance

Revisión:

```text
Cada 3–6 meses
```

Un elemento deberá modificarse cuando:

* deje de representar trabajo activo;
* cambie la prioridad profesional;
* se consolide y pase a formar parte estable de la identidad;
* aparezca un foco estratégico más relevante.

---

## 25.9 Confidentiality

No deberá mencionar:

* tickets;
* nombres internos;
* repositorios privados;
* proyectos confidenciales;
* arquitecturas empresariales;
* clientes;
* problemas internos;
* información protegida.

La experiencia profesional se describirá mediante capacidades generales.

---

## 25.10 Restrictions

No incluir:

* tareas semanales;
* cursos menores;
* tecnologías estudiadas superficialmente;
* objetivos personales no técnicos;
* más de cuatro focos;
* estados temporales como “currently fixing...”;
* información que quede obsoleta en pocas semanas.

---

## 25.11 Acceptance Criteria

* [ ] Refleja prioridades reales.
* [ ] Incluye como máximo cuatro puntos.
* [ ] Puede mantenerse varios meses.
* [ ] Complementa el About.
* [ ] No repite el Technology Stack.
* [ ] No expone información confidencial.
* [ ] Muestra evolución sin alterar la identidad principal.

---

# 26. Engineering Portfolio

La sección `Engineering Portfolio` constituirá la evidencia principal del perfil.

---

## 26.1 Purpose

Presentar una selección curada de proyectos que demuestren:

* capacidades técnicas;
* variedad de dominios;
* profundidad;
* documentación;
* arquitectura;
* evolución;
* calidad de ejecución.

---

## 26.2 User Question

> ¿Qué proyectos demuestran realmente estas capacidades?

---

## 26.3 Section Name

Nombre definitivo recomendado:

```text
Engineering Portfolio
```

Se prefiere frente a:

```text
Featured Projects
My Projects
Portfolio
```

porque comunica una selección profesional y técnica.

---

## 26.4 Portfolio Size

Primera versión:

```text
4–6 proyectos
```

Cantidad inicial recomendada:

```text
5 proyectos
```

Esto permite:

* representar backend;
* mostrar full stack;
* incluir IA;
* demostrar documentación y arquitectura;
* reservar espacio para evolución.

---

## 26.5 Initial Candidate Projects

La selección inicial deberá evaluar:

### NovaCoquinaria

Capacidades potenciales:

* knowledge systems;
* documentation architecture;
* semantic relationships;
* automation;
* Python tooling;
* quality validation.

### OnlyFilm

Capacidades potenciales:

* Java;
* Spring Boot;
* web application;
* layered architecture;
* testing;
* domain workflows.

### Aula Robótica

Capacidades potenciales:

* Python;
* FastAPI;
* SQLAlchemy;
* RBAC;
* modular architecture;
* real-world management platform.

### Cognitiva AI

Capacidades potenciales:

* machine learning;
* deep learning;
* medical imaging;
* model evaluation;
* data analysis;
* experimentation.

### Dental Clinic

Capacidades potenciales:

* full stack;
* Spring Boot;
* Angular;
* authentication;
* role management;
* relational database.

La selección definitiva dependerá de:

* visibilidad pública;
* estado;
* calidad documental;
* coherencia;
* posibilidad de enlazar;
* ausencia de información sensible.

---

## 26.6 Portfolio Narrative

El conjunto deberá contar una historia.

Orden conceptual recomendado:

1. Proyecto más representativo del posicionamiento actual.
2. Proyecto backend sólido.
3. Proyecto full stack.
4. Proyecto de IA.
5. Proyecto de arquitectura o plataforma.
6. Proyecto futuro diferencial.

El orden definitivo no deberá depender únicamente de la fecha.

---

## 26.7 Featured Project Strategy

Podrá existir un proyecto visualmente destacado.

El proyecto destacado deberá:

* representar el nivel actual;
* estar suficientemente maduro;
* tener documentación sólida;
* diferenciarse;
* poder mantenerse;
* disponer de preview o arquitectura clara.

La primera versión podrá evitar esta jerarquía si todos los proyectos utilizan tarjetas equivalentes.

---

## 26.8 Project Card Content

Cada tarjeta deberá incluir:

```text
Project Name
One- or two-sentence description
3–5 technologies or concepts
Repository link
Optional documentation or demo link
```

---

## 26.9 Project Description Formula

La descripción deberá responder:

```text
What it is
+
What problem it addresses
+
What makes it technically relevant
```

Ejemplo conceptual:

```text
A movie booking platform built with Spring Boot and Thymeleaf, featuring tested domain workflows, authentication and a maintainable layered architecture.
```

---

## 26.10 Technology Labels

Se seleccionarán entre tres y cinco elementos.

Podrán representar:

* lenguajes;
* frameworks;
* arquitectura;
* dominio;
* calidad.

Ejemplo:

```text
Java · Spring Boot · Thymeleaf · JUnit · Layered Architecture
```

No deberán convertirse necesariamente en badges.

El formato se decidirá durante la implementación.

---

## 26.11 Links

Cada proyecto deberá enlazar al repositorio.

Enlaces adicionales posibles:

* Documentation;
* Live Demo;
* Architecture;
* Latest Release.

No se mostrarán enlaces inexistentes ni temporales.

---

## 26.12 Visual Layout

Se evaluarán dos implementaciones.

### Option A — Vertical Cards

Cada proyecto ocupa una sección breve.

Ventajas:

* máxima compatibilidad;
* buena lectura móvil;
* fácil mantenimiento;
* más espacio descriptivo.

### Option B — Two-Column HTML Table

Dos proyectos por fila.

Ventajas:

* menor longitud;
* apariencia de portfolio;
* comparación visual.

Riesgos:

* comportamiento móvil;
* HTML más complejo;
* tarjetas estrechas;
* problemas de alineación.

Decisión inicial recomendada:

```text
Vertical or hybrid layout
```

La implementación deberá probarse en GitHub antes de decidir.

---

## 26.13 Project Order Maintenance

Revisión cuando:

* un proyecto alcance mayor madurez;
* aparezca un proyecto estratégico;
* un repositorio quede obsoleto;
* cambie el posicionamiento;
* un proyecto deje de ser público;
* dos proyectos resulten redundantes.

---

## 26.14 Restrictions

No incluir:

* repositorios no públicos;
* proyectos con README insuficiente;
* ejercicios básicos;
* forks sin contribución relevante;
* proyectos abandonados sin contexto;
* más de seis proyectos;
* tarjetas con descripciones extensas;
* información empresarial confidencial;
* tecnologías sin relación directa con el proyecto.

---

## 26.15 Acceptance Criteria

* [ ] Incluye entre cuatro y seis proyectos.
* [ ] Cada proyecto aporta una historia diferente.
* [ ] Backend, Full Stack e IA están representados.
* [ ] Todos los enlaces funcionan.
* [ ] Cada repositorio tiene documentación suficiente.
* [ ] Las descripciones explican valor y relevancia.
* [ ] Las tecnologías están limitadas.
* [ ] El orden resulta estratégico.
* [ ] La sección funciona en móvil.
* [ ] Ningún proyecto expone información sensible.

---

# 27. Technology Stack

La sección `Technology Stack` mostrará las principales capacidades técnicas agrupadas por dominio.

---

## 27.1 Purpose

Permitir una identificación rápida de tecnologías relevantes sin convertir el perfil en un inventario completo.

---

## 27.2 User Question

> ¿Con qué tecnologías y herramientas trabaja habitualmente?

---

## 27.3 Category Architecture

Categorías iniciales:

```text
Backend
Frontend
AI & Data
Databases
Cloud & DevOps
Testing & Tools
```

---

## 27.4 Backend

Candidatos:

```text
Java
Spring Boot
Python
Django
FastAPI
Node.js
NestJS
```

La selección final deberá priorizar las tecnologías más representativas.

---

## 27.5 Frontend

Candidatos:

```text
Angular
React
TypeScript
JavaScript
HTML
CSS
Bootstrap
Thymeleaf
```

No será necesario mostrar todas.

---

## 27.6 AI & Data

Candidatos:

```text
TensorFlow
scikit-learn
pandas
NumPy
LightGBM
XGBoost
OpenCV
Jupyter
```

LLM, RAG y agentes deberán incorporarse cuando existan proyectos públicos suficientemente representativos.

---

## 27.7 Databases

Candidatos:

```text
PostgreSQL
MySQL
SQL Server
Oracle
MongoDB
SQLite
DB2
```

Se priorizarán entre cuatro y seis.

---

## 27.8 Cloud & DevOps

Candidatos:

```text
Docker
Kubernetes
AWS
GitHub Actions
GitLab CI
Maven
Linux
```

Las herramientas empresariales internas no deberán mostrarse si no aportan valor público o no pueden contextualizarse.

---

## 27.9 Testing & Tools

Candidatos:

```text
JUnit
PyTest
Postman
Selenium
Git
GitHub
IntelliJ IDEA
VS Code
```

Podrá estudiarse si Maven pertenece a Cloud & DevOps o Testing & Tools.

---

## 27.10 Selection Levels

Las tecnologías podrán clasificarse internamente como:

```text
Primary
Working Knowledge
Exploring
Historical
```

El Profile README mostrará principalmente:

```text
Primary
+
Selected Working Knowledge
```

No se mostrarán tecnologías en fase meramente exploratoria como si fueran capacidades consolidadas.

---

## 27.11 Icon Implementation

Podrá utilizarse `skillicons.dev` para aquellas tecnologías compatibles.

Cuando no exista un icono o resulte ambiguo, podrá utilizarse:

* Simple Icons;
* texto;
* SVG propio;
* exclusión del elemento.

No se mezclarán estilos sin una razón clara.

---

## 27.12 Labels

Los iconos deberán acompañarse de:

* encabezado de categoría;
* alt text;
* nombres visibles cuando sea necesario.

No deberá asumirse que todos los visitantes reconocen todos los logotipos.

---

## 27.13 Quantity

Objetivo total:

```text
20–35 tecnologías
```

Esto no significa que todas las categorías deban tener el mismo número.

Recomendación:

```text
4–7 por categoría
```

---

## 27.14 Ordering

Dentro de cada categoría:

1. Tecnologías principales.
2. Tecnologías secundarias.
3. Herramientas complementarias.

No se utilizará orden alfabético si reduce la prioridad visual.

---

## 27.15 Maintenance

Revisión:

```text
Cada 6 meses
```

Una tecnología podrá añadirse cuando:

* exista experiencia práctica;
* aparezca en un proyecto;
* sea relevante para el posicionamiento;
* tenga continuidad.

Podrá eliminarse cuando:

* deje de ser representativa;
* solo tenga valor histórico;
* genere ruido;
* no pueda respaldarse con evidencia.

---

## 27.16 Restrictions

No incluir:

* sistemas operativos básicos sin relevancia;
* suites ofimáticas;
* tecnologías utilizadas únicamente en ejercicios elementales;
* herramientas internas no públicas;
* más de siete elementos por categoría;
* tecnologías futuras sin evidencia;
* ratings subjetivos;
* barras de porcentaje;
* estrellas de nivel.

---

## 27.17 Acceptance Criteria

* [ ] Las tecnologías están agrupadas por dominio.
* [ ] El stack refleja el posicionamiento.
* [ ] Existen evidencias para las tecnologías principales.
* [ ] La cantidad resulta controlada.
* [ ] Los iconos mantienen un estilo coherente.
* [ ] El contenido dispone de alt text.
* [ ] La sección funciona sin reconocer cada logotipo.
* [ ] No utiliza porcentajes ni niveles arbitrarios.
* [ ] Puede actualizarse sin modificar la arquitectura.

---

# 28. Engineering Principles

La sección `Engineering Principles` sintetizará la forma de trabajar definida en `01_BRAND.md`.

---

## 28.1 Purpose

Mostrar de forma breve cómo se aplican los valores profesionales al desarrollo de software.

---

## 28.2 User Question

> ¿Qué principios guían su trabajo técnico?

---

## 28.3 Content Direction

Los principios deberán girar alrededor de:

* architecture;
* maintainability;
* documentation;
* testing;
* simplicity;
* continuous improvement.

---

## 28.4 Initial Candidate Statements

```text
Architecture before unnecessary complexity.
Documentation as part of the product.
Maintainable code over short-term shortcuts.
Testing as a design and confidence tool.
Clear solutions before clever solutions.
Continuous learning through real projects.
```

La redacción final deberá evitar un tono dogmático.

---

## 28.5 Number of Principles

Mínimo:

```text
4
```

Máximo:

```text
6
```

---

## 28.6 Structure

Formato recomendado:

```markdown
## Engineering Principles

- Architecture before unnecessary complexity.
- Documentation as part of the product.
- Maintainable code over short-term shortcuts.
- Testing as a design and confidence tool.
- Continuous improvement through real projects.
```

Podrá diseñarse una presentación más visual si no aumenta el ruido.

---

## 28.7 Evidence Relationship

Los principios deberán poder comprobarse al explorar:

* arquitectura de repositorios;
* documentación;
* tests;
* ADR;
* releases;
* automatización;
* estructura del código.

No deberán formularse principios que el portfolio contradiga.

---

## 28.8 Maintenance

Esta sección será estable.

Solo deberá modificarse si cambia significativamente la filosofía profesional.

---

## 28.9 Restrictions

No incluir:

* más de seis frases;
* explicaciones largas;
* valores genéricos como “work hard”;
* claims empresariales;
* principios no demostrados;
* citas de terceros;
* frases motivacionales.

---

## 28.10 Acceptance Criteria

* [ ] Contiene entre cuatro y seis principios.
* [ ] Los principios son concretos.
* [ ] Pueden observarse en los proyectos.
* [ ] No repiten literalmente `01_BRAND.md`.
* [ ] No alargan excesivamente el perfil.
* [ ] Mantienen vigencia a largo plazo.

---

# 29. GitHub Activity

La sección `GitHub Activity` mostrará métricas complementarias.

---

## 29.1 Purpose

Aportar contexto sobre actividad y distribución técnica sin desplazar el foco de los proyectos.

---

## 29.2 User Question

> ¿Qué actividad pública y patrones generales pueden observarse en GitHub?

---

## 29.3 Candidate Widgets

Podrán evaluarse:

* GitHub Stats;
* Top Languages;
* Contribution Graph;
* Profile Details;
* Productive Time;
* Repository Summary.

---

## 29.4 Maximum Widgets

La primera versión utilizará:

```text
0–2 widgets
```

La ausencia de widgets será preferible a utilizar servicios poco fiables.

---

## 29.5 Preferred Initial Combination

Opción inicial:

```text
GitHub Stats
+
Top Languages
```

Sin embargo, `Top Languages` deberá interpretarse con cautela, ya que mide volumen de código y no dominio técnico.

Podrá reemplazarse por un único widget de actividad si la composición resulta más limpia.

---

## 29.6 Widget Selection Criteria

Un widget deberá:

* cargar de forma fiable;
* funcionar en dark y light mode;
* ofrecer alt text;
* no incluir métricas engañosas;
* ser mantenido;
* permitir configuración visual;
* integrarse con la paleta;
* no dominar la página.

---

## 29.7 Metric Interpretation

Las métricas no deberán presentarse como medida directa de competencia.

No se utilizarán textos como:

```text
My strongest languages
Expertise
Productivity score
Developer ranking
```

---

## 29.8 Placement

La sección aparecerá:

```text
Después de Engineering Principles
Antes de Let's Connect
```

---

## 29.9 Maintenance

Revisión trimestral:

* carga;
* tema;
* estabilidad;
* utilidad;
* cambios del proveedor;
* posibles errores.

---

## 29.10 Restrictions

No incluir:

* streaks como elemento central;
* visitor counter;
* trophies;
* rankings;
* más de dos widgets;
* métricas redundantes;
* gráficos que fallen frecuentemente;
* estadísticas anteriores al portfolio.

---

## 29.11 Acceptance Criteria

* [ ] Utiliza como máximo dos widgets.
* [ ] Los widgets aportan contexto.
* [ ] No desplazan el foco de los proyectos.
* [ ] Funcionan en ambos temas.
* [ ] El perfil sigue siendo comprensible si fallan.
* [ ] No presentan métricas como evidencia de dominio.
* [ ] Mantienen coherencia visual.

---

# 30. Let's Connect

La sección `Let's Connect` cerrará el recorrido principal del perfil.

---

## 30.1 Purpose

Ofrecer canales profesionales claros para iniciar una conversación.

---

## 30.2 User Question

> ¿Cómo puedo contactar con Fran Ramirez o consultar más información profesional?

---

## 30.3 Primary Channels

La primera versión incluirá:

```text
LinkedIn
Email
```

Podrán añadirse posteriormente:

```text
Portfolio
CV
Technical Blog
```

---

## 30.4 Content Tone

El texto deberá ser abierto y profesional.

Ejemplo conceptual:

```text
I'm always open to connecting with developers, technical teams and people interested in backend, full stack and AI-powered software.
```

El mensaje deberá evitar parecer una solicitud genérica de empleo permanente.

---

## 30.5 Structure

Opción textual:

```markdown
## Let's Connect

I'm always open to discussing software engineering, backend development and AI-powered applications.

[LinkedIn](...) · [Email](mailto:...)
```

Opción con badges discretos:

```html
<a href="...">
  <img alt="LinkedIn" src="...">
</a>
<a href="mailto:...">
  <img alt="Email" src="...">
</a>
```

La implementación deberá elegir una sola estrategia.

---

## 30.6 Email Privacy

Antes de publicar un email deberá decidirse:

* utilizar correo personal;
* crear correo profesional específico;
* usar una dirección protegida;
* enlazar únicamente LinkedIn inicialmente.

La dirección no deberá incluirse hasta disponer de una opción adecuada para exposición pública.

---

## 30.7 Length

Extensión:

```text
1–3 líneas
```

---

## 30.8 Maintenance

Revisión cuando cambie:

* LinkedIn;
* email;
* portfolio;
* disponibilidad pública;
* canales profesionales.

---

## 30.9 Restrictions

No incluir:

* teléfono;
* dirección física;
* redes inactivas;
* canales personales;
* múltiples llamadas a la acción;
* calendarios públicos sin necesidad;
* formularios externos;
* mensajes urgentes;
* información sobre disponibilidad que quede obsoleta.

---

## 30.10 Acceptance Criteria

* [ ] LinkedIn funciona.
* [ ] El canal de email es apropiado para exposición pública.
* [ ] La sección ocupa pocas líneas.
* [ ] El tono es profesional y cercano.
* [ ] No parece una llamada comercial agresiva.
* [ ] No expone información personal innecesaria.

---

# 31. Optional Footer

El `Footer` podrá utilizarse como cierre editorial discreto.

---

## 31.1 Purpose

Reforzar mantenimiento, autoría o acceso al idioma alternativo sin añadir ruido.

---

## 31.2 Candidate Content

Podrá incluir:

* autoría;
* última actualización;
* idioma;
* pequeña firma;
* marca compacta.

Ejemplo:

```markdown
---

<p align="center">
  Designed and maintained by Fran Ramirez.
</p>
```

---

## 31.3 Initial Decision

Estado:

```text
Optional
```

La primera implementación deberá evaluarse sin footer.

Solo se añadirá si mejora el cierre del documento.

---

## 31.4 Restrictions

No incluir:

* slogan repetido;
* widgets;
* badges;
* enlaces redundantes;
* información técnica;
* contador;
* animación.

---

## 31.5 Acceptance Criteria

* [ ] Aporta un cierre real.
* [ ] No repite el Hero.
* [ ] No ocupa demasiado espacio.
* [ ] Mantiene tono discreto.
* [ ] Puede eliminarse sin afectar la comprensión.

---

# 32. Cross-Section Relationships

Las secciones deberán complementarse sin duplicarse.

---

## 32.1 Hero and About

El Hero define.

El About explica.

El About no deberá repetir literalmente el posicionamiento y el tagline.

---

## 32.2 About and Current Focus

El About describe una identidad relativamente estable.

Current Focus describe prioridades temporales.

---

## 32.3 Portfolio and Technology Stack

El Portfolio demuestra.

Technology Stack resume.

Las tecnologías deberán estar respaldadas principalmente por proyectos o experiencia.

---

## 32.4 Engineering Principles and Brand Strategy

Engineering Principles sintetiza `01_BRAND.md`.

No deberá reproducir su contenido completo.

---

## 32.5 Portfolio and GitHub Activity

El Portfolio tendrá prioridad.

Las estadísticas solo complementarán la evidencia.

---

## 32.6 Hero and Contact

El Hero podrá incluir enlaces rápidos.

Let's Connect podrá contextualizar la invitación al contacto.

No deberán utilizar exactamente la misma composición visual.

---

# 33. Section Maintenance Matrix

| Section                |           Review Frequency | Expected Stability |
| ---------------------- | -------------------------: | ------------------ |
| Language Switch        | On every structural change | High               |
| Hero                   |                6–12 months | High               |
| About Me               |                6–12 months | High               |
| Current Focus          |                 3–6 months | Medium             |
| Engineering Portfolio  |                 3–6 months | Medium             |
| Technology Stack       |                   6 months | Medium             |
| Engineering Principles |                     Annual | Very High          |
| GitHub Activity        |                  Quarterly | Low                |
| Let's Connect          |                   6 months | High               |
| Footer                 |                     Annual | High               |

---

# 34. Section Priority Matrix

| Section                | Recruiter Value | Technical Value | Maintenance Cost | Initial Priority |
| ---------------------- | --------------: | --------------: | ---------------: | ---------------: |
| Hero                   |        Critical |            High |              Low |         Required |
| About Me               |        Critical |            High |              Low |         Required |
| Current Focus          |            High |            High |           Medium |         Required |
| Engineering Portfolio  |        Critical |        Critical |           Medium |         Required |
| Technology Stack       |        Critical |            High |           Medium |         Required |
| Engineering Principles |          Medium |            High |              Low |         Required |
| GitHub Activity        |             Low |          Medium |           Medium |         Optional |
| Let's Connect          |            High |             Low |              Low |         Required |
| Footer                 |             Low |             Low |              Low |         Optional |

---

# 35. Section Definition of Done

Una sección se considerará preparada para publicación cuando:

* [ ] Tiene un propósito único.
* [ ] Responde a una pregunta concreta.
* [ ] Su contenido está redactado en inglés natural.
* [ ] Existe una versión española equivalente.
* [ ] Respeta la longitud definida.
* [ ] No duplica otras secciones.
* [ ] Todos los enlaces funcionan.
* [ ] El contenido está respaldado por evidencias.
* [ ] No contiene información confidencial.
* [ ] Mantiene coherencia visual.
* [ ] Funciona en móvil.
* [ ] Puede mantenerse con esfuerzo razonable.
* [ ] Cumple sus criterios de aceptación específicos.


---

# 36. Editorial System

El Profile README deberá mantener una voz coherente en todas sus secciones y versiones lingüísticas.

La redacción no se tratará como una fase secundaria.

Formará parte de la arquitectura del perfil, ya que determina cómo se perciben:

* la experiencia;
* la madurez profesional;
* la claridad de pensamiento;
* la capacidad de comunicación;
* la coherencia entre identidad y proyectos.

El sistema editorial deberá permitir que distintas secciones parezcan escritas por la misma persona, incluso cuando se actualicen en momentos diferentes.

---

## 36.1 Editorial Objectives

Toda redacción deberá perseguir los siguientes objetivos:

* comunicar con claridad;
* mantener credibilidad;
* facilitar el escaneo;
* evitar exageraciones;
* sonar natural;
* reforzar el posicionamiento profesional;
* diferenciar hechos, objetivos e intereses;
* mantener coherencia entre idiomas.

---

## 36.2 Editorial Priorities

El orden de prioridad será:

1. Exactitud.
2. Claridad.
3. Credibilidad.
4. Naturalidad.
5. Concisión.
6. Elegancia.

Una frase más elegante no deberá sustituir a otra más precisa.

---

# 37. Voice

La voz representa la personalidad estable del perfil.

Deberá mantenerse constante en:

* Hero;
* About;
* Current Focus;
* Project Cards;
* Engineering Principles;
* Contact;
* versiones inglesa y española.

---

## 37.1 Voice Attributes

La voz será:

### Professional

Transmitirá madurez sin sonar rígida.

### Technical

Utilizará terminología precisa cuando resulte necesaria.

### Clear

Evitará frases innecesariamente complejas.

### Confident

Presentará capacidades reales con seguridad.

### Honest

No exagerará experiencia, dominio o resultados.

### Thoughtful

Explicará decisiones y valor, no solo herramientas.

### International

Será comprensible para una audiencia diversa.

---

## 37.2 Voice Balance

La voz deberá situarse entre dos extremos.

No deberá ser excesivamente informal:

```text
I love coding cool stuff and trying new tech.
```

Tampoco excesivamente corporativa:

```text
I leverage cutting-edge technologies to deliver scalable, high-impact digital solutions.
```

Se preferirá:

```text
I build backend, full stack and AI-powered applications with a strong focus on architecture, maintainability and clear documentation.
```

---

# 38. Tone

El tono podrá variar ligeramente según la sección sin alterar la voz general.

---

## 38.1 Hero Tone

Características:

* directo;
* breve;
* seguro;
* reconocible.

No deberá explicar ni justificar.

---

## 38.2 About Tone

Características:

* profesional;
* cercano;
* reflexivo;
* personal sin resultar íntimo.

---

## 38.3 Current Focus Tone

Características:

* activo;
* concreto;
* orientado a evolución;
* actualizado.

---

## 38.4 Portfolio Tone

Características:

* factual;
* técnico;
* orientado a valor;
* basado en evidencias.

---

## 38.5 Engineering Principles Tone

Características:

* claro;
* estable;
* no dogmático;
* coherente con los proyectos.

---

## 38.6 Contact Tone

Características:

* abierto;
* profesional;
* natural;
* no comercial.

---

# 39. Writing Style

La escritura deberá priorizar frases claras y estructuras sencillas.

---

## 39.1 Sentence Length

Se preferirán frases de extensión corta o media.

Objetivo orientativo:

```text
12–24 palabras por frase
```

Podrán utilizarse frases más largas cuando la claridad no se vea afectada.

---

## 39.2 Paragraph Length

Los párrafos deberán contener:

```text
2–4 frases
```

Se evitarán bloques visualmente densos.

---

## 39.3 Active Voice

Se priorizará la voz activa.

Preferido:

```text
I design and build maintainable backend systems.
```

Evitar:

```text
Maintainable backend systems are designed and built by me.
```

---

## 39.4 Strong Verbs

Se priorizarán verbos concretos como:

* build;
* design;
* develop;
* document;
* test;
* automate;
* improve;
* integrate;
* analyze;
* maintain;
* explore;
* deliver.

Se limitarán verbos vagos como:

* work with;
* deal with;
* do;
* handle;
* use;

cuando exista una alternativa más precisa.

---

## 39.5 First Person

El About, Current Focus y Contact se redactarán principalmente en primera persona.

Las Project Cards podrán utilizar una voz descriptiva neutral.

Ejemplo:

```text
NovaCoquinaria is a structured culinary knowledge system...
```

No será necesario comenzar todas las frases con `I`.

---

## 39.6 Contractions

En inglés podrán utilizarse contracciones naturales de forma limitada:

```text
I'm
I've
I'm currently
```

No se abusará de ellas.

El tono no deberá parecer excesivamente conversacional.

---

# 40. English Language Standard

El inglés será el idioma principal del Profile README.

La redacción deberá sonar natural para una audiencia técnica internacional.

---

## 40.1 English Variant

Se utilizará inglés internacional neutro.

Podrá seguirse mayoritariamente la convención estadounidense por coherencia con el sector tecnológico y GitHub.

Ejemplos:

```text
organization
behavior
analyze
```

La consistencia será más importante que la variante elegida.

---

## 40.2 Technical Terminology

Se utilizarán términos ampliamente reconocidos:

```text
backend
full stack
software architecture
maintainability
testing
deployment
machine learning
AI-powered applications
```

No se traducirán ni reformularán términos técnicos consolidados de forma innecesaria.

---

## 40.3 Natural English

Se evitarán traducciones literales desde el español.

Ejemplos a evitar:

```text
I have formation in...
I realize applications...
I dispose of experience...
Actually I am working in...
```

Se preferirá:

```text
I have experience in...
I build applications...
I am currently working on...
My background includes...
```

---

## 40.4 Professional Titles

Se mantendrá:

```text
Backend • Full Stack • AI Developer
```

No deberá alternarse sin motivo con:

```text
Programmer
Coder
IT Developer
Computer Engineer
Web Developer
```

`Software Engineer` podrá utilizarse como identidad general en el About.

---

## 40.5 AI Terminology

Se utilizará:

```text
AI
Artificial Intelligence
AI-powered applications
Machine Learning
Deep Learning
LLMs
RAG
```

Deberá evitarse presentar como experiencia consolidada cualquier área que todavía se encuentre en exploración.

---

## 40.6 Articles and Prepositions

La revisión final deberá prestar atención especial a:

* artículos;
* preposiciones;
* plurales;
* tiempos verbales;
* concordancia;
* collocations técnicas.

El inglés deberá revisarse por naturalidad, no solo por corrección gramatical.

---

# 41. Spanish Language Standard

La versión española deberá ser equivalente en calidad, estructura y contenido.

No deberá funcionar como una traducción automática visible.

---

## 41.1 Spanish Variant

Se utilizará español de España con redacción comprensible para una audiencia internacional.

Se evitarán localismos innecesarios.

---

## 41.2 Technical Terminology

Podrán mantenerse en inglés términos consolidados como:

* backend;
* full stack;
* framework;
* stack;
* testing;
* deployment;
* machine learning;
* deep learning;
* roadmap;
* release;
* pull request.

Cuando exista una alternativa española natural, podrá utilizarse.

La consistencia deberá mantenerse entre secciones.

---

## 41.3 Translation Strategy

La traducción seguirá el sentido, tono y función del texto.

No se exigirá equivalencia palabra por palabra.

Ejemplo:

```text
Building scalable applications with Java, Python and AI.
```

Podrá traducirse como:

```text
Construyo aplicaciones escalables con Java, Python e inteligencia artificial.
```

o:

```text
Desarrollo aplicaciones escalables con Java, Python e inteligencia artificial.
```

La elección deberá responder al tono general, no a una traducción literal.

---

## 41.4 Professional Positioning

Decisión inicial:

```text
Backend • Full Stack • AI Developer
```

se mantendrá sin traducir en ambas versiones.

Razones:

* identidad internacional;
* consistencia visual;
* reconocimiento profesional;
* sincronización con banner y LinkedIn.

---

## 41.5 Spanish Style

Se evitará un tono excesivamente formal o administrativo.

No se utilizarán expresiones como:

```text
El abajo firmante dispone de experiencia...
```

Se preferirá una redacción directa:

```text
Desarrollo aplicaciones backend, full stack y soluciones impulsadas por inteligencia artificial.
```

---

# 42. Translation Governance

Las versiones inglesa y española deberán mantenerse sincronizadas.

---

## 42.1 Source Language

La versión inglesa será la referencia editorial principal.

Esto no implica que la versión española deba ser menos cuidada.

---

## 42.2 Translation Workflow

Proceso recomendado:

```text
English Draft
↓
English Review
↓
Spanish Translation
↓
Spanish Naturalness Review
↓
Cross-Language Consistency Check
↓
Publication
```

---

## 42.3 Synchronized Elements

Deberán mantenerse idénticos en ambas versiones:

* estructura;
* orden;
* proyectos;
* enlaces;
* tecnologías;
* estados;
* número de principios;
* widgets;
* activos;
* fecha de actualización cuando exista.

---

## 42.4 Permitted Adaptations

Podrán variar:

* longitud de frases;
* orden interno de una oración;
* expresiones idiomáticas;
* formulación de una llamada al contacto;
* traducción de nombres de sección cuando resulte natural.

---

## 42.5 Translation Drift

Se considerará drift cuando:

* una versión contenga proyectos ausentes en la otra;
* cambie el posicionamiento;
* existan enlaces distintos;
* se mantenga información obsoleta;
* una versión sea claramente más extensa;
* un principio tenga un significado diferente.

El drift deberá corregirse antes de considerar completada una actualización.

---

# 43. Terminology System

El README deberá mantener un vocabulario estable.

---

## 43.1 Canonical Terms

Se utilizarán de forma preferente:

| Concept             | Canonical Term                      |
| ------------------- | ----------------------------------- |
| Identidad principal | Software Engineer                   |
| Posicionamiento     | Backend • Full Stack • AI Developer |
| Proyectos           | Engineering Portfolio               |
| Tecnologías         | Technology Stack                    |
| Principios          | Engineering Principles              |
| Actividad           | GitHub Activity                     |
| Contacto            | Let's Connect                       |
| Foco actual         | Current Focus                       |
| Arquitectura        | Software Architecture               |
| Mantenibilidad      | Maintainability                     |
| Documentación       | Documentation                       |
| IA aplicada         | AI-powered applications             |

---

## 43.2 Avoided Variants

Se evitará alternar innecesariamente:

```text
Tech Stack / Skills / Technologies / Tools
Projects / Featured Projects / Portfolio / Work
About / Profile / Bio / Introduction
```

Cada concepto tendrá un nombre estable.

---

## 43.3 Project Naming

Los proyectos deberán aparecer siempre con su nombre oficial.

No se traducirán nombres propios salvo que exista una versión oficial.

Ejemplos:

```text
NovaCoquinaria
OnlyFilm
Cognitiva AI
```

---

# 44. Claim Policy

Toda afirmación profesional deberá cumplir criterios de credibilidad.

---

## 44.1 Supported Claims

Podrán afirmarse capacidades respaldadas por:

* experiencia profesional;
* proyectos públicos;
* formación relevante;
* documentación;
* código;
* resultados;
* releases;
* tests;
* demos.

---

## 44.2 Claim Levels

### Demonstrated

Existe evidencia pública clara.

### Experienced

Existe experiencia profesional o práctica significativa.

### Familiar

Existe conocimiento y uso limitado.

### Exploring

Área activa de aprendizaje.

El README deberá comunicar principalmente:

```text
Demonstrated
+
Experienced
```

`Exploring` podrá aparecer únicamente en Current Focus.

---

## 44.3 Prohibited Claims

Se evitarán:

* expert;
* specialist, cuando no exista profundidad suficiente;
* senior;
* architect, como rol actual no ejercido;
* production-ready, sin validación real;
* enterprise-grade, sin contexto;
* highly scalable, sin evidencia;
* cutting-edge;
* world-class;
* advanced, como adjetivo genérico.

---

## 44.4 Quantitative Claims

Toda cifra deberá:

* ser verificable;
* disponer de contexto;
* mantenerse actualizada;
* aportar valor.

Ejemplo válido:

```text
58 automated tests
```

si el repositorio permite verificarlo.

No se utilizarán cifras únicamente para impresionar.

---

# 45. Confidentiality and Professional Boundaries

El Profile README no deberá exponer información confidencial, interna o sensible.

---

## 45.1 Professional Experience

Podrán mencionarse de forma general:

* enterprise environments;
* backend development;
* CI/CD;
* testing;
* APIs;
* databases;
* team collaboration.

No deberán exponerse:

* nombres internos;
* tickets;
* repositorios corporativos;
* endpoints;
* arquitectura confidencial;
* credenciales;
* herramientas internas no públicas;
* datos de clientes;
* incidencias concretas.

---

## 45.2 Company Names

Las empresas podrán mencionarse únicamente cuando:

* la relación sea pública;
* aparezcan en LinkedIn o CV;
* exista autorización o contexto legítimo;
* no se asocien a información interna.

El About no necesitará enumerar empleadores.

---

## 45.3 Personal Data

No se publicarán:

* teléfono;
* dirección;
* DNI;
* fecha de nacimiento;
* información económica;
* documentos personales;
* ubicación precisa.

La ubicación se limitará a:

```text
Madrid, Spain
```

---

# 46. Markdown Implementation Rules

La implementación deberá priorizar Markdown nativo.

---

## 46.1 Native Markdown First

Se utilizará Markdown para:

* encabezados;
* párrafos;
* listas;
* enlaces;
* tablas simples;
* citas;
* código;
* separadores.

---

## 46.2 Allowed HTML

Podrá utilizarse HTML compatible con GitHub para:

* alineación;
* imágenes responsive;
* `picture`;
* enlaces con imágenes;
* bloques centrados;
* tablas visuales limitadas;
* detalles no resueltos por Markdown.

---

## 46.3 HTML Restrictions

No se utilizarán:

* estilos inline complejos;
* CSS externo;
* JavaScript;
* iframes;
* formularios;
* componentes interactivos no compatibles;
* HTML difícil de mantener;
* etiquetas obsoletas.

---

## 46.4 Heading Structure

La jerarquía deberá ser:

```text
# Profile Title, únicamente si se utiliza fuera del banner
## Main Sections
### Project Names or Subsections
```

No se saltarán niveles sin una razón.

Si el nombre se representa visualmente sin `#`, las secciones podrán comenzar en `##`.

---

## 46.5 Horizontal Rules

Los separadores `---` se utilizarán de forma limitada.

Preferencias:

* después del Hero;
* antes del Contact;
* para separar bloques realmente distintos.

No deberán aparecer entre todas las secciones.

---

## 46.6 Tables

Las tablas se limitarán a información comparativa.

No se utilizarán para maquetar texto largo salvo que una prueba real demuestre una buena adaptación móvil.

---

# 47. Link Rules

Los enlaces forman parte de la experiencia editorial.

---

## 47.1 Descriptive Labels

Se utilizarán etiquetas como:

```text
View Repository
Read Documentation
Explore Architecture
Open Demo
Latest Release
```

---

## 47.2 Link Density

Se limitará el número de enlaces por bloque.

Recomendación:

```text
1–3 enlaces por Project Card
```

---

## 47.3 External Links

Los enlaces externos deberán apuntar a:

* LinkedIn;
* demo;
* documentación;
* portfolio;
* recursos verificables.

No se utilizarán acortadores.

---

## 47.4 Internal Links

Se utilizarán rutas relativas para:

* assets;
* README.es.md;
* documentación dentro del repositorio;
* imágenes;
* diagramas.

---

## 47.5 Link Validation

Antes de publicar deberá comprobarse:

* URL;
* protocolo HTTPS;
* destino;
* permisos;
* estabilidad;
* ausencia de redirecciones innecesarias.

---

# 48. Image and Alt Text Rules

Toda imagen deberá tener una función y un texto alternativo adecuado.

---

## 48.1 Alt Text Objectives

El alt text deberá explicar:

* qué representa;
* qué información relevante contiene;
* por qué aparece.

---

## 48.2 Banner Alt Text

Ejemplo:

```text
Fran Ramirez — Backend, Full Stack and AI Developer
```

No será necesario describir todos los nodos decorativos.

---

## 48.3 Project Preview Alt Text

Ejemplo:

```text
OnlyFilm movie booking workflow and application interface
```

---

## 48.4 Decorative Images

Si una imagen es puramente decorativa, deberá evaluarse si realmente es necesaria.

El sistema visual evita recursos sin función.

---

# 49. Accessibility Rules

La accesibilidad deberá mantenerse durante toda la implementación.

---

## 49.1 Semantic Structure

Se utilizarán:

* encabezados jerárquicos;
* listas reales;
* enlaces descriptivos;
* alt text;
* orden lógico.

---

## 49.2 Readability

Se evitarán:

* bloques centrados extensos;
* mayúsculas prolongadas;
* exceso de cursiva;
* filas de iconos sin contexto;
* imágenes con texto diminuto;
* tablas anchas;
* contrastes bajos.

---

## 49.3 Color Independence

La información no dependerá únicamente de:

* color;
* saturación;
* icono;
* posición.

Deberá existir texto suficiente para comprenderla.

---

## 49.4 Motion

La primera versión no utilizará animaciones.

Cualquier incorporación futura deberá respetar preferencias de movimiento reducido y aportar información real.

---

# 50. Search and Discoverability

El README deberá facilitar que visitantes y buscadores comprendan el perfil.

No se aplicará una estrategia SEO agresiva.

---

## 50.1 Natural Keywords

Podrán aparecer de forma natural:

* Backend Developer;
* Full Stack Developer;
* AI Developer;
* Java;
* Spring Boot;
* Python;
* Software Architecture;
* Machine Learning;
* REST APIs;
* Cloud;
* Testing.

---

## 50.2 Keyword Restrictions

No se repetirán tecnologías artificialmente.

No se añadirán listas ocultas ni bloques orientados exclusivamente a buscadores.

---

## 50.3 Repository Discoverability

La visibilidad dependerá principalmente de:

* descripciones;
* topics;
* README;
* nombres;
* enlaces;
* proyectos fijados.

---

# 51. Date and Freshness Policy

El perfil deberá comunicar actualidad sin mostrar información innecesariamente temporal.

---

## 51.1 Visible Dates

No se mostrará una fecha global de última actualización en la primera versión salvo que aporte valor.

---

## 51.2 Time-Sensitive Content

Se limitará a:

* Current Focus;
* estado de proyectos;
* releases;
* disponibilidad profesional, si se decide incluir.

---

## 51.3 Stale Content

Deberá eliminarse o actualizarse cuando:

* deje de ser cierto;
* dependa de una tecnología abandonada;
* un proyecto ya no esté activo;
* un enlace desaparezca;
* un objetivo se haya completado.

---

# 52. Maintenance Workflow

Toda actualización deberá seguir un proceso común.

---

## 52.1 Change Types

### Editorial

Cambios de redacción.

### Structural

Cambios de sección u orden.

### Portfolio

Alta, baja o reordenación de proyectos.

### Technical

Cambios de stack o herramientas.

### Visual

Cambios de banner, iconos o widgets.

### Contact

Cambios de enlaces profesionales.

---

## 52.2 Standard Update Process

```text
Identify Change
↓
Update English Version
↓
Update Spanish Version
↓
Validate Links
↓
Validate Mobile Layout
↓
Validate Dark and Light Mode
↓
Review Claims
↓
Publish
```

---

## 52.3 Structural Changes

Un cambio estructural deberá actualizar:

* `03_README_ARCHITECTURE.md`;
* `README.md`;
* `README.es.md`;
* plantillas relacionadas;
* checklist de mantenimiento.

---

## 52.4 Project Changes

Al añadir un proyecto deberá:

* superar auditoría;
* tener descripción;
* disponer de enlaces;
* contar con evidencia;
* sustituir o complementar una capacidad;
* actualizar ambas versiones;
* revisar el orden narrativo.

---

# 53. Review Checklist

Antes de publicar una actualización deberá verificarse:

## Editorial

* [ ] ¿El texto es claro?
* [ ] ¿Suena natural?
* [ ] ¿Evita exageraciones?
* [ ] ¿Utiliza terminología consistente?
* [ ] ¿Mantiene una voz común?

## English

* [ ] ¿Evita traducciones literales?
* [ ] ¿Utiliza tiempos verbales correctamente?
* [ ] ¿La terminología técnica es natural?
* [ ] ¿La puntuación es consistente?

## Spanish

* [ ] ¿Suena natural?
* [ ] ¿Mantiene el mismo significado?
* [ ] ¿Evita calcos innecesarios?
* [ ] ¿Conserva el tono?

## Claims

* [ ] ¿Las afirmaciones tienen evidencia?
* [ ] ¿Las áreas en exploración se presentan como tales?
* [ ] ¿Las cifras son verificables?
* [ ] ¿No se atribuye un nivel inexistente?

## Structure

* [ ] ¿Se mantiene el orden aprobado?
* [ ] ¿Cada sección conserva una responsabilidad?
* [ ] ¿No existen duplicaciones?
* [ ] ¿La longitud sigue controlada?

## Links and Assets

* [ ] ¿Todos los enlaces funcionan?
* [ ] ¿Las imágenes cargan?
* [ ] ¿El alt text es adecuado?
* [ ] ¿Los widgets funcionan?
* [ ] ¿Las rutas relativas son correctas?

## Accessibility

* [ ] ¿Los encabezados son jerárquicos?
* [ ] ¿La lectura móvil resulta correcta?
* [ ] ¿El texto esencial existe fuera de las imágenes?
* [ ] ¿La información no depende del color?

## Synchronization

* [ ] ¿README.md está actualizado?
* [ ] ¿README.es.md está actualizado?
* [ ] ¿Los proyectos coinciden?
* [ ] ¿Los enlaces coinciden?
* [ ] ¿El orden coincide?

---

# 54. Editorial Acceptance Criteria

El sistema editorial se considerará correctamente aplicado cuando:

* [ ] El inglés suena natural y profesional.
* [ ] El español mantiene calidad equivalente.
* [ ] La voz es consistente en todas las secciones.
* [ ] Los claims están respaldados.
* [ ] La terminología es estable.
* [ ] La estructura utiliza Markdown semántico.
* [ ] El HTML se limita a necesidades reales.
* [ ] Los enlaces son descriptivos.
* [ ] Todas las imágenes tienen alt text.
* [ ] El contenido respeta límites de confidencialidad.
* [ ] Las dos versiones permanecen sincronizadas.
* [ ] El perfil puede mantenerse con un flujo claro.

---

# 55. Implementation Blueprint

La implementación del GitHub Profile README deberá realizarse como un proceso incremental.

No se construirá directamente una versión final completa.

Cada bloque se diseñará, redactará, validará e integrará de forma independiente antes de continuar con el siguiente.

El objetivo será reducir retrabajo, detectar problemas visuales pronto y mantener sincronizadas las versiones inglesa y española desde el inicio.

---

## 55.1 Implementation Principles

La construcción deberá respetar los siguientes principios:

* implementar primero la estructura;
* validar antes de decorar;
* mantener el contenido esencial en Markdown;
* incorporar dependencias externas únicamente cuando aporten valor;
* probar cada sección en GitHub;
* priorizar la versión móvil;
* mantener sincronizados ambos idiomas;
* evitar optimizaciones prematuras;
* utilizar componentes definidos en `02_VISUAL_IDENTITY.md`;
* registrar cambios estructurales relevantes.

---

## 55.2 Source Files

La implementación principal estará formada por:

```text
github-profile/
├── README.md
├── README.es.md
├── assets/
│   ├── brand/
│   │   ├── banner-dark.svg
│   │   ├── banner-light.svg
│   │   └── mark.svg
│   ├── projects/
│   ├── diagrams/
│   └── icons/
├── docs/
│   ├── 01_BRAND.md
│   ├── 02_VISUAL_IDENTITY.md
│   └── 03_README_ARCHITECTURE.md
└── templates/
```

La ubicación definitiva de los documentos podrá adaptarse al repositorio real del perfil.

---

# 56. README Structural Template

La siguiente plantilla representa la estructura canónica de la primera versión.

No contiene todavía el contenido editorial definitivo.

---

## 56.1 English Template

```markdown
<p align="right">
  <strong>English</strong> ·
  <a href="./README.es.md">Español</a>
</p>

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="./assets/brand/banner-dark.svg"
  >
  <source
    media="(prefers-color-scheme: light)"
    srcset="./assets/brand/banner-light.svg"
  >
  <img
    src="./assets/brand/banner-light.svg"
    alt="Fran Ramirez — Backend, Full Stack and AI Developer"
    width="100%"
  >
</picture>

<h1 align="center">Fran Ramirez</h1>

<p align="center">
  <strong>Backend • Full Stack • AI Developer</strong>
</p>

<p align="center">
  Building scalable applications with Java, Python and AI.
</p>

<p align="center">
  Madrid, Spain ·
  <a href="LINKEDIN_URL">LinkedIn</a> ·
  <a href="mailto:EMAIL_ADDRESS">Email</a>
</p>

---

## About Me

[ABOUT_CONTENT]

## Current Focus

- [FOCUS_ITEM_1]
- [FOCUS_ITEM_2]
- [FOCUS_ITEM_3]
- [FOCUS_ITEM_4]

## Engineering Portfolio

### [PROJECT_NAME]

[PROJECT_DESCRIPTION]

`TECHNOLOGY` · `TECHNOLOGY` · `TECHNOLOGY`

[View Repository](REPOSITORY_URL) · [Read Documentation](DOCUMENTATION_URL)

### [PROJECT_NAME]

[PROJECT_DESCRIPTION]

`TECHNOLOGY` · `TECHNOLOGY` · `TECHNOLOGY`

[View Repository](REPOSITORY_URL)

## Technology Stack

### Backend

[BACKEND_ICONS_OR_LABELS]

### Frontend

[FRONTEND_ICONS_OR_LABELS]

### AI & Data

[AI_DATA_ICONS_OR_LABELS]

### Databases

[DATABASE_ICONS_OR_LABELS]

### Cloud & DevOps

[CLOUD_DEVOPS_ICONS_OR_LABELS]

### Testing & Tools

[TESTING_TOOLS_ICONS_OR_LABELS]

## Engineering Principles

- [PRINCIPLE_1]
- [PRINCIPLE_2]
- [PRINCIPLE_3]
- [PRINCIPLE_4]
- [OPTIONAL_PRINCIPLE_5]

## GitHub Activity

[OPTIONAL_WIDGET_1]

[OPTIONAL_WIDGET_2]

---

## Let's Connect

[CONTACT_TEXT]

[LinkedIn](LINKEDIN_URL) · [Email](mailto:EMAIL_ADDRESS)

[OPTIONAL_FOOTER]
```

---

## 56.2 Spanish Template

```markdown
<p align="right">
  <a href="./README.md">English</a> ·
  <strong>Español</strong>
</p>

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="./assets/brand/banner-dark.svg"
  >
  <source
    media="(prefers-color-scheme: light)"
    srcset="./assets/brand/banner-light.svg"
  >
  <img
    src="./assets/brand/banner-light.svg"
    alt="Fran Ramirez — Backend, Full Stack y AI Developer"
    width="100%"
  >
</picture>

<h1 align="center">Fran Ramirez</h1>

<p align="center">
  <strong>Backend • Full Stack • AI Developer</strong>
</p>

<p align="center">
  Desarrollo aplicaciones escalables con Java, Python e inteligencia artificial.
</p>

<p align="center">
  Madrid, España ·
  <a href="LINKEDIN_URL">LinkedIn</a> ·
  <a href="mailto:EMAIL_ADDRESS">Email</a>
</p>

---

## Sobre mí

[ABOUT_CONTENT_ES]

## Foco actual

- [FOCUS_ITEM_1_ES]
- [FOCUS_ITEM_2_ES]
- [FOCUS_ITEM_3_ES]
- [FOCUS_ITEM_4_ES]

## Portfolio de ingeniería

### [PROJECT_NAME]

[PROJECT_DESCRIPTION_ES]

`TECHNOLOGY` · `TECHNOLOGY` · `TECHNOLOGY`

[Ver repositorio](REPOSITORY_URL) · [Leer documentación](DOCUMENTATION_URL)

## Stack tecnológico

### Backend

[BACKEND_ICONS_OR_LABELS]

### Frontend

[FRONTEND_ICONS_OR_LABELS]

### IA y datos

[AI_DATA_ICONS_OR_LABELS]

### Bases de datos

[DATABASE_ICONS_OR_LABELS]

### Cloud y DevOps

[CLOUD_DEVOPS_ICONS_OR_LABELS]

### Testing y herramientas

[TESTING_TOOLS_ICONS_OR_LABELS]

## Principios de ingeniería

- [PRINCIPLE_1_ES]
- [PRINCIPLE_2_ES]
- [PRINCIPLE_3_ES]
- [PRINCIPLE_4_ES]
- [OPTIONAL_PRINCIPLE_5_ES]

## Actividad en GitHub

[OPTIONAL_WIDGET_1]

[OPTIONAL_WIDGET_2]

---

## Conectemos

[CONTACT_TEXT_ES]

[LinkedIn](LINKEDIN_URL) · [Email](mailto:EMAIL_ADDRESS)

[OPTIONAL_FOOTER]
```

---

# 57. Implementation Phases

La construcción del README se dividirá en fases funcionales.

Cada fase deberá validarse antes de iniciar la siguiente.

---

## Phase 1 — Repository Foundation

Objetivos:

* crear o preparar el repositorio especial de perfil;
* añadir la estructura documental;
* crear directorios de activos;
* confirmar rutas;
* definir estrategia de ramas;
* validar que GitHub renderiza correctamente el README.

Entregables:

```text
README.md
README.es.md
assets/
docs/
templates/
```

Criterios de salida:

* el repositorio es accesible;
* ambos README renderizan;
* los enlaces entre idiomas funcionan;
* las rutas relativas son válidas.

---

## Phase 2 — Brand Assets

Objetivos:

* crear banner oscuro;
* crear banner claro;
* crear marca compacta;
* validar proporciones;
* validar tipografía;
* comprobar light y dark mode;
* optimizar SVG.

Entregables:

```text
assets/brand/banner-dark.svg
assets/brand/banner-light.svg
assets/brand/mark.svg
```

Criterios de salida:

* los activos cargan correctamente;
* el texto es legible;
* ambos temas mantienen coherencia;
* no existen fuentes externas obligatorias;
* el peso resulta razonable.

---

## Phase 3 — Hero

Objetivos:

* integrar el banner;
* añadir nombre;
* añadir posicionamiento;
* añadir tagline;
* añadir enlaces principales;
* validar duplicación visual;
* revisar adaptación móvil.

Criterios de salida:

* la identidad se comprende en menos de diez segundos;
* el Hero resulta legible sin imágenes;
* los enlaces funcionan;
* no existe ruido visual;
* la altura inicial resulta proporcionada.

---

## Phase 4 — Core Narrative

Objetivos:

* redactar About Me;
* redactar Current Focus;
* revisar voz;
* traducir al español;
* comprobar ausencia de duplicaciones;
* verificar confidencialidad.

Criterios de salida:

* la narrativa refleja la identidad real;
* la versión inglesa suena natural;
* la versión española es equivalente;
* el contenido no reproduce el CV;
* Current Focus puede mantenerse varios meses.

---

## Phase 5 — Engineering Portfolio

Objetivos:

* auditar proyectos candidatos;
* seleccionar entre cuatro y seis;
* ordenar la narrativa;
* redactar descripciones;
* seleccionar tecnologías;
* validar enlaces;
* decidir layout;
* preparar previews si se utilizan.

Criterios de salida:

* cada proyecto aporta una evidencia distinta;
* backend, full stack e IA están representados;
* todos los repositorios son públicos;
* los README de destino tienen calidad suficiente;
* ningún enlace está roto;
* la sección funciona en móvil.

---

## Phase 6 — Technology Stack

Objetivos:

* clasificar tecnologías;
* eliminar elementos poco representativos;
* agrupar por dominio;
* elegir fuente de iconos;
* generar alt text;
* revisar densidad;
* probar fallos del servicio externo.

Criterios de salida:

* el stack está alineado con los proyectos;
* no aparece como inventario indiscriminado;
* las categorías son comprensibles;
* los iconos mantienen coherencia;
* la información sigue siendo interpretable si no cargan.

---

## Phase 7 — Principles and Activity

Objetivos:

* redactar Engineering Principles;
* verificar su relación con proyectos;
* evaluar widgets;
* decidir si se incluye GitHub Activity;
* configurar temas;
* comprobar estabilidad.

Criterios de salida:

* existen entre cuatro y seis principios;
* ningún principio resulta grandilocuente;
* se utilizan como máximo dos widgets;
* el perfil funciona aunque fallen;
* las estadísticas no preceden al portfolio.

---

## Phase 8 — Contact and Closure

Objetivos:

* definir mensaje final;
* seleccionar canales;
* decidir email público;
* añadir enlaces;
* evaluar footer;
* revisar recorrido completo.

Criterios de salida:

* el contacto es claro;
* no expone datos innecesarios;
* la llamada a la conversación es profesional;
* el cierre no repite el Hero;
* el footer se incluye únicamente si aporta valor.

---

## Phase 9 — Cross-Language Synchronization

Objetivos:

* comparar ambos archivos;
* revisar secciones;
* revisar orden;
* revisar enlaces;
* revisar tecnologías;
* revisar proyectos;
* validar naturalidad.

Criterios de salida:

* no existe translation drift;
* ambas versiones ofrecen la misma información;
* las adaptaciones lingüísticas mantienen el mismo propósito;
* el selector funciona en ambas direcciones.

---

## Phase 10 — Publication Review

Objetivos:

* validar GitHub Desktop;
* validar GitHub Mobile;
* validar light mode;
* validar dark mode;
* revisar accesibilidad;
* verificar enlaces;
* revisar claims;
* corregir errores;
* publicar versión inicial.

Entregable:

```text
v1.0.0
```

---

# 58. Project Selection Workflow

La selección del Engineering Portfolio deberá seguir un proceso explícito.

---

## 58.1 Candidate Inventory

Se elaborará una lista con:

* nombre;
* URL;
* estado;
* visibilidad;
* dominio;
* stack;
* documentación;
* testing;
* arquitectura;
* diferenciación;
* mantenimiento;
* confidencialidad;
* valor para recruiters;
* valor para Tech Leads.

---

## 58.2 Evaluation Criteria

Cada proyecto podrá evaluarse de 1 a 5 en:

| Criterion           | Description                                |
| ------------------- | ------------------------------------------ |
| Strategic Alignment | Refuerza Backend, Full Stack o IA          |
| Technical Depth     | Muestra decisiones y complejidad relevante |
| Documentation       | Permite comprender y reproducir            |
| Engineering Quality | Testing, arquitectura, mantenibilidad      |
| Differentiation     | Aporta una historia distinta               |
| Visual Readiness    | Puede presentarse profesionalmente         |
| Maintenance         | Está activo o estable                      |
| Public Safety       | No contiene información sensible           |

---

## 58.3 Selection Rule

No se seleccionarán automáticamente los proyectos con mayor puntuación total.

El portfolio deberá mantener equilibrio entre:

* especialidades;
* tecnologías;
* dominios;
* tipos de producto;
* niveles de madurez;
* narrativa profesional.

---

## 58.4 Replacement Rule

Un proyecto nuevo podrá sustituir a otro cuando:

* represente mejor el nivel actual;
* muestre una capacidad ausente;
* tenga mayor madurez;
* reduzca redundancia;
* esté mejor documentado;
* se alinee mejor con los objetivos futuros.

---

# 59. Technology Selection Workflow

La inclusión de tecnologías deberá seguir un proceso similar.

---

## 59.1 Technology Inventory

Cada tecnología se clasificará según:

```text
Primary
Working Knowledge
Exploring
Historical
```

---

## 59.2 Inclusion Criteria

Una tecnología podrá incluirse cuando cumpla al menos uno de estos criterios:

* uso profesional;
* uso significativo en un proyecto público;
* formación extensa con práctica demostrable;
* relevancia central para el posicionamiento;
* continuidad prevista.

---

## 59.3 Exclusion Criteria

Se excluirá cuando:

* solo se haya utilizado superficialmente;
* no tenga evidencia;
* haya quedado obsoleta para el posicionamiento;
* duplique otra herramienta;
* reduzca la claridad;
* se incluya únicamente para aumentar cantidad.

---

## 59.4 Review Rule

Una tecnología en `Exploring` no deberá presentarse como parte estable del stack.

Podrá aparecer en Current Focus hasta alcanzar evidencia suficiente.

---

# 60. Widget Evaluation Framework

Los widgets deberán superar una evaluación previa.

---

## 60.1 Evaluation Criteria

| Criterion      | Question                                     |
| -------------- | -------------------------------------------- |
| Value          | ¿Aporta información relevante?               |
| Reliability    | ¿Carga de forma consistente?                 |
| Maintenance    | ¿El servicio está mantenido?                 |
| Accessibility  | ¿Incluye alt text y contraste?               |
| Theme Support  | ¿Funciona en light y dark?                   |
| Independence   | ¿El README sigue siendo comprensible sin él? |
| Visual Fit     | ¿Se integra con la identidad?                |
| Interpretation | ¿Puede malinterpretarse?                     |

---

## 60.2 Approval Rule

Un widget solo se incorporará si:

* aporta más valor que coste;
* no duplica información;
* no domina la página;
* mantiene fiabilidad razonable;
* puede eliminarse sin romper la estructura.

---

## 60.3 Initial Status

| Widget Type        | Initial Decision    |
| ------------------ | ------------------- |
| GitHub Stats       | Evaluate            |
| Top Languages      | Evaluate carefully  |
| Contribution Graph | Optional            |
| Streak             | Excluded            |
| Trophies           | Excluded            |
| Visitor Counter    | Excluded            |
| Snake              | Excluded            |
| Typing SVG         | Excluded by default |

---

# 61. Testing Strategy

El README deberá probarse como cualquier otro entregable técnico.

---

## 61.1 Rendering Tests

Validar:

* Markdown;
* HTML permitido;
* encabezados;
* tablas;
* enlaces;
* imágenes;
* saltos;
* alineación;
* listas;
* bloques de código.

---

## 61.2 Device Tests

Validar en:

* escritorio ancho;
* portátil;
* tablet;
* móvil;
* ventana reducida.

GitHub no permite controlar todos los breakpoints, por lo que se priorizarán estructuras simples.

---

## 61.3 Theme Tests

Validar:

* dark default;
* dark high contrast, cuando sea posible;
* light default;
* comportamiento de `picture`;
* visibilidad de bordes;
* contraste del texto;
* integración de widgets.

---

## 61.4 Failure Tests

Simular o considerar:

* banner no disponible;
* Skill Icons no disponible;
* widget estadístico no disponible;
* enlace externo caído;
* preview inexistente.

La lectura principal deberá conservar sentido.

---

## 61.5 Content Tests

Revisar:

* ortografía;
* gramática;
* naturalidad;
* consistencia terminológica;
* afirmaciones;
* confidencialidad;
* vigencia;
* sincronización.

---

## 61.6 Link Tests

Verificar:

* enlaces internos;
* rutas relativas;
* enlaces a repositorios;
* documentación;
* LinkedIn;
* correo;
* demos;
* releases.

---

## 61.7 Accessibility Tests

Comprobar:

* orden de encabezados;
* alt text;
* enlaces descriptivos;
* ausencia de texto esencial solo en imágenes;
* contraste;
* legibilidad móvil;
* ausencia de animaciones.

---

# 62. Validation Environments

La validación deberá realizarse preferentemente en:

```text
GitHub Web
GitHub Mobile Web
Local Markdown Preview
VS Code Preview
Light Theme
Dark Theme
```

El resultado renderizado por GitHub tendrá prioridad frente a previews locales.

---

# 63. Quality Gates

La publicación deberá superar varios niveles.

---

## Gate 1 — Content

* identidad correcta;
* claims respaldados;
* inglés revisado;
* español revisado;
* confidencialidad validada.

---

## Gate 2 — Structure

* orden aprobado;
* secciones completas;
* longitud controlada;
* ausencia de duplicaciones;
* arquitectura respetada.

---

## Gate 3 — Visual

* banner correcto;
* iconos coherentes;
* espaciado suficiente;
* densidad adecuada;
* light y dark mode validados.

---

## Gate 4 — Technical

* Markdown válido;
* HTML compatible;
* enlaces correctos;
* imágenes disponibles;
* rutas correctas;
* servicios externos operativos.

---

## Gate 5 — Accessibility

* encabezados;
* alt text;
* contraste;
* enlaces descriptivos;
* móvil;
* contenido independiente de imágenes.

---

## Gate 6 — Portfolio

* proyectos auditados;
* orden estratégico;
* repositorios públicos;
* documentación suficiente;
* ausencia de información sensible.

---

## Gate 7 — Synchronization

* inglés y español equivalentes;
* enlaces coincidentes;
* proyectos coincidentes;
* stack coincidente;
* activos compartidos.

---

# 64. Global Acceptance Criteria

La primera versión del Profile README se considerará aceptable cuando:

* [ ] La identidad se comprende en menos de diez segundos.
* [ ] El posicionamiento aparece de forma clara.
* [ ] El tagline resulta coherente y creíble.
* [ ] El About aporta contexto sin reproducir el CV.
* [ ] Current Focus refleja prioridades reales.
* [ ] El portfolio contiene entre cuatro y seis proyectos.
* [ ] Cada proyecto demuestra una capacidad diferente.
* [ ] Backend, Full Stack e IA están representados.
* [ ] El stack está agrupado y curado.
* [ ] Los principios pueden observarse en los repositorios.
* [ ] Se utilizan como máximo dos widgets.
* [ ] Los canales de contacto son adecuados.
* [ ] El perfil funciona en modo claro.
* [ ] El perfil funciona en modo oscuro.
* [ ] El perfil funciona en móvil.
* [ ] El contenido esencial no depende de servicios externos.
* [ ] Todas las imágenes tienen alt text.
* [ ] Todos los enlaces funcionan.
* [ ] No existe información confidencial.
* [ ] Las versiones inglesa y española están sincronizadas.
* [ ] La estructura puede mantenerse durante varios años.

---

# 65. Definition of Done

El proyecto del Profile README se considerará finalizado en su primera versión cuando:

## Documentation

* [ ] `01_BRAND.md` está estable.
* [ ] `02_VISUAL_IDENTITY.md` está estable.
* [ ] `03_README_ARCHITECTURE.md` está estable.
* [ ] Las decisiones relevantes están documentadas.

## Brand Assets

* [ ] Existe banner dark.
* [ ] Existe banner light.
* [ ] Existe alt text.
* [ ] Los SVG están optimizados.
* [ ] Los activos están versionados.

## English README

* [ ] El Hero está implementado.
* [ ] El About está aprobado.
* [ ] Current Focus está actualizado.
* [ ] El Engineering Portfolio está completo.
* [ ] El Technology Stack está validado.
* [ ] Engineering Principles está aprobado.
* [ ] GitHub Activity está decidido.
* [ ] Let's Connect está implementado.

## Spanish README

* [ ] Mantiene la misma estructura.
* [ ] Mantiene los mismos proyectos.
* [ ] Mantiene los mismos enlaces.
* [ ] Mantiene el mismo stack.
* [ ] Suena natural.
* [ ] No contiene drift.

## Portfolio

* [ ] Los proyectos están auditados.
* [ ] Los repositorios tienen README suficiente.
* [ ] Las descripciones están redactadas.
* [ ] Los enlaces funcionan.
* [ ] Los repositorios fijados están seleccionados.

## Quality

* [ ] Light mode validado.
* [ ] Dark mode validado.
* [ ] Desktop validado.
* [ ] Mobile validado.
* [ ] Markdown validado.
* [ ] Accesibilidad revisada.
* [ ] Servicios externos revisados.
* [ ] Confidencialidad revisada.

## Publication

* [ ] El repositorio especial tiene el nombre correcto.
* [ ] El README se muestra en el perfil.
* [ ] La versión inicial está etiquetada.
* [ ] El changelog o historial registra la publicación.
* [ ] El mantenimiento futuro está definido.

---

# 66. Release Strategy

La primera publicación utilizará:

```text
v1.0.0
```

Representará:

* identidad consolidada;
* estructura completa;
* contenido bilingüe;
* banner funcional;
* portfolio inicial;
* stack curado;
* enlaces validados.

---

## 66.1 Patch Releases

Ejemplos:

```text
v1.0.1
v1.0.2
```

Para:

* correcciones;
* enlaces;
* ortografía;
* pequeños ajustes visuales;
* optimización de activos.

---

## 66.2 Minor Releases

Ejemplos:

```text
v1.1.0
v1.2.0
```

Para:

* nuevo proyecto;
* nuevo componente;
* nueva sección compatible;
* mejora de banner;
* nuevo canal profesional;
* nuevo bloque de actividad.

---

## 66.3 Major Releases

Ejemplos:

```text
v2.0.0
```

Para:

* cambio de posicionamiento;
* nueva arquitectura;
* rediseño profundo;
* cambio de identidad;
* reestructuración incompatible.

---

# 67. Maintenance Plan

El README requerirá un mantenimiento limitado pero regular.

---

## 67.1 Monthly Review

Solo cuando exista actividad relevante:

* comprobar enlaces;
* revisar widgets;
* corregir errores visibles.

No será necesaria una revisión mensual formal si no hay cambios.

---

## 67.2 Quarterly Review

Revisar:

* Current Focus;
* Engineering Portfolio;
* widgets;
* repositorios fijados;
* enlaces;
* estado de proyectos;
* light y dark mode.

---

## 67.3 Semiannual Review

Revisar:

* About;
* Technology Stack;
* posicionamiento;
* proyectos estratégicos;
* coherencia con LinkedIn;
* versión española.

---

## 67.4 Annual Review

Revisar:

* arquitectura global;
* identidad;
* banner;
* principios;
* componentes;
* dependencias externas;
* proyectos archivados;
* evolución profesional.

---

# 68. Change Checklist

Al introducir un cambio deberá comprobarse:

* [ ] ¿Afecta al posicionamiento?
* [ ] ¿Afecta a la arquitectura?
* [ ] ¿Afecta a ambos idiomas?
* [ ] ¿Afecta al banner?
* [ ] ¿Afecta a proyectos?
* [ ] ¿Afecta al stack?
* [ ] ¿Afecta a enlaces?
* [ ] ¿Requiere actualizar documentación?
* [ ] ¿Requiere nueva versión?
* [ ] ¿Requiere revisión visual?
* [ ] ¿Introduce una dependencia?
* [ ] ¿Aumenta el mantenimiento?

---

# 69. Immediate Implementation Backlog

Una vez aprobado este documento, el trabajo continuará en este orden.

---

## Critical

* [ ] Consolidar `03_README_ARCHITECTURE.md`.
* [ ] Confirmar estructura definitiva del repositorio.
* [ ] Crear directorios `assets/brand`.
* [ ] Diseñar `banner-dark.svg`.
* [ ] Diseñar `banner-light.svg`.
* [ ] Implementar el Hero.
* [ ] Confirmar LinkedIn.
* [ ] Decidir email público.

---

## High

* [ ] Redactar About Me en inglés.
* [ ] Redactar About Me en español.
* [ ] Definir Current Focus.
* [ ] Auditar proyectos candidatos.
* [ ] Seleccionar Engineering Portfolio.
* [ ] Redactar Project Cards.
* [ ] Clasificar Technology Stack.

---

## Medium

* [ ] Evaluar Skill Icons.
* [ ] Evaluar GitHub Stats.
* [ ] Diseñar marca compacta.
* [ ] Definir footer.
* [ ] Crear previews de proyectos.
* [ ] Preparar plantilla de mantenimiento.

---

## Deferred

* [ ] Engineering Journey.
* [ ] Open Source Contributions.
* [ ] Blog.
* [ ] Portfolio web.
* [ ] Certificaciones.
* [ ] Disponibilidad profesional permanente.
* [ ] Timeline.
* [ ] Animaciones.

---

# 70. Final Architecture Decisions

Quedan consolidadas las siguientes decisiones:

1. El Profile README será una landing page profesional.
2. El inglés será el idioma principal.
3. Existirá una versión española equivalente.
4. La estructura será lineal y de una columna.
5. El Hero será la primera sección principal.
6. El portfolio aparecerá antes del stack.
7. Se mostrarán entre cuatro y seis proyectos.
8. El stack se agrupará por dominios.
9. Los principios estarán respaldados por proyectos.
10. GitHub Activity será opcional.
11. Se utilizarán como máximo dos widgets.
12. No se utilizará tabla de contenidos.
13. No se incluirá historial laboral completo.
14. No se incluirán certificaciones como sección.
15. Engineering Journey queda aplazado.
16. El contenido esencial será textual.
17. El banner tendrá variantes clara y oscura.
18. La accesibilidad será un requisito.
19. La confidencialidad será un quality gate.
20. Las dos versiones se actualizarán conjuntamente.
21. Los proyectos deberán superar una auditoría.
22. La arquitectura deberá mantenerse estable.
23. Las actualizaciones normales afectarán al contenido, no a la estructura.
24. El README se publicará inicialmente como `v1.0.0`.

---

# 71. Revision History

| Version | Date       | Description                                                     |
| ------- | ---------- | --------------------------------------------------------------- |
| 1.0.0   | 2026-08-05 | Primera versión completa de la arquitectura del Profile README. |

---

# Appendix A — Canonical Profile Identity

```text
Fran Ramirez

Backend • Full Stack • AI Developer

Building scalable applications with Java, Python and AI.
```

---

# Appendix B — Canonical Section Order

```text
Language Switch
Hero
About Me
Current Focus
Engineering Portfolio
Technology Stack
Engineering Principles
GitHub Activity
Let's Connect
Optional Footer
```

---

# Appendix C — Quick Architecture Test

Antes de añadir contenido al Profile README deberá comprobarse:

1. ¿Ayuda a comprender quién es Fran?
2. ¿Refuerza Backend, Full Stack o IA?
3. ¿Aporta evidencia?
4. ¿Está mejor situado en un repositorio?
5. ¿Duplica información?
6. ¿Puede mantenerse?
7. ¿Funciona en móvil?
8. ¿Funciona sin servicios externos?
9. ¿Puede traducirse y sincronizarse?
10. ¿Seguirá siendo relevante dentro de varios años?

Si no supera estas preguntas, no deberá incorporarse al README.
