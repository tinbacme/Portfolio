"""Nav variations: (1) add the BS Industrial Design item (Oregon logo + graduation cap) to every variation, matching the stuart.re dock;
(2) add V9 'Spine, liquid glass': glass tiles, a dark marker slides down the spine and then the branch fills dark across to the tile.
usage: navvars3.py <Piece-navvars.dc.html>"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:90], s.count(old)); s = s.replace(old, new)
UO = '<img src="/_blob/00e0e1ec841a28c4e0055e4a6738e6b1"'
CAP = ('<svg class="nv-cap" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 1.5 8 12 13l10.5-5z" fill="currentColor"></path>'
       '<path d="M6 10.6V15c0 1.7 2.7 3 6 3s6-1.3 6-3v-4.4L12 13.5z" fill="currentColor"></path>'
       '<path d="M21 8.4v5.2" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"></path><circle cx="21" cy="14.6" r="1.3" fill="currentColor"></circle></svg>')

# (1) BS Industrial Design item after Salesforce in each variation
for X in 'ABCDEFGH':
    m = re.search(r'<a class="\{\{%s2\}\}[^"]*"[^>]*>.*?</a>' % X, s, re.S)
    item = m.group(0)
    new = (item.replace('{{%s2}}' % X, '{{%s5}}' % X).replace('pick%s2' % X, 'pick%s5' % X).replace('#uo-teach', '#uo-bs')
               .replace('University of Oregon', 'BS Industrial Design'))
    if X == 'E': new = new.replace('<span class="n5-n">03</span>', '<span class="n5-n">06</span>')
    if X == 'G': new = new.replace('{{G5}}"', '{{G5}} g7-past"').replace('2023&#8211;now', '2014&#8211;18')
    if UO in new:  # put a little graduation cap on the Oregon logo
        i = new.index(UO); j = new.index('>', i) + 1
        new = new[:j] + CAP + new[j:]
    m4 = re.search(r'<a class="\{\{%s4\}\}[^"]*"[^>]*>.*?</a>' % X, s, re.S)
    s = s[:m4.end()] + new + s[m4.end():]
rep("for (let i = 0; i < 5; i++) {", "for (let i = 0; i < 6; i++) {")

# (2) V9: spine in liquid glass
G = 'l9'
LOGO = ['<span class="nv-tin">tin</span>',
        '<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><rect x="0" y="0" width="9" height="9" fill="#f25022"></rect><rect x="11" y="0" width="9" height="9" fill="#7fba00"></rect><rect x="0" y="11" width="9" height="9" fill="#00a4ef"></rect><rect x="11" y="11" width="9" height="9" fill="#ffb900"></rect></svg>',
        UO + ' alt="" width="20" height="17">',
        '<span class="nv-2u">2U</span>',
        '<img src="/_blob/ac43d25c19be4e522f4bd492e1c090ab" alt="" width="24" height="17">',
        UO + ' alt="" width="20" height="17">' + CAP]
ITEMS = [('Home', '#top'), ('Microsoft AI', '#microsoft'), ('University of Oregon', '#uo-teach'), ('2U', '#2u'), ('Salesforce', '#salesforce'), ('BS Industrial Design', '#uo-bs')]
rows = ''.join(f'<a class="{{{{I{i}}}}}" href="{h}" onClick="{{{{pickI{i}}}}}"><span class="l9-br" aria-hidden="true"></span><span class="l9-tile"><span class="l9-fx" aria-hidden="true"></span><span class="l9-ic">{LOGO[i]}</span></span><span class="l9-tx">{l}</span></a>'
               for i, (l, h) in enumerate(ITEMS))
V9 = ('\n  <section class="nv-col nv-row2"><p class="nv-k">V9</p><h2 class="nv-t">Spine, liquid glass</h2>'
      '<p class="nv-s">V2 in glass. The dark marker slides down the spine, and once it lands the branch fills dark across to that tile, which turns to dark glass.</p>'
      '<div class="nv-stage st-soft"><span class="l9-blob" style="left: 150px; top: 40px; width: 180px; height: 140px; background: #f6d3c4" aria-hidden="true"></span>'
      '<span class="l9-blob" style="left: 40px; top: 220px; width: 160px; height: 150px; background: #cfe3d4" aria-hidden="true"></span>'
      '<span class="l9-blob" style="left: 210px; top: 300px; width: 140px; height: 120px; background: #d5e3ff" aria-hidden="true"></span>'
      f'<nav class="l9" aria-label="Site, version 9"><span class="l9-spine" aria-hidden="true"></span><span class="l9-mark" aria-hidden="true" style="transform: translateY({{{{iY}}}})"></span>{rows}</nav></div></section>')
rep('</section>\n</div>\n</x-dc>', '</section>' + V9 + '\n</div>\n</x-dc>')
CSS = r'''
/* graduation cap on the BS Industrial Design marks */
.l1-ic,.l2-tile,.l3-ic,.l4-ic,.t6-ic,.l9-ic{position:relative}
.nv-cap{position:absolute;top:-5px;right:-7px;width:12px;height:12px;transform:rotate(14deg);color:#2b2b2d;pointer-events:none}
.l3 .nv-cap,.l4 .nv-cap{color:#fff}
.l8 .nv-cap{color:#2b2b2d}

/* V9: spine in liquid glass; the branch fills dark once the marker lands */
.st-soft{background:#fbfbfb;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}
.l9-blob{position:absolute;border-radius:50%;filter:blur(28px);opacity:.85;pointer-events:none}
.l9{position:absolute;left:28px;top:44px;display:flex;flex-direction:column;gap:8px}
.l9-spine{position:absolute;left:0;top:22px;bottom:22px;width:1.5px;border-radius:1px;background:rgba(0,0,0,.12)}
.l9-mark{position:absolute;left:-1px;top:4px;width:3.5px;height:36px;border-radius:2px;background:#141414;transition:transform .45s cubic-bezier(.6,0,.2,1)}
.l9 a{position:relative;display:flex;align-items:center;height:44px}
.l9-br{position:relative;flex:none;width:18px;height:1.5px;background:rgba(0,0,0,.12);overflow:hidden}
.l9-br::after{content:"";position:absolute;inset:0;background:#141414;transform:scaleX(0);transform-origin:left;transition:transform .18s ease}
.l9 a.on .l9-br::after{transform:scaleX(1);transition:transform .28s cubic-bezier(.3,.8,.3,1) .42s}
.l9-tile{position:relative;flex:none;display:grid;place-items:center;width:40px;height:40px;border-radius:12px;isolation:isolate;box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.9),inset -1px -1px 1px rgba(255,255,255,.55),inset 0 0 0 1px rgba(0,0,0,.06),0 6px 16px -8px rgba(0,0,0,.25);transition:box-shadow .3s .5s}
.l9-fx{position:absolute;inset:0;z-index:-1;border-radius:inherit;background:rgba(255,255,255,.5);-webkit-backdrop-filter:blur(8px) saturate(1.7);backdrop-filter:blur(8px) saturate(1.7);backdrop-filter:url(#nv-glass) blur(8px) saturate(1.7);transition:background-color .3s ease .5s}
.l9-ic{display:grid;place-items:center;color:#000;transition:filter .3s ease .5s}
.l9-tx{margin-left:12px;font:500 15px/1 Inter,sans-serif;color:#8a8a8a;white-space:nowrap;transition:color .2s}
.l9 a:hover .l9-tx{color:#000}
.l9 a.on .l9-tx{color:#000;font-weight:600}
.l9 a.on .l9-fx{background:rgba(43,43,45,.88)}
.l9 a.on .l9-ic{filter:brightness(0) invert(1)}
.l9 a.on .l9-tile{box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.4),inset -1px -1px 1px rgba(255,255,255,.18),0 8px 20px -8px rgba(0,0,0,.45)}
.l9 a:not(.on) .l9-fx,.l9 a:not(.on) .l9-ic,.l9 a:not(.on) .l9-tile{transition-delay:0s}
@media (prefers-reduced-motion: reduce){.l9-mark,.l9-br::after,.l9-fx,.l9-ic,.l9-tile{transition:none!important}}
'''
rep('\n/* V7: year ledger */', CSS + '\n/* V7: year ledger */')
rep("'D', 'E', 'F', 'G', 'H'])", "'D', 'E', 'F', 'G', 'H', 'I'])")
rep("D: 0, E: 0, F: 0, G: 0, H: 0 };", "D: 0, E: 0, F: 0, G: 0, H: 0, I: 0 };")
rep("    v.bY = (st.B * 52) + 'px';", "    v.bY = (st.B * 52) + 'px';\n    v.iY = (st.I * 52) + 'px';")
rep("v.fW = [101, 146, 208, 78, 135][st.F] + 'px';", "v.fW = [101, 146, 208, 78, 135, 203][st.F] + 'px';")
rep('glass with dark logos -->', 'glass with dark logos, spine in liquid glass -->')
open(p, 'w').write(s); print('ok')
