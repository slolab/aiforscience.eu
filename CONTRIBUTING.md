# Contributing

What to contribute, and through which route, is on the site:
[aiforscience.eu/about/contribute](https://aiforscience.eu/about/contribute/).
Issue templates for proposing a practice, challenging a practice, and
submitting a document; [Discussions](https://github.com/slolab/aiforscience.eu/discussions)
for anything open-ended; the
[AI for Science Google Group](https://groups.google.com/g/aiforscience)
(aiforscience@googlegroups.com) if you do not use GitHub.

This file covers working in the repository.

## Setup

See [Development](README.md#development) in the README.

## Checks

Two checks run on every pull request
([`.github/workflows/ci.yaml`](.github/workflows/ci.yaml)). Run both before
you push:

```sh
uv run mkdocs build --strict              # fails on broken internal links
uv run python scripts/check_provenance.py # provenance ids and references
```

## Conventions

[CLAUDE.md](CLAUDE.md) is the source for page structure, the practice
frontmatter schema, the library templates, and the writing style. Follow it
manually or hand it to an agent. Prose is written one sentence per source
line, which changes the source only and never the rendered page.

## Branches and pull requests

Branch off `main`, one topic per branch, and open a pull request. Do not push
to `main`. The [pull request template](.github/pull_request_template.md) lists
what a reviewer will check. Anything that changes a practice's status or adds
an endorsement needs a second editor, per
[Governance](https://aiforscience.eu/about/governance/).

## Distilled documents

`sources/inbox/` is transient staging. Raw PDFs and Word files are never
committed. What lands in the pull request is the library entry, the practice
updates, and the atom-level edges in `docs/assets/provenance.yml`. Drafting is
AI-assisted (`.claude/skills/distill/`); the editor checks every quote and
locator against the original and is accountable for the result.

## Declaring an interest

If you propose a practice based on your own work, or submit a document you
authored, say so in the issue or pull request. The record notes it where it
applies, and downweights a source whose author is a contributor here.

## Licensing your contribution

Opening a pull request offers the change under the repository's licences:
[MIT](LICENSE) for site configuration and code, [CC-BY-4.0](LICENSE-CONTENT)
for content under `docs/`. You keep copyright in what you write. There is no
contributor licence agreement and no sign-off requirement.

## Code of conduct

The [Contributor Covenant 2.1](CODE_OF_CONDUCT.md) applies in this
repository, in Discussions, on the Google Group, on the monthly call, and at
events held under the AI for Science name.
