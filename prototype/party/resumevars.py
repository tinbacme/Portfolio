"""Resume / work-history variations board for Tin Le's portfolio: V11 (recommended, research-backed) + 10 treatments.
Content pass after the 40-portfolio research: current role first, open ranges, years only, past roles muted,
one line of scope per role, Salesforce as one group with stacked titles, education as one closing line,
Resume (PDF) placeholder + LinkedIn links.
usage: python3 resumevars.py [out.dc.html]"""
import sys

S = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/'
OUT = sys.argv[1] if len(sys.argv) > 1 else S + 'canvas4/project/ResumeVariations.dc.html'


def h(s):
    """HTML text: non-ASCII as numeric entities."""
    return ''.join(c if ord(c) < 128 else f'&#{ord(c)};' for c in s)


UO, SF = '/_blob/00e0e1ec841a28c4e0055e4a6738e6b1', '/_blob/ac43d25c19be4e522f4bd492e1c090ab'
P_MS, P_UO, P_SF, P_GRAD = ('/_blob/effff208332abe411e27c82aaa87e30d', '/_blob/155942c7f1c522f9aec7d43d1c1d0d0d',
                            '/_blob/8bd998ead1110dbdb0a707cdb0cb6c60', '/_blob/54416d11bdc955c9c7fb45c9c479a828')
LINKEDIN = 'https://www.linkedin.com/in/letin08/'
NDA = 'Under NDA — happy to walk you through it'
NOW = 2026 + 10.5 / 12
SKILLS = ['UX research', 'Interaction design', 'Prototyping', 'Design systems', 'AI/search product design', 'Teaching']
SF_NUMS = '60% fewer support cases a month · 75K employees on a back-to-work app · 8+ Partner Community features · 12 product teams on C360'
SF_NUMS_SHORT = [('60%', 'fewer support cases a month on Salesforce Help'), ('75K', 'employees on the back-to-work app'),
                 ('8+', 'Partner Community features shipped'), ('12', 'product teams on my C360 components')]
EDU = dict(title='BS Industrial Design, Business minor', org='University of Oregon', dates='2014–2018',
           note='1st place overall, Quackhatch @UO 2018')

# newest / current first; Salesforce is one entry with its three titles stacked
R = [
    dict(k='ms', org='Microsoft AI', titles=['Senior Product Designer'], dates='2022–', y0=2022, y1=NOW, kind='design', now=True,
         logo='ms', photo=P_MS, yr='2022',
         scope='Search across Bing, Edge and Windows, and what AI agents could do in search.'),
    dict(k='uo', org='University of Oregon', titles=['Product Design Instructor'], dates='2023–', y0=2023, y1=NOW, kind='teach', now=True,
         logo='uo', photo=P_UO, yr='2023',
         scope='A 12-week course in UX research, UX/UI design and prototyping, at the school where I studied industrial design.'),
    dict(k='2u', org='2U', titles=['UX/UI Bootcamp Instructor'], dates='2021–', y0=2021, y1=NOW, kind='teach', now=True,
         logo='2u', photo=None, yr='2021',
         scope='24-week bootcamp cohorts with UO, UC Berkeley, Michigan, Minnesota, Utah and Arizona.'),
    dict(k='sf', org='Salesforce', titles=['Designer', 'Associate Designer', 'Summer UX Designer (intern)'],
         tyears=['2020–2022', '2018–2020', '2017'], dates='2017–2022', y0=2017.42, y1=2022, kind='design', now=False,
         logo='sf', photo=P_SF, yr='2017', yend='2022',
         segs=[(2017.42, 2017.67, ''), (2018, 2020, '2018–20'), (2020, 2022, '2020–22')],
         scope='Redesigned Salesforce Help search and content, built a back-to-work app, and added to the C360 design system.'),
    dict(k='lux', org='Luxium Lighting', titles=['Product Designer'], dates='2017', y0=2017.67, y1=2018, kind='design', now=False,
         logo='lux', photo=None, yr='2017',
         scope='An LED light from concept to working prototype.'),
]
N = len(R)
BY = {r['k']: r for r in R}


def T(r, sep=' · '): return h(sep.join(r['titles']))


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
DOC = ('<svg viewBox="0 0 16 16" width="16" height="16" aria-hidden="true"><path d="M4 1.5h5.5L13 5v9.5H4z" fill="#fff" stroke="#9a9a9a" stroke-width="1.2" '
       'stroke-linejoin="round"></path><path d="M9.5 1.5V5H13" fill="none" stroke="#9a9a9a" stroke-width="1.2"></path></svg>')
DOCSM = ('<svg viewBox="0 0 16 16" width="13" height="13" aria-hidden="true"><path d="M4 1.5h5.5L13 5v9.5H4z" fill="none" stroke="currentColor" '
         'stroke-width="1.3" stroke-linejoin="round"></path></svg>')


def nda(cls='nda'):
    return f'<span class="{cls}">{LOCK}{h(NDA)}</span>'


def extra(r, nda_cls='nda sm', nums_cls='nums'):
    """after the scope line: NDA chip for Microsoft, the short numbers line for Salesforce."""
    if r['k'] == 'ms': return nda(nda_cls)
    if r['k'] == 'sf': return f'<p class="{nums_cls}">{h(SF_NUMS)}</p>'
    return ''


def edu_line(cls=''):
    return (f'<p class="edu {cls}"><span class="edu-k">Education</span><span class="edu-t">{h(EDU["title"])} &#183; {h(EDU["org"])}'
            f' &#183; {h(EDU["note"])}</span><span class="edu-y">{h(EDU["dates"])}</span></p>')


def foot(cls=''):
    return (f'<div class="foot {cls}"><span class="lk-ph" title="Placeholder: no PDF is attached yet">{DOCSM}{h("Résumé (PDF)")}'
            f'<em>placeholder</em></span><a class="lk" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn<span aria-hidden="true"> &#8599;</span></a></div>')


# ---------------------------------------------------------------- V11 recommended
def v11():
    def row(r):
        return (f'<li class="v11-row{" now" if r["now"] else " past"}" tabindex="0"><span class="v11-org">{h(r["org"])}</span>'
                f'<span class="v11-role">{T(r)}</span><span class="v11-yr">{h(r["dates"])}</span>'
                f'<span class="v11-sc"><span class="v11-in">{h(r["scope"])}{extra(r, "nda sm", "nums")}</span></span></li>')
    grp = lambda lab, ks: f'<div class="v11-g"><p class="v11-gl">{lab}</p><ul class="v11-ul">{"".join(row(BY[k]) for k in ks)}</ul></div>'
    return (f'<p class="v11-hero">Senior Product Designer at Microsoft AI. <span>I also teach product design at the University of Oregon.</span></p>'
            f'<div class="v11-bar"><p class="mini-n">Experience</p><button class="v11-tg {{{{v11c}}}}" type="button" aria-pressed="{{{{v11x}}}}" '
            f'aria-controls="v11-list" onClick="{{{{v11f}}}}"><span class="sw-tr" aria-hidden="true"><i></i></span>Show all details</button></div>'
            f'<div class="v11 {{{{v11cls}}}}" id="v11-list">{grp("Design", ["ms", "sf", "lux"])}{grp("Teaching", ["uo", "2u"])}'
            f'<div class="v11-g"><p class="v11-gl">Education</p><p class="v11-edu"><span>{h(EDU["title"])}</span><span class="v11-eo">'
            f'{h(EDU["org"])} &#183; {h(EDU["note"])}</span><span class="v11-yr">{h(EDU["dates"])}</span></p></div></div>'
            + foot('v11-foot'))


# ---------------------------------------------------------------- V1 vertical timeline
def v1():
    items = ''
    for i, r in enumerate(R):
        sub = f'<span class="v1-prev">{T(r, "<br>")}</span>' if len(r['titles']) > 1 else ''
        if sub: sub = f'<span class="v1-prev">{" &#183; ".join(h(t) for t in r["titles"][1:])}</span>'
        items += (f'<li class="v1-it{" now" if r["now"] else " past"} {{{{t1c{i}}}}}"><span class="v1-dot" aria-hidden="true"></span>'
                  f'<button class="v1-hd" type="button" aria-expanded="{{{{t1x{i}}}}}" aria-controls="v1-p{i}" onClick="{{{{t1f{i}}}}}">'
                  f'<span class="v1-date">{h(r["dates"])}</span><span class="v1-role">{h(r["titles"][0])}{sub}</span>'
                  f'<span class="v1-org">{h(r["org"])}</span><span class="v1-chev">{CHEV}</span></button>'
                  f'<div class="v1-body" id="v1-p{i}"><div class="v1-in"><p>{h(r["scope"])}</p>{extra(r)}</div></div></li>')
    items += f'<li class="v1-it v1-end"><span class="v1-dot" aria-hidden="true"></span>{edu_line("v1-edu")}</li>'
    return f'<div class="mini-h"><span>Experience</span><span class="mini-n">9 years</span></div><ol class="v1">{items}</ol>' + foot()


# ---------------------------------------------------------------- V2 year ledger
def v2():
    rows = ''.join(
        f'<button class="v2-row{"" if r["now"] else " past"} {{{{l2c{i}}}}}" type="button" aria-pressed="{{{{l2x{i}}}}}" aria-controls="v2-out" '
        f'onClick="{{{{l2f{i}}}}}" onMouseEnter="{{{{l2f{i}}}}}"><span class="v2-org"><i aria-hidden="true"></i>{h(r["org"])}</span>'
        f'<span class="v2-role">{T(r, "<br>") if False else "<br>".join(h(t) for t in r["titles"])}</span><span class="v2-yr">{h(r["dates"])}</span></button>'
        for i, r in enumerate(R))
    rows += (f'<div class="v2-row v2-edu past"><span class="v2-org">{h(EDU["org"])}</span><span class="v2-role">BS Industrial Design,<br>Business minor</span>'
             f'<span class="v2-yr">{h(EDU["dates"])}</span></div>')
    panels = ''.join(
        f'<div class="v2-p {{{{l2c{i}}}}}"><p class="v2-pk">{i + 1:02d} / {N:02d}{" &#183; NOW" if r["now"] else ""}</p>'
        f'<p class="v2-pt">{h(r["org"])} <span>&#183; {T(r)}</span></p><p class="v2-ps">{h(r["scope"])}</p>{extra(r)}</div>' for i, r in enumerate(R))
    return (f'<div class="v2"><div class="v2-head" aria-hidden="true"><span>Org</span><span>Role</span><span class="v2-yr">Years</span></div>{rows}</div>'
            f'<div class="v2-out" id="v2-out" aria-live="polite">{panels}</div>' + foot())


# ---------------------------------------------------------------- V3 accordion
def v3():
    rows = ''
    for i, r in enumerate(R):
        sub = f'<span class="v3-sub">{"<br>".join(h(t) for t in r["titles"][1:])}</span>' if len(r['titles']) > 1 else ''
        rows += (f'<div class="v3-row{"" if r["now"] else " past"} {{{{a3c{i}}}}}"><button class="v3-hd" type="button" aria-expanded="{{{{a3x{i}}}}}" '
                 f'aria-controls="v3-p{i}" onClick="{{{{a3f{i}}}}}"><span class="v3-meta"><span class="v3-org">{h(r["org"])}</span>'
                 f'<span class="v3-yr">{h(r["dates"])}</span></span><span class="v3-ttl">{h(r["titles"][0])}{sub}</span>'
                 f'<span class="v3-pm" aria-hidden="true"><i></i><i></i></span></button>'
                 f'<div class="v3-body" id="v3-p{i}"><div class="v3-in"><div class="v3-grid"><span class="v3-lg">{logo(r["logo"], 22)}</span>'
                 f'<div class="v3-txt"><p class="v3-p">{h(r["scope"])}</p>{extra(r)}</div></div></div></div></div>')
    return f'<div class="v3">{rows}</div>' + edu_line('v3-edu') + foot()


# ---------------------------------------------------------------- V4 overlap chart
TRACK = 1008


def pct(y): return f'{(y - 2014) / 13 * 100:.3f}%'


def wpct(a, b): return f'{(b - a) / 13 * 100:.3f}%'


def v4():
    axis = ''.join(f'<span style="left: {pct(y)}">{y}</span>' for y in range(2014, 2027))
    rows = ''
    for i, r in enumerate(R):
        if r.get('segs'):
            bars = ''.join(f'<span class="v4-bar seg" style="left: {pct(a)}; width: {wpct(a, b)}">'
                           + (f'<span class="v4-bl">{h(lab)}</span>' if lab else '') + '</span>' for a, b, lab in r['segs'])
            lo = 'Designer · Associate · Intern'
        else:
            inside = (r['y1'] - r['y0']) / 13 * TRACK > 110
            bars = (f'<span class="v4-bar" style="left: {pct(r["y0"])}; width: {wpct(r["y0"], r["y1"])}">'
                    f'<span class="v4-bl{"" if inside else " out"}">{h(r["dates"])}</span></span>')
            lo = r['titles'][0]
        rows += (f'<button class="v4-row k-{r["kind"]}{"" if r["now"] else " past"} {{{{g4c{i}}}}}" type="button" aria-pressed="{{{{g4x{i}}}}}" '
                 f'aria-controls="v4-det" onClick="{{{{g4f{i}}}}}" aria-label="{h(r["org"])}, {T(r, ", ")}, {h(r["dates"])}">'
                 f'<span class="v4-lab"><span class="v4-lt">{h(r["org"])}</span><span class="v4-lo">{h(lo)}</span></span>'
                 f'<span class="v4-trk">{bars}</span></button>')
    det = ''.join(
        f'<div class="v4-dp {{{{g4c{i}}}}}"><span class="v4-dl">{logo(r["logo"], 22)}</span><div><p class="v4-dt">{h(r["org"])} '
        f'<span>&#183; {T(r)} &#183; {h(r["dates"])}</span></p><p class="v4-ds">{h(r["scope"])}</p>{extra(r)}</div></div>' for i, r in enumerate(R))
    legend = ('<div class="v4-leg"><span><i class="sw k-design"></i>Design</span><span><i class="sw k-teach"></i>Teaching</span>'
              '<span><i class="sw past"></i>Past</span><span><i class="sw now"></i>Today</span></div>')
    return (f'<div class="v4-top"><p class="v4-h">Teaching has run alongside design work since 2021.</p>{legend}</div>'
            f'<div class="v4"><div class="v4-axis" aria-hidden="true"><span class="v4-sp"></span><span class="v4-ax">{axis}</span></div>'
            f'<div class="v4-rows">{rows}<span class="v4-today" aria-hidden="true" style="left: calc(240px + (100% - 240px) * {(NOW - 2014) / 13:.4f})"><b>Today</b></span></div></div>'
            f'<div class="v4-det" id="v4-det" aria-live="polite">{det}</div>' + edu_line('v4-edu') + foot())


# ---------------------------------------------------------------- V5 logo cards
TINT = {'ms': ('#f3f3f3', '#141414'), 'uo': ('#e4f3eb', '#00743b'), '2u': ('#141414', '#ffffff'),
        'sf': ('#f4f4f4', '#b3b3b3'), 'lux': ('#f4f4f4', '#b3b3b3')}


def v5():
    cards = ''
    for i, r in enumerate(R):
        bg, ink = TINT[r['k']]
        lg = logo(r['logo'], 30 if r['k'] == 'lux' else 22, 'inv' if r['k'] == '2u' else '')
        tag = '<span class="v5-now">Now</span>' if r['now'] else ''
        yr = (f'{r["yr"]}<span class="dash">&#8211;</span>' if r['now'] else
              f'{r["yr"]}<small>&#8211;{r["yend"]}</small>' if r.get('yend') else r['yr'])
        ttl = '<br>'.join(h(t) for t in r['titles'])
        more = ''
        if r['k'] == 'sf':
            more = (f'<p class="nums v5-nums" id="v5-n">{h(SF_NUMS)}</p><button class="v5-more" type="button" aria-expanded="{{{{c5x}}}}" '
                    f'aria-controls="v5-n" onClick="{{{{c5f}}}}"><span class="t-off">Show the numbers</span><span class="t-on">Hide the numbers</span>{CHEV}</button>')
        cards += (f'<article class="v5-c{"" if r["now"] else " past"}{" sfc {{c5c}}" if r["k"] == "sf" else ""}" style="--tint: {bg}; --ink: {ink}">'
                  f'<div class="v5-top"><div class="v5-tr"><span class="v5-lg">{lg}</span>{tag}</div><p class="v5-yr">{yr}</p></div>'
                  f'<div class="v5-bd"><h3 class="v5-ttl">{ttl}</h3><p class="v5-org">{h(r["org"])}</p><p class="v5-sum">{h(r["scope"])}</p>'
                  + (nda('nda sm') if r['k'] == 'ms' else '') + more + '</div></article>')
    return f'<div class="v5">{cards}</div>' + edu_line('v5-edu')


# ---------------------------------------------------------------- V6 grouped by company
def v6():
    def g(r, hidden=False):
        if len(r['titles']) > 1:
            inner = ('<div class="v6-tree">' + ''.join(f'<div class="v6-r nest"><p class="v6-rt">{h(t)}</p><p class="v6-rd">{h(y)}</p></div>'
                                                      for t, y in zip(r['titles'], r['tyears'])) + '</div>')
            meta = f'{len(r["titles"])} roles · {r["dates"]}'
        else:
            inner = f'<p class="v6-rt">{h(r["titles"][0])}</p>'
            meta = r['dates']
        return (f'<div class="v6-g{"" if r["now"] else " past"}{" v6-extra" if hidden else ""}"><span class="v6-lg">{logo(r["logo"], 24)}</span><div>'
                f'<p class="v6-co">{h(r["org"])}</p><p class="v6-meta">{h(meta)}</p>{inner}<p class="v6-rs">{h(r["scope"])}</p>{extra(r)}</div></div>')
    out = ''.join(g(r, r['k'] == 'lux') for r in R)
    return (f'<div class="mini-h"><span>Experience</span><span class="mini-n">5 places</span></div>'
            f'<div class="v6 {{{{s6c}}}}" id="v6-list">{out}</div>'
            f'<button class="v6-btn" type="button" aria-expanded="{{{{s6x}}}}" aria-controls="v6-list" onClick="{{{{s6f}}}}">'
            f'<span class="t-off">Show 1 more</span><span class="t-on">Show less</span>{CHEV}</button>' + edu_line('v6-edu') + foot())


# ---------------------------------------------------------------- V7 now / before
def v7_row(r):
    return (f'<div class="v7-row k-{r["kind"]}"><span class="v7-lg">{logo(r["logo"], 16)}</span><div><p class="v7-t">{"<br>".join(h(t) for t in r["titles"])}</p>'
            f'<p class="v7-o">{h(r["org"])} &#183; {h(r["dates"])}</p><p class="v7-s">{h(r["scope"])}</p>{nda("nda sm") if r["k"] == "ms" else ""}</div></div>')


def v7():
    now = ''.join(v7_row(r) for r in R if r['now'])
    before = ''.join(v7_row(r) for r in R if not r['now'])
    seg = ''.join(f'<button type="button" class="{{{{f7c{k}}}}}" aria-pressed="{{{{f7x{k}}}}}" onClick="{{{{f7f{k}}}}}">{lab}</button>'
                  for k, lab in [('all', 'All'), ('design', 'Design'), ('teach', 'Teaching')])
    chips = ''.join(f'<span class="chip sm">{h(x)}</span>' for x in SKILLS)
    return (f'<div class="v7-hero"><p class="v7-big"><span>9 years</span> designing products</p>'
            f'<div class="seg v7-seg" role="group" aria-label="Filter roles">{seg}</div></div>'
            f'<div class="v7 {{{{f7cls}}}}"><div><p class="v7-h"><i class="live" aria-hidden="true"></i>Now</p>{now}</div>'
            f'<div class="v7-past"><p class="v7-h">Before</p>{before}</div></div>'
            + edu_line('v7-edu') +
            f'<div class="v7-skills"><p class="v7-sk">Skills</p><div class="chips">{chips}</div></div>' + foot())


# ---------------------------------------------------------------- V8 big type + photo preview
def v8():
    rows = ''.join(
        f'<button class="v8-row{" now" if r["now"] else " past"} {{{{h8c{i}}}}}" type="button" aria-pressed="{{{{h8x{i}}}}}" aria-controls="v8-pv" '
        f'onClick="{{{{h8f{i}}}}}" onMouseEnter="{{{{h8f{i}}}}}" onFocus="{{{{h8f{i}}}}}"><span class="v8-n">{i + 1:02d}</span>'
        f'<span class="v8-org">{h(r["org"])}</span><span class="v8-role">{"<br>".join(h(t) for t in r["titles"])}</span>'
        f'<span class="v8-yr">{h(r["dates"])}</span></button>' for i, r in enumerate(R))
    ph = ''
    for i, r in enumerate(R):
        if r['photo']:
            pos = ' style="object-position: 50% 30%"' if r['k'] in ('ms', 'uo') else ''
            ph += f'<img class="{{{{h8c{i}}}}}" src="{r["photo"]}" alt=""{pos}>'
        else:
            ph += f'<span class="v8-mark {{{{h8c{i}}}}} m-{r["k"]}">{logo(r["logo"], 64)}</span>'
    caps = ''.join(f'<div class="v8-cap {{{{h8c{i}}}}}"><p class="v8-ct">{T(r)}</p><p class="v8-cs">{h(r["scope"])}</p>{extra(r)}</div>'
                   for i, r in enumerate(R))
    return (f'<div class="v8"><div><div class="v8-list">{rows}</div>{edu_line("v8-edu")}{foot()}</div><div class="v8-side"><div class="v8-pv" id="v8-pv" aria-live="polite" '
            f'style="transform: translateY({{{{h8y}}}})"><div class="v8-ph">{ph}</div>{caps}</div></div></div>')


# ---------------------------------------------------------------- V9 bento
def v9():
    tabs = ''.join(f'<button type="button" class="{{{{b9c{i}}}}}" aria-pressed="{{{{b9x{i}}}}}" onClick="{{{{b9f{i}}}}}">{h(lab)}</button>'
                   for i, lab in enumerate(['Designer', 'Associate', 'Intern']))
    p0 = '<div class="v9-mets">' + ''.join(f'<div><b>{n}</b><span>{h(t)}</span></div>' for n, t in SF_NUMS_SHORT) + '</div>'
    panels = (f'<div class="v9-sp {{{{b9c0}}}}"><p class="v9-sr">Designer &#183; 2020&#8211;2022</p>{p0}</div>'
              f'<div class="v9-sp {{{{b9c1}}}}"><p class="v9-sr">Associate Designer &#183; 2018&#8211;2020</p>'
              f'<p class="v9-st">Mapped customer experiences and designed wireframe concepts with the Lightning Design System.</p></div>'
              f'<div class="v9-sp {{{{b9c2}}}}"><p class="v9-sr">Summer UX Designer (intern) &#183; 2017</p>'
              f'<p class="v9-st">First product design role: onboarding improvements and hackathon branding.</p></div>')
    chips = ''.join(f'<span class="chip sm">{h(s)}</span>' for s in SKILLS)
    return (f'<div class="v9">'
            f'<article class="v9-t ph a"><img src="{P_MS}" alt="" style="object-position: 50% 30%"><div class="v9-ov"><span class="v9-pill">Now</span>'
            f'<p class="v9-big">Senior Product Designer</p><p class="v9-sub">{ms_svg(14)} Microsoft AI &#183; 2022&#8211;</p>'
            f'<p class="v9-txt">{h(BY["ms"]["scope"])}</p>{nda("nda glass")}</div></article>'
            f'<article class="v9-t b"><p class="v9-num">9</p><p class="v9-yl">years designing products</p></article>'
            f'<article class="v9-t ph c"><img src="{P_UO}" alt="" style="object-position: 50% 35%"><div class="v9-ov"><span class="v9-pill">Now</span>'
            f'<p class="v9-mid">Product Design Instructor</p><p class="v9-sub">University of Oregon &#183; 2023&#8211;</p>'
            f'<p class="v9-txt">A 12-week course in UX research, UX/UI design and prototyping.</p></div></article>'
            f'<article class="v9-t d"><span class="mk-2u big">2U</span><div><p class="v9-mid">UX/UI Bootcamp Instructor</p>'
            f'<p class="v9-sub">2021&#8211; &#183; 24-week bootcamp cohorts</p><p class="v9-txt sm">With UO, UC Berkeley, Michigan, Minnesota, Utah and Arizona.</p></div></article>'
            f'<article class="v9-t e past"><div class="v9-sfh"><div class="v9-sfn"><span class="v9-sfl">{logo("sf", 22)}</span><div><p class="v9-mid dk">Salesforce</p>'
            f'<p class="v9-sub dk">3 roles &#183; 2017&#8211;2022</p></div></div><div class="seg" role="group" aria-label="Salesforce role">{tabs}</div></div>{panels}</article>'
            f'<article class="v9-t f past"><span class="mk-lux" style="font-size: 12px">LUXIUM</span><div><p class="v9-mid dk">Product Designer</p>'
            f'<p class="v9-sub dk">Luxium Lighting &#183; 2017</p><p class="v9-st sm">{h(BY["lux"]["scope"])}</p></div></article>'
            f'<article class="v9-t ph g"><img src="{P_GRAD}" alt=""><div class="v9-ov"><p class="v9-mid">BS Industrial Design, Business minor</p>'
            f'<p class="v9-sub">University of Oregon &#183; 2014&#8211;2018</p><span class="v9-pill gold">{h(EDU["note"])}</span></div></article>'
            f'<div class="v9-t s"><p class="v9-sk">Skills</p><div class="chips">{chips}</div>{foot("v9-foot")}</div>'
            f'</div>')


# ---------------------------------------------------------------- V10 resume sheet
def v10_entry(r):
    if len(r['titles']) > 1:
        head = (f'<div class="v10-et"><p><b>{h(r["org"])}</b></p><span class="v10-d">{h(r["dates"])}</span></div>'
                + ''.join(f'<div class="v10-et v10-sub"><p>{h(t)}</p><span class="v10-d">{h(y)}</span></div>' for t, y in zip(r['titles'], r['tyears'])))
    else:
        head = f'<div class="v10-et"><p><b>{h(r["titles"][0])}</b> <span>&#183; {h(r["org"])}</span></p><span class="v10-d">{h(r["dates"])}</span></div>'
    body = f'<p class="v10-es">{h(r["scope"])}</p>'
    if r['k'] == 'ms': body += f'<p class="v10-es v10-nda">{h(NDA)}</p>'
    if r['k'] == 'sf': body += f'<p class="v10-es v10-num">{h(SF_NUMS)}</p>'
    return f'<div class="v10-e{"" if r["now"] else " past"}">{head}{body}</div>'


def v10():
    sec = lambda t, inner: f'<section class="v10-sec"><h4 class="v10-sh">{t}</h4><div>{inner}</div></section>'
    seg = ''.join(f'<button type="button" class="{{{{m10c{k}}}}}" aria-pressed="{{{{m10x{k}}}}}" onClick="{{{{m10f{k}}}}}">{lab}</button>'
                  for k, lab in [('d', 'Detailed'), ('c', 'Compact')])
    edu = (f'<div class="v10-e past"><div class="v10-et"><p><b>{h(EDU["title"])}</b> <span>&#183; {h(EDU["org"])}</span></p>'
           f'<span class="v10-d">{h(EDU["dates"])}</span></div><p class="v10-es">{h(EDU["note"])}</p></div>')
    return (f'<div class="v10-bar"><p class="v10-file">{DOC}<span>Tin Le &#8212; {h("Résumé")}</span><span class="v10-pg">1 page</span></p>'
            f'<div class="seg" role="group" aria-label="{h("Résumé")} length">{seg}</div>'
            f'<div class="v10-act"><a class="lk" href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn<span aria-hidden="true"> &#8599;</span></a>'
            f'<button type="button" class="v10-dl" aria-disabled="true" title="Placeholder: no PDF is attached yet">{DOCSM}{h("Résumé (PDF)")}'
            f'<em>placeholder</em></button></div></div>'
            f'<div class="v10-paper {{{{m10cls}}}}"><header class="v10-hd"><div><p class="v10-name">Tin Le</p>'
            f'<p class="v10-tag">Senior Product Designer at Microsoft AI. I also teach product design at the University of Oregon.</p></div>'
            f'<span class="v10-mono">{h("Résumé")} &#183; 2026</span></header>'
            + sec('Design', ''.join(v10_entry(BY[k]) for k in ['ms', 'sf', 'lux']))
            + sec('Teaching', ''.join(v10_entry(BY[k]) for k in ['uo', '2u']))
            + sec('Education', edu)
            + sec('Skills', '<p class="v10-sk">' + h(' · '.join(SKILLS)) + '</p>')
            + '</div>')


# ================================================================ round 3: Awwwards / Codrops-inspired V12-V17
import json, math

SR = lambda txt: f'<span class="sr">{txt}</span>'


def plain_list():
    """static text version used under the playful variations."""
    li = ''.join(f'<li><b>{h(r["org"])}</b> &#183; {T(r, ", ")} <span>{h(r["dates"])}</span></li>' for r in R)
    li += f'<li><b>{h(EDU["title"])}</b> &#183; {h(EDU["org"])} <span>{h(EDU["dates"])}</span></li>'
    return f'<ul class="plain">{li}</ul>'


# ---------------------------------------------------------------- V12 terminal
T12_CMDS = [('whoami', 'whoami'), ('history', 'history'), ('teach', 'teach'), ('ls', 'ls ./microsoft-ai'), ('edu', 'cat education.txt')]
T12_OUT = {
    'whoami': 'Tin Le — Senior Product Designer at Microsoft AI.\nI also teach product design at the University of Oregon.\n9 years designing products.',
    'history': ('YEARS      ORG                   ROLE\n'
                '2022–      Microsoft AI          Senior Product Designer\n'
                '2023–      University of Oregon  Product Design Instructor\n'
                '2021–      2U                    UX/UI Bootcamp Instructor\n'
                '2017–2022  Salesforce            Designer\n'
                '                                 Associate Designer\n'
                '                                 Summer UX Designer (intern)\n'
                '2017       Luxium Lighting       Product Designer'),
    'teach': ('uo  Product Design Instructor, University of Oregon, 2023–\n'
              '    12-week course: UX research, UX/UI design, prototyping\n'
              '2u  UX/UI Bootcamp Instructor, 2U, 2021–\n'
              '    24-week cohorts with UO, UC Berkeley, Michigan,\n'
              '    Minnesota, Utah and Arizona'),
    'ls': ('scope.txt   Search across Bing, Edge and Windows, and what\n'
           '            AI agents could do in search.\n'
           'work/       [redacted — ask me in person]'),
    'edu': 'BS Industrial Design, Business minor\nUniversity of Oregon, 2014–2018\n1st place overall, Quackhatch @UO 2018',
}
T12_LABEL = dict(T12_CMDS)


def v12():
    chips = ''.join(f'<button type="button" class="v12-chip" onClick="{{{{t12f{k}}}}}">{lab}</button>' for k, lab in T12_CMDS)
    chips += '<button type="button" class="v12-chip ghost" onClick="{{t12fclear}}">clear</button>'
    return (f'<div class="v12"><div class="v12-bar" aria-hidden="true"><i></i><i></i><i></i><span>tin --history</span></div>'
            f'<div class="v12-scr" ref="{{{{r12}}}}"><pre class="v12-out" aria-hidden="true">{{{{t12vis}}}}<span class="v12-cur {{{{t12cur}}}}"></span></pre>'
            f'<div class="sr" aria-live="polite">{{{{t12sr}}}}</div></div>'
            f'<div class="v12-cmds" role="group" aria-label="Run a command"><span class="v12-ps" aria-hidden="true">$ tin</span>{chips}</div></div>'
            f'<details class="v12-det"><summary>Plain {h("résumé")} text</summary>{plain_list()}</details>' + foot())


# ---------------------------------------------------------------- V13 ask my resume
Q13 = [('What do you do at Microsoft?',
        'I\'m a Senior Product Designer at Microsoft AI, working on search across Bing, Edge and Windows, and what AI agents could do in search. '
        'The work is under NDA — happy to walk you through it in person.', [2, 1]),
       ('Where do you teach?',
        'At the University of Oregon since 2023: a 12-week course in UX research, UX/UI design and prototyping. Since 2021 I\'ve also led '
        '24-week UX/UI bootcamp cohorts with 2U, with UO, UC Berkeley, Michigan, Minnesota, Utah and Arizona.', [3, 0]),
       ('Biggest Salesforce win?',
        'Redesigning search and content for Salesforce Help, which cut support cases 60% a month. I also built a back-to-work app for 75K '
        'employees, shipped 8+ Partner Community features, and added components to the C360 design system across 12 product teams.', [4, 3]),
       ('Why industrial design?',
        'It\'s where I started: a BS in Industrial Design with a Business minor at the University of Oregon, 2014–2018 — sketching, CAD, '
        'rendering and prototyping by hand. I took 1st place overall at Quackhatch @UO 2018, and at Luxium Lighting I took an LED light '
        'from concept to working prototype.', [0, 2]),
       ('How did Salesforce start?',
        'As a Summer UX Designer intern in 2017: onboarding improvements and branding for a Salesforce hackathon. Then Associate Designer, '
        '2018–2020, and Designer, 2020–2022.', [1, 0])]


def v13():
    qa = ''.join(
        f'<div class="v13-qa {{{{q13c{i}}}}}" style="order: {{{{q13o{i}}}}}"><p class="v13-u">{h(q)}</p>'
        f'<p class="v13-a"><span aria-hidden="true">{{{{q13v{i}}}}}<span class="v13-cur {{{{q13cur{i}}}}}"></span></span>{SR(h(a))}</p></div>'
        for i, (q, a, _) in enumerate(Q13))
    chips = ''.join(f'<button type="button" class="v13-chip {{{{q13k{i}}}}}" onClick="{{{{q13f{i}}}}}">{h(q)}</button>' for i, (q, a, _) in enumerate(Q13))
    chips += '<button type="button" class="v13-chip ghost {{q13rk}}" onClick="{{q13r}}">Start over</button>'
    return (f'<div class="v13"><div class="v13-hd"><span class="v13-av" aria-hidden="true">t</span><div><p class="v13-n">Ask my {h("résumé")}</p>'
            f'<p class="v13-st">Pre-written answers from my {h("résumé")} &#183; no live AI</p></div></div>'
            f'<div class="v13-log" role="log" aria-live="polite" ref="{{{{r13}}}}"><div class="v13-qa on" style="order: 0"><p class="v13-a">Hi, I&#8217;m Tin. '
            f'Pick a question below and I&#8217;ll answer from my {h("résumé")}.</p></div>{qa}</div>'
            f'<div class="v13-chips" role="group" aria-label="Suggested questions">{chips}</div></div>' + foot())


# ---------------------------------------------------------------- V14 workbench
def v14_svg():
    ink, g1, g2, g3, acc, acc2 = '#141414', '#f4f4f4', '#e4e4e4', '#cfcfcf', '#0099ff', '#e0f3ff'
    desk = (f'<polygon points="40,230 380,90 720,230 380,370" fill="#ffffff" stroke="{ink}" stroke-width="1.5" stroke-linejoin="round"></polygon>'
            f'<polygon points="40,230 380,370 380,386 40,246" fill="{g2}" stroke="{ink}" stroke-width="1.5" stroke-linejoin="round"></polygon>'
            f'<polygon points="380,370 720,230 720,246 380,386" fill="{g3}" stroke="{ink}" stroke-width="1.5" stroke-linejoin="round"></polygon>'
            f'<path d="M56 252v80M380 386v66M704 252v80" stroke="{ink}" stroke-width="1.5" stroke-linecap="round"></path>')
    shadow = lambda cx, cy, rx, ry: f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="#000" opacity=".07"></ellipse>'
    o = []
    # 0 envelope (Microsoft, sealed)
    o.append(shadow(222, 268, 74, 20) +
             f'<polygon points="150,262 238,226 296,252 208,288" fill="#fff" stroke="{ink}" stroke-width="1.5" stroke-linejoin="round"></polygon>'
             f'<path d="M150 262l74 -6l14 -30M224 256l72 -4" fill="none" stroke="{ink}" stroke-width="1.2" stroke-linejoin="round"></path>'
             f'<circle cx="224" cy="256" r="12" fill="{acc}"></circle><text x="224" y="259" text-anchor="middle" font-family="IBM Plex Mono, monospace" '
             f'font-size="8" font-weight="600" fill="#fff">NDA</text>')
    # 1 chalkboard on easel + chalk (UO teaching)
    o.append(shadow(158, 222, 60, 12) +
             f'<path d="M120 222l22 -120M196 222l-22 -120M158 108v116" stroke="{ink}" stroke-width="1.5" stroke-linecap="round"></path>'
             f'<rect x="100" y="104" width="116" height="78" rx="4" fill="#2b2b2d" stroke="{ink}" stroke-width="1.5"></rect>'
             f'<path d="M114 122h40M114 134h62M114 146h30M168 160c8 -10 18 -10 26 0" stroke="#f4f4f4" stroke-width="2" stroke-linecap="round" fill="none" opacity=".85"></path>'
             f'<rect x="186" y="214" width="20" height="5" rx="2" fill="#fff" stroke="{ink}" stroke-width="1" transform="rotate(-18 196 216)"></rect>')
    # 2 laptop with cohort sticky notes (2U)
    notes = ''.join(f'<rect x="{x}" y="{y}" width="17" height="17" rx="2" fill="{c}" stroke="{acc}" stroke-width="1" transform="rotate({r} {x + 8} {y + 8})"></rect>'
                    for x, y, c, r in [(318, 98, acc2, -6), (340, 92, '#fff', 4), (362, 86, acc2, -3), (384, 80, '#fff', 6), (406, 74, acc2, -5), (428, 70, '#fff', 3)])
    o.append(shadow(392, 214, 92, 22) +
             f'<polygon points="312,196 446,142 446,72 312,126" fill="{ink}" stroke="{ink}" stroke-width="1.5" stroke-linejoin="round"></polygon>'
             f'<polygon points="320,186 438,138 438,82 320,130" fill="#3a3a3c"></polygon>'
             f'<polygon points="312,196 446,142 496,166 362,220" fill="{g1}" stroke="{ink}" stroke-width="1.5" stroke-linejoin="round"></polygon>'
             f'<polygon points="350,196 440,160 466,172 376,208" fill="{g2}"></polygon>' + notes)
    # 3 three stacked ID badges (Salesforce: three titles)
    badges = ''
    for j, (dx, dy, rot) in enumerate([(0, 0, -8), (14, -6, 0), (28, -12, 8)]):
        x, y = 556 + dx, 128 + dy
        top = acc if j == 2 else g3
        badges += (f'<g transform="rotate({rot} {x + 26} {y + 40})"><rect x="{x}" y="{y}" width="52" height="76" rx="6" fill="#fff" stroke="{ink}" stroke-width="1.4"></rect>'
                   f'<rect x="{x}" y="{y}" width="52" height="16" rx="6" fill="{top}"></rect><rect x="{x + 19}" y="{y + 4}" width="14" height="4" rx="2" fill="#fff"></rect>'
                   f'<circle cx="{x + 26}" cy="{y + 34}" r="9" fill="{g2}"></circle><path d="M{x + 12} {y + 54}h28M{x + 16} {y + 62}h20" stroke="{g3}" stroke-width="3" stroke-linecap="round"></path></g>')
    o.append(shadow(606, 224, 56, 12) + badges)
    # 4 foam model + marker (industrial design / Luxium)
    o.append(shadow(488, 316, 70, 16) +
             f'<polygon points="440,286 488,266 536,286 488,306" fill="#fff" stroke="{ink}" stroke-width="1.4" stroke-linejoin="round"></polygon>'
             f'<polygon points="440,286 488,306 488,338 440,318" fill="{g2}" stroke="{ink}" stroke-width="1.4" stroke-linejoin="round"></polygon>'
             f'<polygon points="488,306 536,286 536,318 488,338" fill="{g3}" stroke="{ink}" stroke-width="1.4" stroke-linejoin="round"></polygon>'
             f'<ellipse cx="488" cy="262" rx="18" ry="8" fill="#fff" stroke="{ink}" stroke-width="1.4"></ellipse>'
             f'<path d="M470 262v-26a18 8 0 0 0 36 0v26" fill="#fff" stroke="{ink}" stroke-width="1.4"></path>'
             f'<ellipse cx="488" cy="236" rx="18" ry="8" fill="{acc2}" stroke="{ink}" stroke-width="1.4"></ellipse>'
             f'<g transform="rotate(-24 560 330)"><rect x="530" y="324" width="66" height="11" rx="5" fill="#fff" stroke="{ink}" stroke-width="1.4"></rect>'
             f'<rect x="530" y="324" width="20" height="11" rx="5" fill="{ink}"></rect></g>')
    gs = ''.join(f'<g class="v14-o v14-o{i} {{{{w14c{i}}}}}">{s}</g>' for i, s in enumerate(o))
    return f'<svg class="v14-svg" viewBox="0 0 760 460" aria-hidden="true" focusable="false">{desk}{gs}</svg>'


W14 = [  # label, box (x, y, w, h) in svg units, role key
    ('Sealed NDA envelope', (146, 220, 156, 76), 'ms'),
    ('Chalkboard and chalk', (96, 96, 128, 132), 'uo'),
    ('Laptop with cohort notes', (306, 64, 194, 160), '2u'),
    ('Three badges', (548, 104, 112, 124), 'sf'),
    ('Marker and foam model', (436, 226, 168, 120), 'id'),
]


def v14():
    btns = ''
    for i, (lab, (x, y, w, hh), k) in enumerate(W14):
        st = f'left: {x / 7.6:.2f}%; top: {y / 4.6:.2f}%; width: {w / 7.6:.2f}%; height: {hh / 4.6:.2f}%'
        btns += (f'<button type="button" class="v14-b v14-b{i} {{{{w14c{i}}}}}" style="{st}" aria-pressed="{{{{w14x{i}}}}}" aria-controls="v14-card" '
                 f'onClick="{{{{w14f{i}}}}}"><span class="v14-lab">{h(lab)}</span></button>')
    cards = ''
    for i, (lab, _, k) in enumerate(W14):
        if k == 'id':
            body = (f'<p class="v14-k">Industrial design</p><p class="v14-t">{h(EDU["title"])}</p><p class="v14-or">{h(EDU["org"])} &#183; {h(EDU["dates"])}</p>'
                    f'<p class="v14-s">Sketching, CAD, rendering and prototyping by hand. {h(EDU["note"])}.</p>'
                    f'<p class="v14-t sm">Product Designer &#183; Luxium Lighting &#183; 2017</p><p class="v14-s">{h(BY["lux"]["scope"])}</p>')
        else:
            r = BY[k]
            kind = {'ms': 'Design &#183; now', 'uo': 'Teaching &#183; now', '2u': 'Teaching &#183; now', 'sf': 'Design &#183; past'}[k]
            body = (f'<p class="v14-k">{kind}</p><p class="v14-t">{"<br>".join(h(t) for t in r["titles"])}</p>'
                    f'<p class="v14-or">{h(r["org"])} &#183; {h(r["dates"])}</p><p class="v14-s">{h(r["scope"])}</p>{extra(r)}')
        cards += f'<div class="v14-cd {{{{w14c{i}}}}}"><p class="v14-obj">{h(lab)}</p>{body}</div>'
    return (f'<div class="v14"><div class="v14-scene">{v14_svg()}{btns}</div>'
            f'<div class="v14-side"><div id="v14-card" aria-live="polite">{cards}</div>'
            f'<details class="v12-det v14-det"><summary>Plain list</summary>{plain_list()}</details>{foot()}</div></div>')


# ---------------------------------------------------------------- V15 sketch -> render
SK_ICON = {
    'ms': '<path d="M14 22h52v36H14z M14 22l26 20l26 -20"></path><circle cx="40" cy="44" r="6"></circle>',
    'uo': '<path d="M12 16h56v38H12z M22 64l8 -10M58 64l-8 -10 M20 28h22M20 36h32M20 44h14"></path>',
    '2u': '<path d="M18 18h44v30H18z M10 56h60l-6 -8H16z M24 24h8v8h-8z M36 24h8v8h-8z M48 24h8v8h-8z"></path>',
    'sf': '<path d="M14 20h22v32H14z M30 16h22v32H30z M46 12h22v32H46z"></path>',
    'lux': '<path d="M40 14a14 14 0 0 1 8 26v8h-16v-8a14 14 0 0 1 8 -26z M34 54h12M36 60h8"></path>',
    'edu': '<path d="M40 14l24 12l-24 12l-24 -12z M16 26v24l24 12l24 -12v-24 M40 38v24"></path>',
}
SK_TINT = {'uo': '#e4f3eb', '2u': '#141414', 'sf': '#e2f4fb', 'lux': '#f6f2ea', 'edu': '#e4f3eb'}


def v15():
    items = [(r['k'], r) for r in R] + [('edu', None)]
    cards = ''
    for i, (k, r) in enumerate(items):
        if r:
            ttl = '<br>'.join(h(t) for t in r['titles']); org = f'{h(r["org"])} &#183; {h(r["dates"])}'; sc = h(r['scope']); lg = r['logo']
        else:
            ttl = h(EDU['title']); org = f'{h(EDU["org"])} &#183; {h(EDU["dates"])}'; sc = h(EDU['note']); lg = 'uo'
        icon = f'<svg viewBox="0 0 80 72" width="80" height="72" aria-hidden="true" fill="none" stroke="#3a3a3a" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{SK_ICON[k]}</svg>'
        sk = (f'<span class="v15-th sk">{icon}</span><span class="v15-t">{ttl}</span><span class="v15-o">{org}</span><span class="v15-s">{sc}</span>')
        if k == 'ms':
            cards += (f'<div class="v15-c ms"><span class="v15-sk">{sk}<span class="v15-note">NDA sketch &#8212; happy to walk you through it</span></span></div>')
            continue
        rd = (f'<span class="v15-th rd" style="background: {SK_TINT[k]}">{logo(lg, 30 if lg == "lux" else 26, "inv" if k == "2u" else "")}</span>'
              f'<span class="v15-t">{ttl}</span><span class="v15-o">{org}</span><span class="v15-s">{sc}</span>')
        cards += (f'<button type="button" class="v15-c{"" if (r and r["now"]) else " past"} {{{{r15c{i}}}}}" aria-pressed="{{{{r15x{i}}}}}" onClick="{{{{r15f{i}}}}}">'
                  f'<span class="v15-sk">{sk}</span><span class="v15-rd" aria-hidden="true">{rd}</span></button>')
    return (f'<div class="v15-top"><p class="v15-h">Marker sketch first, render on hover, focus or tap.</p>'
            f'<button type="button" class="v15-all {{{{all15c}}}}" aria-pressed="{{{{all15x}}}}" onClick="{{{{all15f}}}}">'
            f'<span class="t-off">Render all</span><span class="t-on">Back to sketch</span></button></div>'
            f'<div class="v15 {{{{all15cls}}}}">{cards}</div>' + foot())


# ---------------------------------------------------------------- V16 badge deck
B16_BACK = {
    'ms': 'Scope: search across Bing, Edge and Windows, and what AI agents could do in search. Under NDA — happy to walk you through it.',
    'uo': 'What I teach: a 12-week course in UX research, UX/UI design and prototyping, at the school where I studied industrial design.',
    '2u': '24-week cohorts in UX research, UX and UI design and front-end development, with UO, UC Berkeley, Michigan, Minnesota, Utah and Arizona.',
    'sf': '60% fewer support cases a month on Salesforce Help · a back-to-work app for 75K employees · 8+ Partner Community features · C360 components for 12 product teams.',
    'lux': 'An LED light from concept to working prototype: 3D CAD, studio product design, and testing with engineers.',
}


def v16():
    cards = ''
    for i, r in enumerate(R):
        k = r['k']
        band = {'ms': '#141414', 'uo': '#0099ff', '2u': '#0099ff'}.get(k, '#cfcfcf')
        front = (f'<div class="v16-face front"><span class="v16-slot" aria-hidden="true"></span><span class="v16-band" style="background: {band}"></span>'
                 f'<span class="v16-lg">{logo(r["logo"], 22) if k != "2u" else ""}</span><p class="v16-org">{h(r["org"])}</p><p class="v16-t">{"<br>".join(h(t) for t in r["titles"])}</p>'
                 f'<p class="v16-y">{h(r["dates"])}{" &#183; NOW" if r["now"] else ""}</p></div>')
        back = (f'<div class="v16-face back"><p class="v16-bk">{"Under NDA" if k == "ms" else "On the back"}</p><p class="v16-bt">{h(B16_BACK[k])}</p></div>')
        cards += (f'<div class="v16-card{"" if r["now"] else " past"} {{{{f16c{i}}}}}" style="--i: {i}; --a: {abs(i - 2)}; z-index: {N - i}">'
                  f'<div class="v16-in">{front}{back}</div><button type="button" class="v16-flip" aria-pressed="{{{{f16x{i}}}}}" onClick="{{{{f16f{i}}}}}">'
                  f'<span class="sr">{h(r["org"])}: </span>Flip</button></div>')
    return (f'<div class="v15-top"><p class="v15-h">Hover the stack, or fan it out; flip a badge for its back.</p>'
            f'<button type="button" class="v15-all {{{{fan16c}}}}" aria-pressed="{{{{fan16x}}}}" onClick="{{{{fan16f}}}}">'
            f'<span class="t-off">Fan out</span><span class="t-on">Stack</span></button></div>'
            f'<div class="v16-deck {{{{fan16cls}}}}">{cards}</div>' + edu_line('v16-edu') + foot())


# ---------------------------------------------------------------- V17 era dial
E17 = [
    dict(name='Industrial design student', years='2014–2018', bg='#f4efe6', ink='#3d3326', acc='#75582f', ang=-120,
         rows=[(EDU['title'], f'{EDU["org"]} · {EDU["dates"]}', f'Sketching, CAD, rendering and prototyping by hand. {EDU["note"]}.', ''),
               ('Product Designer', 'Luxium Lighting · 2017', BY['lux']['scope'], '')]),
    dict(name='Salesforce', years='2017–2022', bg='#e8efe9', ink='#23342a', acc='#3f5e4a', ang=-40,
         rows=[('Designer · Associate Designer · Summer UX Designer (intern)', 'Salesforce · 2017–2022', BY['sf']['scope'], 'sf')]),
    dict(name='Bootcamp instructor', years='2021–', bg='#eeeaf6', ink='#2e2740', acc='#5a4a8a', ang=40,
         rows=[('UX/UI Bootcamp Instructor', '2U · 2021–', BY['2u']['scope'], '')]),
    dict(name='Microsoft AI + UO teaching', years='2022– / 2023–', bg='#e0f3ff', ink='#0b2b40', acc='#0069b4', ang=120,
         rows=[('Senior Product Designer', 'Microsoft AI · 2022–', BY['ms']['scope'], 'ms'),
               ('Product Design Instructor', 'University of Oregon · 2023–', BY['uo']['scope'], '')]),
]


def v17():
    ticks = ''
    for j, e in enumerate(E17):
        a = math.radians(e['ang']); x, y = 50 + 62 * math.sin(a), 50 - 62 * math.cos(a)
        ticks += f'<span class="v17-lb {{{{e17c{j}}}}}" style="left: {x:.1f}%; top: {y:.1f}%">{e["years"][:4]}</span>'
        tx, ty = 50 + 44 * math.sin(a), 50 - 44 * math.cos(a)
        ticks += f'<i class="v17-tk" style="left: {tx:.1f}%; top: {ty:.1f}%; transform: translate(-50%, -50%) rotate({e["ang"]}deg)"></i>'
    lst = ''.join(f'<button type="button" class="{{{{e17c{j}}}}}" aria-pressed="{{{{e17x{j}}}}}" onClick="{{{{e17f{j}}}}}"><b>{h(e["years"])}</b> {h(e["name"])}</button>'
                  for j, e in enumerate(E17))
    panels = ''
    for j, e in enumerate(E17):
        rows = ''.join(f'<div class="v17-r"><p class="v17-rt">{h(t)}</p><p class="v17-ro">{h(o)}</p><p class="v17-rs">{h(s)}</p>'
                       + (nda('nda sm') if x == 'ms' else f'<p class="nums">{h(SF_NUMS)}</p>' if x == 'sf' else '') + '</div>'
                       for t, o, s, x in e['rows'])
        panels += f'<div class="v17-p {{{{e17c{j}}}}}"><p class="v17-era">Era {j + 1} of 4</p><p class="v17-n">{h(e["name"])}</p><p class="v17-y">{h(e["years"])}</p>{rows}</div>'
    return (f'<div class="v17" style="--bg: {{{{e17bg}}}}; --ink: {{{{e17ink}}}}; --acc: {{{{e17acc}}}}">'
            f'<div class="v17-dial"><div class="v17-ring">{ticks}'
            f'<div class="v17-knob" role="slider" tabindex="0" aria-label="Career era" aria-valuemin="0" aria-valuemax="3" aria-valuenow="{{{{e17}}}}" '
            f'aria-valuetext="{{{{e17t}}}}" onKeyDown="{{{{e17k}}}}" onPointerDown="{{{{e17pd}}}}" onPointerMove="{{{{e17pm}}}}" onPointerUp="{{{{e17pu}}}}" '
            f'onPointerCancel="{{{{e17pu}}}}" style="transform: rotate({{{{e17a}}}})"><i class="v17-ptr"></i></div></div>'
            f'<p class="v17-hint">Drag the knob, or use the arrow keys</p><div class="v17-list" role="group" aria-label="Eras">{lst}</div></div>'
            f'<div class="v17-panel" aria-live="polite">{panels}{foot("v17-foot")}</div></div>')


JS_DATA = json.dumps({
    't12': {k: dict(cmd=T12_LABEL[k], out=T12_OUT[k]) for k in T12_OUT},
    'q13': [dict(a=a, f=f) for q, a, f in Q13],
    'e17': [dict(t=f'{e["years"]}: {e["name"]}', bg=e['bg'], ink=e['ink'], acc=e['acc'], ang=e['ang']) for e in E17],
}, ensure_ascii=True)


# ---------------------------------------------------------------- assemble
SECS = [
    ('V11', 'Recommended', 'Based on research across 40 designer portfolios (daneden.me, davidhoang.com, jonyablonski.com, haydenbleasel.com, tarng.com…): '
     'a two-sentence hero, then a compact ledger in two groups so the overlapping dates read clearly. Hover a row for its one line of scope.', v11, True, ''),
    ('V1', 'Vertical timeline', 'Inspired by Grok on Mobbin: small dot markers on a thin line, mono dates. Click a role to open its one line of scope; current roles get a blue dot, past ones go gray.', v1, False, ''),
    ('V2', 'Year ledger', 'Inspired by Aino Agency on Mobbin: one mono, all-caps table with years right-aligned. Current roles black, past ones gray; hover or click a row to read it below.', v2, False, ''),
    ('V3', 'Accordion rows', 'Inspired by YLLW on Mobbin: org and years small on the left, the role big in the middle, a plus to open. Salesforce is one row with its titles stacked.', v3, True, ''),
    ('V4', 'Overlap chart', 'Inspired by the Plane timeline view on Mobbin: every place as a bar on one year axis, so teaching overlapping Microsoft is plain to see. Salesforce is one row of three segments.', v4, True, ''),
    ('V5', 'Logo cards', 'Inspired by Revolut on Mobbin: a tinted top with the logo and a big start year, then the role and one line of scope. Past places go gray.', v5, True, ''),
    ('V6', 'Grouped by company', 'Inspired by Upwork profiles on Mobbin: one entry per place, with the three Salesforce titles stacked on a line. The oldest entry hides behind Show more.', v6, False, ''),
    ('V7', 'Now and before', 'Inspired by Customer.io on Mobbin: a big handwritten number beside two plain columns. The filter dims roles that are not design or teaching.', v7, False, ''),
    ('V8', 'Big type, photo preview', 'Inspired by Locomotive on Mobbin: huge org names that go black on hover, with a photo card sliding to the row you are on.', v8, True, ''),
    ('V9', 'Bento grid', 'Inspired by Analogue Agency on Mobbin: photos, roles, a big number and a small skills strip in one grid. The Salesforce tile switches between its three titles.', v9, True, ''),
    ('V10', 'Resume sheet', 'Inspired by the Square client view on Mobbin: a printable page on gray with a length toggle, LinkedIn, and a R&#233;sum&#233; (PDF) placeholder that is not wired up yet.', v10, True, 'st-gray'),
    ('V12', 'tin --history', "Inspired by Vlad Burca's CLI portfolio and the 1-bit Pixel Art Dev Portfolio on Awwwards: command chips print a short answer, and ls ./microsoft-ai stays redacted.", v12, False, ''),
    ('V13', 'Ask my résumé', "Inspired by My Ha's Portfolio and the Conversational AI Portfolio on Awwwards: suggested questions with pre-written answers and follow-ups. No live AI.", v13, False, ''),
    ('V14', 'Workbench', 'Inspired by ULTRAGRID on Awwwards (making-of on Codrops): a flat isometric desk where each object opens a chapter. The Microsoft envelope stays sealed.', v14, True, ''),
    ('V15', 'Sketch to render', "Inspired by Codrops' Sketching the impossible and Mr. Pandas Paper Portfolio on Awwwards: cards start as marker sketches and render in color. Microsoft stays a sketch.", v15, True, ''),
    ('V16', 'Badge deck', "Inspired by Eduard Bodak's card flip (Awwwards, Codrops) and Carl Gordon's stacking cards: ID badges that fan out and flip to an NDA-safe back.", v16, True, ''),
    ('V17', 'Era dial', "Inspired by Brandon Yasin (Codrops) and Future Record's rotary knobs on Awwwards: turn the dial through four eras; the panel re-tints and shows that era's roles.", v17, True, ''),
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
.rv-s{margin:6px 0 0;max-width:820px;font:400 14px/1.45 Inter,sans-serif;color:#7a7a7a}
.rv-sec:not(.rv-full) .rv-s{min-height:40px}
.rv-stage{position:relative;flex:1;margin-top:20px;padding:40px;border-radius:20px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06);overflow:hidden}
.rv-stage.st-gray{background:#f0f0f0}
:where(.rv-root) :where(p,h3,h4,ul,ol){margin:0}
.rv-root :where(button){font:inherit;color:inherit;background:none;border:0;padding:0;margin:0;text-align:left;cursor:pointer;-webkit-tap-highlight-color:transparent}
.rv-root button:focus-visible,.rv-root a:focus-visible,.rv-root [tabindex]:focus-visible{outline:2px solid #0099ff;outline-offset:2px;border-radius:10px}
.rv-root img{display:block}
.mk-2u{font:700 13px/1 Inter,system-ui,sans-serif;letter-spacing:-.03em;color:#141414}
.mk-lux{font:600 10px/1 Inter,sans-serif;letter-spacing:.22em;color:#141414}
.t-on{display:none}
[aria-expanded="true"] > .t-on{display:inline}[aria-expanded="true"] > .t-off{display:none}
.nda{display:inline-flex;align-items:center;gap:6px;margin-top:12px;padding:7px 11px;border-radius:999px;background:#f0f0f0;font:500 12px/1 Inter,sans-serif;color:#4d4d4d;white-space:nowrap}
.nda.sm{margin-top:8px;padding:5px 9px;font-size:11.5px}
.nda.glass{background:rgba(255,255,255,.18);color:#fff;-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px)}
.nums{margin-top:8px;font:500 11px/1.5 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.02em;color:#7a7a7a}
.mini-h{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:20px;font:600 15px/1 Inter,sans-serif}
.mini-n{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a}
.seg{display:inline-flex;padding:3px;border-radius:999px;background:#f0f0f0}
.seg button{padding:7px 13px;border-radius:999px;font:500 13px/1 Inter,sans-serif;color:#666;transition:color .2s,background-color .2s,box-shadow .2s}
.seg button:hover{color:#000}
.seg button.on{background:#fff;color:#000;box-shadow:0 1px 2px rgba(0,0,0,.1),0 0 0 1px rgba(0,0,0,.04)}
.edu{display:flex;align-items:baseline;gap:14px;margin-top:20px;font:400 13.5px/1.5 Inter,sans-serif;color:#7a7a7a}
.edu-k{flex:none;font:500 10.5px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#b3b3b3}
.edu-t{flex:1;min-width:0}
.edu-y{flex:none;margin-left:auto;font:400 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.04em;color:#9a9a9a;font-variant-numeric:tabular-nums}
.foot{display:flex;align-items:center;gap:22px;margin-top:20px;padding-top:16px;border-top:1px solid #f0f0f0;font:500 13px/1 Inter,sans-serif}
.lk{color:#141414;text-decoration:none;padding-bottom:2px;border-bottom:1px solid #d6d6d6;transition:border-color .2s}
.lk:hover{border-color:#141414}
.lk-ph{display:inline-flex;align-items:center;gap:6px;color:#9a9a9a;cursor:not-allowed}
.lk-ph em,.v10-dl em{font:500 9.5px/1 'IBM Plex Mono',ui-monospace,monospace;font-style:normal;letter-spacing:.06em;text-transform:uppercase;padding:3px 5px;border-radius:5px;background:#f0f0f0;color:#9a9a9a}
.chip{padding:8px 13px;border-radius:999px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08);font:500 13px/1 Inter,sans-serif;color:#141414}
.chip.sm{padding:5px 9px;font:400 11.5px/1 Inter,sans-serif;color:#666}
.chips{display:flex;flex-wrap:wrap;gap:6px}

/* V11 recommended */
.s-v11{padding:56px 64px 44px}
.v11-hero{max-width:900px;font:600 34px/1.2 Inter,sans-serif;letter-spacing:-.03em;color:#141414}
.v11-hero span{color:#9a9a9a}
.v11-bar{display:flex;justify-content:space-between;align-items:center;margin:44px 0 6px}
.v11-tg{display:inline-flex;align-items:center;gap:8px;font:500 12.5px/1 Inter,sans-serif !important;color:#666}
.v11-tg:hover{color:#000}
.sw-tr{position:relative;width:26px;height:16px;border-radius:999px;background:#e4e4e4;transition:background-color .2s}
.sw-tr i{position:absolute;left:2px;top:2px;width:12px;height:12px;border-radius:50%;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.2);transition:transform .25s cubic-bezier(.3,1.4,.5,1)}
.v11-tg.on{color:#000}.v11-tg.on .sw-tr{background:#0099ff}.v11-tg.on .sw-tr i{transform:translateX(10px)}
.v11-g{display:grid;grid-template-columns:150px 1fr;border-top:1px solid #e6e6e6;padding:6px 0}
.v11-gl{padding-top:16px;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#9a9a9a}
.v11-ul{list-style:none;padding:0}
.v11-row{display:grid;grid-template-columns:220px 1fr 120px;column-gap:24px;padding:12px 12px;margin:0 -12px;border-radius:10px;outline-offset:0 !important;transition:background-color .2s}
.v11-row + .v11-row{border-top:1px solid #f4f4f4}
.v11-row:hover{background:#fafafa}
.v11-org{font:500 15.5px/1.45 Inter,sans-serif;color:#141414}
.v11-role{font:400 15.5px/1.45 Inter,sans-serif;color:#4d4d4d}
.v11-yr{text-align:right;font:400 12.5px/1.9 'IBM Plex Mono',ui-monospace,monospace;color:#141414;font-variant-numeric:tabular-nums}
.v11-row.past .v11-org,.v11-row.past .v11-role,.v11-row.past .v11-yr{color:#a6a6a6}
.v11-sc{grid-column:2/4;display:grid;grid-template-rows:0fr;opacity:0;transition:grid-template-rows .3s cubic-bezier(.2,.7,.2,1),opacity .25s}
.v11-in{min-height:0;overflow:hidden;padding-top:0;font:400 14px/1.5 Inter,sans-serif;color:#666;transition:padding .3s}
.v11-row:hover .v11-sc,.v11-row:focus .v11-sc,.v11-row:focus-within .v11-sc,.v11.all .v11-sc{grid-template-rows:1fr;opacity:1}
.v11-row:hover .v11-in,.v11-row:focus .v11-in,.v11-row:focus-within .v11-in,.v11.all .v11-in{padding-top:4px}
@media (hover: none){.v11-sc{grid-template-rows:1fr;opacity:1}.v11-in{padding-top:4px}}
.v11-in .nda{margin-left:10px;margin-top:0;vertical-align:1px}
.v11-in .nums{margin-top:4px}
.v11-edu{display:grid;grid-template-columns:220px 1fr 120px;column-gap:24px;padding:12px 0;font:400 15.5px/1.45 Inter,sans-serif;color:#a6a6a6}
.v11-edu span:first-child{grid-column:1/3;color:#7a7a7a}
.v11-eo{grid-column:1/3;grid-row:2;font-size:14px}
.v11-edu .v11-yr{grid-column:3;grid-row:1;color:#a6a6a6}
.v11-foot{margin-top:8px}

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
.v1-prev{display:block;margin-top:2px;font:500 14px/1.4 Inter,sans-serif;color:#9a9a9a}
.v1-it.past .v1-role{color:#7a7a7a}
.v1-it.past.on .v1-role,.v1-it.past .v1-hd:hover .v1-role{color:#141414}
.v1-org{grid-column:1;font:400 14px/1.4 Inter,sans-serif;color:#7a7a7a}
.v1-chev{grid-column:2;grid-row:2/4;align-self:center;display:grid;place-items:center;width:28px;height:28px;border-radius:50%;color:#9a9a9a;transition:transform .3s,color .2s}
.v1-hd:hover .v1-chev{color:#000}
.v1-it.on .v1-chev{transform:rotate(180deg);color:#000}
.v1-body{display:grid;grid-template-rows:0fr;visibility:hidden;transition:grid-template-rows .35s cubic-bezier(.2,.7,.2,1),visibility .35s}
.v1-it.on .v1-body{grid-template-rows:1fr;visibility:visible}
.v1-in{min-height:0;overflow:hidden}
.v1-in p{max-width:470px;font:400 14px/1.55 Inter,sans-serif;color:#4d4d4d}
.v1-it.on .v1-in{padding-bottom:14px}
.v1-end .v1-dot{top:22px;box-shadow:inset 0 0 0 1.5px #dcdcdc}
.v1-edu{margin:0;padding:18px 0 4px;flex-wrap:wrap;row-gap:6px}

/* V2 year ledger */
.s-v2{display:flex;flex-direction:column}
.v2{margin-bottom:28px;font:400 12px/1.5 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.04em;text-transform:uppercase}
.v2-head,.v2-row{display:grid;grid-template-columns:160px 1fr 104px;column-gap:16px;align-items:start}
.v2-head{padding:0 0 12px;color:#b3b3b3;border-bottom:1px solid #e6e6e6}
.v2-row{width:100%;padding:16px 0;text-transform:inherit;letter-spacing:inherit;border-bottom:1px solid #f2f2f2;color:#000;transition:color .2s}
.v2-row.past{color:#b3b3b3}
.v2-org{display:flex;align-items:center;white-space:nowrap}
.v2-org i{flex:none;width:0;height:6px;margin-right:0;border-radius:50%;background:currentColor;transform:scale(0);transition:transform .25s cubic-bezier(.3,1.6,.5,1),width .25s,margin .25s}
.v2-yr{text-align:right;font-variant-numeric:tabular-nums}
.v2-row:hover{color:#000}
.v2-row.on{color:#000;font-weight:500}.v2-row.on .v2-org i{width:6px;margin-right:8px;transform:scale(1)}
.v2-edu{cursor:default;border-bottom:0;color:#c4c4c4 !important}
.v2-out{margin-top:auto;padding:22px 24px;min-height:120px;border-radius:14px;background:#fafafa;box-shadow:inset 0 0 0 1px rgba(0,0,0,.05)}
.v2-p{display:none}.v2-p.on{display:block}
.v2-pk{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;color:#9a9a9a}
.v2-pt{margin-top:12px;font:600 16px/1.3 Inter,sans-serif}
.v2-pt span{font-weight:400;color:#7a7a7a}
.v2-ps{margin-top:6px;font:400 14px/1.55 Inter,sans-serif;color:#4d4d4d}

/* V3 accordion */
.v3-row{border-top:1px solid #ececec}
.v3-row:last-child{border-bottom:1px solid #ececec}
.v3-hd{display:grid;grid-template-columns:240px 1fr 40px;column-gap:32px;align-items:center;width:100%;padding:24px 0}
.v3-meta{display:flex;flex-direction:column;gap:6px}
.v3-org{font:500 14px/1.3 Inter,sans-serif;color:#141414}
.v3-yr{font:400 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a}
.v3-ttl{font:600 32px/1.1 Inter,sans-serif;letter-spacing:-.03em;color:#141414;transition:color .2s}
.v3-sub{display:block;margin-top:8px;font:500 16px/1.45 Inter,sans-serif;letter-spacing:-.01em;color:#b3b3b3}
.v3-row.past .v3-ttl,.v3-row.past .v3-org{color:#a6a6a6}
.v3-row.past .v3-hd:hover .v3-ttl,.v3-row.past.on .v3-ttl,.v3-row.past.on .v3-org{color:#141414}
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
.v3-p{max-width:660px;font:400 17px/1.6 Inter,sans-serif;color:#4d4d4d}
.v3-edu{padding-top:22px;padding-left:272px}.v3-edu .edu-k{margin-left:-272px;width:258px}

/* V4 overlap chart */
.v4-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:28px}
.v4-h{font:600 18px/1.3 Inter,sans-serif;letter-spacing:-.01em}
.v4-leg{display:flex;gap:18px;font:500 12px/1 Inter,sans-serif;color:#666}
.v4-leg span{display:flex;align-items:center;gap:7px}
.sw{width:12px;height:12px;border-radius:3px}
.k-design.sw,.k-design .v4-bar{background:#141414;color:#fff}
.k-teach.sw,.k-teach .v4-bar{background:#0099ff;color:#fff}
.sw.past{background:#c4c4c4}
.past .v4-bar{background:#c4c4c4;color:#141414}
.sw.now{width:2px;height:14px;border-radius:1px;background:#0099ff}
.v4-axis{display:grid;grid-template-columns:240px 1fr;height:24px;border-bottom:1px solid #e6e6e6}
.v4-ax{position:relative}
.v4-ax span{position:absolute;bottom:8px;padding-left:6px;font:400 11px/1 'IBM Plex Mono',ui-monospace,monospace;color:#9a9a9a;border-left:1px solid #e6e6e6;height:14px;line-height:14px;transform:translateY(8px);padding-bottom:8px}
.v4-rows{position:relative}
.v4-row{display:grid;grid-template-columns:240px 1fr;align-items:stretch;width:100%;height:56px;border-bottom:1px solid #f4f4f4;transition:background-color .2s}
.v4-row:hover{background:#fafafa}
.v4-lab{display:flex;flex-direction:column;justify-content:center;gap:3px;padding-right:16px;min-width:0}
.v4-lt{font:500 14px/1.2 Inter,sans-serif;color:#141414;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.v4-lo{font:400 12px/1.2 Inter,sans-serif;color:#9a9a9a;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.v4-row.past .v4-lt{color:#7a7a7a}
.v4-row.on .v4-lt{font-weight:650;color:#141414}
.v4-trk{position:relative;background-image:linear-gradient(90deg,#f0f0f0 1px,transparent 1px);background-size:calc(100% / 13) 100%}
.v4-bar{position:absolute;top:16px;height:24px;border-radius:6px;display:flex;align-items:center;transition:box-shadow .25s,transform .25s,background-color .25s}
.v4-bar.seg + .v4-bar.seg{box-shadow:inset 2px 0 0 #fff}
.v4-row:hover .v4-bar{transform:translateY(-1px)}
.v4-row.on .v4-bar{box-shadow:0 0 0 2px #fff,0 0 0 4px #141414}
.v4-row.on.k-teach .v4-bar{box-shadow:0 0 0 2px #fff,0 0 0 4px #0099ff}
.v4-row.past.on .v4-bar{background:#141414;color:#fff}
.v4-bl{padding:0 10px;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.04em;text-transform:uppercase;white-space:nowrap}
.v4-bl.out{position:absolute;left:100%;margin-left:6px;padding:0;color:#666}
.v4-today{position:absolute;top:-6px;bottom:0;width:2px;margin-left:-1px;background:#0099ff;pointer-events:none}
.v4-today b{position:absolute;top:-22px;left:50%;transform:translateX(-50%);padding:4px 7px;border-radius:6px;background:#e0f3ff;color:#0077cc;font:600 10px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase}
.v4-det{margin-top:24px;padding:20px 24px;border-radius:14px;background:#fafafa;box-shadow:inset 0 0 0 1px rgba(0,0,0,.05);min-height:64px}
.v4-dp{display:none;grid-template-columns:52px 1fr;column-gap:18px;align-items:start}.v4-dp.on{display:grid}
.v4-dl{display:grid;place-items:center;width:52px;height:52px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
.v4-dt{font:600 16px/1.3 Inter,sans-serif}.v4-dt span{font-weight:400;color:#7a7a7a}
.v4-ds{margin-top:6px;max-width:860px;font:400 14px/1.55 Inter,sans-serif;color:#4d4d4d}

/* V5 logo cards */
.v5{display:grid;grid-template-columns:repeat(5,1fr);gap:16px;align-items:start}
.v5-c{border-radius:16px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08);overflow:hidden;transition:transform .25s cubic-bezier(.2,.7,.2,1),box-shadow .25s}
.v5-c:hover{transform:translateY(-3px);box-shadow:inset 0 0 0 1px rgba(0,0,0,.08),0 14px 30px -16px rgba(0,0,0,.28)}
.v5-top{display:flex;flex-direction:column;justify-content:space-between;height:124px;padding:16px 18px 14px;box-sizing:border-box;background:var(--tint)}
.v5-tr{display:flex;justify-content:space-between;align-items:center;height:24px}
.v5-lg{display:grid;place-items:center;min-width:24px;height:24px}
.v5-lg .inv{filter:brightness(0) invert(1)}
.v5-c[style*="#141414;"] .mk-2u,.v5-c[style*="--tint: #141414"] .mk-2u{color:#fff}
.v5-c.past .v5-lg{filter:grayscale(1);opacity:.55}
.v5-now{padding:4px 7px;border-radius:999px;background:#fff;color:#0077cc;font:600 10px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase}
.v5-yr{font:700 40px/1 Inter,sans-serif;letter-spacing:-.04em;color:var(--ink)}
.v5-yr .dash{margin-left:2px;font-weight:500;opacity:.55}
.v5-yr small{margin-left:4px;font:600 18px/1 Inter,sans-serif;letter-spacing:-.02em}
.v5-bd{padding:16px 18px 16px}
.v5-ttl{font:600 15px/1.35 Inter,sans-serif;color:#141414}
.v5-c.past .v5-ttl{color:#7a7a7a}
.v5-org{margin-top:4px;font:400 13px/1.3 Inter,sans-serif;color:#7a7a7a}
.v5-sum{margin-top:10px;font:400 13.5px/1.5 Inter,sans-serif;color:#4d4d4d}
.v5-more{display:inline-flex;align-items:center;gap:4px;margin-top:10px;font:500 13px/1 Inter,sans-serif;color:#0099ff}
.v5-more svg{transition:transform .25s}.v5-c.on .v5-more svg{transform:rotate(180deg)}
.v5-more:hover{color:#0077cc}
.v5-nums{display:none}.v5-c.on .v5-nums{display:block}
.v5-bd .nda.sm{display:flex;width:max-content;max-width:100%;white-space:normal;line-height:1.3}
.v5-edu{margin-top:24px}

/* V6 grouped by company */
.v6-g{display:grid;grid-template-columns:48px 1fr;column-gap:16px;padding:18px 0;border-top:1px solid #f0f0f0}
.v6-g:first-child{border-top:0;padding-top:0}
.v6-extra{display:none}.v6.more .v6-extra{display:grid}
.v6-lg{display:grid;place-items:center;width:48px;height:48px;border-radius:12px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}
.v6-g.past .v6-lg{filter:grayscale(1);opacity:.55}
.v6-co{font:600 16px/1.3 Inter,sans-serif;color:#141414}
.v6-g.past .v6-co,.v6-g.past .v6-rt{color:#7a7a7a}
.v6-meta{margin-top:2px;font:400 12.5px/1.3 Inter,sans-serif;color:#9a9a9a}
.v6-rt{margin-top:8px;font:500 14.5px/1.35 Inter,sans-serif;color:#141414}
.v6-rd{margin-top:2px;font:400 12.5px/1.3 Inter,sans-serif;color:#9a9a9a}
.v6-rs{margin-top:8px;font:400 13.5px/1.5 Inter,sans-serif;color:#4d4d4d}
.v6-tree{position:relative;margin-top:4px}
.v6-tree::before{content:"";position:absolute;left:4px;top:18px;bottom:24px;width:1px;background:#dcdcdc}
.v6-r.nest{position:relative;padding-left:22px}
.v6-r.nest .v6-rt{margin-top:10px}
.v6-r.nest::before{content:"";position:absolute;left:0;top:15px;width:9px;height:9px;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 1.5px #c4c4c4}
.v6-btn{display:flex;align-items:center;justify-content:center;gap:6px;width:100%;margin-top:6px;padding:14px 0;border-top:1px solid #f0f0f0 !important;font:500 14px/1 Inter,sans-serif !important;color:#141414}
.v6-btn:hover{background:#fafafa}
.v6-btn svg{transition:transform .25s}.v6-btn[aria-expanded="true"] svg{transform:rotate(180deg)}
.v6-edu{margin-top:12px}

/* V7 now and before */
.s-v7{display:flex;flex-direction:column}
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
.v7-t{font:500 14.5px/1.35 Inter,sans-serif;color:#141414}
.v7-o{margin-top:2px;font:400 12.5px/1.3 Inter,sans-serif;color:#7a7a7a}
.v7-s{margin-top:8px;font:400 13.5px/1.5 Inter,sans-serif;color:#4d4d4d}
.v7-past .v7-lg{filter:grayscale(1);opacity:.55}
.v7-past .v7-t{color:#7a7a7a}
.v7.f-design .v7-row:not(.k-design),.v7.f-teach .v7-row:not(.k-teach){opacity:.22}
.v7-edu{margin-top:auto;padding-top:28px;flex-wrap:wrap;row-gap:4px}
.v7-skills{display:flex;align-items:center;gap:12px;margin-top:14px}
.v7-sk{font:500 10.5px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#b3b3b3}

/* V8 big type + photo preview */
.v8{display:grid;grid-template-columns:1fr 320px;gap:40px}
.v8-list{border-bottom:1px solid #ececec}
.v8-row{display:grid;grid-template-columns:44px 1fr 240px 100px;align-items:center;width:100%;height:96px;border-top:1px solid #ececec;color:#cfcfcf;transition:color .25s}
.v8-n{font:500 12px/1 'IBM Plex Mono',ui-monospace,monospace;color:inherit}
.v8-org{font:600 46px/1 Inter,sans-serif;letter-spacing:-.04em;white-space:nowrap;transition:transform .35s cubic-bezier(.2,.7,.2,1)}
.v8-role{font:500 13.5px/1.4 Inter,sans-serif;padding-right:12px}
.v8-yr{text-align:right;font:500 12px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.04em;font-variant-numeric:tabular-nums}
.v8-row:not(.on) .v8-role,.v8-row:not(.on) .v8-yr,.v8-row:not(.on) .v8-n{color:#a6a6a6}
.v8-row:hover{color:#7a7a7a}
.v8-row.now:not(.on) .v8-org{color:#bdbdbd}
.v8-row.past:not(.on) .v8-org{color:#e0e0e0}
.v8-row.on{color:#000}.v8-row.on .v8-org{transform:translateX(8px)}.v8-row.on .v8-role{color:#666}
.v8-side{position:relative}
.v8-pv{transition:transform .55s cubic-bezier(.2,.8,.2,1)}
.v8-ph{position:relative;height:220px;border-radius:16px;overflow:hidden;background:#f0f0f0;box-shadow:0 18px 40px -20px rgba(0,0,0,.35)}
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
article.v9-t:hover{transform:translateY(-2px)}
.v9-t.ph{justify-content:flex-end;color:#fff;background:#1d1d1f}
.v9-t.ph img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;transition:transform .8s cubic-bezier(.2,.7,.2,1)}
.v9-t.ph:hover img{transform:scale(1.04)}
.v9-t.ph::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(0,0,0,.55) 62%,rgba(0,0,0,.82))}
.v9-ov{position:relative;z-index:1;text-shadow:0 1px 12px rgba(0,0,0,.35)}
.v9-pill{display:inline-block;margin-bottom:12px;padding:5px 9px;border-radius:999px;background:rgba(255,255,255,.2);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);font:600 10px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase}
.v9-pill.gold{margin:12px 0 0;text-transform:none;font:500 12px/1 Inter,sans-serif;letter-spacing:0}
.v9-big{font:600 34px/1.05 Inter,sans-serif;letter-spacing:-.03em}
.v9-mid{font:600 18px/1.2 Inter,sans-serif;letter-spacing:-.01em}
.v9-sub{display:flex;align-items:center;gap:7px;margin-top:6px;font:400 13px/1.3 Inter,sans-serif;opacity:.85}
.v9-txt{margin-top:10px;max-width:440px;font:400 14px/1.5 Inter,sans-serif;opacity:.9}
.v9-txt.sm{margin-top:6px;font-size:12.5px;opacity:.7}
.dk{color:#141414}.v9-sub.dk{color:#666;opacity:1}
.v9-t.past .v9-mid.dk{color:#7a7a7a}
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
.v9-sfl{display:grid;place-items:center;width:44px;height:44px;border-radius:12px;background:#f4f4f4}
.v9-sfl img{filter:grayscale(1);opacity:.6}
.v9-sp{display:none}.v9-sp.on{display:block}
.v9-sr{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a}
.v9-st{margin-top:10px;max-width:520px;font:400 14.5px/1.55 Inter,sans-serif;color:#4d4d4d}
.v9-st.sm{margin-top:8px;font-size:13.5px}
.v9-mets{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:14px}
.v9-mets b{display:block;font:600 30px/1 Inter,sans-serif;letter-spacing:-.03em;color:#4d4d4d}
.v9-mets span{display:block;margin-top:6px;font:400 12.5px/1.4 Inter,sans-serif;color:#7a7a7a}
.v9 .f{grid-column:3;grid-row:3}
.v9 .g{grid-column:4;grid-row:3}
.v9 .s{grid-column:1/-1;grid-row:4;flex-direction:row;align-items:center;justify-content:flex-start;gap:14px;padding:12px 18px;background:#fafafa}
.v9-sk{font:500 10.5px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#b3b3b3}
.v9-foot{margin:0 0 0 auto;padding:0;border:0}

/* V10 resume sheet */
.v10-bar{display:flex;align-items:center;justify-content:space-between;width:794px;margin:0 auto 16px}
.v10-file{display:flex;align-items:center;gap:8px;font:500 14px/1 Inter,sans-serif}
.v10-pg{padding:4px 7px;border-radius:6px;background:#e4e4e4;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;color:#666}
.v10-bar .seg{background:#e4e4e4}
.v10-act{display:flex;align-items:center;gap:16px;font:500 13px/1 Inter,sans-serif}
.rv-root .v10-dl{display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 12px 0 14px;border-radius:999px;background:#fff;color:#9a9a9a;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1);font:500 13px/1 Inter,sans-serif;cursor:not-allowed}
.v10-paper{width:794px;margin:0 auto;box-sizing:border-box;padding:56px 64px 48px;background:#fff;border-radius:4px;box-shadow:0 1px 2px rgba(0,0,0,.06),0 24px 50px -26px rgba(0,0,0,.28)}
.v10-hd{display:flex;justify-content:space-between;align-items:flex-start;gap:24px;padding-bottom:24px}
.v10-name{font:700 30px/1 Inter,sans-serif;letter-spacing:-.03em}
.v10-tag{margin-top:10px;max-width:460px;font:400 14px/1.45 Inter,sans-serif;color:#666}
.v10-mono,.v10-sh,.v10-d{font:500 10.5px/1.3 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.07em;text-transform:uppercase;color:#9a9a9a;white-space:nowrap}
.v10-d{font-variant-numeric:tabular-nums}
.v10-sec{display:grid;grid-template-columns:110px 1fr;column-gap:24px;padding:20px 0;border-top:1px solid #ececec}
.v10-sh{padding-top:3px}
.v10-e{margin-bottom:16px}.v10-e:last-child{margin-bottom:0}
.v10-et{display:flex;justify-content:space-between;align-items:baseline;gap:16px}
.v10-et p{font:400 14px/1.4 Inter,sans-serif}.v10-et b{font-weight:600}.v10-et span{color:#7a7a7a}
.v10-e.past .v10-et b{color:#4d4d4d}
.v10-sub p{padding-left:12px;font-size:13.5px;color:#4d4d4d}
.v10-d{flex:none}
.v10-es{margin-top:4px;font:400 13px/1.55 Inter,sans-serif;color:#4d4d4d}
.v10-nda{font-style:italic;color:#7a7a7a}
.v10-num{font:400 11px/1.5 'IBM Plex Mono',ui-monospace,monospace;color:#7a7a7a}
.v10-sk{font:400 13px/1.5 Inter,sans-serif;color:#4d4d4d}
.v10-paper.compact .v10-es{display:none}
.v10-paper.compact .v10-e{margin-bottom:8px}

/* shared: screen-reader-only, plain list */
.sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.plain{list-style:none;padding:0;margin:10px 0 0}
.plain li{display:flex;gap:6px;padding:7px 0;border-bottom:1px solid #f2f2f2;font:400 13px/1.45 Inter,sans-serif;color:#4d4d4d}
.plain li b{font-weight:500;color:#141414}
.plain li span{margin-left:auto;padding-left:12px;white-space:nowrap;font:400 11.5px/1.6 'IBM Plex Mono',ui-monospace,monospace;color:#9a9a9a}
@keyframes rvblink{50%{opacity:0}}

/* V12 terminal */
.s-v12,.s-v13{display:flex;flex-direction:column}
.v12{border-radius:14px;background:#141414;color:#e6e6e6;overflow:hidden;box-shadow:0 22px 44px -26px rgba(0,0,0,.55)}
.v12-bar{position:relative;display:flex;align-items:center;gap:6px;padding:12px 14px;border-bottom:1px solid #2b2b2d}
.v12-bar i{width:9px;height:9px;border-radius:50%;background:#3a3a3c}
.v12-bar span{position:absolute;left:0;right:0;text-align:center;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;color:#9a9a9a}
.v12-scr{position:relative;height:330px;overflow:auto;padding:16px 18px;box-sizing:border-box}
.v12-out{margin:0;font:400 12px/1.6 'IBM Plex Mono',ui-monospace,monospace;white-space:pre-wrap;color:#e6e6e6}
.v12-cur{display:inline-block;width:7px;height:14px;vertical-align:-2px;background:#7cc4ff;opacity:0}
.v12-cur.on{opacity:1;animation:rvblink 1s steps(1) infinite}
.v12-cmds{display:flex;flex-wrap:wrap;align-items:center;gap:6px;padding:12px 14px;border-top:1px solid #2b2b2d}
.v12-ps{margin-right:4px;font:500 12px/1 'IBM Plex Mono',ui-monospace,monospace;color:#7cc4ff}
.rv-root .v12-chip{padding:7px 10px;border-radius:8px;background:#2b2b2d;color:#e6e6e6;font:500 12px/1 'IBM Plex Mono',ui-monospace,monospace;transition:background-color .2s}
.rv-root .v12-chip:hover{background:#3a3a3c}
.rv-root .v12-chip.ghost{background:none;color:#9a9a9a;box-shadow:inset 0 0 0 1px #3a3a3c}
.v12-det{margin-top:18px;font:400 13.5px/1.5 Inter,sans-serif}
.v12-det summary{cursor:pointer;font-weight:500;color:#141414}
.v12-det summary:focus-visible{outline:2px solid #0099ff;outline-offset:2px;border-radius:6px}

/* V13 ask my resume */
.v13{display:flex;flex-direction:column;border-radius:16px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08);overflow:hidden}
.v13-hd{display:flex;align-items:center;gap:12px;padding:14px 16px;border-bottom:1px solid #f0f0f0}
.v13-av{display:grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#141414;color:#fff;font:400 22px/1 Caveat,cursive}
.v13-n{font:600 14.5px/1.3 Inter,sans-serif}
.v13-st{font:400 12px/1.3 Inter,sans-serif;color:#9a9a9a}
.v13-log{display:flex;flex-direction:column;gap:12px;height:318px;overflow:auto;padding:16px;box-sizing:border-box;background:#fafafa}
.v13-qa{display:none;flex-direction:column;gap:8px}.v13-qa.on{display:flex}
.v13-u{align-self:flex-end;max-width:80%;padding:9px 13px;border-radius:16px 16px 4px 16px;background:#141414;color:#fff;font:500 13.5px/1.4 Inter,sans-serif}
.v13-a{align-self:flex-start;max-width:88%;padding:10px 14px;border-radius:16px 16px 16px 4px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06);font:400 13.5px/1.55 Inter,sans-serif;color:#333}
.v13-cur{display:inline-block;width:6px;height:6px;margin-left:4px;border-radius:50%;background:#0099ff;opacity:0}
.v13-cur.on{opacity:1;animation:rvblink .8s steps(1) infinite}
.v13-chips{display:flex;flex-wrap:wrap;gap:6px;padding:12px 14px;border-top:1px solid #f0f0f0;min-height:34px}
.rv-root .v13-chip{padding:8px 12px;border-radius:999px;background:#e0f3ff;color:#0069b4;font:500 13px/1 Inter,sans-serif;transition:background-color .2s}
.rv-root .v13-chip:hover{background:#cceaff}
.rv-root .v13-chip.off{display:none}
.rv-root .v13-chip.ghost{background:none;color:#666;box-shadow:inset 0 0 0 1px #e0e0e0}

/* V14 workbench */
.v14{display:grid;grid-template-columns:1fr 360px;gap:32px;align-items:start}
.v14-scene{position:relative;aspect-ratio:760/460;border-radius:16px;background:#fafafa}
.v14-svg{position:absolute;inset:0;width:100%;height:100%;overflow:visible}
.v14-o{transition:transform .4s cubic-bezier(.3,1.5,.5,1)}
.v14-o.on{transform:translateY(-10px)}
.v14-scene:has(.v14-b0:hover) .v14-o0,.v14-scene:has(.v14-b1:hover) .v14-o1,.v14-scene:has(.v14-b2:hover) .v14-o2,
.v14-scene:has(.v14-b3:hover) .v14-o3,.v14-scene:has(.v14-b4:hover) .v14-o4,
.v14-scene:has(.v14-b0:focus-visible) .v14-o0,.v14-scene:has(.v14-b1:focus-visible) .v14-o1,.v14-scene:has(.v14-b2:focus-visible) .v14-o2,
.v14-scene:has(.v14-b3:focus-visible) .v14-o3,.v14-scene:has(.v14-b4:focus-visible) .v14-o4{transform:translateY(-10px)}
.rv-root .v14-b{position:absolute;border-radius:14px}
.v14-lab{position:absolute;left:50%;top:100%;transform:translate(-50%,2px);padding:6px 10px;border-radius:999px;background:#141414;color:#fff;white-space:nowrap;font:500 12px/1 Inter,sans-serif;opacity:0;pointer-events:none;transition:opacity .2s,transform .2s}
.v14-b:hover .v14-lab,.v14-b:focus-visible .v14-lab{opacity:1;transform:translate(-50%,6px)}
.v14-b.on .v14-lab{opacity:1;transform:translate(-50%,6px);background:#0099ff}
@media (hover: none){.v14-lab{opacity:1}}
.v14-cd{display:none;padding:22px 24px;border-radius:16px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08),0 18px 36px -24px rgba(0,0,0,.3)}.v14-cd.on{display:block}
.v14-obj{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#0069b4}
.v14-k{margin-top:14px;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a}
.v14-t{margin-top:8px;font:600 19px/1.25 Inter,sans-serif;letter-spacing:-.01em;color:#141414}
.v14-t.sm{margin-top:18px;font-size:15px}
.v14-or{margin-top:4px;font:400 13px/1.3 Inter,sans-serif;color:#7a7a7a}
.v14-s{margin-top:10px;font:400 14px/1.55 Inter,sans-serif;color:#4d4d4d}
.v14-det{margin-top:16px}

/* V15 sketch -> render */
.v15-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:24px}
.v15-h{font:600 18px/1.3 Inter,sans-serif;letter-spacing:-.01em}
.rv-root .v15-all{padding:10px 16px;border-radius:999px;background:#141414;color:#fff;font:500 13px/1 Inter,sans-serif;transition:background-color .2s}
.rv-root .v15-all:hover{background:#333}
.rv-root .v15-all.on{background:#0099ff}
.v15{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.rv-root .v15-c{position:relative;display:block;width:100%;height:312px;border-radius:14px}
.v15-sk,.v15-rd{position:absolute;inset:0;display:flex;flex-direction:column;padding:20px;border-radius:14px;box-sizing:border-box}
.v15-sk{background:#fff;box-shadow:inset 0 0 0 1.5px #3a3a3a;transform:rotate(-.3deg)}
.v15-sk::after{content:"";position:absolute;inset:3px -3px -3px 3px;border:1px solid #b3b3b3;border-radius:16px 12px 15px 13px;transform:rotate(.6deg);pointer-events:none}
.v15-th{display:grid;place-items:center;flex:none;height:84px;margin-bottom:16px;border-radius:10px}
.v15-th.sk{background:repeating-linear-gradient(-45deg,#d6d6d6 0 1px,transparent 1px 7px);box-shadow:inset 0 0 0 1.5px #3a3a3a}
.v15-t,.v15-o,.v15-s,.v15-note{display:block}
.v15-sk .v15-t{font:600 25px/1 Caveat,cursive;color:#2b2b2b}
.v15-sk .v15-o{margin-top:6px;font:500 19px/1.1 Caveat,cursive;color:#666}
.v15-sk .v15-s{margin-top:8px;font:400 13px/1.5 Inter,sans-serif;color:#7a7a7a}
.v15-note{margin-top:auto;font:600 19px/1.1 Caveat,cursive;color:#0069b4}
.v15-rd{background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.07),0 18px 36px -22px rgba(0,0,0,.35);clip-path:inset(0 100% 0 0 round 14px);transition:clip-path .75s cubic-bezier(.65,0,.25,1)}
.v15-rd .v15-th .inv{filter:brightness(0) invert(1)}
.v15-th.rd[style*="#141414"] .mk-2u{color:#fff}
.v15-rd .v15-t{font:600 17px/1.3 Inter,sans-serif;color:#141414}
.v15-rd .v15-o{margin-top:4px;font:400 13px/1.3 Inter,sans-serif;color:#7a7a7a}
.v15-rd .v15-s{margin-top:8px;font:400 13px/1.5 Inter,sans-serif;color:#4d4d4d}
.v15-c.past .v15-rd .v15-t{color:#4d4d4d}
.v15-c.past .v15-rd .v15-th{filter:saturate(.35)}
.v15-c:hover .v15-rd,.v15-c:focus-visible .v15-rd,.v15-c.on .v15-rd,.v15.all .v15-rd{clip-path:inset(0 0 0 0 round 14px)}
.v15-c.ms .v15-sk{cursor:default}

/* V16 badge deck */
.v16-deck{position:relative;height:410px}
.v16-card{position:absolute;left:calc(50% - 110px);top:34px;width:220px;height:330px;perspective:1100px;transform:translate(calc(var(--i) * 7px),calc(var(--i) * -6px)) rotate(calc((var(--i) - 2) * 2deg));transition:transform .65s cubic-bezier(.3,1.25,.4,1)}
.v16-deck.fan .v16-card,.v16-deck:hover .v16-card,.v16-deck:focus-within .v16-card{transform:translateX(calc((var(--i) - 2) * 252px)) translateY(calc(var(--a) * 10px)) rotate(calc((var(--i) - 2) * 2.5deg))}
.v16-in{position:relative;width:100%;height:100%;transform-style:preserve-3d;transition:transform .65s cubic-bezier(.3,1.2,.4,1)}
.v16-card.on .v16-in{transform:rotateY(180deg)}
.v16-face{position:absolute;inset:0;display:flex;flex-direction:column;padding:18px 20px 52px;border-radius:16px;box-sizing:border-box;-webkit-backface-visibility:hidden;backface-visibility:hidden}
.v16-face.front{background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.09),0 18px 36px -20px rgba(0,0,0,.35)}
.v16-face.back{background:#141414;color:#fff;transform:rotateY(180deg);box-shadow:0 18px 36px -20px rgba(0,0,0,.45)}
.v16-slot{align-self:center;flex:none;width:46px;height:8px;border-radius:4px;background:#f0f0f0;box-shadow:inset 0 0 0 1px rgba(0,0,0,.14)}
.v16-band{flex:none;height:6px;margin:14px 0 18px;border-radius:3px}
.v16-lg{display:flex;align-items:center;height:28px}
.v16-org{margin-top:12px;font:600 20px/1.15 Inter,sans-serif;letter-spacing:-.02em;color:#141414}
.v16-t{margin-top:8px;font:400 14px/1.4 Inter,sans-serif;color:#4d4d4d}
.v16-y{margin-top:auto;font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;color:#7a7a7a}
.v16-card.past .v16-org{color:#7a7a7a}.v16-card.past .v16-lg{filter:grayscale(1);opacity:.55}
.v16-bk{font:500 10.5px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:#7cc4ff}
.v16-bt{margin-top:14px;font:400 14px/1.55 Inter,sans-serif;color:#e6e6e6}
.rv-root .v16-flip{position:absolute;left:50%;bottom:14px;z-index:2;transform:translateX(-50%);padding:7px 14px;border-radius:999px;background:#f0f0f0;color:#141414;font:500 12px/1 Inter,sans-serif;transition:background-color .2s,color .2s}
.rv-root .v16-flip:hover{background:#e0e0e0}
.rv-root .v16-card.on .v16-flip{background:#2b2b2d;color:#fff}
.v16-edu{padding-top:8px}
@media (prefers-reduced-motion: reduce){
  .v16-deck{height:auto;display:grid;grid-template-columns:repeat(5,1fr);gap:12px}
  .v16-card{position:relative;left:auto;top:auto;width:auto;height:auto;transform:none !important}
  .v16-in{display:grid;gap:8px;transform:none !important}
  .v16-face{position:relative;min-height:240px}.v16-face.back{transform:none}
  .rv-root .v16-flip{display:none}}

/* V17 era dial */
.v17{display:grid;grid-template-columns:360px 1fr;gap:44px;padding:36px 40px;border-radius:16px;background:var(--bg);color:var(--ink);transition:background-color .5s,color .5s}
.v17-dial{display:flex;flex-direction:column;align-items:center}
.v17-ring{position:relative;width:270px;height:270px}
.v17-lb{position:absolute;transform:translate(-50%,-50%);font:500 12px/1 'IBM Plex Mono',ui-monospace,monospace;color:var(--ink);opacity:.55;transition:opacity .3s,color .3s}
.v17-lb.on{opacity:1;font-weight:600;color:var(--acc)}
.v17-tk{position:absolute;width:2px;height:10px;border-radius:1px;background:var(--ink);opacity:.35}
.v17-knob{position:absolute;left:50%;top:50%;width:156px;height:156px;margin:-78px 0 0 -78px;border-radius:50%;background:radial-gradient(circle at 35% 28%,#ffffff,#f4f4f4 55%,#dcdcdc);box-shadow:0 16px 30px -12px rgba(0,0,0,.35),inset 0 -3px 6px rgba(0,0,0,.08),0 0 0 7px rgba(255,255,255,.55);cursor:grab;touch-action:none;transition:transform .5s cubic-bezier(.3,1.5,.5,1)}
.v17-knob:active{cursor:grabbing}
.rv-root .v17-knob:focus-visible{outline:2px solid #0099ff;outline-offset:8px;border-radius:50%}
.v17-knob::before{content:"";position:absolute;inset:22px;border-radius:50%;background:repeating-conic-gradient(rgba(0,0,0,.05) 0 4deg,transparent 4deg 8deg)}
.v17-ptr{position:absolute;left:50%;top:12px;width:4px;height:28px;margin-left:-2px;border-radius:2px;background:var(--acc);transition:background-color .4s}
.v17-hint{margin-top:16px;font:400 12.5px/1.3 Inter,sans-serif;opacity:.75}
.v17-list{display:flex;flex-direction:column;gap:4px;width:100%;margin-top:20px}
.rv-root .v17-list button{display:flex;align-items:baseline;gap:10px;padding:9px 12px;border-radius:10px;font:400 13.5px/1.3 Inter,sans-serif;color:var(--ink);transition:background-color .2s}
.v17-list button b{min-width:104px;font:500 11.5px/1 'IBM Plex Mono',ui-monospace,monospace;color:var(--acc)}
.rv-root .v17-list button:hover{background:rgba(255,255,255,.45)}
.rv-root .v17-list button.on{background:rgba(255,255,255,.8);font-weight:500}
.v17-panel{display:flex;flex-direction:column;min-width:0}
.v17-p{display:none}.v17-p.on{display:block}
.v17-era{font:500 11px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.08em;text-transform:uppercase;color:var(--acc)}
.v17-n{margin-top:12px;font:600 36px/1.1 Inter,sans-serif;letter-spacing:-.03em}
.v17-y{margin-top:8px;font:500 13px/1 'IBM Plex Mono',ui-monospace,monospace;color:var(--acc)}
.v17-r{margin-top:20px;padding:18px 20px;border-radius:14px;background:rgba(255,255,255,.7)}
.v17-rt{font:600 16px/1.35 Inter,sans-serif}
.v17-ro{margin-top:3px;font:400 13px/1.3 Inter,sans-serif;opacity:.8}
.v17-rs{margin-top:8px;font:400 14px/1.55 Inter,sans-serif}
.v17 .nums{color:var(--ink);opacity:.8}
.v17-foot{margin-top:auto;padding-top:16px;border-top-color:rgba(0,0,0,.1)}
.v17-foot .lk{color:var(--ink);border-bottom-color:rgba(0,0,0,.25)}
.v17-foot .lk-ph{color:var(--ink);opacity:.6}
@media (prefers-reduced-motion: reduce){.rv-root *{transition:none !important;animation:none !important}}
'''

JS = r'''class Component extends DCLogic {
  constructor(props) {
    super(props);
    this.D = __DATA__;
    this.state = { v11: false, t1: 0, l2: 0, a3: { 0: true }, g4: 0, c5: false, s6: false, f7: 'all', h8: 0, b9: 0, m10: 'd',
      t12: ['history'], t12n: 100000, q13: [], q13n: 0, w14: 0, r15: {}, all15: false, fan16: false, f16: {}, e17: 3 };
    this.timers = {};
  }
  componentWillUnmount() { for (const k in this.timers) clearInterval(this.timers[k]); }
  componentDidUpdate() {
    for (const el of [this.el12, this.el13]) if (el) el.scrollTop = el.scrollHeight;
  }
  calm() { try { return window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } }
  type(key, total) {
    clearInterval(this.timers[key]);
    if (this.calm()) { this.setState({ [key]: total }); return; }
    let n = 0;
    this.setState({ [key]: 0 });
    this.timers[key] = setInterval(() => {
      n = Math.min(total, n + 3);
      this.setState({ [key]: n });
      if (n >= total) clearInterval(this.timers[key]);
    }, 14);
  }
  run12(c) {
    if (c === 'clear') { clearInterval(this.timers.t12n); this.setState({ t12: [], t12n: 0 }); return; }
    this.setState({ t12: this.state.t12.concat([c]).slice(-3) });
    this.type('t12n', this.D.t12[c].out.length);
  }
  ask13(i) {
    if (this.state.q13.indexOf(i) >= 0) return;
    this.setState({ q13: this.state.q13.concat([i]) });
    this.type('q13n', this.D.q13[i].a.length);
  }
  era17(j) { const e = Math.max(0, Math.min(3, j)); if (e !== this.state.e17) this.setState({ e17: e }); }
  dial17(ev) {
    const r = ev.currentTarget.getBoundingClientRect();
    const dx = ev.clientX - (r.left + r.width / 2), dy = ev.clientY - (r.top + r.height / 2);
    const ang = Math.atan2(dx, -dy) * 180 / Math.PI;
    let best = 0, bd = 999;
    this.D.e17.forEach((e, j) => { const d = Math.abs(e.ang - ang); if (d < bd) { bd = d; best = j; } });
    this.era17(best);
  }
  renderVals() {
    const st = this.state, v = {}, D = this.D;
    const flip = (key, i) => () => { const o = Object.assign({}, this.state[key]); o[i] = !o[i]; this.setState({ [key]: o }); };
    v.v11c = st.v11 ? 'on' : ''; v.v11x = String(st.v11); v.v11cls = st.v11 ? 'all' : '';
    v.v11f = () => this.setState({ v11: !this.state.v11 });
    for (let i = 0; i < 5; i++) {
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
      const o8 = st.h8 === i;
      v['h8c' + i] = o8 ? 'on' : ''; v['h8x' + i] = String(o8);
      v['h8f' + i] = () => { if (this.state.h8 !== i) this.setState({ h8: i }); };
      const o14 = st.w14 === i;
      v['w14c' + i] = o14 ? 'on' : ''; v['w14x' + i] = String(o14);
      v['w14f' + i] = () => this.setState({ w14: i });
      const o16 = !!st.f16[i];
      v['f16c' + i] = o16 ? 'on' : ''; v['f16x' + i] = String(o16); v['f16f' + i] = flip('f16', i);
    }
    v.c5c = st.c5 ? 'on' : ''; v.c5x = String(st.c5);
    v.c5f = () => this.setState({ c5: !this.state.c5 });
    v.s6c = st.s6 ? 'more' : ''; v.s6x = String(st.s6);
    v.s6f = () => this.setState({ s6: !this.state.s6 });
    for (const k of ['all', 'design', 'teach']) {
      v['f7c' + k] = st.f7 === k ? 'on' : ''; v['f7x' + k] = String(st.f7 === k);
      v['f7f' + k] = () => this.setState({ f7: k });
    }
    v.f7cls = st.f7 === 'all' ? '' : 'f-' + st.f7;
    v.h8y = Math.min(st.h8 * 96, 150) + 'px';
    for (let i = 0; i < 3; i++) {
      v['b9c' + i] = st.b9 === i ? 'on' : ''; v['b9x' + i] = String(st.b9 === i);
      v['b9f' + i] = () => this.setState({ b9: i });
    }
    for (const k of ['d', 'c']) {
      v['m10c' + k] = st.m10 === k ? 'on' : ''; v['m10x' + k] = String(st.m10 === k);
      v['m10f' + k] = () => this.setState({ m10: k });
    }
    v.m10cls = st.m10 === 'c' ? 'compact' : '';
    // V12 terminal
    const last12 = st.t12.length - 1;
    v.t12vis = st.t12.map((c, i) => {
      const out = D.t12[c].out;
      return '$ tin ' + D.t12[c].cmd + '\n' + (i === last12 ? out.slice(0, st.t12n) : out) + '\n';
    }).join('\n') + (st.t12.length ? '\n' : '') + '$ ';
    v.t12cur = 'on';
    v.t12sr = last12 >= 0 ? D.t12[st.t12[last12]].out : 'Cleared.';
    for (const c of Object.keys(D.t12).concat(['clear'])) v['t12f' + c] = () => this.run12(c);
    v.r12 = (el) => { this.el12 = el; };
    // V13 chat
    const asked = st.q13, lastQ = asked[asked.length - 1];
    let offer = lastQ === undefined ? [0, 1, 2, 3] : D.q13[lastQ].f.filter((q) => asked.indexOf(q) < 0);
    if (!offer.length) offer = [0, 1, 2, 3, 4].filter((q) => asked.indexOf(q) < 0);
    for (let i = 0; i < 5; i++) {
      const k = asked.indexOf(i);
      v['q13c' + i] = k >= 0 ? 'on' : '';
      v['q13o' + i] = String(k + 1);
      v['q13v' + i] = i === lastQ ? D.q13[i].a.slice(0, st.q13n) : D.q13[i].a;
      v['q13cur' + i] = i === lastQ && st.q13n < D.q13[i].a.length ? 'on' : '';
      v['q13k' + i] = offer.indexOf(i) >= 0 ? '' : 'off';
      v['q13f' + i] = () => this.ask13(i);
    }
    v.q13rk = asked.length ? '' : 'off';
    v.q13r = () => { clearInterval(this.timers.q13n); this.setState({ q13: [], q13n: 0 }); };
    v.r13 = (el) => { this.el13 = el; };
    // V15 sketch -> render
    for (let i = 0; i < 6; i++) {
      const o = !!st.r15[i];
      v['r15c' + i] = o ? 'on' : ''; v['r15x' + i] = String(o); v['r15f' + i] = flip('r15', i);
    }
    v.all15c = st.all15 ? 'on' : ''; v.all15x = String(st.all15); v.all15cls = st.all15 ? 'all' : '';
    v.all15f = () => this.setState({ all15: !this.state.all15 });
    // V16 badges
    v.fan16c = st.fan16 ? 'on' : ''; v.fan16x = String(st.fan16); v.fan16cls = st.fan16 ? 'fan' : '';
    v.fan16f = () => this.setState({ fan16: !this.state.fan16 });
    // V17 era dial
    const E = D.e17[st.e17];
    v.e17 = String(st.e17); v.e17t = E.t; v.e17a = E.ang + 'deg';
    v.e17bg = E.bg; v.e17ink = E.ink; v.e17acc = E.acc;
    for (let j = 0; j < 4; j++) {
      v['e17c' + j] = st.e17 === j ? 'on' : ''; v['e17x' + j] = String(st.e17 === j);
      v['e17f' + j] = () => this.era17(j);
    }
    v.e17k = (ev) => {
      const k = ev.key, e = this.state.e17;
      const to = k === 'ArrowRight' || k === 'ArrowUp' ? e + 1 : k === 'ArrowLeft' || k === 'ArrowDown' ? e - 1 : k === 'Home' ? 0 : k === 'End' ? 3 : null;
      if (to === null) return;
      ev.preventDefault(); this.era17(to);
    };
    v.e17pd = (ev) => { this.drag17 = true; try { ev.currentTarget.setPointerCapture(ev.pointerId); } catch (e) {} this.dial17(ev); };
    v.e17pm = (ev) => { if (this.drag17) this.dial17(ev); };
    v.e17pu = () => { this.drag17 = false; };
    return v;
  }
}'''.replace('__DATA__', JS_DATA)
assert all(ord(c) < 128 for c in JS)

doc = f'''<!doctype html>
<html>
<head><meta charset="utf-8"><script src="./support.js"></script></head>
<body>
<!-- Resume / work history: V11 recommended (research-backed two-group ledger) + 10 treatments (timeline, ledger, accordion, overlap chart, logo cards, grouped by company, now and before, big type with photo, bento, resume sheet) -->
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
