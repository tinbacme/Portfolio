"""Box (3): clone the user's badge pair (front + back) for every role from the resume, 2-column grid."""
import sys, re, json
p, cj = sys.argv[1], sys.argv[2]
s = open(p).read()
a = s.index('<div class="bv-pair"'); b = s.index('</x-dc>')
T = s[a:b].rstrip() + '\n'
MS = ('<svg viewBox="0 0 20 20" width="30" height="30" aria-label="Microsoft" role="img" style="display: block"><rect x="0" y="0" width="9" height="9" fill="#f25022"></rect>'
      '<rect x="11" y="0" width="9" height="9" fill="#7fba00"></rect><rect x="0" y="11" width="9" height="9" fill="#00a4ef"></rect><rect x="11" y="11" width="9" height="9" fill="#ffb900"></rect></svg>')
SF = '<img src="/_blob/ac43d25c19be4e522f4bd492e1c090ab" alt="Salesforce" style="display: block; width: 72%; height: auto">'
UO = '<img src="/_blob/00e0e1ec841a28c4e0055e4a6738e6b1" alt="University of Oregon" style="display: block; width: 46%; height: auto">'
TXT = lambda t: f'<span style="font-weight: 700; font-size: 20px; color: #141414; letter-spacing: -0.02em">{t}</span>'
R = [
 ('Microsoft AI', 'Senior Product Designer', '2022 — now', '4 YEARS', MS,
  'I design search across Bing, Edge and Windows: helping people find what they need, growing Bing, and exploring what AI agents could do in search.'),
 ('University of Oregon', 'Product Design Instructor', '2023 — now', '3 YEARS', UO,
  'I teach UX and product design at the school where I studied industrial design. Students learn the way I still work: by building and prototyping.'),
 ('2U', 'UX/UI Bootcamp Instructor', '2021 —', 'REMOTE', TXT('2U'),
  'I led cohorts through a 24-week bootcamp in UX research, UX and UI design and front-end development, teaching with the University of Oregon, UC Berkeley, Michigan, Minnesota, Utah and Arizona.'),
 ('Salesforce', 'Designer', '2020 — 2022', '2 YEARS', SF,
  'I redesigned search and content for Salesforce Help, which cut support cases by 60% per month, built a back-to-work app for 75K employees, shipped more than 8 Partner Community features, and added components to the C360 design system across 12 product teams.'),
 ('Salesforce', 'Associate Designer', '2018 — 2020', '1.5 YEARS', SF,
  'I worked with stakeholders to map customer experiences, find pain points and spot opportunities, then designed wireframe concepts with the Salesforce Lightning Design System.'),
 ('Salesforce', 'Product Design Intern', '2017', 'SUMMER', SF,
  'My first product design role: onboarding improvements, and the branding for a Salesforce hackathon.'),
 ('Luxium Lighting', 'Product Designer', 'Sep — Dec 2017', '4 MONTHS', TXT('L'),
  'I took an LED light from design concept to a working prototype: 3D CAD models, studio product designs, and close work with engineers to test it against usability and quality standards.'),
 ('University of Oregon', 'BS Industrial Design', '2014 — 2018', 'BUSINESS MINOR', UO,
  'I studied industrial design with a business minor: sketching, CAD, rendering and building prototypes by hand. I won 1st place overall at Quackhatch @UO in 2018.'),
]
def one(old, new, t):
    assert t.count(old) == 1, (old[:80], t.count(old)); return t.replace(old, new)
logo_old = re.search(r'<img src="/_blob/ac43d25c19be4e522f4bd492e1c090ab" alt="Salesforce" style="display: block; width: 72%; height: auto">', T).group(0)
desc_old = re.search(r'(<p class="bd-desc"[^>]*>)(.*?)(</p>)', T, re.S)
PW, PH, GX, GY = 683, 622, 40, 40
out = []
for i, (co, title, when, dur, logo, desc) in enumerate(R):
    t = T
    t = one('left: 0px; top: 0px;', f'left: {(i % 2) * (PW + GX)}px; top: {(i // 2) * (PH + GY)}px;', t)
    t = one('<p class="bv-label">Original · current badge</p>', f'<p class="bv-label">#{i + 1:02d} · {co} · {title}</p>', t)
    t = one('<span>2022- 2024</span><span>5 YEARS</span>', f'<span>{when}</span><span>{dur}</span>', t)
    t = re.sub(r'(<p class="bd-name"[^>]*>)Product Design Intern(</p>)', lambda m: m.group(1) + title + m.group(2), t, count=1)
    t = one('font-size: 14px">Salesforce</p>', f'font-size: 14px">{co}</p>', t)
    t = one(logo_old, logo, t)
    t = one('<span>Product Designer At Salesforce</span>', f'<span>{title} at {co}</span>', t)
    t = one(desc_old.group(0), desc_old.group(1) + desc + desc_old.group(3), t)
    out.append(t)
s = s[:a] + ''.join(out) + s[b:]
open(p, 'w').write(s)
c = json.load(open(cj)); bx = c['boards']['Piece-46el.dc.html']
bx['w'] = PW * 2 + GX; bx['h'] = PH * 4 + GY * 3
over = [k for k, v in c['boards'].items() if k != 'Piece-46el.dc.html' and v.get('page') == bx['page'] and v['x'] < bx['x'] + bx['w'] and v['x'] + v['w'] > bx['x'] and v['y'] < bx['y'] + bx['h'] and v['y'] + v.get('h', 900) > bx['y']]
notes = [k for k, v in c['notes'].items() if v.get('page') == bx['page'] and 'w' in v and 'h' in v and v['x'] < bx['x'] + bx['w'] and v['x'] + v['w'] > bx['x'] and v['y'] < bx['y'] + bx['h'] and v['y'] + v['h'] > bx['y']]
json.dump(c, open(cj, 'w'), ensure_ascii=False, indent=2)
print('ok', len(out), 'pairs; board', bx['w'], 'x', bx['h'], 'overlaps', over, notes)
