# Design Principles

Academic AI skills in this repository should be practical, auditable, and conservative.

## Skill Design

- Put trigger-critical context in the `description` frontmatter.
- Keep `SKILL.md` focused on reusable workflow instructions.
- Put repeatable document structures in `templates/`.
- Put deterministic parsing or checking logic in `scripts/`.
- Avoid unnecessary dependencies in early versions.

## Academic Integrity

- Do not fabricate references, data, reviewer comments, journal rules, line numbers, or manuscript changes.
- Preserve confidential manuscript material outside examples and tests.
- Mark uncertain claims as requiring author verification.
- Prefer precise, limited claims over broad assurances.

## Release Quality

- Each skill should include a usable template or script when it improves repeatability.
- Scripts should have minimal tests.
- Examples must be synthetic or public-domain-safe.
- Reference projects may inform structure, but not provide copied content.
