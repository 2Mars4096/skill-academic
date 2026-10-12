---
name: decision-triage
description: Assess tasks and decisions by ambiguity and risk, choose whether to execute, explore, validate, or seek a human decision, and organize a backlog into prioritized next actions. Use when the user asks how to handle uncertain work, decide appropriate AI autonomy, triage tasks, or sort to-dos. Routine execution of an already clear task does not need a separate triage exercise.
---

# Decision Triage

Turn uncertain work into concrete next actions, with AI autonomy proportional to ambiguity and risk. Keep the process lightweight: a short rationale for a consequential choice is more useful than elaborate scoring for ordinary work.

## Assess the decision

Identify the intended outcome, available evidence, existing authorization, and the actual next action. Inspect relevant context before asking the user for information already available. When organizing a backlog, use the supplied list or established project task source; ask which backlog if the source cannot be inferred. Do not inventory unrelated projects or accounts.

Assess two dimensions separately:

- **Ambiguity:** How clearly do the goal, evidence, constraints, and success criteria determine the action? Low means the action and acceptance criteria are clear. High means plausible interpretations or options would materially change the outcome. Distinguish a missing fact that can be inspected from a preference or tradeoff only the user can settle.
- **Risk:** What happens if this specific action is wrong? Consider magnitude, affected people or systems, reversibility, recovery cost, privacy, and external commitments. Ground the assessment in concrete consequences; do not inflate risk from hypothetical possibilities or the topic label alone.

Use low/high as practical categories, not precise measurements. For borderline cases, name the uncertainty and take a small bounded step that resolves it. Model confidence alone does not establish clarity or safety.

Split tasks when their steps have different consequences. Drafting a migration plan, testing on a copy, and changing live data need separate assessments. A risky eventual commitment does not prevent useful preparation.

## Choose the working mode

| Ambiguity | Risk | Mode | Next action |
|---|---|---|---|
| Low | Low | Execute | Complete authorized work and perform proportionate verification. |
| High | Low | Explore | State a reasonable assumption and create a bounded draft, probe, or experiment; use the result to refine the task. |
| Low | High | Control | Check prerequisites, use applicable safeguards, and verify results. Execute within established authorization and limits; escalate exceptions. |
| High | High | Clarify and recommend | Gather evidence, compare concrete options and consequences, recommend a choice, and leave unresolved consequential tradeoffs to the human decision-maker. |

These are working modes, not permission grants. Preserve the user's scope, prior authorization, and applicable tool or environment requirements. Low risk does not authorize unrelated work. High risk does not automatically require another confirmation when the exact action and relevant tradeoffs are already authorized.

Ask a question only when its answer would materially change the next action and cannot reasonably be established from context or a safe probe. Ask the smallest useful question, give a recommendation when possible, and continue independent authorized work while awaiting the answer. Never treat silence as approval.

Before requesting a consequential decision or required approval, complete the authorized preparation so the user can review an actual draft, diff, plan, or options comparison. State exactly what remains undecided and why. Avoid vague requests such as “Please confirm everything.”

For exploration, define the smallest useful artifact and a stopping condition. For controlled execution, choose checks and recovery measures appropriate to the actual consequence. Do not append a generic safety checklist to every task.

## Organize to-dos

When asked to sort tasks:

1. Extract and deduplicate commitments without dropping substantive requirements. Preserve established task IDs and distinguish confirmed commitments from suggestions.
2. Rewrite vague items as an action with an observable outcome. Split out missing decisions or dependencies only when they change what can be done next.
3. Determine priority from importance, real deadlines, dependencies, and effort. Keep priority separate from ambiguity and risk; an easy low-risk task must not displace urgent consequential work merely because it is easier to execute. Do not invent deadlines or numerical scores.
4. Assign each actionable step a working mode and identify who owns any unresolved decision. Separate execution ownership from decision ownership where needed.
5. Identify a completion criterion and the next action that changes the task's state.

Use the smallest readable presentation. For a substantial backlog, a useful table is:

| Task / outcome | Priority and reason | Ambiguity / risk | Next action and mode | Decision owner, if needed | Done when |
|---|---|---|---|---|---|

Group items when it helps scanning:

- **Ready to execute:** The next authorized action is clear; include any necessary controls.
- **Needs exploration:** A bounded investigation or draft can reduce ambiguity.
- **Needs your decision:** Name the specific unresolved choice and provide the prepared recommendation.
- **Blocked by a dependency:** Name the dependency and the action that would unblock it; do available preparation first.

Keep the full backlog visible even when recommending only a few immediate actions. Distinguish deferred items from blocked items and completed work. Sorting a backlog does not authorize executing every item in it. If execution was also requested, proceed with the authorized next steps.

Update an established task file when requested or already within scope; otherwise present the triage in the conversation. Avoid creating a second task tracker or additional artifacts without a concrete need.

## Reassess from outcomes

After a material discovery, failed check, scope change, or transition from draft to external action, reassess the affected step. Record the changed evidence and next action in the existing task record when one is in use. Do not continually reclassify unchanged tasks or silently expand authorization based on previous success.

Examples:

- “Explore a new paper direction” usually calls for a bounded question-and-data feasibility note. Committing months of work to the direction is a separate human decision.
- “Remove duplicate records” may require inspection to define duplicates, a reversible candidate transformation, then a separately assessed overwrite if requested.
- “Publish the announcement” requires assessing publication itself. A clear, previously authorized final message does not need repeated approval merely because it is public; uncertain claims or an unresolved audience may require clarification before publication.

## Basis

Adapted from MIT CISR's [Designing Decision Rights for AI](https://cisr.mit.edu/publication/2026_0601_AIDecisionMatrix_SebastianWeillHaskampVomBrocke) (June 18, 2026). Its categories are routine, consequential, exploratory, and strategic, with corresponding approaches automate, manage, enable, and lead. It also distinguishes framing, acting, and learning. The operational modes and backlog workflow above are this skill's adaptation, not MIT's prescribed implementation.
