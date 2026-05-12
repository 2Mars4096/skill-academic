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

## Tiered Practice Funnel

Run the tiers in order. Ask only the smallest useful subset, prefer inspecting artifacts over asking the user, and stop when you have `2` to `5` concrete candidates that can change the next round.

### Tier 0: Trigger And Budget

- Does the task have specialized metrics, artifacts, tools, constraints, or practitioner norms?
- Would a strong public solution, past winner, field expert, or mature tool know obvious first moves?
- Is the next decision costly enough to justify a practice pass?
- What is the time budget: `mini` one or two questions, `standard` one pass through all tiers, or `deep` with source verification?

Skip the pass if the task is domain-neutral or already has clear acceptance tests and no meaningful strategy choice.

### Tier 1: Task Class

Pick the closest class before asking detailed questions:

- benchmark, modeling, tuning, ranking, or leaderboard work
- empirical, scientific, or academic research
- codebase, architecture, or developer workflow
- product, UX, operations, or business process
- writing, slides, communication, or review
- other specialized domain

Then pin down:

- What object is being improved?
- What metric or review standard decides success?
- What artifacts do practitioners actually manipulate?
- What failure would be expensive or misleading?

### Tier 2: Incumbents And References

- What simple baseline would expose fake progress?
- What incumbent method, workflow, heuristic, or tool is commonly hard to beat?
- What public notebook, reference implementation, mature product, paper, guide, or prior run should be decomposed for parts?
- Which pieces of the reference are trustworthy, and which may be leakage, overfit, outdated, or context-specific?

### Tier 3: Practice Move Menu

Use this menu to generate practical candidates. Do not use every category; pick the ones that match the task class and artifacts.

- `Representation`: features, abstractions, schemas, prompts, transforms, decompositions, data views
- `Baselines`: naive, incumbent, oracle-ish, cheap sanity check, lower-cost fallback
- `Search`: coarse-to-fine grids, thresholds, schedules, seeds, parameter regimes, sensitivity checks
- `Combination`: ensemble, stack, blend, routing, fallback, voting, arbitration
- `Prior or constraint`: physics, invariants, business rules, style rules, monotonicity, feasibility checks
- `Postprocess`: calibration, smoothing, formatting, ranking adjustment, repair pass, consistency enforcement
- `Diagnostics`: error slices, hard cases, stress tests, expert signals, counterexamples
- `Tooling`: library, parser, simulator, benchmark harness, evaluator, automation script

For each candidate, ask: what is the cheapest variant that could produce decision-changing evidence?

### Tier 4: Natural Role

Classify each practice candidate by the role it should naturally play:

- `standalone`: a complete alternative strategy
- `input_or_feature`: a signal, representation, prompt, data view, or helper artifact
- `prior_or_constraint`: a rule that narrows or regularizes the solution
- `gate_or_router`: a confidence signal, branch selector, or escalation rule
- `blend_or_fallback`: a weak component that can improve robustness in combination
- `postprocess`: a final repair, calibration, smoothing, ranking, or formatting step
- `diagnostic`: a check that changes trust, promotion, or kill decisions

Do not kill a candidate because it is weak as a standalone if its natural role is a feature, prior, gate, blend, postprocess, or diagnostic.

### Tier 5: Test And Verification

For the top candidates, define:

- What baseline or incumbent will it compare against?
- What is the smallest credible test?
- What result promotes it?
- What result parks or kills it?
- What would make the result misleading?
- Does the claim need source lookup, benchmark, experiment, or human review?

### Tier 6: Missed Practice Audit

Run this after a weak or surprising round:

- What expert-standard trick, baseline, or diagnostic did we still not test?
- Did we dismiss a public/reference solution too broadly instead of decomposing it into parts?
- Did we test each idea in its natural role?
- Did validation caution prevent cheap practical exploration that could have been made fold-safe, holdout-safe, or otherwise rigorous?
- What single low-cost practice candidate should be added, mutated, or promoted next?

## Convert Answers Into Strategy Branches

For each useful practice, record:

- `Source type`: expert prior, standard baseline, common trap check, diagnostic, or needs verification
- `Branch thesis`: why this practice might help
- `Natural role`: standalone, input_or_feature, prior_or_constraint, gate_or_router, blend_or_fallback, postprocess, or diagnostic
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
- `Natural role and smallest test for each candidate`
- `Common traps and misleading signals`
- `Expert validation signals`
- `Promotion and kill rules`
- `Claims needing external verification`

## Guardrails

- Do not present remembered domain practice as settled fact when the domain is niche, changing, or high-stakes.
- Do not add expert-flavored complexity unless it changes the first test or validation logic.
- Prefer practices that produce immediate discrimination between branches.
- Keep the portfolio narrow after elicitation; merge duplicate practices and park low-value ideas.
