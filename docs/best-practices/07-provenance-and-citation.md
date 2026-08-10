---
title: Make provenance and citation first-class
nav_title: "Make provenance and citation first-class"
practice_id: BP-07
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Best Practice, item 6"
    note: "Best Practice item 6."
  - title: "Agentic AI in the higher-education system (2026)"
    ref: library/hfd-agentic-ai-hochschulsystem-2026.md
    locator: "§3.3 and §4.1, hooks 2 and 4"
    note: "§3.3 (source traceability, retraction notices) and §4.1 (situated judgement is not automatable). Consistent with, grounding only."
  - title: "EU Expert Forum on Frontier AI (2026)"
    ref: library/ec-expert-forum-2026.md
    locator: "§4.2.3, hook 1"
    note: "§4.2.3 (evaluation and verification rest on traceability). Consistent with, grounding only."
  - title: "W3C PROV-O: the PROV Ontology (2013 Recommendation)"
    ref: library/ref-prov-o-2013.md
    locator: "machine-readable provenance"
    note: "Machine-readable provenance and contribution attribution."
  - title: "CRediT contributor roles taxonomy (ANSI/NISO Z39.104-2022)"
    ref: library/ref-credit-2022.md
    locator: "machine-readable contribution attribution"
    note: "Machine-readable provenance and contribution attribution."
  - title: "ICMJE Recommendations and COPE position on AI and authorship (2023)"
    ref: library/ref-icmje-cope-2023.md
    locator: "AI cannot be an author; disclosure required; humans accountable"
    note: "AI cannot be an author; use must be disclosed; humans remain accountable."
  - title: "NISO CREC: Communication of Retractions, Removals, and Expressions of Concern (RP-45-2024)"
    ref: library/ref-niso-crec-2024.md
    locator: "transmitting retraction status to machine and human readers"
    note: "The standard and the open data for propagating retraction status."
  - title: "Crossref and the Retraction Watch database (open since 2023)"
    ref: library/ref-crossref-retraction-watch-2023.md
    locator: "machine-readable retraction data"
    note: "The standard and the open data for propagating retraction status."
  - title: "Krebs, F(AI)2R: Verifiable AI Provenance as an Executable Skill (2026)"
    ref: library/fai2r-verifiable-ai-provenance-2026.md
    locator: "§IV claim-level records and the verification ladder; §VI citation audit and per-activity division of labour"
    note: "§IV (claim-level records, the verification ladder whose top rungs only a human may grant) and §VI (citation audit against the citing sentence, per-activity human and agent attribution). One working implementation, demonstrated on the paper's own production by its author: one operator, one domain, one session, self-audited. Downweighted, grounding only."
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
  { #bp7-a1 }
- It should be clear what was done by a human and what by an agent.
  { #bp7-a2 }

</div>

=== "For practitioners"

    Treat an agent answer with no source trail as unchecked.
    Keep the link between a result and its evidence, and mark what the agent produced and what you did, so the work can be checked and cited later.
    Disclose agent use where it matters (in a paper, a report, a review).
    You are still accountable for the judgement, whatever the agent found.

=== "For providers"

    Make provenance part of the output, not an add-on.
    Return sources with each answer, detailed enough to verify, pass through citation and retraction status, and mark agent-generated content.
    Record enough of each run (model version, inputs, tool calls) that it can be re-examined.
    Machine-readable provenance is what lets others evaluate and audit your system.

=== "For governance"

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

- An agent returns a confident literature summary with no sources; a reader cannot tell a sound claim from a fabricated one, and later finds that one cited paper does not exist.
- Each answer instead carries references detailed enough to check the specific claim, and cited work passes through retraction status, so a withdrawn study is flagged rather than presented as current.
  The NISO CREC recommended practice and the open Crossref/Retraction Watch data make this checkable.
- An agent-written passage is pasted into a manuscript with no marking; a co-author cannot tell which text and which analysis were the agent's, and authorship and error-tracing get muddled.
- Human and agent contributions are labelled, in outputs and in anything the agent writes to, agent use is disclosed where the work is published, and the trace is machine-readable (for example W3C PROV, RO-Crate, or CRediT) so it can be checked automatically.
- The run is recorded: model version, inputs, and tool calls kept so a surprising result can be re-examined and, where possible, re-run.
- The agent supplies the traceable evidence and the person makes the call, remaining accountable for the judgement.

<!-- BP_SOURCES -->
<!-- The Sources list above is generated from this page's frontmatter sources by hooks/bp_pages.py. Edit `sources:`, not here. -->

## Change history

- 2026-08-03: Added the F(AI)2R provenance paper (Krebs 2026) as a supporting source on claim-level provenance and per-activity human and agent attribution, downweighted as a single self-audited demonstration (bp7-a1, bp7-a2).
- 2026-07-27: Renumbered from BP06 to BP07 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including anti-patterns; kept the labelled instances (NISO CREC, Crossref/Retraction Watch, PROV, RO-Crate, CRediT).
- 2026-07-26: Rewritten to add standards grounding (PROV-O, CRediT, ICMJE/COPE, NISO CREC, Crossref/Retraction Watch), fold in run-level recording (reproducibility) and disclosure of agent use, and cite the fabricated-citation and cite-retracted-work evidence as support.
- 2026-07-25: Created from the ELIXIR TF distillation (hook 7), grounded in the HFD paper and the EU Expert Forum entry.
