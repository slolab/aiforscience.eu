---
title: "ELIXIR AI strategy (2026)"
source_type: strategy paper
issuing_body: ELIXIR Europe
published: June 2026 (version 1.0)
doi_or_url: Public strategy document, "ELIXIR AI strategy: Ten priorities for life sciences research", June 2026, V1.0
distilled_on: 2026-07-27
status: draft
tags: [library, agentic-ai]
comments: true
---

# ELIXIR AI strategy (2026)

!!! info "Source"
    **Document:** "ELIXIR AI strategy: Ten priorities for life sciences research". **Issuing body:** ELIXIR Europe (lead author Salvador Capella-Gutierrez; contributors from ELIXIR Nodes and the Hub). **Date:** June 2026, version 1.0. **Distilled:** 2026-07-27.

## Summary

The document is a high-level strategy in which ELIXIR sets ten priorities for supporting AI in European life sciences.
Its stated role is to enable and coordinate rather than to provide AI models or large-scale compute: federated data access, expert-curated datasets, and community standards.
Most of the text is organisational (aligning Nodes, coordinating the Hub, configuring EU AI Factories, securing funding) and sits outside the scope of this record.
The parts that bear on how science is done concern curated AI-ready data with references to primary sources, training and testing on independent data, evaluation and validation of AI models, and responsible-AI-by-design.
It grounds several existing practices and justifies no new one; ELIXIR-specific structures are read as examples.

## Hooks, with citations

**1. Ground truth in biology is ambiguous and revisable, so curated, expert-validated benchmarks are a long-term community endeavour.**
The document: "ground truth in biology is rarely unambiguous: the functional annotation of genes, the pathogenicity classification of variants, and the phenotypic characterisation of disease all require deep domain expertise and are subject to revision as scientific understanding advances. Constructing and maintaining the curated, expert-validated benchmarks that AI models require is therefore a long-term, community-wide endeavour, not a one-off data engineering task" (Introduction, p. 2).
Relevance: supports [BP7](../best-practices/07-evaluate-tools-before-trust.md); the reference against which a tool is judged is itself curated, contested, and moving.
Audiences: practitioners, providers, governance.

**2. Validating biological predictions requires experimental follow-up, and the feedback loop is far slower than automated benchmarking.**
The document: "validating biological predictions almost always requires experimental follow-up, creating feedback loops that are orders of magnitude slower than in domains where automated benchmarking is feasible" (Introduction, p. 2).
Relevance: qualifies the automated-evaluation assumption behind [BP7](../best-practices/07-evaluate-tools-before-trust.md); reinforces that human and experimental judgement stay in the loop ([BP8](../best-practices/08-human-in-the-loop.md)).
Audiences: practitioners, governance.

**3. Training and testing on independent data should be standard practice, with explicit awareness of data leakage.**
The document: "responsible management of sensitive data and awareness of data leakage to ensure the quality of AI models" (Introduction, p. 3); "ELIXIR will promote principles for ensuring that training and testing on independent data is adopted as a standard practice" (§6, p. 6).
Relevance: supports [BP7](../best-practices/07-evaluate-tools-before-trust.md); independence of test data is what keeps a benchmark score from being a misleading proxy.
Audiences: practitioners, providers.

**4. Curated, AI-ready datasets must carry clear references to their primary sources.**
The document: "These datasets require expert curation to accurately represent complex biological information and must include clear references to their primary sources to ensure transparency, build trust and guarantee provenance" (§5, p. 6).
Relevance: supports [BP4](../best-practices/04-documentation-and-data-for-agents.md) (data published with meaning) and [BP6](../best-practices/06-provenance-and-citation.md) (traceable to primary sources).
Audiences: providers, practitioners.

**5. A reference framework builds on DOME and OSAI to keep data, software, and AI models reusable in line with FAIR.**
The document: "Building on ELIXIR's leading role through the DOME recommendations and the Open and Sustainable AI (OSAI) guidelines, we will drive and maintain a reference framework to ensure that research data, software, and AI models are used and reused effectively in line with the FAIR principles" (§6, p. 6).
Relevance: supports [BP4](../best-practices/04-documentation-and-data-for-agents.md); [DOME](ref-dome-2021.md) is a reporting standard for supervised-ML validation that also bears on [BP7](../best-practices/07-evaluate-tools-before-trust.md), and [OSAI](ref-osai-2025.md) covers reproducibility and reusability of AI outputs.
Audiences: providers, practitioners, governance.

**6. External standards such as Model Context Protocol and agentic frameworks are to be adopted and adapted for the life sciences.**
The document: "it will also adopt and adapt whenever necessary external standards for the life sciences while serving as a proxy for emerging components such as Model Context Protocols and Agentic Frameworks" (§6, p. 6).
Relevance: supports [BP5](../best-practices/05-design-around-user-tasks.md); the interface substrate (MCP, agentic frameworks) is imported rather than reinvented.
Audiences: providers.

**7. A European platform for sharing and reusing AI models and datasets is identified as a missing component.**
The document: "the lack of a European, domain-specific platform for sharing and reusing AI models and datasets, akin to platforms such as Hugging Face" (§3, p. 5); it also names "the generation of multimodal synthetic data mimicking real data" as an unmet need.
Relevance: bears on [BP4](../best-practices/04-documentation-and-data-for-agents.md) and [BP6](../best-practices/06-provenance-and-citation.md); shared models and datasets need machine-readable documentation and a provenance trail to be reusable.
Audiences: providers, governance.

**8. Responsible AI is to be embedded by design, with guidelines that turn evaluation into actionable items.**
The document: "Embed by design responsible AI principles, including model explainability, interpretability, and the mitigation of algorithmic bias, across all stages of development and use ... This effort will include guidelines on how to perform AI Model evaluation so principles get translated into actionable items" and will "consider aspects beyond the AI models itself, including collection protocols and data handling practices" (§10, p. 8).
Relevance: supports [BP3](../best-practices/03-govern-autonomy-and-accountability.md) (responsible use built into the system) and [BP7](../best-practices/07-evaluate-tools-before-trust.md) (evaluation made concrete).
Audiences: providers, governance.

**9. The reproducible-research focus is to be extended to AI-related activities.**
The document: "ELIXIR will promote transparent methodologies and extend its current focus on reproducible research to include AI-related activities" (§10, p. 8).
Relevance: supports [BP6](../best-practices/06-provenance-and-citation.md) (recording a run so it can be re-examined) and [BP7](../best-practices/07-evaluate-tools-before-trust.md) (reproducible evaluation).
Audiences: practitioners, providers, governance.

**10. Contributions and underlying services must be properly credited, including where derived models overshadow the original resources.**
The document: "Recognition strategies will be embedded by design to ensure that experts' contributions are properly credited" (§4, p. 5); the uplifting of services should support "service sustainability and proper attribution in an environment where derived models often overshadow original services" (§8, p. 8).
Relevance: supports [BP6](../best-practices/06-provenance-and-citation.md); attribution reaches the data resources and human curation a model was built on, not only the model.
Audiences: providers, governance.

**11. Sensitive human data is to be analysed through federated, privacy-preserving methods on sovereign infrastructures.**
The document: "supporting the integration of both open and controlled-access data resources, including sensitive human data, through federated and privacy-preserving methods" (§5, p. 6); "prioritising the deployment of AI models on federated, sovereign European infrastructures" (§7, p. 7).
Relevance: bears on [BP1](../best-practices/01-default-to-agent-accessibility.md) (access governed by the resource) and on governance of how sensitive data is used for AI.
Audiences: providers, governance.

**12. Some AI applications fall under the EU AI Act high-risk category and need compliance expertise.**
The document: "some of these applications might fall under the high-risk category, as defined by the EU AI Act" (§4, p. 5); the responsible-AI priority commits to alignment "with emerging European and international regulatory frameworks, such as the European AI Act" (§10, p. 8).
Relevance: supports [BP3](../best-practices/03-govern-autonomy-and-accountability.md); the regulatory frame is already anchored in the record via the EU AI Act reference.
Audiences: governance.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1, 3 | [BP7](../best-practices/07-evaluate-tools-before-trust.md) | |
| 2 | [BP7](../best-practices/07-evaluate-tools-before-trust.md), [BP8](../best-practices/08-human-in-the-loop.md) | |
| 4 | [BP4](../best-practices/04-documentation-and-data-for-agents.md), [BP6](../best-practices/06-provenance-and-citation.md) | |
| 5 | [BP4](../best-practices/04-documentation-and-data-for-agents.md), [BP7](../best-practices/07-evaluate-tools-before-trust.md) | BP7 (see below) |
| 6 | [BP5](../best-practices/05-design-around-user-tasks.md) | |
| 7 | [BP4](../best-practices/04-documentation-and-data-for-agents.md), [BP6](../best-practices/06-provenance-and-citation.md) | |
| 8 | [BP3](../best-practices/03-govern-autonomy-and-accountability.md), [BP7](../best-practices/07-evaluate-tools-before-trust.md) | |
| 9 | [BP6](../best-practices/06-provenance-and-citation.md), [BP7](../best-practices/07-evaluate-tools-before-trust.md) | |
| 10 | [BP6](../best-practices/06-provenance-and-citation.md) | |
| 11 | [BP1](../best-practices/01-default-to-agent-accessibility.md) | |
| 12 | [BP3](../best-practices/03-govern-autonomy-and-accountability.md) | |

One nuance sits between hooks 5 and 8 and [BP7](../best-practices/07-evaluate-tools-before-trust.md).
The document places evaluation guidelines and a reference framework at the infrastructure level, promoted for adoption across the community.
BP7 holds that evaluation is the task of the adopter, who alone knows the task and carries the stakes.
These are complementary: shared reporting standards (DOME, REFORMS) make adopter-run evaluations comparable; they do not replace the adopter running one.

## Proposed changes to practices

- [ ] Ground [BP7](../best-practices/07-evaluate-tools-before-trust.md) with this strategy and with DOME. Add an Examples bullet: training and testing on independent data, with explicit checks against data leakage, so a benchmark score is not inflated by contamination. Note in Reasons that in biology the reference itself is curated and revisable and that validation often needs slow experimental follow-up.
- [ ] Add this strategy and DOME as sources on [BP7](../best-practices/07-evaluate-tools-before-trust.md); add this strategy as a source on [BP4](../best-practices/04-documentation-and-data-for-agents.md) and [BP6](../best-practices/06-provenance-and-citation.md).
- [ ] Ground [BP6](../best-practices/06-provenance-and-citation.md): add an Examples bullet that attribution reaches the data resources and human curation a model was derived from, not only the model, so derived work does not overshadow the source (hook 10).
- [ ] Ground [BP4](../best-practices/04-documentation-and-data-for-agents.md) with the DOME/OSAI/FAIR reference framework for reusable data, software, and models (hook 5), and [BP5](../best-practices/05-design-around-user-tasks.md) with MCP and agentic frameworks as external standards to adopt and adapt (hook 6).
- [ ] No new practice. All in-scope material merges into existing practices per the gating rule.

## Cautions and gaps

- The document is a high-level strategy. Most of it is organisational (Node alignment, Hub coordination, flagship-project funding, configuring EU AI Factories and Antennas, digital sovereignty, compute geopolitics) and is out of scope for this record; it is cited here only as context. It states intentions, not methods, so the hooks are directions of travel rather than tested practice.
- Explainability and interpretability are asserted as responsible-AI pillars (§10) without an actionable method. The record has no dedicated interpretability practice, and one strategy statement does not justify creating one. Treated as grounding for BP3, not a new practice.
- [DOME](ref-dome-2021.md) and [OSAI](ref-osai-2025.md) are both added as reference works. OSAI is a preprint (arXiv:2505.16619), community guidance rather than a ratified standard; treated as grounding, not as a settled requirement.
- The commitment to monitor and reduce the environmental impact of computational practices (Implementation roadmap, p. 9), and the Draghi Report framing behind it, touch energy and industrial policy and are out of scope; noted here only because "sustainability" is part of the OSAI framing.
- ELIXIR-specific structures (Nodes, Hub, Platforms, Communities, Core Data Resources, the PDB/AlphaFold example) are read as examples. The practices state the general form.
