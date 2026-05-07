# Reference Audit

This document records public sources reviewed while designing Easy Research. The purpose is transparency: public repositories may be inspected for structural patterns, but public files in this repository are written from scratch.

## Reference Sources

| Source | Purpose | Reused Code? | Reused Text? | License Notes |
|---|---|---:|---:|---|
| Anthropic Skills repository | Understand general skill folder structure, metadata style, and resource organization | No | No | Structural reference only |
| Claude Code Skills documentation | Understand skill creation, management, and triggering concepts | No | No | Documentation reference only |
| Anthropic Agent Skills engineering article | Understand progressive disclosure and metadata design concepts | No | No | Documentation reference only |
| `Yuan1z0825/nature-skills` | Inspect repository-level organization, README index pattern, and modular skill layout | No | No | Cloned only into `_reference/nature-skills`; not committed |

## Inspection Notes

The `nature-skills` repository was inspected only for high-level organization:

- root README with a skill index
- one folder per skill
- self-contained skill resources
- optional `references/`, `scripts/`, `assets/`, or evaluation-oriented folders

No content, prose, tables, examples, scripts, templates, images, or README text from that repository is copied here. Easy Research is a broader general-purpose research writing workflow suite, not a fork or redistribution of `nature-skills`.

## Design Rule

This project does not copy third-party skill content. Existing public skills are used only to understand common patterns, including folder organization, metadata placement, modular resources, and validation habits.

All academic workflow instructions, templates, scripts, and examples in this repository are original to this project.
