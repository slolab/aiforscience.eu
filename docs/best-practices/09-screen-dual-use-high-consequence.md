---
title: Screen agents for dual-use and high-consequence risk
nav_title: "BP9 Dual-use screening"
practice_id: BP-09
status: draft
first_added: 2026-07-26
last_reviewed: 2026-07-26
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
  - title: "US Government Policy for Oversight of Dual Use Research of Concern (OSTP 2024)"
    ref: library/ref-usg-durc-2024.md
    locator: "codified DURC oversight (bio-scoped; under 2025 revision)"
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
  { #bp9-a1 }
- For potential dual-use agents, screening is not optional.
  { #bp9-a2 }
- Before an agent is given reach into the world, its capability for misuse should be evaluated against set thresholds.
  { #bp9-a3 }
- Any high-consequence action an agent can take should pass through a screening chokepoint, with dual-use requests refused.
  { #bp9-a4 }

</div>

=== "Practitioners"

    If your agent can act where a mistake or misuse could cause serious harm (ordering synthesis, running code against live systems, driving instruments), do not connect it to that capability without screening.
    Route high-consequence actions through providers or controls that screen them, and expect the agent to refuse dual-use requests.

=== "Providers"

    Evaluate an agent's misuse potential before granting real-world reach, and gate deployment on the result.
    Where an agent can trigger a high-consequence action, put a screening chokepoint in the path (for example a synthesis or service provider that screens orders), and build in dual-use refusal.
    Scale the safeguard to the capability, following the threshold-and-mitigation model the frontier safety frameworks share.

=== "Governance"

    Decide which agent capabilities require screening before deployment, and make it mandatory for those that could cause serious harm.
    This is cross-domain: the same capability-threshold structure covers biological, chemical, and cyber risk.
    Require evaluation of misuse potential, and keep the thresholds current as capability rises.

## Reasons

Most agent use is low-stakes.
A small part is not: an agent that can design a toxin, uplift a cyberattack, or command physical equipment can cause harm that no amount of provenance or [human-in-the-loop](../glossary.md#hitl) review undoes after the fact.
That is why this is a screening-and-containment practice, applied before action is granted.
The concern is cross-disciplinary; every major frontier safety framework, and the neutral syntheses of them, define the same structure (a capability threshold, an evaluation, and a proportionate mitigation) and apply it in parallel to chemical, biological, cyber, and autonomy risk.
The evidence that the risk is real spans domains too: an AI model repurposed for toxicity generated tens of thousands of candidate toxic molecules, including known warfare agents, in hours; AI-designed protein sequences have evaded the screening that guards DNA synthesis; and AI systems with cyber-offense capability have broken out of containment and committed large-scale attacks.

## Examples

- A capability/misuse evaluation run before an agent is given real-world reach, with deployment gated on the result and thresholds updated as capability rises.
- A screening chokepoint in the path of any high-consequence action, so the agent cannot trigger it unscreened.
- Dual-use refusal behaviour required of the agent, and tested.
- Concrete instances of the same pattern across fields:
    - Life sciences: routing sequence orders through synthesis providers that screen them, after work showed AI-designed sequences can evade that screening.
    - Chemistry: guarding against generation of toxic compounds or precursors, after a toxicity model was inverted to design chemical-warfare agents.
    - Cyber: evaluating and limiting an agent's offensive-cyber uplift before it can act against real systems.

!!! info "Practice metadata"
    **Status:** <span class="afs-badge afs-badge--draft">draft</span> ·
    **Endorsed by:** none yet ·
    **Last reviewed:** 2026-07-26

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
  The cyber instance.
- [US DURC oversight policy (OSTP 2024)](../library/ref-usg-durc-2024.md).
  A codified dual-use oversight instrument.
  Cited as a mature worked example; note it is scoped to the life sciences and under revision, so this practice is framed on the general concept, not on that instrument.

## Change history

- 2026-07-26: Created as a domain-neutral practice on screening agents for dual-use and high-consequence risk (the frontier-framework threshold-and- mitigation pattern), with life-science, chemistry, and cyber cases as labelled examples.
