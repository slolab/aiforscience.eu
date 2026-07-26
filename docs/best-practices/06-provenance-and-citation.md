---
title: Make provenance and citation first-class
nav_title: "BP6 Provenance and citation"
practice_id: BP-06
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Best Practice, item 6"
  - title: "Agentic AI in the higher-education system (2026)"
    ref: library/hfd-agentic-ai-hochschulsystem-2026.md
    locator: "§3.3 and §4.1, hooks 2 and 4"
  - title: "EU Expert Forum on Frontier AI (2026)"
    ref: library/ec-expert-forum-2026.md
    locator: "§4.2.3, hook 1"
  - title: "W3C PROV-O: the PROV Ontology (2013 Recommendation)"
    ref: library/ref-prov-o-2013.md
    locator: "machine-readable provenance"
  - title: "CRediT contributor roles taxonomy (ANSI/NISO Z39.104-2022)"
    ref: library/ref-credit-2022.md
    locator: "machine-readable contribution attribution"
  - title: "ICMJE Recommendations and COPE position on AI and authorship (2023)"
    ref: library/ref-icmje-cope-2023.md
    locator: "AI cannot be an author; disclosure required; humans accountable"
  - title: "NISO CREC: Communication of Retractions, Removals, and Expressions of Concern (RP-45-2024)"
    ref: library/ref-niso-crec-2024.md
    locator: "transmitting retraction status to machine and human readers"
  - title: "Crossref and the Retraction Watch database (open since 2023)"
    ref: library/ref-crossref-retraction-watch-2023.md
    locator: "machine-readable retraction data"
layer: Method
hitl: optional
tags: [practitioner, provider, governance, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- Any answer an [agent](../glossary.md#agent) gives should be traceable to its sources and open to audit.
  { #bp6-a1 }
- It should be clear what was done by a human and what by an agent.
  { #bp6-a2 }

</div>

=== "Practitioners"

    Treat an agent answer with no source trail as unchecked.
    Keep the link between a result and its evidence, and mark what the agent produced and what you did, so the work can be checked and cited later.
    Disclose agent use where it matters (in a paper, a report, a review).
    You are still accountable for the judgement, whatever the agent found.

=== "Providers"

    Make provenance part of the output, not an add-on.
    Return sources with each answer, detailed enough to verify, pass through citation and retraction status, and mark agent-generated content.
    Record enough of each run (model version, inputs, tool calls) that it can be re-examined.
    Machine-readable provenance is what lets others evaluate and audit your system.

=== "Governance"

    Provenance comes before audit and trust.
    Require that agent outputs be traceable, that human and agent contributions be clearly separated, and that agent use be disclosed where results are published.
    Use that trace as the basis for independent evaluation where the stakes are high.

## Reasons

Science depends on the path back to evidence: results are trusted because they can be checked.
Without a path back to the sources, a claim cannot be checked, cited, or corrected, and a wrong answer that looks right cannot be told apart from a correct one.
This is not hypothetical: studies find large fractions of LLM-produced citations are fabricated or wrong, and AI research tools have been shown to cite retracted papers without flagging them.
It also matters to separate what a human did from what the agent produced, for authorship, accountability, and tracing errors.
There is wide editorial consensus (ICMJE, COPE) that AI cannot be an author and that its use must be disclosed.
A research agent has to pass citation and retraction status through to its output, or it will present withdrawn work as current.

## Examples

- Every answer carries references to its sources, detailed enough to check the specific claim.
- Retraction and version status travel with cited sources, so the agent does not present withdrawn or outdated work as current.
  The NISO CREC recommended practice and the open Crossref/Retraction Watch data make this checkable.
- Human and agent contributions are labelled, in outputs and in anything the agent writes to, and agent use is disclosed where the work is published.
- The trace is machine-readable (for example W3C PROV, RO-Crate, or CRediT for contributions), so it can be checked automatically, not only read.
- The run is recorded: model version, inputs, and tool calls kept so a result can be re-examined and, where possible, re-run.
- Judgement stays with the human: the agent supplies the traceable evidence, the person decides.

!!! info "Practice metadata"
    **Status:** <span class="afs-badge afs-badge--draft">draft</span> ·
    **Endorsed by:** none yet ·
    **Last reviewed:** 2026-07-26

## Sources

- [ELIXIR TF Agentic AI: agenda and rolling best practice (2026)](../library/elixir-tf-agentic-ai-2026.md), Best Practice item 6.
- [Agentic AI in the higher-education system (2026)](../library/hfd-agentic-ai-hochschulsystem-2026.md), §3.3 (source traceability, retraction notices) and §4.1 (situated judgement is not automatable).
  Consistent with, grounding only.
- [EU Expert Forum on Frontier AI (2026)](../library/ec-expert-forum-2026.md), §4.2.3 (evaluation and verification rest on traceability).
  Consistent with, grounding only.
- [W3C PROV-O (2013)](../library/ref-prov-o-2013.md) and [CRediT (ANSI/NISO Z39.104-2022)](../library/ref-credit-2022.md).
  Machine-readable provenance and contribution attribution.
- [ICMJE / COPE on AI and authorship (2023)](../library/ref-icmje-cope-2023.md).
  AI cannot be an author; use must be disclosed; humans remain accountable.
- [NISO CREC RP-45-2024](../library/ref-niso-crec-2024.md) and [Crossref / Retraction Watch](../library/ref-crossref-retraction-watch-2023.md).
  The standard and the open data for propagating retraction status.

## Change history

- 2026-07-26: Rewritten to add standards grounding (PROV-O, CRediT, ICMJE/COPE, NISO CREC, Crossref/Retraction Watch), fold in run-level recording (reproducibility) and disclosure of agent use, and cite the fabricated-citation and cite-retracted-work evidence as support.
- 2026-07-25: Created from the ELIXIR TF distillation (hook 7), grounded in the HFD paper and the EU Expert Forum entry.
