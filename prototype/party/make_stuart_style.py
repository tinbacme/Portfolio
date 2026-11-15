"""Tin's portfolio in the stuart.re style: left logo dock, quiet intro, timeline of roles with stacked media + sticky info, contact form."""
import json
S = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/'
B = lambda i: '/_blob/' + i
LOGO_SF = B('ac43d25c19be4e522f4bd492e1c090ab'); LOGO_UO = B('00e0e1ec841a28c4e0055e4a6738e6b1')
MS = lambda w, mono=False: (f'<svg viewBox="0 0 20 20" width="{w}" height="{w}" aria-hidden="true">' + ''.join(
    f'<rect x="{x}" y="{y}" width="9" height="9" fill="{"#fff" if mono else c}"></rect>' for x, y, c in [(0, 0, '#f25022'), (11, 0, '#7fba00'), (0, 11, '#00a4ef'), (11, 11, '#ffb900')]) + '</svg>')
TXT = lambda t, size, color: f'<span style="font: 700 {size}px/1 Inter, system-ui, sans-serif; color: {color}; letter-spacing: -0.02em">{t}</span>'
LOCK = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" aria-hidden="true"><rect x="5" y="11" width="14" height="9" rx="2" stroke="currentColor" stroke-width="1.6"></rect><path d="M8 11V8a4 4 0 0 1 8 0v3" stroke="currentColor" stroke-width="1.6"></path></svg>'
ARR = '<svg viewBox="0 0 24 24" width="12" height="12" fill="none" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"></path></svg>'

def img(src, alt, pos='50% 50%', ratio='16 / 10'):
    return f'<figure class="st-media" style="aspect-ratio: {ratio}"><img src="{src}" alt="{alt}" style="object-position: {pos}"></figure>'
def locked(title, note):
    return f'<figure class="st-media st-locked" style="aspect-ratio: 16 / 7"><div>{LOCK}<p class="st-lk-t">Locked</p><p class="st-lk-n">{title} · {note}</p></div></figure>'
def textcard(big, small):
    return f'<figure class="st-media st-textcard" style="aspect-ratio: 16 / 10"><div><p class="st-tc-big">{big}</p><p class="st-tc-small">{small}</p></div></figure>'

ROWS = [
 dict(id='microsoft', years='2022 — now', name='Microsoft AI', role='Senior Product Designer',
      logo=MS(26), dock=MS(22, True), dockLabel='Microsoft AI',
      blurb='Search across Bing, Edge and Windows. Helping people find what they need, growing Bing, and exploring what AI agents could do in search.',
      cta=('Available on request', None),
      media=[img(B('effff208332abe411e27c82aaa87e30d'), 'Tin with his Microsoft team', '50% 72%'),
             locked('Windows Search Box', 'under NDA, happy to walk you through it'),
             locked('Bing', 'under NDA, happy to walk you through it')]),
 dict(id='uo-teach', years='2023 — now', name='University of Oregon', role='Product Design Instructor',
      logo=f'<img src="{LOGO_UO}" alt="" width="24" height="24">', dock=f'<img src="{LOGO_UO}" alt="" width="20" height="20" class="st-mono">', dockLabel='University of Oregon',
      blurb='Teaching UX and product design at the school where I studied industrial design. Students learn the way I still work: by building and prototyping.',
      cta=('Open', 'https://artdesign.uoregon.edu/directory/product-design-instructors/all/tle'),
      media=[img(B('155942c7f1c522f9aec7d43d1c1d0d0d'), 'Tin teaching a product design class', '50% 62%')]),
 dict(id='2u', years='2021 —', name='2U', role='UX/UI Bootcamp Instructor',
      logo=TXT('2U', 15, '#141414'), dock=TXT('2U', 14, '#fff'), dockLabel='2U',
      blurb='Led cohorts through a 24-week bootcamp in UX research, UX and UI design and front-end development.',
      cta=('Remote', None),
      media=[textcard('24 weeks, cohort after cohort', 'University of Oregon · UC Berkeley · Michigan · Minnesota · Utah · Arizona')]),
 dict(id='salesforce', years='2017 — 2022', name='Salesforce', role='Designer · Associate Designer · Intern',
      logo=f'<img src="{LOGO_SF}" alt="" width="30" height="22">', dock=f'<img src="{LOGO_SF}" alt="" width="24" height="18" class="st-mono">', dockLabel='Salesforce',
      blurb='Redesigned search and content for Salesforce Help (support cases down 60% a month), rebuilt Manage Users, a back-to-work app for 75K employees, and components for the C360 design system.',
      cta=('Open', 'https://help.salesforce.com'),
      media=[img(B('85d39c433632d0b82e694159bcb87420'), 'Salesforce Help home page, version 1 to version 2'),
             img(B('ef76a1fda50ef952e506c2a2c7d5ce17'), 'Salesforce Help search, version 1 to version 2'),
             img(B('359072bfd777de3d29e05c7a7b6fbdd0'), 'Salesforce Help, before and after'),
             img(B('b3da5c6480ae317af83ea7474a9e0c66'), 'Manage Users: legacy, MVP and MVP plus side by side'),
             img(B('8bd998ead1110dbdb0a707cdb0cb6c60'), 'Tin with his Salesforce team', '18% 50%')]),
 dict(id='luxium', years='2017', name='Luxium Lighting', role='Product Designer',
      logo=TXT('L', 18, '#141414'), dock=TXT('L', 16, '#fff'), dockLabel='Luxium Lighting',
      blurb='An LED light, from design concept to a working prototype: sketches, 3D CAD and close work with engineers.',
      cta=('Concept to prototype', None),
      media=[img(B('ba8bd31d630d184e221d64c307637692'), 'Ballpoint sketch of an LED desk lamp with an exploded view', '50% 50%'),
             img(B('17db6e2bb7b0e2021c26e1ecc3bda47f'), 'Product sketches in a sketchbook', '50% 50%')]),
 dict(id='uo-bs', years='2014 — 2018', name='University of Oregon', role='BS Industrial Design',
      logo=f'<img src="{LOGO_UO}" alt="" width="24" height="24">', dock=None, dockLabel='',
      blurb='Industrial design with a business minor. Sketching, CAD, rendering and building prototypes by hand. 1st place overall at Quackhatch @UO, 2018.',
      cta=('Class of 2018', None),
      media=[img(B('54416d11bdc955c9c7fb45c9c479a828'), 'Tin with friends at graduation', '30% 40%'),
             img(B('4eac407aac52c547e08dbd5a341e2432'), 'Tin at his University of Oregon graduation', '42% 35%')]),
]

def row(r):
    label, href = r['cta']
    cta = (f'<a class="st-open" href="{href}" target="_blank" rel="noopener">{label} {ARR}</a>' if href else f'<span class="st-pill">{label}</span>')
    return (f'<section class="st-row" id="{r["id"]}" aria-label="{r["name"]}, {r["role"]}">'
            f'<p class="st-year">{r["years"]}</p>'
            f'<div class="st-stack">{"".join(r["media"])}</div>'
            f'<div class="st-info"><div class="st-info-in">'
            f'<span class="st-logo">{r["logo"]}</span>'
            f'<p class="st-name">{r["name"]}</p><p class="st-role">{r["role"]}</p>'
            f'<p class="st-blurb">{r["blurb"]}</p>{cta}</div></div></section>')

DOCK = ('<nav class="st-dock" aria-label="Jump to a role">'
        '<a class="st-dk st-dk-top" href="#top" aria-label="Back to top"><span class="st-dk-ic" style="font: 400 22px/1 Caveat, cursive; color: #fff">tin</span><span class="st-tip">Tin Le</span></a>'
        + ''.join(f'<a class="st-dk" href="#{r["id"]}" aria-label="{r["dockLabel"]}"><span class="st-dk-ic">{r["dock"]}</span><span class="st-tip">{r["dockLabel"]}</span></a>' for r in ROWS if r['dock'])
        + '</nav>')

INTRO = ('<header class="st-intro" id="top">'
         '<span class="st-av"><img src="/_blob/23c37e811ab58e300330f9e6721ba16c" alt="Tin Le"></span>'
         '<h1 class="st-h1">Tin Le</h1>'
         '<p class="st-tag">A designer who builds things to think<br>from Đà Lạt, made in Oregon.</p>'
         '<div class="st-btns"><button type="button" class="st-btn st-btn-dark" onClick="{{copy}}">{{touchLabel}}</button>'
         '<a class="st-btn st-btn-light" href="https://www.linkedin.com/in/letin08/" target="_blank" rel="noopener">Follow on LinkedIn</a></div>'
         '<p class="st-sign" aria-hidden="true">Tin Le</p>'
         '</header>')

CONTACT = ('<section class="st-contact" id="contact" aria-label="Contact">'
           '<h2 class="st-h2">Let’s work together</h2>'
           '<div class="st-form">'
           '<label class="st-f"><span>Name</span><input type="text" placeholder="Your name" onInput="{{setName}}"></label>'
           '<label class="st-f"><span>Email</span><input type="email" placeholder="you@company.com" onInput="{{setFrom}}"></label>'
           '<label class="st-f"><span>What can I help with?</span><select onChange="{{setKind}}"><option>Full-time role</option><option>Product design project</option><option>Teaching or a workshop</option><option>Something else</option></select></label>'
           '<a class="st-btn st-btn-dark st-submit" href="{{mailHref}}">Send</a>'
           '</div>'
           '<p class="st-thanks">Thank you for watching.</p>'
           '</section>')

BODY = ('<div class="st-root" style="--accent: {{accent}}; --accentBg: {{accentBg}}; --mr: {{mediaRadius}}">'
        '<div class="st-rail">' + DOCK + '</div>'
        + INTRO + ''.join(row(r) for r in ROWS) + CONTACT + '</div>')

CSS = r'''
body{margin:0}
sc-for, sc-if { display: contents; }
.st-root{position:relative;width:1440px;background:#fff;color:#000;font-family:Inter,system-ui,sans-serif;-webkit-font-smoothing:antialiased;padding:220px 0 140px;box-sizing:border-box}
.st-rail{position:absolute;left:20px;top:0;bottom:0;width:64px;z-index:5}
.st-dock{position:sticky;top:220px;display:flex;flex-direction:column;gap:6px;padding:10px 8px;border-radius:22px;background:#2b2b2d;box-shadow:0 1px 0 rgba(255,255,255,.08) inset,0 18px 40px -16px rgba(0,0,0,.45)}
.st-dk{position:relative;display:grid;place-items:center;width:48px;height:48px;border-radius:14px;text-decoration:none;transition:background-color .2s}
.st-dk:hover,.st-dk:focus-visible{background:rgba(255,255,255,.12);outline:none}
.st-dk-ic{display:grid;place-items:center;opacity:.92}
.st-mono{filter:brightness(0) invert(1)}
.st-tip{position:absolute;left:58px;top:50%;transform:translate(-4px,-50%);white-space:nowrap;padding:6px 10px;border-radius:8px;background:#2b2b2d;color:#fff;font-size:13px;font-weight:500;opacity:0;pointer-events:none;transition:opacity .15s,transform .15s}
.st-dk:hover .st-tip,.st-dk:focus-visible .st-tip{opacity:1;transform:translate(0,-50%)}
.st-intro{position:relative;margin-left:296px;width:848px;padding-bottom:80px}
.st-av{display:block;width:64px;height:64px;border-radius:50%;overflow:hidden;position:relative;background:#cfe2ff}
.st-av img{width:100%;height:100%;object-fit:cover;object-position:50% 25%;filter:grayscale(1) contrast(1.35) brightness(1.08);mix-blend-mode:multiply}
.st-av::after{content:"";position:absolute;inset:0;background:radial-gradient(circle,rgba(30,90,170,.55) 0 .9px,transparent 1.1px) 0 0/3px 3px;mix-blend-mode:screen;opacity:.7}
.st-h1{margin:30px 0 0;font:600 22px/1.2 'Inter Display',Inter,sans-serif;letter-spacing:-.01em}
.st-tag{margin:22px 0 0;font:600 20px/1.4 'Inter Display',Inter,sans-serif;color:#6b6b6b;letter-spacing:-.01em}
.st-btns{display:flex;gap:10px;margin-top:34px}
.st-btn{display:inline-flex;align-items:center;justify-content:center;height:38px;padding:0 16px;border-radius:8px;border:0;font:500 15px/1 Inter,sans-serif;text-decoration:none;cursor:pointer;transition:filter .15s,transform .15s}
.st-btn:active{transform:scale(.98)}
.st-btn-dark{background:#000;color:#fff}.st-btn-dark:hover{filter:brightness(1.6)}
.st-btn-light{background:#f2f2f2;color:#5a5a5a;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}.st-btn-light:hover{background:#ebebeb}
.st-sign{position:absolute;right:0;bottom:84px;margin:0;font:400 46px/1 Caveat,cursive;color:#8a8a8a;transform:rotate(-8deg)}
.st-row{display:grid;grid-template-columns:120px 848px 234px;column-gap:32px;padding-left:144px;margin-top:96px;align-items:start;scroll-margin-top:60px}
.st-year{margin:14px 0 0;text-align:right;font:500 15px/1 Inter,sans-serif;color:#a3a3a3;position:sticky;top:120px}
.st-stack{display:flex;flex-direction:column;gap:12px}
.st-media{margin:0;border-radius:var(--mr,14px);overflow:hidden;background:#f2f2f2;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}
.st-media img{display:block;width:100%;height:100%;object-fit:cover}
.st-locked{display:grid;place-items:center;text-align:center;color:#b0b0b0;background:#f5f5f5}
.st-lk-t{margin:8px 0 0;font:500 15px/1 Inter,sans-serif;color:#9a9a9a}
.st-lk-n{margin:8px 0 0;font:400 13px/1.4 Inter,sans-serif;color:#b8b8b8}
.st-textcard{display:grid;place-items:center;background:linear-gradient(160deg,#fff4ef,#ffe1d6);text-align:center;padding:40px;box-sizing:border-box}
.st-tc-big{margin:0;font:600 44px/1.1 'Inter Display',Inter,sans-serif;letter-spacing:-.02em;color:#3b1d12}
.st-tc-small{margin:18px 0 0;font:500 16px/1.5 Inter,sans-serif;color:#9a5a43}
.st-info{position:sticky;top:120px}
.st-info-in{padding-top:4px}
.st-logo{display:grid;place-items:center;width:48px;height:48px;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08),0 1px 2px rgba(0,0,0,.04)}
.st-name{margin:18px 0 0;font:600 20px/1.2 'Inter Display',Inter,sans-serif;letter-spacing:-.01em}
.st-role{margin:6px 0 0;font:500 15px/1.3 Inter,sans-serif;color:#a3a3a3}
.st-blurb{margin:18px 0 0;font:400 15px/1.45 Inter,sans-serif;color:#141414}
.st-open,.st-pill{display:inline-flex;align-items:center;gap:6px;margin-top:20px;height:30px;padding:0 12px;border-radius:7px;font:500 14px/1 Inter,sans-serif;text-decoration:none}
.st-open{background:var(--accentBg,#e6f3ff);color:var(--accent,#1a8cff);transition:filter .15s}.st-open:hover{filter:brightness(.96)}
.st-pill{background:#f2f2f2;color:#9a9a9a}
.st-contact{margin:160px 0 0 296px;width:848px}
.st-h2{margin:0;font:600 28px/1.2 'Inter Display',Inter,sans-serif;letter-spacing:-.02em}
.st-form{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:28px;max-width:640px}
.st-f{display:flex;flex-direction:column;gap:8px;font:500 13px/1 Inter,sans-serif;color:#6b6b6b}
.st-f:nth-child(3){grid-column:1 / -1}
.st-f input,.st-f select{height:42px;border-radius:9px;border:0;background:#f4f4f4;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06);padding:0 12px;font:400 15px/1 Inter,sans-serif;color:#141414;outline:none}
.st-f input:focus,.st-f select:focus{box-shadow:inset 0 0 0 2px #1a8cff;background:#fff}
.st-submit{grid-column:1 / -1;justify-self:start;height:42px;padding:0 22px}
.st-thanks{margin:120px 0 0;font:500 15px/1 Inter,sans-serif;color:#a3a3a3}
a:focus-visible,button:focus-visible{outline:2px solid #1a8cff;outline-offset:3px}
'''
props = {"accent": {"editor": "color", "default": "#1a8cff", "section": "Style"},
         "accentBg": {"editor": "color", "default": "#e6f3ff", "section": "Style"},
         "mediaRadius": {"editor": "range", "default": 14, "min": 0, "max": 32, "step": 1, "unit": "px", "section": "Style"},
         "$preview": {"width": 1440, "height": 9000}}
attr = json.dumps(props, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
JS = r'''class Component extends DCLogic {
  constructor(props) { super(props); this.state = { copied: false, name: '', from: '', kind: 'Full-time role' }; }
  componentWillUnmount() { clearTimeout(this.t); }
  renderVals() {
    const st = this.state;
    const body = `Hi Tin,%0D%0A%0D%0A${encodeURIComponent(st.kind)}%0D%0A%0D%0A— ${encodeURIComponent(st.name || '')} ${encodeURIComponent(st.from || '')}`;
    return {
      accent: this.props.accent ?? '#1a8cff', accentBg: this.props.accentBg ?? '#e6f3ff', mediaRadius: (this.props.mediaRadius ?? 14) + 'px',
      touchLabel: st.copied ? 'Email copied' : 'Get in touch',
      copy: () => { try { navigator.clipboard && navigator.clipboard.writeText('tinbacme@gmail.com'); } catch (e) {} this.setState({ copied: true }); clearTimeout(this.t); this.t = setTimeout(() => this.setState({ copied: false }), 1600); },
      setName: (e) => this.setState({ name: e.target.value }), setFrom: (e) => this.setState({ from: e.target.value }), setKind: (e) => this.setState({ kind: e.target.value }),
      mailHref: `mailto:tinbacme@gmail.com?subject=${encodeURIComponent('Hello from your portfolio: ' + st.kind)}&body=${body}`,
    };
  }
}'''
out = ('<!doctype html>\n<html>\n<head><meta charset="utf-8"><script src="./support.js"></script></head>\n<body>\n'
       '<!-- Tin Le · portfolio in the stuart.re style: logo dock, quiet intro, timeline of roles with stacked media, contact form -->\n<x-dc>\n<helmet>\n'
       '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Caveat:wght@400;600&amp;display=swap">\n'
       '<style>' + CSS + '</style>\n</helmet>\n' + BODY + '\n</x-dc>\n'
       "<script type=\"text/x-dc\" data-dc-script data-props='" + attr + "'>\n" + JS + '\n</script>\n</body>\n</html>\n')
out = ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in out)
open(S + 'canvas4/project/TinHome-Stuart.dc.html', 'w').write(out)
open(S + 'stuart_logic.js', 'w').write('class DCLogic{}\n' + JS)
print('ok', len(out))
