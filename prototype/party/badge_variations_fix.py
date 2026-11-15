"""Badge variations + Piece-46el: Salesforce logo in the placeholder, one-line footers, colorful V3, resume-based description."""
import sys, re
OLD = ('Enterprise tools and the design system behind them. I redesigned Salesforce Help so people could find answers on their own, '
       'reworked Manage Users to cut support cases, and built a back-to-work app for 75K employees.')
NEW = ('Three roles in five years. I redesigned search and content for Salesforce Help (support cases down 60% a month), '
       'built a back-to-work app for 75K employees, shipped 8+ Partner Community features, and added components to the C360 design system across 12 product teams.')
LOGO = '<img src="/_blob/ac43d25c19be4e522f4bd492e1c090ab" alt="Salesforce" style="display: block; width: 72%; height: auto">'
for p in sys.argv[1:]:
    s = open(p).read()
    n = s.count(OLD); s = s.replace(OLD, NEW)
    # grey placeholder box -> white tile with the Salesforce logo, same size and spot
    def logo(m):
        st = m.group(1).replace('display: flex; flex-direction: column;', 'display: grid; place-items: center;').replace('background-color: #b6b0a7', 'background-color: #ffffff')
        return f'<div style="{st}; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08)">{LOGO}</div>'
    s, k = re.subn(r'<div style="(box-sizing: border-box; display: flex; flex-direction: column; [^"]*background-color: #b6b0a7[^"]*)"></div>', logo, s)
    css = '\n.bd-foot > span:first-child{white-space:nowrap;overflow:hidden;text-overflow:ellipsis;min-width:0;margin-right:12px}'
    if 'v3-in' in s:
        css += r'''
/* V3 in color, not black and white */
.v3-in{background:linear-gradient(165deg,#e8f6ff 0%,#f1ebff 55%,#fff3dd 100%) !important;color:#14213d !important}
.v3-top{color:#56648a !important}.v3-top span:last-child{color:#d94fb5 !important}
.v3-photo{background:linear-gradient(#bfe7ff,#7cc8ff) !important}
.v3-photo img{filter:none !important}
.v3-type{color:#56648a !important}
.v3-stats div{background:rgba(255,255,255,.75) !important;box-shadow:0 1px 0 rgba(255,255,255,.9) inset,0 2px 6px rgba(20,33,61,.06)}
.v3-stats div:nth-child(1) b{color:#0176d3}.v3-stats div:nth-child(2) b{color:#d94fb5}.v3-stats div:nth-child(3) b{color:#2a9d63}
.v3-stats span{color:#56648a !important}
.v3-k{color:#0176d3 !important}
.v3-desc{font-size:14.5px !important;line-height:1.45 !important}
.v3-chips span{padding:4px 9px !important;font-size:11px !important}
.v3-chips span{border:0 !important;font-weight:500}
.v3-chips span:nth-child(4n+1){background:#dff1ff;color:#0176d3}.v3-chips span:nth-child(4n+2){background:#fde3f4;color:#b83a93}
.v3-chips span:nth-child(4n+3){background:#dcf5e7;color:#227a4d}.v3-chips span:nth-child(4n+4){background:#fff0cc;color:#a06a00}'''
    i = s.index('</style>\n  </helmet>') if '</style>\n  </helmet>' in s else s.index('</style>\n</helmet>')
    s = s[:i] + css + '\n' + s[i:]
    open(p, 'w').write(s); print(p.rsplit('/', 1)[-1], 'desc', n, 'logo', k)
