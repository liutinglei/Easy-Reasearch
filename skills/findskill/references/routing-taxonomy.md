# Routing Taxonomy

## User Intent Classes

- `route-only`: user asks which skill to use.
- `single-skill-execute`: request clearly maps to one skill.
- `multi-skill-plan`: request needs ordered workflow planning.
- `audit-before-action`: request requires checking claims before drafting.
- `insufficient-context`: task cannot be routed reliably.

## Confidence Labels

- `high`: direct keyword and output match.
- `medium`: likely skill match but missing files or ambiguous output.
- `low`: multiple skills plausible; ask for clarification or use orchestrator.
