# aiforscience.eu

Source for the AI for Science website: a living record of best practices for
applying agentic AI to science. MkDocs Material, deployed to GitHub Pages.

## Commands

- `uv sync` — install dependencies
- `uv run mkdocs serve` — local preview at http://127.0.0.1:8000
- `uv run mkdocs build --strict` — build; fails on broken internal links. Run before every PR.

## Writing style (hard rule)

All prose on this site follows these rules. They apply to every page, every
edit, and every AI-drafted distillation.

- No em-dash asides. Use a period, colon, comma, or parentheses.
- No "not just X but Y" constructions.
- No inflated adjectives or transitions ("crucial", "seamlessly", "robust" as filler).
- Short declarative sentences. Every word carries information.
- Neutral coalition voice. The site speaks for its contributors collectively,
  never for a single institution. No first-person institutional framing
  ("our institute", "our strategy").

## Content conventions

### Best-practice pages (docs/best-practices/NN-slug.md)

One page per practice. Frontmatter schema:

```yaml
---
title: <the practice, stated as an imperative>
practice_id: BP-NN
status: draft | reviewed | endorsed
first_added: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
endorsed_by:
  - <org or task force>
sources:
  - title: <source title>
    ref: <path under docs/, e.g. library/ec-expert-forum-2026.md, or URL>
    locator: "<section/page, e.g. §5.3, p. 28>"
layer: Operational | Method | Ecosystem
hitl: mandatory | optional | in-process | final-check | n/a
tags: [<audience: pioneer/settler/both>, <layer, lowercase>, <status>]
comments: true
---
```

Body sections, in this order, all present:

1. A metadata admonition at the top (status, endorsements, last reviewed).
2. `## Statement` — the practice in two or three sentences.
3. `## Why it matters`
4. `## What it looks like in practice` — concrete examples.
5. `## Sources`
6. `## Change history` — dated bullets, newest first. Git log is the full record.

Status meanings: `draft` (proposed, under discussion), `reviewed` (accepted by
the editor group), `endorsed` (formally backed by at least one named
organisation or task force).

### Library pages (docs/library/)

Distilled source documents. Produced by the `distill` skill
(.claude/skills/distill/). Follow .claude/skills/distill/template.md. Raw
PDFs/docx are never committed; the distilled page with a full citation is the
durable artifact. `sources/inbox/` is a transient staging area only.

## Workflow

- Content changes go through PRs. CI runs a strict build and a link check.
- Editors review; a second editor merges anything that changes practice
  status or adds an endorsement.
- Monthly release: tag `vYYYY.MM`, write a GitHub Release summary, mirror it
  in docs/releases/index.md. Zenodo mints a DOI per release.
