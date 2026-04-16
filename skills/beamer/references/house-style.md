# Beamer House Style

These are stable preferences extracted from prior Beamer sessions.

## Workflow

- Reuse the parent template, existing macros, and current folder layout before inventing a new deck structure.
- If the project uses a `main.tex` hub plus a folder like `beamers/`, keep `main.tex` as the include hub and do the round-specific work in a snippet file.
- Comment out older includes rather than deleting them, unless the user explicitly asks to remove them.
- Compile the local `main.tex` after meaningful edits.
- After compile, review the output for visual problems, not just TeX errors.
- When a figure, table, or TikZ graphic was edited or regenerated, use an explicit review loop: compile, inspect, tweak, and compile again until it looks right.

## Empirical Result Slides

- Clearly state variable construction, variable definitions, window choice, unit of observation, fixed effects, and standard-error or clustering choice.
- Put important x and y definitions in slide text when the audience needs them.
- Use one clean equation per block, not multiple overlapping equations that say almost the same thing.
- Use coefficients with standard errors in parentheses and significance stars rather than sign-only summary tables.
- If sample size changes across outcomes or variable families, add a short sample summary or `N` note.
- Keep only the specification actually used in the deck. Remove unused or confusing alternatives.
- Add a concise summary slide for the block: what is consistent, what the caveat is, and what it implies.

## Tables and Figures

- If the repo already uses `adjustbox`, `resizebox`, and `minipage` notes, stay with that pattern.
- Fix truncated or clipped material by splitting the content or moving a figure to its own frame, not by shrinking everything aggressively.
- When figures are crucial, make sure they show up properly in the rendered PDF. If needed, give them dedicated frames.
- Do not accept default plot config blindly. Tweak width, height, scale, legend placement, label size, margins, line thickness, annotation positions, or panel layout when the slide is hard to read.
- Validate figures at slide scale: axis text, legends, node labels, notes, and in-figure annotations must remain readable without zooming in.
- Generated TikZ plots need repeated visual review. Adjust the source, regenerate, and recompile until the plot is balanced and the intended message is obvious.
- If a figure and text compete for space, prefer changing the layout or giving the figure a larger frame rather than compressing both.

## Literature Review Decks

- Keep the main deck about the scholar and literature first. Put user-specific extension ideas near the end unless asked for a personalized pitch deck.
- Group inventory slides by category rather than scattering reading-tier or side-note slides through the middle of the narrative.
- For frontier-heavy decks, it can be better to lead with the newest or most decision-relevant stream rather than strict chronology.
- Use academic, natural wording. Avoid rigid prompt-shaped labels such as "what makes this important" unless the user asks for that framing.
- If collaborators matter, short affiliations can be more useful than generic area labels.

## Local Anti-Patterns

- Avoid `--` in slide titles when the user has objected to it.
- Avoid `:` in titles when the user has objected to it.
- Avoid `multicolumn` tables when the deck can stay readable without them.
