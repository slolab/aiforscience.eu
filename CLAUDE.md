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
- One sentence per line. Author prose with one sentence per source line and no
  fixed wrap width. Markdown collapses a single newline to a space, so this
  changes only the source (cleaner diffs, easier edits), never the rendered
  page. Keep a blank line between paragraphs; do not end a line with two
  trailing spaces or a backslash (either forces a hard line break). Lists,
  tables, and code blocks keep their own line structure.

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
layer: Operational | Method | Ecosystem   # internal only for now: not shown on pages, not in tags, not explained
hitl: mandatory | optional | in-process | final-check | n/a
tags: [<audience roles, one or more: practitioner/provider/governance>, <status>]
comments: true
---
```

Body sections, in this order, all present:

1. `## Practice` — the practice in two or three sentences, stated in
   audience-neutral terms. Spell out in plain words what it applies to (for
   example agents reaching databases, public endpoints, code, tools, and
   documents). Keep audience-specific advice and the word "you" out of this
   paragraph; that belongs in the tabs.
2. Three content tabs directly under the practice paragraph, with no heading
   (`=== "For practitioners"`, `=== "For providers"`, `=== "For governance"`),
   each two to four sentences adapting the practice to that role. Keep all three
   tabs even when one is thin; say plainly when a role is barely affected.
3. `## Reasons` — why the practice matters.
4. `## Examples` — concrete examples of what it looks like in practice.
5. `## Sources`
6. `## Change history` — dated bullets, newest first. Git log is the full record.

Status, endorsements, and the last-reviewed date come from the frontmatter and
render in the page's info rail ("About this practice"), so there is no metadata
admonition in the body.

Audiences (defined in docs/about/mission.md): **practitioners** (scientists
using agentic AI), **providers** (builders/operators of scientific services
and resources), **governance** (scientific management and leadership).
Pioneers/settlers is an operating principle for how the record is made, not
a taxonomy; never use it in tags or views.

Scope test for all content, including distillations: "Would adopting this
change how science is planned, performed, evaluated, communicated, or
governed?" Out-of-scope material (national economic/industrial policy,
energy, defence, treaties) is cited as context at most. Full statement in
docs/about/mission.md.

Status meanings: `draft` (proposed, under discussion), `reviewed` (accepted by
the editor group), `endorsed` (formally backed by at least one named
organisation or task force).

### Library pages (docs/library/)

The library is the provenance store for the practices. Everything used to model
a practice (whether it supported, qualified, or contradicted a claim) must be
findable here so a reader can check it. It has two tiers, one purpose.

**Distilled sources** (`docs/library/<slug>.md`). Rich documents reduced into
hooks and a practice mapping. Produced by the `distill` skill
(.claude/skills/distill/). Follow .claude/skills/distill/template.md. Raw
PDFs/docx are never committed; the distilled page with a full citation is the
durable artifact. `sources/inbox/` is a transient staging area only.

**Reference works** (`docs/library/ref-<slug>.md`). One file per standard,
paper, report, or guidance cited as point support. Bibliographic record only:
citation, type, stable link, a one-line "What it is", and a practice-level "Role
in the record". Follow .claude/skills/distill/reference-template.md. The
`ref_id` in the frontmatter is the join key. Both tiers are hidden from the nav
by the `not_in_nav: /library/*-*.md` rule and reached from the practices, the
library index, and the provenance data.

**Provenance data** (`docs/assets/provenance.yml`). The atom-level for/against
graph. Keyed by practice-atom id (`bp<N>-a<k>`) to a list of `{ref, stance,
locator, quote}`, where `stance` is `supports`, `qualifies`, or `contradicts`
and `ref` matches a `ref_id` or a distilled-source slug. This is the single
source of truth for which sources bear on which practice line, and the data a
future hover reads. Update it when an atom is added, split, reworded, or removed.

**Practice atoms.** Each `## Practice` statement is written one sentence per
line, wrapped in `<div class="afs-practice" markdown>` around a Markdown list.
Give each atom a stable id with `attr_list` (`{ #bp<N>-a<k> }`), so provenance
and the future hover can address it. Ids are stable handles, not tied to wording.

## Workflow

- Content changes go through PRs. CI runs a strict build and a link check.
- Editors review; a second editor merges anything that changes practice
  status or adds an endorsement.
- Monthly release: tag `vYYYY.MM`, write a GitHub Release summary, mirror it
  in docs/releases/index.md. Zenodo mints a DOI per release. On the 25th,
  `.github/workflows/release.yaml` runs `scripts/prepare_release.py` and opens
  `release: vYYYY.MM` with both drafts already written, or skips if nothing
  changed since the previous tag. Merging it tags the version at the merge
  commit (`release-tag.yaml`). Publishing the release is the human step, and it
  starts `release-doi.yaml`, which waits for the Zenodo mint and opens a second
  PR recording the DOI. The `release` skill (.claude/skills/release/) covers
  reviewing both PRs and preparing the release command.
