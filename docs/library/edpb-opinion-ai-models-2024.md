---
title: EDPB Opinion 28/2024 on personal data in AI models (2024)
source_type: guideline
issuing_body: European Data Protection Board
published: 17 December 2024
doi_or_url: https://www.edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf
distilled_on: 2026-09-05
status: draft
tags: [library, regulation]
comments: true
---

# EDPB Opinion 28/2024 on personal data in AI models (2024)

!!! info "Source"
    **Document:** "Opinion 28/2024 on certain data protection aspects related to the processing of personal data in the context of AI models".
    **Issuing body:** European Data Protection Board (EDPB), adopted under Article 64(2) GDPR at the request of the Irish supervisory authority.
    **Date:** 17 December 2024.
    **Distilled:** 2026-09-05.

## Summary

The Opinion is the joint position of the EU data protection authorities on how the GDPR applies to AI models trained on personal data.
It answers four questions: when a model can be treated as anonymous, how legitimate interest can serve as the legal basis in development and in deployment, and what an unlawful development phase means for later use of the model, including use by a different organisation.
It is addressed to supervisory authorities and is legal analysis, not evidence about harm.
Three findings bear on this record.
A model trained on personal data is not anonymous by default.
An organisation that deploys someone else's model has to check that the model was developed lawfully, and may not rely on the developer's own declaration.
The remedies for unlawful training reach the model itself.
The rest (web scraping for training data, the developer's balancing test) is developer-facing and is cited here as context only.

## Hooks, with citations

**1. A model trained on personal data is not anonymous by default.**
The document: "the EDPB considers that AI models trained on personal data cannot, in all cases, be considered anonymous. Instead, the determination of whether an AI model is anonymous should be assessed, based on specific criteria, on a case-by-case basis" (para 34, p. 14).
For anonymity, "both (i) the likelihood of direct (including probabilistic) extraction of personal data regarding individuals whose personal data were used to train the model; as well as (ii) the likelihood of obtaining, intentionally or not, such personal data from queries, should be insignificant for any data subject" (para 43, p. 16).
Relevance: data sent for training can persist in the model as personal data; this is the premise behind the record's line that model training cannot be undone ([BP10](../best-practices/10-screen-dual-use-high-consequence.md), bp10-a5).
Audiences: providers, governance, practitioners.

**2. An assertion of anonymity is not enough; the claim has to be demonstrated.**
The document: "a mere assertion of anonymity of the model is not enough to exempt it from the application of the GDPR" (para 134, p. 35).
By default, supervisory authorities "should consider that AI models are likely to require a thorough evaluation of the likelihood of identification to reach a conclusion on their possible anonymous nature" (para 43, p. 16).
Relevance: a provider's statement that a model or service holds no personal data is a claim to be checked, not a property to be assumed ([BP03](../best-practices/03-register-and-vet-interfaces.md), bp3-a5).
Audiences: providers, governance.

**3. Each controller is responsible for the lawfulness of its own processing.**
The document: "according to Article 5(1)(a) GDPR, read in light of Article 5(2) GDPR, each controller should ensure the lawfulness of the processing it conducts and be able to demonstrate it. Therefore, SAs should assess the lawfulness of the processing carried out by (i) the controller that originally developed the AI model; and (ii) the controller that acquired the AI model and processes the personal data by itself" (para 126, p. 33).
Relevance: an institution that runs an agent on an external model is a controller for what the agent sends, whatever the provider's terms say; the duty to hold a lawful basis and a compliant contract sits with the institution.
Audiences: governance, providers.

**4. The deploying organisation has to check that the model was developed lawfully.**
The document: supervisory authorities "should take into account whether the controller deploying the model conducted an appropriate assessment, as part of its accountability obligations to demonstrate compliance with Article 5(1)(a) and Article 6 GDPR, to ascertain that the AI model was not developed by unlawfully processing personal data. Such evaluation by SAs should take into account whether the controller has assessed some non-exhaustive criteria, such as the source of the data and whether the AI model is the result of an infringement of the GDPR, particularly if it was determined by a SA or a court" (para 129, p. 34).
The depth of the check scales with risk: "The degree of the assessment of the controller and the level of detail expected by SAs may vary depending on diverse factors, including the type and degree of risks raised by the processing in the AI model during its deployment" (para 130, p. 34).
Relevance: due diligence on the provider is part of deploying a model, and it is the deployer's duty; it is the vetting step [BP03](../best-practices/03-register-and-vet-interfaces.md) describes for interfaces, applied to the model behind them.
Audiences: governance, providers.

**5. A provider's self-declaration is not a finding of compliance.**
The document: the AI Act's EU declaration of conformity "contains a statement that the relevant AI system complies with EU data protection laws. The EDPB notes that such a self-declaration may not constitute a conclusive finding of compliance under the GDPR" (para 131, p. 34).
Relevance: a declared or listed status is not a safety check ([BP03](../best-practices/03-register-and-vet-interfaces.md), bp3-a5).
Audiences: governance, providers.

**6. Remedies for unlawful training reach the model.**
The document: corrective measures "may include, for instance, issuing a fine, imposing a temporary limitation on the processing, erasing part of the dataset that was processed unlawfully or, where this is not possible, depending on the facts at hand, having regard to the proportionality of the measure, ordering the erasure of the whole dataset used to develop the AI model and/or the AI model itself" (para 114, p. 32).
Relevance: once data has trained a model, the ways back are retraining or deleting the model; this is what the record means by an irreversible data commitment ([BP10](../best-practices/10-screen-dual-use-high-consequence.md), bp10-a5).
Audiences: providers, governance.

**7. Mitigating measures in deployment are technical measures in the system.**
The document lists, among deployment-phase measures, "Technical measures may for instance be put in place to prevent the storage, regurgitation or generation of personal data, especially in the context of generative AI models (such as output filters), and/or to mitigate the risk of unlawful reuse by general purpose AI models" and "post-training techniques that attempt to remove or suppress personal data" (para 107, p. 30).
Relevance: the measures the authorities expect are in the system, which is the position of [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1).
Audiences: providers.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5) | |
| 2 | [BP03](../best-practices/03-register-and-vet-interfaces.md) (bp3-a5) | |
| 3 | the proposed BP04 atoms (see the [ERA guidelines entry](era-living-guidelines-genai-2026.md)) | |
| 4 | the proposed BP04 atoms; context for [BP03](../best-practices/03-register-and-vet-interfaces.md) | |
| 5 | [BP03](../best-practices/03-register-and-vet-interfaces.md) (bp3-a5) | |
| 6 | [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5) | |
| 7 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1) | |

No contradictions.
The Opinion does not say that using a provider in a given country is lawful or unlawful.
It says the organisation deploying the model has to check, and has to be able to show that it checked.

## Proposed changes to practices

These are proposals for editor review, not applied here.

- [ ] Add this entry to the `sources:` of [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5) and [BP03](../best-practices/03-register-and-vet-interfaces.md) (bp3-a5); the provenance edges are in place.
- [ ] Cite hooks 3 and 4 as the legal ground for the two BP04 atoms proposed in the [ERA guidelines entry](era-living-guidelines-genai-2026.md): the institution is the controller, and checking the provider is its duty.
- [ ] Consider one sentence in the [BP03](../best-practices/03-register-and-vet-interfaces.md) governance tab: vetting covers the model behind an interface as well as the interface itself (source and lawfulness of its training data), with this Opinion as the source.
- [x] No new practice page.

## Cautions and gaps

The Opinion is addressed to supervisory authorities; controllers read it as a statement of what they will be asked to show, not as guidance written for them.
It concerns AI models, not agents; nothing in it addresses an agent that reads local files and calls a remote model.
Its anonymity analysis concerns models trained on personal data; most scientific use of external models is deployment, where hooks 3, 4, and 7 apply.
It is legal analysis and contains no evidence about how often the risks it describes are realised.
Later EDPB work may supersede parts of it: Guidelines 03/2026 on web scraping in the context of generative AI (July 2026) and guidelines on the interplay between the GDPR and the AI Act expected by the end of 2026, as noted in the [CNIL and CIANum note](ref-cnil-cianum-agentic-ai-2026.md).
The developer-facing analysis of web scraping and the legitimate-interest balancing test is out of scope for this record and is not distilled.
