"""Logos line up by their optical edge (first column holding a real share of the shape), not the single outermost dot."""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
old = "      const dx = AL - (mx - tcell / 2);\n"
assert s.count(old) == 1
s = s.replace(old, """      let edge = mx - tcell / 2;
      if (!home) { // optical edge: skip thin outlying bumps (a cloud's lobe) so the body of the logo meets the text edge
        const cols = new Map(); for (const t of targets) { const c = Math.round((t.tx - mx) / tcell); cols.set(c, (cols.get(c) || 0) + 1); }
        let top = 0; cols.forEach((v) => { if (v > top) top = v; }); const thr = top * this.tp('logoOptical', 0.4);
        for (const c of [...cols.keys()].sort((a, b) => a - b)) if (cols.get(c) >= thr) { edge = mx + c * tcell - tcell / 2; break; }
      }
      const dx = AL - edge;
""")
m = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(m.group(2)))
assert 'logoOptical' not in P
new = {}
for k, v in P.items():
    new[k] = v
    if k == 'logoNudgeX':
        new['logoOptical'] = {"editor": "range", "default": 0.4, "min": 0, "max": 1, "step": 0.05, "section": v.get('section', 'Hover logos')}
assert 'logoOptical' in new
attr = json.dumps(new, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:m.start()] + "data-props='" + attr + "'>" + s[m.end():]
open(p, 'w').write(s); print('ok')
