"""Nav variations: match the stuart.re page's nav. Order Microsoft, Salesforce, UO, 2U, BS Industrial Design, then a waving-hand
'Let's Chat' in place of Home (still goes to #top), selected by default like the page. Glass light follows the mouse across the
whole stage, softer and wider. usage: navorder.py <Piece-navvars.dc.html>"""
import sys, re
p = sys.argv[1]; s = open(p).read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:90], s.count(old)); s = s.replace(old, new)
NEW = [1, 4, 2, 3, 5, 0]  # new position -> old index
WAVE = '<span class="nv-wave" aria-hidden="true">👋</span>'
for X in 'ABCDEFGHI':
    ms = list(re.finditer(r'<a class="\{\{%s(\d)\}\}[^"]*"[^>]*>.*?</a>' % X, s, re.S))
    assert len(ms) == 6, X
    items = {int(m.group(1)): m.group(0) for m in ms}
    out = []
    for pos, old in enumerate(NEW):
        a = items[old].replace('{{%s%d}}' % (X, old), '{{%s%d}}' % (X, pos)).replace('{{pick%s%d}}' % (X, old), '{{pick%s%d}}' % (X, pos))
        if old == 0:
            a = re.sub(r'<span class="nv-tin"[^>]*>tin</span>', WAVE, a)
            a = a.replace('>Home<', '>Let&#39;s Chat<').replace('aria-label="Home"', 'aria-label="Let&#39;s Chat"').replace('<span class="l9-yr">Tin Le</span>', '<span class="l9-yr">Say hi</span>')
        if X == 'E': a = re.sub(r'<span class="n5-n">\d\d</span>', '<span class="n5-n">%02d</span>' % (pos + 1), a)
        out.append(a)
    # items in a variation are contiguous apart from what sits between them (nothing but the anchors): rebuild the run
    start, end = ms[0].start(), ms[-1].end()
    between = s[start:end]
    for m in ms: between = between.replace(m.group(0), '\x00', 1)
    assert set(between) <= {'\x00'}, (X, between.replace('\x00', '')[:200])
    s = s[:start] + ''.join(out) + s[end:]
rep("this.state = { A: 0, B: 0, C: 0, D: 0, E: 0, F: 0, G: 0, H: 0, I: 0 };", "this.state = { A: 5, B: 5, C: 5, D: 5, E: 5, F: 5, G: 5, H: 5, I: 5 };")
rep("v.fW = [101, 146, 208, 78, 135, 203][st.F] + 'px';", "v.fW = [146, 135, 208, 78, 203, WAVEW][st.F] + 'px';")
CSS = r'''
/* waving hand in place of Home, as on the stuart.re page */
.nv-wave{display:inline-block;font:19px/1 'Apple Color Emoji','Segoe UI Emoji','Noto Color Emoji',sans-serif;transform-origin:70% 80%}
nav a:hover .nv-wave,nav a.on .nv-wave{animation:nvWave 1.2s ease-in-out 1}
@keyframes nvWave{0%,100%{transform:rotate(0)}15%{transform:rotate(16deg)}30%{transform:rotate(-8deg)}45%{transform:rotate(14deg)}60%{transform:rotate(-4deg)}75%{transform:rotate(10deg)}}
@media (prefers-reduced-motion: reduce){.nv-wave{animation:none!important}}
'''
rep('/* light that follows the mouse:', CSS + '/* light that follows the mouse:')
# light: subtler, wider, and driven from the whole stage, not just the nav
rep("rgba(255,255,255,.7) 0%,rgba(255,255,255,.22) 35%,rgba(255,255,255,0) 70%)}", "rgba(255,255,255,.42) 0%,rgba(255,255,255,.14) 40%,rgba(255,255,255,0) 72%)}")
rep("circle var(--lr,70px) at", "circle var(--lr,130px) at")
rep(".l9-tile .gl-light{z-index:-1;--lr:48px}", ".l9-tile .gl-light{z-index:-1;--lr:80px}")
rep('<div class="nv-stage st-white"><nav class="t6" aria-label="Site, version 6" style="--fc: {{fColor}}" onPointerMove="{{glassLight}}" onPointerLeave="{{glassDark}}">',
    '<div class="nv-stage st-white" onPointerMove="{{glassLight}}" onPointerLeave="{{glassDark}}"><nav class="t6" aria-label="Site, version 6" style="--fc: {{fColor}}">')
rep('<div class="nv-stage st-soft"><nav class="l9" aria-label="Site, version 9" onPointerMove="{{glassLight}}" onPointerLeave="{{glassDark}}">',
    '<div class="nv-stage st-soft" onPointerMove="{{glassLight}}" onPointerLeave="{{glassDark}}"><nav class="l9" aria-label="Site, version 9">')
rep("cx = Math.max(-40, Math.min(r.width + 40, x)), cy = Math.max(-40, Math.min(r.height + 40, y));", "cx = Math.max(-120, Math.min(r.width + 120, x)), cy = Math.max(-120, Math.min(r.height + 120, y));")
rep("near = Math.max(0, 1 - d / 220);", "near = Math.max(0, 1 - d / 520);")
rep("(0.25 + 0.75 * near).toFixed(3)", "(0.2 + 0.6 * near * near).toFixed(3)")
rep("move each glass piece's glare toward the cursor", "move each glass piece's glare toward the cursor, anywhere over the stage")
open(p, 'w').write(s); print('ok')
