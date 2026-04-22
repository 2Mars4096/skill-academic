# Ledger Schema

Use this schema when a strategy loop needs persistent memory across rounds.

## Top-Level Shape

The scorer accepts either:

- a dictionary with a `strategies` list
- a raw list of strategy objects

Recommended top-level fields:

- `goal`
- `success_metric`
- `round_index`
- `validation_source`
- `strategies`
- `lessons`

## Strategy Fields

Each strategy should include:

- `id`: stable unique identifier
- `thesis`: what the strategy is betting on
- `status`: `live`, `parked`, `killed`, or `validated`
- `parent_id`: source strategy for mutations, optional for originals
- `first_test`: smallest evidence-bearing check
- `average_reward`: normalized reward, ideally `-1.0` to `1.0`
- `confidence`: confidence in the current read, `0.0` to `1.0`
- `novelty`: how non-redundant the path is, `0.0` to `1.0`
- `cost`: execution burden, `0.0` to `1.0`
- `risk`: downside if the path misleads or fails, `0.0` to `1.0`
- `evidence_count`: number of real checks or observations behind the score
- `failure_reason`: blank unless the path has failed or been parked for a specific reason
- `next_action`: `exploit`, `mutate`, `explore`, `park`, or `kill`

The scorer also accepts rough text labels such as `low`, `medium`, and `high` for `confidence`, `novelty`, `cost`, and `risk`.

## Update Rules

- Keep `id` stable across rounds.
- Give each mutated variant a new `id` and point `parent_id` at the source.
- Update `average_reward` only from evidence-backed outcomes.
- Update `confidence` from validation depth, not prose quality.
- Fill `failure_reason` as soon as a path is parked or killed.
- Store cross-round lessons under `lessons` so bad assumptions and weak prompts are not retried blindly.

## Example

```json
{
  "goal": "Improve manager dispatch quality for repo-scale coding tasks",
  "success_metric": "Higher validated completion rate with fewer wasted launches",
  "round_index": 3,
  "validation_source": "holdout implementation tasks and review findings",
  "strategies": [
    {
      "id": "baseline-review-first",
      "thesis": "Start with a narrow review wave before launching writers.",
      "status": "live",
      "average_reward": 0.62,
      "confidence": 0.75,
      "novelty": 0.25,
      "cost": 0.30,
      "risk": 0.20,
      "evidence_count": 3,
      "next_action": "exploit"
    },
    {
      "id": "mutant-split-ownership",
      "parent_id": "baseline-review-first",
      "thesis": "Pre-assign file ownership to reduce merge conflicts.",
      "status": "parked",
      "average_reward": 0.41,
      "confidence": 0.45,
      "novelty": 0.70,
      "cost": 0.35,
      "risk": 0.30,
      "evidence_count": 1,
      "failure_reason": "Helped writers, but planning overhead was too high.",
      "next_action": "mutate"
    }
  ],
  "lessons": [
    "Weak prompts without kill criteria create false optimism.",
    "Cheap review passes improve confidence before expensive writer launches."
  ]
}
```
