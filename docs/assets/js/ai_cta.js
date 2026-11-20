/*
 * "Ask your own AI Assistant" call-to-action, on the short version (a strip)
 * and in the home hero (a dropdown menu).
 *
 * The Open-in-ChatGPT / Open-in-Claude links work without JavaScript: their
 * hrefs are pre-filled in the HTML. This script only enhances them:
 *  - wires each "Copy as Markdown" button ([data-afs-ai-copy]) to a Markdown
 *    mirror written by hooks/llms_txt.py: the attribute's value if it has one,
 *    otherwise the current page's index.md. Falls back to copying the page URL;
 *  - with [data-afs-ai-wrap], wraps the copied Markdown in the block's
 *    data-afs-ai-intro and data-afs-ai-outro, so it pastes as a ready prompt
 *    into Gemini or any assistant that takes no prompt in the URL;
 *  - closes the hero's <details> menu on an outside click or Escape.
 */
(function () {
  "use strict";

  function initCta(cta) {
    var intro = cta.getAttribute("data-afs-ai-intro") || "";
    var outro = cta.getAttribute("data-afs-ai-outro") || "";
    var copyBtns = cta.querySelectorAll("[data-afs-ai-copy]");
    Array.prototype.forEach.call(copyBtns, function (copyBtn) {
      var src = copyBtn.getAttribute("data-afs-ai-copy") || "index.md";
      var mdUrl = new URL(src, window.location.href).href;
      var wrap = copyBtn.hasAttribute("data-afs-ai-wrap");
      copyBtn.addEventListener("click", function () {
        var text = fetch(mdUrl)
          .then(function (r) {
            if (!r.ok) throw new Error("no mirror");
            return r.text();
          })
          .catch(function () {
            return window.location.href;
          })
          .then(function (md) {
            if (!wrap) return md;
            return intro + "\n\n---\n\n" + md.trim() + "\n\n---\n\n" + outro;
          });
        copyText(text)
          .then(function () {
            flash(copyBtn, wrap ? "Copied. Paste it into your assistant." : "Copied");
          })
          .catch(function () {
            flash(copyBtn, "Copy failed");
          });
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

  // Copy a promised string. Safari only allows clipboard writes started inside
  // the click, so hand it a ClipboardItem that resolves after the fetch.
  function copyText(textPromise) {
    if (window.ClipboardItem && navigator.clipboard && navigator.clipboard.write) {
      var item = new ClipboardItem({
        "text/plain": textPromise.then(function (t) {
          return new Blob([t], { type: "text/plain" });
        }),
      });
      return navigator.clipboard.write([item]).catch(function () {
        return textPromise.then(function (t) {
          return navigator.clipboard.writeText(t);
        });
      });
    }
    return textPromise.then(function (t) {
      return navigator.clipboard.writeText(t);
    });
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
