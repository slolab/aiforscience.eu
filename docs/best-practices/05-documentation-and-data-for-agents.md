---
title: Write documentation and data for agents
nav_title: "BP05 Documentation"
practice_id: BP-05
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Best Practice, items 3 and 5"
  - title: "Agentic AI in the higher-education system (2026)"
    ref: library/hfd-agentic-ai-hochschulsystem-2026.md
    locator: "§3.3, hook 2"
  - title: "The FAIR Guiding Principles (Wilkinson et al. 2016)"
    ref: library/ref-fair-2016.md
    locator: "machine-actionability as the founding motivation"
  - title: "W3C Data Catalog Vocabulary (DCAT) version 3 (2024 Recommendation)"
    ref: library/ref-dcat3-2024.md
    locator: "machine-readable dataset metadata"
  - title: "Croissant: a metadata format for ML-ready datasets (MLCommons 2024)"
    ref: library/ref-croissant-2024.md
    locator: "schema.org-based dataset description"
  - title: "Datasheets for Datasets (Gebru et al. 2021)"
    ref: library/ref-datasheets-2021.md
    locator: "documented dataset provenance and intended use"
  - title: "Model Cards for Model Reporting (Mitchell et al. 2019)"
    ref: library/ref-model-cards-2019.md
    locator: "structured model documentation"
layer: Method
hitl: n/a
tags: [practitioner, provider, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- Documentation, data, and metadata are now an [interface](../glossary.md#interface).
  { #bp5-a1 }
- An [agent](../glossary.md#agent) operates a tool or dataset from its tool description / metadata, docstrings, and docs.
  { #bp5-a2 }
- User- and agent-facing documentation needs to be precise, current, and published in context with meaning and examples.
  { #bp5-a3 }
- Precise documentation helps human users and agents alike.
  { #bp5-a4 }

</div>

=== "Practitioners"

    Write your code and notebooks as if an agent will re-run them; assume that one will.
    Put units, data versions, and assumptions in the docstring or close to the code.
    When a resource's documentation misleads your agent, raise the issue with the provider.

=== "Providers"

    Treat docs, docstrings, tool descriptions, and metadata as an interface.
    Run examples and test them in CI so they cannot drift (e.g., using `doctest`).
    Publish data with schemas, controlled vocabularies, and machine-readable metadata, and give examples of how to query it.

=== "Governance"

    Machine-readable documentation is cheap to check and more important than ever.
    Include it in resource review, and fund documentation and data meaning as essential interface work.
    Reward it when assessing any resource.

## Reasons

Agents read documentation literally.
What a human works out from context can send an agent the wrong way, and an out-of-date example can lead to silent failure, if it results in a plausible but wrong result.
Data without stated meaning makes the agent guess at meaning and units.
The FAIR principles aim at making data findable, accessible, interoperable, and reusable; this now applies to agents.
A research agent that tracks a field is only as good as the metadata, citations, and retraction signals it can read.
This work also benefits the people who use the resource directly, and current and future maintainers of the resource.

## Examples

- A parameter is renamed but its docstring still shows the old name; a human reader infers the new one from context, while the agent calls it verbatim, the run fails, and a plausible but wrong number comes back.
- Examples in the documentation run as doctests in CI, so when the API changes a broken example fails the build and is fixed before it can mislead a human or an agent.
- A tool description gives only prose, with no parameter types, units, or valid ranges; the agent passes an out-of-range value and cannot interpret the error it gets back.
- A dataset is published with its meaning attached: a schema, controlled vocabularies, and machine-readable metadata including provenance and, where relevant, retraction status, so the agent does not have to guess at units or fields.
  General-purpose formats such as W3C DCAT, Croissant, datasheets, and model cards carry this; domain profiles such as Bioschemas (life sciences) are concrete instances of the same idea.
- A resource ships natural-language-to-query examples, for a query language such as SPARQL or Cypher, so an agent can turn a user's question into a correct query.
- The same documentation is offered in a form an agent can read directly (plain text, markdown, structured metadata), not only as a rendered web page.
  A convention like `llms.txt` is one proposed approach, not yet a ratified standard.

!!! info "Practice metadata"
    **Status:** <span class="afs-badge afs-badge--draft">draft</span> ·
    **Endorsed by:** none yet ·
    **Last reviewed:** 2026-07-26

## Sources

- [ELIXIR TF Agentic AI: agenda and rolling best practice (2026)](../library/elixir-tf-agentic-ai-2026.md), Best Practice items 3 and 5.
- [Agentic AI in the higher-education system (2026)](../library/hfd-agentic-ai-hochschulsystem-2026.md), §3.3 (research-agent source requirements).
  Consistent with, grounding only.
- [FAIR Guiding Principles (Wilkinson et al. 2016)](../library/ref-fair-2016.md).
  Machine-actionability as the founding motivation; agents make it concrete.
- [W3C DCAT v3 (2024)](../library/ref-dcat3-2024.md), [Croissant (MLCommons 2024)](../library/ref-croissant-2024.md), [Datasheets for Datasets (Gebru et al. 2021)](../library/ref-datasheets-2021.md), and [Model Cards (Mitchell et al. 2019)](../library/ref-model-cards-2019.md).
  Domain-neutral standards for machine-readable data and model documentation.

## Change history

- 2026-07-27: Renumbered from BP04 to BP05 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including anti-patterns; kept the labelled instances (DCAT, Croissant, datasheets, model cards, Bioschemas, llms.txt).
- 2026-07-26: Rewritten to be domain-neutral (FAIR, DCAT, Croissant, datasheets, and model cards as the general anchors; Bioschemas and SPARQL/Cypher demoted to labelled examples), to add tool descriptions alongside datasets, and to flag `llms.txt` as a proposed convention rather than a standard.
- 2026-07-25: Created from the ELIXIR TF distillation (hooks 4, 6), grounded in the HFD paper.
  Replaces the dummy BP0 on documentation and adds the data-and-examples dimension.
