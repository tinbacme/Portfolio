"""Experience badges hanging on a string (under About): front = drawing of Tin, company, title, how long; click flips to the description.
usage: badges.py <board.dc.html>   (edits in place)
"""
import sys, re, json, html
p = sys.argv[1]; s = open(p).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:100], s.count(old)); s = s.replace(old, new)

WAVE0 = re.search(r"const TR_WAVE = \['(/_blob/[0-9a-f]{32})'", s).group(1)
MAIL = re.findall(r"/_blob/[0-9a-f]{32}", re.search(r"const TR_MAIL = \[[^\]]*\]", s).group(0))
PARTY = re.findall(r"/_blob/[0-9a-f]{32}", re.search(r"const TR_PARTY = \[[^\]]*\]", s).group(0))
MS_SVG = ('<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><rect x="0" y="0" width="9" height="9" fill="#f25022"></rect>'
          '<rect x="11" y="0" width="9" height="9" fill="#7fba00"></rect><rect x="0" y="11" width="9" height="9" fill="#00a4ef"></rect>'
          '<rect x="11" y="11" width="9" height="9" fill="#ffb900"></rect></svg>')
ARROW = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
HAND = re.findall(r"/_blob/[0-9a-f]{32}", re.search(r"const TR_HAND = \[[^\]]*\]", s).group(0))
WAVES = re.findall(r"/_blob/[0-9a-f]{32}", re.search(r"const TR_WAVE = \[[^\]]*\]", s).group(0))
SF = '<img src="/_blob/ac43d25c19be4e522f4bd492e1c090ab" alt="" width="22" height="16" style="display: block; object-fit: contain">'
UO = '<img src="/_blob/00e0e1ec841a28c4e0055e4a6738e6b1" alt="" width="18" height="18" style="display: block; object-fit: contain">'
LX = '<span style="font: 700 15px/1 Be Vietnam Pro, system-ui, sans-serif; color: #141414">L</span>'
CARDS = [
 dict(kicker='Experience &middot; Now', bg='#dfe4ff', img=WAVE0, alt='Drawing of Tin waving', logo=MS_SVG,
      name='Microsoft AI', role='Senior Product Designer', when='2022 &mdash; now', dur='4 yrs',
      back_k='What I do there', back=('Search across Bing, Edge and Windows. Today that means helping people find what they need, '
                                       'growing Bing, and exploring what AI agents could do in search.'), tilt=-4, drop=70, dl=-0.6),
 dict(kicker='Teaching &middot; Now', bg='#ffe68a', img=PARTY[14], alt='Drawing of Tin in sunglasses', logo=UO,
      name='University of Oregon', role='Product Design Instructor', when='2023 &mdash; now', dur='3 yrs',
      back_k='What I teach', back=('UX and product design, at the same school where I studied industrial design. '
                                    'Students learn the way I still work: by building and prototyping.'), tilt=2.5, drop=150, dl=-2.1),
 dict(kicker='Experience &middot; Before', bg='#d5ecff', img=MAIL[12], alt='Drawing of Tin posting a letter', logo=SF,
      name='Salesforce', role='Product Designer', when='2017 &mdash; 2022', dur='5 yrs',
      back_k='What I did there', back=('Enterprise tools and the design system behind them. I redesigned Salesforce Help so people could find '
                                        'answers on their own, reworked Manage Users to cut support cases, and built a back-to-work app for 75K employees.'),
      tilt=-2, drop=100, dl=-3.4),
 dict(kicker='Internship', bg='#e6f4ff', img=HAND[12], alt='Drawing of Tin shaking hands', logo=SF,
      name='Salesforce', role='UX/UI Intern', when='2017', dur='Summer',
      back_k='Where it started', back=('My first product design role: onboarding improvements, and the branding for a Salesforce hackathon.'),
      tilt=3, drop=60, dl=-1.2),
 dict(kicker='Industrial design', bg='#dff3e4', img=PARTY[0], alt='Drawing of Tin reaching into his jacket', logo=LX,
      name='Luxium Lighting', role='Industrial Designer', when='2017', dur='Project',
      back_k='What I made', back=('An LED light fixture, taken from concept to a working prototype: sketches, CAD, rendering and hardware prototyping.'),
      tilt=-3, drop=130, dl=-2.7),
 dict(kicker='Education', bg='#e9f1cf', img=WAVES[6], alt='Drawing of Tin waving', logo=UO,
      name='University of Oregon', role='BS Industrial Design', when='Business minor', dur='Alumni',
      back_k='What I learned', back=('How to design physical products: sketching, CAD, rendering and building prototypes by hand. '
                                      'I still work that way, just with pixels.'), tilt=2, drop=90, dl=-4.0),
]
for i, c in enumerate(CARDS): c['k'] = i + 1; c['num'] = '#%02d' % (i + 1); c['row_k'] = i % 3 + 1
def card(c):
    k = c['k']
    return f'''
      <div class="bd-hang" style="--t: {c['tilt']}deg; --drop: {c['drop']}px; --dl: {c['dl']}s; --pin: {{{{bdPin{c['row_k']}}}}}">
        <span class="bd-pin" aria-hidden="true"></span><span class="bd-thread" aria-hidden="true"></span>
        <div class="bd-swing">
          <span class="bd-clip" aria-hidden="true"></span>
          <div class="bd-card {{{{bdFlip{k}Class}}}}" role="button" tabindex="0" aria-pressed="{{{{bdFlip{k}On}}}}" aria-label="{c['name']} badge, flip for details" onClick="{{{{bdFlip{k}}}}}" onKeyDown="{{{{bdKey{k}}}}}">
            <div class="bd-face bd-front">
              <div class="bd-top"><span>{c['kicker']}</span><span>{c['num']}</span></div>
              <div class="bd-photo" style="background-color: {c['bg']}"><img src="{c['img']}" alt="{c['alt']}"><span class="bd-logo">{c['logo']}</span></div>
              <p class="bd-name">{c['name']}</p>
              <p class="bd-role">{c['role']}</p>
              <div class="bd-foot"><span>{c['when']} &middot; {c['dur']}</span><span class="bd-arrow">{ARROW}</span></div>
            </div>
            <div class="bd-face bd-back">
              <div class="bd-top"><span>{c['kicker']}</span><span>{c['num']}</span></div>
              <p class="bd-bk">{c['back_k']}</p>
              <p class="bd-desc">{c['back']}</p>
              <div class="bd-foot"><span>Flip back</span><span class="bd-arrow bd-arrow-back">{ARROW}</span></div>
            </div>
          </div>
        </div>
      </div>'''
WIRE = '    <svg class="bd-wire" viewBox="0 0 1000 {{bdWireH}}" preserveAspectRatio="none" aria-hidden="true" style="height: {{bdWireHpx}}"><path d="{{bdWirePath}}" fill="none" vector-effect="non-scaling-stroke"></path></svg>\n'
rows = [CARDS[i:i + 3] for i in range(0, len(CARDS), 3)]
SECTION = ('  <section class="bd-wrap {{bdSwayClass}}" aria-label="Experience" style="--bw: {{bdWidth}}; --br: {{bdRadius}}; --bc: {{bdColor}}; --pr: {{bdPhotoRadius}}; --tk: {{bdTilt}}; --flip: {{bdFlipMs}}; --wire: {{bdWire}}; --rowgap: {{bdRowGap}}">\n'
  + ''.join('   <div class="bd-line">\n' + WIRE + '    <div class="bd-row">' + ''.join(card(c) for c in row) + '\n    </div>\n   </div>\n' for row in rows)
  + '  </section>\n\n')
i = s.index('  <footer'); s = s[:i] + SECTION + s[i:]

CSS = r'''
/* ===== experience badges on a string ===== */
.bd-wrap{position:relative;padding:40px 150px 140px;display:flex;flex-direction:column;gap:var(--rowgap,56px)}
.bd-line{position:relative}
.bd-wire{position:absolute;left:0;right:0;top:0;width:100%;overflow:visible}
.bd-wire path{stroke:var(--wire,#9d9d9d);stroke-width:1.5}
.bd-row{position:relative;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));align-items:start}
.bd-hang{position:relative;display:flex;flex-direction:column;align-items:center;padding-top:calc(var(--pin) + var(--drop))}
.bd-pin{position:absolute;left:50%;top:var(--pin);width:11px;height:11px;margin:-5.5px 0 0 -5.5px;border-radius:50%;background:#c7c7cc;box-shadow:inset 0 0 0 2px #b4b4ba}
.bd-thread{position:absolute;left:50%;top:var(--pin);width:1.5px;margin-left:-.75px;height:calc(var(--drop) + 6px);background:var(--wire,#9d9d9d)}
.bd-swing{position:relative;transform-origin:50% 0;transform:rotate(calc(var(--t) * var(--tk,1)));perspective:1400px}
.bd-sway .bd-swing{animation:bdIdle 5.5s ease-in-out var(--dl) infinite alternate}
.bd-sway .bd-hang:hover .bd-swing{animation:bdSwing 1.5s cubic-bezier(.25,.6,.35,1) both}
@keyframes bdIdle{from{transform:rotate(calc(var(--t) * var(--tk,1)))}to{transform:rotate(calc(var(--t) * var(--tk,1) + 1.6deg))}}
@keyframes bdSwing{0%{transform:rotate(calc(var(--t) * var(--tk,1)))}18%{transform:rotate(calc(var(--t) * var(--tk,1) + 7deg))}40%{transform:rotate(calc(var(--t) * var(--tk,1) - 4.5deg))}60%{transform:rotate(calc(var(--t) * var(--tk,1) + 2.4deg))}80%{transform:rotate(calc(var(--t) * var(--tk,1) - 1deg))}100%{transform:rotate(calc(var(--t) * var(--tk,1)))}}
.bd-clip{position:absolute;left:50%;top:-14px;z-index:2;width:30px;height:22px;margin-left:-15px;border-radius:15px 15px 4px 4px;background:linear-gradient(#d9d9de,#bdbdc3);box-shadow:0 1px 0 rgba(255,255,255,.8) inset,0 2px 4px rgba(0,0,0,.12)}
.bd-clip::after{content:"";position:absolute;left:50%;top:5px;width:8px;height:8px;margin-left:-6px;border-radius:50%;border:2px solid #8e8e95;background:#f2f2f5}
.bd-card{position:relative;width:var(--bw,300px);cursor:pointer;transform-style:preserve-3d;transition:transform var(--flip,700ms) cubic-bezier(.3,1.25,.45,1);outline:none}
.bd-card.is-flipped{transform:rotateY(180deg)}
.bd-card:focus-visible .bd-face{box-shadow:0 0 0 3px #3078e7,0 24px 48px -26px rgba(0,0,0,.45)}
.bd-face{box-sizing:border-box;border-radius:var(--br,22px);background:var(--bc,#f2f2f2);padding:18px 18px 16px;-webkit-backface-visibility:hidden;backface-visibility:hidden;box-shadow:0 1px 0 rgba(255,255,255,.9) inset,0 24px 48px -26px rgba(0,0,0,.4),0 2px 6px rgba(0,0,0,.06);color:#141414;font-family:'Be Vietnam Pro',system-ui,sans-serif}
.bd-back{position:absolute;inset:0;transform:rotateY(180deg);display:flex;flex-direction:column}
.bd-top{display:flex;justify-content:space-between;align-items:center;margin:2px 4px 12px;font-size:11px;font-weight:500;letter-spacing:.12em;text-transform:uppercase;color:#6e6e6e}
.bd-photo{position:relative;aspect-ratio:1 / 1;border-radius:var(--pr,14px);overflow:hidden;display:grid;place-items:end center}
.bd-photo img{display:block;width:84%;height:84%;object-fit:contain;object-position:50% 100%}
.bd-logo{position:absolute;left:12px;top:12px;width:34px;height:34px;border-radius:10px;background:#fff;display:grid;place-items:center;box-shadow:0 2px 8px rgba(0,0,0,.08)}
.bd-name{margin:18px 4px 0;font-size:30px;line-height:1.1;font-weight:500;letter-spacing:-.02em}
.bd-role{margin:6px 4px 0;font-size:17px;color:#6e6e6e}
.bd-foot{display:flex;justify-content:space-between;align-items:center;margin:22px 4px 0;padding-top:14px;border-top:1px solid rgba(20,20,20,.12);font-size:12px;font-weight:500;letter-spacing:.12em;text-transform:uppercase}
.bd-back .bd-foot{margin-top:auto}
.bd-arrow{flex:none;width:34px;height:34px;border-radius:50%;background:#141414;color:#fff;display:grid;place-items:center;transition:transform .3s cubic-bezier(.3,1.5,.5,1)}
.bd-card:hover .bd-arrow{transform:rotate(45deg)}
.bd-arrow-back{transform:rotate(-135deg)}
.bd-card:hover .bd-arrow-back{transform:rotate(-180deg)}
.bd-bk{margin:6px 4px 0;font-size:13px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:#6e6e6e}
.bd-desc{margin:12px 4px 0;font-size:20px;line-height:1.45;letter-spacing:-.005em}
.party .bd-wire path,.party .bd-thread{stroke:rgba(255,255,255,.35);background:rgba(255,255,255,.35)}
.party .bd-wire path{stroke:rgba(255,255,255,.35)}
@media (prefers-reduced-motion: reduce){.bd-swing{animation:none !important}.bd-card{transition-duration:.01ms}}
'''
rep('</style>\n</helmet>', CSS + '</style>\n</helmet>')

# state + handlers
m = re.search(r"this\.state = \{ i: 0,", s); assert m
s = s[:m.end()] + " bdFlip: {}," + s[m.end():]
key = lambda k: f"(e) => {{ if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); this.bdToggle({k}); }} }}"
vals = ("      bdWidth: this.tp('badgeWidth', 300) + 'px', bdRadius: this.tp('badgeRadius', 22) + 'px', bdColor: this.tp('badgeColor', '#f2f2f2'), bdPhotoRadius: this.tp('photoRadius', 14) + 'px',\n"
        "      bdTilt: String(this.tp('badgeTilt', 1)), bdFlipMs: this.tp('flipMs', 700) + 'ms', bdWire: this.tp('stringColor', '#9d9d9d'), bdRowGap: this.tp('rowGap', 56) + 'px', bdSwayClass: this.tp('badgeSway', true) === false ? '' : 'bd-sway',\n"
        "      ...this.bdWireVals(),\n" +
        "".join(f"      bdFlip{k}: () => this.bdToggle({k}), bdKey{k}: {key(k)}, bdFlip{k}Class: this.state.bdFlip && this.state.bdFlip[{k}] ? 'is-flipped' : '', bdFlip{k}On: this.state.bdFlip && this.state.bdFlip[{k}] ? 'true' : 'false',\n" for k in range(1, 7)))
rep("      trRef: (el) => { this.trCv = el; },", vals + "      trRef: (el) => { this.trCv = el; },")
rep("  goHome() {", """  bdToggle(k) { this.setState((s) => ({ bdFlip: { ...(s.bdFlip || {}), [k]: !(s.bdFlip && s.bdFlip[k]) } })); }
  bdWireVals() { // a sagging string: pins sit on the curve above each badge's centre
    const sag = this.tp('stringSag', 28), H = Math.round(sag + 24), y = (t) => 8 + 4 * sag * t * (1 - t);
    const out = { bdWireH: String(H), bdWireHpx: H + 'px', bdWirePath: `M0,8 Q500,${8 + 2 * sag} 1000,8` };
    [1, 2, 3].forEach((k) => { out['bdPin' + k] = Math.round(y((k - 0.5) / 3)) + 'px'; });
    return out;
  }
  goHome() {""")

mm = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(mm.group(2)))
add = {
 'badgesSection': None,
 'badgeWidth': {"editor": "range", "default": 300, "min": 220, "max": 380, "step": 2, "unit": "px", "section": "Badges"},
 'badgeRadius': {"editor": "range", "default": 22, "min": 0, "max": 44, "step": 1, "unit": "px", "section": "Badges"},
 'badgeColor': {"editor": "color", "default": "#f2f2f2", "section": "Badges"},
 'photoRadius': {"editor": "range", "default": 14, "min": 0, "max": 40, "step": 1, "unit": "px", "section": "Badges"},
 'badgeTilt': {"editor": "range", "default": 1, "min": 0, "max": 2.5, "step": 0.05, "unit": "×", "section": "Badges"},
 'badgeSway': {"editor": "boolean", "default": True, "section": "Badges"},
 'rowGap': {"editor": "range", "default": 56, "min": 0, "max": 200, "step": 2, "unit": "px", "section": "Badges"},
 'stringSag': {"editor": "range", "default": 28, "min": 0, "max": 90, "step": 1, "unit": "px", "section": "Badges"},
 'stringColor': {"editor": "color", "default": "#9d9d9d", "section": "Badges"},
 'flipMs': {"editor": "range", "default": 700, "min": 200, "max": 1600, "step": 50, "unit": "ms", "section": "Badges"},
}
add.pop('badgesSection')
for k in add: assert k not in P, k
new = {}
for k, v in P.items():
    if k == 'introLoader': new.update(add)
    new[k] = v
attr = json.dumps(new, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:mm.start()] + "data-props='" + attr + "'>" + s[mm.end():]
open(p, 'w').write(s)
mm = re.search(r"data-props=(['\"])(.*?)\1>\n(.*?)</script>", s, re.S)
json.loads(html.unescape(mm.group(2)))
open('/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/bd_logic.js', 'w').write('class DCLogic{}\n' + mm.group(3))
print('ok')
