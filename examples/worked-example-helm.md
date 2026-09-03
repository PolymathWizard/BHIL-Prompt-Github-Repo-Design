# Worked Example: PolymathWizard/BHIL-HELM-Sci-Fi-Visualizer

This example runs REPO-TO-EXPERIENCE v1.0 against a real BHIL repository and
demonstrates the prompt's graceful-degradation path when repo contents cannot
be directly read. Every claim below carries an evidence tier.

## Access caveat (Operating Principle 1 in effect)

During research the repository's contents could not be directly retrieved:
direct fetches of the repo page, the raw README, DeepWiki, and the inferred
Netlify explainer were not accessible, and the repo's README and code were
not present in any search index.

What is confirmed:

1. [CORROBORATED] `PolymathWizard` is Barry Hurd's / BHIL's GitHub account,
   corroborated by a public build-tracker gist listing sibling
   `PolymathWizard/*` repos (BHIL-Executive-Photoshoot, BHIL-Colophon-Spec,
   AgentTeam-Tournament), each run through an "explainmyrepo" generator
   producing Netlify explainer sites.
2. [VERIFIED] "HELM" maps to Stanford CRFM's Holistic Evaluation of Language
   Models benchmark. Per Liang et al. (arXiv:2211.09110), HELM measures 7
   metrics (accuracy, calibration, robustness, fairness, bias, toxicity,
   efficiency) across 16 core scenarios (of 42 total) on 30 prominent
   language models, and describes itself as a living benchmark, continuously
   updated. It is an open-source Python framework
   (github.com/stanford-crfm/helm) with a public Web leaderboard.

Everything below is therefore constructed from repo-name semantics, BHIL
context, and HELM domain knowledge, exactly as the prompt's degradation path
requires. The `access_notes` field flags every inference. Replace inference
items with evidence-backed facts by re-running Phase 1 with real repo access
before publishing anything as fact.

## Phase 1 output: repo_brief

- **one_liner:** A sci-fi HUD that turns Stanford HELM LLM-benchmark data
  into a living command console. [INFERENCE]
- **what_it_is:** An interactive visualizer that reframes HELM leaderboard
  scores as a cinematic "ship's console" for exploring and comparing
  foundation models, a BHIL intelligence-IP demonstrator. [INFERENCE]
- **who_its_for:** ML researchers, AI buyers and executives, and BHIL's
  audience of intelligence-ops practitioners. [INFERENCE]
- **core_functionality:** load and parse HELM-style scenario-by-model score
  matrices; rank and compare models; drill into per-scenario metrics; render
  multi-metric radar/HUD readouts; toggle scenarios and aspects. [INFERENCE]
- **architecture:** data layer (HELM JSON/CSV), transform/normalize layer
  (mean-win-rate style aggregation), visualization layer (HUD widgets),
  interaction/state controller. [INFERENCE]
- **key_features:** model-vs-model comparison; scenario filtering; animated
  metric dials; leaderboard table with sci-fi styling. [INFERENCE, evidence
  unavailable, treat as hypotheses]
- **tech_stack:** not observed. Plausible for the domain: JS/TS front end,
  possibly Three.js/WebGL or Canvas/SVG for HUD effects. [UNCORROBORATED]
- **narrative_hook:** "Benchmark data, rendered like the bridge of a
  starship. Evaluate the models, holistically." [INFERENCE]
- **maturity_signals:** not observed.
- **access_notes:** README, file tree, languages, license, stars, commit
  history all UNVERIFIED. All feature claims are inferences from name plus
  HELM domain; confirm against the live repo before publishing as fact.

## Phase 2 output: asset_inventory

Because assets could not be fetched (ASSET_POLICY resolved auto to
no_fetch fallback), the plan leans on generated substitutes:

| Substitute | Type | Planned use |
|---|---|---|
| Inline SVG logo lockup "BHIL // HELM" | generated | hero identity mark |
| Procedural starfield and scanline canvas | generated | hero background |
| CSS-gradient hero fallback | generated | reduced-motion variant |
| SVG radar and dial widgets | generated | the Console centerpiece |
| Inline sample HELM-style score matrix | generated | drives all charts, labeled "illustrative sample data, not official HELM results" |
| Static SVG badge placeholders | generated | license/stars until real values confirmed |

Gate check: every unfetchable asset has a concrete substitute. PASS.

## Phase 3 output: design_system (Sci-Fi HUD / FUI)

- **palette:** background `#05070D` (near-black); surface `#0B111F`; text
  `#E6F1FF` (approx 15:1 on bg); muted `#7FA8C9`; signature hue electric
  cyan `#00F5FF` (one-color ownership); secondary phosphor-green `#00FF9C`;
  accent amber `#FFB020` (alerts); error `#FF4D6D`. Text/background pairs
  target at least 4.5:1.
- **typography:** display, condensed technical/geometric face (Eurostile /
  Michroma / Orbitron lineage), all-caps, wide tracking; body, clean grotesk
  (Inter / IBM Plex Sans); mono, IBM Plex Mono / JetBrains Mono for data
  readouts; 1.25 type scale; self-host or system fallbacks.
- **motion_language:** `cubic-bezier(0.16,1,0.3,1)` power easing; 200-600ms;
  signature transitions are a boot-up scanline sweep, dial-needle settle,
  and data type-in; scroll uses section-pinned reveals. Reduced-motion
  variant: cross-fades only, no sweeps or parallax.
- **layout_grid:** 12-column, max-width 1280px, 8px spacing scale,
  breakpoints 390/768/1280; asymmetric layered panels with angular corner
  brackets that frame without enclosing.
- **iconography:** thin-line duotone, inline SVG, targeting-bracket motifs.
- **mood_references:** Minority Report FUI, Iron Man JARVIS HUD, Alien:
  Isolation MU-TH-UR terminals, the Stanford HELM leaderboard (the real
  content being dramatized), Eurostile-era NASA panels.
- **rationale:** The repo name literally specifies "Sci-Fi Visualizer";
  HELM's multi-metric nature maps naturally to a multi-dial HUD, and
  cyan-on-black FUI is the genre-correct shorthand for high-tech, complex,
  powerful.

Gate check: contrast targets stated per pair; aesthetic justified by repo
naming evidence. PASS.

## Phase 4 output: experience_spec

- **sitemap (DEPTH=landing, single scroll):** (1) Boot-up hero, (2) "What is
  HELM?" scrollytelling primer, (3) The Console (aha moment), (4)
  Architecture flow, (5) About BHIL plus CTA.
- **the_aha_moment:** The Console, an interactive HUD where the visitor
  selects two models and a scenario and watches animated dials and radar
  compare their HELM-style metrics (accuracy, calibration, robustness,
  fairness, bias, toxicity, efficiency), driven by clearly labeled
  illustrative sample data, swappable for a real HELM JSON export in the
  multi-file build.
- **per_section highlights:** hero uses a canvas starfield plus scanline
  sweep plus kinetic headline ("HOLISTIC EVALUATION // RENDERED"); primer
  uses scroll-pinned reveals explaining accuracy vs robustness vs fairness;
  architecture section animates data to transform to HUD flow.
- **copy_deck (TONE = cinematic-authoritative):** Hero H1 "EVALUATE THE
  MODELS. HOLISTICALLY." Subhead "Stanford HELM benchmark data, rendered
  like a starship console. A BHIL intelligence demonstrator."

Gate check: the Console lets the visitor do what the repo does (compare
models on HELM metrics); all elements feasible in both branches. PASS.

## Phase 5: generation choice

- **Resolved context:** if run as a Claude artifact, single_file_artifact
  (inline everything, Canvas/SVG HUD, embedded sample data, no external
  requests, reduced-motion toggle in the top HUD bar). If run in Claude
  Code, multi_file_site: /index.html, /assets, /styles, /scripts, a
  data/helm-sample.json replaceable with a real HELM export, optional
  Three.js/GSAP pinned and lazy-loaded, deploy note targeting a static host
  (matching the sibling repos' Netlify pattern).

### Scorecard (illustrative)

| Check | Verdict |
|---|---|
| Renders with zero console errors | YES |
| Purpose clear in under 60s | YES |
| Console interaction works | YES |
| Responsive at 390 and 1440 | YES |
| Contrast plus reduced-motion honored | YES |
| No fabricated repo facts (all scores labeled illustrative) | YES |
| Graceful degradation | YES |
| Self-contained (artifact branch) | YES |

## Promotion path from INFERENCE to VERIFIED

1. Run Phase 1 against the actual repo via Claude Code with repo access, or
   a gitingest/DeepWiki digest.
2. Replace every flagged item with evidence-backed facts.
3. Swap illustrative data for a real HELM export.
4. Delete the access caveats. Only then publish repo-specific claims as fact.
