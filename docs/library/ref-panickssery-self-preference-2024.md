---
title: "LLM Evaluators Recognize and Favor Their Own Generations (Panickssery, Bowman & Feng 2024)"
ref_id: panickssery-self-preference-2024
source_type: paper
issuing_body: "Panickssery, Bowman & Feng, arXiv preprint"
published: 2024
doi_or_url: https://arxiv.org/abs/2404.13076
added_on: 2026-09-16
grounds: [BP-08]
tags: [library, reference]
comments: true
---

# LLM Evaluators Recognize and Favor Their Own Generations (Panickssery, Bowman & Feng 2024)

!!! info "Reference"
    **Citation:** Panickssery, A., Bowman, S. R. and Feng, S. "LLM Evaluators Recognize and Favor Their Own Generations." arXiv:2404.13076 (2024). **Type:** paper (preprint). **Link:** [arXiv:2404.13076](https://arxiv.org/abs/2404.13076).

## What it is

A study of self-preference in language models used as evaluators: an evaluator scores its own outputs higher than others' while human annotators consider them of equal quality.
Models such as GPT-4 and Llama 2 distinguish their own text from other models' and from humans' with non-trivial accuracy, and that self-recognition correlates linearly with the strength of the self-preference bias.

## Role in the record

- Grounds [BP08](../best-practices/08-evaluate-tools-before-trust.md): a judge model from the same family as the system under test is not independent evidence. The bias is measured, and it grows with the judge's ability to recognise its own kind of output.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
