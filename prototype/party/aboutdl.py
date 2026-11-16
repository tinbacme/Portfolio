"""About page ledger: a black 'Download resume' button with a download icon in place of the Resume (PDF) placeholder;
also repair the ledger's font shorthands (they named 'inherit' as the family, which browsers ignore) to the page font.
usage: aboutdl.py <TinHome-About.dc.html>"""
import sys, re
p=sys.argv[1]; s=open(p).read()
def rep(o,n):
    global s; assert s.count(o)==1,(o[:80],s.count(o)); s=s.replace(o,n)
old = re.search(r'<span class="lk-ph" title="Placeholder: no PDF is attached yet">.*?</span>(?=<a class="lk")', s).group(0)
DL = ('<a class="ab-dl" href="#resume-pdf" title="Placeholder: no PDF is attached yet" onClick="{{noPdf}}">'
      '<svg viewBox="0 0 16 16" width="15" height="15" aria-hidden="true"><path d="M8 2v8.5M4.5 7 8 10.5 11.5 7" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"></path>'
      '<path d="M2.5 11.5v1.5a1 1 0 0 0 1 1h9a1 1 0 0 0 1-1v-1.5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"></path></svg>Download resume</a>')
rep(old, DL)
a = s.index('/* Experiences: the r'); b = s.index('</style>', a)
blk = s[a:b]
blk2 = re.sub(r"(font:[^;}]*?\d(?:px)?(?:/[\d.]+(?:px)?)?) inherit(\s*!important)?", lambda m: m.group(1) + " 'Be Vietnam Pro',system-ui,sans-serif" + (m.group(2) or ''), blk)
print('fonts fixed', blk.count(' inherit') - blk2.count(' inherit'))
blk2 += '''
/* black download button */
.ab-dl{display:inline-flex;align-items:center;gap:8px;height:40px;padding:0 18px 0 15px;border-radius:999px;background:#141414;color:#fff;text-decoration:none;font:500 14px/1 'Be Vietnam Pro',system-ui,sans-serif;transition:background-color .2s,transform .2s}
.ab-dl:hover{background:#000;transform:translateY(-1px)}
.ab-dl:active{transform:none}
.ab-dl svg{flex:none}
'''
s = s[:a] + blk2 + s[b:]
rep("      frames,\n", "      frames,\n      noPdf: (e) => { if (e && e.preventDefault) e.preventDefault(); }, // placeholder until the PDF is attached\n")
open(p,'w').write(s); print('ok')
