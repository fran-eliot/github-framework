# 04 - REPOSITORY AUDIT

| Field              | Value                       |
| ------------------ | --------------------------- |
| **Project**        | GitHub Professional Profile |
| **Document**       | Repository Portfolio Audit  |
| **Version**        | 1.0.0 (Draft)               |
| **Status**         | In Progress                 |
| **Owner**          | Fran Ramirez                |
| **Audit Date**     | 2026-08-05                  |
| **GitHub Account** | `fran-eliot`                |

---

> La calidad de un portfolio no depende del número de repositorios publicados, sino de la claridad con la que una selección reducida demuestra capacidades profesionales relevantes.

Este documento audita el ecosistema público de repositorios de **Fran Ramirez** con el objetivo de:

* identificar los proyectos con mayor valor profesional;
* seleccionar el futuro `Engineering Portfolio`;
* decidir qué repositorios deberán fijarse en el perfil;
* detectar problemas de documentación, presentación y mantenimiento;
* clasificar los repositorios según su función;
* definir un plan de mejora priorizado;
* reducir el ruido producido por proyectos formativos, forks y repositorios históricos.

La auditoría aplica los principios definidos en:

* [`01_BRAND.md`](./01_BRAND.md);
* [`02_VISUAL_IDENTITY.md`](./02_VISUAL_IDENTITY.md);
* [`03_README_ARCHITECTURE.md`](./03_README_ARCHITECTURE.md).

---

# 1. Audit Scope

La auditoría comprende los elementos públicos visibles en la cuenta de GitHub:

* perfil general;
* biografía;
* Profile README actual;
* repositorios públicos;
* repositorios fijados;
* nombres;
* descripciones;
* topics;
* lenguajes principales;
* documentación;
* arquitectura;
* testing;
* automatización;
* releases;
* licencias;
* mantenimiento;
* diferenciación profesional.

La auditoría no evaluará inicialmente:

* repositorios privados;
* código corporativo;
* proyectos sujetos a confidencialidad;
* actividad no publicada;
* contribuciones que no puedan verificarse públicamente.

---

# 2. Audit Objectives

La auditoría deberá responder a cinco preguntas principales.

## 2.1 Portfolio Quality

¿Qué repositorios representan mejor el nivel técnico actual?

## 2.2 Professional Positioning

¿Qué proyectos respaldan de forma demostrable el posicionamiento:

> **Backend • Full Stack • AI Developer**

## 2.3 Narrative Balance

¿Existe una selección equilibrada entre:

* backend;
* full stack;
* inteligencia artificial;
* arquitectura;
* documentación;
* testing;
* automatización?

## 2.4 Repository Readiness

¿Qué repositorios están preparados para ser mostrados y cuáles requieren mejoras?

## 2.5 Profile Simplification

¿Qué proyectos generan ruido, redundancia o una percepción desactualizada?

---

# 3. Current Public Profile

## 3.1 Visible Name

El nombre visible actual es:

```text
Fran Ramírez
```

La identidad definida para el nuevo sistema será:

```text
Fran Ramirez
```

El cambio elimina la tilde para mantener una representación internacional consistente.

---

## 3.2 GitHub Username

```text
fran-eliot
```

El identificador deberá conservarse.

Ventajas:

* ya está consolidado;
* coincide con el identificador de LinkedIn;
* es reconocible;
* es breve;
* evita conflictos con nombres comunes;
* funciona como identidad digital complementaria.

---

## 3.3 Current Biography

La biografía actual se orienta a la etiqueta:

```text
Analista Programador
```

y utiliza una formulación general basada en cualidades personales y búsqueda de crecimiento profesional.

Esta descripción ya no representa adecuadamente:

* el posicionamiento acordado;
* la evolución reciente hacia Java y Spring Boot;
* el trabajo backend en entornos enterprise;
* los proyectos de IA;
* la orientación hacia arquitectura y mantenibilidad.

Deberá sustituirse durante la implementación del nuevo perfil.

---

## 3.4 Current Repository Volume

La cuenta contiene un volumen elevado de repositorios públicos.

Una parte importante corresponde a:

* ejercicios formativos;
* laboratorios;
* forks;
* proyectos parciales;
* repositorios históricos;
* pruebas tecnológicas.

La existencia de estos repositorios no constituye un problema por sí misma.

El problema aparece cuando todos compiten visualmente con los proyectos estratégicos y dificultan identificar el nivel técnico actual.

---

## 3.5 Current Pinned Repositories

La selección fijada actualmente incluye:

```text
dental-front
cognitiva-ai
aula-robotica-platform
dental-back-spring
only_film
dental-back
```

Esta selección muestra:

* frontend Angular;
* backend NestJS;
* backend Spring;
* Java y Spring Boot;
* FastAPI;
* inteligencia artificial;
* testing;
* aplicaciones de dominio real.

Sin embargo, presenta varios problemas narrativos:

1. Clínica Dental ocupa tres de las seis posiciones.
2. Frontend y backend se presentan como proyectos independientes.
3. Existen capacidades redundantes entre varios repositorios.
4. No aparece NovaCoquinaria.
5. OnlyFilm aparece como fork.
6. La selección no comunica una progresión clara.
7. El peso de los proyectos más recientes no está equilibrado.
8. No existe todavía una jerarquía entre proyecto principal y proyectos complementarios.

---

# 4. Current Profile README Assessment

El Profile README actual contiene:

* presentación personal;
* sección sobre el perfil;
* proyectos destacados;
* stack tecnológico;
* formación;
* contacto.

La estructura ofrece una base funcional, pero no responde a la nueva arquitectura profesional.

---

## 4.1 Strengths

### Existing Profile Repository

El repositorio especial del perfil ya existe y está configurado.

### Bilingual Intention

Existe intención de ofrecer contenido en inglés y español.

### Project Visibility

Los proyectos principales aparecen enlazados o mencionados.

### Broad Technical Coverage

El README refleja experiencia en backend, frontend, bases de datos y análisis de datos.

### Contact Access

LinkedIn y correo están presentes.

---

## 4.2 Weaknesses

### Outdated Positioning

La presentación actual utiliza:

```text
Programador Analista
Backend Developer
Entusiasta del aprendizaje constante
```

pero no comunica claramente:

```text
Backend • Full Stack • AI Developer
```

### Generic Opening

El encabezado:

```text
Hola, soy Fran Ramírez
```

no genera una identidad diferencial.

### Technology Inventory

El stack aparece como una clase de Python con una lista extensa.

La solución resulta creativa, pero:

* dificulta el escaneo;
* mezcla niveles de experiencia;
* no establece prioridades;
* no agrupa las tecnologías según el nuevo sistema;
* no funciona como evidencia.

### Education Weight

La formación ocupa una sección significativa.

En la nueva arquitectura deberá trasladarse principalmente a LinkedIn y al CV.

### Project Selection

Los proyectos destacados actuales no coinciden completamente con la selección estratégica prevista.

### Visual Inconsistency

El perfil combina:

* emojis;
* código;
* badges;
* separadores;
* listas;
* diferentes estilos de presentación.

No existe todavía un lenguaje visual unificado.

### Language Link

El enlace de idioma deberá verificarse y reconstruirse con la convención aprobada:

```text
README.md
README.es.md
```

---

# 5. Repository Ecosystem Classification

Los repositorios deberán clasificarse antes de decidir qué hacer con ellos.

---

## 5.1 Strategic Repositories

Representan directamente el posicionamiento profesional y pueden formar parte del Engineering Portfolio.

Candidatos iniciales:

```text
NovaCoquinaria
OnlyFilm
Aula Robótica
Cognitiva AI
Dental Clinic
```

Un sexto espacio podrá reservarse para:

* un futuro proyecto con Kafka;
* una aplicación con LLM y RAG;
* una plataforma backend distribuida;
* otro proyecto que represente mejor el nivel futuro.

---

## 5.2 Supporting Repositories

Demuestran una capacidad concreta, pero no necesitan aparecer fijados ni en el portfolio principal.

Candidatos potenciales:

* Vanguard A/B Test;
* proyectos específicos de Java;
* proyectos de análisis de datos;
* herramientas o pruebas de concepto;
* módulos reutilizables;
* ejercicios avanzados con suficiente elaboración propia.

---

## 5.3 Learning Repositories

Incluyen:

* laboratorios;
* ejercicios de bootcamp;
* repositorios de cursos;
* prácticas guiadas;
* pruebas de frameworks.

Deberán conservar su contexto formativo y no presentarse como productos terminados.

---

## 5.4 Forks

Los forks deberán evaluarse según el nivel de transformación realizado.

Un fork podrá conservar valor profesional cuando:

* incluya desarrollo propio significativo;
* exista una evolución clara respecto al original;
* documente las diferencias;
* mantenga commits y releases propios;
* se explique la autoría original;
* aporte capacidades demostrables.

No obstante, un fork suele transmitir menos propiedad que un repositorio original.

Por este motivo, deberá estudiarse especialmente la presentación de `only_film`.

---

## 5.5 Archive Candidates

Podrán archivarse repositorios que:

* no tengan mantenimiento previsto;
* representen una etapa formativa superada;
* estén incompletos;
* hayan sido sustituidos;
* no aporten valor diferencial;
* contengan pruebas sin contexto;
* generen confusión.

Archivar no significa eliminar.

Permite conservar el historial sin presentarlo como trabajo activo.

---

# 6. Initial Strategic Candidates

## 6.1 NovaCoquinaria

### Role in Portfolio

```text
Architecture and Knowledge Engineering
```

### Expected Evidence

* arquitectura documental;
* grafo de conocimiento;
* automatización;
* validaciones;
* Python;
* documentación extensa;
* gestión de decisiones;
* calidad y mantenibilidad.

### Strategic Value

Puede convertirse en el proyecto más diferencial del portfolio.

### Current Concern

Deberá comprobarse su visibilidad pública, metadata, README, estado y preparación para recruiters.

---

## 6.2 OnlyFilm

### Role in Portfolio

```text
Java Backend and Tested Web Application
```

### Expected Evidence

* Java;
* Spring Boot;
* Spring Security;
* Thymeleaf;
* testing automatizado;
* GitHub Actions;
* SonarQube;
* Docker;
* flujo funcional completo.

### Strategic Value

Es uno de los proyectos más claros para respaldar el posicionamiento backend Java.

### Current Concern

GitHub lo identifica como fork.

Será necesario explicar el alcance de las mejoras propias y valorar si puede presentarse con suficiente identidad.

---

## 6.3 Aula Robótica

### Role in Portfolio

```text
Modular Backend Platform
```

### Expected Evidence

* FastAPI;
* SQLAlchemy;
* MariaDB;
* IAM y RBAC;
* WebSockets;
* arquitectura modular;
* Docker;
* aplicación para un caso real.

### Strategic Value

Demuestra Python backend, seguridad, tiempo real, arquitectura y diseño de una plataforma completa.

### Current Concern

Deberá analizarse su estado funcional, documentación pendiente y nivel de finalización.

---

## 6.4 Cognitiva AI

### Role in Portfolio

```text
Artificial Intelligence and Applied Research
```

### Expected Evidence

* machine learning;
* deep learning;
* MRI;
* datos clínicos;
* ensembles;
* evaluación;
* reproducibilidad;
* documentación técnica.

### Strategic Value

Es la principal evidencia del posicionamiento AI Developer.

### Current Concern

La estructura actual contiene múltiples notebooks y material histórico. Será necesario mejorar la navegación, separar resultados definitivos y simplificar la experiencia inicial.

---

## 6.5 Dental Clinic

### Role in Portfolio

```text
Full Stack Application
```

### Expected Evidence

* Angular;
* Spring Boot o NestJS;
* autenticación;
* autorización;
* roles;
* MySQL;
* gestión de citas;
* integración frontend-backend.

### Strategic Value

Es la evidencia más directa del posicionamiento Full Stack.

### Current Concern

Actualmente el proyecto está dividido entre varios repositorios:

```text
dental-front
dental-back
dental-back-spring
```

Será necesario decidir:

* qué backend representa la versión canónica;
* cómo comunicar la relación entre repositorios;
* si conviene una organización coordinadora;
* si debe crearse un repositorio de presentación;
* qué piezas deben permanecer fijadas.

---

## 6.6 Future Strategic Project

### Role in Portfolio

```text
Modern Distributed or AI-Powered System
```

### Potential Direction

* Kafka;
* event-driven architecture;
* LLM;
* RAG;
* agentes;
* modelos locales;
* observabilidad;
* cloud;
* microservicios.

### Strategic Value

Permitirá demostrar evolución posterior a los proyectos formativos y consolidar el nivel técnico futuro.

### Current Decision

```text
Reserved
```

No se ocupará este espacio con un proyecto débil únicamente para completar seis tarjetas.

---

# 7. Initial Portfolio Coverage

| Capability              | Primary Evidence | Secondary Evidence      |
| ----------------------- | ---------------- | ----------------------- |
| Java Backend            | OnlyFilm         | Dental Clinic Spring    |
| Python Backend          | Aula Robótica    | NovaCoquinaria tooling  |
| Full Stack              | Dental Clinic    | OnlyFilm                |
| Artificial Intelligence | Cognitiva AI     | Future AI project       |
| Architecture            | NovaCoquinaria   | Aula Robótica           |
| Testing                 | OnlyFilm         | Cognitiva AI evaluation |
| Documentation           | NovaCoquinaria   | Aula Robótica           |
| CI/CD                   | OnlyFilm         | Future repositories     |
| Security and IAM        | Aula Robótica    | Dental Clinic           |
| Data Analysis           | Cognitiva AI     | Vanguard A/B Test       |
| Cloud and Containers    | Aula Robótica    | OnlyFilm                |
| Product Thinking        | Dental Clinic    | Aula Robótica           |

La cobertura inicial resulta equilibrada, pero todavía existen dos debilidades:

1. falta un proyecto moderno que combine backend distribuido e IA;
2. Clínica Dental necesita una presentación unificada.

---

# 8. Initial Findings

## Finding 1 — Strong Raw Material

Existe suficiente material técnico para construir un portfolio profesional sin inventar capacidades.

---

## Finding 2 — Excessive Public Noise

El volumen de laboratorios, forks y ejercicios dificulta descubrir los proyectos principales.

---

## Finding 3 — Pinned Repository Redundancy

Tres posiciones fijadas están dedicadas al mismo producto de Clínica Dental.

---

## Finding 4 — Profile Positioning Is Outdated

La biografía y el README actuales no reflejan la evolución profesional reciente.

---

## Finding 5 — AI Evidence Is Strong but Complex

Cognitiva AI aporta profundidad, pero necesita una experiencia de entrada más sencilla.

---

## Finding 6 — Java Evidence Is Valuable but Forked

OnlyFilm es técnicamente relevante, aunque su condición de fork requiere una estrategia de presentación transparente.

---

## Finding 7 — Full Stack Evidence Is Fragmented

Clínica Dental demuestra frontend y backend, pero su fragmentación reduce el impacto.

---

## Finding 8 — Architecture Can Become the Differentiator

NovaCoquinaria y Aula Robótica permiten construir una narrativa basada en arquitectura, documentación y sistemas mantenibles.

---

## Finding 9 — A Sixth Project Should Not Be Forced

Cinco proyectos sólidos serán preferibles a seis proyectos con calidad desigual.

---

# 9. Immediate Audit Priorities

La siguiente fase deberá auditar individualmente:

1. NovaCoquinaria.
2. OnlyFilm.
3. Aula Robótica.
4. Cognitiva AI.
5. Dental Clinic.
6. Vanguard A/B Test como posible proyecto de apoyo.

Para cada proyecto se evaluará:

* alineación estratégica;
* profundidad técnica;
* documentación;
* arquitectura;
* testing;
* automatización;
* metadata;
* visual readiness;
* mantenimiento;
* diferenciación;
* riesgos;
* trabajo necesario antes de fijarlo.

---

# 10. Part 1 Conclusions

El ecosistema actual contiene proyectos suficientes para respaldar el posicionamiento:

> **Backend • Full Stack • AI Developer**

El principal problema no es la ausencia de experiencia demostrable.

El principal problema es la falta de selección, jerarquía y narrativa.

La estrategia no deberá consistir en añadir más repositorios al perfil.

Deberá consistir en:

1. seleccionar;
2. consolidar;
3. documentar;
4. diferenciar;
5. ordenar;
6. mantener.

El objetivo inicial será convertir una colección extensa de repositorios en un portfolio técnico curado.

---

# 11. Individual Repository Audit

Esta sección evalúa individualmente los principales candidatos al `Engineering Portfolio`.

Cada repositorio se analiza según los siguientes criterios:

```text
Strategic Alignment
Technical Depth
Architecture
Documentation
Testing and Quality
Automation and Delivery
Visual Readiness
Maintenance
Differentiation
Portfolio Recommendation
```

La evaluación distingue entre:

* hechos comprobados públicamente;
* información conocida por la documentación del proyecto;
* aspectos que todavía requieren verificación;
* mejoras necesarias antes de destacar el repositorio.

---

# 12. NovaCoquinaria

## 12.1 Repository Status

| Field                       | Assessment                                           |
| --------------------------- | ---------------------------------------------------- |
| **Proposed Classification** | Strategic                                            |
| **Primary Domain**          | Knowledge Engineering and Documentation Architecture |
| **Portfolio Role**          | Architecture, automation and knowledge systems       |
| **Public Verification**     | Pending                                              |
| **Initial Recommendation**  | Strong candidate, subject to publication readiness   |

En el momento de esta auditoría no se ha localizado un repositorio público accesible con el nombre `NovaCoquinaria` dentro de la cuenta `fran-eliot`.

Por ello, esta evaluación se basa en la documentación y el conocimiento acumulado durante el desarrollo del proyecto.

Antes de incorporarlo al portfolio deberán verificarse públicamente:

* URL definitiva;
* visibilidad;
* descripción;
* topics;
* README;
* licencia;
* releases;
* estado;
* estructura documental;
* activos visuales.

---

## 12.2 Strategic Alignment

NovaCoquinaria encaja especialmente con las siguientes dimensiones de la marca:

* arquitectura de información;
* sistemas de conocimiento;
* documentación como producto;
* automatización;
* calidad;
* mantenibilidad;
* evolución controlada;
* diseño basado en decisiones.

No es el proyecto que mejor demuestra desarrollo backend tradicional, pero puede convertirse en el proyecto que más claramente diferencie el perfil frente a otros candidatos junior.

---

## 12.3 Technical Evidence

Según la documentación interna del proyecto, NovaCoquinaria incluye:

* documentación estructurada en Markdown;
* grafo de conocimiento;
* relaciones semánticas entre documentos;
* validación de metadatos;
* control de enlaces;
* auditoría de conocimiento;
* generación de documentación;
* herramientas Python;
* MkDocs;
* ADR;
* estrategia de calidad;
* versionado y releases.

La combinación de estas capacidades permite presentarlo como:

> A structured knowledge engineering system with automated validation, semantic relationships and documentation-first architecture.

---

## 12.4 Architecture

La arquitectura constituye su principal fortaleza.

El proyecto demuestra:

* separación entre conocimiento fuente y documentación generada;
* taxonomías;
* identificadores documentales;
* relaciones semánticas;
* validadores;
* herramientas reutilizables;
* decisiones arquitectónicas documentadas;
* mantenimiento de deuda de conocimiento;
* evolución mediante releases.

Esto respalda directamente los principios definidos en `01_BRAND.md`.

---

## 12.5 Documentation

La documentación es previsiblemente excelente en profundidad, pero deberá evaluarse su experiencia de entrada.

Riesgos:

* exceso de profundidad para un visitante inicial;
* demasiados documentos antes de comprender el propósito;
* terminología interna;
* dificultad para identificar el resultado funcional;
* posibilidad de parecer una colección de Markdown en lugar de un sistema.

El README público deberá explicar primero:

1. qué es;
2. qué problema resuelve;
3. cómo funciona;
4. qué automatiza;
5. por qué resulta técnicamente relevante.

---

## 12.6 Testing and Quality

La calidad se apoya principalmente en validadores y automatización documental.

Deberán mostrarse claramente:

* documentos validados;
* enlaces comprobados;
* identificadores únicos;
* relaciones del grafo;
* auditoría semántica;
* pipeline de generación;
* estado de calidad.

Estas métricas deberán ofrecerse con contexto y no como números aislados.

---

## 12.7 Visual Readiness

El proyecto puede beneficiarse especialmente de:

* diagrama del flujo documental;
* representación del grafo;
* captura de MkDocs;
* panel de auditoría;
* resumen visual de dominios;
* social preview basada en nodos y relaciones.

No deberá utilizar una estética culinaria decorativa como identidad principal.

El valor diferencial se encuentra en la ingeniería del conocimiento.

---

## 12.8 Main Strengths

* Proyecto original.
* Alta diferenciación.
* Arquitectura explícita.
* Documentación excepcional.
* Automatización propia.
* Evolución mediante ADR y releases.
* Relación directa con la identidad de ingeniería.
* Capacidad de convertirse en proyecto insignia.

---

## 12.9 Main Risks

* No se ha verificado su publicación actual.
* Puede resultar difícil de explicar en pocos segundos.
* Puede parecer excesivamente documental.
* Su relación con backend, full stack o IA no es inmediata.
* Requiere una narrativa orientada a producto.
* Necesita una demo visual o documentación pública navegable.

---

## 12.10 Required Improvements

### Critical

* [ ] Confirmar repositorio público y URL.
* [ ] Crear README principal en inglés.
* [ ] Añadir descripción pública.
* [ ] Seleccionar topics.
* [ ] Comunicar claramente el problema que resuelve.
* [ ] Incluir diagrama de arquitectura.
* [ ] Definir licencia.
* [ ] Comunicar estado y versión.

### High

* [ ] Crear social preview.
* [ ] Añadir capturas de documentación.
* [ ] Presentar métricas de validación.
* [ ] Simplificar la entrada al conocimiento.
* [ ] Añadir una sección de ejecución de herramientas.

### Medium

* [ ] Preparar versión española.
* [ ] Crear marca gráfica del proyecto.
* [ ] Añadir una demostración del grafo.
* [ ] Documentar contribuciones.

---

## 12.11 Portfolio Recommendation

```text
Strong Strategic Candidate
```

NovaCoquinaria puede ocupar una de las primeras posiciones del portfolio cuando tenga una presentación pública clara.

Su papel será demostrar:

```text
Architecture
Documentation
Automation
Knowledge Engineering
Long-Term Maintainability
```

---

# 13. OnlyFilm

## 13.1 Repository Status

| Field                      | Assessment                                        |
| -------------------------- | ------------------------------------------------- |
| **Classification**         | Strategic                                         |
| **Primary Domain**         | Java backend and server-rendered web application  |
| **Portfolio Role**         | Spring Boot, testing and software quality         |
| **Public Verification**    | Completed                                         |
| **Initial Recommendation** | Include after attribution and presentation review |

GitHub identifica públicamente `only_film` como un fork de `certidevs/g1_testing`. El repositorio muestra más de cuatrocientos commits, documentación propia, workflows, código fuente, carpeta de documentación y configuración de SonarQube.

El README lo presenta como una plataforma de gestión cinematográfica construida con Spring Boot y Thymeleaf, con arquitectura MVC, Spring Security, testing multinivel, CI, SonarQube, Docker y cobertura superior al 83 %.

---

## 13.2 Strategic Alignment

OnlyFilm es actualmente una de las evidencias más completas para:

* Java;
* Spring Boot;
* Spring Security;
* Spring MVC;
* Spring Data JPA;
* Hibernate;
* testing;
* CI/CD;
* calidad;
* aplicación funcional completa.

Respalda directamente el eje `Backend Developer`.

También aporta una dimensión full stack ligera mediante Thymeleaf y Bootstrap.

---

## 13.3 Functional Depth

El README documenta:

* consulta de películas;
* cartelera;
* sesiones;
* registro y login;
* compra de entradas;
* selección de butacas;
* checkout;
* tickets QR;
* historial;
* reseñas;
* administración de películas;
* salas;
* sesiones;
* usuarios.

Estas funcionalidades permiten presentar el proyecto como una aplicación de dominio completa y no como un CRUD aislado.

---

## 13.4 Architecture

La arquitectura pública se describe mediante:

```text
Controllers
↓
Services
↓
Repositories
↓
Database
```

Incluye Spring MVC, Spring Security, Spring Data JPA, Hibernate, Thymeleaf y H2.

La arquitectura resulta fácil de comprender, aunque deberá mejorarse mediante:

* un diagrama más profesional;
* explicación de responsabilidades;
* modelo de dominio;
* flujo de compra;
* estrategia de seguridad;
* decisiones de persistencia.

---

## 13.5 Testing and Quality

El proyecto muestra una de las estrategias de calidad más completas del portfolio:

* repository tests;
* service tests;
* controller tests;
* security tests;
* Selenium E2E;
* GitHub Actions;
* SonarQube;
* cobertura superior al 83 %;
* Docker.

Existe una inconsistencia pública que deberá corregirse: la descripción de GitHub menciona **126 pruebas**, mientras que el historial previo del proyecto y otras referencias pueden reflejar cifras distintas. La cifra final deberá obtenerse directamente de la suite actual y mantenerse sincronizada.

---

## 13.6 Ownership and Fork Risk

La principal debilidad no es técnica.

Es perceptiva.

GitHub muestra inmediatamente:

```text
forked from certidevs/g1_testing
```

Esto puede generar dudas sobre:

* autoría;
* alcance inicial;
* proporción de trabajo propio;
* evolución;
* relación con el proyecto original.

El repositorio no deberá intentar ocultar su origen.

La estrategia correcta será documentar:

* origen formativo;
* estado inicial recibido;
* contribuciones realizadas;
* funcionalidades añadidas;
* refactorizaciones;
* tests incorporados;
* CI/CD añadido;
* documentación creada;
* mejoras de calidad;
* despliegue.

---

## 13.7 Documentation

El README actual es amplio y cubre:

* descripción;
* funcionalidades;
* arquitectura;
* modelo de datos;
* seguridad;
* detalles técnicos;
* testing;
* calidad;
* instalación;
* Docker;
* estructura;
* autoría.

La base es fuerte.

Sin embargo, deberá revisarse:

* exceso de emojis;
* consistencia de encabezados;
* idioma principal;
* apertura del README;
* badges;
* atribución del fork;
* enlaces;
* capturas;
* release actual;
* licencia;
* demo.

---

## 13.8 Visual Readiness

Puede presentarse mediante:

* captura de cartelera;
* flujo de selección de butacas;
* ticket QR;
* panel administrativo;
* diagrama de flujo de compra;
* resumen de calidad;
* social preview cinematográfica sobria.

La identidad visual no deberá convertirse en un cartel de cine recargado.

---

## 13.9 Main Strengths

* Stack principal alineado con el objetivo profesional.
* Aplicación funcional completa.
* Seguridad.
* Testing multinivel.
* CI/CD.
* SonarQube.
* Docker.
* Numerosas mejoras propias.
* Documentación extensa.
* Gran potencial para entrevistas Java.

---

## 13.10 Main Risks

* Condición de fork.
* Autoría inicial compartida o heredada.
* Inconsistencia en el número de tests.
* README en español.
* Falta de atribución claramente destacada.
* Posible ausencia de release profesional.
* Uso de H2 como base principal desplegada.
* Posible exceso de contenido en README.
* Necesidad de diferenciar qué se recibió y qué se desarrolló después.

---

## 13.11 Required Improvements

### Critical

* [ ] Añadir una sección visible de origen y contribuciones propias.
* [ ] Verificar número actual de tests.
* [ ] Sincronizar descripción y README.
* [ ] Definir estado actual.
* [ ] Verificar licencia y derechos derivados del fork.
* [ ] Revisar enlaces y ejecución reproducible.

### High

* [ ] Crear README principal en inglés.
* [ ] Mantener `README.es.md`.
* [ ] Crear social preview.
* [ ] Añadir capturas.
* [ ] Crear diagrama de arquitectura profesional.
* [ ] Documentar CI/CD y quality gates.
* [ ] Crear release propia.

### Medium

* [ ] Reducir emojis.
* [ ] Añadir roadmap.
* [ ] Añadir changelog.
* [ ] Documentar limitaciones.
* [ ] Preparar demo estable.

---

## 13.12 Portfolio Recommendation

```text
Include with Transparent Attribution
```

OnlyFilm deberá ocupar una posición alta como proyecto Java, siempre que la presentación explique claramente su evolución respecto al repositorio original.

Su papel será demostrar:

```text
Java
Spring Boot
Testing
Security
CI/CD
Software Quality
```

---

# 14. Aula Robótica Platform

## 14.1 Repository Status

| Field                      | Assessment                                  |
| -------------------------- | ------------------------------------------- |
| **Classification**         | Strategic                                   |
| **Primary Domain**         | Python backend platform                     |
| **Portfolio Role**         | Modular architecture, security and realtime |
| **Public Verification**    | Completed                                   |
| **Initial Recommendation** | Include and prioritize                      |

El repositorio público contiene código de aplicación, documentación, tests, workflows, configuración de cobertura, SonarQube y más de sesenta commits.

El README presenta una plataforma para la gestión colaborativa del Aula de Robótica de la Universidad de Alcalá, con IAM, RBAC contextual, proyectos, Kanban realtime, auditoría, notificaciones, dashboard y preparación para SAML/SSO.

---

## 14.2 Strategic Alignment

Aula Robótica es uno de los proyectos que mejor respalda:

* Python backend;
* FastAPI;
* SQLAlchemy;
* MariaDB;
* seguridad;
* IAM;
* RBAC;
* WebSockets;
* arquitectura modular;
* testing;
* CI/CD;
* Docker.

Aporta profundidad técnica y un dominio real.

---

## 14.3 Functional Depth

La plataforma documenta módulos para:

* usuarios;
* identidades;
* roles;
* permisos;
* proyectos;
* tareas;
* Kanban;
* notificaciones;
* auditoría;
* dashboard;
* actividad;
* colaboración;
* integración institucional futura.

La combinación demuestra diseño de plataforma, no únicamente operaciones CRUD.

---

## 14.4 Architecture

El README describe una arquitectura multicapa:

```text
Jinja2 / AdminLTE / Bootstrap
↓
FastAPI Routers
↓
Service Layer
↓
SQLAlchemy ORM
↓
MariaDB
```

También combina SSR, REST y WebSockets.

Esta arquitectura es comprensible y adecuada para entrevistas.

Puede reforzarse mediante:

* diagrama C4;
* mapa de módulos;
* modelo IAM;
* flujo WebSocket;
* límites entre SSR y API;
* estrategia de persistencia;
* deployment view.

---

## 14.5 Security

La seguridad es uno de sus principales diferenciadores:

* JWT;
* cookies HTTPOnly;
* refresh tokens;
* bcrypt;
* middleware;
* roles globales;
* roles contextuales;
* permisos granulares;
* ownership;
* protección SSR y API;
* auditoría;
* preparación para SAML y OAuth.

Debe evitarse afirmar soporte real de SAML/SSO si solo está preparado arquitectónicamente.

---

## 14.6 Realtime

El proyecto incluye:

* WebSockets;
* salas por proyecto;
* broadcast;
* sincronización de Kanban;
* notificaciones;
* actividad en tiempo real.

Esto aporta una diferenciación clara frente al resto del portfolio.

---

## 14.7 Testing and Quality

El README declara:

* más de 240 tests automatizados;
* cobertura superior al 75 %;
* Pytest;
* Ruff;
* SonarQube Cloud;
* GitHub Actions;
* coverage.

La raíz pública también muestra `.coverage`, archivos ZIP de cobertura y tests, que no deberían formar parte del repositorio activo.

---

## 14.8 Documentation

La documentación es extensa y cubre:

* visión;
* funcionalidades;
* arquitectura;
* seguridad;
* stack;
* testing;
* estructura;
* modelo de datos;
* instalación;
* Docker;
* API;
* roadmap;
* documentación adicional.

El principal riesgo es que el README sea demasiado largo.

Debería funcionar como una portada y derivar el detalle hacia `docs/`.

---

## 14.9 Metadata and Topics

La descripción pública es sólida y comunica FastAPI, WebSockets, IAM y Docker.

Los topics cubren bien el dominio, pero existe al menos un error tipográfico:

```text
sqlachemy
```

deberá sustituirse por:

```text
sqlalchemy
```

Los topics `cloud`, `devops`, `nginx` o `docker-compose` deberán mantenerse únicamente si existen implementaciones reales y visibles.

---

## 14.10 Main Strengths

* Proyecto original.
* Caso de uso real.
* Arquitectura modular.
* Seguridad avanzada para el nivel del portfolio.
* RBAC contextual.
* WebSockets.
* Testing amplio.
* CI/CD.
* SonarQube.
* Docker.
* Documentación extensa.
* Alta relevancia para Tech Leads.

---

## 14.11 Main Risks

* README excesivamente largo.
* Algunas funcionalidades pueden estar incompletas.
* Claims de escalabilidad o cloud deben contextualizarse.
* SAML/SSO todavía futuro.
* Archivos generados versionados.
* Falta de releases visibles.
* Falta de licencia visible en la raíz examinada.
* Ausencia de social preview.
* Autoría y formación ocupan demasiado espacio al final.
* Estado funcional no está resumido al inicio.

---

## 14.12 Required Improvements

### Critical

* [ ] Eliminar `.coverage`, ZIP de tests y cobertura del repositorio.
* [ ] Verificar `.gitignore`.
* [ ] Corregir topic `sqlachemy`.
* [ ] Añadir licencia.
* [ ] Comunicar claramente estado y limitaciones.
* [ ] Verificar instrucciones de instalación completas.
* [ ] Confirmar que Docker está realmente disponible.

### High

* [ ] Crear README principal en inglés.
* [ ] Mover detalle técnico a `docs/`.
* [ ] Crear social preview.
* [ ] Añadir capturas.
* [ ] Crear diagrama C4.
* [ ] Crear release inicial.
* [ ] Añadir changelog.
* [ ] Añadir `PROJECT_STATUS.md`.

### Medium

* [ ] Reducir emojis.
* [ ] Simplificar sección de autor.
* [ ] Documentar threat model.
* [ ] Añadir demo o vídeo.
* [ ] Preparar Docker Compose si procede.

---

## 14.13 Portfolio Recommendation

```text
High-Priority Strategic Project
```

Aula Robótica debería formar parte del portfolio inicial y es un candidato claro a repositorio fijado.

Su papel será demostrar:

```text
Python
FastAPI
Modular Architecture
IAM and RBAC
Realtime Systems
Testing
```

---

# 15. Cognitiva AI

## 15.1 Repository Status

| Field                      | Assessment                                          |
| -------------------------- | --------------------------------------------------- |
| **Classification**         | Strategic                                           |
| **Primary Domain**         | Applied AI and medical research                     |
| **Portfolio Role**         | Machine learning, deep learning and experimentation |
| **Public Verification**    | Completed                                           |
| **Initial Recommendation** | Include after major repository cleanup              |

El repositorio público contiene múltiples directorios de experimentación, notebooks, modelos, artefactos, figuras, documentación, versiones antiguas y una release reproducible.

El README documenta un sistema de clasificación multimodal para cribado temprano de deterioro cognitivo combinando información clínica y MRI de OASIS-1 y OASIS-2.

---

## 15.2 Strategic Alignment

Cognitiva AI es la evidencia principal para:

* AI Developer;
* machine learning;
* deep learning;
* computer vision;
* medical imaging;
* ensembles;
* calibration;
* model evaluation;
* reproducible research;
* data analysis.

Es imprescindible para que `AI Developer` no sea únicamente una declaración.

---

## 15.3 Experimental Depth

El proyecto documenta una evolución amplia:

* baselines clínicos;
* modelos sobre MRI;
* ResNet;
* EfficientNet-B3;
* embeddings;
* fine-tuning;
* calibración;
* ensembles;
* stacking;
* metamodelos;
* umbrales por cohorte;
* análisis de coste;
* fusión multimodal.

Esto demuestra profundidad y perseverancia experimental.

---

## 15.4 Methodological Strengths

El README destaca:

* separación por paciente;
* prevención de data leakage;
* calibración;
* cohort-specific thresholds;
* priorización del recall;
* evaluación con AUC, PR-AUC y Brier;
* consideración explícita de falsos negativos;
* comparación entre OASIS-1 y OASIS-2.

Estas decisiones aportan más valor que una simple métrica alta.

---

## 15.5 Results

El README comunica resultados finales de modelos unimodales e intermodales y reconoce limitaciones de generalización entre cohortes.

Esta honestidad metodológica es una fortaleza.

No deberá presentarse como herramienta diagnóstica.

Deberá utilizar formulaciones como:

```text
research prototype
screening-oriented experiment
applied machine learning project
```

y mantener un disclaimer sanitario claro.

---

## 15.6 Repository Structure

La raíz pública contiene numerosos elementos:

* múltiples pipelines;
* modelos;
* artefactos;
* carpetas antiguas;
* notebooks;
* varios README alternativos;
* presentaciones;
* ZIP;
* archivos temporales de Office;
* dataset Excel;
* scripts auxiliares.

Este es actualmente el mayor problema del repositorio.

La profundidad técnica queda oculta por una experiencia de navegación caótica.

---

## 15.7 Documentation

La documentación es extremadamente extensa.

Existen:

* README principal;
* README alternativos;
* informe técnico;
* bitácora;
* presentación;
* storytelling;
* contexto;
* release;
* ejemplos.

La cantidad de documentación es valiosa, pero necesita una arquitectura editorial.

---

## 15.8 Reproducibility

El repositorio afirma incluir una release reproducible y pipelines con configuraciones, modelos y QA.

Deberá verificarse que un visitante puede:

1. instalar dependencias;
2. ejecutar una demo sin datasets restringidos;
3. reproducir resultados parciales;
4. entender qué artefactos están incluidos;
5. conocer limitaciones de licencias y datos.

---

## 15.9 Metadata

La descripción pública es específica y técnicamente relevante.

Los topics son numerosos y cubren bien IA médica, calibración, MRI, ensembles y reproducibilidad.

Sin embargo, el número de topics puede reducirse para priorizar descubrimiento y evitar dispersión.

---

## 15.10 Main Strengths

* Principal evidencia de IA.
* Problema con relevancia real.
* Profundidad experimental.
* Uso combinado de datos clínicos e imagen.
* Prevención de leakage.
* Calibración.
* Evaluación por cohorte.
* Interpretación honesta de resultados.
* Release reproducible.
* Amplia documentación.
* Resultados cuantitativos.

---

## 15.11 Main Risks

* Raíz caótica.
* Archivos temporales.
* Múltiples README.
* ZIP y datasets versionados.
* Modelos o artefactos pesados.
* Navegación compleja.
* README excesivamente largo.
* Riesgo de interpretación clínica incorrecta.
* Posibles cuestiones de licencia de datos.
* Falta de tests software convencionales.
* Dificultad de ejecución para terceros.
* Terminología y pipelines históricos mezclados con el resultado final.

---

## 15.12 Required Improvements

### Critical

* [ ] Eliminar archivo temporal de PowerPoint.
* [ ] Revisar datasets y licencias.
* [ ] Mover ZIP y artefactos fuera de la raíz.
* [ ] Elegir un único README canónico.
* [ ] Archivar versiones antiguas.
* [ ] Crear un disclaimer médico.
* [ ] Definir claramente el modelo final.
* [ ] Verificar reproducibilidad real.

### High

* [ ] Rediseñar la estructura del repositorio.
* [ ] Crear README en inglés.
* [ ] Mantener versión española.
* [ ] Crear Quick Start.
* [ ] Separar research history de release.
* [ ] Crear social preview.
* [ ] Añadir diagrama del pipeline.
* [ ] Añadir tabla ejecutiva de resultados.
* [ ] Documentar datos y licencias.

### Medium

* [ ] Reducir topics.
* [ ] Añadir tests del pipeline.
* [ ] Automatizar validaciones.
* [ ] Preparar demo Streamlit o FastAPI.
* [ ] Añadir model card.
* [ ] Añadir data card.
* [ ] Crear changelog.

---

## 15.13 Portfolio Recommendation

```text
Mandatory AI Project after Cleanup
```

Cognitiva AI debe aparecer en el portfolio porque constituye la evidencia esencial del eje IA.

Su papel será demostrar:

```text
Applied AI
Medical Imaging
Machine Learning
Deep Learning
Calibration
Reproducible Research
```

---

# 16. Dental Clinic Ecosystem

## 16.1 Repository Status

| Field                      | Assessment                                            |
| -------------------------- | ----------------------------------------------------- |
| **Classification**         | Strategic ecosystem                                   |
| **Primary Domain**         | Full stack application                                |
| **Portfolio Role**         | Angular, API development and authentication           |
| **Public Verification**    | Completed                                             |
| **Initial Recommendation** | Include as one project, not three pinned repositories |

El ecosistema se reparte actualmente entre:

```text
dental-front
dental-back
dental-back-spring
```

`dental-front` contiene una aplicación Angular 17 conectada a un backend NestJS, con autenticación JWT, roles, agenda, pacientes, profesionales y disponibilidad.

`dental-back` contiene una API NestJS con MySQL, TypeORM, JWT, roles, Swagger y módulos para pacientes, profesionales, citas, disponibilidad, slots y tratamientos.

`dental-back-spring` presenta una migración o implementación alternativa con Spring Boot 3, Angular 17, JWT, MySQL, MongoDB y DTO.

---

## 16.2 Strategic Alignment

Clínica Dental es la evidencia más clara de:

* full stack;
* Angular;
* TypeScript;
* API REST;
* NestJS;
* Spring Boot;
* JWT;
* roles;
* MySQL;
* integración frontend-backend;
* modelado de dominio.

El problema no es la capacidad demostrada.

Es la fragmentación de la historia.

---

## 16.3 Frontend Assessment

`dental-front` cuenta con:

* Angular 17;
* Angular Material;
* RxJS;
* TypeScript;
* autenticación JWT;
* roles;
* agenda;
* comunicación con backend;
* capturas;
* documentación amplia.

La documentación indica dependencia del backend NestJS, no del backend Spring.

Debe explicarse cuál es la integración canónica actual.

---

## 16.4 NestJS Backend Assessment

`dental-back` incluye:

* NestJS;
* MySQL;
* TypeORM;
* JWT;
* roles;
* Swagger;
* DTO validation;
* bcrypt;
* módulos de negocio;
* endpoints documentados.

El README reconoce como mejora futura la incorporación de tests automáticos.

También identifica varios autores, lo que exige atribución clara dentro del portfolio.

La instalación contiene todavía URLs y nombres genéricos como `tuusuario`, que deberán corregirse.

---

## 16.5 Spring Backend Assessment

`dental-back-spring` tiene únicamente catorce commits públicos y un README muy amplio.

El README describe una solución full stack con:

* Angular 17;
* Spring Boot 3;
* JWT;
* DTO;
* MySQL;
* MongoDB;
* gestión de pacientes;
* profesionales;
* agenda;
* citas;
* disponibilidades;
* administración.

No obstante, la raíz pública examinada solo muestra el backend Spring, mientras que algunas instrucciones del README se refieren a una estructura conjunta y al directorio `backend`.

Esto genera posibles inconsistencias entre documentación y código real.

---

## 16.6 Architecture

La solución global puede representarse como:

```text
Angular Frontend
        ↓
REST API
        ↓
NestJS or Spring Boot Backend
        ↓
MySQL
        ↓
Optional MongoDB
```

La arquitectura necesita una decisión canónica:

### Option A

Angular + NestJS representa la versión funcional principal.

### Option B

Angular + Spring Boot sustituye progresivamente a NestJS.

### Option C

Ambos backends se documentan como implementaciones alternativas.

La tercera opción puede ser técnicamente interesante, pero requiere explicar claramente:

* por qué existen dos implementaciones;
* qué funcionalidades comparte cada una;
* qué estado tiene cada backend;
* cuál debe ejecutar un visitante;
* qué versión se mantiene.

---

## 16.7 Ownership

El backend NestJS fue desarrollado por varios autores.

La presentación en el portfolio deberá distinguir:

* trabajo en equipo;
* contribuciones propias;
* responsabilidad asumida;
* posteriores mejoras individuales;
* migración a Spring.

No deberá presentarse todo el producto como autoría individual sin matices.

---

## 16.8 Documentation

Los tres repositorios tienen documentación considerable, pero existe duplicación.

Problemas:

* tres README cuentan partes de la misma historia;
* stacks diferentes;
* posible desalineación funcional;
* instalación no coordinada;
* falta de repositorio agregador;
* falta de versión canónica;
* exceso de posiciones pinned.

---

## 16.9 Visual Readiness

El producto tiene un buen potencial visual:

* login;
* agenda semanal;
* gestión de citas;
* pacientes;
* historial;
* roles;
* disponibilidad;
* Swagger;
* diagrama ER.

Puede presentarse como una única tarjeta en el Profile README, con enlaces a:

* frontend;
* backend canónico;
* backend alternativo;
* documentación global.

---

## 16.10 Main Strengths

* Evidencia full stack directa.
* Angular moderno.
* API REST.
* Dos tecnologías backend.
* JWT y roles.
* Dominio coherente.
* Interfaz visible.
* MySQL.
* Documentación.
* Experiencia de equipo.
* Potencial de migración tecnológica.

---

## 16.11 Main Risks

* Fragmentación.
* Tres repositorios fijados actualmente.
* Dos backends sin jerarquía clara.
* Backend NestJS sin tests.
* Autoría compartida.
* README Spring posiblemente desalineado con la estructura real.
* Falta de integración reproducible.
* Ausencia de repositorio coordinador.
* MongoDB puede parecer innecesario si su uso es marginal.
* Instrucciones genéricas o incorrectas.
* Licencia no explícita en la versión NestJS.

---

## 16.12 Required Improvements

### Critical

* [ ] Definir backend canónico.
* [ ] Definir relación entre NestJS y Spring.
* [ ] Corregir instrucciones de instalación.
* [ ] Documentar autoría y contribuciones.
* [ ] Añadir tests al backend canónico.
* [ ] Verificar integración frontend-backend.
* [ ] Definir licencia.

### High

* [ ] Crear un repositorio agregador o landing repository.
* [ ] Crear README global.
* [ ] Añadir arquitectura completa.
* [ ] Crear Docker Compose.
* [ ] Añadir social preview.
* [ ] Crear capturas coordinadas.
* [ ] Publicar una release integrada.
* [ ] Añadir estado de cada componente.

### Medium

* [ ] Reducir emojis.
* [ ] Revisar uso real de MongoDB.
* [ ] Añadir CI.
* [ ] Añadir changelog.
* [ ] Preparar demo.
* [ ] Homogeneizar topics.

---

## 16.13 Portfolio Recommendation

```text
Include as One Full Stack Product
```

Clínica Dental deberá mostrarse como un único proyecto del portfolio, aunque esté compuesto por varios repositorios.

Su papel será demostrar:

```text
Angular
Full Stack Integration
REST APIs
Authentication
Role-Based Access
Spring Boot or NestJS
Relational Data
```

No deberán dedicarse tres posiciones pinned al mismo producto.

---

# 17. Vanguard A/B Test

## 17.1 Repository Status

| Field                       | Assessment                                |
| --------------------------- | ----------------------------------------- |
| **Proposed Classification** | Supporting                                |
| **Primary Domain**          | Data analysis and experimentation         |
| **Portfolio Role**          | Statistical analysis and business insight |
| **Public Verification**     | Incomplete                                |
| **Initial Recommendation**  | Supporting project, not initial pin       |

El Profile README público actual menciona un experimento A/B de Vanguard con limpieza, análisis exploratorio, pruebas estadísticas, Power BI y presentación final.

No se ha identificado con certeza la URL del repositorio durante esta auditoría.

Por tanto, deberán verificarse:

* nombre;
* visibilidad;
* README;
* notebooks;
* dashboard;
* datos;
* licencias;
* conclusiones;
* reproducibilidad.

---

## 17.2 Strategic Alignment

El proyecto respalda:

* data analysis;
* experimentation;
* estadística;
* pandas;
* visualización;
* Power BI;
* comunicación de resultados.

No respalda directamente el eje backend.

Tampoco representa IA avanzada.

Por ello tiene más sentido como proyecto de apoyo que como uno de los primeros cinco proyectos estratégicos.

---

## 17.3 Potential Value

Puede demostrar:

* formulación de hipótesis;
* preparación de datos;
* análisis exploratorio;
* tests estadísticos;
* evaluación de KPIs;
* interpretación de negocio;
* dashboard;
* presentación ejecutiva.

También refuerza la capacidad de comunicar resultados a perfiles no técnicos.

---

## 17.4 Main Strengths

* Diversifica el portfolio.
* Demuestra estadística.
* Aporta orientación de negocio.
* Incluye dashboard.
* Permite mostrar comunicación.
* Refuerza el background de análisis de datos.

---

## 17.5 Main Risks

* Puede parecer un ejercicio típico de bootcamp.
* Menor profundidad de ingeniería software.
* Posible dataset externo con restricciones.
* Posible dependencia excesiva de notebooks.
* Poca relación con el posicionamiento principal.
* Puede competir con Cognitiva AI sin aportar suficiente diferenciación.
* Estado público no verificado.

---

## 17.6 Required Improvements

### Critical

* [ ] Identificar repositorio.
* [ ] Verificar licencia y datos.
* [ ] Crear README orientado a decisiones.
* [ ] Explicar hipótesis y resultados.
* [ ] Documentar reproducibilidad.

### High

* [ ] Crear resumen ejecutivo.
* [ ] Incluir dashboard o capturas.
* [ ] Separar notebooks exploratorios y finales.
* [ ] Añadir estructura del análisis.
* [ ] Publicar conclusiones verificables.

### Medium

* [ ] Crear social preview.
* [ ] Añadir tests de datos.
* [ ] Automatizar limpieza.
* [ ] Preparar versión inglesa.

---

## 17.7 Portfolio Recommendation

```text
Supporting Project
```

Vanguard puede aparecer en una sección secundaria futura o sustituir temporalmente a otro proyecto si se quiere reforzar el eje Data.

No se recomienda como repositorio fijado en la primera selección mientras existan cinco candidatos estratégicos más alineados.

---

# 18. Comparative Assessment

## 18.1 Strategic Role

| Project           | Primary Portfolio Role                 |
| ----------------- | -------------------------------------- |
| NovaCoquinaria    | Architecture and knowledge engineering |
| OnlyFilm          | Java, Spring Boot and testing          |
| Aula Robótica     | Python platform, security and realtime |
| Cognitiva AI      | Applied artificial intelligence        |
| Dental Clinic     | Full stack development                 |
| Vanguard A/B Test | Data analysis support                  |

---

## 18.2 Strength Comparison

| Project        | Strongest Evidence                               |
| -------------- | ------------------------------------------------ |
| NovaCoquinaria | Architecture, documentation and automation       |
| OnlyFilm       | Java, testing and delivery quality               |
| Aula Robótica  | Security, modularity and realtime                |
| Cognitiva AI   | ML research and model evaluation                 |
| Dental Clinic  | Frontend-backend integration                     |
| Vanguard       | Statistical analysis and business interpretation |

---

## 18.3 Main Weakness Comparison

| Project        | Main Weakness                                |
| -------------- | -------------------------------------------- |
| NovaCoquinaria | Public readiness not verified                |
| OnlyFilm       | Fork status and ownership perception         |
| Aula Robótica  | Oversized README and repository cleanup      |
| Cognitiva AI   | Repository complexity and clutter            |
| Dental Clinic  | Fragmentation across repositories            |
| Vanguard       | Lower alignment and public status unverified |

---

## 18.4 Initial Readiness

| Project        | Current Readiness                    |
| -------------- | ------------------------------------ |
| Aula Robótica  | High after focused cleanup           |
| OnlyFilm       | Medium-high after attribution review |
| Cognitiva AI   | Medium after major cleanup           |
| Dental Clinic  | Medium-low until consolidation       |
| NovaCoquinaria | Pending public verification          |
| Vanguard       | Pending identification               |

---

# 19. Initial Portfolio Decision

La selección provisional será:

```text
1. NovaCoquinaria
2. OnlyFilm
3. Aula Robótica
4. Cognitiva AI
5. Dental Clinic
```

Vanguard permanecerá como:

```text
Supporting Project
```

El orden definitivo todavía no está cerrado.

Dependerá de:

* preparación pública de NovaCoquinaria;
* limpieza de Cognitiva AI;
* consolidación de Clínica Dental;
* estrategia de atribución de OnlyFilm;
* madurez final de Aula Robótica.

---

# 20. Part 2 Conclusions

La auditoría individual confirma que existe cobertura real para:

> **Backend • Full Stack • AI Developer**

Cada proyecto aporta una dimensión diferente:

* NovaCoquinaria demuestra diseño de sistemas de conocimiento.
* OnlyFilm demuestra Java y calidad software.
* Aula Robótica demuestra plataforma backend y seguridad.
* Cognitiva AI demuestra inteligencia artificial aplicada.
* Clínica Dental demuestra integración full stack.
* Vanguard aporta análisis de datos como capacidad secundaria.

La principal necesidad no consiste en desarrollar inmediatamente más proyectos.

Consiste en mejorar la presentación y reducir los riesgos de los ya existentes:

```text
Publish
Attribute
Clean
Consolidate
Document
Prioritize
```

---

# 21. Evaluation Method

La selección del `Engineering Portfolio` no se basará únicamente en la calidad individual de cada repositorio.

También deberá considerar:

* el equilibrio global del portfolio;
* la cobertura del posicionamiento profesional;
* la diferenciación entre proyectos;
* la claridad de la narrativa;
* el estado público;
* el esfuerzo necesario antes de destacar cada proyecto.

La evaluación utilizará una matriz cuantitativa como herramienta de apoyo.

La puntuación no sustituirá al criterio estratégico.

Un proyecto con una puntuación ligeramente inferior podrá seleccionarse si representa una capacidad que no aparece en ningún otro repositorio.

---

## 21.1 Evaluation Scale

Cada criterio se puntuará entre:

```text
1 — Very Weak
2 — Weak
3 — Acceptable
4 — Strong
5 — Excellent
```

Interpretación:

| Score | Meaning                                                       |
| ----: | ------------------------------------------------------------- |
|     1 | No existe evidencia suficiente o presenta problemas graves.   |
|     2 | Existe evidencia limitada y requiere una mejora considerable. |
|     3 | Cumple un nivel aceptable, aunque necesita evolución.         |
|     4 | Presenta evidencia sólida y valor profesional claro.          |
|     5 | Constituye una fortaleza diferencial del repositorio.         |

---

# 22. Evaluation Criteria

## 22.1 Strategic Alignment

Evalúa cuánto refuerza el proyecto el posicionamiento:

> **Backend • Full Stack • AI Developer**

---

## 22.2 Technical Depth

Evalúa si el repositorio muestra:

* complejidad real;
* decisiones técnicas;
* dominio funcional;
* integración de componentes;
* resolución de problemas no triviales.

---

## 22.3 Architecture

Evalúa:

* claridad estructural;
* separación de responsabilidades;
* modularidad;
* decisiones documentadas;
* capacidad de evolución.

---

## 22.4 Documentation

Evalúa:

* claridad del README;
* facilidad de entrada;
* documentación técnica;
* reproducibilidad;
* decisiones explicadas;
* estado comunicado.

---

## 22.5 Testing and Quality

Evalúa:

* tests;
* cobertura;
* validadores;
* análisis estático;
* quality gates;
* reproducibilidad;
* prácticas de calidad.

---

## 22.6 Delivery and Automation

Evalúa:

* CI/CD;
* Docker;
* releases;
* scripts;
* automatización;
* despliegue;
* validación automática.

---

## 22.7 Visual Readiness

Evalúa si el proyecto puede presentarse profesionalmente mediante:

* capturas;
* diagramas;
* demo;
* social preview;
* métricas;
* resultados visuales.

---

## 22.8 Maintenance

Evalúa:

* actividad;
* estado;
* claridad del roadmap;
* limpieza del repositorio;
* estabilidad;
* facilidad de actualización.

---

## 22.9 Differentiation

Evalúa cuánto aporta una historia única al portfolio.

Un proyecto pierde puntuación si duplica capacidades ya demostradas con mayor calidad por otro repositorio.

---

## 22.10 Ownership and Credibility

Evalúa:

* autoría;
* contribuciones propias;
* transparencia;
* condición de fork;
* trabajo en equipo;
* coherencia entre claims y evidencia.

---

# 23. Criterion Weights

No todos los criterios tendrán el mismo peso.

| Criterion                 |   Weight |
| ------------------------- | -------: |
| Strategic Alignment       |      15% |
| Technical Depth           |      15% |
| Architecture              |      12% |
| Documentation             |      12% |
| Testing and Quality       |      10% |
| Delivery and Automation   |       8% |
| Visual Readiness          |       6% |
| Maintenance               |       7% |
| Differentiation           |      10% |
| Ownership and Credibility |       5% |
| **Total**                 | **100%** |

La alineación estratégica y la profundidad técnica reciben el peso principal.

La presentación visual aporta valor, pero nunca deberá compensar una carencia técnica.

---

# 24. Current-State Scoring

Las siguientes puntuaciones representan el estado actual o el último estado conocido.

No representan el potencial final después de aplicar el plan de mejora.

| Project           | Alignment | Depth | Architecture | Documentation | Quality | Delivery | Visual | Maintenance | Differentiation | Ownership |
| ----------------- | --------: | ----: | -----------: | ------------: | ------: | -------: | -----: | ----------: | --------------: | --------: |
| NovaCoquinaria    |         4 |     4 |            5 |             5 |       4 |        4 |      3 |           5 |               5 |         5 |
| OnlyFilm          |         5 |     4 |            4 |             4 |       5 |        5 |      3 |           4 |               4 |         3 |
| Aula Robótica     |         5 |     5 |            5 |             4 |       5 |        4 |      3 |           4 |               5 |         5 |
| Cognitiva AI      |         5 |     5 |            4 |             4 |       4 |        3 |      4 |           3 |               5 |         5 |
| Dental Clinic     |         5 |     4 |            3 |             3 |       2 |        2 |      4 |           3 |               4 |         3 |
| Vanguard A/B Test |         3 |     3 |            2 |             4 |       3 |        1 |      4 |           2 |               3 |         3 |

---

# 25. Weighted Score

Aplicando los pesos establecidos:

| Rank | Project           | Weighted Score | Percentage |
| ---: | ----------------- | -------------: | ---------: |
|    1 | Aula Robótica     |       4.61 / 5 |      92.2% |
|    2 | NovaCoquinaria    |       4.43 / 5 |      88.6% |
|    3 | Cognitiva AI      |       4.32 / 5 |      86.4% |
|    4 | OnlyFilm          |       4.22 / 5 |      84.4% |
|    5 | Dental Clinic     |       3.43 / 5 |      68.6% |
|    6 | Vanguard A/B Test |       2.84 / 5 |      56.8% |

Estas puntuaciones deben interpretarse como una fotografía de preparación estratégica, no como una clasificación absoluta de calidad.

---

# 26. Score Interpretation

## 26.1 Aula Robótica

La puntuación más alta procede de su equilibrio entre:

* backend Python;
* arquitectura modular;
* IAM y RBAC;
* WebSockets;
* testing;
* dominio real;
* autoría propia;
* diferenciación.

Su principal necesidad se encuentra en la presentación y limpieza del repositorio, no en la ausencia de profundidad técnica.

---

## 26.2 NovaCoquinaria

Obtiene una puntuación especialmente alta en:

* arquitectura;
* documentación;
* diferenciación;
* mantenimiento;
* ownership.

Su principal limitación actual es no disponer todavía de una presencia pública evaluable y preparada para visitantes externos.

Una vez publicado y presentado correctamente puede convertirse en el proyecto insignia del perfil.

---

## 26.3 Cognitiva AI

Destaca en:

* IA aplicada;
* profundidad experimental;
* metodología;
* diferenciación;
* resultados.

La puntuación disminuye por:

* estructura compleja;
* acumulación de artefactos;
* dificultad de entrada;
* menor automatización software;
* mantenimiento editorial elevado.

---

## 26.4 OnlyFilm

Destaca en:

* Java;
* Spring Boot;
* testing;
* CI/CD;
* SonarQube;
* despliegue;
* aplicación funcional.

El repositorio público se identifica como fork del proyecto original y actualmente documenta 126 pruebas, cobertura del 83,5 %, GitHub Actions, SonarQube y Docker. Esto refuerza su valor técnico, pero exige atribución transparente y corrección de instrucciones que todavía apuntan al repositorio de origen.

---

## 26.5 Dental Clinic

Su principal valor consiste en representar:

* Angular;
* integración frontend-backend;
* autenticación;
* roles;
* API REST;
* dominio funcional.

Su puntuación se reduce por:

* fragmentación;
* dos backends;
* autoría compartida;
* testing insuficiente;
* ausencia de una experiencia integrada;
* documentación descoordinada.

Actualmente el ecosistema público está dividido entre frontend Angular, backend NestJS y backend Spring Boot.

---

## 26.6 Vanguard A/B Test

Vanguard demuestra correctamente análisis de datos, formulación de hipótesis, tests estadísticos, KPIs, Power BI y comunicación de conclusiones. El repositorio contiene datos, notebooks, dashboard y slides, pero carece de releases y se declara como proyecto educativo colaborativo.

Su menor puntuación no significa que sea un proyecto débil.

Significa que está menos alineado con el posicionamiento principal y muestra menos ingeniería de software que los otros candidatos.

---

# 27. Potential-State Scoring

La puntuación potencial estima el valor de cada proyecto después de completar sus mejoras prioritarias.

| Project           | Current | Potential | Main Condition                            |
| ----------------- | ------: | --------: | ----------------------------------------- |
| NovaCoquinaria    |   88.6% |       95% | Publicación y onboarding profesional      |
| Aula Robótica     |   92.2% |       95% | Limpieza, diagramas y release             |
| Cognitiva AI      |   86.4% |       94% | Reestructuración y reproducibilidad       |
| OnlyFilm          |   84.4% |       91% | Atribución, README inglés y release       |
| Dental Clinic     |   68.6% |       88% | Consolidación del ecosistema              |
| Vanguard A/B Test |   56.8% |       72% | Limpieza, reproducibilidad y presentación |

La diferencia entre puntuación actual y potencial representa el trabajo pendiente de presentación, consolidación y mantenimiento.

---

# 28. Strategic Portfolio Selection

La selección inicial recomendada será:

```text
NovaCoquinaria
Aula Robótica
OnlyFilm
Cognitiva AI
Dental Clinic
```

Vanguard permanecerá como proyecto de apoyo.

---

## 28.1 Selection Rationale

### NovaCoquinaria

Representa:

```text
Architecture
Knowledge Engineering
Documentation
Automation
Maintainability
```

### Aula Robótica

Representa:

```text
Python Backend
FastAPI
Security
Realtime Systems
Modular Architecture
```

### OnlyFilm

Representa:

```text
Java
Spring Boot
Testing
CI/CD
Software Quality
```

### Cognitiva AI

Representa:

```text
Artificial Intelligence
Machine Learning
Deep Learning
Medical Imaging
Experimentation
```

### Dental Clinic

Representa:

```text
Full Stack
Angular
REST APIs
Authentication
Role-Based Access
```

El conjunto ofrece una cobertura directa y comprensible del posicionamiento profesional.

---

# 29. Recommended Portfolio Order

El orden del Profile README no deberá seguir exactamente la puntuación numérica.

Deberá contar una historia profesional.

## Recommended Initial Order

```text
1. NovaCoquinaria
2. OnlyFilm
3. Aula Robótica
4. Cognitiva AI
5. Dental Clinic
```

---

## 29.1 Why NovaCoquinaria First

NovaCoquinaria deberá abrir el portfolio cuando:

* sea público;
* tenga README internacional;
* disponga de una entrada clara;
* muestre visualmente su arquitectura;
* comunique automatización y calidad.

Será el proyecto más diferencial y el que mejor representa la filosofía profesional.

---

## 29.2 Why OnlyFilm Second

OnlyFilm conecta inmediatamente con el mercado objetivo:

* Java;
* Spring Boot;
* testing;
* seguridad;
* CI/CD.

Su posición alta permite que un recruiter identifique rápidamente una evidencia backend convencional y relevante.

---

## 29.3 Why Aula Robótica Third

Aula Robótica demuestra mayor complejidad arquitectónica que OnlyFilm, pero su stack Python es secundario respecto al objetivo principal de consolidación backend Java.

Situarlo tercero permite mostrar profundidad sin diluir el eje profesional.

---

## 29.4 Why Cognitiva AI Fourth

Cognitiva AI deberá aparecer claramente, pero después de que el visitante haya identificado primero la solidez como desarrollador de software.

Así, la IA se interpreta como una especialidad respaldada por una base de ingeniería y no como un posicionamiento aislado.

---

## 29.5 Why Dental Clinic Fifth

Clínica Dental cierra el portfolio mostrando capacidad full stack.

Su posición será adecuada hasta que:

* se consolide;
* se unifique;
* tenga tests;
* disponga de una release integrada.

Después podrá subir posiciones.

---

# 30. Alternative Portfolio Order

Para vacantes con mayor orientación a Python, plataformas o arquitectura:

```text
1. NovaCoquinaria
2. Aula Robótica
3. OnlyFilm
4. Cognitiva AI
5. Dental Clinic
```

Para vacantes Java:

```text
1. OnlyFilm
2. NovaCoquinaria
3. Aula Robótica
4. Dental Clinic
5. Cognitiva AI
```

El Profile README general deberá utilizar una única ordenación estable.

No se reordenará continuamente según cada candidatura.

---

# 31. Pinned Repository Strategy

GitHub permite fijar hasta seis repositorios o gists.

La selección fijada deberá responder a una narrativa de portfolio, no a una lista cronológica.

---

## 31.1 Recommended Initial Pins

Cuando NovaCoquinaria esté publicado:

```text
1. NovaCoquinaria
2. only_film
3. aula-robotica-platform
4. cognitiva-ai
5. Dental Clinic canonical repository
6. vanguard-ab-test or future strategic project
```

---

## 31.2 Pin 1 — NovaCoquinaria

Condiciones:

* repositorio público;
* README preparado;
* licencia definida;
* descripción y topics;
* social preview;
* estado claro.

---

## 31.3 Pin 2 — OnlyFilm

Condiciones:

* atribución visible;
* instrucciones corregidas;
* README inglés;
* métricas validadas;
* release propia.

---

## 31.4 Pin 3 — Aula Robótica

Condiciones:

* limpieza de archivos generados;
* README condensado;
* licencia;
* release;
* estado.

---

## 31.5 Pin 4 — Cognitiva AI

Condiciones:

* raíz limpia;
* modelo final identificable;
* disclaimer;
* Quick Start;
* estructura editorial simplificada.

---

## 31.6 Pin 5 — Dental Clinic

No deberán fijarse por separado:

```text
dental-front
dental-back
dental-back-spring
```

Deberá fijarse únicamente:

* un repositorio canónico;
* o un futuro repositorio agregador.

Hasta que exista, podrá mantenerse temporalmente `dental-back-spring` o `dental-front`, pero no ambos junto al backend NestJS.

---

## 31.7 Pin 6 — Reserved Slot

La sexta posición deberá considerarse flexible.

Opciones:

### Temporary

```text
vanguard-ab-test
```

Ventajas:

* añade Data Analytics;
* muestra estadística;
* demuestra comunicación de resultados;
* diversifica el perfil.

### Future

Proyecto moderno con:

* Kafka;
* arquitectura orientada a eventos;
* LLM;
* RAG;
* agentes;
* modelos locales;
* observabilidad;
* cloud.

La recomendación es utilizar Vanguard temporalmente y sustituirlo cuando exista un proyecto estratégico más alineado.

---

# 32. Vanguard Final Classification

Con el repositorio ya identificado, Vanguard se clasifica como:

```text
Supporting Portfolio Project
Temporary Pin Candidate
```

No formará parte inicialmente de las cinco tarjetas principales del `Engineering Portfolio`.

Podrá:

* ocupar temporalmente el sexto pin;
* aparecer en una futura sección secundaria;
* enlazarse desde Cognitiva AI o el contexto Data;
* utilizarse en candidaturas orientadas a análisis de datos.

---

## 32.1 Vanguard Verified Strengths

El repositorio demuestra públicamente:

* limpieza y fusión de datos;
* análisis de outliers;
* definición de KPIs;
* pruebas de hipótesis;
* Mann-Whitney U;
* análisis de conversión;
* segmentación;
* Power BI;
* presentación;
* recomendaciones de negocio.

---

## 32.2 Vanguard Priority Improvements

### Critical

* [ ] Añadir una licencia formal o aclarar las restricciones de los datos.
* [ ] Revisar si los datos originales deben permanecer versionados.
* [ ] Documentar el orden exacto de ejecución de notebooks.
* [ ] Verificar que `requirements.txt` permite reproducir el análisis.
* [ ] Explicar claramente la autoría colaborativa.

### High

* [ ] Crear README principal en inglés.
* [ ] Mantener `README.es.md`.
* [ ] Reducir emojis.
* [ ] Añadir una tabla ejecutiva de resultados.
* [ ] Incluir capturas del dashboard.
* [ ] Crear una release final.
* [ ] Añadir social preview.
* [ ] Normalizar topics actualmente mezclados en inglés y español.

### Medium

* [ ] Convertir pasos repetidos en funciones o scripts.
* [ ] Añadir validaciones automáticas de datos.
* [ ] Separar notebooks exploratorios y finales.
* [ ] Añadir un informe metodológico.
* [ ] Crear un entorno reproducible con `environment.yml` o lock file.

---

# 33. NovaCoquinaria Publication Strategy

NovaCoquinaria deberá convertirse en repositorio público.

La publicación permitirá demostrar públicamente:

* arquitectura;
* documentación;
* automatización;
* gestión de conocimiento;
* validación;
* evolución mediante releases.

---

## 33.1 Initial Collaboration Model

La primera etapa utilizará:

```text
Public Repository
+
Single Maintainer
+
External Contributions Not Yet Accepted
```

Esto significa:

* el código y la documentación serán visibles;
* las issues podrán utilizarse para gestión propia;
* no se solicitarán contribuciones;
* no será necesario crear inicialmente `CONTRIBUTING.md`;
* los pull requests externos no se promoverán;
* el README comunicará el estado del proyecto;
* la licencia definirá los usos permitidos.

---

## 33.2 Recommended Public Notice

Podrá añadirse una nota breve:

```text
> [!NOTE]
> NovaCoquinaria is currently maintained as a personal engineering project.
> External contributions are not being accepted during the current development stage.
```

Versión española:

```text
> [!NOTE]
> NovaCoquinaria se mantiene actualmente como un proyecto personal de ingeniería.
> Durante esta fase de desarrollo no se aceptan contribuciones externas.
```

Esta nota deberá ser neutral.

No deberá sonar defensiva ni hostil.

---

## 33.3 Contribution Files

Estado inicial recomendado:

| File or Feature       | Decision                            |
| --------------------- | ----------------------------------- |
| `CONTRIBUTING.md`     | Deferred                            |
| Pull request template | Deferred                            |
| Issue templates       | Optional, for internal organization |
| Discussions           | Disabled initially                  |
| Wiki                  | Disabled                            |
| Public roadmap        | Recommended                         |
| License               | Required                            |
| Security policy       | Evaluate                            |
| Code of Conduct       | Not necessary initially             |

---

## 33.4 License Decision

La publicación pública requiere decidir explícitamente qué usos se permiten.

Opciones a evaluar:

* MIT;
* Apache 2.0;
* GPLv3;
* Creative Commons para contenidos;
* modelo dual para código y documentación;
* todos los derechos reservados durante la fase inicial.

La elección deberá considerar que NovaCoquinaria combina:

* scripts y herramientas;
* documentación;
* conocimiento estructurado;
* recetas;
* contenidos editoriales;
* posibles datos derivados.

No deberá aplicarse una única licencia por comodidad sin evaluar estos tipos de contenido.

---

## 33.5 Pre-Publication Gate

Antes de hacerlo público deberá verificarse:

* [ ] No existen secretos.
* [ ] No existen rutas personales.
* [ ] No existen datos privados.
* [ ] No existen archivos temporales.
* [ ] El historial Git puede publicarse.
* [ ] Las referencias externas son legítimas.
* [ ] Las imágenes tienen derechos adecuados.
* [ ] La licencia está decidida.
* [ ] El README explica el proyecto.
* [ ] El estado está comunicado.
* [ ] Las instrucciones funcionan.
* [ ] Los enlaces internos funcionan.
* [ ] La documentación generada está correctamente gestionada.
* [ ] No se invita todavía a contribuciones externas.

---

# 34. Portfolio Coverage Matrix

| Capability       | NovaCoquinaria |  OnlyFilm | Aula Robótica |  Cognitiva AI | Dental Clinic |    Vanguard |
| ---------------- | -------------: | --------: | ------------: | ------------: | ------------: | ----------: |
| Java             |              — |   Primary |             — |             — |     Secondary |           — |
| Python           |     Supporting |         — |       Primary |       Primary |             — |     Primary |
| Backend          |     Supporting |   Primary |       Primary |    Supporting |       Primary |           — |
| Full Stack       |              — | Secondary |     Secondary |             — |       Primary |           — |
| AI               |      Potential |         — |             — |       Primary |             — |           — |
| Data Analysis    |     Supporting |         — |             — |       Primary |             — |     Primary |
| Architecture     |        Primary |    Strong |       Primary |        Strong |        Medium |         Low |
| Testing          |     Validation |   Primary |       Primary |    Evaluation |          Weak | Statistical |
| Security         |              — |    Strong |       Primary | Data concerns |        Strong |           — |
| CI/CD            |     Supporting |   Primary |        Strong |          Weak |          Weak |           — |
| Documentation    |        Primary |    Strong |        Strong |        Strong |        Medium |      Strong |
| Realtime         |              — |         — |       Primary |             — |             — |           — |
| Business Insight |         Medium |    Medium |        Medium |        Medium |        Medium |     Primary |

El conjunto presenta una cobertura suficientemente amplia sin que todos los proyectos cuenten la misma historia.

---

# 35. Final Selection Rules

## 35.1 Engineering Portfolio

Primera versión:

```text
NovaCoquinaria
OnlyFilm
Aula Robótica
Cognitiva AI
Dental Clinic
```

---

## 35.2 Pinned Repositories

Objetivo final:

```text
NovaCoquinaria
only_film
aula-robotica-platform
cognitiva-ai
Dental Clinic canonical repository
Future strategic project
```

Configuración provisional:

```text
NovaCoquinaria
only_film
aula-robotica-platform
cognitiva-ai
Dental Clinic canonical or temporary repository
vanguard-ab-test
```

---

## 35.3 Supporting Projects

```text
vanguard-ab-test
```

y otros repositorios que demuestren capacidades específicas sin formar parte del relato principal.

---

## 35.4 Replacement Priority

El primer proyecto que deberá abandonar los pins cuando exista un nuevo proyecto estratégico será:

```text
vanguard-ab-test
```

Esto no implica archivarlo ni reducir su valor.

Solo refleja la prioridad del posicionamiento general.

---

# 36. Part 3 Conclusions

La selección cuantitativa confirma una narrativa profesional equilibrada:

```text
Architecture
↓
Java Backend
↓
Python Platform
↓
Applied AI
↓
Full Stack
```

NovaCoquinaria deberá hacerse público y convertirse progresivamente en la puerta de entrada del portfolio.

Aula Robótica es actualmente el proyecto con mejor equilibrio técnico.

OnlyFilm es la evidencia más directa para backend Java, pero requiere atribución transparente.

Cognitiva AI es imprescindible para sostener el posicionamiento en inteligencia artificial.

Clínica Dental representa el eje full stack, aunque debe consolidarse.

Vanguard es un proyecto de apoyo valioso y un candidato adecuado para ocupar temporalmente el sexto repositorio fijado.

La selección final no intenta mostrar todo lo realizado.

Intenta contar con claridad la historia profesional correcta.

---

# 37. Repository Improvement Roadmap

La auditoría no termina con la selección del portfolio.

Su objetivo final es convertir cada repositorio estratégico en una referencia profesional capaz de superar una revisión técnica por parte de:

* Software Engineers
* Tech Leads
* Engineering Managers
* Principal Engineers
* Technical Recruiters

Cada proyecto dispondrá de un backlog propio de mejora.

---

# 38. Improvement Priority Matrix

Se utilizarán cuatro niveles de prioridad.

## P0 — Critical

Impide utilizar el repositorio como referencia profesional.

Debe resolverse antes de destacarlo.

---

## P1 — High

No impide su publicación, pero reduce significativamente su impacto.

---

## P2 — Medium

Mejoras de calidad, mantenimiento o presentación.

---

## P3 — Low

Optimizaciones futuras.

---

# 39. Repository Backlog

## 39.1 NovaCoquinaria

### P0

* [ ] README internacional definitivo
* [ ] README.es.md sincronizado
* [ ] Banner propio
* [ ] Topics
* [ ] Descripción pública
* [ ] Licencia
* [ ] Social Preview

### P1

* [ ] Diagrama de arquitectura
* [ ] Diagrama Knowledge Graph
* [ ] Quick Start
* [ ] Project Status
* [ ] Release v1.0

### P2

* [ ] GitHub Pages / MkDocs público
* [ ] Demo del grafo
* [ ] Arquitectura C4

### P3

* [ ] Security Policy
* [ ] CITATION
* [ ] GitHub Discussions (si algún día tiene sentido)

---

## 39.2 OnlyFilm

### P0

* [ ] Explicar claramente el origen del fork
* [ ] Documentar todas las aportaciones propias
* [ ] README en inglés
* [ ] README.es.md
* [ ] Corregir instrucciones

### P1

* [ ] Diagramas
* [ ] Social Preview
* [ ] Release estable
* [ ] Docker actualizado

### P2

* [ ] Changelog
* [ ] Arquitectura C4

---

## 39.3 Aula Robótica

### P0

* [ ] Eliminar artefactos generados
* [ ] Revisar .gitignore
* [ ] Licencia
* [ ] README simplificado

### P1

* [ ] Diagramas
* [ ] Capturas
* [ ] Releases

### P2

* [ ] Demo
* [ ] Docker Compose completo

---

## 39.4 Cognitiva AI

### P0

* [ ] Limpiar raíz
* [ ] Un único README
* [ ] Organizar modelos
* [ ] Organizar notebooks
* [ ] Eliminar archivos temporales

### P1

* [ ] Model Card
* [ ] Data Card
* [ ] Quick Start

### P2

* [ ] Demo
* [ ] API sencilla

---

## 39.5 Dental Clinic

### P0

* [ ] Elegir backend canónico
* [ ] Explicar coexistencia NestJS / Spring
* [ ] Reorganizar documentación

### P1

* [ ] Docker Compose
* [ ] Landing repository

### P2

* [ ] Demo online

---

## 39.6 Vanguard

### P0

* [ ] README profesional
* [ ] Reproducibilidad

### P1

* [ ] Dashboard mejor presentado
* [ ] Capturas

### P2

* [ ] Release
* [ ] Automatización

---

# 40. Recommended Execution Order

No todos los repositorios deben mejorarse al mismo tiempo.

Orden recomendado:

## Phase 1

NovaCoquinaria

Motivo:

Será el proyecto insignia.

---

## Phase 2

OnlyFilm

Motivo:

Refuerza Java.

---

## Phase 3

Aula Robótica

Motivo:

Refuerza Python Backend.

---

## Phase 4

Cognitiva AI

Motivo:

Refuerza IA.

---

## Phase 5

Dental Clinic

Motivo:

Refuerza Full Stack.

---

## Phase 6

Vanguard

Motivo:

Proyecto complementario.

---

# 41. Pinned Repository Migration

Estado actual

```text id="nygs6i"
Dental Front
Cognitiva AI
Aula Robótica
Dental Spring
OnlyFilm
Dental Backend
```

↓

Estado objetivo

```text id="rnp94x"
NovaCoquinaria
OnlyFilm
Aula Robótica
Cognitiva AI
Dental Clinic
Future Project
```

↓

Estado futuro

```text id="ezzq0x"
NovaCoquinaria
OnlyFilm
Aula Robótica
Future Kafka Project
Future AI Platform
Dental Clinic
```

El sexto repositorio será sustituido cuando exista un proyecto claramente superior.

---

# 42. Repository Metadata Standards

Todos los proyectos estratégicos deberán cumplir el mismo estándar.

## Description

Máximo:

```text id="1v70g2"
160 caracteres
```

Siempre en inglés.

---

## Topics

Entre:

```text id="0xw8ea"
8–15
```

No más.

Ordenados por importancia.

---

## README

* Inglés principal.
* Español sincronizado.
* Quick Start.
* Arquitectura.
* Tecnologías.
* Capturas.
* Licencia.
* Roadmap.

---

## Releases

Todos los proyectos estratégicos deberán tener al menos:

```text id="zdhwwg"
v1.0.0
```

---

## License

Todos los proyectos públicos deberán tener licencia explícita.

---

## Social Preview

Todos deberán tener una imagen personalizada.

---

# 43. Repository Quality Gates

Un repositorio se considerará "Portfolio Ready" únicamente cuando cumpla:

## Metadata

* [ ] Nombre correcto
* [ ] Descripción
* [ ] Topics

---

## Documentation

* [ ] README inglés
* [ ] README español
* [ ] Quick Start

---

## Engineering

* [ ] Arquitectura documentada
* [ ] Tecnologías
* [ ] Estado

---

## Quality

* [ ] Licencia
* [ ] Releases
* [ ] Changelog
* [ ] Sin archivos basura

---

## Visual

* [ ] Capturas
* [ ] Banner
* [ ] Social Preview

---

# 44. Long-Term Repository Strategy

No todos los repositorios tendrán el mismo papel.

## Strategic

Siempre visibles.

---

## Supporting

Visibles, pero secundarios.

---

## Archived

Conservados por histórico.

---

## Experimental

Laboratorios.

No deberán competir visualmente con los proyectos estratégicos.

---

# 45. Portfolio Evolution

El portfolio evolucionará aproximadamente así.

## 2026

NovaCoquinaria

OnlyFilm

Aula Robótica

Cognitiva AI

Dental Clinic

---

## 2027

Nueva plataforma Backend distribuida

Kafka

Docker

Observabilidad

Cloud

↓

Sustituye a Vanguard.

---

## 2028

Proyecto con IA Generativa

LLM

RAG

Agentes

↓

Pasa a ocupar una de las primeras posiciones.

---

# 46. Success Metrics

El portfolio se considerará exitoso cuando:

* un recruiter comprenda el perfil en menos de 30 segundos;
* un Tech Lead identifique rápidamente evidencia técnica;
* cada proyecto demuestre una capacidad distinta;
* no existan duplicidades;
* el README del perfil enlace únicamente a proyectos excelentes;
* todos los proyectos fijados sean "Portfolio Ready".

---

# 47. Final Engineering Portfolio

## Tier S

⭐ NovaCoquinaria

Arquitectura • Knowledge Engineering • Automatización

---

⭐ OnlyFilm

Java • Spring Boot • Testing • CI/CD

---

⭐ Aula Robótica

FastAPI • Seguridad • Arquitectura

---

⭐ Cognitiva AI

Machine Learning • Deep Learning • Investigación Aplicada

---

⭐ Dental Clinic

Angular • REST • Full Stack

---

## Tier A

Vanguard A/B Test

Data Analytics

Power BI

Business Insights

---

## Tier B

Laboratorios

Cursos

Pruebas

Repositorios históricos

---

# 48. Strategic Conclusions

La auditoría demuestra que el valor diferencial del perfil no reside en la cantidad de repositorios públicos.

Reside en la combinación equilibrada de cinco disciplinas:

* Backend Engineering
* Full Stack Development
* Artificial Intelligence
* Software Architecture
* Technical Documentation

Esta combinación resulta poco frecuente en perfiles junior y constituye el principal elemento diferenciador de la marca profesional.

---

# 49. Repository Audit Definition of Done

La auditoría se considerará completada cuando:

* [ ] Todos los repositorios estén clasificados.
* [ ] Exista un Engineering Portfolio definitivo.
* [ ] Los repositorios fijados estén seleccionados.
* [ ] Cada proyecto tenga backlog propio.
* [ ] Exista un roadmap de mejora.
* [ ] Los estándares de calidad estén definidos.
* [ ] El mantenimiento futuro sea incremental.
* [ ] La estrategia de GitHub esté alineada con LinkedIn y el CV.

---

# 50. Revision History

| Version | Date       | Description                                                                                                        |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------ |
| 1.0.0   | 2026-08-05 | Primera auditoría completa del ecosistema GitHub.                                                                  |
| 1.1.0   | 2026-08-05 | Incorporación de NovaCoquinaria como repositorio público y validación de Vanguard A/B Test como proyecto de apoyo. |
