import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Arc

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


def ray_edge(ax, angle_deg, L, ts, small=(), name=None, r=0.3):
    """حافة على شعاع من المركز: ts = مواقع الرؤوس (0..1)، small = نقاط ⋯."""
    a = math.radians(angle_deg)
    u = (math.cos(a), math.sin(a))
    ax.add_patch(Polygon(stadium((0, 0), (L * u[0], L * u[1]), r), closed=True,
                         fill=False, edgecolor="black", lw=LW))
    for t in ts:
        dot(ax, t * L * u[0], t * L * u[1], hollow=True)
    for t in small:
        ax.plot(t * L * u[0], t * L * u[1], "o", color="black", markersize=2.3, zorder=6)
    if name:
        ax.text((L + 0.55) * u[0], (L + 0.55) * u[1], name, ha="center", va="center",
                fontsize=16)
    return u


def center(ax):
    dot(ax, 0, 0, size=9)
    ax.text(0.45, -0.45, r"$c$", ha="center", va="center", fontsize=16)   # بين الشعاعين


def draw_star(ax, n, k, L=2.6):
    """S_n^(k): n حافة، كل حافة = c + (k-1) رأساً جديداً."""
    for i in range(n):
        ang = 90 - 360 * i / n
        ts = [j / (k - 1) for j in range(1, k)]
        ray_edge(ax, ang, L, ts, name=rf"$e_{{{i + 1}}}$")
    center(ax)


def draw_general(ax, L=2.6):
    """S_n^(k) العام: e1, e2, e3, ..., e_n والباقي مختصر."""
    ts, small = [0.38, 0.58, 1.0], [0.72, 0.78, 0.84]
    shown = [(90, r"$e_1$"), (30, r"$e_2$"), (-30, r"$e_3$"), (150, r"$e_n$")]
    for ang, name in shown:
        u = ray_edge(ax, ang, L, ts, small, name)
        if ang == 90:                                   # أسماء رؤوس الحافة الأولى فقط
            for t, lab in zip(ts, [r"$v_{1,1}$", r"$v_{1,2}$", r"$v_{1,k-1}$"]):
                ax.text(t * L * u[0] + 0.78, t * L * u[1], lab, ha="center",
                        va="center", fontsize=13)
    # الحواف المحذوفة بين e3 و e_n
    ax.add_patch(Arc((0, 0), 2 * 1.9, 2 * 1.9, theta1=165, theta2=-45 + 360,
                     color="black", ls="--", lw=1.0))
    ax.text(-0.15, -1.45, r"$\cdots$", ha="center", va="center", fontsize=22)
    center(ax)


fig, axes = plt.subplots(1, 3, figsize=(17, 6.6))

draw_star(axes[0], 4, 3)
axes[0].set_title(r"(a) $S_4^{(3)}$", fontsize=15)
axes[0].text(0, -3.75, r"$|V|=4\cdot2+1=9,\ |E|=4$", ha="center", fontsize=14)

draw_star(axes[1], 6, 4)
axes[1].set_title(r"(b) $S_6^{(4)}$", fontsize=15)
axes[1].text(0, -3.75, r"$|V|=6\cdot3+1=19,\ |E|=6$", ha="center", fontsize=14)

draw_general(axes[2])
axes[2].set_title(r"(c) $S_n^{(k)}$", fontsize=15)
axes[2].text(0, -3.75, r"$|V|=n(k-1)+1,\ |E|=n$", ha="center", fontsize=14)

for ax in axes:
    ax.set_xlim(-3.7, 3.7)
    ax.set_ylim(-4.1, 3.6)
    ax.set_aspect("equal")
    ax.axis("off")

fig.text(0.5, -0.01,
         r"$e_i=\{c,\,v_{i,1},\ldots,v_{i,k-1}\},\ i=1,\ldots,n$;  "
         r"$e_i\cap e_j=\{c\}$ for $i\neq j$  (the $k$-th power of the star $K_{1,n}$)",
         ha="center", fontsize=14)

plt.tight_layout()
plt.savefig("hyperstar.png", dpi=300, bbox_inches="tight")
plt.savefig("hyperstar.pdf", bbox_inches="tight")
plt.show()