# Skill Authoring Guide

This guide defines how to add or revise skills in this repository.

## Required Files

Each skill folder must contain:

- `SKILL.md`
- `README.md`

Use `references/`, `templates/`, and `examples/` when they add practical value.

## Frontmatter

Every `SKILL.md` must begin with YAML frontmatter:

```yaml
---
name: skill-name
description: Clear one-sentence description specifying when to use the skill and what output it produces.
---
```

The `name` must match the folder name. The `description` should mention user intent, workflow type, and expected output.

## Writing Rules

- Use concise, procedural language.
- Put routing cues in the description, not only in the body.
- Separate workflow steps from integrity rules.
- Mark unverifiable claims as `[Author to verify]`.
- Do not include confidential or real unpublished material.
- Do not copy third-party skill prose or templates.

## Resource Rules

- `references/`: detailed guidance that an agent can load when needed.
- `templates/`: reusable output shapes.
- `examples/`: synthetic examples showing safe usage.

Keep resources directly linked from `SKILL.md` or the skill README.

## Validation

Run:

```bash
python scripts/check_frontmatter.py
python scripts/validate_skill_structure.py
pytest tests/
```
