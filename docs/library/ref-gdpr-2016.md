---
title: "EU General Data Protection Regulation (Regulation (EU) 2016/679)"
ref_id: gdpr
source_type: policy
issuing_body: "European Union"
published: 2016
doi_or_url: https://eur-lex.europa.eu/eli/reg/2016/679/oj
added_on: 2026-07-28
grounds: [BP-04, BP-10]
tags: [library, reference]
comments: true
---

# EU General Data Protection Regulation (Regulation (EU) 2016/679)

!!! info "Reference"
    **Citation:** European Union. "Regulation (EU) 2016/679 (General Data Protection Regulation)" (2016). **Type:** policy. **Link:** [eur-lex.europa.eu](https://eur-lex.europa.eu/eli/reg/2016/679/oj).

## What it is

The European Union regulation on the protection of personal data.
Where processing rests on consent, the data subject has the right to withdraw it at any time (Article 7(3)), and a right to erasure of personal data (Article 17).
Processing of special categories of data, including health and genetic data, is prohibited unless an Article 9(2) exception applies.
Controllers implement data protection by design and by default (Article 25).
A controller that lets another organisation process personal data on its behalf needs a contract that binds that processor to documented instructions (Article 28).
Transfers to third countries need an adequacy decision, appropriate safeguards such as standard contractual clauses, or a derogation (Articles 44 to 49); a foreign court order or administrative decision is enforceable only if based on an international agreement (Article 48).
Processing for scientific research is subject to safeguards (Article 89).

## Role in the record

- Grounds [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1): Article 25 requires the protection to be built into the system and its defaults. That is the record's position that an agent's limits belong in the system rather than in written policy alone.
- Would ground the two BP04 atoms proposed in the [ERA guidelines entry](era-living-guidelines-genai-2026.md): Article 28 (processor contract), Articles 44 to 49 (transfer basis), and Article 48 (foreign orders) are the provisions a service's terms have to satisfy before personal data may reach it.
- Grounds [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5): consent is revocable and erasure is a right, so personal data held under withdrawable consent cannot be authorised for an irreversible use such as third-party model training or a perpetual licence.

Atom-level for/against detail and quotes are in the provenance data
(`assets/provenance.yml`), keyed by practice atom.
