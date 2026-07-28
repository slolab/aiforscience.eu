---
title: Design agent interfaces around user tasks, not raw endpoints
nav_title: "BP06 Design interfaces around user tasks"
practice_id: BP-06
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
  - title: "MIT Project NANDA, The GenAI Divide (2025)"
    ref: library/mit-genai-divide-2025.md
    locator: "Executive Summary p.3; §5.1 p.15 tools fail on workflow fit"
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
  { #bp6-a1 }
- Simply passing on pre-existing endpoints ("wrapping") is fast but often does not respect agent patterns.
  { #bp6-a2 }
- Wrapping an API one call at a time forces the [agent](../glossary.md#agent) to assemble each task itself, which is slow, costly, and error-prone.
  { #bp6-a3 }

</div>

=== "For practitioners"

    If a routine task takes many awkward steps, report it.
    Providers shape interfaces around real use from this kind of feedback, and your cases are the evidence they need.

=== "For providers"

    Start from the tasks users do, not the endpoints you already have.
    Shape operations so a common goal takes as few calls as possible, and watch for ones that trigger many small calls.
    Learn what your users want; it may be different from your assumptions.

=== "For governance"

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

- A provider exposes its API one endpoint per tool; to answer one common question the agent makes dozens of small calls, hits rate limits, and stitches the pieces together wrong.
- The provider replaces those with a single operation shaped around the question users actually ask, and the same task now takes one call.
- Watching real usage, a provider finds users mostly want a comparison the API never offered directly, adds a task-level tool for it, and drops an assumption about what people wanted that turned out to be wrong.
- A spike of many tiny calls aimed at one goal flags an interface that is misaligned with how it is used, and prompts a redesign.
- For a very large API, instead of hand-building a task tool for every workflow, the provider lets the agent write code against the endpoints (progressive disclosure and code execution).

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
- [MIT Project NANDA, The GenAI Divide (2025)](../library/mit-genai-divide-2025.md).
  Enterprise field evidence that tools fail on workflow fit rather than model quality: custom systems stall due to "brittle workflows ... and misalignment with day-to-day operations", and buyers want a "deep understanding of our workflow" (pg. 3, pg. 15). Out-of-domain business report; cited as external context.

## Change history

- 2026-07-27: Added The GenAI Divide (MIT NANDA 2025) as a supporting source on workflow fit (bp6-a1).
- 2026-07-27: Renumbered from BP05 to BP06 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including an anti-pattern, replacing restatements of the practice.
- 2026-07-26: Rewritten to add vendor-primary grounding (the Anthropic tool-design guidance, with quantified evidence) and to note the two accepted remedies to endpoint-wrapping (task-level tools and code execution for very large APIs).
  "Providers don't know their users" kept as stated judgement.
- 2026-07-25: Created from the ELIXIR TF distillation (hooks 5, 12).
