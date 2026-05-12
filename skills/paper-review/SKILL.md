---
name: paper-review
description: Review academic papers and manuscripts and write, revise, or audit journal referee reports, especially empirical operations, management, supply-chain, finance-operations, and OM-interface papers. Use when the user asks to review a paper/manuscript/PDF, judge a submission, produce a recommendation, draft major/minor comments, critique contribution or identification, assess a revision/response round, perform a final submission check, or polish a LaTeX review report.
---

# Paper Review

## Overview

This skill produces rigorous academic referee reports. It should help the user judge whether a manuscript clears the publication bar, identify the few issues that matter most, and write comments that are accurate, concise, collegial, and useful to the editor.

The default style is direct but fair: summarize the paper, acknowledge real effort or strengths when present, state the recommendation clearly, and focus major comments on issues that affect contribution, identification, measurement, mechanism, managerial relevance, or revision feasibility.

## Start Here

Run this sequence:

1. `Lock review context`
2. `Read evidence first`
3. `Build the issue ledger`
4. `Decide the recommendation`
5. `Respect the requested edit mode`
6. `Draft the report`
7. `Accuracy and style pass`
8. `Submission check`

Do not start by polishing prose. First decide what the paper claims, what evidence supports those claims, and which concerns are important enough to include.

When working in an existing review folder, inspect the local structure first. Typical folders contain `main.tex`, a submission-specific `comments.tex`, and `ref.bib`. Preserve that structure.

## 1. Lock Review Context

Capture what is available:

- `Manuscript`: title, journal, submission id, round, and files
- `User stance`: reject, risky major revision, major revision, minor revision, accept, or undecided
- `Prior round`: previous report, response letter, or revision memo if available
- `Evidence sources`: manuscript PDF, tables, figures, appendix, response letter, prior comments, local bib files, relevant PDFs
- `Output target`: quick assessment, issue list, full report, LaTeX report, or final submit check
- `Edit mode`: patch the file, return a snippet only, polish current wording, reorganize comments, or only assess readiness

If the user provides a likely recommendation, respect it unless the evidence contradicts it. If the recommendation is missing, infer it from the severity and revision feasibility, then state the inference.

Ask at most `1` to `3` clarifying questions only when the answer would change the recommendation or the report structure.

## 2. Read Evidence First

Read in this order when files are available:

1. abstract, introduction, and claimed contribution
2. research design, data construction, variable definitions, and sample
3. main tables and figures
4. mechanisms, heterogeneity, placebo tests, robustness checks, and appendix tables
5. response letter and prior reviews for revision rounds
6. related literature or local PDFs only when needed to judge novelty or a specific method

Track exact anchors: table numbers, figure numbers, sample sizes, variable names, coefficient signs, timing, and page or section references when available.

Do not rely on memory or the authors' summary when a table, figure, or appendix can be checked directly.

## 3. Build The Issue Ledger

Before drafting, sort possible concerns into:

- `Contribution`: what is new, what literature benchmark it clears, and why OM or the target journal should care
- `Identification`: whether the design supports the causal or descriptive claim being made
- `Measurement and data`: whether key variables, sample coverage, dataset construction, and representativeness are credible
- `Specification`: whether controls, fixed effects, IVs, DiD/event-study methods, transformations, and standard errors match the design
- `Timing and dynamics`: whether event timing, lag structure, pre-trends, and dynamic effects support the mechanism
- `Mechanism`: whether the mechanism evidence is on the same sample, uses appropriate variables, and distinguishes alternatives
- `Economic and managerial significance`: whether statistically significant effects are large and actionable enough to matter
- `Internal consistency`: whether tables, figures, text, and response claims contradict each other
- `Readability and structure`: whether the paper's organization helps readers follow the main story
- `Revision feasibility`: whether the needed fixes are bounded or would require a new paper

Use [references/review-criteria.md](references/review-criteria.md) when choosing which concerns deserve major comments.

## 4. Decide The Recommendation

Use recommendation severity consistently:

- `Reject`: weak or unclear contribution, fundamental identification or measurement failure, misleading causal claims, severe internal inconsistency, or revision would require a new paper.
- `Risky major revision`: concerns may be addressable, but fixes are substantial and may change the scope or results.
- `Major revision`: important concerns remain, but there is a plausible path to a stronger paper.
- `Minor revision`: the main claim is credible and remaining issues are clarifications, presentation, or limited robustness checks.
- `Accept`: only when there are no decision-relevant concerns.

The recommendation paragraph should make the decision feel inevitable from the concerns, not surprising after a neutral summary.

## 5. Respect The Requested Edit Mode

The user often supplies rough but intentional language. Preserve the intended critique and edit only as much as needed.

- If asked to `polish`, keep the user's point and wording where it works; fix clarity, tone, organization, and non-native phrasing.
- If asked for `snippet only`, return only the replacement snippet and do not patch files.
- If asked to `patch`, edit the relevant `comments.tex` or report file directly.
- If asked whether a comment `makes sense`, first assess the logic and evidence, then suggest a concise version only if useful.
- If asked `good to submit?`, run an accuracy, tone, consistency, and recommendation check before saying yes.
- If the user says a point should not be raised, drop it unless it creates a serious accuracy problem elsewhere.

## 6. Draft The Report

Default report structure:

1. `Summary and Recommendation`
2. `Major Comments`
3. `Minor Comments`

For revision rounds, start by acknowledging what improved before listing remaining concerns. For rejection, keep the tone professional and explain why a satisfactory revision is unlikely.

For each major comment:

- use a short phrase heading, not a sentence
- make one central point
- ground it in specific evidence from the manuscript
- explain why it matters for the paper's claim or contribution
- end with a concrete request or implication
- keep it to `1` or `2` paragraphs unless the issue is structurally complex

For minor comments:

- keep only the most useful `2` to `5`
- make each comment concrete and fixable
- use `1` to `3` sentences
- do not hide a major concern in the minor section

Use [references/report-template.md](references/report-template.md) for a LaTeX report skeleton and reusable prose patterns.

## 7. Accuracy And Style Pass

Run this pass before finalizing:

- Check that every table, figure, variable, sample, and citation mentioned is real and correctly interpreted.
- Remove comments based only on untabulated or response-letter-only material unless the report is explicitly about the response.
- Merge repeated issues.
- Drop low-value complaints that distract from the central recommendation.
- Convert long technical excursions into the high-level concern the editor needs to understand.
- Preserve the user's substantive intention when polishing.
- Avoid over-polishing into vague or overly fancy language.
- Avoid `--` in LaTeX prose unless the user requests it.
- If adding literature, use only the closest and most credible references; create or update `ref.bib` when needed.
- When the user asks for top-journal citations only, prefer UTD24 or otherwise field-leading journal references and avoid citation sprawl.
- If patching a LaTeX report and a compile command is clear, compile after substantive edits; otherwise say visual/compile checking was limited.

Use [references/style-rules.md](references/style-rules.md) for the house style learned from prior reports and Cursor revision traces.

## 8. Submission Check

Before saying a report is ready to submit, verify:

- the recommendation in the summary matches the severity of the detailed comments
- major comments are ordered by importance
- minor comments do not introduce new major issues
- the tone is firm but not personal
- the report is concise enough for an editor to scan
- citations compile or are present in `ref.bib` if the report is in LaTeX
- no accidental draft notes, commented private thoughts, duplicate table numbers, or placeholders remain

## Output Modes

- `Quick read`: recommendation, top concerns, and uncertainty.
- `Issue ledger`: ranked concerns with evidence anchors and potential author requests.
- `Full report`: summary/recommendation plus major and minor comments.
- `LaTeX report`: compile-ready `comments.tex` or patch to an existing review folder.
- `Final check`: accuracy, tone, consistency, and submission readiness.

## Guardrails

- Do not invent literature, table contents, or statistical results.
- Do not turn a weak contribution concern into a laundry list of robustness checks.
- Do not ask authors for every possible test; ask for tests that would change interpretation.
- Do not overstate causal concerns when the paper only claims description, but flag causal language when the design is correlational.
- Do not write comments that are more technical than needed for the editor to understand the flaw.
- Keep the report useful even when recommending rejection.
