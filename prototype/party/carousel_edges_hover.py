"""Carousel ends: each side's blur + arrow fade in only while the pointer is on that side (always on for touch screens). CSS only."""
import sys
p = sys.argv[1]; s = open(p).read()
def side(x):
    on = [f'.bd-car:has(.bd-edge-{x}:hover) .bd-edge-{x}', f'.bd-car:has(.bd-edge-{x}:hover) .bd-nav-{x}',
          f'.bd-car:has(.bd-nav-{x}:hover) .bd-edge-{x}', f'.bd-car:has(.bd-nav-{x}:hover) .bd-nav-{x}',
          f'.bd-car:has(.bd-nav-{x}:focus-visible) .bd-edge-{x}', f'.bd-car:has(.bd-nav-{x}:focus-visible) .bd-nav-{x}']
    return ','.join(on) + '{opacity:1}'
CSS = ('\n/* ends: blur + arrow show only while hovering that side */\n'
       '.bd-car .bd-edge,.bd-car .bd-nav{opacity:0;transition:opacity .35s ease}\n'
       '.bd-car .bd-edge{pointer-events:auto}\n' + side('l') + '\n' + side('r') + '\n'
       '@media (hover: none){.bd-car .bd-edge,.bd-car .bd-nav{opacity:1}.bd-car .bd-edge{pointer-events:none}}\n')
assert s.count('</style>\n</helmet>') == 1
s = s.replace('</style>\n</helmet>', CSS + '</style>\n</helmet>', 1)
open(p, 'w').write(s); print('ok')
