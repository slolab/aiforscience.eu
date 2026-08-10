---
title: Govern agent autonomy and accountability
nav_title: "Govern agent autonomy and accountability"
practice_id: BP-04
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "Agentic AI in the higher-education system (2026)"
    ref: library/hfd-agentic-ai-hochschulsystem-2026.md
    locator: "§4-6, hooks 3, 5, 6, 7, 9, 10, 11, 12"
    note: 'The "from guidelines to guardrails" framing is quoted at §5.2. That quotation is attributed in the source paper to "Kassorla et al. (2026)", a reference we could not verify as a published work; the underlying point is independently supported by the frameworks below, which is what this practice relies on.'
  - title: "EU Expert Forum on Frontier AI (2026)"
    ref: library/ec-expert-forum-2026.md
    locator: "§4.2.3, hooks 1 and 3"
    note: "§4.2.3 (independent audit, evaluation and verification capacity). Consistent with, grounding only."
  - title: "NIST AI Risk Management Framework (AI 100-1, 2023) and Generative AI Profile (AI 600-1, 2024)"
    ref: library/ref-nist-ai-rmf.md
    locator: "GOVERN function; system inventory; stop-build authority"
    note: "GOVERN roles and accountability, a documented system inventory, and stop-build authority."
  - title: "EU AI Act, Articles 14 and 26"
    ref: library/ref-eu-ai-act.md
    locator: "human oversight; deployer duties"
    note: "Named natural persons for oversight and deployer duties."
  - title: "EU AI Omnibus (2026)"
    ref: library/ai-omnibus-2026.md
    locator: "Art 5(1a)(a)(ii); Recital 12 (foreseeable-misuse standard)"
    note: "Art 5(1a)(a)(ii). A provider is responsible where a prohibited output is a reasonably foreseeable and reproducible outcome absent adequate technical safeguards, which places the limit in the system rather than in policy (bp4-a1)."
  - title: "OECD AI Principles (2019, updated 2024)"
    ref: library/ref-oecd-ai-principles-2024.md
    locator: "accountability; traceability"
    note: "Traceability placed under Accountability."
  - title: "ISO/IEC 42001:2023, AI management systems"
    ref: library/ref-iso-42001-2023.md
    locator: "assigned accountability; AI system inventory; continual improvement"
    note: "Assigned accountability, an AI system inventory, and governance as continual improvement."
  - title: "OpenAI, Practices for Governing Agentic AI Systems (2023)"
    ref: library/ref-openai-governing-agentic-ai-2023.md
    locator: "constraining the action space; human accountability; action ledger"
    note: "Constraining the action space, human accountability, and an action ledger."
  - title: "Chan et al., Visibility into AI Agents (ACM FAccT 2024)"
    ref: library/ref-chan-visibility-2024.md
    locator: "agent identifiers, real-time monitoring, activity logging"
    note: "Agent identifiers, real-time monitoring, and activity logging as the substrate of accountability."
  - title: "Kolt, Governing AI Agents (Notre Dame Law Review, 2025)"
    ref: library/ref-kolt-governing-agents-2025.md
    locator: "accountability and control of agents"
    note: "Legal treatment of agent accountability and control."
  - title: "European Commission JRC, The Role of AI in Scientific Research (JRC143482, 2025)"
    ref: library/ref-jrc-ai-in-science-2025.md
    locator: "AI as tool; human accountability in science"
    note: 'AI as a tool with human accountability in science. The HFD source attributes a "situated judgement is not automatable" claim to the JRC; we cite the JRC report for the accountability framing and do not attribute that exact wording to it without a located passage.'
layer: Ecosystem
hitl: n/a
tags: [governance, provider, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- An [agent's](../glossary.md#agent) limits ([guardrails](../glossary.md#guardrails)) belong in the system that runs it, not only in written policy.
  { #bp4-a1 }
- An agent cannot be talked into following a rule; it can only be stopped from taking an action.
  { #bp4-a2 }
- Limits have to be implemented in permission scopes, autonomy limits, resource and spend caps, and shutdown paths.
  { #bp4-a3 }
- Regardless of implemented safeguards, something can always go wrong.
  { .afs-practice__pivot #bp4-a4 }
- Thus, every agent also needs a named human owner for each responsibility it carries.
  { #bp4-a5 }
- The agent's actions have to be logged under an attributable identity, so that accountability can be traced after the fact.
  { #bp4-a6 }

</div>

=== "For practitioners"

    When you run an agent in your own work, set its limits where they take effect: what it can access, how far it can act on its own, how much it may consume, and when it must stop and ask.
    Stay the decision-maker for anything that affects results or other people.
    A personal agent connected to your mail and files is part of the institution's risk, even if no one else set it up.

=== "For providers"

    Put the limits you promise in the system, not only in the docs, so an agent cannot exceed its scope by being told to.
    Give operators the stop, escalation, spend-cap, and shutdown controls they need, log agent actions under attributable identities, and record which role holds each responsibility.
    Roll out new agent features in stages, with clear success and go-live criteria.

=== "For governance"

    Written policy alone does not bind a system that acts.
    Move the rules you care about into guardrails and enforced permissions.
    Give each responsibility a named role with clear escalation and shutdown paths, keep a list of the agents in use, require that their actions are logged and attributable, and require independent evaluation where the risk is high.
    A budget an agent can exceed is not a limit; the cap belongs in the system that meters the spending.
    Decide what autonomy the organisation is willing to grant, and treat governance as ongoing, not a one-time policy.

## Reasons

An agent acts.
A policy document tells a person what to do.
It does nothing to a system that only follows the actions it is allowed to take.
As agents get more autonomous, the gap between written rules and enforced limits becomes the main risk.
To close it, put the limits where they take effect: what the agent can access, how far it can act without a human, how much it may consume, and when it must stop or escalate.
Consumption belongs in that list because an agent that loops does not crash.
It keeps working, and it keeps billing, so an unmetered run can exhaust a budget while staying inside every permission it was granted.
Accountability has to be just as concrete.
If responsibility sits with "the institution" in general, no one is answerable; it has to sit with named roles, with clear paths to escalate and to shut an agent down.
Accountability also needs a record: if an agent's actions are not logged under an attributable identity, no one can reconstruct what it did or hold the right role answerable.
Personal agents with broad access to mail, files, and calendars sit outside all of this, so governance has to cover individual use, not only institutional deployments.
This is the consensus position across the main governance frameworks (NIST, the EU AI Act, OECD, ISO/IEC 42001), which agree on enforced limits, named accountability, an agent inventory, logging, and independent review.

## Examples

- A policy document says the agent must not delete production records, but nothing in the system stops it; a [prompt-injected](../glossary.md#prompt-injection) instruction gets it to do exactly that.
  The rule was written, not enforced.
- The same agent runs with a scoped token that carries no delete permission and a shutdown control a named on-call engineer can trigger, so the injected instruction fails because the action was never available to it.
- After an agent writes a wrong value to a shared dataset, the team traces it through the action ledger to the run, the model version, and the role that owned that workflow, and closes the gap.
- Responsibility for an agent sits with "the department" in general; when it misbehaves, no one is answerable and no one has clear authority to shut it down.
- An agent runs against a token ceiling set per run and an alert at half of it; when a misconfiguration sends it looping over the same records, it stops at the ceiling instead of billing for months against a budget that existed only on paper.
- A new agent feature goes live for low-risk cases first, with success and go-live criteria and an accepted risk limit set in advance, before any wider rollout.
- A personal agent connected to a researcher's mail and files is entered in the institution's agent inventory and reviewed like any deployed one, because its broad access is part of the same risk.

<!-- BP_SOURCES -->
<!-- The Sources list above is generated from this page's frontmatter sources by hooks/bp_pages.py. Edit `sources:`, not here. -->

## Change history

- 2026-07-31: Extended bp4-a3 to name resource and spend caps alongside permission scopes, autonomy limits, and shutdown paths, with matching Reasons, tab, and Example text. An agent inside every permission it was granted can still exhaust a budget, because a looping agent does not crash. Prompted by the reported Amazon cost overruns, recorded in the provenance data as a qualification on bp4-a3.
- 2026-07-27: Added the EU AI Omnibus (2026) as a supporting source on bp4-a1 (technical safeguards in the system, not policy; Art 5(1a) foreseeable-misuse standard).
- 2026-07-27: Renumbered from BP03 to BP04 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including anti-patterns, replacing restatements of the practice.
- 2026-07-26: Rewritten to merge action-logging and attributable agent identity into the practice, add independent grounding (NIST, EU AI Act, OECD, ISO/IEC 42001, OpenAI, Chan et al., Kolt), and add two citation caveats: the "guidelines to guardrails / Kassorla et al." attribution in the source could not be verified, and the JRC "not automatable" wording is unconfirmed.
- 2026-07-25: Created from the HFD distillation, grounded in the EU Expert Forum entry.
  New practice added because the guidelines-to-guardrails point is a separate action, not a sub-case of stating a human-in-the-loop level ([BP09](09-human-in-the-loop.md)).
