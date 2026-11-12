"""Tablet C: 'Intro text' tweaks for the prose paragraph (line spacing, text size, pill spacing, width)."""
import sys, re, json, html
p = sys.argv[1]
s = open(p).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:100], s.count(old)); s = s.replace(old, new)

rep('<div class="th-prose" style="grid-column: 1 / -1; max-width: 700px; font-size: 24px; line-height: 1.8;',
    '<div class="th-prose" style="grid-column: 1 / -1; max-width: {{proseWidth}}; font-size: {{proseSize}}; line-height: {{proseLine}}; --pill-x: {{pillSpace}}; --pill-y: {{pillLift}};')
rep('.th-prose{line-height:2.2 !important}\n', '')
rep('gap:9px;margin:0 2px !important;vertical-align:-8px;', 'gap:9px;')
rep('.th-prose .th-co{margin:0 5px;vertical-align:-6px}', '.th-prose .th-co{margin:0 var(--pill-x,5px);vertical-align:var(--pill-y,-6px)}')
rep("      trWidth: (this.props.trailWidth ?? 55) + '%',",
    "      trWidth: (this.props.trailWidth ?? 55) + '%',\n"
    "      proseLine: String(this.tp('lineSpacing', 2.2)), proseSize: this.tp('textSize', 24) + 'px', proseWidth: this.tp('paragraphWidth', 700) + 'px',\n"
    "      pillSpace: this.tp('pillSpace', 5) + 'px', pillLift: -this.tp('pillDrop', 6) + 'px',")

m = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(m.group(2)))
new = {}
add = {
 'lineSpacing': {"editor": "range", "default": 2.2, "min": 1.3, "max": 3.2, "step": 0.05, "unit": "×", "section": "Intro text"},
 'textSize': {"editor": "range", "default": 24, "min": 16, "max": 40, "step": 1, "unit": "px", "section": "Intro text"},
 'paragraphWidth': {"editor": "range", "default": 700, "min": 420, "max": 760, "step": 10, "unit": "px", "section": "Intro text"},
 'pillSpace': {"editor": "range", "default": 5, "min": 0, "max": 20, "step": 1, "unit": "px", "section": "Intro text"},
 'pillDrop': {"editor": "range", "default": 6, "min": 0, "max": 14, "step": 1, "unit": "px", "section": "Intro text"},
}
for k in add: assert k not in P, k
for k, v in P.items():
    if k == 'introLoader': new.update(add)
    new[k] = v
attr = json.dumps(new, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:m.start()] + "data-props='" + attr + "'>" + s[m.end():]
open(p, 'w').write(s)
print('ok')
