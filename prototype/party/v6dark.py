"""V6: hover shows the logo in its own colors; selected = darker glass lens with white logo and white text. usage: v6dark.py <Piece-navvars.dc.html>"""
import sys
p = sys.argv[1]; s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:80], s.count(old)); s = s.replace(old, new)
rep('.t6 a:hover .t6-ic{opacity:.75}', '.t6 a:hover .t6-ic{filter:none;opacity:1}')
rep('.t6 a.on .t6-tx{color:#000;font-weight:600;opacity:1;transform:none}', '.t6 a.on .t6-tx{color:#fff;font-weight:600;opacity:1;transform:none}')
rep('.t6 a.on .t6-ic{filter:none;opacity:1}', '.t6 a.on .t6-ic,.t6 a.on:hover .t6-ic{filter:brightness(0) invert(1);opacity:1}')
rep('.t6-lens-fx{background:color-mix(in srgb,var(--fc,#141414) 9%,rgba(255,255,255,.55));',
    '.t6-lens-fx{background:rgba(43,43,45,var(--lensTint,.92));')
rep('.t6-lens-shine{box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.95),inset -1px -1px 1px rgba(255,255,255,.7),inset 0 0 0 1px color-mix(in srgb,var(--fc,#141414) 14%,rgba(0,0,0,.05)),inset 0 -6px 12px -6px color-mix(in srgb,var(--fc,#141414) 18%,transparent)}',
    '.t6-lens-shine{box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.45),inset -1px -1px 1px rgba(255,255,255,.2),inset 0 0 14px rgba(255,255,255,.08)}')
rep("gray logos; the current one sits in a gray liquid-glass lens and shows its name.",
    "gray logos that light up in their own colors on hover; the current one sits in a dark liquid-glass lens with a white logo and name.")
open(p, 'w').write(s); print('ok')
