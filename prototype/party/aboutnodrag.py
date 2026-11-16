"""About page: photos and logos on the experience cards can't be dragged out (no ghost image).
usage: aboutnodrag.py <TinHome-About.dc.html>"""
import sys, re
p=sys.argv[1]; s=open(p).read()
a=s.index('<section class="bd-wrap'); b=s.index('</section>',a)
sec=s[a:b]; n=0
def fix(m):
    global n
    t=m.group(0)
    if 'draggable=' in t: return t
    n+=1; return t[:4]+' draggable="false"'+t[4:]
sec=re.sub(r'<img\b[^>]*>',fix,sec); s=s[:a]+sec+s[b:]
o='.bd-wrap :focus:not(:focus-visible){outline:none}'
assert s.count(o)==1
s=s.replace(o,o+'\n.bd-wrap img,.bd-wrap svg,.bd-wrap a{-webkit-user-drag:none;user-drag:none}')
open(p,'w').write(s); print('ok', n)
