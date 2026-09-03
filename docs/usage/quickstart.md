# Quickstart

## 1. Copy the canonical prompt

Copy the full fenced block from `prompt/repo-to-experience.md`. Do not edit
inside the block except to fill placeholders.

## 2. Fill the control surface

Only one input is required:

```
REPO_URL: https://github.com/your-org/your-repo
```

Leave every optional override blank to let the system infer theme,
audience, tone, and depth from the repository itself. Set overrides only
when you have a hard requirement (for instance a brand lockup that must be
respected verbatim goes in BRAND_LOCK).

## 3. Choose where to run it

| Environment | Resolved branch | What you get |
|---|---|---|
| Claude.ai chat (artifact) | `single_file_artifact` | One self-contained HTML file, no external requests, renders in the sandbox |
| Claude Code / agentic workspace | `multi_file_site` | Deployable static site tree with run and deploy README |
| Anything else | `auto` resolves it | The prompt states its resolved choice and why |

## 4. Read the build report first

The output opens with a build report: resolved execution context, inferred
theme, and the Phase 5 scorecard. If any scorecard line is NO after three
fix passes, the prompt ships the best safe version and tells you exactly
what failed. Treat "No fabricated repo facts" and "reduced-motion honored
plus toggle present" as non-negotiable acceptance lines.

## 5. Verify before publishing

If the executing AI could not read the repo directly, every repo-specific
claim will be flagged as inference in `access_notes`. Re-run Phase 1 with
real repo access and promote flags to evidence before publishing anything
as fact.
