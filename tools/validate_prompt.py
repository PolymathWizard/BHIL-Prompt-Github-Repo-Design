#!/usr/bin/env python3
"""REPO-TO-EXPERIENCE validator suite.

Stdlib-only. Enforces the framework's laws against the canonical prompt and
all derived prose. Exit code 0 on PASS, 1 on any FAIL.

Laws enforced:
  V1  Canonical file exists and declares version 1.0
  V2  Required placeholder REPO_URL present exactly once in <required>
  V3  All eight optional placeholders present in <optional_overrides>
  V4  Exactly five phases, numbered 1-5, in order
  V5  Every phase closes with a self_check gate="true"
  V6  Final scorecard contains all eight check lines
  V7  Both execution branches present (single_file_artifact, multi_file_site)
  V8  Six operating principles present
  V9  Em-dash sweep: no em dashes in any tracked .md file
  V10 Docs drift: any {{PLACEHOLDER}} referenced in docs/ exists in canonical
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = ROOT / "prompt" / "repo-to-experience.md"

OPTIONAL_PLACEHOLDERS = [
    "FORCED_THEME",
    "TARGET_AUDIENCE",
    "TONE",
    "EXECUTION_CONTEXT",
    "PRIMARY_CTA",
    "BRAND_LOCK",
    "DEPTH",
    "ASSET_POLICY",
]

PHASE_NAMES = [
    "REPO_EXPLORATION",
    "ASSET_DISCOVERY",
    "DESIGN_STYLE_AND_THEME_ANALYSIS",
    "EXPERIENCE_DESIGN",
    "SITE_GENERATION",
]

SCORECARD_FRAGMENTS = [
    "zero console errors",
    "<60s of scrolling",
    "aha moment",
    "390px and 1440px",
    "reduced-motion honored",
    "No fabricated repo facts",
    "Degrades gracefully",
    "self-contained",
]

failures: list[str] = []


def check(law: str, ok: bool, detail: str) -> None:
    status = "PASS" if ok else "FAIL"
    print(f"  [{status}] {law}: {detail}")
    if not ok:
        failures.append(f"{law}: {detail}")


def main() -> int:
    print("REPO-TO-EXPERIENCE validator suite")
    print(f"root: {ROOT}\n")

    # V1
    exists = CANONICAL.exists()
    check("V1", exists, "canonical prompt file exists")
    if not exists:
        print("\nFATAL: cannot continue without canonical file")
        return 1
    text = CANONICAL.read_text(encoding="utf-8")
    check("V1", 'version="1.0"' in text, "canonical declares version 1.0")

    # V2
    required_block = re.search(r"<required>(.*?)</required>", text, re.S)
    ok = bool(required_block) and required_block.group(1).count("{{REPO_URL}}") == 1
    check("V2", ok, "REPO_URL placeholder present exactly once in <required>")

    # V3
    opt_block = re.search(
        r"<optional_overrides.*?>(.*?)</optional_overrides>", text, re.S
    )
    opt_text = opt_block.group(1) if opt_block else ""
    for name in OPTIONAL_PLACEHOLDERS:
        check("V3", f"{{{{{name}}}}}" in opt_text, f"optional placeholder {name}")

    # V4
    phases = re.findall(r'<phase number="(\d)" name="([A-Z_]+)">', text)
    numbers = [int(n) for n, _ in phases]
    names = [nm for _, nm in phases]
    check("V4", numbers == [1, 2, 3, 4, 5], f"phases numbered {numbers}")
    check("V4", names == PHASE_NAMES, "phase names match canonical order")

    # V5
    phase_blocks = re.findall(r"<phase number=.*?</phase>", text, re.S)
    gated = sum(1 for b in phase_blocks if 'self_check gate="true"' in b)
    check("V5", gated == 5, f"{gated}/5 phases carry a gated self_check")

    # V6
    final_check = re.findall(r'<self_check gate="true">(.*?)</self_check>', text, re.S)
    scorecard = final_check[-1] if final_check else ""
    for frag in SCORECARD_FRAGMENTS:
        check("V6", frag in scorecard, f"scorecard line: {frag!r}")

    # V7
    for branch in ("single_file_artifact", "multi_file_site"):
        check("V7", f'<branch context="{branch}">' in text, f"branch {branch}")

    # V8
    principles = re.search(
        r"<operating_principles>(.*?)</operating_principles>", text, re.S
    )
    count = len(re.findall(r"^\s+\d\.", principles.group(1), re.M)) if principles else 0
    check("V8", count == 6, f"{count}/6 operating principles")

    # V9: em-dash sweep across all tracked markdown
    emdash_hits = []
    for md in sorted(ROOT.rglob("*.md")):
        if "site" in md.parts or ".git" in md.parts or "engagements" in md.parts:
            continue
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if "\u2014" in line:
                emdash_hits.append(f"{md.relative_to(ROOT)}:{i}")
    check(
        "V9",
        not emdash_hits,
        "no em dashes in prose" if not emdash_hits else f"em dashes at {emdash_hits[:5]}",
    )

    # V10: docs drift, placeholders referenced in docs must exist in canonical
    canonical_placeholders = set(re.findall(r"\{\{([A-Z_]+)\}\}", text))
    drift = []
    docs_dir = ROOT / "docs"
    if docs_dir.exists():
        for md in sorted(docs_dir.rglob("*.md")):
            for name in set(re.findall(r"\{\{([A-Z_]+)\}\}", md.read_text("utf-8"))):
                if name not in canonical_placeholders:
                    drift.append(f"{md.relative_to(ROOT)}: {{{{{name}}}}}")
    check(
        "V10",
        not drift,
        "docs placeholders match canonical" if not drift else f"drift: {drift}",
    )

    print()
    if failures:
        print(f"RESULT: FAIL ({len(failures)} violation(s))")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
