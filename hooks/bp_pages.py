"""MkDocs hook: keep best-practice titles spelled once.

Each best-practice title lives only in the BP page's frontmatter `title`. This
hook renders two things from it, so no literal copy is kept in page bodies:

- The overview list (best-practices/index.md): the `<!-- BP_LIST -->`
  placeholder becomes clickable boxes, one per BP page, ordered by filename.
- Each BP page's H1: the `<!-- BP_TITLE -->` placeholder becomes
  `# BPn: <title>`.
- Each BP page's sidebar nav label: from the page's frontmatter `nav_title`,
  so the short label lives in the page, not in mkdocs.yml.

The BPn handle comes from the numeric filename prefix. No new dependency:
PyYAML ships with MkDocs, and `hooks` is built in.
"""

import re
from pathlib import Path

import yaml

OVERVIEW = "best-practices/index.md"
LIST_PLACEHOLDER = "<!-- BP_LIST -->"
TITLE_PLACEHOLDER = "<!-- BP_TITLE -->"
BP_GLOB = "best-practices/[0-9][0-9]-*.md"
BP_PAGE = re.compile(r"best-practices/(\d\d)-.*\.md$")

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _load_meta(path):
    match = _FRONTMATTER.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(match.group(1)) if match else {}


def _handle(num):
    return f"BP{num.lstrip('0') or '0'}"


def _render_list(markdown, config):
    docs_dir = Path(config["docs_dir"])
    items = []
    for src in sorted(docs_dir.glob(BP_GLOB)):
        title = _load_meta(src).get("title")
        if not title:
            continue
        num = src.stem.split("-", 1)[0]
        items.append(
            f'<a class="afs-bp-item" href="{src.stem}/">'
            f'<span class="afs-bp-item__handle">{_handle(num)}</span>'
            f'<span class="afs-bp-item__title">{title}</span></a>'
        )
    block = '<div class="afs-bp-list" markdown>\n\n' + "\n".join(items) + "\n\n</div>"
    return markdown.replace(LIST_PLACEHOLDER, block)


def on_page_markdown(markdown, page, config, files):
    src = page.file.src_uri
    if src == OVERVIEW and LIST_PLACEHOLDER in markdown:
        return _render_list(markdown, config)

    match = BP_PAGE.match(src)
    if match and TITLE_PLACEHOLDER in markdown:
        title = page.meta.get("title", "")
        return markdown.replace(TITLE_PLACEHOLDER, f"# {_handle(match.group(1))}: {title}")

    return markdown


def on_nav(nav, config, files):
    # Set each BP page's sidebar label from its frontmatter `nav_title`. Runs
    # before pages are read, so read the frontmatter from disk. Leaving the
    # nav entry untitled in mkdocs.yml keeps page.title None here, so this set
    # sticks (MkDocs only fills an unset title from meta/H1 afterwards).
    docs_dir = Path(config["docs_dir"])
    for page in nav.pages:
        if BP_PAGE.match(page.file.src_uri):
            label = _load_meta(docs_dir / page.file.src_uri).get("nav_title")
            if label:
                page.title = label
    return nav
