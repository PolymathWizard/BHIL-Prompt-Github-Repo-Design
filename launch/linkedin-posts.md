# LinkedIn Post Variants

## Variant 1 (technical authority)

Task-verification failures cause 21.30% of multi-agent AI breakdowns
(MAST taxonomy, NeurIPS 2025). That number shaped the newest BHIL
release.

REPO-TO-EXPERIENCE v1.0 is a master prompt that turns any GitHub
repository into an interactive visual experience. Five phases, each
closed by a PASS/FAIL gate: repo exploration in high-signal order,
asset discovery with substitute planning, a design system derived in
concrete tokens, experience design with a required interactive
centerpiece, and generation branched between a strict-CSP single-file
artifact and a deployable static site.

The rules that matter most are the ones that never bend: every repo
claim traces to a file actually read, and reduced-motion plus WCAG
contrast are acceptance gates, not suggestions. A stdlib validator
enforces ten laws in CI, including a docs-drift check against the
canonical prompt.

Repo, docs, worked example, and ADRs are public.

Human-Directed. AI-Enabled. Commercially Tested.

## Variant 2 (inquiry-driving)

What does your GitHub repo look like to someone with 60 seconds?

For most projects: a wall of markdown. The README says what it is.
Nothing shows what it feels like.

REPO-TO-EXPERIENCE is a single reusable prompt that fixes that. Point
it at a repo and it produces an interactive experience with a working
demo of the project's core function, a design system derived from the
repo's own signals, and a hard rule against inventing a single fact it
did not read.

It resolves its own execution environment: a self-contained HTML
artifact under strict CSP, or a deployable static site with a full
build tree. Same prompt, both outputs.

If your project deserves better than a README, the prompt is open
source. I would be interested to see what it builds from your repo.

Human-Directed. AI-Enabled. Commercially Tested.

## Variant 3 (peer/builder ship post)

Shipped: REPO-TO-EXPERIENCE v1.0.

One master prompt, five gated phases, two output branches. Feed it a
repo URL and it ships either a single-file HTML artifact that survives
a strict-CSP sandbox or a deployable multi-file static site, resolved
automatically.

Things I am glad I enforced in tooling rather than review: placeholder
integrity, gate presence, an eight-line scorecard, an em-dash sweep,
and a drift check that fails CI if the docs ever quote a placeholder
the canonical prompt no longer has. Every regression test in the suite
is named for the specific bug it prevents.

The worked example runs the prompt against a repo it could not fully
read, on purpose. Every unverifiable claim ships flagged as inference
with a promotion path to verified. Honest degradation over confident
fabrication, every time.

MIT for code, CC BY 4.0 for content. Links in comments.

Human-Directed. AI-Enabled. Commercially Tested.
