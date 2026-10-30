"""Render the link-preview card, docs/assets/img/social-card.png (1200x630).

Uses a local Chrome in headless mode. Run: python scripts/social_card.py
Set CHROME to the browser binary if it is not at the default macOS path.
"""

import os
import subprocess
import tempfile
from pathlib import Path

CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)

ROOT = Path(__file__).resolve().parent.parent
LOGO = (ROOT / "docs/assets/img/logo.svg").read_text()
OUT = ROOT / "docs/assets/img/social-card.png"

HTML = f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
  html, body {{ margin: 0; }}
  body {{
    width: 1200px; height: 630px; box-sizing: border-box;
    padding: 72px 84px; display: flex; flex-direction: column;
    justify-content: space-between;
    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    color: #f4fafc;
    background:
      radial-gradient(circle at 82% 14%, rgba(44, 168, 194, 0.30), transparent 420px),
      radial-gradient(circle at 9% 20%, rgba(96, 122, 247, 0.12), transparent 380px),
      linear-gradient(140deg, #06161d, #0c2530 62%, #12384a);
  }}
  .brand {{ display: flex; align-items: center; gap: 22px;
    font-size: 40px; font-weight: 800; letter-spacing: -0.02em; }}
  .brand svg {{ width: 84px; height: 84px; }}
  h1 {{ margin: 0; font-size: 82px; line-height: 1.04; font-weight: 800;
    letter-spacing: -0.035em; }}
  p {{ margin: 0; font-size: 30px; color: #b9d3dc; }}
  .url {{ color: #8ee6f5; font-weight: 700; }}
</style></head><body>
  <div class="brand">{LOGO}<span>AI for Science</span></div>
  <h1>Best practices for<br>agentic AI in science.</h1>
  <p>Cited, versioned, open to challenge. <span class="url">aiforscience.eu</span></p>
</body></html>"""

with tempfile.TemporaryDirectory() as tmp:
    src = Path(tmp) / "card.html"
    src.write_text(HTML)
    subprocess.run(
        [
            CHROME,
            "--headless",
            "--hide-scrollbars",
            "--window-size=1200,630",
            f"--user-data-dir={tmp}/profile",
            f"--screenshot={OUT}",
            src.as_uri(),
        ],
        check=True,
        capture_output=True,
    )
print(f"wrote {OUT}")
