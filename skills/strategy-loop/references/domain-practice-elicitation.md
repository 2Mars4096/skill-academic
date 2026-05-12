# Domain Practice Elicitation

Use this reference when a task may depend on field-specific experience: standard baselines, common diagnostics, practical heuristics, known traps, or expert workflows. The goal is to enrich the strategy portfolio with domain-informed candidates before execution starts.

Treat domain practice as priors to test, not as authority. If a claim is time-sensitive, high-stakes, niche, or uncertain, mark it for external verification or direct experiment.

## When To Use

Use this before seeding or mutating the portfolio when:

- the domain likely has standard baselines or common workflows
- a field expert would know obvious first checks
- the task involves specialized metrics, artifacts, data, tools, or failure modes
- early branches feel generic or ignore known practice
- the strategy loop is reinventing things practitioners already test routinely

Skip it when the task is domain-neutral, already has explicit expert context, or only needs a small implementation with clear acceptance tests.

## Core Questions

Ask the smallest useful subset.

### Expert First Checks

- What would an experienced practitioner check first?
- What quick diagnostic would reveal whether the current framing is wrong?
- What simple baseline or sanity check should exist before complex work starts?

### Standard Baselines

- What default method, workflow, heuristic, or benchmark is commonly hard to beat?
- What naive baseline would expose fake progress?
- What incumbent should every proposed branch compare against?

### Common Practices

- What practices, feature ideas, parameter regimes, workflows, or decomposition patterns are commonly useful here?
- What cheap variants are worth testing before expensive ones?
- What field-specific tools, artifacts, or representations usually matter?

### Common Traps

- What mistakes often create misleading wins?
- What leakage, confounding, shortcut, metric mismatch, UX illusion, benchmark artifact, or deployment mismatch should be checked?
- What result would look impressive to a non-expert but fail expert review?

### Expert Signals

- What signals would a field expert use to tell whether progress is real?
- What hard cases, slices, edge cases, or stress checks are considered diagnostic?
- What secondary metric can override the headline score?

### Domain Constraints

- What assumptions, invariants, interfaces, norms, or safety boundaries should not be violated?
- Which constraints are hard requirements versus preferences?
- What hidden cost, latency, complexity, or maintenance burden matters in this field?

### Verification Need

- Which expert-practice claims can be trusted from current context?
- Which should be verified from docs, papers, benchmarks, source code, user feedback, or direct experiments?
- Which claims are likely outdated or context-dependent?

## Convert Answers Into Strategy Branches

For each useful practice, record:

- `Source type`: expert prior, standard baseline, common trap check, diagnostic, or needs verification
- `Branch thesis`: why this practice might help
- `Smallest test`: cheapest evidence-bearing check
- `Comparison`: baseline or incumbent to compare against
- `Promotion rule`: evidence that advances the branch
- `Kill rule`: evidence that stops or parks the branch
- `Verification need`: none, source lookup, benchmark, experiment, or human review

## Output Shape

End the pass with:

- `Expert priors worth testing`
- `Standard baselines to include`
- `Cheap diagnostic checks`
- `Domain-informed candidate branches`
- `Common traps and misleading signals`
- `Expert validation signals`
- `Promotion and kill rules`
- `Claims needing external verification`

## Guardrails

- Do not present remembered domain practice as settled fact when the domain is niche, changing, or high-stakes.
- Do not add expert-flavored complexity unless it changes the first test or validation logic.
- Prefer practices that produce immediate discrimination between branches.
- Keep the portfolio narrow after elicitation; merge duplicate practices and park low-value ideas.
