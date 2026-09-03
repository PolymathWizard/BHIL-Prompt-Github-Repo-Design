# Worked Example: BHIL-HELM-Sci-Fi-Visualizer

The full worked example, with evidence tiers, access caveats, and all five
phase outputs, lives at
[`examples/worked-example-helm.md`](https://github.com/PolymathWizard/BHIL-REPO-TO-EXPERIENCE/blob/main/examples/worked-example-helm.md).

## What it demonstrates

This example intentionally exercises the prompt's hardest path: the target
repository's contents could not be directly retrieved, so the run operates
in graceful degradation. Three behaviors to notice:

1. **Access honesty.** The `access_notes` field declares exactly what
   could not be read and how that limits the build. Nothing unreadable is
   presented as fact.
2. **Evidence tiers on every claim.** Confirmed facts carry VERIFIED or
   CORROBORATED tags (the PolymathWizard account attribution, the Stanford
   HELM benchmark definition per Liang et al., arXiv:2211.09110).
   Everything derived from repo-name semantics carries INFERENCE.
3. **Substitute planning.** With zero fetchable assets, Phase 2 plans
   generated substitutes for every slot (inline SVG lockup, procedural
   starfield, illustrative sample data clearly labeled as not official
   HELM results), so Phase 5 still ships a working artifact.

## Promotion path

The example closes with the promotion path from INFERENCE to VERIFIED:
re-run Phase 1 with real repo access, replace flagged items with
evidence-backed facts, swap illustrative data for a real HELM export, then
delete the caveats. Only then do repo-specific claims publish as fact.
