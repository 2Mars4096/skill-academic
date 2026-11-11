---
name: extend-existing-software
description: "Add a capability to software that already has a related workflow."
metadata:
  level: task
  status: draft
  action: "Modify"
  category: software-maintenance
---

# Extend an existing feature

Shared rules · [Software implementation and maintenance](../software-maintenance/SKILL.md)

**Use when** — Add a capability to software that already has a related workflow.

**Do** — Find the existing interaction that represents the same state or action. Reuse its behavior and styling when adding another way to trigger it, such as synchronizing scroll position with selected navigation. Check the new and existing paths together.

**Don’t** — Add a second highlight style, state variable, or feature path for the same user selection without a functional reason.

**Check** — The two interaction paths produce the same visible state and continue to work together.

**Stay asleep for** — Review an existing feature without implementing a change.
