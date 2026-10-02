import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse   # ضعه في أول الملف
fig, ax = plt.subplots(figsize=(7, 4))   # fig = الورقة، ax = منطقة الرسم

ax.set_xlim(-3, 3)
ax.set_ylim(-1, 3)
ax.set_aspect("equal")
ax.grid(True)


ax.plot(0, 0, "o", color="black", markersize=6)    # نقطة عند (0,0)
ax.plot(-1, 0, "o", color="black", markersize=6)   # نقطة عند (-1,0)
ax.plot(0, 1, "o", color="black", markersize=6)    # نقطة عند (0,1) 

plt.rcParams["mathtext.fontset"] = "cm"   # ضعه في أول الملف: خط مثل LaTeX

ax.text(0, -0.4, r"$v_{00}$", ha="center", va="center", fontsize=14)
ax.text(0, 1.3,  r"$v_{31}$", ha="center", va="center", fontsize=14)

e = Ellipse((-1, 0), width=3, height=1, fill=False, edgecolor="black")
ax.add_patch(e)

vertices = [
    (0, 0, r"$v_{00}$", -0.45),   # (x, y, الاسم, إزاحة الاسم)
    (-1, 0, r"$v_{11}$", -0.25),
    (0, 1, r"$v_{31}$", 0.28),
]
for x, y, name, dy in vertices:
    ax.plot(x, y, "o", color="black", markersize=6)
    ax.text(x, y + dy, name, ha="center", va="center", fontsize=14)

    ax.axis("off")    # إخفاء المحاور والشبكة
plt.savefig("my_graph.png", dpi=300, bbox_inches="tight")   # صورة عالية الدقة
plt.savefig("my_graph.pdf", bbox_inches="tight")            # للإدراج في LaTeX
plt.show()
plt.show()