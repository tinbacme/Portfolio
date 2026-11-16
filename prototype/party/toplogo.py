"""Tin's hand-drawn logo (8-frame loop, CSS only) at the top of the stuart.re-style page. usage: toplogo.py <TinHome-Stuart.dc.html>"""
import sys
p = sys.argv[1]; s = open(p).read()
F = ['8fbd77508883c78b84540da031e5f678', 'e09f528d7a65e7ee280d22130c36c17d', 'ca23789dd45bf344382c52b8987884a8', '720e3e91bd1b388459c182e4c63e3469',
     'a25aa6071a426de3b10058361008b0e1', '2ed749d513062c2fc935541bb195ad95', 'eb61a3bdf25e26fc602c11f962cebff2', '971b6a3ff00fa61ea013489a3df324e6']
imgs = ''.join(f'<img src="/_blob/{f}" alt="" style="animation-delay: {-(8 - k) * 0.7:.1f}s">' for k, f in enumerate(F))
LOGO = f'<a class="st-toplogo" href="#top" aria-label="Tin Le, back to top">{imgs}</a>'
old = '<header class="st-intro" id="top">'
assert s.count(old) == 1; s = s.replace(old, LOGO + old)
CSS = ('\n/* Tin logo at the top: the homepage\'s 8-frame hand-drawn loop */\n'
       '.st-toplogo{position:absolute;top:96px;left:296px;display:block;width:72px;height:72px}\n'
       '.st-toplogo img{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;opacity:0;animation:stLogo 5.6s steps(1,end) infinite}\n'
       '@keyframes stLogo{0%{opacity:1}12.5%{opacity:0}100%{opacity:0}}\n'
       '@media (prefers-reduced-motion: reduce){.st-toplogo img{animation:none}.st-toplogo img:last-child{opacity:1}}\n'
       '.st-toplogo:focus-visible{outline:2px solid #0099ff;outline-offset:4px;border-radius:8px}\n')
a = '.st-defs{position:absolute;width:0;height:0;overflow:hidden}'
assert s.count(a) == 1; s = s.replace(a, a + CSS)
open(p, 'w').write(s); print('ok')
