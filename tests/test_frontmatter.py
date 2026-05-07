from pathlib import Path

from scripts import build_skill_index, check_frontmatter


ROOT = Path(__file__).resolve().parents[1]


def test_all_skill_frontmatter_is_valid():
    assert check_frontmatter.validate(ROOT / "skills") == []


def test_skill_index_is_current():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    expected = build_skill_index.replace_index(readme, build_skill_index.build_index(ROOT / "skills"))
    assert expected == readme
