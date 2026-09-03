# Execution Contexts

REPO-TO-EXPERIENCE is execution-agnostic by design. Phase 5 resolves the
context and applies exactly one branch's constraints.

## Resolution logic

`EXECUTION_CONTEXT=auto` resolves by capability probing: if the
environment can only emit one self-contained file or runs a sandboxed
artifact preview, the artifact branch is chosen. If the environment can
write multiple files to a workspace and run a build, the multi-file branch
is chosen. The prompt must state its resolved choice and why, so the
decision is auditable in the build report.

## Branch: single_file_artifact

Hard constraints (strict-CSP sandbox):

- One .html file; all CSS inline in style tags, all JS inline in script tags
- No external scripts, stylesheets, or CDN libraries
- No fetch, XHR, or WebSocket at runtime
- Images as data URIs or inline SVG
- Total rendered size well under the environment ceiling (about 16 MiB)

Implementation consequences: animations are hand-rolled with CSS and
requestAnimationFrame; charts and diagrams are inline SVG or Canvas 2D;
sample data is embedded as a JS object; unfetchable assets get inline SVG
or procedural substitutes. Meaningful content stays in the raw HTML so the
page reads without script execution.

## Branch: multi_file_site

A deployable static site: index.html plus routes if DEPTH exceeds landing,
self-hosted assets, styles, scripts, and a README with run and deploy
instructions. External libraries (GSAP, three.js, a syntax highlighter)
are permitted with pinned versions and lazy loading for heavy ones. Assets
are optimized (compressed images, subset fonts) and a deploy note targets
a static host.

## Why build to the artifact first

The single-file branch is the hardest constraint set to satisfy and the
most portable proof. A design that survives strict CSP is trivially
achievable as a multi-file site; the reverse is not true. Default demos
ship as artifacts for this reason.
