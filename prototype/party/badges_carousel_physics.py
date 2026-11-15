"""Carousel v2: cards ride along a sagging (curved) string and swing like pendulums as they slide; hover nudges a card.
usage: carousel2.py <party-desktop.dc.html> (carousel version, any card count)"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:100], s.count(old)); s = s.replace(old, new)

rep('<div class="bd-track" style="transform: {{bdX}}; transition: {{bdTrans}}">', '<div class="bd-track" ref="{{bdTrackRef}}" onPointerOver="{{bdPoke}}">')
rep('<svg class="bd-wire" viewBox="0 0 1000 24" preserveAspectRatio="none" aria-hidden="true" style="height: 24px"><path d="M0,12 L1000,12" fill="none" vector-effect="non-scaling-stroke"></path></svg>',
    '<svg class="bd-wire" viewBox="0 0 1000 {{bdWireH}}" preserveAspectRatio="none" aria-hidden="true" style="height: {{bdWireHpx}}"><path d="{{bdWirePath}}" fill="none" vector-effect="non-scaling-stroke"></path></svg>')
rep('class="bd-wrap bd-car {{bdSwayClass}} {{bdMovingClass}}"', 'class="bd-wrap bd-car {{bdSwayClass}}"')
rep('.bd-moving .bd-swing{animation:bdSwing 1.6s cubic-bezier(.25,.6,.35,1) both !important}\n',
    '.bd-car .bd-swing{animation:none !important;transform:rotate(calc(var(--t) * var(--tk,1) + var(--sw,0deg)))}\n')

N = int(re.search(r"bdGo\(d\) \{[^\n]*\n    const n = (\d+),", s).group(1))
a = s.index("  bdGo(d) {"); b = s.index("  bdToggle(k) {")
s = s[:a] + ("""  bdGo(d) { // slide one job along the string; the frame loop eases the track and swings the cards
    this.bdIdx = (this.bdIdx || 0) + d;
    const reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.bdTw = { from: this.bdPos ?? this.bdTarget(this.bdIdx - d), to: this.bdTarget(this.bdIdx), t0: performance.now(), dur: reduce ? 1 : this.tp('slideMs', 1100) };
  }
  bdTarget(i) { return this.tp('carouselStart', 150) - (%(N)d + i) * (this.tp('badgeWidth', 300) + this.tp('badgeGap', 64)); }
  bdStart() {
    clearInterval(this.tBdAuto); cancelAnimationFrame(this.bdRaf);
    const reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    this.bdIdx = 0; this.bdPos = null; this.bdTh = []; this.bdOm = []; this.bdT = performance.now(); this.bdVel = 0;
    const n = %(N)d, ease = (u) => (u < 0.5 ? 4 * u * u * u : 1 - Math.pow(-2 * u + 2, 3) / 2);
    const tick = (now) => {
      this.bdRaf = requestAnimationFrame(tick);
      const tr = this.bdTrackEl; if (!tr || !tr.isConnected) return;
      const dt = Math.min(0.05, Math.max(0.001, (now - this.bdT) / 1000)); this.bdT = now;
      const step = this.tp('badgeWidth', 300) + this.tp('badgeGap', 64);
      let pos = this.bdPos ?? this.bdTarget(this.bdIdx);
      const T = this.bdTw;
      if (T) { const u = Math.min(1, (now - T.t0) / T.dur); pos = T.from + (T.to - T.from) * ease(u); if (u >= 1) this.bdTw = null; }
      else if (this.bdIdx >= n || this.bdIdx < 0) { // seamless wrap once settled: jump a full set of six, keep each card's swing
        const sh = this.bdIdx >= n ? n : -n; this.bdIdx -= sh; pos += sh * step;
        const th = this.bdTh, om = this.bdOm, kids = tr.children.length;
        this.bdTh = Array.from({ length: kids }, (_, j) => th[j + sh] ?? 0); this.bdOm = Array.from({ length: kids }, (_, j) => om[j + sh] ?? 0);
      }
      const vel = this.bdPos == null ? 0 : (pos - this.bdPos) / dt, acc = (vel - this.bdVel) / dt; this.bdVel = vel; this.bdPos = pos;
      tr.style.transform = `translate3d(${pos.toFixed(2)}px, 0, 0)`;
      const W = tr.parentElement ? tr.parentElement.clientWidth : 1440, sag = this.tp('stringSag', 28), amt = reduce ? 0 : this.tp('swingAmount', 1);
      const sway = this.tp('badgeSway', true) === false || reduce ? 0 : 1, t = now / 1000;
      const kids = tr.children;
      for (let j = 0; j < kids.length; j++) {
        const el = kids[j], x = pos + j * step + step / 2, f = Math.max(0, Math.min(1, x / W));
        el.style.setProperty('--pin', (8 + 4 * sag * f * (1 - f)).toFixed(1) + 'px');
        // pendulum: the pivot's acceleration kicks the card back, a spring pulls it home, damping settles it
        let th = this.bdTh[j] || 0, om = this.bdOm[j] || 0;
        om += (-16 * th - 2.4 * om - 0.05 * amt * Math.max(-4000, Math.min(4000, acc))) * dt; th += om * dt;
        this.bdTh[j] = th; this.bdOm[j] = om;
        const idle = sway * 0.9 * Math.sin(t * 1.15 + (j %% n) * 1.7);
        el.style.setProperty('--sw', (th + idle).toFixed(2) + 'deg');
      }
    };
    this.bdRaf = requestAnimationFrame(tick);
    if (reduce) return;
    this.tBdAuto = setInterval(() => {
      if (this.tp('autoRotate', true) === false || this.bdHeld || this.bdTw) return;
      if (this.state.bdFlip && Object.values(this.state.bdFlip).some(Boolean)) return; // let people read a flipped card
      this.bdGo(1);
    }, Math.max(1.5, this.tp('autoSecs', 3.5)) * 1000);
  }
""" % {'N': N}) + s[b:]
rep("  componentWillUnmount() { clearInterval(this.tBdAuto); clearTimeout(this.tBd); ", "  componentWillUnmount() { clearInterval(this.tBdAuto); clearTimeout(this.tBd); cancelAnimationFrame(this.bdRaf); ")
rep("bdPrev: () => this.bdGo(-1), bdNext: () => this.bdGo(1),",
    "bdPrev: () => this.bdGo(-1), bdNext: () => this.bdGo(1), bdTrackRef: (el) => { this.bdTrackEl = el; },\n"
    "      bdPoke: (e) => { const h = e.target && e.target.closest && e.target.closest('.bd-hang'); if (!h || h === this.bdLastPoke || !this.bdTrackEl) return; this.bdLastPoke = h; const j = Array.prototype.indexOf.call(this.bdTrackEl.children, h); if (j >= 0) this.bdOm[j] = (this.bdOm[j] || 0) + 26 * this.tp('swingAmount', 1) * (Math.random() < 0.5 ? -1 : 1); },")

mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(mm.group(2)))
add = {'stringSag': {"editor": "range", "default": 28, "min": 0, "max": 90, "step": 1, "unit": "px", "section": "Badges"},
       'swingAmount': {"editor": "range", "default": 1, "min": 0, "max": 3, "step": 0.05, "unit": "×", "section": "Badges"}}
if 'slideMs' in P: P['slideMs']['default'] = 1100
new = {}
for k, v in P.items():
    if k in add: continue
    new[k] = v
    if k == 'slideMs': new.update(add)
assert 'stringSag' in new and 'swingAmount' in new
attr = json.dumps(new, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:mm.start()] + "data-props='" + attr + "'>" + s[mm.end():]
open(p, 'w').write(s)
mm = re.search(r"data-props=(['\"])(.*?)\1>\n(.*?)</script>", s, re.S)
open('/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/c2_logic.js', 'w').write('class DCLogic{}\n' + mm.group(3))
print('ok', N)
