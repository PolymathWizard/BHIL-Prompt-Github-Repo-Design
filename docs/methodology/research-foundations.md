# Research Foundations

Every design choice in REPO-TO-EXPERIENCE traces to a finding. Evidence
tiers per BHIL convention: VERIFIED, CORROBORATED, UNCORROBORATED,
INFERENCE, STATED.

## 1. Repo understanding has a consistent high-signal path

[CORROBORATED] DeepWiki (built by Cognition AI, powered by Claude)
analyzes codebases, READMEs, and configuration files to create structured
documentation plus interactive diagrams and dependency maps. gitingest and
code2prompt flatten a repo into a single LLM-ready digest with a source
tree. The convergent lesson: read README, then manifest and config, then
directory tree, then entry point plus core modules, then sample data, then
commit and release history, in that order, for maximum
purpose-and-architecture signal per token. Sources: Codersera DeepWiki
guide (2026); mufeedvh/code2prompt.

## 2. Phase gates and self-verification are not optional

[VERIFIED] Task-verification failures account for 21.30% of multi-agent
failures per the MAST taxonomy (Cemri et al., "Why Do Multi-Agent LLM
Systems Fail?", NeurIPS 2025 Spotlight), built from 1,600+ annotated
traces across 7 frameworks (kappa 0.88), clustering 14 failure modes into
system-design issues, inter-agent misalignment, and task verification.
[STATED] Anthropic's prompting guidance recommends XML-tagged sections,
distinct phases, and giving the model a check it can run. The prompt
therefore ends every phase with a PASS/FAIL gate and closes with an
evaluator-style scorecard capped at three fix passes. Caveat: the 21.30%
figure comes from a study of 7 agent frameworks; it motivates the gate
design but guarantees nothing about any single execution.

## 3. Winning dev-tool sites balance credibility and spectacle

[STATED] Anton Lovchikov, Head of Design at Evil Martians, analyzed 100+
dev-tool landing pages (July 2025) and found near-universal patterns: no
salesy copy, clever and simple wins, centered layouts with a max-width
container, and for solo-dev tools, big numbers (GitHub stars, usage
stats) in place of testimonials. [CORROBORATED] Award-tier sites (Stripe,
Linear, Vercel, Raycast) layer shader-based WebGL heroes, kinetic and
variable typography, scroll-driven storytelling, one signature hue
(one-color ownership), and embedded demos that create an instant aha
moment.

## 4. Sci-fi HUD/FUI has a codified visual grammar

[CORROBORATED] Cyan or electric-blue and phosphor-green on near-black;
condensed technical and monospace type (Eurostile and Microgramma
lineage); angular scan-frame brackets that frame content without enclosing
it; scan-line animation artifacts; asymmetric layered layouts, balanced
against real usability so the interface informs rather than overwhelms.

## 5. Execution context dictates hard technical limits

[CORROBORATED] Single-file HTML artifacts run under a strict Content
Security Policy: external scripts, stylesheets, fonts, and image loading
are blocked; fetch, XHR, and WebSocket are prohibited; publishable size is
at most 16 MiB; output must be one self-contained file. So charts must be
Canvas or SVG, data must be inlined, and images become data URIs or inline
SVG. Agentic multi-file tools have none of these limits. The prompt
branches precisely on this fork. Caveat: CSP limits vary by environment;
the no_fetch fallback keeps the prompt safe regardless.

## 6. Accessibility and performance are gating requirements

[VERIFIED] WCAG requires at least 4.5:1 contrast for normal text.
[CORROBORATED] Every animation must honor prefers-reduced-motion (ideally
plus an in-page toggle); animating width, height, top, or left harms CLS
and INP (use transform and opacity); and because most LLM and AI crawlers
do not execute JavaScript, meaningful content must exist in the raw HTML.
