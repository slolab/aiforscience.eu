---
title: appliedAI AI Act Governance white paper (2025)
ref_id: appliedai-ai-act-governance-2025
source_type: guideline
issuing_body: appliedAI Initiative GmbH
published: June 2025 (file revised August 2026)
doi_or_url: https://www.appliedai.de/en/ai-resources/white-papers/ai-act-governance-best-practices-for-implementing-the-eu-ai-act/
distilled_on: 2026-11-05
status: draft
tags: [library, regulation]
comments: true
---

# appliedAI AI Act Governance white paper (2025)

!!! info "Source"
    **Document:** "AI Act Governance: Best Practices for Implementing the EU AI Act".
    **Authors:** Alexander Machado, Manuel Jiménez Mérida, Akhil Deo, Anish Pathak.
    **Issuing body:** appliedAI Initiative GmbH, Munich, from two 2024 working groups with more than 15 corporate partners (among them Carl Zeiss, Infineon, Linde, EnBW, MTU Aero Engines, Roche Diagnostics, TÜV SÜD, Giesecke+Devrient).
    **Date:** June 2025; the downloadable PDF was revised on 25 August 2026.
    **Link:** [PDF](https://www.appliedai.de/uploads/files/Whitepapers/appliedAI-Whitepaper-AI-Act-Governance-2025-EN.pdf) (60 pages).
    **Distilled:** 2026-11-05.

## Summary

The white paper is an industry practitioners' guide to operationalising the EU AI Act inside companies, written for heads of AI governance, compliance officers, product owners, and ML engineers.
It proposes a three-layer "AI Act Governance Pyramid" (an orchestration layer for strategy and oversight, an integration layer that builds compliance into shared infrastructure and templates, and an execution layer where project teams apply them), then lists working-group best practices for each high-risk requirement of Articles 10 and 12 to 15, mapped to ISO/IEC standards, with open questions and trade-offs for each.
It is written for conventional ML systems in an enterprise, with a hypothetical hospital diagnostic classifier as the running example, and does not discuss agents, scientific research, or the AI Act's research exclusion.
For this record its value is narrow and concrete: it gives worked detail on making human oversight effective (interface defaults, warnings, rotating reviewers), on starting governance from an inventory of AI systems with assigned roles, on what an event log should capture, and on setting performance thresholds with domain experts before development.
It grounds BP04, BP09, and BP08; it does not justify a new practice.

## Hooks, with citations

**1. Start from an inventory of AI systems, then assign roles.**
The document's first two steps for getting started: "Identify your landscape of obligations (risk landscape) under the AI Act by creating an inventory of AI systems in your company and classifying their risk class and role" and "Set up an EU AI Act governance process [...] define clear roles & responsibilities on policies oversight, and governance evaluation" ("Getting Started Today", p. 52).
Relevance: the inventory and the assignment of roles are the same first moves BP04 asks of institutions, here described by companies that have tried them ([BP04](../best-practices/04-govern-autonomy-and-accountability.md)).
Audiences: governance.

**2. Governance responsibilities are functions, which may be shared or combined.**
"These layers are not related to individual roles but to a set of functions, related skills, or 'hats' that may span over multiple stakeholders or be consolidated depending on the size and structure of the organization" (§3, p. 16).
Relevance: this fits small research groups, where one person often holds several roles; it also leaves open who answers when a function spans several people, which BP04 settles with a named owner ([BP04](../best-practices/04-govern-autonomy-and-accountability.md)).
Audiences: governance.

**3. Rules go into shared infrastructure and gates, not only into policy.**
The integration layer "integrates the legal requirements into technical infrastructure and documentation templates to be reused across use cases"; its examples include "A data validation step fails if data quality thresholds (defined by governance) aren't met, blocking deployment" (§3, Layer 2, p. 20).
Relevance: the same move as `bp4-a1`, applied to data quality: the requirement is enforced by the pipeline, so a project cannot pass it by assertion ([BP04](../best-practices/04-govern-autonomy-and-accountability.md)).
Audiences: providers, governance.

**4. Design the oversight interface against automation bias.**
For Article 14(4)(b) the working group lists: "Identify what UI based features can prevent the overseer from over-relying on the AI system", with the examples "Warning messages to human overseer" and "UI Design to not opt-in to the AI system result by default"; and "Identify what organizational measures can prevent the overseer from over-relying on the AI system, including, e.g., rotating human overseer at appropriate times" (§4, Human Oversight, p. 42).
Relevance: three specific design measures for `bp9-a5` (a stated check has to work in deployment): no pre-selected AI answer, warnings, and reviewer rotation ([BP09](../best-practices/09-human-in-the-loop.md)).
Audiences: providers, governance, practitioners.

**5. Oversight strength is a trade-off set by risk and autonomy.**
"The more observable and controllable, the less speed a system operates with. Based on the risk, context and level of autonomy you need to select your trade off"; "The more oversight is required, the higher the costs to design and operate"; "The less technically adept the user, the simpler the observability and controllability UI must be" (§4, Open Questions and Tradeoffs for Article 14, p. 43).
Relevance: supports matching the HITL level to the stakes, and names the cost of each level openly ([BP09](../best-practices/09-human-in-the-loop.md)).
Audiences: providers, governance.

**6. The overseer's controls are listed concretely.**
The controllability catalogue for deployment includes "Rollback", "Disable endpoint (Stop button)", "Manually correct data predictions", "Disregard output", "Override output", and "Reverse the output" (§4, Controlability, p. 43).
Relevance: a checklist of the actions a human needs in order to intervene, which BP04 lists as shutdown paths and BP09 as approve, edit, veto, and stop ([BP04](../best-practices/04-govern-autonomy-and-accountability.md), [BP09](../best-practices/09-human-in-the-loop.md)).
Audiences: providers.

**7. What an accountable log records, and who may read it.**
Step 5 of the log-identification process: "Comprehensive Logs: Capture who, what, when, and outcomes of key events"; "Access Management: Define who can access logs and under what conditions"; "Model Logging: Record input/output data, timestamps, expected outputs, and user changes" (§4, Record-Keeping, p. 36).
Relevance: gives content to `bp4-a6` (actions logged under an attributable identity) and to recording what a human changed ([BP04](../best-practices/04-govern-autonomy-and-accountability.md), [BP07](../best-practices/07-provenance-and-citation.md)).
Audiences: providers.

**8. Decide what to log from the risks, not from what is easy to log.**
The working group's process starts from the system's intended purpose, identifies situations that may pose risk or count as substantial modification, and only then decides "what to log per risk", weighing "the cost/benefit ratio of each log" (§4, Record-Keeping, pp. 35-36).
Its own trade-off note: "Logging as much as possible might be an organizational and engineering overhead" (p. 37).
Relevance: a usable method for scoping an agent action ledger without logging everything ([BP04](../best-practices/04-govern-autonomy-and-accountability.md)).
Audiences: providers.

**9. Set metrics and acceptance thresholds with domain experts before development.**
The accuracy best practices, steps 2 and 3: "Select performance metrics", "Discuss with Domain Experts & AI Governance team"; "Set appropriate thresholds", "Get input from technical roles (advisory only)"; "Specify and document the target thresholds and quality gates to continue with the AI use case"; "Revisit target performance metrics defined in step 2 regularly during development" (§4, Accuracy, p. 45).
The data-quality table adds "Curated Test Sets: Use curated domain-specific test sets to assess performance and identify failure points qualitatively" (p. 33).
Relevance: the domain expert, not the engineer, decides what is good enough, and the bar is fixed before results are seen ([BP08](../best-practices/08-evaluate-tools-before-trust.md)).
Audiences: practitioners, providers.

**10. Data lineage and versioning back every trained model.**
"Data lineage and versioning between data sources, transformations and features used to train and test ML models"; "Document information about data by rely on instruments such as datasheets, data-cards, or data catalogues" (§4, Data Provisioning & Documentation, p. 34).
Relevance: grounding for traceability of results to their data ([BP07](../best-practices/07-provenance-and-citation.md)); relevant mainly where a group trains or fine-tunes its own models.
Audiences: practitioners, providers.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (inventory, assigned roles) | |
| 2 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (roles) | `bp4-a5` (named human owner) |
| 3 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) `bp4-a1` | |
| 4 | [BP09](../best-practices/09-human-in-the-loop.md) `bp9-a5` | |
| 5 | [BP09](../best-practices/09-human-in-the-loop.md) `bp9-a1` | |
| 6 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) `bp4-a3`, [BP09](../best-practices/09-human-in-the-loop.md) Examples | |
| 7 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) `bp4-a6`, [BP07](../best-practices/07-provenance-and-citation.md) | |
| 8 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) `bp4-a6` | |
| 9 | [BP08](../best-practices/08-evaluate-tools-before-trust.md) `bp8-a1` | |
| 10 | [BP07](../best-practices/07-provenance-and-citation.md) `bp7-a1` | |

Hook 2 is a mild tension with `bp4-a5`.
The document assigns governance to functions that may span several people; BP04 asks for a named human owner for each responsibility.
The two fit when each function has one named person answerable for it; a function shared across a team with no such person is the "responsibility sits with the department" failure BP04 describes.

## Proposed changes to practices

- [ ] Add as a source to [BP09](../best-practices/09-human-in-the-loop.md).
  `ref: library/appliedai-ai-act-governance-2025.md`, `locator: "§4, Human Oversight, pp. 42-43"`, `note: "Industry working-group measures for Article 14 of the AI Act: an interface that does not pre-select the AI result, warnings to the reviewer, and rotating reviewers against automation bias; oversight strength set by risk and autonomy. Written for conventional ML systems, not agents."`
- [ ] Add an Example to [BP09](../best-practices/09-human-in-the-loop.md): "A review screen shows the agent's proposal without pre-selecting it; the reviewer has to choose accept, edit, or reject, and long batches are split between reviewers, so no one approves hundreds of items in one sitting."
- [ ] Add as a source to [BP04](../best-practices/04-govern-autonomy-and-accountability.md).
  `ref: library/appliedai-ai-act-governance-2025.md`, `locator: "Getting Started Today, p. 52; §3, pp. 16-20; §4, Record-Keeping, p. 36"`, `note: "Industry working-group guide to the EU AI Act: start from an inventory of AI systems with assigned roles, enforce rules through shared infrastructure and quality gates, and log who, what, when, and outcome. Enterprise ML context; agents are not discussed."`
- [ ] Add provenance edges (applied in this branch, see below): `bp4-a1`, `bp4-a5` (qualifies), `bp4-a6`, `bp9-a1`, `bp9-a5`, `bp8-a1`, `bp7-a1`.
- [ ] No new practice. The document grounds existing practices.

## Cautions and gaps

The document is enterprise compliance guidance for conventional ML systems and was written by a consultancy whose partners fund it; its best practices are working-group consensus, not evaluated evidence.
It does not discuss AI agents, general-purpose AI used through an interface, or the AI Act's exclusion of systems developed and used solely for scientific research (Article 2(6)).
Most scientific use of agentic AI falls outside the high-risk obligations the paper centres on, so its article-by-article detail applies mainly to providers of regulated services, for example clinical or diagnostic tools.
Some legal statements are out of date after the [AI Omnibus](ai-omnibus-2026.md): the paper gives 2 August 2026 for Annex III high-risk obligations (now 2 December 2027) and calls AI literacy training "mandatory under Article 4" (now a duty to support AI literacy).
The ISO/IEC standards it maps to were partly unpublished at the time of writing, and the harmonised standards it anticipated for early 2026 should be checked before relying on its mapping.
The running example is a hospital triage classifier; it illustrates the requirements and is not a recommendation for that use.
The paper reports no failures or incidents, so nothing from it was added to the failures log.
