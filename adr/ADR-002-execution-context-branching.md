# ADR-002: Dual Execution Branches Resolved at Runtime

Status: Accepted
Date: 2026-09-03

## Context

The two dominant execution environments impose incompatible constraint
sets. Sandboxed artifact previews enforce a strict Content Security
Policy: no external scripts, stylesheets, fonts, or image loads; no
fetch, XHR, or WebSocket; one self-contained file; a size ceiling near
16 MiB. Agentic workspaces have none of these limits and can self-host
assets, pin and lazy-load libraries, and deploy to static hosts. A single
undifferentiated output either breaks in the sandbox or leaves the
workspace build needlessly constrained.

## Decision

Phase 5 carries two explicit branch elements, single_file_artifact and
multi_file_site, each with its own hard constraints and implementation
guidance. EXECUTION_CONTEXT defaults to auto, resolved by capability
probing at runtime, and the prompt must state its resolved choice and
reasoning in the build report. The single-file branch is the default
demo target because it is the hardest constraint set: a design that
survives strict CSP is trivially achievable as a multi-file site, and the
reverse is not true.

## Consequences

Positive: one prompt serves both environments without manual editing, and
the resolved-choice statement makes context resolution auditable.
Negative: branch constraints can drift toward each other during edits;
regression test test_regression_branch_constraints_not_swapped exists
because that drift silently breaks the CSP guarantee.

## Settling criteria

Settled unless a third execution class emerges with constraints neither
branch covers (for example a server-rendered environment), which would add
a branch and trigger a MAJOR version change.
