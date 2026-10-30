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

- **2026-09** — A court order overrode a provider's deletion promise for consumer and standard-API chat logs for four months.
  In May 2025 a US federal court ordered OpenAI to preserve all ChatGPT output logs that would otherwise be deleted, including logs users had deleted and logs whose deletion privacy law required; the order covered Free, Plus, Pro, and Team accounts and API use without a zero-data-retention agreement, and excluded Enterprise, Edu, and zero-data-retention API customers.
  The going-forward obligation ended on 26 September 2025; a 20-million-log de-identified sample was later ordered produced to the plaintiffs.
  The written retention policy did not hold; the tiers where non-retention was built into the system did.
  Reported outside science; the structure applies to any lab whose members use a consumer or standard-tier AI account for work.
  Related practices: [BP11](11-decide-where-research-data-may-go.md), [BP04](04-govern-autonomy-and-accountability.md), [BP10](10-screen-dual-use-high-consequence.md).
  Source: [Court-ordered retention of ChatGPT logs in the New York Times litigation (2025)](../library/ref-openai-preservation-order-2025.md).

- **2026-09** — Staff entered patient data into a consumer AI chatbot against their organisation's rules; the regulator treated it as a data breach.
  The Dutch Data Protection Authority reported several breach notifications in 2024 in which employees had entered personal data into AI chatbots, among them a general-practice employee who entered patients' medical data "contrary to the agreements" and a telecom employee who entered a file of customer addresses.
  The regulator's point: most chatbot providers store everything entered, so the data left the organisation's control the moment it was typed in; a written rule did not prevent it.
  Reported outside research; the same tool is at hand in every lab.
  Related practices: [BP11](11-decide-where-research-data-may-go.md), [BP04](04-govern-autonomy-and-accountability.md), [BP10](10-screen-dual-use-high-consequence.md).
  Source: [Dutch DPA: AI chatbot use leads to data breaches (2024)](../library/ref-dutch-dpa-chatbot-breaches-2024.md).

- **2026-07** — Hidden instructions in a shared document made an assistant alter the draft it was writing and copy the attack into that draft, which then compromised the next one.
  A [prompt injection](../glossary.md#prompt-injection) concealed as white 8-point text in an attached Word file caused Copilot to halve every financial figure in a generated report and to append the same instructions, hidden the same way, to the output; a later drafting session reproduced the attack from that generated document alone, with the original file no longer attached.
  Two vendor mitigations over a 144-day coordinated disclosure, one of them a model upgrade, closed the reported payloads but not the class, which still reproduced at publication.
  Human review was the only mitigation available to customers, and the researcher had to instruct the model to announce its own edits because they were otherwise too subtle for a reviewer to notice.
  Demonstrated in a commercial productivity suite, not observed in the wild and not in a scientific setting; the affected workflow, drafting a document from attached documents, is the one used for manuscripts, reviews, and reports.
  Related practices: [BP03](03-register-and-vet-interfaces.md), [BP09](09-human-in-the-loop.md), [BP07](07-provenance-and-citation.md), [BP04](04-govern-autonomy-and-accountability.md).
  Source: [Self-propagating prompt injection in Copilot for Word (2026)](../library/ref-copilot-word-ai-worm-2026.md).

- **2026-07** — Three citations in an [agent](../glossary.md#agent)-assisted paper claimed more than their cited sources supported.
  A self-audit compared each load-bearing citing sentence against the actual content of its source, rather than only confirming that the source existed, and found the three overreaches; the text was repaired before the sources were promoted.
  A plain existence check would have passed all three.
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
