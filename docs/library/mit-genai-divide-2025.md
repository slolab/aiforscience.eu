---
title: The GenAI Divide (2025)
source_type: report
issuing_body: MIT Project NANDA (Challapally, Pease, Raskar, Chari)
published: 2025 (July)
doi_or_url: https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf
distilled_on: 2026-07-27
status: draft
tags: [library, adoption]
comments: true
---

# The GenAI Divide (2025)

!!! info "Source"
    **Document:** "The GenAI Divide: State of AI in Business 2025".
    **Issuing body:** MIT Project NANDA (Aditya Challapally, Chris Pease, Ramesh Raskar, Pradyumna Chari).
    **Date:** July 2025. **Distilled:** 2026-07-27.

## Summary

An enterprise-adoption report from MIT's Project NANDA, based on 300+ public AI initiatives, 52 organisation interviews, and 153 senior-leader surveys collected January to June 2025.
Its headline finding is that despite $30 to 40 billion in enterprise GenAI investment, 95% of organisations see no measurable return, a gap the authors call the "GenAI Divide".
The report locates the cause not in model quality, regulation, or talent but in a "learning gap": most deployed systems do not retain feedback, adapt to context, or improve over time.
The document is about business P&L, not science, so most of its content (sales-and-marketing ROI, BPO displacement, workforce impact) is out of scope for this record.
Its transferable mechanisms are in scope: tool choice by task, evaluation on task outcomes rather than benchmarks, workflow fit over generic wrappers, memory and adaptation as the deciding capability, and the observation that unsanctioned personal-tool use often outperforms governed deployments.

## Hooks, with citations

**1. The failure is one of approach, not model quality.**
The document: "95% of organizations are getting zero return ... This divide does not seem to be driven by model quality or regulation, but seems to be determined by approach" (Executive Summary, pg. 3).
Relevance: frames adoption failure as a method-and-integration problem, the same premise behind [BP-01](../best-practices/01-match-method-to-task.md) and [BP-06](../best-practices/06-design-around-user-tasks.md).
Audiences: practitioners, providers, governance.

**2. The core barrier is learning, not infrastructure or talent.**
The document: "The core barrier to scaling is not infrastructure, regulation, or talent. It is learning. Most GenAI systems do not retain feedback, adapt to context, or improve over time" (Executive Summary, pg. 3; expanded in §4, pg. 10).
Relevance: names memory, context retention, and adaptation as the deciding capabilities; bears on what documentation and state an agent operates from ([BP-05](../best-practices/05-documentation-and-data-for-agents.md)).
Audiences: practitioners, providers.

**3. Fitness splits sharply by task type.**
The document: "AI has already won the war for simple work, 70% prefer AI for drafting emails ... But for anything complex or long-term, humans dominate by 9-to-1 margins. The dividing line isn't intelligence, it's memory, adaptability, and learning capability" (§4.3, pg. 13).
Relevance: direct field evidence that method should follow task, and that high-stakes work keeps a human in the loop ([BP-01](../best-practices/01-match-method-to-task.md), [BP-09](../best-practices/09-human-in-the-loop.md)).
Audiences: practitioners, governance.

**4. Buyers who succeed evaluate on outcomes, not model benchmarks.**
The document: buyers who cross the divide "Benchmarked tools on operational outcomes, not model benchmarks" and "evaluate tools based on business outcomes rather than software benchmarks" (§6.2, pg. 20; Executive Summary, pg. 3).
Relevance: mirrors [BP-08](../best-practices/08-evaluate-tools-before-trust.md): general leaderboard scores are not evidence a tool is fit for a specific task.
Audiences: practitioners, providers, governance.

**5. Tools fail on workflow fit, not features.**
The document: custom tools "fail due to brittle workflows, lack of contextual learning, and misalignment with day-to-day operations"; buyers want a "Deep understanding of our workflow" and "Most vendors don't get how our approvals or data flows work" (Executive Summary, pg. 3; §5.1, pg. 15).
Relevance: supports designing interfaces around real user tasks rather than wrapping generic capability ([BP-06](../best-practices/06-design-around-user-tasks.md)).
Audiences: providers, practitioners.

**6. A "shadow AI economy" outpaces official deployment.**
The document: "only 40% of companies say they purchased an official LLM subscription, [but] workers from over 90% of the companies we surveyed reported regular use of personal AI tools for work tasks ... This 'shadow AI' often delivers better ROI than formal initiatives" (§3.3, pg. 8).
Relevance: bears on [BP-03](../best-practices/03-register-and-vet-interfaces.md); governed channels that ignore how people actually work get bypassed, so vetting has to learn from real usage, not only restrict it.
Audiences: governance, providers.

**7. External partnerships reach deployment about twice as often as internal builds.**
The document: "external partnerships with learning-capable, customized tools reached deployment ~67% of the time, compared to ~33% for internally built tools", with the caveat that "correlation between external partnerships and success does not necessarily prove causation" (§6.1, pg. 19).
Relevance: a build-versus-buy signal relevant to how research groups and services resource agent capability; the causation caveat is part of the finding.
Audiences: providers, governance.

**8. Adoption is driven by "prosumers" with accountability retained at the top.**
The document: successful organisations "Sourced AI initiatives from frontline managers, not central labs"; deployments "began with power users ... who had already experimented with tools like ChatGPT or Claude", paired with "executive accountability"; and hiring now "consistently emphasize[s] AI literacy as a fundamental capability requirement" (§6.2, pg. 20; §6.4.2, pg. 22).
Relevance: distributed initiative with retained accountability tracks [BP-04](../best-practices/04-govern-autonomy-and-accountability.md); AI literacy as a skill requirement bears on training.
Audiences: governance, practitioners.

**9. The report positions agent memory and interoperability protocols (MCP, A2A, NANDA) as the fix.**
The document: "Agentic AI, the class of systems that embeds persistent memory and iterative learning by design, directly addresses the learning gap"; infrastructure is "emerging through frameworks like Model Context Protocol (MCP), Agent-to-Agent (A2A), and NANDA, which enable agent interoperability" (§4.3, pg. 13-14; §5.3, pg. 18; §6.5, pg. 22).
Relevance: same protocol substrate the record treats under agent-accessibility and trusted interfaces ([BP-02](../best-practices/02-default-to-agent-accessibility.md), [BP-03](../best-practices/03-register-and-vet-interfaces.md)); note the authors' stake in NANDA (see cautions).
Audiences: providers, practitioners.

## Mapping to practices

| Hook | Supports | In tension with |
|---|---|---|
| 1 | [BP-01](../best-practices/01-match-method-to-task.md), [BP-06](../best-practices/06-design-around-user-tasks.md) | |
| 2 | [BP-05](../best-practices/05-documentation-and-data-for-agents.md) | |
| 3 | [BP-01](../best-practices/01-match-method-to-task.md), [BP-09](../best-practices/09-human-in-the-loop.md) | |
| 4 | [BP-08](../best-practices/08-evaluate-tools-before-trust.md) | |
| 5 | [BP-06](../best-practices/06-design-around-user-tasks.md) | |
| 6 | [BP-03](../best-practices/03-register-and-vet-interfaces.md) | [BP-03](../best-practices/03-register-and-vet-interfaces.md) |
| 7 | [BP-01](../best-practices/01-match-method-to-task.md) | |
| 8 | [BP-04](../best-practices/04-govern-autonomy-and-accountability.md) | |
| 9 | [BP-02](../best-practices/02-default-to-agent-accessibility.md), [BP-03](../best-practices/03-register-and-vet-interfaces.md) | [BP-01](../best-practices/01-match-method-to-task.md) |

Tension on hook 6: the shadow-AI finding shows that vetting confined to a locked-down approved list gets routed around when the approved tools do not fit the work.
The practice still holds; the finding sharpens it toward vetting that learns from observed usage rather than blocking it.

Tension on hook 9: the report treats agentic systems with memory as the general answer, while [BP-01](../best-practices/01-match-method-to-task.md) holds that an agent is one option among several and often not the right one.
The report is co-produced by Project NANDA, an agent-infrastructure effort, so this framing carries a vendor interest.

## Proposed changes to practices

- [ ] Add this report as a supporting source to [BP-08](../best-practices/08-evaluate-tools-before-trust.md): field evidence that buyers who benchmark on task outcomes rather than model benchmarks succeed far more often (atom bp8-a3).
- [ ] Add as a supporting source to [BP-06](../best-practices/06-design-around-user-tasks.md): tools that miss workflow fit stall regardless of model quality (atom bp6-a1).
- [ ] Add as a supporting source to [BP-01](../best-practices/01-match-method-to-task.md): task type, not model capability, decides fit; simple tasks suit generic tools, complex work stays with humans (atoms bp1-a1, bp1-a2).
- [ ] Consider a one-line "what it looks like in practice" note on [BP-03](../best-practices/03-register-and-vet-interfaces.md): unsanctioned personal-tool use outpaces governed deployment when approved tools do not fit real work, so vetting should learn from observed usage. No wording change to the practice statement itself.
- [ ] No new practice. The report grounds existing practices; it does not clear the gating bar for a new one (it is out-of-domain enterprise evidence, and its distinct actions are already covered).

## Cautions and gaps

Domain mismatch. This is an enterprise business report; its subject is corporate P&L, not scientific work. Its statistics (95% zero return, ROI figures, industry disruption scores) describe commercial adoption and should be cited as external context, not as findings about science. The one direct science touch is thin: healthcare and pharma appear only as "documentation/transcription pilots; clinical models unchanged" (pg. 5), and a pharma procurement quote notes AI "helps our scientists get their tools faster ... several degrees removed from bottom-line impact" (pg. 9).

Author interest. The report is produced with Project NANDA, which builds agent-interoperability infrastructure (MCP, A2A, NANDA). Its conclusion that agentic, memory-equipped systems are the way across the divide aligns with that interest. Treat the agentic-web framing (§6.5, pg. 22) as advocacy, not evidence.

Method limits stated by the authors. Findings are "directionally accurate based on individual interviews rather than official company reporting" (pg. 6); build-versus-buy success rates "may reflect organizational capabilities rather than implementation approach alone" (pg. 19); the six-month observation window "may be insufficient" and could understate success (pg. 24). Selection bias toward organisations willing to discuss AI is acknowledged.

Not peer reviewed. The document is a preliminary industry report, self-described as "Preliminary Findings" (pg. 2).
