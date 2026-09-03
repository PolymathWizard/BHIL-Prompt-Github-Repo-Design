# REPO-TO-EXPERIENCE

**A reusable BHIL master prompt for turning any GitHub repository into an
interactive visual experience.**

REPO-TO-EXPERIENCE v1.0 drives any capable AI through five gated phases,
Repo Exploration, Asset Discovery, Design Style and Theme Analysis,
Experience Design, and Site Generation, and branches its final output
between a single-file HTML artifact (strict-CSP sandbox) and a deployable
multi-file static site.

## Why it exists

Most "make my repo a website" prompts fail in one of three ways: they
hallucinate features the repo doesn't have, they default to a generic
template aesthetic, or they produce output that breaks in the target
environment. REPO-TO-EXPERIENCE is engineered against all three:

1. **High-signal repo comprehension.** The exploration order (README, then
   manifest and config, then structure, then core code, then history)
   mirrors how DeepWiki, gitingest, and code2prompt read repositories,
   maximizing purpose-and-architecture signal per token.
2. **Phase gates and self-verification.** Every phase ends with a PASS/FAIL
   gate and the build closes with an eight-line scorecard capped at three
   fix passes. Task-verification failures account for 21.30% of multi-agent
   breakdowns per the MAST taxonomy (Cemri et al., NeurIPS 2025 Spotlight),
   so verification is structural, not optional.
3. **Execution-aware output.** The prompt resolves its own execution
   context and applies the correct hard constraints: strict CSP, inline
   everything, and a 16 MiB ceiling for artifacts; pinned, lazy-loaded
   libraries and deploy notes for multi-file sites.

## Start here

- [Quickstart](usage/quickstart.md): fill the placeholders and run
- [The control surface](usage/placeholders.md): all nine inputs explained
- [The five phases](methodology/five-phases.md): what each gate enforces
- [Worked example](example/helm-worked-example.md): the prompt run against
  a real repo with degraded access, evidence tiers intact

## The canonical prompt

The single source of truth lives at
[`prompt/repo-to-experience.md`](https://github.com/PolymathWizard/BHIL-REPO-TO-EXPERIENCE/blob/main/prompt/repo-to-experience.md).
These docs describe it; they never fork it.

*Human-Directed. AI-Enabled. Commercially Tested.*
