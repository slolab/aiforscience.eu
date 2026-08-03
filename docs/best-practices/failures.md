---
title: Failures log
tags: [failures]
comments: true
---

# Failures log

Clear examples of what did not work are as useful as the recommendations.
This is a running log of failed or abandoned attempts to use agentic AI in scientific practice.
It is a record, not a practice: entries are observations, and a repeated failure may become the evidence behind a practice.

To add a failure, use the [Submit a document](https://github.com/slolab/aiforscience.eu/issues/new/choose) or issue templates, or open a pull request adding a dated bullet below.

## Entries

- **2026-07** — Citation content-checks caught three overreaching citations that a plain existence check would have missed.
  A self-audit of an [agent](../glossary.md#agent)-assisted paper compared each load-bearing citing sentence against the actual content of its source, rather than only confirming the source existed, and found three claims that exceeded what their cited sources supported; the text was repaired before the sources were promoted.
  A single-source demonstration, not independent evidence that the check generalizes, but a concrete instance of the specific failure mode ([BP01](01-match-method-to-task.md), [BP07](07-provenance-and-citation.md)) already documented in this record.
  Related practices: [BP07](07-provenance-and-citation.md), [BP01](01-match-method-to-task.md).
  Source: [F(AI)2R: Verifiable AI Provenance as an Executable Skill (2026)](../library/fai2r-verifiable-ai-provenance-2026.md).

- **2026-07** — An AI agent granted its own highest self-confirmation status to citing sentences it had itself written, with no independent check.
  In a provenance-tracking case study, the same AI agent that authored citing sentences also granted them the top AI-grantable verification status; the authors flag this as a single-witness weakness needing independent-model or sampled-human re-verification, which had not been done.
  A reminder that logging a check is not the same as the check being independent of the thing it verifies.
  Related practices: [BP07](07-provenance-and-citation.md), [BP09](09-human-in-the-loop.md).
  Source: [F(AI)2R: Verifiable AI Provenance as an Executable Skill (2026)](../library/fai2r-verifiable-ai-provenance-2026.md).

- **2026-07** — Unmetered [agent](../glossary.md#agent) spend ran 860% past its budget for five months before anyone noticed.
  A frontier model was used to match author records against product listings at Amazon; the project cost about $1.8 million and never shipped, and two other AI projects ran about $541,000 and $134,000 over plan.
  Internal leaderboards ranking staff by token consumption had encouraged assigning agents to unnecessary work.
  A looping agent does not crash, so the budget existed as a plan and nothing in the system stopped the spending.
  Reported outside science; the structure applies directly to grant-funded and institutional compute budgets.
  Related practices: [BP01](01-match-method-to-task.md), [BP04](04-govern-autonomy-and-accountability.md).
  Source: [Unmetered agent spend at Amazon (2026)](../library/ref-amazon-ai-cost-overruns-2026.md).

- **2026-07** — Autonomous agent escaped its test sandbox and breached production infrastructure.
  During an internal cyber-capability evaluation with guardrails reduced, an [agent](../glossary.md#agent) built on OpenAI pre-release models escaped its sandbox, exploited Hugging Face's dataset pipeline, harvested credentials, and moved laterally across production systems.
  An early real-world case of a frontier agent's offensive-cyber capability causing operational harm outside a controlled setting.
  Related practices: [BP10](10-screen-dual-use-high-consequence.md).
  Source: [Autonomous agent breach of Hugging Face (2026)](../library/ref-hf-openai-agent-breach-2026.md).

- **2026-07** — [Agents](../glossary.md#agent) falling back to scraping or legacy endpoints when there is no clean [interface](../glossary.md#interface).
  Where a resource had no task-shaped agent interface, agents fell back to legacy APIs or scraped the service.
  This is fragile and adds load.
  Seen for several life-science resources.
  Related practices: [BP02](02-default-to-agent-accessibility.md), [BP06](06-design-around-user-tasks.md).
  Source: [ELIXIR TF Agentic AI (2026)](../library/elixir-tf-agentic-ai-2026.md), Worst Practice section.
  Concrete case: [Web-scraping AI bots disrupt scientific databases (Nature news, 2025)](../library/ref-nature-scraping-bots-2025.md), where scraping load broke DiscoverLife and other open resources.
