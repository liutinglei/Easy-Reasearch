---
name: reviewer-response
description: Prepare, audit, and revise academic reviewer response letters, editor cover letters, thesis examiner responses, rebuttal tables, revision maps, and manuscript correction packages. Use when working with peer-review comments, journal revisions, thesis corrections, response-to-reviewers documents, comment-to-change traceability, non-defensive academic rebuttals, overclaiming checks, or final revision package audits.
---

# Reviewer Response

Use this skill to turn reviewer, editor, examiner, or supervisor feedback into a clear academic response package. Keep the work traceable: every response should connect a comment, an action, a manuscript location, and the claim made in the response letter.

## Operating Rules

- Preserve each comment's meaning before drafting a response.
- Answer every comment explicitly, including minor formatting comments.
- Separate what was changed in the manuscript from what is merely explained in the response.
- Use respectful, precise, non-defensive language.
- Mark missing locations, line numbers, references, or author decisions as `[Author to verify]`.
- Do not invent reviewer comments, manuscript changes, references, data, page numbers, line numbers, ethics details, or journal rules.
- Do not claim an issue is fully resolved unless the revised manuscript supports that claim.
- When the manuscript text is unavailable, draft provisional responses and label all change claims that require verification.

## Workflow

### 1. Establish the Review Context

Identify the review type:

- journal peer review
- editor technical check
- thesis or dissertation examination
- post-viva correction
- supervisor or committee review
- resubmission after rejection

Capture any known constraints: journal name, decision type, deadline, required files, reviewer count, line-numbering requirements, and whether the reply must be reviewer-specific or combined.

### 2. Extract and Number Comments

Break the source review into atomic comments. Prefer this convention:

```text
Editor, Comment 1
Reviewer 1, Comment 1
Reviewer 1, Comment 2
Reviewer 2, Comment 1
Examiner 1, Comment 1
```

Do not merge separate concerns unless they clearly ask for the same manuscript change.

Use `scripts/comment_parser.py` for a first-pass split when the comments are in plain text.

### 3. Classify the Issue

Assign one or more labels:

- conceptual framing
- literature coverage
- method or experimental design
- data analysis
- results interpretation
- discussion or implication
- limitation
- figure, table, or caption
- terminology or consistency
- language and style
- formatting or journal compliance
- reference or citation
- ethics, consent, or data availability
- requires author decision

### 4. Draft Each Response

Use this structure unless the journal requires another format:

```markdown
**Response:** Thank you for this helpful comment. We have revised the manuscript to clarify [specific issue]. The revised text now [specific change]. This change appears in [section/page/line].

**Revision made:** [quote or concise summary of the revised manuscript text]

**Status:** Addressed / partially addressed / clarified / not changed with justification / author verification needed
```

For disagreement or partial changes, acknowledge the concern, explain the rationale, and state what was changed to reduce ambiguity. Keep the tone calm and evidence-based.

### 5. Build a Revision Map

Create a table with these fields:

| Comment ID | Concern | Action Taken | Manuscript Location | Revised Text or Summary | Status |
|---|---|---|---|---|---|

Use `requires author verification` when the response depends on unavailable manuscript text, line numbers, page numbers, data, or references.

### 6. Check for Overclaiming

Prefer precise revision claims:

| Risky wording | Safer wording |
|---|---|
| This issue has been completely resolved. | We revised the relevant section to address the concern more directly. |
| All inconsistencies were removed. | We reviewed the relevant passages and corrected the inconsistencies identified in the comment. |
| The manuscript is now much stronger. | The revised version provides a clearer explanation of the issue. |
| We rewrote the whole section. | We revised the relevant paragraphs to clarify the specific point raised. |

### 7. Final Audit

Before finalizing, check:

- Every comment has a response.
- The response preserves the reviewer's meaning.
- Each claimed change appears in the manuscript or is marked for verification.
- Page, line, section, table, and figure references are real.
- References and data claims are real and relevant.
- The tone is professional, concise, and non-defensive.
- Partial disagreements are justified without sounding dismissive.
- The editor can trace each concern to a manuscript action.

## Bundled Resources

- `templates/editor_cover_letter.md`: cover letter structure for revised submissions.
- `templates/reviewer_response_table.md`: reviewer-by-reviewer response table.
- `templates/revision_map.md`: traceability table between comments and manuscript changes.
- `templates/consistency_checklist.md`: final audit checklist.
- `scripts/comment_parser.py`: dependency-free plain-text comment parser.
