import random, re
random.seed(7)
tpl=open('tpl.html').read()
logo=open('logo-paths.txt').read().replace('\n','')
S=640/1024
VN=(164,464); OR=(780,400); WA=(768,352)
route=f"M{VN[0]} {VN[1]} C 330 180, 640 160, {OR[0]-2} {OR[1]-2} Q 792 374, {WA[0]} {WA[1]}"
pin=lambda p:f"left: {p[0]*S:.0f}px; top: {p[1]*S:.0f}px;"
imgs="be80b2dbdedae7a3d6b7e813977ab9bc 47d7348bdeaaf475e13eb76281441a60 cf74e14fcd359da9a957be1f0f57f261 172e09e27c48b1ba6ee837a153fbc532 4d164a51804f8978f2607d488602f4a2 81ae3fff42161e29a6464458e8f07d62 058a1e4f71c41cad18dbe6a632862617 bb63863a75e37522abd7a2f10361fa3e 7dbf645f6df4f60061eba9b8bddb022e 80ecf61f9f73902c1a2417fc0c0ea2db 872c055ad51680554fde4a4d40a9c019 37663bc52d5e9b05200ebf2b14bb1ae7".split()
tiles=[]
n=len(imgs)
for i,b in enumerate(imgs):
    a=i*360/n+random.uniform(-8,8)-90
    w=random.choice([104,118,132,146]); h=random.choice([w, int(w*1.25), int(w*0.8)])
    tiles.append(f'<span class="g-tile" data-a="{a:.1f}" data-far="{random.uniform(1.7,2.3):.2f}" data-tw="{random.uniform(-50,50):.0f}" data-r="{random.uniform(-8,8):.1f}" data-w="{w}" data-h="{h}" style="width: {w}px; height: {h}px; opacity: 0;"><img src="/_blob/{b}" alt=""></span>')
out=(tpl.replace('%%LOGO%%',logo).replace('%%ROUTE%%',route).replace('%%VN%%',pin(VN)).replace('%%OR%%',pin(OR)).replace('%%WA%%',pin(WA))
     .replace('%%TILES%%',''.join(tiles)).replace('%%VNPT%%',f"[{VN[0]*S:.1f}, {VN[1]*S:.1f}]"))
assert '%%' not in out
open('project/VariationPixelSky.dc.html','w').write(out)
