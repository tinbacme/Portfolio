"""Rig v2: rotate the hand at the wrist, with the wrist lines always reaching the cuff."""
import math
import numpy as np
from PIL import Image, ImageDraw, ImageChops
D = '/tmp/claude-0/-home-user-Portfolio/981b70c2-10b1-51ba-9954-e71e8ead3214/scratchpad/wave/'
PAD = 190
src = Image.open(D + 'ref.png').convert('L').point(lambda v: 255 if v > 200 else (0 if v < 90 else v))
ref = Image.new('L', (src.size[0] + PAD, src.size[1]), 255); ref.paste(src, (PAD, 0))
W, H = ref.size
P = lambda pts: [(x + PAD, y) for x, y in pts]
# hand + motion lines; bottom edge runs just above the cuff's top line
HAND = P([(55, 215), (270, 215), (275, 330), (350, 440), (350, 505), (326, 540), (300, 585), (290, 604), (270, 624), (140, 624), (100, 610), (55, 430)])
# below this line belongs to the cuff/sleeve: the rotated hand never draws there
FLOOR = P([(-PAD, 636), (100, 632), (130, 638), (170, 655), (230, 659), (262, 653), (300, 636), (1100, 636)])
PIVOT = (205 + PAD, 650)
LEFT, RIGHT = -36, 6

mask = Image.new('L', (W, H), 0); ImageDraw.Draw(mask).polygon(HAND, fill=255)
white = Image.new('L', (W, H), 255)
body = Image.composite(white, ref, mask)
hand = np.asarray(Image.composite(ref, white, mask)).copy()
m = np.asarray(mask) > 0
# extend the wrist strokes straight down ~60px so they still meet the cuff after rotating
for x in range(PAD + 95, PAD + 295):
    ys = np.nonzero(m[:, x])[0]
    if not len(ys): continue
    yb = ys.max()
    hand[yb + 1:yb + 26, x] = hand[yb, x]
hand = Image.fromarray(hand)
floor = Image.new('L', (W, H), 0); ImageDraw.Draw(floor).polygon(FLOOR + [(W, H), (0, H)], fill=255)

def frame(deg):
    r = hand.rotate(-deg, resample=Image.BICUBIC, center=PIVOT, fillcolor=255)
    r = Image.composite(white, r, floor)           # nothing below the cuff line
    return ImageChops.darker(body, r)

if __name__ == '__main__':
    N = 16
    frames = []
    for i in range(N):
        t = (1 - math.cos(2 * math.pi * i / N)) / 2
        frames.append(frame(LEFT + (RIGHT - LEFT) * t))
    frames[0].save(D + 'wave2-preview.gif', save_all=True, append_images=frames[1:], duration=65, loop=0)
    picks = [0, 3, 5, 8, 11, 13]
    cw = 512; chh = round(cw * H / W)
    strip = Image.new('L', (cw * len(picks), chh), 255)
    for k, i in enumerate(picks): strip.paste(frames[i].resize((cw, chh), Image.LANCZOS), (k * cw, 0))
    strip.save(D + 'wave2-sprite.png')
    zoom = Image.new('L', (680, 340), 255)
    zoom.paste(frames[0].crop((PAD + 40, 400, PAD + 380, 740)), (0, 0)); zoom.paste(frames[8].crop((PAD + 40, 400, PAD + 380, 740)), (340, 0))
    zoom.save(D + 'seam.png')
    print('ok')
