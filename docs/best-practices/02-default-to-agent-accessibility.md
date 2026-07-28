---
title: Default to agent-accessibility; prioritise effort by demand and importance
nav_title: "BP02 Default to agent-accessibility"
practice_id: BP-02
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
  { #bp2-a1 }
- Often, programmatic use by agents cannot be distinguished from human users.
  { #bp2-a2 }
- Resources should be [machine-actionable](../glossary.md#machine-actionable) and discoverable by default.
  { #bp2-a3 }
- Access should be governed by resource.
  { #bp2-a4 }
- However, not every resource needs its own maintained agent [interface](../glossary.md#interface).
  { .afs-practice__pivot #bp2-a5 }
- How much effort to invest depends on how widely it is used and how important it is to the community.
  { #bp2-a6 }
- Sorting resources into types based on usage and importance can help prioritise maintenance effort.
  { #bp2-a7 }

</div>

=== "For practitioners"

    The resources you use will support agents to different degrees, by design.
    If one you depend on is poorly supported, say so.
    Providers use demand to decide what to improve.

=== "For providers"

    Make resources machine-actionable and discoverable by default, then set the level of support by type.
    Sort resources by how widely used and important they are, and invest accordingly.
    Keep a generic path for minor resources instead of building a custom interface for each.
    Govern access (authenticate and rate-shape where needed); a default of accessibility does not mean unmetered access.

=== "For governance"

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

- The maintainer of a heavily-used database ships a first-party MCP server covering the queries people actually run, and links it from the documentation.
  Traffic that used to arrive as thousands of small REST calls now comes through one path the provider designed, and answers improve because the agent is no longer reverse-engineering the API.
- With no first-party interface on offer, a scientist reaches a popular resource through a third-party MCP server they have not checked.
  It maps one field to the wrong column, the analysis runs on the wrong data, and the output looks plausible while being wrong.
  A vetted first-party path is what would have avoided the detour (checking a third-party tool before trusting it is [BP08](08-evaluate-tools-before-trust.md); vetting at connect time is [BP03](03-register-and-vet-interfaces.md)).
- A team spends weeks building and maintaining a bespoke agent interface for a niche tool that one group runs twice a year.
  The same effort spent on a top-tier resource would have served far more people; the work did not follow demand.
- A minor tool stays reachable through a shared registry's metadata instead of a bespoke interface, so an agent can still discover and call it.
  A registry such as bio.tools (life sciences) is one worked instance of this light generic path.
- A provider sorts its resources into tiers by how widely used and important they are, funds the top tier as maintained infrastructure, and leaves minor resources on the generic path.
  The ELIXIR Core Data Resources (life sciences) are one such tier, selected on quantitative and qualitative indicators.
- A resource keeps a default-open path but authenticates and rate-shapes automated traffic, so a burst of agent calls does not knock it over for its human users.
  Its logs cannot tell agents from people, which is why the limit is set at the resource rather than inferred from the client.

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

- 2026-07-27: Renumbered from BP01 to BP02 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including anti-patterns, replacing restatements of the practice; kept the labelled life-science instances (Core Data Resources, bio.tools).
- 2026-07-26: Rewritten to be domain-neutral (FAIR as the general anchor; ELIXIR and bio.tools demoted to labelled examples) and to replace "open to agents" with machine-actionable, discoverable, and governed-per-tier, grounded in FAIR and the COAR load survey.
- 2026-07-25: Created from the ELIXIR TF distillation (hooks 2, 3).
