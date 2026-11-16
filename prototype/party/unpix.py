"""Take the pixel/scatter photo hover back off the stuart.re-style page (it moves to the Photo dots lab first).
usage: unpix.py <TinHome-Stuart.dc.html>"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
a = s.index('  pxStart() {'); b = s.index('  rvStart() {'); s = s[:a] + s[b:]
s = s.replace("setTimeout(() => { this.rvStart(); this.pxStart(); }, 0)", "setTimeout(() => this.rvStart(), 0)")
s = s.replace(" cancelAnimationFrame(this.pxRaf); if (this.rootEl && this.pxMove) { this.rootEl.removeEventListener('pointermove', this.pxMove); this.rootEl.removeEventListener('pointerleave', this.pxOut); }", "")
a = s.index('/* photo hover: canvas tiles over the photo while hovered */'); b = s.index('/* scroll reveal:', a); s = s[:a] + s[b:]
mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S); P = json.loads(html.unescape(mm.group(2)))
for k in ['pixelHover', 'pixelTile', 'pixelRadius', 'pixelForce', 'pixelMs']: P.pop(k, None)
s = s[:mm.start()] + "data-props='" + json.dumps(P, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;') + "'>" + s[mm.end():]
assert 'pxStart' not in s and 'st-px' not in s and 'pixelTile' not in s
open(p, 'w').write(s); print('ok')
