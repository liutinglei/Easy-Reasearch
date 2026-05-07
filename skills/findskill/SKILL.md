---
name: findskill
description: Meta-skill for selecting the correct academic-ai-skills module based on user intent, missing information, workflow type, and routing uncertainty, producing a concise routing decision without fabricating unavailable file contents.
---

# findskill

Use this skill before acting when a user request could map to more than one academic workflow skill.

## Routing Workflow

1. Identify the user's task type, requested output, available inputs, and missing files.
2. Match the request to one primary skill and optional supporting skills.
3. Check for over-triggering: do not select a large workflow skill when a focused skill is enough.
4. Mark uncertain decisions as `needs user verification`.
5. Do not claim access to manuscripts, reviews, search results, or submission rules that were not provided.

## Routing Output

```markdown
**Routing decision:** [skill name]
**Why:** [one sentence]
**Supporting skills:** [optional]
**Missing information:** [files, metadata, or decisions needed]
**Uncertainty:** [none / needs user verification]
**Next action:** [concise action]
```

## Skill Map

- Use `reviewer-response` for reviewer comments, response letters, revision maps, and rebuttal tone.
- Use `manuscript-audit` for consistency checks across manuscript sections, claims, results, and conclusions.
- Use `systematic-review` for PRISMA-style review planning, search strategy, screening, and synthesis.
- Use `journal-submission-checker` for submission packages, cover letters, ethics, data availability, and file checks.
- Use `academic-workflow-orchestrator` for end-to-end workflows that require multiple skills and quality gates.

Read `references/skill-selection-rules.md` when routing is uncertain.
