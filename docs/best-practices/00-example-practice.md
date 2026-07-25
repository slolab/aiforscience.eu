---
title: Write documentation with agents in mind
practice_id: BP-00
status: draft
first_added: 2026-07-25
last_reviewed: 2026-07-25
endorsed_by: []
sources:
  - title: Task force observation, working groups
    ref: https://github.com/slolab/aiforscience.eu
    locator: "July 2026"
layer: Method
hitl: n/a
tags: [both, method, draft]
comments: true
---

# BP-00: Write documentation with agents in mind

!!! warning "Dummy page"
    This page exists to review the practice-page format: frontmatter,
    metadata block, section structure, tags, and the discussion thread at
    the bottom. It is not a reviewed practice and will be replaced when the
    first real practices land.

!!! info "Practice metadata"
    **Status:** <span class="afs-badge afs-badge--draft">draft</span> ·
    **Endorsed by:** none yet ·
    **Last reviewed:** 2026-07-25

## Statement

Documentation should be precise, machine-readable, and current. Docs and
docstrings are the primary surface an agent uses to operate a tool or
service.

## Why it matters

Agents read documentation literally. Ambiguity that a human reader resolves
from context sends an agent down the wrong path. Outdated examples fail
silently: the agent follows them and produces wrong results. The precision
required for agents also serves human users, so this investment pays twice.

## What it looks like in practice

- Docstrings state parameter types, units, valid ranges, and failure modes.
- Examples are executable and tested in CI, so they cannot drift.
- One canonical description per capability, rather than the same information
  paraphrased in several places that then diverge.
- Documentation is published in formats agents can retrieve directly
  (plain text, markdown, structured metadata), without requiring a browser
  session.

## Sources

- Task force observation of working groups, July 2026.

## Change history

- 2026-07-25: Dummy page created to review the format.
