"""Validate SKILL.md frontmatter for academic-ai-skills."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass
class Frontmatter:
    name: str
    description: str


def parse_frontmatter(path: Path) -> Frontmatter:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening YAML frontmatter delimiter")

    fields: dict[str, str] = {}
    closing_index = None
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_index = index
            break
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')

    if closing_index is None:
        raise ValueError("missing closing YAML frontmatter delimiter")
    if "name" not in fields:
        raise ValueError("frontmatter missing name")
    if "description" not in fields:
        raise ValueError("frontmatter missing description")

    name = fields["name"]
    description = fields["description"]
    if not NAME_RE.match(name):
        raise ValueError(f"invalid skill name: {name}")
    if len(description.split()) < 8:
        raise ValueError("description is too short to guide routing")
    return Frontmatter(name=name, description=description)


def iter_skill_files(root: Path = SKILLS_DIR) -> list[Path]:
    return sorted(path / "SKILL.md" for path in root.iterdir() if path.is_dir())


def validate(root: Path = SKILLS_DIR) -> list[str]:
    errors: list[str] = []
    if not root.exists():
        return [f"missing skills directory: {root}"]

    for skill_file in iter_skill_files(root):
        if not skill_file.exists():
            errors.append(f"{skill_file.parent.name}: missing SKILL.md")
            continue
        try:
            frontmatter = parse_frontmatter(skill_file)
        except ValueError as exc:
            errors.append(f"{skill_file}: {exc}")
            continue
        if frontmatter.name != skill_file.parent.name:
            errors.append(
                f"{skill_file}: frontmatter name '{frontmatter.name}' does not match folder '{skill_file.parent.name}'"
            )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=SKILLS_DIR, help="Skills directory to validate.")
    args = parser.parse_args(argv)

    errors = validate(args.root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Frontmatter OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
