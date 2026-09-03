# ADR-004: Design Derived from Repo Signals, Anchored on Real Brand Assets

Status: Accepted
Date: 2026-09-03

## Context

Generic template aesthetics are the second most common failure of
automated site generation after fabrication. Research on 100+ dev-tool
landing pages (Lovchikov, Evil Martians, 2025) shows the winning pattern
is credibility plus one distinctive move: a signature hue (one-color
ownership), a justified motion language, and an embedded demo, not a
theme picked at random. Some target repos carry real brand assets
(declared colors, fonts, logos); most carry only domain signals.

## Decision

Phase 3 derives the design system from four inputs (domain, naming,
discovered assets, tone) and emits concrete tokens, never adjectives:
hex values with contrast ratios, type scales with fallbacks, easing
curves with durations, grid specs, and named mood references, plus a
rationale tying the system to repo evidence. When Phase 2 finds at least
one declared brand color and a logo, the system ANCHORS on the real
tokens and extends them; otherwise it infers from domain psychology under
WCAG constraints. FORCED_THEME and BRAND_LOCK override inference, with
BRAND_LOCK strongest: locked tokens are respected verbatim.

## Consequences

Positive: every aesthetic choice is auditable back to evidence or an
explicit override, and anchored builds preserve existing brand equity
instead of replacing it. Negative: the anchor threshold (one color plus
a logo) is a heuristic; repos with partial or conflicting brand signals
require operator judgment via BRAND_LOCK.

## Settling criteria

Settled unless field runs show the anchor threshold misfiring in more
than isolated cases, in which case the threshold moves into the control
surface as an explicit placeholder, a MINOR version change.
