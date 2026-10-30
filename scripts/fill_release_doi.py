#!/usr/bin/env python3
"""Record the Zenodo version DOI of a published release on the releases page.

The version DOI does not exist until the GitHub Release is published: Zenodo
mints it from the release webhook. So `scripts/prepare_release.py` writes the
entry without a DOI, and this script adds it once the mint lands. Two edits to
`docs/releases/index.md`:

- the release entry gains `DOI: <link> · ` before its GitHub release link;
- the "How to cite" example moves to this release and its DOI.

The DOI is read from Zenodo, not passed in by hand. Requesting the concept
record follows the redirect to the latest version, and the deposit's `version`
field is the tag it was minted from, which is what proves the DOI belongs to
this release rather than the previous one. Minting is asynchronous, so the
lookup is retried until it matches or the timeout expires.

Run: `uv run python scripts/fill_release_doi.py [--version vYYYY.MM]`
Add `--dry-run` to print the edit without writing it.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

from prepare_release import RELEASES_PAGE, VERSION, emit_outputs, tags

ZENODO_API = "https://zenodo.org/api/records"
CONCEPT_DOI = re.compile(r"concept DOI \[?(10\.5281/zenodo\.(\d+))")
CITATION = "> AI for Science contributors."
USER_AGENT = "aiforscience.eu release tooling (https://aiforscience.eu)"


def concept_recid(page: str) -> tuple[str, str]:
    """(concept DOI, record id) as the releases page states them."""
    match = CONCEPT_DOI.search(page)
    if not match:
        sys.exit(
            f"no concept DOI found in {RELEASES_PAGE.name}. Pass --concept-doi."
        )
    return match.group(1), match.group(2)


def fetch_latest(recid: str) -> dict:
    request = urllib.request.Request(
        f"{ZENODO_API}/{recid}", headers={"User-Agent": USER_AGENT}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def wait_for_mint(recid: str, version: str, timeout: int, interval: int) -> str:
    """The version DOI Zenodo minted for `version`."""
    wanted = version.lstrip("v")
    deadline = time.monotonic() + timeout
    last = ""
    while True:
        try:
            record = fetch_latest(recid)
            minted = str(record.get("metadata", {}).get("version") or "")
            doi = str(record.get("doi") or "")
            if minted.lstrip("v") == wanted and doi:
                return doi
            last = f"latest deposit is {minted or 'unversioned'} ({doi or 'no DOI'})"
        except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as error:
            last = f"lookup failed: {error}"
        if time.monotonic() + interval >= deadline:
            sys.exit(
                f"Zenodo has no deposit for {version} after {timeout}s: {last}. "
                "Minting may still be in flight, or the release did not reach "
                "Zenodo. Re-run this workflow, or fill the DOI by hand."
            )
        print(f"waiting for the {version} deposit: {last}")
        time.sleep(interval)


def fill(page: str, version: str, doi: str) -> tuple[str, bool]:
    """Add the DOI to the entry and move the citation example. (page, changed)"""
    lines = page.splitlines()
    start = next(
        (i for i, l in enumerate(lines) if l.startswith(f"### {version} (")), None
    )
    if start is None:
        sys.exit(
            f"{RELEASES_PAGE.name} has no entry for {version}. The release PR "
            "for this version has to be merged first."
        )
    end = next(
        (
            i for i in range(start + 1, len(lines))
            if lines[i].startswith("### ") or lines[i].startswith("## ")
        ),
        len(lines),
    )

    link = f"[{doi}](https://doi.org/{doi})"
    changed = False
    for i in range(start, end):
        if lines[i].startswith("DOI:"):
            print(f"note: the {version} entry already records a DOI.")
            break
        if lines[i].startswith("[GitHub release]"):
            lines[i] = f"DOI: {link} · {lines[i]}"
            changed = True
            break
    else:
        sys.exit(f"the {version} entry has no GitHub release link to prefix.")

    for i, line in enumerate(lines):
        if line.startswith(CITATION):
            updated = re.sub(r"release \d{4}\.\d{2}", f"release {version[1:]}", line)
            updated = re.sub(r"DOI: \S+?\.$", f"DOI: {doi}.", updated)
            if updated != line:
                lines[i] = updated
                changed = True
            break

    return "\n".join(lines) + "\n", changed


def render_pr_body(version: str, doi: str, concept: str) -> str:
    return "\n".join(
        [
            f"Zenodo minted the version DOI for `{version}`: "
            f"[{doi}](https://doi.org/{doi}).",
            "",
            "This records it on the release entry and moves the citation "
            f"example to `{version}`. The concept DOI ({concept}) is unchanged: "
            "it resolves to the newest snapshot on its own.",
            "",
            "Prepared by `.github/workflows/release-doi.yaml` after the release "
            "was published. It reads the DOI from the Zenodo API and checks the "
            "deposit's version against the tag, so a mint still in flight "
            "cannot be recorded as this release's.",
            "",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version", help="released version vYYYY.MM (default: the newest tag)"
    )
    parser.add_argument(
        "--concept-doi",
        help="Zenodo concept DOI (default: the one on the releases page)",
    )
    parser.add_argument(
        "--timeout", type=int, default=900, help="seconds to wait for the mint"
    )
    parser.add_argument(
        "--interval", type=int, default=30, help="seconds between lookups"
    )
    parser.add_argument("--pr-body-out", help="write a pull-request body here")
    parser.add_argument(
        "--dry-run", action="store_true", help="print the edit, write nothing"
    )
    args = parser.parse_args()

    version = args.version or next(iter(tags()), None)
    if not version:
        sys.exit("no vYYYY.MM tag found; nothing has been released.")
    if not VERSION.match(version):
        sys.exit(f"version '{version}' is not vYYYY.MM")

    page = RELEASES_PAGE.read_text(encoding="utf-8")
    if f"### {version} (" not in page:  # cheap check, before any waiting
        sys.exit(
            f"{RELEASES_PAGE.name} has no entry for {version}. The release PR "
            "for this version has to be merged first."
        )
    if args.concept_doi:
        concept = args.concept_doi
        recid = concept.rsplit(".", 1)[-1]
    else:
        concept, recid = concept_recid(page)

    doi = wait_for_mint(recid, version, args.timeout, args.interval)
    updated, changed = fill(page, version, doi)

    emit_outputs(
        {"version": version, "doi": doi, "changed": "true" if changed else "false"}
    )

    if not changed:
        print(f"{version} already records {doi}; nothing to do.")
        return 0
    if args.dry_run:
        print(f"--- docs/releases/index.md ({version} -> {doi})")
        print(updated)
        return 0

    RELEASES_PAGE.write_text(updated, encoding="utf-8")
    if args.pr_body_out:
        Path(args.pr_body_out).write_text(
            render_pr_body(version, doi, concept), encoding="utf-8"
        )
    print(f"Recorded {doi} for {version} in docs/releases/index.md.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
