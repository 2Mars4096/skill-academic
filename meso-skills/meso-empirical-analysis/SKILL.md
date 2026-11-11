---
name: meso-empirical-analysis
description: "On explicit request, suggest a bounded workflow for empirical code and data."
metadata:
  level: category
  status: draft
---

# Empirical code and data

[Meso-skill map](../README.md) · [Micro-skill category](../../micro-skills/empirical-analysis/SKILL.md)

**Use when** — Prepare research data, organize a reproducible pipeline, or decide what can be learned from an empirical comparison.

**Suggest** — Choose the task that matches the requested deliverable. Someone with a finished panel can start directly at the analytical question.

### Data cleaning and construction

- [Clean records for an analysis sample](../meso-clean-analysis-records/SKILL.md) — Eligibility and exclusions.
- [Link data sources and audit coverage](../meso-link-analysis-sources/SKILL.md) — Match cardinality and coverage.
- [Construct a panel and its measures](../meso-construct-analysis-panel/SKILL.md) — Row and measure reconstruction.

### Research file structure

- [Organize research files for reruns](../meso-organize-analysis-pipeline/SKILL.md) — Rerun from documented inputs.

### Data analysis

- [Check a descriptive pattern](../meso-describe-empirical-pattern/SKILL.md) — Size and coverage of the contrast.
- [Estimate and verify a baseline](../meso-estimate-empirical-baseline/SKILL.md) — Reference estimate and uncertainty.
- [Compare a regression variation with its baseline](../meso-vary-regression/SKILL.md) — A change the researcher has already specified.

### Progressive data analysis

- [Choose the next empirical test](../meso-advance-empirical-analysis/SKILL.md) — One test chosen from the current evidence.

If the open question is whether a pattern exists, suggest the descriptive comparison. If a pattern is established and the user wants a reference estimate, suggest the baseline. Once there is a result and a choice about what to investigate next, suggest one follow-up test. A coverage problem can send the decision back to the data. An inconclusive result can justify stopping. Each suggestion ends with the human’s choice.

**Stay asleep for** — A request to format existing estimates can proceed from the saved output.

**Stop** — Return at most one suggestion, its expected output, and its pass limit. A category selection opens a menu. Only an explicit choice of a task starts that task.
