"""Carousel badges rebuilt from Tin's resume + work history: one badge per role (8). Titles, dates and bullets only.
usage: resume_badges.py <party-desktop.dc.html>  (edits in place; board must already be the carousel version)"""
import sys, re
p = sys.argv[1]; s = open(p).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:100], s.count(old)); s = s.replace(old, new)
blobs = lambda name: re.findall(r"/_blob/[0-9a-f]{32}", re.search(r"const %s = \[[^\]]*\]" % name, s).group(0))
WAVE, MAIL, HAND, PARTY = blobs('TR_WAVE'), blobs('TR_MAIL'), blobs('TR_HAND'), blobs('TR_PARTY')
MS = ('<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><rect x="0" y="0" width="9" height="9" fill="#f25022"></rect>'
      '<rect x="11" y="0" width="9" height="9" fill="#7fba00"></rect><rect x="0" y="11" width="9" height="9" fill="#00a4ef"></rect>'
      '<rect x="11" y="11" width="9" height="9" fill="#ffb900"></rect></svg>')
SF = '<img src="/_blob/ac43d25c19be4e522f4bd492e1c090ab" alt="" width="22" height="16" style="display: block; object-fit: contain">'
UO = '<img src="/_blob/00e0e1ec841a28c4e0055e4a6738e6b1" alt="" width="18" height="18" style="display: block; object-fit: contain">'
TXT = lambda t: f'<span style="font: 700 13px/1 Be Vietnam Pro, system-ui, sans-serif; color: #141414">{t}</span>'
ARROW = '<svg viewBox="0 0 24 24" width="16" height="16" fill="none" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'
CARDS = [
 dict(kicker='Experience &middot; Now', bg='#dfe4ff', img=WAVE[0], alt='Drawing of Tin waving', logo=MS,
      name='Microsoft AI', role='Senior Product Designer', when='2022 &mdash; now', dur='4 yrs', back_k='What I do there',
      back='Search across Bing, Edge and Windows. Today that means helping people find what they need, growing Bing, and exploring what AI agents could do in search.'),
 dict(kicker='Teaching &middot; Now', bg='#ffe68a', img=PARTY[14], alt='Drawing of Tin in sunglasses', logo=UO,
      name='University of Oregon', role='Product Design Instructor', when='2023 &mdash; now', dur='3 yrs', back_k='What I teach',
      back='UX and product design, at the same school where I studied industrial design. Students learn the way I still work: by building and prototyping.'),
 dict(kicker='Teaching', bg='#ffd9cf', img=PARTY[20], alt='Drawing of Tin with his fist up', logo=TXT('2U'),
      name='2U', role='UX/UI Bootcamp Instructor', when='Since 2021', dur='Remote', back_k='What I taught',
      back='Led cohorts through a 24-week bootcamp in UX research, UX and UI design and front-end development, with the University of Oregon, UC Berkeley, Michigan, Minnesota, Utah and Arizona.'),
 dict(kicker='Experience &middot; Before', bg='#d5ecff', img=MAIL[12], alt='Drawing of Tin posting a letter', logo=SF,
      name='Salesforce', role='Designer', when='2020 &mdash; 2022', dur='2 yrs', back_k='What I did there',
      back='Redesigned search and content for Salesforce Help, cutting support cases 60% a month. Built a back-to-work app for 75K employees, shipped 8+ Partner Community features, and added components to the C360 design system across 12 product teams.'),
 dict(kicker='Experience &middot; Before', bg='#e6f4ff', img=MAIL[0], alt='Drawing of Tin', logo=SF,
      name='Salesforce', role='Associate Designer', when='2018 &mdash; 2020', dur='1.5 yrs', back_k='What I did there',
      back='Worked with stakeholders to map customer experiences, find pain points and spot opportunities, then designed wireframe concepts with the Salesforce Lightning Design System.'),
 dict(kicker='Internship', bg='#eaf0ff', img=HAND[12], alt='Drawing of Tin shaking hands', logo=SF,
      name='Salesforce', role='Summer UX Designer', when='2017', dur='Summer', back_k='Where it started',
      back='My first product design role, the summer before Salesforce hired me full time: onboarding improvements, and the branding for a Salesforce hackathon.'),
 dict(kicker='Industrial design', bg='#dff3e4', img=PARTY[0], alt='Drawing of Tin reaching into his jacket', logo=TXT('L'),
      name='Luxium Lighting', role='Product Designer', when='Sep &mdash; Dec 2017', dur='4 mos', back_k='What I made',
      back='An LED light, from design concept to a working prototype: 3D CAD models, studio product designs, and close work with engineers to test it against usability and quality standards.'),
 dict(kicker='Education', bg='#e9f1cf', img=WAVE[6], alt='Drawing of Tin waving', logo=UO,
      name='University of Oregon', role='BS Industrial Design', when='2014 &mdash; 2018', dur='Business minor', back_k='What I learned',
      back='How to design physical products: sketching, CAD, rendering and building prototypes by hand. Won 1st place overall at Quackhatch @UO in 2018.'),
]
TILT = [-4, 2.5, -2, 3, -3, 2, -2.5, 3.5]; DROP = [70, 150, 100, 60, 130, 90, 140, 80]; DL = [-0.6, -2.1, -3.4, -1.2, -2.7, -4.0, -1.8, -3.1]
N = len(CARDS)
def card(i, c, copy):
    k = i + 1
    hid = ' aria-hidden="true"' if copy else ''
    tab = '-1' if copy else '0'
    return f'''
      <div class="bd-hang"{hid} style="--t: {TILT[i]}deg; --drop: {DROP[i]}px; --dl: {DL[i]}s; --pin: 12px">
        <span class="bd-pin" aria-hidden="true"></span><span class="bd-thread" aria-hidden="true"></span>
        <div class="bd-swing">
          <span class="bd-clip" aria-hidden="true"></span>
          <div class="bd-card {{{{bdFlip{k}Class}}}}" role="button" tabindex="{tab}" aria-pressed="{{{{bdFlip{k}On}}}}" aria-label="{c['name']}, {c['role']} badge, flip for details" onClick="{{{{bdFlip{k}}}}}" onKeyDown="{{{{bdKey{k}}}}}">
            <div class="bd-face bd-front">
              <div class="bd-top"><span>{c['kicker']}</span><span>#{k:02d}</span></div>
              <div class="bd-photo" style="background-color: {c['bg']}"><img src="{c['img']}" alt="{c['alt']}"><span class="bd-logo">{c['logo']}</span></div>
              <p class="bd-name">{c['name']}</p>
              <p class="bd-role">{c['role']}</p>
              <div class="bd-foot"><span>{c['when']} &middot; {c['dur']}</span><span class="bd-arrow">{ARROW}</span></div>
            </div>
            <div class="bd-face bd-back">
              <div class="bd-top"><span>{c['kicker']}</span><span>#{k:02d}</span></div>
              <p class="bd-bk">{c['back_k']}</p>
              <p class="bd-desc">{c['back']}</p>
              <div class="bd-foot"><span>Flip back</span><span class="bd-arrow bd-arrow-back">{ARROW}</span></div>
            </div>
          </div>
        </div>
      </div>'''
track = ''.join(card(i, c, True) for i, c in enumerate(CARDS)) + ''.join(card(i, c, False) for i, c in enumerate(CARDS)) + ''.join(card(i, c, True) for i, c in enumerate(CARDS))
a = s.index('<div class="bd-track"'); a = s.index('>', a) + 1
b = s.index('\n    </div></div>\n    <div class="bd-edge', a)
s = s[:a] + track + s[b:]
# 6 -> 8 jobs in the logic
old_n = int(re.search(r"bdGo\(d\) \{[^\n]*\n    const n = (\d+),", s).group(1))
rep(f"const n = {old_n}, ms = this.tp('slideMs', 900);", f"const n = {N}, ms = this.tp('slideMs', 900);")
rep(f"- ({old_n} + (this.state.bdI || 0))", f"- ({N} + (this.state.bdI || 0))")
key = lambda k: f"(e) => {{ if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); this.bdToggle({k}); }} }}"
for k in range(old_n + 1, N + 1):
    anchor = f"      bdFlip{old_n}: () => this.bdToggle({old_n}),"
    line_start = s.index(anchor); line_end = s.index('\n', line_start) + 1
    s = s[:line_end] + f"      bdFlip{k}: () => this.bdToggle({k}), bdKey{k}: {key(k)}, bdFlip{k}Class: this.state.bdFlip && this.state.bdFlip[{k}] ? 'is-flipped' : '', bdFlip{k}On: this.state.bdFlip && this.state.bdFlip[{k}] ? 'true' : 'false',\n" + s[line_end:]
    old_n_line = k  # keep appending after the newest line
    anchor = None
open(p, 'w').write(s)
m = re.search(r"data-props=(['\"])(.*?)\1>\n(.*?)</script>", s, re.S)
open('/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/rb_logic.js', 'w').write('class DCLogic{}\n' + m.group(3))
print('ok', N, 'cards; was', old_n)
