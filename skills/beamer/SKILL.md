---
name: beamer
description: Build or revise academic Beamer slide decks in LaTeX, especially research talks, literature reviews, empirical update decks, and snippet-based `main.tex` plus include-file workflows. Use when the user wants slides created or updated, existing figures/tables/results translated into readable frames, or the deck compiled and checked for layout and logic.
---

# Beamer

## Overview

This skill is for academic Beamer work. Reuse the local deck conventions first. If the repo already has a parent template, local macros, a `main.tex`, or an include folder such as `beamers/`, preserve that structure instead of inventing a new one.

## Start Here

Run this sequence:

1. `Project Scan`
2. `Deck Type`
3. `Slide Plan`
4. `Edit Strategy`
5. `Compile`
6. `Visual Review Loop`
7. `QA`
8. `Tighten`

## Project Scan

At the start, find:

- `main.tex`, parent templates, theme macros, and local commands
- include folders such as `beamers/`, `sections/`, or `slides/`
- `citation.bib`, figure folders, table fragments, and result `.tex` inputs
- TikZ sources, generated plot scripts, or intermediate figure files that may need regeneration
- build hints such as `latexmkrc`, makefiles, or existing compile commands

If a parent template exists above the current deck or elsewhere in the project, inspect it first and follow it.

## Deck Type

Pick the working mode before writing slides:

- `Empirical update`: results, design, interpretation, and sanity checks
- `Literature review`: agenda map, paper inventory, deep dives, and reading priorities
- `Theory or framework`: setup, mechanism, logic chain, predictions, and implications
- `Hybrid`: literature framing followed by empirical or extension ideas

When the user clearly cares most about one stream, let that stream lead the deck even if strict chronology would not.

## Edit Strategy

Prefer the repo's existing include pattern.

- If `main.tex` is a hub and a folder like `beamers/` exists, create or update a round-specific snippet file and include it from the hub.
- Comment out older includes rather than deleting them unless the user explicitly asks for removal.
- Do not delete old snippets or build artifacts unless the user explicitly asks.

## Empirical Slide Rules

For result blocks:

- Put the point of the slide in the title or first line.
- State the unit of observation, window construction, fixed effects, and standard-error or clustering choice once per block.
- Define important x and y variables in the slide body when they matter. Do not bury them only in notes.
- Show one clean regression equation per block. Remove unused or redundant equations.
- Prefer coefficients with standard errors in parentheses and significance stars over sign-only summaries.
- If columns do not use the same sample, add an `N` row or a short sample note.
- Explain how to read the coefficient when sign direction is not obvious.
- Keep summary slides concise: consistent findings, caveats, and implication.

If the local deck already uses `adjustbox`, `resizebox`, and `minipage` notes for tables, keep that style.

## Literature Review Rules

Default structure:

1. `Author information`
2. `Research map by category`
3. `Collaborators by category or stream`
4. `Paper inventory by category`
5. `Deep dives on the priority papers`
6. `Summary`
7. `What to read closely`
8. `Extension or build-on ideas`

Rules:

- Keep the deck about the scholar or literature, not about the user, unless the user explicitly wants a personalized pitch deck.
- If tying the literature to the user's agenda, keep that material near the end unless told otherwise.
- Paper slides should feel academic and natural. Do not force identical subheadings on every paper.
- Put paper inventories by category. For scholar decks, list all relevant papers in compact category inventory slides before selective deep dives.
- Keep reading priorities separate from the main narrative unless the user asks to weave them into the deck.
- For deep dives, include only the fields that help: question, setup or data, design or model, mechanism, results, tradeoffs, and conclusion.
- When the user wants screenshots or placeholders, name the exact paper id and figure or table number.
- Keep user-specific extension ideas at the end. The main deck should read as a literature review first and an extension pitch second.

## Writing and Layout Rules

- Keep neighboring frames logically consecutive.
- Split dense material across frames instead of shrinking it until it is unreadable.
- Give important figures their own frame if necessary.
- Prefer category-based inventory slides over arbitrary mid-deck detours unless the user asks for them.
- Use concise academic wording. Avoid obvious prompt-shaped labels or filler headings.
- For research-group literature reviews, use a restrained seminar style: clear, serious, and not flashy or corporate.
- Default to single-column tiered `itemize` for analytical slides: a short framing line if useful, 2-4 top-level bullets, and 1-2 sub-bullets per top-level bullet.
- Use single-column numbered progressions for genuinely sequential material such as stage games, mechanisms, pipelines, timing, or causal logic.
- Do not use repeated Beamer `block` cards as the default slide grammar. Use blocks only when they clarify a real distinction.
- Avoid 2-column layouts for normal text-heavy slides. Columns are acceptable for genuine side-by-side comparisons, collaborator lists, or diagrams where the layout improves comprehension.
- Use bold lead-ins such as `Question`, `Setup`, `Mechanism`, `Evidence`, `Trade-off`, `Implication`, and `Takeaway`, but only where they make the slide easier to read.
- Avoid `:`, `;`, and `--` in slide titles and visible slide prose when practical. Rewrite the line instead of relying on punctuation-heavy phrasing.
- Avoid `\multicolumn` tables unless the existing deck already depends on them or there is no clean alternative.
- Avoid leaving only one or two words on their own line. Rephrase, adjust manual line breaks, resize the local block, or split the frame.
- If a slide only exists to say a weaker version of an adjacent slide, remove it.

## Paper Slide Rules

- For theory or game-theory papers, make the setup clear before the result: players, decisions, timing, tradeoffs, constraints, mechanism, and implication.
- For empirical papers, state how the result is obtained before interpreting it: data, measurement, research design or specification, identification logic, and main outcomes.
- Do not let every paper slide look like a rigid prompt template. Keep a consistent grammar, but include only the fields that matter for that paper.
- For deep dives, build logic gradually. Each slide should answer the audience's current question and make the next question natural.
- Remove presenter-roadmap slides from the middle of the deck. Convert them into actual presentation content or move them to notes if needed.
- For extension slides, prefer a small number of crisp research questions plus data support. Each question should state what will be analyzed.
- When deriving extensions from the user's research interests, use broad topical alignment rather than exposing the user's exact existing projects unless asked.

## Figure and TikZ Guardrails

- Do not accept default figure sizing or TikZ config if the result looks cramped, clipped, tiny, or visually unbalanced.
- When figures are generated in TikZ or by a plot pipeline, treat figure tuning as iterative work: adjust config, regenerate, recompile, and review until it looks right.
- Validate that axis labels, legends, annotations, footnotes, panel labels, and captions are readable at slide scale, not just when zoomed in.
- Check that text does not overlap marks, lines, bars, nodes, or neighboring annotations.
- Check that the figure's visual emphasis matches the slide claim. If the point is hard to see, simplify or restyle the figure instead of adding more explanation text.
- If a generated figure still fails after small tuning, give it more space, split the content across frames, or simplify the plot.
- For multi-panel or dense figures, prefer legibility over compactness.
- For screenshot figures that already contain their own caption or numbering, do not repeat the figure number, title, or caption in slide text.
- Use figure-only or near-figure-only slides when needed. A `plain` frame is acceptable for standalone screenshot slides.
- For result figures, add one short headline before the figure that tells the audience what to see, unless the slide is intentionally figure-only.
- If a figure must show only one panel from a larger screenshot, crop in LaTeX with `trim`, `viewport`, `clip`, width, and height settings before creating a new image file.
- Keep explanatory text left-aligned. Center the figure, not the takeaway sentence or itemized text.

## Title Rules

- Use informative functional titles. Prefer `Paper Short Name: Slide Function` when the deck accepts colon titles.
- Avoid titles like `...: Figure`, generic `Overview`, or repeated `Category: Paper Title` patterns when a more precise function exists.
- Good second-half title functions include `Core Idea`, `Setup`, `Stage Game`, `Research Design`, `Data`, `Mechanism`, `Main Findings`, `Calibration`, `Implications`, and `Synthesis`.
- Keep category opener, inventory, and reference titles distinct from paper deep-dive titles.

## Compile

Use the local build convention if one exists.

Otherwise:

- prefer `latexmk -pdf main.tex`
- fall back to `pdflatex -interaction=nonstopmode -halt-on-error main.tex`

After substantive edits, compile before stopping.

## Visual Review Loop

After each meaningful round of slide or figure edits:

1. compile the deck
2. review the edited frames in the rendered output
3. tweak slide layout or figure config
4. compile again

Do this repeatedly until the edited slides look right and all intended text, tables, figures, captions, notes, and annotations show up correctly in the rendered PDF.

This is especially important for:

- generated TikZ plots
- regenerated statistical figures
- frames with dense tables or notes
- slides where text and figures share limited space
- slides with manual line breaks or text wrapping that may create one- or two-word dangling lines

Do not treat `it compiled` as sufficient when the visual result is still off.

## QA

Do not stop at a successful compile.

- read the log for fatal errors, missing files, bad bibliography keys, duplicate labels, and overfull or underfull boxes that change layout
- inspect the rendered deck if local tools allow it; otherwise say that visual inspection was limited
- verify that edited text, figures, and TikZ output are actually shown properly on the slide
- fix truncated tables, clipped figures, frame spillover, confusing ordering, unreadable labels, and unused equations or notes
- fix awkward line wrapping, especially one- or two-word dangling lines
- if a generated TikZ or plot frame still looks wrong, keep iterating instead of stopping at the first barely acceptable version

## References

Read these only when needed:

- `references/house-style.md` for stable Beamer preferences extracted from prior sessions
- `references/deck-checklists.md` for empirical, literature-review, and framework-deck checklists
