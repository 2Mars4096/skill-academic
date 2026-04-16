# Canonical Paths

Use this when the user has an interesting area but the actual proposal type is still unclear.

Choose one primary path first. Secondary paths can be added later if the base design survives.

## Path 1: Measurement

Choose this when the main contribution is documenting a new fact, constructing a new measure, or organizing previously fragmented evidence.

### Core Claim

`This project reveals a pattern that is economically meaningful, previously under-measured, or newly measurable.`

### Minimum Evidence

- clear definition of the object being measured
- reason existing measures are inadequate
- data construction logic
- validation checks
- descriptive patterns that matter for theory, policy, or later causal work

### Common Failure Mode

The project becomes a descriptive exercise with no clear reason the facts matter.

## Path 2: Reduced-Form

Choose this when there is a plausible policy change, shock, institutional rule, or exposure that can support a credible comparison.

### Core Claim

`This project estimates the effect of a specific change in exposure on a specific outcome.`

### Minimum Evidence

- unit of treatment and unit of outcome
- timing or cross-sectional variation
- identification logic
- baseline empirical design
- most likely threats and falsification logic

### Common Failure Mode

The treatment is interesting but the identifying variation is weak, endogenous, or too small to matter.

## Path 3: Mechanism

Choose this only when there is already a believable baseline effect or a very strong reason to expect one.

### Core Claim

`This project explains why the effect happens and distinguishes the main channel from competing explanations.`

### Minimum Evidence

- baseline effect or benchmark result
- observable proxies or tests for the mechanism
- competing channels
- timing, heterogeneity, or mediator evidence

### Common Failure Mode

The mechanism becomes a story the data cannot actually distinguish.

## Path 4: Extension

Choose this when the best version of the project starts from a known paper or design and adds value through a new setting, sample, institutional detail, or interpretation.

### Core Claim

`This project shows whether a known result travels to a new margin that matters.`

### Minimum Evidence

- closest template paper
- reason the new setting is genuinely informative
- what can be learned beyond simple replication
- data and design adapted to the new context

### Common Failure Mode

The project looks like a low-value replication because the new setting is not tied to a sharper question.

## Default Decision Rules

- If data construction is the main novelty, start with `Measurement`.
- If credible variation already exists, start with `Reduced-Form`.
- If the user wants to explain `why`, first confirm there is a believable baseline effect, then use `Mechanism`.
- If the user already has a template paper, use `Extension` only if the new setting clearly changes the interpretation or importance of the result.

## Recommended Narrowing Order

When several paths seem possible, narrow in this order:

1. reduced-form
2. measurement
3. extension
4. mechanism

This ordering is conservative. It reduces the chance of writing an elegant but infeasible proposal.
