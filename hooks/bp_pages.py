"""MkDocs hook: keep best-practice titles spelled once.

Each best-practice title lives only in the BP page's frontmatter. This hook
renders two things from it, so no literal copy is kept in page bodies:

- Each BP page's H1: the `<!-- BP_TITLE -->` placeholder becomes a
  "Best practice N" kicker plus the title as the page lead.
- Each BP page's sidebar nav label: from the page's frontmatter `nav_title`,
  so the short label lives in the page, not in mkdocs.yml.

No new dependency: PyYAML ships with MkDocs, and `hooks` is built in.
"""

import re
from pathlib import Path

import yaml

TITLE_PLACEHOLDER = "<!-- BP_TITLE -->"
SOURCES_PLACEHOLDER = "<!-- BP_SOURCES -->"
BP_PAGE = re.compile(r"best-practices/(\d\d)-.*\.md$")

_FRONTMATTER = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def _load_meta(path):
    match = _FRONTMATTER.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(match.group(1)) if match else {}


def _render_sources(sources):
    source_list = '## Sources\n'
    for sc in sources:
        source_list = source_list + f'- [{sc["title"]}](../{sc["ref"]}). {sc["note"]}\n'
    return(source_list)


def on_page_markdown(markdown, page, config, files):
    match = BP_PAGE.match(page.file.src_uri)
    if not match:
        return markdown
    if TITLE_PLACEHOLDER in markdown:
        title = page.meta.get("title", "")
        # Title as the lead: a quiet "Best practice N" kicker above the title,
        # and the title itself as the H1 (styled small in home.css).
        kicker = f'<p class="afs-bp-kicker">Best practice {int(match.group(1))}</p>'
        # TITLE_PLACEHOLDER
        markdown = markdown.replace(TITLE_PLACEHOLDER, f"{kicker}\n\n# {title}")
        # SOURCES_PLACEHOLDER
        return markdown.replace(SOURCES_PLACEHOLDER, _render_sources(page.meta.get("sources", [])))
    return markdown


def on_nav(nav, config, files):
    # Set each BP page's sidebar label from its frontmatter `nav_title`. Runs
    # before pages are read, so read the frontmatter from disk. Leaving the nav
    # entry untitled in mkdocs.yml keeps page.title None here, so this set sticks
    # (MkDocs only fills an unset title from meta/H1 afterwards).
    docs_dir = Path(config["docs_dir"])
    for page in nav.pages:
        if BP_PAGE.match(page.file.src_uri):
            label = _load_meta(docs_dir / page.file.src_uri).get("nav_title")
            if label:
                page.title = label
    return nav
