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

What to contribute and through which route:
[aiforscience.eu/about/contribute](https://aiforscience.eu/about/contribute/).
How to work in this repository: [CONTRIBUTING.md](CONTRIBUTING.md).
Everyone taking part is covered by the
[code of conduct](CODE_OF_CONDUCT.md).

## Editors

- Sebastian Lobentanzer (Helmholtz Munich)

The role, the time it takes, and how to join:
[aiforscience.eu/about/editors](https://aiforscience.eu/about/editors/).

## Releases

A dated release is cut monthly (`vYYYY.MM`) and mirrored at
[aiforscience.eu/releases](https://aiforscience.eu/releases/). Each release
receives a version DOI via Zenodo. The concept DOI
[10.5281/zenodo.21709875](https://doi.org/10.5281/zenodo.21709875) is stable
across releases and resolves to the latest snapshot.

## License

Site configuration and code: [MIT](LICENSE). Written content under `docs/`:
[CC-BY-4.0](LICENSE-CONTENT).
