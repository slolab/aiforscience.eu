---
title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
source_type: other
issuing_body: ELIXIR Europe, AI Ecosystem Focus Group, TF Agentic AI
published: 2026 (rolling document; meetings May to July 2026)
doi_or_url: https://docs.google.com/document/d/1brlPU2qEvx6bpzUNmHSjmGragoR21bbQqiobGJlZ_NQ/
distilled_on: 2026-07-25
status: draft
tags: [library, agentic-ai]
comments: true
---

# ELIXIR TF Agentic AI: agenda and rolling best practice (2026)

!!! info "Source"
    **Document:** "Agenda 2026 TF Agentic AI Agenda", the task force's working agenda, which carries two rolling sub-documents: "Best Practice – Agentic AI" and "Failures in Agentic AI". **Issuing body:** ELIXIR Europe, AI Ecosystem Focus Group, Task Force Agentic AI. **Date:** rolling; meetings May to July 2026. **Link:** [open to read](https://docs.google.com/document/d/1brlPU2qEvx6bpzUNmHSjmGragoR21bbQqiobGJlZ_NQ/). **Distilled:** 2026-07-25.
    Personal data (attendee lists, apologies, chat transcripts) is excluded by design; this entry distills the Best Practice and Worst Practice sections and the framing text.

## Summary

The ELIXIR AI Ecosystem Focus Group runs a task force on agentic AI for life-science research infrastructure.
It keeps a rolling list of best practices, revised in monthly meetings, learned from early adopters and written for the larger group building durable services.
The ten practices cover how providers open data resources and tools to agents: what to expose, how to design the interface, how to make answers traceable, and how to keep access safe and manageable.
This reading generalises from life-science infrastructure to scientific services in general; ELIXIR-specific cases are treated as examples.
The document is the main source for the provider-facing practices here.

## Hooks, with citations

**1.
Pioneers and settlers are different populations and need different support.** The document: "There are two groups of users: pioneers and settlers. ...
Pioneers should be enabled ('the best you can do is get out of their way') and observed.
Learning from them is what yields the good practices below.
Settlers are far more numerous, coming in after the pioneers have moved on, to build something sustainable."
(Best Practice, framing paragraph).
Relevance: an operating principle for how the record is made, adopted in [the mission](../about/mission.md); it is not itself a practice.
Audiences: practitioners, providers, governance.

**2.
Default to agent-accessibility, but be selective about depth.** The document: "Agent access to resources is to be assumed, while accepting that not everything needs a bespoke maintained agent-accessible interface.
Prioritisation can follow demand and service tier."
(Best Practice, item 1).
Relevance: sets the provider stance behind [BP02](../best-practices/02-default-to-agent-accessibility.md).
Audiences: providers, governance.

**3.
A typology of resources decides which solution fits which service.** The document: "Generic vs. service-specific agentic interfaces should follow a taxonomy of services."
Generalisable approaches suit widely-used core resources, interoperability resources and deposition databases; long-tail services can be lighter-touch (Best Practice, item 2).
Relevance: the prioritisation mechanism in [BP02](../best-practices/02-default-to-agent-accessibility.md).
Audiences: providers, governance.

**4.
Write documentation with agents in mind.** The document: "Precise, machine-readable, up-to-date.
Docs and docstrings are the primary surface an agent will use; the added precision will be useful to human users as well."
(Best Practice, item 3).
Relevance: grounds [BP05](../best-practices/05-documentation-and-data-for-agents.md).
Audiences: practitioners, providers.

**5.
Design the interface around user tasks, not the underlying API.** The document: "Don't just wrap REST.
Design MCP servers, skills, or plugins to address the expected user queries, rather than simply following the data-driven API."
It warns that misaligned surfaces cause many fine-grained calls, raising server load and cost (Best Practice, item 4).
Relevance: grounds [BP06](../best-practices/06-design-around-user-tasks.md).
Audiences: providers, practitioners.

**6.
Provide structured data and semantics with concrete examples.** The document: "Concrete low-level examples: natural language to query language (SPARQL, Cypher), per-source RAG indexing strategies (e.g., Lucene + FAISS with MCP orchestrator)."
(Best Practice, item 5).
Relevance: the second half of [BP05](../best-practices/05-documentation-and-data-for-agents.md), covering data and worked examples, not only prose docs.
Audiences: practitioners, providers.

**7.
Make provenance and citation first-class.** The document: "Allow verification and tracing of any answer given by an agent.
Allow distinguishing human and LLM-agent contributions."
(Best Practice, item 6).
Relevance: grounds [BP07](../best-practices/07-provenance-and-citation.md).
Audiences: practitioners, providers, governance.

**8.
State the human-in-the-loop level for each use case.** The document: "For each use case, clearly state the HITL level (mandatory, optional, in-process, final check)."
(Best Practice, item 7).
Relevance: grounds [BP09](../best-practices/09-human-in-the-loop.md).
Audiences: practitioners, providers, governance.

**9.
Register agent interfaces through a channel that implies review.** The document: "Register dedicated agent interfaces and tag them. ...
Registration implies a check / human review.
Will be very important to be safer towards malware and prompt injection attacks."
(Best Practice, item 8).
Relevance: grounds [BP03](../best-practices/03-register-and-vet-interfaces.md).
Audiences: providers, governance.

**10.
An approved channel makes agent traffic manageable.** The document: "Find ways to manage agent traffic.
An approved MCP channel can make management of bot traffic easier, but blocking IPs can reduce the resources exposure / usefulness."
(Best Practice, item 9).
Relevance: the traffic-management facet of [BP03](../best-practices/03-register-and-vet-interfaces.md).
Audiences: providers, governance.

**11.
Collect failures as readily as success stories.** The document: "Clear examples of what did not work are as important as the recommendations."
The parallel document, "Failures in Agentic AI", lists cases such as agents reaching legacy APIs over HTTP instead of REST, and scraping of services and databases (Best Practice, item 10; Worst Practice).
Relevance: seeds the [Failures log](../best-practices/failures.md), a record convention rather than a practice.
Audiences: practitioners, providers.

**12.
Providers lack a clear handle on their users.** The document: "Service providers don't have a good handle on their users, which needs to inform the user case-driven development of agentic interfaces for that service."
(Minutes, 1 July 2026, item 4.5, summarising insights from the ELIXIR All-Hands workshop.)
Relevance: reinforces the task-first design in [BP06](../best-practices/06-design-around-user-tasks.md).
Audiences: providers.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | (operating principle, see [mission](../about/mission.md)) | |
| 2, 3 | [BP02](../best-practices/02-default-to-agent-accessibility.md) | |
| 4, 6 | [BP05](../best-practices/05-documentation-and-data-for-agents.md) | |
| 5, 12 | [BP06](../best-practices/06-design-around-user-tasks.md) | |
| 7 | [BP07](../best-practices/07-provenance-and-citation.md) | |
| 8 | [BP09](../best-practices/09-human-in-the-loop.md) | |
| 9, 10 | [BP03](../best-practices/03-register-and-vet-interfaces.md) | |
| 11 | [Failures log](../best-practices/failures.md) | |

No direct tensions with the current practices.
The one internal tension, "default to accessibility" against "not everything needs an interface", is resolved inside BP02 through prioritisation by demand and importance.

## Proposed changes to practices

- [x] Create [BP02](../best-practices/02-default-to-agent-accessibility.md) from hooks 2 and 3.
- [x] Create [BP03](../best-practices/03-register-and-vet-interfaces.md) from hooks 9 and 10.
- [x] Create [BP05](../best-practices/05-documentation-and-data-for-agents.md) from hooks 4 and 6 (replaces the dummy BP0 on documentation).
- [x] Create [BP06](../best-practices/06-design-around-user-tasks.md) from hooks 5 and 12.
- [x] Create [BP07](../best-practices/07-provenance-and-citation.md) from hook 7.
- [x] Create [BP09](../best-practices/09-human-in-the-loop.md) from hook 8.
- [x] Create [BP08](../best-practices/08-evaluate-tools-before-trust.md) from the evaluation gap recorded below (adopter-side evaluation before trust).
- [x] Seed the [Failures log](../best-practices/failures.md) from hook 11.

## Cautions and gaps

- Evaluation and trust of agent interfaces is raised as an open question: how to assess whether a skill or MCP server is useful and safe, without an agreed method.
  This gap is now addressed by [BP08](../best-practices/08-evaluate-tools-before-trust.md), grounded in this entry, which covers adopter-side evaluation before trust.
- The source is a working agenda and a rolling document, not a peer-reviewed or formally endorsed output.
  All derived practices are `draft`.
- ELIXIR-specific instances (Core Data Resources, biocontext.ai, bio.tools) are examples, not requirements.
  The practices state the general form.
- Pioneers and settlers is an operating principle, not a practice and not a tag.
