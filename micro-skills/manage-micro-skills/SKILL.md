---
name: manage-micro-skills
description: Manage the user's micro-skill collection during ongoing work. Use when asked which rules apply, to try or skip a rule once, or to remember, edit, activate, pause, or retire a preference.
---

# Manage micro-skills

Start from the [task map](../README.md). When invoked through an installed link, resolve this SKILL.md to its real path first. The map and its linked files are the source of truth.

**Which rules apply?** Identify the current subtask. Read the relevant category and task, checking each entry’s status, trigger, exclusions, and context independently. Apply matching active rules. If asked, name them and explain the match briefly. If there are only drafts, identify the closest draft and offer a one-run trial. Refresh the selection when the work changes.

**“This time” or “for this chat.”** Apply the instruction for the stated duration. An explicit trial can use a draft. A one-off correction belongs in the current output. Leave its saved rule alone unless the user asks for a standing change.

**“Remember this” or “from now on.”** Update the narrowest matching rule and apply the correction to work in progress. Use a category for preferences shared across its tasks. For a conditional exception, record the context, the exact rule it overrides, and the changed behavior. The current request wins. Ask a focused question if an unresolved conflict would change the output.

**Learn from a correction.** Treat “no,” “you should,” “I meant,” and similar replies as priority evidence. Read the preceding request and the response being rejected before assigning the correction to a task. Identify the unwanted behavior, requested replacement, and scope. Check later replies for a reversal or narrower instruction. Use the person’s correction as evidence, and keep assistant suggestions distinct. If prior context is unavailable, record the uncertainty. Generalize the rule without retaining project details. Persist it when the user asks to update the collection or states a standing preference.

**Add or change a skill.** Read the latest file before editing. Fix the trigger for a missed or unwanted activation, and fix the instruction or check for an incorrect result. Create a new entry only for a distinct purpose. Follow a sibling’s format and update the map and affected links when adding, moving, or renaming an entry.

**Manage status.** Store the decision in `metadata.status`. New proposals start as `draft`. A standing instruction or explicit activation makes the relevant rule `active`. If a new standing instruction would also activate unrelated draft preferences, give it its own active entry. Pause or retire a named entry by setting `paused` or `retired` and retaining its text. “Skip this once” expires after that use.

**Check and continue.** Re-read a saved change, check its scope against one matching and one nearby excluded request, and verify affected links. Tell the user which rule changed and whether the change is temporary or saved. Then continue the original task when applicable.
