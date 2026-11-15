"""(1) nav variations: add V8 liquid glass with dark logos on light glass. (2) stuart page: dock becomes the V4 dark liquid glass.
usage: glass2.py <Piece-navvars.dc.html> <TinHome-Stuart.dc.html>"""
import sys, re, json, html
nv, st = sys.argv[1], sys.argv[2]

# ---- (1) V8 ----
s = open(nv).read()
def rep(old, new, src=None):
    global s
    assert s.count(old) == 1, (old[:80], s.count(old)); s = s.replace(old, new)
UO, SF = '/_blob/00e0e1ec841a28c4e0055e4a6738e6b1', '/_blob/ac43d25c19be4e522f4bd492e1c090ab'
G = '#2b2b2d'
MS = ''.join(f'<rect x="{x}" y="{y}" width="9" height="9" fill="{G}"></rect>' for x, y in [(0, 0), (11, 0), (0, 11), (11, 11)])
LOGO = ['<span class="nv-tin">tin</span>', f'<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true">{MS}</svg>',
        f'<img src="{UO}" alt="" width="20" height="17" class="nv-ink">', '<span class="nv-2u">2U</span>',
        f'<img src="{SF}" alt="" width="24" height="17" class="nv-ink">']
ITEMS = [('Home', '#top'), ('Microsoft AI', '#microsoft'), ('University of Oregon', '#uo-teach'), ('2U', '#2u'), ('Salesforce', '#salesforce')]
items = ''.join(f'<a class="{{{{H{i}}}}}" href="{h}" aria-label="{l}" onClick="{{{{pickH{i}}}}}"><span class="l4-ic">{LOGO[i]}</span><span class="l4-tip">{l}</span></a>' for i, (l, h) in enumerate(ITEMS))
bg = ''.join(f'<img src="/_blob/{b}" alt="">' for b in ['155942c7f1c522f9aec7d43d1c1d0d0d', '8bd998ead1110dbdb0a707cdb0cb6c60', 'effff208332abe411e27c82aaa87e30d', '155942c7f1c522f9aec7d43d1c1d0d0d'])
V8 = ('\n  <section class="nv-col nv-row2"><p class="nv-k">V8</p><h2 class="nv-t">Liquid glass, dark logos</h2>'
      '<p class="nv-s">The same glass, but clear and bright, with the logos in the original dock&#8217;s dark gray.</p>'
      f'<div class="nv-stage st-photo"><div class="l4-bg" aria-hidden="true"><div class="l4-track">{bg}</div></div>'
      '<nav class="l4 l8" aria-label="Site, version 8" style="left: 237px; top: 80px"><span class="l4-fx" aria-hidden="true"></span><span class="l4-tint" aria-hidden="true"></span><span class="l4-shine" aria-hidden="true"></span>'
      f'{items}</nav></div></section>')
rep('</section>\n</div>\n</x-dc>', '</section>' + V8 + '\n</div>\n</x-dc>')
CSS = '''
/* V8: clear glass, dark logos */
.l8 .l4-tint{background:rgba(255,255,255,var(--glassTint8,.45))}
.l8 .l4-shine{box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.85),inset -1px -1px 1px rgba(255,255,255,.5),inset 0 0 18px rgba(255,255,255,.3)}
.l8 .l4-ic{color:#2b2b2d;filter:none}
.nv-ink{filter:brightness(0);opacity:.83}
.l8 a:hover{background:rgba(43,43,45,.08)}
.l8 a.on{background:rgba(43,43,45,.12);box-shadow:inset 0 0 0 1px rgba(43,43,45,.12)}
.l8 .l4-tip{color:#2b2b2d;background:rgba(255,255,255,.55);box-shadow:inset 1px 1px 0 rgba(255,255,255,.9),0 4px 14px -6px rgba(0,0,0,.3)}
'''
rep('\n@media (prefers-reduced-motion: reduce){.l4-track{animation:none}', CSS + '@media (prefers-reduced-motion: reduce){.l4-track{animation:none}')
rep("'D', 'E', 'F', 'G'])", "'D', 'E', 'F', 'G', 'H'])")
rep("D: 0, E: 0, F: 0, G: 0 };", "D: 0, E: 0, F: 0, G: 0, H: 0 };")
rep("--glassTint: {{glassTint}}\"", "--glassTint: {{glassTint}}; --glassTint8: {{glassTint8}}\"")
rep("    v.glassBend = String(p.glassBend ?? 60);", "    v.glassBend = String(p.glassBend ?? 60);\n    v.glassTint8 = String(p.glassTint8 ?? 0.45);")
mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S); P = json.loads(html.unescape(mm.group(2)))
P['glassTint8'] = {"editor": "range", "default": 0.45, "min": 0, "max": 1, "step": 0.01, "section": "V8 glass, dark logos"}
s = s[:mm.start()] + "data-props='" + json.dumps(P).replace('&', '&amp;').replace("'", '&#39;') + "'>" + s[mm.end():]
rep('liquid glass, numbered index, accent tick, year ledger -->', 'liquid glass, numbered index, accent tick, year ledger, glass with dark logos -->')
open(nv, 'w').write(s)

# ---- (2) stuart page dock -> dark liquid glass ----
s = open(st).read()
rep('.st-dock{position:sticky;top:222px;display:flex;flex-direction:column;gap:8px;padding:8px;border-radius:20px;background:rgba(0,0,0,.8);box-shadow:inset 0 0 0 1px rgba(255,255,255,.15),0 .8px .6px -1px rgba(0,0,0,.2),0 2.4px 2px -2px rgba(0,0,0,.2),0 10px 24px -6px rgba(0,0,0,.28);-webkit-backdrop-filter:blur(12px);backdrop-filter:blur(12px)}',
    '.st-dock{position:sticky;top:222px;display:flex;flex-direction:column;gap:8px;padding:8px;border-radius:20px;isolation:isolate;box-shadow:0 .8px .6px -1px rgba(0,0,0,.2),0 2.4px 2px -2px rgba(0,0,0,.2),0 10px 24px -6px rgba(0,0,0,.28)}\n'
    '/* liquid glass: refraction + blur, dark gray tint, bright rim */\n'
    '.st-g-fx,.st-g-tint,.st-g-shine{position:absolute;inset:0;border-radius:inherit;pointer-events:none}\n'
    '.st-g-fx{z-index:0;-webkit-backdrop-filter:blur(3px) saturate(1.7);backdrop-filter:blur(3px) saturate(1.7);backdrop-filter:url(#st-glass) blur(3px) saturate(1.7)}\n'
    '.st-g-tint{z-index:1;background:rgba(43,43,45,var(--dockTint,.75))}\n'
    '.st-g-shine{z-index:2;box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.45),inset -1px -1px 1px rgba(255,255,255,.2),inset 0 0 18px rgba(255,255,255,.08)}\n'
    '.st-dock .st-dk{position:relative;z-index:3}\n'
    '.st-defs{position:absolute;width:0;height:0;overflow:hidden}')
rep('.st-dk:hover,.st-dk:focus-visible{background:rgba(255,255,255,.1);outline:none}', '.st-dk:hover,.st-dk:focus-visible{background:rgba(255,255,255,.14);outline:none}')
FILTER = ('<svg class="st-defs" width="0" height="0" aria-hidden="true" focusable="false"><filter id="st-glass" x="0%" y="0%" width="100%" height="100%" filterUnits="objectBoundingBox">'
          '<feTurbulence type="fractalNoise" baseFrequency="0.012 0.012" numOctaves="2" seed="92" result="noise"></feTurbulence>'
          '<feGaussianBlur in="noise" stdDeviation="2" result="soft"></feGaussianBlur>'
          '<feDisplacementMap in="SourceGraphic" in2="soft" scale="60" xChannelSelector="R" yChannelSelector="G"></feDisplacementMap></filter></svg>')
rep('<nav class="st-dock" aria-label="Jump to a role">',
    '<nav class="st-dock" aria-label="Jump to a role" style="--dockTint: {{dockTint}}">' + FILTER +
    '<span class="st-g-fx" aria-hidden="true"></span><span class="st-g-tint" aria-hidden="true"></span><span class="st-g-shine" aria-hidden="true"></span>')
mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S); P = json.loads(html.unescape(mm.group(2)))
P['dockTint'] = {"editor": "range", "default": 0.75, "min": 0, "max": 1, "step": 0.01, "section": "Dock"}
s = s[:mm.start()] + "data-props='" + json.dumps(P, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;') + "'>" + s[mm.end():]
m = re.search(r"\n    return \{\n", s); assert m, 'return'
s = s[:m.end()] + "      dockTint: String(this.props.dockTint ?? 0.75),\n" + s[m.end():]
open(st, 'w').write(s); print('ok')
