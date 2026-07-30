# aiforscience.eu

Source for [aiforscience.eu](https://aiforscience.eu): a living record of
best practices for applying agentic AI to science.

The site is a running document. It aggregates what task forces and
institutions learn about agentic AI in scientific work, revises it at the
pace of the field, and versions it for citation. It grows out of task-force
work on AI for science, starting with Helmholtz AI, and is built to take
more organisations on board.

## Development

```sh
uv sync
uv run mkdocs serve          # preview at http://127.0.0.1:8000
uv run mkdocs build --strict # run before every PR
```

Built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
Content conventions, the practice metadata schema, and the writing style
rules are in [CLAUDE.md](CLAUDE.md).

## Contributing

See [aiforscience.eu/about/contribute](https://aiforscience.eu/about/contribute/).
Short version: issue templates for proposing, challenging, and submitting
documents; discussions for everything open-ended; PRs welcome. Contributors
without a GitHub account can use the
[AI for Science Google Group](https://groups.google.com/g/aiforscience)
(aiforscience@googlegroups.com); editors carry input from there into the
record.

Document ingestion is AI-assisted and human-reviewed: drop a document into
`sources/inbox/`, run the `distill` skill in a Claude Code session, review
the drafted library entry, open a PR. Raw documents are never committed to
`main`.

## Editors

- Sebastian Lobentanzer (Helmholtz Munich)

The role, the time it takes, and how to join:
[aiforscience.eu/about/editors](https://aiforscience.eu/about/editors/).

## Releases

A dated release is cut monthly (`vYYYY.MM`) and mirrored at
[aiforscience.eu/releases](https://aiforscience.eu/releases/). Each release
receives a DOI via Zenodo.

## License

Site configuration and code: [MIT](LICENSE). Written content under `docs/`:
[CC-BY-4.0](LICENSE-CONTENT).
