---
name: write-regression-code
description: "Write or reorganize Stata estimation code for an empirical paper."
metadata:
  level: task
  status: draft
  action: "Create or revise"
  category: empirical-analysis
---

# Write readable regression code

Shared rules · [Empirical code and data](../empirical-analysis/SKILL.md)

**Use when** — Write or reorganize Stata estimation code for an empirical paper.

**Do** — Write the outcome, regressors, controls, and fixed effects explicitly in the estimation command. Export each regression table with outreg2 from the do-file that runs its models. Keep data preparation upstream and the output tied to a concrete exhibit.

**Don’t** — Hide the model specification in macros or add a separate formatting program to reconstruct a table already exportable from the estimation script.

**Check** — Reading the model line reveals the specification, and running its do-file produces the intended table.

**Stay asleep for** — Write a general-purpose software library or a data downloader.
