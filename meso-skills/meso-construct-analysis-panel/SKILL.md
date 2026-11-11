---
name: meso-construct-analysis-panel
description: "On explicit selection, construct a panel and its measures."
metadata:
  level: task
  status: draft
  category: meso-empirical-analysis
---

# Construct a panel and its measures

[Empirical code and data](../meso-empirical-analysis/SKILL.md) · [Related micro rule](../../micro-skills/prepare-analysis-data/SKILL.md)

**Use when** — Records must become one observation per analysis unit and period, or a constructed measure needs to be reproduced.

**Correction behind the workflow** — Aggregating a ratio or filling absent periods changes the quantity being measured. Later regressions need a clear account of what one row means.

**Begin** — Run only after the person selects this task for the current request.

1. Define the output key, time interval, and coverage window. Establish which source rows contribute, which quantities add up, how observations are weighted, and what an absent period means. Add zero rows only when the source supports that interpretation.
2. Build the requested panel. For a share or rate, trace the numerator and denominator to the source fields and transformations that generate them. Record their units and zero-denominator rule. Choose the calculation that answers the question, such as pooled totals for a transaction-weighted share or an average of unit shares for an equal-unit estimand.
3. Check uniqueness of the panel key. Reconstruct one unit-period from its contributing records, including the separate components of a constructed measure, and reconcile an additive total across a period or group. If the reconstruction disagrees, correct the aggregation once and repeat the same check.

**Deliver and stop** — Return the panel or its construction code with the key, measure definitions, and reconciliation. State any coverage assumption that limits interpretation. Allow at most one targeted correction and recheck. Another round or workflow requires a fresh human choice.

**Stay asleep for** — Audit the quality of a join or run an estimator on an existing panel.
