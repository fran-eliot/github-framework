<h1 align="center">
  GitHub Framework
</h1>

🇪🇸 **Español** | 🇬🇧 [English](README.md)

<p align="center">
  <strong>Construye repositorios con la misma disciplina con la que se desarrolla el software.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v0.10.0-blue" alt="Versión" />
  <img src="https://img.shields.io/badge/status-active-success" alt="Estado" />
  <img src="https://img.shields.io/badge/license-MIT-green" alt="Licencia" />
</p>

<p align="center">
  Framework de ingeniería para diseñar, construir y mantener repositorios profesionales en GitHub.
</p>

## 📖 Descripción general

GitHub Framework es un framework de ingeniería con un enfoque definido (*opinionated*) para diseñar, construir y mantener repositorios profesionales en GitHub.

En lugar de tratar los repositorios como simples colecciones de archivos que evolucionan mediante decisiones aisladas, GitHub Framework aplica principios de ingeniería del software a su estructura, documentación y mantenimiento a largo plazo.

El Framework proporciona una base común mediante estándares, componentes reutilizables, plantillas de repositorio e implementaciones de referencia.

Su objetivo es reducir las decisiones repetitivas, permitiendo al mismo tiempo que cada proyecto conserve la flexibilidad necesaria para adaptarse a su propio dominio.

> Los repositorios son activos de software. Merecen ingeniería del software.

---

## ✨ Características

- Estándares de ingeniería para repositorios GitHub
- Repository Design System
- Componentes reutilizables para documentación
- Plantillas reutilizables de repositorios
- Componentes reutilizables de Workflow
- Contrato común de metadata para Components
- Framework Validator con reglas de validación deterministas
- Existing Repository Adoption Assessment, Application e Integration Cores
- Assisted Analysis Core para recopilar Evidence read-only con revisión humana
- Implementaciones de referencia y dogfooding
- Evolución versionada del Framework

---

## 🏗️ Arquitectura del Framework

```text
                    GitHub Framework
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   Standards         Components         Templates
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
              Reference Implementations
```

GitHub Framework se construye alrededor de un pequeño conjunto de bloques fundamentales de ingeniería.

Los **Standards** definen prácticas y convenciones comunes.

Los **Components** proporcionan bloques reutilizables para documentación y repositorios.

Las **Templates** ensamblan componentes para crear estructuras reutilizables de repositorios.

Las **Reference Implementations** validan el Framework mediante su utilización en proyectos reales.

Existing Repository Adoption complementa estos bloques con un mecanismo de revisión humana para reconciliar un repositorio existente con las Responsibilities de un Repository Template sin forzar artifacts canónicos ni modificar automáticamente el consumer.

Para una descripción arquitectónica completa, consulta la [documentación de arquitectura](docs/architecture/).

---

## 🚀 Primeros pasos

La mejor forma de comenzar es explorar la implementación oficial de referencia de GitHub Framework.

Recomendamos el siguiente recorrido:

1. Leer este README.
2. Explorar la documentación.
3. Descubrir los componentes reutilizables.
4. Revisar la arquitectura.
5. Consultar el roadmap del proyecto.

Si quieres utilizar el Framework, elige un punto de partida:

- **Repositorio nuevo:** consulta la [biblioteca de Repository Templates](framework/templates/repositories/README.md) y selecciona una composición adecuada para tu proyecto. Los Templates no son generadores automáticos de repositorios.
- **Repositorio existente:** sigue la [guía de Existing Repository Adoption](framework/adoption/README.md), elige un Repository Template de la [biblioteca](framework/templates/repositories/README.md), confirma su versión en el `metadata.yml` del Template y sigue el [recorrido del primer Assessment](framework/adoption/README.md#your-first-assessment-minimal-walkthrough) para comenzar con el [Assessment Template](framework/adoption/assessment-template.md).

---

## 🔗 Enlaces rápidos

- 📚 [Documentación](docs/)
- 🔄 [Existing Repository Adoption](framework/adoption/README.md)
- 🗺️ [Roadmap](ROADMAP.md)
- 🤝 [Guía de contribución](CONTRIBUTING.md)
- 📄 [Licencia](LICENSE)

---

## 📚 Documentación

La documentación del proyecto está organizada en áreas especializadas.

| Área | Descripción |
|------|-------------|
| [`architecture/`](docs/architecture/) | Arquitectura del Framework y decisiones de diseño. |
| [`standards/`](docs/standards/) | Estándares de ingeniería y convenciones. |
| [`design-system/`](docs/design-system/) | Repository Design System y catálogo de componentes. |
| [`implementation/`](docs/implementation/) | Implementaciones de referencia y guías de implementación. |
| [`governance/`](docs/governance/) | Gobierno del proyecto y documentación de planificación. |
| [`framework/adoption/`](framework/adoption/) | Existing Repository Adoption Assessment Core reutilizable. |

Para información detallada, explora el directorio `docs/` y los artifacts reutilizables bajo `framework/`.

---

## ✅ Validación del Framework

GitHub Framework incorpora un validador determinista para sus Components implementados.

El validador descubre los Components, carga sus archivos de metadata y comprueba el Common Core, la identidad, la unicidad, la madurez, las dependencias y las extensiones Workflow aplicables.

Para ejecutarlo desde la raíz del repositorio:

```bash
python -m scripts.framework_validator
```

El CLI genera un informe legible y devuelve el código de salida `0` cuando la validación es satisfactoria o `1` cuando se detectan errores de validación.

Para obtener una salida legible por herramientas:

```bash
python -m scripts.framework_validator --format json
```

Para guardar el informe JSON en un archivo UTF-8 (también si falla la validación):

```bash
python -m scripts.framework_validator --format json --output validation-report.json
```

Para validar otra biblioteca de Components del Framework, indica su directorio raíz (que contiene los directorios de las distintas familias):

```bash
python -m scripts.framework_validator --components-root ruta/al/framework/components
```

La opción también funciona con `--format json` y `--output`. El directorio indicado debe existir.

Para validar únicamente determinadas familias de Components, se puede repetir `--family`:

```bash
python -m scripts.framework_validator --family documentation --family workflow
```

Las familias disponibles son `readme`, `documentation` y `workflow`. Sin filtro se validan todas. Una ejecución filtrada comprueba únicamente los Components seleccionados, incluida la unicidad entre ellos; no equivale a una validación completa de la biblioteca. Los informes JSON incluyen `scope.families` (familias seleccionadas en orden canónico) y `scope.filtered` (`true` para validaciones parciales), de modo que CI puede distinguirlas de una comprobación completa.

La salida JSON incluye el estado de validación, el número de Components detectados, sus identificadores cargados, los errores globales y un array `components` con la ruta, el ID, el estado y los errores de cada Component. El objeto `summary` incorpora los recuentos de Components válidos, Components con errores y errores totales. Cada Component incluye también una ruta portable `relative_path` (por ejemplo, `documentation/architecture`) además de su `path` original. El alcance y los códigos de salida no cambian.

Para ejecutar la batería de tests automatizados:

```bash
python -m unittest discover -s tests/framework_validator -p "test_*.py"
```

La implementación de referencia de `v0.6.0` valida 21 Components e incluye 109 tests automatizados.

Para más información, consulta el [Component Metadata Standard](docs/standards/21_COMPONENT_METADATA_STANDARD.md) y la [Automation Reference Implementation](docs/implementation/22_AUTOMATION_REFERENCE_IMPLEMENTATION.md).

El validador comprueba reglas deterministas; no sustituye la revisión arquitectónica ni genera contenido para repositorios.

---

## 🔄 Existing Repository Adoption

GitHub Framework incorpora un **Existing Repository Adoption Assessment Core** reutilizable para evaluar un repositorio existente frente a las Responsibilities definidas por un Repository Template.

El proceso soportado es:

```text
ANALYZE
    ↓
ASSESS
    ↓
REVIEW
    ↓
DECIDE
    ↓
REPORT
```

El Assessment Core es:

```text
manual
human-readable
human-editable
human-reviewed
non-destructive
```

Permite reconocer implementaciones no canónicas, equivalentes y distribuidas, manteniendo explícitamente separadas la Evidence, la evaluación y las Adoption Decisions.

Los artifacts reutilizables son:

- [Adoption Guide](framework/adoption/README.md)
- [Assessment Template](framework/adoption/assessment-template.md)
- [Application Guide](framework/adoption/application/README.md)
- [Integration Guide](framework/adoption/integration/README.md)
- [Assisted Analysis Guide](framework/adoption/assisted-analysis/README.md)
- [Evidence Snapshot Template](framework/adoption/assisted-analysis/evidence-snapshot-template.md)

Esta capability no modifica los repositorios consumer ni introduce remediación automática o decisiones automáticas de adopción.

---

## 🗺️ Roadmap

GitHub Framework evoluciona mediante versiones incrementales.

Las versiones publicadas incluyen:

- **v0.2.0** — Preparación Open Source
- **v0.3.0** — Documentation Framework
- **v0.4.0** — Repository Templates
- **v0.5.0** — Workflow Framework
- **v0.6.0** — Framework Automation
- **v0.7.0** — Existing Repository Adoption Assessment Core
- **v0.8.0** — Existing Repository Adoption Application Core
- **v0.9.0** — Existing Repository Adoption Integration Core
- **v0.10.0** — Existing Repository Adoption Assisted Analysis Core
- **v1.0.0** — Versión estable

Para consultar el roadmap completo, visita [ROADMAP.md](ROADMAP.md).

---

## 🤝 Contribuir

Toda contribución, grande o pequeña, es bienvenida.

Antes de abrir un Issue o una Pull Request, consulta [CONTRIBUTING.md](CONTRIBUTING.md).

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT.

---

## ⭐ Estado del proyecto

GitHub Framework evoluciona mediante versiones incrementales.

La última release publicada es:

**v0.10.0 — Existing Repository Adoption Assisted Analysis Core**

Los Cores de Assessment, Application, Integration y Assisted Analysis están implementados, verificados, integrados y publicados. Assisted Analysis recopila Evidence delimitada y trazable a su fuente mediante un proceso read-only con revisión humana, sin automatizar decisiones de adopción ni modificar repositorios consumer.

El siguiente incremento del Framework todavía no está comprometido en una release.

---

> **Diseña una vez. Reutiliza en todas partes.**
