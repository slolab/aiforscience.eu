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

!!! warning "License"
    This source is CC BY-NC-SA 4.0, while this record's content is CC-BY-4.0.
    Treated as citation-only: hooks below tightly paraphrase rather than quote at length, pending editor confirmation of reuse terms.

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
Relevance: a concrete mechanism for keeping final epistemic judgement with a human, relevant to [BP-07](../best-practices/07-provenance-and-citation.md) and to human-in-the-loop design ([BP-09](../best-practices/09-human-in-the-loop.md)).
Audiences: practitioners, providers, governance.

**4. Refusals and disagreement are recorded as audit activities, not discarded.**
The document: a refused promotion (for example, a source that could not be vendored or linked) is itself logged, distinguishing "checked and not convinced" from "never checked" (§IV, verification ladder).
Relevance: preserves negative and inconclusive review outcomes as part of the record, not only successful checks.
Audiences: practitioners, providers.

**5. Provenance binds to immutable artefacts and commits, with hashes on generated content.**
The document: activities bind to an existing commit, the graph describing a commit is itself committed separately from it, and generated artefacts and prompts carry hashes so "the graph never claims a hash it could not have known" (§IV, "Commit binding" and "Telemetry").
Relevance: a concrete technical pattern for making a provenance trail auditable after the fact, supporting the traceability atom of [BP-07](../best-practices/07-provenance-and-citation.md).
Audiences: providers.

**6. Prompts, transcripts, model identity, tools, and run telemetry are recorded together, with missing data marked missing rather than estimated.**
The document: activities record model and provider identity, session identifiers, tool calls, token classes, cost, energy, and sampling parameters where available; the case study's own execution harness initially exposed no usage data, and this gap was recorded rather than backfilled with an estimate (§IV, "Model" and "Telemetry"; §VI, Table II).
Relevance: matches this record's existing call to record enough of a run to re-examine it later; the honest-gap discipline is a specific, checkable practice.
Audiences: practitioners, providers.

**7. Citation metadata is registry-derived and verified before a source is cited.**
The document: reports resolving sources through DOI content negotiation and registries (Crossref, OpenAlex, arXiv, DataCite) and requires a ladder-backed source node before a citation is used (§IV, "Auditability operations"; §VI, "Worked examples").
Relevance: an implementable version of "pass citation status through to output" already named in [BP-07](../best-practices/07-provenance-and-citation.md).
Audiences: practitioners, providers.

**8. Load-bearing citations are content-checked against the citing sentence, not just existence-checked.**
The document: the paper's own citation audit fetched accessible full text, slides, or abstracts and compared them against the citing sentence, finding and repairing three citation overreaches before the sources were promoted (§VI, "Worked examples").
Relevance: a concrete, demonstrated instance of catching a citation-support failure before publication, the specific harm [BP-07](../best-practices/07-provenance-and-citation.md) and [BP-01](../best-practices/01-match-method-to-task.md) already cite evidence for.
Audiences: practitioners.

**9. Human and AI contributions are attributed at the level of the individual activity, not only in a blanket disclosure.**
The document: the graph distinguishes HumanAgent, AIAgent, and ToolAgent classes and counts authoring, audit, repair, build, and human-verification activities separately per agent (§IV, "Model"; §VI, Table III).
Relevance: a machine-readable, fine-grained instance of the human/agent separation named in [BP-07](../best-practices/07-provenance-and-citation.md); the paper itself notes this records who executed an activity better than who originated the underlying idea.
Audiences: practitioners, providers, governance.

**10. The build pipeline validates the graph and regenerates disclosure artefacts automatically.**
The document: continuous integration validates the provenance graph, renders a dashboard, regenerates the AI disclosure statement, builds the paper, and publishes artefacts with digests (§V, "CI as the deterministic build agent").
Relevance: shows provenance enforcement moved into the build process rather than left to manual discipline, relevant to providers building agent-facing infrastructure.
Audiences: providers.

**11. Incidents are recorded as ordinary, recoverable provenance events rather than removed from the history.**
The document: mishaps during the case study (a stale working directory that overwrote committed manuscript sections, a broken CI build from malformed registry metadata, a blocked publisher fetch) are recorded as activities in the graph rather than silently corrected (§VI, "Incidents as first-class records"; Figure 7).
Relevance: models the record's own failures-log practice at the level of a single research artefact.
Audiences: practitioners, providers.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 2 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 3 | [BP-07](../best-practices/07-provenance-and-citation.md), [BP-09](../best-practices/09-human-in-the-loop.md) | |
| 4 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 5 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 6 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 7 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 8 | [BP-07](../best-practices/07-provenance-and-citation.md), [BP-01](../best-practices/01-match-method-to-task.md) | |
| 9 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 10 | [BP-07](../best-practices/07-provenance-and-citation.md) | |
| 11 | [BP-07](../best-practices/07-provenance-and-citation.md) | |

No direct tension with an existing practice.
The paper is a mechanism proposal that instantiates what [BP-07](../best-practices/07-provenance-and-citation.md) already asks for; it does not argue against traceability, disclosure, or human sign-off.

## Proposed changes to practices

- [ ] Add this document as a supporting source on [BP-07](../best-practices/07-provenance-and-citation.md), qualified: the evidence is one self-generated, self-audited demonstration (one operator, one domain, one session), not an independently replicated study. No practice wording change proposed.
- [ ] Add provenance edges under `bp7-a1` (traceable, auditable agent answers) citing hooks 1, 2, 5, 6, 7, 8, 10, 11, stance `supports`, qualified by the self-report caveat.
- [ ] Add provenance edges under `bp7-a2` (clear human/agent attribution) citing hooks 3, 9, stance `supports`, qualified that activity attribution records execution better than it records the origin of an idea.
- [ ] Optional, not applied here: a supporting note on [BP-09](../best-practices/09-human-in-the-loop.md) that a verification ladder with an AI-side ceiling is one concrete mechanism for keeping final judgement with a human (hook 3).
- [ ] Optional, not applied here: a supporting note on [BP-08](../best-practices/08-evaluate-tools-before-trust.md) that separating machine-checkable existence from human-judged support is a reusable pattern for evaluating any agent-generated claim, not only citations (hook 2).

## Cautions and gaps

**Self-declared demonstration, not a study.** The author states this directly: one operator, one domain, one session, no independent replication. Every recorded claim in the case study reached only `ai-confirmed`; human verification of the paper's own sources was incomplete and selective, and 29 human-verified sources remained link-only audit targets rather than fully authenticated.

**Self-report weakness.** The provenance graph is produced and largely checked by the same agent and operator it describes; provider-side telemetry is not independently signed, and energy data is unavailable. The paper's own discussion section names this as an open problem and calls for independent-model or sampled-human re-verification, which had not been done at time of writing.

**Overhead is non-trivial.** The case study reports roughly 12.6% of requests, 11.8% of output tokens, and 9% of computed cost attributable to the provenance method itself, with 87 of 222 commits being bookkeeping-only.

**Portability is asserted, not demonstrated.** The method is designed to generalise across domains, operators, and models, but this paper tests it on nothing but its own writing.

**Author self-interest.** The author is a repeat contributor to this exact line of work (an earlier F(AI)2R paper and related prior work), is involved in an adjacent specification effort the paper proposes to integrate with, and five of the paper's own references are self-citations. No conventional conflict-of-interest statement appears in the source. This should weigh against treating the paper as independent evidence; it is evidence of one working implementation, offered by its own author.

**One internal inconsistency was noted during distillation**, not corrected here: the paper's own Table III appears to report a human-rung total that does not sum cleanly from its stated breakdown. Not treated as a hook; flagged for editor awareness only.

**License.** CC BY-NC-SA 4.0 versus this record's CC-BY-4.0. This entry avoids extended verbatim quotation and paraphrases hooks; an editor should confirm this treatment is acceptable, or seek clearance from the author, before this entry is merged.
