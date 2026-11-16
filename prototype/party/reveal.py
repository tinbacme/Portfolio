"""Scroll reveal on the stuart.re-style page: things blur, fade and rise in as they enter the screen.
usage: reveal.py <TinHome-Stuart.dc.html>"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:80], s.count(old)); s = s.replace(old, new)
rep('<div class="st-root" style="', '<div class="st-root" ref="{{rootRef}}" style="')
rep("  componentWillUnmount() { clearTimeout(this.t); }",
"""  componentWillUnmount() { clearTimeout(this.t); if (this.rvIO) this.rvIO.disconnect(); }
  rvStart() { // blur + fade + rise each block as it scrolls into view; rows stagger year, media, then info
    const root = this.rootEl; if (!root || this.rvIO) return;
    const reduce = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduce || this.props.reveal === false || typeof IntersectionObserver !== 'function') return;
    const groups = [];
    const intro = root.querySelector('.st-intro'); if (intro) groups.push([...intro.children]);
    root.querySelectorAll('.st-row').forEach((row) => groups.push([row.querySelector('.st-year'), ...row.querySelectorAll('.st-media'), row.querySelector('.st-info > div')].filter(Boolean)));
    const contact = root.querySelector('.st-contact'); if (contact) groups.push([...contact.children]);
    const step = this.props.revealStagger ?? 90;
    groups.forEach((g) => g.forEach((el, k) => { el.classList.add('st-rv'); el.style.transitionDelay = (k * step) + 'ms'; }));
    this.rvIO = new IntersectionObserver((entries) => entries.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('is-in'); this.rvIO.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });
    groups.flat().forEach((el) => this.rvIO.observe(el));
  }""")
rep("    return {\n      dockTint:", "    return {\n      rootRef: (el) => { this.rootEl = el; if (el) setTimeout(() => this.rvStart(), 0); },\n      dockTint:")
CSS = ('\n/* scroll reveal: start blurred, faded and a little low; settle in as it enters the screen */\n'
       '.st-rv{opacity:0;filter:blur(var(--rvBlur,14px));transform:translateY(28px);transition:opacity .8s ease,filter .9s ease,transform 1s cubic-bezier(.2,.7,.2,1)}\n'
       '.st-rv.is-in{opacity:1;filter:blur(0);transform:none}\n')
a = '.st-defs{position:absolute;width:0;height:0;overflow:hidden}'
rep(a, a + CSS)
mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S); P = json.loads(html.unescape(mm.group(2)))
P['reveal'] = {"editor": "boolean", "default": True, "section": "Motion"}
P['revealStagger'] = {"editor": "range", "default": 90, "min": 0, "max": 300, "step": 10, "unit": "ms", "section": "Motion"}
s = s[:mm.start()] + "data-props='" + json.dumps(P, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;') + "'>" + s[mm.end():]
open(p, 'w').write(s); print('ok')
