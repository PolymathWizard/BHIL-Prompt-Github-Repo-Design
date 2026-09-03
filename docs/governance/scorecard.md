# The Acceptance Scorecard

The Phase 5 scorecard is the acceptance test for every generated
experience. Eight YES/NO lines, three fix passes maximum, honest reporting
of anything that survives the cap.

| # | Check | Why it gates |
|---|---|---|
| 1 | Renders with zero console errors in target environment | A broken artifact is worse than no artifact |
| 2 | Purpose understandable in under 60s of scrolling | The mission statement, made testable |
| 3 | The aha-moment interactive element works | Without it the page is a brochure, not an experience |
| 4 | Responsive at 390px and 1440px with no overflow | The two verification widths, mobile-first |
| 5 | All text meets contrast; reduced-motion honored plus toggle present | WCAG floor plus motion safety |
| 6 | No fabricated repo facts; every claim traceable to a real file | The credibility line |
| 7 | Degrades gracefully with assets missing | No dead images, no broken interactions |
| 8 | (single_file) truly self-contained, no external requests | The CSP guarantee |

## Non-negotiable lines

Lines 5 and 6 are never waived. They protect the visitor's accessibility
and BHIL's credibility respectively. An experience failing either does not
ship, regardless of how the other six score.

## The three-pass cap

Unbounded fix loops are a known agentic failure mode. The cap forces a
decision: fix within three passes, or ship the best safe version with an
explicit statement of what failed and why. Honest partial delivery beats
silent degradation.
