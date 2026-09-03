# Changelog

All notable changes to REPO-TO-EXPERIENCE are documented here.
Format follows Keep a Changelog. Versioning follows semantic versioning
applied to the prompt system: MAJOR for phase-list or branch changes,
MINOR for new placeholders or gate additions, PATCH for copy fixes.

## [1.0.0] - 2026-09-03

### Added
- Canonical master prompt `prompt/repo-to-experience.md` with five gated
  phases (Repo Exploration, Asset Discovery, Design Style and Theme
  Analysis, Experience Design, Site Generation)
- Dual execution branches: single-file HTML artifact (strict-CSP sandbox)
  and deployable multi-file static site
- Eight-placeholder control surface with auto-inference defaults
- Phase-gate PASS/FAIL self-checks and final eight-line scorecard capped
  at three fix passes
- Worked example: BHIL-HELM-Sci-Fi-Visualizer (inference-flagged, evidence
  tiers applied)
- Validator suite: placeholder integrity, phase-gate presence, scorecard
  completeness, em-dash sweep
- MkDocs Material documentation site
- ADRs 001 through 004 covering gate design, execution branching, evidence
  posture, and design-derivation policy
