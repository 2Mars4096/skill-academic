---
name: idea-cart
description: Capture important ideas, decisions, constraints, risks, questions, and follow-up points during a long conversation or work session, keep them small and prioritized, then review and checkout selected items into concrete actions, plans, TODOs, issues, notes, or deliverables. Use when useful points may otherwise be forgotten before they are acted on.
---

# Idea Cart

## Overview

This skill keeps a lightweight working cart of important points that are not ready to become commitments yet.

Use it to preserve signal across a long conversation or work session without turning the entire discussion into memory. The cart is a temporary buffer: items are captured, reviewed, pruned, and eventually checked out into real work or deliberately dropped.

## Core Model

- `Cart`: a short list of useful points worth preserving.
- `Checkout`: converting selected cart items into committed work, such as a plan, TODO, issue, patch checklist, note, decision record, or final deliverable.
- `Receipt`: a short record of what was checked out, implemented, moved, dropped, or left pending.

The cart is not a transcript, scratchpad, or permanent memory store. Keep only durable points that could change future work.

## When To Use

Use this skill when the user says or implies:

- "cart this"
- "add this to the idea cart"
- "save this for later"
- "do not lose this point"
- "show/review the cart"
- "checkout the cart"
- "turn the saved points into a plan/TODO/issues"
- "we discussed useful things earlier and I do not want them lost"

Also use it when a long exploratory session is producing decisions, constraints, risks, or follow-up actions that may be forgotten before execution.

## Cart File

Prefer a local markdown file so future sessions can recover the cart without relying on conversation history.

Choose the cart location in this order:

1. Use the path explicitly requested by the user.
2. If an idea cart already exists in the current project, use it.
3. If the project has an agent-facing folder such as `.agents/` or `.claude/`, use that folder.
4. Otherwise create `.agents/idea-cart.md` in the current project when file writes are appropriate.
5. If no file can be used, keep a compact in-message cart and state that it is session-local.

Use this file shape:

```markdown
# Idea Cart

Last reviewed: YYYY-MM-DD

## Active Items

### IC-001 - Short title
- Status: carted
- Priority: high
- Kind: constraint
- Scope: checkout flow
- Point: Make checkout idempotent across repeated runs.
- Why: Re-running a session should not duplicate downstream work.
- Checkout target: implementation checklist
- Acceptance: Repeated checkout does not create duplicate tasks or edits.

## Checkout Log

### YYYY-MM-DD
- IC-001 -> moved to implementation checklist.
```

## Item Fields

Keep items compact. Default fields:

- `Status`: `carted`, `selected`, `committed`, `done`, `dropped`, `stale`, or `question`
- `Priority`: `high`, `medium`, or `low`
- `Kind`: `idea`, `decision`, `constraint`, `risk`, `question`, `follow-up`, `evidence`, or `reference`
- `Scope`: where the point applies
- `Point`: the durable idea in one sentence
- `Why`: why this matters later
- `Checkout target`: where it should go if acted on
- `Acceptance`: how to tell the item was handled

Only add optional fields when useful:

- `Source`: short pointer to where the idea came from
- `Owner`: person or role responsible
- `Expires`: date or condition after which the item should be reviewed or dropped
- `Links`: files, issues, notes, or external references

## Add To Cart

When the user asks to cart a point:

1. Identify the durable point, not the surrounding conversation.
2. Classify `Kind`, `Priority`, and `Scope`.
3. Write the smallest useful item to the cart file.
4. Confirm with the item ID and short title.

If the user says "cart this" and the referent is ambiguous, infer from the immediately preceding discussion when safe. If there are multiple plausible points, propose up to `3` candidate cart items and ask which to keep.

When many points appear at once, do not cart everything. Prefer `2` to `5` high-signal items and explicitly merge duplicates.

## Review Cart

When asked to review or show the cart:

1. Read the cart file.
2. Summarize active items by priority and status.
3. Point out duplicates, stale items, unresolved questions, and obvious checkout candidates.
4. Recommend a small action: checkout, prune, merge, clarify, or keep waiting.

If the active cart has more than `12` items, recommend pruning before adding more.

## Checkout

Checkout turns carted points into committed work. Do not simply dump the cart.

Run this sequence:

1. Select items: use requested IDs, or recommend the highest-value set.
2. Dedupe and merge related items.
3. Resolve conflicts between items; ask only if the conflict changes the outcome.
4. Convert selected items into the requested output.
5. Update each selected item's status.
6. Add a checkout log entry.

Common checkout targets:

- `plan`: ordered work plan with dependencies and acceptance tests
- `TODO`: concrete task list in an existing TODO file
- `issues`: issue titles and bodies
- `patch checklist`: implementation checklist before editing
- `notes`: concise persistent notes or decision record
- `deliverable`: integrate items into the final answer, document, design, or artifact

If no target is specified, default to a compact action plan and ask before editing unrelated project files.

## Prune And Maintain

Keep the cart useful by removing noise.

- Mark an item `done` after it has been acted on.
- Mark an item `committed` when it has been moved into a plan, issue, TODO, or implementation checklist.
- Mark an item `dropped` when the user rejects it or it no longer fits the goal.
- Mark an item `stale` when it may no longer apply.
- Mark an item `question` when it cannot be acted on without a decision.

Never delete items silently. Prefer status changes plus a checkout log entry unless the user explicitly asks for cleanup.

## Interaction Rules

- Keep the active cart small: usually `5` to `12` items.
- Preserve decisions, constraints, risks, and follow-ups; skip vague inspiration unless it affects action.
- Use stable IDs like `IC-001`, `IC-002`, and do not renumber existing items.
- Do not quote long passages from the conversation.
- Do not treat carted items as commitments until checkout.
- Prefer recommendation plus concise rationale over neutral listing.
- When checking out, force prioritization instead of carrying every item forward.

## Default Responses

For add:

```markdown
Carted `IC-003`: Make checkout idempotent.
```

For review:

```markdown
The cart has 6 active items: 2 high priority, 3 medium, 1 question. I would checkout IC-001 and IC-004 now, merge IC-002 with IC-005, and leave IC-006 pending.
```

For checkout:

```markdown
Checked out IC-001 and IC-004 into `docs/todo.md`; marked both `committed` and added a receipt entry.
```
