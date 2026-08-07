# 15 - WORKING AGREEMENTS

## Objetivo

Este documento define los acuerdos de trabajo del proyecto GitHub Framework.

Su finalidad es mantener una forma de trabajo consistente durante toda la evolución del Framework.

---

# Arquitectura

La arquitectura principal del repositorio se considera estable.

No deberán realizarse cambios estructurales salvo que una implementación real demuestre una necesidad objetiva.

---

# Simplicidad

Se priorizarán siempre las soluciones más simples que resuelvan correctamente el problema.

Se evitará el sobre diseño.

---

# Componentes

Todo componente nuevo deberá:

* resolver un problema existente;
* ser reutilizable;
* mantener una única responsabilidad;
* aportar valor al Framework.

Siempre que sea posible deberá reutilizarse en al menos dos repositorios.

---

# Dogfooding

Toda funcionalidad nueva deberá utilizarse primero dentro del propio GitHub Framework antes de recomendar su uso en otros proyectos.

---

# Documentación

La documentación interna del Framework se redactará en español.

El contenido orientado al usuario final (README, documentación pública o ejemplos internacionales) se redactará en inglés.

---

# Gobierno

Cada Sprint finalizará actualizando:

* PROJECT_STATUS
* BITÁCORA
* CHANGELOG

Cuando corresponda también se revisará el ROADMAP y se publicará un nuevo tag.

---

# Versionado

Se seguirá Semantic Versioning.

Los cambios deberán reflejarse en CHANGELOG antes de crear un tag.

---

# Desarrollo

Se priorizarán:

* entregables pequeños;
* commits frecuentes;
* refactorización continua;
* validación mediante casos de uso reales.

---

# Calidad

Antes de incorporar una nueva funcionalidad se responderán las siguientes preguntas:

1. ¿Resuelve un problema real?
2. ¿Será reutilizable?
3. ¿Mantiene la simplicidad del Framework?
4. ¿Existe una implementación que la valide?

Si alguna respuesta es negativa, deberá reconsiderarse su incorporación.

---

# Filosofía del Proyecto

GitHub Framework pretende ayudar a construir repositorios con los mismos principios de calidad, organización y mantenibilidad que se aplican al desarrollo de software.

La documentación es un medio para conseguir ese objetivo, no un fin en sí misma.

---

# Revisión

Estos acuerdos podrán evolucionar conforme madure el proyecto, procurando mantener siempre la estabilidad y coherencia del Framework.

---

# Historial

| Versión | Fecha      | Descripción                                 |
| ------- | ---------- | ------------------------------------------- |
| 1.0.0   | 2026-08-07 | Primera versión de los acuerdos de trabajo. |
