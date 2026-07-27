/*
 * Provenance citation cards.
 *
 * The cards (hooks/provenance.py) and their hover/focus behaviour (CSS) work
 * without JavaScript. This adds click-to-pin so a reader can open a card and
 * follow its links on touch and keyboard: clicking the marker toggles the card
 * open, clicking elsewhere or pressing Escape closes it.
 */
(function () {
  function closeAll(except) {
    document.querySelectorAll(".afs-cite.is-open").forEach(function (cite) {
      if (cite === except) return;
      cite.classList.remove("is-open");
      var toggle = cite.querySelector(".afs-cite__toggle");
      if (toggle) toggle.setAttribute("aria-expanded", "false");
    });
  }

  document.addEventListener("click", function (event) {
    var toggle = event.target.closest(".afs-cite__toggle");
    if (!toggle) {
      // A click outside any marker: if it was not inside an open card, close.
      if (!event.target.closest(".afs-cite__card")) closeAll(null);
      return;
    }
    var cite = toggle.closest(".afs-cite");
    closeAll(cite);
    var open = cite.classList.toggle("is-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    event.preventDefault();
    event.stopPropagation();
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeAll(null);
  });
})();
