"""Photo dots lab: each photo is drawn as dots (like the homepage hero). Dots fly in and form the photo when it scrolls into view,
and push away from the cursor, springing back. A separate board for tuning before it goes on the stuart.re-style page.
usage: dotslab.py <out.dc.html>"""
import sys, json
out = sys.argv[1]
PHOTOS = [('effff208332abe411e27c82aaa87e30d', 'Tin with his Microsoft team', '50% 72%', 'Microsoft AI'),
          ('155942c7f1c522f9aec7d43d1c1d0d0d', 'Tin teaching a product design class', '50% 50%', 'University of Oregon'),
          ('8bd998ead1110dbdb0a707cdb0cb6c60', 'Tin with his Salesforce team', '50% 45%', 'Salesforce')]
OPEN = '<a class="dl-open" href="#" aria-label="Open {cap}" onClick="{{{{noop}}}}"><span class="dl-open-fx" aria-hidden="true"></span><span class="dl-open-tint" aria-hidden="true"></span><span class="dl-open-shine" aria-hidden="true"></span><svg class="dl-open-ic" viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg><span class="dl-open-tx">Open</span></a>'
figs = ''.join(
    f'<figure class="dl-fig"><div class="dl-frame"><canvas class="dl-cv" ref="{{{{cv{i}}}}}" data-src="/_blob/{b}" data-pos="{pos}" role="img" aria-label="{alt}, drawn in dots"></canvas>' + OPEN.format(cap=cap) + '</div>'
    f'<figcaption class="dl-cap">{cap}</figcaption></figure>' for i, (b, alt, pos, cap) in enumerate(PHOTOS))
CSS = r'''
body{margin:0}
sc-for, sc-if { display: contents; }
.dl-root{width:1440px;box-sizing:border-box;padding:72px 296px 120px;background:var(--bg,#fff);color:#000;font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}
.dl-k{margin:0;font:600 12px/1 Inter,sans-serif;letter-spacing:.08em;color:#b3b3b3}
.dl-h{margin:10px 0 0;font:600 24px/36px Inter,sans-serif;letter-spacing:-.01em}
.dl-p{margin:6px 0 0;max-width:620px;font:400 15px/22px Inter,sans-serif;color:#666}
.dl-bar{display:flex;gap:8px;margin-top:20px}
.dl-btn{border:0;border-radius:10px;padding:8px 16px;font:600 15px/22.5px Inter,sans-serif;cursor:pointer;background:#000;color:#fff}
.dl-btn:hover{filter:brightness(1.6)}
.dl-btn:focus-visible{outline:2px solid #0099ff;outline-offset:3px}
.dl-stack{display:flex;flex-direction:column;gap:48px;margin-top:48px}
.dl-fig{margin:0}
.dl-cv{position:absolute;left:calc(var(--bleed,140px) * -1);top:calc(var(--bleed,140px) * -1);width:calc(848px + var(--bleed,140px) * 2);height:calc(524px + var(--bleed,140px) * 2);pointer-events:none;z-index:1}
.dl-frame{position:relative;width:848px;height:524px;touch-action:pan-y;cursor:crosshair}
.dl-frame:hover{z-index:2}
/* Open button: a dark-gray liquid-glass circle in the middle of each photo */
.dl-open{z-index:3;position:absolute;left:50%;top:50%;width:var(--ob,104px);height:var(--ob,104px);margin:calc(var(--ob,104px) / -2) 0 0 calc(var(--ob,104px) / -2);border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;color:#fff;text-decoration:none;isolation:isolate;box-shadow:0 12px 30px -10px rgba(0,0,0,.45),0 2px 6px rgba(0,0,0,.18);opacity:0;transform:scale(0);pointer-events:none;transition:opacity .18s ease,transform .5s cubic-bezier(.34,1.56,.64,1)}
/* only shows while the photo is hovered (or the button has keyboard focus) */
.dl-frame:hover .dl-open,.dl-open:focus-visible{opacity:1;transform:scale(1);pointer-events:auto}
.dl-open:hover{transform:scale(1.06)!important}
@media (prefers-reduced-motion: reduce){.dl-open{transition:none}}
.dl-open:active{transform:scale(.97)}
.dl-open:focus-visible{outline:2px solid #0099ff;outline-offset:4px}
.dl-open-fx,.dl-open-tint,.dl-open-shine{position:absolute;inset:0;border-radius:inherit;pointer-events:none}
.dl-open-fx{z-index:-3;-webkit-backdrop-filter:blur(6px) saturate(1.6);backdrop-filter:blur(6px) saturate(1.6);backdrop-filter:url(#dl-glass) blur(6px) saturate(1.6)}
.dl-open-tint{z-index:-2;background:rgba(43,43,45,var(--ot,.62))}
.dl-open-shine{z-index:-1;box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.5),inset -1px -1px 1px rgba(255,255,255,.22),inset 0 0 18px rgba(255,255,255,.1)}
.dl-open-ic{display:block;filter:drop-shadow(0 1px 1px rgba(0,0,0,.3))}
.dl-open-tx{font:600 14px/1 Inter,sans-serif;letter-spacing:.01em;text-shadow:0 1px 1px rgba(0,0,0,.25)}
.dl-defs{position:absolute;width:0;height:0;overflow:hidden}
.dl-cap{margin-top:12px;font:500 13px/1 Inter,sans-serif;color:#b3b3b3}
'''
JS = r'''
class Component extends DCLogic {
  constructor(props) { super(props); this.state = {}; this.P = []; this.refFns = [0, 1, 2].map((i) => (el) => this.attach(i, el)); }
  componentWillUnmount() { cancelAnimationFrame(this.raf); if (this.io) this.io.disconnect(); this.P.forEach((p) => p.off && p.off()); }
  tp(k, d) { const v = this.props[k]; return v === undefined || v === null ? d : v; }
  sig() { return ['dotDetail', 'dotSize', 'dotShape', 'sizeByShade', 'formFrom', 'bleed'].map((k) => this.tp(k, '')).join('|'); }
  attach(i, cv) {
    if (!cv || (this.P[i] && this.P[i].cv === cv)) return;
    const prev = this.P[i], carry = !!(prev && prev.seen); // canvas re-mounted: keep it formed, no replay, no blank frame
    if (prev) { if (prev.off) prev.off(); if (this.io && prev.cv) this.io.unobserve(prev.cv); }
    const P = { cv, img: new Image(), mx: -1e4, my: -1e4, dots: [], t0: 0, seen: carry, imgA: carry ? 1 : 0 };
    this.P[i] = P;
    P.img.onload = () => { this.build(P); if (carry) P.t0 = performance.now() - 1e6; else if (P.wantForm) { P.wantForm = false; P.t0 = performance.now(); } this.kick(); };
    P.img.src = cv.dataset.src;
    const host = cv.parentElement || cv;
    const move = (e) => { const r = host.getBoundingClientRect(); P.mx = e.clientX - r.left; P.my = e.clientY - r.top; this.kick(); };
    const leave = () => { P.mx = P.my = -1e4; this.kick(); };
    host.addEventListener('pointermove', move); host.addEventListener('pointerleave', leave);
    P.off = () => { host.removeEventListener('pointermove', move); host.removeEventListener('pointerleave', leave); };
    if (typeof IntersectionObserver === 'function') {
      this.io = this.io || new IntersectionObserver((es) => es.forEach((e) => { const Q = this.P.find((q) => q && q.cv === e.target); if (Q && e.isIntersecting && !Q.seen) { Q.seen = true; this.form(Q); } }), { threshold: 0.25 });
      this.io.observe(cv);
    } else P.seen = true;
  }
  build(P) { // sample the photo (cover crop) into a grid; one dot per cell
    const { cv, img } = P; if (!img.naturalWidth) return;
    const fr = cv.parentElement || cv, W = fr.clientWidth || 848, H = fr.clientHeight || 524, B = Math.max(0, this.tp('bleed', 140)), dpr = Math.min(2, window.devicePixelRatio || 1);
    cv.width = Math.round((W + 2 * B) * dpr); cv.height = Math.round((H + 2 * B) * dpr); P.B = B;
    const cols = Math.max(20, Math.round(this.tp('dotDetail', 114))), cell = W / cols, rows = Math.ceil(H / cell);
    const pos = (cv.dataset.pos || '50% 50%').split(' ').map((v) => parseFloat(v) / 100);
    const sc = Math.max(W / img.naturalWidth, H / img.naturalHeight), sw = W / sc, sh = H / sc;
    const sx = (img.naturalWidth - sw) * pos[0], sy = (img.naturalHeight - sh) * pos[1];
    const t = document.createElement('canvas'); t.width = cols; t.height = rows;
    const x = t.getContext('2d', { willReadFrequently: true }); x.drawImage(img, sx, sy, sw, sh, 0, 0, cols, rows);
    let d; try { d = x.getImageData(0, 0, cols, rows).data; } catch (e) { return; }
    const size = this.tp('dotSize', 0.52), shade = this.tp('sizeByShade', 0.1), from = this.tp('formFrom', 'Center');
    P.W = W; P.H = H; P.dpr = dpr; P.cell = cell; P.dots = []; P.crop = [sx, sy, sw, sh]; P.imgA = P.seen ? (P.imgA || 0) : 0; P.maxDl = 0; P.still = 0;
    for (let j = 0; j < rows; j++) for (let i = 0; i < cols; i++) {
      const o = (j * cols + i) * 4, r = d[o], g = d[o + 1], b = d[o + 2], l = (0.299 * r + 0.587 * g + 0.114 * b) / 255;
      const tx = (i + 0.5) * cell, ty = (j + 0.5) * cell;
      let fx, fy;
      if (from === 'Bottom') { fx = tx + (Math.random() - 0.5) * 120; fy = H + 40 + Math.random() * 200; }
      else if (from === 'Center') { const a = Math.random() * 6.283, q = Math.random() * 30; fx = W / 2 + Math.cos(a) * q; fy = H / 2 + Math.sin(a) * q; }
      else { fx = Math.random() * W * 1.4 - W * 0.2; fy = Math.random() * H * 1.4 - H * 0.2; }
      const dist = Math.hypot(tx - fx, ty - fy);
      P.dots.push({ tx, ty, fx, fy, ox: 0, oy: 0, vx: 0, vy: 0, r: (cell / 2) * size * (1 - shade * l), c: `rgb(${r},${g},${b})`, dl: Math.random() * 420 + Math.min(500, dist * 0.35) });
      P.maxDl = Math.max(P.maxDl, P.dots[P.dots.length - 1].dl);
    }
    if (!P.seen) P.t0 = Infinity;
  }
  form(P) { if (!P.dots.length) { P.wantForm = true; return; } P.t0 = performance.now(); this.kick(); }
  kick() { if (this.running) return; this.running = true; const tick = (now) => { const busy = this.step(now); if (busy) this.raf = requestAnimationFrame(tick); else this.running = false; }; this.raf = requestAnimationFrame(tick); }
  step(now) {
    const reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    const dur = this.tp('formTime', 1100), R = this.tp('pushReach', 300), F = this.tp('pushForce', 1.75), back = this.tp('springBack', 0.1), damp = this.tp('damping', 0.82);
    const shape = this.tp('dotShape', 'Circle'); let busy = false;
    for (const P of this.P) {
      if (!P || !P.dots.length) continue;
      const ctx = P.cv.getContext('2d'), B = P.B || 0; ctx.setTransform(P.dpr, 0, 0, P.dpr, B * P.dpr, B * P.dpr); ctx.clearRect(-B, -B, P.W + 2 * B, P.H + 2 * B);
      if (P.t0 === Infinity) continue; // not on screen yet: stays empty until it scrolls in
      const el = now - P.t0, R2 = R * R, hover = P.mx > -1e3; P.moving = false;
      const dotsA = 1 - (P.imgA || 0);
      for (const q of P.dots) {
        let u = reduce ? 1 : Math.max(0, Math.min(1, (el - q.dl) / dur)); if (u < 1) busy = true;
        const e = u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2;
        const bx = q.fx + (q.tx - q.fx) * e, by = q.fy + (q.ty - q.fy) * e;
        if (hover && !reduce) { const dx = bx + q.ox - P.mx, dy = by + q.oy - P.my, d2 = dx * dx + dy * dy; if (d2 < R2) { const dd = Math.sqrt(d2) || 1, f = (1 - dd / R) * F; q.vx += (dx / dd) * f * 2; q.vy += (dy / dd) * f * 2; } }
        q.vx = (q.vx - q.ox * back) * damp; q.vy = (q.vy - q.oy * back) * damp; q.ox += q.vx; q.oy += q.vy;
        if (Math.abs(q.ox) + Math.abs(q.oy) > 0.2) { busy = true; P.moving = true; }
        const x = bx + q.ox, y = by + q.oy, rr = q.r * (0.25 + 0.75 * e);
        if (rr < 0.3 || dotsA <= 0.001) continue;
        ctx.fillStyle = q.c; ctx.globalAlpha = Math.min(1, 0.15 + u * 1.2) * dotsA;
        if (shape === 'Square') ctx.fillRect(x - rr, y - rr, rr * 2, rr * 2);
        else { ctx.beginPath(); if (shape === 'Rounded square' && ctx.roundRect) ctx.roundRect(x - rr, y - rr, rr * 2, rr * 2, rr * 0.45); else ctx.arc(x, y, rr, 0, 6.2832); ctx.fill(); }
      }
      ctx.globalAlpha = 1;
      // once every dot has landed (and nothing is pushed), the dots melt into the full photo; hovering breaks it back into dots
      P.still = P.moving ? 0 : (P.still || 0) + 1; // hysteresis: only melt into the photo after ~10 calm frames
      const formed = reduce || el > P.maxDl + dur + 150, want = formed && !hover && (P.still > 10 || P.imgA > 0.5) && this.tp('settleToPhoto', true) !== false ? 1 : 0;
      const dt = Math.min(50, Math.max(0, now - (P.last || now))), fade = Math.max(60, this.tp('photoFade', 600)); P.last = now;
      P.imgA = want > P.imgA ? Math.min(1, P.imgA + dt / fade) : Math.max(0, P.imgA - dt / (fade * 0.35));
      if (P.imgA > 0.001) { // the settled photo stays inside the frame, with its rounded corners
        ctx.save(); ctx.beginPath(); if (ctx.roundRect) ctx.roundRect(0, 0, P.W, P.H, this.tp('radius', 6)); else ctx.rect(0, 0, P.W, P.H); ctx.clip();
        ctx.globalAlpha = P.imgA; ctx.drawImage(P.img, P.crop[0], P.crop[1], P.crop[2], P.crop[3], 0, 0, P.W, P.H); ctx.restore(); ctx.globalAlpha = 1; }
      if (P.imgA !== want || (this.tp('settleToPhoto', true) !== false && !hover && P.imgA < 1)) busy = true; // keep ticking until it has melted into the photo
      if (hover) busy = true;
    }
    return busy;
  }
  renderVals() {
    const s = this.sig();
    if (s !== this.lastSig) { const first = this.lastSig === undefined; this.lastSig = s; if (!first) setTimeout(() => { this.P.forEach((P) => P && P.img.complete && (this.build(P), P.seen && (P.t0 = performance.now() - 1e6))); this.kick(); }, 0); }
    else setTimeout(() => this.kick(), 0);
    const v = { bg: this.tp('background', '#ffffff'), mr: this.tp('radius', 6) + 'px', ob: this.tp('openSize', 104) + 'px', bleed: this.tp('bleed', 140) + 'px', ot: String(this.tp('openTint', 0.62)), noop: (e) => { if (e && e.preventDefault) e.preventDefault(); },
      replay: () => this.P.forEach((P) => { if (!P) return; this.build(P); P.seen = true; this.form(P); }) };
    for (let i = 0; i < 3; i++) v['cv' + i] = this.refFns[i];
    return v;
  }
}
'''
PROPS = {
    'dotDetail': {"editor": "range", "default": 114, "min": 30, "max": 180, "step": 2, "section": "Dots"},
    'dotSize': {"editor": "range", "default": 0.52, "min": 0.3, "max": 1.4, "step": 0.02, "unit": "×", "section": "Dots"},
    'sizeByShade': {"editor": "range", "default": 0.1, "min": 0, "max": 0.9, "step": 0.05, "section": "Dots"},
    'dotShape': {"editor": "enum", "options": ["Circle", "Rounded square", "Square"], "default": "Circle", "section": "Dots"},
    'formFrom': {"editor": "enum", "options": ["Scatter", "Bottom", "Center"], "default": "Center", "section": "Form in"},
    'formTime': {"editor": "int", "default": 1100, "min": 200, "max": 3000, "step": 50, "unit": "ms", "section": "Form in"},
    'pushReach': {"editor": "int", "default": 300, "min": 20, "max": 300, "unit": "px", "section": "Hover push"},
    'pushForce': {"editor": "range", "default": 1.75, "min": 0, "max": 4, "step": 0.05, "section": "Hover push"},
    'springBack': {"editor": "range", "default": 0.1, "min": 0.02, "max": 0.4, "step": 0.01, "section": "Hover push"},
    'damping': {"editor": "range", "default": 0.82, "min": 0.5, "max": 0.97, "step": 0.01, "section": "Hover push"},
    'settleToPhoto': {"editor": "boolean", "default": True, "section": "Form in"},
    'photoFade': {"editor": "int", "default": 600, "min": 100, "max": 2000, "step": 50, "unit": "ms", "section": "Form in"},
    'openSize': {"editor": "int", "default": 104, "min": 64, "max": 180, "unit": "px", "section": "Open button"},
    'openTint': {"editor": "range", "default": 0.62, "min": 0, "max": 1, "step": 0.01, "section": "Open button"},
    'bleed': {"editor": "int", "default": 140, "min": 0, "max": 300, "unit": "px", "section": "Hover push"},
    'background': {"editor": "color", "default": "#ffffff", "section": "Look"},
    'radius': {"editor": "int", "default": 6, "min": 0, "max": 40, "unit": "px", "section": "Look"},
}
HTML = f'''<!doctype html>
<html>
<head><meta charset="utf-8"><script src="./support.js"></script></head>
<body>
<!-- Photo dots lab: photos drawn as dots that form in on scroll and push away from the cursor. For tuning before the stuart.re-style page. -->
<x-dc>
  <helmet>
    <style>
      html, body {{ margin: 0; height: 100%; }}
    </style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..700&amp;display=swap">
<style>{CSS}</style>
  </helmet>
<div class="dl-root" style="--bg: {{{{bg}}}}; --mr: {{{{mr}}}}; --ob: {{{{ob}}}}; --ot: {{{{ot}}}}; --bleed: {{{{bleed}}}}"><svg class="dl-defs" width="0" height="0" aria-hidden="true" focusable="false"><filter id="dl-glass" x="0%" y="0%" width="100%" height="100%" filterUnits="objectBoundingBox"><feTurbulence type="fractalNoise" baseFrequency="0.02 0.02" numOctaves="2" seed="7" result="noise"></feTurbulence><feGaussianBlur in="noise" stdDeviation="2" result="soft"></feGaussianBlur><feDisplacementMap in="SourceGraphic" in2="soft" scale="40" xChannelSelector="R" yChannelSelector="G"></feDisplacementMap></filter></svg>
  <p class="dl-k">LAB</p>
  <h1 class="dl-h">Photo dots</h1>
  <p class="dl-p">Each photo is drawn as dots, like the homepage hero. The dots fly in and form the picture when it scrolls into view, then melt into the full photo. Hover and it breaks back into dots that push away from your cursor; move off and it becomes the photo again. Tune it in Tweaks, then we&#8217;ll move it onto the stuart.re-style page.</p>
  <div class="dl-bar"><button type="button" class="dl-btn" onClick="{{{{replay}}}}">Replay</button></div>
  <div class="dl-stack">{figs}</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{json.dumps(PROPS).replace("&", "&amp;").replace("'", "&#39;")}'>
{JS.strip()}
</script>
</body>
</html>
'''
open(out, 'w').write(HTML); print('ok', len(HTML))
