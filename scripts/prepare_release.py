#!/usr/bin/env python3
"""Prepare a dated monthly release for review: draft the release body and
update the releases page.

This is the mechanical half of the `release` skill's Phase A. Everything it
writes is checkable from the repository itself: the version from the release
month, the practice list and statuses from frontmatter, the changes from the
diff against the previous tag, the library and failure counts from the files.
Nothing is tagged and nothing is published. The prose is a factual summary; a
reviewer edits it on the release branch if the snapshot deserves a narrative.

Outputs:

- `release-notes/vYYYY.MM.md`, the GitHub Release body (outside `docs/`, so it
  is not part of the built site), used later as `gh release create
  --notes-file`;
- an entry at the top of `## Past releases` in `docs/releases/index.md`, without
  a DOI. Zenodo mints the version DOI from the published release, which does not
  exist yet, so `scripts/fill_release_doi.py` adds that line afterwards;
- optionally a pull-request body (`--pr-body-out`).

Run: `uv run python scripts/prepare_release.py [--version vYYYY.MM]`
Add `--dry-run` to print the drafts without touching any file.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
BP_DIR = DOCS / "best-practices"
LIB_DIR = DOCS / "library"
RELEASES_PAGE = DOCS / "releases" / "index.md"
NOTES_DIR = REPO / "release-notes"

BP_PREFIX = "docs/best-practices"
LIB_PREFIX = "docs/library"
FAILURES_PATH = f"{BP_PREFIX}/failures.md"

FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
PRACTICE_FILE = re.compile(r"^\d\d-.+\.md$")
FAILURE_ENTRY = re.compile(r"^- \*\*\d{4}-\d{2}\*\*", re.MULTILINE)
VERSION = re.compile(r"^v(\d{4})\.(\d{2})$")
PAST_RELEASES = "## Past releases"

WORDS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve",
}
ORDINALS = {
    1: "First", 2: "Second", 3: "Third", 4: "Fourth", 5: "Fifth", 6: "Sixth",
    7: "Seventh", 8: "Eighth", 9: "Ninth", 10: "Tenth", 11: "Eleventh",
    12: "Twelfth",
}
STATUS_ORDER = ["draft", "reviewed", "endorsed"]


# --------------------------------------------------------------------------- #
# words
# --------------------------------------------------------------------------- #

def num(n: int) -> str:
    return WORDS.get(n, str(n))


def Num(n: int) -> str:  # noqa: N802 - sentence-initial form
    word = num(n)
    return word[0].upper() + word[1:]


def plural(n: int, word: str) -> str:
    return word if n == 1 else f"{word}s"


def ordinal(n: int) -> str:
    if n in ORDINALS:
        return ORDINALS[n]
    suffix = "th" if 11 <= n % 100 <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


def join_and(items: list[str]) -> str:
    items = [i for i in items if i]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return f"{', '.join(items[:-1])} and {items[-1]}"


# --------------------------------------------------------------------------- #
# git
# --------------------------------------------------------------------------- #

def git(*args: str, check: bool = True) -> str:
    proc = subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True
    )
    if check and proc.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed: {proc.stderr.strip()}")
    return proc.stdout


def git_show(rev: str, path: str) -> str | None:
    proc = subprocess.run(
        ["git", "show", f"{rev}:{path}"], cwd=REPO, capture_output=True, text=True
    )
    return proc.stdout if proc.returncode == 0 else None


def ls_tree(rev: str, prefix: str) -> list[str]:
    out = git("ls-tree", "-r", "--name-only", rev, "--", prefix, check=False)
    return [line for line in out.splitlines() if line.strip()]


def tags() -> list[str]:
    out = git("tag", "--list", "v*", "--sort=-v:refname", check=False)
    return [t for t in out.splitlines() if VERSION.match(t)]


def tag_exists(version: str) -> bool:
    proc = subprocess.run(
        ["git", "rev-parse", "-q", "--verify", f"refs/tags/{version}"],
        cwd=REPO, capture_output=True, text=True,
    )
    return proc.returncode == 0


def repo_slug() -> str:
    """owner/name from origin, so links follow the repo if it moves."""
    url = git("remote", "get-url", "origin", check=False).strip()
    match = re.search(r"github\.com[:/](?P<slug>[^/]+/[^/]+?)(?:\.git)?$", url)
    return match.group("slug") if match else "slolab/aiforscience.eu"


# --------------------------------------------------------------------------- #
# reading the record
# --------------------------------------------------------------------------- #

@dataclass
class Practice:
    pid: str
    title: str
    status: str
    endorsed_by: list[str] = field(default_factory=list)
    path: str = ""


def parse_practice(path: str, text: str) -> Practice | None:
    match = FRONTMATTER.match(text)
    if not match:
        return None
    try:
        fm = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return None
    pid = str(fm.get("practice_id") or "").strip()
    if not pid:
        return None
    endorsed = fm.get("endorsed_by") or []
    if isinstance(endorsed, str):
        endorsed = [endorsed]
    return Practice(
        pid=pid,
        title=str(fm.get("nav_title") or fm.get("title") or "").strip(),
        status=str(fm.get("status") or "unknown").strip(),
        endorsed_by=[str(e).strip() for e in endorsed if str(e).strip()],
        path=path,
    )


def practices_at(rev: str | None) -> dict[str, Practice]:
    """Practices keyed by practice_id. `rev=None` reads the working tree."""
    found: dict[str, Practice] = {}
    if rev is None:
        paths = [
            f"{BP_PREFIX}/{p.name}"
            for p in sorted(BP_DIR.glob("*.md"))
            if PRACTICE_FILE.match(p.name)
        ]
        texts = {p: (REPO / p).read_text(encoding="utf-8") for p in paths}
    else:
        paths = [
            p for p in ls_tree(rev, BP_PREFIX)
            if PRACTICE_FILE.match(Path(p).name)
        ]
        texts = {p: git_show(rev, p) or "" for p in paths}
    for path, text in texts.items():
        practice = parse_practice(path, text)
        if practice:
            found[practice.pid] = practice
    return found


def library_at(rev: str | None) -> tuple[set[str], set[str]]:
    """(distilled source slugs, reference work slugs)."""
    if rev is None:
        names = [p.name for p in sorted(LIB_DIR.glob("*.md"))]
    else:
        names = [Path(p).name for p in ls_tree(rev, LIB_PREFIX) if p.endswith(".md")]
    slugs = {n[:-3] for n in names if n != "index.md"}
    return {s for s in slugs if not s.startswith("ref-")}, {
        s for s in slugs if s.startswith("ref-")
    }


def failures_at(rev: str | None) -> int:
    if rev is None:
        text = (REPO / FAILURES_PATH).read_text(encoding="utf-8")
    else:
        text = git_show(rev, FAILURES_PATH) or ""
    return len(FAILURE_ENTRY.findall(text))


# --------------------------------------------------------------------------- #
# what changed
# --------------------------------------------------------------------------- #

@dataclass
class Changes:
    previous: str | None
    added: list[Practice] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    status_moves: list[tuple[str, str, str]] = field(default_factory=list)
    endorsements: list[tuple[str, list[str]]] = field(default_factory=list)
    revised: list[str] = field(default_factory=list)
    distilled_added: list[str] = field(default_factory=list)
    refs_added: list[str] = field(default_factory=list)
    failures_added: int = 0
    other_pages: list[str] = field(default_factory=list)

    @property
    def any(self) -> bool:
        return bool(
            self.added or self.removed or self.status_moves or self.endorsements
            or self.revised or self.distilled_added or self.refs_added
            or self.failures_added or self.other_pages
        )


def collect_changes(previous: str | None, current: dict[str, Practice]) -> Changes:
    changes = Changes(previous=previous)
    if previous is None:
        return changes

    before = practices_at(previous)
    changes.added = [current[p] for p in sorted(set(current) - set(before))]
    changes.removed = sorted(set(before) - set(current))

    for pid in sorted(set(current) & set(before)):
        old, new = before[pid], current[pid]
        if old.status != new.status:
            changes.status_moves.append((pid, old.status, new.status))
        gained = [e for e in new.endorsed_by if e not in old.endorsed_by]
        if gained:
            changes.endorsements.append((pid, gained))

    # Any other edit to a practice page. Compares the working tree to the tag,
    # so a local run sees uncommitted edits too.
    touched = git("diff", "--name-only", previous, "--", BP_PREFIX, check=False)
    added_paths = {p.path for p in changes.added}
    by_path = {p.path: p.pid for p in current.values()}
    changes.revised = sorted(
        {
            by_path[path]
            for path in touched.splitlines()
            if path in by_path and path not in added_paths
        }
    )

    distilled_before, refs_before = library_at(previous)
    distilled_now, refs_now = library_at(None)
    changes.distilled_added = sorted(distilled_now - distilled_before)
    changes.refs_added = sorted(refs_now - refs_before)

    changes.failures_added = max(0, failures_at(None) - failures_at(previous))

    # Pages outside the practices and the library still change what a reader
    # gets from the snapshot, so a month that only touched them is still a
    # release. Generated data and the releases page itself do not count.
    skip = (f"{BP_PREFIX}/", f"{LIB_PREFIX}/", "docs/assets/", "docs/releases/")
    other = git("diff", "--name-only", previous, "--", "docs", check=False)
    changes.other_pages = sorted(
        {
            path[len("docs/"):-len(".md")]
            for path in other.splitlines()
            if path.endswith(".md") and not path.startswith(skip)
        }
    )
    return changes


def change_sentences(changes: Changes) -> list[str]:
    """One factual sentence per kind of change, most significant first."""
    if changes.previous is None:
        return []
    lines: list[str] = []

    if changes.added:
        listed = ", ".join(f"{p.pid} {p.title}" for p in changes.added)
        n = len(changes.added)
        lines.append(f"{Num(n)} {plural(n, 'practice')} added: {listed}.")
    if changes.removed:
        n = len(changes.removed)
        lines.append(
            f"{Num(n)} {plural(n, 'practice')} withdrawn: "
            f"{join_and(changes.removed)}."
        )

    moves: dict[tuple[str, str], list[str]] = {}
    for pid, old, new in changes.status_moves:
        moves.setdefault((old, new), []).append(pid)
    for (old, new), pids in moves.items():
        lines.append(f"{join_and(pids)} moved from {old} to {new}.")

    for pid, orgs in changes.endorsements:
        lines.append(f"{pid} endorsed by {join_and(orgs)}.")

    if changes.revised:
        n = len(changes.revised)
        lines.append(
            f"{Num(n)} {plural(n, 'practice')} revised: "
            f"{', '.join(changes.revised)}."
        )

    library = []
    if changes.distilled_added:
        n = len(changes.distilled_added)
        library.append(f"{num(n)} distilled {plural(n, 'source')}")
    if changes.refs_added:
        n = len(changes.refs_added)
        library.append(f"{num(n)} reference {plural(n, 'work')}")
    if library:
        lines.append(f"Library: {join_and(library)} added.")

    if changes.failures_added:
        n = changes.failures_added
        lines.append(f"{Num(n)} {plural(n, 'failure')} logged.")

    if changes.other_pages:
        lines.append(f"Also updated: {join_and(changes.other_pages)}.")

    if not lines:
        lines.append(f"No changes to the record since {changes.previous}.")
    return lines


# --------------------------------------------------------------------------- #
# drafts
# --------------------------------------------------------------------------- #

def status_counts(practices: dict[str, Practice]) -> list[tuple[str, int]]:
    counts: dict[str, int] = {}
    for practice in practices.values():
        counts[practice.status] = counts.get(practice.status, 0) + 1
    return sorted(
        counts.items(),
        key=lambda kv: (
            STATUS_ORDER.index(kv[0]) if kv[0] in STATUS_ORDER else len(STATUS_ORDER),
            kv[0],
        ),
    )


def contents_sentence(practices: dict[str, Practice]) -> str:
    total = len(practices)
    counts = status_counts(practices)
    if len(counts) == 1:
        status = f"all at `{counts[0][0]}` status"
    else:
        status = join_and([f"{num(c)} at `{s}`" for s, c in counts])
    distilled, refs = library_at(None)
    return (
        f"{Num(total)} {plural(total, 'practice')}, {status}, with the failures "
        f"log and the library that grounds them: {num(len(distilled))} distilled "
        f"{plural(len(distilled), 'source')} and {num(len(refs))} reference "
        f"{plural(len(refs), 'work')}."
    )


def practice_list(practices: dict[str, Practice]) -> list[str]:
    return [
        f"- **{p.pid}** {p.title} ({p.status})"
        for p in sorted(practices.values(), key=lambda p: p.pid)
    ]


def render_notes(practices: dict[str, Practice], changes: Changes) -> str:
    if changes.previous is None:
        summary = ["First dated snapshot of the record.", contents_sentence(practices)]
    else:
        summary = change_sentences(changes)
    return "\n".join(
        [
            "## What changed",
            "",
            *summary,
            "",
            "## Practices in this snapshot",
            "",
            *practice_list(practices),
            "",
            "This is a dated snapshot of the living record at https://aiforscience.eu.",
            "The live site always shows the current state.",
            "",
        ]
    )


def render_entry(
    version: str,
    entry_date: date,
    practices: dict[str, Practice],
    changes: Changes,
    index: int,
    slug: str,
) -> list[str]:
    lines = [
        f"### {version} ({entry_date.isoformat()})",
        "",
        f"{ordinal(index)} dated snapshot.",
        contents_sentence(practices),
    ]
    endorsed = [
        f"{p.pid} ({join_and(p.endorsed_by)})"
        for p in sorted(practices.values(), key=lambda p: p.pid)
        if p.endorsed_by
    ]
    if endorsed:
        lines.append(f"Endorsed: {'; '.join(endorsed)}.")
    elif changes.previous is None:
        lines.append("No endorsements yet.")
    sentences = change_sentences(changes)
    if sentences:
        lines.append(" ".join(sentences[:2]))
    # No DOI line. Zenodo mints the version DOI from the published release, so
    # it cannot exist while this PR is open, and a placeholder here would go
    # live on merge. `scripts/fill_release_doi.py` prepends it afterwards.
    lines += [
        "",
        f"[GitHub release](https://github.com/{slug}/releases/tag/{version})",
    ]
    return lines


def update_releases_page(text: str, version: str, entry: list[str]) -> str:
    lines = text.splitlines()
    heading = f"### {version} ("

    start = next((i for i, l in enumerate(lines) if l.startswith(heading)), None)
    if start is not None:  # rerun: replace the entry we wrote before
        end = next(
            (
                i for i in range(start + 1, len(lines))
                if lines[i].startswith("### ") or lines[i].startswith("## ")
            ),
            len(lines),
        )
        while end > start and lines[end - 1].strip() == "":
            end -= 1
        lines[start:end] = entry
    else:
        anchor = next(
            (i for i, l in enumerate(lines) if l.strip() == PAST_RELEASES), None
        )
        if anchor is None:
            sys.exit(
                f"{RELEASES_PAGE.relative_to(REPO)} has no '{PAST_RELEASES}' "
                "heading; add it before preparing a release."
            )
        insert = anchor + 1
        while insert < len(lines) and lines[insert].strip() == "":
            insert += 1
        lines[insert:insert] = entry + [""]

    # The citation example keeps pointing at the previous release until this
    # one has a DOI. Accurate is better than pointing at a DOI that does not
    # exist yet; `scripts/fill_release_doi.py` moves it on.
    return "\n".join(lines) + "\n"


def render_pr_body(
    version: str, previous: str | None, notes_path: str, notes: str, slug: str
) -> str:
    prev = previous or "no previous tag"
    return "\n".join(
        [
            f"Prepared by `.github/workflows/release.yaml`. Version `{version}` "
            f"(previous: {prev}). Nothing is tagged and nothing is published yet.",
            "",
            "The drafts below are assembled from the diff against the previous "
            "tag and from practice frontmatter. They state facts, not a "
            "narrative. Edit them on this branch if the snapshot deserves one.",
            "",
            "## Review",
            "",
            f"- [ ] `## What changed` in `{notes_path}` reads as a summary of "
            "this snapshot.",
            "- [ ] The statuses in the practice list match what the editor "
            "group accepted.",
            "- [ ] The `docs/releases/index.md` entry says what the snapshot "
            "contains. Its date is the day this PR was prepared: correct it if "
            "the merge will land on another day.",
            "- [ ] Nothing else merged since this PR was prepared. The tag "
            "lands on the merge commit, so anything merged in between is in "
            "the snapshot without being in these notes. To redraft: "
            f"`gh workflow run release.yaml -f version={version} "
            "-f refresh=true` (this replaces edits made on the branch).",
            "",
            "## After merge",
            "",
            f"`release-tag.yaml` tags `{version}` at the merge commit, so the "
            "tag is exactly what was reviewed here. Tagging is not publishing: "
            "the release is yours to publish when you want it archived.",
            "",
            "```",
            f'gh release create {version} --title "{version}" '
            f"--notes-file {notes_path}",
            "```",
            "",
            "That publication is what makes Zenodo mint the version DOI. The "
            "entry above carries no DOI yet, because the DOI does not exist "
            "until the release does. `release-doi.yaml` waits for the mint and "
            "opens a second, one-line PR that adds it and moves the citation "
            "example on.",
            "",
            "<details>",
            "<summary>Release body draft</summary>",
            "",
            notes,
            "</details>",
            "",
        ]
    )


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def emit_outputs(values: dict[str, str]) -> None:
    path = os.environ.get("GITHUB_OUTPUT")
    if not path:
        return
    with open(path, "a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--version", help="release version vYYYY.MM (default: the current month)"
    )
    parser.add_argument(
        "--previous", help="tag to diff against (default: the newest other tag)"
    )
    parser.add_argument(
        "--date", help="date for the releases-page entry (default: today, UTC)"
    )
    parser.add_argument("--pr-body-out", help="write a pull-request body here")
    parser.add_argument(
        "--dry-run", action="store_true", help="print the drafts, write nothing"
    )
    args = parser.parse_args()

    today = (
        date.fromisoformat(args.date)
        if args.date
        else datetime.now(timezone.utc).date()
    )
    version = args.version or f"v{today.year}.{today.month:02d}"
    if not VERSION.match(version):
        sys.exit(f"version '{version}' is not vYYYY.MM")

    existing = tag_exists(version)
    previous = args.previous or next((t for t in tags() if t != version), None)
    index = len([t for t in tags() if t != version]) + 1
    slug = repo_slug()

    practices = practices_at(None)
    if not practices:
        sys.exit(f"no practices found under {BP_PREFIX}")
    changes = collect_changes(previous, practices)

    notes = render_notes(practices, changes)
    notes_path = f"release-notes/{version}.md"
    entry = render_entry(version, today, practices, changes, index, slug)
    page = update_releases_page(
        RELEASES_PAGE.read_text(encoding="utf-8"), version, entry
    )

    emit_outputs(
        {
            "version": version,
            "previous": previous or "",
            "notes_path": notes_path,
            "changed": "true" if changes.any else "false",
            "tag_exists": "true" if existing else "false",
            "proceed": "true" if changes.any and not existing else "false",
        }
    )

    if existing:
        print(f"note: tag {version} already exists; this snapshot was cut already.")
    if not changes.any and previous:
        print(f"note: nothing changed since {previous}.")

    if args.dry_run:
        print(f"--- {notes_path}\n{notes}")
        print("--- docs/releases/index.md entry\n" + "\n".join(entry))
        return 0

    NOTES_DIR.mkdir(exist_ok=True)
    (NOTES_DIR / f"{version}.md").write_text(notes, encoding="utf-8")
    RELEASES_PAGE.write_text(page, encoding="utf-8")
    if args.pr_body_out:
        Path(args.pr_body_out).write_text(
            render_pr_body(version, previous, notes_path, notes, slug),
            encoding="utf-8",
        )

    print(f"Wrote {notes_path} and updated docs/releases/index.md for {version}.")
    for sentence in change_sentences(changes) or ["First dated snapshot."]:
        print(f"  {sentence}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
