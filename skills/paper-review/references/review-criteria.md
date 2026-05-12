# Review Criteria

Use these criteria to decide what belongs in a referee report. A good major comment should usually satisfy at least three conditions:

- it affects the paper's contribution, validity, interpretation, or publication fit
- it is grounded in a specific table, figure, design choice, variable, sample, or literature benchmark
- it gives authors and the editor a clear reason why the issue matters
- it points to a feasible fix or explains why a fix is unlikely

## Contents

- `Contribution`
- `Identification And Causal Claims`
- `Measurement, Data, And Representativeness`
- `Sample Consistency`
- `Timing And Dynamics`
- `Mechanism And Alternative Explanations`
- `Economic And Managerial Significance`
- `Internal Consistency`
- `Structure And Readability`
- `Revision Feasibility`

## Contribution

Ask:

- Is the paper's main insight new relative to the closest literature?
- Does the paper add theory, mechanism, setting, measurement, identification, or managerial insight rather than only a new sample?
- Is the "so what" clear for OM, supply-chain, operations, or the target journal audience?
- Are claimed contributions actually supported by the analyses?
- Does the paper contribute to OM theory, operations practice, or the target journal's audience beyond documenting a familiar empirical pattern?

Strong concerns:

- The central finding is already known and the paper does not explain the incremental contribution.
- The managerial implication is intuitive, generic, or not connected to actionable evidence.
- The paper changes context but not the conceptual or empirical insight.

Useful author requests:

- clarify the closest benchmark paper and state the exact incremental insight
- add evidence connecting the result to a real operational or managerial outcome
- narrow the contribution to a descriptive, measurement, mechanism, or setting contribution if the causal contribution is weak
- compare directly against the closest prior paper rather than a broad literature category

## Identification And Causal Claims

Ask:

- Does the design support the strength of the causal language?
- Are simultaneous shocks, omitted variables, selection, reverse causality, or timing confounds credible?
- Are fixed effects at the right level for the treatment variation?
- For staggered DiD, are heterogeneous treatment effects, pre-trends, and dynamic effects handled credibly?
- For IVs, is the exclusion restriction plausible at the actual level of identifying variation?

Strong concerns:

- The paper attributes effects to one event while other shocks occur at the same time.
- The instrument appears to capture historical industry, region, or group trends that directly affect outcomes.
- The treatment timing is endogenous or not shown to precede the outcome.
- The paper uses causal wording for correlational evidence.

Useful author requests:

- add event-study or dynamic evidence with pre-treatment indicators
- use a more robust DiD estimator when TWFE is fragile
- absorb relevant time-varying industry, country, region, or group trends where feasible
- soften causal language if the design cannot isolate the mechanism
- explain why the identifying variation is not just historical industry, region, or country trends

## Measurement, Data, And Representativeness

Ask:

- Is the key variable measuring the concept claimed in the paper?
- Is the dataset coverage representative of the population the paper discusses?
- Are start dates, end dates, disclosure-based observations, or platform samples likely to create selection bias?
- Are stock variables being interpreted as flows?
- Are variables and data sources clearly defined enough to replicate?

Strong concerns:

- The data measure documentation of a relationship rather than the relationship itself.
- The sample excludes important channels, non-English observations, private firms, distributors, or indirect transactions without justification.
- A key measure confounds two mechanisms, such as trade credit generation and payment timing.
- The data source is named but not described enough for readers to judge coverage.

Useful author requests:

- report coverage and representativeness statistics
- discuss selection bias and how it affects interpretation
- re-define or decompose the variable to better match the theoretical object
- add key variables to summary statistics and clarify construction

## Sample Consistency

Ask:

- Are main outcome tests, mechanism tests, and placebo tests estimated on comparable samples?
- Do sample-size changes alter interpretation?
- Are authors comparing coefficients from different populations?

Strong concerns:

- Mechanism evidence is estimated on firms that do not appear in the main outcome sample.
- A placebo or comparison outcome uses a different sample, making magnitude comparisons hard to interpret.
- Treatment or outcome availability mechanically selects observations.

Useful author requests:

- re-estimate related tests on a common subsample
- show whether mechanism results hold on the same observations as the main outcome
- explain sample attrition and provide a sample construction table

## Timing And Dynamics

Ask:

- Does the effect appear when the mechanism predicts it should?
- Are delayed effects explained with direct evidence rather than post hoc interpretation?
- Do event-study figures and aggregated ATT tables tell the same story?
- Does the event window overlap with other major shocks?

Strong concerns:

- Effects appear only after long lags, while the mechanism predicts immediate or early changes.
- Effects are significant only after pooling across event times.
- The timing of observed changes conflicts with the paper's event narrative.
- A figure or robust estimator shows null post-treatment coefficients while the text emphasizes positive effects.

Useful author requests:

- reconcile dynamic patterns with the proposed mechanism
- provide horizon-specific estimates and confidence intervals
- test whether mechanism variables move before or when the outcome moves
- clarify the event date and baseline period
- reconcile the dynamic evidence with the mechanism rather than relying on a post hoc adaptation story

## Mechanism And Alternative Explanations

Ask:

- Does the mechanism evidence test the mechanism directly or only show consistency?
- Are alternative mechanisms ruled out or at least discussed?
- Are mechanism variables measured on the right sample and timing?
- Does the paper distinguish the focal mechanism from broader digital, financial, policy, or demand changes?

Strong concerns:

- The mechanism is asserted but not measured directly.
- The evidence is consistent with several explanations, not just the authors' preferred one.
- Mechanism tests are in a different sample or use proxies that map poorly to the theory.

Useful author requests:

- add a small number of direct mechanism tests
- test operational outcomes that should move if the mechanism is real
- distinguish the focal mechanism from close alternatives
- soften mechanism claims if evidence remains only suggestive
- when possible, ask for one direct table on operations-side outcomes rather than a broad new empirical section

## Economic And Managerial Significance

Ask:

- Are statistically significant effects large enough to matter?
- Can a manager act on the result?
- Are nonlinear turning points inside the relevant data range?
- Are coefficient magnitudes interpreted in operational units or standardized terms?

Strong concerns:

- The effect is tiny relative to the outcome mean or standard deviation.
- The optimum or threshold lies far outside the sample's typical range.
- The paper claims managerial relevance without translating estimates into decisions.

Useful author requests:

- calculate effect sizes for one-standard-deviation changes
- show where firms lie relative to a nonlinear optimum
- translate the result into a concrete operational decision
- add model-free or descriptive evidence showing practical magnitude

## Internal Consistency

Ask:

- Do tables, figures, text, appendix, and response letter agree?
- Do interaction signs, first-order terms, and net effects support the interpretation?
- Are table numbers, labels, and definitions consistent?

Strong concerns:

- The text emphasizes interaction signs while ignoring large opposite-signed main effects.
- A figure suggests null effects while the text describes robust positive effects.
- A table label, variable definition, or sample period contradicts another part of the paper.
- The paper compares outcomes, placebo tests, or mechanisms across different samples without acknowledging it.

Useful author requests:

- discuss the full coefficient pattern, not only preferred signs
- reconcile text and table or figure evidence
- correct table numbering, labels, and duplicate text

## Structure And Readability

Ask:

- Can readers distinguish main identification evidence from reassurance checks?
- Are robustness tests crowding out the main argument?
- Are extended analyses integrated into the paper's logic?

Strong concerns:

- The paper feels like disconnected analyses rather than one continuous argument.
- The main story is hidden behind too many robustness checks.
- Important results appear in the wrong section or appendix.

Useful author requests:

- group baseline, identification, and mechanism evidence into a clearer sequence
- move secondary robustness or alternative-explanation checks to the appendix
- streamline the main text around the core claim

## Revision Feasibility

Ask:

- Are the requested fixes data re-runs, clearer exposition, or a fundamentally new design?
- Could the authors address the issue without changing the paper's core claim?
- Would a revision likely produce a publishable paper?

Recommendation mapping:

- `Reject`: new contribution, new design, or new measurement would be needed.
- `Risky major revision`: fixes are possible but substantial and uncertain.
- `Major revision`: important but bounded analyses or reframing are needed.
- `Minor revision`: remaining issues are presentation, clarification, or limited checks.
