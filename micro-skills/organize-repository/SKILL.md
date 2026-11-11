---
name: organize-repository
description: "Reduce unnecessary files, duplicate artifacts, or nested folders."
metadata:
  level: task
  status: draft
  action: "Organize"
  category: software-maintenance
---

# Organize an existing repository

Shared rules · [Software implementation and maintenance](../software-maintenance/SKILL.md)

**Use when** — Reduce unnecessary files, duplicate artifacts, or nested folders.

**Do** — Trace files to their current consumers. Consolidate duplicates and keep the shallowest structure that still explains where working inputs, code, and outputs belong. Verify affected entry points after moves.

**Don’t** — Remove an older-looking file until its role in the current workflow is understood.

**Check** — Every retained directory has a purpose and the normal workflow still resolves its files.

**Stay asleep for** — Plan a new feature without changing repository structure.
