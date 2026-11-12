"""Tablet C: 'Let's work together' moves to its own line as two buttons: black 'Say hello' (LinkedIn) and white 'Email' (copies the address)."""
import sys, re
p = sys.argv[1]; s = open(p).read()
i = s.index('<div class="th-prose"'); j = s.index('</div>', i)
seg = s[i:j]
m = re.search(r"<span>, where I also graduated\. Let's work together</span> <button type=\"button\" onClick=\"\{\{copy\}\}\".*?</button> <span><span style=\"color: #9a948a\">or</span> <a href=\"https://www\.linkedin\.com/in/letin08/\".*?</a>\.</span>$", seg, re.S)
assert m, 'cta not found'
seg = seg[:m.start()] + '<span>, where I also graduated.</span>'
CTA = ('<div class="th-cta" style="grid-column: 1 / -1; display: flex; flex-direction: row; flex-wrap: wrap; align-items: center; gap: 12px; margin-top: -4px">'
  '<a class="th-btn th-btn-primary" href="https://www.linkedin.com/in/letin08/" target="_blank" rel="noopener" onPointerEnter="{{liEnter}}" onPointerLeave="{{liLeave}}" onFocus="{{liEnter}}" onBlur="{{liLeave}}" '
  'style="box-sizing: border-box; display: inline-flex; align-items: center; justify-content: center; padding: 14px 28px; border-radius: 999px; border: 1.5px solid #141414; background-color: #141414; color: #ffffff; font-size: 18px; font-weight: 500; text-decoration: none; cursor: pointer">Say hello</a>'
  '<button type="button" class="th-btn th-btn-secondary" onClick="{{copy}}" onPointerEnter="{{gmEnter}}" onPointerLeave="{{gmLeave}}" onFocus="{{gmEnter}}" onBlur="{{gmLeave}}" title="Copy my email" '
  'style="box-sizing: border-box; display: inline-flex; align-items: center; justify-content: center; padding: 14px 28px; border-radius: 999px; border: 1.5px solid rgba(20, 20, 20, 0.18); background-color: #ffffff; color: #141414; font: inherit; font-size: 18px; font-weight: 500; cursor: pointer">{{copyLabel}}</button>'
  '</div>')
s = s[:i] + seg + s[j:j + len('</div>')] + CTA + s[j + len('</div>'):]
CSS = '''
/* contact buttons on their own line */
.th-btn{transition:transform .2s cubic-bezier(.3,1.5,.5,1),box-shadow .2s,filter .2s}
.th-btn:hover{transform:translateY(-2px);box-shadow:0 10px 22px -12px rgba(0,0,0,.45)}
.th-btn:active{transform:translateY(0) scale(.98)}
.th-btn:focus-visible{outline:2px solid #3078e7;outline-offset:3px}
.th-btn-primary:hover{filter:brightness(1.35)}
.th-btn-secondary:hover{filter:brightness(.97)}
'''
assert s.count('</style>\n</helmet>') == 1
s = s.replace('</style>\n</helmet>', CSS + '</style>\n</helmet>')
open(p, 'w').write(s); print('ok')
