# Operationalization Questions

Use this reference when the task is still too broad, abstract, or under-constrained for a good strategy loop. The purpose is not to ask more questions for their own sake. The purpose is to ask the smallest set of questions that changes what should be tried, how it should be judged, or when it should stop.

These questions are meant to improve many task classes, not one domain. Use them before branching, before launching workers, or after a weak round that produced vague work.

## Core Rule

Prefer questions that reduce decision ambiguity.

Avoid questions that are merely descriptive, interesting, or nice to know unless the answer changes:

- path selection
- success criteria
- validation method
- risk handling
- stopping rules

## Universal Questions

Ask only the highest-value subset.

### 1. Target

- What concrete outcome should be better at the end of this loop?
- What decision will this work support or unlock?
- What would count as "good enough" rather than perfect?

### 2. Evaluator

- Who or what will judge success: a test suite, benchmark, human reviewer, user behavior, external holdout, or operational metric?
- What is the primary score, and what secondary signals matter enough to override it?
- What result would be impressive but misleading?

### 3. Unit Of Work

- What is the smallest end-to-end unit that can produce evidence?
- What artifact should each branch return: patch, report, benchmark delta, reproduction, design draft, ranking, or recommendation?
- What is the cheapest credible test for one branch?

### 4. Controllable Levers

- What can actually be changed in this loop: prompts, parameters, code paths, workflow steps, data slices, thresholds, or task decomposition?
- Which levers are cheap to vary and which are expensive?
- Which changes are reversible and which create lock-in?

If the domain has specialized practices, standard baselines, or common traps, read [domain-practice-elicitation.md](domain-practice-elicitation.md) before finalizing the first branches.

### 5. Invariants And Constraints

- What must not regress?
- What interfaces, assumptions, or deliverables are fixed?
- What limits matter most: time, compute, risk, latency, complexity, cost, or human attention?

### 6. Failure Surface

- What are the likely ways a branch can look good while being wrong?
- What evidence would falsify the current favorite quickly?
- What common failure should be checked before spending more budget?

### 7. Promotion And Kill Rules

- What evidence promotes a branch?
- What evidence parks it?
- What evidence kills it immediately?
- What level of uncertainty is acceptable for the next decision?

### 8. Stopping Rule

- When should the loop stop even if more improvement is possible?
- What would indicate diminishing returns?
- What result is strong enough to switch from searching to packaging, adoption, or delivery?

## Task-Class Adapters

Choose the smallest relevant adapter and combine it with the universal questions.

### Build Or Implementation Tasks

- What exact behavior must exist at the end?
- What invariants or interfaces must stay stable?
- What is the smallest vertical slice that proves the path works?
- What test, demo, or observable behavior would confirm completion?

### Debug Or Diagnosis Tasks

- What is the observed behavior versus the expected behavior?
- Is there a minimal reproduction?
- What changed recently or what hypotheses explain the failure?
- What is the fastest discriminating check that would eliminate one major cause?

### Search Or Optimization Tasks

- What is the incumbent baseline?
- What is the cheap evaluation tier versus the confirmation tier?
- Which parts of the search space deserve broad coverage first?
- What evidence distinguishes a stable region from a lucky point?

For these tasks, also read [staged-search.md](staged-search.md).

### Research Or Analysis Tasks

- What exact claim, estimate, or decision is needed?
- What evidence sources are admissible?
- What would disconfirm the current interpretation?
- What deliverable shape is actually useful: memo, table, summary, model comparison, or recommendation?

### Review Or Audit Tasks

- What risk classes matter most?
- What severity threshold is worth surfacing?
- What proof is needed for a finding?
- Is the task read-only diagnosis or should it propose repairs too?

### Comparative Choice Tasks

- What are the candidate options being compared?
- Which dimensions truly decide the choice?
- Which differences are cosmetic rather than decision-relevant?
- What cheap check could eliminate one option quickly?

## Output Shape

End an operationalization pass with:

- `Decision to support`
- `Primary evaluator`
- `Key constraints and invariants`
- `Controllable levers`
- `Smallest evidence-bearing unit`
- `Promotion, park, and kill rules`
- `Stopping rule`
- `Open questions worth asking now`

## Prompting Rule

When using these questions in a live prompt:

- ask at most 3 to 7 questions unless the user explicitly wants a deeper intake
- prefer questions that force thresholds, artifacts, or tradeoffs
- offer provisional assumptions when waiting for answers would stall useful work
- do not let the conversation remain at the level of goals, themes, or hopes
