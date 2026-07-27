"""MkDocs hook: hover cards on glossary links.

Every link that points at a glossary anchor (`.../glossary/#<id>`) gets a small
definition card, so a reader can see what a term means without leaving the page.
The link itself is untouched and stays clickable; the card is baked into the
HTML at build time (no client-side fetch), mirroring the provenance cards
(hooks/provenance.py). CSS (assets/css/glossary.css) reveals it on hover/focus.

Definitions are parsed once from docs/glossary.md, which is a Markdown
definition list where each term carries a stable id via attr_list
(`Term { #id }`). The glossary page itself is skipped: its links are same-page
jumps and the definition is already right there.
"""

import html
import re
from pathlib import Path

# `Term { #id }` on its own line, immediately above a `:` definition line.
_TERM = re.compile(r"^(?P<term>.+?)\s*\{\s*#(?P<id>[a-z0-9-]+)\s*\}\s*$")
# `[text](url)` -> keep the link text only (targets would be wrong off-page).
_LINK = re.compile(r"\[([^\]]+)\]\([^)]*\)")
# `` `code` `` spans, wrapped in <code> after escaping.
_CODE = re.compile(r"`([^`]+)`")
# An <a> whose href ends in `glossary/#<id>` (directory URLs), any attributes,
# any inner markup.
_ANCHOR = re.compile(
    r'<a\b[^>]*\bhref="[^"]*glossary/#([a-z0-9-]+)"[^>]*>.*?</a>', re.DOTALL
)

# id -> (term label, definition HTML). Populated in on_config.
_DEFS = {}


def _to_html(text):
    """Render one definition's plain text: drop link targets, keep code."""
    text = _LINK.sub(r"\1", text)
    out, last = [], 0
    for m in _CODE.finditer(text):
        out.append(html.escape(text[last : m.start()]))
        out.append(f"<code>{html.escape(m.group(1))}</code>")
        last = m.end()
    out.append(html.escape(text[last:]))
    return "".join(out)


def on_config(config):
    _DEFS.clear()
    path = Path(config["docs_dir"]) / "glossary.md"
    if not path.exists():
        return config

    lines = path.read_text(encoding="utf-8").splitlines()
    i, n = 0, len(lines)
    while i < n:
        m = _TERM.match(lines[i].strip())
        if m and i + 1 < n and lines[i + 1].lstrip().startswith(":"):
            term, tid = m.group("term").strip(), m.group("id")
            # First definition line: strip the leading ':'.
            body = [lines[i + 1].lstrip()[1:].strip()]
            j = i + 2
            while j < n and lines[j].strip() and lines[j][:1] in " \t":
                body.append(lines[j].strip())
                j += 1
            text = " ".join(part for part in body if part)
            _DEFS[tid] = (term, _to_html(text))
            i = j
            continue
        i += 1
    return config


def on_page_content(html_out, page, config, files):
    if page.file.src_uri == "glossary.md" or "glossary/#" not in html_out:
        return html_out

    def wrap(match):
        entry = _DEFS.get(match.group(1))
        if not entry:
            return match.group(0)
        term, definition = entry
        card = (
            '<span class="afs-term__card" role="tooltip">'
            f'<span class="afs-term__title">{html.escape(term)}</span>'
            f'<span class="afs-term__def">{definition}</span>'
            "</span>"
        )
        return f'<span class="afs-term">{match.group(0)}{card}</span>'

    return _ANCHOR.sub(wrap, html_out)
