"""Carousel cards take the Box (3) design: each role's front and back faces from Box (3) go into the flip cards on the string.
usage: box2carousel.py <Piece-46el.dc.html> <TinHome-Party-Desktop.dc.html>  (edits the party board in place)"""
import sys, re
box = open(sys.argv[1]).read(); p = sys.argv[2]; s = open(p).read()

def block(txt, start):  # balanced <div ...>...</div> starting at index `start`
    d = 0
    for m in re.finditer(r'<div\b|</div>', txt[start:]):
        d += 1 if m.group(0).startswith('<div') else -1
        if d == 0: return txt[start:start + m.end()]
    raise ValueError('unbalanced')
def inner(div):
    return div[div.index('>') + 1: div.rindex('</div>')]
def style(div):
    m = re.match(r'<div[^>]*\bstyle="([^"]*)"', div); return m.group(1) if m else ''

roles = []
for m in re.finditer(r'<p class="bv-label">([^<]*)</p>', box):
    nxt = box.find('<p class="bv-label">', m.end()); nxt = len(box) if nxt < 0 else nxt
    seg = box[m.end():nxt]
    f0 = seg.index('<div class="bd-face o-card"'); front = block(seg, f0)
    b0 = seg.index('<div class="bd-face o-card o-back"'); back = block(seg, b0)
    roles.append((m.group(1), front, back))
N = len(roles); assert N >= 3, N
TILT = [-4, 2.5, -2, 3, -3, 2, -2.5, 3.5, -1.5, 2.2]; DROP = [70, 150, 100, 60, 130, 90, 140, 80, 110, 70]; DL = [-0.6, -2.1, -3.4, -1.2, -2.7, -4.0, -1.8, -3.1, -0.9, -2.4]
def card(i, label, front, back, copy):
    k = i + 1; hid = ' aria-hidden="true"' if copy else ''; tab = '-1' if copy else '0'
    fs = style(front).replace('position: relative; ', ''); bs = style(back)
    name = label.split('·', 1)[-1].strip().replace('"', '')
    return (f'\n      <div class="bd-hang"{hid} style="--t: {TILT[i % 10]}deg; --drop: {DROP[i % 10]}px; --dl: {DL[i % 10]}s; --pin: 12px">'
            f'<span class="bd-pin" aria-hidden="true"></span><span class="bd-thread" aria-hidden="true"></span>'
            f'<div class="bd-swing"><span class="bd-clip" aria-hidden="true"></span>'
            f'<div class="bd-card {{{{bdFlip{k}Class}}}}" role="button" tabindex="{tab}" aria-pressed="{{{{bdFlip{k}On}}}}" aria-label="{name} badge, flip for details" onClick="{{{{bdFlip{k}}}}}" onKeyDown="{{{{bdKey{k}}}}}">'
            f'<div class="bd-face bd-front bx-face" style="{fs}">{inner(front)}</div>'
            f'<div class="bd-face bd-back bx-face" style="{bs}">{inner(back)}</div>'
            f'</div></div></div>')
track = ''.join(card(i, *r, True) for i, r in enumerate(roles)) + ''.join(card(i, *r, False) for i, r in enumerate(roles)) + ''.join(card(i, *r, True) for i, r in enumerate(roles))
a = s.index('<div class="bd-track"'); a = s.index('>', a) + 1
b = s.index('\n    </div></div>\n    <div class="bd-edge', a)
s = s[:a] + track + s[b:]
old = int(re.search(r"const n = (\d+), ease", s).group(1))
s = s.replace(f"const n = {old}, ease", f"const n = {N}, ease")
s = s.replace(f"- ({old} + i) *", f"- ({N} + i) *").replace(f"- ({old} + (this.state.bdI || 0))", f"- ({N} + (this.state.bdI || 0))")
assert f"const n = {N}, ease" in s and f"- ({N} + i) *" in s
key = lambda k: f"(e) => {{ if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); this.bdToggle({k}); }} }}"
have = set(int(x) for x in re.findall(r"bdFlip(\d+): \(\) => this\.bdToggle", s))
last = max(have)
for k in range(1, N + 1):
    if k in have: continue
    anchor = f"      bdFlip{last}: () => this.bdToggle({last}),"
    ls = s.index(anchor); le = s.index('\n', ls) + 1
    s = s[:le] + f"      bdFlip{k}: () => this.bdToggle({k}), bdKey{k}: {key(k)}, bdFlip{k}Class: this.state.bdFlip && this.state.bdFlip[{k}] ? 'is-flipped' : '', bdFlip{k}On: this.state.bdFlip && this.state.bdFlip[{k}] ? 'true' : 'false',\n" + s[le:]
    last = k
CSS = '''
/* carousel cards in the Box (3) design */
.bx-face.bd-back{display:flex;flex-direction:column}
.bx-face.bd-back .bd-foot{margin-top:auto}
.bx-face .bd-photo{flex:none}
.bx-face .bd-name{margin:14px 4px 0}
.bx-face .bd-foot > span:first-child{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0;margin-right:12px}
.party .bx-face [style*="color: #6e6e6e"]{color:#6e6e6e !important}
'''
s = s.replace('</style>\n</helmet>', CSS + '</style>\n</helmet>', 1)
open(p, 'w').write(s)
m = re.search(r"data-props=(['\"])(.*?)\1>\n(.*?)</script>", s, re.S)
open('/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/b2c_logic.js', 'w').write('class DCLogic{}\n' + m.group(3))
print('ok', N, 'roles:', [r[0] for r in roles])
