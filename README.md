# REPO-TO-EXPERIENCE

**A reusable BHIL master prompt that turns any GitHub repository into an
interactive visual experience.**

[![License: MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE)
[![Content: CC BY 4.0](https://img.shields.io/badge/content-CC%20BY%204.0-lightgrey.svg)](LICENSE-CONTENT)
[![Version](https://img.shields.io/badge/prompt-v1.0-1B4FD8.svg)](CHANGELOG.md)

Paste one prompt, point it at a repo, and get back a production-grade
interactive site: either a single self-contained HTML artifact (strict-CSP
safe) or a deployable multi-file static site, resolved automatically from
the executing environment.

## What it does

REPO-TO-EXPERIENCE drives any capable AI through five gated phases:

1. **Repo Exploration**: high-signal reading order (README, config,
   structure, core code, history), emitting an evidence-backed brief
2. **Asset Discovery**: full inventory of visual and content assets, with
   generated substitutes planned for anything unfetchable
3. **Design Style and Theme Analysis**: a concrete, justified design
   system in tokens (hex plus contrast ratios, type scale, motion
   language), anchored on real brand assets when they exist
4. **Experience Design**: information architecture with a required
   aha-moment interactive centerpiece that mirrors the repo's real function
5. **Site Generation**: the runnable experience, branched by execution
   context, closed by an eight-line acceptance scorecard

Every phase ends with a PASS/FAIL gate. Task-verification failures cause
21.30% of multi-agent breakdowns (MAST taxonomy, Cemri et al., NeurIPS
2025 Spotlight); this prompt makes verification structural.

## Quick start

1. Copy the fenced block from [`prompt/repo-to-experience.md`](prompt/repo-to-experience.md)
2. Fill `REPO_URL`. Leave the eight optional overrides blank to let the
   system infer them
3. Run it in Claude.ai (artifact output) or Claude Code (deployable site)
4. Read the build report and scorecard before publishing anything

Full guide: [docs/usage/quickstart.md](docs/usage/quickstart.md)

## Repository layout

```
prompt/       Canonical master prompt (single source of truth)
docs/         MkDocs Material documentation site
examples/     Worked example: BHIL-HELM-Sci-Fi-Visualizer (evidence-tiered)
tools/        Stdlib-only validator suite (10 laws, V1-V10)
tests/        Pytest conformance suite with named regression tests
adr/          Architecture decision records
launch/       Release collateral (descriptions, posts)
engagements/  Client working files (gitignored)
```

## Governance

- **Canonical source discipline.** `prompt/repo-to-experience.md` is the
  only editable source; docs describe it and CI fails on drift.
- **Evidence tiers.** VERIFIED / CORROBORATED / STATED / UNCORROBORATED /
  INFERENCE on every research claim and every worked-example claim.
- **Validator-first.** `python tools/validate_prompt.py` enforces
  placeholder integrity, phase gates, scorecard completeness, the em-dash
  sweep, and docs drift. Regression tests name the bug each prevents.
- **Acceptance scorecard.** "No fabricated repo facts" and "reduced-motion
  honored plus toggle present" are never waived.

## Verify locally

```
python tools/validate_prompt.py
python -m pytest tests/ -q
mkdocs build --strict
```

## License

Dual-licensed: [MIT](LICENSE) for code, schemas, validators, and CI;
[CC BY 4.0](LICENSE-CONTENT) for the prompt text, documentation, and
examples. Attribution format in LICENSE-CONTENT; citation metadata in
[CITATION.cff](CITATION.cff).

---

**Barry Hurd Intelligence Lab (BHIL)**
*Human-Directed. AI-Enabled. Commercially Tested.*
