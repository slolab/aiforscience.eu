---
title: "F(AI)2R: Verifiable AI Provenance as an Executable Skill (2026)"
source_type: preprint
issuing_body: "Florian Krebs"
published: 2026 (July)
doi_or_url: https://arxiv.org/abs/2607.25637
distilled_on: 2026-08-03
status: draft
tags: [library, provenance, evaluation]
comments: true
---

# F(AI)2R: Verifiable AI Provenance as an Executable Skill (2026)

!!! info "Source"
    **Document:** "F(AI)2R: Who Did What, and Who Checked? Verifiable AI Provenance as an Executable Skill".
    **Author:** Florian Krebs.
    **Date:** July 2026 (arXiv:2607.25637v1, cs.DL). **Distilled:** 2026-08-03.

## Summary

A methods paper that proposes `aiprov`, a claim-level provenance vocabulary for AI-assisted work, and packages it as an executable skill that an AI coding agent runs during its own work.
The method records a generating activity, an attributed agent, and a verification state for every claim, and enforces a verification ladder on which the highest rung an AI may itself grant is `ai-confirmed`; only a human agent can grant `human-confirmed` or `human-read`.
The paper's own writing process is used as a one-session case study: 206 recorded activities, a citation audit that repaired three overreaching citations, and several recorded incidents (a working-directory overwrite, a broken CI build, a blocked publisher fetch).
The author states plainly that this is a demonstration, not a study: one operator, one domain, one session, with no independent replication and self-generated, self-audited evidence throughout.
The author has a declared stake in the method's adoption (prior related work, self-citations, involvement in an adjacent specification effort).

## Hooks, with citations

**1. Provenance is recorded at claim level, not only at document level.**
The document: every claim requires a generating activity, an attributed agent, and a verification state; a claim with no recorded parent activity is treated as a hard validation failure (§IV, "Invariant I"; §V, Figure 3).
Relevance: operationalises traceability down to the individual assertion rather than the whole output, directly on point for [BP-07](../best-practices/07-provenance-and-citation.md).
Audiences: practitioners, providers.

**2. Reference existence is separated from evidential support.**
The document: distinguishes a reference that is machine-checkable to exist from a reference whose content actually supports the claim, which requires judgement (§II, "Background and Related Work"; §IV, Table I).
Relevance: names a specific failure mode this record already documents (fabricated or non-supporting citations), and proposes a structural fix rather than a caution alone.
Audiences: practitioners, providers.

**3. The highest verification rung an AI may grant itself is bounded; only a human can grant the top rungs.**
The document: the verification ladder caps AI-granted status at `ai-confirmed`; `human-confirmed` and `human-read` are human-only, and an AI attempt to grant them is a validator failure (§IV, verification ladder and Table I; §V, Figure 3).
A refused promotion changes no state and is logged as an audit activity carrying the refused rung, so "checked and not convinced" stays distinguishable from "never checked" (§IV, verification ladder).
Relevance: a concrete mechanism for keeping final epistemic judgement with a human, and for keeping negative review outcomes in the record, relevant to [BP-07](../best-practices/07-provenance-and-citation.md) and to human-in-the-loop design ([BP-09](../best-practices/09-human-in-the-loop.md)).
Audiences: practitioners, providers, governance.

**4. Load-bearing citations are content-checked against the citing sentence, not just existence-checked.**
The document: the paper's own citation audit fetched accessible full text, slides, or abstracts and compared them against the citing sentence, finding and repairing three citation overreaches before the sources were promoted (§VI, "Worked examples").
Relevance: a concrete, demonstrated instance of catching a citation-support failure before publication, the specific harm [BP-07](../best-practices/07-provenance-and-citation.md) and [BP-01](../best-practices/01-match-method-to-task.md) already cite evidence for.
Audiences: practitioners.

**5. Human and AI contributions are attributed at the level of the individual activity, not only in a blanket disclosure.**
The document: the graph distinguishes HumanAgent, AIAgent, and ToolAgent classes and counts authoring, audit, repair, build, and human-verification activities separately per agent (§IV, "Model"; §VI, Table III).
Relevance: a machine-readable, fine-grained instance of the human/agent separation named in [BP-07](../best-practices/07-provenance-and-citation.md); the paper itself notes this records who executed an activity better than who originated the underlying idea.
Audiences: practitioners, providers, governance.

**6. The discipline is enforced by the build, not by memory.**
The document: an activity binds a commit that already exists and the graph entry describing it is committed separately, so "the graph never claims a hash it could not have known", and generated artefacts and prompts carry content hashes (§IV, "Commit binding" and "Telemetry").
Citation metadata comes from DOI content negotiation and registry sweeps (Crossref, OpenAlex, arXiv, DataCite) rather than from memory, and no reference is used without a ladder-backed source node (§IV, "Auditability operations"; §VI, "Worked examples").
Telemetry records model and provider identity, session, tools, token classes, and cost, with absent data recorded as absent instead of estimated (§IV, "Telemetry"; §VI, Table II).
Continuous integration validates the graph, regenerates the disclosure statement, and blocks the build on a violation; mishaps, including an overwrite of committed manuscript sections, a build broken by malformed registry metadata, and a publisher refusing automated fetches, are logged as ordinary activities (§V, "CI as the deterministic build agent"; §VI, "Incidents as first-class records").
Relevance: the implementation pattern behind hooks 1 to 5, for providers building agent-facing infrastructure; the trail holds because the pipeline refuses work that breaks it, rather than because an operator remembers to log.
Audiences: providers.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 2 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 3 | [BP-07](../best-practices/07-provenance-and-citation.md), [BP-09](../best-practices/09-human-in-the-loop.md) | |
| 4 | [BP-07](../best-practices/07-provenance-and-citation.md), [BP-01](../best-practices/01-match-method-to-task.md) | |
| 5 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 6 | [BP-07](../best-practices/07-provenance-and-citation.md) | |

No direct tension with an existing practice.
The paper is a mechanism proposal that instantiates what [BP-07](../best-practices/07-provenance-and-citation.md) already asks for; it does not argue against traceability, disclosure, or human sign-off.

## Proposed changes to practices

- [ ] Add this document as a supporting source on [BP-07](../best-practices/07-provenance-and-citation.md), qualified: the evidence is one self-generated, self-audited demonstration (one operator, one domain, one session), not an independently replicated study. No practice wording change proposed.
- [ ] Add provenance edges under `bp7-a1` (traceable, auditable agent answers) citing hooks 1, 2, 4, 6, stance `supports`, qualified by the self-report caveat.
- [ ] Add provenance edges under `bp7-a2` (clear human/agent attribution) citing hooks 3, 5, stance `supports`, qualified that activity attribution records execution better than it records the origin of an idea.
- [ ] Optional, not applied here: a supporting note on [BP-09](../best-practices/09-human-in-the-loop.md) that a verification ladder with an AI-side ceiling is one concrete mechanism for keeping final judgement with a human (hook 3).
- [ ] Optional, not applied here: a supporting note on [BP-08](../best-practices/08-evaluate-tools-before-trust.md) that separating machine-checkable existence from human-judged support is a reusable pattern for evaluating any agent-generated claim, not only citations (hook 2).

## Cautions and gaps

**The evidence is one self-audited demonstration.** The author states the scope directly: one operator, one domain, one session, no independent replication.
All eight recorded claims stopped at `ai-confirmed`, granted by the agent that had written the citing sentences, and the paper names measuring that self-confirmation bias as the next audit the method owes itself.
The operator reports having checked all sources and claims, and formalised part of those checks as human grants: 29 of the human-verified sources rest on link-only audit targets, which stay mutable, and 13 of the 34 human grants are checkable only against the committed transcript.
Provider telemetry is relayed by the agent rather than signed at source, and energy is unrecorded because no provider reported it.
The method is designed to carry across domains, operators, and models, and this paper tests it on its own writing only.

**Overhead is non-trivial.** The case study reports roughly 12.6% of requests, 11.8% of output tokens, and 9% of computed cost attributable to the provenance method itself, with 87 of 222 commits being bookkeeping-only.

**Author self-interest.** The author is a repeat contributor to this exact line of work (an earlier F(AI)2R paper and related prior work), is involved in an adjacent specification effort the paper proposes to integrate with, and five of the paper's own references are self-citations. No conventional conflict-of-interest statement appears in the source. This should weigh against treating the paper as independent evidence; it is evidence of one working implementation, offered by its own author.
