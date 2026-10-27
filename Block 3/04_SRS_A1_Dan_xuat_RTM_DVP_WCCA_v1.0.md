# SRS BASELINE A.1 (ĐÃ KÝ 24/10/2026) — YÊU CẦU DẪN XUẤT `SRS-Dxx`, RTM/DVP CẤP PHÂN HỆ, V-MODEL & WCCA RÚT GỌN

**Mã tài liệu:** `SRS-A1-8.5EMG-TROLLEY-v1.0` — Gói `SOW-3.5` (Phạm Văn Hưng & Nghiêm Trọng Đông) — Khối 3  
**Ngày:** 24/10/2026 — **Trạng thái:** **ĐÃ DUYỆT — Cổng G4 (`CDR-EVT`) đóng ngày 24/10/2026**. **SRS Baseline A.1 CÓ HIỆU LỰC từ 24/10/2026** (Người dùng ký CR-01..CR-07), thay thế Baseline A v1.2 đối với các ID nêu ở §1; các ID khác giữ nguyên nội dung v1.2. ~~Tệp Block 1 v1.2 vẫn giữ nguyên làm hồ sơ lịch sử.~~ **Cập nhật 26/10/2026 (Người dùng duyệt nhóm A):** CR-01, CR-02, CR-03 đã được tích hợp vào Block 0/1 — PRD v3.2, SOW v1.3, BCA-QFD v1.2, slide MCR v2.1, SRS Baseline A v1.3, SRS chi tiết v1.3, RTM/DVP v1.3 (tên tệp giữ hậu tố cũ); bản trước khi sửa lưu trong lịch sử phiên bản của từng tệp.  
**Nguồn số:** `00_Tinh_toan_Xe_con_x2_v1.4.xlsx` sheet `Dẫn xuất`, `Kiểm tra`, `WCCA`  
**Lịch sử:** v1.3 (27/10/2026) theo Checker lượt 1 (K8-1, K7-1, K10-3, K11-1): nguồn số chuyển sang Excel v1.4; thêm mã con `SRS-D05d` ($P_{Rh}$); đăng ký `SRS-D14`, `SRS-D15` (nhóm C, Người dùng duyệt 26/10/2026); RTM, V-model và DFMEA cập nhật theo KT-33..43; ghi rõ ngưỡng PASS của DV-04 không phải $P_{dc}$ = 436.5 W; các giá trị khác không đổi · v1.2 (25/10/2026) nhập $i_{\text{thực}}$ = 155.34 (SEW R87), xác minh BE1 7 N·m, R_h, QF1/KM1; số liệu tính lại · v1.0 (24/10/2026) bản đầu · v1.1 (24/10/2026) xử lý Checker: K11-1 mở rộng CR-01/CR-03, K8-1/K8-2 (cha của D02, quy ước mã con), K7-1 (D10, D13 theo bước thử mô-men), K7-2 (tiêu chí DVP-SS), K6-2/K6-4 (WCCA theo $U_N$ = 400 V, có trong Excel)

---

## 1. NHẬT KÝ THAY ĐỔI BASELINE (Baseline A v1.2 → A.1)

| # | ID bị ảnh hưởng | Nội dung v1.2 | Đề xuất A.1 | Lý do | Ngày | Quyết định |
| :---: | :--- | :--- | :--- | :--- | :---: | :--- |
| CR-01 | **SRS-PERM-04**; kéo theo **QCD-Q02** ("$k_{dt} \in [1.20;\ 1.50]$", SOW v1.2) và mệnh đề $k_{dt}$ trong **SOW-3.1** (chỉ ghi nhận, không sửa Block 0) | $k_{dt} = P_{đm}/P_{đt} \in [1.20;\ 1.50]$ | **$k_{dt} \ge 1.20$** (bỏ cận trên) | Xung đột `K11`: với $v_{\max} = 0.12$ m/s, $M_\Sigma = 14,244$ kg, $a \approx 0.5$ m/s² động cơ phải định cỡ theo mô-men đỉnh ($\lambda$) → $k_{dt} \approx 3.6 \div 5.3$; ép $k_{dt} \le 1.5$ cần $\lambda \approx 6.5$ (không khả thi). Phù hợp đề xuất sẵn có tại `00_Bang_thong_so_goc_SSoT.md` Phần 2 dòng 12. | 24/10/2026 | **Người dùng chấp thuận (QĐ-02); đã ký A.1 ngày 24/10/2026** |
| CR-02 | **DV-08** (DVP v1.2) | FAIL khi $k_{dt} < 1.20$ **hoặc $k_{dt} > 1.50$** | FAIL chỉ khi $k_{dt} < 1.20$ hoặc $\lambda_K (U_{\min}/U_N)^2 < M_{\max}/M_N$ | Hệ quả CR-01; bổ sung điều kiện quá tải để không mất kiểm soát "dư công suất" | 24/10/2026 | **Đã ký (A.1, 24/10/2026)** |
| CR-03 | `SOW-3.1`, `QCD-C01` (ghi nhận, không sửa Block 0) | "Chọn dải 1.5 ÷ 2.2 kW"; "$P_{đm}$ ≤ 150% công suất tính toán" | Động cơ đề xuất 0.75 kW (≤ 2.2 kW vẫn đạt trần QCD-C01). **QĐ-08 (Người dùng, 24/10/2026):** "150% công suất tính toán" được hiểu là **so với công suất đỉnh $P_{\max}$ = 1.23 kW** → trần 1.84 kW; 0.75 kW = 61% → **Đạt** (KT-09) | Tính toán độc lập theo `RRM-04` | 24/10/2026 | **Đã ký (A.1, 24/10/2026)** — ghi nhận độ lệch SOW |
| CR-05 | `SRS-D04` (thiết bị phần lực) | — | **DRN80M4 0.75 kW + ACS380-04xS-03A3-4** | Định cỡ theo λ (QĐ-02); biên quá tải WC-5 = 1.03 | 24/10/2026 | **Người dùng chốt (QĐ-04)**; chấp nhận biên 1.03 |
| CR-06 | `SRS-D10`, `SRS-D13` (FSM, phanh) | Chỉ kiểm khả năng mô-men trước khi nhả phanh; $M_B$ = 5 N·m | Phát và đo $M_{hold}$ khi phanh còn kẹp; $M_B$ = 7 N·m | Đúng câu chữ SRS-FUNC-02 (Checker K7-1) | 24/10/2026 | **Người dùng chốt (QĐ-05)** |
| CR-07 | Phạm vi vận hành; `SRS-D13`, DFMEA FM-07, FM-12, KT-29 | Thiết kế có xét dừng khẩn, mất điện, E-STOP/STO/SS1, sự cố thiết bị | **Chỉ xét điều kiện vận hành lý tưởng** — các mục trên ghi `Không áp dụng` | Đồ án môn học năm 4: chỉ cần bảo đảm hệ vận hành được trong điều kiện lý tưởng | 24/10/2026 | **Người dùng chốt (QĐ-07)**; thay thế QĐ-06 |
| CR-04 | `P-16 [C]` | $i = 150$ | Dùng $i_{\text{thực}}$ = **155.34** của hộp số SEW R87 (`[W-06]`) qua `SRS-D03` — **không sửa SSoT** | Đúng mốc \"kiểm tra lại ở Khối 2/3\" của giả định `[C]`; xác định ngày 25/10/2026 | 24/10/2026 | **Đã ký (A.1)**; giá trị chốt 25/10/2026 |

> ID khác của Baseline A (SRS-FUNC-01..04, SRS-PERM-01..03) **giữ nguyên**.

---

## 2. DANH MỤC YÊU CẦU DẪN XUẤT `SRS-Dxx` (Checker K8)

Mọi mã có yêu cầu cha, bước tính sinh ra (ô Excel) và phép kiểm chứng. **Quy ước mã con:** một mã `SRS-Dxx` có thể gồm nhiều tham số; trong Excel và tài liệu thiết kế chúng được tách thành `SRS-Dxxa/b/c` (vd. `SRS-D05a` = $R_h$, `D05b` = $P_{dc}$, `D05c` = ngưỡng chopper, `D05d` = $P_{Rh}$) — mã con thừa kế yêu cầu cha và DV của mã gốc.

| Mã | Câu yêu cầu dẫn xuất (shall) | Giá trị / Ngưỡng | Cha | Bước tính | KC | DV |
| :---: | :--- | :--- | :---: | :--- | :---: | :---: |
| **SRS-D01** | Cụm động cơ–hộp số phải tạo được lực kéo tiếp tuyến ≥ $F_{\max}$ và bộ điều khiển phải giới hạn $\lvert i_{sq}\rvert \le i_{sq,\lim}$ để $F_k \le F_{\text{bám}}/1.2$ | $F_{\max} = 9,218$ N (khả năng 11,940 N ở −10% áp); $i_{sq,\lim} = 3.52$ A | SRS-PERM-01 | `Tính chọn` B, D, J | A | DV-05 |
| **SRS-D02** | Động cơ phải có $\lambda_K \ge 2.0$ và $\lambda_K (U_{\min}/U_N)^2 \ge M_{\max}/M_N$ | $M_{\max}/M_N = 2.19 \le \lambda_K(342/400)^2 = 2.485$ | SRS-PERM-01, -04 | `Tính chọn` D | A / I | DV-08 |
| **SRS-D03** | Mọi quy đổi tốc độ/mô-men phải dùng tỷ số truyền thực tế của hộp số; $i_{\text{thực}} \in [149.6; 165.3]$ | 155.34 (R87) | SRS-PERM-02 | `Tính chọn` C | I | DV-06 |
| **SRS-D04** | Động cơ $P_{đm}$ = 0.75 kW (S1) và biến tần $I_{Hd} \ge I_{N,\text{ĐC}}$, $1.5I_{Hd} \ge I_{\text{đỉnh}}$ | 0.75 kW; 2.6 A ≥ 1.75 A; 3.9 A ≥ 3.32 A | SRS-PERM-04 | `Tính chọn` F, G | A / I | DV-08 |
| **SRS-D05** | Nhánh hãm phải có $R_h \in [R_{\min}; \min(U_{chop}^2/P_{dc}; R_{\max})]$, chopper mở ở $700 \pm 20$ V, giữ $U_{dc} \le 780$ V, trip $800 \pm 10$ V | $R_h$ = 210 Ω ∈ [99; 428]; $P_{dc}$ = 436.5 W (công thức WORKFLOW §4.2-C4; kể $\delta$, $J_B$: 724 W ≤ 1,130 W — `Tính chọn` khối S, tham khảo); **D05d:** $P_{Rh}$ = 200 W ≥ $P_{Rh,tb}$ = 0.20 W (KT-42, `[W-09]`). $P_{dc}$ là giá trị định cỡ, **không phải ngưỡng PASS** của DV-04 (PASS: $U_{dc} \le 780$ V, không trip) | SRS-FUNC-04 | `Tính chọn` H, S; `GiaDinh_K3` D60 | A / I / S | DV-04 |
| **SRS-D06** | Bộ tạo quỹ đạo phải dùng $a^* = 0.45$ m/s², $\rho^* = 1.8$ m/s³ | $t_{acc}$ = 0.517 s | SRS-FUNC-03, SRS-PERM-03 | `Tính chọn` E | A / S | DV-03, DV-07 |
| **SRS-D07** | PI tốc độ chỉnh theo SO tại $J_{tune}$ phải cho $M_p \le 10\%$ ($v_{\text{peak}} \le 0.132$ m/s) | $K_{p,\omega}$ = 0.714 A·s/rad; $T_{i,\omega}$ = 7 ms; PM = 34.6° | SRS-PERM-02 (Downstream #1) | `Tính chọn` L | S | DV-06 |
| **SRS-D08** | Sai lệch tốc độ xác lập $e_{xl} \le 5\%$ | khâu I ⇒ 0 (lý thuyết) | SRS-PERM-02 (Downstream #2) | SDD §4.3 | S | DV-06 |
| **SRS-D09** | PI dòng chỉnh theo MO phải cho $\Delta t_{torque} \le 10$ ms | $K_{p,I}$ = 108.4 V/A; $T_{i,I}$ = 5.55 ms; 1.76 ms | SRS-FUNC-01 (Downstream #4) | `Tính chọn` K | S / I | DV-01 |
| **SRS-D10** | FSM chỉ nhả phanh sau khi động cơ **đã phát và đo được** $M_e \ge 0.95\,M_{hold}$ trong 0.1 s khi phanh còn kẹp, $M_{hold}$ = 100% $M_N$ (trong [100; 150]%) | 4.95 N·m | SRS-FUNC-02 (Downstream #5) | SDD §5 | S | DV-02 |
| **SRS-D11** | FSM đóng phanh khi $\lvert v\rvert \le 0.005$ m/s; cấm chốt chiều mới khi $\lvert v\rvert > 0.002$ m/s; phân giải đo $\Delta v \le 2$ mm/s | 0.005 / 0.002 m/s; $\Delta v$ = 1.23 mm/s | SRS-FUNC-02 (Downstream #5) | SDD §5, `Tính chọn` M | S | DV-02 |
| **SRS-D12** | Cấp tốc độ bò $v_{creep}$ | 0.033 m/s (27.5%) | SRS-FUNC-03 (Downstream #8) | `Tính chọn` N | S | DV-06 |
| **SRS-D13** | Phanh cơ phải có $\max(k_p M_c;\ 1.2 M_{hold}) \le M_B \le F_{\text{bám}}k_{qđ}\eta$ | 7 N·m ∈ [5.94; 10.12] (cấp BE1 7 N·m — `[W-07]`) | SRS-FUNC-02 | `Tính chọn` I | A / I | DV-02 |
| **SRS-D14** | Khi lưới −10%, bộ điều khiển phải giảm từ thông theo giới hạn điện áp nghịch lưu ($U_1 \le k_u U_{dc}/\sqrt2$) mà dòng vẫn trong giới hạn (bổ sung 26/10/2026, nhóm C) | $\psi_r^*/\psi_{rN}$ = 0.804 tại $v_{\max}$; $i_{sq}$ = 2.98 A ≤ 3.52 A (KT-37); $I_s$ = 2.25 A ≤ 3.9 A (KT-38) | SRS-PERM-02 | `Tính chọn` P | S | DV-06 |
| **SRS-D15** | Tốc độ động cơ bắt đầu giảm từ thông $\omega_{fw}$ (lưới danh định; mô phỏng tính trực tuyến theo $U_{dc}$ đo) | 133.2 rad/s (lưới −10%: 119.9 rad/s) | SRS-PERM-02 | `Tính chọn` P | S | DV-06 |

---

## 3. RTM CẤP PHÂN HỆ (Forward: PRD → SRS → SRS-Dxx → Phân hệ → Thiết kế → DV → Report)

| PRD | SRS | SRS-Dxx | Phân hệ (Khối 2) | Thiết kế (Khối 3) | DV | Report |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: |
| PRD-FUNC-01 | SRS-FUNC-01 | D09 | SS-4, SS-5 (ES7C), SS-2 | SDD §4.2, §5.4; BOM B1, A1 | DV-01 | A: Đạt (KT-22); S: chưa chạy |
| PRD-FUNC-04 | SRS-FUNC-02 | D10, D11, D13 | SS-4 (FSM), SS-5 (BE1) | SDD §5; Thuyết minh §8.2 | DV-02 | A: Đạt (KT-25, 27, 28, 30); KT-29 Không áp dụng (QĐ-07); S: chưa chạy |
| PRD-FUNC-02 | SRS-FUNC-03 | D06, D12 | SS-4 (S-curve) | SDD §3; Excel `Quy_dao` | DV-03 | A: Đạt (KT-18..20, 26); S: chưa chạy |
| PRD-FUNC-03 | SRS-FUNC-04 | D05 (a–d) | SS-2 (chopper), SS-3 ($R_h$) | Thuyết minh §8.1; DWG | DV-04 | A: Đạt (KT-13..17, 39, 42); S: chưa chạy |
| PRD-PERM-01 | SRS-PERM-01 | D01, D02 | SS-5, SS-6 | Thuyết minh §1, §5 | DV-05 | A: Đạt (KT-02..06, 11, 12, 33, 37); S: chưa chạy |
| PRD-PERM-02 | SRS-PERM-02 | D03, D07, D08, D12, D14, D15 | SS-4, SS-6 | SDD §4.1, §4.3; Thuyết minh §2, §6 | DV-06 | A: Đạt (KT-23, 24, 31, 35, 36); S: chưa chạy |
| PRD-PERM-03 | SRS-PERM-03 | D06 | SS-4, SS-6 | SDD §3.4 | DV-07 | A: θ_dư 0.63° (KT-21, tham khảo); KT-41 Đạt; S: chưa chạy |
| PRD-PERM-04 | SRS-PERM-04 (A.1) | D02, D04 | SS-2, SS-5 | Thuyết minh §4, §5, §7 | DV-08 | A/I: Đạt theo A.1 (KT-07, 09, 10, 38, 43); KT-08 Không áp dụng (CR-01) |

**Backward check:** mọi SRS-Dxx đều có cha thuộc 8 mã Baseline A; mọi DV-01..08 có ít nhất một SRS-Dxx → không có mã mồ côi.

---

## 4. DVP CẤP PHÂN HỆ (bổ sung cho DVP L0 v1.2 — không thay thế)

| Mã | Phân hệ | Bài kiểm chứng phân hệ | Phương pháp | Tín hiệu / Đại lượng | PASS | Liên kết DV L0 |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| DVP-SS-01 | SS-4 | Đáp ứng bước $i_{sq}^*$ = 100% $i_{sq,N}$ khi $\omega = 0$ (rotor khóa) | S | $i_{sq}(t)$, $M_e(t)$ | Thời gian tăng ≤ 10 ms; quá điều chỉnh ≤ 10% | DV-01 |
| DVP-SS-02 | SS-4 | Đáp ứng vòng tốc độ với lượng đặt S-curve ở $J_\Sigma$ và $J_{\Sigma,0}$ | S | $\omega_m(t)$, $v(t)$ | $M_p \le 10\%$, $e_{xl} \le 5\%$ | DV-06 |
| DVP-SS-03 | SS-4 | Khối S-curve độc lập: bước 0 → 0.12 → 0.033 → 0 → −0.12 | A / S | `a_ref`, `jerk_ref`, `v_ref` | $\lvert a\rvert \le 0.45$; $\lvert\rho\rvert \le 1.8$; mức bò xác lập ∈ [0.030; 0.036] m/s | DV-03, DV-06 |
| DVP-SS-04 | SS-4 (FSM) | Bảng chân lý chuyển trạng thái + lệnh đảo chiều khi $v = 0.1$ m/s | S | `state`, `dir`, `brake_cmd`, $M_e$, $v$ | Không đổi `dir` khi $\lvert v\rvert > 0.002$; `brake_cmd` chỉ = 1 sau khi $M_e \ge 0.95 M_{hold}$ (phanh kẹp); `brake_cmd` → 0 khi $\lvert v\rvert \le 0.005$; $\Delta s \le 10$ mm | DV-02 |
| DVP-SS-05 | SS-2/SS-3 | Giảm tốc đầy tải ở lưới +10% (WC-7) | S | $U_{dc}(t)$, $I_{Rh}(t)$ | $U_{dc} \le 780$ V; không trip (ngưỡng theo $U_{dc}$, không so công suất hãm đo được với $P_{dc}$ = 436.5 W của D05b) | DV-04 |
| DVP-SS-06 | SS-5 | Tăng tốc đầy tải ở lưới −10% (342 V, động cơ 400 V — WC-5) và chu trình S3 ở 342 V | S | $M_e(t)$, $i_s(t)$, $\psi_r(t)$, $i_{s,rms}$ | $M_e$ không bão hòa ở $M_K$; $i_s \le 1.5 I_{Hd}$; $i_{s,rms}$ chu trình ≤ $I_N/1.2$ (kiểm nhiệt DV-08 ở 342 V) | DV-05, DV-08 |
| DVP-SS-07 | SS-4 | Độ nhạy RFOC với $R_r$ ±30% (nhiễu N-03) | S | $v(t)$, $\psi_r(t)$ | Vẫn đạt DV-06 | DV-06 |
| DVP-SS-08 | Tích hợp | Đo $\rho(t)$ qua $G_d(s) = s/(T_f s + 1)$, $T_f$ = 5 ms | S | $\rho(t)$ | $\lvert\rho\rvert \le 2.0$ | DV-07 |

Toàn bộ cột kết quả: **`Report: chưa chạy`** (Khối 5).

---

## 5. BẢNG ĐỐI XỨNG V-MODEL

| Nhánh trái (thiết kế) | Tài liệu | ↔ | Nhánh phải (kiểm chứng) | Phương pháp |
| :--- | :--- | :---: | :--- | :--- |
| Yêu cầu sản phẩm | PRD v3.1 | ↔ | Nghiệm thu SAR — DVP&R L0 Report | Tổng hợp |
| Yêu cầu hệ thống | SRS A v1.2 / A.1 | ↔ | DV-01..08 (TS-01..03) | A / S / I |
| Kiến trúc | SAD, ICD v1.0 | ↔ | Kiểm tra giao diện K9 + tích hợp Simulink | Checker + S |
| Thiết kế chi tiết phần lực | Thuyết minh, Excel, DWG, BOM | ↔ | `Kiểm tra` KT-01..43; DVP-SS-05, -06 | A / I / S |
| Thiết kế chi tiết điều khiển | SDD | ↔ | DVP-SS-01..04, -07, -08 | S |

---

## 6. WCCA RÚT GỌN (chi tiết: Thuyết minh §9)

Tổ hợp xấu nhất được xét: đầy tải 14,244 kg (+20% $m_{xc}$), lưới −10%, $w_0$ = 0.018, $\eta$ = 0.85 (kéo); và $w_0$ = 0.012, $\eta$ = 0.95, lưới +10% (hãm).

| Chỉ tiêu | Xấu nhất | Ngưỡng | Kết luận |
| :--- | :---: | :---: | :---: |
| Biên quá tải $\lambda_K (U/U_N)^2/(M_{\max}/M_N)$, $U_N$ = 400 V | **1.02** (WC-5, sát; với $i$ = 155.34) | ≥ 1.0 | Đạt — **Người dùng chấp nhận biên 1.03 (QĐ-04)** |
| $k_{\text{bám}}$ tại $a$ = 0.5 | 1.450 (WC-2/5) | ≥ 1.20 | Đạt |
| $P_{dc,\text{hãm}}$ | 499 W (WC-7) | ≤ $P_{BR,\max}$ 1,130 W | Đạt |
| $U_{dc0}$ khi đứng yên | 591 V (WC-7) | < 680 V | Đạt |
| $k_{dt}$ ước lượng | 2.51 (WC-5) | ≥ 1.20 (A.1) | Đạt |
| $k_{\text{bám}}$ khi $\varphi$ = 0.15 (độ nhạy) | 1.137 tại $a$ = 0.5 / 1.232 tại $a^*$ = 0.45 | ≥ 1.20 | Đạt nhờ $a^*$ = 0.45 |

---

## 7. CẬP NHẬT DFMEA XUỐNG CẤP PHÂN HỆ (từ DFMEA L1 v1.0)

| ID L1 | Biện pháp đã hiện thực trong Khối 3 | Bằng chứng | Trạng thái AP₁ |
| :---: | :--- | :--- | :---: |
| FM-01 | S-curve $a^* = 0.45$, $\rho^* = 1.8$; θ_dư ≈ 0.63° | SDD §3; KT-18..21 | L (chờ DV-07) |
| FM-02 | ACS380 chopper + $R_h$ = 210 Ω, 200 W `[W-09]` | KT-13..17, 39, 42 | L (chờ DV-04) |
| FM-03 | Thử mô-men giữ thật khi phanh còn kẹp (S3) rồi mới nhả (S3B) | SDD §5 (v1.1) | L (chờ DV-02) |
| FM-04 | Khóa chéo `dir` khi $\lvert v\rvert > 0.002$ | SDD §5.3; KT-25 | L (chờ DV-02) |
| FM-05 | $k_{dt}$ = 3.61; TF động cơ | KT-07 | L |
| FM-06 | $i_{sq,\lim}$ = 3.52 A; $k_{\text{bám}}$ = 1.516 | KT-02, 03 | L |
| FM-07 | Không áp dụng (QĐ-07): không xét dừng khẩn/mất điện; $M_B$ = 7 N·m ∈ [5.94; 10.12] | KT-27, 28 (KT-29: Không áp dụng) | — |
| FM-08 | `SRS-D03` dùng $i_{\text{thực}}$ = 155.34 | KT-31 Đạt (+1.1%) | L |
| FM-09 | $J_{tune}$ = √(J_max·J_min), PM 34.6° | KT-23, 24 | L (chờ DV-06) |
| FM-10 | ICD v1.0; bảng §6 SDD | Checker K9 | L |
| FM-11 | Chọn biến tần theo $1.5I_{Hd}$ | KT-11, 12 | L |
| FM-12 | Không áp dụng (QĐ-07): không xét sự cố phanh | — | — |
