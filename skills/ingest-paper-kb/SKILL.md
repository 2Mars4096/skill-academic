---
name: ingest-paper-kb
description: "Ingest one or many local academic-paper PDFs plus user-supplied Google Scholar BibTeX entries into Lizhi's Hugo my-knowledge-base: pair and validate batch inputs, move and rename PDFs by BibTeX key with an optional established journal-code suffix, skim each paper, and create or safely enrich the citation-key paper page with front matter, an exact paperPDF embed, and evidence-based reading notes. Use when the user asks to organize, import, catalog, skim, or take notes on paper PDFs for this specific knowledge-base project, whether singly or in batches."
---

# Ingest Paper KB

Ingest local papers into the `my-knowledge-base` PDF library and paper-note
bundles without losing files or existing notes. Treat the user-supplied BibTeX
entry as the citation-key authority and the PDF as the paper-content authority.

## Resolve the project

Resolve the knowledge-base root in this order:

1. A root explicitly supplied by the user.
2. `$MY_KNOWLEDGE_BASE_ROOT`.
3. `/Users/lizhi/Downloads/local_projects/my-knowledge-base`.
4. `~/local_projects/my-knowledge-base`.

Require both `static/papers/` and `content/papers/`. Read the root `AGENTS.md`
completely before inspecting or changing project files; it overrides this skill
when conventions evolve. Read
[references/project-conventions.md](references/project-conventions.md) when
assigning a journal suffix, resolving a collision, or when the live instructions
are absent or ambiguous.

Do not use `static/papers` as the Markdown location. The canonical pair is:

- `static/papers/<key>[-<journal-code>].pdf`
- `content/papers/<key>/index.md`

## Intake one paper or a batch

Collect one record per paper:

- absolute or `~`-relative local PDF path
- complete Google Scholar BibTeX entry
- optional journal code, tags, canonical link, or note emphasis

Accept records in prose, numbered blocks, a Markdown table, or JSON. When the
user gives separate PDF and BibTeX lists, pair by position only if their counts
match and the PDF title/authors agree with the corresponding BibTeX entry.
Otherwise, stop before mutations and ask for the ambiguous mapping. Never search
Google Scholar merely to replace BibTeX the user already supplied.

For each entry, extract the exact citation key from `@type{key,`. Keep that key
unchanged as the folder name and `pageID`. Check title, authors, and year against
the PDF's first pages; flag a mismatch instead of silently ingesting it. Supply a
human-readable `title` override in the manifest when the BibTeX title contains
LaTeX commands or accents that should not appear in Hugo front matter.

## Choose the PDF filename

The live project's canonical default is `<key>.pdf`. Treat `-<journal-code>` as
the opt-in extension requested for this workflow. Add it only when the user asks
for journal suffixes, gives a code, or a consistent nearby naming pattern makes
that preference clear and an exact venue-to-code mapping is established. Inspect
nearby PDFs before deciding. Omit the suffix when uncertain; do not invent
abbreviations. Keep the project's underscore suffixes such as `_wp`, `_v1`, and
`_r1` reserved for noncanonical paper versions.

The optional suffix changes only the PDF filename and shortcode:

```text
static/papers/smith2024inventory-MSOM.pdf
content/papers/smith2024inventory/index.md
pageID: "smith2024inventory"
{{< paperPDF filename="smith2024inventory-MSOM.pdf" height="800px" >}}
```

## Preflight the whole batch

Build a temporary JSON manifest and run
`scripts/ingest_papers.py <manifest.json>` from this skill directory. Planning is
the default and changes nothing. Use this schema:

```json
{
  "kb_root": "/Users/lizhi/Downloads/local_projects/my-knowledge-base",
  "papers": [
    {
      "pdf": "/absolute/path/to/download.pdf",
      "bibtex": "@article{smith2024inventory,\n  title={...},\n  author={...},\n  journal={...},\n  year={2024}\n}",
      "journal_code": "MSOM",
      "abstract": "One-sentence summary for the page listing.",
      "link": "https://doi.org/...",
      "tags": ["inventory", "supply-chain"],
      "notes_markdown": "## Takeaways\n\n- ...\n\n## Q&A"
    }
  ]
}
```

For the first preflight, `abstract`, `tags`, and `notes_markdown` may be absent.
Resolve every reported mismatch or collision before skimming and applying. The
script refuses existing Markdown and different-content PDFs for the same key.
Do not bypass that guardrail with manual overwrite commands.

## Skim each paper

Use the available PDF extraction and rendering workflow. Extract text with page
anchors; visually inspect pages when tables, figures, equations, or extraction
quality matter. For a normal skim, read:

1. title page and abstract
2. introduction and stated contribution
3. data/setting and research design or model
4. main tables and figures
5. conclusion
6. mechanism, robustness, or appendix only as needed to understand the result

Write compact, evidence-based notes. Separate the authors' claims from your own
assessment. Include page, section, table, or figure anchors for non-obvious
details. Never infer unreadable numbers or equations. If the PDF is scanned or
malformed, try OCR/rendering; if it remains unreadable, report the limitation and
do not fabricate a skim.

Use these body sections when supported by the paper, omitting empty analytical
sections:

- `## Takeaways`: 3–7 high-value bullets, starting with the central question and
  answer
- `## Research question and contribution`
- `## Data and setting`
- `## Method`
- `## Main findings`
- `## Mechanisms and interpretation`
- `## Caveats and questions`
- `## Q&A`: preserve as the user's space for ongoing notes

Reuse established knowledge-base tags when possible. Prefer 2–5 substantive
tags; do not produce a large speculative tag list. Put a one-sentence neutral
summary in front-matter `abstract`.

## Apply and verify

Add the finished `abstract`, `tags`, and `notes_markdown` to the manifest. Run the
planner again. After it reports a clean plan, run:

```bash
python scripts/ingest_papers.py <manifest.json> --apply
```

This safely copies and verifies new PDFs before deleting their original paths.
Use `--copy` only when the user wants to retain the source files. A batch with
any error changes nothing. If the user explicitly wants the clean subset, make a
new manifest containing only those records and plan it again.

Verify every item after applying:

- the source was moved, unless copy mode was requested
- the PDF exists under `static/papers/`
- `content/papers/<key>/index.md` exists
- folder name, `pageID`, and BibTeX key match exactly
- `paperPDF` names the actual PDF, including any suffix
- front matter uses `abstract`, not `description`
- headings start at `##`
- the BibTeX entry remains complete

When Hugo is available, build to a temporary destination so validation does not
edit tracked content or `public/`. Report a concise per-paper table with key,
PDF filename, Markdown path, journal code, and status.

## Existing paper pages

If `content/papers/<key>/index.md` already exists, do not use the batch script to
replace it. Inspect its PDF shortcode and current notes. Reuse the existing PDF
when it matches, then make only targeted edits the user requested: fill blank
metadata, correct the embed, or append/merge skim sections while preserving all
prior notes. If the existing PDF differs, ask whether it is a revision,
supplement, or pairing error.

## Guardrails

- Never overwrite or delete an existing destination file.
- Never change a Google Scholar BibTeX key merely to make a filename prettier.
- Never append a journal code to the folder or `pageID`.
- Never edit `public/` or the theme submodule.
- Never claim a paper was skimmed unless its relevant PDF pages were read.
- Keep each PDF paired with exactly one BibTeX entry throughout a batch.
