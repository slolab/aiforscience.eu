---
title: Library
---

# Library

The library is the provenance store for the [best practices](../best-practices/01-match-method-to-task.md).
Everything used to model a practice, whether it supported, qualified, or
contradicted a claim, is recorded here so a reader can check it. It has two
tiers.

**Distilled sources** are rich documents (strategy papers, policy reports,
institutional documents) reduced into the passages that matter, with locators
and a mapping to the practices. **Reference works** are the standards, papers,
reports, and guidance cited as point support, each a short bibliographic record.

Raw documents are not hosted here. Each entry carries a full citation to the
original. The atom-level record of which source bears on which practice line, and
whether it is for or against, lives in the provenance data (`assets/provenance.yml`).

## Distilled sources

| Document | Issuing body | Date | Role in the record |
|---|---|---|---|
| [ELIXIR TF Agentic AI: agenda and rolling best practice](elixir-tf-agentic-ai-2026.md) | ELIXIR Europe, AI Ecosystem Focus Group | 2026 | Main source for the provider-facing practices (BP02, BP03, BP05, BP06, BP07, BP09); also seeds BP08 (evaluation). |
| [Agentic AI in the higher-education system](hfd-agentic-ai-hochschulsystem-2026.md) | Hochschulforum Digitalisierung / KI-Campus | May 2026 | Main source for the governance practice (BP04); grounds several others. |
| [EU Expert Forum on Frontier AI](ec-expert-forum-2026.md) | European Commission, European AI Office | July 2026 | Largely out of scope; grounds BP01, BP03, BP04, BP07 on method choice, evaluation, and provider choice. |
| [ELIXIR AI strategy](elixir-ai-strategy-2026.md) | ELIXIR Europe | June 2026 | Largely organisational; grounds BP05, BP07, BP08 on curated data, provenance, and validation. |
| [The GenAI Divide](mit-genai-divide-2025.md) | MIT Project NANDA | July 2025 | Out-of-domain enterprise report; grounds BP01, BP06, BP08 on task fit, workflow design, and outcome-based evaluation; qualifies BP03. |
| [Expectation–Realisation Gap for Agentic AI](expectation-realisation-gap-2026.md) | Lobentanzer (Helmholtz Munich) | February 2026 | Review of controlled trials on realised vs expected benefit; downweighted context (author is a contributor); grounds BP01 on heterogeneity and benefit planning, with optional context for BP06, BP08, BP09. |
| [EU AI Omnibus](ai-omnibus-2026.md) | European Union | July 2026 | Largely out-of-scope regulatory simplification of the AI Act; grounds BP04 and BP10 on technical safeguards against foreseeable misuse, with context for BP03, BP08. |
| [A safer framework for patient data in AI-for-Science grants](gagneur-rare-disease-patient-data-2026.md) | Gagneur (TU Munich) | July 2026 | Individual commentary on grant data terms; grounds BP04, BP02, BP09 on data-egress control, governed access, and effective oversight; flags a gap on controlled-access data in third-party training. |
| [F(AI)2R: Verifiable AI Provenance as an Executable Skill](fai2r-verifiable-ai-provenance-2026.md) | Florian Krebs | July 2026 | Self-demonstrated claim-level provenance method; grounds BP07 on traceable, auditable agent output and human/agent attribution. Single-session, self-audited case study; author has a declared stake in the method. |

## Reference works

The standards, papers, and reports cited by the practices, grouped by theme.
Each links to its bibliographic record.

**Method selection**

- [Building Effective AI Agents (Anthropic 2024)](ref-anthropic-building-effective-agents-2024.md)
- [AI Agents That Matter (Kapoor et al. 2024)](ref-kapoor-agents-that-matter-2024.md)
- [Fine-tuned small LLMs beat zero-shot frontier models (Bucher & Martini 2024)](ref-bucher-fine-tuned-2024.md)
- [Leakage and the reproducibility crisis in ML-based science (Kapoor & Narayanan 2023)](ref-kapoor-narayanan-leakage-2023.md)
- [Unmetered agent spend at Amazon (2026)](ref-amazon-ai-cost-overruns-2026.md)

**Data and metadata standards**

- [FAIR Guiding Principles (2016)](ref-fair-2016.md)
- [ELIXIR Core Data Resources (2020)](ref-elixir-cdr-2020.md)
- [bio.tools registry (2019)](ref-biotools-2019.md)
- [W3C DCAT version 3 (2024)](ref-dcat3-2024.md)
- [Croissant dataset metadata (2024)](ref-croissant-2024.md)
- [Datasheets for Datasets (2021)](ref-datasheets-2021.md)
- [Model Cards for Model Reporting (2019)](ref-model-cards-2019.md)

**Provenance, citation, and retraction**

- [W3C PROV-O (2013)](ref-prov-o-2013.md)
- [CRediT contributor roles taxonomy (2022)](ref-credit-2022.md)
- [ICMJE and COPE on AI and authorship (2023)](ref-icmje-cope-2023.md)
- [NISO CREC (RP-45-2024)](ref-niso-crec-2024.md)
- [Crossref and the Retraction Watch database (2023)](ref-crossref-retraction-watch-2023.md)
- [Fabricated citations from LLMs (Walters & Wilder 2023)](ref-walters-wilder-2023.md)
- [AI tools cite retracted papers (MIT Technology Review 2025)](ref-mit-tech-review-retracted-2025.md)

**Governance and risk frameworks**

- [NIST AI Risk Management Framework (2023, 2024)](ref-nist-ai-rmf.md)
- [EU AI Act (2024)](ref-eu-ai-act.md)
- [OECD AI Principles (2024)](ref-oecd-ai-principles-2024.md)
- [ISO/IEC 42001:2023](ref-iso-42001-2023.md)
- [OpenAI, Practices for Governing Agentic AI Systems (2023)](ref-openai-governing-agentic-ai-2023.md)
- [Chan et al., Visibility into AI Agents (2024)](ref-chan-visibility-2024.md)
- [Kolt, Governing AI Agents (2025)](ref-kolt-governing-agents-2025.md)
- [JRC, The Role of AI in Scientific Research (2025)](ref-jrc-ai-in-science-2025.md)
- [DeepMind, An Approach to Technical AGI Safety (2025)](ref-deepmind-agi-safety-2025.md)

**Interface security and channels**

- [OWASP Top 10 for LLM Applications 2025](ref-owasp-llm-top10-2025.md)
- [OWASP MCP Top 10](ref-owasp-mcp-top10.md)
- [Invariant Labs, MCP tool poisoning (2025)](ref-invariant-tool-poisoning-2025.md)
- [Self-propagating prompt injection in Copilot for Word (2026)](ref-copilot-word-ai-worm-2026.md)
- [Official MCP Registry (2025)](ref-mcp-registry-2025.md)
- [IETF AIPREF vocabulary (draft)](ref-ietf-aipref.md)
- [COAR survey on AI bots and crawlers (2025)](ref-coar-ai-bots-2025.md)
- [Web-scraping AI bots disrupt scientific databases (Nature news, 2025)](ref-nature-scraping-bots-2025.md)

**Agent-tool design**

- [Anthropic, Writing effective tools for agents (2025)](ref-anthropic-writing-tools-2025.md)
- [Anthropic, Code execution with MCP (2025)](ref-anthropic-code-execution-mcp-2025.md)
- [Anthropic, Advanced tool use (2025)](ref-anthropic-advanced-tool-use-2025.md)
- [Model Context Protocol specification](ref-mcp-spec.md)

**Human oversight**

- [Elish, Moral Crumple Zones (2019)](ref-elish-2019.md)
- [Green, Flaws of Policies Requiring Human Oversight (2022)](ref-green-2022.md)

**Evaluation**

- [REFORMS reporting standards (2024)](ref-reforms-2024.md)
- [NeurIPS Paper Checklist](ref-neurips-checklist.md)
- [DOME recommendations for ML validation in biology (2021)](ref-dome-2021.md)
- [Open and Sustainable AI in the life sciences (OSAI, 2025)](ref-osai-2025.md)

**Dual-use and frontier safety**

- [METR, Common Elements of Frontier AI Safety Policies (2025)](ref-metr-common-elements-2025.md)
- [Frontier Model Forum, Components of Frontier AI Safety Frameworks](ref-fmf-safety-frameworks.md)
- [Urbina et al., Dual use of AI-powered drug discovery (2022)](ref-urbina-dual-use-2022.md)
- [Wittmann et al., Nucleic-acid biosecurity screening (2025)](ref-wittmann-biosecurity-2025.md)
- [UK AI Security Institute, Frontier AI Trends (2025)](ref-aisi-frontier-trends-2025.md)
- [Autonomous agent breach of Hugging Face (2026)](ref-hf-openai-agent-breach-2026.md)
- [US policy for oversight of Dual Use Research of Concern (2024)](ref-usg-durc-2024.md)

**Research ethics and data protection**

- [WMA Declaration of Helsinki (2024)](ref-helsinki-2024.md)
- [EU General Data Protection Regulation (2016)](ref-gdpr-2016.md)
