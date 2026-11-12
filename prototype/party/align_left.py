"""Logos and the waving drawing line up their left edge with the text column (with nudge + free mode tweaks)."""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:100], s.count(old)); s = s.replace(old, new)
rep("    // the trail's own pixels, oldest first, become the logo: each one flies from where it is\n",
"""    const AL = this.trLeft(home); // left-align the figure's ink with the text column
    if (AL != null && targets.length) {
      let mx = Infinity; for (const t of targets) if (t.tx < mx) mx = t.tx;
      if (anim) for (const pa of anim.paths) for (const t of pa) if (t.x < mx) mx = t.x;
      const dx = AL - (mx - tcell / 2);
      for (const t of targets) t.tx += dx;
      if (anim) { const seen = new Set(); for (const pa of anim.paths) for (const t of pa) if (!seen.has(t)) { seen.add(t); t.x += dx; } anim.grid.ox += dx; anim.rect.x += dx; }
    }
    // the trail's own pixels, oldest first, become the logo: each one flies from where it is
""")
rep("  trailWaveImg(ctx, set, i, R, a) {",
"""  trLeft(home) { // the text column's left edge in canvas px, or null when the figure is placed freely by waveX / logoX
    if ((home ? this.tp('waveAlign', 'Left with text') : this.tp('logoAlign', 'Left with text')) !== 'Left with text') return null;
    const cv = this.trCv, sec = cv && cv.closest('section'); if (!sec) return null;
    const vis = (e) => e.getClientRects().length > 0;
    const el = [...sec.querySelectorAll('.th-prose')].find(vis) || [...sec.querySelectorAll('p')].find(vis); if (!el) return null;
    const b = cv.getBoundingClientRect(), k = cv.clientWidth / (b.width || 1);
    return (el.getBoundingClientRect().left - b.left) * k + (home ? this.tp('waveNudgeX', 0) : this.tp('logoNudgeX', 0));
  }
  trailWaveImg(ctx, set, i, R, a) {""")
m = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(m.group(2)))
for k in ('logoAlign', 'logoNudgeX', 'waveAlign', 'waveNudgeX'): assert k not in P, k
new = {}
for k, v in P.items():
    new[k] = v
    if k == 'waveX':
        new['waveAlign'] = {"editor": "enum", "options": ["Left with text", "Free (use waveX)"], "default": "Left with text", "section": v.get('section', 'Waving me')}
        new['waveNudgeX'] = {"editor": "range", "default": 0, "min": -150, "max": 150, "step": 1, "unit": "px", "section": v.get('section', 'Waving me')}
    if k == 'logoX':
        new['logoAlign'] = {"editor": "enum", "options": ["Left with text", "Free (use logoX)"], "default": "Left with text", "section": v.get('section', 'Hover logos')}
        new['logoNudgeX'] = {"editor": "range", "default": 0, "min": -150, "max": 150, "step": 1, "unit": "px", "section": v.get('section', 'Hover logos')}
assert 'logoAlign' in new and 'waveAlign' in new
attr = json.dumps(new, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:m.start()] + "data-props='" + attr + "'>" + s[m.end():]
open(p, 'w').write(s); print('ok')
