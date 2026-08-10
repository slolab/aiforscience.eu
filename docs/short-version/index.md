---
title: The short version
tags: [governance]
comments: true
---

# The short version

Agentic AI only works if the deployed agents have autonomy.
This autonomy comes with technical, economic, and societal risks.
AI Agents increasingly do work that previously required human experts.
Our fundamental challenge is to decide which tasks they should handle and how.
Suitable tasks need to be sufficiently trivial and contained that the AI system cannot cause lasting damage.
Judgment, provenance, and accountability needs to stay with people.
This page is the short version of the [record](../best-practices/01-match-method-to-task.md), written as the decisions to make: what to enable, what to resource, what to require.
Each point links to the practice it comes from.

<div class="afs-ai-strip" markdown="0" data-afs-ai-cta>
  <div class="afs-ai-strip__bar">
    <span class="afs-ai-strip__label">Ask your own AI Assistant</span>
    <div class="afs-ai-strip__actions">
      <a class="afs-ai-strip__btn afs-ai-strip__btn--primary" data-afs-ai-chatgpt rel="noopener noreferrer" target="_blank" href="https://chatgpt.com/?q=Read%20the%20AI%20for%20Science%20record%20of%20best%20practices%20for%20agentic%20AI%20in%20research%20at%20https%3A%2F%2Faiforscience.eu%2Fllms-full.txt%20and%20answer%20my%20questions%20using%20only%20that%20source%2C%20citing%20the%20practice%20each%20point%20comes%20from.%20My%20question%3A%20">ChatGPT</a>
      <a class="afs-ai-strip__btn afs-ai-strip__btn--primary" data-afs-ai-claude rel="noopener noreferrer" target="_blank" href="https://claude.ai/new?q=Read%20the%20AI%20for%20Science%20record%20of%20best%20practices%20for%20agentic%20AI%20in%20research%20at%20https%3A%2F%2Faiforscience.eu%2Fllms-full.txt%20and%20answer%20my%20questions%20using%20only%20that%20source%2C%20citing%20the%20practice%20each%20point%20comes%20from.%20My%20question%3A%20">Claude</a>
      <button class="afs-ai-strip__btn" type="button" data-afs-ai-copy>Copy as Markdown</button>
    </div>
  </div>
  <p class="afs-ai-strip__note">Answers from the record's <a href="../llms-full.txt">own text</a>, citing each practice. No account, no install.</p>
</div>

## The decisions, in order of impact

Ranked from the calls that shape the whole programme down to operational groundwork.
Each point is tagged by the kind of decision it is (<span class="afs-badge afs-badge--enable">Enable</span> <span class="afs-badge afs-badge--resource">Resource</span> <span class="afs-badge afs-badge--require">Require</span>) or the <span class="afs-badge afs-badge--risk">Risk</span> you carry by not acting.

- <span class="afs-badge afs-badge--resource">Resource</span> **Method choice and evaluation, not model spend.** An agent or a frontier model is one option among several, and often not the cheapest reliable one.
  Fund the work of choosing the method that fits the task and evaluating it.
  Total token spend is not a productivity metric.
  See [BP01](../best-practices/01-match-method-to-task.md).
- <span class="afs-badge afs-badge--require">Require</span> **Screening for serious-harm capabilities.** Some agent capabilities carry dual-use or high-consequence risk.
  Screen them before an agent is given reach, make screening mandatory where a mistake or misuse could cause serious harm.
  See [BP10](../best-practices/10-screen-dual-use-high-consequence.md).
- <span class="afs-badge afs-badge--risk">Risk</span> **Harm that cannot be undone.** Misuse of a high-consequence capability, or training a third-party model on data whose consent can be withdrawn, cannot be walked back after the fact.
  The safeguard is to screen and contain before the action, not to review it afterwards.
  See [BP10](../best-practices/10-screen-dual-use-high-consequence.md).
- <span class="afs-badge afs-badge--enable">Enable</span> **Keep more than one provider.** Keep more than one interface provider in use so the institution is not locked to a single vendor's agent platform.
  See [BP03](../best-practices/03-register-and-vet-interfaces.md).
- <span class="afs-badge afs-badge--require">Require</span> **Limits enforced by the system, with named owners.** A system that acts cannot be talked into following a rule; it can only be stopped from taking an action.
  The limits you care about belong in permission scopes and guardrails, not only in a policy document, and every agent responsibility needs a named human owner with clear stop, escalation, and shutdown paths.
  See [BP04](../best-practices/04-govern-autonomy-and-accountability.md).
- <span class="afs-badge afs-badge--risk">Risk</span> **Policy that a system ignores.** The gap between written rules and enforced limits is the main risk as agents get more autonomous.
  Personal agents connected to staff mail, files, and calendars are part of the institution's risk even when no one deployed them centrally.
  See [BP04](../best-practices/04-govern-autonomy-and-accountability.md).
- <span class="afs-badge afs-badge--require">Require</span> **Evaluation before reliance.** A tool being popular, available, or convincing in a demo is not evidence that it is correct for your work.
  Require that tools feeding into results or decisions are tested on representative tasks first, in proportion to the stakes.
  See [BP08](../best-practices/08-evaluate-tools-before-trust.md).
- <span class="afs-badge afs-badge--resource">Resource</span> **Shared benchmarks and independent evaluation.** Fund shared evaluation practice so adopters are not each testing blind, and support independent tests on data the tool has not seen.
  See [BP08](../best-practices/08-evaluate-tools-before-trust.md).
- <span class="afs-badge afs-badge--require">Require</span> **Vetted, catalogued interfaces.** Agent interfaces (such as MCP servers, skills, and plugins) should reach staff through a catalogue that reviews them and records who maintains each one and when it was last checked.
  Registration is where risk is assessed, and it doubles as an inventory of what is in use.
  See [BP03](../best-practices/03-register-and-vet-interfaces.md).
- <span class="afs-badge afs-badge--resource">Resource</span> **Documentation and data that agents can read.** Agents operate a tool or dataset from its documentation and metadata.
  Fund precise, current documentation and machine-readable descriptions of what the data means.
  It is cheap to check, it now carries real weight, and it helps the people who use the resource directly.
  See [BP05](../best-practices/05-documentation-and-data-for-agents.md).
- <span class="afs-badge afs-badge--require">Require</span> **Stated human-in-the-loop levels.** Every use case should declare where human review is required and where the agent acts alone, and the system should enforce that level.
  Stronger checks apply where an action changes records, results, or the outside world.
  See [BP09](../best-practices/09-human-in-the-loop.md).
- <span class="afs-badge afs-badge--require">Require</span> **Traceable outputs.** Any answer an agent produces should be traceable to its sources, with the human and the agent contributions labelled.
  Provenance is what makes a result checkable, citable, and open to audit.
  See [BP07](../best-practices/07-provenance-and-citation.md).
- <span class="afs-badge afs-badge--risk">Risk</span> **Confident wrong answers.** Without a source trail, a wrong answer that looks right cannot be told from a correct one, and retracted work gets presented as current.
  See [BP07](../best-practices/07-provenance-and-citation.md).
- <span class="afs-badge afs-badge--resource">Resource</span> **Core interfaces as infrastructure.** Fund maintained agent interfaces for the resources that are most used and most important, and tie the level of investment to demand and importance.
  This keeps resources open to agents without an open-ended maintenance bill.
  See [BP02](../best-practices/02-default-to-agent-accessibility.md).
- <span class="afs-badge afs-badge--risk">Risk</span> **Agents route around missing interfaces.** Where a resource has no clean agent interface, agents fall back to older interfaces or scrape data from pages built for people.
  This is fragile and adds load.
  (One observed instance is recorded in the [failures log](../best-practices/failures.md).)
- <span class="afs-badge afs-badge--enable">Enable</span> **Open resources to agents by default.** Agents reach resources whether or not those were built for them.
  Planning for that access means agents can be steered to interfaces that work, instead of falling back to fragile ones.
  Set the default to open and decide the level of support per resource.
  See [BP02](../best-practices/02-default-to-agent-accessibility.md).
- <span class="afs-badge afs-badge--resource">Resource</span> **Interfaces built around users' real tasks.** Interfaces built around the tasks users actually perform cut load, cost, and error.
  Fund the work of learning those tasks.
  See [BP06](../best-practices/06-design-around-user-tasks.md).

## How to check it is working

A short checklist.
Each item links to the practice that defines it.

- [ ] Screening in place for any capability that could cause serious harm. ([BP10](../best-practices/10-screen-dual-use-high-consequence.md))
- [ ] Permission scopes and guardrails enforced by the system, not only written down. ([BP04](../best-practices/04-govern-autonomy-and-accountability.md))
- [ ] A named owner for each agent responsibility, with escalation and shutdown paths. ([BP04](../best-practices/04-govern-autonomy-and-accountability.md))
- [ ] Independent evaluation or audit where the stakes are high. ([BP08](../best-practices/08-evaluate-tools-before-trust.md))
- [ ] Interfaces that record a maintainer and a review date. ([BP03](../best-practices/03-register-and-vet-interfaces.md))
- [ ] An inventory of the agents in use, including personal ones. ([BP04](../best-practices/04-govern-autonomy-and-accountability.md))
- [ ] A stated, enforced human-in-the-loop level for each use case. ([BP09](../best-practices/09-human-in-the-loop.md))
- [ ] Outputs that carry their sources, with human and agent contributions labelled. ([BP07](../best-practices/07-provenance-and-citation.md))
- [ ] Evaluation evidence recorded before a tool is relied on. ([BP08](../best-practices/08-evaluate-tools-before-trust.md))

Governance here is ongoing, not a one-time policy.
Guardrails are revised as agents and their uses change, and decisions are recorded.
See [BP04](../best-practices/04-govern-autonomy-and-accountability.md).
