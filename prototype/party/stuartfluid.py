"""Stuart page: fluid layout. Media column grows from 848 up to 1200px (page caps at 1792 and centres), images keep their
848x524 shape; below 1180 the info moves under the images; below 760 one column, nav hidden. Also: nav tiles are plain white
glass (no coloured glow behind the logos). usage: stuartfluid.py <TinHome-Stuart.dc.html>"""
import sys
p = sys.argv[1]; s = open(p).read()
def rep(o, n, c=1):
    global s
    assert s.count(o) == c, (o[:80], s.count(o)); s = s.replace(o, n)
rep('position: absolute; left: max(0px, calc((100% - 1440px) / 2)); top: 0px; right: auto; margin-left: 0px; margin-right: 0px">',
    'position: absolute; left: 0px; right: 0px; top: 0px; max-width: 1792px; margin-left: auto; margin-right: auto">')
rep('body{margin:0;background:#fff} /* wide screens: the 1440 page sits centred on white */', 'body{margin:0;background:#fff} /* wide screens: the page grows to 1792 (1200px images), then sits centred on white */')
CSS = '''
/* fluid: the image column grows with the window up to 1200px; images keep their 848 x 524 shape */
.st-root{width:auto;min-width:0}
.st-row{grid-template-columns:240px minmax(0,1200px) 240px}
.st-intro{width:auto;max-width:1200px;margin-right:272px}
.st-media{height:auto;aspect-ratio:848/524}
/* nav tiles: plain white glass, no coloured glow behind the logos */
.sv-nav .l9-glow{display:none}
/* narrower windows: the role info moves under its images */
@media (max-width:1180px){
  .st-row{grid-template-columns:240px minmax(0,1fr)}
  .st-row>.st-info{grid-column:2;position:static;margin-top:20px}
  .st-intro{margin-right:0}
}
/* phones: one column, the role nav steps aside (the logo still takes you home) */
@media (max-width:760px){
  .st-root{padding:120px 16px 96px}
  .st-row{grid-template-columns:minmax(0,1fr);margin-top:56px}
  .st-row>.st-stack,.st-row>.st-info{grid-column:1}
  .st-intro{margin-left:0}
  .sv-nav{display:none!important}
  .st-toplogo{top:20px!important;width:48px!important;height:48px!important}
  .st-btns{flex-wrap:wrap}
  .st-sig-svg{display:none}
  .st-form{width:100%;max-width:359px}
}
'''
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
open(p, 'w').write(s); print('ok')
