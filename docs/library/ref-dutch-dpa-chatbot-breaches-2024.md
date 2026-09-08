---
title: "Dutch DPA: AI chatbot use leads to data breaches (2024)"
ref_id: dutch-dpa-chatbot-breaches-2024
source_type: guidance
issuing_body: "Autoriteit Persoonsgegevens (Dutch Data Protection Authority)"
published: 2024
doi_or_url: https://www.autoriteitpersoonsgegevens.nl/en/current/caution-use-of-ai-chatbot-may-lead-to-data-breaches
added_on: 2026-09-05
grounds: [BP-04, BP-10]
tags: [library, reference]
comments: true
---

# Dutch DPA: AI chatbot use leads to data breaches (2024)

!!! info "Reference"
    **Citation:** Autoriteit Persoonsgegevens. "Caution: use of AI chatbot may lead to data breaches", 6 August 2024. **Type:** regulator notice. **Link:** [autoriteitpersoonsgegevens.nl](https://www.autoriteitpersoonsgegevens.nl/en/current/caution-use-of-ai-chatbot-may-lead-to-data-breaches).

## What it is

A regulator's notice that it "has received a number of notifications of data breaches caused by employees sharing personal data of, for example, patients or customers with a chatbot that uses artificial intelligence (AI)".
In one case "an employee of a GP practice had entered medical data of patients into an AI chatbot, contrary to the agreements"; in another, a telecom employee entered a file with customer addresses.
The regulator's reasoning: "Most companies behind the chatbots store all data entered. As a result, these data end up on the servers of those tech companies, often without the person who entered the data realising and without that person knowing exactly what that company will do with those data."
Entering personal data into a chatbot against the employer's rules is a reportable breach; doing so as organisational policy "is not a data breach, but often not permitted by law".
The regulator asks organisations to state which data may and may not be entered, and adds: "Organisations could also arrange with the provider of a chatbot that this provider will not store the data entered."

## Role in the record

- Grounds [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1): the GP practice had rules, and the breach happened "contrary to the agreements". A written rule did not prevent the data from leaving; a contract with the provider, or a system that cannot send the data, would have.
- Grounds [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5): a regulator's statement that entered data is stored by the provider and leaves the entering organisation's control.
- Recorded in the [Failures log](../best-practices/failures.md).
- Limits: the cases are from healthcare delivery and telecoms, not research, and concern chatbots, not agents. The structure (staff use a consumer tool with sensitive data because it is at hand) is what transfers to any lab.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
