/*
 * Cursor spotlight for the home feature cards.
 *
 * On hover, two masked overlays follow the cursor: the interior dot grid behind
 * each card's line art, and the glow on the card rim (see .afs-feature-card__media
 * and .afs-feature-card::before in home.css). This script feeds them the pointer
 * position as CSS variables:
 *  - --afs-mx / --afs-my on the media box (percentages of the media rect), for
 *    the interior dot spotlight;
 *  - --afs-cx / --afs-cy on the card (percentages of the card rect), for the rim.
 * Without JavaScript both simply stay centred at their default 50% 50%.
 */
(function () {
  "use strict";

  function init() {
    var cards = document.querySelectorAll(".afs-feature-card");
    Array.prototype.forEach.call(cards, function (card) {
      var media = card.querySelector(".afs-feature-card__media");
      if (!media) {
        return;
      }
      card.addEventListener("pointermove", function (e) {
        var mRect = media.getBoundingClientRect();
        if (mRect.width && mRect.height) {
          media.style.setProperty(
            "--afs-mx",
            ((e.clientX - mRect.left) / mRect.width) * 100 + "%"
          );
          media.style.setProperty(
            "--afs-my",
            ((e.clientY - mRect.top) / mRect.height) * 100 + "%"
          );
        }
        var cRect = card.getBoundingClientRect();
        if (cRect.width && cRect.height) {
          card.style.setProperty(
            "--afs-cx",
            ((e.clientX - cRect.left) / cRect.width) * 100 + "%"
          );
          card.style.setProperty(
            "--afs-cy",
            ((e.clientY - cRect.top) / cRect.height) * 100 + "%"
          );
        }
      });
    });
  }

  if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
