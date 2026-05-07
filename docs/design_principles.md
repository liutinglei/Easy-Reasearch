# Design Principles

Easy Research is built around practical structure, transparent uncertainty, and respect for scholarly judgment.

## Originality

- Write all public project content from scratch.
- Use third-party repositories only for structural inspiration unless a future contribution explicitly handles license compatibility and attribution.
- Keep local reference repositories under `_reference/` and out of git.
- Document inspected public sources in `docs/reference_audit.md`.

## Skill Design

- Put trigger-critical context in each `description` frontmatter field.
- Keep `SKILL.md` focused on the essential workflow.
- Move detailed guidance into `references/`.
- Put reusable document shapes in `templates/`.
- Keep examples synthetic, short, and safe to publish.
- Prefer deterministic scripts for validation and indexing.

## Academic Integrity

- Do not fabricate references, data, reviewer comments, journal rules, line numbers, page numbers, ethics details, or manuscript changes.
- Preserve confidential manuscripts and private peer-review material outside the repository.
- Mark uncertain or unverifiable claims as `[Author to verify]`.
- Avoid publication guarantees, exaggerated quality claims, and journal-specific assertions that are not verified.

## Human Verification

Skills should identify where a human author, supervisor, statistician, ethics officer, editor, or reviewer must verify the output. A workflow is not complete until its verification checkpoints are resolved.
