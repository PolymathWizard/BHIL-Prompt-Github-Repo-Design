# Evidence Tiers

REPO-TO-EXPERIENCE inherits the BHIL five-tier evidence classification.
Every claim in research foundations, worked examples, and generated
experiences carries exactly one tag.

| Tier | Meaning | Publishing rule |
|---|---|---|
| VERIFIED | Confirmed against a primary source read directly | Publishable as fact |
| CORROBORATED | Supported by two or more independent secondary sources | Publishable with source note |
| STATED | A party's self-description, quarantined as such | Attribute, never adopt |
| UNCORROBORATED | Single secondary source, unconfirmed | Flag or omit |
| INFERENCE | Derived from evidence but not observed | Flag always, never publish as fact |

## How the prompt enforces this

Operating Principle 1 (Evidence over Invention) is the runtime form of
this table: every claim about the target repo must trace to a real file
actually read, unreadable material is declared in `access_notes`, and the
Phase 5 scorecard line "No fabricated repo facts" is a hard acceptance
gate. Maturity signals (stars, commits, releases) report "not observed"
rather than plausible guesses.

## Worked-example posture

The HELM worked example ships with INFERENCE flags intact as a deliberate
demonstration. A regression test
(`test_regression_worked_example_keeps_inference_flags`) fails the build
if a cleanup pass ever strips those tags, because silent promotion of
inference to fact is the exact failure this framework exists to prevent.
