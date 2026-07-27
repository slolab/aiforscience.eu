"""MkDocs hook: render the provenance hover cards on practice atoms.

Each `## Practice` statement is a list of atoms, each carrying a stable id
(`bp<N>-a<k>`) on its `<li>`. `docs/assets/provenance.yml` maps each atom id to
the sources that bear on it, with a stance (supports / qualifies / contradicts)
and an optional locator. The reference metadata (title, link) lives in the
library entries (`docs/library/ref-<slug>.md` for reference works, or the
distilled-source page for the three rich documents).

This hook joins the two at build time and injects, into each atom `<li>`, a
citation marker plus a hidden card listing the for/against sources with links
into the library. No client-side fetch: the data is baked into the page. CSS
(assets/css/provenance.css) shows the card on hover or focus; a small script
(assets/js/provenance.js) pins it open on click.
"""

import html
import re
from pathlib import Path

import yaml
from mkdocs.utils import get_relative_url

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
BP_PAGE = re.compile(r"best-practices/(\d\d)-.*\.md$")

# Populated in on_config.
_PROV = {}
_REFS = {}  # ref key -> (title, src_uri under docs/)


def _load_meta(path):
    match = _FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        # A malformed library frontmatter must not break the provenance hook;
        # fall back to no metadata (the file stem is used as the title).
        return {}


def on_config(config):
    docs_dir = Path(config["docs_dir"])

    prov_path = docs_dir / "assets" / "provenance.yml"
    _PROV.clear()
    if prov_path.exists():
        _PROV.update(yaml.safe_load(prov_path.read_text(encoding="utf-8")) or {})

    _REFS.clear()
    for path in sorted((docs_dir / "library").glob("*.md")):
        if path.name == "index.md":
            continue
        meta = _load_meta(path)
        title = meta.get("title") or path.stem
        src = f"library/{path.name}"
        # Reference works join by `ref_id`; distilled sources join by page slug.
        _REFS.setdefault(path.stem, (title, src))
        if meta.get("ref_id"):
            _REFS[meta["ref_id"]] = (title, src)
    return config


def _items_html(edges, stance, page, files):
    items = []
    for edge in edges:
        if edge.get("stance") != stance:
            continue
        meta = _REFS.get(edge.get("ref"))
        if not meta:
            continue
        title, src = meta
        f = files.get_file_from_path(src)
        if f is None:
            continue
        href = get_relative_url(f.url, page.url)
        loc = edge.get("locator")
        loc_html = (
            f' <span class="afs-cite__loc">{html.escape(loc)}</span>' if loc else ""
        )
        items.append(
            f'<li class="afs-cite__item">'
            f'<a class="afs-cite__ref" href="{href}">{html.escape(title)}</a>'
            f"{loc_html}</li>"
        )
    return items


def _group_html(label, stance, items, always):
    if not items and not always:
        return ""
    if items:
        body = f'<ul class="afs-cite__list">{"".join(items)}</ul>'
    else:
        body = '<span class="afs-cite__empty">None recorded</span>'
    return (
        f'<div class="afs-cite__group afs-cite__group--{stance}">'
        f'<span class="afs-cite__label">{label}</span>{body}</div>'
    )


def _card_html(atom_id, edges, page, files):
    fors = _items_html(edges, "supports", page, files)
    quals = _items_html(edges, "qualifies", page, files)
    againsts = _items_html(edges, "contradicts", page, files)
    if not (fors or quals or againsts):
        return None

    groups = (
        _group_html("For", "supports", fors, always=True)
        + _group_html("Qualifies", "qualifies", quals, always=False)
        + _group_html("Against", "contradicts", againsts, always=True)
    )
    n_for, n_against = len(fors), len(againsts)
    return (
        f'<span class="afs-cite" data-atom="{atom_id}">'
        f'<button class="afs-cite__toggle" type="button" aria-expanded="false" '
        f'aria-label="{n_for} for, {n_against} against">'
        f'<span class="afs-cite__n afs-cite__n--for">{n_for}</span>'
        f'<span class="afs-cite__sep">·</span>'
        f'<span class="afs-cite__n afs-cite__n--against">{n_against}</span>'
        f"</button>"
        f'<span class="afs-cite__card" role="group">{groups}</span>'
        f"</span>"
    )


def on_page_content(html_out, page, config, files):
    if not BP_PAGE.match(page.file.src_uri):
        return html_out
    for atom_id, edges in _PROV.items():
        if f'id="{atom_id}"' not in html_out:
            continue
        card = _card_html(atom_id, edges, page, files)
        if not card:
            continue
        pattern = re.compile(
            r'(<li\b[^>]*\bid="' + re.escape(atom_id) + r'"[^>]*>)(.*?)(</li>)',
            re.DOTALL,
        )
        html_out = pattern.sub(
            lambda m: m.group(1) + m.group(2) + card + m.group(3), html_out, count=1
        )
    return html_out
