"""Badges -> one full-width string that auto-rotates through the jobs, with arrows and blurred fading edges.
Keeps each card's markup (and any edits) from the board. usage: carousel.py <board.dc.html>"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:100], s.count(old)); s = s.replace(old, new)

a = s.index('  <section class="bd-wrap'); b = s.index('</section>', a) + len('</section>')
sec = s[a:b]
open_tag = sec[:sec.index('>') + 1]
# pull out each .bd-hang block (balanced divs)
hangs = []; pos = 0
while True:
    i = sec.find('<div class="bd-hang"', pos)
    if i < 0: break
    d = 0; j = i
    for m in re.finditer(r'<div\b|</div>', sec[i:]):
        d += 1 if m.group(0).startswith('<div') else -1
        if d == 0: j = i + m.end(); break
    hangs.append(sec[i:j]); pos = j
assert len(hangs) == 6, len(hangs)
N = len(hangs)
hangs = [re.sub(r'--pin: \{\{bdPin\d\}\}', '--pin: 12px', h) for h in hangs]
copy = lambda h: h.replace('<div class="bd-hang"', '<div class="bd-hang" aria-hidden="true"', 1).replace('tabindex="0"', 'tabindex="-1"')
track = ''.join(copy(h) for h in hangs) + ''.join(hangs) + ''.join(copy(h) for h in hangs)
ARR = lambda d: f'<svg viewBox="0 0 24 24" width="20" height="20" fill="none" aria-hidden="true"><path d="{d}" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
open_tag = open_tag.replace('class="bd-wrap {{bdSwayClass}}"', 'class="bd-wrap bd-car {{bdSwayClass}} {{bdMovingClass}}" onPointerEnter="{{bdHold}}" onPointerLeave="{{bdFree}}" onFocus="{{bdHold}}" onBlur="{{bdFree}}"')
open_tag = open_tag.replace('; --rowgap: {{bdRowGap}}', '; --gap: {{bdGap}}; --edge: {{bdEdge}}; --eb: {{bdEdgeBlur}}')
assert 'bd-car' in open_tag and '--gap' in open_tag, open_tag
NEW = (open_tag + '\n'
  '    <svg class="bd-wire" viewBox="0 0 1000 24" preserveAspectRatio="none" aria-hidden="true" style="height: 24px"><path d="M0,12 L1000,12" fill="none" vector-effect="non-scaling-stroke"></path></svg>\n'
  '    <div class="bd-viewport"><div class="bd-track" style="transform: {{bdX}}; transition: {{bdTrans}}">' + track + '\n    </div></div>\n'
  '    <div class="bd-edge bd-edge-l" aria-hidden="true"><i></i><i></i><i></i><i></i></div><div class="bd-edge bd-edge-r" aria-hidden="true"><i></i><i></i><i></i><i></i></div>\n'
  '    <button type="button" class="bd-nav bd-nav-l" aria-label="Previous job" onClick="{{bdPrev}}">' + ARR('M15 5 8 12l7 7') + '</button>'
  '<button type="button" class="bd-nav bd-nav-r" aria-label="Next job" onClick="{{bdNext}}">' + ARR('m9 5 7 7-7 7') + '</button>\n'
  '  </section>')
s = s[:a] + NEW + s[b:]

CSS = r'''
/* ===== badges carousel: one string, end to end ===== */
.bd-car{padding:40px 0 120px;gap:0;--fadec:#f5f5f5}
.party .bd-car{--fadec:#0d0c12}
.bd-car .bd-wire{position:absolute;left:0;right:0;top:40px;width:100%}
.bd-viewport{position:relative;overflow-x:clip;overflow-y:visible;padding-bottom:20px}
.bd-track{display:flex;align-items:flex-start;will-change:transform}
.bd-car .bd-hang{flex:none;width:calc(var(--bw,300px) + var(--gap,64px))}
.bd-moving .bd-swing{animation:bdSwing 1.6s cubic-bezier(.25,.6,.35,1) both !important}
.bd-edge{position:absolute;top:0;bottom:0;width:var(--edge,220px);z-index:3;pointer-events:none}
.bd-edge-l{left:0}.bd-edge-r{right:0;transform:scaleX(-1)}
.bd-edge::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,var(--fadec) 0%,color-mix(in srgb,var(--fadec) 72%,transparent) 30%,transparent 100%)}
.bd-edge i{position:absolute;inset:0;-webkit-backdrop-filter:blur(var(--b));backdrop-filter:blur(var(--b))}
.bd-edge i:nth-child(1){--b:calc(var(--eb,12px) * .12);-webkit-mask:linear-gradient(90deg,#000 0 55%,transparent 100%);mask:linear-gradient(90deg,#000 0 55%,transparent 100%)}
.bd-edge i:nth-child(2){--b:calc(var(--eb,12px) * .3);-webkit-mask:linear-gradient(90deg,#000 0 38%,transparent 78%);mask:linear-gradient(90deg,#000 0 38%,transparent 78%)}
.bd-edge i:nth-child(3){--b:calc(var(--eb,12px) * .6);-webkit-mask:linear-gradient(90deg,#000 0 22%,transparent 58%);mask:linear-gradient(90deg,#000 0 22%,transparent 58%)}
.bd-edge i:nth-child(4){--b:var(--eb,12px);-webkit-mask:linear-gradient(90deg,#000 0 8%,transparent 38%);mask:linear-gradient(90deg,#000 0 8%,transparent 38%)}
.bd-nav{position:absolute;top:calc(50% - 10px);z-index:4;width:52px;height:52px;margin-top:-26px;border-radius:50%;border:0;background:#141414;color:#fff;display:grid;place-items:center;cursor:pointer;box-shadow:0 10px 24px -10px rgba(0,0,0,.5);transition:transform .25s cubic-bezier(.3,1.5,.5,1),background-color .2s}
.bd-nav:hover{transform:scale(1.08)}.bd-nav:active{transform:scale(.94)}
.bd-nav:focus-visible{outline:2px solid #3078e7;outline-offset:3px}
.bd-nav-l{left:40px}.bd-nav-r{right:40px}
.party .bd-nav{background:#f4f1ea;color:#0d0c12}
@media (prefers-reduced-motion: reduce){.bd-track{transition:none !important}.bd-moving .bd-swing{animation:none !important}}
'''
rep('</style>\n</helmet>', CSS + '</style>\n</helmet>')

# logic
m = re.search(r"this\.state = \{ i: 0,", s); assert m
s = s[:m.end()] + " bdI: 0, bdAnim: false, bdMoving: false," + s[m.end():]
rep("  bdToggle(k) {",
"""  bdGo(d) { // slide one job along the string; three copies of the six cards make the loop seamless
    const n = %d, ms = this.tp('slideMs', 900); const i = (this.state.bdI || 0) + d;
    this.setState({ bdI: i, bdAnim: true, bdMoving: true }); clearTimeout(this.tBd);
    this.tBd = setTimeout(() => { const j = this.state.bdI; this.setState({ bdMoving: false, ...(j >= n || j < 0 ? { bdI: ((j %% n) + n) %% n, bdAnim: false } : {}) }); }, ms + 40);
  }
  bdStart() {
    clearInterval(this.tBdAuto);
    const reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches; if (reduce) return;
    this.tBdAuto = setInterval(() => {
      if (this.tp('autoRotate', true) === false || this.bdHeld) return;
      if (this.state.bdFlip && Object.values(this.state.bdFlip).some(Boolean)) return; // let people read a flipped card
      this.bdGo(1);
    }, Math.max(1.5, this.tp('autoSecs', 3.5)) * 1000);
  }
  bdToggle(k) {""" % N)
rep("  componentDidMount() { ", "  componentDidMount() { this.bdStart(); ")
rep("  componentWillUnmount() { ", "  componentWillUnmount() { clearInterval(this.tBdAuto); clearTimeout(this.tBd); ")
rep("bdRowGap: this.tp('rowGap', 56) + 'px',",
    "bdGap: this.tp('badgeGap', 64) + 'px', bdEdge: this.tp('edgeWidth', 220) + 'px', bdEdgeBlur: this.tp('edgeBlur', 12) + 'px',\n"
    "      bdX: `translate3d(${this.tp('carouselStart', 150) - (%d + (this.state.bdI || 0)) * (this.tp('badgeWidth', 300) + this.tp('badgeGap', 64))}px, 0, 0)`,\n"
    "      bdTrans: this.state.bdAnim ? `transform ${this.tp('slideMs', 900)}ms cubic-bezier(.65, 0, .25, 1)` : 'none', bdMovingClass: this.state.bdMoving ? 'bd-moving' : '',\n"
    "      bdPrev: () => this.bdGo(-1), bdNext: () => this.bdGo(1), bdHold: () => { this.bdHeld = true; }, bdFree: () => { this.bdHeld = false; }," % N)

mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(mm.group(2)))
for k in ('stringSag', 'rowGap'): P.pop(k, None)
add = {
 'autoRotate': {"editor": "boolean", "default": True, "section": "Badges"},
 'autoSecs': {"editor": "range", "default": 3.5, "min": 1.5, "max": 10, "step": 0.5, "unit": "s", "section": "Badges"},
 'slideMs': {"editor": "range", "default": 900, "min": 300, "max": 2000, "step": 50, "unit": "ms", "section": "Badges"},
 'badgeGap': {"editor": "range", "default": 64, "min": 0, "max": 200, "step": 2, "unit": "px", "section": "Badges"},
 'carouselStart': {"editor": "range", "default": 150, "min": -200, "max": 600, "step": 2, "unit": "px", "section": "Badges"},
 'edgeWidth': {"editor": "range", "default": 220, "min": 0, "max": 500, "step": 5, "unit": "px", "section": "Badges"},
 'edgeBlur': {"editor": "range", "default": 12, "min": 0, "max": 40, "step": 1, "unit": "px", "section": "Badges"},
}
new = {}
for k, v in P.items():
    new[k] = v
    if k == 'badgeSway': new.update(add)
assert 'autoRotate' in new
attr = json.dumps(new, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:mm.start()] + "data-props='" + attr + "'>" + s[mm.end():]
open(p, 'w').write(s)
mm = re.search(r"data-props=(['\"])(.*?)\1>\n(.*?)</script>", s, re.S)
json.loads(html.unescape(mm.group(2)))
open('/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/car_logic.js', 'w').write('class DCLogic{}\n' + mm.group(3))
print('ok')
