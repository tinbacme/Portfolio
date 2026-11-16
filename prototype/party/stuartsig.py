"""Put signature S1 (Fine pen) on the stuart.re-style page in place of the Caveat 'Tin', signing itself (one line, then the T bar).
usage: stuartsig.py <TinHome-Stuart.dc.html>"""
import sys, re, importlib.util
spec = importlib.util.spec_from_file_location('sb', '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/sigboard.py')
src = open(spec.origin).read(); src = src[:src.index('cards = ')]  # load only the helpers, not the board writer
ns = {}; exec(compile(src.replace('out = sys.argv[1]', 'out = None'), 'sb', 'exec'), ns)
svg = ns['signing_svg'](0, '/_blob/b50ab447ec0cca3f6303a8901bde60d6', 'Tin Le signature')
svg = svg.replace('id="sgm0"', 'id="stsig"').replace('url(#sgm0)', 'url(#stsig)').replace('class="sg-sign"', 'class="sg-sign st-sig-svg"')
svg = re.sub(r' width="\d+" height="\d+" role="img"', ' role="img"', svg)
p = sys.argv[1]; s = open(p).read()
old = '<p class="st-sign" aria-hidden="true">Tin</p>'
assert s.count(old) == 1
s = s.replace(old, '<div class="st-sign st-sign-svg" aria-hidden="true">' + svg.replace('role="img" aria-label="Tin Le signature"', 'aria-hidden="true"') + '</div>')
CSS = ('\n/* signature: signs itself on load (one stroke, then the T bar); hover to sign again */\n'
       '.st-sign-svg{top:178px;right:-8px;width:190px;font:inherit;transform:rotate(-6deg);opacity:.55}\n'
       '.st-sign-svg svg{display:block;width:100%;height:auto;overflow:visible}\n'
       '.st-sign-svg path{stroke-dasharray:1 1;stroke-dashoffset:0;animation-name:sgDraw;animation-timing-function:cubic-bezier(.4,.1,.5,1);animation-fill-mode:both}\n'
       '@keyframes sgDraw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}@keyframes sgDraw2{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}\n'
       '.st-sign-svg{--cd:.6s}.st-sign-svg:hover{--cd:0s}.st-sign-svg:hover path{animation-name:sgDraw2}\n'
       '@media (prefers-reduced-motion: reduce){.st-sign-svg path{animation:none}}\n')
a = '.st-defs{position:absolute;width:0;height:0;overflow:hidden}'
assert s.count(a) == 1; s = s.replace(a, a + CSS)
open(p, 'w').write(s); print('ok', len(svg))
