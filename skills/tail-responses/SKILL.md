---
name: tail-responses
description: Generate N candidate responses, compare their underlying ideas, and retrieve four concise candidates spanning a common baseline, rare alternatives, and a plausible wild card. Use for creative ideation, unusual hypotheses, or diverse solutions when the user wants semantic outliers with explicit quality checks.
---

# Tail Responses

Retrieve useful ideas from the uncommon parts of a generated response pool. Novelty means rarity within this pool; do not claim originality in the world without external evidence.

## Set the run

Use the user's question, constraints, and requested N. Default to N = 16 and four returned candidates. These are practical defaults, not statistically calibrated sample sizes. If the actual question is missing, ask for it; do not invent a task. Otherwise resolve routine choices without a questionnaire.

Keep the requested N exact. If N is less than four, return at most N and explain the shortfall. If resource limits prevent N responses, state the actual count. For a supplied response pool, compare that pool without silently adding generated responses.

Before generating, define what counts as a relevant, coherent answer and any task-specific validity requirements. For research, distinguish hypotheses from established findings; for verifiable problems, check correctness before rewarding rarity.

## Generate and preserve the pool

Assign stable IDs R01, R02, etc. Preserve the original response and a concise idea record for each:

- **Proposal:** what is suggested or claimed.
- **Mechanism:** why or how it could work.
- **Assumption:** the key condition it depends on.

Use separate generation contexts where available and authorized, sharing the same task and constraints but no other candidates. This skill does not itself require delegation, a particular provider, or paid API calls. If working in one context, generate the whole pool before judging it and disclose that it was a single-context batch, not independent sampling.

For a broad creative search, use roughly half neutral prompts and distribute the remainder across alternative mechanisms, changed assumptions, and different constraints or resources. Keep actual user constraints fixed. Record the prompt variation. For a user asking specifically for the tail of repeated identical prompts, use the same prompt throughout. Rarity in a mixed-prompt pool reflects that generation design.

Generate substantive alternatives, not stylistic rewrites. Do not force a bizarre answer to satisfy the wild-card slot.

## Compare ideas

Compare the proposal, mechanism, and assumption records, checking against the originals so compression does not erase their distinctive content. Ignore incidental differences in vocabulary, formatting, tone, or length.

Choose an honest comparison mode:

- **Embedding comparison:** when an embedding facility is already available, embed the normalized idea records consistently and compute cosine similarity. Record the model and the transformation used for any rescaling.
- **Judged comparison:** otherwise judge semantic overlap with the anchors below. Label values as heuristic assessments, not measured embedding similarity or probabilities. For large N, use coarse families followed by within-family and cross-family checks; disclose that this is approximate rather than a complete pairwise comparison.

Judged similarity anchors: 1.0 = essentially the same idea; 0.75 = same mechanism with a meaningful variant; 0.5 = some shared approach but materially different mechanism or assumptions; 0.25 = little substantive overlap; 0 = no shared solution approach. Topic overlap alone is not idea overlap.

Group near-duplicates into families. Inspect small families as well as isolated answers. Family boundaries and numeric thresholds are heuristics; revise them when original responses show a meaningful distinction.

For a complete numeric matrix, use [the selector contract](references/selector.md) and `scripts/select_candidates.py`. It computes mean distance to the nearest k eligible neighbors, with k = min(3, eligible_count - 1). A high score indicates local isolation. Small coherent families may still have low isolation scores, so inspect family representation during final review.

Do not manufacture numeric distances when only a qualitative comparison was performed. Use Low / Medium / High novelty instead.

## Quality gate and selection

Exclude responses that miss the question, contradict hard constraints, contain a decisive reasoning error, or depend on a false claim. An uncertain but coherent hypothesis can remain if its assumptions are explicit. Do not equate familiarity with quality or uncertainty with invalidity.

Assess every eligible response using the same criteria:

| Criterion | Low | Medium | High |
| --- | --- | --- | --- |
| Novelty within pool | Repeats a common idea | Distinct variant or small family | Unusual mechanism or assumption with few close neighbors |
| Usefulness | Weak link to the objective | Plausible benefit, indirect or limited | Directly advances the objective |
| Feasibility | Major unresolved barriers | Workable with explicit dependencies | Credible route using available resources |
| Confidence | Speculative, little supporting evidence | Reasoned support with material uncertainty | Strong task-relevant evidence or validation |

Unknown feasibility or confidence is **Unknown**, not automatically Low. Give a short rationale; ratings are judgments, not probabilities. For non-execution tasks, feasibility means internal viability under the stated constraints.

Select four distinct candidates by default:

1. **Baseline:** a quality-passing representative of the largest idea family, for comparison. It is not a tail result.
2. **Rare alternative A:** a useful uncommon mechanism or assumption.
3. **Rare alternative B:** another uncommon approach, materially different from both earlier choices.
4. **Wild card:** the most unusual remaining plausible idea, with its principal uncertainty explicit.

After selecting each alternative, penalize similarity to already selected ideas. Avoid selecting several versions of the same unusual idea. Prefer representation of different rare families over tiny score differences. Break ties using usefulness, then feasibility and confidence. Retain the baseline even if it is not the strongest recommendation, and label its role clearly.

If the user requests four tail responses only, replace the baseline with another rare alternative. If fewer than four distinct eligible ideas exist, return fewer with the reason; do not pad, lower the validity gate, or silently exceed N. Any second generation round requires the user's requested iteration or an explicitly available generation budget.

## Concise report

Adapt report-in-points' two-level grouping: one bold first-tier bullet per candidate, with the same concrete second-tier fields under each. This skill includes the template so it works without the other skill installed. Completion labels such as Done belong to implementation reports, not unevaluated ideas.

Start with one short audit line: generated or supplied count, eligible count, comparison mode, and sampling mode. Then use exactly this shape for each selected candidate, targeting 60–90 words per candidate:

- **1. [Short title] — [Baseline / Rare alternative / Wild card] · [source ID]**
  - **Idea:** one sentence stating the proposal and mechanism.
  - **Difference:** the substantive departure from the common family or other selected ideas.
  - **Assessment:** Novelty [L/M/H]; Usefulness [L/M/H]; Feasibility [L/M/H/Unknown]; Confidence [L/M/H/Unknown]. Include a brief reason for the most consequential rating.
  - **Check:** principal uncertainty and the smallest useful validation step.

Return the candidates themselves, not just descriptions of their qualities. Do not add a long essay, full matrix, or rejected-response dump unless requested. Mention a material selection limitation or shortfall in one sentence. If a recommendation is useful, finish with a single sentence identifying which candidate to test first and why. Do not automatically implement the selected ideas.

Keep original responses and selection records available in working context. Save the pool and detailed comparisons when requested or when needed for a long run, following the user's artifact destination. Never claim persisted or independently generated results without evidence.
