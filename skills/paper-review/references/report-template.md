# Report Template

Use this as a flexible structure, not a rigid form. Preserve the user's recommendation and substantive intent.

## Contents

- `LaTeX Skeleton`
- `Summary And Recommendation Pattern`
- `Major Comment Pattern`
- `Minor Comment Pattern`
- `Optional Closing`

## LaTeX Skeleton

```tex
\begin{center}
    \large
    \noindent{\bf \underline{Review Comments}}

    \emph{``<Title>''} \\
    Submitted to \emph{<Journal>} (<Submission ID>)
\end{center}

\subsection*{Summary and Recommendation}

<One paragraph summarizing the question, main evidence, strengths, main concerns, and recommendation.>

\vspace{1em}

\subsection*{Major Comments}

\begin{enumerate}[leftmargin=*]

\item \textbf{<Short phrase heading>.} <Evidence-based concern. Explain why it matters. End with a concrete request or implication.>

\item \textbf{<Short phrase heading>.} <Evidence-based concern. Explain why it matters. End with a concrete request or implication.>

\end{enumerate}

\subsection*{Minor Comments}

\begin{enumerate}[leftmargin=*]

\item \textbf{<Short phrase heading>.} <Concrete fixable issue.>

\item \textbf{<Short phrase heading>.} <Concrete fixable issue.>

\end{enumerate}
```

## Summary And Recommendation Pattern

Use four moves:

1. Identify the paper's question and core finding.
2. Name one or two strengths, especially in revision rounds.
3. State the core concerns that determine the recommendation.
4. Give the recommendation clearly.

Keep the summary concise. It should set up the editor's decision, not preview every comment.

For a new submission:

```text
This paper studies <question/context>. The authors find <main finding> using <data/design>. The topic is <important/timely/relevant>, and the paper has <strength>. However, I am concerned that <core concern 1> and <core concern 2>. These issues <weaken the contribution/undermine the causal interpretation/make the managerial implications unclear>. My recommendation is <decision>. Please see my detailed comments below.
```

For a revision:

```text
I appreciate the authors' substantial effort in this revision. The new analyses on <items> materially strengthen the paper. However, several important issues remain regarding <issue family>. Because these changes may be non-trivial to implement, my recommendation is <decision>. Please see my detailed comments below.
```

If the revision substantially addressed prior comments but more work remains, use a collegial opening while keeping the recommendation honest:

```text
I appreciate the authors' substantial effort in this revision, which addresses many of my previous concerns. I have only a few additional points to help clarify the interpretation and reinforce the identification and mechanism evidence. Because some suggested revisions may be non-trivial to implement, my recommendation is <decision>.
```

For rejection:

```text
Despite the authors' efforts, I do not see a sufficiently strong contribution relative to <benchmark>, and I am not persuaded that <design/evidence> isolates <claimed effect>. Together, these issues make a satisfactory revision unlikely. My recommendation is rejection.
```

## Major Comment Pattern

Each major comment should follow this logic:

```text
\item \textbf{<Issue phrase>.} <What the paper does or claims.> <What the table/figure/design actually shows.> <Why this creates a problem for the contribution, identification, mechanism, or interpretation.> Please <specific request>, so readers can <interpretation goal>.
```

Good issue headings are short phrases:

- `Limited contribution`
- `Identification concerns`
- `Weak dynamic evidence`
- `Measurement clarity`
- `Mechanism tests on an inconsistent sample`
- `Economic significance`
- `External validity`
- `Bartik IV with a fragile exclusion restriction`
- `Heterogeneity coefficients are internally inconsistent`
- `Sales-forecast placebo interpretation`

Avoid sentence-style headings that already make the whole argument.

When the user supplies rough language, preserve the intended point and severity:

```text
Rough thought: <user's point>
Polished comment: \item \textbf{<Issue phrase>.} <same point, tightened and grounded in evidence>
```

## Minor Comment Pattern

Minor comments should be concrete:

```text
\item \textbf{<Issue phrase>.} In <table/figure/page/section>, <specific issue>. Please <specific fix>.
```

Good minor comments include:

- unclear figure axes or event-time labels
- duplicate table numbers
- mislabeled table references
- inconsistent sample-period statements
- missing variable definitions in summary statistics
- repeated sentences or distracting typos

Do not include:

- a new identification critique
- a new contribution critique
- a request requiring major new data

## Optional Closing

Use a closing only when helpful, especially for rejection:

```text
I thank the authors for their work on this important topic and hope these comments are useful as they revise the project.
```

Do not add a closing if it makes the report longer without improving tone.
