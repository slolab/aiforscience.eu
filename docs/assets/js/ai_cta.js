/*
 * "Ask your own AI Assistant" call-to-action, on the short version (a strip)
 * and in the home hero (a dropdown menu).
 *
 * The Open-in-ChatGPT / Open-in-Claude links work without JavaScript: their
 * hrefs are pre-filled in the HTML. This script only enhances them:
 *  - wires each "Copy as Markdown" button ([data-afs-ai-copy]) to a Markdown
 *    mirror written by hooks/llms_txt.py: the attribute's value if it has one,
 *    otherwise the current page's index.md. Falls back to copying the page URL;
 *  - for links marked [data-afs-ai-copy-prompt] (Gemini, which takes no prompt
 *    in the URL), copies the block's data-afs-ai-prompt before the link opens;
 *  - closes the hero's <details> menu on an outside click or Escape.
 */
(function () {
  "use strict";

  function initCta(cta) {
    var copyBtns = cta.querySelectorAll("[data-afs-ai-copy]");
    Array.prototype.forEach.call(copyBtns, function (copyBtn) {
      var src = copyBtn.getAttribute("data-afs-ai-copy") || "index.md";
      var mdUrl = new URL(src, window.location.href).href;
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
    });

    var prompt = cta.getAttribute("data-afs-ai-prompt");
    var promptLinks = cta.querySelectorAll("[data-afs-ai-copy-prompt]");
    Array.prototype.forEach.call(promptLinks, function (link) {
      link.addEventListener("click", function () {
        if (prompt && navigator.clipboard) {
          navigator.clipboard.writeText(prompt).catch(function () {});
        }
      });
    });

    if (cta.tagName === "DETAILS") {
      document.addEventListener("click", function (e) {
        if (cta.open && !cta.contains(e.target)) cta.open = false;
      });
      cta.addEventListener("keydown", function (e) {
        if (e.key === "Escape" && cta.open) {
          cta.open = false;
          cta.querySelector("summary").focus();
        }
      });
    }
  }

  // Swap the label briefly. innerHTML, so a button's hint span survives.
  function flash(btn, label) {
    if (!btn.hasAttribute("data-afs-label")) {
      btn.setAttribute("data-afs-label", btn.innerHTML);
    }
    var original = btn.getAttribute("data-afs-label");
    btn.textContent = label;
    btn.setAttribute("data-afs-copied", "true");
    window.setTimeout(function () {
      btn.innerHTML = original;
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
