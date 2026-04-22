---
name: strategy-loop
description: Run evidence-driven multi-round strategy refinement with complementary agents and a persistent strategy ledger. Use when a user wants Codex to compare competing approaches over repeated rounds, assign roles such as explorer, critic, and validator, update priorities from real evidence, and decide what to exploit, mutate, park, or kill.
---

# Strategy Loop

## Overview

This skill runs an iterative manager loop over a live strategy portfolio. Use it after there are already candidate strategies, or when the user explicitly wants multi-agent orchestration, cross-round memory, and evidence-based updating instead of a one-shot brainstorming decision.

If the problem is still loose and needs initial path generation, use `path-bandit` first. If the work needs persistent external child CLI sessions, hand off execution to `team-leader` after this skill defines the portfolio, roles, and round plan.

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

1. `Lock the state`
2. `Seed or import the portfolio`
3. `Define the round`
4. `Assign complementary roles`
5. `Run propose -> attack -> repair -> validate`
6. `Update the ledger`
7. `Reallocate budget`
8. `Stop, continue, or reframe`

## 1. Lock The State

Capture these before dispatching work:

- `Goal`
- `Success metric`
- `Constraints`
- `Budget`
- `Current artifacts`
- `Known failures`
- `Holdout or external test source`
- `Open questions`

If any of `Goal`, `Success metric`, or `Validation source` is missing, state the gap explicitly before sending agents or sessions to work.

## 2. Seed Or Import The Portfolio

Start with `2` to `5` candidate strategies. If the user already has them, normalize their labels and theses. If not, derive them from the current work or hand off to `path-bandit` to build the first portfolio.

For each strategy, capture:

- `Strategy id`
- `Thesis`
- `Status`: `live`, `parked`, `killed`, or `validated`
- `Parent`: blank for originals, or the source strategy when mutated
- `First test`
- `Expected upside`
- `Main uncertainty`
- `Kill criteria`

Use [references/ledger-schema.md](references/ledger-schema.md) for the canonical fields and update rules.

## 3. Define The Round

Set the allocation before launching work. Default split:

- `70% exploit`: push the best evidence-backed path
- `20% mutate`: repair or extend a promising path
- `10% explore weird`: test a distinct alternative with upside

Change the split only when evidence justifies it. Do not spend all effort on novelty, and do not freeze on the current leader while decision-changing uncertainty is still high.

## 4. Assign Complementary Roles

Use separate agents or sessions only when the user explicitly wants delegation or multi-agent work and the environment supports it. Do not launch redundant workers.

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

## 5. Run Propose -> Attack -> Repair -> Validate

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

## 6. Update The Ledger

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

## 7. Reallocate Budget

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

## 8. Stop, Continue, Or Reframe

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
