/*
 * "Ask your own assistant" call-to-action.
 *
 * The Open-in-ChatGPT / Open-in-Claude links work without JavaScript: their
 * hrefs are pre-filled in the HTML. This script only enhances the block:
 *  - wires the "Copy as Markdown" button to the page's .md mirror (written by
 *    hooks/llms_txt.py), falling back to copying the page URL;
 *  - appends the current page URL to the assistant prompts, so an assistant
 *    can also read the specific page the reader came from.
 */
(function () {
  "use strict";

  function initCta(cta) {
    var copyBtn = cta.querySelector("[data-afs-ai-copy]");
    if (copyBtn) {
      var mdUrl = new URL("index.md", window.location.href).href;
      copyBtn.addEventListener("click", function () {
        fetch(mdUrl)
          .then(function (r) {
            if (!r.ok) throw new Error("no mirror");
            return r.text();
          })
          .catch(function () {
            return window.location.href;
          })
          .then(function (text) {
            return navigator.clipboard.writeText(text);
          })
          .then(function () {
            flash(copyBtn, "Copied");
          })
          .catch(function () {
            flash(copyBtn, "Copy failed");
          });
      });
    }
  }

  function flash(btn, label) {
    var original = btn.getAttribute("data-afs-label") || btn.textContent;
    btn.setAttribute("data-afs-label", original);
    btn.textContent = label;
    btn.setAttribute("data-afs-copied", "true");
    window.setTimeout(function () {
      btn.textContent = original;
      btn.removeAttribute("data-afs-copied");
    }, 1600);
  }

  function init() {
    var blocks = document.querySelectorAll("[data-afs-ai-cta]");
    for (var i = 0; i < blocks.length; i++) {
      initCta(blocks[i]);
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
