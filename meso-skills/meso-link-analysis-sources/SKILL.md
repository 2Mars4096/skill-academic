---
name: meso-link-analysis-sources
description: "On explicit selection, link data sources and audit coverage."
metadata:
  level: task
  status: draft
  category: meso-empirical-analysis
---

# Link data sources and audit coverage

[Empirical code and data](../meso-empirical-analysis/SKILL.md) · [Related micro rule](../../micro-skills/prepare-analysis-data/SKILL.md)

**Use when** — Two sources must be linked and the usable coverage matters for analysis.

**Correction behind the workflow** — A high match rate among distinct identifiers can coexist with poor coverage of the observations that carry the analysis.

**Begin** — Run only after the person selects this task for the current request.

1. Identify each source’s unit, candidate keys, time validity, and expected match cardinality. Check key uniqueness on the side expected to be unique. Separate missing identifiers from identifiers that are present but unmatched.
2. Apply the justified linkage rule. Inspect conflicting matches before accepting them and keep unmatched records identifiable. Compare row counts before and after the join so that repeated lookup keys cannot silently multiply observations.
3. Report matched counts and denominators for distinct eligible entities and for eligible analysis rows. Inspect an ambiguous or unmatched case and a successful link when available. If one identifiable key defect explains a discrepancy, repair it once and rerun the coverage check.

**Deliver and stop** — Return the linked data or crosswalk, the matching rule, and what the sources cover. Identify material gaps by period or group when they affect the intended comparison. Allow at most one targeted correction and recheck. Another round or workflow requires a fresh human choice.

**Stay asleep for** — Reshape an already linked file to a new observation level.
