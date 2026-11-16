"""Stuart page: replace the dark glass dock with the V6 nav (gray logos that light up in color on hover; the current one sits in a
sliding dark liquid-glass pill with a white logo and name). Current item follows scrolling (scroll-spy) and clicks.
usage: stuartv6.py <TinHome-Stuart.dc.html>"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:90], s.count(old)); s = s.replace(old, new)
a = s.index('<div class="st-rail"'); b = s.index('</nav></div>', a) + len('</nav></div>')
old = s[a:b]
rail_open = old[:old.index('>') + 1]
defs = re.search(r'<svg class="st-defs".*?</svg>', old, re.S).group(0)
cap = re.search(r'<svg class="st-cap".*?</svg>', old, re.S).group(0)  # keep the owner's cap size and placement
order = re.findall(r'<a class="st-dk" href="(#[^"]+)"', old)
MS = ('<svg viewBox="0 0 20 20" width="20" height="20" aria-hidden="true"><rect x="0" y="0" width="9" height="9" fill="#f25022"></rect><rect x="11" y="0" width="9" height="9" fill="#7fba00"></rect>'
      '<rect x="0" y="11" width="9" height="9" fill="#00a4ef"></rect><rect x="11" y="11" width="9" height="9" fill="#ffb900"></rect></svg>')
UO = '<img src="/_blob/00e0e1ec841a28c4e0055e4a6738e6b1" alt="" width="20" height="20">'
ITEM = {
    '#microsoft': ('Microsoft AI', MS),
    '#salesforce': ('Salesforce', '<img src="/_blob/ac43d25c19be4e522f4bd492e1c090ab" alt="" width="24" height="18">'),
    '#uo-teach': ('University of Oregon', UO),
    '#2u': ('2U', '<span style="font: 700 14px/1 Inter, system-ui, sans-serif; color: #000; letter-spacing: -0.02em">2U</span>'),
    '#uo-bs': ('BS Industrial Design', UO + cap),
    '#top': ('Home', '<span style="font: 400 22px/1 Caveat, cursive; color: #000">tin</span>'),
}
links = ''.join(f'<a class="{{{{sv{i}}}}}" href="{h}" aria-current="{{{{svC{i}}}}}" onClick="{{{{svGo{i}}}}}"><span class="sv-ic">{ITEM[h][1]}</span><span class="sv-tx">{ITEM[h][0]}</span></a>'
                for i, h in enumerate(order))
new = (rail_open + '<nav class="sv-nav" aria-label="Jump to a role" ref="{{navRef}}">' + defs +
       '<span class="sv-lens" aria-hidden="true"><span class="sv-lens-fx"></span><span class="sv-lens-shine"></span></span>' + links + '</nav></div>')
s = s[:a] + new + s[b:]
CSS = r'''
/* nav: gray logos that light up on hover; the current one sits in a sliding dark liquid-glass pill with a white logo and name */
.sv-nav{position:sticky;top:222px;display:flex;flex-direction:column;align-items:flex-start;gap:4px}
.sv-nav a{position:relative;z-index:1;display:flex;align-items:center;gap:10px;height:40px;padding:0 14px;border-radius:999px;text-decoration:none;white-space:nowrap;-webkit-tap-highlight-color:transparent}
.sv-nav a:focus-visible{outline:2px solid #0099ff;outline-offset:2px}
.sv-ic{position:relative;flex:none;display:grid;place-items:center;width:24px;height:24px;filter:grayscale(1);opacity:.4;transition:filter .3s,opacity .3s}
.sv-nav a:hover .sv-ic{filter:none;opacity:1}
.sv-tx{font:600 15px/1 Inter,sans-serif;color:#fff;opacity:0;transform:translateX(-6px);pointer-events:none;transition:opacity .3s,transform .35s cubic-bezier(.2,.7,.2,1)}
.sv-nav a.on .sv-tx{opacity:1;transform:none}
.sv-nav a.on .sv-ic,.sv-nav a.on:hover .sv-ic{filter:brightness(0) invert(1);opacity:1}
.sv-lens{position:absolute;left:0;top:0;width:52px;height:40px;border-radius:999px;isolation:isolate;pointer-events:none;transition:transform .55s cubic-bezier(.34,1.45,.5,1),width .45s cubic-bezier(.3,1.3,.5,1);box-shadow:0 8px 22px -8px rgba(0,0,0,.35),0 1px 3px rgba(0,0,0,.1)}
.sv-lens-fx,.sv-lens-shine{position:absolute;inset:0;border-radius:inherit}
.sv-lens-fx{background:rgba(43,43,45,var(--lensTint,.92));-webkit-backdrop-filter:blur(6px) saturate(1.8);backdrop-filter:blur(6px) saturate(1.8);backdrop-filter:url(#st-glass) blur(6px) saturate(1.8)}
.sv-lens-shine{box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.45),inset -1px -1px 1px rgba(255,255,255,.2),inset 0 0 14px rgba(255,255,255,.08)}
.sv-ic .st-cap{color:#2b2b2d;filter:none}
@media (prefers-reduced-motion: reduce){.sv-lens,.sv-tx,.sv-ic{transition:none}}
'''
anchor = '.st-defs{position:absolute;width:0;height:0;overflow:hidden}'
rep(anchor, anchor + CSS)
N = len(order); top_i = order.index('#top') if '#top' in order else 0
JS = """  svPlace() { // slide the glass pill to the current item and size it to fit its name
    const nav = this.navEl; if (!nav) return;
    const a = nav.querySelector('a.on'), lens = nav.querySelector('.sv-lens'); if (!a || !lens) return;
    lens.style.transform = 'translateY(' + a.offsetTop + 'px)'; lens.style.width = a.offsetWidth + 'px';
  }
  svSpy() { // the nav follows the page: whichever role is in the middle of the screen is current
    if (this.svIO || typeof IntersectionObserver !== 'function' || !this.rootEl) return;
    const ids = %s;
    this.svIO = new IntersectionObserver((es) => es.forEach((e) => { if (!e.isIntersecting) return; const k = ids.indexOf(e.target.id); if (k >= 0 && this.state.nav !== k) this.setState({ nav: k }); }), { rootMargin: '-45%% 0px -50%% 0px' });
    ids.forEach((id) => { const el = this.rootEl.querySelector('#' + CSS.escape(id)); if (el) this.svIO.observe(el); });
  }
""" % json.dumps([h[1:] for h in order])
rep("  rvStart() {", JS + "  rvStart() {")
rep("clearInterval(this.lgT); if (this.rvIO)", "clearInterval(this.lgT); if (this.svIO) this.svIO.disconnect(); if (this.rvIO)")
rep("if (el) setTimeout(() => this.rvStart(), 0); }", "if (el) setTimeout(() => { this.rvStart(); this.svSpy(); }, 0); }")
VALS = ("      navRef: (el) => { this.navEl = el; },\n"
        f"      ...Object.fromEntries(Array.from({{ length: {N} }}, (_, k) => {{ const on = (this.state.nav ?? {top_i}) === k; return [['sv' + k, on ? 'on' : ''], ['svC' + k, on ? 'true' : 'false'], ['svGo' + k, () => this.setState({{ nav: k }})]]; }}).flat()),\n")
rep("    setTimeout(() => this.lgStart(), 0);\n    return {\n", "    setTimeout(() => { this.lgStart(); this.svPlace(); }, 0);\n    return {\n" + VALS)
# the old dock tint tweak no longer applies
mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S); P = json.loads(html.unescape(mm.group(2))); P.pop('dockTint', None)
s = s[:mm.start()] + "data-props='" + json.dumps(P, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;') + "'>" + s[mm.end():]
s = s.replace("      dockTint: String(this.props.dockTint ?? 0.9),\n", "")
open(p, 'w').write(s); print('ok', order)
