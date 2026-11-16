"""About page: put the résumé ledger (Resume V11, Recommended) into the Experiences section: Design / Teaching / Education
groups, a 'Show all details' switch, hover a row for its scope, Résumé (PDF) placeholder + LinkedIn.
usage: aboutledger.py <TinHome-About.dc.html> <ResumeVariations.dc.html>"""
import sys, re
p, rp = sys.argv[1], sys.argv[2]; s = open(p).read(); r = open(rp).read()
def rep(old, new, n=1):
    global s
    assert s.count(old) == n, (old[:90], s.count(old)); s = s.replace(old, new)
a = r.index('<section class="rv-sec rv-full"><p class="rv-k">V11</p>'); b = r.index('</section>', a)
sec = r[a:b]
bar = sec[sec.index('<div class="v11-bar">'):]
bar = bar[:bar.rindex('</div>')]  # drop the stage's closing div
assert bar.count('<div') == bar.count('</div>'), (bar.count('<div'), bar.count('</div>'))
bar = bar.replace('<p class="mini-n">Experience</p>', '<p class="mini-n">Roles</p>')
# the ledger's CSS, scoped to the about page
RL = r.split('\n')
want = lambda l: any(k in l for k in ('.v11', '.sw-tr', '.mini-n{', '.nums{', '.foot{', '.lk{', '.lk:hover', '.lk-ph', '.nda{', '.nda.sm')) and not l.startswith('.s-v11') and not l.startswith('.v11-hero')
css = '\n'.join(l.replace('.lk-ph em,.v10-dl em', '.lk-ph em') for l in RL[:530] if want(l))
css = css.replace("Inter,sans-serif", "inherit")
CSS = '''
/* Experiences: the résumé ledger from Resume V11 */
.ab-ledger{flex:1 1 100%;max-width:1140px}
.ab-ledger :where(button){font:inherit;color:inherit;background:none;border:0;padding:0;margin:0;text-align:left;cursor:pointer;-webkit-tap-highlight-color:transparent}
.ab-ledger :where(p,ul){margin:0}
.ab-ledger button:focus-visible,.ab-ledger a:focus-visible,.ab-ledger [tabindex]:focus-visible{outline:2px solid #0099ff;outline-offset:2px;border-radius:10px}
''' + css + '''
.ab-ledger .v11-row:hover{background:rgba(0,0,0,.035)}
.ab-ledger .v11-g{border-top-color:#e2e2e2}
.ab-ledger .v11-row + .v11-row{border-top-color:#ececec}
.ab-ledger .foot{border-top-color:#e6e6e6}
.ab-ledger .nda,.ab-ledger .lk-ph em{background:#ebebeb}
'''
rep('</style>', CSS + '</style>', 1) if s.count('</style>') == 1 else None
if CSS not in s:  # several style blocks: add to the first one
    i = s.index('</style>'); s = s[:i] + CSS + s[i:]
# the second About section (heading "Experiences"): ledger in place of the repeated intro paragraph
h = s.index('>Experiences</h2>'); sa = s.rindex('<section id="about"', 0, h); se = s.index('</section>', h)
blk = s[sa:se]
para = re.search(r'<div style="display: flex; flex-direction: column; gap: 12px; line-height: 1.6"><p style="margin: 0; font-size: 16px">I\'m a product designer.*?</p></div>', blk, re.S).group(0)
blk2 = blk.replace(para, '<div class="ab-ledger">' + bar + '</div>')
blk2 = blk2.replace('<div style="flex: 1 1 420px; max-width: 560px;', '<div style="flex: 1 1 100%; max-width: 1140px;', 1)
s = s[:sa] + blk2 + s[se:]
rep('family=Caveat:wght@400;500;600;700&amp;display=swap"></helmet>', 'family=Caveat:wght@400;500;600;700&amp;family=IBM+Plex+Mono:wght@400;500&amp;display=swap"></helmet>')
# state + toggle
rep("bdFlip: {}, copied: false,", "bdFlip: {}, v11: false, copied: false,")
rep("      frames,\n", "      frames,\n      v11c: this.state.v11 ? 'on' : '', v11x: String(!!this.state.v11), v11cls: this.state.v11 ? 'all' : '',\n      v11f: () => this.setState((st) => ({ v11: !st.v11 })),\n")
open(p, 'w').write(s); print('ok')
