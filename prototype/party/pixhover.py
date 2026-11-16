"""Photo hover on the stuart.re-style page: pixelated -> sharp, then the photo splits into tiles that scatter from the cursor and spring back.
usage: pixhover.py <TinHome-Stuart.dc.html>"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:80], s.count(old)); s = s.replace(old, new)
JS = r"""
  pxStart() { // hover a photo: it pixelates, sharpens, then breaks into tiles that scatter from the cursor
    const root = this.rootEl; if (!root || this.pxOn) return; this.pxOn = true;
    const reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce || this.props.pixelHover === false) return;
    this.pxMove = (e) => {
      const fig = e.target && e.target.closest ? e.target.closest('.st-media') : null;
      if (fig !== this.pxFig) { this.pxLeave(); if (fig && fig.querySelector('img')) this.pxEnter(fig); }
      const P = this.pxS; if (P && P.fig === fig) { const r = fig.getBoundingClientRect(); P.mx = e.clientX - r.left; P.my = e.clientY - r.top; }
    };
    this.pxOut = () => this.pxLeave();
    root.addEventListener('pointermove', this.pxMove); root.addEventListener('pointerleave', this.pxOut);
  }
  pxEnter(fig) {
    const img = fig.querySelector('img'); if (!img || !img.complete || !img.naturalWidth) return;
    if (this.pxS) this.pxEnd();
    this.pxFig = fig;
    const W = fig.clientWidth, H = fig.clientHeight, dpr = Math.min(2, window.devicePixelRatio || 1);
    let cv = fig.querySelector('canvas.st-px'); if (!cv) { cv = document.createElement('canvas'); cv.className = 'st-px'; cv.setAttribute('aria-hidden', 'true'); fig.appendChild(cv); }
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
    const ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const op = getComputedStyle(img).objectPosition.split(' ').map((v) => (v.endsWith('%') ? parseFloat(v) / 100 : 0.5));
    const sc = Math.max(W / img.naturalWidth, H / img.naturalHeight), sw = W / sc, sh = H / sc;
    const sx = (img.naturalWidth - sw) * (op[0] ?? 0.5), sy = (img.naturalHeight - sh) * (op[1] ?? 0.5);
    const T = Math.max(6, this.props.pixelTile ?? 16), tiles = [];
    for (let y = 0; y < H; y += T) for (let x = 0; x < W; x += T) tiles.push({ x, y, dx: 0, dy: 0, vx: 0, vy: 0 });
    this.pxS = { fig, cv, ctx, img, W, H, sx, sy, sc, T, tiles, small: document.createElement('canvas'), t0: performance.now(), mx: -1e4, my: -1e4, leaving: false };
    fig.classList.add('px-on');
    cancelAnimationFrame(this.pxRaf);
    const tick = (now) => { if (!this.pxS) return; this.pxRaf = requestAnimationFrame(tick); this.pxDraw(now); };
    this.pxRaf = requestAnimationFrame(tick);
  }
  pxLeave() { const P = this.pxS; if (P) { P.leaving = true; P.mx = P.my = -1e4; } this.pxFig = null; }
  pxEnd() { const P = this.pxS; if (!P) return; cancelAnimationFrame(this.pxRaf); P.fig.classList.remove('px-on'); this.pxS = null; }
  pxDraw(now) {
    const P = this.pxS, { ctx, img, W, H, T } = P;
    const u = Math.min(1, (now - P.t0) / (this.props.pixelMs ?? 700));
    ctx.clearRect(0, 0, W, H);
    if (u < 1) { // pixelated -> sharp
      if (P.leaving) { this.pxEnd(); return; }
      const e = 1 - Math.pow(1 - u, 3), b = Math.max(1, 56 * (1 - e));
      const w = Math.max(1, Math.round(W / b)), h = Math.max(1, Math.round(H / b));
      P.small.width = w; P.small.height = h; P.small.getContext('2d').drawImage(img, P.sx, P.sy, W / P.sc, H / P.sc, 0, 0, w, h);
      ctx.imageSmoothingEnabled = false; ctx.drawImage(P.small, 0, 0, w, h, 0, 0, W, H); ctx.imageSmoothingEnabled = true;
      return;
    }
    const R = this.props.pixelRadius ?? 120, F = this.props.pixelForce ?? 1; let moving = false;
    for (const t of P.tiles) { // tiles push away from the cursor and spring home
      const ddx = t.x + T / 2 + t.dx - P.mx, ddy = t.y + T / 2 + t.dy - P.my, d2 = ddx * ddx + ddy * ddy;
      if (d2 < R * R) { const d = Math.sqrt(d2) || 1, f = (1 - d / R) * 2.4 * F; t.vx += (ddx / d) * f; t.vy += (ddy / d) * f; }
      t.vx = (t.vx - t.dx * 0.07) * 0.8; t.vy = (t.vy - t.dy * 0.07) * 0.8; t.dx += t.vx; t.dy += t.vy;
      const off = Math.abs(t.dx) + Math.abs(t.dy); if (off > 0.25) moving = true;
      const k = Math.max(0.55, 1 - off / 160), ts = T * k, o = (T - ts) / 2;
      ctx.drawImage(img, P.sx + t.x / P.sc, P.sy + t.y / P.sc, T / P.sc, T / P.sc, t.x + t.dx + o, t.y + t.dy + o, ts, ts);
    }
    if (P.leaving && !moving) this.pxEnd();
  }"""
rep("  rvStart() {", JS.lstrip('\n') + "\n  rvStart() {")
rep("if (el) setTimeout(() => this.rvStart(), 0); }", "if (el) setTimeout(() => { this.rvStart(); this.pxStart(); }, 0); }")
rep("if (this.rvIO) this.rvIO.disconnect(); }",
    "if (this.rvIO) this.rvIO.disconnect(); cancelAnimationFrame(this.pxRaf); if (this.rootEl && this.pxMove) { this.rootEl.removeEventListener('pointermove', this.pxMove); this.rootEl.removeEventListener('pointerleave', this.pxOut); } }")
CSS = ('/* photo hover: canvas tiles over the photo while hovered */\n'
       '.st-media{position:relative}\n'
       '.st-px{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;opacity:0}\n'
       '.st-media.px-on .st-px{opacity:1}\n'
       '.st-media.px-on img{visibility:hidden}\n')
rep('/* scroll reveal:', CSS + '/* scroll reveal:')
mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S); P = json.loads(html.unescape(mm.group(2)))
P.update({'pixelHover': {"editor": "boolean", "default": True, "section": "Motion"},
          'pixelTile': {"editor": "range", "default": 16, "min": 6, "max": 48, "step": 1, "unit": "px", "section": "Motion"},
          'pixelRadius': {"editor": "range", "default": 120, "min": 40, "max": 300, "step": 5, "unit": "px", "section": "Motion"},
          'pixelForce': {"editor": "range", "default": 1, "min": 0, "max": 3, "step": 0.05, "unit": "×", "section": "Motion"},
          'pixelMs': {"editor": "range", "default": 700, "min": 200, "max": 2000, "step": 50, "unit": "ms", "section": "Motion"}})
s = s[:mm.start()] + "data-props='" + json.dumps(P, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;') + "'>" + s[mm.end():]
open(p, 'w').write(s); print('ok')
