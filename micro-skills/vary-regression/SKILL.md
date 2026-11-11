---
name: vary-regression
description: "Rerun a baseline with a different outcome, exposure, group, or sample."
metadata:
  level: task
  status: draft
  action: "Modify"
  category: empirical-analysis
---

# Change a regression specification

Shared rules · [Empirical code and data](../empirical-analysis/SKILL.md)

**Use when** — Rerun a baseline with a different outcome, exposure, group, or sample.

**Do** — Start from the working baseline and vary the named component. Keep the other controls, fixed effects, transformations, and comparison convention aligned. If the change itself affects who enters estimation, identify the difference.

**Don’t** — Redesign the model or change the exhibit layout during a one-component comparison.

**Check** — The old and new columns can be compared, and every substantive difference has an explanation.

**Stay asleep for** — Reformat an existing regression table without rerunning the model.
