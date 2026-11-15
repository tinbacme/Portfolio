"""Carousel: drop the big arrow buttons; add a mini pager under the cards (black bar = current job, circles = the rest,
small chevrons either side). Blurred ends always visible again.  usage: dots.py <party-desktop.dc.html>"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:100], s.count(old)); s = s.replace(old, new)

# 1) remove the two round arrow buttons
s, k = re.subn(r'<button type="button" class="bd-nav bd-nav-l"[^>]*>.*?</button><button type="button" class="bd-nav bd-nav-r"[^>]*>.*?</button>', '', s, flags=re.S)
assert k == 1, k
# 2) blurred ends: back to always on (drop the hover-only block)
a = s.find('\n/* ends: blur + arrow show only while hovering that side */')
if a >= 0:
    b = s.index('@media (hover: none){.bd-car .bd-edge,.bd-car .bd-nav{opacity:1}.bd-car .bd-edge{pointer-events:none}}\n', a)
    s = s[:a] + s[b + len('@media (hover: none){.bd-car .bd-edge,.bd-car .bd-nav{opacity:1}.bd-car .bd-edge{pointer-events:none}}\n'):]
# 3) pager under the cards
CH = lambda d: f'<svg viewBox="0 0 24 24" width="14" height="14" fill="none" aria-hidden="true"><path d="{d}" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
PAGER = ('<div class="bd-pager">'
         '<button type="button" class="bd-chev" aria-label="Previous job" onClick="{{bdPrev}}">' + CH('M15 5 8 12l7 7') + '</button>'
         '<sc-for list="{{bdDots}}" as="d" hint-placeholder-count="7"><button type="button" class="{{d.cls}}" aria-label="{{d.label}}" aria-current="{{d.current}}" onClick="{{d.go}}"></button></sc-for>'
         '<button type="button" class="bd-chev" aria-label="Next job" onClick="{{bdNext}}">' + CH('m9 5 7 7-7 7') + '</button>'
         '</div>')
i = s.index('<div class="bd-viewport">'); j = s.index('\n    </div></div>\n', i) + len('\n    </div></div>')
s = s[:j] + '\n    ' + PAGER + s[j:]
m = re.search(r'(<section class="bd-wrap bd-car[^"]*"[^>]*style=")([^"]*)(")', s)
s = s[:m.start()] + m.group(1) + m.group(2) + '; --dot: {{bdDot}}; --bar: {{bdBar}}' + m.group(3) + s[m.end():]
CSS = '''
/* mini pager: black bar = current job, circles = the others */
.bd-pager{position:relative;z-index:4;display:flex;align-items:center;justify-content:center;gap:10px;margin-top:6px}
.bd-dot{position:relative;flex:none;width:var(--dot,6px);height:var(--dot,6px);padding:0;border:0;border-radius:999px;background:rgba(20,20,20,.22);cursor:pointer;transition:width .5s cubic-bezier(.6,0,.2,1),background-color .3s}
.bd-dot::after{content:"";position:absolute;inset:-9px -5px}
.bd-dot:hover{background:rgba(20,20,20,.45)}
.bd-dot.on{width:var(--bar,22px);background:#141414}
.bd-dot:focus-visible,.bd-chev:focus-visible{outline:2px solid #3078e7;outline-offset:3px}
.bd-chev{display:grid;place-items:center;width:26px;height:26px;padding:0;border:0;border-radius:50%;background:none;color:#141414;opacity:.5;cursor:pointer;transition:opacity .2s,background-color .2s}
.bd-chev:hover{opacity:1;background:rgba(20,20,20,.06)}
.party .bd-dot{background:rgba(255,255,255,.3)}.party .bd-dot:hover{background:rgba(255,255,255,.55)}.party .bd-dot.on{background:#fff}
.party .bd-chev{color:#fff}.party .bd-chev:hover{background:rgba(255,255,255,.1)}
'''
s = s.replace('</style>\n</helmet>', CSS + '</style>\n</helmet>', 1)
# 4) logic: current job in state for the pager, jump to any job
N = int(re.search(r"const n = (\d+), ease", s).group(1))
rep("  bdGo(d) { // slide one job along the string; the frame loop eases the track and swings the cards\n    this.bdIdx = (this.bdIdx || 0) + d;",
    "  bdGo(d) { // slide one job along the string; the frame loop eases the track and swings the cards\n    this.bdIdx = (this.bdIdx || 0) + d; this.setState({ bdCur: ((this.bdIdx %% %d) + %d) %% %d });" % (N, N, N))
rep("  bdTarget(i) {", """  bdGoTo(k) { // jump to a job from the pager, the short way round
    const n = %d, cur = (((this.bdIdx || 0) %% n) + n) %% n; let d = k - cur;
    if (d > n / 2) d -= n; if (d < -n / 2) d += n; if (d) this.bdGo(d);
  }
  bdTarget(i) {""" % N)
rep("bdPrev: () => this.bdGo(-1), bdNext: () => this.bdGo(1),",
    "bdPrev: () => this.bdGo(-1), bdNext: () => this.bdGo(1),\n"
    "      bdDot: this.tp('dotSize', 6) + 'px', bdBar: this.tp('barWidth', 22) + 'px',\n"
    "      bdDots: Array.from({ length: %d }, (_, k) => { const on = (this.state.bdCur || 0) === k; return { cls: on ? 'bd-dot on' : 'bd-dot', current: on ? 'true' : 'false', label: 'Show job ' + (k + 1), go: () => this.bdGoTo(k) }; })," % N)
mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(mm.group(2)))
add = {'dotSize': {"editor": "range", "default": 6, "min": 2, "max": 14, "step": 1, "unit": "px", "section": "Badges"},
       'barWidth': {"editor": "range", "default": 22, "min": 5, "max": 60, "step": 1, "unit": "px", "section": "Badges"}}
new = {}
for kk, v in P.items():
    if kk in add: continue
    new[kk] = v
    if kk == 'edgeBlur': new.update(add)
assert 'dotSize' in new
attr = json.dumps(new, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:mm.start()] + "data-props='" + attr + "'>" + s[mm.end():]
open(p, 'w').write(s)
mm = re.search(r"data-props=(['\"])(.*?)\1>\n(.*?)</script>", s, re.S)
open('/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/dots_logic.js', 'w').write('class DCLogic{}\n' + mm.group(3))
print('ok', N)
