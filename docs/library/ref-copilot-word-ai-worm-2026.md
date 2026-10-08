---
title: "Self-propagating prompt injection in Copilot for Word (2026)"
ref_id: copilot-word-ai-worm-2026
source_type: report
issuing_body: "Håkon Måløy (independent researcher)"
published: 2026
doi_or_url: https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/
added_on: 2026-08-04
grounds: [BP-03, BP-04, BP-07, BP-09]
tags: [library, reference]
comments: true
---

# Self-propagating prompt injection in Copilot for Word (2026)

!!! info "Reference"
    **Citation:** Måløy, H. "Context Collapse, Part 3: AI Worming through Word", En Klype Salt (28 July 2026, updated 30 July 2026). **Type:** coordinated vulnerability disclosure. **Link:** [enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/).

## What it is

A coordinated disclosure, run with the Microsoft Security Response Center over 144 days, showing that instructions hidden in an ordinary Word document can make Copilot alter the document it is drafting and copy the same instructions into the output, so the generated document becomes the next carrier.
The proof of concept halved every financial figure in a drafted report and appended the attack as white 8-point text; a later drafting session reproduced the attack from that generated document alone, with the original malicious file no longer attached.
Two vendor mitigations, one of them a model upgrade, closed the reported payloads but not the class, which still reproduced at publication.
Demonstrated in a commercial productivity suite, not observed in the wild and not in a scientific setting; the affected workflow, drafting a document from attached documents, is the one used for manuscripts, reviews, and reports.

## Role in the record

- Grounds [BP03](../best-practices/03-register-and-vet-interfaces.md): a document that reaches the model's context is part of the interface surface, and one shared through email or an internal SharePoint site carries the attack as well as one from outside, so where content comes from does not vet it; the injection can also be written back out into the agent's own output, which becomes the next carrier.
  The exposure follows from the agent having to read the content in order to judge it, so filtering moves it rather than removes it.
- Grounds [BP04](../best-practices/04-govern-autonomy-and-accountability.md): the model cannot be relied on to judge whether what it reads is safe, because that content is already shaping the judgement, and a second model placed in front of it inherits the same exposure; two vendor mitigations, one of them a model upgrade, closed the reported payloads but not the class.
- Grounds [BP07](../best-practices/07-provenance-and-citation.md): the author's own recommendation is that generated documents preserve provenance for source material and model-performed edits in metadata; approved Copilot edits left no visible trace, which is what made the manipulation untraceable afterwards.
- Grounds [BP09](../best-practices/09-human-in-the-loop.md): the only mitigation offered to customers is human review of the attached and the generated document, and the payload was invisible (white text, small font) while the edits it caused were too subtle to spot, so the check works only if it shows the reviewer what the model read and what the model changed.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
