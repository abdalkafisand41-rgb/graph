import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

plt.rcParams["mathtext.fontset"] = "cm"
LW = 1.2


def stadium(p, q, r, steps=40):
    """شكل مستطيل بطرفين دائريين يحيط بالقطعة pq."""
    ang = math.atan2(q[1] - p[1], q[0] - p[0])
    pts = []
    for cx, cy, a0 in [(q[0], q[1], ang - math.pi / 2), (p[0], p[1], ang + math.pi / 2)]:
        for t in range(steps + 1):
            a = a0 + math.pi * t / steps
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def dot(ax, x, y, hollow=False, size=8):
    ax.plot(x, y, "o", color="white" if hollow else "black", mec="black",
            markersize=size, zorder=5)


def edge(ax, x0, x1, r, name, inner, small=()):
    """حافة أفقية من x0 إلى x1: inner = مواقع الرؤوس الداخلية (0..1)، small = نقاط ⋯."""
    ax.add_patch(Polygon(stadium((x0, 0), (x1, 0), r), closed=True, fill=False,
                         edgecolor="black", lw=LW))
    for t in inner:
        dot(ax, x0 + t * (x1 - x0), 0, hollow=True)
    for t in small:
        ax.plot(x0 + t * (x1 - x0), 0, "o", color="black", markersize=2.3, zorder=6)
    ax.text((x0 + x1) / 2, 0.85, name, ha="center", va="center", fontsize=16)


def shared(ax, x, name):
    dot(ax, x, 0, size=9)
    ax.text(x, -0.75, name, ha="center", va="center", fontsize=16)


def draw_path(ax, n, k, gap=2.2):
    """P_n^(k): n حافة على خط، الحواف المتتالية تشترك في رأس واحد."""
    X = [i * gap for i in range(n + 1)]
    for i in range(n):
        r = 0.32 if i % 2 == 0 else 0.44          # تناوب نصف القطر لتمييز الحواف المتجاورة
        inner = [j / (k - 1) for j in range(1, k - 1)]
        edge(ax, X[i], X[i + 1], r, rf"$e_{{{i + 1}}}$", inner)
    for i, x in enumerate(X):
        shared(ax, x, rf"$v_{{{i + 1}}}$")
    return X[-1]


def draw_general(ax, gap=3.0):
    """P_n^(k) العام: e1, e2, ..., e_n."""
    inner, small = [0.22, 0.4, 0.8], [0.55, 0.6, 0.65]
    edge(ax, 0, gap, 0.32, r"$e_1$", inner, small)
    edge(ax, gap, 2 * gap, 0.44, r"$e_2$", inner, small)
    # الحواف المحذوفة
    ax.plot([2 * gap + 0.6, 2 * gap + 1.9], [0, 0], color="black", ls="--", lw=1.0)
    ax.text(2 * gap + 1.25, 0.45, r"$\cdots$", ha="center", va="center", fontsize=22)
    x0 = 2 * gap + 2.5
    edge(ax, x0, x0 + gap, 0.32, r"$e_n$", inner, small)
    for x, name in [(0, r"$v_1$"), (gap, r"$v_2$"), (2 * gap, r"$v_3$"),
                    (x0, r"$v_n$"), (x0 + gap, r"$v_{n+1}$")]:
        shared(ax, x, name)
    # أسماء الرؤوس الداخلية للحافة الأولى فقط
    for t, lab in zip(inner, [r"$u_{1,1}$", r"$u_{1,2}$", r"$u_{1,k-2}$"]):
        ax.text(t * gap, -0.75, lab, ha="center", va="center", fontsize=13)
    return x0 + gap


fig, axes = plt.subplots(3, 1, figsize=(13, 10.5))

w = draw_path(axes[0], 4, 3)
axes[0].set_title(r"(a) $P_4^{(3)}$:  $|V|=4\cdot2+1=9,\ |E|=4$", fontsize=15)

w2 = draw_path(axes[1], 3, 4)
axes[1].set_title(r"(b) $P_3^{(4)}$:  $|V|=3\cdot3+1=10,\ |E|=3$", fontsize=15)

w3 = draw_general(axes[2])
axes[2].set_title(r"(c) $P_n^{(k)}$:  $|V|=n(k-1)+1,\ |E|=n$", fontsize=15)

W = max(w, w2, w3)
for ax, width in zip(axes, (w, w2, w3)):
    pad = (W - width) / 2                      # توسيط كل مسار أفقياً
    ax.set_xlim(-0.9 - pad, width + 0.9 + pad)
    ax.set_ylim(-1.3, 1.4)
    ax.set_aspect("equal")
    ax.axis("off")

fig.text(0.5, 0.0,
         r"$e_i=\{v_i,\,u_{i,1},\ldots,u_{i,k-2},\,v_{i+1}\}$;  "
         r"$|e_i\cap e_{i+1}|=1$,  $e_i\cap e_j=\emptyset$ for $|i-j|\geq2$",
         ha="center", fontsize=14)

plt.tight_layout(rect=(0, 0.03, 1, 1))
plt.savefig("loose_path.png", dpi=300, bbox_inches="tight")
plt.savefig("loose_path.pdf", bbox_inches="tight")
plt.show()