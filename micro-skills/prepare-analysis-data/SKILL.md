---
name: prepare-analysis-data
description: "Clean, link, or aggregate records into an analysis dataset."
metadata:
  level: task
  status: draft
  action: "Modify"
  category: empirical-analysis
---

# Prepare analysis datasets

Shared rules · [Empirical code and data](../empirical-analysis/SKILL.md)

**Use when** — Clean, link, or aggregate records into an analysis dataset.

**Do** — Identify the keys and observation level before joining. Check unmatched records and describe their effect on coverage. Keep variables that share the same unit and sample together where practical.

**Don’t** — Silently treat missing identifiers or unobserved activity as zeros.

**Check** — One can explain a row, its keys, and which records survived the join.

**Stay asleep for** — Describe existing variables in a manuscript without rebuilding the data.
