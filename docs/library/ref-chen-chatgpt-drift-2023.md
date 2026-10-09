---
title: "How Is ChatGPT's Behavior Changing Over Time? (Chen, Zaharia & Zou 2023)"
ref_id: chen-chatgpt-drift-2023
source_type: paper
issuing_body: "Chen, Zaharia & Zou, arXiv preprint"
published: 2023
doi_or_url: https://arxiv.org/abs/2307.09009
added_on: 2026-09-16
grounds: [BP-01]
tags: [library, reference]
comments: true
---

# How Is ChatGPT's Behavior Changing Over Time? (Chen, Zaharia & Zou 2023)

!!! info "Reference"
    **Citation:** Chen, L., Zaharia, M. and Zou, J. "How Is ChatGPT's Behavior Changing Over Time?" arXiv:2307.09009 (2023). **Type:** paper (preprint). **Link:** [arXiv:2307.09009](https://arxiv.org/abs/2307.09009).

## What it is

A measurement study of two hosted model services (GPT-3.5 and GPT-4) on the same tasks at two dates in 2023.
The same service name returned substantially different behaviour within three months: GPT-4's accuracy at identifying prime versus composite numbers fell from 84% (March 2023) to 51% (June 2023).

## Role in the record

- Grounds [BP01](../best-practices/01-match-method-to-task.md): a hosted frontier model is a dependency the adopter does not control. Its behaviour can change with no version change visible to the user, so a workflow validated on it can need revalidation, which a script or pipeline the adopter controls does not.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
