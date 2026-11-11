---
name: meso-verify-reported-bug
description: "On explicit selection, determine whether a reported failure persists after a change."
metadata:
  level: task
  status: draft
  category: meso-software-maintenance
---

# Verify a reported bug fix

[Software implementation and maintenance](../meso-software-maintenance/SKILL.md) · [Related micro rule](../../micro-skills/verify-reported-bug/SKILL.md)

**Use when** — Determine whether a reported failure persists after a change.

**Correction behind the workflow** — A workaround can prevent the original action while leaving its failure unexplained. Verification needs the capability and acceptance condition established in the preceding turns.

**Begin** — Run only after the person selects this task for the current request. A suggestion alone ends at the suggestion.

1. Reconstruct the reported action from the complaint and preceding turns. Identify the capability the user was trying to use, the starting state, and the expected result. Reproduce the failure on the affected version where possible.
2. Trace the failure to the responsible state change, calculation, or handoff. If a proposed fix restricts the failing action, check whether the user requested that restriction. A rejected workaround sends the investigation back to the cause and the original acceptance condition.
3. When a fix is in scope, apply the smallest supported correction and repeat the original action through the normal entry point. Also exercise the adjacent state implicated by the cause, such as crossing the boundary that triggered the failure. If one correction does not resolve it, report the remaining failure at this pass's stopping point.

**Deliver and stop** — Return the tested version, action, expected and observed result, and verdict. Label a check on a substitute build or partial path as partial verification. This run permits one initial pass and at most one targeted correction and recheck. A further round or another workflow needs a fresh human choice.

**Stay asleep for** — Design a new feature or perform a general code review.
