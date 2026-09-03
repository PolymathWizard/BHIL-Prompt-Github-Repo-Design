# Contributing to REPO-TO-EXPERIENCE

REPO-TO-EXPERIENCE is a versioned BHIL intelligence asset. Contributions
are welcome within the governance rules below.

## Canonical source discipline

The single source of truth is `prompt/repo-to-experience.md`. Documentation
pages describe the prompt; they never fork it. If a change alters prompt
behavior, edit the canonical file first, then update docs to match. CI
fails any pull request where the docs quote a placeholder or gate that no
longer exists in the canonical prompt.

## Ground rules

1. Evidence over invention. Any claim added to the research foundations
   must carry an evidence tier tag (VERIFIED, CORROBORATED, UNCORROBORATED,
   INFERENCE, STATED) and a source.
2. No em dashes in derived prose. Use commas or parentheses. CI enforces
   this with a grep sweep.
3. Every significant design decision gets an ADR in `adr/` with settling
   criteria. Do not paper over decisions in commit messages.
4. Version bumps follow the policy in CHANGELOG.md. A change to the phase
   list, the scorecard, or the execution branches is MAJOR.

## Workflow

1. Fork, branch from `main`, use conventional commits scoped to the
   framework: `feat(rte): ...`, `fix(rte): ...`, `docs(rte): ...`
2. Run the validators locally before pushing:

   ```
   python tools/validate_prompt.py
   python -m pytest tests/ -q
   mkdocs build --strict
   ```

3. Open a pull request. The quality gate must pass before review.

## What gets accepted

- Fixes to gate logic, placeholder handling, or branch constraints backed
  by an observed failure (add it as a regression test)
- New deployment recipes for additional execution environments
- Worked examples that ran the prompt against a real, accessible repo with
  evidence-backed Phase 1 output

## What gets declined

- Aesthetic rewrites of the canonical prompt without behavioral rationale
- Claims without sources or evidence tiers
- Docs-only changes that drift from the canonical prompt
