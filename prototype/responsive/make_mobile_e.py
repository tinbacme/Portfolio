"""Mobile option E: phone version of Tablet C's greeting band + prose intro (logo pills inline)."""
import sys, re, json, html
S = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/'
src = S + 'canvas4/project/TinHome-Tablet-C.dc.html'
out = S + 'canvas4/project/TinHome-Mobile-E.dc.html'
tune = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}
s = open(src).read()

OLD_T = 'Homepage · Tablet option C · greeting band + prose intro (kenjilambert-style)'
NEW_T = 'Homepage · Mobile option E · greeting + prose intro with logo pills (from Tablet C)'
assert s.count(OLD_T) == 2
s = s.replace(OLD_T, NEW_T)

a = s.index('/* ' + NEW_T)
b = s.index('/* prose intro: logos live inside the sentence */')
MOBILE = '/* ' + NEW_T + ' — layout option preview (copy of TinHome-Tablet-C) */\n' + '''
  header{padding-left:20px !important;padding-right:20px !important}
  #top,main,#about,footer{padding-left:20px !important;padding-right:20px !important}
  .th-trail{display:block !important;width:100%% !important}
  main{gap:48px !important;padding-top:8px !important}
  main > div > [style*="aspect-ratio"]{width:100%% !important}
  main p{width:auto !important;max-width:100%%}
  main > div > div:first-child{flex-direction:column !important;gap:2px !important}
  .th-shots{grid-template-columns:1fr !important}
  .th-side{grid-template-columns:1fr 1fr !important;grid-template-rows:none !important}
  .th-side > .th-small:only-child{grid-column:1 / -1;height:auto !important;aspect-ratio:16 / 10 !important}
  .th-meta{grid-template-columns:1fr !important;gap:2px !important}
  #about{padding-top:72px !important;padding-bottom:96px !important;gap:28px !important;justify-content:center !important}
  #about .ab-board{zoom:.58}
  #about > div:first-child{flex-basis:auto !important}
  footer{flex-wrap:wrap;gap:12px}
  #top{display:flex !important;flex-direction:column !important;justify-content:flex-start !important;min-height:auto !important;padding-top:%(pt)spx !important;padding-bottom:56px !important;gap:16px !important}
  #top p[style*="font-size: 46px"]{font-size:44px !important;line-height:1.1}
  .th-prose{max-width:100%% !important}

''' % dict(pt=tune.get('pt', 210))
s = s[:a] + MOBILE + s[b:]

# phone-sized prose + pills, appended after Tablet C's pill rules
PHONE = '''
/* phone sizing for the prose pills */
.th-prose{font-size:%(fs)spx !important;line-height:%(lh)s !important}
.th-prose .lg,.th-prose .lg-frame{width:20px !important;height:20px !important}
.th-prose .th-co{margin:0 3px;vertical-align:-5px}
''' % dict(fs=tune.get('fs', 19), lh=tune.get('lh', 2.25))
s = s.replace('</style>\n</helmet>', PHONE + '</style>\n</helmet>', 1)
assert PHONE in s

# pills: phone-sized inline padding/gap/label so the canvas tweak panel shows the real values
i = s.index('<div class="th-prose"'); j = s.index('</div>', i)
seg = s[i:j]
seg = re.sub(r'padding-top: \d+px; padding-bottom: \d+px; padding-right: \d+px; padding-left: \d+px',
             'padding-top: 4px; padding-bottom: 4px; padding-right: 12px; padding-left: 10px', seg)
seg = seg.replace('gap: 10px;', 'gap: 7px;')
seg = seg.replace('<p style="margin: 0; font-size: 20px; color: #6e6e6e">', '<p style="margin: 0; font-size: 16px; color: #6e6e6e">')
assert seg.count('padding-right: 12px') == 3 and seg.count('font-size: 16px') == 3, (seg.count('padding-right: 12px'), seg.count('font-size: 16px'))
s = s[:i] + seg + s[j:]

m = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
P = json.loads(html.unescape(m.group(2)))
for k, v in {'logoSize': tune.get('ls', 130), 'sizeWave': tune.get('sw', 1.0), 'waveX': tune.get('wx', 0.26), 'waveY': tune.get('wy', 0.16),
             'logoX': tune.get('wx', 0.26), 'logoY': tune.get('wy', 0.16)}.items():
    P[k]['default'] = v
P['$preview'] = {"width": 390, "height": P.get('$preview', {}).get('height', 4600)}
attr = json.dumps(P, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
s = s[:m.start()] + "data-props='" + attr + "'>" + s[m.end():]
open(out, 'w').write(s)
print('ok')
