# Numeric selector

Use this optional, dependency-free Python helper after generation, quality assessment, and semantic comparison. It does not call a model, generate responses, compute embeddings, or verify correctness. The skill handles those steps using available capabilities.

Run from the skill directory:

```sh
python3 scripts/select_candidates.py pool.json > selection.json
```

Input shape (this abbreviated two-response example deliberately produces a shortfall):

```json
{
  "comparison_method": "judged semantic overlap",
  "sampling_mode": "single-context batch",
  "candidates": [
    {"id": "R01", "family": "common", "eligible": true,
     "usefulness": 3, "feasibility": 3, "confidence": 2},
    {"id": "R02", "family": "alternative", "eligible": true,
     "usefulness": 3, "feasibility": 2, "confidence": 1}
  ],
  "similarity": [[1.0, 0.25], [0.25, 1.0]]
}
```

Matrix row order must match candidate order. Values must be finite, symmetric, within [0, 1], with diagonal 1. For cosine similarity s in [-1, 1], use (s + 1) / 2 and record that transformation in comparison_method. Threshold interpretation changes under rescaling; review the selected ideas rather than treating a cutoff as universal.

Each candidate requires a unique nonempty string ID, a nonempty semantic family, an explicit boolean eligible, usefulness in {1,2,3}, and feasibility/confidence in {1,2,3,null}. Here 1/2/3 correspond to Low/Medium/High and null to Unknown. These are ordinal tie-breakers only. Additional fields (original response, idea record, exclusion reason, prompt variation) are preserved in selected output. Include exclusion reasons for ineligible records in real runs.

Optional fields:

- `tail_only`: boolean, default false. Select four rare candidates without a baseline when true.
- `duplicate_threshold`: number in (0,1], default 0.9. Candidates at or above this similarity to any selection are skipped.

The helper identifies the largest eligible family and selects its most central member as baseline, breaking ties by quality ratings, then input order. Other choices prioritize as-yet unrepresented families, then the average of local novelty and minimum distance to the selected set. The final wild card prioritizes local novelty within that same family-diversity rule. Unknown ratings tie below supported Low ratings but never affect eligibility. Novelty uses all eligible responses, so repetition changes the observed density by design.

Output includes selected source records, role, novelty, pool counts, excluded IDs, comparison metadata, and any shortfall. Scores are selection heuristics, not calibrated creativity measurements. If semantic review changes a family, eligibility, or similarity, update the input and rerun rather than silently overriding a score. The concise user report uses qualitative criteria and explanations; do not dump this JSON by default.
