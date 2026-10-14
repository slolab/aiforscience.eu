---
title: Mission
---

# Mission

## Vision

Science that uses agentic AI well: agents do the connecting, scientists keep the thinking.
Agentic AI is most valuable in science when it links data, tools, and models across groups and institutions, while the epistemic core of research (judgement, provenance, accountability) stays with humans.

## Mission

Maintain the shared, citable, current record of best practices for applying agentic AI to science.
Guidance written as static reports is outdated before it is published; these practices are revised at the pace of the field, versioned for citation, and open to challenge.
They aggregate what task forces and institutions learn, so organisations build on each other's experience instead of writing siloed reports and guidelines.

## Scope

Current developments around generative AI, particularly large language models, impact fundamentally how science is done.
This living document aims to capture anything that matters in this frame.
The test for any practice, document hook, or discussion:

> Would adopting this change how science is planned, performed, evaluated,
> communicated, or governed?

**In scope**: research workflows and methods; scientific services, data resources, and infrastructure; provenance, citation, and evaluation of agentic systems; research skills and training; governance of AI within scientific institutions.

**Out of scope**: national economic and industrial policy, energy and compute geopolitics, security and defence, international treaties.
When such material directly constrains scientific practice, the practices cite it as context; they do not distill or debate it.

The practices also draw a method boundary.
They cover the practice of applying agents to scientific work.
The design and validation of AI methods as scientific instruments (predictors, generative models, classifiers) have their own established community norms (FAIR, DOME, model cards, datasheets, REFORMS).
The practices cite these rather than restating them, and treat an agent or model as a method chosen for a task, not a default (see [Match the method to the task](../best-practices/01-match-method-to-task.md)).

Research ethics and data protection are handled the same way.
Consent, ethics approval, and data protection law (in the EU, the GDPR) are established norms with their own institutions: ethics committees, data protection officers, and supervisory authorities.
The practices cite these norms and do not restate them.
They cover what changes when AI tools and agents handle research data.
This is covered in [Decide where research data may be sent](../best-practices/11-decide-where-research-data-may-go.md).
The irreversible case, training a third-party model on data held under withdrawable consent, is screened under [Screen agents for dual-use and high-consequence risk](../best-practices/10-screen-dual-use-high-consequence.md).

The [library](../library/index.md) likewise extracts relevant context from the cited materials.

## Audiences

The practices are written for three roles.
There are overlaps, and most practices speak to all audiences.
To give concrete guidance, all practice pages carry an audience-specific section.

- **Practitioners**: scientists and research groups using agentic AI in their daily work.
- **Providers**: the people who build and operate scientific services, data resources, and tools that agents use (for example the teams behind research-infrastructure services).
- **Governance**: scientific management and administration, from institute leadership to head offices and funders, deciding what to enable, require, and resource.

## How the practices are made

Two groups shape adoption.

**Pioneers** adopt early and learn by doing; they exist in every audience but concentrate among practitioners.
The best support for them is to remove obstacles and observe.
Pioneers contribute to the practices or ignore them (either is fine).
Learning from pioneers is one of the central aims of this record.

**Settlers** are far more numerous.
They come after the pioneers and build things meant to last, so they need reliable, current guidance.
The practices are learned from the pioneers and written for the settlers, across all three audiences.

## How it stays current

The practices are maintained on [GitHub](https://github.com/slolab/aiforscience.eu).
Changes go through public review.
A dated release is cut monthly and receives a DOI, so it can be cited by scientists and by institutional strategy documents alike.
Every practice records which organisations endorse it, and any organisation can propose, challenge, or endorse practices; the value of the shared practices grows with every organisation that joins.
See [Partners](partners.md), [Governance](governance.md), and [Releases](../releases/index.md).
