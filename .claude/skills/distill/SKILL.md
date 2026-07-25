---
name: distill
description: Distill a strategy document, report, or policy paper into a library entry for aiforscience.eu, with citations and mapping to the best practices. Use when a document lands in sources/inbox/ or when given a URL/DOI to ingest.
---

# Distill a document into a library entry

You turn a source document into a page under `docs/library/`, following
`template.md` in this directory. The distilled page is the durable artifact;
the raw document is never committed.

## Inputs

One of:

- a file in `sources/inbox/` (PDF, docx, or markdown),
- a URL or DOI provided by the user.

If the document is long, read all of it before writing. Distillation from a
partial read produces wrong emphasis.

## Scope filter

The record covers what changes how science is done. Apply this test to every
candidate hook (full statement in `docs/about/mission.md`):

> Would adopting this change how science is planned, performed, evaluated,
> communicated, or governed?

Keep: research workflows and methods; scientific services, data resources,
and infrastructure; provenance, citation, and evaluation of agentic systems;
research skills and training; governance of AI within scientific
institutions. Drop: national economic and industrial policy, energy and
compute geopolitics, security and defence, treaties. If dropped material
directly constrains scientific practice, mention it in one sentence under
"Cautions and gaps"; never distill it into hooks. When a document is largely
out of scope, say so in the Summary and keep the entry short.

## Procedure

1. Read the full document. Note its structure (sections, page numbers).
2. Read `docs/best-practices/index.md` and skim the individual practice pages
   so the mapping step is grounded in the current state of the record.
3. Create `docs/library/<slug>.md` from `template.md`. Slug: short,
   descriptive, with the publication year (example: `ec-expert-forum-2026`).
4. Fill every section of the template:
   - **Summary**: three to five declarative sentences. What the document
     says, who says it, why it matters for agentic AI in science.
   - **Hooks**: the passages that matter, numbered, each of which passed the
     scope filter. Each hook quotes or tightly paraphrases the source, gives
     a locator (section and page, like "§3.2, p. 20"), adds one sentence of
     relevance in neutral voice, and names the audiences it touches
     (practitioners, providers, governance). Aim for the 5 to 12 passages
     that carry the document's weight, not an outline of everything.
   - **Mapping to practices**: which hooks support which BP-nn, and where
     the document is in tension with a practice. Tensions are findings,
     not problems; state them plainly.
   - **Proposed changes to practices**: a checkbox list of concrete edits the
     document justifies (new practice, changed wording, added source, status
     change). Where a proposal creates or reworks a practice, draft the
     per-audience tab text ("What this means for you": Practitioners,
     Providers, Governance) as part of the proposal. These are proposals for
     human review. Never apply them to the practice pages yourself in the
     same session unless the user asks.
   - **Cautions and gaps**: what the document does not support, framings to
     avoid, honest limits.
6. Add the entry to the table in `docs/library/index.md` and to the `nav`
   section of `mkdocs.yml`.
7. If the source file was in `sources/inbox/`, delete it in the same branch.
8. Run `uv run mkdocs build --strict` and fix anything it reports.

## Style (hard rules)

- Follow the writing style section of the repository CLAUDE.md exactly: no
  em-dash asides, no "not just X but Y", no inflated adjectives, short
  declarative sentences.
- Neutral coalition voice. The entry serves all readers of the record, not
  one institution. No "we", "our institute", "our strategy".
- Quotes are verbatim and attributed with locators. Do not improve quotes.
- If the document is internal or confidential, stop and ask. Only public or
  explicitly cleared documents get library entries.

## Output

Report to the user: the new page path, the number of hooks, the proposed
practice changes (the checklist), and any tensions found. The user reviews
and opens the PR.
