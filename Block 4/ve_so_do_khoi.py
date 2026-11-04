"""Vẽ sơ đồ khối mô hình hệ truyền động xe con cầu trục (bản đơn giản cho mô phỏng).

Chạy: python ve_so_do_khoi.py "<thư mục lưu hình>"
"""
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, Polygon

OUTDIR = sys.argv[1] if len(sys.argv) > 1 else "."
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10, "mathtext.fontset": "dejavusans"})
BLUE = "#1F4E79"; GREY = "#7F7F7F"; RED = "#B03A2E"; GREEN = "#2E7D32"; GOLD = "#B7950B"


def box(ax, x, y, w, h, text, fc="#FFFFFF", ec=BLUE, fs=11, ls="-", lw=1.6):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.02", fc=fc, ec=ec, lw=lw, ls=ls))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs)


def gain(ax, x, y, w, h, text, left=False, fs=12):
    pts = [(x + w / 2, y - h / 2), (x + w / 2, y + h / 2), (x - w / 2, y)] if left else \
          [(x - w / 2, y - h / 2), (x - w / 2, y + h / 2), (x + w / 2, y)]
    ax.add_patch(Polygon(pts, closed=True, fc="white", ec=BLUE, lw=1.6))
    ax.text(x + (w / 8 if left else -w / 8), y, text, ha="center", va="center", fontsize=fs)


def summ(ax, x, y, r=0.22):
    ax.add_patch(Circle((x, y), r, fc="white", ec="black", lw=1.4))
    for s in (1, -1):
        ax.plot([x - r * 0.7, x + r * 0.7], [y - s * r * 0.7, y + s * r * 0.7], color="black", lw=0.8)


def arrow(ax, pts, color="black", ls="-", label=None, lpos=None):
    for (x0, y0), (x1, y1) in zip(pts[:-2], pts[1:-1]):
        ax.plot([x0, x1], [y0, y1], color=color, ls=ls, lw=1.4)
    ax.annotate("", xy=pts[-1], xytext=pts[-2], arrowprops=dict(arrowstyle="-|>", color=color, lw=1.4, ls=ls, mutation_scale=14))
    if label:
        ax.text(lpos[0], lpos[1], label, ha="center", va="bottom", fontsize=11, color=color)


def sign(ax, x, y, s):
    ax.text(x, y, s, ha="center", va="center", fontsize=13, fontweight="bold")


fig, ax = plt.subplots(figsize=(20, 8.4))
ax.set_xlim(-0.3, 20.3); ax.set_ylim(0.0, 8.2); ax.axis("off")
Y = 4.0

# Nhóm khối (nền)
box(ax, 6.55, Y + 0.05, 4.9, 2.6, "", fc="#EEF4FB", ec=BLUE, ls="--", lw=1.0)
ax.text(6.55, Y + 1.55, "Biến tần ACS380 + ĐC DRN71M4 (FOC, vòng dòng coi là lý tưởng)", ha="center", fontsize=10, color=BLUE)
box(ax, 14.4, Y + 0.85, 8.9, 4.6, "", fc="#FDF5F4", ec=RED, ls="--", lw=1.0)
ax.text(14.4, Y + 3.35, "Phần cơ khí: xe con + tải (khối cứng), quy về trục động cơ", ha="center", fontsize=10, color=RED)

# Lượng đặt: a*(t) hình thang (nguồn PWL) -> tích phân -> v*(t) S-curve
box(ax, 0.55, Y, 1.0, 1.1, "$a^*(t)$\nPWL", fc="#FFF8E1", ec=GOLD, fs=10)
ax.text(0.95, Y + 1.1, "Quỹ đạo S-curve", ha="center", fontsize=10, color=GOLD)
arrow(ax, [(1.05, Y), (1.3, Y)])
box(ax, 1.62, Y, 0.6, 0.8, "$\\dfrac{1}{s}$", fc="#FFF8E1", ec=GOLD, fs=11)
arrow(ax, [(1.92, Y), (2.15, Y)], label="$v^*$", lpos=(2.03, Y + 0.08))
gain(ax, 2.6, Y, 0.9, 0.9, "$1/k$", fs=11)
arrow(ax, [(3.05, Y), (3.68, Y)], label="$\\omega^*$", lpos=(3.37, Y + 0.08))
summ(ax, 3.9, Y); sign(ax, 3.58, Y + 0.38, "+"); sign(ax, 4.2, Y - 0.45, "−")
arrow(ax, [(4.12, Y), (4.6, Y)])
box(ax, 5.35, Y, 1.5, 0.95, "PI tốc độ\n$K_p\\left(1+\\dfrac{1}{T_i s}\\right)$", fs=9.5)
arrow(ax, [(6.1, Y), (6.85, Y)], label="$i_{sq}^*$", lpos=(6.48, Y + 0.08))
gain(ax, 7.4, Y, 1.0, 1.0, "$k_M$", fs=12)
ax.text(7.4, Y - 0.85, "$T_{đ} = k_M\\, i_{sq}$", ha="center", fontsize=10, color=BLUE)
arrow(ax, [(7.9, Y), (9.53, Y)], label="$T_{đ}$", lpos=(8.7, Y + 0.08))

# Cơ khí
summ(ax, 9.75, Y); sign(ax, 9.43, Y + 0.38, "+"); sign(ax, 10.05, Y + 0.45, "−")
arrow(ax, [(9.97, Y), (10.5, Y)])
box(ax, 11.1, Y, 1.05, 0.9, "$\\dfrac{1}{J_\\Sigma}$", fs=13)
arrow(ax, [(11.63, Y), (12.1, Y)])
box(ax, 12.55, Y, 0.8, 0.9, "$\\dfrac{1}{s}$", fs=13)
arrow(ax, [(12.95, Y), (14.05, Y)], label="$\\omega_m$", lpos=(13.5, Y + 0.08))
gain(ax, 14.55, Y, 1.0, 0.95, "$k$", fs=13)
arrow(ax, [(15.05, Y), (15.8, Y)], label="$v$", lpos=(15.42, Y + 0.08))
box(ax, 17.1, Y, 2.5, 1.0, "$F_c = M\\, g\\, w_0\\, \\mathrm{sat}(v/\\varepsilon)$", fc="#FDEDEC", ec=RED, fs=11)
ax.text(17.1, Y - 0.75, "sat: giới hạn ±1; $\\varepsilon = 10^{-4}$ m/s", ha="center", va="top", fontsize=9, color=RED)
arrow(ax, [(18.35, Y), (19.2, Y), (19.2, 6.3), (15.05, 6.3)], label="$F_c$", lpos=(19.5, 5.0))
gain(ax, 14.55, 6.3, 1.0, 0.95, "$k/\\eta$", left=True, fs=11)
arrow(ax, [(14.05, 6.3), (9.75, 6.3), (9.75, Y + 0.22)], label="$T_c$", lpos=(11.9, 6.35))

# Phản hồi tốc độ (encoder)
arrow(ax, [(13.55, Y), (13.55, 1.6), (3.9, 1.6), (3.9, Y - 0.22)], color=GREEN, ls="--")
ax.text(8.7, 1.15, "Encoder ES7C: phản hồi tốc độ động cơ $\\omega_m$", ha="center", fontsize=10, color=GREEN)
# Đầu ra quan sát
arrow(ax, [(15.42, Y), (15.42, 2.75)], color=GREY)
ax.text(15.42, 2.45, "$v(t)$, $T_{đ}(t)$: so với\nđồ thị phụ tải Excel", ha="center", va="top", fontsize=9.5, color=GREY)

ax.text(10.15, 7.75, "Sơ đồ khối mô hình hệ truyền động xe con cầu trục (dựng bằng phần tử điều khiển PSIM)", ha="center", fontsize=14, fontweight="bold")
ax.text(4.6, 6.75, "$J_\\Sigma \\dfrac{d\\omega_m}{dt} = T_{đ} - T_c$      $T_c = \\dfrac{F_c\\, k}{\\eta}$      "
        "$J_\\Sigma = J_B + \\dfrac{\\delta M k^2}{\\eta}$      $v = k\\,\\omega_m$", ha="center", fontsize=11.5,
        bbox=dict(boxstyle="round", fc="#F7F9FC", ec="#C9D6E8"))

fig.savefig(OUTDIR + "/02_So_do_khoi_mo_phong.png", dpi=150, bbox_inches="tight")
fig.savefig(OUTDIR + "/02_So_do_khoi_mo_phong.svg", bbox_inches="tight")
print("ok")
