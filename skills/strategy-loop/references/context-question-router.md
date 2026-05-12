# Context Question Router

Use this when the strategy loop needs to turn an abstract request into project-specific questions. The purpose is not to collect everything. It is to decide which narrow question family should govern the next round.

## Router Rules

- Ask only `1` to `3` questions unless the user requests a full diagnostic.
- Ask a question only if the answer would change the candidate portfolio, validation source, or next action.
- Prefer reading existing artifacts over asking the user to summarize them.
- Stop routing once the decision object and validation source are concrete enough to compare strategies.
- Do not mix every question pack. Pick the smallest relevant pack for the current project.

## Universal Funnel

Use these when the project type or decision object is unclear:

- What kind of project is this: academic research, codebase, agent workflow, product/tool, writing/deck, or something else?
- What decision are we making this round: choose the main direction, repair a weak path, pick a validation test, or allocate execution work?
- What existing artifacts should define the context: files, notes, drafts, datasets, tests, dashboards, prior run reports, or feedback?
- What evidence would actually distinguish the options?
- What is the next expensive or hard-to-reverse choice?

## Academic Proposal Or Paper

Use when the strategies are research directions, proposal framings, empirical designs, or paper-development paths.

- Are we choosing the research question, data construction, identification strategy, contribution framing, or next empirical result?
- What is already fixed: setting, unit, outcome, treatment or exposure, comparison, mechanism, data source, or target audience?
- What would kill a path fastest: no data access, no observable variation, weak outcome, bad identification, weak contribution, or excessive construction cost?
- What evidence would promote a path: data availability, first table, balance check, event-study shape, advisor approval, literature gap, or feasible draft section?
- Which alternative framing is still live enough to deserve comparison?

## Data Construction

Use when competing paths differ mainly in how evidence will be built.

- What is the unit of observation and what raw source creates it?
- Which construction step is most uncertain: scraping, linking, cleaning, labeling, aggregation, or measurement validity?
- What minimum dataset slice would prove the path is feasible?
- What quality check would expose a bad construction path early?
- What cost grows fastest if this path is wrong?

## Identification Or Empirical Design

Use when strategies differ by comparison, source of variation, or causal claim.

- What comparison is each strategy betting on?
- What assumption would make the leading design invalid?
- Is the current claim causal, descriptive, predictive, or mechanism-oriented?
- What falsification, placebo, pre-trend, robustness check, or benchmark would change the ranking?
- If identification fails, is there a weaker but still valuable descriptive path?

## Literature Review Or Writing

Use when the strategies are ways to organize, argue, or draft.

- Are we choosing the map of the literature, the priority readings, the paper structure, or the argument spine?
- What audience or venue defines success?
- What existing notes, citations, figures, or draft sections should anchor the round?
- What would make one structure clearly better: coverage, novelty, readability, advisor fit, or ease of drafting?
- Which section or claim is currently blocking progress?

## Codebase Or Product Implementation

Use when strategies are implementation architectures, feature slices, refactors, or validation approaches.

- Are we choosing architecture, API shape, data model, UI workflow, migration plan, or test strategy?
- What existing files, tests, errors, or user workflows define the context?
- What failure is most expensive: regression, bad abstraction, migration risk, poor UX, performance, or maintainability?
- What is the smallest implementation or test that would distinguish the options?
- Which paths touch shared contracts or require coordination with other work?

## Agent Workflow Or Orchestration

Use when strategies concern prompts, roles, dispatch policy, validation, or child-session management.

- Are we choosing roles, delegation boundaries, planner policy, validation gates, provider mix, or monitoring UX?
- What prior runs, dashboards, child reports, or failure modes define the evidence?
- What failure is most costly: redundant agents, runaway work, weak validation, merge conflicts, stale context, or bad handoff?
- What artifact should the next round produce: ledger update, launch manifest, prompt template, test run, review report, or controller patch?
- Should this loop only decide strategy, or should execution be handed to `team-leader` after the round plan is clear?
