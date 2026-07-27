---
title: A safer framework for patient data in AI-for-Science grants (2026)
source_type: other
issuing_body: Julien Gagneur (Technical University of Munich)
published: July 2026
doi_or_url: https://medium.com/@gagneur/anthropics-ai-for-science-rare-disease-research-grants-need-a-safer-framework-for-patient-data-de319ce8f05b
distilled_on: 2026-07-28
status: draft
tags: [library, governance]
comments: true
---

# A safer framework for patient data in AI-for-Science grants (2026)

!!! info "Source"
    **Document:** "Anthropic's AI for Science rare disease research grants need a safer framework for patient data".
    **Author:** Julien Gagneur, Technical University of Munich.
    **Type:** individual commentary (Medium).
    **Date:** July 2026. **Distilled:** 2026-07-28.

## Summary

The article responds to [Anthropic's AI for Science rare-disease research grants](https://www.anthropic.com/news/rare-disease-research-grants), which offer up to $50,000 in Claude credits over six months to researchers studying rare disease.
It argues that the program's data terms are incompatible with how patient data is governed in research.
The core point is a distinction the terms collapse: permission to analyse patient data under consent and data-access rules is not permission to transfer that data, or patient-level information derived from it, to a third party for model training or product development.
It also describes a concrete technical risk specific to agentic tools: a coding agent that runs code and reads outputs can transmit study-participant data out of an approved environment without a deliberate upload.
It proposes a protected research tier (training exclusion, local or secure processing, egress controls, auditability, and a data-processing agreement) that would keep the collaboration while protecting participants.
This is one researcher's argued position, not a standard or an institutional report.

## Hooks, with citations

**1. Agentic tools can move sensitive data out of an approved environment without a deliberate upload.**
The document: "AI agents may run code, inspect results, and transmit relevant material to the external service operating it. Study-participant-level information can therefore leave the approved environment without a deliberate upload" (body).
Relevance: names a data-egress path that exists whenever an agent can read local files and call an external model, and it sharpens why stating an oversight level is not enough if a person approves agent-generated code without reading it ([BP09](../best-practices/09-human-in-the-loop.md)).
Audiences: practitioners, providers, governance.

**2. Permission to analyse data is not permission to transfer or train on it.**
The document: "Permission to analyse them does not imply permission to transfer them, or derived patient-level information, to a third party for model training or product development" (body).
Relevance: separates two rights that data-access agreements keep distinct, and that a blanket grant conflates.
Audiences: governance, practitioners.

**3. The program's terms take a broad, perpetual grant over program data.**
The document quotes the terms: researchers "warrant that they have obtained all necessary permissions ... to allow Anthropic to collect, analyze, train models on, and conduct research on all data, including Inputs and Outputs", and grant "a perpetual, irrevocable license to use Program data for these purposes" (body).
Relevance: for controlled-access clinical or genomic data, a researcher often cannot lawfully make that warranty, so the burden shifts to the person least able to carry it.
Audiences: governance, practitioners.

**4. A protected research tier: exclude sensitive data from training, process it locally, control egress, and audit.**
The document: "patient-level data, derived patient-level outputs, and other controlled-access material are excluded from model training and product-development use, and no perpetual licence is taken over them; sensitive data remain within an institutionally approved environment, with analysis against those data performed locally or through an approved secure-processing arrangement; technical controls prevent patient-level information from being transmitted to Anthropic and allow institutions to audit what the agent can access and send" (body).
Relevance: puts the protection in enforced controls and a governed environment rather than in a researcher's promise, matching guardrails-in-the-system ([BP04](../best-practices/04-govern-autonomy-and-accountability.md)) and access governed by the resource ([BP02](../best-practices/02-default-to-agent-accessibility.md)).
Audiences: providers, governance.

**5. Terms, retention, and responsibilities belong in a data-processing agreement.**
The document: "retention, processing locations, subprocessors, security measures, and institutional responsibilities are clearly defined in an appropriate data-processing agreement" (body).
Relevance: makes the arrangement auditable and assigns responsibility, rather than leaving it to the grant's default license.
Audiences: governance, providers.

**6. Open science with boundaries is compatible with protection.**
The document argues code, methods, evaluations, curated public resources, and non-sensitive findings can be shared openly while patient data, confidential records, and controlled-access outputs remain protected, and notes that "Anthropic acknowledges, in its commercial offerings, that customers may require stronger restrictions on training, retention, and data use" (body).
Relevance: openness by default and protection of controlled-access data are not in conflict; the stronger-restriction option already exists commercially.
Audiences: practitioners, providers, governance.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a5); context for [BP03](../best-practices/03-register-and-vet-interfaces.md) | |
| 2 | context for [BP04](../best-practices/04-govern-autonomy-and-accountability.md) governance | |
| 3 | context for [BP04](../best-practices/04-govern-autonomy-and-accountability.md), [BP02](../best-practices/02-default-to-agent-accessibility.md) | |
| 4 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1, bp4-a6), [BP02](../best-practices/02-default-to-agent-accessibility.md) (bp2-a4) | |
| 5 | context for [BP04](../best-practices/04-govern-autonomy-and-accountability.md) | |
| 6 | [BP02](../best-practices/02-default-to-agent-accessibility.md) (bp2-a4); context for [BP07](../best-practices/07-provenance-and-citation.md) | |

No direct contradictions with the current practices.
The article exposes a gap rather than a conflict: the record governs agent autonomy, access, and oversight, but has no explicit line on controlling what data an agent may send outward and keeping controlled-access data out of third-party training and retention.

## Proposed changes to practices

These are proposals for editor review, not applied here.

- [ ] Add `gagneur-rare-disease-patient-data-2026` as a supporting source on [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1, bp4-a6): egress controls that prevent an agent from transmitting sensitive data, and audit of what the agent can access and send, are guardrails in the system.
- [ ] Add it as a supporting source on [BP02](../best-practices/02-default-to-agent-accessibility.md) (bp2-a4): controlled-access data governed by local or approved secure processing.
- [ ] Add it as a supporting source on [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a5): a concrete case where approving agent-generated code without review defeats the stated oversight.
- [ ] Consider a new atom or Examples bullet on [BP04](../best-practices/04-govern-autonomy-and-accountability.md) on data egress: an agent's outbound data should be constrained and auditable, and controlled-access data (with patient-level data as the labelled example) should be excluded from third-party model training and retention unless an agreement permits it. Draft tab text for editor review:
    - **Practitioners:** Before you point an agent at sensitive or controlled-access data, know what it can read and where it can send it; agent-run code can transmit that data to an external service without a deliberate upload, so do not approve generated code you have not read.
    - **Providers:** Give operators controls that constrain and log an agent's outbound data, keep controlled-access data in an approved environment, and offer terms that exclude it from training and retention; put those terms in a data-processing agreement.
    - **Governance:** Require that agents handling controlled-access data run under enforced egress limits and audit, and that third-party processing and training of that data is barred unless an agreement allows it.
- [ ] Optionally add a reference entry for Anthropic's AI-for-Science rare-disease grants as the program the critique responds to.

## Cautions and gaps

This is individual commentary published on Medium, not a peer-reviewed paper, standard, or institutional report; weight it as an argued position and ground any practice change on it accordingly.
It critiques one program's terms at one point in time, and those terms may change; the quoted warranty and licence language should be checked against the current program terms before being relied on.
The argument is about risk and governance, not evidence of a breach; it does not measure how often agent-driven egress happens in practice.
The rare-disease and genomics setting is the article's example; the transferable practice is domain-neutral and concerns any controlled-access or confidential data an agent can reach.
