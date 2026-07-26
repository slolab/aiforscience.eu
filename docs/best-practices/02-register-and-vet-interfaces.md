---
title: Register, vet, and manage agent interfaces through trusted channels
nav_title: "BP2 Trusted interfaces"
practice_id: BP-02
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
    ref: https://owasp.org/www-project-top-10-for-large-language-model-applications/
    locator: "LLM01; supply-chain risks"
  - title: "OWASP MCP Top 10 (MCP03 Tool Poisoning)"
    ref: https://owasp.org/www-project-mcp-top-10/
    locator: "MCP03:2025 Tool Poisoning"
  - title: "Invariant Labs: MCP tool poisoning attacks (2025)"
    ref: https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks
    locator: "poisoned tool descriptions; rug pull"
  - title: "Official Model Context Protocol Registry (preview, 2025)"
    ref: https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/
    locator: "listing of self-reported data; no security review"
  - title: "EU AI Act, Article 25 (responsibilities along the value chain)"
    ref: https://artificialintelligenceact.eu/article/25/
    locator: "substantial modification; deployer becomes provider"
  - title: "IETF AIPREF: a vocabulary for expressing AI usage preferences (draft)"
    ref: https://ietf-wg-aipref.github.io/drafts/draft-ietf-aipref-vocab.html
    locator: "machine-readable access preferences"
layer: Ecosystem
hitl: mandatory
tags: [provider, governance, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- An [agent](../glossary.md#agent) reaches tools, data, and actions outside the model through [interfaces](../glossary.md#interface) (e.g., MCP servers, skills, plugins).
- Each interface runs code and acts for the user, so each is a point where risk enters.
- Interfaces should be published through a channel that lists and vets them.
- Listing makes an interface discoverable and records where it comes from and who maintains it.
- Vetting is a separate step; a discoverable interface is not automatically safe.
  { .afs-practice__pivot }
- Public interfaces (e.g., public GitHub repositories) are generally vulnerable to prompt injection attacks.
- Safety and omnipotence are on a tradeoff; a system that can run arbitrary code (e.g., from web search) is vulnerable to injection – a system that cannot is less autonomous.

</div>

=== "Practitioners"

    Prefer interfaces that have been vetted, not just listed.
    Before trusting one with your data or actions, check who maintains it, when it was reviewed, and what it is allowed to do.
    Presence in a registry is not a safety check on its own: an unvetted interface can carry prompt-injection or malware risk you cannot see from its description.

=== "Providers"

    List your interfaces through a channel that records their source and maintainer, and have them vetted (reviewed or signed) before they are trusted.
    Route agent traffic through an approved, identified channel so you can shape and rate-limit it by identity, which beats blocking addresses that also blocks real users.
    If you adapt or repurpose someone else's interface, you may take on the duties of its provider.

=== "Governance"

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

- A channel that both lists an interface (source, maintainer, review date) and vets it (review or signing) before it is trusted, instead of open self-publication treated as if it were a safety check.
- A record of each interface's maintainer, review date, and permitted scope, visible to its users, with a signed provenance record where the channel supports it.
- An approved, identified channel for shaping and rate-limiting agent traffic by identity, instead of blocking addresses.
  Machine-readable access preferences (for example the emerging IETF AIPREF vocabulary) let a provider declare what automated clients may do.
- Attention to who is responsible: adapting, fine-tuning, or repurposing an interface can move responsibility to whoever changed it.
  Under the EU AI Act, a substantial modification can turn a deployer into a provider with the provider's duties, though the threshold is defined for high-risk systems and its exact bounds are still being clarified.
- More than one provider kept open, so a resource is not reachable only through one company's agent ecosystem.

!!! info "Practice metadata"
    **Status:** <span class="afs-badge afs-badge--draft">draft</span> ·
    **Endorsed by:** none yet ·
    **Last reviewed:** 2026-07-26

## Sources

- [ELIXIR TF Agentic AI: agenda and rolling best practice (2026)](../library/elixir-tf-agentic-ai-2026.md), Best Practice items 8 and 9 (registration implies review; managing agent traffic through an approved channel).
- [Agentic AI in the higher-education system (2026)](../library/hfd-agentic-ai-hochschulsystem-2026.md), §5.2 to 5.3 (deployer-versus-provider, infrastructure as a governance point).
- [EU Expert Forum on Frontier AI (2026)](../library/ec-expert-forum-2026.md), §4.2.2 (provider diversity and openness).
  Consistent with, grounding only.
- [OWASP Top 10 for LLM Applications 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and [OWASP MCP Top 10](https://owasp.org/www-project-mcp-top-10/).
  Prompt injection (LLM01) and tool poisoning (MCP03) as the documented risks vetting guards against.
- [Invariant Labs, tool poisoning attacks (2025)](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks).
  How a poisoned tool description hides instructions from the user.
- [Official MCP Registry (2025)](https://blog.modelcontextprotocol.io/posts/2025-09-08-mcp-registry-preview/).
  Evidence that the official registry lists self-reported data and does not vet, so listing and vetting must be kept distinct.
- [EU AI Act, Article 25](https://artificialintelligenceact.eu/article/25/).
  Substantial modification can move provider responsibility to whoever changed the system.
- [IETF AIPREF vocabulary (draft)](https://ietf-wg-aipref.github.io/drafts/draft-ietf-aipref-vocab.html).
  Emerging machine-readable way to declare access preferences to automated clients.

## Change history

- 2026-07-26: Rewritten to separate listing from vetting (the official MCP Registry lists but does not vet), merge agent-traffic management into this practice, reframe traffic control around identified traffic rather than IP blocking, qualify the Article 25 point, and add OWASP, MITRE-adjacent, and AIPREF grounding.
- 2026-07-25: Created from the ELIXIR TF distillation (hooks 9, 10), grounded in the HFD paper and the EU Expert Forum entry.
