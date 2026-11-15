"""Graduation cap on the second UO dock item (BS Industrial Design) and on the UO BS row's logo tile. usage: gradcap.py <TinHome-Stuart.dc.html>"""
import sys, re
p = sys.argv[1]; s = open(p).read()
CAP = lambda cls: (f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 1.5 8 12 13l10.5-5z" fill="currentColor"></path>'
                   '<path d="M6 10.6V15c0 1.7 2.7 3 6 3s6-1.3 6-3v-4.4L12 13.5z" fill="currentColor"></path>'
                   '<path d="M21 8.4v5.2" stroke="currentColor" stroke-width="1.4" stroke-linecap="round"></path><circle cx="21" cy="14.6" r="1.3" fill="currentColor"></circle></svg>')
a = s.index('<nav class="st-dock"'); b = s.index('</nav>', a); dock = s[a:b]
uo = [m for m in re.finditer(r'<a class="st-dk" href="#uo-teach" aria-label="University of Oregon">(.*?)</a>', dock)]
assert len(uo) == 2, len(uo)
m = uo[1]; inner = m.group(1)
inner = inner.replace('<span class="st-dk-ic">', '<span class="st-dk-ic st-capped">', 1)
inner = inner.replace('</span>', CAP('st-cap') + '</span>', 1) if inner.count('</span>') == 1 else inner[:inner.rindex('</span>')] + CAP('st-cap') + inner[inner.rindex('</span>'):]
new = f'<a class="st-dk" href="#uo-bs" aria-label="University of Oregon, BS Industrial Design">{inner}</a>'
dock = dock[:m.start()] + new + dock[m.end():]
s = s[:a] + dock + s[b:]
# row logo tile badge
i = s.index('id="uo-bs"'); j = s.index('<span class="st-logo">', i); k = s.index('<span class="st-lg">', j)
s = s[:k] + '<span class="st-capbadge">' + CAP('') + '</span>' + s[k:]
CSS = ('\n/* graduation cap on the BS Industrial Design marks */\n'
       '.st-capped{position:relative}\n'
       '.st-cap{position:absolute;top:-8px;right:-10px;width:14px;height:14px;color:#fff;transform:rotate(14deg);filter:drop-shadow(0 1px 1px rgba(0,0,0,.35))}\n'
       '.st-capbadge{position:absolute;top:-7px;right:-7px;z-index:2;display:grid;place-items:center;width:20px;height:20px;border-radius:50%;background:#fff;color:#2b2b2d;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08),0 1px 3px rgba(0,0,0,.12);transform:rotate(12deg)}\n'
       '.st-capbadge svg{width:13px;height:13px}\n')
anchor = '.st-defs{position:absolute;width:0;height:0;overflow:hidden}'
assert s.count(anchor) == 1; s = s.replace(anchor, anchor + CSS)
open(p, 'w').write(s); print('ok')
