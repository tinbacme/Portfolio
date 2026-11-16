"""Stuart page: rows follow the nav order (Microsoft, Salesforce, UO teaching, 2U, Luxium, UO BS); anchor jumps leave top room and scroll smoothly; the top logo stays fixed like the nav.
usage: stuartorder.py <TinHome-Stuart.dc.html>"""
import sys, re
p = sys.argv[1]; s = open(p).read()
rows = list(re.finditer(r'<section class="st-row[^"]*" id="([^"]+)".*?</section>', s, re.S))
ids = [m.group(1) for m in rows]
want = ['microsoft', 'salesforce', 'uo-teach', '2u', 'luxium', 'uo-bs']
assert sorted(ids) == sorted(want), ids
start, end = rows[0].start(), rows[-1].end()
between = s[rows[0].end():rows[1].start()]  # whatever separates rows (usually nothing)
assert all(s[rows[i].end():rows[i + 1].start()] == between for i in range(len(rows) - 1)), 'unexpected content between rows'
by = {m.group(1): m.group(0) for m in rows}
s = s[:start] + between.join(by[k] for k in want) + s[end:]
# room on top when jumping to a role, and smooth scrolling
a = '.st-row{display:grid;grid-template-columns:240px 848px 240px;column-gap:32px;margin-top:80px;align-items:start;scroll-margin-top:48px}'
assert s.count(a) == 1
s = s.replace(a, a.replace('scroll-margin-top:48px', 'scroll-margin-top:120px') + '\nhtml{scroll-behavior:smooth}\n@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}}')
# the tin logo stays put while scrolling, like the nav (rail is at 47px, logo offset -10px)
old = '<a class="st-toplogo" href="#top" aria-label="Tin Le, back to top" style="left: -10px; top: 117px; position: absolute">'
assert s.count(old) == 1
s = s.replace(old, '<a class="st-toplogo" href="#top" aria-label="Tin Le, back to top" style="left: 37px; top: 117px; position: fixed; z-index: 20">')
open(p, 'w').write(s); print('ok', ids, '->', want)
