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

You (agent):

- determine the version and the change summary,
- draft the GitHub Release body,
- update `docs/releases/index.md`,
- run the strict build,
- prepare the tag and release commands,
- fill the DOI into the two placeholder spots once the human gives you the number.

Human / repository owner:

- decides the repo's permanent home before the first DOI (see gate below),
- enables the Zenodo GitHub integration once (owner action in the Zenodo UI),
- reviews and merges the release PR,
- creates the tag and Release (or approves you running the prepared command),
- copies the minted concept DOI from Zenodo back to you.

## Gate before the first release

The first release fixes the citation identity. Zenodo's GitHub integration
binds the concept DOI to the specific repo owner and name. If the repo may move
to a neutral organisation later, that move must happen before the first DOI is
minted, or the DOI lineage splits across two repos. Do not cut the first
release until the human confirms the repo is in its permanent home. State this
gate and stop if it is unresolved.

## Version scheme

Calendar versioning, monthly: `vYYYY.MM` (example: `v2026.07`). The version is
the release month, not a semver bump. Do not infer a version from commit types.

## Procedure

### Phase A: prepare (you do this, human reviews the PR)

1. Determine the version `vYYYY.MM` from the release month the user names, or the
   current month if they do not.
2. Find the previous tag (`git tag --list 'v*' --sort=-v:refname | head -1`).
   For the first release there is none.
3. Collect what changed since the previous tag: new and reworded practices,
   status changes (`draft` -> `reviewed` -> `endorsed`), new endorsements, new
   library entries, and failures logged. Read the practice frontmatter and the
   git log for the range; write the summary for a reader, not as a commit dump.
4. Draft the GitHub Release body (see template below).
5. Update `docs/releases/index.md`:
   - On the first release, replace the "No releases yet" note with a
     `## Past releases` list.
   - Add the new entry at the top of that list, newest first, following the
     entry format below. Leave the DOI as a clearly marked slot
     (`DOI: CONCEPT_DOI` and `DOI: VERSION_DOI`) for Phase C.
   - Keep the "How to cite" block; update its example to this release.
6. Run `uv run mkdocs build --strict` and fix anything it reports.
7. Open a PR titled `release: vYYYY.MM` for editor review. Do not tag yet.

### Phase B: tag and mint (human owns; you prepare)

8. After the PR merges, the human ensures the Zenodo toggle is on (one-time) and
   creates the tag and Release from `main`. Prepare the command for them to run
   or approve:

   ```
   gh release create vYYYY.MM --title "vYYYY.MM" --notes-file <release-body>
   ```

   `.zenodo.json` at the repo root supplies the deposit metadata; do not inline
   author or license data into the release for Zenodo's sake.
9. Zenodo catches the release webhook and mints the DOI automatically. This is
   asynchronous. The DOI does not exist until after the release is published, so
   the tagged snapshot itself will not contain the filled-in DOI. That is
   expected.

### Phase C: fill the DOI (you do this, human supplies the number)

10. Ask the human for the **concept** DOI (the "all versions" DOI that resolves
    to the latest snapshot), not the version DOI. Zenodo shows it only after the
    first deposit exists.
11. Fill it into the two placeholder spots:
    - `overrides/home.html`: the DOI pill (currently `10.5281/zenodo.xxxxx`).
      Set the concept DOI and make the pill a link to
      `https://doi.org/<concept-doi>`.
    - `docs/releases/index.md`: replace `CONCEPT_DOI` in the "How to cite" block
      and `VERSION_DOI` in this release's entry with the real numbers (the
      version DOI is per-release; the concept DOI is stable across all).
12. Run `uv run mkdocs build --strict` and open a short follow-up PR for review.

## Release body template

```
## What changed

<two to four sentences: what a reader gets from this snapshot. Practices
added or reworded, status and endorsement changes, new library entries.>

## Practices in this snapshot

<one line per practice: BP-NN, title, status.>

This is a dated snapshot of the living record at https://aiforscience.eu.
The live site always shows the current state.
```

## Releases page entry format

Under `## Past releases` in `docs/releases/index.md`, newest first:

```
### vYYYY.MM (YYYY-MM-DD)

<one or two sentences on what this snapshot contains.>
DOI: VERSION_DOI · [GitHub release](https://github.com/<owner>/aiforscience.eu/releases/tag/vYYYY.MM)
```

Use the repo's current `origin` owner for the link; do not hardcode an owner
that may have changed.

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
