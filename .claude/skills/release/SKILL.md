---
name: release
description: Cut a dated monthly snapshot of aiforscience.eu as a git tag and GitHub Release, update the releases page, and fill in the Zenodo DOI once minted. Use when the user wants to cut a release, tag a monthly snapshot, or update the releases page and DOI.
---

# Cut a dated release

The live site always shows the current state of the record. For citation, a
dated snapshot is cut monthly as a git tag and GitHub Release. Zenodo archives
each release and mints a DOI.

You do everything except the steps that require repository-owner credentials or
human judgement. Leave those to the human: approving and merging the release PR,
enabling Zenodo, and reading the minted DOI off Zenodo. Do the rest and stop for
review at each gate.

## The split

`.github/workflows/release.yaml` (automated, 25th of each month):

- runs `scripts/prepare_release.py`, which determines the version, diffs against
  the previous tag, writes the release body to `release-notes/vYYYY.MM.md`, and
  adds the entry to `docs/releases/index.md`,
- runs the provenance check and the strict build,
- opens `release: vYYYY.MM` from branch `release/vYYYY.MM`.

`.github/workflows/release-drift.yaml` (automated, on every push to main):

- counts what has landed on main since the open release PR was drafted and keeps
  one comment on that PR current with it,
- touches nothing else: redrafting would discard the reviewer's edits, so the
  decision to redraft stays with them.

`.github/workflows/release-tag.yaml` (automated, when the release PR merges):

- tags `vYYYY.MM` at the merge commit, so the tag is the reviewed state,
- comments the `gh release create` command on the merged PR,
- publishes nothing: Zenodo mints from a published release, not from a tag.

`.github/workflows/release-doi.yaml` (automated, on release publication):

- runs `scripts/fill_release_doi.py`, which waits for Zenodo to mint, verifies
  the deposit's version against the tag, records the DOI on the entry, and moves
  the citation example to this release,
- opens `release: record the vYYYY.MM DOI` from branch `release/vYYYY.MM-doi`.

You (agent):

- review or rewrite what the scripts cannot judge: the change summary as prose,
  the statuses, the entry date,
- prepare the tag and release commands,
- take over either script's job by hand when a workflow is off or a release is
  off-cycle.

Everything the scripts write is derived from the repository or read from Zenodo
(frontmatter, the diff, file counts, the deposit), so it is checkable. Nothing in
it is generated prose.

Human / repository owner:

- keeps the Zenodo GitHub integration enabled (one-time owner action, done),
- reviews and merges the release PR,
- creates the tag and Release (or approves you running the prepared command),
- copies the minted version DOI from Zenodo back to you.

## The citation identity is bound to this repo

Zenodo's GitHub integration binds the concept DOI to one repo owner and name.
`v2026.07` was minted from `slolab/aiforscience.eu`, so that binding exists now.
A move to a neutral organisation later splits the DOI lineage across two repos.
Raise this before any repo move, not after.

## Version scheme

Calendar versioning, monthly: `vYYYY.MM` (example: `v2026.07`). The version is
the release month, not a semver bump. Do not infer a version from commit types.

## Procedure

### Phase A: prepare (the workflow drafts it, you review, human merges)

The 25th-of-the-month workflow has usually opened the PR already. Check with
`gh pr list --search "release:" --state open`. Your work is the judgement the
script cannot make:

1. Read the PR. `uv run python scripts/prepare_release.py --dry-run` prints the
   same drafts locally without writing anything.
2. Rewrite `## What changed` in `release-notes/vYYYY.MM.md` if the month
   deserves a summary rather than a list of facts. Two to four sentences.
   Leave the practice list alone: it is generated from frontmatter.
3. Check the statuses against what the editor group actually accepted, and the
   entry date in `docs/releases/index.md` against when the tag will land.
   The script dates the entry the day it ran.
4. Read the `release-drift.yaml` comment on the PR. It lists what has landed on
   main since the drafts were written. Those commits are in the snapshot
   regardless, because the tag lands on the merge commit, so decide whether the
   notes have to account for them. Redrafting with `-f refresh=true` picks them
   up and discards any edits made on the branch, so do it before step 2, not
   after.
5. Run `uv run mkdocs build --strict` after any edit.

If there is no PR, the month had no changes, the month is already tagged, an
earlier release PR is still open, or the workflow is off. Only one release PR
may be open at a time: an untagged snapshot is not a diff base, so the next
month would be drafted against the tag before it and would re-list the open
month's changes as its own. Merge or close the earlier one first.

For an off-cycle or forced release, either run the workflow manually
(`gh workflow run release.yaml -f version=vYYYY.MM -f force=true`) or do it
yourself:

```
uv run python scripts/prepare_release.py --version vYYYY.MM --pr-body-out /tmp/pr-body.md
git checkout -b release/vYYYY.MM
git add docs/releases/index.md release-notes && git commit -m "release: prepare vYYYY.MM"
gh pr create --title "release: vYYYY.MM" --body-file /tmp/pr-body.md
```

Do not tag in this phase.

### Phase B: tag and mint (human owns; you prepare)

6. The merge tags `vYYYY.MM` on its own. The human decides when to publish the
   release, which is the act that archives the snapshot. Prepare the command for
   them to run or approve:

   ```
   git pull
   gh release create vYYYY.MM --title "vYYYY.MM" --verify-tag --notes-file release-notes/vYYYY.MM.md
   ```

   Both parts matter. `release-notes/vYYYY.MM.md` only reaches the checkout on
   `git pull`, and `--verify-tag` makes the command fail on a missing tag
   instead of creating one: without it, a `release-tag.yaml` that did not run
   means the release is cut at whatever `main` is at, not at the reviewed
   commit, and Zenodo archives that.

   `.zenodo.json` at the repo root supplies the deposit metadata; do not inline
   author or license data into the release for Zenodo's sake. If the tag needs to
   move because something merged wrong, do it before publishing: an unpublished
   tag has no deposit and no DOI depending on it.
7. Zenodo catches the release webhook and mints the DOI automatically. This is
   asynchronous. The DOI does not exist until after the release is published, so
   the tagged snapshot itself does not contain its own DOI. That is expected.
   Publishing the release also starts `release-doi.yaml`.

### Phase C: record the DOI (automated; you review the PR)

8. `release-doi.yaml` waits for the mint, then opens
   `release: record the vYYYY.MM DOI`. Check two things on that PR: the DOI
   resolves, and the version it belongs to is this release. Then the human
   merges. The concept DOI is unchanged; only the version DOI is new.
9. If that workflow did not run or Zenodo timed out, do it by hand:

   ```
   uv run python scripts/fill_release_doi.py --version vYYYY.MM
   uv run mkdocs build --strict
   ```

   The DOI is read from Zenodo, so do not ask the human for the number. Ask only
   if the deposit cannot be reached at all, and then pass `--concept-doi` or edit
   the two spots in `docs/releases/index.md` directly (the entry's DOI line and
   the citation example).

## What the scripts emit

`scripts/prepare_release.py` implements the two formats below. They are
documented here so a hand-written release matches, and so a change to one is
made in both places.

Release body (`release-notes/vYYYY.MM.md`, fed to `gh release create`):

```
## What changed

<what the diff against the previous tag shows: practices added, status moves,
endorsements, revised pages, new library entries, failures logged. Replace with
two to four sentences of summary when the month warrants it.>

## Practices in this snapshot

<one line per practice: BP-NN, title, status.>

This is a dated snapshot of the living record at https://aiforscience.eu.
The live site always shows the current state.
```

Releases page entry, under `## Past releases` in `docs/releases/index.md`,
newest first:

```
### vYYYY.MM (YYYY-MM-DD)

<ordinal snapshot, what it contains, what changed since the previous tag.>

[GitHub release](https://github.com/<owner>/aiforscience.eu/releases/tag/vYYYY.MM)
```

The owner comes from the repo's current `origin`; do not hardcode an owner that
may have changed.

`scripts/fill_release_doi.py` then turns the last line into
`DOI: [<doi>](https://doi.org/<doi>) · [GitHub release](...)` and updates the
citation example. No placeholder is ever published: an entry either has its DOI
or has no DOI line at all.

## Style (hard rules)

- Follow the writing style section of the repository CLAUDE.md exactly: no
  em-dash asides, no "not just X but Y", no inflated adjectives, short
  declarative sentences.
- Neutral coalition voice on the releases page and in the release body. The
  record speaks for its contributors collectively, never for one institution.
- A draft-stage snapshot is legitimate. The record is living and each deposit is
  a dated state, so do not gate a release on practices reaching `reviewed` or
  `endorsed`. Say plainly in the body which statuses the snapshot contains.

## Output

Report to the user: the version, the change summary, the release-body draft, the
files edited, and which gate you stopped at (PR review, tag creation, or DOI
number). Name the human step needed to proceed.
