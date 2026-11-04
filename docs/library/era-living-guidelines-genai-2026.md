---
title: Living guidelines on the responsible use of generative AI in research (2026)
source_type: guideline
issuing_body: European Commission, Directorate-General for Research and Innovation, with the ERA Forum
published: 15 October 2026 (fourth version; first version 20 March 2024)
doi_or_url: https://research-and-innovation.ec.europa.eu/document/download/2b6cf7e5-36ac-41cb-aab5-0d32050143dc_en?filename=ec_rtd_ai-guidelines.pdf
distilled_on: 2026-11-04
status: draft
tags: [library, governance]
comments: true
---

# Living guidelines on the responsible use of generative AI in research (2026)

!!! info "Source"
    **Document:** "Living guidelines on the responsible use of generative AI in research. ERA Forum Stakeholders' document. Fourth version, October 2026".
    **Issuing body:** European Commission, Directorate-General for Research and Innovation (Unit E4, AI in Science and Critical Technologies), developed with the European Research Area Forum.
    **Date:** 15 October 2026 (fourth version; first published 20 March 2024; next revision foreseen in the third quarter of 2027).
    **Distilled:** 2026-11-04, replacing the distillation of the third version (May 2026) made on 2026-09-05.

## Summary

The guidelines are the European Commission's non-binding recommendations to researchers, research organisations, and research funders on using generative AI.
They rest on the European Code of Conduct for Research Integrity and on the High-Level Expert Group's trustworthy-AI requirements, and open with four principles: consider whether AI is the right tool, accountability stays with researchers and their institutions, confidentiality is non-negotiable, and use is disclosed.
The fourth version addresses AI agents directly for the first time: researchers set checkpoints for critical decisions, constrain an agent's use of sensitive data, and stay legally and scientifically accountable for what it does.
It also asks for disclosure of oversight and verification strategies, for retention of prompts, logs, and model versions where they are needed to audit the work, and warns funders about hidden prompts in submitted proposals.
For this record the weight sits in four places: accountability and checkpoints for agents, what data may reach which tool, disclosure and retention of AI use, and AI in peer review and proposal evaluation.

## Hooks, with citations

**1. Consider first whether AI is the right tool for the task.**
The document lists as its first principle: "Always consider whether AI is the right and best tool for a particular task" (§1, p. 4).
Researchers minimise environmental impact "by evaluating whether and which AI tool is best suited for the intended task" (§2, recommendation 5, p. 6).
Editors and reviewers "should first assess whether it is the most suitable and reliable means of performing the specific task, taking into account the nature of the material, the disciplinary context, the need for verifiable provenance, and whether the tool can be used within the applicable confidentiality and accountability guardrails" (§5, Use of AI in peer review, p. 13).
Relevance: method fit is now a headline principle of the guidelines ([BP01](../best-practices/01-match-method-to-task.md), bp1-a1), and the peer-review passage adds suitability and provenance as conditions of use ([BP08](../best-practices/08-evaluate-tools-before-trust.md), bp8-a2).
Audiences: practitioners, governance.

**2. Delegating to an agent does not delegate responsibility.**
The document: "AI systems are neither authors nor co-authors nor owners. Authorship implies agency and responsibility, so it lies with researchers" and "The use of AI agents may never be considered a delegation of control or responsibility" (§2, recommendation 1, p. 5).
"Researchers should be mindful that they are not exempted from their legal responsibilities because an agent acted on their behalf" (§2, recommendation 4, p. 6).
"AI agents must be deployed strictly as advanced research tools, not independent scientists", and "Researchers may inadvertently relinquish or lose control of their work by delegating too many research tasks into agents" (§5, Agentic AI, p. 12).
Relevance: a named human answers for each agent ([BP04](../best-practices/04-govern-autonomy-and-accountability.md), bp4-a5), and AI is not an author ([BP07](../best-practices/07-provenance-and-citation.md), bp7-a2).
Audiences: practitioners, governance.

**3. Set checkpoints where an agent makes critical decisions.**
The document: "When aiming to implement complex tasks autonomously, for example with AI agents, researchers identify and ensure relevant check points throughout the process to ensure that critical decisions (for example methodological) are validated by the researchers" (§2, recommendation 1, p. 5).
Footnote 29 distinguishes human-in-the-loop, human-on-the-loop, and human-in-command: "HITL involves human intervention in every decision cycle of the system, which in many cases is neither possible nor desirable. HOTL involves human intervention during the design cycle of the system and monitoring how the system operates" (§6, Trustworthy AI, p. 17).
Relevance: grounds stating where a person checks an agent workflow ([BP09](../best-practices/09-human-in-the-loop.md), bp9-a1) and the range of oversight levels (bp9-a2).
Audiences: practitioners, providers.

**4. Disclose what AI contributed and how it was checked; keep what an audit needs.**
The document: "Researchers disclose which AI tools or systems were used substantially in their research or reporting processes and describe what they contributed or were used for" and "describe meaningful information about oversight and verification strategies (such as measures to identify hallucinations, mitigate bias, etc.)" (§2, recommendation 2, p. 5).
On non-determinism: "Authors decide whether prompts, logs, model versions, parameters and other information should be retained or shared, based on whether these are needed to understand, reproduce or audit the research, or to assess its validity. This is particularly relevant when AI agents perform sequences of research tasks or contribute to methodological decisions" (§2, recommendation 2, p. 5).
The disclosure box: "In principle, AI use should be documented and reported like any other important research method or tool", and "In case of doubt, disclosure is advised" (§2, Disclosure of AI use, p. 8).
Relevance: human/agent attribution ([BP07](../best-practices/07-provenance-and-citation.md), bp7-a2), a retained run record that makes the work auditable (bp7-a1), and a record of the oversight applied ([BP09](../best-practices/09-human-in-the-loop.md), bp9-a6).
Audiences: practitioners, providers, governance.

**5. Anything uploaded may be used for training; protect unpublished or sensitive work.**
The document: "Researchers remain mindful that generated or uploaded input (text, data, prompts, images, etc.) could be used for other purposes, such as the training of AI models. Therefore, they protect unpublished or sensitive work (such as their own or others' unpublished work) by taking care not to upload it into an external AI system unless there are assurances that the data will not be re-used, e.g., to train future language models or to the untraceable and unverifiable reuse of data" (§2, recommendation 3, pp. 5-6).
Relevance: training on inputs is named as the default hazard of an external tool, and the researcher has to obtain assurances ([BP11](../best-practices/11-decide-where-research-data-may-go.md), bp11-a1; [BP10](../best-practices/10-screen-dual-use-high-consequence.md), bp10-a5).
Audiences: practitioners, governance.

**6. Third parties' personal data reaches an external tool only with a lawful basis and a clear purpose.**
The document: "Researchers take care not to provide third parties' personal data to external generative AI systems unless the data subject (individual) has given their consent and researchers have a clear goal for which the personal data are to be used so compliance with EU data protection rules is ensured" (§2, recommendation 3, p. 6).
Footnote 12 adds: "Apart from personal consent there could be other lawful basis that could justify the processing of personal data".
Relevance: sending personal data to an external model is a processing step that needs its own lawful basis and purpose ([BP11](../best-practices/11-decide-where-research-data-may-go.md), bp11-a3).
Audiences: practitioners, governance.

**7. Check who owns the tool, where it runs, and under which privacy options.**
The document: "They check, for example, their institutional guidelines, the privacy options of the tools, who is owning or managing the tool (public or private institutions, companies, etc.), where the tool is running and implications for any information uploaded. This could range from closed environments, hosting on a third-party infrastructure with guaranteed privacy, to open internet-accessible platforms" (§2, recommendation 3, p. 6).
Footnote 13: "This includes research-security elements (e.g. sensitive/dual-use research data being exposed to non-trusted foreign entities)".
Relevance: the operator, location, and terms of a tool decide what happens to uploaded data ([BP11](../best-practices/11-decide-where-research-data-may-go.md), bp11-a2 and bp11-a3).
Audiences: practitioners, governance, providers.

**8. An agent with access to sensitive data is instructed and constrained, and the researcher answers for it.**
The document: "If an AI agent is granted access to sensitive information following a suitability assessment, the researcher shall instruct and constrain potential confidentiality breaches and remain accountable for how the agent uses that sensitive information" (§2, recommendation 3, p. 6).
"Researchers are responsible for taking steps to ensure that AI agents do not breach any applicable legislation in their efforts to reach their goals" (§2, recommendation 4, p. 6).
Relevance: the guidelines' first statement on agents and sensitive data; it puts the limit on the researcher and allows instructions as a means ([BP11](../best-practices/11-decide-where-research-data-may-go.md), bp11-a5; [BP04](../best-practices/04-govern-autonomy-and-accountability.md), bp4-a5). See the tension below.
Audiences: practitioners, providers.

**9. Peer review and proposal evaluation stay human, and confidential material stays in secure tools.**
Evaluators, reviewers, and editors "Ensure that the judgement task is not delegated to an AI tool when assessing scientific quality and merit of proposals and papers", "do not disclose unpublished proposals, manuscripts, review reports or key ideas through non-secured AI tools, including through excerpts or prompts. Ensure the use of secure, trusted tools; preferably provided by the institution, funder or publisher", and "Verify factual claims, references and any substantive information used against original sources" (§2, recommendation 6, p. 7).
Footnote 17: "do not rely on public instances of AI systems and prefer bespoke solutions with clear data management and governance in place".
§5 adds: "unpublished materials should not be uploaded to AI systems that cannot guarantee high levels of confidentiality, data protection and non-use for training" (§5, Use of AI in peer review, p. 13).
For funders, "confidentiality and non-delegation of the evaluation of scientific merit must be present throughout the whole funding process" (§4, recommendation 2, p. 10).
Relevance: grounds the peer-review line in the [BP09](../best-practices/09-human-in-the-loop.md) governance tab, and routes confidential review material to governed tools ([BP11](../best-practices/11-decide-where-research-data-may-go.md), bp11-a3).
Audiences: practitioners, governance.

**10. Organisations host tools they govern, secure them, and keep track of use.**
Research organisations should, "Whenever possible and necessary, implement locally hosted or cloud-based generative AI tools that they govern themselves. This enables their employees to feed their scientific data into a tool that ensures data protection, confidentiality and research security" (§3, recommendation 4, p. 9).
Footnote 19 defines govern as "to establish and maintain the organisational rules, responsibilities and controls that ensure how it is developed, deployed and used safely", and allows "trustworthy third parties that meet EU data protection and research security requirements".
"Organisations ensure the appropriate level of cybersecurity of these systems, especially those connected to the internet" (§3, recommendation 4, p. 10).
Organisations also "Actively keep track of the evolution and use of generative AI systems within their organisations", and that knowledge can "be published and shared with the scientific community" (§3, recommendation 2, p. 9).
Relevance: the institution supplies a governed route for scientific data ([BP02](../best-practices/02-default-to-agent-accessibility.md), bp2-a4; [BP11](../best-practices/11-decide-where-research-data-may-go.md), bp11-a3) and keeps an inventory of use ([BP04](../best-practices/04-govern-autonomy-and-accountability.md) governance tab).
Audiences: governance, providers.

**11. Content received from third parties may carry hidden prompts.**
Funders, "When using generative AI as part of the internal processes, take into account the risks related to hidden prompts in content received from third parties, in particular in applications and proposals"; they "remain aware that content may contain hidden prompts or invisible instructions intended to influence generative AI tools" and "set clear rules prohibiting such manipulation and introduce appropriate safeguards, in particular in the IT systems involved in the processing of that information" (§4, recommendation 6, p. 11).
Footnote 22 defines a hidden prompt as "an instruction secretly embedded in a document or input for an AI system, without being visible to the human reader", done "through invisible text, formatting tricks, or metadata".
Funders also keep "safeguards against biased, discriminatory or erroneous outcomes, particularly in screening, ranking, prioritisation or exclusion" (§4, recommendation 2, p. 10).
Relevance: a Commission statement that documents submitted for assessment are an injection route ([BP03](../best-practices/03-register-and-vet-interfaces.md), bp3-a6 and the content-vetting lines in its tabs).
Audiences: governance, providers.

**12. Other people's AI tools are part of the exposure.**
The document: "Researchers and organisations remain mindful that third parties may use generative AI tools. For example, in the context of meetings, note-taking, summarising discussions or creating overviews of documents (that could be confidential)", and "In your contacts with third parties inform them if you are the one using those AI tools and how you are protecting collected information" (§2, Consider the use of generative AI by third parties, p. 8).
Relevance: confidentiality can be lost through a collaborator's or a reviewer's tool as well as through one's own ([BP11](../best-practices/11-decide-where-research-data-may-go.md) context).
Audiences: practitioners, governance.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | [BP01](../best-practices/01-match-method-to-task.md) (bp1-a1); [BP08](../best-practices/08-evaluate-tools-before-trust.md) (bp8-a2) | |
| 2 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a5); [BP07](../best-practices/07-provenance-and-citation.md) (bp7-a2) | |
| 3 | [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a1, bp9-a2) | |
| 4 | [BP07](../best-practices/07-provenance-and-citation.md) (bp7-a1, bp7-a2); [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a6) | |
| 5 | [BP11](../best-practices/11-decide-where-research-data-may-go.md) (bp11-a1); [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5) | |
| 6 | [BP11](../best-practices/11-decide-where-research-data-may-go.md) (bp11-a3) | |
| 7 | [BP11](../best-practices/11-decide-where-research-data-may-go.md) (bp11-a2, bp11-a3) | |
| 8 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a5) | [BP11](../best-practices/11-decide-where-research-data-may-go.md) (bp11-a5); [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1, bp4-a2) |
| 9 | [BP09](../best-practices/09-human-in-the-loop.md) governance tab; [BP11](../best-practices/11-decide-where-research-data-may-go.md) (bp11-a3) | |
| 10 | [BP02](../best-practices/02-default-to-agent-accessibility.md) (bp2-a4); [BP11](../best-practices/11-decide-where-research-data-may-go.md) (bp11-a3); [BP04](../best-practices/04-govern-autonomy-and-accountability.md) governance tab | |
| 11 | [BP03](../best-practices/03-register-and-vet-interfaces.md) (bp3-a6) | |
| 12 | context for [BP11](../best-practices/11-decide-where-research-data-may-go.md) | |

One tension.
Hook 8 tells the researcher to "instruct and constrain" an agent that has sensitive data.
BP11 (bp11-a5) and BP04 (bp4-a1, bp4-a2) hold that instructions alone do not limit an agent, and that the limit belongs in the agent's technical environment.
The guidelines' "constrain" is compatible with that; "instruct" as a sufficient means is not.
The record keeps its position and cites hook 8 as qualifying bp11-a5.

One difference in framing remains from the third version.
The guidelines put each check on the individual researcher.
The record moves the checks for agents into the institution's contracts and the agent's configured limits, because the researcher may never see what an agent sends.

## Proposed changes to practices

Proposals for editor review.
Citation upkeep was done in this change: the five practice pages that already cite this entry (BP01, BP02, BP07, BP10, BP11) have their locators moved to the fourth version's pages, and the existing provenance edges have their quotes and locators checked against the fourth version.

- [ ] Add this entry to the `sources:` of [BP09](../best-practices/09-human-in-the-loop.md): ref `library/era-living-guidelines-genai-2026.md`, locator "§2 recommendations 1 and 6, pp. 5, 7; §5 peer review, p. 13; footnote 29, p. 17", note "Researchers set checkpoints so an agent's critical decisions are validated by them; evaluators and reviewers do not delegate the judgement of scientific merit; footnote 29 separates human-in-the-loop, human-on-the-loop, and human-in-command, and says intervention in every decision cycle is often neither possible nor desirable (bp9-a1, bp9-a2). Non-binding." Provenance edges for bp9-a1, bp9-a2, and bp9-a6 are in place.
- [ ] Add this entry to the `sources:` of [BP04](../best-practices/04-govern-autonomy-and-accountability.md): ref as above, locator "§2 recommendations 1 and 4, pp. 5-6; §5 Agentic AI, p. 12", note "Using an agent is never a delegation of control or responsibility, and an agent acting for a researcher does not exempt them from legal responsibility (bp4-a5). Non-binding, and addressed to the researcher." Provenance edge for bp4-a5 is in place.
- [ ] Add this entry to the `sources:` of [BP03](../best-practices/03-register-and-vet-interfaces.md): ref as above, locator "§4 recommendation 6, p. 11; footnote 22", note "Recommendation 6 for funders warns that applications and proposals may carry hidden prompts aimed at AI tools used in evaluation, and asks for rules and safeguards in the IT systems that process them (bp3-a6). Non-binding." Provenance edge for bp3-a6 is in place.
- [ ] Optionally extend the BP07 source note to name retention: "Researchers disclose which tools were used and what they contributed, describe oversight and verification, and decide which prompts, logs, and model versions to retain based on what an audit needs (bp7-a1, bp7-a2). Non-binding." Provenance edge for bp7-a1 is in place.
- [ ] Optionally add a sentence to the [BP09](../best-practices/09-human-in-the-loop.md) governance tab, after the peer-review line: "The same holds for funders' evaluation of proposals."
- [ ] Optionally add an Example to [BP03](../best-practices/03-register-and-vet-interfaces.md): "A funder that screens proposals with an AI tool treats each submitted document as untrusted input: hidden text or metadata in a proposal can steer the tool's assessment, so the funder sets rules against such content and checks for it before the tool reads the file."
- [ ] Bring the BP11 source note in line with the fourth version: replace "written for tools a person uses, not agents" with "the fourth version adds that a researcher who gives an agent sensitive data instructs and constrains it; the record holds that instructions alone are insufficient (qualifies bp11-a5)". Provenance edge for bp11-a5 (qualifies) is in place.

No new practice is proposed; every agent-specific addition in the fourth version grounds or qualifies an existing atom.

## Cautions and gaps

The guidelines are non-binding recommendations, and say so.
The fourth version supersedes the third; quotes and page numbers here are from the October 2026 text and should carry the version when cited.
Retention of prompts, logs, and model versions is left to the authors' judgement ("Authors decide whether ..."); the guidelines do not require it.
The guidelines treat agents as tools a researcher operates; they do not discuss agents run by an institution or a service, where no single researcher is in a position to instruct or check them.
They name no provider, no jurisdiction, and no contract type; "assurances that the data will not be re-used" is left to the reader to obtain.
"Trustworthy third parties that meet EU data protection and research security requirements" (footnote 19) replaces the third version's "trusted countries"; research security and strategic autonomy (§6, p. 15) are policy context for this record, cited only where they bear on where data may go.
The open questions on disclosure (threshold, detail, format, per output type) are left to a global reporting standard under development for the World Conference on Research Integrity 2026 (§5, pp. 12-13); the record should check it when published.
The OECD definition of agentic AI cited in §5 (OECD AI Papers No. 56, 2026) was not reviewed for this entry.
The environmental-impact material is cited only for its method-fit sentence.
