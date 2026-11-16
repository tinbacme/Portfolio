"""Stuart page: swap the V6 pill nav for V9 (spine + liquid-glass tiles, title and years on the selected item, cursor light),
and take the dates off the rows since the nav now carries them. usage: stuartv9.py <TinHome-Stuart.dc.html> <Piece-navvars.dc.html>"""
import sys, re
p, nvp = sys.argv[1], sys.argv[2]; s = open(p).read(); nv = open(nvp).read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:90], s.count(old)); s = s.replace(old, new)
L = nv.split('\n')
def block(start, end):  # lines from the one starting with `start` up to (not incl.) the one starting with `end`
    i = next(k for k, l in enumerate(L) if l.startswith(start)); j = next(k for k, l in enumerate(L) if k > i and l.startswith(end))
    return '\n'.join(L[i:j])
css = '\n'.join([
    next(l for l in L if l.startswith('.nv-2u{')), next(l for l in L if l.startswith('.nv-cap{')),
    block('.l9{position', '/* V6 lens in the same'), block('/* waving hand', '/* V7: year ledger */')])
css = css.replace('.t6-lens .gl-light{z-index:1}\n', '')
glass9 = re.search(r'<filter id="nv-glass9".*?</filter>', nv, re.S).group(0)
a = nv.index('<nav class="l9"'); b = nv.index('</nav>', a); inner = nv[nv.index('>', a) + 1:b]
inner = inner.replace('style="transform: translateY({{iY}})"', 'style="transform: translateY({{svY}})"')
for k in range(6):
    go = '{{goHome}}' if k == 5 else '{{svGo%d}}' % k
    inner = inner.replace('<a class="{{I%d}}" ' % k, '<a class="{{sv%d}}" aria-current="{{svC%d}}" ' % (k, k)).replace('onClick="{{pickI%d}}"' % k, 'onClick="%s"' % go)
assert '{{I' not in inner and 'pickI' not in inner
hrefs = re.findall(r'<a class="\{\{sv\d\}\}"[^>]*href="(#[^"]+)"', inner); assert hrefs == ['#microsoft', '#salesforce', '#uo-teach', '#2u', '#uo-bs', '#top'], hrefs
inner = inner.replace('href="#top" ', 'href="#top" aria-label="Let&#39;s Chat, back to the top" ', 1)
# swap the nav
a = s.index('<nav class="sv-nav"'); b = s.index('</nav>', a) + len('</nav>')
old = s[a:b]
defs = re.search(r'<svg class="st-defs".*?</svg>', old, re.S).group(0).replace('</svg>', glass9 + '</svg>')
s = s[:a] + '<nav class="sv-nav l9" aria-label="Jump to a role" ref="{{navRef}}">' + defs + inner + '</nav>' + s[b:]
CSS = '''
/* nav: V9 from the nav variations - a spine with liquid-glass tiles; the current role gets dark glass, its name and years */
''' + css + '''
.sv-nav.l9{position:fixed;left:auto;top:var(--navTop,298px);z-index:20;margin-left:-16px;gap:8px;display:flex;flex-direction:column;align-items:flex-start}
.sv-nav.l9 a{height:44px;padding:0;border-radius:0;gap:0}
.sv-nav.l9 a:focus-visible{outline:none}
.sv-nav.l9 a:focus-visible .l9-tile{outline:2px solid #0099ff;outline-offset:2px}
/* the dates now live in the nav: rows keep their three columns with the first one empty */
.st-row>.st-stack{grid-column:2}.st-row>.st-info{grid-column:3}
'''
rep('</style>', CSS + '</style>')
# take the dates off the rows
n0 = len(re.findall(r'<p class="st-year"[^>]*>[^<]*</p>', s)); assert n0 == 6, n0
s = re.sub(r'<p class="st-year"[^>]*>[^<]*</p>', '', s)
# marker position + the cursor light across the page
rep("      navRef: (el) => { this.navEl = el; },\n", "      navRef: (el) => { this.navEl = el; },\n      svY: ((this.state.nav ?? 5) * 52) + 'px',\n"
    "      glassLight: (e) => { const nav = this.navEl; if (!nav) return; nav.querySelectorAll('.gl-light').forEach((l) => { const r = l.getBoundingClientRect(); if (!r.width) return;\n"
    "        const x = e.clientX - r.left, y = e.clientY - r.top, cx = Math.max(-120, Math.min(r.width + 120, x)), cy = Math.max(-120, Math.min(r.height + 120, y));\n"
    "        const near = Math.max(0, 1 - Math.hypot(x - r.width / 2, y - r.height / 2) / 520);\n"
    "        l.style.setProperty('--lx', cx.toFixed(1) + 'px'); l.style.setProperty('--ly', cy.toFixed(1) + 'px'); l.style.setProperty('--li', (0.2 + 0.6 * near * near).toFixed(3)); }); },\n"
    "      glassDark: () => { const nav = this.navEl; if (nav) nav.querySelectorAll('.gl-light').forEach((l) => l.style.setProperty('--li', '0')); },\n")
rep('<div class="st-root" ref="{{rootRef}}"', '<div class="st-root" ref="{{rootRef}}" onPointerMove="{{glassLight}}" onPointerLeave="{{glassDark}}"')
open(p, 'w').write(s); print('ok')
