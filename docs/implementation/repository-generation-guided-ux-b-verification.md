# Repository Generation Guided Experience — UX-B Verification

Date: 2026-11-21  
Status: **UX-B implementation integrated; automated verification passed — maintainer unit acceptance pending**  
Integrated main baseline: `eaa3fbeffef4c2b452efc8cccf024aa25c2c6da4`  
CI: [44932448813](https://github.com/fran-eliot/github-framework/actions/runs/44932448813) — **success**, all four jobs completed.  
Implementation: [PR #427](https://github.com/fran-eliot/github-framework/pull/427) (UX-B1) and [PR #428](https://github.com/fran-eliot/github-framework/pull/428) (UX-B2), both merged.  
PR #428 head CI: [44930291463](https://github.com/fran-eliot/github-framework/actions/runs/44930291463) — success.

## Authorization and boundaries

The maintainer approved UXG-01–UXG-12 and the Guided Experience Implementation Plan, explicitly authorized UX-A, later approved its technical closure and authorized **UX-B**. This document evaluates the integrated UX-B code; it is not an independent UX study or final acceptance of GEN-15.

UX-B does not change canonical Components, template selection, generated Markdown whitespace, the original noninteractive `plan`/`generate` behavior, or publication. UX-C / UX-D, GEN-15 and GEN-16 remain pending. v0.13.0 is a conditional candidate only; published version remains v0.12.0.

## UX-B implementation evidence

- `guided.py`: bounded collection of ten required and three optional project fields, plain-language descriptions, explicit optional category choices, ordered lists terminated with `done`, Markdown with `:end` and escaped literal `::end`, full JSON review, edit/cancel and reuse of `parse_project_input` for contract validation.
- `cli.py`: opt-in terminal-only `guide` command. Non-TTY stdin/stdout is rejected promptly; the former `plan`/`generate` invocations are unchanged. Guided preflight uses existing `require_profile`, `load_composition`, `assemble`, `validate_destination`, `summary_report` and `write_documents`.
- **No destination is created by data entry, review or the plan**. Only the exact `yes` confirmation allows generation; required composition/rendering/destination checks repeat immediately before the writer. The exclusive writer rejects existing children.
- `guide` outcomes: 0 for generated and verified output, 1 destination/write error, 2 input/source/noninteractive/EOF error, 3 explicit cancellation or interrupt. There is no automatic draft persistence or cleanup of potentially incomplete output.
- `framework/generation/README.md`: interactive entry command, field syntax, preview, confirmation, output inspection, cancellation and error recovery. The guide remains English-language technical documentation.

## Observed automated checks

| Gate | Actual evidence | Assessment |
| --- | --- | --- |
| UXG-01 | Existing CLI tests continue in the successful main CI; guided mode is opt-in | Technical PASS within tested scope |
| UXG-02 | `test_help_and_noninteractive_rejection`, `test_no_and_empty_confirmation_never_write`, `test_eof_or_interrupt_before_write` | Technical PASS for tested non-TTY, cancellation and EOF paths |
| UXG-03 | `test_complete_draft_matches_original_parser`, `test_optional_categories_are_explicit`, `test_invalid_schema_is_not_coerced` | Technical PASS for tested field contracts |
| UXG-04 | `test_markdown_terminator_escape_and_spaces`, `test_edit_invalid_field_then_continue`, list and category tests | Technical PASS for tested Markdown and edit cases |
| UXG-05 | `test_no_and_empty_confirmation_never_write` and `test_generation_uses_canonical_two_file_output` | Technical PASS for tested preconfirmation/confirmation cases |
| UXG-06 | `run_guided` directly uses established canonical inputs, resolver, assembly and safe writer, without a parallel generator | Source reviewed; integrated tests PASS |
| UXG-07 | Guided plan uses UX-A `summary_report` and tests assert VCL-HERO and actual digest values | Technical PASS for tested summary |
| UXG-08 | Existing destination preservation, invalid path, validation error and collision tests; incomplete-output error policy inherited from writer | Partial — no new independent guided injected partial-write fault test |
| UXG-09 | Integrated run 44932448813 success: Ubuntu/Windows Component validation, Component catalog parity, generated-document byte parity | Technical PASS for executed matrix |
| UXG-10 | Renderer untouched by UX-B; whitespace defect observed in prior walkthrough remains for UX-C | Pending UX-C |
| UXG-11 | No fresh maintainer-run guided walkthrough yet | Pending UX-D |
| UXG-12 | Final UXG and GEN evidence reconciliation not yet performed | Pending UX-D |

The tests rely on mocked input/output for scripted interactive paths and an actual subprocess for non-TTY rejection. This does not prove terminal UX quality under a human session; it does demonstrate the tested safety paths. The reader must not infer independent usability, telemetry, support for other Templates, or full Template conformance.

## Post-integration readiness

Current UX-B result is **implemented and automated-verification complete**, subject to maintainer review and explicit closure. UX-C is not authorized by this verification document or its merge. UX-C should address only known renderer-introduced blank lines with exact cross-platform byte-parity checks and preservation of author text. UX-D will require a fresh maintainer walkthrough with real feedback before GEN-15 may be accepted.

No release, tag, Sprint, milestone, Only Film modification or UX-02 execution is authorized.
