# Release Checklist

Use this checklist before publishing a release or announcing the repository.

## Repository Hygiene

- [ ] `_reference/` is ignored and absent from tracked files.
- [ ] Examples contain only synthetic, public, or non-confidential material.
- [ ] README skill index matches `skills/*/SKILL.md`.
- [ ] `LICENSE`, `CITATION.cff`, `CHANGELOG.md`, and `CONTRIBUTING.md` are present.
- [ ] `docs/reference_audit.md` lists inspected third-party references.

## Skill Quality

- [ ] Each skill has `SKILL.md` and `README.md`.
- [ ] Each `SKILL.md` has valid YAML frontmatter.
- [ ] Each frontmatter `name` matches the folder name.
- [ ] Trigger descriptions mention concrete use cases and expected outputs.
- [ ] Integrity rules prohibit fabricated comments, references, data, line numbers, page numbers, and manuscript changes.
- [ ] Templates are usable without requiring private manuscript material.

## Validation

- [ ] Run `python scripts/check_frontmatter.py`.
- [ ] Run `python scripts/validate_skill_structure.py`.
- [ ] Run `pytest tests/`.
- [ ] Run `python scripts/build_skill_index.py --check`.
