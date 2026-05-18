---
name: strategy-loop-recursive
description: Add bounded recursive concretization to problem fixing, optimization, strategy-loop, and team-leader planning so vague goals, symptoms, causes, expert personas, definitions, criteria, abstractions, failures, and tasks become concrete artifacts, tests, and decisions. Use when work is producing broad advice instead of converging on a workable solution, especially debugging, performance tuning, benchmark optimization, research strategy, architecture, product/workflow fixes, or multi-agent orchestration.
---

# Strategy Loop Recursive

## Overview

This skill adds a bounded recursion layer to any problem-fixing or optimization loop. Use it when the work has a plausible high-level direction but is still too vague, too incremental, symptom-focused, or stuck at the wrong abstraction level.

The goal is not more questions. The goal is to recursively convert vague problem language into project-specific artifacts, tests, fixes, dispatch prompts, and stop rules.

If `strategy-loop` is also active, keep its portfolio, ledger, staged search, representation contract, and abstraction-level gates. Add the recursive checks below before seeding strategies, before dispatching children, and after weak rounds.

When `strategy-loop` asks for mechanism compression, use this skill only if the idea, mechanism, necessary implication, cheapest proxy, kill result, or scale trigger is still vague after one pass.

## Core Rule

For any important goal, symptom, proposed fix, criterion, or phrase that is still abstract, ask:

1. What does this mean in this project?
2. What artifact would show we did it?
3. What test would falsify it?
4. What fix, decision, or dispatch task changes because of the answer?

If the answer is still vague, recurse once:

- Name the exact object, file, experiment, prompt, metric, slice, artifact, workflow step, or user-visible behavior.
- If that still cannot be named, drop the question or mark it as background only.

Default recursion budget:

- maximum `2` levels deep
- maximum `3` vague phrases per pass
- stop as soon as the answer changes the problem definition, fix, validation rule, artifact, dispatch prompt, or stop decision

## Where To Recurse

### Problem Definition

When the request is "fix this", "improve this", "optimize this", or "make it better", recurse before acting:

- What is the exact symptom, failure, opportunity, or bottleneck?
- What object is failing: code path, model, document, workflow, interface, metric, user path, or decision process?
- What is the current baseline and what would count as a real improvement?
- What hidden assumption would make the proposed fix irrelevant?

### Objective And Metric

When the goal is "better", "faster", "stronger", "cleaner", "more robust", or "higher quality", make the objective operational:

- What metric, review standard, user outcome, or business/research criterion matters?
- What should not get worse while optimizing it?
- What hard slice, edge case, regression test, or external check can override the headline result?
- What threshold triggers exploit, mutate, park, kill, or abstraction escalation?

### Assumptions And Root Causes

When a fix is proposed, recurse on why it should work:

- What root cause does this fix assume?
- What cheaper diagnostic can separate root cause from symptom?
- What observation would prove the current explanation wrong?
- If this fix works only locally, what transfer or deployment risk remains?

### Mechanism Compression

For a costly, expressive, or high-upside idea, recurse through:

1. `Verbal theory`: what claim or story makes this plausible?
2. `Mechanism hypothesis`: what process would make it work?
3. `Necessary implication`: if the mechanism is true, what must be observable?
4. `Cheapest proxy`: what plot, table, query, regression, test, log check, mock, or slice can measure that implication?
5. `Kill result`: what proxy result would downgrade or stop the idea?
6. `Scale trigger`: what proxy result justifies a fuller implementation?

If any answer is still vague, recurse once by naming the exact artifact, metric, slice, command, file, or decision. Do not build the expressive version until the cheap proxy survives.

### Levers And Options

Before broad exploration, name the levers:

- What can actually be changed: data, prompt, code path, algorithm, architecture, workflow, incentive, UI, narrative, threshold, or resource allocation?
- Which lever is cheapest to test?
- Which lever changes the abstraction level rather than decorating the current one?
- What known-strong incumbent, reference, or baseline should be replicated before mutation?

### Expert Archetypes

When the loop says "think like an expert", "Kaggle master", "senior engineer", "field practitioner", "reviewer", or similar, translate the archetype into practice:

- What would they inspect first?
- What artifact would they demand?
- What baseline, ablation, reference, or failure check would they run?
- What would make them reject this as noise?
- What exact next task follows?

Do not keep persona advice unless it becomes a concrete artifact or test.

### Definitions

Recurse on important nouns and adjectives:

- `similar`
- `robust`
- `strong`
- `clean`
- `novel`
- `practical`
- `good`
- `high quality`
- `domain-aware`

Ask what the term means for the current artifacts, metric, user, reviewer, system, or deployment context.

### Criteria

Recurse on success and failure criteria until they are operational:

- What numeric, qualitative, or review threshold matters?
- What comparison baseline is required?
- What slice, hard case, or external check can override the headline result?
- What result triggers exploit, mutate, park, kill, or abstraction escalation?

### Evidence Quality

When a result looks promising or disappointing, recurse on evidence quality:

- Is the evidence direct, proxy, anecdotal, local-only, or externally validated?
- What artifact produced it: test, log, benchmark, OOF file, screenshot, user feedback, review note, or reproducible output?
- What simpler baseline could make the gain look fake?
- What would show that the improvement transfers beyond the current case?

### Abstraction Level

When progress is marginal, ask whether the loop is changing the right kind of thing:

- `surface_patch`: wording, columns, parameters, local rules, styling, prompt phrasing
- `component`: module, feature family, data source, prompt block, model, section, workflow step
- `workflow`: end-to-end candidate generator, research design, user flow, review process, automation path
- `full_architecture`: alternate trunk, system design, solution family, narrative structure, operating model

If all current work is surface patches, recurse on what component, workflow, or full architecture would represent the domain idea more faithfully.

### Practices And Workflows

When a domain idea sounds like a workflow, do not test only one isolated piece.

Ask:

- What is the thinnest end-to-end version?
- What intermediate artifacts must it produce?
- Which ablation would prove the workflow matters?
- Which existing public, prior, or incumbent workflow should be reproduced before mutation?

### Failures

After a weak or surprising round, recurse on the failure reason:

- What assumption failed?
- Was this a root-cause miss, implementation miss, validation miss, transfer miss, or abstraction-level miss?
- Was the idea tested in its natural role?
- Was the abstraction level too low?
- Did validation fail, transfer fail, implementation fail, or only the chosen representation fail?
- What one diagnostic would separate these explanations?

### Dispatch Prompts

Before delegating or using `team-leader`, recurse until each child task has:

- one hypothesis
- one abstraction level
- one owned artifact or file area
- one falsification check
- one return contract

Avoid child prompts like "explore features", "think of improvements", or "try more configs".

## Output Shape

For each recursive pass, report:

- `Vague goal, symptom, fix, criterion, or claim`
- `First concretization`
- `Second concretization if needed`
- `Artifact or test`
- `Kill result`
- `Scale trigger`
- `Decision changed`
- `Dispatch-ready task`
- `Drop or keep`

## Guardrails

- Do not recurse for style. Recurse only where the answer could change work.
- Do not keep expert-flavored advice without an artifact, test, or refusal criterion.
- Prefer inspecting existing files, results, dashboards, and failures before asking the user.
- Keep the final portfolio narrow. Recursive thinking should sharpen fixes and branches, not multiply vague ones.
