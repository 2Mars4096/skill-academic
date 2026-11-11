---
name: meso-vary-regression
description: "On explicit selection, assess how a requested specification change affects an existing estimate."
metadata:
  level: task
  status: draft
  category: meso-empirical-analysis
---

# Compare a regression variation with its baseline

[Empirical code and data](../meso-empirical-analysis/SKILL.md) · [Related micro rule](../../micro-skills/vary-regression/SKILL.md)

**Use when** — Assess how a requested specification change affects an existing estimate.

**Correction behind the workflow** — An unexplained change of sample can be mistaken for a change in the relationship being estimated.

**Begin** — Run only after the person selects this task for the current request. A suggestion alone ends at the suggestion.

1. Locate the working baseline, its output, and the exact requested variation. Read the estimation commands to identify controls, fixed effects, transformations, uncertainty estimates, and actual sample membership. Check any earlier instruction about which baseline the comparison should follow.
2. Implement the named change with the baseline's other choices carried through. For follow-up regressions tied to that baseline, include its control set unless the research question or current instruction justifies a change. Run the variation when execution is in scope and record who enters or leaves estimation.
3. Compare the estimates alongside their sample and specification differences. Trace an unexpected discrepancy to a changed input or modeling choice before interpreting it. Correct an unintended difference once and rerun the affected comparison. Where a measure changes eligibility, disclose that change and use a common-sample check when it fits the authorized comparison.

**Deliver and stop** — Return a side-by-side result, the specification and sample differences, and what the comparison can support. If the baseline or required inputs cannot be reproduced, identify the unresolved difference and stop. This run permits one initial pass and at most one targeted correction and recheck. A further round or another workflow needs a fresh human choice.

**Stay asleep for** — Restyle a table already produced by the analysis.
