# HTML Artifact Contract

Use this contract when creating or revising an interactive proposal artifact for `refine-proposal`.

## Required Files

Recommended session layout:

```text
proposal-review/
  current.html
  annotations/
    annotations_v001.json
  versions/
    manifest.json
    proposal_v001.html
```

`current.html` is the editable working artifact. `versions/` contains immutable snapshots. `annotations/` stores exported browser annotations when the user provides them.

## Required HTML Regions

The generated artifact must include these semantic regions:

- `proposal meta`: title, version, date, owner or audience, and status
- `proposal synopsis`: abstract, question, contribution, design, and main risk
- `motivation and benchmark`: motivating problem, puzzle, closest literature or decision benchmark, and contribution claim
- `research questions`: primary and secondary questions with hypotheses
- `setting and variation`: institutional details, treatment timing, unit, and exogeneity limit
- `data and linkage`: sources, units, fields, construction burden, and linkage design
- `treatment and controls`: baseline exposure, mechanism-specific shocks, unexpected assignment, and best comparison groups
- `identification and strategy`: event-study or equivalent evidence statement, assumptions, local comparisons, and scope of claim
- `outcomes and mechanisms`: main outcomes, mechanism outcomes, and heterogeneity dimensions
- `validity and interpretation`: threats, planned responses, positive/null/mixed result interpretation, and execution roadmap
- `project-specific extensions`: optional theory, institutional, data construction, measurement, qualitative, ethics, simulation, appendix, or field-specific modules when they are needed for the actual proposal
- `exploration answer ledger`: initial questions, user answers, agent inferences, and impact on the draft, when available
- `question response ledger`: anchored reviewer questions, responses, decisions, and status
- `revision notes`: version-to-version change history

Use a document-first layout unless the user's project already requires a dashboard. Favor sections, readable paragraphs, definition lists, and tables over repeated cards. Visual notation is useful only when it clarifies the research logic.

The required regions are a research-proposal spine, not a rigid outline. Adapt section names, table rows, and optional modules to the project's discipline, method, evidence, and audience. Remove irrelevant placeholders. Add extensions only when they help readers understand the research question, empirical setting, data construction, theory, validity, ethics, feasibility, or interpretation.

Use the bundled HTML template unless the user's project already has an established frontend.

## Element Targeting Rules

Every reviewable element inside the proposal body must have a stable `data-qa-id`.

Good identifiers:

- `claim-main`
- `audience-reviewers`
- `evidence-budget-1`
- `method-sample`
- `risk-compliance`
- `timeline-phase-2`

Avoid generated IDs such as `p1` when semantic names are practical. Do not change a `data-qa-id` across versions unless the underlying idea has been removed or split. If content is split, note the old and new IDs in revision notes.

## Annotation Schema

The template exports annotations in this shape:

```json
{
  "schemaVersion": 1,
  "documentId": "proposal-review",
  "version": "v001",
  "threads": [
    {
      "id": "thread-...",
      "targetId": "claim-main",
      "targetLabel": "Main Claim",
      "selectedText": "exact selected phrase if any",
      "question": "What evidence supports this claim?",
      "response": "User or agent response and decision.",
      "status": "open",
      "createdAt": "2026-05-26T00:00:00.000Z",
      "updatedAt": "2026-05-26T00:00:00.000Z"
    }
  ]
}
```

Allowed status values:

- `open`
- `answered`
- `revised`
- `parked`

## Revision Protocol

When the user returns annotations or asks for updates:

1. Parse or summarize all question threads.
2. Group threads by `targetId`.
3. Decide whether each thread requires a text change, a ledger-only answer, a parked issue, or a user follow-up.
4. Update the proposal body first. The revised body should directly reflect resolved decisions in the affected synopsis, question, data, design, outcome, validity, extension, or roadmap section.
5. Preserve all unrelated content. Do not rewrite unqueried sections unless they directly depend on a questioned section and would otherwise become inaccurate or inconsistent.
6. Update the static question response ledger in the HTML after the body changes are made.
7. Update revision notes with the new version label, concrete changes, and any dependent sections touched.
8. Save a new version snapshot with `scripts/save_version.py`.

Do not leave resolved decisions only in the ledger. Ledger-only answers are acceptable only for administrative notes, already-addressed questions, or deliberately parked issues. If a previous version has a "resolved decisions" table, migrate each decision into the relevant proposal text before creating the next snapshot.

Avoid broad restyling, simplification, reorganization, or copyediting during a question-response revision pass. That kind of holistic rewrite should happen only when the user explicitly asks for it.

Do not erase old resolved threads unless the user explicitly asks for a cleaned public copy. For working review artifacts, preserve the audit trail.

## Quality Checks

Before handing the artifact back:

- Open or inspect the HTML enough to ensure the required regions exist.
- Confirm there are stable `data-qa-id` attributes in the proposal body.
- Confirm the annotation script is present.
- Confirm the newest HTML was saved in `versions/`.
- Confirm `versions/manifest.json` has the newest entry.
- Report unresolved questions separately from completed revisions.
