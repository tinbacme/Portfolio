import json, sys, os
S='/tmp/claude-0/-home-user/ab4b1994-dd78-54cb-abb4-90a167a3ba6b/scratchpad/'
local = len(sys.argv) > 1 and sys.argv[1] == 'local'
tpl=open(S+'kenji/tpl.html').read()
logo=open(S+'varg/logo-paths.txt').read().replace('\n','')
ids=json.load(open(S+'kenji/ids.json')) if os.path.exists(S+'kenji/ids.json') else {}
names=['k-matcha','k-plane','k-laptop','k-caphe','k-lamp','k-search','k-suitcase','k-cloud','ic3-marker','ic3-pencil']
fixed={'ic3-marker':'79bb50bb238a7b2d4851798d6f37e28a','ic3-pencil':'ba54284045a3441f2243c3763409fd93'}
def src(n):
    if local:
        f={'ic3-marker':'parts/ic-marker.png','ic3-pencil':'parts/ic-pencil.png'}.get(n, f'parts/{n}.png')
        return 'file://'+S+f
    return '/_blob/'+(fixed.get(n) or ids[n])
avail=[n for n in names if (local and os.path.exists(S+('parts/'+n+'.png' if n.startswith('k-') else 'parts/ic-'+n[4:]+'.png'))) or (not local and (n in fixed or n in ids))]
objs=''.join(f'<img src="{src(n)}" alt="">' for n in avail)
badge='file://'+S+'kit/nb-matcha.webp' if local else '/_blob/925284f08d8587128bce2a50c9d0f2e9'
# about paragraph, word by word
about=[('<span class="star">*</span>',''),("I’m Tin Le, a senior designer at",''),('Microsoft AI','c-blue'),('who moves between',''),('search,','c-terra'),('AI,','c-blue'),
       ('<em>industrial design</em>',''),('and','') ,('<em>systems</em>',''),('— always in love with craft. Before that I designed at',''),('Salesforce,','c-blue'),
       ('and I studied industrial design at the',''),('University of Oregon.','c-green'),('Make yourself at',''),('<span class="pill">home</span>!','')]
words=[]
for txt,c in about:
    parts=[txt] if txt.startswith('<') else txt.split(' ')
    for w in parts:
        words.append(f'<span class="w {c}">{w}</span>' if c else f'<span class="w">{w}</span>')
aboutH=' '.join(words)
logos=''.join(f'<span>{x}</span>' for x in ['Microsoft AI','Windows','Bing','Salesforce','University of Oregon','Đà Lạt','Seattle']*2)
big=''.join('<span>Featured work</span><span class="ast">*</span>' for _ in range(6))
foot=''.join('<span>Say hi</span><span class="ast">*</span><span>Tin Le</span><span class="ast">*</span>' for _ in range(4))
out=(tpl.replace('%%LOGO%%',logo).replace('%%OBJS%%',objs).replace('%%BADGE%%',badge).replace('%%ABOUT%%',aboutH)
     .replace('%%LOGOS%%',logos).replace('%%BIG%%',big).replace('%%FOOTBIG%%',foot))
assert '%%' not in out
os.makedirs(S+'kenji/project',exist_ok=True)
open(S+('kenji/local.dc.html' if local else 'kenji/project/VariationJobPoint.dc.html'),'w').write(out)
print('objs',len(avail))
