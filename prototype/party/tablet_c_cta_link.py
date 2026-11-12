"""Tablet C contact line: 'Let's work together' on its own line, black 'Say hello' button, 'Email me' as a plain text link."""
import sys, re
p = sys.argv[1]; s = open(p).read()
i = s.index('<div class="th-cta"'); j = s.index('</div>', i) + len('</div>')
old = s[i:j]
prim = re.search(r'<a class="th-btn th-btn-primary".*?</a>', old, re.S).group(0)
NEW = ('<div class="th-cta" style="grid-column: 1 / -1; display: flex; flex-direction: column; align-items: flex-start; gap: 14px; margin-top: -4px">'
  '<p style="margin: 0; font-size: {{proseSize}}; color: #141414">Let&#39;s work together</p>'
  '<div style="display: flex; flex-direction: row; flex-wrap: wrap; align-items: center; gap: 24px">' + prim +
  '<button type="button" class="th-link" onClick="{{copy}}" onPointerEnter="{{gmEnter}}" onPointerLeave="{{gmLeave}}" onFocus="{{gmEnter}}" onBlur="{{gmLeave}}" title="Copy my email" '
  'style="background: none; border: 0; padding: 0; font: inherit; font-size: 18px; font-weight: 500; color: #141414; text-decoration: underline; text-underline-offset: 5px; text-decoration-thickness: 1.5px; cursor: pointer">{{emailMeLabel}}</button>'
  '</div></div>')
s = s[:i] + NEW + s[j:]
assert s.count("      copyLabel: this.state.copied ? 'Email copied' : 'Email',") == 1
s = s.replace("      copyLabel: this.state.copied ? 'Email copied' : 'Email',", "      copyLabel: this.state.copied ? 'Email copied' : 'Email',\n      emailMeLabel: this.state.copied ? 'Email copied' : 'Email me',")
CSS = '''.th-link{transition:color .2s,text-decoration-color .2s;text-decoration-color:rgba(20,20,20,.35) !important}
.th-link:hover{text-decoration-color:currentColor !important}
.th-link:focus-visible{outline:2px solid #3078e7;outline-offset:4px;border-radius:2px}
'''
s = s.replace('</style>\n</helmet>', CSS + '</style>\n</helmet>', 1)
open(p, 'w').write(s); print('ok')
