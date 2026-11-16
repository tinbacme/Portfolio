"""Resume / work-history variations board (10 treatments) for Tin Le's portfolio.
usage: python3 resumevars.py [out.dc.html]"""
import json, sys

S = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/'
OUT = sys.argv[1] if len(sys.argv) > 1 else S + 'canvas4/project/ResumeVariations.dc.html'


def h(s):
    """HTML text: non-ASCII as numeric entities."""
    return ''.join(c if ord(c) < 128 else f'&#{ord(c)};' for c in s)


UO, SF = '/_blob/00e0e1ec841a28c4e0055e4a6738e6b1', '/_blob/ac43d25c19be4e522f4bd492e1c090ab'
P_MS, P_UO, P_SF, P_GRAD = ('/_blob/effff208332abe411e27c82aaa87e30d', '/_blob/155942c7f1c522f9aec7d43d1c1d0d0d',
                            '/_blob/8bd998ead1110dbdb0a707cdb0cb6c60', '/_blob/54416d11bdc955c9c7fb45c9c479a828')
NDA = 'Under NDA — happy to walk you through it'
NOW = 2026 + 10.5 / 12
SKILLS = ['UX research', 'Interaction design', 'Prototyping', 'Design systems', 'AI/search product design', 'Teaching']
SF_BUL = ['Redesigned search and content for Salesforce Help, cutting support cases 60% a month',
          'Built a back-to-work app for 75K employees',
          'Shipped 8+ Partner Community features',
          'Added components to the C360 design system across 12 product teams']

R = [
    dict(k='ms', title='Senior Product Designer', org='Microsoft AI', logo='ms', dates='2022 — now', y0=2022, y1=NOW,
         kind='design', now=True, photo=P_MS, yr='2022', yrs='— now',
         sum='Search across Bing, Edge and Windows: helping people find what they need, growing Bing, and exploring what AI agents could do in search.'),
    dict(k='uo', title='Product Design Instructor', org='University of Oregon', logo='uo', dates='2023 — now', y0=2023, y1=NOW,
         kind='teach', now=True, photo=P_UO, yr='2023', yrs='— now',
         sum='Teaching UX and product design at the school where I studied industrial design: a 12-week course in UX research, UX/UI design and prototyping more effectively.'),
    dict(k='2u', title='UX/UI Bootcamp Instructor', org='2U', logo='2u', dates='Since 2021', y0=2021, y1=2024, open=True,
         kind='teach', now=False, photo=None, yr='2021', yrs='since',
         sum='Led cohorts through a 24-week bootcamp in UX research, UX and UI design and front-end development, with UO, UC Berkeley, Michigan, Minnesota, Utah and Arizona.'),
    dict(k='sf3', title='Designer', org='Salesforce', logo='sf', dates='2020 — 2022', y0=2020, y1=2022,
         kind='design', now=False, photo=P_SF, yr='2020', yrs='— 2022',
         sum='Redesigned search and content for Salesforce Help, cutting support cases 60% a month; built a back-to-work app for 75K employees; shipped 8+ Partner Community features; added components to the C360 design system across 12 product teams.'),
    dict(k='sf2', title='Associate Designer', org='Salesforce', logo='sf', dates='2018 — 2020', y0=2018, y1=2020,
         kind='design', now=False, photo=P_SF, yr='2018', yrs='— 2020',
         sum='Mapped customer experiences with stakeholders, found pain points, and designed wireframe concepts with the Lightning Design System.'),
    dict(k='sf1', title='Summer UX Designer (intern)', org='Salesforce', logo='sf', dates='2017', y0=2017.42, y1=2017.67,
         kind='design', now=False, photo=P_SF, yr='2017', yrs='summer',
         sum='My first product design role: onboarding improvements and branding for a Salesforce hackathon.'),
    dict(k='lux', title='Product Designer', org='Luxium Lighting', logo='lux', dates='Sep — Dec 2017', y0=2017.67, y1=2018,
         kind='design', now=False, photo=None, yr='2017', yrs='Sep — Dec',
         sum='An LED light from concept to working prototype: 3D CAD, studio product design, and testing with engineers.'),
    dict(k='edu', title='BS Industrial Design, Business minor', org='University of Oregon', logo='uo', dates='2014 — 2018', y0=2014, y1=2018,
         kind='school', now=False, photo=P_GRAD, yr='2014', yrs='— 2018',
         sum='Sketching, CAD, rendering and prototyping by hand. 1st place overall at Quackhatch @UO 2018.'),
]
N = len(R)


def ms_svg(s, mono=None):
    c = [mono] * 4 if mono else ['#f25022', '#7fba00', '#00a4ef', '#ffb900']
    return (f'<svg viewBox="0 0 20 20" width="{s}" height="{s}" aria-hidden="true"><rect x="0" y="0" width="9" height="9" fill="{c[0]}"></rect>'
            f'<rect x="11" y="0" width="9" height="9" fill="{c[1]}"></rect><rect x="0" y="11" width="9" height="9" fill="{c[2]}"></rect>'
            f'<rect x="11" y="11" width="9" height="9" fill="{c[3]}"></rect></svg>')


def logo(k, s=20, cls=''):
    c = f' class="{cls}"' if cls else ''
    if k == 'ms': return ms_svg(s)
    if k == 'uo': return f'<img src="{UO}" alt=""{c} width="{round(s * 1.21)}" height="{s}">'
    if k == 'sf': return f'<img src="{SF}" alt=""{c} width="{round(s * 1.43)}" height="{s}">'
    if k == '2u': return f'<span class="mk-2u" style="font-size: {round(s * .72)}px">2U</span>'
    if k == 'lux': return f'<span class="mk-lux" style="font-size: {max(7, round(s * .3))}px">LUXIUM</span>'


LOCK = ('<svg viewBox="0 0 16 16" width="12" height="12" aria-hidden="true"><rect x="3" y="7" width="10" height="7" rx="2" fill="currentColor"></rect>'
        '<path d="M5.5 7V5a2.5 2.5 0 0 1 5 0v2" fill="none" stroke="currentColor" stroke-width="1.6"></path></svg>')
CHEV = ('<svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M4 6l4 4 4-4" fill="none" stroke="currentColor" '
        'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>')
ARROW_DL = ('<svg viewBox="0 0 16 16" width="14" height="14" aria-hidden="true"><path d="M8 2.5v8M4.5 7.5 8 11l3.5-3.5M3 13.5h10" fill="none" '
            'stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path></svg>')
DOC = ('<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M4 1.5h5.5L13 5v9.5H4z" fill="#fff" stroke="#9a9a9a" stroke-width="1.2" '
       'stroke-linejoin="round"></path><path d="M9.5 1.5V5H13" fill="none" stroke="#9a9a9a" stroke-width="1.2"></path></svg>')


def nda(cls='nda'):
    return f'<span class="{cls}">{LOCK}{h(NDA)}</span>'


def summ(r, tag='p', cls=''):
    """summary paragraph; Microsoft gets the NDA chip next to it."""
    c = f' class="{cls}"' if cls else ''
    out = f'<{tag}{c}>{h(r["sum"])}</{tag}>'
    if r['k'] == 'ms': out += nda()
    return out


# ---------------------------------------------------------------- V1 vertical timeline
def v1():
    items = ''
    for i, r in enumerate(R):
        items += (f'<li class="v1-it{" now" if r["now"] else ""} {{{{t1c{i}}}}}"><span class="v1-dot" aria-hidden="true"></span>'
                  f'<button class="v1-hd" type="button" aria-expanded="{{{{t1x{i}}}}}" aria-controls="v1-p{i}" onClick="{{{{t1f{i}}}}}">'
                  f'<span class="v1-date">{h(r["dates"])}</span><span class="v1-role">{h(r["title"])}</span>'
                  f'<span class="v1-org">{h(r["org"])}</span><span class="v1-chev">{CHEV}</span></button>'
                  f'<div class="v1-body" id="v1-p{i}"><div class="v1-in">{summ(r)}</div></div></li>')
    return f'<div class="mini-h"><span>Experience</span><span class="mini-n">9 years</span></div><ol class="v1">{items}</ol>'


# ---------------------------------------------------------------- V2 year ledger
def v2():
    rows = ''.join(
        f'<button class="v2-row{"" if r["now"] else " past"} {{{{l2c{i}}}}}" type="button" aria-pressed="{{{{l2x{i}}}}}" aria-controls="v2-out" '
        f'onClick="{{{{l2f{i}}}}}" onMouseEnter="{{{{l2f{i}}}}}"><span class="v2-org"><i aria-hidden="true"></i>{h(r["org"])}</span>'
        f'<span class="v2-role">{h(r["title"])}</span><span class="v2-yr">{h(r["dates"].replace(" — ", "–"))}</span></button>'
        for i, r in enumerate(R))
    panels = ''.join(
        f'<div class="v2-p {{{{l2c{i}}}}}"><p class="v2-pk">{i + 1:02d} / {N:02d}{" &#183; NOW" if r["now"] else ""}</p>'
        f'<p class="v2-pt">{h(r["title"])}, {h(r["org"])}</p>{summ(r, cls="v2-ps")}</div>' for i, r in enumerate(R))
    return (f'<div class="v2"><div class="v2-head" aria-hidden="true"><span>Org</span><span>Role</span><span class="v2-yr">Years</span></div>{rows}</div>'
            f'<div class="v2-out" id="v2-out" aria-live="polite">{panels}</div>')


# ---------------------------------------------------------------- V3 accordion
def v3():
    rows = ''
    for i, r in enumerate(R):
        extra = ''
        if r['k'] == 'sf3':
            extra = '<ul class="v3-ul">' + ''.join(f'<li>{h(b)}</li>' for b in SF_BUL) + '</ul>'
            body = extra
        else:
            body = summ(r, cls='v3-p')
        rows += (f'<div class="v3-row {{{{a3c{i}}}}}"><button class="v3-hd" type="button" aria-expanded="{{{{a3x{i}}}}}" aria-controls="v3-p{i}" onClick="{{{{a3f{i}}}}}">'
                 f'<span class="v3-meta"><span class="v3-org">{h(r["org"])}</span><span class="v3-yr">{h(r["dates"])}</span></span>'
                 f'<span class="v3-ttl">{h(r["title"])}</span><span class="v3-pm" aria-hidden="true"><i></i><i></i></span></button>'
                 f'<div class="v3-body" id="v3-p{i}"><div class="v3-in"><div class="v3-grid"><span class="v3-lg">{logo(r["logo"], 22)}</span>'
                 f'<div class="v3-txt">{body}</div></div></div></div></div>')
    return f'<div class="v3">{rows}</div>'


# ---------------------------------------------------------------- V4 gantt
def pct(y): return f'{(y - 2014) / 13 * 100:.3f}%'


def v4():
    axis = ''.join(f'<span style="left: {pct(y)}">{y}</span>' for y in range(2014, 2027))
    rows = ''
    for i, r in enumerate(R):
        w = (r['y1'] - r['y0']) / 13 * 972
        inside = w > 130
        lab = f'<span class="v4-bl{"" if inside else " out"}">{h(r["dates"])}</span>'
        rows += (f'<button class="v4-row k-{r["kind"]}{" open" if r.get("open") else ""} {{{{g4c{i}}}}}" type="button" aria-pressed="{{{{g4x{i}}}}}" '
                 f'aria-controls="v4-det" onClick="{{{{g4f{i}}}}}" aria-label="{h(r["title"])}, {h(r["org"])}, {h(r["dates"])}">'
                 f'<span class="v4-lab"><span class="v4-lt">{h(r["title"])}</span><span class="v4-lo">{h(r["org"])}</span></span>'
                 f'<span class="v4-trk"><span class="v4-bar" style="left: {pct(r["y0"])}; width: {(r["y1"] - r["y0"]) / 13 * 100:.3f}%">{lab}</span></span></button>')
    det = ''.join(
        f'<div class="v4-dp {{{{g4c{i}}}}}"><span class="v4-dl">{logo(r["logo"], 22)}</span><div><p class="v4-dt">{h(r["title"])} '
        f'<span>&#183; {h(r["org"])} &#183; {h(r["dates"])}</span></p>{summ(r, cls="v4-ds")}</div></div>' for i, r in enumerate(R))
    legend = ('<div class="v4-leg"><span><i class="sw k-design"></i>Design</span><span><i class="sw k-teach"></i>Teaching</span>'
              '<span><i class="sw k-school"></i>School</span><span><i class="sw now"></i>Today</span></div>')
    return (f'<div class="v4-top"><p class="v4-h">Teaching has run alongside design work since 2021.</p>{legend}</div>'
            f'<div class="v4"><div class="v4-axis" aria-hidden="true"><span class="v4-sp"></span><span class="v4-ax">{axis}</span></div>'
            f'<div class="v4-rows">{rows}<span class="v4-today" aria-hidden="true" style="left: calc(240px + (100% - 240px) * {(NOW - 2014) / 13:.4f})"><b>Today</b></span></div></div>'
            f'<div class="v4-det" id="v4-det" aria-live="polite">{det}</div>')


# ---------------------------------------------------------------- V5 cards grid
TINT = {'ms': ('#f3f3f3', '#141414'), 'uo': ('#e4f3eb', '#00743b'), '2u': ('#141414', '#ffffff'), 'sf3': ('#e2f4fb', '#0a6f99'),
        'sf2': ('#e2f4fb', '#0a6f99'), 'sf1': ('#e2f4fb', '#0a6f99'), 'lux': ('#f3f3f3', '#141414'), 'edu': ('#e4f3eb', '#00743b')}


def v5():
    cards = ''
    for i, r in enumerate(R):
        bg, ink = TINT[r['k']]
        lg = logo(r['logo'], 30 if r['k'] == 'lux' else 22, 'inv' if r['k'] == '2u' else '')
        yr = f'<small class="pre">{h(r["yrs"])}</small>{r["yr"]}' if r['k'] == '2u' else f'{r["yr"]}<small>{h(r["yrs"])}</small>'
        more = (f'<button class="v5-more" type="button" aria-expanded="{{{{c5x{i}}}}}" aria-controls="v5-s{i}" onClick="{{{{c5f{i}}}}}">'
                f'<span class="t-off">Read more</span><span class="t-on">Show less</span>{CHEV}</button>') if len(r['sum']) > 110 else ''
        tag = '<span class="v5-now">Now</span>' if r['now'] else ''
        cards += (f'<article class="v5-c {{{{c5c{i}}}}}" style="--tint: {bg}; --ink: {ink}"><div class="v5-top"><div class="v5-tr"><span class="v5-lg">{lg}</span>{tag}</div>'
                  f'<p class="v5-yr">{yr}</p></div><div class="v5-bd"><h3 class="v5-ttl">{h(r["title"])}</h3>'
                  f'<p class="v5-org">{h(r["org"])} &#183; {h(r["dates"])}</p><p class="v5-sum" id="v5-s{i}">{h(r["sum"])}</p>'
                  + (nda('nda sm') if r['k'] == 'ms' else '') + more + '</div></article>')
    return f'<div class="v5">{cards}</div>'


# ---------------------------------------------------------------- V6 grouped by company
def v6_role(r, nested=False):
    return (f'<div class="v6-r{" nest" if nested else ""}"><p class="v6-rt">{h(r["title"])}</p><p class="v6-rd">{h(r["dates"])}</p>'
            f'<p class="v6-rs">{h(r["sum"])}</p>{nda("nda sm") if r["k"] == "ms" else ""}</div>')


def v6():
    g = lambda r, meta, inner, extra=False: (
        f'<div class="v6-g{" v6-extra" if extra else ""}"><span class="v6-lg">{logo(r["logo"], 24)}</span><div>'
        f'<p class="v6-co">{h(r["org"])}</p><p class="v6-meta">{h(meta)}</p>{inner}</div></div>')
    sf = [r for r in R if r['logo'] == 'sf']
    by = {r['k']: r for r in R}
    out = (g(by['ms'], 'Search', v6_role(by['ms'])) + g(by['uo'], 'Teaching', v6_role(by['uo']))
           + g(by['2u'], 'Teaching', v6_role(by['2u']))
           + g(sf[0], '3 roles · 2017 — 2022', '<div class="v6-tree">' + ''.join(v6_role(r, True) for r in sf) + '</div>')
           + g(by['lux'], 'Product design', v6_role(by['lux']), True) + g(by['edu'], 'Education', v6_role(by['edu']), True))
    return (f'<div class="mini-h"><span>Experience</span><span class="mini-n">6 places</span></div>'
            f'<div class="v6 {{{{s6c}}}}" id="v6-list">{out}</div>'
            f'<button class="v6-btn" type="button" aria-expanded="{{{{s6x}}}}" aria-controls="v6-list" onClick="{{{{s6f}}}}">'
            f'<span class="t-off">Show 2 more</span><span class="t-on">Show less</span>{CHEV}</button>')


# ---------------------------------------------------------------- V7 now / before
def v7_row(r, rich):
    return (f'<div class="v7-row k-{r["kind"]}"><span class="v7-lg">{logo(r["logo"], 16)}</span><div><p class="v7-t">{h(r["title"])}</p>'
            f'<p class="v7-o">{h(r["org"])} &#183; {h(r["dates"])}</p>'
            + (f'<p class="v7-s">{h(r["sum"])}</p>' + (nda('nda sm') if r['k'] == 'ms' else '') if rich else '') + '</div></div>')


def v7():
    now = ''.join(v7_row(r, True) for r in R if r['now'])
    before = ''.join(v7_row(r, False) for r in R if not r['now'])
    seg = ''.join(f'<button type="button" class="{{{{f7c{k}}}}}" aria-pressed="{{{{f7x{k}}}}}" onClick="{{{{f7f{k}}}}}">{lab}</button>'
                  for k, lab in [('all', 'All'), ('design', 'Design'), ('teach', 'Teaching')])
    return (f'<div class="v7-hero"><p class="v7-big"><span>9 years</span> designing products</p>'
            f'<div class="seg v7-seg" role="group" aria-label="Filter roles">{seg}</div></div>'
            f'<div class="v7 {{{{f7cls}}}}"><div><p class="v7-h"><i class="live" aria-hidden="true"></i>Now</p>{now}</div>'
            f'<div><p class="v7-h">Before</p>{before}</div></div>'
            f'<div class="v7-skills"><p class="v7-h">Skills</p><div class="chips">' + ''.join(f'<span class="chip">{h(x)}</span>' for x in SKILLS) + '</div></div>')


# ---------------------------------------------------------------- V8 editorial list + hover photo
def v8():
    rows = ''.join(
        f'<button class="v8-row {{{{h8c{i}}}}}" type="button" aria-pressed="{{{{h8x{i}}}}}" aria-controls="v8-pv" onClick="{{{{h8f{i}}}}}" '
        f'onMouseEnter="{{{{h8f{i}}}}}" onFocus="{{{{h8f{i}}}}}"><span class="v8-n">{i + 1:02d}</span><span class="v8-org">{h(r["org"])}</span>'
        f'<span class="v8-role">{h(r["title"])}</span><span class="v8-yr">{h(r["dates"])}</span></button>' for i, r in enumerate(R))
    ph = ''
    for i, r in enumerate(R):
        if r['photo']:
            pos = ' style="object-position: 50% 30%"' if r['k'] in ('ms', 'uo') else ''
            ph += f'<img class="{{{{h8c{i}}}}}" src="{r["photo"]}" alt=""{pos}>'
        else:
            ph += f'<span class="v8-mark {{{{h8c{i}}}}} m-{r["k"]}">{logo(r["logo"], 64)}</span>'
    caps = ''.join(f'<div class="v8-cap {{{{h8c{i}}}}}"><p class="v8-ct">{h(r["title"])}</p>{summ(r, cls="v8-cs")}</div>' for i, r in enumerate(R))
    return (f'<div class="v8"><div class="v8-list">{rows}</div><div class="v8-side"><div class="v8-pv" id="v8-pv" aria-live="polite" '
            f'style="transform: translateY({{{{h8y}}}})"><div class="v8-ph">{ph}</div>{caps}</div></div></div>')


# ---------------------------------------------------------------- V9 bento
def v9():
    by = {r['k']: r for r in R}
    tabs = ''.join(f'<button type="button" class="{{{{b9c{i}}}}}" aria-pressed="{{{{b9x{i}}}}}" onClick="{{{{b9f{i}}}}}">{h(lab)}</button>'
                   for i, lab in enumerate(['Designer', 'Associate', 'Intern']))
    mets = [('60%', 'fewer support cases a month on Salesforce Help'), ('75K', 'employees on the back-to-work app'),
            ('8+', 'Partner Community features shipped'), ('12', 'product teams on my C360 components')]
    p0 = '<div class="v9-mets">' + ''.join(f'<div><b>{n}</b><span>{h(t)}</span></div>' for n, t in mets) + '</div>'
    panels = (f'<div class="v9-sp {{{{b9c0}}}}"><p class="v9-sr">Designer &#183; 2020 &#8212; 2022</p>{p0}</div>'
              f'<div class="v9-sp {{{{b9c1}}}}"><p class="v9-sr">Associate Designer &#183; 2018 &#8212; 2020</p><p class="v9-st">{h(by["sf2"]["sum"])}</p></div>'
              f'<div class="v9-sp {{{{b9c2}}}}"><p class="v9-sr">Summer UX Designer (intern) &#183; 2017</p><p class="v9-st">{h(by["sf1"]["sum"])}</p></div>')
    chips = ''.join(f'<span class="chip">{h(s)}</span>' for s in SKILLS)
    return (f'<div class="v9">'
            f'<article class="v9-t ph a"><img src="{P_MS}" alt="" style="object-position: 50% 30%"><div class="v9-ov"><span class="v9-pill">Now</span>'
            f'<p class="v9-big">Senior Product Designer</p><p class="v9-sub">{ms_svg(14)} Microsoft AI &#183; 2022 &#8212; now</p>'
            f'<p class="v9-txt">Search across Bing, Edge and Windows, and what AI agents could do in search.</p>{nda("nda glass")}</div></article>'
            f'<article class="v9-t b"><p class="v9-num">9</p><p class="v9-yl">years designing products</p></article>'
            f'<article class="v9-t ph c"><img src="{P_UO}" alt="" style="object-position: 50% 35%"><div class="v9-ov"><span class="v9-pill">Now</span>'
            f'<p class="v9-mid">Product Design Instructor</p><p class="v9-sub">University of Oregon &#183; 2023 &#8212; now</p>'
            f'<p class="v9-txt">A 12-week course in UX research, UX/UI design and prototyping.</p></div></article>'
            f'<article class="v9-t d"><span class="mk-2u big">2U</span><div><p class="v9-mid">UX/UI Bootcamp Instructor</p>'
            f'<p class="v9-sub">Since 2021 &#183; 24-week bootcamp</p></div></article>'
            f'<article class="v9-t e"><div class="v9-sfh"><div class="v9-sfn"><span class="v9-sfl">{logo("sf", 22)}</span><div><p class="v9-mid dk">Salesforce</p>'
            f'<p class="v9-sub dk">3 roles &#183; 2017 &#8212; 2022</p></div></div><div class="seg" role="group" aria-label="Salesforce role">{tabs}</div></div>{panels}</article>'
            f'<article class="v9-t f"><span class="mk-lux" style="font-size: 12px">LUXIUM</span><div><p class="v9-mid dk">Product Designer</p>'
            f'<p class="v9-sub dk">Luxium Lighting &#183; Sep &#8212; Dec 2017</p><p class="v9-st sm">An LED light from concept to working prototype.</p></div></article>'
            f'<article class="v9-t ph g"><img src="{P_GRAD}" alt=""><div class="v9-ov"><p class="v9-mid">BS Industrial Design</p>'
            f'<p class="v9-sub">University of Oregon &#183; 2014 &#8212; 2018</p><span class="v9-pill gold">1st place, Quackhatch @UO 2018</span></div></article>'
            f'<article class="v9-t s"><p class="v9-sk">Skills</p><div class="chips">{chips}</div></article>'
            f'</div>')


# ---------------------------------------------------------------- V10 resume sheet
def v10_entry(r):
    body = (f'<p class="v10-es">{h(r["sum"])}</p>' if r['k'] != 'sf3' else
            '<ul class="v10-ul">' + ''.join(f'<li>{h(b)}</li>' for b in SF_BUL) + '</ul>')
    if r['k'] == 'ms': body = f'<p class="v10-es">{h(r["sum"])}</p><p class="v10-es v10-nda">{h(NDA)}</p>'
    return (f'<div class="v10-e"><div class="v10-et"><p><b>{h(r["title"])}</b> <span>&#183; {h(r["org"])}</span></p>'
            f'<span class="v10-d">{h(r["dates"])}</span></div>{body}</div>')


def v10():
    by = {r['k']: r for r in R}
    sec = lambda t, inner: f'<section class="v10-sec"><h4 class="v10-sh">{t}</h4><div>{inner}</div></section>'
    seg = ''.join(f'<button type="button" class="{{{{m10c{k}}}}}" aria-pressed="{{{{m10x{k}}}}}" onClick="{{{{m10f{k}}}}}">{lab}</button>'
                  for k, lab in [('d', 'Detailed'), ('c', 'Compact')])
    return (f'<div class="v10-bar"><p class="v10-file">{DOC}<span>Tin Le &#8212; Resume</span><span class="v10-pg">1 page</span></p>'
            f'<div class="seg" role="group" aria-label="Resume length">{seg}</div>'
            f'<div class="v10-act"><span class="v10-note">Placeholder: no PDF is attached yet</span>'
            f'<button type="button" class="v10-dl" title="Placeholder: not wired up yet">{ARROW_DL}Download PDF</button></div></div>'
            f'<div class="v10-paper {{{{m10cls}}}}"><header class="v10-hd"><div><p class="v10-name">Tin Le</p>'
            f'<p class="v10-tag">Product designer &#183; 9 years designing products</p></div><span class="v10-mono">Resume &#183; 2026</span></header>'
            + sec('Experience', ''.join(v10_entry(by[k]) for k in ['ms', 'sf3', 'sf2', 'sf1', 'lux']))
            + sec('Teaching', ''.join(v10_entry(by[k]) for k in ['uo', '2u']))
            + sec('Education', v10_entry(by['edu']))
            + sec('Skills', '<p class="v10-sk">' + h(' · '.join(SKILLS)) + '</p>')
            + '</div>')


# ---------------------------------------------------------------- assemble
M = 'https://mobbin.com/'
SECS = [
    ('V1', 'Vertical timeline', 'Inspired by Grok on Mobbin: small dot markers on a thin line, mono dates. Click a role to open its summary; current roles get a blue dot.', v1, False, ''),
    ('V2', 'Year ledger', 'Inspired by Aino Agency on Mobbin: one mono, all-caps table. Current roles black, past ones gray; hover or click a row to read it below.', v2, False, ''),
    ('V3', 'Accordion rows', 'Inspired by YLLW on Mobbin: org and years small on the left, the role big in the middle, a plus to open. Several can be open at once.', v3, True, ''),
    ('V4', 'Overlap chart', 'Inspired by the Plane timeline view on Mobbin: every role as a bar on one year axis, so teaching overlapping Microsoft is plain to see. Click a bar for details.', v4, True, ''),
    ('V5', 'Logo cards', 'Inspired by Revolut on Mobbin: a tinted top with the logo and a big start year, then the role. Longer summaries open in place.', v5, True, ''),
    ('V6', 'Grouped by company', 'Inspired by Upwork profiles on Mobbin: one entry per place, with the three Salesforce roles stacked on a line. Older entries hide behind Show more.', v6, False, ''),
    ('V7', 'Now and before', 'Inspired by Customer.io on Mobbin: a big handwritten number beside two plain columns. The filter dims roles that are not design or teaching.', v7, False, ''),
    ('V8', 'Big type, photo preview', 'Inspired by Locomotive on Mobbin: huge gray org names that go black on hover, with a photo card sliding to the row you are on.', v8, True, ''),
    ('V9', 'Bento grid', 'Inspired by Analogue Agency on Mobbin: photos, roles, a big number and skills in one grid. The Salesforce tile switches between its three roles.', v9, True, ''),
    ('V10', 'Resume sheet', 'Inspired by the Square client view on Mobbin: a printable page on gray with a length toggle and a Download PDF button (placeholder, not wired up).', v10, True, 'st-gray'),
]

body = ''
for tag, title, sub, fn, full, st in SECS:
    body += (f'\n  <section class="rv-sec{" rv-full" if full else ""}"><p class="rv-k">{tag}</p><h2 class="rv-t">{h(title)}</h2>'
             f'<p class="rv-s">{h(sub)}</p><div class="rv-stage {st} s-{tag.lower()}">{fn()}</div></section>')

CSS = r'''
body{margin:0}
sc-for, sc-if { display: contents; }
.rv-root{width:1440px;box-sizing:border-box;padding:56px;background:#fafafa;color:#000;font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased;display:grid;grid-template-columns:1fr 1fr;gap:64px 24px}
.rv-sec{display:flex;flex-direction:column;min-width:0}
.rv-full{grid-column:1/-1}
.rv-k{margin:0;font:600 12px/1 Inter,sans-serif;letter-spacing:.08em;color:#b3b3b3}
.rv-t{margin:10px 0 0;font:600 20px/1.3 Inter,sans-serif;letter-spacing:-.01em}
.rv-s{margin:6px 0 0;max-width:760px;font:400 14px/1.45 Inter,sans-serif;color:#7a7a7a}
.rv-sec:not(.rv-full) .rv-s{min-height:40px}
.rv-stage{position:relative;flex:1;margin-top:20px;padding:40px;border-radius:20px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06);overflow:hidden}
.rv-stage.st-gray{background:#f0f0f0}
.rv-root p,.rv-root h3,.rv-root h4,.rv-root ul,.rv-root ol{margin:0}
.rv-root :where(button){font:inherit;color:inherit;background:none;border:0;padding:0;margin:0;text-align:left;cursor:pointer;-webkit-tap-highlight-color:transparent}
.rv-root button:focus-visible{outline:2px solid #0099ff;outline-offset:2px;border-radius:10px}
.rv-root img{display:block}
.mk-2u{font:700 13px/1 Inter,system-ui,sans-serif;letter-spacing:-.03em;color:#141414}
.mk-lux{font:600 10px/1 Inter,sans-serif;letter-spacing:.22em;color:#141414}
.t-on{display:none}
[aria-expanded="true"] > .t-on{display:inline}[aria-expanded="true"] > .t-off{display:none}
.nda{display:inline-flex;align-items:center;gap:6px;margin-top:12px;padding:7px 11px;border-radius:999px;background:#f0f0f0;font:500 12px/1 Inter,sans-serif;color:#4d4d4d;white-space:nowrap}
.nda.sm{margin-top:8px;padding:5px 9px;font-size:11.5px}
.nda.glass{background:rgba(255,255,255,.18);color:#fff;-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}
.mini-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:20px;font:600 15px/1 Inter,sans-serif}
.mini-n{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a}
.seg{display:inline-flex;padding:3px;border-radius:999px;background:#f0f0f0}
.seg button{padding:7px 13px;border-radius:999px;font:500 13px/1 Inter,sans-serif;color:#666;transition:color .2s,background-color .2s,box-shadow .2s}
.seg button:hover{color:#000}
.seg button.on{background:#fff;color:#000;box-shadow:0 1px 2px rgba(0,0,0,.1),0 0 0 1px rgba(0,0,0,.04)}

/* V1 vertical timeline */
.v1{list-style:none;padding:0}
.v1-it{position:relative;padding-left:30px}
.v1-it::before{content:"";position:absolute;left:5px;top:0;bottom:0;width:1px;background:#e6e6e6}
.v1-it:first-child::before{top:30px}
.v1-it:last-child::before{bottom:auto;height:30px}
.v1-dot{position:absolute;left:0;top:25px;width:11px;height:11px;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 1.5px #c4c4c4;transition:background-color .25s,box-shadow .25s}
.v1-it.now .v1-dot{box-shadow:inset 0 0 0 1.5px #0099ff}
.v1-it.on .v1-dot{background:#000;box-shadow:inset 0 0 0 1.5px #000}
.v1-it.now.on .v1-dot{background:#0099ff;box-shadow:inset 0 0 0 1.5px #0099ff,0 0 0 4px #e0f3ff}
.v1-hd{display:grid;grid-template-columns:1fr auto;column-gap:16px;box-sizing:border-box;width:calc(100% + 12px);margin-left:-12px;padding:12px;border-radius:12px;transition:background-color .2s}
.v1-hd:hover{background:#fafafa}
.v1-date{grid-column:1/-1;margin-bottom:7px;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a}
.v1-role{font:600 16px/1.3 Inter,sans-serif;color:#141414}
.v1-org{grid-column:1;font:400 14px/1.4 Inter,sans-serif;color:#7a7a7a}
.v1-chev{grid-column:2;grid-row:2/4;align-self:center;display:grid;place-items:center;width:28px;height:28px;border-radius:50%;color:#9a9a9a;transition:transform .3s,color .2s}
.v1-hd:hover .v1-chev{color:#000}
.v1-it.on .v1-chev{transform:rotate(180deg);color:#000}
.v1-body{display:grid;grid-template-rows:0fr;visibility:hidden;transition:grid-template-rows .35s cubic-bezier(.2,.7,.2,1),visibility .35s}
.v1-it.on .v1-body{grid-template-rows:1fr;visibility:visible}
.v1-in{min-height:0;overflow:hidden}
.v1-in p{max-width:470px;padding:0 0 4px;font:400 14px/1.55 Inter,sans-serif;color:#4d4d4d}
.v1-in{padding-bottom:0}.v1-it.on .v1-in{padding-bottom:14px}

/* V2 year ledger */
.v2{font:400 12px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.04em;text-transform:uppercase}
.v2-head,.v2-row{display:grid;grid-template-columns:160px 1fr 104px;column-gap:16px;align-items:center}
.v2-head{padding:0 0 12px;color:#b3b3b3;border-bottom:1px solid #e6e6e6}
.v2-row{width:100%;height:52px;border-bottom:1px solid #f2f2f2;color:#000;transition:color .2s,background-color .2s}
.v2-row.past{color:#b3b3b3}
.v2-row span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.v2-org{display:flex;align-items:center}
.v2-org i{flex:none;width:6px;height:6px;margin-right:0;border-radius:50%;background:currentColor;transform:scale(0);width:0;transition:transform .25s cubic-bezier(.3,1.6,.5,1),width .25s,margin .25s}
.v2-yr{text-align:right;font-variant-numeric:tabular-nums}
.v2-row:hover{color:#000}
.v2-row.on{color:#000;font-weight:500}.v2-row.on .v2-org i{width:6px;margin-right:8px;transform:scale(1)}
.s-v2{display:flex;flex-direction:column}.v2{margin-bottom:28px}
.v2-out{margin-top:auto;padding:22px 24px;min-height:112px;border-radius:14px;background:#fafafa;box-shadow:inset 0 0 0 1px rgba(0,0,0,.05)}
.v2-p{display:none}.v2-p.on{display:block}
.v2-pk{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;color:#9a9a9a}
.v2-pt{margin-top:12px;font:600 16px/1.3 Inter,sans-serif}
.v2-ps{margin-top:6px;font:400 14px/1.55 Inter,sans-serif;color:#4d4d4d}

/* V3 accordion */
.v3-row{border-top:1px solid #ececec}
.v3-row:last-child{border-bottom:1px solid #ececec}
.v3-hd{display:grid;grid-template-columns:240px 1fr 40px;column-gap:32px;align-items:center;width:100%;padding:24px 0}
.v3-meta{display:flex;flex-direction:column;gap:6px}
.v3-org{font:500 14px/1.3 Inter,sans-serif;color:#141414}
.v3-yr{font:400 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a}
.v3-ttl{font:600 32px/1.1 Inter,sans-serif;letter-spacing:-.03em;color:#141414;transition:color .2s}
.v3-pm{position:relative;width:40px;height:40px;border-radius:50%;box-shadow:inset 0 0 0 1px #e0e0e0;transition:background-color .25s,box-shadow .25s,transform .35s cubic-bezier(.3,1.4,.5,1)}
.v3-pm i{position:absolute;left:13px;top:19.25px;width:14px;height:1.5px;border-radius:1px;background:#141414;transition:background-color .25s}
.v3-pm i + i{transform:rotate(90deg)}
.v3-hd:hover .v3-pm{box-shadow:inset 0 0 0 1px #000}
.v3-row.on .v3-pm{background:#000;box-shadow:inset 0 0 0 1px #000;transform:rotate(45deg)}
.v3-row.on .v3-pm i{background:#fff}
.v3-body{display:grid;grid-template-rows:0fr;visibility:hidden;transition:grid-template-rows .4s cubic-bezier(.2,.7,.2,1),visibility .4s}
.v3-row.on .v3-body{grid-template-rows:1fr;visibility:visible}
.v3-in{min-height:0;overflow:hidden}
.v3-grid{display:grid;grid-template-columns:240px 1fr 40px;column-gap:32px;padding:0 0 30px}
.v3-lg{display:grid;place-items:center;width:52px;height:52px;border-radius:14px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
.v3-p,.v3-ul{max-width:660px;font:400 17px/1.6 Inter,sans-serif;color:#4d4d4d}
.v3-ul{padding-left:20px}.v3-ul li{margin-bottom:4px}

/* V4 overlap chart */
.v4-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:28px}
.v4-h{font:600 18px/1.3 Inter,sans-serif;letter-spacing:-.01em}
.v4-leg{display:flex;gap:18px;font:500 12px/1 Inter,sans-serif;color:#666}
.v4-leg span{display:flex;align-items:center;gap:7px}
.sw{width:12px;height:12px;border-radius:3px}
.k-design.sw,.k-design .v4-bar{background:#141414;color:#fff}
.k-teach.sw,.k-teach .v4-bar{background:#0099ff;color:#fff}
.k-school.sw,.k-school .v4-bar{background:#dcdcdc;color:#141414}
.sw.now{width:2px;height:14px;border-radius:1px;background:#0099ff}
.v4-row.open .v4-bar{background:linear-gradient(90deg,#0099ff 55%,rgba(0,153,255,0))}
.v4-axis{display:grid;grid-template-columns:240px 1fr;height:24px;border-bottom:1px solid #e6e6e6}
.v4-ax{position:relative}
.v4-ax span{position:absolute;bottom:8px;padding-left:6px;font:400 11px/1 'IBM Plex Mono',ui-monospace,monospace;color:#9a9a9a;border-left:1px solid #e6e6e6;height:14px;line-height:14px;transform:translateY(8px);padding-bottom:8px}
.v4-rows{position:relative}
.v4-row{display:grid;grid-template-columns:240px 1fr;align-items:stretch;width:100%;height:50px;border-bottom:1px solid #f4f4f4;transition:background-color .2s}
.v4-row:hover{background:#fafafa}
.v4-lab{display:flex;flex-direction:column;justify-content:center;gap:3px;padding-right:16px;min-width:0}
.v4-lt{font:500 13.5px/1.2 Inter,sans-serif;color:#141414;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.v4-lo{font:400 12px/1.2 Inter,sans-serif;color:#9a9a9a}
.v4-row.on .v4-lt{font-weight:650}
.v4-trk{position:relative;background-image:linear-gradient(90deg,#f0f0f0 1px,transparent 1px);background-size:calc(100% / 13) 100%}
.v4-bar{position:absolute;top:13px;height:24px;border-radius:6px;display:flex;align-items:center;transition:box-shadow .25s,transform .25s}
.v4-row:hover .v4-bar{transform:translateY(-1px)}
.v4-row.on .v4-bar{box-shadow:0 0 0 2px #fff,0 0 0 4px #141414}
.v4-row.on.k-teach .v4-bar{box-shadow:0 0 0 2px #fff,0 0 0 4px #0099ff}
.v4-bl{padding:0 10px;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.04em;text-transform:uppercase;white-space:nowrap}
.v4-bl.out{position:absolute;left:100%;margin-left:6px;padding:0;color:#666}
.v4-today{position:absolute;top:-6px;bottom:0;width:2px;margin-left:-1px;background:#0099ff;pointer-events:none}
.v4-today b{position:absolute;top:-22px;left:50%;transform:translateX(-50%);padding:4px 7px;border-radius:6px;background:#e0f3ff;color:#0077cc;font:600 10px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase}
.v4-det{margin-top:24px;padding:20px 24px;border-radius:14px;background:#fafafa;box-shadow:inset 0 0 0 1px rgba(0,0,0,.05);min-height:84px}
.v4-dp{display:none;grid-template-columns:52px 1fr;column-gap:18px;align-items:start}.v4-dp.on{display:grid}
.v4-dl{display:grid;place-items:center;width:52px;height:52px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
.v4-dt{font:600 16px/1.3 Inter,sans-serif}.v4-dt span{font-weight:400;color:#7a7a7a}
.v4-ds{margin-top:6px;max-width:860px;font:400 14px/1.55 Inter,sans-serif;color:#4d4d4d}

/* V5 logo cards */
.v5{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-items:start}
.v5-c{border-radius:16px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08);overflow:hidden;transition:transform .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s}
.v5-c:hover{transform:translateY(-3px);box-shadow:inset 0 0 0 1px rgba(0,0,0,.08),0 14px 30px -16px rgba(0,0,0,.28)}
.v5-top{display:flex;flex-direction:column;justify-content:space-between;height:124px;padding:16px 18px 14px;box-sizing:border-box;background:var(--tint)}
.v5-tr{display:flex;justify-content:space-between;align-items:center;height:24px}
.v5-lg{display:grid;place-items:center;min-width:24px;height:24px}
.v5-lg .inv{filter:brightness(0) invert(1)}
.v5-c[style*="#141414"] .mk-2u{color:#fff}
.v5-now{padding:4px 7px;border-radius:999px;background:#fff;color:#0077cc;font:600 10px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase}
.v5-yr{font:700 40px/1 Inter,sans-serif;letter-spacing:-.04em;color:var(--ink)}
.v5-yr small.pre{margin:0 8px 0 0}
.v5-yr small{margin-left:8px;font:500 12px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.02em;text-transform:uppercase;opacity:.7}
.v5-bd{padding:16px 18px 14px}
.v5-ttl{font:600 15px/1.3 Inter,sans-serif;color:#141414}
.v5-org{margin-top:4px;font:400 13px/1.3 Inter,sans-serif;color:#7a7a7a}
.v5-sum{margin-top:12px;font:400 13.5px/1.5 Inter,sans-serif;color:#4d4d4d;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.v5-c.on .v5-sum{-webkit-line-clamp:unset;display:block}
.v5-more{display:inline-flex;align-items:center;gap:4px;margin-top:12px;font:500 13px/1 Inter,sans-serif;color:#0099ff}
.v5-more svg{transition:transform .25s}.v5-c.on .v5-more svg{transform:rotate(180deg)}
.v5-more:hover{color:#0077cc}
.v5-bd .nda.sm{display:flex;width:max-content}

/* V6 grouped by company */
.v6-g{display:grid;grid-template-columns:48px 1fr;column-gap:16px;padding:18px 0;border-top:1px solid #f0f0f0}
.v6-g:first-child{border-top:0;padding-top:0}
.v6-extra{display:none}.v6.more .v6-extra{display:grid}
.v6-lg{display:grid;place-items:center;width:48px;height:48px;border-radius:12px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
.v6-co{font:600 16px/1.3 Inter,sans-serif;color:#141414}
.v6-meta{margin-top:2px;font:400 13px/1.3 Inter,sans-serif;color:#9a9a9a}
.v6-r{margin-top:10px}
.v6-rt{font:500 14.5px/1.35 Inter,sans-serif;color:#141414}
.v6-rd{margin-top:2px;font:400 12.5px/1.3 Inter,sans-serif;color:#7a7a7a}
.v6-rs{margin-top:6px;font:400 13.5px/1.5 Inter,sans-serif;color:#4d4d4d;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.v6-tree{position:relative;margin-top:6px}
.v6-tree::before{content:"";position:absolute;left:4px;top:18px;bottom:44px;width:1px;background:#dcdcdc}
.v6-r.nest{position:relative;padding-left:22px;margin-top:12px}
.v6-r.nest::before{content:"";position:absolute;left:0;top:5px;width:9px;height:9px;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 1.5px #b3b3b3}
.v6-r.nest:first-child::before{background:#141414;box-shadow:none}
.v6-btn{display:flex;align-items:center;justify-content:center;gap:6px;width:100%;margin-top:6px;padding:14px 0;border-top:1px solid #f0f0f0 !important;font:500 14px/1 Inter,sans-serif !important;color:#141414}
.v6-btn:hover{background:#fafafa}
.v6-btn svg{transition:transform .25s}.v6-btn[aria-expanded="true"] svg{transform:rotate(180deg)}

/* V7 now and before */
.v7-hero{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:28px}
.v7-big{font:400 15px/1.3 Inter,sans-serif;color:#666}
.v7-big span{display:block;margin-bottom:2px;font:600 64px/.9 Caveat,cursive;color:#0099ff}
.v7{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:28px}
.v7 .nda{white-space:normal;line-height:1.3;border-radius:10px;align-items:flex-start}
.v7-h{display:flex;align-items:center;gap:7px;padding-bottom:10px;border-bottom:1px solid #e6e6e6;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#9a9a9a}
.live{width:7px;height:7px;border-radius:50%;background:#0099ff;box-shadow:0 0 0 3px #e0f3ff}
.v7-row{display:grid;grid-template-columns:30px 1fr;column-gap:12px;padding:14px 0;border-bottom:1px solid #f2f2f2;transition:opacity .3s}
.v7-lg{display:grid;place-items:center;height:20px}
.v7-lg .mk-lux{font-size:5.5px !important;letter-spacing:.1em}
.s-v7{display:flex;flex-direction:column}
.v7-skills{margin-top:auto;padding-top:32px}
.v7-skills .v7-h{margin-bottom:14px;border:0;padding:0}
.v7-t{font:500 14.5px/1.35 Inter,sans-serif;color:#141414}
.v7-o{margin-top:2px;font:400 12.5px/1.3 Inter,sans-serif;color:#7a7a7a}
.v7-s{margin-top:8px;font:400 13.5px/1.5 Inter,sans-serif;color:#4d4d4d}
.v7.f-design .v7-row:not(.k-design),.v7.f-teach .v7-row:not(.k-teach){opacity:.22}

/* V8 big type + photo preview */
.v8{display:grid;grid-template-columns:1fr 320px;gap:40px}
.v8-list{border-bottom:1px solid #ececec}
.v8-row{display:grid;grid-template-columns:44px 1fr 250px 116px;align-items:center;width:100%;height:76px;border-top:1px solid #ececec;color:#cfcfcf;transition:color .25s}
.v8-n{font:500 12px/1 'IBM Plex Mono',ui-monospace,monospace;color:inherit}
.v8-org{font:600 40px/1 Inter,sans-serif;letter-spacing:-.035em;white-space:nowrap;transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.v8-role{font:500 14px/1.3 Inter,sans-serif;padding-right:12px}
.v8-yr{text-align:right;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.05em;text-transform:uppercase}
.v8-row:hover{color:#7a7a7a}
.v8-row:not(.on) .v8-role,.v8-row:not(.on) .v8-yr,.v8-row:not(.on) .v8-n{color:#a6a6a6}
.v8-row.on{color:#000}.v8-row.on .v8-org{transform:translateX(8px)}.v8-row.on .v8-role{color:#666}
.v8-side{position:relative}
.v8-pv{transition:transform .55s cubic-bezier(.2,.8,.2,1)}
.v8-ph{position:relative;height:236px;border-radius:16px;overflow:hidden;background:#f0f0f0;box-shadow:0 18px 40px -20px rgba(0,0,0,.35)}
.v8-ph > img,.v8-ph > .v8-mark{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0;transform:scale(1.06);transition:opacity .35s,transform .6s cubic-bezier(.2,.7,.2,1)}
.v8-ph > .on{opacity:1;transform:none}
.v8-mark{display:grid;place-items:center;background:#141414}
.v8-mark.m-2u .mk-2u{color:#fff}
.v8-mark.m-lux{background:#f0f0f0}
.v8-cap{display:none;padding:16px 4px 0}.v8-cap.on{display:block}
.v8-ct{font:600 15px/1.3 Inter,sans-serif}
.v8-cs{margin-top:6px;font:400 13.5px/1.5 Inter,sans-serif;color:#4d4d4d}

/* V9 bento */
.v9{display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:212px 212px 236px auto;gap:12px}
.v9-t{position:relative;display:flex;flex-direction:column;justify-content:space-between;padding:22px;border-radius:18px;background:#f4f4f4;overflow:hidden;transition:transform .3s cubic-bezier(.2,.7,.2,1)}
.v9-t:hover{transform:translateY(-2px)}
.v9-t.ph{justify-content:flex-end;color:#fff;background:#1d1d1f}
.v9-t.ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.v9-t.ph:hover img{transform:scale(1.04)}
.v9-t.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(0,0,0,.55) 62%,rgba(0,0,0,.82))}
.v9-ov{text-shadow:0 1px 12px rgba(0,0,0,.35)}
.v9-ov{position:relative;z-index:1}
.v9-pill{display:inline-block;margin-bottom:12px;padding:5px 9px;border-radius:999px;background:rgba(255,255,255,.2);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);font:600 10px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase}
.v9-pill.gold{margin:12px 0 0;text-transform:none;font:500 12px/1 Inter,sans-serif;letter-spacing:0}
.v9-big{font:600 34px/1.05 Inter,sans-serif;letter-spacing:-.03em}
.v9-mid{font:600 18px/1.2 Inter,sans-serif;letter-spacing:-.01em}
.v9-sub{display:flex;align-items:center;gap:7px;margin-top:6px;font:400 13px/1.3 Inter,sans-serif;opacity:.85}
.v9-txt{margin-top:10px;max-width:440px;font:400 14px/1.5 Inter,sans-serif;opacity:.9}
.dk{color:#141414}.v9-sub.dk{color:#666;opacity:1}
.v9 .a{grid-column:1/3;grid-row:1/3}
.v9 .b{grid-column:3;grid-row:1;background:#e0f3ff;color:#0099ff;justify-content:flex-end}
.v9-num{font:600 120px/.8 Caveat,cursive}
.v9-yl{margin-top:8px;font:500 15px/1.3 Inter,sans-serif;color:#0077cc}
.v9 .c{grid-column:4;grid-row:1/3}
.v9 .d{grid-column:3;grid-row:2;background:#141414;color:#fff}
.mk-2u.big{font-size:30px;color:#fff}
.v9 .e{grid-column:1/3;grid-row:3;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08);justify-content:flex-start;gap:20px}
.v9-sfh{display:flex;justify-content:space-between;align-items:center}
.v9-sfn{display:flex;align-items:center;gap:12px}
.v9-sfl{display:grid;place-items:center;width:44px;height:44px;border-radius:12px;background:#e2f4fb}
.v9-sp{display:none}.v9-sp.on{display:block}
.v9-sr{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a}
.v9-st{margin-top:10px;max-width:520px;font:400 14.5px/1.55 Inter,sans-serif;color:#4d4d4d}
.v9-st.sm{margin-top:8px;font-size:13.5px}
.v9-mets{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:14px}
.v9-mets b{display:block;font:600 32px/1 Inter,sans-serif;letter-spacing:-.03em;color:#0a6f99}
.v9-mets span{display:block;margin-top:6px;font:400 12.5px/1.4 Inter,sans-serif;color:#666}
.v9 .f{grid-column:3;grid-row:3}
.v9 .g{grid-column:4;grid-row:3}
.v9 .s{grid-column:1/-1;grid-row:4;flex-direction:row;align-items:center;justify-content:flex-start;gap:20px;padding:18px 22px}
.v9-sk{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#9a9a9a}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{padding:8px 13px;border-radius:999px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08);font:500 13px/1 Inter,sans-serif;color:#141414}

/* V10 resume sheet */
.v10-bar{display:flex;align-items:center;justify-content:space-between;width:794px;margin:0 auto 16px}
.v10-file{display:flex;align-items:center;gap:8px;font:500 14px/1 Inter,sans-serif}
.v10-pg{padding:4px 7px;border-radius:6px;background:#e4e4e4;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;color:#666}
.v10-bar .seg{background:#e4e4e4}
.v10-act{display:flex;align-items:center;gap:12px}
.v10-note{font:400 12px/1.3 Inter,sans-serif;color:#9a9a9a}
.rv-root .v10-dl{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 15px;border-radius:999px;background:#000;color:#fff;font:500 13px/1 Inter,sans-serif;transition:background-color .2s,transform .2s}
.rv-root .v10-dl:hover{background:#333}.rv-root .v10-dl:active{transform:scale(.97)}
.v10-paper{width:794px;margin:0 auto;box-sizing:border-box;padding:56px 64px 48px;background:#fff;border-radius:4px;box-shadow:0 1px 2px rgba(0,0,0,.06),0 24px 50px -26px rgba(0,0,0,.28)}
.v10-hd{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:24px}
.v10-name{font:700 30px/1 Inter,sans-serif;letter-spacing:-.03em}
.v10-tag{margin-top:8px;font:400 14px/1.3 Inter,sans-serif;color:#666}
.v10-mono,.v10-sh,.v10-d{font:500 10.5px/1.3 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.07em;text-transform:uppercase;color:#9a9a9a}
.v10-sec{display:grid;grid-template-columns:110px 1fr;column-gap:24px;padding:20px 0;border-top:1px solid #ececec}
.v10-sh{padding-top:3px}
.v10-e{margin-bottom:16px}.v10-e:last-child{margin-bottom:0}
.v10-et{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.v10-et p{font:400 14px/1.4 Inter,sans-serif}.v10-et b{font-weight:600}.v10-et span{color:#7a7a7a}
.v10-d{flex:none}
.v10-es,.v10-ul{margin-top:4px;font:400 13px/1.55 Inter,sans-serif;color:#4d4d4d}
.v10-ul{padding-left:18px}
.v10-nda{font-style:italic;color:#7a7a7a}
.v10-sk{font:400 13.5px/1.5 Inter,sans-serif;color:#141414}
.v10-paper.compact .v10-es,.v10-paper.compact .v10-ul{display:none}
.v10-paper.compact .v10-e{margin-bottom:8px}

@media (prefers-reduced-motion: reduce){.rv-root *{transition:none !important}}
'''

JS = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.state = { t1: 0, l2: 0, a3: { 0: true }, g4: 0, c5: {}, s6: false, f7: 'all', h8: 0, b9: 0, m10: 'd' };
  }
  renderVals() {
    const st = this.state, v = {};
    const flip = (key, i) => () => { const o = Object.assign({}, this.state[key]); o[i] = !o[i]; this.setState({ [key]: o }); };
    for (let i = 0; i < 8; i++) {
      const o1 = st.t1 === i;
      v['t1c' + i] = o1 ? 'on' : ''; v['t1x' + i] = String(o1);
      v['t1f' + i] = () => this.setState({ t1: this.state.t1 === i ? -1 : i });
      const o2 = st.l2 === i;
      v['l2c' + i] = o2 ? 'on' : ''; v['l2x' + i] = String(o2);
      v['l2f' + i] = () => { if (this.state.l2 !== i) this.setState({ l2: i }); };
      const o3 = !!st.a3[i];
      v['a3c' + i] = o3 ? 'on' : ''; v['a3x' + i] = String(o3); v['a3f' + i] = flip('a3', i);
      const o4 = st.g4 === i;
      v['g4c' + i] = o4 ? 'on' : ''; v['g4x' + i] = String(o4);
      v['g4f' + i] = () => this.setState({ g4: i });
      const o5 = !!st.c5[i];
      v['c5c' + i] = o5 ? 'on' : ''; v['c5x' + i] = String(o5); v['c5f' + i] = flip('c5', i);
      const o8 = st.h8 === i;
      v['h8c' + i] = o8 ? 'on' : ''; v['h8x' + i] = String(o8);
      v['h8f' + i] = () => { if (this.state.h8 !== i) this.setState({ h8: i }); };
    }
    v.s6c = st.s6 ? 'more' : ''; v.s6x = String(st.s6);
    v.s6f = () => this.setState({ s6: !this.state.s6 });
    for (const k of ['all', 'design', 'teach']) {
      v['f7c' + k] = st.f7 === k ? 'on' : ''; v['f7x' + k] = String(st.f7 === k);
      v['f7f' + k] = () => this.setState({ f7: k });
    }
    v.f7cls = st.f7 === 'all' ? '' : 'f-' + st.f7;
    v.h8y = Math.min(st.h8 * 76, 200) + 'px';
    for (let i = 0; i < 3; i++) {
      v['b9c' + i] = st.b9 === i ? 'on' : ''; v['b9x' + i] = String(st.b9 === i);
      v['b9f' + i] = () => this.setState({ b9: i });
    }
    for (const k of ['d', 'c']) {
      v['m10c' + k] = st.m10 === k ? 'on' : ''; v['m10x' + k] = String(st.m10 === k);
      v['m10f' + k] = () => this.setState({ m10: k });
    }
    v.m10cls = st.m10 === 'c' ? 'compact' : '';
    return v;
  }
}'''
assert all(ord(c) < 128 for c in JS)

doc = f'''<!doctype html>
<html>
<head><meta charset="utf-8"><script src="./support.js"></script></head>
<body>
<!-- Resume / work history: 10 treatments (timeline, ledger, accordion, overlap chart, logo cards, grouped by company, now and before, big type with photo, bento, resume sheet) -->
<x-dc>
  <helmet>
    <style>
      html, body {{ margin: 0; height: 100%; }}
    </style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,400..700&amp;family=Caveat:wght@400;600&amp;family=IBM+Plex+Mono:wght@400;500;600&amp;display=swap">
<style>{CSS}</style>
  </helmet>
<div class="rv-root">{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{}}'>
{JS}
</script>
</body>
</html>
'''
assert all(ord(c) < 128 for c in doc), [c for c in doc if ord(c) >= 128][:5]
open(OUT, 'w').write(doc)
print('wrote', OUT, len(doc))
