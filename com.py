import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, PathPatch
from matplotlib.path import Path

plt.rcParams["mathtext.fontset"] = "cm"

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
u, v = (-1.5, 0.0), (1.5, 0.0)      # الرأسان


def draw_vertices(ax, below=False):
    for (x, y), name, dx in [(u, r"$v_1$", -0.35), (v, r"$v_2$", 0.35)]:
        ax.plot(x, y, "o", color="black", markersize=8, zorder=5)
        if below:   # الاسم تحت الرأس حتى لا يتقاطع مع الأشكال البيضاوية
            ax.text(x, y - 0.22, name, ha="center", va="center", fontsize=16)
        else:
            ax.text(x + dx, y, name, ha="center", va="center", fontsize=18)


# ---------- (a) رؤية البيان المتعدد: أقواس بين الرأسين ----------
heights = [0, 0.35, -0.35, 0.7, -0.7, 1.05, -1.05]          # ارتفاع كل قوس
for j, h in enumerate(heights):
    path = Path([u, (0, 2 * h), v], [Path.MOVETO, Path.CURVE3, Path.CURVE3])
    ax1.add_patch(PathPatch(path, fill=False, lw=1.4, color="black"))
    ax1.text(0, h, rf"$e_{{{j + 1}}}$",            # الاسم فوق القوس مباشرة
             ha="center", va="center", fontsize=12,
             bbox=dict(fc="white", ec="none", pad=1.0))
# أقواس باهتة متقطعة + نقاط = "وهكذا إلى ما لا نهاية"
for h in [1.4, -1.4, 1.65, -1.65]:
    path = Path([u, (0, 2 * h), v], [Path.MOVETO, Path.CURVE3, Path.CURVE3])
    ax1.add_patch(PathPatch(path, fill=False, lw=1.0, color="gray", ls="--", alpha=0.6))
ax1.text(0, 1.95, r"$\vdots$", ha="center", va="center", fontsize=22)
ax1.text(0, -1.95, r"$\vdots$", ha="center", va="center", fontsize=22)
draw_vertices(ax1)
ax1.set_title("(a) Multigraph view: infinitely many parallel edges", fontsize=13)

# ---------- (b) رؤية البيان الفائق: أشكال بيضاوية متداخلة ----------
for j in range(4):
    w, hgt = 3.9 + 0.7 * j, 1.2 + 0.55 * j
    ax2.add_patch(Ellipse((0, 0), w, hgt, fill=False, lw=1.4, color="black"))
    ax2.text(0, hgt / 2 - 0.15, rf"$e_{{{j + 1}}}$", ha="center", va="center", fontsize=13)
for j in range(4, 6):                                   # باهتة = تستمر
    w, hgt = 3.9 + 0.7 * j, 1.2 + 0.55 * j
    ax2.add_patch(Ellipse((0, 0), w, hgt, fill=False, lw=1.0, color="gray", ls="--", alpha=0.6))
ax2.text(0, 2.3, r"$\vdots$", ha="center", va="center", fontsize=22)
ax2.text(0, -2.4, r"$e_i=\{v_1,v_2\},\quad i=1,2,3,\ldots$", ha="center", va="center", fontsize=15)
draw_vertices(ax2, below=True)
ax2.set_title("(b) Hypergraph view: each edge $e_i=\\{v_1,v_2\\}$", fontsize=13)

for ax in (ax1, ax2):
    ax.set_xlim(-3.9, 3.9)
    ax.set_ylim(-2.75, 2.65)
    ax.set_aspect("equal")
    ax.axis("off")

plt.tight_layout()
plt.savefig("two_vertex_infinite.png", dpi=300, bbox_inches="tight")
plt.savefig("two_vertex_infinite.pdf", bbox_inches="tight")
plt.show()