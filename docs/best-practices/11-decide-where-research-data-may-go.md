---
title: Decide where research data may be sent
nav_title: "Decide where research data may be sent"
practice_id: BP-11
status: draft
first_added: 2026-10-08
last_reviewed: 2026-10-27
endorsed_by: []
sources:
  - ref: library/ref-gdpr-2016.md
    locator: "Arts 6, 9, 28, 32, 44 to 49"
    note: "Sending personal data to a service is processing: it needs a lawful basis (Article 6), an Article 9 exception for special-category data, a processor contract (Article 28), appropriate security (Article 32), and a transfer basis for a provider outside the EU (Articles 44 to 49), also when the provider does not train on the data (bp11-a3)."
  - ref: library/edpb-opinion-ai-models-2024.md
    locator: "paras 126, 129-130"
    note: "The organisation deploying a model is a controller for its own processing and has to check the provider (bp11-a3)."
  - ref: library/era-living-guidelines-genai-2026.md
    locator: "Recommendations for researchers 3, pp. 8-9; Recommendations for research organisations 4, p. 10"
    note: "Uploaded input may be used for other purposes such as training; researchers check who runs a tool, where, and under which privacy options, and do not upload sensitive work without assurances against re-use; organisations provide tools they govern themselves (bp11-a1, bp11-a2, bp11-a3). Non-binding, and written for tools a person uses, not agents."
  - ref: library/ref-edps-commission-m365-2024.md
    locator: "2024 decision; 2025 closure"
    note: "The provider's standard terms did not meet the institution's legal duties; compliance came from a renegotiated contract and technical measures (bp11-a3). An office suite and an EU institution, not an AI service; the decision is challenged before the General Court."
  - ref: library/ref-dutch-dpa-chatbot-breaches-2024.md
    locator: "2024 breach notifications; GP practice case"
    note: "Most chatbot providers store all data entered; staff entered patient data into a consumer chatbot against written rules, and the regulator treated it as a data breach (bp11-a1, bp11-a3). Outside research."
  - ref: library/ref-anthropic-consumer-terms-2025.md
    locator: "consumer plans versus commercial terms"
    note: "Consumer accounts train on inputs by default with five-year retention; commercial terms exclude training (bp11-a2). One provider at one date."
  - ref: library/ref-openai-preservation-order-2025.md
    locator: "13 May 2025 order; provider statement on covered tiers"
    note: "A court order overrode a written deletion promise for consumer and standard-API tiers; zero-retention tiers were unaffected (bp11-a2). US copyright litigation, outside science."
  - ref: library/ref-dsk-ki-datenschutz-2024.md
    locator: "§1.7 para 20; §2.1 para 33; §2.4 para 41; §2.5 para 43"
    note: "German regulators: closed systems preferable, a processor agreement, work accounts so staff need no private ones, and training settings fixed at account setup (bp11-a2, bp11-a3)."
  - ref: library/ref-aepd-agentic-ai-2026.md
    locator: "pp. 34, 52, 57-58"
    note: "The deployer configures which services an agent may reach and evaluates each service's terms, Article 28 status, transfers, and retention; online service terms change unilaterally; an agent with screen access can send third parties' information to external servers (bp11-a2, bp11-a3, bp11-a4, bp11-a5)."
  - ref: library/ref-cnil-cianum-agentic-ai-2026.md
    locator: "pp. 14-15"
    note: "Actions classified by risk per connected service, including sending data outside the system (bp11-a5). Exploratory, non-binding."
  - ref: library/gagneur-rare-disease-patient-data-2026.md
    locator: "hook 1"
    note: "An agent that runs code and inspects results transmits material to the service operating it, so participant-level data can leave an approved environment without a deliberate upload (bp11-a4). A commentary arguing from risk, not a measured incident."
  - ref: library/ref-ehds-2025.md
    locator: "Art 73"
    note: "Article 73 allows access only inside a secure processing environment, from which no personal data may leave (bp11-a3). Health-data instance, cited as an example."
  - ref: library/ref-edpb-edps-cloud-act-2019.md
    locator: "Article 48 analysis"
    note: "A CLOUD Act order is not in itself a legal ground for transfer under Article 48 GDPR. Context for the governance tab on EU hosting at a provider under US jurisdiction; no atom rests on it."
  - ref: library/ref-senat-microsoft-hearing-2025.md
    locator: "hearing of 10 June 2025"
    note: "A US provider's legal director could not guarantee under oath that EU-hosted data stays out of US hands. Context for the governance tab; no atom rests on it."
layer: Operational
hitl: n/a
tags: [practitioner, provider, governance, draft]
comments: true
---

<!-- BP_TITLE -->
<!-- The H1 above is generated from this page's frontmatter title by hooks/bp_pages.py. Edit `title:`, not here. -->

## Practice

<div class="afs-practice" markdown>

- Sending data to an AI service hands it to the provider under their terms of service.
  { #bp11-a1 }
- The account tier and its terms decide whether inputs train a model, how long they are kept, and who else can use them.
  { #bp11-a2 }
- Personal, confidential, or controlled-access data must only be provided to a service under a contract that fits the legal regime of the data, or must stay in an environment governed by the party responsible for the data.
  { #bp11-a3 }
- An [agent](../glossary.md#agent) using an externally hosted model sends everything it reads to the model's provider, so reading a file already discloses it.
  { #bp11-a4 }
- For an agent, the services it may send data to must be limited by its technical environment; instructions alone are insufficient.
  { #bp11-a5 }

</div>

=== "For practitioners"

    Sending personal data to an AI service is itself processing under data protection law: it needs a legal basis, a processor contract, and, for a provider outside the EU, a transfer basis.
    This holds even when the provider does not train on the data.
    For personal, confidential, or controlled-access data, use the account or deployment your institution has contracted, check how long inputs are kept and whether they are used for training, and keep such data local when no contracted route exists.
    Anything an agent using an externally hosted model reads goes to the provider, so keep secrets and protected data out of the directories it can read, preferably by sandboxing your agents.

=== "For providers"

    If you offer an AI service, offer a tier that excludes training and long retention, processes under a contract and in a location that fit the customer's legal regime, and state plainly which legal process can reach the data.
    Make that tier the default for institutional customers.
    If your scientific service passes user data to a model provider, say which provider and under which terms, and offer a route that keeps the data in an environment the user's institution governs.

=== "For governance"

    Contract the AI services used by your staff; ensure a processor agreement, exclude use of data for training, and establish the transfer basis; provide institutional accounts, and ensure no one uses a consumer account for work.
    State which data classes may reach which tier.
    Hosting in the EU at a provider under US jurisdiction does not by itself remove the reach of US legal process; decide what that means for each data class.

## Reasons

Typing data into an AI service, or letting an agent send it, hands the data to the service provider.
The user's account tier and the contract determine downstream effects: whether the input can be used to train a model and how long it is kept.
For instance, consumer accounts of one provider train on inputs by default and keep them for five years; its commercial tier excludes training and keeps them for 30 days.
Service providers fall under their own jurisdictions: a US court ordered another provider to keep consumer and standard-API chats that users had deleted; zero-retention customers were unaffected.

For personal data, the act of sending is already processing under data protection law.
It needs a lawful basis, a processor contract, appropriate security, and a transfer basis when the provider is outside the EU.
These requirements apply even if the provider never trains on the data.
A regulator has treated staff entering patient data into a consumer chatbot as a data breach, although the practice had written rules against it.
The EDPB and the data protection authorities of Germany, France, and Spain place the check on the organisation that deploys the service.
The EDPS found the European Commission's own use of a cloud office suite under the provider's standard terms unlawful until the contract was renegotiated.

This practice does not restate data protection law or research ethics.
It covers what AI changes: the decision to disclose data moves to the moment of use.
These decisions are made at institutional level (e.g., via enterprise settings), by single persons (e.g., by deciding what to work on), or even autonomously (in agentic setups).
What happens to the data then depends on the provider's terms and jurisdiction.

For an agent on an externally hosted model, this applies to every file it opens, every command output, and every tool result, because they enter the model's context and thus are sent to the provider.
Data held under withdrawable consent must also never be committed to third-party training; that irreversible case is screened under [BP10](10-screen-dual-use-high-consequence.md).
How an agent's limits are enforced in the system, and who answers for them, is [BP04](04-govern-autonomy-and-accountability.md).

## Examples

- A researcher's consumer chatbot account trains on inputs by default and keeps them for five years; the same provider's institutional tier excludes training and keeps them for 30 days.
  The lab's governance decides which account is used for work.
- A US court orders a provider to preserve all consumer and standard-API chat logs, including ones users deleted; enterprise and zero-retention customers are excluded.
  A lab on a consumer account has its deleted chats kept for four months; a lab on a zero-retention contract does not.
- An employee of a general practice enters patients' medical data into a consumer chatbot against the practice's rules, and the national regulator treats it as a data breach (healthcare delivery, outside research).
  An institutional account under a processor agreement, or a network that blocks the consumer service, would have kept the data in.
- A social science group transcribes and codes research interviews with an AI service.
  The transcripts go to the institution's contracted deployment, which runs under a processor agreement with training excluded, and not to a team member's personal account.
- A coding agent asked to fix a failing script opens the project's `.env` file to check a setting.
  The API keys and database password in it are now in the provider's logs under the account's retention terms, and the keys have to be rotated.
  Keeping secrets outside the directories the agent can read prevents this.
- An agent analysing survey records runs on the institution's contracted model deployment, so the records reach only a provider under contract.
  It can also call a web search tool; its configuration lists the services it may send data to, and the search tool receives the query only, never the records.
- Under the European Health Data Space, an agent working on permitted health data computes inside a secure processing environment and cannot move personal data out of it, to a model provider or anywhere else (health-data instance).

<!-- BP_SOURCES -->
<!-- The Sources list above is generated from this page's frontmatter sources by hooks/bp_pages.py. Edit `sources:`, not here. -->

## Change history

- 2026-10-08: Created from the ingestion on EU data protection and AI-provider terms (Commission living guidelines, EDPB Opinion 28/2024, and decisions and guidance from the EDPS and the Dutch, German, French, and Spanish data protection authorities), in response to challenge [#33](https://github.com/slolab/aiforscience.eu/issues/33) and editor review on PR [#22](https://github.com/slolab/aiforscience.eu/pull/22).
  New practice rather than atoms on BP04, because deciding which data may go to which service is a separate action that applies to people using AI tools as well as to agents.
