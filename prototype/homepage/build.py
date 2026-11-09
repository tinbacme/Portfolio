"""Build the homepage prototype from the Claude Design board.

usage: python3 build.py <board.dc.html> <assets_dir> <out_dir>

- Copies the board's <helmet> (fonts, styles) into the page head area.
- Puts the board's markup in a <template> and runs the board's own
  Component code with dc-lite.js, using each Tweak's current value.
- Rewrites /_blob/<id> asset links to assets/<id>.<ext>.
The output is body-only HTML (works opened directly and as an Artifact).
"""
import html, json, os, re, shutil, sys

board, assets_dir, out = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(board, encoding='utf-8').read()

# asset ids -> local files
ext = {}
for f in os.listdir(assets_dir):
    stem, e = os.path.splitext(f)
    if re.fullmatch(r'[0-9a-f]{32}', stem): ext[stem] = e
os.makedirs(os.path.join(out, 'assets'), exist_ok=True)
used = sorted(set(re.findall(r'/_blob/([0-9a-f]{32})', s)))
missing = [u for u in used if u not in ext]
if missing: sys.exit('missing assets: ' + ', '.join(missing))
for u in used: shutil.copy(os.path.join(assets_dir, u + ext[u]), os.path.join(out, 'assets', u + ext[u]))
s = re.sub(r'/_blob/([0-9a-f]{32})', lambda m: 'assets/' + m.group(1) + ext[m.group(1)], s)

xdc = s[s.index('<x-dc>') + 6:s.index('</x-dc>')]
helmets = re.findall(r'<helmet>(.*?)</helmet>', s, re.S)
markup = re.sub(r'<helmet>.*?</helmet>', '', xdc, flags=re.S).strip()

m = re.search(r"<script type=\"text/x-dc\" data-dc-script data-props=(['\"])(.*?)\1>\n?(.*?)</script>", s, re.S)
spec = json.loads(html.unescape(m.group(2)))
code = m.group(3)
props = {k: v['default'] for k, v in spec.items() if isinstance(v, dict) and 'default' in v}

runtime = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dc-lite.js'), encoding='utf-8').read()
page = f'''<title>Tin Le Portfolio</title>
<meta name="description" content="Tin Le, product designer. Homepage prototype.">
{''.join(helmets)}
<style>html,body{{background:#f5f5f5}}body{{margin:0;overflow-x:hidden}}
/* prototype-only: keep fixed canvas widths inside small screens */
#app [style*="aspect-ratio"]{{max-width:100%}}
@media (max-width:700px){{#app .ab-board{{zoom:calc(min(1,(100vw - 32px)/605px))}}
  #app #top,#app main,#app #about,#app header,#app footer{{padding-left:max(20px,env(safe-area-inset-left,0px))!important;padding-right:max(20px,env(safe-area-inset-right,0px))!important}}
  #app #top{{min-height:auto!important;padding-block:96px 120px!important}}
  #app #about{{padding-block:96px 120px!important}}}}
@supports not (zoom:calc(1)){{@media (max-width:700px){{#app .ab-board{{zoom:.56}}}}}}
</style>
<template id="dc-tpl">
{markup}
</template>
<div id="app"></div>
<script>
{runtime}
</script>
<script>
{code}
dcLite.run({{ template: document.getElementById('dc-tpl'), host: document.getElementById('app'), Component, props: {json.dumps(props, ensure_ascii=False)} }});
</script>
'''
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page)
print('built', os.path.join(out, 'index.html'), len(page), 'bytes,', len(used), 'assets')
