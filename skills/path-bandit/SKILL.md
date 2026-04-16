---
name: path-bandit
description: Turn brainstorming into a small portfolio of diverse, concrete next paths, then decide what to explore, exploit, park, or drop. Use when the user has a goal, vague ideas, too many options, scattered tactics, or early-stage brainstorming that needs to be narrowed into exact next paths without collapsing too quickly into one obvious answer.
---

# Path Bandit

## Overview

This skill treats brainstorming as raw material, not the final product.

Its job is to decide what to do next, not to execute the work itself. Other tools or skills may execute later.

Start wide enough to surface genuinely different options, then compress into a small path portfolio and make an explicit allocation:

- `Explore`: test a promising path that still has decision-changing uncertainty
- `Exploit`: push the best current path forward
- `Park`: keep a plausible path visible without spending effort on it now
- `Drop`: remove a weak or noisy path from the live set

Do not stop at ideation. Every round must end with a concrete path decision.

## Start Here

Run this sequence:

1. `Goal Lock`
2. `Open Brainstorm`
3. `Diversity Gate`
4. `Path Compression`
5. `Explore vs Exploit Choice`
6. `Commit Move`
7. `Review Trigger`

## Goal Lock

Before discussing tactics, make the target explicit:

- `Goal`: what outcome the user wants
- `Horizon`: by when
- `Success test`: what would count as progress or completion
- `Constraints`: time, money, tools, skills, risk tolerance, dependencies

If the goal is vague, convert it into one operational sentence before choosing paths.

## Open Brainstorm

Let the user think out loud first. Accept fragments, hunches, naive ideas, and half-baked directions.

Collect candidate ideas into a rough map:

- `possible directions`
- `known constraints`
- `useful assets`
- `obvious blockers`
- `assumptions`
- `missing information`

Do not critique too early. The first pass is for surfacing paths, not selecting them.

Separate `stated by user` from `inferred by agent`.

## Diversity Gate

Before compressing the brainstorm, force some real variation.

Try to surface at least 3 distinct path families. A path counts as distinct only if it differs meaningfully on at least one of these dimensions:

- `mechanism`: how it could work
- `asset`: what existing strength or resource it uses
- `evidence source`: what signal would validate it
- `time profile`: faster feedback versus slower but bigger payoff
- `risk profile`: safer versus more contrarian

Useful default families:

- `safe`: straightforward and low-risk
- `asset-leveraged`: uses something the user already has
- `contrarian`: attacks the problem from an unusual angle
- `wildcard`: high-variance but not absurd

Do not keep multiple paths that only differ cosmetically.

## Path Compression

Keep the live set narrow. Default to 3 to 5 candidate paths after the diversity gate.

For each path, capture:

- `Path`: a short exact label
- `Thesis`: what this path is betting on
- `Why distinct`: what makes it materially different from the others
- `First move`: the smallest real next action
- `First artifact`: the concrete output expected from that move
- `Time to first signal`: how quickly the path yields useful evidence
- `Required asset or dependency`: what it needs to start
- `Upside`: why it could win
- `Uncertainty`: what could break it
- `Kill criteria`: what would cause the path to be dropped quickly

Merge duplicate ideas. Cut ornamental variants. If a path has no `First move`, `First artifact`, or `Kill criteria`, it is probably not executable enough.

## Explore vs Exploit Choice

After compressing the brainstorm, classify each surviving path:

- `Explore`: promising, but still missing decision-changing information
- `Exploit`: currently the best path and strong enough to push now
- `Park`: not worthless, but not worth active effort this round
- `Drop`: weak enough to remove from the live set

Do not label all good ideas as `Explore`. The skill should usually produce:

- `1` exploit path
- `1 to 2` explore paths
- the rest parked or dropped

### Choose a path for `Explore` when

- one or two checks could change the recommendation
- a cheap test can eliminate a weak path or validate a strong one
- the decision is sensitive to missing information
- the option value of learning is higher than the value of immediate execution

An explore move does not have to be research-only. It can be a bounded prototype, thin slice, draft, simulation, outreach, or other information-bearing action.

### Choose a path for `Exploit` when

- one path already dominates on expected value and evidence
- the cost of waiting is meaningful
- the main unknowns are no longer decision-changing
- execution itself is the fastest way to learn

### Choose `Stop or Reframe` when

- the goal is underspecified or internally inconsistent
- every current path is weak, blocked, or too expensive
- the user is optimizing a tactic without a credible objective
- the problem should be decomposed into a smaller or different target

## Default Heuristics

Use rough labels such as `low`, `medium`, and `high`. Precision is less important than disciplined comparison.

For each path, assess:

- `Expected value`
- `Evidence strength`
- `Learning value`
- `Execution cost`
- `Reversibility`

Bias toward `Explore` when learning value is high and tests are cheap.

Bias toward `Exploit` when expected value is high, evidence is at least moderate, and delay is costly.

Bias toward `Park` when the path is plausible but weaker than the lead path.

Bias toward `Drop` when the path set is getting noisy and the extra option is not worth attention.

Bias toward `Stop or Reframe` when the path set is weak enough that choosing among them is fake precision.

## Commit Move

After choosing the path allocation, convert it into a bounded move.

For each `Explore` path, define:

- the exact question being tested
- the smallest test that answers it
- the threshold that would promote it, keep it parked, or kill it

For the `Exploit` path, define:

- the lead path
- the next 1 to 3 actions
- the immediate output expected from those actions

If choosing `Stop or Reframe`, define:

- what is being abandoned or deferred
- the new framing or smaller target
- what will be tried next instead

## Review Trigger

Every round must specify when to re-evaluate. Good triggers:

- a key assumption fails
- a predefined threshold is met
- a fixed amount of time or effort is spent
- a path produces an observable result

Do not keep exploring without a stopping condition.
Do not keep exploiting after the path has clearly stalled.
Do not keep brainstorming after the path set is already good enough to choose.

## Interaction Rules

- Treat brainstorming as a useful phase, but not an excuse for option sprawl.
- Ask at most 1 to 3 high-value questions per turn unless the user wants a full diagnostic.
- Prefer recommendation plus rationale over neutral enumeration.
- Name parked alternatives, but do not keep revisiting them unless new evidence appears.
- Keep output compact and decision-oriented.
- If the user asks for brainstorming, still end with an explicit path allocation.
- If the user resists narrowing, show the tradeoff explicitly: `more optionality now` versus `faster progress now`.

## Default Output Shape

End each round with this structure:

- `Goal`
- `Candidate paths`
- `Exploit path`
- `Explore paths`
- `Parked or dropped paths`
- `Why this allocation wins now`
- `Next move`
- `Promotion or kill criteria`
- `Review trigger`

## Tone

Be direct, pragmatic, and slightly skeptical of unfocused ideation. The skill exists to convert brainstorming into a diverse but executable set of next paths.
