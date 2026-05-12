# Beamer House Style

These are stable preferences extracted from prior Beamer sessions.

## Workflow

- Reuse the parent template, existing macros, and current folder layout before inventing a new deck structure.
- If the project uses a `main.tex` hub plus a folder like `beamers/`, keep `main.tex` as the include hub and do the round-specific work in a snippet file.
- Comment out older includes rather than deleting them, unless the user explicitly asks to remove them.
- Compile the local `main.tex` after meaningful edits.
- After compile, review the output for visual problems, not just TeX errors.
- When a figure, table, TikZ graphic, or dense text frame was edited or regenerated, use an explicit review loop: compile, inspect, tweak, and compile again until everything intended is visible, readable, and correctly placed.

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
- Avoid `\multicolumn` tables unless the existing deck already depends on them or there is no clean alternative.
- Fix truncated or clipped material by splitting the content or moving a figure to its own frame, not by shrinking everything aggressively.
- When figures are crucial, make sure they show up properly in the rendered PDF. If needed, give them dedicated frames.
- Do not accept default plot config blindly. Tweak width, height, scale, legend placement, label size, margins, line thickness, annotation positions, or panel layout when the slide is hard to read.
- Validate figures at slide scale: axis text, legends, node labels, notes, and in-figure annotations must remain readable without zooming in.
- Generated TikZ plots need repeated visual review. Adjust the source, regenerate, and recompile until the plot is balanced and the intended message is obvious.
- If a figure and text compete for space, prefer changing the layout or giving the figure a larger frame rather than compressing both.

## Literature Review Decks

- Keep the main deck about the scholar and literature first. Put user-specific extension ideas near the end unless asked for a personalized pitch deck.
- Group inventory slides by category rather than scattering reading-tier or side-note slides through the middle of the narrative.
- For scholar decks, include compact category inventory slides that account for all relevant papers before deciding which papers deserve deep dives.
- For frontier-heavy decks, it can be better to lead with the newest or most decision-relevant stream rather than strict chronology.
- Use academic, natural wording. Avoid rigid prompt-shaped labels such as "what makes this important" unless the user asks for that framing.
- If collaborators matter, short affiliations can be more useful than generic area labels.
- Keep user-specific motivation out of the main literature narrative unless asked. It belongs in the extension or future-work section.

## Research Group Slide Grammar

- The default analytical slide should be single-column tiered `itemize`: a short framing sentence when useful, 2-4 top-level bullets, and 1-2 sub-bullets per top-level bullet.
- Use numbered progressions only for sequential material: stage games, timing, classification pipelines, causal chains, or mechanisms.
- Do not make repeated stacked `block` cards the default deck grammar. Blocks are fine occasionally when they mark a real conceptual distinction.
- Avoid 2-column layouts for normal text-heavy slides. Columns are acceptable for true side-by-side comparisons, collaborator lists, or diagrams.
- Use bold lead-ins when they help scanning, but avoid prompt-like labels that sound mechanical or redundant.
- The presentation should look like a serious research group literature review, not a corporate deck or design showcase.

## Paper Deep Dives

- Theory slides should define players, decisions, timing, constraints, tradeoffs, mechanisms, and implications before moving to results.
- Empirical slides should explain data, measurement, design or specification, identification logic, and outcomes before asking the audience to interpret a result.
- Keep consistency across papers without forcing every paper into the same rigid template.
- Remove presenter-roadmap slides from the middle of the deck; turn them into actual content or notes.
- Every line should earn its place. Consecutive slides should answer the audience's current question and set up the next one.

## Local Anti-Patterns

- Avoid `:`, `;`, and `--` in slide titles and visible slide prose when practical.
- Avoid `\multicolumn` tables when the deck can stay readable without them.
- Avoid line wraps that leave only one or two words on their own line.

## Figure Slides

- Screenshot figures that already contain captions or numbering should not get repeated captions, figure numbers, or "Figure" titles in the slide.
- Figure-led slides can be plain frames, especially when the image is the whole point.
- For result figures, add one short headline telling the audience what to see unless the frame is intentionally figure-only.
- If only one panel is needed from a multi-panel figure, crop it in LaTeX with `trim`, `viewport`, `clip`, width, and height settings before creating new image assets.
- Keep takeaway text left-aligned and center only the figure.

## Slide Titles

- For paper deep dives, prefer `Paper Short Name: Slide Function` when the deck accepts colon titles.
- Avoid generic titles such as `Overview` or `Figure` when the slide has a more specific job.
- Good functional labels include `Core Idea`, `Setup`, `Stage Game`, `Research Design`, `Data`, `Mechanism`, `Main Findings`, `Calibration`, `Implications`, and `Synthesis`.
