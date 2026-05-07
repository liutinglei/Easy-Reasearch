---
name: manuscript-audit
description: Audit academic manuscripts for consistency across abstract, methods, results, discussion, conclusion, tables, hypotheses, response letters, and claims, producing claim-evidence matrices and verification notes.
---

# Manuscript Audit

Use this skill to identify unsupported claims, inconsistent interpretations, missing methodological details, and misalignment across manuscript sections.

## Workflow

1. Identify available inputs: abstract, introduction, hypotheses, methods, results, tables, figures, discussion, conclusion, response letter, and reviewer comments.
2. Extract major claims and map each claim to evidence.
3. Check whether results are interpreted consistently in discussion and conclusion.
4. Flag unsupported causal language, statistical overinterpretation, and claims that exceed the data.
5. Check whether abstract and conclusion match the reported results.
6. Mark unverifiable statements as `[Author to verify]`.

## Output

Produce:

- claim-evidence matrix
- section alignment notes
- unsupported or overextended claim list
- statistical interpretation warnings
- AI-tone or overpolishing warnings when wording becomes vague, inflated, or mechanically polished
- prioritized revision recommendations

Read `references/claim-evidence-consistency.md` for the matrix method.
