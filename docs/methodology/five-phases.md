# The Five Phases

Each phase emits a structured, tagged output and closes with a PASS/FAIL
gate. A FAIL stops forward progress. This page describes what each gate
protects.

## Phase 1: Repo Exploration

Reads the repository in a strict priority order: README, manifest and
config files, directory structure, entry point plus 2-4 core modules,
data and example files, then changelog and commit history. The order is
research-backed: it mirrors how DeepWiki, gitingest, and code2prompt
flatten repositories for LLM comprehension, front-loading purpose and
architecture signal.

**Output:** `repo_brief` (one-liner, audience, functionality verbs,
architecture, evidence-backed features, narrative hook, access notes).

**Gate protects:** fabrication. Every key feature must trace to a real
file, and a stranger must be able to restate the project's purpose from
the brief alone.

## Phase 2: Asset Discovery

Inventories every visual and content asset: images, logos, SVGs, declared
colors and fonts, sample data, badges, existing brand marks. Each asset is
recorded as usable, degraded, or unusable.

**Output:** `asset_inventory` plus a generated-substitutes list.

**Gate protects:** broken builds. Every unusable or unfetchable asset must
have a concrete planned substitute before the build proceeds.

## Phase 3: Design Style and Theme Analysis

Derives a concrete design system from four inputs: domain, naming and
vocabulary, discovered assets, and tone. Existing brand tokens are
anchored and extended; absent tokens are inferred from domain psychology
under WCAG constraints. Output is tokens, not adjectives: hex values with
contrast ratios, type scales, easing curves, grid specs, and named mood
references.

**Gate protects:** accessibility and justification. All text pairs must
meet 4.5:1 (or carry noted exceptions) and the aesthetic must trace to
repo evidence or an explicit override.

## Phase 4: Experience Design

Designs the information architecture and interaction plan before any code.
The centerpiece requirement is the aha moment: at least one section must
let the visitor do something that mirrors the repo's actual function, not
merely read about it.

**Gate protects:** substance and feasibility. Every interactive element
must be feasible in the resolved execution context.

## Phase 5: Site Generation

Resolves the execution context, applies the matching branch constraints,
and generates the runnable experience. Universal requirements apply to
both branches: responsive at 390px and 1440px, keyboard operable, 4.5:1
contrast, reduced-motion honored plus an in-page toggle, transform and
opacity animation only, graceful degradation, meaningful content in raw
HTML.

**Gate protects:** shipping quality. The eight-line scorecard is the
acceptance test, capped at three fix passes. Failures that survive the cap
are reported honestly and the best safe version ships.
