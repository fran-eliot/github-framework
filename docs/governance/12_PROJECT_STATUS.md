# 12 - PROJECT STATUS

| Campo                    | Valor                          |
| ------------------------ | ------------------------------ |
| **Proyecto**             | GitHub Framework               |
| **Versión actual**       | v0.4.0                         |
| **Estado**               | En desarrollo                  |
| **Fase**                 | Workflow Framework             |
| **Sprint actual**        | Sprint 7 — Workflow Framework  |
| **Última actualización** | 2026-08-19                     |

---

# Estado General

GitHub Framework ha completado las fases de arquitectura, Open Source Readiness y Documentation Framework.

El Framework dispone actualmente de una arquitectura formal, estándares de repositorio, un sistema de Components reutilizables, mecanismos de gobierno y una primera biblioteca de Documentation Components validada mediante dogfooding.

El proyecto se encuentra actualmente en Sprint 6 — Repository Templates.

Durante este Sprint se ha definido la Repository Template Architecture, se han implementado los primeros Core Repository Templates y se ha validado el modelo mediante una Reference Implementation basada en dogfooding sobre el propio GitHub Framework.

La validación ha permitido además formalizar los Repository Template Standards y consolidar las reglas de composición, conformidad, lifecycle y mantenimiento de futuras plantillas.

La auditoría de consistencia realizada durante la Reference Implementation ha permitido además refinar la clasificación `Implemented / Conceptual`, sincronizar el Component Catalog con las implementaciones físicas reales y distinguir entre disponibilidad de Framework Components y conformidad de repositorios consumidores.

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
| Workflow Component Architecture | 🟡 |
| Core Workflow Components | ⚪ |
| Workflow Reference Implementation | ⚪ |
| Workflow Component Standards | ⚪ |

---

# Sprint Actual

## Sprint 7 — Workflow Framework

**Target:** `v0.5.0`

### Objetivo

Transformar las responsabilidades Workflow actualmente conceptuales en una primera biblioteca reutilizable de Workflow Components, validada mediante implementación real y dogfooding.

### Historias

| Issue | Historia | Prioridad | Estado |
| ----- | -------- | :-------: | :----: |
| #17 | Workflow Component Architecture | Alta | ✅ |
| #18 | Core Workflow Components | Alta | ✅ |
| #19 | Workflow Reference Implementation | Alta | ⚪ |
| #20 | Workflow Component Standards | Media | ⚪ |

---

# Próximo Hito

## Versión objetivo

**v0.5.0 — Workflow Framework**

### Definition of Done

- [x] Workflow Component Architecture definida.
- [x] Contrato de implementación de Workflow Components establecido.
- [x] Core Workflow Components implementados.
- [x] Diferentes mecanismos de materialización validados.
- [ ] Reference Implementation completada.
- [ ] Dogfooding completado.
- [ ] Workflow Component Standards definidos.
- [x] Component Catalog actualizado cuando corresponda.
- [ ] Documentación de gobierno actualizada.
- [ ] Release `v0.5.0` preparada.

---

# Riesgos

Actualmente se identifican los siguientes riesgos:

- Sobrearquitectura del Framework.
- Crecimiento de componentes sin casos de uso reales.
- Duplicidad documental.
- Incremento innecesario de complejidad.
- Divergencia entre los componentes reutilizables y sus implementaciones reales.

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

1. Validar los Core Workflow Components mediante Reference Implementation y dogfooding (#19).
2. Refinar los Components según los findings de la Reference Implementation.
3. Formalizar Workflow Component Standards (#20).
4. Preparar `v0.5.0 — Workflow Framework`.

---

# Historial de Versiones

| Versión | Fecha      | Estado                  |
| ------- | ---------- | ----------------------- |
| v0.1.0 | 2026-08-07 | Arquitectura completada |
| v0.2.0 | 2026-08-09 | Open Source Readiness completado |
| v0.3.0 | 2026-08-13 | Documentation Framework completado |
| v0.4.0 | 2026-08-18 | Repository Templates completado |