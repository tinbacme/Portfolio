"""Make tablet/mobile layout options as separate canvas boards (copies of the homepage + layout overrides)."""
import sys, re, json, html
D = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/canvas4/project/'
src = open(D + 'TinHome-2goy.dc.html').read()
tune = json.loads(sys.argv[1]) if len(sys.argv) > 1 else {}

SHARED = {
 'tablet': '''
  #top,main,#about,footer{padding-left:48px !important;padding-right:48px !important}
  main{gap:64px !important}
  main > div > [style*="aspect-ratio"]{width:100% !important}
  main p{width:auto !important;max-width:100%}
''',
 'mobile': '''
  header{padding-left:20px !important;padding-right:20px !important}
  #top,main,#about,footer{padding-left:20px !important;padding-right:20px !important}
  .th-trail{display:block !important;width:100% !important}
  #top p[style*="font-size: 46px"]{font-size:38px !important}
  #top > div{width:100%}
  main{gap:48px !important;padding-top:8px !important}
  main > div > [style*="aspect-ratio"]{width:100% !important}
  main p{width:auto !important;max-width:100%}
  main > div > div:first-child{flex-direction:column !important;gap:2px !important}
  .th-shots{grid-template-columns:1fr !important}
  .th-side{grid-template-columns:1fr 1fr !important;grid-template-rows:none !important}
  .th-side > .th-small:only-child{grid-column:1 / -1;height:auto !important;aspect-ratio:16 / 10 !important}
  .th-meta{grid-template-columns:1fr !important;gap:2px !important}
  #about{padding-top:72px !important;padding-bottom:96px !important;gap:28px !important;justify-content:center !important}
  #about .ab-board{zoom:.58}
  #about > div:first-child{flex-basis:auto !important}
  footer{flex-wrap:wrap;gap:12px}
''',
}
V = {
 'TinHome-Tablet-A': dict(w=834, title='Homepage · Tablet option A · two columns, smaller drawing', kind='tablet',
   css='''  #top{min-height:640px !important}
  #top > div:not(.th-trail){max-width:52%}
''', props={'logoSize': 210, 'sizeWave': 1.45, 'waveX': 0.76, 'waveY': 0.5, 'logoX': 0.76, 'logoY': 0.5}),
 'TinHome-Tablet-B': dict(w=834, title='Homepage · Tablet option B · drawing on top, intro below', kind='tablet',
   css='''  #top{min-height:auto !important;justify-content:flex-start !important;padding-top:470px !important;padding-bottom:72px !important}
''', props={'logoSize': 250, 'sizeWave': 1.5, 'waveX': 0.5, 'waveY': tune.get('tbY', 0.27), 'logoX': 0.5, 'logoY': tune.get('tbY', 0.27)}),
 'TinHome-Mobile-A': dict(w=390, title='Homepage · Mobile option A · drawing first, then intro', kind='mobile',
   css='''  #top{min-height:auto !important;justify-content:flex-start !important;padding-top:330px !important;padding-bottom:56px !important;gap:18px !important}
''', props={'logoSize': 150, 'sizeWave': 1.65, 'waveX': 0.5, 'waveY': tune.get('maY', 0.2), 'logoX': 0.5, 'logoY': tune.get('maY', 0.2)}),
 'TinHome-Mobile-B': dict(w=390, title='Homepage · Mobile option B · intro first, then drawing', kind='mobile',
   css='''  #top{min-height:auto !important;justify-content:flex-start !important;padding-top:48px !important;padding-bottom:330px !important;gap:18px !important}
''', props={'logoSize': 150, 'sizeWave': 1.65, 'waveX': 0.5, 'waveY': tune.get('mbY', 0.8), 'logoX': 0.5, 'logoY': tune.get('mbY', 0.8)}),
}
for name, v in V.items():
    s = src
    css = f"\n/* {v['title']} — layout option preview (copy of TinHome-2goy) */\n" + SHARED[v['kind']] + v['css']
    s = s.replace('</style>', css + '</style>', 1)
    m = re.search(r"data-props=(['\"])(.*?)\1>", s, re.S)
    P = json.loads(html.unescape(m.group(2)))
    for k, val in v['props'].items(): P[k]['default'] = val
    P['$preview'] = {"width": v['w'], "height": P.get('$preview', {}).get('height', 4600)}
    attr = json.dumps(P, ensure_ascii=False).replace('&', '&amp;').replace("'", '&#39;')
    s = s[:m.start()] + "data-props='" + attr + "'>" + s[m.end():]
    s = s.replace('<x-dc>', f"<!-- {v['title']} · layout option preview, copy of TinHome-2goy.dc.html -->\n<x-dc>", 1)
    open(D + name + '.dc.html', 'w').write(s)
json.dump({k: {'w': v['w'], 'title': 'Tin Le · ' + v['title']} for k, v in V.items()}, open(D + '../variants_meta.json', 'w'))
print('ok')
