---
title: State human-in-the-loop requirements explicitly
nav_title: "BP09 State human-in-the-loop requirements"
practice_id: BP-09
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Best Practice, item 7"
  - title: "Agentic AI in the higher-education system (2026)"
    ref: library/hfd-agentic-ai-hochschulsystem-2026.md
    locator: "§4.1 and §6, hooks 3 and 11"
  - title: "EU AI Act, Article 14 (human oversight)"
    ref: library/ref-eu-ai-act.md
    locator: "oversight must be effective; automation bias named"
  - title: "NIST Generative AI Profile (AI 600-1, 2024)"
    ref: library/ref-nist-ai-rmf.md
    locator: "oversight calibrated to risk"
  - title: "Elish, Moral Crumple Zones (Engaging Science, Technology, and Society, 2019)"
    ref: library/ref-elish-2019.md
    locator: "the nominal human absorbs blame for uncontrollable systems"
  - title: "Green, The Flaws of Policies Requiring Human Oversight of Government Algorithms (2022)"
    ref: library/ref-green-2022.md
    locator: "human-oversight mandates often fail to deliver"
layer: Operational
hitl: in-process
tags: [practitioner, provider, governance, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- Every [agent](../glossary.md#agent) use case should state its [human-in-the-loop](../glossary.md#hitl) (HITL) level plainly.
  { #bp9-a1 }
- HITL involvement can be mandatory or optional; it can range between tight in-process control and a mere final check.
  { #bp9-a2 }
- A workflow stating no HITL involvement means it has full autonomy.
  { #bp9-a3 }
- Left unstated, no one knows where a person is required and where the agent acts alone.
  { #bp9-a4 }
- Stating the level is necessary, but not sufficient: the check has to be designed so it actually works in deployment.
  { .afs-practice__pivot #bp9-a5 }
- HITL engagement provenance should be recorded according to [BP07](07-provenance-and-citation.md).
  { #bp9-a6 }

</div>

=== "For practitioners"

    Know the HITL level of the agent workflows you use, and do not assume a check that has not been stated.
    For anything that changes results or affects others, keep a real human decision point even if the tool lets you skip it.
    Do not automate approval; acceptance without scrutiny is not oversight.

=== "For providers"

    State the HITL level for each use case you support, and build the check into the workflow; do not count on the user to remember or even know.
    Match the check to the stakes, have the system enforce the stated level, and design the check so the human can actually understand and override the output.
    Try to facilitate understanding and to prevent "just clicking approve."

=== "For governance"

    Stated HITL levels make oversight auditable.
    Require each use case to declare its level and enforce it.
    Make stronger checks mandatory where actions have real consequences.
    Test that the oversight works in practice rather than assuming a named reviewer is enough.
    This includes peer-review integrity: confidential manuscripts should not be uploaded to external models, and reviewer AI use should be declared.

## Reasons

How much oversight is right depends on the use case.
A low-stakes lookup and an action that changes a record or a result do not need the same check.
If the level is unstated, oversight is left to chance, which is neither reliable nor checkable.
But a stated level is not a guarantee.
There is strong evidence that human oversight often fails in practice: people defer to plausible-looking output (automation bias), rubber-stamp at scale, and can be left holding blame for systems they could not realistically control (for instance, due to volume).
So the check must be designed for effectiveness, giving the human what they need to understand and override.
Pipelines need to be assessed for realistically achievable volumes.
The four labels used here (mandatory / optional, in-process / final check) are a useful shorthand, not settled standards.
Agent autonomy is a spectrum from tight supervision to full autonomy.
Stating and enforcing HITL levels fulfils part of [BP04](04-govern-autonomy-and-accountability.md) at the single use case level.

## Examples

- A workflow never states its HITL level; each user assumes someone else checks, and an unreviewed agent edit reaches a shared record.
- Every use case instead declares its level from a short list (mandatory, optional, in-process, final check), and a workflow that declares none is understood to run at full autonomy, so the choice is explicit.
- A pipeline has a mandatory "human approves each item" step, but at hundreds of items an hour the reviewer clicks approve without reading; the check exists on paper and fails in practice.
- The check is designed so the human can actually judge: it shows what changed, at a realistic volume, with approve, edit, veto, and stop, and the strength of the check is set by the stakes.
- The stated level is enforced by the system rather than left to habit, which ties it to the guardrails in [BP04](04-govern-autonomy-and-accountability.md), and the HITL engagement is recorded in provenance ([BP07](07-provenance-and-citation.md)) so oversight is auditable instead of assumed.
- A reviewer uploads a confidential manuscript to an external model against the stated boundary of the conference for a high-stakes task. They submit the AI-generated review without declaring the AI use. The conference had inserted a [prompt injection](../glossary.md#prompt-injection) into their review version and catches the reviewer with the prompted output form. The reviewer is barred from conference participation for two years.

## Sources

- [ELIXIR TF Agentic AI: agenda and rolling best practice (2026)](../library/elixir-tf-agentic-ai-2026.md), Best Practice item 7.
- [Agentic AI in the higher-education system (2026)](../library/hfd-agentic-ai-hochschulsystem-2026.md), §4.1 (explicit intervention points) and §6 (defined escalation and control).
  Consistent with, grounding only.
- [EU AI Act, Article 14](../library/ref-eu-ai-act.md) and [NIST Generative AI Profile (AI 600-1)](../library/ref-nist-ai-rmf.md).
  Oversight must be effective and calibrated to risk; Article 14 names automation bias as a hazard the overseer must be able to counter.
- [Elish, Moral Crumple Zones (2019)](../library/ref-elish-2019.md) and [Green, Flaws of Policies Requiring Human Oversight (2022)](../library/ref-green-2022.md).
  Evidence that human oversight frequently fails in practice; a stated level must be designed for effectiveness.

## Change history

- 2026-07-27: Renumbered from BP08 to BP09 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including anti-patterns (unstated level, rubber-stamping at volume), replacing restatements of the practice.
- 2026-07-26: Renumbered from BP08 to BP09 in the reordering.
  Added grounding (EU AI Act Article 14, NIST AI 600-1) and a caveat that a stated level is necessary but not sufficient (automation bias, rubber-stamping, moral crumple zones; Elish 2019, Green 2022), plus a peer-review confidentiality instance.
- 2026-07-25: Created from the ELIXIR TF distillation (hook 8), grounded in the HFD paper.
