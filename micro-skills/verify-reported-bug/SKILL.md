---
name: verify-reported-bug
description: "Diagnose or retest a failure someone can reproduce."
metadata:
  level: task
  status: draft
  action: "Review and fix"
  category: software-maintenance
---

# Verify a reported bug fix

Shared rules · [Software implementation and maintenance](../software-maintenance/SKILL.md)

**Use when** — Diagnose or retest a failure someone can reproduce.

**Do** — Recover the exact gesture, input, and expected result from the user’s report. Reproduce it in the affected interface and retest after fixing the cause. Check another relevant input to establish that the fix covers the supported case. State the build actually exercised.

**Don’t** — Replace a requested gesture with a different interaction and call the original bug fixed, hard-code the demonstration input, or rely only on compilation or lower-level tests.

**Check** — The original action succeeds on the reported case and a relevant additional case in the tested build.

**Stay asleep for** — Design a new feature with no failure to reproduce.
