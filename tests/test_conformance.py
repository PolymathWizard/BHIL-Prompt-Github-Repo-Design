"""Conformance suite for REPO-TO-EXPERIENCE v1.0.

Runs the validator as a subprocess (the same gate CI uses) and adds
structural assertions plus regression tests. Regression tests are named for
the specific failure they prevent, per BHIL convention.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANONICAL = (ROOT / "prompt" / "repo-to-experience.md").read_text("utf-8")


def test_validator_suite_passes():
    result = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate_prompt.py")],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_repo_layout_complete():
    for path in [
        "README.md",
        "LICENSE",
        "LICENSE-CONTENT",
        "NOTICE",
        "CITATION.cff",
        "CHANGELOG.md",
        "CONTRIBUTING.md",
        "mkdocs.yml",
        "prompt/repo-to-experience.md",
        "examples/worked-example-helm.md",
        "engagements/.gitkeep",
    ]:
        assert (ROOT / path).exists(), f"missing {path}"


def test_never_block_on_missing_optional():
    """The control surface must instruct inference, not blocking."""
    assert "Never block on a missing value" in CANONICAL


def test_fix_pass_cap_is_three():
    """Scorecard remediation is capped to prevent unbounded fix loops."""
    assert "cap 3 fix passes" in CANONICAL


# Regression tests: each names the bug it prevents.


def test_regression_scorecard_lost_single_file_line():
    """Bug prevented: an edit to the Phase 5 gate dropped the
    self-containment check, which is the only line that protects the
    artifact branch's no-external-requests guarantee."""
    scorecard = re.findall(
        r'<self_check gate="true">(.*?)</self_check>', CANONICAL, re.S
    )[-1]
    assert "self-contained, no external requests" in scorecard


def test_regression_branch_constraints_not_swapped():
    """Bug prevented: CSP hard constraints (no CDN, no fetch) drifting into
    the multi_file branch, or CDN permission drifting into single_file."""
    single = re.search(
        r'<branch context="single_file_artifact">(.*?)</branch>', CANONICAL, re.S
    ).group(1)
    multi = re.search(
        r'<branch context="multi_file_site">(.*?)</branch>', CANONICAL, re.S
    ).group(1)
    assert "NO external scripts" in single
    assert "NO fetch/XHR/WebSocket" in single
    assert "External libraries" in multi and "permitted" in multi
    assert "NO fetch" not in multi


def test_regression_evidence_principle_stays_first():
    """Bug prevented: reordering operating principles demoted EVIDENCE OVER
    INVENTION below aesthetic principles; it must remain principle 1 because
    the whole credibility posture hangs on it."""
    principles = re.search(
        r"<operating_principles>(.*?)</operating_principles>", CANONICAL, re.S
    ).group(1)
    first = re.search(r"1\.\s+([A-Z ]+)\.", principles).group(1)
    assert first.strip() == "EVIDENCE OVER INVENTION"


def test_regression_worked_example_keeps_inference_flags():
    """Bug prevented: cleanup passes stripping evidence-tier tags from the
    worked example, silently promoting inferences to fact."""
    example = (ROOT / "examples" / "worked-example-helm.md").read_text("utf-8")
    assert example.count("[INFERENCE]") >= 5
    assert "[VERIFIED]" in example
    assert "[CORROBORATED]" in example
    assert "UNVERIFIED" in example


def test_regression_reduced_motion_in_both_design_and_requirements():
    """Bug prevented: reduced-motion surviving only in Phase 3 tokens but
    dropped from Phase 5 universal requirements (or vice versa)."""
    assert "reduced-motion variant" in CANONICAL
    assert "prefers-reduced-motion" in CANONICAL
    assert "in-page motion toggle" in CANONICAL
