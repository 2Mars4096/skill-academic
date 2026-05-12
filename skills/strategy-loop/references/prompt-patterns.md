# Prompt Patterns

Use these templates when the default `Strategy Loop` guidance is too abstract and a round needs explicit role prompts. Keep prompts short, bounded, and artifact-oriented.

## Shared Inputs

Every role prompt should include:

- `Goal`
- `Success metric`
- `Project type`
- `Decision object`
- `Stage`
- `Context anchors`
- `Current strategies`
- `Owned strategy ids`
- `Budget or time cap`
- `Validation source`
- `Known failures`
- `Expensive next choice`
- `Required output format`

For search-heavy tasks, also include:

- `Search stage`: broad screen, local refinement, or full confirmation
- `Search space or region under test`
- `Baseline`
- `Promotion rule`
- `Kill rule`
- `Evaluation tier`

When the task is still underspecified, tighten it first with [operationalization-questions.md](operationalization-questions.md) instead of launching vague role prompts.

When domain practice could matter, add a short pass from [domain-practice-elicitation.md](domain-practice-elicitation.md) before proposing branches.

## Context Router Template

```text
You are routing a strategy loop into project-specific questions.

Known context:
- Goal: <goal or unknown>
- Project type: <academic, codebase, agent workflow, product/tool, writing/deck, or unknown>
- Decision object: <what choice this round should resolve>
- Stage: <ideation, competing paths, one lead with uncertainty, stalled, failed validation, post-result>
- Available artifacts: <files, notes, tests, datasets, drafts, prior runs, feedback>
- Known failures: <failures or unknown>

Return:
- inferred project type
- inferred decision object
- context anchors to inspect
- validation source candidates
- the next 1 to 3 questions, only if their answers would change the strategy portfolio
```

## Operationalization Template

```text
Your job is not to solve the task yet. Your job is to tighten it into a form that supports honest branching and validation.

Goal: <goal>
Current context: <brief context>
Known constraints: <constraints>
Current ambiguity: <what still feels broad or underspecified>

Ask only the smallest set of questions that would change:
- which paths should exist
- how success should be measured
- what each branch should return
- what evidence should promote, park, or kill a branch
- when the loop should stop

Return:
- 3 to 7 high-value questions
- why each question is decision-relevant
- provisional assumptions if no answer arrives
- the smallest evidence-bearing unit of work
- the validation source or missing validator
```

## Domain Practice Elicitation Template

```text
Your job is to surface domain practice that could change the strategy portfolio. Do not solve the task yet.

Task: <task>
Domain or suspected field: <domain>
Goal and success metric: <goal and metric>
Known constraints: <constraints>
Current baseline or incumbent: <baseline if known>

Identify:
- what experienced practitioners usually check first
- standard baselines or simple methods that are often hard to beat
- common practices, heuristics, diagnostics, or parameter regimes worth testing
- common mistakes that produce false progress
- field-specific invariants, constraints, or risk checks
- which claims are uncertain and need external verification

Return:
- expert priors worth testing
- standard baselines to include
- cheap diagnostic checks
- domain-informed candidate branches
- common traps and misleading signals
- promotion and kill criteria for each branch
- items that should be verified from sources or experiments
```

## Manager Kickoff Template

```text
You are managing a strategy portfolio, not writing a one-shot answer.

Goal: <goal>
Success metric: <metric>
Project type: <project type>
Decision object: <decision object>
Stage: <stage>
Context anchors: <artifacts and prior failures>
Budget: <budget>
Validation source: <holdout, benchmark, or external check>
Expensive next choice: <choice where being wrong is costly>
Current strategies:
<strategy list with ids, theses, and statuses>

For this round:
- choose one exploit path
- choose up to two mutate or explore paths
- assign complementary roles
- define kill or promotion criteria before work starts

Return:
- round allocation
- role assignments
- exact questions being tested
- expected artifacts
- review trigger
```

## Explorer Template

```text
Role: Explorer
Owned strategy ids: <ids>

Goal: <goal>
Success metric: <metric>
Project type: <project type>
Decision object: <decision object>
Stage: <stage>
Context anchors: <artifacts and prior failures>
Current strategy thesis:
<thesis>

Produce a stronger or more distinct path without duplicating existing strategies.

Return:
- proposed strategy or mutation
- why it is materially different
- smallest test worth running
- expected upside
- required artifact
- what evidence would falsify it
```

## Critic Template

```text
Role: Critic
Target strategy ids: <ids>

Goal: <goal>
Success metric: <metric>
Project type: <project type>
Decision object: <decision object>
Stage: <stage>
Context anchors: <artifacts and prior failures>
Strategies under review:
<strategy summaries>

Attack the ideas, not the formatting.

Return:
- top failure modes
- hidden assumptions
- cheapest falsification checks
- what would kill or park each path
- what evidence would rescue a weak path
```

## Validator Template

```text
Role: Validator
Target strategy ids: <ids>

Goal: <goal>
Success metric: <metric>
Project type: <project type>
Decision object: <decision object>
Stage: <stage>
Context anchors: <artifacts and prior failures>
Validation source: <holdout, benchmark, user acceptance test, or external check>

Run or define the cheapest credible test.

Return:
- test performed or proposed
- observed result
- comparison to baseline or threshold
- confidence update
- reward or penalty recommendation
- next action: exploit, mutate, park, or kill
```

## Search Round Addendum

Append this when the task is tuning or optimization over a search surface:

```text
Search stage: <broad screen|local refinement|full confirmation>
Region or family under test: <slice of the search space>
Baseline: <current incumbent>
Promotion rule: <what evidence advances this region>
Kill rule: <what evidence stops this region>
Evaluation tier: <cheap|medium|full>

Do not report a winner from one lucky point alone.
State whether the signal looks like a stable region, a fragile spike, or noise.
Prefer neighboring evidence and repeatability over single best-score claims.
```

## Synthesizer Template

```text
Role: Synthesizer

Goal: <goal>
Project type: <project type>
Decision object: <decision object>
Stage: <stage>
Round artifacts:
<artifact list>
Current ledger excerpt:
<leaderboard or strategy summaries>

Integrate only the decision-relevant information.

Return:
- updated leaderboard
- key evidence gained
- repeated failure patterns
- prompt or dispatch lessons
- next round allocation
```

## Prompt Hygiene Rules

- Keep ownership explicit so each role knows which strategy ids it owns.
- Ask for artifacts, thresholds, and falsification criteria, not polished essays.
- Freeze success tests before seeing results whenever possible.
- Avoid asking the proposer to also grade its own proposal.
