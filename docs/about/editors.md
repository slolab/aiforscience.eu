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

## A worked example

[Pull request #6](https://github.com/slolab/aiforscience.eu/pull/6) is a small ingest end to end.
Follow it when material comes in.
The input was a news URL: a report that a company had spent about $1.8 million of frontier-model tokens on a bulk record-matching job that ran 860% over budget and never shipped.

The first decision is which tier the material belongs to, and most of it sits below a new practice.
A single incident is a reference work (`docs/library/ref-<slug>.md`), not a distilled source, and it grounds practices that already exist instead of earning a page of its own.
This one bore on [BP01](../best-practices/01-match-method-to-task.md), where a frontier model was chosen for bulk record matching, and on [BP04](../best-practices/04-govern-autonomy-and-accountability.md), where a budget existed on paper with nothing in the system enforcing it.
The gate in [How the record works](how-the-record-works.md) rules out the third option: a practice about controlling agent spend would not have been distinct from BP04.

The first commit was the whole ingest, across four files.
It added the reference page, a dated entry in the [failures log](../best-practices/failures.md), a line in the [library index](../library/index.md), and the atom-level edges in `docs/assets/provenance.yml`.
No practice page changed in that commit.

Two limits went on the reference page itself.
The source is out-of-domain corporate reporting, cited as external context, so the failure structure transfers to research and the setting does not.
The sourcing is secondary: the primary account is an internal company meeting, the original report is paywalled, the company confirmed it only in general terms, and outlets disagree on whether the 860% overrun and the $1.8 million project are one project or two.
The page therefore says the figures are reported rather than verified.
Do not publish an entry that hides either limit.

The most useful part of the ingest was the one edge that did not fit.
The BP04 atom `bp4-a3` listed permission scopes, autonomy limits, and shutdown paths, and an agent operating inside all three can still exhaust a budget, because a looping agent does not crash.
That edge was recorded as `qualifies` rather than forced into `supports`.
A second commit then extended the atom to name resource and spend caps, and carried the change through the Reasons, tab, and Example text, where the same enumeration recurs.
The atom kept its id: ids are stable handles and are not tied to wording.
Both edited practice pages got a dated change-history bullet.

When a source qualifies an atom instead of supporting it, the practice needs work.
Record the qualification, then fix the atom.
Do not file every source as support.

## Current editors

- Sebastian Lobentanzer, Helmholtz Munich.
