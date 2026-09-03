# ADR-001: Phase-Gate Architecture with Structured Emissions

Status: Accepted
Date: 2026-09-03

## Context

Prompt systems that run comprehension, design, and generation in a single
undifferentiated pass exhibit the failure profile documented by the MAST
taxonomy (Cemri et al., NeurIPS 2025 Spotlight): task-verification
failures alone account for 21.30% of multi-agent breakdowns across 1,600+
annotated traces. Anthropic's prompting guidance independently recommends
XML-tagged sections, distinct phases, and giving the model a check it can
run. A repo-to-site transformation compounds the risk: hallucinated
features, defaulted aesthetics, and environment-incompatible output are
each downstream of a skipped verification step.

## Decision

The prompt is structured as five sequential phases, each of which must
emit a named, tagged structured output (repo_brief, asset_inventory,
design_system, experience_spec, then the artifact) and close with a
self_check element carrying gate="true" and an explicit PASS/FAIL verdict.
A FAIL blocks forward progress. The final phase closes with an eight-line
YES/NO scorecard, and remediation is capped at three fix passes, after
which the prompt ships the best safe version with an honest statement of
what failed.

## Consequences

Positive: every claim in the final experience is traceable to a phase
output, gates catch fabrication and infeasibility at the phase boundary
where they are cheapest to fix, and the build report gives the operator an
auditable verification trail. Negative: gated execution costs tokens and
produces longer transcripts; a model that ignores gate semantics degrades
to single-pass behavior, which is why the validator (V4-V6) enforces gate
presence in the canonical text and the scorecard doubles as an external
acceptance test.

## Settling criteria

This ADR is settled unless field runs show gates being systematically
skipped by target models, in which case gate phrasing moves from
declarative self-checks to forced-output schemas, a MAJOR version change.
