# Style Rules

These rules capture the preferred review-report style learned from prior finalized reports and revision traces.

## Contents

- `Voice`
- `Concision`
- `Headings`
- `Technical Level`
- `Evidence Discipline`
- `Citation Discipline`
- `Recommendation Language`
- `LaTeX Preferences`
- `Final Submit Check`

## Voice

- Be direct, academic, and fair.
- Preserve the user's substantive intention.
- Polish wording only where it improves clarity, accuracy, tone, or native phrasing.
- Do not make the report sound more certain than the evidence supports.
- Do not use ornate words when simple ones work.
- When converting rough thoughts, keep the user's intended severity, recommendation, and skepticism.

Preferred tone:

- "I appreciate the authors' effort..."
- "I am not persuaded that..."
- "This weakens the interpretation because..."
- "Please reconcile this pattern with..."
- "The authors should clarify..."

Avoid:

- overly harsh personal language
- excessive praise that undercuts a negative recommendation
- vague complaints such as "the paper is messy" without the exact readability problem
- fancy substitutes when "hard to address", "unlikely", or "unclear" is enough
- wording that blames the reviewer for asking for robustness checks; acknowledge author effort without self-reference

## Concision

- Major comments should usually be `1` or `2` paragraphs.
- Minor comments should be `1` to `3` sentences.
- Keep only the strongest `2` to `5` minor comments.
- Merge author questions into the relevant comment instead of adding a separate question list.
- Avoid detailed coefficient narration unless the numerical comparison is central to the critique.
- If the user asks for fewer comments, compress rather than preserving every concern.
- Do not make a comment longer just because the underlying econometric issue is complex.

## Headings

- Use highlighted phrase headings.
- Keep headings neutral but informative.
- Do not start every heading with "Lack of".

Examples:

- `Identification concerns`
- `Weak dynamic evidence`
- `Measurement clarity`
- `Mechanism tests on an inconsistent sample`
- `Sales-forecast placebo interpretation`

## Technical Level

- Make the editor-level concern clear before technical detail.
- Use advanced econometric terminology only when it changes the recommendation.
- If the user wants a high-level point, do not expand into niche diagnostics.
- Do not ask for a long list of robustness checks when one targeted check would reveal the problem.
- Prefer broad, interpretable requests such as "some industry-by-time controls" when the user asks not to over-specify a fix.

Examples:

- For a fragile shift-share or Bartik IV, explain the actual identifying variation and why historical shares may be correlated with later trends.
- For staggered DiD, mention TWFE bias or heterogeneous treatment effects when relevant, but connect it to the paper's treatment timing and event-study evidence.
- For mechanism comments, prefer common-sample or direct-outcome checks over abstract mediation language unless the paper itself uses mediation.

## Evidence Discipline

- Check the manuscript before asserting a contradiction.
- Do not rely on untabulated response-letter results in a final report unless the comment is about the revision response itself.
- If a table appears only in a response letter, be explicit or avoid the point.
- If sample sizes differ, state why the difference matters for interpretation, not just that they differ.
- If comparing coefficient magnitudes, consider whether the variables are on comparable scales and whether a common subsample is needed.
- Distinguish what authors argue from what they actually provide evidence for.
- Before finalizing, check whether the report falsely interprets a table, figure, sample, or response.
- If a concern depends on unavailable or hidden evidence, either verify it from the files or do not raise it.

## Citation Discipline

- Add citations only when they materially support a contribution or method critique.
- Prefer the single closest benchmark paper over a broad literature list.
- If the user requests UTD24-only citations, keep only relevant UTD24 or field-leading journal citations.
- Create or update `ref.bib` when adding a citation to a LaTeX report.
- Do not cite papers just to make the report look scholarly.

## Recommendation Language

For rejection:

- say why a satisfactory revision is unlikely
- avoid sounding punitive
- keep the report useful

For risky major revision:

- explain that concerns are addressable but substantial and uncertain
- do not overstate as rejection if a plausible path exists

For major revision:

- state the remaining issues and why they matter
- acknowledge meaningful improvements in revision rounds

For minor revision:

- keep comments bounded and avoid opening new fundamental issues

## LaTeX Preferences

- Use `\textbf{...}` for comment headings.
- Use `\citep{...}` or `\citet{...}` only when the citation is in `ref.bib` or can be verified.
- Avoid `--` in prose.
- Escape journal-style terms where needed, such as `M\&SOM` and `R\&R`.
- Keep table and figure references simple, such as `Table~2` and `Figure~R2-1`.
- When the user asks for a snippet, return only the LaTeX snippet and do not edit the file.

## Final Submit Check

Before saying "ready to submit", confirm:

- no placeholder text remains
- no private draft notes or commented brainstorming remain
- recommendation is stated once and consistently
- major comments are not duplicated in minor comments
- every issue mentioned in the summary is developed below
- all citations used in the report have bib entries
- tone is collegial but firm
- the report is not making a point the user explicitly decided to drop
- the report answers the editor's decision problem, not every possible improvement to the paper
