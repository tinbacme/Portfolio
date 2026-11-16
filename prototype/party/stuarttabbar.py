"""Stuart page, phones (<=760px): the role nav becomes a bottom tab bar - icons in a frosted liquid-glass pill, with a brighter
glass lens that slides to the current role (tap or scroll). usage: stuarttabbar.py <TinHome-Stuart.dc.html>"""
import sys
p=sys.argv[1]; s=open(p).read()
def rep(o,n):
    global s; assert s.count(o)==1,(o[:80],s.count(o)); s=s.replace(o,n)
rep('<span class="l9-mark" style="transform: translateY({{svY}})">', '<span class="l9-mark" style="transform: translateY({{svY}}); --k: {{svK}}">')
rep("      svY: ((this.state.nav ?? 0) * 52) + 'px',", "      svY: ((this.state.nav ?? 0) * 52) + 'px', svK: String(this.state.nav ?? 0),")
rep("  .sv-nav{display:none!important}\n", "")
rep("/* phones: one column, the role nav steps aside (the logo still takes you home) */", "/* phones: one column; the role nav becomes a bottom tab bar (below) */")
CSS = '''
/* phones: the role nav as a bottom tab bar - icons sit in a frosted liquid-glass pill; a brighter glass lens slides to the current one */
@media (max-width:760px){
  .st-root{padding-bottom:140px}
  .sv-nav.l9{position:fixed;left:50%;right:auto;top:auto;bottom:calc(16px + env(safe-area-inset-bottom,0px));margin:0;transform:translateX(-50%);z-index:30;
    flex-direction:row;align-items:center;gap:4px;padding:6px;border-radius:999px;isolation:isolate;
    background:linear-gradient(150deg,rgba(255,255,255,.72),rgba(255,255,255,.46) 50%,rgba(255,255,255,.62));
    -webkit-backdrop-filter:blur(14px) saturate(1.8);backdrop-filter:blur(14px) saturate(1.8);backdrop-filter:url(#nv-glass9) blur(14px) saturate(1.8);
    box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.95),inset -1px -1px 1px rgba(255,255,255,.6),inset 0 0 0 1px rgba(0,0,0,.06),0 12px 30px -10px rgba(0,0,0,.3),0 2px 6px -2px rgba(0,0,0,.12)}
  .sv-nav .l9-spine,.sv-nav .l9-elb,.sv-nav .l9-br,.sv-nav .l9-tx{display:none!important}
  .sv-nav.l9 a{width:44px;height:44px;justify-content:center;z-index:1}
  .sv-nav .l9-tile{width:44px;height:44px;border-radius:999px;box-shadow:none!important;background:none;transform:none!important}
  .sv-nav .l9-fx,.sv-nav .l9-shine,.sv-nav .l9-tile .gl-light{display:none}
  .sv-nav .l9-ic{filter:none!important;opacity:.55;transition:opacity .3s}
  .sv-nav a.on .l9-ic{opacity:1}
  /* the lens: the spine marker, turned into a glass bubble that slides sideways */
  .sv-nav .l9-track{left:6px;top:6px;bottom:auto;width:44px;height:44px;overflow:visible;border-radius:999px}
  .sv-nav .l9-track .l9-mark{left:0;top:0;width:44px;height:44px;border-radius:999px;transform:translateX(calc(var(--k,0) * 48px))!important;
    transition:transform .5s cubic-bezier(.34,1.3,.5,1);
    background:radial-gradient(120% 80% at 30% 0%,rgba(255,255,255,1) 0%,rgba(255,255,255,.75) 45%,rgba(255,255,255,.55) 100%);
    box-shadow:inset 1.5px 1.5px 1px #fff,inset -1px -1px 1px rgba(255,255,255,.7),inset 0 0 0 1px rgba(0,0,0,.07),0 6px 14px -6px rgba(0,0,0,.35),0 1px 2px rgba(0,0,0,.12)}
  @media (prefers-reduced-motion: reduce){.sv-nav .l9-track .l9-mark{transition:none}}
}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
open(p,'w').write(s); print('ok')
