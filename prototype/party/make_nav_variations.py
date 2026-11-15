"""Box (6) nav variations: V1 gray line + logo + label, V2 spine with branches, V3 dark dock with labels, V4 liquid glass dock.
usage: navvars.py <out.dc.html>"""
import sys, json
out = sys.argv[1]
UO, SF = '/_blob/00e0e1ec841a28c4e0055e4a6738e6b1', '/_blob/ac43d25c19be4e522f4bd492e1c090ab'
BG = ['/_blob/effff208332abe411e27c82aaa87e30d', '/_blob/155942c7f1c522f9aec7d43d1c1d0d0d', '/_blob/8bd998ead1110dbdb0a707cdb0cb6c60']

def ms(white=False):
    c = ['#fff'] * 4 if white else ['#f25022', '#7fba00', '#00a4ef', '#ffb900']
    return (f'<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><rect x="0" y="0" width="9" height="9" fill="{c[0]}"></rect>'
            f'<rect x="11" y="0" width="9" height="9" fill="{c[1]}"></rect><rect x="0" y="11" width="9" height="9" fill="{c[2]}"></rect>'
            f'<rect x="11" y="11" width="9" height="9" fill="{c[3]}"></rect></svg>')
def logos(mono):
    m = ' class="nv-mono"' if mono else ''
    return [
        '<span class="nv-tin">tin</span>',
        ms(mono),
        f'<img src="{UO}" alt="" width="20" height="17"{m}>',
        '<span class="nv-2u">2U</span>',
        f'<img src="{SF}" alt="" width="24" height="17"{m}>',
    ]
ITEMS = [('Home', '#top'), ('Microsoft AI', '#microsoft'), ('University of Oregon', '#uo-teach'), ('2U', '#2u'), ('Salesforce', '#salesforce')]

def nav(v, mono, row):
    L = logos(mono)
    return ''.join(row(v, i, lab, href, L[i]) for i, (lab, href) in enumerate(ITEMS))

r1 = lambda v, i, lab, href, lg: (f'<a class="{{{{{v}{i}}}}}" href="{href}" onClick="{{{{pick{v}{i}}}}}">'
                                  f'<span class="l1-line" aria-hidden="true"></span><span class="l1-ic">{lg}</span><span class="l1-tx">{lab}</span></a>')
r2 = lambda v, i, lab, href, lg: (f'<a class="{{{{{v}{i}}}}}" href="{href}" onClick="{{{{pick{v}{i}}}}}">'
                                  f'<span class="l2-br" aria-hidden="true"></span><span class="l2-tile">{lg}</span><span class="l2-tx">{lab}</span></a>')
r3 = lambda v, i, lab, href, lg: (f'<a class="{{{{{v}{i}}}}}" href="{href}" onClick="{{{{pick{v}{i}}}}}">'
                                  f'<span class="l3-ic">{lg}</span><span class="l3-tx">{lab}</span></a>')
r4 = lambda v, i, lab, href, lg: (f'<a class="{{{{{v}{i}}}}}" href="{href}" aria-label="{lab}" onClick="{{{{pick{v}{i}}}}}">'
                                  f'<span class="l4-ic">{lg}</span><span class="l4-tip">{lab}</span></a>')

def col(tag, title, sub, stage_cls, inner):
    return (f'<section class="nv-col"><p class="nv-k">{tag}</p><h2 class="nv-t">{title}</h2><p class="nv-s">{sub}</p>'
            f'<div class="nv-stage {stage_cls}">{inner}</div></section>')

bgstack = ''.join(f'<img src="{u}" alt="">' for u in BG + BG[:1])
V1 = col('V1', 'Gray line', 'A gray line runs in from the left edge to each logo and label. The current page gets a longer black line.', 'st-white',
         f'<nav class="l1" aria-label="Site, version 1">{nav("A", False, r1)}</nav>')
V2 = col('V2', 'Spine', 'One gray line down the left with a branch out to each item. A black marker slides to the current page.', 'st-white',
         f'<nav class="l2" aria-label="Site, version 2"><span class="l2-spine" aria-hidden="true"></span><span class="l2-mark" aria-hidden="true" style="transform: translateY({{{{bY}}}})"></span>{nav("B", False, r2)}</nav>')
V3 = col('V3', 'Dark dock, labeled', 'The original dock, opened up so every logo has its name next to it.', 'st-white',
         f'<nav class="l3" aria-label="Site, version 3">{nav("C", True, r3)}</nav>')
V4 = col('V4', 'Liquid glass', 'The dock as a sheet of glass: it blurs, bends and tints whatever scrolls under it. Labels appear on hover.', 'st-photo',
         f'<div class="l4-bg" aria-hidden="true"><div class="l4-track">{bgstack}</div></div>'
         f'<nav class="l4" aria-label="Site, version 4"><span class="l4-fx" aria-hidden="true"></span><span class="l4-tint" aria-hidden="true"></span><span class="l4-shine" aria-hidden="true"></span>{nav("D", True, r4)}</nav>')

SVG = ('<svg class="nv-defs" width="0" height="0" aria-hidden="true" focusable="false"><filter id="nv-glass" x="0%" y="0%" width="100%" height="100%" filterUnits="objectBoundingBox">'
       '<feTurbulence type="fractalNoise" baseFrequency="0.012 0.012" numOctaves="2" seed="92" result="noise"></feTurbulence>'
       '<feGaussianBlur in="noise" stdDeviation="2" result="soft"></feGaussianBlur>'
       '<feDisplacementMap in="SourceGraphic" in2="soft" scale="{{glassBend}}" xChannelSelector="R" yChannelSelector="G"></feDisplacementMap>'
       '</filter></svg>')

CSS = r'''
body{margin:0}
sc-for, sc-if { display: contents; }
.nv-root{width:1600px;box-sizing:border-box;padding:56px;background:#fafafa;color:#000;font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased;display:grid;grid-template-columns:repeat(4,1fr);gap:24px}
.nv-defs{position:absolute;width:0;height:0;overflow:hidden}
.nv-k{margin:0;font:600 12px/1 Inter,sans-serif;letter-spacing:.08em;color:#b3b3b3}
.nv-t{margin:10px 0 0;font:600 20px/1.3 Inter,sans-serif;letter-spacing:-.01em}
.nv-s{margin:6px 0 0;min-height:60px;font:400 14px/1.45 Inter,sans-serif;color:#7a7a7a}
.nv-stage{position:relative;margin-top:20px;height:440px;border-radius:20px;overflow:hidden}
.st-white{background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}
.st-photo{background:#1d2633}
.nv-tin{font:400 22px/1 Caveat,cursive}
.nv-2u{font:700 13px/1 Inter,system-ui,sans-serif;letter-spacing:-.02em}
.nv-mono{filter:brightness(0) invert(1)}
.nv-root a{text-decoration:none;color:inherit;-webkit-tap-highlight-color:transparent}
.nv-root a:focus-visible{outline:2px solid #0099ff;outline-offset:2px;border-radius:8px}
.nv-root img{display:block}

/* V1: gray line, logo, label */
.l1{position:absolute;left:0;top:56px;display:flex;flex-direction:column;gap:var(--rowGap,6px)}
.l1 a{display:flex;align-items:center;height:36px;padding-right:12px}
.l1-line{flex:none;width:var(--lineLen,24px);height:1px;background:#d6d6d6;transition:width .35s cubic-bezier(.2,.7,.2,1),background-color .25s}
.l1-ic{flex:none;display:grid;place-items:center;width:28px;height:28px;margin-left:10px;color:#000}
.l1-tx{margin-left:8px;font:500 15px/1 Inter,sans-serif;color:#9a9a9a;white-space:nowrap;transition:color .2s}
.l1 a:hover .l1-line{width:calc(var(--lineLen,24px) + 12px);background:#8c8c8c}
.l1 a:hover .l1-tx{color:#000}
.l1 a.on .l1-line{width:calc(var(--lineLen,24px) + 20px);background:#000}
.l1 a.on .l1-tx{color:#000;font-weight:600}

/* V2: spine with branches */
.l2{position:absolute;left:28px;top:56px;display:flex;flex-direction:column;gap:8px;padding:0}
.l2-spine{position:absolute;left:0;top:22px;bottom:22px;width:1px;background:#e3e3e3}
.l2-mark{position:absolute;left:-1px;top:4px;width:3px;height:36px;border-radius:2px;background:#000;transition:transform .45s cubic-bezier(.6,0,.2,1)}
.l2 a{position:relative;display:flex;align-items:center;height:44px}
.l2-br{flex:none;width:18px;height:1px;background:#e3e3e3;transition:background-color .2s}
.l2-tile{flex:none;display:grid;place-items:center;width:36px;height:36px;border-radius:10px;background:#fff;color:#000;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08),0 1px 2px rgba(0,0,0,.05);transition:box-shadow .2s,transform .2s}
.l2-tx{margin-left:12px;font:500 15px/1 Inter,sans-serif;color:#9a9a9a;white-space:nowrap;transition:color .2s}
.l2 a:hover .l2-tx{color:#000}.l2 a:hover .l2-tile{box-shadow:inset 0 0 0 1px rgba(0,0,0,.16),0 2px 6px rgba(0,0,0,.08)}
.l2 a.on .l2-br{background:#000}
.l2 a.on .l2-tx{color:#000;font-weight:600}
.l2 a.on .l2-tile{box-shadow:inset 0 0 0 1px rgba(0,0,0,.9)}

/* V3: dark dock with labels */
.l3{position:absolute;left:24px;top:56px;display:flex;flex-direction:column;gap:4px;padding:8px;border-radius:20px;background:#2b2b2d;box-shadow:0 1px 0 rgba(255,255,255,.08) inset,0 18px 40px -16px rgba(0,0,0,.45)}
.l3 a{display:flex;align-items:center;gap:6px;height:44px;padding:0 16px 0 0;border-radius:12px;transition:background-color .2s}
.l3-ic{flex:none;display:grid;place-items:center;width:44px;height:44px;color:#fff;opacity:.92}
.l3-tx{font:500 14px/1 Inter,sans-serif;color:rgba(255,255,255,.6);white-space:nowrap;transition:color .2s}
.l3 a:hover{background:rgba(255,255,255,.08)}.l3 a:hover .l3-tx{color:#fff}
.l3 a.on{background:rgba(255,255,255,.14)}.l3 a.on .l3-tx{color:#fff}

/* V4: liquid glass */
.l4-bg{position:absolute;inset:0;overflow:hidden}
.l4-track{display:flex;flex-direction:column;gap:12px;padding:0 14px;animation:l4scroll 26s linear infinite}
.l4-track img{width:100%;height:260px;object-fit:cover;border-radius:10px}
@keyframes l4scroll{to{transform:translateY(calc(-3 * 272px))}}
.l4{position:absolute;left:20px;top:56px;display:flex;flex-direction:column;gap:6px;padding:8px;border-radius:24px;isolation:isolate;box-shadow:0 10px 30px -10px rgba(0,0,0,.35),0 2px 6px rgba(0,0,0,.12)}
.l4-fx,.l4-tint,.l4-shine{position:absolute;inset:0;border-radius:inherit;pointer-events:none}
.l4-fx{z-index:0;overflow:hidden;-webkit-backdrop-filter:blur(var(--glassBlur,3px)) saturate(1.7);backdrop-filter:blur(var(--glassBlur,3px)) saturate(1.7);backdrop-filter:url(#nv-glass) blur(var(--glassBlur,3px)) saturate(1.7)}
.l4-tint{z-index:1;background:rgba(255,255,255,var(--glassTint,.16))}
.l4-shine{z-index:2;box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.7),inset -1px -1px 1px rgba(255,255,255,.35),inset 0 0 18px rgba(255,255,255,.18)}
.l4 a{position:relative;z-index:3;display:grid;place-items:center;width:48px;height:48px;border-radius:16px;transition:background-color .2s,box-shadow .2s}
.l4-ic{display:grid;place-items:center;color:#fff;filter:drop-shadow(0 1px 2px rgba(0,0,0,.35))}
.l4 a:hover{background:rgba(255,255,255,.14)}
.l4 a.on{background:rgba(255,255,255,.26);box-shadow:inset 0 0 0 1px rgba(255,255,255,.45),inset 0 1px 0 rgba(255,255,255,.6)}
.l4-tip{position:absolute;left:62px;top:50%;transform:translate(-4px,-50%);white-space:nowrap;padding:7px 11px;border-radius:10px;font:500 13px/1 Inter,sans-serif;color:#fff;background:rgba(30,30,34,.38);-webkit-backdrop-filter:blur(14px) saturate(1.6);backdrop-filter:blur(14px) saturate(1.6);box-shadow:inset 1px 1px 0 rgba(255,255,255,.4),inset -1px -1px 0 rgba(255,255,255,.12);opacity:0;pointer-events:none;transition:opacity .15s,transform .15s}
.l4 a:hover .l4-tip,.l4 a:focus-visible .l4-tip{opacity:1;transform:translate(0,-50%)}
@media (prefers-reduced-motion: reduce){.l4-track{animation:none}.l1-line,.l2-mark{transition:none}}
'''

TPL = f'''<!doctype html>
<html>
<head><meta charset="utf-8"><script src="./support.js"></script></head>
<body>
<!-- Box (6) nav variations: gray line, spine, labeled dark dock, liquid glass -->
<x-dc>
  <helmet>
    <style>
      html, body {{ margin: 0; height: 100%; }}
    </style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..700&amp;family=Caveat:wght@400;600&amp;display=swap">
<style>{CSS}</style>
  </helmet>
<div class="nv-root" style="--lineLen: {{{{lineLen}}}}; --rowGap: {{{{rowGap}}}}; --glassBlur: {{{{glassBlur}}}}; --glassTint: {{{{glassTint}}}}">{SVG}
  {V1}
  {V2}
  {V3}
  {V4}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='PROPS'>
class Component extends DCLogic {{
  constructor(props) {{ super(props); this.state = {{ A: 0, B: 0, C: 0, D: 0 }}; }}
  renderVals() {{
    const st = this.state, p = this.props, v = {{}};
    const base = {{ A: '', B: '', C: '', D: '' }};
    for (const k of ['A', 'B', 'C', 'D']) for (let i = 0; i < 5; i++) {{
      v[k + i] = st[k] === i ? 'on' : '';
      v['pick' + k + i] = (e) => {{ if (e && e.preventDefault) e.preventDefault(); this.setState({{ [k]: i }}); }};
    }}
    v.bY = (st.B * 52) + 'px';
    v.lineLen = (p.lineLength ?? 24) + 'px';
    v.rowGap = (p.rowGap ?? 6) + 'px';
    v.glassBlur = (p.glassBlur ?? 3) + 'px';
    v.glassTint = String(p.glassTint ?? 0.16);
    v.glassBend = String(p.glassBend ?? 60);
    return v;
  }}
}}
</script>
</body>
</html>
'''
PROPS = {
    'lineLength': {"editor": "range", "default": 24, "min": 8, "max": 80, "step": 1, "unit": "px", "section": "V1 gray line"},
    'rowGap': {"editor": "range", "default": 6, "min": 0, "max": 24, "step": 1, "unit": "px", "section": "V1 gray line"},
    'glassBend': {"editor": "range", "default": 60, "min": 0, "max": 160, "step": 1, "section": "V4 liquid glass"},
    'glassBlur': {"editor": "range", "default": 3, "min": 0, "max": 16, "step": 0.5, "unit": "px", "section": "V4 liquid glass"},
    'glassTint': {"editor": "range", "default": 0.16, "min": 0, "max": 0.6, "step": 0.01, "section": "V4 liquid glass"},
}
s = TPL.replace('PROPS', json.dumps(PROPS).replace('&', '&amp;').replace("'", '&#39;'))
open(out, 'w').write(s)
print('ok', len(s))
