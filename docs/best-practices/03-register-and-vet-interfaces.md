---
title: Register, vet, and manage agent interfaces through trusted channels
nav_title: "BP03 Register and vet interfaces"
practice_id: BP-03
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Best Practice, items 8 and 9"
  - title: "Agentic AI in the higher-education system (2026)"
    ref: library/hfd-agentic-ai-hochschulsystem-2026.md
    locator: "§5.2-5.3, hooks 8 and 9"
  - title: "EU Expert Forum on Frontier AI (2026)"
    ref: library/ec-expert-forum-2026.md
    locator: "§4.2.2, hook 2"
  - title: "OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection)"
    ref: library/ref-owasp-llm-top10-2025.md
    locator: "LLM01; supply-chain risks"
  - title: "OWASP MCP Top 10 (MCP03 Tool Poisoning)"
    ref: library/ref-owasp-mcp-top10.md
    locator: "MCP03:2025 Tool Poisoning"
  - title: "Invariant Labs: MCP tool poisoning attacks (2025)"
    ref: library/ref-invariant-tool-poisoning-2025.md
    locator: "poisoned tool descriptions; rug pull"
  - title: "Official Model Context Protocol Registry (preview, 2025)"
    ref: library/ref-mcp-registry-2025.md
    locator: "listing of self-reported data; no security review"
  - title: "EU AI Act, Article 25 (responsibilities along the value chain)"
    ref: library/ref-eu-ai-act.md
    locator: "substantial modification; deployer becomes provider"
  - title: "IETF AIPREF: a vocabulary for expressing AI usage preferences (draft)"
    ref: library/ref-ietf-aipref.md
    locator: "machine-readable access preferences"
  - title: "MIT Project NANDA, The GenAI Divide (2025)"
    ref: library/mit-genai-divide-2025.md
    locator: "§3.3 p.8 shadow AI outpaces governed deployment"
layer: Ecosystem
hitl: mandatory
tags: [provider, governance, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- An [agent](../glossary.md#agent) reaches tools, data, and actions outside the model through [interfaces](../glossary.md#interface) (e.g., [MCP](../glossary.md#mcp) servers, skills, plugins).
  { #bp3-a1 }
- Each interface runs code and acts for the user, so each is a point where risk enters.
  { #bp3-a2 }
- Interfaces should be published through a channel that lists and vets them.
  { #bp3-a3 }
- Listing makes an interface discoverable and records where it comes from and who maintains it.
  { #bp3-a4 }
- Vetting is a separate step; a discoverable interface is not automatically safe.
  { .afs-practice__pivot #bp3-a5 }
- Public interfaces (e.g., public GitHub repositories) are generally vulnerable to [prompt injection](../glossary.md#prompt-injection) attacks.
  { #bp3-a6 }
- Safety and omnipotence are on a tradeoff; a system that can run arbitrary code (e.g., from web search) is vulnerable to injection – a system that cannot is less autonomous.
  { #bp3-a7 }

</div>

=== "For practitioners"

    Prefer interfaces that have been vetted, not just listed.
    Before trusting one with your data or actions, check who maintains it, when it was reviewed, and what it is allowed to do.
    Presence in a registry is not a safety check on its own: an unvetted interface can carry prompt-injection or malware risk you cannot see from its description.

=== "For providers"

    List your interfaces through a channel that records their source and maintainer, and have them vetted (reviewed or signed) before they are trusted.
    Route agent traffic through an approved, identified channel so you can shape and rate-limit it by identity, which beats blocking addresses that also blocks real users.
    If you adapt or repurpose someone else's interface, you may take on the duties of its provider.

=== "For governance"

    Treat listing and vetting as two things: an inventory and a safety check.
    Back a trusted channel, require listed interfaces to record their source and review date, and make vetting (not mere registration) the point where risk is assessed.
    Keep more than one provider in use so the institution is not locked to a single vendor.

## Reasons

An agent interface runs code and acts for the user.
A malicious or careless one can carry malware or prompt-injection attacks hidden in a tool description, which the model reads but the user does not see.
Prompt injection is the top-ranked risk in the OWASP Top 10 for LLM Applications, and tool poisoning is a documented attack on agent interfaces specifically.
This is why listing and vetting are different acts.
A registry that only lists (like the official MCP Registry, which records self-reported data and runs no security review) makes interfaces discoverable but guarantees nothing about safety.
Vetting, a review or a signed provenance record, is what lets a user trust an interface.
The same approved channel also makes traffic manageable: identified agent traffic can be shaped and rate-limited per identity, whereas blocking addresses also blocks real users, and modern bots rotate addresses anyway.
Knowing where an interface comes from, and keeping more than one option open, avoids lock-in to a single provider.

## Examples

- A lab installs an MCP server because a public registry lists it and it has many stars, treating the listing as a safety check.
  The tool description carries instructions the model reads but the user never sees, and the agent leaks data on first use; nothing in the listing had vetted it.
- A provider publishes its interface through a channel that records source, maintainer, and review date and signs it, so a user can see it was reviewed before trusting it with their data or actions.
- An agent with web search and code execution reads a public repository issue that contains injected instructions and runs them; a colleague's agent, limited to a fixed set of read-only tools, is unaffected but can do less.
  The reach that makes an agent useful is the same reach that exposes it, so the safeguard has to match the capability.
- A resource routes agent calls through an approved, identified channel and rate-limits per identity, instead of blocking address ranges that also lock out real users.
  It declares what automated clients may do in machine-readable form; the emerging IETF AIPREF vocabulary is one instance.
- A group fine-tunes and repackages someone else's interface and ships it under their own name, without realising that under the EU AI Act a substantial modification can move the provider's duties onto them (the threshold is defined for high-risk systems and its exact bounds are still being clarified).
- An institution keeps more than one agent ecosystem in use, so a critical resource is not reachable only through a single vendor's channel.
- When the approved list is too narrow to do real work, people route around it: in one enterprise survey 40% of organisations bought an official tool while staff at over 90% used personal AI tools unofficially, often to better effect. A vetting process that watches what people actually reach for, and brings the useful cases into the trusted channel, holds up better than one that only blocks.

## Sources

- [ELIXIR TF Agentic AI: agenda and rolling best practice (2026)](../library/elixir-tf-agentic-ai-2026.md), Best Practice items 8 and 9 (registration implies review; managing agent traffic through an approved channel).
- [Agentic AI in the higher-education system (2026)](../library/hfd-agentic-ai-hochschulsystem-2026.md), §5.2 to 5.3 (deployer-versus-provider, infrastructure as a governance point).
- [EU Expert Forum on Frontier AI (2026)](../library/ec-expert-forum-2026.md), §4.2.2 (provider diversity and openness).
  Consistent with, grounding only.
- [OWASP Top 10 for LLM Applications 2025](../library/ref-owasp-llm-top10-2025.md) and [OWASP MCP Top 10](../library/ref-owasp-mcp-top10.md).
  Prompt injection (LLM01) and tool poisoning (MCP03) as the documented risks vetting guards against.
- [Invariant Labs, tool poisoning attacks (2025)](../library/ref-invariant-tool-poisoning-2025.md).
  How a poisoned tool description hides instructions from the user.
- [Official MCP Registry (2025)](../library/ref-mcp-registry-2025.md).
  Evidence that the official registry lists self-reported data and does not vet, so listing and vetting must be kept distinct.
- [EU AI Act, Article 25](../library/ref-eu-ai-act.md).
  Substantial modification can move provider responsibility to whoever changed the system.
- [IETF AIPREF vocabulary (draft)](../library/ref-ietf-aipref.md).
  Emerging machine-readable way to declare access preferences to automated clients.
- [MIT Project NANDA, The GenAI Divide (2025)](../library/mit-genai-divide-2025.md).
  Enterprise field evidence of a "shadow AI economy": unsanctioned personal-tool use outpaces governed deployment and often delivers better results (§3.3, pg. 8), so vetting should learn from observed usage rather than only restrict it. Out-of-domain business report; qualifies rather than grounds the practice.

## Change history

- 2026-07-27: Added a "what it looks like in practice" example on shadow usage and vetting that learns from observed use, grounded in The GenAI Divide (MIT NANDA 2025) as a qualifier (bp3-a3).
- 2026-07-27: Renumbered from BP02 to BP03 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including anti-patterns; kept the labelled instances (IETF AIPREF, EU AI Act Article 25) and cross-references.
- 2026-07-26: Rewritten to separate listing from vetting (the official MCP Registry lists but does not vet), merge agent-traffic management into this practice, reframe traffic control around identified traffic rather than IP blocking, qualify the Article 25 point, and add OWASP, MITRE-adjacent, and AIPREF grounding.
- 2026-07-25: Created from the ELIXIR TF distillation (hooks 9, 10), grounded in the HFD paper and the EU Expert Forum entry.
