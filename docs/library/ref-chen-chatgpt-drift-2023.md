---
title: "How Is ChatGPT's Behavior Changing Over Time? (Chen, Zaharia & Zou 2024)"
ref_id: chen-chatgpt-drift-2023
source_type: paper
issuing_body: "Chen, Zaharia & Zou; Harvard Data Science Review"
published: 2024
doi_or_url: https://doi.org/10.1162/99608f92.5317da47
added_on: 2026-09-16
grounds: [BP-01]
tags: [library, reference]
comments: true
---

# How Is ChatGPT's Behavior Changing Over Time? (Chen, Zaharia & Zou 2024)

!!! info "Reference"
    **Citation:** Chen, L., Zaharia, M. and Zou, J. "How Is ChatGPT's Behavior Changing Over Time?" *Harvard Data Science Review* 6(2) (2024). **Type:** paper. **Link:** [doi.org/10.1162/99608f92.5317da47](https://doi.org/10.1162/99608f92.5317da47); open-access preprint [arXiv:2307.09009](https://arxiv.org/abs/2307.09009) (2023).

## What it is

A measurement study of two hosted model services (GPT-3.5 and GPT-4) on the same tasks at two dates in 2023.
The same service name returned substantially different behaviour within three months: GPT-4's accuracy at identifying prime versus composite numbers fell from 84% (March 2023) to 51% (June 2023).

## Role in the record

- Grounds [BP01](../best-practices/01-match-method-to-task.md): a hosted frontier model is a dependency the adopter does not control. Its behaviour can change with no version change visible to the user, so a workflow validated on it can need revalidation, which a script or pipeline the adopter controls does not.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
