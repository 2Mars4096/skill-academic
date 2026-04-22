# Prompt Patterns

Use these templates when the default `Strategy Loop` guidance is too abstract and a round needs explicit role prompts. Keep prompts short, bounded, and artifact-oriented.

## Shared Inputs

Every role prompt should include:

- `Goal`
- `Success metric`
- `Current strategies`
- `Owned strategy ids`
- `Budget or time cap`
- `Validation source`
- `Known failures`
- `Required output format`

## Manager Kickoff Template

```text
You are managing a strategy portfolio, not writing a one-shot answer.

Goal: <goal>
Success metric: <metric>
Budget: <budget>
Validation source: <holdout, benchmark, or external check>
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

## Synthesizer Template

```text
Role: Synthesizer

Goal: <goal>
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
