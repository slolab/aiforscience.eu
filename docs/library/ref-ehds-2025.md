---
title: "European Health Data Space Regulation (Regulation (EU) 2025/327)"
ref_id: ehds-2025
source_type: policy
issuing_body: "European Union"
published: 2025
doi_or_url: https://eur-lex.europa.eu/eli/reg/2025/327/oj
added_on: 2026-09-05
grounds: [BP-02, BP-04]
tags: [library, reference]
comments: true
---

# European Health Data Space Regulation (Regulation (EU) 2025/327)

!!! info "Reference"
    **Citation:** European Union. "Regulation (EU) 2025/327 of the European Parliament and of the Council of 11 February 2025 on the European Health Data Space", OJ L, 5 March 2025. **Type:** policy. **Link:** [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2025/327/oj).

## What it is

The EU regulation that governs, among other things, secondary use of electronic health data for research.
Access for secondary use is granted "only through a secure processing environment" (Art 73(1)), with access restricted to persons named in the data permit, state-of-the-art measures against "unauthorised reading, copying, modification or removal", and "identifiable logs of access to and activities in the secure processing environment" kept for at least one year (Art 73(1)(a), (b), (e)).
Users may download only "non-personal electronic health data, including electronic health data in an anonymised statistical format" (Art 73(2)).
Permitted purposes include scientific research and "training, testing and evaluation of algorithms, including in ... AI systems" (Art 53(1)(e)(ii)); prohibited uses include detrimental decisions about individuals and marketing (Art 54).
Downloading personal health data outside the secure processing environment is listed among the serious infringements subject to administrative fines (Recital 103).
Where a third party manages the environment, Article 28 GDPR and, where applicable, Chapter V apply (Recital 77).
The secondary-use chapter applies from 26 March 2029, with some provisions earlier and later (Art 105).

## Role in the record

- Grounds [BP02](../best-practices/02-default-to-agent-accessibility.md) (bp2-a4): the secure processing environment is the legal form of access governed by the resource for one class of controlled-access data. A life-science instance, cited as an example.
- Grounds [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a6): identifiable, retained access logs as a legal requirement.
- Context for [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5) and for the protected research tier described in the [Gagneur entry](gagneur-rare-disease-patient-data-2026.md): under this regulation an agent working on permitted health data may compute inside the environment but may not move personal data out of it, to a model provider or anywhere else.
- Limits: health data only; the domain-neutral pattern is governed access with no personal-data egress. Most provisions are not yet applicable.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
