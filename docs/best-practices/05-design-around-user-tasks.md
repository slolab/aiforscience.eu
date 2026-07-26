---
title: Design agent interfaces around user tasks, not raw endpoints
nav_title: "BP5 User-centric design"
practice_id: BP-05
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Best Practice, item 4; July 2026 discussion"
  - title: "Anthropic, Writing effective tools for agents (2025)"
    ref: library/ref-anthropic-writing-tools-2025.md
    locator: "avoid wrapping existing endpoints; consolidate into task tools"
  - title: "Anthropic, Code execution with MCP (2025)"
    ref: library/ref-anthropic-code-execution-mcp-2025.md
    locator: "token cost of per-endpoint tool use; progressive disclosure"
  - title: "Anthropic, Advanced tool use (2025)"
    ref: library/ref-anthropic-advanced-tool-use-2025.md
    locator: "tool-surface size vs selection accuracy and cost"
  - title: "Model Context Protocol specification"
    ref: library/ref-mcp-spec.md
    locator: "the interface substrate (MCP servers, tools)"
layer: Method
hitl: n/a
tags: [provider, practitioner, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- An agent [interface](../glossary.md#interface) works best when it is built around the tasks a user wants to complete.
  { #bp5-a1 }
- Simply passing on pre-existing endpoints ("wrapping") is fast but often does not respect agent patterns.
  { #bp5-a2 }
- Wrapping an API one call at a time forces the [agent](../glossary.md#agent) to assemble each task itself, which is slow, costly, and error-prone.
  { #bp5-a3 }

</div>

=== "Practitioners"

    If a routine task takes many awkward steps, report it.
    Providers shape interfaces around real use from this kind of feedback, and your cases are the evidence they need.

=== "Providers"

    Start from the tasks users do, not the endpoints you already have.
    Shape operations so a common goal takes as few calls as possible, and watch for ones that trigger many small calls.
    Learn what your users want; it may be different from your assumptions.

=== "Governance"

    Interfaces built around user tasks cut load and cost, and work more reliably.
    Governance is barely involved directly, but it is worth supporting and funding the user research that makes this possible.

## Reasons

An API for programmers exposes small operations that a developer combines by hand.
An agent given the same operations has to work out how to combine them for every task.
That means many small calls, more server load and cost, and more chances to go wrong.
Vendor engineering guidance reports the same failure mode: tools that merely wrap existing endpoints perform worse than a few tools built for high-impact workflows, and a large, fine-grained tool surface measurably raises token cost and lowers the agent's accuracy at picking the right call.
An interface built around real tasks (the questions users ask, the analyses they run) lets the agent reach the goal in a few calls.
There is more than one way to get there: shaping task-level tools is one, and for very large APIs, letting the agent write code against the endpoints (progressive disclosure, code execution) is another.
Both need to know what users are trying to do, and providers often do not, so learning the real use cases is part of the job.

## Examples

- Operations named and scoped for user tasks, so a common goal takes one call or a few, not a long chain of primitives.
- Task design based on the queries users actually make, not the shape of the existing endpoints.
- A watch on call patterns: an interface that triggers many small calls is probably misaligned with how it is used.
- For very large APIs, a code-execution or search-and-call surface as an alternative to hand-building a task tool for every workflow.
- Effort spent understanding users, since providers rarely have a full picture of what agents are asked to do.

!!! info "Practice metadata"
    **Status:** <span class="afs-badge afs-badge--draft">draft</span> ·
    **Endorsed by:** none yet ·
    **Last reviewed:** 2026-07-26

## Sources

- [ELIXIR TF Agentic AI: agenda and rolling best practice (2026)](../library/elixir-tf-agentic-ai-2026.md), Best Practice item 4, and the July 2026 discussion on providers' limited view of their users.
- [Anthropic, Writing effective tools for agents (2025)](../library/ref-anthropic-writing-tools-2025.md).
  Wrapping existing endpoints is a common error; build a few tools for high-impact workflows.
  Vendor-primary grounding for this practice.
- [Anthropic, Code execution with MCP (2025)](../library/ref-anthropic-code-execution-mcp-2025.md) and [Advanced tool use (2025)](../library/ref-anthropic-advanced-tool-use-2025.md).
  Quantify the token cost of per-endpoint tool use and the accuracy loss from a large tool surface; document progressive disclosure as the alternative remedy.
- [Model Context Protocol specification](../library/ref-mcp-spec.md).
  The interface substrate the practice is about.

## Change history

- 2026-07-26: Rewritten to add vendor-primary grounding (the Anthropic tool-design guidance, with quantified evidence) and to note the two accepted remedies to endpoint-wrapping (task-level tools and code execution for very large APIs).
  "Providers don't know their users" kept as stated judgement.
- 2026-07-25: Created from the ELIXIR TF distillation (hooks 5, 12).
