# Easy Research

[![Tests](https://github.com/liutinglei/Easy-Reasearch/actions/workflows/test.yml/badge.svg)](https://github.com/liutinglei/Easy-Reasearch/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-v0.1.0_draft-blue.svg)](CHANGELOG.md)

Original AI-agent skills for academic researchers, PhD students, journal authors, and reviewers.

Easy Research is a general-purpose research writing workflow suite. It covers systematic literature reviews, reviewer response letters, manuscript revision audits, journal submission checks, citation integrity, and multi-step research workflow orchestration. The scope is broader than narrowly focused academic writing skill packs: it is designed to help agents plan, route, audit, and assemble full research writing workflows while preserving human verification.

The repository is designed for Claude, Codex, and other agentic coding environments that can load modular `SKILL.md` instructions.

## Skill Index

<!-- skill-index:start -->
| Skill | Purpose |
|---|---|
| `academic-workflow-orchestrator` | End-to-end academic workflow planning skill for revise-and-resubmit, thesis correction, systematic review, journal submission, and pre-submission audit workflows, producing ordered task plans, input requirements, output packages, quality gates, and human-verification checkpoints. |
| `findskill` | Meta-skill for selecting the correct Easy Research module based on user intent, missing information, workflow type, and routing uncertainty, producing a concise routing decision without fabricating unavailable file contents. |
| `journal-submission-checker` | Prepare and audit journal submission packages, including cover letters, ethics and consent statements, data availability, conflicts of interest, author contributions, AI-use disclosure, scope fit, and file checklists. |
| `manuscript-audit` | Audit academic manuscripts for consistency across abstract, methods, results, discussion, conclusion, tables, hypotheses, response letters, and claims, producing claim-evidence matrices and verification notes. |
| `reviewer-response` | Prepare, audit, and revise academic reviewer response letters, editor cover letters, thesis examiner responses, response tables, and revision maps with traceable manuscript-location claims and overclaiming checks. |
| `systematic-review` | Support PRISMA-style systematic literature review workflows, including research question decomposition, database search planning, screening protocols, inclusion and exclusion criteria, duplicate handling, quality appraisal planning, and synthesis tables. |
<!-- skill-index:end -->

## Project Philosophy

Academic work benefits from structure, but it cannot be automated responsibly without verification. These skills help agents organize scholarly workflows while preserving human academic judgment.

Core rules:

- Do not fabricate references, reviewer comments, data, line numbers, page numbers, journal rules, ethics details, or manuscript changes.
- Mark unverifiable claims as `[Author to verify]`.
- Keep confidential manuscripts and private review materials out of examples and tests.
- Treat third-party repositories as structural references only unless their license and attribution terms are explicitly handled.
- Prefer precise, auditable claims over polished but unsupported prose.

## Folder Structure

```text
Easy Research/
+-- README.md
+-- LICENSE
+-- CHANGELOG.md
+-- CONTRIBUTING.md
+-- CITATION.cff
+-- docs/
+-- skills/
|   +-- findskill/
|   +-- reviewer-response/
|   +-- manuscript-audit/
|   +-- systematic-review/
|   +-- journal-submission-checker/
|   +-- academic-workflow-orchestrator/
+-- scripts/
+-- examples/
+-- tests/
+-- _reference/      # ignored; local structural references only
```

## Quick Start

Validate the repository:

```bash
python scripts/check_frontmatter.py
python scripts/validate_skill_structure.py
pytest tests/
```

Rebuild the README skill index:

```bash
python scripts/build_skill_index.py --write
```

Use a skill by pointing an agent at the relevant folder, for example:

```text
Use the reviewer-response skill in skills/reviewer-response to convert these reviewer comments into a point-by-point response table. Mark all unknown manuscript locations as [Author to verify].
```

## Usage Examples

Reviewer response:

```text
Use reviewer-response to draft a respectful reply to Reviewer 2. Preserve the original comments, create a revision map, and flag any change claims that need author verification.
```

Manuscript audit:

```text
Use manuscript-audit to compare this abstract, results excerpt, and conclusion. Build a claim-evidence matrix and identify unsupported causal claims.
```

Systematic review:

```text
Use systematic-review to design a search strategy and screening protocol for the topic in examples/demo_slr_topic.md. Do not invent database results.
```

Journal submission:

```text
Use journal-submission-checker to audit the submission package. Check ethics, consent, data availability, conflicts of interest, AI-use disclosure, and missing files.
```

Workflow orchestration:

```text
Use academic-workflow-orchestrator for a revise-and-resubmit project. Identify required input files, choose component skills, define outputs, and add human-verification checkpoints.
```

## Ethical Rules

- These skills support research workflows; they do not replace author responsibility, supervisor review, editor judgment, reviewer judgment, ethics review, statistical review, or legal advice.
- No skill should claim guaranteed acceptance, guaranteed publication, or guaranteed compliance with a journal.
- No skill should generate fake citations, fake search results, fake reviewer comments, or fake manuscript edits.
- Examples must be synthetic, public, or explicitly cleared for publication.

## Development Roadmap

- v0.1.0: Core academic skill suite, validation scripts, and tests.
- v0.2.0: Stronger example packages and template refinements.
- v0.3.0: Optional deterministic utilities for screening logs, claim matrices, and package checks.
- v0.4.0: Cross-skill evaluation examples using synthetic academic tasks.

## Attribution

This project is original. Public repositories may be inspected for structural inspiration, such as folder organization, skill indexing, and modular resource layout. No third-party text, code, templates, examples, images, scripts, or README content is copied into this repository.

`Yuan1z0825/nature-skills` was reviewed only as a local structural reference. Easy Research is not a fork, rebrand, redistribution, or derivative copy of that project. The public repository contains original files written for a broader academic research workflow scope.

Local third-party references must stay under `_reference/`, which is ignored by git. See `docs/reference_audit.md` for the audit record.

## License

This project is released under the MIT License.
