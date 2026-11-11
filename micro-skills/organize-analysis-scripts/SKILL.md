---
name: organize-analysis-scripts
description: "Arrange recurring data-cleaning and estimation scripts for reruns."
metadata:
  level: task
  status: draft
  action: "Organize"
  category: empirical-analysis
---

# Organize a research pipeline

Shared rules · [Empirical code and data](../empirical-analysis/SKILL.md)

**Use when** — Arrange recurring data-cleaning and estimation scripts for reruns.

**Do** — Separate data preparation, estimation or model training, and exhibit production, with clear inputs and outputs for each stage. Number scripts in execution order and retain section/item numbering where used. Standard Python cleaning scripts should run directly without arguments. Download scripts can take options.

**Don’t** — Repeat cleaning inside each figure script or hide the standard cleaning run behind undocumented flags.

**Layout** — For a research package, keep codes, tables, and figures as sibling folders and name output subfolders after their generating scripts. Keep untouched source data in raw. Preserve working references to data held elsewhere during cleanup.

**Check** — A collaborator can run raw data through working panels to results in order, and identify the input and output of each script.

**Stay asleep for** — Write a one-off download command for a source.
