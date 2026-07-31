---
title: Become an editor
---

# Become an editor

Agentic AI is changing extremely fast; most papers are outdated when they come out.
For best practices, a typical white paper or peer-reviewed manuscript is no longer suitable.
Practitioners, developers, and decision-makers need up-to-date guidance in real time.

This site proposes to be a mechanism for maintaining a shared record of best practices.
The number of practices is limited; each claim can be traced to a source, can be revised, and is snapshotted monthly with a DOI.
Input is open: anyone can propose or challenge.
Output is curated by a small editor group.
The process is described in [How the record works](how-the-record-works.md), governance in [Governance](governance.md).

## Editorial tasks

- Review incoming proposals and challenges, and decide whether a submission becomes a practice, is integrated into an existing practice, or is declined with a stated reason.
- Distill submitted documents into library entries with quotes and locators.
  Drafting is AI-assisted; the editor is accountable for all decisions.
- Keep practices current: update the review date, move status from draft to reviewed, record endorsements.
- Provide a second review to change status to reviewed.

Editors do not own practices individually, and editing does not commit their institution to anything.
Endorsement by an organisation is a separate, formal step (see [Partners](partners.md)).

## Requirements

- A few hours a month: review a proposal, challenge, or document, plus the monthly call (as availability allows).
- A response time of less than two weeks on anything in your area, or a note that you cannot take it.
- A GitHub account and enough comfort with pull requests to review a diff.
- Any relevant working knowledge of agentic AI in a scientific setting (application, development, or governance).

## Credit

Editors are named on this page and in the repository.

## How to join

1. Read [Mission](mission.md), [How the record works](how-the-record-works.md), and [Governance](governance.md).
   Fifteen minutes.
2. Familiarise yourself with the practice pages and the library system (how practice sources are cited).
3. Make a contribution.
   Challenge a practice you disagree with, submit a relevant document that is not yet represented, or propose a practice, through the [issue templates](https://github.com/slolab/aiforscience.eu/issues/new/choose).
4. Say that you want to edit.
   Open a thread in [Discussions](https://github.com/slolab/aiforscience.eu/discussions) or write to [aiforscience@googlegroups.com](mailto:aiforscience@googlegroups.com).
   State which group you come from, which audiences and practices you can cover, and how much time you have.
5. The editors add you: repository write access and your name on this page.

## Conventions

The repository's [CLAUDE.md](https://github.com/slolab/aiforscience.eu/blob/main/CLAUDE.md) is the practice document for the page structure, the practice metadata schema, and the writing style rules.
You can run the instructions with any agent or follow them manually.
Run `uv run mkdocs build --strict` before every pull request to detect broken internal links.

If you want to use the AI-assisted distillation of a document, drop it into `sources/inbox/` and ask an agent for a distillation.
It will use the repository skill to draft the library entry and propose changes (update practice, add practice, etc).
The editor checks every quote and change recommendation against the original and confirms the final state.
Raw files should not be committed; all that remains should be the library entry and practice updates.

## Editor workflow example

[Pull request #6](https://github.com/slolab/aiforscience.eu/pull/6) is a small ingest end to end.
The input was a news article of a relevant event (massive overspending due to missing guardrails and incentive misalignment).

The instruction was: "Ingest this source and, if relevant, prepare a PR."

The first commit was the whole ingest, automatically done by Claude (Opus 5).
It added the reference page, a dated entry in the [failures log](../best-practices/failures.md), a line in the [library index](../library/index.md), and the atom-level edges in `docs/assets/provenance.yml`.

The PR message flagged a checklist of proposed but not enacted changes. The editor chose to implement the first two (update the wording of a practice atom and replace a synthetic example by this real one).
A second commit then extended this practice.
Both edited practice pages got a dated change-history bullet.
On approval, the PR was merged, triggering an update to the website.

## Current editors

- Sebastian Lobentanzer, Helmholtz Munich.
