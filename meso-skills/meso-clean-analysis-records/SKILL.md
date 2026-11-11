---
name: meso-clean-analysis-records
description: "On explicit selection, clean records for an analysis sample."
metadata:
  level: task
  status: draft
  category: meso-empirical-analysis
---

# Clean records for an analysis sample

[Empirical code and data](../meso-empirical-analysis/SKILL.md) · [Related micro rule](../../micro-skills/prepare-analysis-data/SKILL.md)

**Use when** — A source needs cleaning or a sample restriction needs auditing before analysis.

**Correction behind the workflow** — A pipeline audit must establish which filters changed the analysis sample and whether a disputed rule is an error or an accepted convention.

**Begin** — Run only after the person selects this task for the current request.

1. Identify the analysis that consumes the cleaned data and the fields it actually needs. Trace existing eligibility filters and count the records each excludes. For a network sample, check whether requiring both incoming and outgoing links excludes valid endpoint entities.
2. Classify each suspected problem before changing the cleaning code. Distinguish an invalid value, a missing required field, a legitimate repeated event, and a difference in a grouping convention. Trace a disputed boundary case through both implementations and honor any instruction to retain the current convention.
3. Apply the justified correction. Restrict missing-value exclusions to fields required by the named analysis. Preserve the full event key when several events belong to one entity. For a requested tail treatment, implement the specified capping or trimming rule and its reference sample.
4. Rebuild the affected working data and reconcile losses and recoveries by filter. Inspect a restored observation and a retained boundary case where available. Check an affected downstream output so that the reported impact rests on the rebuilt sample. If a check exposes an implementation error, correct it once and recheck.

**Deliver and stop** — Return the cleaned output or revised cleaning step, what makes a row eligible, and a compact accounting of exclusions. Flag any decision that depends on an undocumented source convention. Allow at most one targeted correction and recheck. Another round or workflow requires a fresh human choice.

**Stay asleep for** — Link two already-clean sources, or write prose describing an established sample.
