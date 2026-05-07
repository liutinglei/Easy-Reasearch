"""Build or check the README skill index from skills/*/SKILL.md."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SKILLS_DIR = ROOT / "skills"
START = "<!-- skill-index:start -->"
END = "<!-- skill-index:end -->"


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: missing frontmatter")
    fields: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return fields
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip('"')
    raise ValueError(f"{path}: missing closing frontmatter delimiter")


def build_index(skills_dir: Path = SKILLS_DIR) -> str:
    rows = ["| Skill | Purpose |", "|---|---|"]
    for skill_file in sorted(skills_dir.glob("*/SKILL.md")):
        fields = parse_frontmatter(skill_file)
        name = fields.get("name", skill_file.parent.name)
        description = fields.get("description", "").strip()
        rows.append(f"| `{name}` | {description} |")
    return "\n".join([START, *rows, END])


def replace_index(readme_text: str, new_index: str) -> str:
    pattern = re.compile(
        rf"{re.escape(START)}.*?{re.escape(END)}",
        flags=re.DOTALL,
    )
    if not pattern.search(readme_text):
        raise ValueError("README missing skill index markers")
    return pattern.sub(new_index, readme_text)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Update README.md in place.")
    parser.add_argument("--check", action="store_true", help="Fail if README.md index is stale.")
    args = parser.parse_args(argv)

    new_index = build_index()
    current = README.read_text(encoding="utf-8")
    updated = replace_index(current, new_index)

    if args.write:
        README.write_text(updated, encoding="utf-8", newline="\n")
        print("README skill index updated")
        return 0

    if args.check and updated != current:
        print("ERROR: README skill index is stale. Run: python scripts/build_skill_index.py --write", file=sys.stderr)
        return 1
    if args.check:
        print("README skill index OK")
        return 0

    print(new_index)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
