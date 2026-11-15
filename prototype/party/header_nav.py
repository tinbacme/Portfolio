"""Header: logo on the left; Work, About and a 'Say hi' button on the right.  usage: nav.py <board> [about]"""
import sys
p = sys.argv[1]; about = len(sys.argv) > 2; s = open(p).read()
def rep(old, new, count=1):
    global s
    assert s.count(old) == count, (old[:100], s.count(old)); s = s.replace(old, new)
rep('<header class="th-head {{headClass}}" style="position: sticky; top: 0; z-index: 10; display: flex; justify-content: center; align-items: center; padding: 14px 40px; flex-direction: row">',
    '<header class="th-head {{headClass}}" style="position: sticky; top: 0; z-index: 10; display: flex; justify-content: space-between; align-items: center; padding: 14px 150px; flex-direction: row">')
i = s.index('<header class="th-head'); j = s.index('</header>', i)
k = s.rindex('</button>', i, j) + len('</button>')
NAV = ('\n    <nav class="th-nav" aria-label="Main">'
       f'<a class="th-navlink{"" if about else " on"}" href="#work"{"" if about else " aria-current=\"page\""}>Work</a>'
       f'<a class="th-navlink{" on" if about else ""}" href="#about"{" aria-current=\"page\"" if about else ""}>About</a>'
       '<button type="button" class="th-sayhi" onClick="{{copy}}" title="Copy my email">{{sayHiLabel}}</button></nav>')
s = s[:k] + NAV + s[k:]
if not about and '<main aria-label="Work"' in s: s = s.replace('<main aria-label="Work"', '<main id="work" aria-label="Work"', 1)
rep("copyLabel: this.state.copied ? 'Email copied' : 'Email',", "copyLabel: this.state.copied ? 'Email copied' : 'Email', sayHiLabel: this.state.copied ? 'Email copied' : 'Say hi',")
CSS = '''
/* header nav */
.th-nav{position:relative;z-index:1;display:flex;align-items:center;gap:28px}
.th-navlink{font-size:16px;font-weight:500;color:#141414;text-decoration:none;opacity:.55;transition:opacity .2s}
.th-navlink:hover,.th-navlink.on{opacity:1}
.th-navlink:focus-visible,.th-sayhi:focus-visible{outline:2px solid #3078e7;outline-offset:4px;border-radius:4px}
.th-sayhi{border:0;border-radius:999px;background:#141414;color:#fff;padding:11px 20px;font:inherit;font-size:15px;font-weight:500;cursor:pointer;transition:transform .2s cubic-bezier(.3,1.5,.5,1),filter .2s}
.th-sayhi:hover{transform:translateY(-1px);filter:brightness(1.35)}
.party .th-navlink{color:#f4f1ea}.party .th-sayhi{background:#f4f1ea;color:#0d0c12}
'''
assert s.count('</style>\n</helmet>') == 1
s = s.replace('</style>\n</helmet>', CSS + '</style>\n</helmet>')
open(p, 'w').write(s); print('ok', 'about' if about else 'home')
