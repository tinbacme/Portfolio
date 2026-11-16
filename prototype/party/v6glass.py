"""V6: the selected item sits in a sliding liquid-glass pill (tinted with that company's color) instead of the tick.
usage: v6glass.py <Piece-navvars.dc.html>"""
import sys
p = sys.argv[1]; s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:80], s.count(old)); s = s.replace(old, new)
rep('<nav class="t6" aria-label="Site, version 6"><span class="t6-tick" aria-hidden="true" style="transform: translateY({{fY}}); background-color: {{fColor}}"></span>',
    '<nav class="t6" aria-label="Site, version 6" style="--fc: {{fColor}}"><span class="t6-lens" aria-hidden="true" style="transform: translateY({{fY}}); width: {{fW}}"><span class="t6-lens-fx"></span><span class="t6-lens-shine"></span></span>')
CSS = '''
/* V6 selection as a liquid-glass lens */
.t6{padding-left:0}
.t6 a{position:relative;z-index:1;padding:0 14px;gap:10px}
.t6-lens{position:absolute;left:0;top:2px;height:36px;border-radius:999px;isolation:isolate;transition:transform .55s cubic-bezier(.34,1.45,.5,1),width .45s cubic-bezier(.3,1.3,.5,1);box-shadow:0 8px 22px -8px rgba(0,0,0,.28),0 1px 3px rgba(0,0,0,.08)}
.t6-lens-fx,.t6-lens-shine{position:absolute;inset:0;border-radius:inherit}
.t6-lens-fx{background:color-mix(in srgb,var(--fc,#141414) 9%,rgba(255,255,255,.55));-webkit-backdrop-filter:blur(6px) saturate(1.8);backdrop-filter:blur(6px) saturate(1.8);backdrop-filter:url(#nv-glass) blur(6px) saturate(1.8);transition:background-color .45s}
.t6-lens-shine{box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.95),inset -1px -1px 1px rgba(255,255,255,.7),inset 0 0 0 1px color-mix(in srgb,var(--fc,#141414) 14%,rgba(0,0,0,.05)),inset 0 -6px 12px -6px color-mix(in srgb,var(--fc,#141414) 18%,transparent)}
'''
rep('\n/* V7: year ledger */', CSS + '\n/* V7: year ledger */')
rep("    v.fY = (st.F * 44) + 'px';", "    v.fY = (st.F * 44) + 'px';\n    v.fW = [101, 146, 208, 78, 135][st.F] + 'px';")
rep("gray logos, and only the current one shows its name, in black, with a short tick in that company&#8217;s color.",
    "gray logos; the current one sits in a liquid-glass lens tinted with that company&#8217;s color and shows its name.")
open(p, 'w').write(s); print('ok')
