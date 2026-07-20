# My Knowledge Base Paper Conventions

Use the live `AGENTS.md` in the knowledge-base root as the authority. These are
the stable paper-ingest conventions observed on 2026-07-20.

## Root and layout

Default root:

`/Users/lizhi/Downloads/local_projects/my-knowledge-base`

The fallback root is `~/local_projects/my-knowledge-base`. Prefer an explicit
user path or `MY_KNOWLEDGE_BASE_ROOT` when either is supplied.

- Canonical PDF default: `static/papers/<BibTeX-key>.pdf`
- Optional journal-coded PDF for this workflow:
  `static/papers/<BibTeX-key>-<journal-code>.pdf`
- Paper page: `content/papers/<BibTeX-key>/index.md`
- The page folder and `pageID` stay equal to the exact BibTeX key even when the
  PDF has a journal suffix.
- Do not edit `public/` or the theme submodule.

## Paper page

Use YAML front matter with `abstract`, not `description`:

```markdown
---
title: "Human-readable paper title"
subtitle: ""
date: 2026-07-20T00:00:00Z
draft: false
abstract: "One-sentence summary."
link: "https://doi.org/..."
pageID: "citationKey"
bibtex: >
    @article{citationKey,
    title={...},
    author={...},
    year={...}
    }
tags: [topic]
---

{{< paperPDF filename="citationKey-JOURNAL.pdf" height="800px" >}}

## Takeaways

## Research question and contribution

## Data and setting

## Method

## Main findings

## Caveats and questions

## Q&A
```

Omit empty analytical sections rather than filling them with generic prose.
Keep `## Takeaways` and `## Q&A`. Start headings at `##`, never `#`.

## Journal suffix policy

A journal code is optional. Apply one only when it is explicit or confidently
established by nearby filenames. Never change the BibTeX key, page folder, or
`pageID` to include the code.

The live project otherwise defines `<key>.pdf` as canonical and reserves
`<key>_wp.pdf`, `<key>_v1.pdf`, and `<key>_r1.pdf` for working-paper or revision
history. Treat the hyphenated journal code as an opt-in extension requested by
the user, not as a version marker.

Precedence:

1. An explicit code supplied by the user.
2. An exact journal-name match already used consistently in the user's paper
   store.
3. The starter mapping below.
4. No suffix when the venue is absent or ambiguous.

Starter codes observed in the broader paper store:

| BibTeX journal or venue | Code |
|---|---|
| American Economic Review | `AER` |
| American Economic Review: Papers and Proceedings | `AERPP` |
| Econometrica | `ECMA` |
| European Journal of Operational Research | `EJOR` |
| Journal of Accounting and Economics | `JAE` |
| Journal of Economic Perspectives | `JEP` |
| Journal of Finance | `JF` |
| Journal of Financial Economics | `JFE` |
| Journal of Financial and Quantitative Analysis | `JFQA` |
| Journal of International Economics | `JIE` |
| Journal of Political Economy | `JPE` |
| Management Science | `MS` |
| Manufacturing & Service Operations Management | `MSOM` |
| Operations Research | `OR` |
| Production and Operations Management | `POMS` |
| Quarterly Journal of Economics | `QJE` |
| Review of Economic Studies | `RES` |
| Review of Economics and Statistics | `reStat` |
| Review of Finance | `RF` |
| Review of Financial Studies | `RFS` |
| NBER working paper | `NBER` |
| SSRN working paper | `SSRN` |
| Other working paper | `WP` |

Treat `OR-SM` and similar suffixes as supplemental-material labels, not the
default code for a main paper. Do not propagate legacy `*` characters into new
filenames.

## Collision rules

- Never overwrite a PDF or `index.md`.
- If the same key and same PDF bytes already exist, reuse the existing PDF
  filename and do not create a second copy.
- If the same key points to different PDF bytes, stop that item and ask the user
  whether this is a revision, supplement, or mistaken pairing.
- If `index.md` already exists, preserve all notes. Merge only requested missing
  metadata or sections with a targeted edit.
- Before a batch mutation, validate all input pairs and destinations. A single
  unresolved collision blocks the batch unless the user explicitly asks to run
  the clean subset.
