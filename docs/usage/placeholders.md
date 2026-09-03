# The Control Surface

Nine inputs. One required, eight optional. Blank optional values are never
an error: the prompt infers them and states its inference.

## Required

| Placeholder | Purpose |
|---|---|
| `{{REPO_URL}}` | The target repository. Everything else derives from it. |

## Optional overrides

| Placeholder | Values | When to set it |
|---|---|---|
| `{{FORCED_THEME}}` | e.g. "sci-fi HUD", "clean data-forward", "brutalist", "editorial" | You want a specific aesthetic regardless of what the repo signals |
| `{{TARGET_AUDIENCE}}` | e.g. "ML researchers", "enterprise buyers", "OSS contributors" | The site must speak to a narrower audience than the repo's natural one |
| `{{TONE}}` | e.g. "authoritative", "playful", "cinematic", "minimal" | Copy voice must match a campaign or brand register |
| `{{EXECUTION_CONTEXT}}` | `single_file_artifact`, `multi_file_site`, `auto` | You know the target environment; otherwise `auto` resolves it |
| `{{PRIMARY_CTA}}` | e.g. "Star on GitHub", "Read the docs", "Try the demo" | The conversion goal differs from the inferred default |
| `{{BRAND_LOCK}}` | hex and font overrides | Brand tokens must be respected verbatim, no derivation |
| `{{DEPTH}}` | `landing`, `microsite`, `docs+showcase` | You need more than a single scrolling page |
| `{{ASSET_POLICY}}` | `fetch_ok`, `no_fetch`, `auto` | The environment forbids fetching, or you want substitutes forced |

## Interaction rules

- `BRAND_LOCK` beats `FORCED_THEME` beats inference. Locked tokens are
  anchored and extended, never replaced.
- `EXECUTION_CONTEXT=auto` resolves from capability: one-file sandbox
  environments get the artifact branch, workspace environments get the
  multi-file branch. The prompt must state its resolved choice.
- `ASSET_POLICY=no_fetch` forces the generated-substitutes path (inline
  SVG, CSS gradients, procedural canvas) so the build never breaks.
