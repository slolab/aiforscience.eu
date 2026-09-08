---
title: "CNIL and CIANum: Agentic AI and personal data protection (2026)"
ref_id: cnil-cianum-agentic-ai-2026
source_type: report
issuing_body: "Commission nationale de l'informatique et des libertés (CNIL) and Conseil de l'IA et du Numérique (CIANum)"
published: 2026
doi_or_url: https://www.cnil.fr/sites/default/files/2026-07/ia-cianum-cnil.pdf
added_on: 2026-09-05
grounds: [BP-04, BP-09]
tags: [library, reference]
comments: true
---

# CNIL and CIANum: Agentic AI and personal data protection (2026)

!!! info "Reference"
    **Citation:** CNIL and Conseil de l'IA et du Numérique. "IA agentique et protection des données personnelles : équation à inconnues multiples pour les utilisateurs", exploratory note, July 2026. In French. **Type:** regulator and advisory-council note. **Link:** [cnil.fr](https://www.cnil.fr/sites/default/files/2026-07/ia-cianum-cnil.pdf).

## What it is

A 17-page exploratory note from the French data protection authority and the national AI advisory council on how the GDPR applies to agentic AI.
It holds that agents remain fully subject to the GDPR, that persistent memory and autonomous action across several services strain purpose limitation, data minimisation, and storage limitation, and that the flows between agents and services blur who is responsible for what (pp. 1-2, 11).
The AI Act contains no agent-specific rules (p. 1).
The note proposes measures on both sides.
Legal: traceability so that "Pour chaque tâche exécutée, l'utilisateur devrait pouvoir identifier les données personnelles mobilisées, les agents intervenus, les services tiers sollicités, les échanges réalisés ainsi que leur chronologie" (for each task executed, the user should be able to identify the personal data used, the agents involved, the third-party services called, the exchanges made, and their sequence; p. 13); user control over which data agents can access (p. 13).
Technical: detection and filtering of unintended use, applied at every model call, including calls made by orchestrating or specialised agents after the user's first request (pp. 13-14); memory compartmentalised per agent and per processing, and deployment in an isolated environment (sandboxing) so that "Le risque d'exfiltration de données se limiterait alors au périmètre de données susceptibles d'être traitées par l'IA agentique" (p. 14); classification of the possible actions on each connected service by risk level ("accès à des données, modification et suppression de donnés, envoi de données hors système et typologie de données traitées"), with human validation before critical actions and a kill switch to stop a running process (pp. 14-15); independent evaluation of agents' data protection and security (p. 15).
It notes that providers may reuse user data to train models, concentrating data with few actors (p. 16), and that EDPB and Commission guidelines on the interplay of the GDPR and the AI Act are expected by the end of 2026 (p. 12).

## Role in the record

- Grounds [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1, bp4-a3, bp4-a6): sandboxing and filtering as limits in the system; actions classified by risk per connected service with a stop control; per-task traceability of data, agents, and services.
- Grounds [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a1): human validation required for actions whose consequences are judged critical, with the user choosing which actions need it.
- Limits: exploratory and non-prescriptive, as the authors say; it announces no binding guidance. It addresses consumer-facing agents and user control; the research setting is not discussed.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
