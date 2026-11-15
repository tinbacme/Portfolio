"""Add V5 numbered index, V6 accent tick, V7 year ledger to the nav variations board (patches the latest file in place).
usage: navvars2.py <Piece-navvars.dc.html>"""
import sys
p = sys.argv[1]; s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (old[:80], s.count(old)); s = s.replace(old, new)

UO, SF = '/_blob/00e0e1ec841a28c4e0055e4a6738e6b1', '/_blob/ac43d25c19be4e522f4bd492e1c090ab'
MS = ('<svg viewBox="0 0 20 20" width="15" height="15" aria-hidden="true"><rect x="0" y="0" width="9" height="9" fill="#f25022"></rect>'
      '<rect x="11" y="0" width="9" height="9" fill="#7fba00"></rect><rect x="0" y="11" width="9" height="9" fill="#00a4ef"></rect>'
      '<rect x="11" y="11" width="9" height="9" fill="#ffb900"></rect></svg>')
LOGO = ['<span class="nv-tin" style="font-size: 18px">tin</span>', MS, f'<img src="{UO}" alt="" width="17" height="14">',
        '<span class="nv-2u" style="font-size: 11px">2U</span>', f'<img src="{SF}" alt="" width="20" height="14">']
ITEMS = [('Home', '#top'), ('Microsoft AI', '#microsoft'), ('University of Oregon', '#uo-teach'), ('2U', '#2u'), ('Salesforce', '#salesforce')]
YEARS = ['&#8212;', '2022&#8211;now', '2023&#8211;now', '2021&#8211;', '2017&#8211;22']
PAST = [False, False, False, True, True]

v5 = ''.join(f'<a class="{{{{E{i}}}}}" href="{h}" onClick="{{{{pickE{i}}}}}"><span class="n5-n">0{i+1}</span><span class="n5-tx">{l}</span></a>' for i, (l, h) in enumerate(ITEMS))
v6 = ''.join(f'<a class="{{{{F{i}}}}}" href="{h}" onClick="{{{{pickF{i}}}}}"><span class="t6-ic">{LOGO[i]}</span><span class="t6-tx">{l}</span></a>' for i, (l, h) in enumerate(ITEMS))
v7 = ''.join(f'<a class="{{{{G{i}}}}}{" g7-past" if PAST[i] else ""}" href="{h}" onClick="{{{{pickG{i}}}}}"><span class="g7-dot" aria-hidden="true"></span><span class="g7-tx">{l}</span><span class="g7-yr">{YEARS[i]}</span></a>' for i, (l, h) in enumerate(ITEMS))

def col(tag, title, sub, inner):
    return (f'\n  <section class="nv-col nv-row2"><p class="nv-k">{tag}</p><h2 class="nv-t">{title}</h2><p class="nv-s">{sub}</p>'
            f'<div class="nv-stage st-white">{inner}</div></section>')
NEW = (col('V5', 'Numbered index', 'From Zara on Mobbin: a quiet numbered list in small caps. The current page goes bold and black.',
           f'<nav class="n5" aria-label="Site, version 5">{v5}</nav>')
     + col('V6', 'Accent tick', 'From Microsoft Copilot on Mobbin: gray names with a short tick in that company&#8217;s color on the current one. Logos stay gray until active.',
           f'<nav class="t6" aria-label="Site, version 6"><span class="t6-tick" aria-hidden="true" style="transform: translateY({{{{fY}}}}); background-color: {{{{fColor}}}}"></span>{v6}</nav>')
     + col('V7', 'Year ledger', 'From Aino Agency on Mobbin: name and years in two columns, like a tiny resume. Roles you hold now are black, past ones gray.',
           f'<nav class="g7" aria-label="Site, version 7"><div class="g7-head" aria-hidden="true"><span>Work</span><span>Years</span></div>{v7}</nav>'))
rep('</section>\n</div>\n</x-dc>', '</section>' + NEW + '\n</div>\n</x-dc>')

CSS = '''
/* row 2 */
.nv-row2{margin-top:32px}

/* V5: numbered index */
.n5{position:absolute;left:32px;top:56px;display:flex;flex-direction:column;gap:4px}
.n5 a{display:flex;align-items:baseline;gap:10px;height:30px;font:500 12px/30px 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;color:#9a9a9a;transition:color .2s}
.n5-n{display:inline-block;padding:0 4px;border-left:1px solid #cfcfcf;border-right:1px solid #cfcfcf;line-height:12px;font-size:11px;color:#b3b3b3;transition:color .2s,border-color .2s}
.n5 a:hover{color:#000}
.n5 a.on{color:#000;font-weight:600}.n5 a.on .n5-n{color:#000;border-color:#000}

/* V6: accent tick */
.t6{position:absolute;left:32px;top:56px;display:flex;flex-direction:column;gap:4px;padding-left:16px}
.t6-tick{position:absolute;left:0;top:11px;width:3px;height:18px;border-radius:2px;transition:transform .45s cubic-bezier(.6,0,.2,1),background-color .45s}
.t6 a{display:flex;align-items:center;gap:10px;height:40px}
.t6-ic{flex:none;display:grid;place-items:center;width:20px;height:20px;color:#000;filter:grayscale(1);opacity:.4;transition:filter .3s,opacity .3s}
.t6-tx{font:500 15px/1 Inter,sans-serif;color:#9a9a9a;white-space:nowrap;transition:color .2s}
.t6 a:hover .t6-tx{color:#000}.t6 a:hover .t6-ic{opacity:.75}
.t6 a.on .t6-tx{color:#000;font-weight:600}.t6 a.on .t6-ic{filter:none;opacity:1}

/* V7: year ledger */
.g7{position:absolute;left:32px;right:32px;top:56px;font:400 12px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.04em;text-transform:uppercase}
.g7-head{display:flex;justify-content:space-between;padding:0 0 12px 14px;color:#b3b3b3;border-bottom:1px solid #ececec}
.g7 a{display:flex;align-items:center;height:38px;border-bottom:1px solid #f2f2f2;color:#000;transition:color .2s}
.g7 a.g7-past{color:#b3b3b3}
.g7-dot{flex:none;width:6px;height:6px;margin-right:8px;border-radius:50%;background:currentColor;transform:scale(0);transition:transform .25s cubic-bezier(.3,1.6,.5,1)}
.g7-tx{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.g7-yr{flex:none;margin-left:12px;font-variant-numeric:tabular-nums}
.g7 a:hover{color:#000}
.g7 a.on{color:#000;font-weight:500}.g7 a.on .g7-dot{transform:scale(1)}
'''
rep('@media (prefers-reduced-motion: reduce){.l4-track{animation:none}.l1-line,.l2-mark{transition:none}}',
    CSS.strip('\n') + '\n@media (prefers-reduced-motion: reduce){.l4-track{animation:none}.l1-line,.l2-mark,.t6-tick{transition:none}}')
rep('family=Caveat:wght@400;600&amp;display=swap', 'family=Caveat:wght@400;600&amp;family=IBM+Plex+Mono:wght@400;500;600&amp;display=swap')
rep("this.state = { A: 0, B: 0, C: 0, D: 0 };", "this.state = { A: 0, B: 0, C: 0, D: 0, E: 0, F: 0, G: 0 };")
rep("for (const k of ['A', 'B', 'C', 'D'])", "for (const k of ['A', 'B', 'C', 'D', 'E', 'F', 'G'])")
rep("    v.bY = (st.B * 52) + 'px';", "    v.bY = (st.B * 52) + 'px';\n    v.fY = (st.F * 44) + 'px';\n    v.fColor = ['#141414', '#00a4ef', '#00934b', '#141414', '#00a1e0'][st.F] || '#141414';")
rep('<!-- Box (6) nav variations: gray line, spine, labeled dark dock, liquid glass -->',
    '<!-- Box (6) nav variations: gray line, spine, labeled dark dock, liquid glass, numbered index, accent tick, year ledger -->')
open(p, 'w').write(s); print('ok')
