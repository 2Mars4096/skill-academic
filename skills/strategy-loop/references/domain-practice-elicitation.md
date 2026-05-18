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

Before keeping a question, ask: if answered, what representation, candidate, validation rule, or dispatch task would change? Drop or sharpen questions that only collect background.

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

### Tier 2: Representation Contract

For data/modeling/benchmark/search tasks, answer this before proposing sweeps:

- What are the stable comparable objects, states, users, documents, rows, cases, or regimes?
- What does the current distance, similarity, grouping, prompt, or benchmark slice assume?
- Which raw fields are coordinate-system artifacts, proxies, labels, leaks, or train-only signals?
- What allowed observables can verify same-status or same-regime comparison?
- What fold-safe, holdout-safe, or deployment-safe proxy is needed for any target-like concept?

If this contract is weak, first test representations, selectors, or diagnostics rather than deeper model or parameter sweeps.

### Tier 3: Abstraction-Level Check

Classify the next useful move before generating variants:

- `surface_patch`: changes wording, columns, parameters, local rules, or presentation without changing the underlying process
- `component`: replaces a separable module, feature family, data source, prompt block, model, section, or workflow step
- `workflow`: implements an end-to-end process such as a candidate generator, research design, user flow, review pipeline, or automation path
- `full_architecture`: creates an alternate trunk, system design, solution family, narrative structure, or operating model

If recent work has only changed surface patches, ask whether the domain idea actually requires a component, workflow, or full architecture. When a practice describes a workflow, test a thin end-to-end version before judging it from one isolated piece.

### Tier 4: Mechanism Compression

For costly, expressive, or high-upside ideas, do not jump straight to full implementation. Compress the idea:

- `Verbal theory`: what claim or story makes the idea plausible?
- `Mechanism hypothesis`: what process would make it work?
- `Necessary implication`: if the mechanism is true, what must be observable?
- `Cheapest proxy`: what small plot, table, query, regression, test, log check, mock, or slice can measure that implication?
- `Kill result`: what proxy result would downgrade or stop the idea?
- `Scale trigger`: what proxy result justifies a fuller workflow, architecture, model, design, or implementation?

If any item is still vague, recurse once with `strategy-loop-recursive` until it names an artifact, check, or decision. Prefer high-falsifiability proxies over expressive systems that can produce ambiguous partial wins.

### Tier 5: Incumbents And References

- What simple baseline would expose fake progress?
- What incumbent method, workflow, heuristic, or tool is commonly hard to beat?
- What public notebook, reference implementation, mature product, paper, guide, or prior run should be decomposed for parts?
- Which pieces of the reference are trustworthy, and which may be leakage, overfit, outdated, or context-specific?

### Tier 6: Practice Move Menu

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

### Tier 7: Natural Role

Classify each practice candidate by the role it should naturally play:

- `standalone`: a complete alternative strategy
- `input_or_feature`: a signal, representation, prompt, data view, or helper artifact
- `prior_or_constraint`: a rule that narrows or regularizes the solution
- `gate_or_router`: a confidence signal, branch selector, or escalation rule
- `blend_or_fallback`: a weak component that can improve robustness in combination
- `postprocess`: a final repair, calibration, smoothing, ranking, or formatting step
- `diagnostic`: a check that changes trust, promotion, or kill decisions

Do not kill a candidate because it is weak as a standalone if its natural role is a feature, prior, gate, blend, postprocess, or diagnostic.

### Tier 8: Test And Verification

For the top candidates, define:

- What baseline or incumbent will it compare against?
- What is the smallest credible test?
- What result promotes it?
- What result parks or kills it?
- What would make the result misleading?
- Does the claim need source lookup, benchmark, experiment, or human review?

### Tier 9: Missed Practice Audit

Run this after a weak or surprising round:

- What expert-standard trick, baseline, or diagnostic did we still not test?
- Did we keep searching inside a bad representation or similarity assumption?
- Are we decorating the current representation when we need a new component, workflow, or architecture?
- Did we implement a large idea before testing its weakest necessary consequence?
- Did we dismiss a public/reference solution too broadly instead of decomposing it into parts?
- Did we test each idea in its natural role?
- Did validation caution prevent cheap practical exploration that could have been made fold-safe, holdout-safe, or otherwise rigorous?
- What single low-cost practice candidate should be added, mutated, or promoted next?

## Convert Answers Into Strategy Branches

For each useful practice, record:

- `Source type`: expert prior, standard baseline, common trap check, diagnostic, or needs verification
- `Branch thesis`: why this practice might help
- `Abstraction level`: surface_patch, component, workflow, or full_architecture
- `Natural role`: standalone, input_or_feature, prior_or_constraint, gate_or_router, blend_or_fallback, postprocess, or diagnostic
- `Artifact contract`: runnable, reviewable, or evidence-bearing output expected from the branch
- `Mechanism compression`: verbal theory, mechanism, necessary implication, cheapest proxy, kill result, and scale trigger when useful
- `Smallest test`: cheapest evidence-bearing check
- `Comparison`: baseline or incumbent to compare against
- `Promotion rule`: evidence that advances the branch
- `Kill rule`: evidence that stops or parks the branch
- `Verification need`: none, source lookup, benchmark, experiment, or human review

## Output Shape

End the pass with:

- `Question-quality check`: decision-changing questions kept, vague questions dropped or sharpened
- `Expert priors worth testing`
- `Representation contract`: comparable objects, similarity assumptions, allowed regime signals, invalid shortcuts
- `Abstraction-level check`: surface patches, components, workflows, and full architectures under consideration
- `Mechanism compression`: idea -> mechanism -> necessary implication -> cheapest proxy -> kill result -> scale trigger
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
