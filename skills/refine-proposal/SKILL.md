---
name: refine-proposal
description: Build, interrogate, and iteratively improve any proposal through exploratory questions, an interactive HTML review artifact, anchored element-level question threads, documented answers and responses, and versioned HTML snapshots. Use when a user has a proposal draft or idea for research, grant, product, policy, business, nonprofit, or internal planning work and wants Codex to ask clarifying questions, produce an HTML proposal artifact, let reviewers question any part of it, document those responses, update the proposal, and save each revision.
---

# Refine Proposal

## Overview

This skill turns proposal development into a reviewable artifact loop. It helps Codex ask the right exploratory questions, create an interactive HTML proposal, collect anchored questions on any proposal element, document responses, revise the proposal, and preserve each version.

## Workflow

Use this sequence unless the user explicitly asks for only one piece.

1. `Intake`
2. `Exploration Questions`
3. `HTML Artifact`
4. `Anchored Review`
5. `Response Documentation`
6. `Revision`
7. `Version Snapshot`

Do not skip version snapshots when modifying an existing artifact.

## Intake

First identify the proposal type and decision context.

- `proposal type`: research, grant, product, policy, business, nonprofit, internal plan, or other
- `audience`: funder, advisor, reviewer, executive, customer, committee, or public reader
- `decision`: approval, feedback, funding, prioritization, recruitment, alignment, or implementation
- `current state`: raw idea, notes, partial draft, full draft, or revised artifact
- `constraints`: deadline, format, length, evidence, budget, methods, politics, or reviewer expectations

If the user has supplied only a rough idea, ask 1 to 3 high-value questions before drafting. If the user asks for a fuller exploration, ask up to 7 questions grouped by purpose.

## Exploration Questions

Ask questions that expose the proposal's logic, not generic preferences.

- What decision should this proposal make easier?
- Who must be convinced, and what do they currently doubt?
- What claim is the proposal making?
- What evidence, precedent, prototype, data, or example supports the claim?
- What is out of scope?
- What would make the proposal fail?
- What must be true for the proposal to be worth pursuing?

After the user answers, create an `Exploration Answer Ledger` with:

- `question`
- `user answer`
- `agent inference`
- `impact on proposal`
- `open follow-up`

Keep stated user answers separate from agent inferences.

## HTML Artifact

Create or update a self-contained HTML file using `assets/interactive-proposal-template.html` as the starting point. The artifact must include:

- proposal title, version, date, and status
- proposal abstract and short project synopsis
- motivation, puzzle, and benchmark literature
- research questions and hypotheses
- institutional setting and source of variation
- data, linkage, and measurement plan
- treatment definitions and controls
- identification and empirical strategy
- outcomes, mechanisms, and heterogeneity
- validity threats, interpretation tree, and execution roadmap
- project-specific extensions such as theory, institutional detail, data construction, measurement validation, qualitative evidence, ethics, simulations, or field-specific appendices when the project needs them
- exploration answer ledger
- anchored question and response ledger
- revision notes

Use a document-first layout by default. Avoid turning every proposal component into a separate card; use paragraphs, definition lists, section rules, tables, and a slim review rail so the artifact reads like a research proposal rather than a dashboard.

Keep the template flexible. Treat the required regions as the default spine, not a fixed cage. Rename sections, remove irrelevant rows, and add project-specific extension modules when they clarify the proposal's actual research logic. Do not add extensions as filler; each extension should support the question, setting, evidence, design, interpretation, or feasibility.

Every meaningful heading, paragraph, list item, table cell, figure caption, and proposal block must have a stable `data-qa-id`. Use short semantic identifiers such as `claim-main`, `evidence-budget-1`, or `risk-adoption`.

Read `references/html-artifact-contract.md` before building or revising the artifact.

## Anchored Review

The HTML artifact must let a reviewer click or select text inside the proposal body and add a question thread anchored to that element. The bundled template does this with browser-local JavaScript and supports:

- element click targeting
- text selection targeting
- question entry
- response or decision entry
- status tracking
- import and export of annotation JSON
- copyable prompt text for bringing reviewer questions back to Codex

Static HTML cannot safely write new files to disk from the browser. Treat exported annotation JSON or pasted question text as the bridge back into Codex.

## Response Documentation

When the user returns reviewer questions, exported annotations, or free-form responses:

1. Match each question to its `data-qa-id` or nearest proposal section.
2. Record the question, response, decision, and status in the artifact ledger.
3. Mark whether the proposal text was revised, left unchanged, or parked.
4. Preserve unresolved questions in a visible `Open Issues` area.
5. Separate reviewer questions from user answers and agent decisions.

The ledger is not a substitute for revision. For every answered or revised question, first update the relevant proposal passage, table row, figure note, roadmap item, or section summary. Then update the ledger to document what changed. Use ledger-only responses only when the question is genuinely administrative, already answered in the body, or explicitly parked.

Do not silently resolve an anchored question by rewriting text without documenting the response.

Preserve unrelated content. Do not rewrite sections, paragraphs, tables, or wording that did not receive questions unless they directly depend on a questioned part and would otherwise become inconsistent. When a dependent update is necessary, keep it narrow and name the dependency in the revision notes.

## Revision

Revise the proposal to address documented questions.

- Strengthen unclear claims.
- Add missing evidence or mark evidence as needed.
- Narrow scope when objections reveal overreach.
- Add assumptions, risks, or validation steps when the proposal depends on uncertain facts.
- Preserve the proposal's intended audience and decision context.
- Preserve unaffected proposal content exactly where practical; avoid stylistic rewrites, broad cleanup, or opportunistic restructuring outside the questioned areas.
- Keep a visible revision note for every substantive change.

When prior decisions exist only in a response ledger, migrate them into the proposal sections they affect before saving the next version. Examples: target-audience decisions should update the synopsis or contribution; method decisions should update the design section; data-sequencing decisions should update the data plan and roadmap; go/no-go decisions should update feasibility, validity, or execution text.

When a question reveals a contradiction, fix the contradiction directly and record the prior inconsistency in the revision notes.

## Version Snapshots

Use `scripts/save_version.py` to preserve each HTML version.

Recommended session layout:

```text
proposal-review/
  current.html
  annotations/
  versions/
    manifest.json
    proposal_v001.html
    proposal_v002.html
```

After creating `current.html`, immediately save it as `v001`:

```bash
python3 skills/refine-proposal/scripts/save_version.py proposal-review proposal-review/current.html --label "initial artifact"
```

Before revising an existing artifact, ensure the current state is already captured in `versions/`. After revising, save the new artifact as the next version:

```bash
python3 skills/refine-proposal/scripts/save_version.py proposal-review proposal-review/current.html --label "address reviewer questions"
```

In the final response, report the current HTML path and the newest version snapshot.

## Resource Guide

- `assets/interactive-proposal-template.html`: self-contained review UI for anchored questions and response documentation.
- `references/html-artifact-contract.md`: artifact structure, annotation schema, and revision protocol.
- `scripts/save_version.py`: copy an HTML artifact into `versions/` and update `manifest.json`.
