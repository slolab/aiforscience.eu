---
title: Default to agent-accessibility; prioritise effort by demand and importance
nav_title: "BP1 Accessibility"
practice_id: BP-01
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Best Practice, items 1 and 2"
  - title: "The FAIR Guiding Principles for scientific data management and stewardship (Wilkinson et al. 2016)"
    ref: library/ref-fair-2016.md
    locator: "machine-actionability; Accessible principle (auth permitted)"
  - title: "The ELIXIR Core Data Resources (Drysdale et al. 2020)"
    ref: library/ref-elixir-cdr-2020.md
    locator: "selection by demand and importance"
  - title: "The bio.tools registry of software tools and data resources (Ison et al. 2019)"
    ref: library/ref-biotools-2019.md
    locator: "registry model for the long tail"
  - title: "COAR survey: the impact of AI bots and crawlers on open repositories (2025)"
    ref: library/ref-coar-ai-bots-2025.md
    locator: "load and the blocking dilemma"
layer: Ecosystem
hitl: n/a
tags: [provider, governance, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- [Agents](../glossary.md#agent) use resources like humans do: databases, public endpoints, code, tools, and documents.
  { #bp1-a1 }
- Often, programmatic use by agents cannot be distinguished from human users.
  { #bp1-a2 }
- Resources should be machine-actionable and discoverable by default.
  { #bp1-a3 }
- Access should be governed by resource.
  { #bp1-a4 }
- However, not every resource needs its own maintained agent [interface](../glossary.md#interface).
  { .afs-practice__pivot #bp1-a5 }
- How much effort to invest depends on how widely it is used and how important it is to the community.
  { #bp1-a6 }
- Sorting resources into types based on usage and importance can help prioritise maintenance effort.
  { #bp1-a7 }

</div>

=== "Practitioners"

    The resources you use will support agents to different degrees, by design.
    If one you depend on is poorly supported, say so.
    Providers use demand to decide what to improve.

=== "Providers"

    Make resources machine-actionable and discoverable by default, then set the level of support by type.
    Sort resources by how widely used and important they are, and invest accordingly.
    Keep a generic path for minor resources instead of building a custom interface for each.
    Govern access (authenticate and rate-shape where needed); a default of accessibility does not mean unmetered access.

=== "Governance"

    Prioritisation is a funding decision.
    Back a scheme that ties interface investment to how used and important a resource is, and fund the top-tier interfaces as infrastructure.
    This keeps resources reachable by agents without an open-ended maintenance cost.

## Reasons

Agents already reach resources whether or not they were built for them.
Not planning for this does not stop it.
It means agents use interfaces no one designed, with more load and worse results.
Planning for it means agents can be steered to interfaces that work.
Machine-actionability is not a new demand: it is the founding goal of the FAIR principles, which agents now make concrete.
But a custom interface for every resource costs too much and is rarely worth it.
Widely used and important resources are worth a proper interface.
Minor resources can use a lighter, generic path.
Sorting resources into types makes these choices clear.
A default of accessibility is not a default of unlimited access.
The Accessible principle (the *A* of *FAIR*) always allowed authentication.
The load that automated clients now place on open resources makes governed access the realistic default.

## Examples

- A default that resources are machine-actionable and discoverable, with the level of support and the access controls set per resource.
- A list of resource types by how widely used and important they are (for example core resources, interoperability resources, archives, and minor tools), each tied to a level of investment.
  The ELIXIR Core Data Resources are one worked instance in the life sciences: a tier selected on quantitative and qualitative indicators and funded as infrastructure.
- A light generic path for minor resources, so they stay reachable without their own maintained interface.
  A registry such as bio.tools (life sciences) shows the pattern: many tools kept discoverable through shared metadata rather than a bespoke interface each.
- Demand (agent traffic, user requests) guiding which interfaces to improve next.
- Access governed per tier: default reachability paired with authentication and rate-shaping, so a resource is not knocked over by the traffic its openness invites.

!!! info "Practice metadata"
    **Status:** <span class="afs-badge afs-badge--draft">draft</span> ·
    **Endorsed by:** none yet ·
    **Last reviewed:** 2026-07-26

## Sources

- [ELIXIR TF Agentic AI: agenda and rolling best practice (2026)](../library/elixir-tf-agentic-ai-2026.md), Best Practice items 1 and 2.
  Provider stance and the resource typology.
- [FAIR Guiding Principles (Wilkinson et al. 2016)](../library/ref-fair-2016.md).
  Grounds machine-actionability as the general goal; the Accessible principle permits authentication, so "accessible" never meant "open without limit".
- [ELIXIR Core Data Resources (Drysdale et al. 2020)](../library/ref-elixir-cdr-2020.md).
  A concrete demand-and-importance typology with the top tier funded as infrastructure.
  Life-science instance, cited as an example.
- [bio.tools registry (Ison et al. 2019)](../library/ref-biotools-2019.md).
  The light generic path for the long tail.
  Life-science instance, cited as an example.
- [COAR survey on AI bots and crawlers (2025)](../library/ref-coar-ai-bots-2025.md).
  Evidence that open resources face heavy automated load and that blunt blocking also blocks real users.
  Qualifies "default accessible" toward governed access.

## Change history

- 2026-07-26: Rewritten to be domain-neutral (FAIR as the general anchor; ELIXIR and bio.tools demoted to labelled examples) and to replace "open to agents" with machine-actionable, discoverable, and governed-per-tier, grounded in FAIR and the COAR load survey.
- 2026-07-25: Created from the ELIXIR TF distillation (hooks 2, 3).
