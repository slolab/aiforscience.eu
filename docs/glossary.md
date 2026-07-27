---
title: Glossary
---

# Glossary

The basic terms, as this site uses them.
The list grows with the record.
If a term is missing or unclear, [open an issue](https://github.com/slolab/aiforscience.eu/issues/new/choose).

<div class="afs-glossary" markdown>

Agent { #agent }
:   A system built around a language model that carries out multi-step work: it plans, calls tools, reads the results, and decides what to do next.
    The model supplies the reasoning; the surrounding [harness](#harness) does the acting.
    Distinct from a chat model that answers one prompt at a time.

Agentic AI { #agentic-ai }
:   The use of agents for real work.
    In science: literature triage, data analysis, coding, drafting.
    The subject of this record.
    Distinct from AI used as a scientific instrument (a predictor, a generative model, a classifier), which has its own established norms.
    The record treats an agent or model as a method chosen for a task rather than a default, and cites those norms rather than restating them (see [Match the method to the task](best-practices/01-match-method-to-task.md)).

Best practice { #best-practice }
:   A numbered, versioned statement of what works, written as an imperative.
    Each practice carries a status, its sources, and the organisations that endorse it.

Challenge { #challenge }
:   A documented disagreement with a practice, ideally with a concrete case where the practice fails.
    Challenges are the main input that drives revision.

Confabulation { #confabulation }
:   A confident, fluent output from a language model that is not grounded in fact, also called hallucination.
    Because it reads like a correct answer, it is caught by checking against sources, not by judging how plausible it looks.

Distillation { #distillation }
:   The process behind the [Library](library/index.md).
    A strategy paper or report is condensed into a cited entry and mapped to the practices it supports or contradicts.

Dual use { #dual-use }
:   Knowledge, tools, or capabilities that serve legitimate research and can also be turned to serious harm, for example designing a toxin, uplifting a cyberattack, or enhancing a pathogen.
    A dual-use request to an agent is one whose output could enable such harm, which is why high-consequence capabilities are screened (see [Screen agents for dual-use and high-consequence risk](best-practices/10-screen-dual-use-high-consequence.md)).

Endorsement { #endorsement }
:   A named organisation's formal backing of a practice.
    Recorded in the practice's metadata, never implied.

Guardrails { #guardrails }
:   Limits on what an agent can do, enforced by the system that runs it rather than stated only in policy.
    They take the form of permission scopes, autonomy limits, stop and escalation conditions, and shutdown paths.
    An agent cannot be talked out of a guardrail; it can only be stopped from taking the action (see [Govern agent autonomy and accountability](best-practices/04-govern-autonomy-and-accountability.md)).

Harness { #harness }
:   Everything in an agent except the language model itself: the loop that runs it, the tools and [interfaces](#interface) it can call, and the connections to outside systems.
    The model decides what to do; the harness carries it out.

Human in the loop (HITL) { #hitl }
:   A human checkpoint in an agentic workflow.
    Each practice states what oversight it requires: mandatory, optional, during the process, or as a final check.

Interface { #interface }
:   A component added to an agent's [harness](#harness) so it can reach a tool, data source, or action outside the model, for example an [MCP](#mcp) server, a skill, or a plugin.
    An interface runs code and acts for the user, so it is where much of the risk enters, which is why interfaces are registered and vetted (see [Register, vet, and manage agent interfaces](best-practices/03-register-and-vet-interfaces.md)).

Living record { #living-record }
:   This site.
    The live version is always current.
    Monthly dated releases, each with a DOI, exist for citation.
    See [Releases](releases/index.md).

Machine-actionable { #machine-actionable }
:   Data, metadata, and documentation structured so software can find, read, and act on it without a human interpreting it first.
    It is the founding goal of the FAIR principles, which agents now make concrete.
    Machine-readable is the weaker form: a program can parse the content but still needs a human to know what it means.

MCP (Model Context Protocol) { #mcp }
:   An open standard for connecting an agent to external tools, data, and actions.
    An MCP server is a common kind of [interface](#interface): it exposes a set of tools an agent can call.
    Used throughout this record as the running example of an agent interface, alongside skills and plugins.

Pioneer { #pioneer }
:   An early adopter who learns by doing.
    What pioneers learn is where the practices come from.

Prompt injection { #prompt-injection }
:   An attack that hides instructions inside content an agent reads (a web page, a document, a tool description), so the model follows them as if they came from the user.
    The user never sees the injected text, which is what makes it dangerous.
    Tool poisoning is one form, where the hidden instructions sit in an [interface's](#interface) tool description.

Settler { #settler }
:   The larger group that follows the pioneers and builds things meant to last.
    The practices are written for them.

Status { #status }
:   Where a practice stands. `draft`: proposed, under discussion. `reviewed`: accepted by the editor group. `endorsed`: formally backed by at least one named organisation or task force.

</div>
