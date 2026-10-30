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
    note: "An ontology for stating provenance in machine-readable form: which entities, activities, and agents produced a result."
  - title: "CRediT contributor roles taxonomy (ANSI/NISO Z39.104-2022)"
    ref: library/ref-credit-2022.md
    locator: "machine-readable contribution attribution"
    note: "A contributor-role taxonomy that records attribution at the byline, so human and agent contributions can be separated."
  - title: "ICMJE Recommendations and COPE position on AI and authorship (2023)"
    ref: library/ref-icmje-cope-2023.md
    locator: "AI cannot be an author; disclosure required; humans accountable"
    note: "AI cannot be an author; use must be disclosed; humans remain accountable."
  - title: "NISO CREC: Communication of Retractions, Removals, and Expressions of Concern (RP-45-2024)"
    ref: library/ref-niso-crec-2024.md
    locator: "transmitting retraction status to machine and human readers"
    note: "The recommended practice for communicating retractions and expressions of concern as signals both systems and people can act on."
  - title: "Crossref and the Retraction Watch database (open since 2023)"
    ref: library/ref-crossref-retraction-watch-2023.md
    locator: "machine-readable retraction data"
    note: "The open, machine-readable retraction data that makes propagating retraction status feasible."
  - title: "Krebs, F(AI)2R: Verifiable AI Provenance as an Executable Skill (2026)"
    ref: library/fai2r-verifiable-ai-provenance-2026.md
    locator: "§IV claim-level records and the verification ladder; §VI citation audit and per-activity division of labour"
    note: "§IV (claim-level records, the verification ladder whose top rungs only a human may grant) and §VI (citation audit against the citing sentence, per-activity human and agent attribution). One working implementation, demonstrated on the paper's own production by its author: one operator, one domain, one session, self-audited. Downweighted, grounding only."
  - title: "Måløy, Self-propagating prompt injection in Copilot for Word (2026)"
    ref: library/ref-copilot-word-ai-worm-2026.md
    locator: "Implications; Impact"
    note: "Recommends that generated documents preserve provenance for source material and model-performed edits in metadata; in the proof of concept, approved assistant edits left no visible trace, which is what made the manipulation untraceable afterwards (bp7-a2). A proof of concept in a commercial productivity suite, not an incident observed in science; grounding only."
  - title: "Living guidelines on the responsible use of generative AI in research (European Commission and ERA Forum, 2026)"
    ref: library/era-living-guidelines-genai-2026.md
    locator: "Recommendations for researchers 1 and 2, pp. 7-8"
    note: "Researchers stay accountable for AI-assisted content, AI is not an author, and substantial use is noted in the methods section (bp7-a2). Non-binding."
  - title: "DFG Code of Conduct: Guidelines for Safeguarding Good Research Practice (2019)"
    ref: library/ref-dfg-code-of-conduct-2019.md
    locator: "Guideline 17, Archiving"
    note: "Guideline 17 asks for research data and central materials to be backed up and normally archived for ten years, which a provider's chat history does not guarantee (bp7-a1)."
  - title: "Two years of academic work lost from a ChatGPT account (Bucher, Nature 2026)"
    ref: library/ref-bucher-chatgpt-data-loss-2026.md
    locator: "subtitle and opening paragraph; OpenAI response as reported in press coverage"
    note: "A researcher lost the chats and project folders behind grant applications, teaching materials and publication drafts after a settings change; the provider said deleted chats cannot be recovered and advised personal backups (bp7-a1). A single first-person account; grounding only."
  - title: "University guidance on ChatGPT Edu content when a licence ends (2026)"
    ref: library/ref-chatgpt-edu-licence-end-2026.md
    locator: "Politecnico di Torino, Washington University in St. Louis, San José State University IT pages"
    note: "Three universities state that content is lost when a licence, an employment, or the institution's contract ends, and that a complete export is not available (bp7-a1). Institutional policy pages, not a documented loss."
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
    Keep the work that matters (drafts, analyses, decisions) in your own repository or institutional storage; a provider's chat history is not a record and can disappear.

=== "For providers"

    Make provenance part of the output, not an add-on.
    Return sources with each answer, detailed enough to verify, pass through citation and retraction status, and mark agent-generated content.
    Record enough of each run (model version, inputs, tool calls) that it can be re-examined.
    Machine-readable provenance is what lets others evaluate and audit your system.

=== "For governance"

    Provenance comes before audit and trust.
    Require that agent outputs be traceable, that human and agent contributions be clearly separated, and that agent use be disclosed where results are published.
    Use that trace as the basis for independent evaluation where the stakes are high.
    Research records have to outlive any one AI service: before cancelling or switching a licence, plan how users export their work, and do not let a provider's history be the only copy.

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
- An assistant's edits to a report are accepted with no record of which passages it changed or which attached file drove them.
  When the figures turn out to have been halved by hidden instructions ([prompt injection](../glossary.md#prompt-injection)) in one attachment, no one can tell the model's edits from the authors' or say which source introduced them.
  Provenance for source material and for model-performed edits, kept with the document, is what would make the change traceable; a reviewer without it has nothing to check against ([BP09](09-human-in-the-loop.md)).
- The run is recorded: model version, inputs, and tool calls kept so a surprising result can be re-examined and, where possible, re-run.
- The agent supplies the traceable evidence and the person makes the call, remaining accountable for the judgement.
- A researcher who used a chat assistant daily for two years changes one account setting, and the chats and project folders behind grant applications, teaching material and manuscript drafts are deleted; the provider cannot restore them.
  Drafts kept in the researcher's own files would have survived.
- An institution cancels its chat-assistant licences for some staff, and users find that projects and drafts existed only in the provider's history.
  Some universities state in advance that content is lost when the licence or the contract ends and that the institutional tier offers no complete export.
  Asking users to move their work to their own storage before the cutover, and keeping it there from the start, prevents the loss.

<!-- BP_SOURCES -->
<!-- The Sources list above is generated from this page's frontmatter sources by hooks/bp_pages.py. Edit `sources:`, not here. -->

## Change history

- 2026-10-30: Added keeping work outside the provider's chat history to the practitioner and governance tabs, with two Examples (a researcher's account deleted after a settings change; content lost when an institution's licence ends), grounded in the DFG Code of Conduct (Guideline 17), Bucher (Nature 2026), and university guidance on ChatGPT Edu (bp7-a1).
- 2026-10-08: Added the Commission's living guidelines on generative AI in research (2026) as a supporting source on bp7-a2 (AI is not an author; substantial use disclosed).
- 2026-09-16: Added the Copilot for Word disclosure (Måløy 2026) as a supporting source on bp7-a2, with an Example: assistant edits accepted without a record of what changed or which attachment drove them cannot be traced afterwards.
- 2026-08-03: Added the F(AI)2R provenance paper (Krebs 2026) as a supporting source on claim-level provenance and per-activity human and agent attribution, downweighted as a single self-audited demonstration (bp7-a1, bp7-a2).
- 2026-07-27: Renumbered from BP06 to BP07 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including anti-patterns; kept the labelled instances (NISO CREC, Crossref/Retraction Watch, PROV, RO-Crate, CRediT).
- 2026-07-26: Rewritten to add standards grounding (PROV-O, CRediT, ICMJE/COPE, NISO CREC, Crossref/Retraction Watch), fold in run-level recording (reproducibility) and disclosure of agent use, and cite the fabricated-citation and cite-retracted-work evidence as support.
- 2026-07-25: Created from the ELIXIR TF distillation (hook 7), grounded in the HFD paper and the EU Expert Forum entry.
