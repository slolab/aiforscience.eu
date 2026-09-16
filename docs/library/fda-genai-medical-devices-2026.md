---
title: FDA discussion paper on generative AI-enabled medical devices (2026)
source_type: policy report
issuing_body: US Food and Drug Administration, Center for Devices and Radiological Health (CDRH)
published: 2026-08-18
doi_or_url: https://www.fda.gov/medical-devices/digital-health-center-excellence/considerations-regulation-generative-ai-enabled-medical-devices-discussion-paper-and-request
distilled_on: 2026-09-15
status: draft
tags: [library, regulation, evaluation]
comments: true
---

# FDA discussion paper on generative AI-enabled medical devices (2026)

!!! info "Source"
    **Document:** "Considerations for the Regulation of Generative AI-Enabled Medical Devices: Discussion Paper and Request for Feedback".
    **Issuing body:** US Food and Drug Administration, Center for Devices and Radiological Health (CDRH).
    **Date:** 18 August 2026. Docket FDA-2026-N-7874, comments open until 19 October 2026.
    **Distilled:** 2026-09-15.
    Page numbers below are the printed page numbers in the document footer.

## Summary

The US Food and Drug Administration's Center for Devices and Radiological Health (CDRH) published this discussion paper on 18 August 2026 and asks for comments until 19 October 2026.
It is not guidance, it proposes no binding policy, and it poses 26 open questions.
It sets out a two-axis risk framework (how independently a system acts, against the consequence of relying on a wrong output), a competency-based premarket evaluation (task-scoped benchmarking of the deployed system, then confirmation in real or representative use), postmarket monitoring with re-benchmarking after changes, and a list of competencies specific to agentic systems.
Medical device regulation is outside the scope of this record, and the clinical content appears here only as a labelled instance.
The evaluation method transfers: the paper names the failure modes of generative and agentic systems, the weaknesses of public benchmarks, the independence required of a judge (including an LLM judge), and the conditions under which human oversight reduces risk, and on these points it grounds BP08, BP09, BP04, BP03, BP10, BP07, and BP01.

## Hooks, with citations

**1. Generative and agentic systems cannot be cleared by exhaustive testing.**
The document: "They may accept open-ended inputs, perform multiple subtasks, and produce variable outputs to similar inputs." (§II, p. 2).
It lists the risks this brings: "confabulations (or hallucinations) that may appear authentic to users, uncertainty in the bounds of a device’s intended use, limited visibility into underlying third-party foundation models, and performance degradation of the device and its components across test environments and in real-world applications across the TPLC" (§II, p. 2).
On the classical approach of testing a representative sample of inputs: "for GenAI-enabled devices, the range of possible inputs and outputs may be too large for such testing to be practical" (§V, p. 10).
Relevance: these are the properties that make task-specific evaluation and continued monitoring necessary ([BP08](../best-practices/08-evaluate-tools-before-trust.md)), and the failure modes a frontier model adds where a fixed method would do ([BP01](../best-practices/01-match-method-to-task.md)).
Audiences: practitioners, providers, governance.

**2. Risk is the product of how independently the system acts and what a wrong output costs.**
The document: "The framework places device activity on one axis and the “consequences,” or severity of harm of relying on an incorrect device output, on the other." (§IV, p. 5).
"A function that acts with continuous healthcare professional (HCP) supervision is meaningfully different from a function that acts in fully autonomous fashion." (§IV, p. 6).
A function that takes an action, such as issuing a prescription, "is typically higher risk than a GenAI-enabled informational function" (§IV, p. 7).
The paper asks whether further dimensions belong in the framework: "the reversibility of a resulting action, the availability of downstream safeguards, the time pressure of the deployment setting, or the traceability of the output (i.e., to primary source materials)" (§IV.A, question 1, p. 9).
Relevance: a scale for setting oversight in proportion to stakes, matching the autonomy spectrum in [BP09](../best-practices/09-human-in-the-loop.md) and the screening of high-consequence actions in [BP10](../best-practices/10-screen-dual-use-high-consequence.md); reversibility and traceability as risk modifiers connect to [BP10](../best-practices/10-screen-dual-use-high-consequence.md) and [BP07](../best-practices/07-provenance-and-citation.md).
Audiences: governance, providers.

**3. A disclaimer does not lower risk; an output the user cannot check raises it.**
The document: "a patient-facing informational function may not become any less directive because it includes a “talk to your doctor” or an “I am not a medical professional” statement in addition to the “action-directing” information" (§IV, p. 7).
On measurement outputs, the user typically cannot "independently evaluate the basis for the output (and therefore the function may migrate higher on the consequences axis)" (§IV, p. 8).
Communication quality includes "the risk of automation bias, in which a user accepts an output without appropriate scrutiny because of the device’s fluency or perceived authority" (Appendix A, E.4, p. 25).
Relevance: a human check reduces risk only when the human can judge the output ([BP09](../best-practices/09-human-in-the-loop.md), bp9-a5); traceability to sources is what makes an output checkable ([BP07](../best-practices/07-provenance-and-citation.md), bp7-a1).
Audiences: practitioners, providers, governance.

**4. Assess behaviour over whole interactions, because scope drifts one step at a time.**
The document: "A device may begin by performing an informational function and migrate, over the course of a conversation, to an action-directing function." (§IV, p. 8).
The proposed response is to "consider the device’s behavior across realistic conversational trajectories, not only at the level of individual functions" (§IV, p. 8).
Scope testing should include "multi-turn conversations in which individual turns appear in-scope but the cumulative interaction drifts out of scope" (Appendix A, S.2, p. 24).
Relevance: representative evaluation means whole workflows rather than single calls ([BP08](../best-practices/08-evaluate-tools-before-trust.md), bp8-a5), and autonomy limits have to bind cumulative action ([BP04](../best-practices/04-govern-autonomy-and-accountability.md), bp4-a3).
Audiences: practitioners, providers.

**5. Evaluate the deployed configuration, not the foundation model on its own.**
The document: "the final user-facing device, as configured and intended to be deployed for real-world use—and not the foundation model standing alone or other isolated subcomponent—would be evaluated" (§V.A, p. 11).
Benchmarking is organised into safety (recognition and escalation, scope maintenance, calibration and deferral), proficiency, generalizability (robustness and subgroup performance), and agentic capabilities, with elements "chosen based on applicability to the device’s intended use and risk profile" (§V.B.1, p. 12; Figure 2, p. 13).
Relevance: a model's leaderboard score is not evidence about the system built on it ([BP08](../best-practices/08-evaluate-tools-before-trust.md), bp8-a3), and the element list is a reusable checklist for what to test in an agentic system.
Audiences: practitioners, providers.

**6. Public benchmarks are contaminated and saturated; prespecify the test and keep the judge independent, also when the judge is an LLM.**
The document: "there may be challenges with publicly available benchmarking assets due to data contamination, saturation, and lack of representativeness of real-world conditions" (§V.B, p. 12).
"test methods and acceptance criteria would be prespecified prior to testing" (§V.B.2, p. 14).
Adjudicators would be "structurally independent from the device sponsor and, where the device incorporates a third-party model, from the developer of that model", and "These considerations would still be applicable when the expert adjudicator is itself an LLM." (§V.B.2, p. 14).
The paper asks what role sponsor-built benchmarks should play "given potential concerns around independence and optimization to the test" (question 10, p. 18), and how to stop synthetic test data "generated by models of the same class as the device under evaluation" from reproducing "the very performance gaps the evaluation is intended to detect" (question 13, p. 18).
Independent third parties could maintain "sequestered evaluation datasets and benchmarks that are developed independently from the device manufacturer" (§V.D.2, p. 17).
Relevance: supports [BP08](../best-practices/08-evaluate-tools-before-trust.md) on task-specific benchmarks with prespecified criteria (bp8-a1) and on the weakness of general proxies (bp8-a3); the independence condition on an LLM judge matches the self-verification entry in the [failures log](../best-practices/failures.md).
Audiences: practitioners, providers, governance.

**7. Benchmarking alone is not enough; confirm in real or representative use, in graded steps, and compare the human-AI team as it will run.**
The document: "device benchmarking, as described above and however thorough, may not fully establish how a GenAI-enabled device will perform in real clinical use" (§V.C, p. 14).
Confirmation methods are listed in "approximate order of increasing rigor and patient exposure": retrospective evaluation on real inputs, shadow deployment in which "outputs are not shown to clinicians or patients and do not affect care", standardized interactions, independent adjudication of real cases, and a prospective study (§V.C.1, p. 15).
For open-ended outputs "a single correct response often does not exist and many different responses may be acceptable", so the comparator may be a panel of qualified experts, and the choice includes "the combined performance of the clinician and device working together as a human-AI team versus the device working in a fully autonomous workflow" (§V.D.1, p. 16).
Relevance: staged trust on representative tasks is what [BP08](../best-practices/08-evaluate-tools-before-trust.md) asks of adopters (bp8-a5), and shadow deployment is a pattern any pipeline can use; evaluating the human-AI team as deployed is the design test [BP09](../best-practices/09-human-in-the-loop.md) sets for a stated check (bp9-a5).
Audiences: practitioners, providers.

**8. Safety behaviours are competencies to test: calibration, refusal in both directions, and stable safety-critical behaviour across runs.**
The document: "Presenting uncertain, outdated, or contested information with false confidence is treated as a safety failure." (Appendix A, S.3, p. 24).
"Both under-refusal (producing outputs beyond the device’s intended use, such as diagnosing or prescribing when not designed to do so) and over-refusal (declining requests that fall within the device’s intended use) are relevant failures." (Appendix A, S.2, p. 24).
"Variation in non-safety-critical phrasing may be acceptable, but variation in safety-critical behaviors such as escalation, refusal, or diagnostic conclusions is treated as a failure." (Appendix A, R.1, p. 25).
Robustness covers "reproducibility across repeated runs, consistency across semantically equivalent paraphrases" and "sensitivity to the order in which information is presented, behavior under missing or contradictory inputs, degradation across long conversations, and resistance to adversarial inputs targeting safety-critical behaviors" (Appendix A, R.1, p. 26).
Relevance: a concrete list of perturbations for recording how an agent fails ([BP08](../best-practices/08-evaluate-tools-before-trust.md), bp8-a5), including the repeated-run check the practice already names.
Audiences: practitioners, providers.

**9. Monitoring continues after deployment; any change, including a vendor's model update, triggers re-benchmarking against the original baseline.**
The document: "CDRH is considering whether it is appropriate to accept greater premarket uncertainty regarding a GenAI-enabled device’s benefit-risk profile through greater reliance on postmarket monitoring." (§VI, p. 19).
Monitoring approaches are periodic re-benchmarking "on a defined cadence and after defined triggering events, including changes to the underlying model or other components of the deployment architecture", sample-based review by independent adjudicators, and monitoring for "performance degradation (e.g., drift)" (§VI.A, p. 19-20).
Changes come in three kinds: discrete sponsor updates, model-evolution changes, and "unplanned changes arising from updates to an underlying third-party foundation model" (§VI.C, p. 20).
A device "benchmarked against a defined set of capabilities for premarket authorization could potentially be “re-benchmarked” against the same capabilities following a modification" (§VI.C, p. 21).
The paper asks whether "machine-based supervisory agents" can take on part of the monitoring, and what "the evaluation and reliability of the supervisory agent itself" requires (§VI.D, question 20, p. 21).
Relevance: evaluation is not a one-off ([BP08](../best-practices/08-evaluate-tools-before-trust.md)); the paper qualifies the benchmark-before-autonomy atom (bp8-a1) by treating some evidence as obtainable only in use; the monitoring rationale supports [BP04](../best-practices/04-govern-autonomy-and-accountability.md) on safeguards failing (bp4-a4); and a shared upstream model is a dependency whose silent update invalidates an adopter's earlier evaluation.
Audiences: providers, governance, practitioners.

**10. Third-party foundation models limit visibility, and a documentation channel does not move responsibility.**
The document: "Many are built on general-purpose foundation models developed by third-party entities, whose models offer varying levels of transparency into their training data, architecture, and evaluation methods, making it difficult to attribute specific behaviors and errors to the device or its underlying model." (§II, p. 2).
Voluntary Foundation Model Master Files could carry "structured model cards or system cards", including "characterized behaviors, known limitations, and failure modes relevant to healthcare contexts" and "safety-relevant behavioral constraints and guardrails built into the model; update notification commitments; and audit log availability" (§VII.A, p. 22, footnote 24).
Even so, "sponsors would remain responsible for independently demonstrating the safety and effectiveness of their own device built on a foundation model" (§VII.A, p. 22).
The paper notes that "model developers may have limited incentive to disclose safety-relevant information" (question 25, p. 23).
Relevance: a component's documentation is not vetting of the system built on it ([BP03](../best-practices/03-register-and-vet-interfaces.md), bp3-a5); the list of what a model file should carry (failure modes, guardrails, update notification, audit logs) is what an institution can ask a model vendor for under [BP04](../best-practices/04-govern-autonomy-and-accountability.md); see also [Model Cards](ref-model-cards-2019.md).
Audiences: providers, governance.

**11. Agentic systems need their own competencies: a safety envelope, oversight checkpoints before irreversible actions, tool-error recognition, and resistance to injection through tool outputs.**
The document defines the class: "Agentic AI systems are GenAI-enabled systems that autonomously plan and execute multi-step tasks, use external tools, or take actions across a sequence of steps." (§III, p. 4).
The agentic element tests whether a system "appropriately plans, sequences, and executes multi-step tasks while recognizing when a planned action sequence would exceed its intended use or safety envelope", and covers "accurate tool use and recognition of erroneous tool outputs, compliance with human-oversight checkpoints before irreversible or high-consequence actions, graceful handling of tool failures, and resistance to prompt injection through user inputs, retrieved content, and tool outputs" (Appendix A, A.1, p. 26).
The paper asks how "the elevated risk associated with autonomous multi-step action, tool use, and reduced opportunity for human review" should be reflected in acceptance criteria and oversight (§VII.C, question 26, p. 23).
Relevance: injection through retrieved content and tool outputs is the attack surface [BP03](../best-practices/03-register-and-vet-interfaces.md) names (bp3-a6); checkpoints before irreversible actions are limits enforced in the system ([BP04](../best-practices/04-govern-autonomy-and-accountability.md), bp4-a3), a stated oversight level ([BP09](../best-practices/09-human-in-the-loop.md), bp9-a1), and a chokepoint before high-consequence action ([BP10](../best-practices/10-screen-dual-use-high-consequence.md), bp10-a4).
Audiences: practitioners, providers, governance.

**12. Shared roles must not diffuse accountability.**
The document summarises Freyer et al.: "human clinicians face professional, legal, and reputational consequences when expected standards are not met", and "analogous mechanisms are needed for flawed GenAI-enabled devices" (§V, p. 10).
It lists clinicians, institutions, payers, professional societies, consortia, standards bodies, and public authorities, "each with potential roles to play in the deployment, monitoring, reporting, and ongoing evaluation of GenAI-enabled devices" (§VI.B, p. 20), and asks "how can these roles be structured without diffusing manufacturer accountability?" (§VI.D, question 21, p. 21).
Relevance: supports [BP04](../best-practices/04-govern-autonomy-and-accountability.md) on a named owner for each responsibility (bp4-a5).
Audiences: governance.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | [BP08](../best-practices/08-evaluate-tools-before-trust.md) (bp8-a3), [BP01](../best-practices/01-match-method-to-task.md) (bp1-a4) | |
| 2 | [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a2), [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a4); context for [BP07](../best-practices/07-provenance-and-citation.md) | |
| 3 | [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a5), [BP07](../best-practices/07-provenance-and-citation.md) (bp7-a1) | |
| 4 | [BP08](../best-practices/08-evaluate-tools-before-trust.md) (bp8-a5), [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a3) | |
| 5 | [BP08](../best-practices/08-evaluate-tools-before-trust.md) (bp8-a3) | |
| 6 | [BP08](../best-practices/08-evaluate-tools-before-trust.md) (bp8-a1, bp8-a3) | |
| 7 | [BP08](../best-practices/08-evaluate-tools-before-trust.md) (bp8-a5), [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a5) | |
| 8 | [BP08](../best-practices/08-evaluate-tools-before-trust.md) (bp8-a5) | |
| 9 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a3, bp4-a4) | qualifies [BP08](../best-practices/08-evaluate-tools-before-trust.md) bp8-a1 |
| 10 | [BP03](../best-practices/03-register-and-vet-interfaces.md) (bp3-a5); context for [BP04](../best-practices/04-govern-autonomy-and-accountability.md) | |
| 11 | [BP03](../best-practices/03-register-and-vet-interfaces.md) (bp3-a6), [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a3), [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a4); context for [BP09](../best-practices/09-human-in-the-loop.md) | |
| 12 | [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a5) | |

Hook 9 qualifies bp8-a1 ("Run task-specific benchmarks before giving an agent autonomy").
The paper considers granting market access on less premarket evidence in exchange for enforced monitoring with re-benchmarking triggers.
In the record's terms this is staged trust with a monitoring plan, as in the staged rollout example in [BP04](../best-practices/04-govern-autonomy-and-accountability.md); the evaluation before reliance stays, and part of it moves into the deployment period.

Who evaluates differs in emphasis.
[BP08](../best-practices/08-evaluate-tools-before-trust.md) places evaluation with the adopter; the paper places the burden on the sponsor (the provider), with independent third parties holding sequestered test data.
The two are complementary: the provider's published evidence (the BP08 providers tab) plus the adopter's own task check.

The paper draws on proposals to oversee generative AI the way clinicians are credentialed (structured assessment, supervised practice, periodic re-evaluation) and cites Freyer et al. on the accountability gap in that analogy.
The record takes no position on the analogy.

## Proposed changes to practices

Provenance edges were recorded in this session; practice pages were not edited.
Everything after the first item is for editor review.

- [x] Recorded 2026-09-15: provenance edges in `assets/provenance.yml`, stance `supports` on bp1-a4, bp3-a5, bp3-a6, bp4-a3, bp4-a4, bp4-a5, bp7-a1, bp8-a1, bp8-a3, bp8-a5, bp9-a2, bp9-a5, bp10-a4, and stance `qualifies` on bp8-a1 (hook 9).
- [ ] Add `fda-genai-medical-devices-2026` to the `sources:` of [BP08](../best-practices/08-evaluate-tools-before-trust.md) with the note: "Discussion paper, no legal force. Proposes task-scoped benchmarking of the deployed configuration with prespecified acceptance criteria and adjudicators independent of the sponsor and of the model developer, also when the adjudicator is an LLM; names contamination, saturation, and unrepresentativeness of public benchmarks; treats benchmarking as insufficient without confirmation in use (bp8-a1, bp8-a3, bp8-a5)."
- [ ] Add an Example to [BP08](../best-practices/08-evaluate-tools-before-trust.md), labelled as a regulated medical instance: "Regulated instance (medical devices): a 2026 FDA discussion paper proposes testing the system as deployed rather than the foundation model, against acceptance criteria fixed before testing, judged by adjudicators independent of the vendor and of the model developer, then confirming in shadow deployment where outputs are recorded but not acted on, and re-running the same benchmark after any change to the model, prompts, retrieval, or tools."
- [ ] Add an Example to [BP08](../best-practices/08-evaluate-tools-before-trust.md) on judge independence: "A team scores its agent's outputs with a second model from the same vendor and reports the agreement as validation; an adjudicator has to be independent of the system under test, and that condition holds when the adjudicator is a model."
- [ ] Add an Example to [BP08](../best-practices/08-evaluate-tools-before-trust.md) on re-evaluation triggers: "An agent's model, prompt, retrieval index, or tool set changes and the benchmark from three months earlier is still cited as its evidence; every such change re-runs the benchmark against the earlier result." If the editors judge re-evaluation after change to be load-bearing, it becomes a new atom (bp8-a6) instead of an example.
- [ ] Add the document to the `sources:` of [BP09](../best-practices/09-human-in-the-loop.md) (bp9-a2, bp9-a5), with two Examples. Labelled clinical: "Clinical instance: a patient-facing assistant appends 'talk to your doctor' to a dosing instruction; the regulator's view is that the disclaimer does not make the output less directive, so the oversight has to sit with a person who can judge the output." General: "The check is evaluated as it will run, person and agent together on real cases, not the agent alone."
- [ ] Add the document to the `sources:` of [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a3, bp4-a4, bp4-a5), with an Example: "A vendor updates the foundation model under a deployed agent without notice; the institution's evaluation from three months earlier no longer describes the system it is running. The contract now requires notice of model updates, and the agent inventory records the model version." Providers tab, one added sentence: "Ask model vendors for update notification and audit-log access, and record the model version in the agent inventory."
- [ ] Add the document to the `sources:` of [BP03](../best-practices/03-register-and-vet-interfaces.md) (bp3-a5, bp3-a6). No wording change; the three entry points for injection named in A.1 (user inputs, retrieved content, tool outputs) could enter the Reasons as what a vetting review tests.
- [ ] Add the document to the `sources:` of [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a4). No wording change; reversibility as a risk dimension (question 1) fits the existing Reasons paragraph on irreversible actions.
- [ ] Optional: add the document to the `sources:` of [BP07](../best-practices/07-provenance-and-citation.md) (bp7-a1) and [BP01](../best-practices/01-match-method-to-task.md) (bp1-a4). Both edges are modest; the paper is not about provenance or method choice.
- [ ] Candidate reference works, to add after reading: Garcia, Sidulova, and Badano, "Performance Assessment Strategies for Language Model Applications in Healthcare" (Artificial Intelligence in the Life Sciences, 2026, doi:10.1016/j.ailsci.2026.100162) for bp8-a3; Freyer et al., "Overcoming Regulatory Barriers to the Implementation of AI Agents in Healthcare" (Nature Medicine, 2025, doi:10.1038/s41591-025-03841-1) for bp4-a5; Patel and Blumenthal (JAMA Health Forum, 2026) and Bergman, Wachter, and Emanuel (JAMA, 2026) as context on competency-based oversight. None was created here, because none has been read.
- [ ] No new practice. "Evaluate the deployed system, not the model" and "re-evaluate after change" are sub-cases of BP08; "checkpoints before irreversible actions" is a sub-case of BP04 and BP10.

## Cautions and gaps

The paper is a request for comment from a US medical device regulator.
It is not guidance, has no legal force, and states that it does not address whether the approaches fall within FDA's existing authority (cover note, p. 1).
Positions may change after the comment period closes on 19 October 2026.
Medical device regulation is outside the scope of this record; the clinical elements (escalation, dosing, patient-facing versus clinician-facing functions) are domain material and belong only in labelled examples, never in a practice statement.
The paper proposes evaluation methods; it reports no evaluation results and no incidents, so it grounds how to evaluate and is not evidence that a given method works.
Its claims about benchmark contamination and saturation rest on a cited paper (Garcia, Sidulova, and Badano 2026) that has not been read for this entry.
The sponsor role maps imperfectly onto research: a group that builds its own agent is provider and adopter at once, so the paper's split between manufacturer evidence and independent confirmation collapses into one team, and the independence conditions in hook 6 become harder to meet.
The paper says nothing about provenance or citation beyond listing traceability as a candidate risk dimension; hooks 2 and 3 are modest support for BP07.
Framings to avoid: "the FDA requires" (it requires nothing here) and "the FDA endorses LLM judges" (it sets independence conditions on a possibility it puts up for comment).
The docket number and comment deadline come from the FDA's announcement page, not from the PDF.
Page numbers are the printed footer numbers, one less than the PDF page index.
