---
title: "Court-ordered retention of ChatGPT logs in the New York Times litigation (2025)"
ref_id: openai-preservation-order-2025
source_type: report
issuing_body: "US District Court for the Southern District of New York (order); OpenAI (statement)"
published: 2025
doi_or_url: https://openai.com/index/response-to-nyt-data-demands/
added_on: 2026-09-05
grounds: [BP-04, BP-10]
tags: [library, reference]
comments: true
---

# Court-ordered retention of ChatGPT logs in the New York Times litigation (2025)

!!! info "Reference"
    **Citation:** In re OpenAI, Inc. Copyright Infringement Litigation, No. 25-md-3143 (S.D.N.Y.), order of Magistrate Judge Ona T. Wang, 13 May 2025 (relating to 23-cv-11195, docket entry 551); OpenAI, "How we're responding to The New York Times' data demands in order to protect user privacy", 5 June 2025, updated after 26 September 2025. **Type:** court order and provider statement. **Links:** [OpenAI statement](https://openai.com/index/response-to-nyt-data-demands/), [docket entry (Justia)](https://docs.justia.com/cases/federal/district-courts/new-york/nysdce/1:2023cv11195/612697/551).

## What it is

In a copyright suit brought by news publishers, a US federal court ordered OpenAI "to preserve and segregate all output log data that would otherwise be deleted on a going forward basis until further order of the Court (in essence, the output log data that OpenAI has been destroying), whether such data might be deleted at a user's request or because of 'numerous privacy laws and regulations' that might require OpenAI to do so" (order, p. 2).
OpenAI stated that the order covered "ChatGPT Free, Plus, Pro, and Team" subscriptions and API use "without a Zero Data Retention agreement", and did not cover "ChatGPT Enterprise or ChatGPT Edu customers" or API customers on zero-data-retention endpoints.
OpenAI's position: "This fundamentally conflicts with the privacy commitments we have made to our users."
The going-forward obligation ended on 26 September 2025.
OpenAI then stated that it was no longer required to retain new data "or any conversations originating from the European Economic Area, Switzerland, or the United Kingdom", while a limited set of April to September 2025 data stayed under legal hold.
In January 2026 the district judge affirmed orders requiring production of a sample of 20 million de-identified consumer logs to the plaintiffs.

## Role in the record

- Grounds [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1): a written deletion promise was overridden by a court order for four months; only the tiers with retention excluded in the system (zero-data-retention endpoints) were unaffected.
- Context for [BP10](../best-practices/10-screen-dual-use-high-consequence.md) (bp10-a5) and for the BP04 atoms proposed in the [ERA guidelines entry](era-living-guidelines-genai-2026.md): the account tier decided what "delete" meant, and a provider under US jurisdiction can be compelled to keep data that EU law says must be erased.
- Recorded in the [Failures log](../best-practices/failures.md).
- Limits: the case is US civil litigation over copyright, outside science; the structure (tier decides exposure, legal process overrides terms) is what transfers. The primary order is on the court docket; the plan-by-plan detail comes from the provider's own statement.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
