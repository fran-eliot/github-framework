# Repository Template Composition Preview

The read-only preview joins a canonical Repository Template's ordered Component references with the Component Catalog classification and physical metadata evidence. It is separate from the Framework Validator and does not assess a consumer repository.

## Run from a Framework checkout

Python 3.11 and PyYAML 6.0.2 are required.

```bash
python -m pip install PyYAML==6.0.2
python -B -m scripts.template_composition_preview TPL-BACKEND
python -B -m scripts.template_composition_preview TPL-FULLSTACK
python -B -m scripts.template_composition_preview TPL-DOCUMENTATION
```

Use `--help` for the command's arguments. Exactly one case-sensitive canonical Template ID is accepted. Source paths are resolved from the module's checkout. The optional Python interpreter flag `-B` prevents bytecode cache writes.

## Read the report

The text report gives the Template identity and version, source locations, and the required, recommended and optional references in declared order. Each reference includes its registry classification, outcome, reason and available metadata paths, versions and statuses. Counts include all five outcomes, even when zero. Multiple matches are listed without selecting a winner.

| Outcome | Meaning |
| --- | --- |
| Resolved | Implemented registry entry and one physical metadata match |
| Conceptual | Explicit Conceptual entry and no physical match |
| Unknown | No registry entry and no physical match |
| Inconsistent | Registry and physical evidence disagree |
| Ambiguous | Multiple physical metadata matches |

A required Conceptual reference is not a failure by itself. For example, the Documentation Template declares README-LICENSE as required and its registry classification is Conceptual at the delivery baseline.

| Exit code | Meaning |
| --- | --- |
| 0 | Complete preview with only Resolved or Conceptual outcomes |
| 1 | Complete preview containing Unknown, Inconsistent or Ambiguous references |
| 2 | Invalid arguments or source error; diagnostics on stderr, no partial preview |

## Boundaries

The adapter reads four specific Markdown registry sections and the three supported physical Component families. Unsupported structures and unreliable source reads fail explicitly. Structural checks cannot prove registry completeness: a syntactically valid deleted row may not be detectable. Reads are not atomic snapshots. Resolved does not certify valid materialization, successful Validator execution or consumer conformance.

The command does not generate files, accept consumer paths, export JSON, retrieve network resources or alter the Validator interface. Python may create normal bytecode caches unless run with `-B`. No consumer is inspected or modified.

The full acceptance evidence and cross-platform delivery closeout are tracked separately in the approved [Delivery Scope](repository-template-composition-preview-delivery-scope.md) and [Implementation Plan](repository-template-composition-preview-implementation-plan.md).
