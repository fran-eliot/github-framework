# 12 - PROJECT STATUS

| Campo                    | Valor                          |
| ------------------------ | ------------------------------ |
| **Proyecto**             | GitHub Framework               |
| **Versión actual**       | v0.5.0                         |
| **Estado**               | En desarrollo                  |
| **Fase**                 | Framework Automation           |
| **Sprint actual**        | Sprint 8 — Framework Automation |
| **Última actualización** | 2026-09-17                     |

---

# Estado General

GitHub Framework ha completado las fases de arquitectura, Open Source Readiness, Documentation Framework y Repository Templates.

El Framework dispone actualmente de una arquitectura formal, estándares de repositorio, un sistema de Components reutilizables, mecanismos de gobierno, una biblioteca de Documentation Components y una primera familia de Repository Templates validadas mediante Reference Implementation y dogfooding.

El Sprint 7 — Workflow Framework ha finalizado.

Durante este Sprint se ha definido la Workflow Component Architecture y se han implementado los primeros Core Workflow Components:

- `WCL-ISSUE`.
- `WCL-BRANCH`.
- `WCL-COMMIT`.
- `WCL-PULL-REQUEST`.
- `WCL-CODE-REVIEW`.

Los Core Workflow Components han sido validados mediante una primera Workflow Reference Implementation basada en dogfooding sobre el propio GitHub Framework.

La validación ha confirmado distintos mecanismos de materialización, incluyendo Community Files, Configuration y Convention, así como la separación entre clasificación de implementación, lifecycle y estado de validación.

A partir de la evidencia obtenida se han consolidado los Workflow Component Standards, manteniendo los cinco Core Workflow Components como `Implemented`, en lifecycle `Experimental` y con Reference Implementation `Validated`.

El alcance de Sprint 7 está completado y la release `v0.5.0 — Workflow Framework` ha sido integrada en `main`, etiquetada y publicada.

Tras la publicación de `v0.5.0`, se ha realizado una fase de discovery para definir el alcance de `v0.6.0 — Framework Automation`.

El análisis de los 21 Framework Components actualmente implementados ha identificado tres familias físicas —README, Documentation y Workflow— y ha confirmado la viabilidad de establecer un contrato común de metadata sin pérdida de semántica específica por familia.

Como resultado del discovery, `v0.6.0` se centrará en la definición de un Common Component Metadata Schema, la normalización de los metadata existentes, la implementación del primer Framework Validator y su validación mediante Reference Implementation y dogfooding.

La generación de componentes y repositorios queda fuera del alcance de `v0.6.0`. La automatización se limitará inicialmente a operaciones deterministas sobre contratos ya demostrados por el Framework.

Tras validar este alcance se ha abierto formalmente el Sprint 8 — Framework Automation, asociado a la milestone `v0.6.0 — Framework Automation`.

El Sprint se estructura en cuatro historias sucesivas: Component Metadata Standard (#23), Component Metadata Normalization (#24), Framework Validator (#25) y Automation Reference Implementation (#26).

La implementación comenzará por la formalización del contrato común de metadata antes de modificar los Components existentes o desarrollar tooling de validación.

---

# Estado por Áreas

| Área | Estado |
| ---- | :----: |
| Arquitectura del Framework | ✅ |
| GitHub Repository Standards (GRS) | ✅ |
| Repository Design System (RDS) | ✅ |
| Component Catalog | ✅ |
| Componentes README | ✅ |
| Open Source Readiness | ✅ |
| Documentation Component Architecture | ✅ |
| Core Documentation Components | ✅ |
| Documentation Reference Implementation | ✅ |
| Documentation Writing Standards | ✅ |
| Repository Template Architecture | ✅ |
| Core Repository Templates | ✅ |
| Repository Template Reference Implementation | ✅ |
| Repository Template Standards | ✅ |
| Workflow Component Architecture | ✅ |
| Core Workflow Components | ✅ |
| Workflow Reference Implementation | ✅ |
| Workflow Component Standards | ✅ |
| Component Metadata Standard | ⚪ |
| Component Metadata Normalization | ⚪ |
| Framework Validator | ⚪ |
| Automation Reference Implementation | ⚪ |

---

# Sprint Actual

## Sprint 8 — Framework Automation

**Target:** `v0.6.0`

### Objetivo

Introducir capacidades de automatización deterministas sobre el modelo de componentes de GitHub Framework, partiendo de un contrato común de metadata, normalizando los Components implementados y validando el propio Framework mediante su primer Framework Validator.

### Historias

| Issue | Historia | Prioridad | Estado |
| ----- | -------- | :-------: | :----: |
| #23 | Component Metadata Standard | Alta | Todo |
| #24 | Component Metadata Normalization | Alta | Todo |
| #25 | Framework Validator | Alta | Todo |
| #26 | Automation Reference Implementation | Media | Todo |

---

# Próximo Hito

## Versión objetivo

**v0.6.0 — Framework Automation**

### Definition of Done

- [ ] Common Component Metadata Schema definido.
- [ ] Metadata de los Framework Components implementados normalizada.
- [ ] Framework Validator implementado.
- [ ] Reglas de validación deterministas definidas.
- [ ] Validación de estructura física y artefactos implementada.
- [ ] Resultados legibles y códigos de salida deterministas disponibles.
- [ ] Punto de entrada CLI mínimo disponible.
- [ ] Automation Reference Implementation completada.
- [ ] Dogfooding sobre GitHub Framework completado.

---

# Riesgos

Actualmente se identifican los siguientes riesgos:

- Sobrearquitectura del Framework.
- Crecimiento de componentes sin casos de uso reales.
- Duplicidad documental.
- Incremento innecesario de complejidad.
- Divergencia entre los componentes reutilizables y sus implementaciones reales.
- Automatizar inconsistencias históricas en lugar de normalizar primero los contratos del Framework.
- Introducir tooling más complejo que los problemas deterministas que pretende resolver.

---

# Principios Activos

Durante la evolución del proyecto se mantendrán los siguientes principios:

* Simplicidad.
* Reutilización.
* Modularidad.
* Dogfooding.
* Versionado continuo.
* Documentación como soporte, no como fin.

---

# Próximos Objetivos

1. Completar #23 — Component Metadata Standard.
2. Normalizar los metadata existentes mediante #24 antes de implementar tooling.
3. Implementar #25 — Framework Validator sobre el contrato normalizado.
4. Validar la automatización mediante #26 — Automation Reference Implementation y dogfooding.

---

# Historial de Versiones

| Versión | Fecha      | Estado                  |
| ------- | ---------- | ----------------------- |
| v0.1.0 | 2026-08-07 | Arquitectura completada |
| v0.2.0 | 2026-08-09 | Open Source Readiness completado |
| v0.3.0 | 2026-08-13 | Documentation Framework completado |
| v0.4.0 | 2026-08-18 | Repository Templates completado |
| v0.5.0 | 2026-09-14 | Workflow Framework completado |