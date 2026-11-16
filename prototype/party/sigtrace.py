"""Trace a signature PNG (transparent ink) into ordered pen strokes.
Skeletonize the ink, split the skeleton graph into segments, then walk them like a pen: start at the leftmost free end,
keep going along the smoothest continuation, lift the pen only when a stroke ends. Output: list of strokes, each a list of (x, y),
plus a stroke width that covers the ink. usage: sigtrace.py <in.png> <out.json>"""
import sys, json, math
import numpy as np
from PIL import Image
from skimage.morphology import skeletonize
from scipy import ndimage as ndi

def trace(path):
    im = Image.open(path).convert('RGBA'); a = np.array(im)[:, :, 3].astype(np.float32) / 255
    ink = a > 0.35
    ink = ndi.binary_closing(ink, iterations=1)
    dist = ndi.distance_transform_edt(ink)
    sk = skeletonize(ink)
    H, W = sk.shape
    pts = set(zip(*np.nonzero(sk)))  # (y, x)
    N8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    nb = lambda p: [(p[0] + dy, p[1] + dx) for dy, dx in N8 if (p[0] + dy, p[1] + dx) in pts]
    deg = {p: len(nb(p)) for p in pts}
    nodes = {p for p in pts if deg[p] != 2}
    # walk segments between nodes
    seen_edges = set(); segs = []
    def walk(start, nxt):
        seg = [start, nxt]; prev, cur = start, nxt
        while cur not in nodes:
            cand = [q for q in nb(cur) if q != prev and q not in seg[-3:]]
            if not cand: break
            prev, cur = cur, cand[0]; seg.append(cur)
        return seg
    for n in nodes:
        for q in nb(n):
            key = (n, q)
            if key in seen_edges: continue
            seg = walk(n, q)
            seen_edges.add((seg[0], seg[1])); seen_edges.add((seg[-1], seg[-2]))
            if len(seg) >= 3: segs.append(seg)
    # pure loops with no nodes
    covered = {p for s in segs for p in s}
    rest = pts - covered
    while rest:
        p = min(rest, key=lambda t: t[1]); loop = [p]; prev = None; cur = p
        while True:
            cand = [q for q in nb(cur) if q in rest and q != prev and q not in loop]
            if not cand: break
            prev, cur = cur, cand[0]; loop.append(cur)
        rest -= set(loop)
        if len(loop) >= 6: segs.append(loop)
    # drop tiny spurs (skeleton noise) shorter than ~1.5x stroke width at ends
    sw = float(np.percentile(dist[sk], 90)) * 2 if sk.any() else 4
    def is_spur(s): return len(s) < max(6, sw * 1.5) and (deg.get(s[0], 0) == 1 or deg.get(s[-1], 0) == 1)
    segs = [s for s in segs if not is_spur(s)]
    # pen order: from the leftmost end, follow the smoothest continuation at each node
    used = [False] * len(segs)
    ends = {}
    for i, s in enumerate(segs):
        ends.setdefault(s[0], []).append((i, False)); ends.setdefault(s[-1], []).append((i, True))
    def direction(seg, at_end):
        k = min(6, len(seg) - 1)
        if at_end: a_, b_ = seg[-1 - k], seg[-1]
        else: a_, b_ = seg[k], seg[0]
        return (b_[0] - a_[0], b_[1] - a_[1])
    def near_node(p, r=3):
        return [q for q in ends if abs(q[0] - p[0]) <= r and abs(q[1] - p[1]) <= r]
    strokes = []
    while not all(used):
        # start a new stroke at the leftmost unused segment end
        best = None
        for i, s in enumerate(segs):
            if used[i]: continue
            for rev, p in ((False, s[0]), (True, s[-1])):
                if best is None or p[1] < best[0][1]: best = (p, i, rev)
        _, i, rev = best
        stroke = list(reversed(segs[i])) if rev else list(segs[i]); used[i] = True
        while True:
            tip = stroke[-1]; d0 = direction(stroke, True)
            options = []
            for q in near_node(tip):
                for j, at_end in ends[q]:
                    if used[j]: continue
                    seg = list(reversed(segs[j])) if at_end else list(segs[j])
                    d1 = (seg[min(6, len(seg) - 1)][0] - seg[0][0], seg[min(6, len(seg) - 1)][1] - seg[0][1])
                    n0, n1 = math.hypot(*d0) or 1, math.hypot(*d1) or 1
                    cos = (d0[0] * d1[0] + d0[1] * d1[1]) / (n0 * n1)
                    options.append((cos, j, seg))
            if not options: break
            cos, j, seg = max(options)
            if cos < -0.6: break  # would double straight back: lift the pen instead
            stroke += seg[1:]; used[j] = True
        strokes.append(stroke)
    # simplify (RDP) and convert to x, y
    def rdp(P, eps=0.9):
        if len(P) < 3: return P
        (y1, x1), (y2, x2) = P[0], P[-1]; dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy) or 1
        dmax, idx = 0, 0
        for k in range(1, len(P) - 1):
            y, x = P[k]; d = abs(dy * x - dx * y + x2 * y1 - y2 * x1) / L
            if d > dmax: dmax, idx = d, k
        if dmax > eps: return rdp(P[:idx + 1], eps)[:-1] + rdp(P[idx:], eps)
        return [P[0], P[-1]]
    out = [[(round(float(x), 1), round(float(y), 1)) for y, x in rdp(s)] for s in strokes if len(s) >= 4]
    return {"w": int(W), "h": int(H), 'sw': round(max(4.0, sw * 1.9 + 4), 1), 'strokes': out}

if __name__ == '__main__':
    r = trace(sys.argv[1]); json.dump(r, open(sys.argv[2], 'w'))
    print(sys.argv[1], 'strokes', len(r['strokes']), 'sw', r['sw'], 'pts', sum(len(s) for s in r['strokes']))
