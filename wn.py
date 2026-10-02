import math
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Ellipse

plt.rcParams["mathtext.fontset"] = "cm"
LW = 1.2          # سمك خطوط الحواف


# ================= أدوات مشتركة =================
def stadium(p, q, r, steps=40):
    """شكل مستطيل بطرفين دائريين يحيط بالقطعة pq (حافة رؤوسها على خط واحد)."""
    ang = math.atan2(q[1] - p[1], q[0] - p[0])
    pts = []
    for cx, cy, a0 in [(q[0], q[1], ang - math.pi / 2), (p[0], p[1], ang + math.pi / 2)]:
        for t in range(steps + 1):
            a = a0 + math.pi * t / steps
            pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    return pts


def rounded_hull(points, r, steps=30):
    """منحنى مغلق ناعم يحيط بنقاط في وضع محدّب."""
    cx = sum(p[0] for p in points) / len(points)
    cy = sum(p[1] for p in points) / len(points)
    pts = sorted(points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    out = []
    for i in range(len(pts)):
        prev, cur, nxt = pts[i - 1], pts[i], pts[(i + 1) % len(pts)]
        a1 = math.atan2(-(cur[0] - prev[0]), cur[1] - prev[1])
        a2 = math.atan2(-(nxt[0] - cur[0]), nxt[1] - cur[1])
        if a2 < a1:
            a2 += 2 * math.pi
        for t in range(steps + 1):
            a = a1 + (a2 - a1) * t / steps
            out.append((cur[0] + r * math.cos(a), cur[1] + r * math.sin(a)))
    return out


def lerp(p, q, t):
    return (p[0] + t * (q[0] - p[0]), p[1] + t * (q[1] - p[1]))


def edge_shape(ax, pts):
    ax.add_patch(Polygon(pts, closed=True, fill=False, edgecolor="black", lw=LW))


def dot(ax, x, y, hollow=False, size=8):
    ax.plot(x, y, "o", color="white" if hollow else "black", mec="black",
            markersize=size, zorder=5)


def label(ax, x, y, s, size=14):
    ax.text(x, y, s, ha="center", va="center", fontsize=size)


def finish(ax, title, info, cx=0.0, cy=0.0, half=3.6):
    """كل لوحة مربع ثابت حول (cx, cy) والمعلومة تحت الرسم."""
    ax.set_title(title, fontsize=14)
    ax.text(cx, cy - half + 0.25, info, ha="center", va="center", fontsize=13)
    ax.set_xlim(cx - half, cx + half)
    ax.set_ylim(cy - half, cy + half)
    ax.set_aspect("equal")
    ax.axis("off")


# ================= (a) المسار الفضفاض P_4^(3) =================
def loose_path(ax, n=4, k=3, gap=1.6):
    V = [(i * gap, 0) for i in range(n + 1)]
    for i in range(n):
        r = 0.32 if i % 2 == 0 else 0.42          # نصف قطر متناوب لتمييز الحواف المتجاورة
        edge_shape(ax, stadium(V[i], V[i + 1], r))
        for t in range(1, k - 1):
            x, y = lerp(V[i], V[i + 1], t / (k - 1))
            dot(ax, x, y, hollow=True)
        label(ax, (V[i][0] + V[i + 1][0]) / 2, 0.75, rf"$e_{{{i + 1}}}$")
    for i, (x, y) in enumerate(V):
        dot(ax, x, y)
        label(ax, x, -0.7, rf"$v_{{{i + 1}}}$")
    finish(ax, r"(a) Loose path $P_4^{(3)}$", r"$|V|=n(k-1)+1=9,\ |E|=4$", cx=n * gap / 2, half=4.0)


# ================= (b) النجمة الفائقة S_5^(3) =================
def hyperstar(ax, n=5, k=3, L=2.4):
    c = (0, 0)
    for i in range(n):
        a = math.pi / 2 - 2 * math.pi * i / n
        far = (L * math.cos(a), L * math.sin(a))
        edge_shape(ax, stadium(c, far, 0.3))
        for t in range(1, k):
            x, y = lerp(c, far, t / (k - 1))
            dot(ax, x, y, hollow=True)
        lx, ly = lerp(c, far, 1.22)
        label(ax, lx, ly, rf"$e_{{{i + 1}}}$")
    dot(ax, *c)
    label(ax, 0.0, -0.55, r"$c$")
    finish(ax, r"(b) Hyperstar $S_5^{(3)}$", r"$|V|=n(k-1)+1=11,\ |E|=5$")


# ================= (c) زهرة عباد الشمس (sunflower) =================
def sunflower(ax, petals=4, L=2.7):
    c1, c2 = (0, 0.18), (0, -0.18)                   # النواة (kernel) في المركز
    for i in range(petals):
        a = math.pi / 4 + 2 * math.pi * i / petals
        u = (math.cos(a), math.sin(a))
        # كل بتلة شكل بيضاوي يبدأ من النواة ويمتد للخارج
        ctr = ((L / 2 - 0.15) * u[0], (L / 2 - 0.15) * u[1])
        ax.add_patch(Ellipse(ctr, L + 0.6, 0.95, angle=math.degrees(a),
                             fill=False, edgecolor="black", lw=LW))
        for t in (1.35, 2.25):
            dot(ax, t * u[0], t * u[1], hollow=True)
        label(ax, 3.05 * u[0], 3.05 * u[1], rf"$e_{{{i + 1}}}$")
    dot(ax, *c1)
    dot(ax, *c2)
    finish(ax, "(c) Sunflower: 4 petals, kernel $\\{c_1,c_2\\}$",
           r"$k=4,\ e_i\cap e_j=\{c_1,c_2\}\ (i\neq j)$")


# ================= (d) المسار المشدود (tight path) =================
def tight_path(ax, nv=6):
    V = [(i * 1.15, 1.3 if i % 2 else 0.0) for i in range(nv)]  # تعرّج حتى تظهر المثلثات
    radii = [0.22, 0.30, 0.38, 0.46]       # أنصاف أقطار مختلفة حتى لا تتطابق الحدود
    for i in range(nv - 2):
        edge_shape(ax, rounded_hull([V[i], V[i + 1], V[i + 2]], radii[i % 4]))
    for i, (x, y) in enumerate(V):
        dot(ax, x, y)
        label(ax, x, y + (0.7 if i % 2 else -0.7), rf"$v_{{{i + 1}}}$")
    finish(ax, r"(d) Tight path (3-uniform, 6 vertices)",
           r"$e_i=\{v_i,v_{i+1},v_{i+2}\},\ |e_i\cap e_{i+1}|=2$",
           cx=(nv - 1) * 1.15 / 2, cy=0.65)


# ================= (e) الشجرة الفائقة الفضفاضة (power of a tree) =================
def loose_hypertree(ax, k=3):
    P = {"r": (0, 2.2), "a": (-2.2, 0), "b": (0, 0), "c": (2.2, 0),
         "d": (-3.2, -2.2), "f": (-1.2, -2.2), "g": (2.2, -2.2)}
    tree = [("r", "a"), ("r", "b"), ("r", "c"), ("a", "d"), ("a", "f"), ("c", "g")]
    for (u, v) in tree:
        edge_shape(ax, stadium(P[u], P[v], 0.3))
        for t in range(1, k - 1):
            dot(ax, *lerp(P[u], P[v], t / (k - 1)), hollow=True)
    for (x, y) in P.values():
        dot(ax, x, y)
    finish(ax, r"(e) Loose hypertree $T^{(3)}$ (power of a tree)",
           r"$|V|=|E|(k-1)+1=13,\ |E|=6$", cy=-0.3)


# ================= (f) مستوى فانو (Fano plane) =================
def fano(ax):
    A, B, C = (0, 2.6), (-2.25, -1.3), (2.25, -1.3)
    O = (0, 0)
    mAB, mBC, mAC = lerp(A, B, .5), lerp(B, C, .5), lerp(A, C, .5)
    for p, q in [(A, B), (B, C), (A, C), (A, mBC), (B, mAC), (C, mAB)]:
        ax.plot([p[0], q[0]], [p[1], q[1]], color="black", lw=LW)
    ax.add_patch(Circle(O, 1.3, fill=False, color="black", lw=LW))   # الحافة السابعة
    for p in [A, B, C, O, mAB, mBC, mAC]:
        dot(ax, *p, size=9)
    finish(ax, "(f) Fano plane", r"$|V|=|E|=7$; two edges meet in one vertex", cy=0.2)


fig, axes = plt.subplots(2, 3, figsize=(17, 11))
loose_path(axes[0, 0])
hyperstar(axes[0, 1])
sunflower(axes[0, 2])
tight_path(axes[1, 0])
loose_hypertree(axes[1, 1])
fano(axes[1, 2])

plt.tight_layout(h_pad=3)
plt.savefig("standard_hypergraphs.png", dpi=300, bbox_inches="tight")
plt.savefig("standard_hypergraphs.pdf", bbox_inches="tight")
plt.show()