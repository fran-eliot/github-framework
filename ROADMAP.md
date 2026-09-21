# GitHub Framework Roadmap

Este roadmap describe la evolución prevista del proyecto.

Las versiones podrán ajustarse conforme evolucione el Framework.

---

# v0.2.0 — Open Source Readiness

**Estado:** ✅ Released

## Objetivos

* README oficial del Framework.
* LICENSE.
* Documentación de gobierno.
* Preparación de `.github/`.
* Consolidación de la estructura del repositorio.

---

# v0.3.0 — Documentation Framework

**Estado:** ✅ Released

## Objetivos

* Documentation Component Architecture.
* Core Documentation Components.
* Documentation Reference Implementation.
* Documentation Writing Standards.
* Validación mediante dogfooding.

---

# v0.4.0 — Repository Templates

**Estado:** ✅ Released

## Objetivos

* Repository Template Architecture.
* Core Repository Templates.
* Repository Template Reference Implementation.
* Repository Template Standards.
* Validación mediante dogfooding.

---

# v0.5.0 — Workflow Framework

**Estado:** ✅ Released

## Objetivos

* Definir la Workflow Component Architecture.
* Implementar los Core Workflow Components.
* Validar los Core Workflow Components mediante Reference Implementation y dogfooding.
* Consolidar los Workflow Component Standards.
* Preparar una primera Workflow Component Library reutilizable.

---

# v0.6.0 — Framework Automation

**Estado:** ⏳ Implementation completed and merged into `main` — release pending

## Objetivo

Introducir capacidades de automatización deterministas sobre el modelo de componentes de GitHub Framework, partiendo de un contrato de metadata común y validando el propio Framework mediante sus herramientas.

## Alcance

### Component Metadata Standard

* Definir un contrato común de metadata para los Framework Components implementados.
* Establecer un núcleo compartido entre las familias README, Documentation y Workflow.
* Preservar extensiones específicas de cada familia.
* Normalizar la representación de valores comunes sin alterar su semántica.

### Component Metadata Normalization

* Migrar los componentes implementados al contrato común de metadata.
* Eliminar diferencias estructurales innecesarias entre formatos existentes.
* Preservar estados de lifecycle, prioridades y semántica específica de cada componente.
* Validar la normalización antes de construir tooling sobre ella.

### Framework Validator

* Descubrir los componentes implementados desde `framework/components/`.
* Validar metadata mediante reglas deterministas.
* Aplicar reglas comunes y reglas específicas por familia.
* Validar estructura física y artefactos declarados.
* Detectar identificadores duplicados, referencias inválidas e inconsistencias estructurales.
* Producir resultados legibles y códigos de salida deterministas.

### Automation Reference Implementation

* Ejecutar el Framework Validator sobre el propio repositorio GitHub Framework.
* Validar mediante dogfooding el contrato de metadata normalizado.
* Proporcionar un punto de entrada CLI mínimo para la validación.
* Documentar los patrones de automatización demostrados y sus límites.

## Fuera de alcance

* Generadores de componentes o repositorios.
* Reescritura automática de documentación libre.
* Publicación automática de releases.
* Orquestación compleja mediante GitHub Actions.
* Bots o mantenimiento autónomo de repositorios.
* Sistemas de plugins o plataformas extensibles de reglas.
* Interfaces gráficas o servicios de automatización.
* Automatización de decisiones arquitectónicas o de diseño.

## Principio de la Release

> Automation follows demonstrated architecture: normalize established contracts first, then automate deterministic operations over them.

---

## Resultado de implementación — Sprint 8

**Estado funcional:** Completed.

Las cuatro historias previstas para `v0.6.0` han sido implementadas y cerradas:

| Issue | Entregable                          | Estado |
| ----- | ----------------------------------- | ------ |
| #23   | Component Metadata Standard         | Done   |
| #24   | Component Metadata Normalization    | Done   |
| #25   | Framework Validator                 | Done   |
| #26   | Automation Reference Implementation | Done   |

### Evidencias de validación

* Los 21 Components implementados han sido normalizados y validados.
* El Framework Validator dispone de reglas deterministas para el Common Core, la identidad, la unicidad, la madurez, las dependencias y las extensiones Workflow.
* El CLI proporciona informes legibles y códigos de salida `0` y `1`.
* La batería completa de 109 tests ha finalizado correctamente.
* La Automation Reference Implementation ha sido validada mediante dogfooding sobre GitHub Framework.

La implementación de referencia y sus limitaciones están documentadas en `docs/implementation/22_AUTOMATION_REFERENCE_IMPLEMENTATION.md`.

### Integración

La implementación de Framework Automation se integró en `main` mediante el Pull Request #27, con el commit de merge `4b357d8`.

Las cuatro historias (#23–#26) están completadas y cerradas. La preparación documental de la release se realiza en la rama `chore/v0.6.0-post-merge`.

### Pendiente para la publicación

* Finalizar y revisar la documentación de release.
* Integrar la rama `chore/v0.6.0-post-merge` en `main`.
* Crear el tag `v0.6.0` y publicar la release en GitHub.
* Verificar el estado del repositorio tras la publicación.

La implementación funcional y su integración en `main` están completadas. La versión publicada continúa siendo `v0.5.0` hasta que se publique `v0.6.0`.

---

# v1.0.0 — Stable Release

**Estado:** ⚪ Planned

## Objetivos

* Framework completamente funcional.
* Generación consistente de repositorios.
* Biblioteca estable de componentes.
* Documentación consolidada.
* Primera versión estable del Framework.

---

# Visión

GitHub Framework aspira a convertirse en un marco de referencia para diseñar, documentar y mantener repositorios profesionales mediante estándares de ingeniería, componentes reutilizables y una arquitectura consistente.

---

# Principios del Roadmap

El roadmap representa la dirección prevista del proyecto.

Las versiones podrán cambiar conforme evolucionen las necesidades del Framework.

Las prioridades vendrán determinadas por el Product Backlog.