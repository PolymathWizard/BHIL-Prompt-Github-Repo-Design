# ADR-003: Evidence over Invention as Principle Zero

Status: Accepted
Date: 2026-09-03

## Context

The single most damaging failure for a repo showcase is a fabricated
claim: an invented feature, benchmark, star count, or quote discovered by
the repo's own maintainer or community. BHIL doctrine already requires
five-tier evidence classification on all intelligence products, and
rights or fact claims require a verified primary source before anything
ships. The prompt runs in environments where repo access can fail
partially or completely, which is precisely when fabrication pressure is
highest.

## Decision

Evidence over Invention is Operating Principle 1 and is enforced at three
layers: the Phase 1 gate requires every key feature to trace to a real
file actually read; the access_notes field mandates declaring what could
not be read and how it limits the build; and scorecard line 6 ("No
fabricated repo facts") is a never-waived acceptance line. When access
fails, the prompt degrades to explicitly flagged inference, as the HELM
worked example demonstrates end to end, including illustrative sample
data labeled as not official results.

## Consequences

Positive: degraded runs remain publishable as clearly labeled inference,
and the promotion path (re-run Phase 1 with real access, replace flags,
delete caveats) is mechanical. Negative: honest output is less impressive
than confident fabrication; the framework accepts that trade
categorically. A regression test protects the principle's position as
number one and the worked example's inference flags against cleanup
passes.

## Settling criteria

Settled permanently. This principle does not have a revision path; edits
that weaken it are rejected at review.
