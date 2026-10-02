import math
from itertools import combinations

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

plt.rcParams["mathtext.fontset"] = "cm"

# ========= غيّر هذه القيم فقط =========
n = 4          # عدد الرؤوس
k = 3          # حجم كل حافة (k-uniform)
center = True  # True: ضع الرأس الأخير في المركز (أوضح لـ K4^(3))
# =====================================


def rounded_hull(points, r, steps=30):
    """منحنى مغلق ناعم يحيط بالنقاط على بعد r منها."""
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    pts = sorted(points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    m = len(pts)
    if m == 1:  # حافة من رأس واحد: دائرة
        x, y = pts[0]
        return [(x + r * math.cos(2 * math.pi * t / steps),
                 y + r * math.sin(2 * math.pi * t / steps)) for t in range(steps)]

    def normal_angle(a, b):  # زاوية العمودي الخارجي على الضلع a→b
        return math.atan2(-(b[0] - a[0]), b[1] - a[1])

    outline = []
    for i in range(m):
        prev, cur, nxt = pts[i - 1], pts[i], pts[(i + 1) % m]
        a1 = normal_angle(prev, cur)
        a2 = normal_angle(cur, nxt)
        if a2 < a1:
            a2 += 2 * math.pi
        for t in range(steps + 1):
            a = a1 + (a2 - a1) * t / steps
            outline.append((cur[0] + r * math.cos(a), cur[1] + r * math.sin(a)))
    return outline


# 1) مواقع الرؤوس: على دائرة نصف قطرها 2
R = 2.0
outer = n - 1 if center else n
pos = {}
for i in range(outer):
    angle = math.pi / 2 - 2 * math.pi * i / outer   # يبدأ من الأعلى ويدور مع عقارب الساعة
    pos[i] = (R * math.cos(angle), R * math.sin(angle))
if center:
    pos[n - 1] = (0.0, 0.0)

# 2) كل الحواف: جميع المجموعات الجزئية ذات k عنصر
edges = list(combinations(range(n), k))

fig, ax = plt.subplots(figsize=(6, 6))
colors = plt.cm.tab10.colors

# 3) رسم الحواف (نصف قطر مختلف قليلاً لكل حافة حتى لا تتطابق الحدود)
for j, e in enumerate(edges):
    r = 0.30 + 0.07 * (j % 4)
    shape = rounded_hull([pos[v] for v in e], r)
    c = colors[j % len(colors)]
    ax.add_patch(Polygon(shape, closed=True, facecolor=c, alpha=0.12,
                         edgecolor=c, linewidth=1.6))

# 4) رسم الرؤوس وأسمائها (الاسم خارج الدائرة في اتجاه الرأس)
for i, (x, y) in pos.items():
    ax.plot(x, y, "o", color="black", markersize=7, zorder=5)
    d = math.hypot(x, y)
    ux, uy = (x / d, y / d) if d > 1e-9 else (0.0, -1.0)   # رأس المركز: الاسم تحته
    ax.text(x + 0.75 * ux, y + 0.75 * uy, rf"$v_{{{i + 1}}}$",
            ha="center", va="center", fontsize=16)

ax.set_title(rf"Complete ${k}$-uniform hypergraph $K_{{{n}}}^{{({k})}}$"
             rf"  ({len(edges)} edges)", fontsize=14)
ax.set_aspect("equal")
ax.autoscale_view()
ax.margins(0.15)
ax.axis("off")

plt.savefig(f"complete_K{n}_{k}.png", dpi=300, bbox_inches="tight")
plt.savefig(f"complete_K{n}_{k}.pdf", bbox_inches="tight")
plt.show()