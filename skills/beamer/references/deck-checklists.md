# Deck Checklists

## Empirical Update Deck

Use this when the deck is translating analysis outputs into slides.

- Question and headline answer are visible early.
- Each result block states unit, time window, FE, and SE or cluster choice.
- Important x and y variables are defined on-slide.
- Summary tables show coefficients, standard errors, and stars when possible.
- Sample changes across columns are acknowledged.
- Redundant equations or unused specifications are removed.
- There is a short implications or takeaway slide after the dense result section.
- Generated figures and TikZ plots have been visually reviewed after compilation, not just inserted.

## Literature Review Deck

Use this when the deck is summarizing a scholar, field, or paper set.

- Author or context slide exists when useful.
- Research map groups the agenda into a small number of categories.
- Paper inventory is organized by category and accounts for all relevant papers.
- Only the priority papers get deep-dive slides.
- Deep dives feel natural and do not force the same template on every paper.
- Reading-priority guidance is separated from the main narrative unless the user wants it inside the deck.
- User-specific extension ideas appear near the end unless the user wants a personalized presentation.
- Collaborator slides use short affiliations or roles when that is more informative than topic labels.
- The deck reads as a literature review first and an extension pitch second.

## Research Group Layout

Use this when the deck should feel serious, clear, and seminar-appropriate.

- Most analytical slides use single-column tiered `itemize`, not repeated stacked cards.
- Numbered lists appear only for genuine sequences, stage games, pipelines, or mechanisms.
- 2-column layouts are avoided for dense prose and used only when comparison, lists, or diagrams benefit from them.
- The slide grammar is consistent, but different content types still look different enough to scan.
- There are no presenter-roadmap slides left in the middle of the deck.

## Paper Deep Dive

Use this when a paper gets more than a summary mention.

- Theory papers define players, choices, timing, constraints, tradeoffs, and mechanism before implications.
- Empirical papers explain data, measurement, design or specification, identification logic, and outcomes before conclusions.
- Results slides say how the result was obtained, not only what the result is.
- Paper slides sound academic and natural, not like a filled prompt template.
- Consecutive slides move from setup to mechanism to evidence to takeaway without gaps.

## Framework or Theory Deck

Use this when the deck explains a model or conceptual paper.

- The economic environment is defined before the mechanism.
- Consecutive slides move from setup to intuition to implications without jumping around.
- Terms are introduced before they are used.
- Comparative statics or predictions appear only after the audience has the mechanism.
- Figures are used when they clarify the logic, not as filler.

## Figure-Heavy Or TikZ Deck

Use this when the deck depends heavily on generated plots or custom diagrams.

- Figure config has been tuned for slide readability rather than left at script defaults.
- Axis labels, legends, annotations, and node text are readable at presentation scale.
- No important label overlaps or clipping remain.
- Multi-panel figures are balanced and not visually cramped.
- The edited figure frames have gone through at least one full compile and visual-review loop after the latest figure change.
- Screenshot figures with embedded captions or numbering do not repeat those captions or numbers in slide text.
- Figure-led frames include a short result headline when helpful.
- Cropped panels are checked in the PDF so the intended panel is visible and not truncated.
- Takeaway text is left-aligned when present; only the figure is centered.

## Final QA

- The deck compiles.
- The log has no fatal errors.
- Any overfull or underfull warnings that affect readability are addressed.
- No frame looks visibly overstuffed.
- Edited text, tables, figures, captions, notes, and annotations are actually visible and readable in the rendered output.
- TikZ or regenerated plots were reviewed repeatedly until they looked right, not just until they compiled.
- Visible slide text avoids `:`, `;`, and `--` where practical.
- Tables avoid `\multicolumn` unless there is no clean alternative.
- Line wrapping does not leave one- or two-word dangling lines.
- Titles follow a consistent function pattern, such as `Paper Short Name: Slide Function`, when that style is used.
- Titles avoid generic `Figure` or `Overview` labels when a more informative title is available.
- Titles and section order match the actual story.
- The last slide before references leaves the audience with the intended takeaway.
