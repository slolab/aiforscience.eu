---
title: "DSK guidance: Artificial intelligence and data protection (2024)"
ref_id: dsk-ki-datenschutz-2024
source_type: guidance
issuing_body: "Datenschutzkonferenz (conference of the German federal and state data protection authorities)"
published: 2024
doi_or_url: https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf
added_on: 2026-09-05
grounds: [BP-04, BP-10]
tags: [library, reference]
comments: true
---

# DSK guidance: Artificial intelligence and data protection (2024)

!!! info "Reference"
    **Citation:** Konferenz der unabhängigen Datenschutzaufsichtsbehörden des Bundes und der Länder (DSK). "Orientierungshilfe: Künstliche Intelligenz und Datenschutz", Version 1.0, 6 May 2024. In German. **Type:** regulator guidance. **Link:** [datenschutzkonferenz-online.de](https://www.datenschutzkonferenz-online.de/media/oh/20240506_DSK_Orientierungshilfe_KI_und_Datenschutz.pdf).

## What it is

A checklist from the German data protection authorities for organisations selecting, implementing, and using AI applications, written with LLM chatbots in mind.
It distinguishes closed systems, where processing happens in a bounded environment and the provider does not use inputs for training, from open systems run as internet-accessible cloud services, where inputs leave the user's protected area and transfers to third countries are common (§1.7, paras 15-19).
Its conclusion: "Technisch geschlossene Systeme sind daher aus datenschutzrechtlicher Sicht vorzugswürdig" (technically closed systems are therefore preferable from a data protection standpoint; §1.7, para 20).
Controllers check whether inputs and outputs are used for training and whether that can be excluded; "Datenschutzrechtlich vorzugswürdig sind daher Anwendungen, die die Ein- und Ausgabedaten nicht zu Trainingszwecken verwenden" (applications that do not use inputs and outputs for training are therefore preferable; §1.9, para 24).
Where an external provider's application is used, a processor agreement under Article 28 GDPR is usually required (§2.1, para 33).
Employers provide work accounts and devices so that staff do not have to use private accounts (§2.4, para 41), and configure accounts at setup "dass keine Eingabedaten zu Trainingszwecken verarbeitet werden und keine Eingabe-Historie über die Sitzung hinaus gespeichert wird" (so that no input data is processed for training and no input history is kept beyond the session; §2.5, para 43).
The Article 9 prohibition on special-category data applies to input, processing, and output alike (§3.2, para 62).
A companion guidance on technical and organisational measures for developing and operating AI systems followed in June 2025.

## Role in the record

- Grounds [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5): a regulator's preference for applications that do not train on inputs, stated as a selection criterion.
- Grounds [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1): the training and history settings are fixed in the account at setup, not left to each user's discretion.
- Context for the BP04 atoms proposed in the [ERA guidelines entry](era-living-guidelines-genai-2026.md): work accounts, a processor agreement, and a closed system are the three elements that proposal asks institutions to supply.
- Limits: German-language guidance addressed to controllers under German and EU law; the translations here are the record's own. It concerns chatbots used by people, not agents.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
