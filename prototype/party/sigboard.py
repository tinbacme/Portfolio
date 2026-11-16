"""Signature options board: 10 'Tin Le' signatures made with gpt-image-2.5-flare, on white and on dark, with a size preview."""
import sys, json, math
SIGDIR = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/sig/'
def signing_svg(i, blob, alt, total=2.6, lift=0.12):
    """The original ink, revealed through a mask whose strokes follow the traced pen path in order."""
    t = json.load(open(SIGDIR + 'tr%02d.json' % (i + 1)))
    W, H, sw = t['w'], t['h'], t['sw']
    lens = [sum(math.dist(a, b) for a, b in zip(st, st[1:])) for st in t['strokes']]
    L = sum(lens) or 1; avail = max(0.6, total - lift * (len(lens) - 1))
    paths, at = [], 0.0
    for st, ln in zip(t['strokes'], lens):
        dur = max(0.05, avail * ln / L)
        d = 'M' + ' L'.join(f'{x:g} {y:g}' for x, y in st)
        paths.append(f'<path d="{d}" pathLength="1" style="animation-duration: {dur:.3f}s; animation-delay: calc(var(--cd, 0s) + {at:.3f}s)"></path>')
        at += dur + lift
    sc = min(440 / W, 170 / H)
    return (f'<svg class="sg-sign" viewBox="0 0 {W} {H}" width="{W * sc:.0f}" height="{H * sc:.0f}" role="img" aria-label="{alt}">'
            f'<defs><mask id="sgm{i}" maskUnits="userSpaceOnUse" x="0" y="0" width="{W}" height="{H}"><g fill="none" stroke="#fff" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{"".join(paths)}</g></mask></defs>'
            f'<image href="{blob}" x="0" y="0" width="{W}" height="{H}" mask="url(#sgm{i})"></image></svg>')
out = sys.argv[1]
IDS = ['b50ab447ec0cca3f6303a8901bde60d6', '1e6cd943c48f78f7ff61c8d603097c89', '19c77e986ec7f059e207a98279bd2013', 'd316bb421b3af01517904a93bf1aa6b0', '19fcf8ee6e0cfc7132cb5d51e636d320',
       '99b598f8e16ca0aebaa9e2ed60b823a9', '3751c3469bdc0fb7ccca0c535518f0a7', '3f1ccfd5c2f251b4e6297e0fb52084b3', '5ef54d00b163e9f0d6875bf59f10f151', '1324962addb5ed35403c73efd43757fa']
NAMES = [('Fine pen', 'One fluid stroke, long T bar that sweeps into the name.'),
         ('Brush pen', 'Bold, fast, dry-brush edges. The loudest option.'),
         ('Monoline', 'Neat, compact, even line. Quiet and product-y.'),
         ('Swash underline', 'The e trails into a loop that underlines the whole name.'),
         ('Pointed pen', 'Calligraphic thick-and-thin. Note: the T reads a little like a J.'),
         ('Marker', 'Rounded felt-tip, friendly and legible at small sizes.'),
         ('Long crossbar', 'T bar runs over the whole name; i dotted with a small circle.'),
         ('Architect scribble', 'Light and quick, rising to the right.'),
         ('Fountain pen', 'Rising slightly, one loop on the L, soft tail.'),
         ('Connected T and L', 'T and L joined into one monogram-like stroke.')]
cards = ''.join(
    f'<section class="sg-card"><div class="sg-top"><span class="sg-k">S{i+1}</span><span class="sg-t">{n}</span></div>'
    f'<div class="sg-stage" style="--cd: {i * 0.25:.2f}s">' + signing_svg(i, '/_blob/' + b, f'Tin Le signature, option {i+1}: {n}') + '</div>'
    f'<div class="sg-row"><div class="sg-mini sg-light"><img src="/_blob/{b}" alt=""></div><div class="sg-mini sg-dark"><img src="/_blob/{b}" alt=""></div>'
    f'<p class="sg-d">{d}</p></div></section>' for i, (b, (n, d)) in enumerate(zip(IDS, NAMES)))
HTML = f'''<!doctype html>
<html>
<head><meta charset="utf-8"><script src="./support.js"></script></head>
<body>
<!-- Signature options: 10 Tin Le signatures from gpt-image-2.5-flare -->
<x-dc>
  <helmet>
    <style>
      html, body {{ margin: 0; height: 100%; }}
    </style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..700&amp;display=swap">
<style>
body{{margin:0}}
.sg-root{{width:1440px;box-sizing:border-box;padding:56px;background:#fafafa;color:#000;font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.sg-k0{{margin:0;font:600 12px/1 Inter,sans-serif;letter-spacing:.08em;color:#b3b3b3}}
.sg-h{{margin:10px 0 0;font:600 24px/36px Inter,sans-serif;letter-spacing:-.01em}}
.sg-p{{margin:6px 0 0;max-width:720px;font:400 15px/22px Inter,sans-serif;color:#666}}
.sg-grid{{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-top:36px}}
.sg-card{{background:#fff;border-radius:20px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06);padding:20px 24px 22px}}
.sg-top{{display:flex;align-items:baseline;gap:10px}}
.sg-k{{font:600 12px/1 Inter,sans-serif;letter-spacing:.08em;color:#b3b3b3}}
.sg-t{{font:600 17px/1 Inter,sans-serif}}
.sg-stage{{display:grid;place-items:center;height:200px;margin-top:12px}}
.sg-sign{{display:block;overflow:visible}}
/* signs itself stroke by stroke: each traced pen stroke draws in order (dash offset), revealing the real ink under it; hover a card to sign again */
.sg-sign path{{stroke-dasharray:1 1;stroke-dashoffset:0;animation-name:sgDraw;animation-timing-function:cubic-bezier(.4,.1,.5,1);animation-fill-mode:both}}
@keyframes sgDraw{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
@keyframes sgDraw2{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
.sg-card:hover .sg-stage{{--cd:0s!important}}.sg-card:hover .sg-sign path{{animation-name:sgDraw2}}
@media (prefers-reduced-motion: reduce){{.sg-sign path{{animation:none}}}}
.sg-row{{display:flex;align-items:center;gap:10px;margin-top:6px}}
.sg-mini{{flex:none;display:grid;place-items:center;width:120px;height:52px;border-radius:10px}}
.sg-mini img{{max-width:96px;max-height:36px;display:block}}
.sg-light{{background:#f4f4f4}}
.sg-dark{{background:#141414}}.sg-dark img{{filter:invert(1)}}
.sg-d{{margin:0 0 0 6px;font:400 14px/1.45 Inter,sans-serif;color:#7a7a7a}}
</style>
  </helmet>
<div class="sg-root" style="--wr: {{{{wr}}}}">
  <p class="sg-k0">SIGNATURE</p>
  <h1 class="sg-h">Tin Le &#183; 10 signature options</h1>
  <p class="sg-p">Made with GPT image 2.5 flare, cleaned to transparent ink so each works on light and dark. Small swatches show them at nav or footer size. Each one signs itself stroke by stroke, in pen order; hover a card to watch it sign again. Pick one and I&#8217;ll swap it in for the &#8220;Tin&#8221; signature on the stuart.re-style page.</p>
  <div class="sg-grid">{cards}</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"writeTime": {{"editor": "range", "default": 2.4, "min": 0.6, "max": 6, "step": 0.1, "unit": "s", "section": "Animation"}}}}'>
class Component extends DCLogic {{
  renderVals() {{ return {{ wr: (this.props.writeTime ?? 2.4) + 's' }}; }}
}}
</script>
</body>
</html>
'''
open(out, 'w').write(HTML); print('ok')
