"""Drive Tin's 8-frame logo loop from component state (same as the homepage header) instead of a CSS animation,
so a frame always shows even where CSS animations are paused. usage: logojs.py nav <NavHeaderVariations> | stuart <TinHome-Stuart>"""
import sys, re
mode, p = sys.argv[1], sys.argv[2]; s = open(p).read()
IDS = ['8fbd77508883c78b84540da031e5f678', 'e09f528d7a65e7ee280d22130c36c17d', 'ca23789dd45bf344382c52b8987884a8', '720e3e91bd1b388459c182e4c63e3469',
       'a25aa6071a426de3b10058361008b0e1', '2ed749d513062c2fc935541bb195ad95', 'eb61a3bdf25e26fc602c11f962cebff2', '971b6a3ff00fa61ea013489a3df324e6']
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:80], s.count(old)); s = s.replace(old, new)
TIMER = """  lgStart() { // Tin's logo: step through the 8 marks like the homepage header
    if (this.lgT) return;
    const reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce) { this.setState({ lg: 7 }); return; }
    this.lgT = setInterval(() => this.setState((st) => ({ lg: ((st.lg || 0) + 1) % 8 })), 700);
  }
"""
VALS = "      ...Object.fromEntries(Array.from({ length: 8 }, (_, k) => ['lg' + k, (this.state.lg || 0) === k ? '1' : '0'])),\n"
if mode == 'nav':
    for k, i in enumerate(IDS):
        rep(f'<img src="/_blob/{i}" alt="">', f'<img src="/_blob/{i}" alt="" style="opacity: {{{{lg{k}}}}}">', 5)
    rep('.lg img{position:absolute;inset:0;width:100%;height:100%;opacity:0;animation:hvLoop 5.6s steps(1,end) infinite}', '.lg img{position:absolute;inset:0;width:100%;height:100%;transition:opacity .12s}')
    s = re.sub(r"\.lg img:nth-child\(1\)\{animation-delay:-5\.6s\}.*?\n.*?\n@keyframes hvLoop\{[^\n]*\}\n", '', s, flags=re.S)
    rep('  .lg img{animation:none;opacity:0}.lg img:nth-child(8){opacity:1}\n', '')
    rep("  componentWillUnmount() { clearTimeout(this.t); }", "  componentDidMount() { this.lgStart(); }\n  componentWillUnmount() { clearTimeout(this.t); clearInterval(this.lgT); }\n" + TIMER.rstrip('\n'))
    rep("    v.t4 = st.p4 === 'a' ? '92px' : '0px';", "    for (let k = 0; k < 8; k++) v['lg' + k] = (st.lg || 0) === k ? '1' : '0';\n    setTimeout(() => this.lgStart(), 0);\n    v.t4 = st.p4 === 'a' ? '92px' : '0px';")
    assert 'animation:hvLoop' not in s and 'hvLoop' not in s
else:
    for k, i in enumerate(IDS):
        s, n = re.subn(r'<img src="/_blob/%s" alt="" style="animation-delay: [^"]*">' % i, f'<img src="/_blob/{i}" alt="" style="opacity: {{{{lg{k}}}}}">', s); assert n == 1, (i, n)
    rep('.st-toplogo img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;opacity:0;animation:stLogo 5.6s steps(1,end) infinite}', '.st-toplogo img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;transition:opacity .12s}')
    rep('@keyframes stLogo{0%{opacity:1}12.5%{opacity:0}100%{opacity:0}}\n', '')
    rep('@media (prefers-reduced-motion: reduce){.st-toplogo img{animation:none}.st-toplogo img:last-child{opacity:1}}\n', '')
    rep("  rvStart() {", TIMER + "  rvStart() {")
    rep("clearTimeout(this.t); if (this.rvIO)", "clearTimeout(this.t); clearInterval(this.lgT); if (this.rvIO)")
    rep("    return {\n      rootRef:", "    setTimeout(() => this.lgStart(), 0);\n    return {\n" + VALS + "      rootRef:")
open(p, 'w').write(s); print('ok', mode)
