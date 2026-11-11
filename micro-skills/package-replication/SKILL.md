---
name: package-replication
description: "Organize code and outputs so a reader can regenerate the paper’s exhibits."
metadata:
  level: task
  status: draft
  action: "Deliver a replication package"
  category: empirical-analysis
---

# Prepare a replication package

Shared rules · [Empirical code and data](../empirical-analysis/SKILL.md)

**Use when** — Organize code and outputs so a reader can regenerate the paper’s exhibits.

**Do** — Keep scripts needed for the current paper and requested research extensions, including the builders they depend on. Trace each exhibit to its script and specification in one compact index. In a cleanup, remove obsolete intermediate helpers from the delivered package after checking their consumers.

**Don’t** — Let standalone validation scripts, comparison reports, or internal process files dominate the research package, or discard useful research extensions solely because they are absent from the current draft.

**Check** — A reader can locate and reproduce each paper exhibit, and every additional retained script has a concrete research purpose.

**Stay asleep for** — Tidy an application repository that has no paper or exhibits.
