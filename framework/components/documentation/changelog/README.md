# DOC-CHANGELOG — Changelog

## 1. Propósito

`DOC-CHANGELOG` define una estructura reutilizable para registrar los cambios relevantes publicados durante la evolución de un proyecto.

Su objetivo es permitir que usuarios, colaboradores y maintainers puedan comprender qué ha cambiado entre versiones sin necesidad de interpretar directamente el historial de commits.

El Changelog representa la evolución publicada del proyecto.

---

## 2. Cuándo utilizarlo

Se recomienda utilizar este componente cuando un proyecto:

- publica versiones identificables;
- utiliza Semantic Versioning u otro esquema de versionado;
- necesita comunicar cambios entre releases;
- mantiene compatibilidad con usuarios o consumidores;
- evoluciona de forma continuada.

Resulta especialmente recomendable en repositorios públicos y proyectos de madurez `L2` o superior.

---

## 3. Cuándo no utilizarlo

Puede no ser necesario cuando:

- el repositorio es experimental y de vida muy corta;
- no existen versiones o releases diferenciadas;
- el historial de cambios no aporta información útil a consumidores externos;
- otro mecanismo constituye explícitamente la fuente oficial de cambios.

El Changelog no debe mantenerse únicamente por formalismo.

---

## 4. Responsabilidad

`DOC-CHANGELOG` responde principalmente a la pregunta:

> ¿Qué cambios relevantes se han publicado entre las distintas versiones del proyecto?

No sustituye a:

- Git history;
- Pull Requests;
- Issues;
- `DOC-RELEASE-NOTES`;
- `DOC-PROJECT-STATUS`;
- `DOC-ROADMAP`.

El Changelog resume cambios publicados.

No debe convertirse en un registro exhaustivo de commits ni en una bitácora de desarrollo.

---

## 5. Estructura

El componente sigue una estructura cronológica inversa:

```text
Unreleased
    ↓
Latest Release
    ↓
Previous Release
    ↓
Older Releases
```

Cada versión podrá agrupar sus cambios mediante categorías semánticas.

---

## 6. Unreleased

La sección:

```text
[Unreleased]
```

recoge cambios relevantes que ya forman parte del desarrollo pero todavía no han sido incluidos en una versión publicada.

Permite preparar progresivamente el siguiente Changelog sin esperar al momento de crear la release.

Cuando se publica una nueva versión, los cambios correspondientes se trasladan desde `Unreleased` hacia la nueva sección versionada.

La sección deberá permanecer disponible aunque temporalmente no contenga cambios.

---

## 7. Versiones

Cada versión publicada seguirá el formato:

```text
[VERSION] - YYYY-MM-DD
```

Ejemplo:

```text
[0.3.0] - 2026-08-10
```

Las versiones se ordenarán desde la más reciente hasta la más antigua.

Cuando el proyecto utilice Semantic Versioning, el número de versión deberá corresponder con la release publicada.

---

## 8. Categorías de Cambios

Los cambios podrán organizarse mediante categorías semánticas.

Las categorías recomendadas son:

### Added

Nuevas funcionalidades, capacidades, componentes o elementos incorporados.

### Changed

Cambios relevantes sobre funcionalidades o comportamientos existentes.

### Deprecated

Funcionalidades que continúan disponibles pero cuyo uso deja de recomendarse.

### Removed

Funcionalidades o elementos eliminados.

### Fixed

Correcciones de errores.

### Security

Correcciones o mejoras relacionadas con seguridad.

Solo deberán aparecer las categorías que contengan cambios.

No deberán mantenerse secciones vacías por uniformidad visual.

---

## 9. Granularidad

Cada entrada debe describir un cambio relevante desde la perspectiva del consumidor del proyecto.

Debe evitarse registrar:

- commits individuales;
- cambios puramente cosméticos;
- refactors internos sin impacto relevante;
- tareas administrativas sin efecto sobre el producto;
- detalles excesivamente técnicos que pertenezcan a otros documentos.

Ejemplo adecuado:

```text
- Added reusable Documentation Components.
```

Ejemplo demasiado granular:

```text
- Renamed local variable in documentation validation script.
```

---

## 10. Orden

El Changelog seguirá dos niveles de ordenación.

### Versiones

Orden cronológico inverso:

```text
Unreleased
0.3.0
0.2.0
0.1.0
```

### Categorías

No se exige que aparezcan todas las categorías ni que mantengan siempre el mismo orden.

Cuando se utilicen varias, se recomienda:

```text
Added
Changed
Deprecated
Removed
Fixed
Security
```

La claridad prevalece sobre la rigidez formal.

---

## 11. Relación con Releases

El Changelog y las Release Notes tienen responsabilidades relacionadas pero diferentes.

```text
Development Changes
        ↓
DOC-CHANGELOG
        ↓
Release
        ↓
DOC-RELEASE-NOTES
```

El Changelog mantiene el historial estructurado y acumulativo del proyecto.

Las Release Notes pueden proporcionar contexto adicional, highlights, instrucciones de migración o información específica de una publicación.

No debe mantenerse el mismo contenido detallado en ambos lugares.

---

## 12. Relación con Semantic Versioning

Cuando el proyecto utilice Semantic Versioning:

```text
MAJOR.MINOR.PATCH
```

los cambios registrados deberán corresponder con la versión publicada.

El Changelog no determina por sí mismo qué incremento de versión debe realizarse.

La estrategia de versionado pertenece a la gobernanza del proyecto.

--- 

## 13. Reglas de Contenido

El Changelog debe:

- registrar únicamente cambios relevantes;
- utilizar lenguaje claro y conciso;
- mantener orden cronológico inverso;
- distinguir cambios no publicados de releases publicadas;
- mantener correspondencia con las versiones reales del proyecto;
- evitar información redundante con otros documentos.

Cada entrada debe poder comprenderse sin consultar el commit que originó el cambio.

---

## 14. Mantenimiento

El documento deberá actualizarse:

- cuando se incorpore un cambio relevante;
- antes de publicar una nueva versión;
- cuando una funcionalidad sea deprecada o eliminada;
- cuando se publique una corrección relevante;
- cuando sea necesario registrar un cambio de seguridad publicable.

Al publicar una versión deberá comprobarse que:

1. los cambios correspondientes han salido de `Unreleased`;
2. la versión coincide con la release;
3. la fecha es correcta;
4. no permanecen categorías vacías.

---

## 15. Quality Gates

Antes de considerar válida una implementación:

- [ ] Existe una sección `Unreleased`.
- [ ] Las versiones están ordenadas de forma cronológica inversa.
- [ ] Cada release incluye versión y fecha.
- [ ] Las entradas describen cambios relevantes.
- [ ] No se registran commits individuales innecesariamente.
- [ ] No existen categorías vacías.
- [ ] Las versiones corresponden con releases reales.
- [ ] El contenido no duplica innecesariamente las Release Notes.

---

## 16. Estado del Componente

`DOC-CHANGELOG` se encuentra actualmente en estado `Experimental`.

Su contrato será validado mediante dogfooding sobre GitHub Framework antes de considerarse `Stable`.