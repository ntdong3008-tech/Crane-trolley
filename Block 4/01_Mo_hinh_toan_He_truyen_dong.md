# MÔ HÌNH TOÁN VÀ SƠ ĐỒ KHỐI HỆ TRUYỀN ĐỘNG XE CON CẦU TRỤC ($x = 2$)

**Học phần:** Thiết kế hệ thống truyền động điện (EE4332) — GVHD: TS. Nguyễn Duy Đỉnh
**Nhiệm vụ:** bước 4 — *Xây dựng mô hình hệ truyền động* (sau: ☑ chọn động cơ, ☑ ước lượng tham số, ☑ mô phỏng kiểm chứng động cơ).
**Nguồn công thức và số liệu:** `Block 3/00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx`, sheet `Phu_tai` (mã dòng ghi trong ngoặc vuông, ví dụ `[Phu_tai.Mc]`). Thiết bị: SEW DRN71M4 0.37 kW + ABB ACS380-04xS-01A8-4; lượng đặt $a^*$ = 0.10 m/s², $\rho^*$ = 0.40 m/s³ (CR-19).
**Ngày:** 04/11/2026

---

## 1. Cơ sở lý thuyết

Mô hình dựa trên hai công thức chung của bài giảng `[R5]` (Class_1_Introduction, slide 28 và 31–32), áp dụng cho mọi hệ truyền động:

- **Phương trình động học:** $J \dfrac{d\omega}{dt} = T_{đ} - T_c$
- **Quy đổi mô-men và quán tính về trục động cơ** qua bộ truyền có tỉ số $i$ và hiệu suất $\eta$.

Theo phân loại tải ở cùng bài giảng (slide 22), cơ cấu di chuyển xe con là **tải ma sát khô**: mô-men cản không phụ thuộc tốc độ, chỉ đổi dấu theo chiều chuyển động. Đây là điểm khác cơ bản so với ví dụ xe máy điện trên lớp, nơi có lực khí động tỉ lệ $v^2$ (tải dạng quạt gió) và lực dốc.

---

## 2. Giả định của hệ truyền động xe con

| Mã | Giả định | Hệ quả trong mô hình | Căn cứ |
| :---: | :--- | :--- | :--- |
| GT-01 | Ray nằm ngang, xe chạy trong nhà xưởng | Không có lực dốc, không có lực gió | SRS §1.1–1.2 (ray nhà xưởng) `[C]` |
| GT-02 | Mọi lực cản di chuyển (lăn bánh thép/ray, ma sát ổ trục, ma sát gờ bánh) gộp vào suất cản $w_0$ = 0.015 | $F_c = M g w_0$, không phụ thuộc $v$ (tải ma sát khô) | SSoT P-13, Phần 1b |
| GT-03 | Tốc độ thấp $v$ = 0.12 m/s | Lực cản khí động bỏ qua (≈ 0.04 N so với $F_c$ ≈ 2,096 N) | SSoT P-09 |
| GT-04 | Bánh thép trên ray thép không biến dạng | Bán kính lăn = $D_{bx}/2$ (không cần $r_{eff}$ như lốp xe) | SSoT P-12 |
| GT-05 | Bánh dẫn không trượt trên ray | $v = k\,\omega_m$ đúng tuyệt đối; kiểm $k_{bám} \ge 1.2$ | `Kiem_tra` KT-04, KT-05 |
| GT-06 | Truyền động qua hộp số SEW R87, $i$ = 155.34; hiệu suất cả chuỗi $\eta$ = 0.90 | Khi động cơ kéo: chia $\eta$; khi hãm tái sinh: nhân $\eta$ | `[Params.iin]`, SSoT P-15 |
| GT-07 | Quán tính các chi tiết quay của hộp số, khớp nối kể bằng hệ số $\delta$ = 1.15 nhân khối lượng tịnh tiến; quán tính động cơ + phanh $J_B$ cộng riêng | $M_{đg} = \delta M a k/\eta + J_B a/k$ | `[Params.delta]`, `[Catalogue.JB]` |
| GT-08 | **Tải gắn cứng với xe** (bỏ qua lắc khi tính chọn thiết bị) | Một khối lượng $M_\Sigma$ duy nhất | Excel v2.0 toàn bộ sheet `Phu_tai` |
| GT-09 | Động cơ cấp từ biến tần FOC; vòng dòng điện nhanh hơn nhiều so với cơ khí | Động cơ coi như nguồn mô-men $T_{đ} = k_M\, i_{sq}$ | Excel v2.0 `Tham_so_DC` |
| GT-10 | Phanh cơ chỉ đóng khi $v \approx 0$ | Phanh không tham gia phương trình khi xe chạy | SRS-FUNC-02 |

GT-08 là giả định đơn giản hóa lớn nhất. Mục 6 bỏ giả định này để quan sát lắc tải (không có trong Excel v2.0, chỉ dùng cho mô phỏng).

---

## 3. Hệ phương trình — đúng theo Excel v2.0

**(1) Lực cản di chuyển** (GT-01, GT-02, GT-03):

$$F_c = M\, g\, w_0\, \mathrm{sign}(v)$$

| | Khối lượng | $F_c$ | Mã Excel |
| :--- | :---: | :---: | :---: |
| Đầy tải | $M_\Sigma$ = 14,244 kg | 2,096 N | `[Phu_tai.Fc]` |
| Không tải | $m_0$ = 2,022 kg | 298 N | `[Phu_tai.Fc0]` |

**(2) Quy đổi tốc độ** (GT-04, GT-05, GT-06):

$$k = \frac{D_{bx}}{2i} = \frac{0.25}{2 \cdot 155.34} = 8.047\times10^{-4}\ \text{m/rad}, \qquad v = k\,\omega_m$$

Khi $v$ = 0.12 m/s: $\omega_m$ = 149.1 rad/s (1,424 vg/ph). Mã Excel: `[Phu_tai.k]`, `[Phu_tai.wm]`.

**(3) Mô-men cản quy về trục động cơ** (GT-06, khi động cơ kéo):

$$M_c = \frac{F_c\, k}{\eta}$$

Đầy tải 1.874 N·m, không tải 0.266 N·m. Mã Excel: `[Phu_tai.Mc]`, `[Phu_tai.Mc0]`.

**(4) Mô-men động khi xe có gia tốc $a$** (GT-07):

$$M_{đg}(a) = \frac{\delta\, M\, a\, k}{\eta} + J_B\,\frac{a}{k}$$

Tại $a = a^*$ = 0.10 m/s²: đầy tải 1.790 N·m, không tải 0.534 N·m. Mã Excel: `[Phu_tai.Mdg]`, `[Phu_tai.Mdg0]`.

**(5) Mô-men động cơ phải sinh ra** (công thức dùng để vẽ đồ thị phụ tải ở `Phu_tai` cột L, M):

$$T_{đ}(t) = M_c + M_{đg}(a(t)) = M_c + M_{đg}(a^*)\,\frac{a(t)}{a^*}$$

- Tăng tốc đầy tải, $a = a^*$: $T_{đ,\max}$ = 1.874 + 1.790 = **3.664 N·m** `[Phu_tai.Mkd]`
- Chạy đều, $a = 0$: $T_{đ} = M_c$ = 1.874 N·m
- Giảm tốc, $a = -a^*$: $T_{đ}$ = 1.874 − 1.790 = 0.084 N·m `[Phu_tai.Mh]` (vẫn dương: lực cản đủ hãm xe)

**(6) Viết (5) dưới dạng phương trình động học** để vẽ sơ đồ khối. Vì $a = k\,\dfrac{d\omega_m}{dt}$, thay vào (4):

$$M_{đg} = \underbrace{\left(J_B + \frac{\delta\, M\, k^2}{\eta}\right)}_{J_\Sigma}\frac{d\omega_m}{dt} \quad\Longrightarrow\quad J_\Sigma\,\frac{d\omega_m}{dt} = T_{đ} - M_c$$

| | $J_B$ | $\delta M k^2/\eta$ | $J_\Sigma$ |
| :--- | :---: | :---: | :---: |
| Đầy tải | 0.00262 | 0.01179 | **0.01441 kg·m²** |
| Không tải | 0.00262 | 0.00167 | **0.00429 kg·m²** |

> **Ghi chú đối chiếu Excel:** dòng `[Phu_tai.Jl]` hiện ghi $J_{tải} = \delta M k^2$ = 0.0106 kg·m² (không chia $\eta$). Dòng này chỉ để tham khảo, không được công thức nào dùng; công thức $M_{đg}$ ở `[Phu_tai.Mdg]` có chia $\eta$. Để thống nhất, nên sửa `[Phu_tai.Jl]` thành $\delta M k^2/\eta$ và thêm dòng $J_\Sigma = J_B + J_{tải}$. Kết quả chọn thiết bị không đổi.

**(7) Điều kiện không trượt** (GT-05; không nằm trong vòng kín, chỉ là ràng buộc):

$$F_c + \delta M a \le \frac{\varphi\, k_{dẫn}\, M g}{k_{bám}}, \qquad k_{bám} = 3.74 \text{ tại } a^* \ (\text{KT-04})$$

**(8) Khi hãm tái sinh** (GT-06): nếu $T_{đ} < 0$ thì năng lượng đi ngược từ tải về động cơ, phần cản dùng $F_c\,k\,\eta$ thay cho $F_c\,k/\eta$. Với $a^*$ = 0.10 m/s² chỉ xảy ra khi giảm tốc không tải ($M_{h,0}$ = −0.27 N·m `[Phu_tai.Mh0]`); khi mô phỏng có thể dùng một giá trị $\eta$ cho cả hai chiều mà sai số không đáng kể.

---

## 4. Sơ đồ khối — Hình 1 (mô hình khối cứng, GT-08)

![Sơ đồ khối mô hình khối cứng](02_So_do_khoi_khoi_cung.png)

*(Bản vector: `02_So_do_khoi_khoi_cung.svg`)*

| Khối trên hình | Phương trình | Mã Excel |
| :--- | :--- | :--- |
| Quỹ đạo S-curve | $v^*(t)$ 7 đoạn, $a^*$, $\rho^*$ | `[Phu_tai.Tj]`, `[Phu_tai.Ta]`, `[Phu_tai.tacc]` |
| Biến tần + ĐC (FOC) | $T_{đ} = k_M\, i_{sq}$ (mục 5) | `Tham_so_DC` |
| Σ mô-men, $1/J_\Sigma$, $\int$ | (6): $J_\Sigma\, d\omega_m/dt = T_{đ} - T_c$ | $J_\Sigma$ từ (6) |
| $k$ | (2): $v = k\,\omega_m$ | `[Phu_tai.k]` |
| Lực cản | (1): $F_c = M g w_0\,\mathrm{sign}(v)$; lực dốc = 0 (GT-01); lực gió ≈ 0 (GT-03) | `[Phu_tai.Fc]` |
| $k/\eta$ | (3): $T_c = F_\Sigma k/\eta$ | `[Phu_tai.Mc]` |
| Encoder ES7C | phản hồi $\omega_m$ cho vòng tốc độ | `Catalogue` |

**Kiểm tra mô hình khớp Excel:** chạy theo S-curve với $a^*$ = 0.10 m/s², đầy tải, mô hình cho $T_{đ}$ = 3.664 N·m khi tăng tốc, 1.874 N·m khi chạy đều, 0.084 N·m khi giảm tốc — trùng `[Phu_tai.Mkd]`, `[Phu_tai.Mc]`, `[Phu_tai.Mh]` và đồ thị phụ tải.

Khi mô phỏng nên dùng $\mathrm{sign}(v)$ có vùng chết nhỏ (ví dụ $|v| < 10^{-4}$ m/s thì $F_c$ = 0) để tránh dao động số quanh $v = 0$; khi xe đứng yên phanh BE1 giữ trục (GT-10).

---

## 5. Mô hình động cơ trong FOC (khối "Biến tần + ĐC", GT-09)

$$T_{đ} = \frac{3}{2}\, p\, \frac{L_m}{L_r}\, \psi_r\, i_{sq} = k_M\, i_{sq}, \qquad T_r \frac{d\psi_r}{dt} + \psi_r = L_m\, i_{sd}$$

Tham số: bộ hiệu chỉnh của DRN71M4 ở `Tham_so_DC` mục C: $R_s$ = 17.25 Ω, $R_r'$ = 17.31 Ω, $L_{\sigma s} = L_{\sigma r}$ = 0.0731 H, $L_m$ = 0.905 H.

| Đại lượng | Công thức | Giá trị |
| :--- | :--- | :---: |
| Điện cảm rotor | $L_r = L_m + L_{\sigma r}$ | 0.978 H |
| Hằng số thời gian rotor | $T_r = L_r/R_r'$ | 0.0565 s |
| Hệ số tản | $\sigma = 1 - L_m^2/(L_s L_r)$ | 0.144 |
| Dòng từ hóa định mức (biên độ dq) | từ mạch thay thế hình T tại điểm định mức | $i_{sd,N}$ = 1.00 A |
| Từ thông rotor định mức | $\psi_r = L_m\, i_{sd,N}$ | 0.907 Wb |
| Hệ số mô-men | $k_M = \tfrac32 p\,(L_m/L_r)\,\psi_r$ | 2.52 N·m/A |
| Dòng $i_{sq}$ ứng $M_N$ = 2.5 N·m | $i_{sq} = M_N/k_M$ | 0.99 A |

Kiểm tra: tại điểm định mức mô hình cho 2.54 N·m, catalogue 2.50 N·m (lệch 1.6%).

---

## 6. Mở rộng: bỏ giả định GT-08, xét con lắc tải treo — Hình 2

**Giả định thêm** (không có trong Excel v2.0; tương ứng khối O của Excel v1.5):

| Mã | Giả định |
| :---: | :--- |
| GT-11 | Tải + móc là chất điểm treo trên cáp không giãn, dài $h$ = 12 m |
| GT-12 | Góc lắc nhỏ: $\sin\theta \approx \theta$, lực căng cáp $\approx m_p g$ |
| GT-13 | Không có cản dao động (bảo thủ), không có gió |

**(9) Con lắc** ($\theta > 0$ khi tải ở phía trước xe theo chiều chạy):

$$\ddot\theta = -\omega_p^2\,\theta - \frac{a}{h}, \qquad \omega_p = \sqrt{g/h} = 0.904\ \text{rad/s}\ \ (T_p = 6.95\ \text{s})$$

**(10) Lực ngang của cáp lên xe:** $F_\theta = m_p\, g\, \theta$, với $m_p = Q + m_{nh}$ = 12,444 kg (đầy tải), 222 kg (không tải).

**(11) Phần xe:**

$$F_\Sigma = F_c - F_\theta, \quad F_c = (m_{xc} + m_p)\,g\,w_0\,\mathrm{sign}(v), \quad J_{xc} = J_B + \frac{[(\delta-1)M_\Sigma + m_{xc}]\,k^2}{\eta} = 0.00545\ \text{kg·m}^2$$

Trọng lượng tải vẫn đè lên bánh nên lực cản lăn giữ nguyên như (1); nhưng quán tính phía động cơ chỉ còn xe, cụm nâng và phần quay của hộp số. Tải chỉ tác dụng lên xe qua $F_\theta$. Khi tăng tốc tải bị trễ lại ($\theta < 0$), $F_\theta < 0$ nên $F_\Sigma$ tăng: cáp kéo ngược xe lại.

![Sơ đồ khối mở rộng con lắc](03_So_do_khoi_con_lac.png)

*(Bản vector: `03_So_do_khoi_con_lac.svg`)*

**Dùng mô hình nào cho việc gì:**
- **Hình 1 (GT-08):** chọn động cơ, kiểm tra quá tải và phát nhiệt; khớp toàn bộ Excel v2.0.
- **Hình 2 (GT-11..13):** quan sát góc lắc $\theta(t)$ và lực cáp. Mô-men đỉnh theo Hình 2 nhỏ hơn Hình 1 (≈ 2.55 so với 3.66 N·m), vì trong 1.45 s tăng tốc tải chưa kịp lệch nhiều. Đây không phải lỗi; Hình 1 là trường hợp bảo thủ dùng để chọn thiết bị.

---

## 7. Đối chiếu với ví dụ xe máy điện trên lớp

Chỉ cấu trúc chung (mục 1) được dùng lại. Các thành phần cụ thể khác nhau như sau:

| Thành phần | Xe máy điện (trên lớp) | Xe con cầu trục | Giả định |
| :--- | :--- | :--- | :---: |
| Nguồn cấp | Lưới 220 V / 50 Hz | Lưới 380 V / 50 Hz qua biến tần FOC | GT-09 |
| Nối động cơ – bánh | Gắn trực tiếp, $v = r\,\omega$ | Qua hộp số: $v = k\,\omega_m$, $k = D/(2i)$ | GT-06 |
| Bán kính lăn | $r_{eff}$ của lốp (biến dạng) | $D_{bx}/2$ (bánh thép cứng) | GT-04 |
| Quy đổi lực → mô-men | $T = F\,r$ | $T = F\,k/\eta$ (kéo), $F\,k\,\eta$ (hãm) | GT-06 |
| Lực cản lăn | $R_r$ (lốp) | $F_c = M g w_0$ (lăn + ổ + gờ bánh) | GT-02 |
| Lực dốc $F_t$ | Có | 0 | GT-01 |
| Lực khí động $F_a \propto v^2$ | Có, đáng kể | ≈ 0 | GT-03 |
| Loại tải | Ma sát + quạt gió + thế năng | Ma sát khô (mô-men không đổi) | Mục 1 |
| Khối lượng quán tính | $m$ | $\delta M$ + $J_B$ của động cơ | GT-07 |
| Thành phần riêng | — | Con lắc tải treo (Hình 2) | GT-11..13 |

---

## 8. Bảng thông số cho mô phỏng

| Ký hiệu | Ý nghĩa | Đầy tải | Không tải | Nguồn |
| :---: | :--- | :---: | :---: | :--- |
| $M$ | Khối lượng tịnh tiến | 14,244 kg | 2,022 kg | SSoT P-04, P-05 |
| $k$ | Hệ số quy đổi $D/(2i)$ | 8.047×10⁻⁴ m/rad | ← | `[Phu_tai.k]` |
| $\eta$ | Hiệu suất cơ khí | 0.90 | ← | SSoT P-15 |
| $J_\Sigma$ | Quán tính quy đổi (Hình 1) | 0.01441 kg·m² | 0.00429 kg·m² | (6) |
| $J_{xc}$ | Quán tính phía xe (Hình 2) | 0.00545 kg·m² | ← | (11) |
| $m_p$ | Khối lượng con lắc (Hình 2) | 12,444 kg | 222 kg | (10) |
| $M_c$ | Mô-men cản khi chạy đều | 1.874 N·m | 0.266 N·m | `[Phu_tai.Mc]` |
| $T_{đ,\max}$ | Mô-men đỉnh khi tăng tốc | 3.664 N·m | 0.800 N·m | `[Phu_tai.Mkd]` |
| $h$, $\omega_p$ | Chiều dài cáp, tần số con lắc | 12 m; 0.904 rad/s | ← | SSoT P-06, P-07 |
| $k_M$ | Hệ số mô-men FOC | 2.52 N·m/A | ← | Mục 5 |

---

## 9. Việc tiếp theo

1. Sửa dòng `[Phu_tai.Jl]` trong Excel theo ghi chú ở (6) và thêm dòng $J_\Sigma$.
2. Viết `init_params.m` lấy số từ bảng mục 8 (không gõ tay hằng số trong mô hình).
3. Dựng Simulink theo Hình 1, chạy một hành trình đầy tải, so $T_{đ}(t)$ với đồ thị phụ tải của Excel.
4. Thay phần cơ khí bằng Hình 2 để quan sát góc lắc.

> Lượng đặt $a^*$ = 0.10 m/s², $\rho^*$ = 0.40 m/s³ đang được cân nhắc đổi sang 0.06 / 0.24 cho khớp TCVN 4244:2005 Bảng 2.1.2.3.1.1. Nếu đổi, chỉ khối S-curve và các số mô-men đỉnh thay đổi; cấu trúc mô hình giữ nguyên.
