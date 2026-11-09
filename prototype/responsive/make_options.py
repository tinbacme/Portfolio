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
 'TinHome-Tablet-C': dict(w=834, title='Homepage · Tablet option C · greeting band, info in a 2×2 grid', kind='tablet',
   css='''  #top{display:grid !important;grid-template-columns:1fr 1fr !important;column-gap:48px;row-gap:32px;align-content:start;min-height:auto !important;padding-top:96px !important;padding-bottom:88px !important}
  #top > div:first-child{grid-column:1 / -1;min-height:250px;display:flex;align-items:center}
  #top p[style*="font-size: 46px"]{font-size:72px !important}
''', props={'logoSize': 170, 'sizeWave': 1.5, 'waveX': 0.75, 'waveY': tune.get('tcY', 0.3), 'logoX': 0.75, 'logoY': tune.get('tcY', 0.3)}),
 'TinHome-Tablet-D': dict(w=834, title='Homepage · Tablet option D · two columns + work as a 2-column grid', kind='tablet',
   css='''  #top{min-height:640px !important}
  #top > div:not(.th-trail){max-width:52%}
  main{display:grid !important;grid-template-columns:1fr 1fr;column-gap:24px !important;row-gap:48px !important;align-items:start}
  main .th-shots{grid-template-columns:1fr !important}
  main .th-side{grid-template-columns:1fr 1fr !important;grid-template-rows:none !important}
  main .th-side > .th-small:only-child{grid-column:1 / -1;height:auto !important;aspect-ratio:16 / 10 !important}
  main .th-meta{grid-template-columns:1fr !important;gap:2px !important}
  main > div > div:first-child{flex-direction:column !important;gap:2px !important}
''', props={'logoSize': 210, 'sizeWave': 1.45, 'waveX': 0.76, 'waveY': 0.5, 'logoX': 0.76, 'logoY': 0.5}),
 'TinHome-Mobile-C': dict(w=390, title='Homepage · Mobile option C · compact: small waving avatar beside the greeting', kind='mobile',
   css='''  #top{min-height:auto !important;justify-content:flex-start !important;padding-top:40px !important;padding-bottom:48px !important;gap:16px !important}
  #top > div:first-child{min-height:150px;display:flex;align-items:center;padding-right:150px;box-sizing:border-box}
  #top p[style*="font-size: 46px"]{font-size:34px !important;line-height:1.1}
''', props={'logoSize': 95, 'sizeWave': 1.6, 'waveX': 0.73, 'waveY': tune.get('mcY', 0.16), 'logoX': 0.5, 'logoY': tune.get('mcY', 0.16)}),
 'TinHome-Mobile-D': dict(w=390, title='Homepage · Mobile option D · drawing first + swipeable work cards', kind='mobile',
   css='''  #top{min-height:auto !important;justify-content:flex-start !important;padding-top:330px !important;padding-bottom:56px !important;gap:18px !important}
  main{flex-direction:row !important;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px !important;padding-bottom:24px !important;scrollbar-width:none}
  main > *{flex:0 0 84%;scroll-snap-align:start}
''', props={'logoSize': 150, 'sizeWave': 1.65, 'waveX': 0.5, 'waveY': tune.get('maY', 0.2), 'logoX': 0.5, 'logoY': tune.get('maY', 0.2)}),
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
