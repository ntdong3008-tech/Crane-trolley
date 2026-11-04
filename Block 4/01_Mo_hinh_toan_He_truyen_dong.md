# MÔ HÌNH TOÁN VÀ SƠ ĐỒ KHỐI HỆ TRUYỀN ĐỘNG XE CON CẦU TRỤC ($x = 2$)

**Học phần:** Thiết kế hệ thống truyền động điện (EE4332) — GVHD: TS. Nguyễn Duy Đỉnh
**Nhiệm vụ:** bước 4 — *Xây dựng mô hình hệ truyền động* để chạy mô phỏng (sau: ☑ chọn động cơ, ☑ ước lượng tham số, ☑ mô phỏng kiểm chứng động cơ).
**Công cụ mô phỏng:** PSIM.
**Nguồn công thức và số liệu:** `Block 3/00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx`, sheet `Phu_tai` (mã dòng ghi trong ngoặc vuông, ví dụ `[Phu_tai.Mc]`). Thiết bị: SEW DRN71M4 0.37 kW + ABB ACS380-04xS-01A8-4; lượng đặt $a^*$ = 0.10 m/s², $\rho^*$ = 0.40 m/s³ (CR-19).
**Nguyên tắc:** mô hình đơn giản nhất mà vẫn khớp file Excel.
**Ngày:** 04/11/2026 (cập nhật sau góp ý của nhóm: thêm Kịch bản 1, lưới 380 V, PI chỉnh theo không tải).

| Kịch bản | Nội dung | Mục đích |
| :--- | :--- | :--- |
| **1 — Động cơ đấu lưới** (mục 4) | Khối động cơ KĐB của PSIM cắm thẳng lưới 380 V, kéo phương trình xe con | Đúng sơ đồ thầy vẽ trên bảng: kiểm tra động cơ 0.37 kW kéo được xe con và mô-men cản đúng như Excel |
| **2 — Biến tần FOC bám S-curve** (mục 5) | Động cơ + FOC rút gọn thành $k_M$, có PI tốc độ | Kiểm tra xe chạy đúng quỹ đạo S-curve, mô-men khớp đồ thị phụ tải của Excel |

---

## 1. Cơ sở lý thuyết

Mô hình dùng hai công thức chung của bài giảng `[R5]` (Class_1_Introduction, slide 28 và 31–32):

- **Phương trình động học:** $J \dfrac{d\omega}{dt} = T_{đ} - T_c$
- **Quy đổi lực và quán tính về trục động cơ** qua bộ truyền có tỉ số $i$, hiệu suất $\eta$.

Theo phân loại tải ở cùng bài giảng (slide 22), cơ cấu di chuyển xe con là **tải ma sát khô**: mô-men cản không phụ thuộc tốc độ, chỉ đổi dấu theo chiều chạy.

---

## 2. Giả định

| Mã | Giả định | Hệ quả trong mô hình | Căn cứ |
| :---: | :--- | :--- | :--- |
| GT-01 | Ray nằm ngang, xe chạy trong nhà xưởng | Không có lực dốc, không có lực gió | SRS §1 `[C]` |
| GT-02 | Mọi lực cản di chuyển gộp vào suất cản $w_0$ = 0.015 | $F_c = M g w_0$, không phụ thuộc $v$ | SSoT P-13, Phần 1b |
| GT-03 | Tốc độ thấp $v$ = 0.12 m/s | Bỏ qua lực cản khí động (≈ 0.04 N so với 2,096 N) | SSoT P-09 |
| GT-04 | Bánh thép không biến dạng, không trượt trên ray | $v = k\,\omega_m$, bán kính lăn = $D_{bx}/2$ | SSoT P-12; KT-04 |
| GT-05 | Hộp số $i$ = 155.34; một hiệu suất $\eta$ = 0.90 cho cả chuỗi và cả hai chiều năng lượng | $T_c = F_c k/\eta$ | `[Params.iin]`, SSoT P-15 |
| GT-06 | Quán tính phần quay của hộp số, khớp nối kể bằng $\delta$ = 1.15; quán tính động cơ + phanh $J_B$ cộng riêng | $J_\Sigma = J_B + \delta M k^2/\eta$ | `[Params.delta]`, `[Catalogue.JB]` |
| GT-07 | **Cơ cấu và tải coi như gắn cố định với xe; chỉ xét chuyển động tiến/lùi** | Một khối lượng $M$ duy nhất; không xét lắc tải | Nhóm chốt 04/11/2026 |
| GT-08 | Lưới 3 pha 380 V / 50 Hz | Nguồn của Kịch bản 1 | SSoT P-19 |
| GT-09 | *(chỉ Kịch bản 2)* Vòng dòng của FOC thay bằng khâu quán tính $T_{\Sigma i}$ = 2 ms | Động cơ coi là $T_{đ} = k_M\, i_{sq}$ | Excel `Tham_so_DC` |
| GT-10 | Phanh cơ chỉ đóng khi xe đã dừng | Không đưa phanh vào mô hình khi xe chạy | SRS-FUNC-02 |

Về GT-05: khi hãm tái sinh, đúng ra phải nhân $\eta$ thay vì chia. Với $a^*$ = 0.10 m/s² điều này chỉ xảy ra lúc giảm tốc không tải với mô-men rất nhỏ (−0.27 N·m), nên sai số không đáng kể.

---

## 3. Hệ phương trình (theo Excel v2.0)

**(1) Lực cản di chuyển** (GT-01..03):

$$F_c = M\, g\, w_0\, \mathrm{sign}(v)$$

Đầy tải ($M$ = 14,244 kg): 2,096 N `[Phu_tai.Fc]`; không tải ($M$ = 2,022 kg): 297.5 N `[Phu_tai.Fc0]`.

**(2) Quy đổi tốc độ** (GT-04):

$$k = \frac{D_{bx}}{2i} = \frac{0.25}{2 \cdot 155.34} = 8.047\times10^{-4}\ \text{m/rad}, \qquad v = k\,\omega_m$$

**(3) Mô-men cản quy về trục động cơ** (GT-05):

$$T_c = \frac{F_c\, k}{\eta}$$

Đầy tải 1.874 N·m `[Phu_tai.Mc]`; không tải 0.266 N·m `[Phu_tai.Mc0]`.

**(4) Mô-men động khi xe có gia tốc $a$** (GT-06), đúng công thức `[Phu_tai.Mdg]`:

$$M_{đg} = \frac{\delta\, M\, a\, k}{\eta} + J_B\,\frac{a}{k}$$

**(5) Viết (4) thành phương trình động học** bằng cách thay $a = k\,\dfrac{d\omega_m}{dt}$:

$$J_\Sigma\,\frac{d\omega_m}{dt} = T_{đ} - T_c, \qquad J_\Sigma = J_B + \underbrace{\frac{\delta\, M\, k^2}{\eta}}_{J_{tải}}$$

| | $J_B$ | $J_{tải} = \delta M k^2/\eta$ | $J_\Sigma$ |
| :--- | :---: | :---: | :---: |
| Đầy tải | 0.00262 | 0.01179 | **0.01441 kg·m²** |
| Không tải | 0.00262 | 0.00167 | **0.00429 kg·m²** |

**Kiểm tra khớp Excel:** khi tăng tốc đầy tải với $a^*$ = 0.10 m/s²: $T_{đ}$ = 1.874 + 0.01441 · 0.10 / 8.047×10⁻⁴ = **3.664 N·m**, trùng `[Phu_tai.Mkd]`.

> **Cần sửa trong Excel:** dòng `[Phu_tai.Jl]` đang ghi $\delta M k^2$ = 0.0106 kg·m² (không chia $\eta$), trong khi công thức (4) ở `[Phu_tai.Mdg]` có chia $\eta$. Kết quả chọn thiết bị không đổi, nhưng nên sửa thành $\delta M k^2/\eta$ = 0.01179 và thêm dòng $J_\Sigma$ = 0.01441 cho thống nhất với mô phỏng.

**(6) Hàm sign trong mô phỏng.** Thay $\mathrm{sign}(v)$ bằng $\mathrm{sat}(v/\varepsilon)$, $\varepsilon = 10^{-4}$ m/s: khâu khuếch đại $1/\varepsilon$, nối khâu giới hạn ±1. Khi $|v| > \varepsilon$ kết quả đúng như (1); gần $v = 0$ lực cản giảm tuyến tính về 0, tránh dao động số khi xe vừa khởi động hoặc vừa dừng.

---

## 4. Kịch bản 1 — Động cơ đấu lưới trực tiếp kéo xe con

Đúng sơ đồ thầy vẽ trên bảng: nguồn → động cơ → trục → tải. So với bước 3 (kiểm chứng động cơ với tải hằng số), chỉ thay tải hằng số bằng phương trình (1)–(6) của xe con. Không có biến tần, PI hay S-curve.

![Kịch bản 1](02_Kich_ban_1_Dong_co_dau_luoi.png)

*(Bản vector: `02_Kich_ban_1_Dong_co_dau_luoi.svg`)*

### 4.1. Phần tử PSIM và thông số

| Phần tử PSIM | Thư viện | Thông số | Chức năng |
| :--- | :--- | :--- | :--- |
| 3-ph Sine (nguồn áp 3 pha) | Power → Sources → Voltage | V (line-line, rms) = **380**; Frequency = **50** | Lưới xưởng (GT-08) |
| Induction Machine (rotor lồng sóc) | Power → Motor Drive Module | Rs = **17.247**; Ls = **0.0731**; Rr = **17.312**; Lr = **0.0731**; Lm = **0.9049**; Ns/Nr = **1**; No. of Poles = **4**; Moment of Inertia = **0.00262**; Torque Flag = 1 | DRN71M4, bộ tham số hiệu chỉnh (`Tham_so_DC` mục C). Ls, Lr trong PSIM là **điện cảm tản** |
| Speed Sensor | Power → Mechanical Elements | Mặc định | Đo tốc độ trục $n_m$ (vg/ph) |
| Mechanical Load, điều khiển từ ngoài | Power → Mechanical Elements | Moment of Inertia = **0.01179** (đầy tải) / **0.00167** (không tải) | Nhận mô-men cản $T_c$ từ mạch điều khiển; cộng $J_{tải}$ với $J_B$ thành $J_\Sigma$ |
| Proportional | Control | **0.10472** ($2\pi/60$) | $n_m$ (vg/ph) → $\omega_m$ (rad/s) |
| Proportional | Control | **8.047×10⁻⁴** ($k$) | $\omega_m$ → $v$ |
| Proportional | Control | **10000** ($1/\varepsilon$) | (6) |
| Limiter | Control | −1 … +1 | (6) |
| Proportional | Control | **2096** (đầy tải) / **297.5** (không tải) ($M g w_0$) | $F_c$ |
| Proportional | Control | **8.941×10⁻⁴** ($k/\eta$) | $T_c = F_c k/\eta$ → đưa vào Mechanical Load |
| Integrator (tùy chọn) | Control | Hệ số 1, giá trị đầu 0 | Quãng đường $x$ |

**Hai lỗi cần tránh:**
1. **Không vẽ thêm $1/J$ và $1/s$ bên ngoài.** Khối Induction Machine đã tự giải $(J_B + J_{tải})\,d\omega_m/dt = T_e - T_c$; vẽ thêm sẽ tích phân hai lần.
2. **No. of Poles = 4** (số cực), không phải 2 (số đôi cực). Nhập 2 thì tốc độ đồng bộ thành 3000 vg/ph.

Simulation Control: bước thời gian 1×10⁻⁵ s (mô hình điện của động cơ cần bước nhỏ), tổng thời gian 1.5 s.

### 4.2. Kết quả mong đợi (380 V)

Tính bằng mạch thay thế hình T với bộ tham số hiệu chỉnh:

| Đại lượng | Không tải | Đầy tải | Ghi chú |
| :--- | :---: | :---: | :--- |
| Mô-men cản xác lập $T_c$ | 0.266 N·m | 1.874 N·m | Trùng `[Phu_tai.Mc0]`, `[Phu_tai.Mc]` |
| Mô-men điện từ xác lập $T_e$ | 0.266 N·m | 1.874 N·m | $T_e = T_c$, nhỏ hơn $M_N$ = 2.50 N·m |
| Hệ số trượt | 0.59% | 4.52% | |
| Tốc độ động cơ $n_m$ | 1491.1 vg/ph | 1432.3 vg/ph | |
| Vận tốc xe $v$ | 0.1257 m/s | 0.1207 m/s | Không chỉnh được; thay đổi theo tải |
| Dòng stator xác lập | 0.713 A | 0.874 A | Nhỏ hơn $I_N$ = 1.02 A |
| Mô-men tới hạn $M_K$ | 6.32 N·m | 6.32 N·m | Giảm theo $U^2$ so với 7.00 N·m ở 400 V |
| Thời gian tăng tốc (98% tốc độ) | ≈ 0.14 s | ≈ 0.65 s | Tính tựa tĩnh, chưa kể dao động điện từ lúc đóng điện |
| Gia tốc xe lớn nhất khi khởi động | **1.14 m/s²** | 0.25 m/s² | Không tải **vượt** $a_{\max}$ = 0.5 m/s² |

**Lưu ý khi đọc kết quả:**
- Lúc đóng điện, mô hình động cơ cho dao động mô-men vài chu kỳ đầu, có thể vượt $M_K$. Đó là hiện tượng thật khi khởi động trực tiếp, không phải lỗi.
- Bộ tham số hiệu chỉnh cho mô-men khởi động ($s$ = 1) là 4.45 N·m ở 380 V và dòng khởi động 3.97 A, **thấp hơn catalogue** ($M_A$ = 2.8·$M_N$ = 7.0 N·m, $I_A$ = 4.8·$I_N$ = 4.9 A ở 400 V). Mạch thay thế một lồng sóc không khớp được cùng lúc mô-men khởi động và mô-men tới hạn, nên đồ thị khởi động trên PSIM sẽ "hiền" hơn thực tế.

### 4.3. Kết luận rút ra từ Kịch bản 1 — vì sao cần biến tần (dẫn sang Kịch bản 2)

1. **Gia tốc vượt giới hạn đề bài khi không tải:** khoảng 1.14 m/s² > 0.5 m/s². Lực cần để tăng tốc khi đó khoảng 2,600 N, vượt lực bám của bánh dẫn lúc không tải (1,983 N), nên **bánh xe trượt trên ray**.
2. **Không khống chế được độ giật:** mô-men nhảy bậc khi đóng điện, trái với yêu cầu $\rho \le 2.0$ m/s³.
3. **Không chỉnh được tốc độ:** vận tốc 0.1207–0.1257 m/s tùy tải, không có tốc độ bò để căn vị trí.
4. **Dòng khởi động lớn:** catalogue cho $I_A$ = 4.8·$I_N$.

---

## 5. Kịch bản 2 — Biến tần FOC bám quỹ đạo S-curve

Động cơ + FOC rút gọn thành khâu $k_M$ (GT-09), nên phần cơ khí phải vẽ đủ $1/J_\Sigma$ và $1/s$ (khác Kịch bản 1). Bộ PI tốc độ và phản hồi encoder được vẽ ra ngoài vì không còn khối biến tần đóng gói sẵn.

![Kịch bản 2](03_Kich_ban_2_S_curve_FOC.png)

*(Bản vector: `03_Kich_ban_2_S_curve_FOC.svg`)*

### 5.1. Phần tử PSIM và thông số

Toàn bộ dựng trong mạch điều khiển của PSIM.

| Khối | Phần tử PSIM | Thông số |
| :--- | :--- | :--- |
| $a^*(t)$ | Piecewise Linear Voltage Source (nối đất) | Các điểm ở mục 5.2 |
| $1/s$ (S-curve) | Integrator | Hệ số 1, giá trị đầu 0 → ra $v^*$ |
| $1/k$ | Proportional | 1242.7 |
| Σ tốc độ | Summer (+, −) | — |
| PI tốc độ | PI controller, $G(s) = k\,\dfrac{1+sT}{sT}$ | $k$ = **0.426** A/(rad/s); $T$ = **0.008** s |
| Giới hạn dòng | Limiter | **−2.34 … +2.34** A |
| Trễ vòng dòng | Transfer function bậc 1: $\dfrac{1}{1 + sT_{\Sigma i}}$ | $T_{\Sigma i}$ = **0.002** s |
| $k_M$ | Proportional | 2.52 |
| Σ mô-men | Summer (+, −) | — |
| $1/J_\Sigma$ | Proportional | **233.1** (không tải) / **69.40** (đầy tải) |
| $1/s$ (cơ khí) | Integrator | Hệ số 1, giá trị đầu 0 → ra $\omega_m$ |
| $k$ | Proportional | 8.047×10⁻⁴ |
| $F_c$ | Proportional $1/\varepsilon$ → Limiter ±1 → Proportional $M g w_0$ | 10000; 297.5 / 2096 |
| $k/\eta$ | Proportional | 8.941×10⁻⁴ |

**Cách tính các thông số mới:**
- **Giới hạn dòng ±2.34 A:** biến tần ACS380-01A8-4 cho phép $1.5\,I_{Hd}$ = 1.8 A (hiệu dụng) trong 1 phút/10 phút, tức biên độ 2.55 A. Trừ thành phần từ hóa $i_{sd}$ = 1.00 A: $i_{sq,\max} = \sqrt{2.55^2 - 1.00^2}$ = 2.34 A, ứng với $T_{đ,\max}$ = 2.52 · 2.34 = 5.9 N·m.
- **PI tốc độ chỉnh theo tối ưu đối xứng tại trạng thái không tải** (nhóm chốt 04/11/2026; bài giảng Bài 2.1): $k = \dfrac{J_{\Sigma,0}}{2\,k_M\,T_{\Sigma i}} = \dfrac{0.00429}{2 \cdot 2.52 \cdot 0.002}$ = 0.426; $T = 4\,T_{\Sigma i}$ = 8 ms. Độ dự trữ pha: 36.9° khi không tải, 28.9° khi đầy tải ($J_\Sigma$ lớn gấp 3.4 lần) — vẫn ổn định. Với lượng đặt S-curve (thay đổi mềm), độ vọt lố thực tế nhỏ hơn nhiều so với đáp ứng bậc thang.

### 5.2. Cài đặt mô phỏng một hành trình

Gia tốc đặt của S-curve 7 đoạn có dạng hình thang nên nhập đúng bằng nguồn tuyến tính từng đoạn. Đoạn chạy đều rút ngắn còn 3 s.

| Thời điểm (s) | 0 | 0.25 | 1.20 | 1.45 | 4.45 | 4.70 | 5.65 | 5.90 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $a^*$ (m/s²) | 0 | 0.10 | 0.10 | 0 | 0 | −0.10 | −0.10 | 0 |

Các mốc lấy từ Excel: $T_j$ = 0.25 s `[Phu_tai.Tj]`, $T_a$ = 0.95 s `[Phu_tai.Ta]`, $t_{acc}$ = 1.45 s `[Phu_tai.tacc]`. Diện tích một hình thang = 0.10 × (0.95 + 0.25) = 0.12 m/s, đúng $v_{\max}$.

Simulation Control: bước thời gian 1×10⁻⁴ s; tổng thời gian 7 s. Chạy hai lần (không tải, đầy tải), mỗi lần chỉ đổi $1/J_\Sigma$ và $M g w_0$.

**Kết quả mong đợi (đầy tải):** $v$ lên 0.12 m/s trong 1.45 s và giữ đúng 0.12 m/s ở cả hai trạng thái tải (khác Kịch bản 1); $T_{đ}$ ≈ 3.66 N·m trong đoạn gia tốc không đổi, 1.874 N·m khi chạy đều, ≈ 0.08 N·m khi giảm tốc — các giá trị của đồ thị phụ tải trong `Phu_tai` (cột I..M). Bộ PI làm $T_{đ}$ lệch một chút ở các chỗ chuyển đoạn. Gia tốc xe không vượt 0.10 m/s², $i_{sq}$ không chạm giới hạn 2.34 A.

---

## 6. Hệ số mô-men $k_M$ (dùng ở Kịch bản 2)

Với FOC, khi từ thông rotor giữ ở định mức:

$$T_{đ} = \frac{3}{2}\, p\, \frac{L_m}{L_r}\, \psi_r\, i_{sq} = k_M\, i_{sq}$$

| Đại lượng | Công thức | Giá trị |
| :--- | :--- | :---: |
| Điện cảm rotor | $L_r = L_m + L_{\sigma r}$ | 0.978 H |
| Dòng từ hóa định mức (biên độ dq) | từ mạch thay thế hình T tại điểm định mức | $i_{sd,N}$ = 1.00 A |
| Từ thông rotor định mức | $\psi_r = L_m\, i_{sd,N}$ | 0.907 Wb |
| Hệ số mô-men | $k_M = \tfrac32 p\,(L_m/L_r)\,\psi_r$ | 2.52 N·m/A |

Kiểm tra: tại điểm định mức ($i_{sq}$ = 1.01 A) cho $T_{đ}$ = 2.54 N·m, catalogue 2.50 N·m (lệch 1.6%).

---

## 7. Khác biệt so với ví dụ xe máy điện trên lớp

| Thành phần | Xe máy điện | Xe con cầu trục | Giả định |
| :--- | :--- | :--- | :---: |
| Nối động cơ – bánh | Trực tiếp, $v = r\,\omega$, bán kính lốp $r_{eff}$ | Qua hộp số, $v = k\,\omega_m$, $k = D/(2i)$ | GT-04, GT-05 |
| Quy đổi lực → mô-men | $T = F\,r$ | $T = F\,k/\eta$ | GT-05 |
| Lực cản | Lăn + dốc + khí động ($\propto v^2$) | Chỉ ma sát khô $F_c = M g w_0$ | GT-01..03 |
| Nguồn cấp | Lưới trực tiếp | Kịch bản 1: lưới trực tiếp 380 V; Kịch bản 2: biến tần FOC | GT-08, GT-09 |

---

## 8. Việc tiếp theo

1. Sửa dòng `[Phu_tai.Jl]` trong Excel (mục 3).
2. Dựng và chạy Kịch bản 1 (không tải, đầy tải); chụp đồ thị $v(t)$, $T_e(t)$, $T_c(t)$, $i_{abc}(t)$; so với bảng mục 4.2.
3. Dựng và chạy Kịch bản 2; so $v(t)$, $T_{đ}(t)$ với đồ thị phụ tải của Excel.
4. Có thể khai báo các hệ số bằng phần tử *Parameter File* của PSIM (lấy số từ các bảng trên) để không gõ tay hằng số.

**Còn chờ nhóm chốt:** lượng đặt giữ $a^*$ = 0.10 / $\rho^*$ = 0.40, hay đổi sang 0.06 / 0.24 cho khớp TCVN 4244:2005 Bảng 2.1.2.3.1.1. Nếu đổi, chỉ thay bảng điểm PWL ở mục 5.2.
