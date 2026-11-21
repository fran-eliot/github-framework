# Repository Generation Guided Experience — Maintainer First-Use Retest

Date: 2026-11-21  
Status: **Ready for maintainer execution — no new human observation recorded**  
Approved unit: **UX-D** (explicitly authorized after UX-C technical closure, conditional on successful integrated main CI).  
Baseline: `1d99eee80d42f05edc764ae567f565332e2210c7`  
CI: [44935345596](https://github.com/fran-eliot/github-framework/actions/runs/44935345596) — **success** on this exact commit, including Windows, Ubuntu and both parity jobs.  
Guide: [Repository Generation Guide](../../framework/generation/README.md)  
Prior evidence: [Original maintainer walkthrough](repository-generation-core-first-use.md) — usability concern, **not** acceptance.

## Purpose and evidence limitations

Assess whether the opt-in `guide` workflow is actually understandable and recoverable for a maintainer using a real terminal, with new user-authored project facts and a genuinely fresh destination. The operator's feedback is required: successful automated tests alone do **not** satisfy UXG-11 or GEN-15.

Do not record a passed human task, time measurement, satisfaction rating, full delivery acceptance or release readiness before the maintainer actually reports it. This is one maintainer session; it does not establish independent participant validation. It does not modify Only Film or another consumer. Use only fictitious or intentionally public facts.

## Starting conditions

1. Use a local checkout of `fran-eliot/github-framework`; ensure no uncommitted work would be lost. Record `git rev-parse HEAD` and `git status --short`. The commit may advance after this protocol PR merges: **record the actual tested SHA**, not the preparation baseline as though tested.
2. From the Framework root use a real **interactive** Windows PowerShell or Bash session. Record operating system, shell, Python interpreter version (`python --version`) and PyYAML version (`python -c "import yaml; print(yaml.__version__)"`). Target verified by CI: Python 3.11 / PyYAML 6.0.2. Testing another installed pair is a compatibility observation, not a support promise.
3. Run `python -B -m scripts.repository_generation --help`, then `python -B -m scripts.repository_generation guide`. Avoid supplying a scripted input stream or a real consumer project. Notice that `plan`/`generate` with JSON remain available separately.
4. Choose a pre-existing **external** output parent and a new portable child name. A safe example for a new *parent* on Windows is:
   
   ```powershell
   $parent = (New-Item -ItemType Directory -Path (Join-Path ([System.IO.Path]::GetTempPath()) ("guided-retest-" + [guid]::NewGuid().ToString("N")))).FullName
   $parent
   ```

   The command only creates a test parent, **not** a generator output child. Do not remove any existing project. If preparation fails, report it rather than deleting other files.

## Manual tasks (record outcomes, do not premark PASS)

| ID | Action | Evidence to record |
| --- | --- | --- |
| UXD-01 | Read help and enter `guide` | Does the purpose and the two-document/text-only boundary make sense? |
| UXD-02 | Enter **new, explicitly chosen** project facts, including a sufficiently long overview (80–1200 chars), a two-item Features list, a two-item Technologies list, and at least two Documentation entries | Were the descriptions useful? Did any prompt or limit surprise you? |
| UXD-03 | Enter Markdown containing an intentional blank line and a literal placeholder such as `{{ project_name }}`; finish Markdown with `:end`, lists with `done` | Was the input mechanism understandable? Did the literal/blank line survive? |
| UXD-04 | Review all fields; intentionally edit one field before continuing | Was the correction discoverable and does the full review reflect the edit? |
| UXD-05 | Select the existing external parent and a fresh child name. Examine the read-only plan; **before typing `yes`** verify the new child does not exist | Can you distinguish planned from written files, 8 selected/20 unselected, the named `VCL-HERO` gap and both intended hashes? |
| UXD-06 | At first confirmation, answer `no` or another non-`yes` value; inspect that child remains absent | Exit `3` expected; record actual exit and whether cancellation is clear |
| UXD-07 | Restart `guide` with the intended same facts but a fresh child, review plan, then type exact `yes` | Exit `0` expected; exactly two generated files and a verified success report |
| UXD-08 | Inspect the README Hero, Features, Documentation, and authored Markdown spacing; inspect CHANGELOG (Unreleased, only facts explicitly supplied) | Is the rendered output legible? Are author paragraph breaks preserved? |
| UXD-09 | Compare printed digests to local SHA-256 of each actual file; attempt to repeat the same destination without deleting it | Matching hashes and non-destructive rejection expected; report any confusion |
| UXD-10 | Assess errors and recovery: optionally try a second run with an already occupied child or an invalid name; **do not overwrite or delete** existing material | Did the message explain a safe next step? |
| UXD-11 | Report overall usability, help adequacy, confusing steps, needed changes and elapsed duration **only if actually timed** | Explicit maintainer judgement; no independent-user claim |

For `UXD-07`, a repeat of the previous `no` run can only succeed if the earlier run created nothing. If unsure, use another fresh name. Author a simple fictitious example rather than pasting all of the earlier Atlas fixture. The workflow is interactive and requires re-entering fields; input is deliberately not saved automatically.

### Suggested Windows inspection after successful generation

Only run these **after** a verified successful `yes` generation. Replace `new-docs` with the child name actually chosen:

```powershell
$child = Join-Path $parent "new-docs"
Test-Path -LiteralPath $child
Get-ChildItem -LiteralPath $child | Select-Object Name,Length
Get-Content -LiteralPath (Join-Path $child "README.md") -Raw
Get-Content -LiteralPath (Join-Path $child "CHANGELOG.md") -Raw
Get-FileHash -Algorithm SHA256 -LiteralPath (Join-Path $child "README.md"), (Join-Path $child "CHANGELOG.md")
```

After running the guide, immediately query `$LASTEXITCODE` to record the process exit value. Compare its full output to the actual command's stage; the `plan` shown inside the guide must not create a child.

## Evidence capture sheet

| Evidence field | Maintainer observation |
| --- | --- |
| Tested commit SHA and clean/dirty checkout state | **Not provided** |
| OS / shell / Python / PyYAML | **Not provided** |
| UXD-01–04 input and edit behavior | **Not observed** |
| UXD-05 pre-confirmation destination check | **Not observed** |
| UXD-06 cancellation result and exit | **Not observed** |
| UXD-07 successful generation and exit | **Not observed** |
| UXD-08 file content and readability | **Not observed** |
| UXD-09 digests and collision protection | **Not observed** |
| UXD-10 error messages and recovery understanding | **Not observed** |
| UXD-11 clarity, friction and overall judgement | **Not provided** |
| Duration | **Not measured / not provided** |

When observations are available, append a separate *observed results* record with verbatim-relevant transcript excerpts or measured facts; keep this protocol as the preparation baseline. If defects are identified, classify and reproduce them before any GEN-15 closure; corrective PRs need their own CI verification.

## Acceptance boundary

Human-run task completion, comprehension and a positive maintainer assessment are **required evidence** for the GEN-15/UXG-11 disposition. A successful session does not automatically authorize a release or prove universal usability.

Complete the [Acceptance Evidence Matrix](repository-generation-guided-ux-d-acceptance-matrix.md) against the actual retest and commit after these observations are supplied. The maintainer must separately approve GEN-15/GEN-16 delivery closure and any v0.13.0 release scope, exact tag target and GitHub Release. No release, tag, Sprint, milestone, Only Film or UX-02 execution is authorized by UX-D preparation.
