---
name: academic-workflow-orchestrator
description: End-to-end academic workflow planning skill for revise-and-resubmit, thesis correction, systematic review, journal submission, and pre-submission audit workflows, producing ordered task plans, input requirements, output packages, quality gates, and human-verification checkpoints.
---

# Academic Workflow Orchestrator

Use this skill for multi-stage academic work that combines several component skills.

## Supported Modes

- revise-and-resubmit workflow
- thesis correction workflow
- systematic review workflow
- journal submission workflow
- manuscript pre-submission audit workflow

## Workflow

1. Identify the workflow type and decision context.
2. Select component skills.
3. Define required input files.
4. Define expected output package.
5. Create an ordered task plan.
6. Add quality gates before finalization.
7. Mark human-verification checkpoints.
8. Prevent false claims of completion when inputs are missing.

## Component Skill Use

- `reviewer-response`: response letters and revision maps.
- `manuscript-audit`: consistency and claim-evidence checks.
- `systematic-review`: review protocol, search, screening, and synthesis planning.
- `journal-submission-checker`: final package and declaration checks.
- `findskill`: routing when the workflow is ambiguous.

Never fabricate references, data, page numbers, reviewer comments, journal rules, or completion status.
