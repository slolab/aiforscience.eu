# Inbox

Transient staging area for documents to be distilled into library entries.

Drop a document (PDF, docx, markdown) here, then run the `distill` skill in a
Claude Code session in this repository. The skill drafts a page under
`docs/library/` with citations and a mapping to the best practices. You
review the draft, open a PR, and delete the raw file in the same PR.

Raw documents are never committed to `main`. The distilled page with its full
citation is the durable artifact. See `.claude/skills/distill/SKILL.md`.
