---
title: "AEPD guidance on agentic AI from a data protection perspective (2026)"
ref_id: aepd-agentic-ai-2026
source_type: guidance
issuing_body: "Agencia Española de Protección de Datos"
published: 2026
doi_or_url: https://www.aepd.es/guias/orientaciones-ia-agentica.pdf
added_on: 2026-09-05
grounds: [BP-04]
tags: [library, reference]
comments: true
---

# AEPD guidance on agentic AI from a data protection perspective (2026)

!!! info "Reference"
    **Citation:** Agencia Española de Protección de Datos. "Inteligencia artificial agéntica desde la perspectiva de protección de datos", version 1.2, February 2026. In Spanish. **Type:** regulator guidance. **Link:** [aepd.es](https://www.aepd.es/guias/orientaciones-ia-agentica.pdf).

## What it is

A 76-page guidance from the Spanish data protection authority for controllers and processors that implement processing with AI agents.
It treats the agent's connections to external services as a compliance problem in their own right.
Even services from one provider evolve separately, "con términos y contratos no homogéneos, incompatibilidades, discontinuidad de los servicios y cambios de interfaz" (p. 20).
When a controller deploys agents itself, it should configure which services the agents may access, "evaluar los contratos o términos de servicio, revisar las cláusulas de protección de datos", determine the lawfulness of the processing, weigh the risk to data subjects, and judge "si es proporcional el uso de dicho servicio o es más conveniente buscar alternativas", checking compliance "en particular con relación, entre otros, al artículo 28 del RGPD, transferencias internacionales, conservación de datos" (p. 34).
Relations with model developers and agent providers are to be formalised, "aclarando la distribución de obligaciones en los términos y condiciones o contratos" (p. 55).
On the reality of online service contracts: "los contratos no se ajustan al régimen jurídico local, los términos de los contratos cambian unilateralmente, e incluso el objeto del contrato se altera sin previo aviso" (contracts do not fit the local legal regime, terms change unilaterally, and even the object of the contract changes without notice; pp. 57-58).
Among threats, an agent with screen access "puede procesar información de terceros abierta en el escritorio ... para finalidades no autorizadas por esos terceros, como el entrenamiento de modelos o la exfiltración a servidores externos" (p. 52).

## Role in the record

- Grounds [BP04](../best-practices/04-govern-autonomy-and-accountability.md) (bp4-a1, bp4-a3): configuring which services an agent may reach is a permission scope set by the controller, and the terms of each reachable service are part of that decision.
- Context for the BP04 atoms proposed in the [ERA guidelines entry](era-living-guidelines-genai-2026.md): a supervisory authority states that evaluating the provider's terms, Article 28 status, transfers, and retention is the deployer's duty, and that alternatives should be sought where the service is disproportionate.
- Limits: Spanish-language, addressed to controllers under Spanish and EU law; translations here are the record's own. Not research-specific.

Atom-level for/against detail and quotes are in the provenance data (`assets/provenance.yml`), keyed by practice atom.
