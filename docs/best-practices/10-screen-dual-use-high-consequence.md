---
title: Screen agents for dual-use and high-consequence risk
nav_title: "Screen for dual-use and high-consequence risk"
practice_id: BP-10
status: draft
first_added: 2026-07-26
last_reviewed: 2026-07-28
endorsed_by: []
sources:
  - title: "METR, Common Elements of Frontier AI Safety Policies (2025)"
    ref: library/ref-metr-common-elements-2025.md
    locator: "shared capability-threshold structure across CBRN, cyber, autonomy"
  - title: "Frontier Model Forum, Components of Frontier AI Safety Frameworks"
    ref: library/ref-fmf-safety-frameworks.md
    locator: "CBRN, offensive cyber, automated AI R&D as high-consequence domains"
  - title: "Urbina et al., Dual use of AI-powered drug discovery (Nature Machine Intelligence 2022)"
    ref: library/ref-urbina-dual-use-2022.md
    locator: "40,000 toxic molecules incl. VX generated in under 6 hours"
  - title: "Wittmann et al., Strengthening nucleic acid biosecurity screening against generative protein design (Science 2025)"
    ref: library/ref-wittmann-biosecurity-2025.md
    locator: "AI-designed sequences evaded synthesis screening; patches restored detection"
  - title: "UK AI Security Institute, Frontier AI Trends (2025)"
    ref: library/ref-aisi-frontier-trends-2025.md
    locator: "cyber-offense capability rising toward expert level"
  - title: "Autonomous agent breach of Hugging Face (Hugging Face; OpenAI, 2026)"
    ref: library/ref-hf-openai-agent-breach-2026.md
    locator: "autonomous agent escaped its evaluation sandbox and breached production infrastructure"
  - title: "US Government Policy for Oversight of Dual Use Research of Concern (OSTP 2024)"
    ref: library/ref-usg-durc-2024.md
    locator: "codified DURC oversight (bio-scoped; under 2025 revision)"
  - title: "EU AI Omnibus (2026)"
    ref: library/ai-omnibus-2026.md
    locator: "Art 5(1a)(a)(ii); Recital 12 (provider safeguards against foreseeable prohibited output)"
  - title: "WMA Declaration of Helsinki (2024)"
    ref: library/ref-helsinki-2024.md
    locator: "voluntary participation; right to withdraw at any time"
  - title: "EU General Data Protection Regulation (2016)"
    ref: library/ref-gdpr-2016.md
    locator: "Art 7(3) withdraw consent; Art 17 right to erasure"
  - title: "A safer framework for patient data in AI-for-Science grants (2026)"
    ref: library/gagneur-rare-disease-patient-data-2026.md
    locator: "no perpetual licence; analysis is not training permission"
layer: Operational
hitl: mandatory
tags: [practitioner, provider, governance, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- Some [agents](../glossary.md#agent) carry [dual-use](../glossary.md#dual-use) risk: they can be used for good or bad.
  { #bp10-a1 }
- For potential dual-use agents, screening is not optional.
  { #bp10-a2 }
- Before an agent is given reach into the world, its capability for misuse should be evaluated against set thresholds.
  { #bp10-a3 }
- Any high-consequence action an agent can take should pass through a screening chokepoint, with dual-use requests refused.
  { #bp10-a4 }
- Because model training cannot be undone, data held under withdrawable consent can never be authorised for third-party model training or a perpetual licence, and an agent must be prevented from transmitting it for those uses.
  { #bp10-a5 }

</div>

=== "For practitioners"

    If your agent can act where a mistake or misuse could cause serious harm (ordering synthesis, running code against live systems, driving instruments), do not connect it to that capability without screening.
    Route high-consequence actions through providers or controls that screen them, and expect the agent to refuse dual-use requests.
    The same holds for data you cannot take back: never let an agent send data held under withdrawable consent to a service that will train on it or take a perpetual licence, and do not accept terms that authorise this.

=== "For providers"

    Evaluate an agent's misuse potential before granting real-world reach, and gate deployment on the result.
    Where an agent can trigger a high-consequence action, put a screening chokepoint in the path (for example a synthesis or service provider that screens orders), and build in dual-use refusal.
    Scale the safeguard to the capability, following the threshold-and-mitigation model the frontier safety frameworks share.
    Constrain and audit what an agent can send outward, exclude controlled-access data from third-party training and retention, and do not require a perpetual licence over data whose consent can be withdrawn.

=== "For governance"

    Decide which agent capabilities require screening before deployment, and make it mandatory for those that could cause serious harm.
    This is cross-domain: the same capability-threshold structure covers biological, chemical, and cyber risk.
    Require evaluation of misuse potential, and keep the thresholds current as capability rises.
    Treat irreversible data commitments as high-consequence too: do not accept grant or service terms that train third-party models on data held under withdrawable consent, and require enforced egress limits and audit where agents reach such data.

## Reasons

Most agent use is low-stakes.
A small part is not: an agent that can design a toxin, uplift a cyberattack, or command physical equipment can cause harm that no amount of provenance or [human-in-the-loop](../glossary.md#hitl) review undoes after the fact.
That is why this is a screening-and-containment practice, applied before action is granted.
The concern is cross-disciplinary; every major frontier safety framework, and the neutral syntheses of them, define the same structure (a capability threshold, an evaluation, and a proportionate mitigation) and apply it in parallel to chemical, biological, cyber, and autonomy risk.
The evidence that the risk is real spans domains too: an AI model repurposed for toxicity generated tens of thousands of candidate toxic molecules, including known warfare agents, in hours; AI-designed protein sequences have evaded the screening that guards DNA synthesis; and AI systems with cyber-offense capability have broken out of containment and committed large-scale attacks.

Some high-consequence actions are irreversible in a second sense: they cannot be walked back once taken.
Training a third-party model on data, or granting a perpetual licence over it, cannot be undone, and the data cannot be reliably removed from the model afterwards.
When the consent behind that data can be withdrawn, as it can be for human-subjects data under research ethics and data-protection law, no one can validly authorise a use that could not later honour a withdrawal.
The safeguard is the same as for any irreversible harm: prevent the action before it happens.
In agentic workflows this means constraining and auditing what an agent can send outward, because an agent that runs code and reads files can transmit such data without a deliberate upload.

## Examples

- An agent's misuse capability is evaluated against set thresholds before it is given real-world reach, deployment is gated on the result, and the thresholds are raised as capability rises.
- An agent is wired straight to an ordering or execution capability with no screen in the path, and a dual-use request goes through because nothing was positioned to catch it.
- The agent is required to refuse dual-use requests, and that refusal is tested rather than assumed.
- The same screen-before-acting pattern recurs across fields:
    - Life sciences: routing sequence orders through synthesis providers that screen them, after work showed AI-designed sequences can evade that screening.
    - Chemistry: guarding against generation of toxic compounds or precursors, after a toxicity model was inverted to design chemical-warfare agents.
    - Cyber: evaluating and limiting an agent's offensive-cyber uplift before it can act against real systems, after an autonomous system was shown to break out of containment.
- Human-subjects data: an agent working on consented patient or genomic data is blocked from sending it to a third-party service that would train on it or take a perpetual licence, and grant or service terms requiring such a licence are refused, because consent for that data can be withdrawn and training cannot be undone.

## Sources

- [METR, Common Elements of Frontier AI Safety Policies (2025)](../library/ref-metr-common-elements-2025.md) and [Frontier Model Forum, Components of Frontier AI Safety Frameworks](../library/ref-fmf-safety-frameworks.md).
  Independent syntheses showing the capability-threshold structure spans CBRN, cyber, and autonomy, which is the evidence this is a generic category.
- [Urbina et al., Dual use of AI-powered drug discovery (2022)](../library/ref-urbina-dual-use-2022.md).
  A toxicity model inverted to generate 40,000 toxic molecules, including VX, in under 6 hours.
  The sharpest non-life-science instance.
- [Wittmann et al., Science (2025)](../library/ref-wittmann-biosecurity-2025.md).
  AI-designed sequences evaded nucleic-acid synthesis screening; patches restored detection.
  The life-science instance.
- [UK AI Security Institute, Frontier AI Trends (2025)](../library/ref-aisi-frontier-trends-2025.md).
  Measured cyber-offense capability rising toward expert level.
  The cyber capability trend.
- [Autonomous agent breach of Hugging Face (2026)](../library/ref-hf-openai-agent-breach-2026.md).
  An autonomous system on OpenAI pre-release models escaped its evaluation sandbox and breached Hugging Face's production infrastructure.
  A realised cyber instance, disclosed by both organisations.
- [US DURC oversight policy (OSTP 2024)](../library/ref-usg-durc-2024.md).
  A codified dual-use oversight instrument.
  Cited as a mature worked example; note it is scoped to the life sciences and under revision, so this practice is framed on the general concept, not on that instrument.
- [EU AI Omnibus (2026)](../library/ai-omnibus-2026.md), Art 5(1a)(a)(ii).
  Obliges providers to build technical safeguards against reasonably foreseeable and reproducible prohibited output rather than rely on intent or policy, the same provider-safeguard logic as routing high-consequence actions through a screening chokepoint (bp10-a4).
- [WMA Declaration of Helsinki (2024)](../library/ref-helsinki-2024.md) and [EU GDPR (2016)](../library/ref-gdpr-2016.md).
  Research participants may withdraw at any time, and data subjects have a right to withdraw consent (Art 7(3)) and to erasure (Art 17); revocable consent cannot authorise a use that cannot be undone (bp10-a5).
- [A safer framework for patient data in AI-for-Science grants (2026)](../library/gagneur-rare-disease-patient-data-2026.md).
  Adjacent support: analysis permission is not training permission, and no perpetual licence should be taken over patient-level data.
  Individual commentary; it does not itself make the revocable-consent argument.

## Change history

- 2026-07-28: Added atom bp10-a5 (data under withdrawable consent cannot be authorised for irreversible third-party training or a perpetual licence, and an agent must be prevented from transmitting it for those uses), grounded in the Declaration of Helsinki and GDPR (right to withdraw; right to erasure), with the Gagneur commentary as adjacent support. Extended the tabs, Reasons, and Examples to match.
- 2026-07-27: Added the EU AI Omnibus (2026) as a supporting source on bp10-a4 (provider safeguards against foreseeable prohibited output; Art 5(1a)).
- 2026-07-27: Renumbered from BP09 to BP10 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including an anti-pattern (unscreened path); kept the labelled cross-field instances (life sciences, chemistry, cyber).
- 2026-07-26: Created as a domain-neutral practice on screening agents for dual-use and high-consequence risk (the frontier-framework threshold-and- mitigation pattern), with life-science, chemistry, and cyber cases as labelled examples.
