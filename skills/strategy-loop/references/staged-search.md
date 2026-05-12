# Staged Search

Use this reference when the loop is optimizing over a search surface rather than choosing among purely discrete strategies. Typical examples:

- parameter or hyperparameter tuning
- prompt or workflow configuration search
- benchmark optimization
- model, heuristic, or policy selection
- threshold, ranking, or scoring-rule tuning

The goal is to search broadly enough to learn the shape of the surface, then narrow deliberately without overfitting to noise.

## Core Principle

Treat the search as a sequence of evidence filters:

1. broad screen to find promising regions
2. local refinement to test whether the signal survives nearby perturbations
3. full confirmation on a deeper validation surface

Do not jump straight from a broad search to declaring one point the winner.

## Lock Before Search

Before launching a search round, freeze:

- `Objective`: what metric is being optimized and whether higher or lower is better
- `Baseline`: current incumbent or simple reference
- `Search space`: parameters, ranges, and any forbidden combinations
- `Evaluation tiers`: cheap screen, deeper confirmation, and external or holdout check
- `Promotion rule`: what moves a region from one tier to the next
- `Kill rule`: what drops a region early
- `Complexity budget`: how much added complexity or cost is acceptable

If any of these are missing, the round is underspecified.

## Stage A: Broad Screen

Use coarse spacing and cheap evaluation.

Default behavior:

- sample the space with large gaps
- cover materially different families or regimes first
- keep the evaluation cheap enough to test several families
- log both results and notable failures

Good outputs from Stage A:

- 2 to 4 promising regions or families
- early evidence about dead zones
- a clearer sense of sensitivity and interaction effects

Bad Stage A behavior:

- searching too finely before the broad shape is known
- spending most of the budget confirming one early winner
- mutating the search grid after every result

## Promotion Rule

Promote a region, family, or pattern, not only the single best point.

A candidate is worth promoting when most of the following are true:

- it beats the baseline or matches it at lower cost
- the improvement survives small nearby changes
- the gain is not driven by a single slice, seed, or lucky split
- the complexity increase is justified by the margin

If the signal disappears under a tiny perturbation, treat it as fragile rather than "best."

## Stage B: Local Refinement

Narrow only around the promoted regions.

Default behavior:

- reduce step size around the best regions
- test neighboring settings that reveal whether there is a plateau
- compare against the incumbent, not only against siblings
- cap how many local refinement rounds happen before confirmation

The purpose of Stage B is to answer:

- is there a stable local region worth trusting?
- which variables matter most?
- does the apparent win survive small changes?

## Stage C: Full Confirmation

Run the expensive or decision-bearing evaluation only on a small finalist set.

Typical confirmation checks:

- deeper validation budget
- tougher holdout or external benchmark
- stress cases or hard slices
- stability across repeated runs
- comparison against a simpler fallback

Do not keep adding finalists once Stage C starts unless earlier assumptions were clearly wrong.

## Ranking

Do not rank candidates by the headline metric alone when the task has noise or transfer risk.

Use a conservative selection rule such as:

- `selection_score = primary_value - instability_penalty - complexity_penalty - transfer_risk_penalty` when higher is better
- `selection_score = primary_value + instability_penalty + complexity_penalty + transfer_risk_penalty` when lower is better

Pick penalties that reflect the real failure cost of a misleading local win.

Useful supporting signals:

- central tendency on the main metric
- spread across seeds, folds, or repeated runs
- worst-case or tail behavior
- performance on hard slices
- disagreement against a simpler baseline
- added cost, latency, or operational complexity

## Anti-Overfit Rules

- Freeze grids, thresholds, and promotion rules before running a stage whenever practical.
- Separate exploration metrics from final confirmation metrics.
- Prefer broad evidence over repeated micro-adjustments to one apparent winner.
- Stop local refinement when improvements shrink below practical significance.
- Stop when added complexity rises faster than validated gain.
- Prefer plateaus that remain good under perturbation over sharp optima that collapse under small changes.

## Stop Conditions

Stop the search when:

- one region is clearly strong and stable on the full evaluation surface
- recent rounds are only reshuffling near-ties
- the remaining uncertainty is not decision-changing
- the next confirmation step costs more than the value of the expected learning

Reframe when:

- the whole surface looks flat
- every win depends on fragile settings
- all strong candidates fail the harder confirmation tier
- the objective or validation surface appears misaligned with the real goal

## Output Shape For A Search Round

End each search-heavy round with:

- `Objective and baseline`
- `Current stage`
- `Live regions or families`
- `Promotion and kill rules`
- `Evidence gained`
- `Conservative ranking`
- `Next grid or refinement plan`
- `Confirmation trigger`
