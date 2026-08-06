# README-HERO · Example

Este documento muestra una implementación de referencia del componente **README-HERO** utilizando el proyecto **NovaCoquinaria**.

---

# Input

```yaml
project_name: NovaCoquinaria

tagline: >
  Plataforma de ingeniería del conocimiento culinario basada en recetas,
  ingredientes, técnicas y relaciones semánticas.

alignment: center

banner:

  source: assets/banner.png

  alt: Banner oficial de NovaCoquinaria

  link: https://github.com/fran-eliot/NovaCoquinaria

badges:

  - label: Version
    image: https://img.shields.io/badge/version-1.2.0-blue
    alt: Version

  - label: Status
    image: https://img.shields.io/badge/status-active-success
    alt: Status

  - label: License
    image: https://img.shields.io/badge/license-MIT-green
    alt: License

  - label: Documentation
    image: https://img.shields.io/badge/docs-available-blue
    alt: Documentation

short_description: >
  Sistema de gestión del conocimiento gastronómico diseñado para organizar,
  relacionar y reutilizar información culinaria mediante una arquitectura
  documental modular.
```

---

# Rendered Output

```markdown
<p align="center">
  <a href="https://github.com/fran-eliot/NovaCoquinaria">
    <img
      src="assets/banner.png"
      alt="Banner oficial de NovaCoquinaria"
      width="100%"
    />
  </a>
</p>

<h1 align="center">
NovaCoquinaria
</h1>

<p align="center">
<strong>
Plataforma de ingeniería del conocimiento culinario basada en recetas,
ingredientes, técnicas y relaciones semánticas.
</strong>
</p>

<p align="center">

<img src="https://img.shields.io/badge/version-1.2.0-blue" alt="Version"/>

<img src="https://img.shields.io/badge/status-active-success" alt="Status"/>

<img src="https://img.shields.io/badge/license-MIT-green" alt="License"/>

<img src="https://img.shields.io/badge/docs-available-blue" alt="Documentation"/>

</p>

<p align="center">

Sistema de gestión del conocimiento gastronómico diseñado para organizar,
relacionar y reutilizar información culinaria mediante una arquitectura
documental modular.

</p>
```

---

# Component Analysis

## Obligatorios

| Elemento     | Estado |
| ------------ | ------ |
| Banner       | ✓      |
| Project Name | ✓      |
| Tagline      | ✓      |

---

## Opcionales

| Elemento          | Estado |
| ----------------- | ------ |
| Badges            | ✓      |
| Short Description | ✓      |

---

# Quality Validation

| Rule                            | Result |
| ------------------------------- | ------ |
| Único H1                        | ✓      |
| Menos de seis badges            | ✓      |
| Banner con texto alternativo    | ✓      |
| Compatible con Dark Mode        | ✓      |
| Compatible con Light Mode       | ✓      |
| Orden correcto de los elementos | ✓      |

---

# Supported Repository Types

Este ejemplo puede utilizarse como referencia para:

* Backend
* Full Stack
* AI
* Documentation
* Library
* GitHub Profile

---

# Variants

El componente admite distintas configuraciones.

## Minimal

* Sin banner.
* Sin descripción.
* Dos badges.

---

## Standard

* Banner.
* Cuatro badges.
* Descripción breve.

---

## Strategic

* Banner.
* Cinco o seis badges.
* Descripción.
* Integración con el resto del Design System.

---

# Notes

Este ejemplo pretende ilustrar el uso correcto del componente.

No representa el README completo del proyecto.

Únicamente la implementación del componente **README-HERO**.

---

# Related Components

* README-STATUS
* README-OVERVIEW
* VCL-HERO
* VCL-BANNER
* VCL-BADGES

---

# Revision History

| Version | Date       | Description                                        |
| ------- | ---------- | -------------------------------------------------- |
| 1.0.0   | 2026-08-06 | Primer ejemplo oficial del componente README-HERO. |
