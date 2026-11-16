"""Stuart page: the added Microsoft photo scales with its column (up to 1200px), and the current nav tile is white glass too.
usage: stuartwhite.py <TinHome-Stuart.dc.html>"""
import sys
p=sys.argv[1]; s=open(p).read()
def rep(o,n):
    global s; assert s.count(o)==1,(o[:80],s.count(o)); s=s.replace(o,n)
rep('width="1200" height="780" style="width: 848px; height: 550px; position: absolute;', 'width="1200" height="780" style="width: 100%; max-width: 1200px; height: auto; aspect-ratio: 1200 / 780; object-fit: cover; position: absolute;')
CSS = '''
/* nav tiles: every tile is plain white glass, the current one too; the dark marker and branch show where you are */
.sv-nav a.on .l9-fx{background:linear-gradient(150deg,rgba(255,255,255,.78) 0%,rgba(255,255,255,.42) 48%,rgba(255,255,255,.62) 100%)!important}
.sv-nav a.on .l9-ic{filter:none}
.sv-nav a.on .l9-shine{background:radial-gradient(120% 70% at 30% 0%,rgba(255,255,255,.9) 0%,rgba(255,255,255,.25) 38%,rgba(255,255,255,0) 60%),radial-gradient(90% 60% at 80% 110%,rgba(255,255,255,.35),rgba(255,255,255,0) 60%);box-shadow:inset 1.5px 1.5px 1px rgba(255,255,255,.95),inset -1px -1px 1px rgba(255,255,255,.55),inset 0 0 0 1px rgba(0,0,0,.07),inset 0 -6px 10px -6px rgba(0,0,0,.12)}
.sv-nav a.on .l9-tile{box-shadow:0 1px 1px rgba(0,0,0,.06),0 10px 22px -8px rgba(0,0,0,.32),0 2px 5px -2px rgba(0,0,0,.14)!important}
'''
i=s.rindex('</style>'); s=s[:i]+CSS+s[i:]
open(p,'w').write(s); print('ok')
