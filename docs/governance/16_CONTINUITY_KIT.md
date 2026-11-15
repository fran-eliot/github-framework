# 16 - CONTINUITY KIT

| Campo                    | Valor            |
| ------------------------ | ---------------- |
| **Proyecto**             | GitHub Framework |
| **Documento**            | Continuity Kit   |
| **Versión**              | 1.3.0            |
| **Estado**               | Activo           |
| **Última actualización** | 2026-11-15       |

> Este documento constituye el punto oficial de incorporación al proyecto.

Todo nuevo colaborador o asistente deberá utilizar este documento como referencia inicial antes de comenzar cualquier desarrollo.

---

# Snapshot vigente — Post-release Validator Catalog (2026-11-15)

> **Punto de reanudación actual.** Esta actualización prevalece sobre el snapshot histórico de PR #330 y sobre las instrucciones de reanudación antiguas que aparecen más abajo. Antes de actuar, verificar siempre las PR, `main` y los workflows directamente en GitHub.

| Campo | Evidencia / situación verificada |
| --- | --- |
| Repositorio | [fran-eliot/github-framework](https://github.com/fran-eliot/github-framework) |
| Última release publicada | [v0.11.0 — Framework Validator CLI and CI](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0) |
| Tag inmutable de release | `v0.11.0` → `55680b388b0fd8256c95e15866e53d21cc9a5033` |
| `main` al revisar este snapshot | [`f8c032cfbf035d8936b3c48c0baf1bc9bd60f435`](https://github.com/fran-eliot/github-framework/commit/f8c032cfbf035d8936b3c48c0baf1bc9bd60f435) |
| Última PR fusionada | [#349 — Previous-page catalog navigation](https://github.com/fran-eliot/github-framework/pull/349) |
| Última verificación de la PR #349 | [Framework Validator run 43740069053](https://github.com/fran-eliot/github-framework/actions/runs/43740069053): `success` |
| PR abiertas / rama de PR #349 | Ninguna / rama remota eliminada, comprobado antes de crear la rama de actualización de este kit |
| Estado de esta actualización | La **PR que introduce este snapshot debe revisarse y fusionarse**; el SHA anterior no incluye todavía esta actualización |
| Release/Sprint/milestone siguientes | **Sin compromiso ni autorización de publicación o apertura** |
| Only Film | Assessment `Complete` **solo documental**, sobre SHA `28d75a50e0a178954dd46acc23300d9dd327843c`; no modificar ni aplicar/integrar sin autorización |
| UX-02 | `Prepared — Not Executed`; no presentar evidencia de participantes independientes |

## Evolución integrada posterior al tag v0.11.0

**Todo el trabajo enumerado a continuación está fusionado en `main` pero es posterior al tag `v0.11.0`.** No atribuir estas capacidades a la release ya publicada. El historial completo figura en [Unreleased / CHANGELOG](../../CHANGELOG.md), GitHub PR y el código vigente.

| Área | Incrementos integrados |
| --- | --- |
| Exportación y seguridad | Catálogo JSON a archivo (`--output`), escritura atómica, conservación del archivo ante selecciones vacías o errores y tests de regresión |
| Selección por rutas y metadatos | Filtros `--match`, `--exclude`, `--metadata-status` (estado de carga), `--metadata-id`, `--metadata-name`, `--metadata-version` y `--component-status` (estado declarado) |
| Resúmenes JSON | `--family-summary`, `--metadata-summary` y `--component-status-summary`, aplicados al conjunto seleccionado |
| Ordenación | `--sort-by path|id|name|version|status` y `--sort-order asc|desc`; por defecto se conserva el orden por ruta. Metadatos ausentes quedan al final |
| Paginación | `--limit`, `--offset`, y objeto JSON `pagination` con `total`, `offset`, `limit`, `has_next`, `next_offset`, `has_previous` y `previous_offset` |
| Verificación | Tests CLI de integración y smoke test sobre la biblioteca real en CI Ubuntu y Windows, incluida navegación paginada sin omisiones o duplicados |

Entre las PR verificadas están [#339](https://github.com/fran-eliot/github-framework/pull/339) (versión), [#340](https://github.com/fran-eliot/github-framework/pull/340) (ordenación), [#341](https://github.com/fran-eliot/github-framework/pull/341) (nombre), [#342](https://github.com/fran-eliot/github-framework/pull/342) (smoke test ampliado), [#343](https://github.com/fran-eliot/github-framework/pull/343) y [#344](https://github.com/fran-eliot/github-framework/pull/344) (estado y resumen), [#345](https://github.com/fran-eliot/github-framework/pull/345) y [#346](https://github.com/fran-eliot/github-framework/pull/346) (ordenación), y [#347](https://github.com/fran-eliot/github-framework/pull/347), [#348](https://github.com/fran-eliot/github-framework/pull/348) y [#349](https://github.com/fran-eliot/github-framework/pull/349) (paginación y navegación). La exportación JSON inicial se incorporó mediante [#330](https://github.com/fran-eliot/github-framework/pull/330).

### Contratos que deben preservarse

- Catálogo de Components de **solo lectura**: no altera ni verifica automáticamente un repositorio consumidor. `--list-components` no equivale a una validación semántica de Adoption.
- Los filtros se aplican antes de ordenar y paginar; las salidas paginadas presentan `count`, `components`, `details` y resúmenes **de la página actual**. `pagination.total` corresponde al conjunto completo filtrado, antes de paginar.
- La ordenación de versiones es **lexicográfica**, no SemVer. Los filtros glob son sensibles a mayúsculas. Los campos opcionales se añaden al JSON cuando se solicita la opción correspondiente.
- Una selección sin resultados o una página vacía devuelve código `1`, sin sobrescribir una exportación anterior. Error de escritura devuelve `2`; argumentos incorrectos, `2`.
- No publicar una nueva versión, tag o release ni iniciar Sprint/milestone por inferencia. El trabajo integrado queda bajo `Unreleased` hasta decisión formal.
- Protocolo operativo: el asistente crea rama, implementa y abre PR; el mantenedor revisa, fusiona y elimina la rama remota. Se verifica CI y estado de GitHub antes del siguiente incremento.

### Reanudación recomendada

1. Comprobar que la PR de **actualización de este kit** se haya fusionado y eliminado su rama; este snapshot registra el estado **previo** a dicha PR.
2. Obtener la punta vigente de `main`, PR abiertas, resultados de CI y estado de tags/releases directamente en GitHub. Ante discrepancias, prevalece GitHub.
3. Leer la sección `Unreleased` del [CHANGELOG](../../CHANGELOG.md), `scripts/framework_validator/__main__.py`, `scripts/framework_validator/smoke.py` y `tests/framework_validator/test_cli.py`.
4. Priorizar mejoras con casos de uso observables y compatibilidad contrastable; valorar consolidar contratos, usabilidad y aplicación real **de solo lectura** antes de seguir acumulando opciones pequeñas.
5. Mantener el Assessment de Only Film cerrado documentalmente y no modificar el consumidor sin nueva autorización explícita.

---

# Snapshot histórico — PR #330 (2026-11-15)

> **Snapshot histórico sustituido por el bloque vigente anterior.** Este snapshot prevalecía sobre los capítulos históricos de agosto de 2026 (Sprint 4, v0.2.0 y prioridades iniciales) y sobre el snapshot sustituido del 2026-11-14. No sustituye la consulta en vivo de GitHub: al reanudar, comprobar primero el estado real de `main`, las PR y los checks. [Project Status](12_PROJECT_STATUS.md), [Product Backlog](14_BACKLOG.md), [Roadmap](../../ROADMAP.md) y [CHANGELOG](../../CHANGELOG.md) reflejan el estado documental tras los merges verificados.

| Campo | Estado confirmado el 2026-11-15 |
| --- | --- |
| Repositorio | [`fran-eliot/github-framework`](https://github.com/fran-eliot/github-framework) |
| Última release publicada | **[`v0.11.0 — Framework Validator CLI and CI`](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0)**, publicada 2026-11-15 |
| Tag publicado | `v0.11.0` → commit **`55680b388b0fd8256c95e15866e53d21cc9a5033`**, verificado mediante la referencia GitHub |
| Referencia `main` revisada | [`1aab5a6a402d013e1797bbb71482715e62e84291`](https://github.com/fran-eliot/github-framework/commit/1aab5a6a402d013e1797bbb71482715e62e84291) — merge de PR #330 |
| Última PR fusionada en este snapshot | [#330 — Export Component catalogs to JSON files](https://github.com/fran-eliot/github-framework/pull/330) |
| PR abiertas al elaborar el snapshot | **Ninguna**; volver a verificar en GitHub antes del siguiente cambio |
| Último CI sobre `main` | [Run 43715010476](https://github.com/fran-eliot/github-framework/actions/runs/43715010476): **success**, Ubuntu y Windows, 165 tests y smoke test superados por plataforma |
| Verificación de Components | 21 Components reales en el catálogo/smoke test; validación completa en los jobs de CI |
| Próxima versión / Sprint / milestone | **Ninguna comprometida / ningún Sprint activo**; `v1.0.0` sigue siendo una aspiración futura, no una release aprobada |
| Existing Repository Adoption | Assessment, Application, Integration y Assisted Analysis son capabilities documentadas del Framework, con límites propios |
| Consumer Only Film | **Assessment documental `Complete`**; no se ha modificado Only Film ni autorizado Application/Integration |
| UX-02 | **`Prepared — Not Executed`**; no atribuir resultados de usabilidad independiente |

## Release v0.11.0 — cierre y trazabilidad

La [GitHub Release v0.11.0](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0) se publicó con la aprobación explícita del mantenedor bajo la **opción A (snapshot completo del repositorio)**, no como una entrega limitada a código del Validator. El tag `v0.11.0` se verificó contra el SHA autorizado, `55680b388b0fd8256c95e15866e53d21cc9a5033`. La [validación de ese commit](https://github.com/fran-eliot/github-framework/actions/runs/43708742212) superó los tests y smoke tests en Ubuntu y Windows.

La [PR #329](https://github.com/fran-eliot/github-framework/pull/329) sincronizó después `CHANGELOG.md`, `README.md`, `README_es.md`, `ROADMAP.md` y `12_PROJECT_STATUS.md`: `v0.11.0` figura como **publicada**, con badges EN/ES actualizados. Los documentos de propuesta y baseline en `docs/releases/` conservan **evidencia histórica de preparación**; sus referencias y afirmaciones sobre aprobación pendiente no deben confundirse con el estado actual de la release.

La rama [`candidate/option-a-snapshot-20261115`](https://github.com/fran-eliot/github-framework/tree/candidate/option-a-snapshot-20261115) quedó vinculada al SHA publicado al cerrar el ciclo. **No es la referencia de desarrollo futuro** y no debe fusionarse por rutina contra `main`; el siguiente trabajo empieza desde `main`. Consultar si conviene conservarla o retirarla solo después de verificar el estado remoto y los requisitos de trazabilidad.

## Desarrollo posterior a v0.11.0 — PR #330

Se integró una mejora concreta y **posterior al tag**: el Framework Validator permite exportar su catálogo JSON de Components a un archivo mediante:

```bash
python -m scripts.framework_validator --list-components --format json --details --output component-catalog.json
```

La opción también permite `--family` y `--components-root`. Reutiliza escritura atómica mediante archivo temporal y reemplazo, mantiene stdout si no se indica `--output`, y conserva el contrato histórico de error en exportaciones de informes. Una escritura fallida devuelve código `2`; no se crea automáticamente el directorio de destino. Se incorporaron cuatro nuevos tests y se actualizaron los README EN/ES.

La primera revisión de CI de la PR #330 detectó dos tests existentes que exigían el mensaje de error original. El cambio se corrigió **dentro de la misma PR**; el último CI del merge en `main` terminó con **165/165 tests por plataforma**, smoke test del catálogo de 21 Components y validación de la biblioteca correctos: [run 43715010476](https://github.com/fran-eliot/github-framework/actions/runs/43715010476). No confundir la primera ejecución fallida con el resultado final fusionado.

Esta exportación JSON es trabajo **Unreleased posterior a v0.11.0**. No alterar el tag publicado, no presentar la funcionalidad como incluida en esa release, ni fijar automáticamente `v0.12.0` o iniciar Sprint/milestone.

## Caso práctico de Assessment — Only Film

La [evaluación canónica](../../framework/adoption/examples/only-film-assessment.md) utiliza el consumer [`fran-eliot/only_film`](https://github.com/fran-eliot/only_film) en el SHA inmutable `28d75a50e0a178954dd46acc23300d9dd327843c` frente a `TPL-BACKEND 0.1.0`. Registra **28/28 clasificaciones State/Applicability aprobadas** y **28/28 Adoption Decisions resueltas**: 14 `PRESERVE`, 3 `OMIT`, 9 `ADAPT`, 2 `ADD`. La [matriz consolidada](../../framework/adoption/examples/only-film-consolidated-review-matrix.md) conserva la trazabilidad. Los documentos de verificación y Completion Readiness históricos pueden retener estados intermedios; **el estado canónico final es `Complete`, solo documental**.

`Complete` **no implica** ejecución verificada de Docker Compose o Selenium, suite Maven completa, Quality Gate aprobado, certificación de seguridad, autorización de derechos de terceros, modificación del consumidor, ni permiso automático para Application o Integration. Mantener las decisiones aprobadas y sus limitaciones; **no modificar Only Film** sin una autorización específica e independiente.

## Flujo de trabajo operativo acordado

1. **Ante cada “go”**, consultar GitHub: verificar si la PR anterior está efectivamente fusionada, buscar PR abiertas, identificar el SHA de `main` y revisar el CI relevante. Si la PR anterior continúa abierta o fallan los checks, atender esa situación **antes de crear otra PR funcional**.
2. El asistente desarrolla **directamente en GitHub**: crea una rama temática desde `main`, realiza cambios acotados y verificables, ejecuta o revisa tests/CI y abre una PR real. Facilitar siempre su **enlace directo**.
3. El mantenedor **revisa y hace el merge y elimina la rama remota de trabajo**. El asistente **no realiza el merge** ni borra ramas de trabajo por su cuenta. Las ramas de release/candidato tienen tratamiento específico, distinto de las ramas de PR.
4. No crear versiones, tags, releases, Sprints o milestones sin autorización explícita. Una aprobación de alcance, de versión o de notas **no equivale** a una autorización de publicación. Nunca afirmar acciones de GitHub no comprobadas.
5. Las PR y la documentación técnica nueva se redactan profesionalmente **en inglés**, salvo contenido ya establecido en español o mantenimiento de la versión española. **No incluir indicaciones internas, comentarios sobre uso de IA ni instrucciones al revisor** en el texto público de la PR. Evitar archivos de Discovery redundantes y priorizar **funcionalidad comprobable**.
6. Conservar el contexto de código y documentación anterior: cambios mínimos, tests de regresión, compatibilidad de contratos de CLI e informes JSON, rutas y ejemplos de README sincronizados entre idiomas. Ante una discrepancia entre este kit y GitHub, prevalece la **evidencia actual del repositorio**.

## Punto de reanudación inmediato

- **Primero:** verificar si la PR que actualice este propio Kit se fusionó y si su rama remota fue eliminada. No asumirlo porque aparezca el archivo actualizado.
- **Después:** partir del último `main`; revisar [Product Backlog](14_BACKLOG.md), el historial [v0.11.0](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0) y la CLI `scripts/framework_validator/__main__.py`, con tests en `tests/framework_validator/`. El nuevo soporte de exportación JSON está disponible **en `main`, no en el tag v0.11.0**.
- **Siguiente posible desarrollo:** continuar mejorando la usabilidad e integración de las capacidades del Framework Validator y sus contratos de salida, con una necesidad concreta y criterios verificables; no abrir una nueva release sin planificación. Si se decide un trabajo distinto, validarlo con las fuentes del repositorio.
- **Para retomar en un chat nuevo:** proporcionar este archivo (o la URL de su versión integrada), el enlace al repositorio y una petición como “Continúa GitHub Framework desde el último Continuity Kit: verifica PR, `main` y CI, y prepara el siguiente incremento en rama y PR; yo haré el merge y borraré la rama remota”.

## Fuentes de continuidad

- [GitHub Framework — main](https://github.com/fran-eliot/github-framework)
- [Release v0.11.0](https://github.com/fran-eliot/github-framework/releases/tag/v0.11.0)
- [Project Status](12_PROJECT_STATUS.md) y [Product Backlog](14_BACKLOG.md)
- [Roadmap](../../ROADMAP.md) y [CHANGELOG](../../CHANGELOG.md)
- [Adoption Guide](../../framework/adoption/README.md)
- [Only Film Assessment canónico](../../framework/adoption/examples/only-film-assessment.md)
- [Release candidate baseline histórico](../releases/OPTION_A_CANDIDATE_BASELINE.md)
- [Release notes históricas](../releases/PROPOSED_V0_11_0_RELEASE_NOTES.md)

---

# Cómo utilizar este documento

 Este documento está pensado para leerse de forma secuencial.

Cada parte puede utilizarse de forma independiente, aunque se recomienda recorrer el documento completo durante la primera incorporación al proyecto.

Tiempo estimado de lectura: 10-15 minutos.

---

# 1. Propósito

El objetivo de este documento es proporcionar el contexto necesario para retomar el desarrollo del proyecto en cualquier momento, minimizando el tiempo de incorporación y evitando la pérdida de conocimiento.

Este documento está dirigido tanto a nuevos colaboradores como al propio autor del proyecto y a asistentes de IA que participen en su evolución.

No sustituye a la documentación técnica del Framework.

Su misión es explicar el contexto general del proyecto, el estado actual y la forma de continuar el trabajo de manera consistente.

---

# 2. ¿Qué es GitHub Framework?

GitHub Framework es un framework de ingeniería diseñado para construir repositorios profesionales mediante una combinación de estándares, componentes reutilizables, plantillas y documentación estructurada.

Su propósito es aplicar principios de ingeniería del software al diseño, organización y mantenimiento de repositorios GitHub.

El Framework pretende reducir la variabilidad entre proyectos, mejorar la mantenibilidad y facilitar la reutilización de conocimiento.

---

# 3. Visión

La visión del proyecto es disponer de un marco de trabajo reutilizable que permita construir repositorios consistentes independientemente de la tecnología utilizada.

El Framework no está orientado a un lenguaje de programación concreto.

Debe poder utilizarse en proyectos Backend, Full Stack, Inteligencia Artificial, Ciencia de Datos, documentación técnica o cualquier otro dominio donde sea necesario mantener repositorios bien estructurados.

---

# 4. Estado Actual

En el momento de redactar este documento el proyecto ha completado la fase de arquitectura.

Se dispone de:

* Arquitectura general del Framework.
* GitHub Repository Standards (GRS).
* Repository Design System (RDS).
* Component Catalog.
* Primera biblioteca de componentes README.
* Documentación de gobierno.
* Repositorio Git inicializado.
* Versionado mediante Semantic Versioning.
* Primer tag oficial (`v0.1.0`).

Actualmente comienza la fase de implementación.

---

# 5. Objetivo de la Fase Actual

La prioridad del proyecto consiste en validar el propio Framework utilizándolo para construir el repositorio oficial de GitHub Framework.

Este enfoque, conocido como *dogfooding*, permitirá comprobar que los componentes diseñados son realmente reutilizables y detectar oportunidades de mejora antes de ampliar el Framework.

La implementación del README oficial constituye el primer entregable de esta nueva etapa.

---

# 6. Filosofía del Proyecto

GitHub Framework se desarrolla siguiendo los siguientes principios:

* Simplicidad antes que complejidad.
* Reutilización antes que duplicación.
* Componentes antes que documentos.
* Implementación antes que teoría.
* Evolución basada en casos de uso reales.
* Arquitectura estable y cambios controlados.

El objetivo no es crear la mayor cantidad posible de componentes, sino construir un Framework útil, mantenible y capaz de evolucionar durante muchos años.

---

# 7. Arquitectura del Proyecto

La arquitectura del repositorio ha sido diseñada para separar claramente las distintas responsabilidades del Framework.

Cada directorio responde a un propósito concreto y evita mezclar documentación, componentes, herramientas o ejemplos.

La estructura principal se considera estable y únicamente deberá modificarse cuando exista una necesidad real demostrada durante la implementación.

```text
github-framework/

.github/

docs/
│
├── architecture/
├── design-system/
├── governance/
├── implementation/
└── standards/

framework/
│
├── components/
├── templates/
├── assets/
└── profiles/

examples/

tools/

README.md
ROADMAP.md
CHANGELOG.md
LICENSE
.gitignore
```

---

# 8. Organización de la Documentación

La carpeta `docs/` constituye la base documental del proyecto.

Su contenido se divide en áreas funcionales claramente diferenciadas.

## architecture/

Describe la arquitectura del Framework.

Incluye:

* visión arquitectónica;
* decisiones técnicas;
* estructura general del proyecto.

---

## standards/

Contiene los estándares reutilizables del Framework.

Ejemplos:

* GitHub Repository Standards (GRS).
* Convenciones.
* Buenas prácticas.

---

## design-system/

Recoge el Repository Design System (RDS).

Incluye:

* principios visuales;
* catálogo de componentes;
* reglas de diseño;
* patrones reutilizables.

---

## governance/

Agrupa la documentación necesaria para gestionar el proyecto.

Actualmente incluye:

* PROJECT_STATUS
* BITÁCORA
* BACKLOG
* WORKING_AGREEMENTS
* CONTINUITY_KIT

---

## implementation/

Describe implementaciones concretas del Framework.

Su finalidad es explicar cómo se ensamblan los distintos componentes para construir un repositorio real.

---

# 9. Organización del Framework

La carpeta `framework/` contiene los elementos reutilizables del proyecto.

No almacena documentación de análisis.

Almacena los activos que permitirán construir nuevos repositorios.

---

## components/

Biblioteca de componentes reutilizables.

Cada componente mantiene una estructura homogénea.

```text
component/

metadata.yml

template.md

README.md

example.md
```

---

## templates/

Plantillas compuestas por uno o varios componentes.

Una plantilla representa una solución reutilizable para un tipo de repositorio determinado.

Ejemplos futuros:

* Backend
* Full Stack
* AI
* Documentation

---

## assets/

Recursos compartidos.

Ejemplos:

* imágenes;
* iconografía;
* banners;
* diagramas;
* recursos gráficos.

---

## profiles/

Configuraciones específicas para distintos tipos de perfil o repositorio.

Su implementación se realizará en fases posteriores del proyecto.

---

# 10. Ejemplos

La carpeta `examples/` contendrá implementaciones reales construidas utilizando GitHub Framework.

Estos ejemplos servirán para validar el Framework y demostrar su utilización práctica.

Ejemplos previstos:

* GitHub Framework
* NovaCoquinaria
* OnlyFilm
* Aula Robótica

---

# 11. Herramientas

La carpeta `tools/` agrupará las herramientas auxiliares del Framework.

Su objetivo será automatizar tareas repetitivas.

Entre otras:

* validadores;
* generadores;
* scripts de mantenimiento;
* futuras utilidades CLI.

---

# 12. Arquitectura Congelada

En la versión **v0.1.0** se considera finalizada la arquitectura base del proyecto.

A partir de este momento:

* podrán añadirse nuevos componentes;
* podrán incorporarse nuevas plantillas;
* podrán desarrollarse herramientas;
* podrá evolucionar la documentación.

Sin embargo, la estructura principal del repositorio deberá permanecer estable.

Las modificaciones arquitectónicas únicamente se realizarán cuando una implementación real justifique objetivamente dicho cambio.

---

# 13. Estado del Desarrollo

GitHub Framework se encuentra actualmente en una fase temprana de implementación.

La fase de diseño y arquitectura puede considerarse finalizada, por lo que el desarrollo se centrará a partir de ahora en construir entregables reales utilizando el propio Framework.

La versión actual es:

**v0.1.0**

---

# 14. Estado de Implementación

## Completado

Actualmente se encuentran implementados los siguientes elementos:

### Arquitectura

* Arquitectura general del Framework.
* Estructura del repositorio.
* Arquitectura documental.
* Arquitectura de componentes.

---

### Estándares

* GitHub Repository Standards (GRS).
* Repository Design System (RDS).

---

### Componentes

Se encuentra disponible la primera biblioteca de componentes README.

Actualmente incluye:

* README-HERO
* README-STATUS
* README-OVERVIEW
* README-FEATURES
* README-TECH-STACK
* README-QUICK-START
* README-ARCHITECTURE
* README-DOCUMENTATION
* README-TESTING
* README-ROADMAP
* README-AUTHOR
* README-FOOTER

---

### Gobierno

Se dispone de la documentación necesaria para la gestión del proyecto:

* PROJECT_STATUS
* BITÁCORA
* BACKLOG
* WORKING_AGREEMENTS
* CHANGELOG
* ROADMAP

---

# 15. Trabajo en Curso

En el momento de redactar este documento el principal objetivo consiste en construir la primera implementación real del Framework.

Esta implementación corresponde al propio repositorio GitHub Framework.

Los trabajos actualmente priorizados son:

* README oficial.
* Preparación Open Source.
* Consolidación del repositorio.

---

# 16. Roadmap Inmediato

Los próximos hitos previstos son:

## v0.2.0

Open Source Readiness.

Objetivos principales:

* README oficial.
* LICENSE.
* Documentación de gobierno.
* Preparación de `.github/`.

---

## v0.3.0

Documentation Framework.

Objetivos principales:

* Componentes Documentation.
* Mejora de la Component Library.

---

## v0.4.0

Repository Templates.

Objetivos principales:

* Plantillas reutilizables.
* Casos de uso.
* Primeras implementaciones completas.

---

# 17. Sprint Actual

## Sprint 4

### Objetivo

Convertir GitHub Framework en un repositorio con calidad equivalente a un proyecto open source profesional.

---

### Entregables

* README oficial.
* LICENSE.
* Estructura `.github/`.
* Documentación de gobierno consolidada.

---

### Definition of Done

El Sprint finalizará cuando:

* exista un README estable;
* la documentación de gobierno esté completa;
* el repositorio esté preparado para evolucionar como proyecto open source;
* se publique la versión **v0.2.0**.

---

# 18. Próxima Prioridad

Una vez finalizado el Sprint actual, el siguiente objetivo será desarrollar la primera biblioteca de componentes Documentation.

Esta nueva familia permitirá extender el Framework más allá de los README y reutilizar documentación técnica entre distintos proyectos.

---

# 19. Gestión del Proyecto

El desarrollo se organiza mediante Sprints.

Cada Sprint deberá comenzar revisando:

* PROJECT_STATUS
* ROADMAP
* BACKLOG

Y finalizar actualizando:

* PROJECT_STATUS
* BITÁCORA
* CHANGELOG

Cuando corresponda también se publicará un nuevo tag siguiendo Semantic Versioning.

---

# 20. Estado General

Actualmente el proyecto dispone de una arquitectura estable y una base documental consolidada.

La prioridad deja de ser el diseño del Framework y pasa a ser la implementación progresiva de funcionalidades reales que permitan validar todas las decisiones arquitectónicas adoptadas hasta la fecha.


---

# 21. Forma de Trabajo

GitHub Framework se desarrolla siguiendo un enfoque iterativo e incremental.

El objetivo es construir un Framework útil mediante pequeñas entregas frecuentes, validando cada decisión arquitectónica mediante implementaciones reales.

La prioridad es entregar valor de forma continua, evitando fases prolongadas de diseño sin resultados tangibles.

---

# 22. Ciclo de Desarrollo

Todo desarrollo del Framework seguirá, siempre que sea posible, el siguiente ciclo de trabajo.

```text id="cycle001"
Planificar

↓

Implementar

↓

Utilizar el Framework

↓

Validar

↓

Refactorizar

↓

Versionar

↓

Documentar
```

Este ciclo pretende garantizar que todas las decisiones se apoyan en experiencia práctica y no únicamente en hipótesis de diseño.

---

# 23. Dogfooding

GitHub Framework utiliza el principio de *dogfooding*.

Toda nueva funcionalidad deberá utilizarse primero dentro del propio proyecto antes de recomendar su uso en otros repositorios.

Este enfoque permite:

* detectar limitaciones;
* simplificar componentes;
* validar estándares;
* mejorar la experiencia de uso.

El propio repositorio GitHub Framework constituye la primera implementación de referencia del Framework.

---

# 24. Component Driven Development

El desarrollo del proyecto sigue un enfoque basado en componentes reutilizables.

Siempre que sea posible:

* primero se diseñará un componente;
* posteriormente se validará mediante una implementación real;
* finalmente podrá reutilizarse en otros repositorios.

El objetivo es evitar soluciones específicas cuando puedan transformarse en activos reutilizables.

---

# 25. Gestión de Sprints

El trabajo se organiza mediante Sprints de alcance reducido.

Cada Sprint deberá definir:

* un objetivo principal;
* entregables concretos;
* criterios de finalización (*Definition of Done*).

Siempre se priorizarán entregas pequeñas frente a grandes desarrollos difíciles de validar.

---

# 26. Gestión del Backlog

Todo trabajo pendiente deberá registrarse en el Product Backlog.

Las nuevas ideas no deberán desarrollarse inmediatamente.

Primero deberán evaluarse atendiendo a:

* utilidad;
* reutilización;
* prioridad;
* impacto sobre el Framework.

Las funcionalidades sin un caso de uso real permanecerán en el apartado **Icebox** hasta que exista una necesidad objetiva.

---

# 27. Versionado

El proyecto utiliza Semantic Versioning.

Cada nueva versión deberá incluir:

* actualización del CHANGELOG;
* revisión del PROJECT_STATUS;
* actualización de la BITÁCORA;
* creación del correspondiente tag cuando proceda.

Las versiones representan hitos funcionales del proyecto y no únicamente acumulación de cambios.

---

# 28. Gestión de Cambios

La arquitectura principal del proyecto se considera estable.

Las modificaciones deberán responder siempre a una necesidad identificada durante la implementación.

Antes de modificar la arquitectura deberá comprobarse si el problema puede resolverse mediante:

* un nuevo componente;
* una nueva plantilla;
* una mejora de un componente existente.

La reorganización estructural del repositorio será el último recurso.

---

# 29. Criterios para Nuevos Componentes

Antes de incorporar un nuevo componente deberán responderse las siguientes preguntas:

1. ¿Resuelve un problema real?
2. ¿Será reutilizable?
3. ¿Mantiene una única responsabilidad?
4. ¿Evita duplicidades?
5. ¿Existe una implementación que permita validarlo?

Si alguna respuesta es negativa, deberá reconsiderarse su incorporación.

---

# 30. Rol Esperado del Asistente

Durante el desarrollo del proyecto se espera que el asistente actúe como:

* Principal Software Architect.
* Tech Lead.
* Framework Maintainer.
* Revisor técnico.
* Mentor de buenas prácticas.

Las recomendaciones deberán priorizar siempre:

* simplicidad;
* mantenibilidad;
* reutilización;
* calidad;
* visión a largo plazo.

No deberán proponerse soluciones complejas cuando exista una alternativa más sencilla que satisfaga adecuadamente los objetivos del proyecto.

---

# 31. Decisiones Arquitectónicas Consolidadas

Durante la fase de diseño se analizaron distintas alternativas arquitectónicas.

Las decisiones recogidas en esta sección se consideran consolidadas y únicamente deberán revisarse cuando una implementación real demuestre una necesidad objetiva.

---

## Identidad del Proyecto

El proyecto adopta definitivamente el nombre:

**GitHub Framework**

Queda descartada la denominación inicial **GitHub Profile**, ya que el alcance del proyecto supera ampliamente la construcción de perfiles personales.

GitHub Framework constituye un framework reutilizable para el diseño y mantenimiento de repositorios profesionales.

---

## Arquitectura del Repositorio

La estructura principal del repositorio se considera estable.

No deberán realizarse reorganizaciones generales del árbol de directorios salvo que exista una justificación técnica derivada de la implementación.

La evolución del proyecto deberá producirse principalmente mediante nuevos componentes, plantillas y herramientas.

---

## Organización Documental

La documentación permanecerá organizada mediante áreas funcionales independientes.

Actualmente:

* architecture
* standards
* design-system
* governance
* implementation

Esta organización se considera suficientemente flexible para soportar la evolución futura del Framework.

---

## Componentes

Los componentes constituyen la unidad básica de reutilización del Framework.

Cada componente mantendrá una estructura homogénea basada en:

* metadata.yml
* template.md
* README.md

Cuando resulte necesario también podrá incorporar:

* example.md

No se añadirán nuevos archivos salvo que exista una necesidad claramente justificada.

---

## Idioma

Se adopta la siguiente política lingüística.

### Inglés

* README principal.
* Componentes.
* Identificadores.
* Metadatos técnicos.
* Nombres de archivos.
* Directorios.

### Español

* Documentación interna.
* Arquitectura.
* Gobierno.
* Explicaciones.
* Documentación de diseño.

Esta separación se considera definitiva.

---

# 32. Conocimiento Consolidado

Durante la fase de arquitectura se han identificado los siguientes principios fundamentales.

## Simplicidad

El Framework deberá permanecer tan simple como sea posible.

La incorporación de nuevas funcionalidades deberá justificarse mediante casos de uso reales.

---

## Reutilización

Siempre que resulte viable se preferirá reutilizar componentes existentes frente a crear nuevas soluciones específicas.

---

## Implementación antes que Documentación

La documentación deberá apoyar la implementación.

No deberá crecer más rápido que el propio Framework.

---

## Casos de Uso Reales

Las decisiones arquitectónicas deberán validarse utilizando proyectos reales.

El Framework evolucionará a partir de necesidades observadas durante su utilización.

---

## Dogfooding

El propio GitHub Framework constituye el primer consumidor del Framework.

Las implementaciones desarrolladas para este repositorio servirán como referencia para el resto de proyectos.

---

# 33. Riesgos Conocidos

Actualmente se consideran los siguientes riesgos principales.

## Sobrearquitectura

Existe el riesgo de introducir complejidad innecesaria mediante componentes, documentos o estructuras que todavía no responden a necesidades reales.

---

## Crecimiento del Alcance

El proyecto abarca múltiples áreas:

* documentación;
* componentes;
* plantillas;
* automatización;
* herramientas.

Será necesario mantener una adecuada priorización para evitar desviaciones del objetivo principal.

---

## Duplicidad Documental

Toda nueva documentación deberá comprobar previamente si la información ya existe en otro documento del proyecto.

Cada documento debe mantener una única responsabilidad.

---

## Automatización Prematura

La automatización constituye un objetivo del proyecto, pero no deberá desarrollarse antes de consolidar el conocimiento que pretende automatizar.

---

# 34. Próximas Prioridades

Tras finalizar la fase de arquitectura, las prioridades del proyecto serán las siguientes.

1. Finalizar el README oficial.
2. Completar la preparación Open Source.
3. Publicar la versión v0.2.0.
4. Desarrollar los primeros Documentation Components.
5. Diseñar Repository Templates.
6. Iniciar las primeras herramientas del Framework.

---

# 35. Qué No Debe Volver a Discutirse

Salvo que aparezcan nuevas evidencias derivadas de la implementación, se consideran cerradas las siguientes decisiones.

* Nombre oficial del proyecto.
* Arquitectura principal del repositorio.
* Organización documental.
* Idioma de la documentación.
* Metodología basada en componentes.
* Uso de Semantic Versioning.
* Metodología basada en Sprints.
* Dogfooding como estrategia de validación.
* Desarrollo incremental mediante entregables pequeños.

Estas decisiones constituyen la línea base del proyecto y deberán considerarse estables durante las siguientes fases de desarrollo.

---

# 36. Quick Onboarding

Esta sección describe el recorrido recomendado para incorporarse al proyecto.

Su objetivo es reducir el tiempo necesario para comprender el estado del Framework y comenzar a trabajar de forma productiva.

---

## Primera incorporación

Si es la primera vez que se participa en el proyecto, se recomienda seguir el siguiente orden de lectura.

1. README.md
2. PROJECT_STATUS.md
3. ROADMAP.md
4. BACKLOG.md
5. WORKING_AGREEMENTS.md
6. CONTINUITY_KIT.md

Posteriormente podrá consultarse el resto de la documentación según las necesidades de cada tarea.

---

## Incorporación durante el desarrollo

Si el proyecto ya se conoce y únicamente se desea retomar el trabajo, normalmente será suficiente revisar:

* PROJECT_STATUS
* BACKLOG
* CHANGELOG
* BITÁCORA

Estos documentos permiten comprender rápidamente el estado actual del proyecto y las prioridades del Sprint en curso.

---

# 37. Cómo Comenzar un Nuevo Sprint

Antes de iniciar cualquier Sprint se recomienda seguir el siguiente proceso.

## Paso 1

Revisar el estado del proyecto.

Documentos:

* PROJECT_STATUS
* ROADMAP

---

## Paso 2

Consultar el trabajo pendiente.

Documento:

* BACKLOG

---

## Paso 3

Revisar los cambios recientes.

Documentos:

* CHANGELOG
* BITÁCORA

---

## Paso 4

Seleccionar el objetivo del Sprint.

El Sprint deberá tener un único objetivo principal claramente definido.

---

## Paso 5

Implementar.

Siempre que sea posible mediante pequeñas entregas.

---

# 38. Cierre de un Sprint

Al finalizar un Sprint deberán realizarse las siguientes acciones.

* Actualizar PROJECT_STATUS.
* Añadir una nueva entrada a la BITÁCORA.
* Actualizar CHANGELOG.
* Revisar ROADMAP (si procede).
* Publicar un nuevo tag cuando corresponda.

---

# 39. Contexto para Asistentes de IA

Cuando un asistente de IA participe en el proyecto deberá asumir el siguiente rol.

## Rol

* Principal Software Architect.
* Senior Tech Lead.
* Framework Maintainer.
* Revisor técnico.
* Mentor de buenas prácticas.

---

## Prioridades

Las recomendaciones deberán priorizar siempre:

1. Simplicidad.
2. Reutilización.
3. Calidad.
4. Mantenibilidad.
5. Evolución progresiva.

---

## Restricciones

El asistente deberá evitar:

* sobrearquitectura;
* duplicidad documental;
* componentes innecesarios;
* cambios estructurales sin justificación;
* automatización prematura.

---

## Filosofía

Las decisiones deberán apoyarse siempre en implementaciones reales.

El Framework evoluciona mediante la experiencia obtenida durante su utilización y no mediante hipótesis teóricas.

---

# 40. Criterios para Retomar el Proyecto

Antes de introducir nuevas funcionalidades deberán responderse las siguientes preguntas.

1. ¿Cuál es el objetivo del Sprint actual?
2. ¿Qué prioridad tiene la tarea?
3. ¿Existe ya un componente reutilizable?
4. ¿Debe evolucionar un componente existente en lugar de crear uno nuevo?
5. ¿La solución mantiene la simplicidad del Framework?

Si alguna de estas preguntas no puede responderse con claridad, se recomienda revisar previamente la documentación de gobierno.

---

# 41. Visión a Largo Plazo

GitHub Framework aspira a convertirse en una plataforma reutilizable para diseñar, construir y mantener repositorios profesionales.

La evolución prevista del proyecto incluye:

* ampliación de la biblioteca de componentes;
* desarrollo de plantillas reutilizables;
* herramientas de validación;
* automatización documental;
* generación de repositorios;
* herramientas de línea de comandos;
* nuevas implementaciones de referencia.

Cada una de estas funcionalidades deberá desarrollarse únicamente cuando exista una necesidad demostrada y manteniendo los principios fundamentales del Framework.

---

# 42. Mensaje Final

GitHub Framework no pretende ser únicamente una colección de documentos o plantillas.

Su objetivo es proporcionar una forma consistente de diseñar, documentar y evolucionar repositorios aplicando principios de ingeniería del software.

La prioridad no es construir el Framework más grande, sino uno que permanezca útil, mantenible y reutilizable durante muchos años.

Cada decisión futura deberá respetar esta filosofía.

---

# Historial

| Versión | Fecha      | Descripción                                                                                               |
| ------- | ---------- | --------------------------------------------------------------------------------------------------------- |
| 1.0.0   | 2026-08-07 | Primera versión del Continuity Kit, utilizada como documento de incorporación y continuidad del proyecto. |
| 1.1.0   | 2026-11-14 | Incorporación del snapshot de continuidad post-release y del Assessment documental Complete de Only Film; preservación histórica del contenido de agosto. |
