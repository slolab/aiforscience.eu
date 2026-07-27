#!/usr/bin/env python3
"""Validate provenance integrity so the hover-card join cannot fail silently.

`hooks/provenance.py` joins `docs/assets/provenance.yml` to the library entries
by ref key and drops any edge whose ref does not resolve, whose stance is
unrecognised, or whose atom id never appears on a best-practice page. Those
drops produce a green build with a missing citation. This script turns each of
those silent drops into a hard error, mirroring the hook's join semantics:

- valid ref  = a library page slug (file stem under docs/library/) or a
               `ref_id` declared in a library entry's frontmatter;
- valid atom = an id `bp<N>-a<k>` that appears as `{ #bp<N>-a<k> }` on a
               best-practice page;
- valid stance = supports | qualifies | contradicts.

It also checks that every `sources:` entry in a best-practice page points to a
file that exists. Run: `uv run python scripts/check_provenance.py`.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
LIBRARY = DOCS / "library"
BP_DIR = DOCS / "best-practices"
PROV_PATH = DOCS / "assets" / "provenance.yml"

FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ATOM_ID = re.compile(r"\{[^}]*#(bp\d+-a\d+)[^}]*\}")
ATOM_KEY = re.compile(r"^bp\d+-a\d+$")
STANCES = {"supports", "qualifies", "contradicts"}


def load_frontmatter(path: Path) -> dict:
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        return {}


def valid_refs() -> set[str]:
    """Every key the hook would accept: library page slugs and ref_ids."""
    refs: set[str] = set()
    for path in sorted(LIBRARY.glob("*.md")):
        if path.name == "index.md":
            continue
        refs.add(path.stem)
        ref_id = load_frontmatter(path).get("ref_id")
        if ref_id:
            refs.add(str(ref_id))
    return refs


def page_atom_ids() -> set[str]:
    """Every atom id declared on a best-practice page."""
    ids: set[str] = set()
    for path in sorted(BP_DIR.glob("*.md")):
        ids.update(ATOM_ID.findall(path.read_text(encoding="utf-8")))
    return ids


def check_provenance(errors: list[str]) -> None:
    if not PROV_PATH.exists():
        errors.append(f"{PROV_PATH} not found")
        return
    data = yaml.safe_load(PROV_PATH.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        errors.append("provenance.yml must be a mapping of atom id to edges")
        return

    refs = valid_refs()
    atoms = page_atom_ids()

    for atom_id, edges in data.items():
        if not ATOM_KEY.match(str(atom_id)):
            errors.append(f"provenance key '{atom_id}' is not a bp<N>-a<k> id")
            continue
        if atom_id not in atoms:
            errors.append(
                f"atom '{atom_id}' has provenance but no {{ #{atom_id} }} on any "
                f"best-practice page (card would never render)"
            )
        if not isinstance(edges, list):
            errors.append(f"atom '{atom_id}': edges must be a list")
            continue
        for i, edge in enumerate(edges):
            where = f"atom '{atom_id}' edge {i}"
            if not isinstance(edge, dict):
                errors.append(f"{where}: not a mapping")
                continue
            ref = edge.get("ref")
            stance = edge.get("stance")
            if not ref:
                errors.append(f"{where}: missing 'ref'")
            elif ref not in refs:
                errors.append(
                    f"{where}: ref '{ref}' resolves to no library entry "
                    f"(slug or ref_id); citation would be dropped"
                )
            if stance not in STANCES:
                errors.append(
                    f"{where}: stance '{stance}' not in {sorted(STANCES)}"
                )


def check_page_sources(errors: list[str]) -> None:
    for path in sorted(BP_DIR.glob("*.md")):
        for src in load_frontmatter(path).get("sources", []) or []:
            ref = src.get("ref") if isinstance(src, dict) else None
            if not ref or "://" in str(ref):
                continue  # URL sources are checked by the link checker
            if not (DOCS / ref).exists():
                errors.append(
                    f"{path.name}: source ref '{ref}' points to a missing file"
                )


def main() -> int:
    errors: list[str] = []
    check_provenance(errors)
    check_page_sources(errors)
    if errors:
        print(f"Provenance check failed with {len(errors)} error(s):\n")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("Provenance check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
