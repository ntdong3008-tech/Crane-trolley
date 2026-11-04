import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon

OUTDIR = sys.argv[1]
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "mathtext.fontset": "dejavusans"})
BLUE = "#1F4E79"; GREY = "#8C8C8C"; RED = "#B03A2E"; GREEN = "#2E7D32"

def box(ax, x, y, w, h, text, fc="#FFFFFF", ec=BLUE, fs=10, ls="-"):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02", fc=fc, ec=ec, lw=1.6, ls=ls))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, color="black")

def tri(ax, x, y, w, h, text, ec=BLUE, fs=10):
    ax.add_patch(Polygon([(x - w / 2, y - h / 2), (x - w / 2, y + h / 2), (x + w / 2, y)], closed=True, fc="white", ec=ec, lw=1.6))
    ax.text(x - w / 8, y, text, ha="center", va="center", fontsize=fs)

def tri_left(ax, x, y, w, h, text, ec=BLUE, fs=10):
    ax.add_patch(Polygon([(x + w / 2, y - h / 2), (x + w / 2, y + h / 2), (x - w / 2, y)], closed=True, fc="white", ec=ec, lw=1.6))
    ax.text(x + w / 8, y, text, ha="center", va="center", fontsize=fs)

def summ(ax, x, y, r=0.22):
    ax.add_patch(Circle((x, y), r, fc="white", ec="black", lw=1.4))
    ax.plot([x - r * 0.7, x + r * 0.7], [y - r * 0.7, y + r * 0.7], color="black", lw=0.8)
    ax.plot([x - r * 0.7, x + r * 0.7], [y + r * 0.7, y - r * 0.7], color="black", lw=0.8)

def arrow(ax, pts, color="black", ls="-", lw=1.4, label=None, lpos=None, lc=None):
    for (x0, y0), (x1, y1) in zip(pts[:-2], pts[1:-1]):
        ax.plot([x0, x1], [y0, y1], color=color, ls=ls, lw=lw)
    (x0, y0), (x1, y1) = pts[-2], pts[-1]
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, ls=ls, mutation_scale=14))
    if label:
        ax.text(lpos[0], lpos[1], label, ha="center", va="bottom", fontsize=11, color=lc or color)

def sign(ax, x, y, s, fs=12):
    ax.text(x, y, s, ha="center", va="center", fontsize=fs, fontweight="bold")

# =============================================================== Hình 1: mô hình khối cứng
fig, ax = plt.subplots(figsize=(19, 8.2))
ax.set_xlim(-0.5, 19.2); ax.set_ylim(-0.6, 7.6); ax.axis("off")
Y = 3.4
# lưới 3 pha
for dy in (0.6, 0, -0.6):
    ax.add_patch(Circle((0.3, Y + dy), 0.22, fc="white", ec="black", lw=1.3)); ax.text(0.3, Y + dy, "~", ha="center", va="center", fontsize=13)
    ax.plot([0.52, 1.3], [Y + dy, Y + dy], color="black", lw=1.2)
ax.text(0.3, Y + 1.15, "Lưới 3 pha\n380 V / 50 Hz", ha="center", va="bottom", fontsize=10)
box(ax, 2.3, Y, 2.0, 1.7, "Biến tần\nABB ACS380\n01A8-4\n(FOC)", fc="#EEF4FB")
# S-curve
box(ax, 2.3, 6.4, 2.6, 1.0, "Quỹ đạo S-curve\n$a^*$ = 0.10 m/s², $\\rho^*$ = 0.40 m/s³", fc="#FFF8E1", ec="#B7950B")
arrow(ax, [(2.3, 5.9), (2.3, Y + 0.85)], label="$v^*(t)$  →  $\\omega^* = v^*/k$", lpos=(3.75, 5.05))
# đo V I cosφ
arrow(ax, [(3.3, Y), (4.25, Y)])
ax.plot([3.75, 3.75], [Y - 0.15, Y - 1.0], color=GREY, lw=1); ax.text(3.75, Y - 1.45, "$U,\\ I,\\ \\cos\\varphi$", ha="center", fontsize=10, color=GREY)
# động cơ
ax.add_patch(Circle((5.0, Y), 0.75, fc="#EEF4FB", ec=BLUE, lw=1.8)); ax.add_patch(Circle((5.0, Y), 0.45, fc="white", ec=BLUE, lw=1.2))
ax.text(5.0, Y + 1.05, "ĐC SEW DRN71M4\n0.37 kW, 4 cực", ha="center", va="bottom", fontsize=10)
ax.text(5.0, Y - 1.05, "$M_e = k_M\\, i_{sq}$", ha="center", va="top", fontsize=10, color=BLUE)
arrow(ax, [(5.75, Y), (6.98, Y)], label="$T_{đ}$", lpos=(6.35, Y + 0.08))
# Σ mô-men
summ(ax, 7.2, Y); sign(ax, 6.85, Y + 0.35, "+"); sign(ax, 7.5, Y + 0.45, "−")
arrow(ax, [(7.42, Y), (8.05, Y)])
box(ax, 8.65, Y, 1.1, 0.9, "$\\dfrac{1}{J_\\Sigma}$", fs=13)
arrow(ax, [(9.2, Y), (9.75, Y)], label="$\\dfrac{d\\omega}{dt}$", lpos=(9.48, Y + 0.12))
box(ax, 10.3, Y, 1.0, 0.9, "$\\int$", fs=15)
arrow(ax, [(10.8, Y), (12.15, Y)], label="$\\omega_m$", lpos=(11.3, Y + 0.1))
tri(ax, 12.7, Y, 1.1, 1.0, "$k$", fs=13)
ax.text(12.7, Y - 0.75, "$k=\\dfrac{D_{bx}}{2i}$", ha="center", va="top", fontsize=10, color=BLUE)
arrow(ax, [(13.25, Y), (14.05, Y)], label="$v$", lpos=(13.65, Y + 0.1))
box(ax, 15.25, Y, 2.3, 1.0, "$F_c = M_\\Sigma\\, g\\, w_0\\, \\mathrm{sign}(v)$", fc="#FDEDEC", ec=RED, fs=10)
arrow(ax, [(16.4, Y), (17.38, Y)], label="$F_c$", lpos=(16.9, Y + 0.1))
summ(ax, 17.6, Y)
# lực bằng 0
box(ax, 17.6, 1.35, 2.3, 0.75, "$F_{dốc}=0$ (ray nằm ngang)\n$F_{gió}\\approx 0$ ($v$ = 0.12 m/s)", ec=GREY, fs=9, ls="--")
arrow(ax, [(17.6, 1.73), (17.6, Y - 0.22)], color=GREY, ls="--")
sign(ax, 17.3, Y - 0.45, "+"); sign(ax, 17.85, Y + 0.45, "+")
# phản hồi T_c
arrow(ax, [(17.82, Y), (18.6, Y), (18.6, 5.3), (13.75, 5.3)], label="$F_\\Sigma$", lpos=(18.85, 4.3))
tri_left(ax, 13.2, 5.3, 1.1, 1.0, "$k/\\eta$", fs=12)
arrow(ax, [(12.65, 5.3), (7.2, 5.3), (7.2, Y + 0.22)], label="$T_c$", lpos=(9.9, 5.35))
# encoder
arrow(ax, [(11.6, Y), (11.6, 0.7), (2.3, 0.7), (2.3, Y - 0.85)], color=GREEN, ls="--", lw=1.3)
ax.text(7.0, 0.32, "Encoder ES7C (1024 xung/vg) — phản hồi $\\omega_m$ cho FOC", ha="center", fontsize=10, color=GREEN)
# công thức
ax.text(9.5, 7.25, "Hình 1 — Sơ đồ khối hệ truyền động xe con cầu trục (mô hình khối cứng: tải treo gắn cứng với xe)",
        ha="center", fontsize=13, fontweight="bold")
ax.text(13.3, 6.4, "$J_\\Sigma \\dfrac{d\\omega_m}{dt} = T_{đ} - T_c$     $T_c = \\dfrac{F_\\Sigma\\, k}{\\eta}$     "
        "$J_\\Sigma = J_B + \\dfrac{\\delta M_\\Sigma k^2}{\\eta}$", ha="center", fontsize=11.5,
        bbox=dict(boxstyle="round", fc="#F7F9FC", ec="#C9D6E8"))
fig.savefig(OUTDIR + "/02_So_do_khoi_khoi_cung.png", dpi=150, bbox_inches="tight")
fig.savefig(OUTDIR + "/02_So_do_khoi_khoi_cung.svg", bbox_inches="tight")
plt.close(fig)

# =============================================================== Hình 2: mở rộng con lắc tải treo
fig, ax = plt.subplots(figsize=(19, 8.6))
ax.set_xlim(-0.5, 19.2); ax.set_ylim(-1.2, 7.6); ax.axis("off")
Y = 4.4
ax.text(0.9, Y + 0.1, "$T_{đ}$\n(từ ĐC,\nHình 1)", ha="center", va="bottom", fontsize=10)
arrow(ax, [(0.2, Y), (1.78, Y)])
summ(ax, 2.0, Y); sign(ax, 1.65, Y + 0.35, "+"); sign(ax, 2.3, Y + 0.45, "−")
arrow(ax, [(2.22, Y), (2.95, Y)])
box(ax, 3.6, Y, 1.2, 0.9, "$\\dfrac{1}{J_{xc}}$", fs=13)
arrow(ax, [(4.2, Y), (4.95, Y)])
box(ax, 5.5, Y, 1.0, 0.9, "$\\int$", fs=15)
arrow(ax, [(6.0, Y), (7.15, Y)], label="$\\omega_m$", lpos=(6.55, Y + 0.1))
tri(ax, 7.7, Y, 1.1, 1.0, "$k$", fs=13)
arrow(ax, [(8.25, Y), (10.45, Y)], label="$v$", lpos=(9.0, Y + 0.1))
box(ax, 11.8, Y, 2.7, 1.0, "$F_c = (m_{xc}+m_p)\\, g\\, w_0\\, \\mathrm{sign}(v)$", fc="#FDEDEC", ec=RED, fs=9.5)
arrow(ax, [(13.15, Y), (15.38, Y)], label="$F_c$", lpos=(14.2, Y + 0.1))
summ(ax, 15.6, Y); sign(ax, 15.3, Y + 0.4, "+"); sign(ax, 15.95, Y - 0.45, "−")
# nhánh con lắc
arrow(ax, [(9.4, Y), (9.4, 2.1)])
box(ax, 9.4, 1.6, 1.0, 0.8, "$\\dfrac{d}{dt}$", fs=12)
arrow(ax, [(9.9, 1.6), (11.0, 1.6)], label="$a$", lpos=(10.45, 1.65))
box(ax, 12.4, 1.6, 2.6, 1.15, "Con lắc tải treo\n$\\ddot\\theta = -\\omega_p^2\\,\\theta - a/h$\n$\\omega_p=\\sqrt{g/h}$ = 0.904 rad/s", fc="#EAF4EA", ec=GREEN, fs=9.5)
arrow(ax, [(13.7, 1.6), (14.4, 1.6)], label="$\\theta$", lpos=(14.05, 1.65))
tri(ax, 14.9, 1.6, 0.9, 0.9, "$m_p g$", fs=9)
arrow(ax, [(15.35, 1.6), (15.6, 1.6), (15.6, Y - 0.22)], label="$F_\\theta$", lpos=(16.0, 2.6))
ax.text(17.3, 1.6, "$F_\\theta = m_p\\, g\\, \\theta$\nlực ngang của cáp\ntác dụng lên xe", ha="center", va="center", fontsize=9.5, color=GREEN)
# phản hồi
arrow(ax, [(15.82, Y), (18.4, Y), (18.4, 6.3), (9.05, 6.3)], label="$F_\\Sigma = F_c - F_\\theta$", lpos=(17.2, 6.35))
tri_left(ax, 8.5, 6.3, 1.1, 1.0, "$k/\\eta$", fs=12)
arrow(ax, [(7.95, 6.3), (2.0, 6.3), (2.0, Y + 0.22)], label="$T_c$", lpos=(5.0, 6.35))
ax.text(9.5, 7.25, "Hình 2 — Phần cơ khí mở rộng: xe con + con lắc tải treo (dùng cho mô phỏng góc lắc; phần điện giống Hình 1)",
        ha="center", fontsize=13, fontweight="bold")
ax.text(4.2, 0.25, "$J_{xc} = J_B + \\dfrac{[(\\delta-1)M_\\Sigma + m_{xc}]\\,k^2}{\\eta}$      $m_p = Q + m_{nh}$ (đầy tải) / $m_{nh}$ (không tải)\n"
        "$h = 12$ m; $\\theta > 0$ khi tải ở phía trước xe theo chiều chạy",
        ha="center", fontsize=10.5, bbox=dict(boxstyle="round", fc="#F7F9FC", ec="#C9D6E8"))
fig.savefig(OUTDIR + "/03_So_do_khoi_con_lac.png", dpi=150, bbox_inches="tight")
fig.savefig(OUTDIR + "/03_So_do_khoi_con_lac.svg", bbox_inches="tight")
plt.close(fig)
print("ok")
