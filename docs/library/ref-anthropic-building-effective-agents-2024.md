---
title: "Building Effective AI Agents (Anthropic, 2024)"
ref_id: anthropic-building-effective-agents-2024
source_type: guidance
issuing_body: "Anthropic"
published: 2024
doi_or_url: https://www.anthropic.com/engineering/building-effective-agents
added_on: 2026-07-27
grounds: [BP-01]
tags: [library, reference]
comments: true
---

# Building Effective AI Agents (Anthropic, 2024)

!!! info "Reference"
    **Citation:** Anthropic. "Building Effective AI Agents" (Engineering, 2024). **Type:** guidance. **Link:** [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents).

## What it is

Vendor engineering guidance on when and how to build agentic systems.
It distinguishes workflows (predefined paths) from agents (model-driven control) and advises starting with the simplest approach that works.

## Role in the record

- Grounds [BP01](../best-practices/01-match-method-to-task.md): find the simplest solution and add agentic complexity only when the task needs flexible, model-driven decisions at scale; agents trade latency and cost for task performance, and a single optimised call is often enough.

Atom-level for/against detail and quotes are in the provenance data
(`assets/provenance.yml`), keyed by practice atom.
