# THUYẾT MINH TÍNH CHỌN PHẦN LỰC — ĐỘNG CƠ, HỘP SỐ, BIẾN TẦN, ĐIỆN TRỞ HÃM, PHANH ($x = 2$)

**Mã tài liệu:** `CALC-PWR-8.5EMG-TROLLEY-v1.0` — Gói `SOW-3.1` (Khối 3) — Phụ trách: Đặng Nguyên Bình (PE-HW)  
**Ngày:** 24/10/2026 — **Trạng thái:** **ĐÃ DUYỆT — Cổng G4 (`CDR-EVT`) đóng ngày 24/10/2026** — thiết bị chốt: DRN80M4 + ACS380-04xS-03A3-4 (QĐ-04)  
**File tính toán đi kèm (nguồn số duy nhất):** `00_Tinh_toan_Xe_con_x2_v1.2.xlsx` (sheet `Params`, `GiaDinh_K3`, `Catalogue`, `Tính chọn`, `Kiểm tra`, `Dẫn xuất`)  
**Kế thừa:** SSoT v1.2, SRS Baseline A v1.2 (đề xuất A.1 cho `SRS-PERM-04`), SAD/ICD/BOM/DFMEA Khối 2 v1.0  
**Tiền điều kiện cổng:** Khối 2 (G3) đã được duyệt ngày 24/10/2026, trước khi đóng G4.

> Mọi số dưới đây là **kết quả công thức Excel** (đã tính lại bằng Microsoft Excel, 0 lỗi công thức) với ứng viên đang chọn `sel = 1` (**DRN80M4 + ACS380-04xS-03A3-4**). Cột "Ứng viên 2" là kết quả của cùng file khi đặt `sel = 2` rồi tính lại (giá trị lưu trong file là của `sel = 1`). Bảng WCCA nằm ở sheet `WCCA`. Ký hiệu nguồn `[W-xx]`: xem `Block 2/01_SAD_...` §8.1.
>
> **Cập nhật v1.2 (25/10/2026) — đóng các mục TBD catalogue:** hộp số **SEW R87, tỷ số truyền tổng $i_{\text{thực}} = 155.34$**, mô-men ra cho phép 1,550 N·m, tải hướng kính 17,100 N (`[W-06]` SEW Drive Selection); phanh **BE1 cấp 7 N·m** có trong danh mục cấp 10/7/5 N·m (`[W-07]`); điện trở hãm **Danotherm CBH 360 C T 406 210R** 200 W (`[W-05]` tr.24, `[W-09]`); bảo vệ đầu vào **cầu chì gG 6 A OFAF000H6** (`[W-08]`); contactor **ABB AF09-30-10-13** (`[W-10]`); bảng định mức ACS380 đã đối chiếu ảnh trang gốc (`[W-05]` tr.12). Mọi số trong tài liệu được tính lại với $i = 155.34$ (Excel `00_Tinh_toan_Xe_con_x2_v1.2.xlsx`); biên quá tải ở tổ hợp xấu nhất WC-5 đổi từ 1.03 thành **1.02** (vẫn ≥ 1). Nguồn lưu tại `Tài liệu tham khảo/Catalogue web/`.
>
> **Lịch sử:** v1.0 (24/10/2026) bản đầu · **v1.1 (24/10/2026)** xử lý báo cáo Checker (`Block 2/05_Bao_cao_Checker_G3_G4.md`): K6-2 quy $\lambda$ về $U_N = 400$ V của động cơ; K6-3 kể quán tính khi phanh; K6-4 WCCA bằng công thức; K7-1 thêm bước thử mô-men giữ khi phanh còn kẹp ⇒ $M_B$ = 7 N·m; K6-5 ghi chú quy ước mô-men giảm tốc.

---

## 1. PHỤ TẢI TĨNH, ĐỘNG LỰC HỌC VÀ BÁM RAY (`Tính chọn` khối A, B)

| Đại lượng | Công thức | Giá trị | Kiểm tra |
| :--- | :--- | :---: | :--- |
| Tốc độ bánh xe | $\omega_{bx} = 2v_{\max}/D_{bx}$ | 0.960 rad/s (9.167 vg/ph) | — |
| Lực cản tĩnh đầy / không tải | $F_c = M g w_0$ | 2,096.0 / 297.5 N | KT-01: khớp P-20 ✓ |
| Công suất tĩnh | $F_{c.\text{đầy}} v_{\max}/\eta$ | 279.5 W | — |
| Lực kéo cực đại (a = 0.5) | $F_c + M_\Sigma a_{\max}$ | 9,218 N | Downstream #6 |
| Công suất đỉnh | $F_{\max} v_{\max}/\eta$ | 1,229 W | — |
| Lực bám bánh dẫn đầy / không tải | $\varphi k_{dẫn} M g$ | 13,973 / 1,984 N | — |
| Hệ số bám đầy / không tải | $F_{\text{bám}}/F_{\max}$ | **1.516 / 1.516** | KT-02, 03: ≥ 1.20 ✓ |

---

## 2. TỶ SỐ TRUYỀN VÀ QUY ĐỔI VỀ TRỤC ĐỘNG CƠ (khối C)

- $i_{\text{yc}} = \omega_N/\omega_{bx}$: **157.08** (DRN80M4, 1440 vg/ph) / 158.72 (DRN90S4, 1455 vg/ph). So với `P-16 = 150 [C]`: nếu dùng $i = 150$ thì ở 50 Hz xe chạy nhanh hơn 4.7% (vẫn trong ±5% và biến tần bù bằng tần số), nhưng **mọi quy đổi trong bộ điều khiển phải dùng $i_{\text{thực}}$** (`SRS-D03`, DFMEA FM-08).
- **$i_{\text{thực}}$ = 155.34 — hộp số SEW R87** (`[W-06]`): ở 50 Hz, $v = 0.12 \times 157.08/155.34 = 0.1213$ m/s (+1.1%, trong ±5%; biến tần bù về đúng 0.12 m/s ở 49.4 Hz). Ô `i_in` = 155.34; `KT-31` **Đạt**.

| Đại lượng (DRN80M4) | Công thức | Giá trị |
| :--- | :--- | :---: |
| Hệ số quy đổi | $k_{qđ} = D_{bx}/(2i)$ | $8.047 \times 10^{-4}$ m/rad |
| Mô-men cản kéo đầy / không tải | $F_c k_{qđ}/\eta$ | 1.874 / 0.266 N·m |
| Mô-men cản khi hãm (đầy tải) | $F_c k_{qđ}\eta$ | 1.518 N·m |
| Quán tính tải quy đổi đầy / không tải ($\delta = 1.15$) | $\delta M k_{qđ}^2$ | 0.01061 / 0.00151 kg·m² |
| Quán tính tổng (kèm $J_{\text{BMot}} = 26.2\times10^{-4}$ [W-02]) | $J_\Sigma$ | **0.01323 / 0.00413 kg·m²** (tỷ số 3.21) |

---

## 3. QUỸ ĐẠO S-CURVE DÙNG CHO PHỤ TẢI (khối E — chi tiết ở SDD)

$a^* = 0.45\text{ m/s}^2$, $\rho^* = 1.8\text{ m/s}^3$ (`SRS-D06`, dự trữ 10% dưới P-10/P-11): $T_j = 0.250$ s, $T_a = 0.0167$ s, $t_{acc} = 0.5167$ s, $s_{acc} = 0.031$ m; điều kiện đủ 3 đoạn $a^{*2}/\rho^* = 0.1125 < 0.12$ ✓ (KT-20).

---

## 4. CHU TRÌNH S3-40% VÀ BIỂU ĐỒ PHỤ TẢI (khối F)

**Giả định chu trình `[C]`** (ghi tại `GiaDinh_K3`): mỗi chu kỳ 600 s gồm 1 hành trình đầy tải (Tiến) + 1 hành trình không tải (Lùi), tổng thời gian đóng điện $\Sigma t_{lv} = CD \cdot T_{ck} = 240$ s → mỗi hành trình 120 s, quãng đường suy ra $L_{ht} = 14.34$ m.

| Pha (mỗi hành trình) | Thời gian (s) | Mô-men ĐC đầy tải (N·m) | Mô-men ĐC không tải (N·m) | Góc phần tư |
| :--- | :---: | :---: | :---: | :---: |
| Tăng tốc S-curve (đỉnh tại $a^*$) | 0.517 | $M_c + M_{đg}$ = **9.93** | 2.67 | I (Tiến) / III (Lùi) |
| Chạy đều | 118.97 | $M_c$ = 1.87 | 0.26 | I / III |
| Giảm tốc S-curve (đỉnh) | 0.517 | $M_c - M_{đg}$ = **−6.18** | −2.14 | II / IV |
| Nghỉ (phanh kẹp) | 180 | 0 | 0 | — |

```
 v(t) [m/s]                                                                       
 +0.12 ┤  ╭───────────── đầy tải (Tiến) ─────────────╮                            
     0 ┼──╯                                           ╰──── nghỉ 180 s ──╮      ╭── nghỉ 180 s
 -0.12 ┤                                                                  ╰─ không tải (Lùi) ─╯
 M(t) [N·m]
 +9.93 ┤ ▌(0.52 s)
 +1.87 ┤ ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▄         (không tải: ±2.7 / ∓0.26 N·m)
     0 ┼──────────────────────────────────────────────▐───────────────────────────────────────
 −6.18 ┤                                               ▌(0.52 s, hãm tái sinh góc II)
        0                                           120                300   420           600 t[s]
```

*Ghi chú (Checker K6-5):* mô-men pha giảm tốc dùng $M_c = F_c k_{qđ}/\eta$ (quy ước "kéo") thay cho $M_{c,\text{hãm}} = F_c k_{qđ}\eta$; sai khác 0.35 N·m, hướng an toàn cho tính nhiệt (bình phương mô-men lớn hơn ở pha kéo chiếm ưu thế), nên giữ để công thức $\Sigma M^2 t$ đơn giản.

**Kết quả nhiệt** ($\Sigma M^2 t$ tính giải tích cho biên dạng gia tốc hình thang, hệ số $f_2 = (2T_j/3 + T_a)/t_{acc} = 0.355$):

| Đại lượng | Công thức | Ứng viên 1 DRN80M4 | Ứng viên 2 DRN90S4 |
| :--- | :--- | :---: | :---: |
| Mô-men đẳng trị | $M_{đt} = \sqrt{\Sigma M^2 t/\Sigma t_{lv}}$ | 1.378 N·m | 1.375 N·m |
| Công suất đẳng trị | $P_{đt} = M_{đt}\omega_N$ | 207.8 W | 209.5 W |
| Hệ số dự trữ nhiệt | $k_{dt} = P_{đm}/P_{đt}$ | **3.61** | 5.25 |
| (Tham khảo) tương đương S1 | $P_{đt}\sqrt{CD}$ | 131 W | 132 W |

→ `KT-07` ($k_{dt} \ge 1.20$, A.1) **Đạt**; `KT-08` ($k_{dt} \le 1.50$, v1.2) **Không đạt — XUNG ĐỘT đã trình và được Người dùng xử lý tại QĐ-02**. Ghi chú: $P_{đm}$ dùng giá trị S1 của catalogue (bảo thủ, vì công suất cho phép ở S3-40% của cùng động cơ lớn hơn).

---

## 5. CHỌN ĐỘNG CƠ — KIỂM TRA QUÁ TẢI MÔ-MEN (khối D, `KT-04..06`)

$M_{\max} = \dfrac{(F_c + \delta M_\Sigma a_{\max})k_{qđ}}{\eta} + J_{\text{BMot}}\dfrac{a_{\max}}{k_{qđ}}$ (tính ở $a_{\max} = 0.5$ để bao Downstream #6, dù quỹ đạo thật chỉ dùng $a^* = 0.45$).

| Tiêu chí | DRN80M4 (0.75 kW) | DRN90S4 (1.1 kW) | Ngưỡng / Nguồn |
| :--- | :---: | :---: | :--- |
| $P_N$ / $M_N$ / $n_N$ / $I_N$ | 0.75 kW / 4.95 N·m / 1440 / 1.75 A | 1.1 kW / 7.2 N·m / 1455 / 2.55 A | [W-01] tr.866 |
| $\cos\varphi_N$ / $\eta_N$ | 0.74 / 82.9% | 0.73 / 84.5% | [W-01] |
| $\lambda_K = M_K/M_N$ | **3.4** | 3.3 | ≥ 2.0 (Downstream #7) ✓ |
| $M_{\max}$ yêu cầu | 10.82 N·m | 12.73 N·m | — |
| $M_{\max}/M_N$ | 2.19 | 1.77 | — |
| $\lambda_K (U_{\min}/U_N)^2 = \lambda_K (342/400)^2$ | **2.485 ≥ 2.19 ✓** (biên 1.14) | 2.412 ≥ 1.77 ✓ (biên 1.36) | WORKFLOW §4.2-C2; Checker K6-2 |
| Lực kéo tối đa tạo được ở −10% áp | 11,940 N ≥ 9,218 ✓ | — | Downstream #6 |
| $k_{dt}$ | 3.61 | 5.25 | ≥ 1.20 (A.1) |
| Phanh tiêu chuẩn | BE1 (cấp 10/7/5 N·m `[W-07]`) | BE2 (cấp 20/14/10/7/5 N·m `[W-07]`) | §8 |
| $P_N \le \min(2.2;\ 1.5 P_{\max})$ = 1.84 kW (QCD-C01, cách hiểu QĐ-08: so với $P_{\max}$ = 1.23 kW) | ✓ (61%) | ✓ (89%) | KT-09 |

**QĐ-04 (Người dùng, 24/10/2026): CHỐT ứng viên 1 — SEW DRN80M4 0.75 kW + ABB ACS380-04xS-03A3-4; chấp nhận biên quá tải 1.03 ở tổ hợp xấu nhất WC-5** (lưới −10%, $w_0$ = 0.018, $m_{xc}$ +20%, $\eta$ = 0.85).

**Đề xuất ban đầu của Writer:** **Ứng viên 1 — SEW DRN80M4** (nhỏ nhất vẫn đạt $\lambda$ ở tổ hợp xấu nhất WCCA, §9; phanh BE1 có khả năng chọn cấp mô-men thấp nằm trong cửa sổ cho phép). Ứng viên 2 dự phòng khi `P-03 [C]` tăng mạnh hoặc khi cấp mô-men BE1 không phù hợp.

> **Lưu ý điện áp (Checker K6-2, K11-7):** động cơ SEW trong [W-01] định mức **400 V/50 Hz**, còn lưới là 380 V ±10% (`P-19`). Vì vậy $\lambda$ khả dụng được quy về $U_N = 400$ V (342 V ⇒ hệ số 0.731 thay cho 0.81). Biến tần cấp từ 380 V không xuất được 400 V ở 50 Hz: gần $v_{\max}$ động cơ làm việc với từ thông giảm tối đa còn ≈ 85.5% (khi lưới −10%). Điều này chấp nhận được vì đỉnh gia tốc của S-curve xảy ra ở khoảng giữa dải tốc độ (đủ điện áp), còn khi chạy đều chỉ cần 1.87 N·m (38% $M_N$). Phương án triệt để: đặt động cơ có cuộn dây 380 V/50 Hz (chưa xác minh SEW có cung cấp) — **Người dùng chọn tại G4**; DVP-SS-06 kiểm chứng trường hợp này bằng mô phỏng.

> **Lưu ý `K11`:** `SOW-3.1` ghi "chọn dải 1.5 ÷ 2.2 kW" — cả hai ứng viên đều nhỏ hơn dải này. Đây là hệ quả trực tiếp của tính toán độc lập (đúng tinh thần `RRM-04`: *"không sao chép công suất Case Study"*); ghi nhận độ lệch SOW trong `04_SRS_A1_...` §1.

---

## 6. HỘP GIẢM TỐC (GEARED MOTOR, QĐ-01)

| Yêu cầu | Giá trị | Trạng thái |
| :--- | :--- | :---: |
| Kiểu | Hộp giảm tốc bánh răng trụ đồng trục **SEW R87** (lắp chân đế, trục đặc 50×100 mm), liền khối với DRN80M4 — tổ hợp R87 + khung DRN80 cần SEW xác nhận khi đặt hàng | XM (hộp số) / CXM (tổ hợp) |
| Tỷ số truyền | **$i_{\text{thực}} = 155.34$** (R87, `[W-06]`); yêu cầu $i_{\text{yc}} = 157.1$, dải chấp nhận [149.6; 165.3] ✓ | **XM** `[W-06]` |
| Mô-men ra | Đỉnh khi tăng tốc $(F_c + \delta M_\Sigma a_{\max}) D_{bx}/2$ = 1,286 N·m ≤ $M_{a,\max}$ = **1,550 N·m** (KT-33 ✓; SEW tính 1,280 N·m, mức sử dụng 83%); tải hướng kính cho phép 17,100 N | **XM** `[W-06]` |
| Hiệu suất | Dùng $\eta = 0.90$ (`P-15 [C]`) cho toàn chuỗi; giá trị riêng hộp số SEW chưa xác minh | CXM |

---

## 7. CHỌN BIẾN TẦN (khối G, `KT-10..12`)

Dòng đỉnh khi tăng tốc đầy tải ước lượng: $I_0 = I_N(\sin\varphi_N - \cos\varphi_N/b)$ với $b = \lambda_K + \sqrt{\lambda_K^2 - 1}$ (sơ đồ vòng tròn, bỏ qua $R_s$) → $I_0 = 0.982$ A; $I_{q,N} = 1.448$ A; $I_{\text{đỉnh}} = \sqrt{I_0^2 + (I_{q,N} M_{\max}/M_N)^2} = 3.32$ A.

| Tiêu chí | ACS380-04xS-03A3-4 (cho DRN80M4) | ACS380-04xS-04A0-4 (cho DRN90S4) | Nguồn |
| :--- | :---: | :---: | :--- |
| $I_N$ / $P_N$ | 3.3 A / 1.1 kW | 4.0 A / 1.5 kW | [W-05] tr.12 |
| $I_{Hd}$ / $P_{Hd}$ | 2.6 A / 0.75 kW | 3.3 A / 1.1 kW | [W-05] tr.12 |
| $I_{Hd} \ge I_{N,\text{ĐC}}$ | 2.6 ≥ 1.75 ✓ | 3.3 ≥ 2.55 ✓ | KT-10 |
| $1.5 I_{Hd}$ (1 phút/10 phút) ≥ $I_{\text{đỉnh}}$ | 3.9 ≥ 3.32 ✓ | 4.95 ≥ 3.98 ✓ | KT-11 |
| $I_{\max}$ (2 s khi khởi động) ≥ $I_{\text{đỉnh}}$ | 4.7 ≥ 3.32 ✓ | 5.9 ≥ 3.98 ✓ | KT-12 |
| Chopper tích hợp / module encoder | Có / BTAC-02 (HTL/TTL) | Có / BTAC-02 | [W-05] tr.10, 24 |
| Thời gian tăng mô-men (bước định mức) | < 10 ms | < 10 ms | [W-05] tr.10 → Downstream #4 (I) |

> ⚠ Bảng định mức ACS380 được trích từ PDF bằng công cụ chuyển văn bản bị lệch cột; giá trị đã được đối chiếu chéo (vd. $P_{BR,\text{cont}} = P_{Hd}$ cho cùng mã) nhưng **cần kiểm lại trên bản PDF gốc** trước khi chốt BOM chính thức.

---

## 8. HÃM TÁI SINH — CHOPPER VÀ ĐIỆN TRỞ $R_h$ (khối H, `KT-13..17`); PHANH CƠ (khối I, `KT-27..30`)

### 8.1. Điện trở hãm

| Đại lượng | Công thức | Giá trị |
| :--- | :--- | :---: |
| Lực hãm cực đại | $F_{h} = M_\Sigma a_{\max} - F_c$ | 5,026 N |
| Công suất hãm đỉnh về DC-link | $F_h v \eta \eta_{đc} \eta_{inv}$ | **436.5 W** |
| Cận trên theo công suất | $U_{chop}^2/P_{dc}$ = 700²/436.5 | 1,123 Ω |
| Dải cho phép của chopper ACS380-03A3-4 | $[R_{\min}; R_{\max}]$ | [99; 428] Ω |
| **$R_h$ chọn** (`SRS-D05a`) | — | **210 Ω** (KT-13, 14 ✓) |
| Dòng chopper / công suất tức thời khi dẫn tại 700 V | $U/R_h$, $U^2/R_h$ | 3.33 A / 2,333 W ≥ 436.5 W ✓ |
| Năng lượng vào $R_h$ mỗi lần dừng đầy tải | $(E_đ - F_c s_{acc})\eta\eta_{đc}\eta_{inv}$ | 59.9 J |
| Công suất trung bình chu kỳ (bảo thủ) | $E_{Rh} n_{ht}/T_{ck}$ | 0.20 W |
| $P_{BR,\max}$ biến tần ≥ $P_{dc}$ | 1.13 kW ≥ 0.437 kW | KT-15 ✓ |
| $U_{dc}$ không tải khi lưới +10% | $\sqrt{2}\cdot 418$ | 591 V < 680 V (chopper không băm khi đứng yên) — KT-16 ✓ |

**Giải thích ngắn:** công suất hãm rất nhỏ so với khả năng chopper vì vận tốc thấp; điều kiện ràng buộc thực chất là **$R_h \ge R_{\min}$ của IGBT hãm** (bảo vệ dòng). Công suất định mức của điện trở 210 Ω (ví dụ loại Danotherm trong [W-05] tr.25) **chưa xác minh** — đề xuất chọn loại ≥ 100 W có tiếp điểm nhiệt (dư rất lớn so với 0.2 W trung bình, chủ yếu để chịu xung 2.3 kW trong ≈ 0.5 s).

> ⚠ Ngưỡng chopper ON 700 ± 20 V, $U_{dc} \le 780$ V, trip 800 ± 10 V (Downstream #3) là **tham số thiết kế cho mô hình Simulink**; ngưỡng thật trong firmware ACS380 **chưa xác minh** (cần ACS380 Firmware manual). Nếu khác, ghi `XUNG ĐỘT K11` và cập nhật `SRS-D05c`.

### 8.2. Phanh cơ điện từ thường đóng

**QĐ-07 (Người dùng, 24/10/2026) — Phạm vi vận hành lý tưởng:** đồ án môn học chỉ cần bảo đảm hệ vận hành đúng trong điều kiện lý tưởng: **không mất điện, không dừng khẩn / E-STOP, không xét sự cố thiết bị** (mất encoder, phanh không nhả…). Các nội dung liên quan được ghi `Không áp dụng vì điều kiện vận hành lý tưởng (QĐ-07)`; QĐ-06 (chấp nhận rủi ro trượt khi mất điện) vì thế không còn cần thiết. Dao động lưới ±10% (`P-19`) vẫn giữ vì là điều kiện làm việc bình thường, không phải sự cố.

| Đại lượng | Công thức | Giá trị |
| :--- | :--- | :---: |
| Mô-men phanh tối thiểu | $\max(k_p M_{c,\text{đầy}};\ 1.2\,M_{hold})$, $k_p = 1.25$, $M_{hold} = M_N$ | max(2.32; **5.94**) = 5.94 N·m |
| Mô-men phanh tối đa không trượt — đầy tải | $F_{\text{bám}} k_{qđ}\eta$ | 10.12 N·m |
| Mô-men phanh tối đa không trượt — không tải | $F_{\text{bám},0} k_{qđ}\eta$ | 1.44 N·m (chỉ liên quan dừng khẩn khi đang chạy — Không áp dụng, QĐ-07) |
| **$M_B$ chọn** (`SRS-D13`, ô quyết định) | — | **7 N·m** (cấp BE1 — *chưa xác minh catalogue*) |
| Gia tốc dừng bằng phanh — đầy tải / không tải | $\dfrac{M_B/(k_{qđ}\eta) + F_c}{\delta M + J_B/(k_{qđ}^2\eta)}$ (kể quán tính quay — Checker K6-3) | 0.563 / 1.128 m/s² (không tải: trượt, giới hạn bởi bám) |
| Quãng dừng nếu phanh kẹp khi đang chạy 0.12 m/s, đầy tải (tham khảo — Không áp dụng, QĐ-07) | $v^2/(2a_B) + v t_{kẹp}$ | 18.8 mm |
| Độ trôi danh nghĩa sau lệnh đóng phanh | $\lvert v\rvert_{\text{đóng}} t_{kẹp}$ | 0.25 mm ≤ 10 mm ✓ (KT-30) |

→ `KT-29` **Không áp dụng (QĐ-07)**: kiểm tra trượt bánh khi phanh cơ kẹp lúc xe đang chạy không tải chỉ xảy ra khi dừng khẩn/mất điện — ngoài phạm vi điều kiện vận hành lý tưởng. Trong vận hành bình thường xe dừng bằng điện theo S-curve và phanh chỉ kẹp khi $\lvert v \rvert \le 0.005$ m/s nên không có trượt bánh.

---

## 9. PHÂN TÍCH TRƯỜNG HỢP XẤU NHẤT RÚT GỌN (WCCA — DRN80M4)

Nguồn: sheet `WCCA` (công thức). $\lambda$ khả dụng $= \lambda_K\,[U_{\text{lưới}}(1+\Delta U)/U_N]^2$ với $U_N = 400$ V; $k_{dt}$ ước lượng $\approx k_{dt,0}\,F_{c,0}/F_c \cdot \min(1;\ U/U_N)$ (gần đúng).

| Kịch bản | $M_{\max}/M_N$ | $\lambda$ khả dụng | Biên | $k_{\text{bám}}$ tại $a$ = 0.5 / $a^*$ = 0.45 | $P_{dc,\text{hãm}}$ (W) | $U_{dc0}$ (V) | $k_{dt}$ ước lượng |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| WC-0: Danh định (380 V) | 2.187 | 3.069 | 1.40 | 1.516 / 1.643 | 436.5 | 537 | 3.43 |
| WC-1: lưới −10% | 2.187 | 2.485 | 1.14 | 1.516 / 1.643 | 436.5 | 484 | 3.09 |
| WC-2: $w_0 = 0.018$ (cận trên SOW) | 2.263 | 3.069 | 1.36 | 1.450 / 1.566 | 400.1 | 537 | 2.86 |
| WC-3: $m_{xc}$ +20% (2,160 kg) | 2.234 | 3.069 | 1.37 | 1.516 / 1.643 | 447.5 | 537 | 3.34 |
| WC-4: $\eta = 0.85$ | 2.296 | 3.069 | 1.34 | 1.516 / 1.643 | 412.2 | 537 | 3.43 |
| **WC-5: tổ hợp kéo** (WC-1+2+3+4) | **2.428** | **2.485** | **1.02 ✓ (sát)** | 1.450 / 1.566 | 387.4 | 484 | 2.51 |
| WC-6: $\varphi = 0.15$ (ray ẩm, độ nhạy) | 2.187 | 3.069 | 1.40 | **1.137** / 1.232 ✓ | 436.5 | 537 | 3.43 |
| WC-7: tổ hợp hãm ($w_0$ = 0.012, $\eta$ = 0.95, lưới +10%) | 2.017 | 3.713 | 1.84 | 1.588 / 1.728 | **499.2** (≪ $P_{BR,\max}$ 1,130) | **591** (< 680) | 4.51 |

**Kết luận WCCA:** sheet `WCCA` trả "Đạt" cho cả 8 kịch bản. Hai điểm nhạy: (1) **biên quá tải ở WC-5 chỉ còn 1.02** (1.03 với $i$ = 157.08 lúc chốt QĐ-04) do động cơ định mức 400 V trên lưới 380 V −10% — nếu Người dùng muốn biên ≥ 1.2 thì chọn DRN90S4 (biên ≈ 1.25 ở WC-5) hoặc cuộn dây 380 V; (2) hệ số bám $\varphi$ (`P-14 [C]`) — dùng $a^* = 0.45$ thay vì 0.5 cho dự trữ đủ tới $\varphi \approx 0.15$.

---

## 10. GIẢI THÍCH NGẮN: VÌ SAO TÍNH NHƯ VẬY (để bảo vệ từng con số)

1. **Vì sao động cơ chỉ 0.75 kW trong khi $P_{\max} = 1.23$ kW?** $P_{\max}$ là công suất *tức thời* tại đỉnh gia tốc, kéo dài < 0.3 s; động cơ KĐB chịu được nhờ $\lambda_K = 3.4$ (mô-men tới hạn gấp 3.4 lần định mức). Điều kiện ràng buộc là mô-men đỉnh, không phải công suất trung bình.
2. **Vì sao $k_{dt}$ lớn (3.61)?** Nhiệt chỉ phụ thuộc mô-men hiệu dụng; 99% thời gian chạy đều chỉ cần 1.87 N·m (38% $M_N$). Ép $k_{dt} \le 1.5$ buộc dùng động cơ 0.25 kW không đủ mô-men khởi động — đó là xung đột đã xử lý ở QĐ-02.
3. **Vì sao $R_h = 210\ \Omega$ mà không phải giá trị nhỏ?** Giá trị nhỏ làm tăng dòng IGBT hãm; giá trị lớn quá thì không hấp thụ đủ công suất. Cửa sổ thực tế là [99; 428] Ω, chọn ở giữa.
4. **Vì sao kiểm tra λ ở $(342/400)^2$?** Mô-men tới hạn tỷ lệ bình phương điện áp; động cơ định mức 400 V nên khi lưới sụt còn 342 V, mô-men tới hạn còn 73.1%.
5. **Vì sao phanh 7 N·m?** Phải ≥ 5.94 N·m để chịu được mô-men thử $1.2 M_{hold}$ khi phanh còn kẹp (bước TORQUE_PROVE, SDD §5) và ≥ 2.32 N·m để giữ xe; phải ≤ 10 N·m để không trượt bánh khi phanh khẩn đầy tải. Cấp cụ thể phụ thuộc catalogue BE1 (TBD).
