"""MkDocs hook: publish the record in AI-readable form.

Non-technical readers cannot run an MCP server, and this site hosts no chatbot.
So the record is emitted at build time in the shapes assistants already read,
and the "Ask your own assistant" block on the short version points a reader's
own ChatGPT or Claude at them:

- ``/llms.txt``      a grouped index of the pages, per the llms.txt convention;
- ``/llms-full.txt`` the whole record in one file, for an assistant to ingest;
- ``<page>.md``      a Markdown mirror beside each page's HTML, so an assistant
                     (or the "Copy as Markdown" button) can fetch one page.

No new dependency and no runtime service: the files are static, generated from
the Markdown MkDocs already has. Register this hook after the others in
mkdocs.yml so the Markdown it captures is the same text the pages render from
(for example with BP titles already substituted by hooks/bp_pages.py).
"""

import re
from pathlib import Path

# Accumulated in on_page_markdown, written in on_post_build. Cleared per build
# so `mkdocs serve` rebuilds do not stack duplicates.
_PAGES = []

# Friendly labels for the top-level section a page sits in. Anything else falls
# back to the directory name, or "Pages" for files at the docs root.
_SECTION_LABELS = {
    "short-version": "The short version",
    "best-practices": "Best practices",
    "library": "Library",
    "about": "About",
    "releases": "Releases",
}
_SECTION_ORDER = [
    "short-version",
    "best-practices",
    "library",
    "about",
    "releases",
]

# Lines to skip when guessing a one-line description for the index.
_SKIP_PREFIX = ("#", "<", "!!!", "===", "---", "{", "|", "- ", "* ", ">")


def on_config(config):
    _PAGES.clear()
    return config


def _title(page):
    return page.meta.get("title") or page.title or page.file.src_uri


def _section(src_uri):
    head, sep, _ = src_uri.partition("/")
    return head if sep else ""


def _md_path(dest_path):
    dest = dest_path.replace("\\", "/")
    return dest[:-5] + ".md" if dest.endswith(".html") else dest + ".md"


def _summary(markdown):
    for line in markdown.splitlines():
        s = line.strip()
        if not s or s.startswith(_SKIP_PREFIX):
            continue
        # Drop inline link syntax and stray markup, keep the prose.
        s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
        s = re.sub(r"[*`]", "", s)
        s = re.sub(r"\s+", " ", s).strip()
        if s:
            return s[:200]
    return ""


def on_page_markdown(markdown, page, config, files):
    _PAGES.append(
        {
            "title": _title(page),
            "url": page.url,
            "md_path": _md_path(page.file.dest_path),
            "section": _section(page.file.src_uri),
            "src": page.file.src_uri,
            "markdown": markdown,
        }
    )
    return markdown


def _ordered_sections():
    present = {p["section"] for p in _PAGES}
    known = [s for s in _SECTION_ORDER if s in present]
    rest = sorted(present - set(_SECTION_ORDER))
    return known + rest


def on_post_build(config):
    site_dir = Path(config["site_dir"])
    site_url = (config.get("site_url") or "").rstrip("/")
    site_name = config.get("site_name", "")
    site_desc = (config.get("site_description") or "").strip()

    def abs_url(rel):
        return f"{site_url}/{rel}" if site_url else "/" + rel

    # Per-page Markdown mirrors.
    for p in _PAGES:
        out = site_dir / p["md_path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(p["markdown"], encoding="utf-8")

    pages_by_section = {}
    for p in _PAGES:
        pages_by_section.setdefault(p["section"], []).append(p)

    # llms.txt: an index of the record, linking to the Markdown mirrors.
    lines = [f"# {site_name}", ""]
    if site_desc:
        lines += [f"> {site_desc}", ""]
    lines += [
        f"The full record in one file is at {abs_url('llms-full.txt')}. "
        "Each link below points to a single page's Markdown source.",
        "",
    ]
    for section in _ordered_sections():
        label = _SECTION_LABELS.get(section, section or "Pages")
        lines.append(f"## {label}")
        for p in sorted(pages_by_section[section], key=lambda x: x["src"]):
            desc = _summary(p["markdown"])
            entry = f"- [{p['title']}]({abs_url(p['md_path'])})"
            lines.append(f"{entry}: {desc}" if desc else entry)
        lines.append("")
    (site_dir / "llms.txt").write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    # llms-full.txt: the whole record concatenated, in section order.
    full = [f"# {site_name}", ""]
    if site_desc:
        full += [f"> {site_desc}", ""]
    for section in _ordered_sections():
        for p in sorted(pages_by_section[section], key=lambda x: x["src"]):
            full += [
                "",
                "---",
                "",
                f"# {p['title']}",
                f"Source: {abs_url(p['md_path'])}",
                "",
                p["markdown"].strip(),
            ]
    (site_dir / "llms-full.txt").write_text("\n".join(full).rstrip() + "\n", encoding="utf-8")
