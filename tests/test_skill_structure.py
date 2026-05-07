from pathlib import Path
import subprocess

from scripts import validate_skill_structure


ROOT = Path(__file__).resolve().parents[1]


def test_required_skill_structure_is_present():
    assert validate_skill_structure.validate(ROOT) == []


def test_reference_directory_is_gitignored():
    completed = subprocess.run(
        ["git", "check-ignore", "_reference/"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    )
    assert "_reference/" in completed.stdout
