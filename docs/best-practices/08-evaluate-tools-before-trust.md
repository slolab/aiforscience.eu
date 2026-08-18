---
title: Evaluate / benchmark agentic tools before trusting their outputs
nav_title: "Evaluate tools before trust"
practice_id: BP-08
status: draft
first_added: 2026-07-26
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Cautions and gaps (evaluation of skills/MCP servers as an open question)"
    note: "Cautions and gaps: how to assess whether a skill or MCP server is useful and safe is recorded there as an open question and a candidate future practice."
  - title: "REFORMS: consensus-based recommendations for machine-learning-based science (Science Advances 2024)"
    ref: library/ref-reforms-2024.md
    locator: "reporting standards for ML-based science"
    note: "Consensus reporting standards for machine-learning-based science."
  - title: "NeurIPS Paper Checklist / ML reproducibility checklist"
    ref: library/ref-neurips-checklist.md
    locator: "reproducibility and evaluation reporting"
    note: "Reproducibility and evaluation reporting practice."
  - title: "MIT Project NANDA, The GenAI Divide (2025)"
    ref: library/mit-genai-divide-2025.md
    locator: "§6.2 p.20 benchmark on operational outcomes, not model benchmarks"
    note: 'Enterprise field evidence that buyers who "benchmark tools on operational outcomes, not model benchmarks" succeed far more often; general benchmark scores do not predict fitness for a specific task (§6.2, pg. 20). Out-of-domain business report; cited as external context.'
  - title: "EU AI Omnibus (2026)"
    ref: library/ai-omnibus-2026.md
    locator: "Art 4a; Recital 9 (conditional basis for special-category data in bias detection)"
    note: "Art 4a. The amended AI Act sets a conditional legal basis for processing special-category data to detect and correct bias, an evaluation dimension, subject to strict safeguards (bp8-a2)."
layer: Operational
hitl: n/a
tags: [practitioner, provider, governance, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- Run task-specific benchmarks before giving an [agent](../glossary.md#agent) autonomy in your workflow.
  { #bp8-a1 }
- Before an AI system informs scientific work, it needs to prove its suitability for the task at hand.
  { #bp8-a2 }
- For LLM-driven systems, there is no good general proxy (e.g., leaderboards) for their correctness in individual applications.
  { #bp8-a3 }
- Benchmarking is separate from safety ([BP03](03-register-and-vet-interfaces.md)) and auditability ([BP07](07-provenance-and-citation.md)).
  { .afs-practice__pivot #bp8-a4 }
- It is the adopter measuring a tool's performance on representative tasks and recording how it fails.
  { #bp8-a5 }

</div>

=== "For practitioners"

    A tool being available, popular, or well-described is not evidence that it is correct for your task.
    Before you rely on its output, run it on cases where you know the answer, check it across repeated runs, and note where it breaks.
    Keep that evidence; it is what justifies trusting the result.

=== "For providers"

    Publish evaluation evidence for what you ship: how the tool was tested, on what tasks, with what error rate and known failure modes.
    Make it easy for adopters to reproduce your evaluation.
    Benchmark scores on general tasks do not tell a user whether the tool is reliable for theirs.

=== "For governance"

    Require evaluation before reliance for tools that feed into results or decisions, proportionate to the stakes.
    Fund shared benchmarks and evaluation practice so adopters are not each testing blind.
    Support and fund independent evaluation efforts and community-driven challenges on held-out data.

## Reasons

Whether a tool is safe to connect and whether it is correct are different questions, answered by different people.
Registration and vetting ([BP03](03-register-and-vet-interfaces.md)) concern security at connect time; provenance and auditability ([BP07](07-provenance-and-citation.md)) concern the ability to trace answers after execution.
Evaluation (this practice) concerns accuracy and reliability at use time.
Goodhart's law states that a metric that becomes the target ceases to be a good metric; LLM leaderboards today decide on highest-volume investments for frontier AI companies.
Evaluation is the task of users, adopters, and community; only they know the task *and* possess the necessary stakes and incentives to desire an objective evaluation.
The evidence is clear that this cannot be skipped: a single benchmark score does not predict deployment reliability, agents vary run to run, and [confabulation](../glossary.md#confabulation) is common.
A tool that looks capable in a demo can be wrong in ways that only representative testing reveals.

## Examples

- A team adopts a tool because it tops a public leaderboard, then finds it wrong on their own data; the leaderboard measured a different task from theirs.
- Before relying on a tool, the adopter runs it on cases where the answer is known, checks it across repeated runs, and records where it breaks; that evidence is what justifies trusting the result.
- A tool that looked convincing in a demo is wired into a study without testing, and a confabulated value reaches an analysis before anyone checks it.
- A provider ships evaluation evidence with the tool (tasks, metrics, error rate, known failure modes) that an adopter can reproduce, not only a feature description.
- Red-teaming and hallucination/confabulation testing are run as the safety-and-correctness side of the same evaluation, not a separate afterthought.
- Evaluations follow an established checklist (for example REFORMS for ML-based science, or a reproducibility checklist), so different groups' results are comparable.

<!-- BP_SOURCES -->
<!-- The Sources list above is generated from this page's frontmatter sources by hooks/bp_pages.py. Edit `sources:`, not here. -->

## Change history

- 2026-07-27: Added the EU AI Omnibus (2026) as a qualifying source on bp8-a2 (conditional legal basis for special-category data in bias detection; Art 4a).
- 2026-07-27: Added The GenAI Divide (MIT NANDA 2025) as a supporting source on outcome-based evaluation over benchmark scores (bp8-a3).
- 2026-07-27: Renumbered from BP07 to BP08 on inserting the new BP01 (match the method to the task).
- 2026-07-27: Rewrote Examples as concrete scenarios (actor, action, outcome), including anti-patterns; kept the labelled instance (REFORMS).
- 2026-07-26: Created.
  New practice for adopter-side evaluation of agentic tools, distinct from vetting at registration ([BP03](03-register-and-vet-interfaces.md)) and from self-audit of one's own agent ([BP04](04-govern-autonomy-and-accountability.md)).
  The ELIXIR task force flagged evaluation as an unresolved open question; red-teaming and hallucination-rate testing fold in as its safety and correctness dimensions.
