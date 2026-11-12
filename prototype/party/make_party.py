"""Party mode board: copy of Tablet C + a small celebration button in the header corner.
Click it: confetti, the page goes dark, the waving drawing puts on sunglasses and dances,
and the page turns into Tin's creative side (after-hours intro + a wall of photos and drawings).
usage: party.py <tablet-c.dc.html> <out.dc.html>
"""
import sys, re, json, html, random
S = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/'
s = open(sys.argv[1]).read()
IDS = json.load(open(S + 'party_ids.json'))
lo = lambda i: open(S + f'vid/p24/lo{i}.b64').read().strip()

ent = lambda x: ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in x)  # swapped (sc-if) parts: plain ASCII + entities
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:110], s.count(old))
    s = s.replace(old, new)

DESKTOP = 'class="th-prose"' not in s
OLD_T = 'Homepage · Tablet option C · greeting band + prose intro (kenjilambert-style)'
NEW_T = 'Homepage · Party mode · tap the corner button (from Tablet C)'
if not DESKTOP: rep(OLD_T, NEW_T, 2)

PH = {  # photos from the About collage
 'sketch': ('17db6e2bb7b0e2021c26e1ecc3bda47f', 'Product sketches in a sketchbook'),
 'matcha': ('c64573ac38f1a52f639acbd6f13d6637', 'Matcha bowl and whisk'),
 'poppy':  ('b5356d519834afcefbc6a6d64e6511d6', 'Orange poppy against blue sky'),
 'pup':    ('493d7640386543da1bdedbc47e54eb3c', 'Puppy in a party hat'),
 'leaves': ('da160242c64c297a138460aca71fda7e', 'Plant leaves in sunlight'),
 'lantern':('81ebdd55c5cfbf822db09d0ea5979994', 'Silk lanterns on a yellow wall'),
 'paint':  ('9d447d5db4b8c8dd6afc9b5b38a4e43a', 'Red and green paint strokes'),
 'teacup': ('c987b1a2bfa77858ecd7e812aefcfdd5', 'Teacup in window light'),
}

# ---------- CSS ----------
CSS = r'''
/* ===== party mode ===== */
.th-root{transition:background-color .9s ease,color .9s ease}
.th-root.party{background-color:#0d0c12 !important;color:#f4f1ea !important}
.party .th-fade::before{background:linear-gradient(to bottom,rgba(13,12,18,.94) 0%,rgba(13,12,18,.8) 45%,rgba(13,12,18,0) 100%)}
.party .th-loop img{filter:invert(1)}
.party [style*="color: #141414"]{color:#f4f1ea !important}
.party [style*="color: #6e6e6e"]{color:#aaa4b8 !important}
.party footer{color:#aaa4b8 !important}
.party .ab-board{background-color:#17151f !important}
.party #top p[style*="Caveat"]{text-shadow:0 0 28px rgba(255,79,216,.55),0 0 2px rgba(255,255,255,.6)}
.party .th-prose .th-co{background-color:rgba(255,255,255,.08)}
.party .th-prose .th-co:hover,.party .th-prose .th-co:focus-within{background-color:rgba(255,255,255,.16)}
.party .th-prose .th-co p{color:#e9e4f2 !important}
.party .th-cta .th-btn-primary{background-color:#f4f1ea !important;border-color:#f4f1ea !important;color:#0d0c12 !important;box-shadow:0 0 28px rgba(255,79,216,.35)}
.party .th-cta .th-btn-secondary{background-color:transparent !important;border-color:rgba(255,255,255,.35) !important;color:#f4f1ea !important}
/* the corner button */
.th-party-btn{position:absolute;right:28px;top:50%;transform:translateY(-50%);width:44px;height:44px;border-radius:50%;border:1.5px solid rgba(20,20,20,.16);background:#fff;color:#141414;display:grid;place-items:center;padding:0;cursor:pointer;z-index:3;transition:transform .25s cubic-bezier(.3,1.6,.5,1),background-color .5s,border-color .5s,color .5s,box-shadow .5s}
.th-party-btn:hover{transform:translateY(-50%) scale(1.1) rotate(-8deg)}
.th-party-btn:active{transform:translateY(-50%) scale(.92)}
.th-party-btn:focus-visible{outline:2px solid #3078e7;outline-offset:3px}
.th-party-btn svg{display:block;transition:transform .5s cubic-bezier(.3,1.6,.5,1)}
.party .th-party-btn{background:#1b1826;border-color:rgba(255,255,255,.22);color:#fff;box-shadow:0 0 0 4px rgba(255,79,216,.18),0 0 26px rgba(255,79,216,.45)}
.party .th-party-btn svg{transform:rotate(-24deg) scale(1.05)}
.th-party-btn .pb-ring{position:absolute;inset:-5px;border-radius:50%;border:1.5px dashed rgba(255,255,255,.55);opacity:0;transition:opacity .5s}
.party .th-party-btn .pb-ring{opacity:1;animation:pbSpin 6s linear infinite}
@keyframes pbSpin{to{transform:rotate(360deg)}}
.th-party-btn .pb-tip{position:absolute;right:54px;top:50%;transform:translate(6px,-50%);white-space:nowrap;font:500 13px/1 'Be Vietnam Pro',system-ui,sans-serif;color:#6e6e6e;opacity:0;pointer-events:none;transition:opacity .2s,transform .2s}
.th-party-btn:hover .pb-tip,.th-party-btn:focus-visible .pb-tip{opacity:1;transform:translate(0,-50%)}
.party .th-party-btn .pb-tip{color:#aaa4b8}
/* confetti */
.th-cf{position:absolute;left:50%;top:50%;width:var(--w);height:var(--h);margin:calc(var(--h) / -2) 0 0 calc(var(--w) / -2);border-radius:var(--br);background:var(--c);pointer-events:none;opacity:0;animation:cfFly var(--d) cubic-bezier(.15,.7,.3,1) var(--dl) both}
@keyframes cfFly{0%{opacity:1;transform:translate(0,0) rotate(0) scale(.4)}12%{opacity:1;transform:translate(calc(var(--dx) * .35),calc(var(--dy) * .12 - 70px)) rotate(calc(var(--r) * .3)) scale(1)}80%{opacity:1}100%{opacity:0;transform:translate(var(--dx),var(--dy)) rotate(var(--r)) scale(.9)}}
/* neon light in the hero */
.th-pglow{position:absolute;top:0;left:0;right:0;height:1100px;z-index:-1;pointer-events:none;opacity:0;transition:opacity 1.4s ease;overflow:hidden}
.party .th-pglow{opacity:1}
.th-pglow i{position:absolute;border-radius:50%;filter:blur(90px);animation:pgDrift 10s ease-in-out infinite alternate}
.th-pglow i:nth-child(1){width:520px;height:520px;background:#ff4fd8;opacity:.42;left:-160px;top:-180px}
.th-pglow i:nth-child(2){width:560px;height:560px;background:#4d5bff;opacity:.5;right:-200px;top:-80px;animation-duration:12s;animation-delay:-4s}
.th-pglow i:nth-child(3){width:420px;height:420px;background:#00e0c6;opacity:.26;left:28%;top:420px;animation-duration:14s;animation-delay:-7s}
.th-pglow b{position:absolute;inset:0;background-image:radial-gradient(1.5px 1.5px at 12% 18%,#fff 50%,transparent 51%),radial-gradient(1px 1px at 32% 8%,#fff 50%,transparent 51%),radial-gradient(1.5px 1.5px at 61% 22%,#fff 50%,transparent 51%),radial-gradient(1px 1px at 84% 12%,#fff 50%,transparent 51%),radial-gradient(1px 1px at 72% 40%,#fff 50%,transparent 51%),radial-gradient(1.5px 1.5px at 22% 46%,#fff 50%,transparent 51%),radial-gradient(1px 1px at 92% 52%,#fff 50%,transparent 51%),radial-gradient(1px 1px at 45% 36%,#fff 50%,transparent 51%);opacity:.5;animation:pgTwinkle 3.2s ease-in-out infinite alternate}
@keyframes pgDrift{to{transform:translate3d(90px,70px,0) scale(1.18)}}
@keyframes pgTwinkle{to{opacity:.15}}
/* after-hours intro pills: photo thumbnails instead of logos */
.th-pp{cursor:default}
.th-pp .lg{border-radius:50%;object-fit:cover}
.th-pp:hover .lg{transform:rotate(-8deg) scale(1.15)}
.th-pp .lg{transition:transform .3s cubic-bezier(.3,1.6,.5,1)}
/* the wall: Tin's creative side */
.th-wall{padding:40px 48px 96px}
.th-wall-k{margin:0 0 6px;font:600 13px/1 'Be Vietnam Pro',system-ui,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#ff7ae0}
.th-wall h2{margin:0 0 36px;font:400 54px/1.05 Caveat,sans-serif;color:#f4f1ea}
.th-wall-grid{columns:3;column-gap:22px}
.th-wall figure{break-inside:avoid;margin:0 0 26px;display:block;transform:rotate(var(--t));transition:transform .35s cubic-bezier(.3,1.5,.5,1)}
.th-wall figure:hover{transform:rotate(0) translateY(-6px) scale(1.03)}
.th-wall .wl-ph{display:block;width:100%;border-radius:10px;background:#1b1826;box-shadow:0 18px 40px -18px rgba(0,0,0,.8),0 0 0 6px #f4f1ea}
.th-wall .wl-dr{display:block;width:100%;padding:18px;box-sizing:border-box;filter:invert(1)}
.th-wall .wl-drbox{border-radius:10px;background:#1b1826;overflow:hidden;box-shadow:inset 0 0 0 1px rgba(255,255,255,.14),0 18px 40px -18px rgba(0,0,0,.8)}
.th-wall figcaption{margin-top:12px;font:400 24px/1 Caveat,sans-serif;color:#d8d2e6}
.th-wall figure:nth-child(3n+1) figcaption{color:#ff9be8}
.th-wall figure:nth-child(3n+2) figcaption{color:#8fe9ff}
@media (prefers-reduced-motion: reduce){.th-cf,.th-pglow i,.th-pglow b,.party .th-party-btn .pb-ring{animation:none !important}.th-cf{display:none}}
'''
if DESKTOP: CSS += r'''
/* desktop: after-hours paragraph pills + a four-column wall */
.th-prose .th-co{display:inline-flex !important;width:auto;align-items:center;gap:8px !important;padding:4px 14px 4px 6px;background-color:rgba(20,20,20,.06);border-radius:200px;margin:0 5px;vertical-align:-7px}
.th-prose .th-co p{line-height:1.3 !important;font-size:19px !important}
.th-prose .lg,.th-prose .lg-frame{width:26px !important;height:26px !important}
.th-prose button,.th-prose a[href]{font-family:inherit}
.th-wall{padding:40px 150px 140px}
.th-wall-grid{columns:4;column-gap:28px}
.th-wall h2{font-size:64px}
'''
rep('</style>\n</helmet>', CSS + '</style>\n</helmet>')

# ---------- markup ----------
rep('<div class="{{introClass}} {{gradClass}}" style="position: relative; isolation: isolate;',
    '<div class="th-root {{introClass}} {{gradClass}} {{partyClass}}" style="position: relative; isolation: isolate;')
rep('<div class="th-grad" aria-hidden="true"><i class="g-ms"></i><i class="g-sf"></i><i class="g-uo"></i></div>',
    '<div class="th-grad" aria-hidden="true"><i class="g-ms"></i><i class="g-sf"></i><i class="g-uo"></i></div>\n<div class="th-pglow" aria-hidden="true"><i></i><i></i><i></i><b></b></div>')

POPPER = ('<svg viewBox="0 0 24 24" width="22" height="22" fill="none" aria-hidden="true">'
  '<path d="M3.6 20.4 8.7 8.8l6.5 6.5z" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"></path>'
  '<path d="M6.1 14.9l3 3M7.6 11.5l4.9 4.9" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"></path>'
  '<path d="M12.2 3.6c1 1.3.8 2.7-.5 3.8" stroke="#e5839a" stroke-width="1.6" stroke-linecap="round"></path>'
  '<path d="M15.6 8.4l3.3-3.3" stroke="#d64d45" stroke-width="1.6" stroke-linecap="round"></path>'
  '<path d="M16.6 12.6c1.3-.8 2.7-.7 3.9.3" stroke="#7fba00" stroke-width="1.6" stroke-linecap="round"></path>'
  '<circle cx="18.6" cy="2.9" r="1.2" fill="#5f73c4"></circle><circle cx="21" cy="8.4" r="1.1" fill="#ffb900"></circle><circle cx="14.6" cy="2.4" r=".9" fill="#00a4ef"></circle>'
  '</svg>')
BTN = ('\n    <button type="button" class="th-party-btn" aria-pressed="{{partyPressed}}" aria-label="{{partyLabel}}" onClick="{{partyToggle}}">'
       '<span class="pb-ring" aria-hidden="true"></span>' + POPPER +
       '<span class="pb-tip" aria-hidden="true">{{partyTip}}</span>'
       '<sc-for list="{{confetti}}" as="c" hint-placeholder-count="0"><i class="th-cf" style="{{c.style}}"></i></sc-for></button>\n  </header>')
rep('    </button>\n    \n  </header>', '    </button>' + BTN)

# after-hours intro: same tweaks as the day intro, photo pills
if DESKTOP:
    g = s.index("Hi, I'm Tin</p></div>") + len("Hi, I'm Tin</p></div>")
    i = g; j = s.index('<div class="th-trail"', g)
    while s[j - 1] in ' \n': j -= 1
    day = s[i:j]
    open_tag = '<div class="th-prose" style="max-width: 660px; font-size: 22px; line-height: 2.1; color: #141414; font-weight: 400">'
else:
    i = s.index('<div class="th-prose"'); j = s.index('</div>', i) + len('</div>')
    day = s[i:j]
    open_tag = day[:day.index('>') + 1]
m = re.search(r'<a class="th-co" href="https://microsoft\.ai"[^>]*style="([^"]*)"', day); chip_style = m.group(1)
if DESKTOP: chip_style = chip_style.replace('display: flex;', 'display: inline-flex;')
m = re.search(r'<span class="lg-frame" style="([^"]*)"', day); frame_style = m.group(1)
m = re.search(r'<a class="th-co"[^>]*>.*?<p style="([^"]*)">', day, re.S); label_style = m.group(1)
def pill(key, label, hk):
    bid, alt = PH[key]
    return (f'<span class="th-co th-pp" tabindex="0" onPointerEnter="{{{{{hk}}}}}" onPointerLeave="{{{{ppLeave}}}}" onFocus="{{{{{hk}}}}}" onBlur="{{{{ppLeave}}}}" style="{chip_style}">'
            f'<span class="lg-frame" style="{frame_style}"><img class="lg" src="/_blob/{bid}" alt="{alt}" style="width: 24px; height: 24px; display: block"></span>'
            f'<p style="{label_style}">{label}</p></span>')
em = re.search(r'<button type="button" onClick="\{\{copy\}\}".*?</button>', day, re.S)
li = re.search(r'<a href="https://www\.linkedin\.com/in/letin08/".*?</a>', day, re.S)
tail = ('<span>. Grew up in &#272;&#224; L&#7841;t, made in Oregon. Come hang out:</span> ' + em.group(0) + ' <span><span style="color: #9a948a">or</span> ' + li.group(0) + '.</span></div>') if em and li else '<span>. Grew up in &#272;&#224; L&#7841;t, made in Oregon.</span></div>'
night = (open_tag +
  '<span>After hours I keep making things: sketching in</span> ' + pill('sketch', 'my sketchbook', 'ppSketch') +
  '<span>, whisking</span> ' + pill('matcha', 'matcha', 'ppMatcha') +
  '<span>, chasing light with</span> ' + pill('poppy', 'my camera', 'ppPoppy') +
  ' <span>and throwing very small parties for</span> ' + pill('pup', 'this guy', 'ppPup') +
  tail)
if DESKTOP: day = '<div style="display: contents">' + day + '</div>'
s = s[:i] + '<sc-if value="{{partyOff}}" hint-placeholder-val="{{ true }}">' + ent(day) + '</sc-if><sc-if value="{{partyOn}}" hint-placeholder-val="{{ false }}">' + ent(night) + '</sc-if>' + s[j:]

# work list ↔ the wall
a = s.index('  <main aria-label="Work"'); b = s.index('</main>', a) + len('</main>')
work = s[a:b]
def ph(key, cap, t):
    bid, alt = PH[key]
    return f'<figure style="--t: {t}deg"><img class="wl-ph" src="/_blob/{bid}" alt="{alt}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
def dr(src, alt, cap, t):
    return f'<figure style="--t: {t}deg"><div class="wl-drbox"><img class="wl-dr" src="{src}" alt="{alt}" loading="lazy"></div><figcaption>{cap}</figcaption></figure>'
WAVE0 = re.search(r"const TR_WAVE = \['(/_blob/[0-9a-f]{32})'", s).group(1)
MAIL = re.findall(r"/_blob/[0-9a-f]{32}", re.search(r"const TR_MAIL = \[[^\]]*\]", s).group(0))
HAND = re.findall(r"/_blob/[0-9a-f]{32}", re.search(r"const TR_HAND = \[[^\]]*\]", s).group(0))
items = [
  dr('/_blob/' + IDS[14], 'Line drawing of Tin in sunglasses, fist up', 'party mode (this page)', -2),
  ph('sketch', 'sketchbook, always open', 1.5),
  ph('matcha', 'morning matcha', -1),
  ph('pup', 'party guest', 2),
  dr(WAVE0, 'Line drawing of Tin waving', 'self-portrait, waving', -1.5),
  ph('poppy', 'poppy season', 1),
  ph('lantern', 'lanterns', -2),
  dr(MAIL[12], 'Line drawing of Tin posting a letter', 'posting a letter', 1.5),
  ph('paint', 'paint, no plan', -1),
  ph('leaves', 'window plants', 2),
  dr(HAND[12], 'Line drawing of two people shaking hands', 'nice to meet you', -1.5),
  ph('teacup', 'tea in window light', 1),
]
WALL = ('  <section class="th-wall" aria-label="After hours">\n    <p class="th-wall-k">After hours</p>\n    <h2>Things I make when nobody asks</h2>\n'
        '    <div class="th-wall-grid">' + ''.join(items) + '</div>\n  </section>')
s = s[:a] + '<sc-if value="{{partyOff}}" hint-placeholder-val="{{ true }}">\n' + ent(work) + '\n  </sc-if><sc-if value="{{partyOn}}" hint-placeholder-val="{{ false }}">\n' + ent(WALL) + '\n  </sc-if>' + s[b:]

rep('<span>© 2026 Tin Le · Grew up in Đà Lạt, made in Oregon</span>',
    '<span>© 2026 Tin Le · Grew up in Đà Lạt, made in Oregon<sc-if value="{{partyOn}}" hint-placeholder-val="{{ false }}"> · after-hours edition</sc-if></span>')

# ---------- logic ----------
m = re.search(r"const TR_SPRITES = \{ wave:", s)
s = s[:m.start()] + "const TR_PARTY = [" + ", ".join(f"'/_blob/{i}'" for i in IDS) + "]; // you, putting on sunglasses and dancing (Seedance clip)\n" + s[m.start():]
rep("hs: { key: 'h', n: 24, imgs: TR_HAND } };",
    "hs: { key: 'h', n: 24, imgs: TR_HAND }, party: { key: 'p', n: 24, imgs: TR_PARTY, seq: [...Array(24).keys(), 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10], loop0: 9, reach: 5 } };")
rep("R2 = (tcell * 16) ** 2;", "R2 = (tcell * (spr.reach || 16)) ** 2; // big moves (the dance) match within a smaller reach so building it stays fast")
rep("for (const k of ['m', 'h']) for (let i = 0; i < 24; i++) TR_DRAW[k + i] = 1;",
    "for (const k of ['m', 'h', 'p']) for (let i = 0; i < 24; i++) TR_DRAW[k + i] = 1;\n"
    "Object.assign(TR_IMAGES, {" + ", ".join(f"p{i}: 'data:image/png;base64,{lo(i)}'" for i in range(24)) + "});\n"
    "Object.assign(TR_IMAGES, {" + ", ".join(f"ph_{k}: '/_blob/{v[0]}'" for k, v in PH.items()) + "}); // after-hours photos: hover a pill and the dots rebuild the photo")
rep("const home = name === 'wave', spr = TR_SPRITES[name],", "const home = name === 'wave' || name === 'party', spr = TR_SPRITES[name],")
rep("anim = { set: name, scrub: spr.scrub, paths, seq: Array.from({ length: spr.n }, (_, k) => k),",
    "anim = { set: name, scrub: spr.scrub, loop0: spr.loop0, paths, seq: spr.seq || Array.from({ length: spr.n }, (_, k) => k),")
rep("idx = (k) => A.seq[(((s0 + k) % L) + L) % L];",
    "idx = (k) => { const t = s0 + k; if (A.loop0 != null && t >= A.loop0) return A.seq[A.loop0 + ((t - A.loop0) % (L - A.loop0))]; return A.seq[((t % L) + L) % L]; };")
rep("r.homeTry = now; this.trailForm('wave'); }", "r.homeTry = now; this.trailForm(this.state.party ? 'party' : 'wave'); }")
rep("const m = this.trailSample(name, Math.max(8, TR_DRAW[name] ? this.tp('drawDetail', 64) : this.tp('detail', 26)));",
    "const photo = name.startsWith('ph_'), m = this.trailSample(name, Math.max(8, TR_DRAW[name] ? this.tp('drawDetail', 64) : photo ? this.tp('photoDetail', 46) : this.tp('detail', 26)));")
rep("s: tcell * this.tp('logoFill', 0.86),", "s: tcell * (name.startsWith('ph_') ? 1.04 : this.tp('logoFill', 0.86)),")
# white ink at night
n_ink = s.count("this.tp('drawInk', '#141414')"); assert n_ink >= 3, n_ink
s = s.replace("this.tp('drawInk', '#141414')", "this.trInk()")
rep("  trailPal() {\n", "  trInk() { return this.state.party ? this.tp('partyInk', '#f4f1ea') : this.tp('drawInk', '#141414'); }\n  trailPal() {\n"
    "    if (this.state.party) return [this.tp('partyColor1', '#ff4fd8'), this.tp('partyColor2', '#7cf9ff'), this.tp('partyColor3', '#fff05a'), this.tp('partyColor4', '#8bff6a')];\n")
rep("this.state = { i: 0, copied: false, paused: false };", "this.state = { i: 0, copied: false, paused: false, party: props.partyStart === true, confetti: [] };")
rep("  componentWillUnmount() { clearInterval(this.timer);", "  componentWillUnmount() { clearTimeout(this.tCf); clearInterval(this.timer);")
rep("  goHome() {", r"""  partySet(on) {
    const pal = ['#ff4fd8', '#7cf9ff', '#fff05a', '#8bff6a', '#ff7a3d', '#f25022', '#00a4ef', '#ffb900', '#ffffff'];
    const R = (a, b) => a + Math.random() * (b - a);
    const confetti = !on ? [] : Array.from({ length: Math.round(this.tp('confettiCount', 90)) }, (_, k) => {
      const w = R(6, 12), round = Math.random() < 0.3, a = R(Math.PI * 0.5, Math.PI * 1.05), d = R(180, 760);
      return { k, style: `--dx: ${Math.round(Math.cos(a) * d)}px; --dy: ${Math.round(Math.sin(a) * d * 1.1 + R(40, 260))}px; --r: ${Math.round(R(-720, 720))}deg; --w: ${w.toFixed(1)}px; --h: ${(round ? w : w * R(0.35, 0.6)).toFixed(1)}px; --br: ${round ? '50%' : '2px'}; --c: ${pal[k % pal.length]}; --d: ${R(1.3, 2.2).toFixed(2)}s; --dl: ${R(0, 0.12).toFixed(2)}s` };
    });
    this.setState({ party: on, confetti, grad: null }); clearTimeout(this.tCf);
    if (on) this.tCf = setTimeout(() => this.setState({ confetti: [] }), 2600);
    const r = this.tr; if (r) { if (r.form) this.trailUnform(); r.ps = []; r.homeTry = performance.now() + 150; } // rebuild the figure once the confetti is already flying
  }
  goHome() {""")
rep("      trRef: (el) => { this.trCv = el; },",
    "      partyOn: !!this.state.party, partyOff: !this.state.party, partyClass: this.state.party ? 'party' : '', partyPressed: this.state.party ? 'true' : 'false',\n"
    "      partyLabel: this.state.party ? 'Leave party mode' : 'Party mode', partyTip: this.state.party ? 'back to work' : 'party mode', confetti: this.state.confetti || [],\n"
    "      partyToggle: () => this.partySet(!this.state.party),\n"
    "      ppSketch: () => this.trailForm('ph_sketch'), ppMatcha: () => this.trailForm('ph_matcha'), ppPoppy: () => this.trailForm('ph_poppy'), ppPup: () => this.trailForm('ph_pup'), ppLeave: () => this.trailRelease(),\n"
    "      trRef: (el) => { this.trCv = el; },")
rep("  componentDidUpdate(prev) {", "  componentDidUpdate(prev) { if (prev.partyStart !== this.props.partyStart) this.partySet(this.props.partyStart === true);")

# ---------- tweaks ----------
m = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(m.group(2)))
add = {
 'partyStart': {"editor": "boolean", "default": False, "section": "Party mode"},
 'photoDetail': {"editor": "range", "default": 46, "min": 16, "max": 80, "step": 2, "section": "Party mode"},
 'confettiCount': {"editor": "range", "default": 90, "min": 0, "max": 220, "step": 10, "section": "Party mode"},
 'partyInk': {"editor": "color", "default": "#f4f1ea", "section": "Party mode"},
 'partyColor1': {"editor": "color", "default": "#ff4fd8", "section": "Party mode"},
 'partyColor2': {"editor": "color", "default": "#7cf9ff", "section": "Party mode"},
 'partyColor3': {"editor": "color", "default": "#fff05a", "section": "Party mode"},
 'partyColor4': {"editor": "color", "default": "#8bff6a", "section": "Party mode"},
}
colors = [v for v in P.values() if isinstance(v, dict) and v.get('editor') in ('color',)]
if not colors:
    ce = next((v.get('editor') for k, v in P.items() if k.startswith('trailColor')), 'color')
    for k in add:
        if add[k]['editor'] == 'color': add[k]['editor'] = ce
new = {}
for k, v in P.items():
    if k == 'introLoader': new.update(add)
    new[k] = v
attr = json.dumps(new, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:m.start()] + "data-props='" + attr + "'>" + s[m.end():]
s = s.replace('<!-- ' + NEW_T + ' · layout option preview, copy of TinHome-2goy.dc.html -->', '<!-- ' + NEW_T + ' · copy of TinHome-Tablet-C.dc.html with a party mode -->')
open(sys.argv[2], 'w').write(s)
mm = re.search(r"data-props=(['\"])(.*?)\1>\n(.*?)</script>", s, re.S)
json.loads(html.unescape(mm.group(2)))
open(S + 'party_logic.js', 'w').write('class DCLogic{}\n' + mm.group(3))
print('ok')
