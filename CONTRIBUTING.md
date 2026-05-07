# Contributing

Thank you for helping improve Academic AI Skills. Contributions should keep the project original, transparent, and useful for academic workflows.

## Ground Rules

- Do not copy third-party skill text, scripts, examples, templates, images, or README content.
- Do not submit real unpublished manuscripts, confidential reviewer comments, private data, API keys, or institution-only material.
- Use synthetic examples unless public reuse is clearly permitted.
- Preserve attribution and license notices for any third-party material discussed in documentation.
- Keep claims conservative. Do not promise publication, journal acceptance, or complete compliance.

## Skill Contributions

Every skill must include:

- `SKILL.md` with YAML frontmatter containing `name` and `description`
- `README.md` explaining the skill's purpose and safe use
- references, templates, or examples only when they directly support the skill

Before opening a pull request, run:

```bash
python scripts/check_frontmatter.py
python scripts/validate_skill_structure.py
pytest tests/
```

If you add or rename a skill, rebuild the README index:

```bash
python scripts/build_skill_index.py --write
```

## Review Criteria

Pull requests are reviewed for:

- originality
- academic integrity safeguards
- clear trigger metadata
- practical workflows
- test coverage for structure and frontmatter
- absence of confidential or copied material
