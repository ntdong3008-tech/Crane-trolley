"""Vẽ sơ đồ khối mô hình hệ truyền động xe con cầu trục cho PSIM.

Kịch bản 1: động cơ đấu lưới trực tiếp kéo xe con (giống bảng của thầy).
Kịch bản 2: biến tần FOC bám quỹ đạo S-curve (động cơ + FOC rút gọn thành k_M).

Chạy: python ve_so_do_khoi.py "<thư mục lưu hình>"
"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon

OUTDIR = sys.argv[1] if len(sys.argv) > 1 else "."
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "mathtext.fontset": "dejavusans"})
BLUE = "#1F4E79"; GREY = "#7F7F7F"; RED = "#B03A2E"; GREEN = "#2E7D32"; GOLD = "#B7950B"; BLACK = "black"


def box(ax, x, y, w, h, text, fc="#FFFFFF", ec=BLUE, fs=11, ls="-", lw=1.6):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02", fc=fc, ec=ec, lw=lw, ls=ls))
    if text:
        ax.text(x, y, text, ha="center", va="center", fontsize=fs)


def gain(ax, x, y, w, h, text, left=False, fs=12, ec=BLUE):
    pts = [(x + w / 2, y - h / 2), (x + w / 2, y + h / 2), (x - w / 2, y)] if left else \
          [(x - w / 2, y - h / 2), (x - w / 2, y + h / 2), (x + w / 2, y)]
    ax.add_patch(Polygon(pts, closed=True, fc="white", ec=ec, lw=1.6))
    ax.text(x + (w / 8 if left else -w / 8), y, text, ha="center", va="center", fontsize=fs)


def summ(ax, x, y, r=0.22):
    ax.add_patch(Circle((x, y), r, fc="white", ec="black", lw=1.4))
    for s in (1, -1):
        ax.plot([x - r * 0.7, x + r * 0.7], [y - s * r * 0.7, y + s * r * 0.7], color="black", lw=0.8)


def arrow(ax, pts, color="black", ls="-", label=None, lpos=None, lw=1.4):
    for (x0, y0), (x1, y1) in zip(pts[:-2], pts[1:-1]):
        ax.plot([x0, x1], [y0, y1], color=color, ls=ls, lw=lw)
    ax.annotate("", xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, ls=ls, mutation_scale=14))
    if label:
        ax.text(lpos[0], lpos[1], label, ha="center", va="bottom", fontsize=11, color=color)


def sign(ax, x, y, s):
    ax.text(x, y, s, ha="center", va="center", fontsize=13, fontweight="bold")


def limiter(ax, x, y, w=0.9, h=0.8):
    box(ax, x, y, w, h, "")
    ax.plot([x - w * 0.35, x - w * 0.15, x + w * 0.15, x + w * 0.35], [y - h * 0.25, y - h * 0.25, y + h * 0.25, y + h * 0.25], color=BLUE, lw=1.6)


# =============================================================== Kịch bản 1
fig, ax = plt.subplots(figsize=(20, 8.6))
ax.set_xlim(-0.3, 20.3); ax.set_ylim(0.3, 8.6); ax.axis("off")
ax.text(10.0, 8.25, "Kịch bản 1 — Động cơ đấu lưới trực tiếp kéo xe con (dựng bằng phần tử PSIM)", ha="center", fontsize=14, fontweight="bold")
Y = 5.6  # trục cơ khí
for dy in (0.6, 0, -0.6):
    ax.add_patch(Circle((0.5, Y + dy), 0.22, fc="white", ec="black", lw=1.3)); ax.text(0.5, Y + dy, "~", ha="center", va="center", fontsize=13)
    ax.plot([0.72, 2.6], [Y + dy, Y + dy], color="black", lw=1.2)
ax.text(0.5, Y + 1.05, "Lưới 3 pha\n380 V / 50 Hz\n(3-ph Sine)", ha="center", va="bottom", fontsize=10)
ax.plot([1.6, 1.6], [Y - 0.75, Y - 1.3], color=GREY, lw=1); ax.text(1.6, Y - 1.45, "đo $U$, $I$", ha="center", va="top", fontsize=10, color=GREY)
ax.add_patch(Circle((3.4, Y), 0.85, fc="#EEF4FB", ec=BLUE, lw=1.8)); ax.add_patch(Circle((3.4, Y), 0.5, fc="white", ec=BLUE, lw=1.2))
ax.text(3.4, Y + 1.0, "Induction Motor\nDRN71M4, 4 cực, $J_B$", ha="center", va="bottom", fontsize=10)
# trục
ax.plot([4.25, 6.6], [Y, Y], color=BLACK, lw=4); ax.text(5.4, Y + 0.15, "trục", ha="center", va="bottom", fontsize=9, color=GREY)
box(ax, 7.2, Y, 1.2, 0.9, "Speed\nSensor", fc="#F4F4F4", ec=BLACK, fs=10)
ax.plot([7.8, 10.4], [Y, Y], color=BLACK, lw=4)
box(ax, 11.4, Y, 2.0, 1.2, "Mechanical\nLoad (ngoài)\n$J_{tải} = \\delta M k^2/\\eta$", fc="#FDEDEC", ec=RED, fs=10)
ax.text(11.4, Y + 0.85, "nhận mô-men cản $T_c$ từ mạch điều khiển", ha="center", va="bottom", fontsize=9, color=RED)
# mạch điều khiển (hàng dưới)
Yc = 2.6
arrow(ax, [(7.2, Y - 0.45), (7.2, Yc), (7.75, Yc)], label="$n_m$ (vg/ph)", lpos=(6.55, 3.6))
gain(ax, 8.25, Yc, 1.0, 0.9, "$\\frac{2\\pi}{60}$", fs=11)
arrow(ax, [(8.75, Yc), (9.35, Yc)], label="$\\omega_m$", lpos=(9.05, Yc + 0.08))
gain(ax, 9.8, Yc, 0.9, 0.9, "$k$", fs=12)
arrow(ax, [(10.25, Yc), (11.15, Yc)], label="$v$", lpos=(10.6, Yc + 0.08))
gain(ax, 11.6, Yc, 0.9, 0.9, "$\\frac{1}{\\varepsilon}$", fs=11)
arrow(ax, [(12.05, Yc), (12.45, Yc)])
limiter(ax, 12.9, Yc)
arrow(ax, [(13.35, Yc), (13.75, Yc)])
gain(ax, 14.25, Yc, 1.0, 0.9, "$Mgw_0$", fs=9)
arrow(ax, [(14.75, Yc), (15.45, Yc)], label="$F_c$", lpos=(15.1, Yc + 0.08))
gain(ax, 15.95, Yc, 1.0, 0.9, "$k/\\eta$", fs=11)
arrow(ax, [(16.45, Yc), (17.3, Yc), (17.3, 4.4), (11.4, 4.4), (11.4, Y - 0.62)], label="$T_c$", lpos=(17.6, 3.3))
ax.text(15.6, Yc - 0.75, "$F_c = M g w_0\\,\\mathrm{sat}(v/\\varepsilon)$,  $\\varepsilon = 10^{-4}$ m/s", ha="center", va="top", fontsize=10, color=RED)
# quãng đường (tùy chọn)
arrow(ax, [(10.7, Yc), (10.7, 1.3), (11.3, 1.3)], color=GREY)
box(ax, 11.75, 1.3, 0.8, 0.7, "$\\frac{1}{s}$", ec=GREY, fs=11)
arrow(ax, [(12.15, 1.3), (12.8, 1.3)], color=GREY, label="$x$", lpos=(12.5, 1.33))
ax.text(14.2, 1.3, "quãng đường (tùy chọn)", ha="center", va="center", fontsize=9, color=GREY)
box(ax, 3.4, 2.1, 5.6, 1.6, "", fc="#F7F9FC", ec="#C9D6E8", lw=1.0)
ax.text(3.4, 2.1, "Không vẽ thêm $1/J$ và $1/s$ bên ngoài:\nkhối Induction Motor đã tự giải\n$(J_B + J_{tải})\\,d\\omega_m/dt = T_e - T_c$",
        ha="center", va="center", fontsize=10.5)
fig.savefig(OUTDIR + "/02_Kich_ban_1_Dong_co_dau_luoi.png", dpi=150, bbox_inches="tight")
fig.savefig(OUTDIR + "/02_Kich_ban_1_Dong_co_dau_luoi.svg", bbox_inches="tight")
plt.close(fig)

# =============================================================== Kịch bản 2
fig, ax = plt.subplots(figsize=(21, 8.4))
ax.set_xlim(-0.3, 21.3); ax.set_ylim(0.0, 8.2); ax.axis("off")
Y = 4.0
box(ax, 7.4, Y + 0.05, 6.6, 2.6, "", fc="#EEF4FB", ec=BLUE, ls="--", lw=1.0)
ax.text(7.4, Y + 1.55, "Biến tần ACS380 + ĐC DRN71M4 (FOC rút gọn)", ha="center", fontsize=10, color=BLUE)
box(ax, 15.6, Y + 0.85, 9.0, 4.6, "", fc="#FDF5F4", ec=RED, ls="--", lw=1.0)
ax.text(15.6, Y + 3.35, "Phần cơ khí: xe con + tải (khối cứng), quy về trục động cơ", ha="center", fontsize=10, color=RED)
box(ax, 0.55, Y, 1.0, 1.1, "$a^*(t)$\nPWL", fc="#FFF8E1", ec=GOLD, fs=10)
ax.text(0.95, Y + 1.1, "Quỹ đạo S-curve", ha="center", fontsize=10, color=GOLD)
arrow(ax, [(1.05, Y), (1.3, Y)])
box(ax, 1.62, Y, 0.6, 0.8, "$\\frac{1}{s}$", fc="#FFF8E1", ec=GOLD, fs=11)
arrow(ax, [(1.92, Y), (2.15, Y)])
ax.text(2.03, Y + 0.5, "$v^*$", ha="center", fontsize=11)
gain(ax, 2.6, Y, 0.9, 0.9, "$1/k$", fs=11)
arrow(ax, [(3.05, Y), (3.68, Y)], label="$\\omega^*$", lpos=(3.37, Y + 0.08))
summ(ax, 3.9, Y); sign(ax, 3.58, Y + 0.38, "+"); sign(ax, 4.2, Y - 0.45, "−")
arrow(ax, [(4.12, Y), (4.6, Y)])
box(ax, 5.35, Y, 1.5, 0.95, "PI tốc độ\n$k\\,\\frac{1+sT}{sT}$", fs=10)
ax.text(5.35, Y - 0.75, "$k$ = 0.426; $T$ = 8 ms", ha="center", va="top", fontsize=9, color=BLUE)
arrow(ax, [(6.1, Y), (6.5, Y)])
limiter(ax, 6.95, Y)
ax.text(6.95, Y - 0.6, "±2.34 A", ha="center", va="top", fontsize=9, color=BLUE)
arrow(ax, [(7.4, Y), (7.9, Y)], label="$i_{sq}^*$", lpos=(7.65, Y + 0.08))
box(ax, 8.55, Y, 1.2, 0.9, "$\\frac{1}{1+sT_{\\Sigma i}}$", fs=11)
ax.text(8.55, Y - 0.6, "$T_{\\Sigma i}$ = 2 ms", ha="center", va="top", fontsize=9, color=BLUE)
arrow(ax, [(9.15, Y), (9.7, Y)], label="$i_{sq}$", lpos=(9.42, Y + 0.08))
gain(ax, 10.2, Y, 1.0, 1.0, "$k_M$", fs=12)
arrow(ax, [(10.7, Y), (11.48, Y)], label="$T_{đ}$", lpos=(11.1, Y + 0.08))
summ(ax, 11.7, Y); sign(ax, 11.38, Y + 0.38, "+"); sign(ax, 12.0, Y + 0.45, "−")
arrow(ax, [(11.92, Y), (12.35, Y)])
box(ax, 12.9, Y, 1.0, 0.9, "$\\frac{1}{J_\\Sigma}$", fs=13)
arrow(ax, [(13.4, Y), (13.8, Y)])
box(ax, 14.2, Y, 0.75, 0.9, "$\\frac{1}{s}$", fs=13)
arrow(ax, [(14.58, Y), (15.45, Y)], label="$\\omega_m$", lpos=(15.0, Y + 0.08))
gain(ax, 15.9, Y, 0.9, 0.9, "$k$", fs=13)
arrow(ax, [(16.35, Y), (17.0, Y)], label="$v$", lpos=(16.67, Y + 0.08))
box(ax, 18.3, Y, 2.5, 1.0, "$F_c = M\\, g\\, w_0\\, \\mathrm{sat}(v/\\varepsilon)$", fc="#FDEDEC", ec=RED, fs=11)
arrow(ax, [(19.55, Y), (20.4, Y), (20.4, 6.3), (16.4, 6.3)], label="$F_c$", lpos=(20.7, 5.0))
gain(ax, 15.9, 6.3, 1.0, 0.95, "$k/\\eta$", left=True, fs=11)
arrow(ax, [(15.4, 6.3), (11.7, 6.3), (11.7, Y + 0.22)], label="$T_c$", lpos=(13.5, 6.35))
arrow(ax, [(15.0, Y), (15.0, 1.6), (3.9, 1.6), (3.9, Y - 0.22)], color=GREEN, ls="--")
ax.text(9.4, 1.15, "Encoder ES7C: phản hồi tốc độ động cơ $\\omega_m$", ha="center", fontsize=10, color=GREEN)
ax.text(10.6, 7.75, "Kịch bản 2 — Biến tần FOC bám quỹ đạo S-curve (dựng bằng phần tử điều khiển PSIM)", ha="center", fontsize=14, fontweight="bold")
ax.text(4.3, 6.75, "$J_\\Sigma \\frac{d\\omega_m}{dt} = T_{đ} - T_c$     $T_c = \\frac{F_c\\, k}{\\eta}$     "
        "$J_\\Sigma = J_B + \\frac{\\delta M k^2}{\\eta}$     $v = k\\,\\omega_m$", ha="center", fontsize=11.5,
        bbox=dict(boxstyle="round", fc="#F7F9FC", ec="#C9D6E8"))
fig.savefig(OUTDIR + "/03_Kich_ban_2_S_curve_FOC.png", dpi=150, bbox_inches="tight")
fig.savefig(OUTDIR + "/03_Kich_ban_2_S_curve_FOC.svg", bbox_inches="tight")
plt.close(fig)
print("ok")
