---
name: tex-revision-compare
description: Make local LaTeX review copies that preserve original wording and show labeled, colored proposed edits at the smallest meaningful word, phrase, sentence, or paragraph span. Use for granular revision comparisons and original-plus-proposal markup in TeX and compiled PDFs.
---

# LaTeX revision comparison

Produce a comparison that an unfamiliar reader can understand immediately. Preserve the original wording, show each proposal next to the exact affected span, and highlight only necessary changes. This is a presentation workflow; it does not authorize speculative rewriting or changes beyond the requested editorial scope.

## Local review copy

- Inspect the document and project instructions. Leave source originals untouched; create a clearly named local comparison copy, such as `paper-review.tex`, or a review directory for multi-file projects. Never overwrite an existing review artifact without checking its role.
- Keep original text in its original order, including punctuation, citations, and LaTeX markup. Wrapping an affected span is allowed; silently correcting or deleting original wording is not.
- For included files, route the review entry point to review copies of edited files. Do not inadvertently compile the unchanged original or modify shared originals. Keep bibliography and asset paths working.
- Do not publish, synchronize, or change an Overleaf project merely to create a local comparison.

## Smallest meaningful changes

- Edit only what the user's request requires. Leave acceptable wording alone; optional stylistic alternatives do not belong in the comparison unless requested.
- Show unchanged text once in normal black. Wrap only the changed word or phrase when that accurately communicates the proposal. Include punctuation only when affected.
- Split independent edits when intervening words are unchanged. Keep a grammatically coupled change together when splitting it would make acceptance ambiguous or the sentence incoherent.
- Use a complete sentence only when its structure genuinely changes; use a paragraph only for an actual paragraph-level restructuring. Do not highlight a whole paragraph because it contains several small edits.
- A minimal character diff is not the objective: preserve whole readable words and the smallest coherent editorial unit. Avoid nested or overlapping revisions.
- For insertions, show only the added content at its insertion point. For deletions, retain the exact original span and explicitly mark it for deletion. Never replace a deleted span with unexplained blank text.

## Readable visual organization

Use `assets/review-markup.tex` as a starting point for ordinary prose, adapting it to the document rather than forcing incompatible markup.

- Unchanged text: black, unmarked.
- Affected original span: dark muted red, fully legible, without strikeout.
- Proposed replacement: dark blue, immediately following the original, enclosed in brackets with its change ID and the words **replace with**.
- Insertion: dark blue bracketed annotation labeled **insert**.
- Deletion: retain the red original and follow it with a blue bracketed annotation labeled **delete preceding marked text**.
- Include only a compact inline legend near the beginning of the manuscript, on the same page as manuscript content. Never create a separate legend page, cover page, or forced page break for it. Explain that red marks affected original text and blue brackets contain labeled proposals. Labels and brackets must make the comparison understandable in grayscale as well.
- Maintain the manuscript's readable font size, normal wrapping, and paragraph spacing. Avoid tiny annotations, large colored boxes, full-line background fills, and commentary between every word.
- Use IDs `R1C1`, `R1C2`, etc. for a first review if no scheme is supplied. Treat them as neutral change IDs; do not invent meanings for R and C. Respect supplied reviewer/comment IDs, adding suffixes if several edits map to one comment. Preserve IDs when revising an existing comparison and assign new IDs to new changes.
- Put substantive reasons, if needed, in a compact separate list keyed to IDs. Do not repeat obvious substitutions in a long change log.

Example (only `show` changes):

```latex
Our results \TRreplace{R1C1}{show}{suggest} that investment increased.
```

The original word remains red; the immediately following blue annotation reads `[R1C1 — replace with: suggest]`. The rest remains black. Never highlight `Our results` or `that investment increased` in this example.

## LaTeX integrity and verification

- Copy the helper into the review project and load it in the preamble, then place `\TRlegend` inline near the first manuscript text, after any title-page machinery so it does not occupy a standalone page. Inspect existing macros/packages for conflicts first. The helper is for ordinary prose, not a universal TeX parser.
- Preserve command boundaries, braces, math delimiters, environments, references, and citation keys. Do not apply blind word-diff markup inside command names or arguments.
- Headings, captions, bookmarks, verbatim, equations, alignment tables, and other fragile structures need context-specific treatment. If inline markup is unsafe, keep the original structure intact and place a clearly anchored, labeled original/proposed comparison immediately nearby. Do not duplicate executable labels, footnotes, counters, or citation side effects inside both alternatives.
- For a genuine paragraph rewrite, present a compact pair of original/proposed paragraphs with the ID and explicit labels. Do not force a long proposal into an unreadable inline bracket.
- Verify every original span against the source, and check that reading the proposed alternatives yields coherent prose. Check that shared words were not needlessly highlighted and each change has an unambiguous boundary.
- Compile using the project's existing engine and bibliography workflow when available. Inspect the resulting PDF for legibility, wrapping, clipping, and clear replacement boundaries; fix markup-induced problems. Never claim visual inspection based only on a successful compilation. If compilation or rendering is unavailable, state the limit.
- Deliver the local comparison TeX and, when generated, its PDF. Identify any unresolved compilation limitations. A clean revised version is optional when requested, not a substitute for the comparison.
