---
title: EU AI Omnibus (2026)
source_type: policy report
issuing_body: European Union
published: 2026, in force 27 July 2026 (proposed 19 November 2025)
doi_or_url: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202601744
distilled_on: 2026-07-27
status: draft
tags: [library, regulation]
comments: true
---

# EU AI Omnibus (2026)

!!! info "Source"
    **Document:** "Regulation (EU) 2026/1744 amending Regulation (EU) 2024/1689 (the Digital Omnibus on AI)".
    **Issuing body:** European Union.
    **Date:** Proposed 19 November 2025; in force 27 July 2026.
    **Distilled:** 2026-07-27.

## Summary

The AI Omnibus is a targeted simplification package that amends the EU AI Act (Regulation (EU) 2024/1689).
Most of it is administrative and regulatory: postponed compliance timelines for high-risk systems, simplified documentation and registration for smaller providers, an EU-level regulatory sandbox, expanded AI Office oversight of general-purpose models and large platforms, and new prohibitions on AI-generated non-consensual intimate imagery and child sexual abuse material.
Little of the document speaks to scientific practice directly, and it adds no research or R&D exemption.
The provisions that bear on the record are narrow: the softening of the AI literacy obligation, a new legal basis for processing special-category data to detect and correct bias, the narrowing and delay of high-risk classification, and the framing that a provider is responsible for a "reasonably foreseeable and reproducible" prohibited output unless it has built adequate technical safeguards.
It updates the grounding the AI Act already provides for BP03, BP04, and BP09 (see [ref-eu-ai-act](ref-eu-ai-act.md)); it does not justify a new practice.

## Hooks, with citations

**1. AI literacy shifts from a duty to ensure to a duty to support.**
The regulation replaces the obligation on providers and deployers to "ensure" AI literacy with a duty to "take measures to support the development of AI literacy" of their staff, with Member States and the Commission to support and facilitate that effort, especially for SMEs (Art 4; Recital 8).
Relevance: bears on how institutions train scientists to use agentic AI; the legal floor is now a supportive measure rather than a hard obligation.
Audiences: governance, providers.

**2. New legal basis to process special-category data for bias detection.**
A new Article 4a permits providers and deployers of high-risk (and, under conditions, other) AI systems to process special categories of personal data where necessary to detect and correct bias, subject to strict safeguards: use only where non-sensitive or synthetic data cannot achieve the purpose, strict access controls, no transmission to third parties, deletion once bias is corrected, and documented necessity (Art 4a; Recital 9).
Relevance: bias detection is an evaluation dimension; this sets the conditions under which sensitive research data may be used to test AI systems for it (see [BP08](../best-practices/08-evaluate-tools-before-trust.md)).
Audiences: providers, practitioners, governance.

**3. Provider responsibility for foreseeable and reproducible misuse.**
For the new prohibitions, a provider is liable not only where a system is intended to produce prohibited material but where that output is a "reasonably foreseeable and reproducible outcome" absent "reasonable and adequate technical safety measures and other safeguards" (Art 5(1a)(a)(ii); Recital 12).
Relevance: the standard puts the burden on providers to build technical safeguards against foreseeable misuse rather than rely on policy or intent, which mirrors the guardrail and screening logic in [BP04](../best-practices/04-govern-autonomy-and-accountability.md) and [BP10](../best-practices/10-screen-dual-use-high-consequence.md).
Audiences: providers, governance.

**4. High-risk classification narrowed; compliance dates postponed.**
AI used solely for non-safety aspects such as user assistance, performance optimisation, or service efficiency does not qualify as a safety component (Art 6(1a); Recital 7), and the application dates for high-risk obligations are pushed to 2 December 2027 for Annex III systems and 2 August 2028 for Annex I product-integrated systems (Art 113; Recital 40).
Relevance: affects when and whether providers of regulated scientific services (for example clinical or diagnostic AI) fall under high-risk obligations.
Audiences: providers, governance.

**5. EU-level regulatory sandbox and expanded real-world testing.**
The AI Office may establish a Union-level sandbox, with priority access for SMEs and startups, and real-world testing is extended to high-risk systems under Union harmonisation legislation subject to safeguards (Art 57-60, Art 60a; Recitals 24-27).
Relevance: gives developers of scientific AI a supervised route to test systems before deployment, adjacent to the evaluate-before-trust principle in [BP08](../best-practices/08-evaluate-tools-before-trust.md).
Audiences: providers, governance.

**6. Conformity assessment aligned with sectoral law; simplified documentation for smaller providers.**
Notified bodies may run a single, unified conformity assessment covering the AI Act and sectoral law such as the medical-device regulations (MDR/IVDR) (Recital 17), and the Commission must provide a simplified technical-documentation form for SMEs and small mid-caps that notified bodies must accept (Art 11; Recital 18).
Relevance: lowers the compliance overhead for smaller builders of regulated biomedical AI, a common provider profile in the life sciences.
Audiences: providers.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | context for [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (institutional governance of AI use) | weakens a prior training obligation |
| 2 | [BP08](../best-practices/08-evaluate-tools-before-trust.md) (bias detection as evaluation) | |
| 3 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md), [BP10](../best-practices/10-screen-dual-use-high-consequence.md) | |
| 4 | context for [BP03](../best-practices/03-register-and-vet-interfaces.md), [BP04](../best-practices/04-govern-autonomy-and-accountability.md) | |
| 5 | context for [BP08](../best-practices/08-evaluate-tools-before-trust.md) | |
| 6 | context for providers | |

Hook 1 is a tension, not a contradiction: the Act still expects AI literacy, but the legal obligation is now to support rather than ensure it.
The record's position (that practitioners and institutions should build the skills to use agentic AI well) is unchanged; the regulatory floor beneath it has moved.

## Proposed changes to practices

Note edits applied on 2026-07-27; a new practice was not warranted.

- [x] Add `ai-omnibus-2026` as a supporting note on [BP04](../best-practices/04-govern-autonomy-and-accountability.md): the foreseeable-and-reproducible-misuse standard (Art 5(1a)) puts technical safeguards in the system, not in policy, which is exactly `bp4-a1`.
- [x] Add `ai-omnibus-2026` as a supporting note on [BP10](../best-practices/10-screen-dual-use-high-consequence.md): the same standard obliges providers to build safeguards against foreseeable prohibited output (`bp10-a4`).
- [x] Note on [BP08](../best-practices/08-evaluate-tools-before-trust.md) that the amended Act now provides a conditional legal basis (Art 4a) for using special-category data to detect and correct bias, an evaluation dimension.
- [x] Update [ref-eu-ai-act](ref-eu-ai-act.md) to record the 2026 amendment (Art 4 literacy softening, Art 4a bias detection, postponed high-risk timelines) and cross-link to this entry.
- [x] No new practice. The document grounds and updates existing practices; it does not pass the gate for its own page.

## Cautions and gaps

Most of the Omnibus is out of scope for this record.
The prohibitions on non-consensual intimate imagery and CSAM, the DSA platform oversight, the machinery reclassification, and the cybersecurity interplay with the Cyber Resilience Act are general AI regulation, cited here only as context.
The document adds no dedicated research or R&D exemption; the only research-adjacent openings are the bias-detection basis (Art 4a) and a red-teaming allowance for compliance testing under the new prohibitions (Recital 13).
Applicability is narrow: most scientific use of agentic AI is not "high-risk" under the Act, so the postponed timelines and conformity-assessment changes bear mainly on providers of regulated systems such as medical AI.
The article and recital numbers here refer to the AI Act (Regulation (EU) 2024/1689) as amended, not to the amending regulation's own numbering. They were verified on 2026-07-27 against the Official Journal text and independent legal trackers; the new prohibitions themselves apply from 2 December 2026.
