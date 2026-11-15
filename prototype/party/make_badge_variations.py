"""Badge variations board: the Salesforce badge, original + 5 styles, each shown front and back side by side."""
import json
S = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/'
IMG = '/_blob/078fce442a609c4bff7139218f2023a2'   # drawing: posting a letter
LOGO = '/_blob/ac43d25c19be4e522f4bd492e1c090ab'  # Salesforce cloud
DESC = ('Enterprise tools and the design system behind them. I redesigned Salesforce Help so people could find answers on their own, '
        'reworked Manage Users to cut support cases, and built a back-to-work app for 75K employees.')
ARROW = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
LG = f'<img src="{LOGO}" alt="Salesforce" width="22" height="16" style="display: block; object-fit: contain">'
bd_css = open(S + 'bd_css.txt').read()

PAIRS = []
# Original (the badge on the homepage)
PAIRS.append(('Original &middot; current badge', 'row', f'''
<div class="hang"><span class="thread"></span><span class="bd-clip"></span>
<div class="bd-face o-card">
  <div class="bd-top"><span>Experience &middot; Before</span><span>#03</span></div>
  <div class="bd-photo" style="background-color: #d5ecff"><img src="{IMG}" alt="Drawing of Tin posting a letter"><span class="bd-logo">{LG}</span></div>
  <p class="bd-name">Salesforce</p><p class="bd-role">Product Designer</p>
  <div class="bd-foot"><span>2017 &mdash; 2022 &middot; 5 yrs</span><span class="bd-arrow">{ARROW}</span></div>
</div></div>''', f'''
<div class="bd-face o-card o-back">
  <div class="bd-top"><span>Experience &middot; Before</span><span>#03</span></div>
  <p class="bd-bk">What I did there</p>
  <p class="bd-desc">{DESC}</p>
  <div class="bd-foot"><span>Flip back</span><span class="bd-arrow bd-arrow-back">{ARROW}</span></div>
</div>'''))

# V1 Lanyard ID
PAIRS.append(('V1 &middot; Lanyard ID', 'row', f'''
<div class="hang"><span class="v1-strap"></span>
<div class="v1">
  <div class="v1-band"><span class="v1-slot"></span><div class="v1-brand">{LG}<span>Salesforce</span></div></div>
  <div class="v1-photo"><img src="{IMG}" alt="Drawing of Tin posting a letter"></div>
  <p class="v1-name">Tin Le</p><p class="v1-role">Product Designer</p>
  <div class="v1-meta"><div><span>From</span><b>2017</b></div><div><span>To</span><b>2022</b></div><div><span>Tenure</span><b>5 yrs</b></div></div>
  <div class="v1-barcode"></div><p class="v1-id">ID 03 &middot; Experience</p>
</div></div>''', f'''
<div class="v1">
  <div class="v1-band"><span class="v1-slot"></span><div class="v1-brand">{LG}<span>Salesforce</span></div></div>
  <div class="v1-body">
    <p class="v1-k">What I did there</p>
    <p class="v1-desc">{DESC}</p>
    <p class="v1-fine">If found, please return to Tin Le.</p>
    <p class="v1-sign">Tin Le</p>
  </div>
</div>'''))

# V2 Polaroid
PAIRS.append(('V2 &middot; Polaroid', 'row', f'''
<div class="hang"><span class="thread"></span><span class="v2-pin"></span>
<div class="v2">
  <div class="v2-photo"><img src="{IMG}" alt="Drawing of Tin posting a letter"></div>
  <p class="v2-cap">Salesforce, 2017&ndash;22</p>
  <p class="v2-sub">Product Designer &middot; 5 yrs</p>
</div></div>''', f'''
<div class="v2 v2-back">
  <span class="v2-tape"></span>
  <p class="v2-hand">{DESC}</p>
  <div class="v2-stamp"><span>five</span><b>years</b><span>2017&ndash;22</span></div>
</div>'''))

# V3 Trading card
PAIRS.append(('V3 &middot; Trading card', 'row', f'''
<div class="hang"><span class="thread"></span><span class="v3-ring"></span>
<div class="v3"><div class="v3-in">
  <div class="v3-top"><span>#03 &middot; Before</span><span>&#9733; Rare</span></div>
  <div class="v3-photo"><img src="{IMG}" alt="Drawing of Tin posting a letter"><span class="v3-logo">{LG}</span></div>
  <p class="v3-name">Salesforce</p><p class="v3-type">Product Designer</p>
  <div class="v3-stats"><div><b>5</b><span>Years</span></div><div><b>2017</b><span>From</span></div><div><b>2022</b><span>To</span></div></div>
</div></div></div>''', f'''
<div class="v3"><div class="v3-in v3-back">
  <div class="v3-top"><span>#03 &middot; Before</span><span>&#9733; Rare</span></div>
  <p class="v3-k">Abilities</p>
  <p class="v3-desc">{DESC}</p>
  <div class="v3-chips"><span>Design system</span><span>Salesforce Help</span><span>Manage Users</span><span>Back-to-work app</span></div>
</div></div>'''))

# V4 Boarding pass
PAIRS.append(('V4 &middot; Boarding pass', 'col', f'''
<div class="hang"><span class="thread"></span>
<div class="v4">
  <div class="v4-main">
    <div class="v4-head"><span class="v4-brand">{LG}Salesforce</span><span>Boarding pass &middot; Experience</span></div>
    <div class="v4-route"><div><span>From</span><b>2017</b></div><span class="v4-plane">&#9992;</span><div><span>To</span><b>2022</b></div></div>
    <div class="v4-fields"><div><span>Passenger</span><b>Tin Le</b></div><div><span>Seat</span><b>Product Designer</b></div><div><span>Flight</span><b>SF&middot;03</b></div><div><span>Duration</span><b>5 yrs</b></div></div>
  </div>
  <div class="v4-stub"><img src="{IMG}" alt="Drawing of Tin posting a letter"><div class="v4-code"></div></div>
</div></div>''', f'''
<div class="v4 v4-back">
  <div class="v4-main">
    <div class="v4-head"><span class="v4-brand">{LG}Salesforce</span><span>Itinerary notes</span></div>
    <p class="v4-desc">{DESC}</p>
    <p class="v4-stops"><span>Stops</span> Design system &middot; Salesforce Help &middot; Manage Users &middot; Back-to-work app</p>
  </div>
  <div class="v4-stub"><p class="v4-gate">Gate<br><b>03</b></p><div class="v4-code"></div></div>
</div>'''))

# V5 Brand pop-out
PAIRS.append(('V5 &middot; Brand pop-out', 'row', f'''
<div class="hang">
<div class="v5">
  <img class="v5-pop" src="{IMG}" alt="Drawing of Tin posting a letter">
  <span class="v5-mark"><img src="{LOGO}" alt=""></span>
  <p class="v5-k">Experience &middot; #03</p>
  <p class="v5-name">Salesforce</p><p class="v5-role">Product Designer</p>
  <div class="v5-chip">2017 &mdash; 2022 &middot; 5 yrs</div>
</div></div>''', f'''
<div class="v5 v5-back">
  <p class="v5-k">What I did there</p>
  <p class="v5-desc">{DESC}</p>
  <div class="v5-chip">Salesforce &middot; 5 yrs</div>
</div>'''))

CSS = r'''
body{margin:0}
sc-for, sc-if { display: contents; }
.bv{box-sizing:border-box;width:1440px;padding:56px 64px 96px;background:var(--desk,#f5f5f5);font-family:'Be Vietnam Pro',system-ui,sans-serif;color:#141414}
.bv h1{margin:0;font:400 44px/1.1 Caveat,sans-serif}
.bv-sub{margin:6px 0 40px;color:#6e6e6e;font-size:15px}
.bv-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:48px;row-gap:64px}
.bv-pair{border-radius:28px;background:var(--panel,#ececec);padding:26px 26px 30px}
.bv-label{margin:0 0 22px;font-size:13px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#6e6e6e}
.bv-sides{display:flex;gap:28px;align-items:stretch;justify-content:center}
.bv-sides.col{flex-direction:column;align-items:center}
.bv-side{display:flex;flex-direction:column;align-items:center;gap:12px}
.bv-side > .bv-cap{order:2;margin:0;font-size:12px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:#9a9a9a}
.bv-sides.row .bv-side{flex:1 1 0;min-width:0}
.bv-sides.row .bv-side > :first-child{flex:1}
.hang{position:relative;display:flex;flex-direction:column;align-items:center;padding-top:36px;height:100%;box-sizing:border-box}
.thread{position:absolute;left:50%;top:0;width:1.5px;height:30px;margin-left:-.75px;background:#9d9d9d}
.hang > .bd-clip{top:22px}
/* original */
''' + bd_css + r'''
.o-card{width:282px;height:100%}
.o-back{display:flex;flex-direction:column;margin-top:36px;height:calc(100% - 36px)}
.o-back .bd-foot{margin-top:auto}
/* V1 lanyard */
.v1-strap{position:absolute;left:50%;top:0;width:26px;height:44px;margin-left:-13px;background:repeating-linear-gradient(90deg,#0176d3 0 3px,#0b86e0 3px 6px);border-radius:3px 3px 0 0}
.v1{position:relative;width:270px;border-radius:18px;background:#fff;overflow:hidden;box-shadow:0 24px 48px -26px rgba(0,0,0,.4),0 2px 6px rgba(0,0,0,.06);text-align:center;margin-top:8px;height:calc(100% - 8px);display:flex;flex-direction:column}
.v1-band{position:relative;height:104px;background:linear-gradient(135deg,#00a1e0,#0176d3);display:flex;align-items:flex-start;justify-content:center;padding-top:40px;box-sizing:border-box}
.v1-slot{position:absolute;left:50%;top:14px;width:54px;height:12px;margin-left:-27px;border-radius:8px;background:#f5f5f5;box-shadow:inset 0 2px 3px rgba(0,0,0,.25)}
.v1-brand{display:flex;align-items:center;gap:8px;color:#fff;font-weight:600;font-size:17px;letter-spacing:.02em}
.v1-brand img{filter:brightness(0) invert(1)}
.v1-photo{width:132px;height:132px;margin:-26px auto 0;border-radius:50%;background:#d5ecff;border:5px solid #fff;overflow:hidden;display:grid;place-items:end center;position:relative}
.v1-photo img{width:88%;height:88%;object-fit:contain;object-position:50% 100%}
.v1-name{margin:14px 0 0;font-size:26px;font-weight:600;letter-spacing:-.01em}
.v1-role{margin:4px 0 0;color:#6e6e6e;font-size:15px}
.v1-meta{display:grid;grid-template-columns:repeat(3,1fr);margin:18px 18px 0;padding:12px 0;border-top:1px solid #eee;border-bottom:1px solid #eee}
.v1-meta span{display:block;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#9a9a9a}
.v1-meta b{font-size:16px;font-weight:600}
.v1-barcode{height:34px;margin:16px 30px 0;background:repeating-linear-gradient(90deg,#141414 0 2px,transparent 2px 4px,#141414 4px 5px,transparent 5px 8px,#141414 8px 11px,transparent 11px 12px)}
.v1-id{margin:6px 0 18px;font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:#9a9a9a}
.v1-band + .v1-body{margin-top:-40px;position:relative;background:#fff;border-radius:16px 16px 0 0}
.v1-body{padding:22px 24px 22px;text-align:left;display:flex;flex-direction:column;flex:1}
.v1-k{margin:0;font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:#0176d3}
.v1-desc{margin:10px 0 0;font-size:17px;line-height:1.5}
.v1-fine{margin:auto 0 0;padding-top:18px;font-size:11px;color:#9a9a9a}
.v1-sign{margin:6px 0 0;padding-top:4px;border-top:1px solid #ddd;font:400 30px/1 Caveat,sans-serif;color:#0176d3}
/* V2 polaroid */
.v2-pin{position:absolute;left:50%;top:22px;z-index:2;width:16px;height:40px;margin-left:-8px;border-radius:4px;background:linear-gradient(90deg,#c9a173,#e2c296,#c9a173);box-shadow:0 2px 4px rgba(0,0,0,.2)}
.v2{position:relative;width:268px;background:#fff;padding:14px 14px 18px;box-sizing:border-box;box-shadow:0 24px 44px -24px rgba(0,0,0,.45),0 1px 3px rgba(0,0,0,.08);transform:rotate(-2deg);height:100%}
.v2-photo{aspect-ratio:1 / 1;background:#d5ecff;display:grid;place-items:end center;overflow:hidden}
.v2-photo img{width:86%;height:86%;object-fit:contain;object-position:50% 100%}
.v2-cap{margin:16px 4px 0;font:400 32px/1 Caveat,sans-serif}
.v2-sub{margin:6px 4px 0;font-size:13px;color:#6e6e6e}
.v2-back{background:#eadfc8;transform:rotate(1.5deg);margin-top:36px;height:calc(100% - 36px);padding:66px 22px 22px}
.v2-tape{position:absolute;left:50%;top:-12px;width:96px;height:26px;margin-left:-48px;background:rgba(255,255,255,.6);box-shadow:0 1px 2px rgba(0,0,0,.08);transform:rotate(-3deg)}
.v2-hand{margin:0;font:400 25px/1.3 Caveat,sans-serif;color:#2b2620}
.v2-stamp{position:absolute;right:-16px;top:-26px;background:rgba(234,223,200,.6);width:86px;height:86px;border-radius:50%;border:2.5px double #0176d3;color:#0176d3;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-12deg);font-size:10px;letter-spacing:.12em;text-transform:uppercase}
.v2-stamp b{font-size:15px;letter-spacing:.06em}
/* V3 trading card */
.v3-ring{position:absolute;left:50%;top:24px;z-index:2;width:16px;height:16px;margin-left:-8px;border-radius:50%;border:3px solid #a7a7ad;background:transparent}
.v3{width:276px;border-radius:22px;padding:4px;background:conic-gradient(from 180deg,#7cf9ff,#ff4fd8,#fff05a,#8bff6a,#7cf9ff);box-shadow:0 24px 48px -24px rgba(0,0,0,.5);height:100%;box-sizing:border-box}
.v3-in{height:100%;box-sizing:border-box;border-radius:18px;background:#16151c;color:#f4f1ea;padding:16px 16px 18px;display:flex;flex-direction:column}
.v3-top{display:flex;justify-content:space-between;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#aaa4b8}
.v3-top span:last-child{color:#fff05a}
.v3-photo{position:relative;margin-top:12px;aspect-ratio:1 / 1;border-radius:120px 120px 12px 12px;background:linear-gradient(#00a1e0,#0176d3);display:grid;place-items:end center;overflow:hidden}
.v3-photo img{width:86%;height:86%;object-fit:contain;object-position:50% 100%;filter:invert(1)}
.v3-logo{position:absolute;left:10px;bottom:10px;width:34px;height:34px;border-radius:50%;background:#fff;display:grid;place-items:center}
.v3-name{margin:14px 2px 0;font-size:24px;font-weight:700;letter-spacing:.04em;text-transform:uppercase}
.v3-type{margin:2px 2px 0;font-size:14px;color:#aaa4b8}
.v3-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:14px}
.v3-stats div{border-radius:10px;background:rgba(255,255,255,.07);padding:8px 0;text-align:center}
.v3-stats b{display:block;font-size:17px}
.v3-stats span{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#aaa4b8}
.v3-back{margin-top:0}
.v3-k{margin:18px 2px 0;font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#7cf9ff}
.v3-desc{margin:10px 2px 0;font-size:16px;line-height:1.5}
.v3-chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:auto;padding-top:16px}
.v3-chips span{border-radius:999px;border:1px solid rgba(255,255,255,.25);padding:5px 10px;font-size:12px}
.bv-side .v3{margin-top:0}
.bv-sides.row .bv-side:last-child .v3{margin-top:36px;height:calc(100% - 36px)}
/* V4 boarding pass */
.v4{display:flex;width:520px;min-height:208px;border-radius:18px;background:#fff;box-shadow:0 24px 48px -26px rgba(0,0,0,.4),0 2px 6px rgba(0,0,0,.06);overflow:hidden}
.v4-main{flex:1;padding:18px 22px;display:flex;flex-direction:column}
.v4-head{display:flex;justify-content:space-between;align-items:center;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:#9a9a9a}
.v4-brand{display:flex;align-items:center;gap:8px;font-size:14px;letter-spacing:.02em;text-transform:none;font-weight:600;color:#0176d3}
.v4-route{display:flex;align-items:center;gap:18px;margin-top:12px}
.v4-route span{display:block;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#9a9a9a}
.v4-route b{font-size:38px;font-weight:600;letter-spacing:-.02em}
.v4-plane{font-size:22px !important;color:#0176d3 !important;letter-spacing:0 !important}
.v4-fields{display:grid;grid-template-columns:repeat(4,auto);gap:14px;margin-top:auto;padding-top:12px}
.v4-fields span{display:block;font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:#9a9a9a}
.v4-fields b{font-size:13px;font-weight:600}
.v4-stub{position:relative;width:118px;border-left:2px dashed #dcdcdc;background:#d5ecff;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:14px 10px}
.v4-stub::before,.v4-stub::after{content:"";position:absolute;left:-11px;width:20px;height:20px;border-radius:50%;background:var(--panel,#ececec)}
.v4-stub::before{top:-10px}.v4-stub::after{bottom:-10px}
.v4-stub img{width:96px;height:96px;object-fit:contain}
.v4-code{width:84px;height:30px;background:repeating-linear-gradient(90deg,#141414 0 2px,transparent 2px 4px,#141414 4px 5px,transparent 5px 8px)}
.v4-desc{margin:12px 0 0;font-size:15px;line-height:1.5}
.v4-stops{margin:auto 0 0;padding-top:12px;font-size:12px;color:#6e6e6e}
.v4-stops span{font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#9a9a9a;margin-right:6px}
.v4-gate{margin:8px 0 0;text-align:center;font-size:10px;letter-spacing:.14em;text-transform:uppercase;color:#6e6e6e}
.v4-gate b{font-size:40px;letter-spacing:0;color:#0176d3}
/* V5 brand pop-out */
.v5{position:relative;width:276px;border-radius:24px;background:linear-gradient(160deg,#1ab9f0,#0176d3 70%);color:#fff;padding:150px 22px 22px;box-sizing:border-box;margin-top:60px;height:calc(100% - 60px);overflow:visible;box-shadow:0 26px 50px -24px rgba(1,118,211,.65)}
.hang .v5{margin-top:60px}
.v5-pop{position:absolute;left:50%;top:-78px;width:210px;height:210px;margin-left:-105px;object-fit:contain;object-position:50% 100%;filter:invert(1) drop-shadow(0 6px 10px rgba(0,0,0,.25))}
.v5-mark{position:absolute;right:-8px;bottom:12px;width:140px;opacity:.12;filter:brightness(0) invert(1);pointer-events:none}
.v5-mark img{width:100%;display:block}
.v5-k{margin:0;font-size:11px;letter-spacing:.14em;text-transform:uppercase;opacity:.8}
.v5-name{margin:6px 0 0;font-size:32px;font-weight:600;letter-spacing:-.02em}
.v5-role{margin:4px 0 0;font-size:16px;opacity:.9}
.v5-chip{display:inline-block;margin-top:18px;border-radius:999px;padding:8px 14px;background:rgba(255,255,255,.18);backdrop-filter:blur(6px);border:1px solid rgba(255,255,255,.35);font-size:12px;letter-spacing:.1em;text-transform:uppercase}
.v5-back{background:#fff;color:#141414;padding:26px 22px 22px;display:flex;flex-direction:column;box-shadow:0 24px 48px -26px rgba(0,0,0,.4);border-top:6px solid #0176d3}
.v5-back .v5-k{color:#0176d3;opacity:1}
.v5-desc{margin:12px 0 0;font-size:18px;line-height:1.5}
.v5-back .v5-chip{margin-top:auto;align-self:flex-start;background:#eaf5fe;border-color:#cfe6fb;color:#0176d3}
'''

def pair(label, layout, front, back):
    return (f'<div class="bv-pair"><p class="bv-label">{label}</p><div class="bv-sides {layout}">'
            f'<div class="bv-side">{front}<p class="bv-cap">Front</p></div>'
            f'<div class="bv-side">{back}<p class="bv-cap">Back</p></div></div></div>')

BODY = ('<section class="bv" style="--desk: {{desk}}; --panel: {{panel}}">\n'
        '  <h1>Badge variations</h1>\n  <p class="bv-sub">The Salesforce badge from the experience string, front and back. Original first, then five directions to design from.</p>\n'
        '  <div class="bv-grid">' + ''.join(pair(*p) for p in PAIRS) + '</div>\n</section>')
props = {"desk": {"editor": "color", "default": "#f5f5f5", "section": "Board"},
         "panel": {"editor": "color", "default": "#ececec", "section": "Board"},
         "$preview": {"width": 1440, "height": 2400}}
attr = json.dumps(props, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
out = ('<!doctype html>\n<html>\n<head><meta charset="utf-8"><script src="./support.js"></script></head>\n<body>\n'
       '<!-- Badge variations: the experience badge, front and back, original + 5 directions -->\n<x-dc>\n<helmet>\n'
       '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Caveat:wght@400;500;600;700&amp;family=Be+Vietnam+Pro:wght@400;500;600;700&amp;display=swap">\n'
       '<style>' + CSS + '</style>\n</helmet>\n' + BODY + '\n</x-dc>\n'
       "<script type=\"text/x-dc\" data-dc-script data-props='" + attr + "'>\n"
       "class Component extends DCLogic {\n  renderVals() {\n    return { desk: this.props.desk ?? '#f5f5f5', panel: this.props.panel ?? '#ececec' };\n  }\n}\n</script>\n</body>\n</html>\n")
open(S + 'canvas4/project/BadgeVariations.dc.html', 'w').write(out)
print('ok', len(out))
