---
title: Commission Guidelines on Article 50 transparency (2026)
source_type: guideline
issuing_body: European Commission
published: 2026, adopted 20 July 2026
doi_or_url: https://digital-strategy.ec.europa.eu/en/policies/guidelines-transparency-ai-generated-content
distilled_on: 2026-08-04
status: draft
tags: [library, regulation]
comments: true
---

# Commission Guidelines on Article 50 transparency (2026)

!!! info "Source"
    **Document:** "Guidelines on the implementation of the transparency obligations for certain AI systems under Article 50 of Regulation (EU) 2024/1689 (the 'AI Act')" (C(2026) 5054 final, Annex).
    **Issuing body:** European Commission.
    **Date:** Adopted 20 July 2026.
    **Distilled:** 2026-08-04.

## Summary

The Commission's interpretation of Article 50 of the [AI Act](ref-eu-ai-act.md), the transparency chapter, which applies from 2 August 2026.
Article 50 requires four things: that an AI system tell a person they are interacting with AI, that synthetic outputs be marked in a machine-readable way and be detectable as AI-generated, that people exposed to emotion recognition or biometric categorisation be informed, and that deepfakes and AI-generated text published to inform the public on matters of public interest be labelled.
The 51-page guidelines add definitions and worked examples, and three parts of them speak directly to agentic AI in science.
Agents are addressed by name: an agent must disclose both that it is artificial and the person on whose behalf it acts, including to the person instructing it at authorisation, reporting, and validation steps.
Human review is defined, with academic peer review named as a qualifying example, and superficial or automated review named as insufficient.
The Article 2(6) scientific research exclusion is confirmed to cover Article 50, so most research use falls outside the obligation, and the guidelines state where that exclusion stops.

## Hooks, with citations

**1. Article 50 applies from 2 August 2026, with one narrow transitional period.**
"According to Article 113 AI Act, Article 50 AI Act will apply as from 2 August 2026" (§8.4, point 153).
The [AI Omnibus](ai-omnibus-2026.md) added a grandfathering rule for the marking duty under Article 50(2) alone: generative systems placed on the market before 2 August 2026 have until 2 December 2026 to comply, while the disclosure duty for systems interacting directly with people applies from 2 August 2026 with no transition (§8.4, point 153).
Content generated before 2 August 2026 need not be marked retroactively, but text generated before that date and published on or after it must be labelled (§8.4, point 154).
Relevance: dates the point from which providers of scientific services that generate synthetic content carry a marking duty.
Audiences: providers, governance.

**2. The scientific research exclusion covers Article 50, and stops where the research purpose stops.**
Article 2(6) excludes AI systems and models developed and put into service for the sole purpose of scientific research and development, and for Article 50 purposes this exclusion "covers not only interactive AI systems, but also the outputs of generative AI systems (including deep fake content) used in the context of scientific research.
However, if those systems are put into service or their outputs are being used for other purposes than for the sole purpose of scientific research and development, the relevant transparency obligations in Article 50 AI Act would still need to be complied with" (§2.4.2, point 21).
The exclusion is "without prejudice to applicable research ethical standards and EU data protection and other legislation" (§2.4.2, point 21).
The worked example: researchers who build an interactive system to study whether people can tell AI from humans in spoken interaction owe no disclosure under Article 50(1) or 50(2), but they do once the same system is put into service for any other purpose (§2.4.2, point 21).
Relevance: most scientific use of agents sits outside Article 50, so the record's practices rest on scientific grounds rather than on this legal duty; the duty returns when a research tool is offered to others.
Audiences: practitioners, providers, governance.

**3. Pre-market research and development is excluded, testing in real-world conditions is not.**
Article 2(8) excludes research, testing, or development activity before a system is placed on the market or put into service, but "Testing in real world conditions (inside or outside of AI regulatory sandboxes) is not covered by that exclusion", and a system placed on the market as a result of such activity must comply (§2.4.2, point 22).
Relevance: marks the boundary between building and evaluating an agent internally, which is exempt, and running it in a real setting, which is not.
Audiences: providers, governance.

**4. An agent must disclose that it is artificial and who it acts for, including at each authorisation step.**
"AI agents must be designed and developed in such a way that they disclose both their artificial nature and the person on whose behalf they are acting, considering the need for transparency of the origin and the delegation of authority and accountability for the consequences of their actions" (§3.1.1, point 31).
This covers agents operating in multi-agent architectures, and where a provider cannot determine in advance whether an agent will meet a person, "the agent should be designed at the architecture level, and instructed, to disclose itself as such in every situation where it is reasonably likely that the agent may interact with a natural person" (§3.1.1, point 31).
Agents "should also disclose themselves, to the persons instructing them at key steps (e.g. at the point of authorisation, reporting, validation etc., including when the deployed AI agent receives, processes, or relies upon outputs generated by other AI systems rather than directly by a natural person) and at every new interaction" (§3.1.1, point 31).
Backend machine-to-machine calls between agents whose outputs are not intended to reach a person are outside the obligation (§3.1.1, point 30).
Relevance: an official reading that self-disclosure and named delegation belong in the agent's architecture, which is the position taken in [BP04](../best-practices/04-govern-autonomy-and-accountability.md) and [BP07](../best-practices/07-provenance-and-citation.md).
Audiences: providers, practitioners, governance.

**5. Verifiable agent identity is named as a means of disclosure.**
Acceptable disclosure includes "disclosure of AI identifiers, and credentials (e.g. AI agents that disclose their AI identity to the extent feasible in a verifiable manner)" (§3.1.2, point 36).
The accompanying footnote points to electronic attestations of attributes under Regulation (EU) No 910/2014, the EU Digital Identity Wallets, and the proposed European Business Wallets, which "can store and manage electronic attestations that verify the AI agent's identity, attributes, and authorisations" (§3.1.2, footnote 21).
Relevance: names concrete EU infrastructure for the attributable agent identity that [BP04](../best-practices/04-govern-autonomy-and-accountability.md) requires and for the interface provenance that [BP03](../best-practices/03-register-and-vet-interfaces.md) asks registries to record.
Audiences: providers, governance.

**6. Scientific developments count as matters of public interest.**
Text addresses matters of public interest if it covers, among other topics, "any economic, financial, political, scientific, or cultural development that may be relevant subject of public debate", and what counts "can evolve over time and across contexts" (§6.2.1, point 131).
Published means accessible to an indeterminate, fairly large number of unrelated readers, whether or not against payment (§6.2.1, point 131).
Relevance: AI-generated text about a scientific development, published to inform the public, falls inside Article 50(4) unless the human-review exception applies.
Audiences: practitioners, providers, governance.

**7. Human review is defined, and academic peer review is named as a qualifying example.**
"Human review refers to the deliberate examination of the substance of the content by one or more natural persons possessing relevant knowledge and professional judgement pertaining to the subject matter under scrutiny (e.g. academic peer review or professional validation chains).
Fact-checking the accuracy of the content is a minimum requirement that should be part of that review" (§6.2.3, point 134).
Against that: "Superficial, solely formal or procedural checks (e.g. spell-checking or grammatical correction), the mere existence of an editorial policy, automated review processes or cursory editorial approval without substantive engagement by the human reviewer or the editorial entity, cannot fulfil the conditions for human review or editorial control" (§6.2.3, point 135).
A worked negative example is text reviewed and edited by another AI system where a human performs only a superficial grammatical check (§6.2.3).
Relevance: a legal definition of a human check that has to work, which is the substance of [BP09](../best-practices/09-human-in-the-loop.md) atom bp9-a5.
Audiences: practitioners, governance, providers.

**8. A human check placed before the last AI step does not count.**
"Where AI systems are used to modify, supplement, or reformulate content following editorial sign-off, the resulting content must be treated as AI-generated or manipulated for the purposes of Article 50(4) AI Act.
Any substantive AI intervention occurring after the human review or editorial control process has taken place will therefore cause the exception to become void" (§6.2.3, point 136).
Relevance: makes the order of steps part of the requirement, so a workflow has to record when the human check happened relative to the agent's edits ([BP09](../best-practices/09-human-in-the-loop.md), [BP07](../best-practices/07-provenance-and-citation.md)).
Audiences: practitioners, providers.

**9. Editorial responsibility must sit with a named person or function, findable in public.**
A legal or natural person must "hold the ultimate legal responsibility over the publication of the content, including the human review or editorial control (e.g. an individual, editorial board, or the publishing company)", and "the identity and contact details of the legal person, the natural person or the function with editorial responsibility should be made publicly available on an easily findable location" (§6.2.3, point 138).
A qualifying example is "An AI-manipulated academic blog which has undergone internal peer review and where the respective research centre managing the blog holds editorial responsibility" (§6.2.3).
Relevance: matches the named-owner requirement in [BP04](../best-practices/04-govern-autonomy-and-accountability.md) atom bp4-a5, and adds that the name has to be published.
Audiences: governance, providers.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | context for [BP07](../best-practices/07-provenance-and-citation.md) (dates the marking duty) | |
| 2 | | scope: places most research use outside Article 50 |
| 3 | context for [BP08](../best-practices/08-evaluate-tools-before-trust.md) (real-world testing is not exempt) | |
| 4 | [BP07](../best-practices/07-provenance-and-citation.md) (bp7-a2), [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a6) | |
| 5 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a6), context for [BP03](../best-practices/03-register-and-vet-interfaces.md) | |
| 6 | [BP07](../best-practices/07-provenance-and-citation.md) (bp7-a2) | |
| 7 | [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a5) | |
| 8 | [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a5, bp9-a6) | |
| 9 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a5) | |

Hook 2 is the one tension, and it runs the other way from most: the guidelines confirm that scientists doing research are largely outside this obligation.
The record's practices are not restatements of Article 50 and should not be presented as compliance advice.
They hold for scientific reasons, and Article 50 shows that a regulator independently arrived at the same requirements for the cases it does cover.

## Proposed changes to practices

For editor review.
Not applied.

- [ ] Add these guidelines as a source on [BP07](../best-practices/07-provenance-and-citation.md): agent self-disclosure of artificial nature and of the principal it acts for, at authorisation, reporting, and validation steps (hook 4), and the machine-readable marking duty under Article 50(2) (hook 1).
- [ ] Add these guidelines as a source on [BP09](../best-practices/09-human-in-the-loop.md): the definition of human review that qualifies, with superficial and automated review excluded (hook 7), and the rule that any substantive AI edit after the human check voids it (hook 8).
- [ ] Add these guidelines as a source on [BP04](../best-practices/04-govern-autonomy-and-accountability.md): editorial responsibility held by a named person or function whose contact details are published (hook 9), and verifiable agent identity through electronic attestations (hook 5).
- [ ] Add one Examples bullet on [BP09](../best-practices/09-human-in-the-loop.md) for the ordering case: an agent rewrites a passage after the human sign-off, so the review no longer covers what was published (hook 8). The rubber-stamp case is already covered by the existing volume example.
- [ ] Add one Examples bullet on [BP07](../best-practices/07-provenance-and-citation.md) for the delegated-input case: an agent asking for approval says when the input it is acting on came from another agent rather than from the person (hook 4).
- [ ] Record somewhere outside the practices (for example `about/how-the-record-works.md`) that the practices are not compliance requirements, since Article 2(6) puts most research use outside the Act (hook 2). Nothing on the site currently states this.
- [x] Update [ref-eu-ai-act](ref-eu-ai-act.md) to record Article 50 and its 2 August 2026 application date, and the Article 2(6) and 2(8) research exclusions.
- [x] Add [ref-transparency-cop-2026](ref-transparency-cop-2026.md) for the Code of Practice that Article 50(7) provides for.
- [ ] No new practice. The guidelines ground existing practices from an official source; they add no requirement the record does not already state.

## Cautions and gaps

The guidelines are a non-binding first interpretation.
The Commission states it "may decide to withdraw or amend these Guidelines" in light of enforcement experience and rulings of the Court of Justice (§9, point 155).
Weight them as the regulator's current reading, not as settled law.

The Article 2(6) research exclusion limits how far any of this reaches into science.
A scientist running an agent on their own research is generally outside Article 50, so nothing here obliges them to mark or disclose anything under this regulation.
Journal and publisher policies still do, and [ICMJE and COPE](ref-icmje-cope-2023.md) remain the operative rule for authorship and disclosure in publication.

Article 50 is about signalling that content is artificial.
It says nothing about whether the content is correct, where its claims come from, or whether cited work has been retracted.
The marking duty therefore supports the human-and-agent attribution half of [BP07](../best-practices/07-provenance-and-citation.md) and not the source-traceability half.

The subject throughout is disclosure to natural persons.
Backend agent-to-agent calls are explicitly outside Article 50(1), and much scientific agent work is exactly that, so the obligation misses the pipelines where provenance is hardest to keep.

High-risk duties are not covered here and remain deferred to 2 December 2027 and 2 August 2028 under the [AI Omnibus](ai-omnibus-2026.md).
The penalties that attach to Article 50 from 2 August 2026 (up to EUR 15 000 000 or 3% of total worldwide annual turnover, whichever is higher, per §8.3, point 152) are enforcement context, not practice material.
