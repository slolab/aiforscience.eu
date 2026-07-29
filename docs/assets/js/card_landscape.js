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
 * canvas, chosen over thousands of SVG nodes so the draw and the hover redraw
 * stay cheap. On hover the dots near the cursor brighten, so a patch of the
 * terrain lights up as the pointer moves. Without JavaScript the media simply
 * keeps its base tint.
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
    cols: 140, // dots across a row
    rows: 88, // dot rows, back (0) to front (1)
    bleedTopFrac: 0.19, // rows start this far above the top edge (cropped)
    bleedBottomFrac: 0.1, // rows end this far below the bottom edge (cropped)
    rowGamma: 2.1, // >1 bunches the far rows toward the horizon (tilt/depth)
    backScaleX: 1.0, // row width at the back, relative to the box
    frontScaleX: 1.62, // row width at the front (wider, so near rows splay out)
    zLift: 31, // field units a unit of height rises on screen
    reliefBack: 0.45, // relief kept at the back (0..1); full relief at the front
    dotR: 0.3, // dot radius, constant (depth reads from spacing, not size)
    opBack: 0.014, // base opacity of the far rows (hazier)
    opFront: 0.095, // base opacity of the near rows
    peakBoost: 0.03, // extra opacity for the highest dots
    hoverBoost: 0.16, // extra opacity at the cursor on hover
    hoverRadius: 65, // reach of the hover light, field units
    baseFx: 2.2, // noise features across the width (higher = more, smaller)
    baseFy: 1.85, // noise features across the depth
    warpAmp: 1.65, // domain-warp strength: how hard the field swirls
    ridgeMix: 0.52, // blend of ridged (sharp crests) vs rounded fBm, 0..1
    octaves: 5, // noise octaves (detail depth)
    gain: 0.55, // octave amplitude falloff (higher = more mid/fine activity)
    lac: 2.03, // octave frequency step (off 2 so octaves never phase-lock)
    cardStep: 37.0, // how far each card samples into the noise (all differ)
    quant: 28 // opacity levels to batch fills into
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
  // ox, oy offset the sample point so each card gets a different stretch of
  // terrain. Domain warping (sampling fBm at a point that fBm itself displaces)
  // turns smooth swells into swirling, non-repeating ridges and basins; a
  // ridged layer blended on top sharpens the crests.
  function heightAt(u, v, ox, oy) {
    var px = u * CFG.baseFx + ox;
    var py = v * CFG.baseFy + oy;
    var wx = fbm(px, py);
    var wy = fbm(px + 5.2, py + 1.3);
    var qx = px + CFG.warpAmp * (wx - 0.5) * 2;
    var qy = py + CFG.warpAmp * (wy - 0.5) * 2;
    var h = fbm(qx, qy) * (1 - CFG.ridgeMix) + ridged(qx + 3.7, qy - 2.1) * CFG.ridgeMix;
    return h * 2 - 1;
  }

  // The dots for one card, in field units, with a base opacity each. Far rows
  // bunch toward the horizon, splay narrower, sit dimmer, and carry less
  // relief; near rows spread apart and overflow the sides (cropped later).
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
          z: z,
          opd: opd
        });
      }
    }

    var span = zMax - zMin || 1;
    for (var k = 0; k < dots.length; k++) {
      var d = dots[k];
      var nz = (d.z - zMin) / span; // 0 low, 1 high
      d.base = Math.min(0.5, d.opd + CFG.peakBoost * nz);
    }
    return dots;
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
        if (t > 0) op += CFG.hoverBoost * t * t;
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
    var dots = computeDots(index);
    var sc = size(canvas, media);
    if (sc) draw(ctx, dots, sc, null);

    return { canvas: canvas, ctx: ctx, media: media, dots: dots, sc: sc };
  }

  function wire(card, view) {
    var raf = 0;
    var cursor = null;

    function render() {
      raf = 0;
      if (view.sc) draw(view.ctx, view.dots, view.sc, cursor);
    }
    function schedule() {
      if (!raf) raf = requestAnimationFrame(render);
    }

    card.addEventListener("pointermove", function (e) {
      var rect = view.media.getBoundingClientRect();
      if (!rect.width || !rect.height) return;
      cursor = {
        x: ((e.clientX - rect.left) / rect.width) * W,
        y: ((e.clientY - rect.top) / rect.height) * H
      };
      schedule();
    });
    card.addEventListener("pointerleave", function () {
      cursor = null;
      schedule();
    });

    // Redraw at the new resolution when the card is resized.
    if (typeof ResizeObserver === "function") {
      var ro = new ResizeObserver(function () {
        view.sc = size(view.canvas, view.media);
        schedule();
      });
      ro.observe(view.media);
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
