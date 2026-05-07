"""Validate required repository and skill structure."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SKILLS = {
    "findskill",
    "reviewer-response",
    "manuscript-audit",
    "systematic-review",
    "journal-submission-checker",
    "academic-workflow-orchestrator",
}
REQUIRED_ROOT_FILES = {
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CITATION.cff",
    ".gitignore",
}


def read_readme_skill_names(readme: Path) -> set[str]:
    names: set[str] = set()
    for line in readme.read_text(encoding="utf-8").splitlines():
        if line.startswith("| `"):
            parts = line.split("`")
            if len(parts) >= 2:
                names.add(parts[1])
    return names


def is_reference_ignored(root: Path) -> bool:
    completed = subprocess.run(
        ["git", "check-ignore", "_reference/"],
        cwd=root,
        text=True,
        capture_output=True,
    )
    return completed.returncode == 0


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []

    for filename in sorted(REQUIRED_ROOT_FILES):
        if not (root / filename).exists():
            errors.append(f"missing root file: {filename}")

    for doc in [
        "docs/design_principles.md",
        "docs/reference_audit.md",
        "docs/skill_authoring_guide.md",
        "docs/release_checklist.md",
    ]:
        if not (root / doc).exists():
            errors.append(f"missing doc: {doc}")

    skills_dir = root / "skills"
    if not skills_dir.exists():
        errors.append("missing skills directory")
        return errors

    actual_skills = {path.name for path in skills_dir.iterdir() if path.is_dir()}
    missing = REQUIRED_SKILLS - actual_skills
    extra = actual_skills - REQUIRED_SKILLS
    for name in sorted(missing):
        errors.append(f"missing required skill folder: {name}")
    for name in sorted(extra):
        errors.append(f"unexpected skill folder: {name}")

    for name in sorted(REQUIRED_SKILLS & actual_skills):
        folder = skills_dir / name
        for filename in ["SKILL.md", "README.md"]:
            if not (folder / filename).exists():
                errors.append(f"{name}: missing {filename}")

    readme_skills = read_readme_skill_names(root / "README.md")
    for name in sorted(readme_skills - actual_skills):
        errors.append(f"README lists missing skill: {name}")
    for name in sorted(REQUIRED_SKILLS - readme_skills):
        errors.append(f"README missing required skill: {name}")

    if not is_reference_ignored(root):
        errors.append("_reference/ is not ignored by git")

    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root.")
    args = parser.parse_args(argv)

    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Skill structure OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
