---
title: Evaluate / benchmark agentic tools before trusting their outputs
nav_title: "BP7 Evaluate before trust"
practice_id: BP-07
status: draft
first_added: 2026-07-26
last_reviewed: 2026-07-26
endorsed_by: []
sources:
  - title: "ELIXIR TF Agentic AI: agenda and rolling best practice (2026)"
    ref: library/elixir-tf-agentic-ai-2026.md
    locator: "Cautions and gaps (evaluation of skills/MCP servers as an open question)"
  - title: "REFORMS: consensus-based recommendations for machine-learning-based science (Science Advances 2024)"
    ref: https://doi.org/10.1126/sciadv.adk3452
    locator: "reporting standards for ML-based science"
  - title: "NeurIPS Paper Checklist / ML reproducibility checklist"
    ref: https://neurips.cc/public/guides/PaperChecklist
    locator: "reproducibility and evaluation reporting"
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
- Before an AI system informs scientific work, it needs to prove its suitability for the task at hand.
- For LLM-driven systems, there is no good general proxy (e.g., leaderboards) for their correctness in individual applications.
- Benchmarking is separate from safety ([BP2](02-register-and-vet-interfaces.md)) and auditability ([BP6](06-provenance-and-citation.md)).
  { .afs-practice__pivot }
- It is the adopter measuring a tool's performance on representative tasks and recording how it fails.

</div>

=== "Practitioners"

    A tool being available, popular, or well-described is not evidence that it is correct for your task.
    Before you rely on its output, run it on cases where you know the answer, check it across repeated runs, and note where it breaks.
    Keep that evidence; it is what justifies trusting the result.

=== "Providers"

    Publish evaluation evidence for what you ship: how the tool was tested, on what tasks, with what error rate and known failure modes.
    Make it easy for adopters to reproduce your evaluation.
    Benchmark scores on general tasks do not tell a user whether the tool is reliable for theirs.

=== "Governance"

    Require evaluation before reliance for tools that feed into results or decisions, proportionate to the stakes.
    Fund shared benchmarks and evaluation practice so adopters are not each testing blind.
    Support and fund independent evaluation efforts and community-driven challenges on held-out data.

## Reasons

Whether a tool is safe to connect and whether it is correct are different questions, answered by different people.
Registration and vetting ([BP2](02-register-and-vet-interfaces.md)) concern security at connect time; provenance and auditability ([BP6](06-provenance-and-citation.md)) concern the ability to trace answers after execution.
Evaluation (this practice) concerns accuracy and reliability at use time.
Goodhart's law states that a metric that becomes the target ceases to be a good metric; LLM leaderboards today decide on highest-volume investments for frontier AI companies.
Evaluation is the task of users, adopters, and community; only they know the task *and* possess the necessary stakes and incentives to desire an objective evaluation.
The evidence is clear that this cannot be skipped: a single benchmark score does not predict deployment reliability, agents vary run to run, and confabulation is common.
A tool that looks capable in a demo can be wrong in ways that only representative testing reveals.

## Examples

- A tool tested on representative tasks with known answers before it informs a study, with its error rate, consistency across repeated runs, and failure modes recorded.
- Providers publishing evaluation evidence (tasks, metrics, known limits) that an adopter can reproduce, not only a feature description.
- Red-teaming and hallucination/confabulation testing treated as the safety-and-correctness dimension of the same evaluation, not a separate afterthought.
- Reporting that follows an established checklist (for example REFORMS for ML-based science, or a reproducibility checklist), so evaluations are comparable.

!!! info "Practice metadata"
    **Status:** <span class="afs-badge afs-badge--draft">draft</span> ·
    **Endorsed by:** none yet ·
    **Last reviewed:** 2026-07-26

## Sources

- [ELIXIR TF Agentic AI: agenda and rolling best practice (2026)](../library/elixir-tf-agentic-ai-2026.md), Cautions and gaps: how to assess whether a skill or MCP server is useful and safe is recorded there as an open question and a candidate future practice.
- [REFORMS reporting standards (Science Advances 2024)](https://doi.org/10.1126/sciadv.adk3452).
  Consensus reporting standards for machine-learning-based science.
- [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist).
  Reproducibility and evaluation reporting practice.

## Change history

- 2026-07-26: Created.
  New practice for adopter-side evaluation of agentic tools, distinct from vetting at registration ([BP2](02-register-and-vet-interfaces.md)) and from self-audit of one's own agent ([BP3](03-govern-autonomy-and-accountability.md)).
  The ELIXIR task force flagged evaluation as an unresolved open question; red-teaming and hallucination-rate testing fold in as its safety and correctness dimensions.
