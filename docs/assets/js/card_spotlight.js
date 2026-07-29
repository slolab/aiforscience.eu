/*
 * Cursor spotlight for the home cards.
 *
 * On hover, two masked overlays follow the cursor: an interior dot grid and a
 * glow on the card rim (see home.css). This script feeds them the pointer
 * position as CSS variables:
 *  - --afs-mx / --afs-my on the interior element (percentages of its rect), for
 *    the dot spotlight;
 *  - --afs-cx / --afs-cy on the card (percentages of the card rect), for the rim.
 * Without JavaScript both simply stay centred at their default 50% 50%.
 *
 * Two layouts use it: the feature cards, where the interior is a separate media
 * box, and the hero practices index, where the interior and rim are the same
 * element.
 */
(function () {
  "use strict";

  function setVars(el, e, xName, yName) {
    var rect = el.getBoundingClientRect();
    if (!rect.width || !rect.height) {
      return;
    }
    el.style.setProperty(xName, ((e.clientX - rect.left) / rect.width) * 100 + "%");
    el.style.setProperty(yName, ((e.clientY - rect.top) / rect.height) * 100 + "%");
  }

  function wire(card, media) {
    card.addEventListener("pointermove", function (e) {
      setVars(media, e, "--afs-mx", "--afs-my");
      setVars(card, e, "--afs-cx", "--afs-cy");
    });
  }

  function init() {
    Array.prototype.forEach.call(
      document.querySelectorAll(".afs-feature-card"),
      function (card) {
        var media = card.querySelector(".afs-feature-card__media");
        if (media) {
          wire(card, media);
        }
      }
    );
    Array.prototype.forEach.call(
      document.querySelectorAll(".afs-hero-index"),
      function (card) {
        wire(card, card);
      }
    );
  }

  if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
