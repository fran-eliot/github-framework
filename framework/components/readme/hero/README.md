# README-HERO

## Overview

`README-HERO` es el componente responsable de construir la cabecera de un repositorio.

Su objetivo es presentar la identidad del proyecto de forma clara, profesional y consistente con el GitHub Framework.

---

# Cuándo utilizarlo

Este componente debe utilizarse en todos los repositorios creados con el Framework.

Es obligatorio para cualquier repositorio de nivel **L2** o superior.

---

# Responsabilidades

El componente muestra:

* Banner (opcional)
* Nombre del proyecto
* Tagline
* Badges principales
* Descripción breve (opcional)

No debe incluir:

* Arquitectura
* Instalación
* Roadmap
* Documentación técnica

---

# Archivos

| Archivo        | Descripción                  |
| -------------- | ---------------------------- |
| `metadata.yml` | Metadatos del componente     |
| `template.md`  | Plantilla reutilizable       |
| `example.md`   | Implementación de referencia |
| `README.md`    | Documentación del componente |

---

# Dependencias

Recomendadas:

* `VCL-HERO`
* `VCL-BANNER`
* `VCL-BADGES`

---

# Componentes relacionados

Después de este componente normalmente aparecerán:

* `README-STATUS`
* `README-OVERVIEW`

---

# Buenas prácticas

* Utilizar un único H1.
* Mantener un tagline breve y específico.
* Limitar el número de badges.
* Mantener una estructura limpia.
* Verificar la visualización en modo claro y oscuro.

---

# Estado

| Campo     | Valor       |
| --------- | ----------- |
| ID        | README-HERO |
| Versión   | 1.0.0       |
| Estado    | Stable      |
| Prioridad | Required    |

---

# Historial

| Versión | Fecha      | Descripción                     |
| ------- | ---------- | ------------------------------- |
| 1.0.0   | 2026-08-06 | Primera versión del componente. |
