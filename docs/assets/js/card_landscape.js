/*
 * Dot landscape for the home feature cards.
 *
 * Replaces the flat tiled dot grid in the card media zone with a relief: a
 * dense field of small, same-size dots on a receding, tilted plane, displaced
 * by a rough multi-scale height function so they read as a 3D landscape. All
 * depth cues are spacing, never dot size: the plane's perspective bunches the
 * far rows toward a cropped horizon while the near rows splay apart, and the
 * surface compresses the dots on its slopes. The height field is domain-warped
 * fractal value noise with a ridged layer for sharp crests, so the terrain
 * swirls and never repeats (see heightAt); each card samples a different
 * stretch of it. Everything else is projection and shading.
 *
 * The grid bleeds past all four edges and is cropped by the media box (rounded
 * corners and all), so the terrain fills the whole card. Each card gets one
 * canvas, chosen over thousands of SVG nodes so the draw stays cheap. The
 * terrain height is computed once; a small travelling-swell layer is added per
 * frame so the waves roll toward the viewer (a shared rAF ticker drives every
 * on-screen card, paused when scrolled away and disabled for
 * prefers-reduced-motion). On hover the dots near the cursor brighten, more so
 * on the crests. Without JavaScript the media simply keeps its base tint.
 */
(function () {
  "use strict";

  // Field space. The dots are computed once in these units and scaled to the
  // canvas; 16:9 to match the media box so the plane never distorts.
  var W = 160;
  var H = 90;
  var TAU = Math.PI * 2;

  // All the shape knobs in one place. Coordinates are field units unless the
  // name says "frac" (a fraction of the box).
  var CFG = {
    cols: 160, // dots across a row
    rows: 90, // dot rows, back (0) to front (1)
    bleedTopFrac: 0.1, // rows start this far above the top edge (cropped)
    bleedBottomFrac: 0.1, // rows end this far below the bottom edge (cropped)
    rowGamma: 2.5, // >1 bunches the far rows toward the horizon (tilt/depth)
    backScaleX: .5, // row width at the back, relative to the box
    frontScaleX: 1.85, // row width at the front (wider, so near rows splay out)
    zLift: 48, // field units a unit of height rises on screen
    reliefBack: 0.8, // relief kept at the back (0..1); full relief at the front
    dotR: 0.25, // dot radius, constant (depth reads from spacing, not size)
    opBack: 0.02, // base opacity of the far rows (hazier)
    opFront: 0.02, // base opacity of the near rows
    peakBoost: 0.2, // extra opacity for the highest dots
    peakThreshold: 0.35, // height (0..1) where a dot counts as a "peak"; boost
    //                     and peak-lit hover ramp in from here up to the top
    hoverBoost: 0.1, // extra opacity at the cursor on hover
    hoverRadius: 80, // reach of the hover light, field units
    peakHoverGain: 3.0, // extra cursor light on peaks (0 = uniform glow)
    animate: true, // roll the waves (forced off for prefers-reduced-motion)
    animAmp: 0.35, // height of the moving swell over the static terrain (z units)
    animSpeed: 0.1, // wave speed (roughly cycles per second)
    baseFx: 2.3, // noise features across the width (low = long wave crests)
    baseFy: 2.3, // noise features across the depth (high = many crest lines)
    warpAmp: 1.2, // domain-warp strength: how hard the field swirls
    ridgeMix: 0.6, // blend of ridged (sharp crests) vs rounded fBm, 0..1
    swellMix: 0.6, // weight of the big rolling swell under the chop, 0..1
    swellF: 0.5, // swell frequency relative to the chop (low = broad rollers)
    octaves: 8, // noise octaves (detail depth)
    gain: 0.5, // octave amplitude falloff (higher = more mid/fine activity)
    lac: 2.03, // octave frequency step (off 2 so octaves never phase-lock)
    cardStep: 5.5, // how far each card samples into the noise (all differ)
    quant: 24 // opacity levels to batch fills into
  };

  // Deterministic hash and smooth value noise (no Math.random, so the terrain
  // is identical every load). vnoise returns [0, 1] over a unit lattice.
  function frac(t) {
    return t - Math.floor(t);
  }
  function hash(x, y) {
    return frac(Math.sin(x * 127.1 + y * 311.7) * 43758.5453);
  }
  function vnoise(x, y) {
    var xi = Math.floor(x);
    var yi = Math.floor(y);
    var xf = x - xi;
    var yf = y - yi;
    var u = xf * xf * (3 - 2 * xf);
    var v = yf * yf * (3 - 2 * yf);
    var a = hash(xi, yi);
    var b = hash(xi + 1, yi);
    var c = hash(xi, yi + 1);
    var d = hash(xi + 1, yi + 1);
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
  }

  // Fractal noise: octaves of vnoise at frequency stepping by lac and amplitude
  // falling by gain. fbm is rounded; ridged folds each octave to 1 - |2n - 1|
  // for sharp crests.
  function fbm(x, y) {
    var sum = 0;
    var amp = 0.5;
    var f = 1;
    var norm = 0;
    for (var o = 0; o < CFG.octaves; o++) {
      sum += amp * vnoise(x * f, y * f);
      norm += amp;
      f *= CFG.lac;
      amp *= CFG.gain;
    }
    return sum / norm;
  }
  function ridged(x, y) {
    var sum = 0;
    var amp = 0.5;
    var f = 1;
    var norm = 0;
    for (var o = 0; o < CFG.octaves; o++) {
      var n = 1 - Math.abs(2 * vnoise(x * f, y * f) - 1);
      sum += amp * n * n;
      norm += amp;
      f *= CFG.lac;
      amp *= CFG.gain;
    }
    return sum / norm;
  }

  // The surface height in [-1, 1]. u, v in [0, 1] run left-right and back-front;
  // ox, oy offset the sample point so each card gets a different stretch of sea.
  // The base coordinates are anisotropic (long crests across the width, many
  // crest lines in depth), so the chop reads as swell lines. Domain warping
  // (sampling fBm at a point that fBm itself displaces) breaks their regularity
  // into non-repeating waves; a ridged layer sharpens the crests. A broad,
  // low-frequency swell is mixed under the chop so big rollers ride beneath it.
  function heightAt(u, v, ox, oy) {
    var px = u * CFG.baseFx + ox;
    var py = v * CFG.baseFy + oy;
    var wx = fbm(px, py);
    var wy = fbm(px + 5.2, py + 1.3);
    var qx = px + CFG.warpAmp * (wx - 0.5) * 2;
    var qy = py + CFG.warpAmp * (wy - 0.5) * 2;
    var chop = fbm(qx, qy) * (1 - CFG.ridgeMix) + ridged(qx + 3.7, qy - 2.1) * CFG.ridgeMix;
    var swell = fbm(px * CFG.swellF + 7.0, py * CFG.swellF - 4.0);
    var h = chop * (1 - CFG.swellMix) + swell * CFG.swellMix;
    return h * 2 - 1;
  }

  // A dot's peak factor and base opacity from its current height z, normalised
  // to a fixed range so brightness never flickers as the waves move. The peak
  // factor is 0 below the threshold height and smoothsteps to 1 at the top; it
  // drives both the static peak boost and the peak-weighted hover.
  function shade(d, z, zMin, span) {
    var nz = (z - zMin) / span;
    if (nz < 0) nz = 0;
    else if (nz > 1) nz = 1;
    var tspan = 1 - CFG.peakThreshold || 1;
    var pk = (nz - CFG.peakThreshold) / tspan;
    pk = pk <= 0 ? 0 : pk >= 1 ? 1 : pk * pk * (3 - 2 * pk);
    d.pk = pk;
    d.base = Math.min(0.5, d.opd + CFG.peakBoost * pk);
  }

  // The moving part of the height: three travelling sinusoids rolling toward the
  // viewer (crests march from the horizon to the front as t grows). Cheap
  // enough to evaluate for every dot every frame, and it loops forever with no
  // seam, so points transition monotonically. Scaled by animAmp.
  function waveDisp(u, v, t) {
    var s = CFG.animSpeed;
    return (
      CFG.animAmp *
      (0.5 * Math.sin(TAU * (1.2 * v - 0.9 * s * t)) +
        0.3 * Math.sin(TAU * (0.5 * u + 2.0 * v - 1.3 * s * t) + 1.7) +
        0.2 * Math.sin(TAU * (-0.8 * u + 2.9 * v - 1.7 * s * t) + 4.2))
    );
  }

  // The dots for one card, in field units. Each keeps the static terrain height
  // (z0) plus the fields needed to re-place and re-shade it per frame. Far rows
  // bunch toward the horizon, splay narrower, sit dimmer, and carry less relief;
  // near rows spread apart and overflow the sides (cropped later). Returns the
  // dots and the fixed shading range (static span padded by the wave amplitude
  // so moving crests never clip).
  function computeDots(index) {
    var ox = index * CFG.cardStep;
    var oy = index * CFG.cardStep * 0.7;
    var cx = W / 2;
    var yTop = -CFG.bleedTopFrac * H;
    var yBottom = H + CFG.bleedBottomFrac * H;

    var dots = [];
    var zMin = Infinity;
    var zMax = -Infinity;
    for (var j = 0; j < CFG.rows; j++) {
      var v = CFG.rows > 1 ? j / (CFG.rows - 1) : 0;
      var scale = CFG.backScaleX + (CFG.frontScaleX - CFG.backScaleX) * v;
      var groundY = yTop + (yBottom - yTop) * Math.pow(v, CFG.rowGamma);
      var opd = CFG.opBack + (CFG.opFront - CFG.opBack) * v;
      var relief = CFG.zLift * (CFG.reliefBack + (1 - CFG.reliefBack) * v);
      for (var i = 0; i < CFG.cols; i++) {
        var u = CFG.cols > 1 ? i / (CFG.cols - 1) : 0;
        var z = heightAt(u, v, ox, oy);
        if (z < zMin) zMin = z;
        if (z > zMax) zMax = z;
        dots.push({
          x: cx + (u - 0.5) * W * scale,
          y: groundY - z * relief,
          u: u,
          v: v,
          groundY: groundY,
          relief: relief,
          opd: opd,
          z0: z
        });
      }
    }

    var pad = CFG.animate ? CFG.animAmp : 0;
    var lo = zMin - pad;
    var span = zMax + pad - lo || 1;
    for (var k = 0; k < dots.length; k++) shade(dots[k], dots[k].z0, lo, span);

    return { dots: dots, zMin: lo, span: span };
  }

  // Re-place and re-shade every dot for time t (seconds): static height plus the
  // moving swell, giving smooth vertical motion as the waves roll through.
  function computeFrame(view, t) {
    var dots = view.dots;
    for (var k = 0; k < dots.length; k++) {
      var d = dots[k];
      var z = d.z0 + waveDisp(d.u, d.v, t);
      d.y = d.groundY - z * d.relief;
      shade(d, z, view.zMin, view.span);
    }
  }

  // Paint the field. Dots are bucketed by opacity so the whole frame is a
  // handful of fills rather than one per dot. cursor is {x, y} in field units,
  // or null when nothing is hovered.
  function draw(ctx, dots, sc, cursor) {
    var cw = ctx.canvas.width;
    var ch = ctx.canvas.height;
    ctx.clearRect(0, 0, cw, ch);

    var levels = CFG.quant;
    var paths = new Array(levels);
    for (var l = 0; l < levels; l++) {
      paths[l] = new Path2D();
    }

    var reach = CFG.hoverRadius;
    var r = CFG.dotR * sc;
    for (var k = 0; k < dots.length; k++) {
      var d = dots[k];
      var op = d.base;
      if (cursor) {
        var dx = d.x - cursor.x;
        var dy = d.y - cursor.y;
        var t = 1 - Math.sqrt(dx * dx + dy * dy) / reach;
        if (t > 0) op += CFG.hoverBoost * t * t * (1 + CFG.peakHoverGain * d.pk);
      }
      var lvl = (op * levels) | 0;
      if (lvl < 0) lvl = 0;
      else if (lvl >= levels) lvl = levels - 1;
      var p = paths[lvl];
      p.moveTo(d.x * sc + r, d.y * sc);
      p.arc(d.x * sc, d.y * sc, r, 0, TAU);
    }

    ctx.fillStyle = "#ffffff";
    for (var m = 0; m < levels; m++) {
      ctx.globalAlpha = (m + 0.5) / levels;
      ctx.fill(paths[m]);
    }
    ctx.globalAlpha = 1;
  }

  // Size the canvas to its box (device pixels) and return the field-to-pixel
  // scale, or 0 if the box has not been laid out yet.
  function size(canvas, media) {
    var rect = media.getBoundingClientRect();
    if (!rect.width || !rect.height) return 0;
    var dpr = window.devicePixelRatio || 1;
    canvas.width = Math.round(rect.width * dpr);
    canvas.height = Math.round(rect.height * dpr);
    return canvas.width / W;
  }

  function build(media, index) {
    var canvas = document.createElement("canvas");
    canvas.className = "afs-feature-card__dots";
    canvas.setAttribute("aria-hidden", "true");
    media.insertBefore(canvas, media.firstChild);

    var ctx = canvas.getContext("2d");
    var field = computeDots(index);
    var sc = size(canvas, media);
    var view = {
      canvas: canvas,
      ctx: ctx,
      media: media,
      dots: field.dots,
      zMin: field.zMin,
      span: field.span,
      sc: sc,
      cursor: null
    };
    if (sc) draw(ctx, view.dots, sc, null);
    return view;
  }

  // One shared rAF ticker drives every animating, on-screen card, so there is a
  // single loop rather than one per card. It stops itself when nothing is
  // visible and restarts when a card scrolls back in.
  var ticking = [];
  var rafId = 0;
  function tick(ts) {
    var t = ts * 0.001;
    for (var i = 0; i < ticking.length; i++) {
      var view = ticking[i];
      if (!view.sc) continue;
      computeFrame(view, t);
      draw(view.ctx, view.dots, view.sc, view.cursor);
    }
    rafId = ticking.length ? requestAnimationFrame(tick) : 0;
  }
  function startTicking(view) {
    if (ticking.indexOf(view) === -1) ticking.push(view);
    if (!rafId) rafId = requestAnimationFrame(tick);
  }
  function stopTicking(view) {
    var idx = ticking.indexOf(view);
    if (idx !== -1) ticking.splice(idx, 1);
  }

  function paint(view) {
    if (view.sc) draw(view.ctx, view.dots, view.sc, view.cursor);
  }

  function wire(card, view) {
    var reduce =
      window.matchMedia &&
      window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var animate = !!(CFG.animate && !reduce);

    // A rAF for one-off redraws on the static path (hover, resize while paused).
    var raf = 0;
    function schedule() {
      if (!raf)
        raf = requestAnimationFrame(function () {
          raf = 0;
          paint(view);
        });
    }

    card.addEventListener("pointermove", function (e) {
      var rect = view.media.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      view.cursor = {
        x: ((e.clientX - rect.left) / rect.width) * W,
        y: ((e.clientY - rect.top) / rect.height) * H
      };
      if (!animate) schedule(); // animating views redraw every frame anyway
    });
    card.addEventListener("pointerleave", function () {
      view.cursor = null;
      if (!animate) schedule();
    });

    // Redraw at the new resolution when the card is resized.
    if (typeof ResizeObserver === "function") {
      new ResizeObserver(function () {
        view.sc = size(view.canvas, view.media);
        paint(view);
      }).observe(view.media);
    }

    if (!animate) return;

    // Animate only while the card is on-screen; the observer starts and stops
    // the shared ticker as it enters and leaves the viewport.
    if (typeof IntersectionObserver === "function") {
      new IntersectionObserver(function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) startTicking(view);
          else {
            stopTicking(view);
            paint(view);
          }
        }
      }).observe(view.media);
    } else {
      startTicking(view);
    }
  }

  function init() {
    Array.prototype.forEach.call(
      document.querySelectorAll(".afs-feature-card"),
      function (card, index) {
        var media = card.querySelector(".afs-feature-card__media");
        if (!media || media.querySelector(".afs-feature-card__dots")) return;
        wire(card, build(media, index));
      }
    );
  }

  if (document.readyState !== "loading") {
    init();
  } else {
    document.addEventListener("DOMContentLoaded", init);
  }
})();
