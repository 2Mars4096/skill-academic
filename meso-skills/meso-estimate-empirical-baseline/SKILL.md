---
name: meso-estimate-empirical-baseline
description: "On explicit selection, estimate and verify a baseline."
metadata:
  level: task
  status: draft
  category: meso-empirical-analysis
---

# Estimate and verify a baseline

[Empirical code and data](../meso-empirical-analysis/SKILL.md) · [Related micro rule](../../micro-skills/design-empirical-test/SKILL.md)

**Use when** — A defined empirical comparison needs its first reference estimate.

**Correction behind the workflow** — A later variation is hard to interpret when the original comparison, estimation sample, or uncertainty calculation is unclear.

**Begin** — Run only after the person selects this task for the current request.

1. Write down the observation unit, outcome and scale, exposure, reference group or period, sample definition, and variation that identifies the coefficient. Use the established specification where one exists. Identify controls, fixed effects, and the level for uncertainty estimates as appropriate to the design.
2. Run the baseline when estimation is in scope. Verify the actual estimation count and usable variation after restrictions and fixed effects. Account for dropped observations or groups when they change the comparison.
3. Read the coefficient against the stated contrast. Show a meaningful change in the outcome’s units, with uncertainty. Deliver the full baseline specification and available controls, observation count, fit statistic appropriate to the estimator, fixed effects, and uncertainty convention. Correct one implementation discrepancy if the run differs from the intended model.

**Deliver and stop** — Return the reproducible reference output and its supported interpretation. If the design supplies insufficient variation, explain what cannot be estimated. A small or imprecise estimate is still a baseline. Allow at most one targeted correction and recheck. Another round or workflow requires a fresh human choice.

**Stay asleep for** — Change one component of an existing baseline, or write a manuscript section from a completed exhibit.
