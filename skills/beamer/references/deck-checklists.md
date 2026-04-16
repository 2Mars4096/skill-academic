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
- Paper inventory is organized by category.
- Only the priority papers get deep-dive slides.
- Deep dives feel natural and do not force the same template on every paper.
- Reading-priority guidance is separated from the main narrative unless the user wants it inside the deck.
- User-specific extension ideas appear near the end unless the user wants a personalized presentation.

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

## Final QA

- The deck compiles.
- The log has no fatal errors.
- Any overfull or underfull warnings that affect readability are addressed.
- No frame looks visibly overstuffed.
- Edited text and figures are actually visible and readable in the rendered output.
- TikZ or regenerated plots were reviewed repeatedly until they looked right, not just until they compiled.
- Titles and section order match the actual story.
- The last slide before references leaves the audience with the intended takeaway.
