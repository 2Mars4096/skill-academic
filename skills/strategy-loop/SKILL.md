---
name: strategy-loop
description: Run context-specific, evidence-driven strategy refinement over repeated rounds with a persistent ledger. Use when a user wants Codex to route a messy project into focused questions, compare competing approaches, update priorities from real evidence, and decide what to exploit, mutate, explore, park, or kill.
---

# Strategy Loop

## Overview

This skill runs an iterative manager loop over a live strategy portfolio. Use it after there are already candidate strategies, or when the user explicitly wants cross-round memory, context-specific questioning, and evidence-based updating instead of a one-shot brainstorming decision.

If the problem is still loose and needs initial path generation, use `path-bandit` first. If the work needs persistent external child CLI sessions, hand off execution to `team-leader` after this skill defines the portfolio, roles, and round plan.

For search-heavy work such as tuning, model or prompt selection, benchmark optimization, or workflow configuration search, keep the portfolio view but switch the round mechanics to staged search. Read [references/staged-search.md](references/staged-search.md) before defining the round.

If the task is broad, underspecified, or likely to produce vague branches, read [references/operationalization-questions.md](references/operationalization-questions.md) before seeding the portfolio. Use it to tighten the problem into testable paths, better prompts, and cleaner promotion rules across domains.

If the task likely has field-specific practices, standard baselines, common traps, or expert diagnostics, read [references/domain-practice-elicitation.md](references/domain-practice-elicitation.md) before seeding the portfolio. Run its tiered practice funnel to narrow from task class -> representation contract -> standard baselines -> practical moves -> natural integration roles. Use the result as candidates to test, not as facts to trust blindly.

## When To Use

- managing `2` or more candidate strategies over repeated rounds
- assigning complementary roles such as `Explorer`, `Critic`, `Validator`, and `Synthesizer`
- keeping a ledger of strategies, evidence, failures, costs, and open questions
- deciding whether to exploit the leader, mutate a promising path, test a weird alternative, or kill a weak path
- learning which prompts, role pairings, and validation patterns are actually working

## When Not To Use

- the user only needs initial brainstorming or a single next-path decision
- there is only one obvious plan and no meaningful alternative portfolio
- the work does not benefit from explicit validation or cross-round memory
- the user wants child CLI/session management itself rather than the strategy policy; use `team-leader` for that controller layer

## Start Here

Run this sequence:

1. `Run the context funnel`
2. `Lock the state`
3. `Run the practice funnel when triggered`
4. `Seed or import the portfolio`
5. `Define the round`
6. `Assign complementary roles`
7. `Run propose -> attack -> repair -> validate`
8. `Update the ledger`
9. `Reallocate budget`
10. `Stop, continue, or reframe`

## 1. Run The Context Funnel

Before asking detailed questions or assigning work, route the project into a narrower question family. The first questions should decide which future questions are worth asking.

Capture:

- `Project type`: academic proposal, empirical paper, literature review, codebase, agent workflow, product/tool, writing/deck, or other
- `Decision object`: research question, data strategy, identification design, architecture, validation plan, role allocation, next work batch, or another concrete choice
- `Stage`: early ideation, competing paths, one lead path with uncertainty, stalled execution, failed validation, or post-result refinement
- `Context anchors`: files, notes, drafts, datasets, tests, prior runs, dashboards, user/advisor feedback, or failure logs
- `Discriminating evidence`: what could actually separate the strategies
- `Expensive next choice`: the next decision where being wrong would waste meaningful time, money, credibility, or work

Question rule:

- Ask `0` to `3` routing questions only when missing answers would change the next question family.
- Prefer inspecting available context over asking the user to restate it.
- Once routed, stop asking generic strategy questions and ask only context-specific questions tied to the decision object.
- If the user is still brainstorming possible paths, use `path-bandit` first and return here after a small candidate portfolio exists.

Read [references/context-question-router.md](references/context-question-router.md) when the skill needs context-specific question packs.

## 2. Lock The State

Capture these before dispatching work:

- `Goal`
- `Success metric`
- `Project type`
- `Decision object`
- `Stage`
- `Constraints`
- `Budget`
- `Current artifacts`
- `Known failures`
- `Holdout or external test source`
- `Expensive next choice`
- `Open questions`

If any of `Goal`, `Success metric`, or `Validation source` is missing, state the gap explicitly before sending agents or sessions to work.

If these fields exist but are still too broad to drive good branching, run a short operationalization pass before moving on. Ask only the questions that would materially change path choice, validation design, or stopping rules.

If domain knowledge could materially change the first paths, run a short domain-practice elicitation pass before seeding strategies. For benchmark, tuning, modeling, domain-heavy, or specialized-workflow tasks, this pass is mandatory but bounded. Do not launch broad sweeps or child workers until the loop has named the representation assumption it is using.

## 3. Run The Practice Funnel When Triggered

Use [references/domain-practice-elicitation.md](references/domain-practice-elicitation.md) when triggered. Ask the tiered questions in order and stop once they produce enough testable practice candidates.

Minimum output:

- representation contract: comparable objects, raw similarity assumption, allowed status/regime signals, and invalid shortcuts
- standard baseline or incumbent
- practical moves worth testing
- natural role for each move
- smallest credible test
- common trap or misleading signal to guard against

## 4. Seed Or Import The Portfolio

Start with `2` to `5` candidate strategies. If the user already has them, normalize their labels and theses. If not, derive them from the current work or hand off to `path-bandit` to build the first portfolio.

For each strategy, capture:

- `Strategy id`
- `Thesis`
- `Status`: `live`, `parked`, `killed`, or `validated`
- `Parent`: blank for originals, or the source strategy when mutated
- `Natural role`: `standalone`, `input_or_feature`, `prior_or_constraint`, `gate_or_router`, `blend_or_fallback`, `postprocess`, or `diagnostic`
- `First test`
- `Expected upside`
- `Main uncertainty`
- `Kill criteria`

Use [references/ledger-schema.md](references/ledger-schema.md) for the canonical fields and update rules.

When a strategy comes from domain-practice elicitation, mark whether it is `expert prior`, `standard baseline`, `common trap check`, or `needs external verification`. Do not kill a practice-derived idea only because it failed in a role it was not meant to play; first test its natural role or record why that role is too costly or invalid.

## 5. Define The Round

Set the allocation before launching work. Default split:

- `70% exploit`: push the best evidence-backed path
- `20% mutate`: repair or extend a promising path
- `10% explore weird`: test a distinct alternative with upside

Change the split only when evidence justifies it. Do not spend all effort on novelty, and do not freeze on the current leader while decision-changing uncertainty is still high.

For search-heavy tasks, define the evaluation tier for the round up front: cheap screen, local refinement, or full confirmation. Do not mix broad exploration and expensive confirmation in the same round unless there is a clear reason.

For data/modeling/benchmark searches, a round is underspecified if it cannot state what objects are comparable, what distance or similarity means, and what observable evidence would falsify that representation.

When live strategies differ mainly by configuration, thresholds, prompts, or tuning choices, do not run an unstructured sweep. Use staged search: broad first-pass coverage, explicit promotion criteria, local refinement around stable regions, and a harder confirmation pass before adoption.

## 6. Assign Complementary Roles

Use separate agents or sessions only when the user explicitly wants delegation or multi-agent work and the environment supports it. Do not launch redundant workers.

When delegating domain-heavy search work, assign a concrete representation assumption, owned artifact, role-of-idea test, or falsification check. Avoid vague prompts such as "explore features" or "try more configs."

Default roles:

- `Explorer`: propose stronger variants, combinations, and orthogonal alternatives
- `Critic`: attack assumptions, define failure modes, and push for falsification
- `Validator`: run the cheapest credible test or holdout check
- `Synthesizer`: integrate the round results only when aggregation would otherwise become noisy

Minimum viable round:

- one novelty-pushing role
- one rigor-pushing role

Do not let the same role both claim success and define the only success test.

Read [references/prompt-patterns.md](references/prompt-patterns.md) when you need concrete role templates.

If the early prompts keep producing generic or ornamental work, read [references/operationalization-questions.md](references/operationalization-questions.md) and tighten the inputs before launching another round.

If the prompts ignore field practice or reinvent obvious baselines, read [references/domain-practice-elicitation.md](references/domain-practice-elicitation.md) and add a domain-practice pass before the next round.

## 7. Run Propose -> Attack -> Repair -> Validate

Every active round should produce evidence-bearing artifacts, not just better wording.

Default sequence:

1. `Explorer` proposes a stronger or more distinct path.
2. `Critic` attacks it with concrete failure modes, missing assumptions, and cheap falsification checks.
3. `Explorer` repairs only the parts that survive critique.
4. `Validator` checks the repaired path against a holdout, benchmark, test, or observable signal.

Acceptable evidence:

- test results
- benchmark deltas
- reproducible outputs
- explicit user approval
- uncertainty reduction from a falsification check
- measured cost or latency improvement

Unacceptable evidence:

- persuasive prose without a check
- self-grading by the proposing agent
- success criteria invented after the result is known

## 8. Update The Ledger

After every round, update:

- strategy status
- evidence gained
- average reward
- confidence
- novelty
- cost
- risk
- failure reason
- prompt or orchestration lessons
- next action recommendation

Keep stable strategy IDs across rounds. New variants get new IDs plus a parent pointer.

Use `scripts/score_strategies.py` when you want deterministic ranking from a JSON or YAML ledger.

## 9. Reallocate Budget

Use the live leaderboard to choose the next move.

Default ranking formula:

`priority = average_reward + exploration_bonus - cost_penalty - risk_penalty`

Where:

- `average_reward` reflects real outcomes, not narrative quality
- `exploration_bonus` should be higher for novel, low-confidence paths with upside
- `cost_penalty` rises with execution burden
- `risk_penalty` rises when failure would be expensive or misleading

Default action policy:

- `Exploit` the current leader when it dominates on evidence and delay is costly
- `Mutate` a promising path when critique found specific, repairable weaknesses
- `Explore` a weird alternative when its option value is still high
- `Park` a plausible path when it is not leading but still worth remembering
- `Kill` a path when its predefined kill criteria are met or repeated evidence goes against it

Do not reward verbosity. Reward measured progress, validated robustness, and cheaper learning.

## 10. Stop, Continue, Or Reframe

Stop the loop when:

- the lead strategy is validated strongly enough for the current goal
- marginal gains are small for `2` rounds in a row
- the remaining live paths are not worth their test cost

Reframe when:

- all surviving paths share the same broken assumption
- the evaluation target was underspecified
- the portfolio collapsed into cosmetic variants of one bad idea

## Output Shape

End each round with:

- `Goal and current state`
- `Context lens`: project type, decision object, stage, expensive next choice
- `Practice inventory`: only when the practice funnel was triggered; include baselines, practical moves, natural roles, and traps
- `Representation contract`: only for data/modeling/benchmark tasks; include comparable objects, similarity assumptions, and invalid shortcuts
- `Active strategies`
- `This round's role allocation`
- `Evidence gained`
- `Updated leaderboard`
- `Exploit / mutate / explore / park / kill decision`
- `Next round plan`
- `Stop or review trigger`

## Guardrails

- Keep the portfolio narrow enough to compare honestly. Default to `2` to `5` live strategies.
- Separate novelty generation from rigor checks.
- Prefer external checks, holdouts, or fixed validation criteria.
- Store failure memory so weak assumptions and bad prompt patterns are not retried blindly.
- Tighten exploration when the option value of learning drops.
- Update selection weights, prompt templates, priors, and dispatch rules before considering heavier interventions.
- For search-heavy tasks, promote regions or families that show repeatable signal, not isolated lucky winners.
- Prefer stable plateaus over knife-edge optima when the top score difference is small.
- Freeze promotion rules and validation tiers before looking at results whenever practical.
