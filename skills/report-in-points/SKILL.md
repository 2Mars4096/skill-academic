---
name: report-in-points
description: Turn meeting transcripts, scattered comments, and multi-part feedback into a grouped point-by-point completion report. Use when addressing feedback or reviewing what changed and what remains, with minimally overlapping topic bullets, detailed task sub-bullets, and coverage of every substantive request.
---

# Report in Points

Make it easy for the user to check whether their original feedback has been addressed without reconstructing the work from a diff or conversation history. Report in two levels: topic bullets and concrete task sub-bullets. Organize by subject or intended outcome, not by chronology, speaker, file, or completion status.

## Optional technical / STE writing mode

Use the normal report style by default. Activate the optional mode only when the user explicitly asks for it, for example “write technically,” “use STE,” “use Simplified Technical English,” or “follow ASD-STE100.” Technical subject matter, an incidental mention or quotation of STE, and invoking this skill alone do not activate it.

When activated, read [references/ste-writing.md](references/ste-writing.md) and apply its guidance to the requested report or passage. Preserve the topic/sub-point structure, status distinctions, evidence, and coverage requirements. Keep the mode scoped to that deliverable and its revisions unless the user explicitly asks for a broader scope; do not make it a permanent preference. A request for the normal style ends the mode.

## Establish the requests

- Read the supplied transcript, comments, and relevant follow-up instructions. Extract distinct requests, constraints, questions needing answers, and decisions affecting the work. Split compound comments when their parts can have different outcomes.
- Separate actionable feedback from background discussion and tentative suggestions. Do not silently convert brainstorming into approved work. Preserve meaningful ambiguities, conflicting requests, and explicit deferrals.
- Merge repeated requests while preserving distinct conditions and exceptions. Keep lightweight source anchors such as comment numbers, speaker plus timestamp, or a short identifying phrase; do not invent timestamps or quotations.
- Maintain a working mapping from each substantive source point to its task and final disposition. For a small request this can stay in working context; for long or multi-session work, use the project's existing task notes when appropriate. Do not create a separate tracking system by default.

## Group without losing coverage

- Choose first-tier sections with clear, distinct responsibilities. Prefer subjects or deliverables the user recognizes, such as “Sample definition,” “Analysis,” and “Presentation.” Use as many sections as the material needs, without forcing a fixed count.
- Give each task one primary home. If it affects another section, briefly cross-reference it instead of duplicating the task or counting it twice.
- Make section boundaries as mutually exclusive as practical while keeping the sections and their sub-points collectively comprehensive. Do not omit a request merely because it does not fit the initial grouping; revise the grouping.
- Keep the structure and task identifiers stable across follow-ups where useful, so the user can see which items changed status. Distinguish work newly completed in this update from work completed earlier when reporting incremental progress.

## Address or assess the work

Follow the user's requested scope. If asked to implement feedback, carry out the authorized work and track its results. If asked only to organize or report, assess the available evidence and report without making unrelated changes.

For each task, record the actual outcome and enough evidence to support it: the relevant passage, artifact location, diff, check result, or answer. A to-do entry or an intention to change something is not evidence that it was done. Distinguish implementation from validation; if an edit is complete but its effect is unverified, say so. If completion depends on validation that has not happened, keep the task partial.

Use plain status labels:

- **Done**: The requested outcome is supported by available evidence. State what changed or what answer was established.
- **Partial**: Some of the request is addressed. State both the completed portion and the exact remainder.
- **Not done**: No work was completed on this request. State the remaining action.
- **Blocked / Needs clarification**: Identify the missing input, dependency, or unresolved conflict and the specific decision needed.
- **Deferred**: State why it was postponed and by whom, if known. Do not imply user agreement without evidence.
- **No change needed**: Explain how the existing state already satisfies the request, with a review anchor.
- **Not adopted / Superseded**: Preserve the request and explain the reason or the later decision replacing it.
- **Unverified**: The supplied material does not establish whether the work was completed. Do not present missing evidence as proof that nothing was done.

Use only the labels needed. Mixed outcomes belong on separate task sub-points or must be explicitly described as partial; never label a whole section done while hiding unfinished tasks beneath it.

## Write the report

Default to nested Markdown bullets, with bold first-tier topic labels and second-tier task bullets. Avoid a separate essay, a flat checklist, or a file-by-file change log. Lead each task with its status and recognizable request, then state the result and any remaining work. Add a concise source anchor when it helps match the original feedback and a precise review link when available. Prefer direct file/section links over long lists of implementation details.

Use this shape, adapting the number of sections and tasks:

- **[Topic or deliverable]**
  - **Done — [Request].** [Concrete change or answer and its significance.] Review: [artifact/section link]. [Source anchor if useful.]
  - **Partial — [Request].** [Completed portion.] Remaining: [specific unfinished portion and reason].
- **[Another distinct topic]**
  - **No change needed — [Request].** [Evidence that the existing state satisfies it.] Review: [location].
  - **Needs clarification — [Request].** [Conflict or ambiguity and the decision required].

Keep unfinished work under its subject so the user can review that subject in one place. Use a third bullet level only when a task genuinely needs separate independently reviewable parts. Do not compress distinct requests into vague claims such as “addressed the comments” or “improved clarity.” Keep detail proportional to what the user needs to verify the result.

Before delivering, compare the report with the original material: every substantive request must have a disposition, every completion claim must have support, and no task should be duplicated across sections. Account for unresolved questions, rejected suggestions, and unchanged items as well as completed edits. Exclude irrelevant conversation and repeated wording, not meaningful requirements.
