# SRS BASELINE A.1 (ĐÃ KÝ 24/10/2026) — YÊU CẦU DẪN XUẤT `SRS-Dxx`, RTM/DVP CẤP PHÂN HỆ, V-MODEL & WCCA RÚT GỌN

**Mã tài liệu:** `SRS-A1-8.5EMG-TROLLEY-v1.0` — Gói `SOW-3.5` (Phạm Văn Hưng & Nghiêm Trọng Đông) — Khối 3  
**Ngày:** 24/10/2026 — **Trạng thái:** **ĐÃ DUYỆT — Cổng G4 (`CDR-EVT`) đóng ngày 24/10/2026**. **SRS Baseline A.1 CÓ HIỆU LỰC từ 24/10/2026** (Người dùng ký CR-01..CR-07), thay thế Baseline A v1.2 đối với các ID nêu ở §1; các ID khác giữ nguyên nội dung v1.2. ~~Tệp Block 1 v1.2 vẫn giữ nguyên làm hồ sơ lịch sử.~~ **Cập nhật 26/10/2026 (Người dùng duyệt nhóm A):** CR-01, CR-02, CR-03 đã được tích hợp vào Block 0/1 — PRD v3.2, SOW v1.3, BCA-QFD v1.2, slide MCR v2.1, SRS Baseline A v1.3, SRS chi tiết v1.3, RTM/DVP v1.3 (tên tệp giữ hậu tố cũ); bản trước khi sửa lưu trong lịch sử phiên bản của từng tệp.  
**Nguồn số:** `00_Tinh_toan_Xe_con_x2_v1.5.xlsx` sheet `Dẫn xuất`, `Kiểm tra`, `WCCA`, `UocLuong_TS`  
**Lịch sử:** **v1.5 (28/10/2026, nhóm duyệt)** thêm CR-19 (§1): lượng đặt $a^*$ = 0.10 m/s², $\rho^*$ = 0.40 m/s³, chọn lại DRN71M4 0.37 kW + ACS380-01A8-4, rút gọn SRS; nguồn số Excel v2.0 rút gọn · **v1.4 (28/10/2026, Người dùng duyệt)** chốt phạm vi môn học CR-08..CR-18 (§1); nguồn số Excel v1.5: tham số động cơ hiệu chỉnh (KT-44), $i_{sq,\lim}$ = 3.86 A, PI dòng và PI tốc độ chỉnh lại (`SRS-D07`, `SRS-D09`), `SRS-D14/D15` ở lưới danh định, WCCA 2 trường hợp (§6), DVP-SS-06/07 tùy chọn, DFMEA §7 theo DFMEA L1 v1.1 · v1.3 (27/10/2026) theo Checker lượt 1 (K8-1, K7-1, K10-3, K11-1): nguồn số chuyển sang Excel v1.4; thêm mã con `SRS-D05d` ($P_{Rh}$); đăng ký `SRS-D14`, `SRS-D15` (nhóm C, Người dùng duyệt 26/10/2026); RTM, V-model và DFMEA cập nhật theo KT-33..43; ghi rõ ngưỡng PASS của DV-04 không phải $P_{dc}$ = 436.5 W; các giá trị khác không đổi · v1.2 (25/10/2026) nhập $i_{\text{thực}}$ = 155.34 (SEW R87), xác minh BE1 7 N·m, R_h, QF1/KM1; số liệu tính lại · v1.0 (24/10/2026) bản đầu · v1.1 (24/10/2026) xử lý Checker: K11-1 mở rộng CR-01/CR-03, K8-1/K8-2 (cha của D02, quy ước mã con), K7-1 (D10, D13 theo bước thử mô-men), K7-2 (tiêu chí DVP-SS), K6-2/K6-4 (WCCA theo $U_N$ = 400 V, có trong Excel)

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
| CR-08 | PRD §3, §5, PRD-PERM-01/03/04; SOW QCD-Q02/Q03; RTM/DVP chi tiết | Dung sai trên số liệu đầu vào: $m_{nh}$ ±2%, $m_{xc}$ ±5%, $M_\Sigma$ ±4.5%, $h$ ±0.1 m, CD ±2%, chu kỳ ±30 s, $f$ ±2% | Bỏ; giữ $v_{\max}$ = 0.12 m/s ±5% và lưới 380 V ±10% | Đề bài cho giá trị cố định; dung sai không có phép kiểm chứng tương ứng | 28/10/2026 | **Người dùng duyệt** |
| CR-09 | PRD MOP-02/03, PRD-PERM-03; SOW QCD-Q03; SRS chi tiết, RTM/DVP chi tiết | $a \in [0.45;\ 0.50]$ m/s², $\rho \in [1.80;\ 2.00]$ m/s³ | $\lvert a \rvert \le 0.50$ m/s², $\lvert \rho \rvert \le 2.00$ m/s³ (một phía, như SRS Baseline A); $a^*$ = 0.45, $\rho^*$ = 1.8 giữ là lựa chọn thiết kế (`SRS-D06`) | Đề bài chỉ cho cận trên | 28/10/2026 | **Người dùng duyệt** |
| CR-10 | PRD MOE-01, MOP-03, ConOps, §5; SOW QCD-Q03; SRS §1.2 | S-curve "dập tắt lắc dư"; nghiệm thu $\theta_0 \le 2.92°$ | $\theta(t)$ quan sát và báo cáo, không nghiệm thu; chống lắc ngoài phạm vi | S-curve với $t_{acc} \ll T_p$ không giảm được lắc dư (SDD §3.4) | 28/10/2026 | **Người dùng duyệt** |
| CR-11 | PRD §5, MOE-02 | Tiêu chí nghiệm thu $t_{stop} \le 2$ s, IP54, ≤ 48 V, ISO M5, không trôi khi mất điện | Điều kiện biên tham chiếu, không nghiệm thu | Thống nhất với tailoring SOW §1.1 và QĐ-07 | 28/10/2026 | **Người dùng duyệt** |
| CR-12 | SOW-4.1, 4.2, 5.2; RTM/DVP chi tiết §3.2; DVP phân hệ §4; SDD §7.3 | Nghịch lưu IGBT; kịch bản chu trình S3 có tiêm nhiễu; xác nhận PASS toàn bộ DV; DVP-SS-06/07, TS-01b, TS-03 bắt buộc | Nghịch lưu mô hình trung bình; bắt buộc `TS-01a`, `TS-01c`, `TS-02` ở lưới danh định; chu trình S3 và lưới ±10% kiểm bằng tính toán (A); DVP-SS-06, DVP-SS-07, `TS-01b`, `TS-03` tùy chọn; đánh giá Đạt/Không đạt kèm NCR | Đề bài yêu cầu mô phỏng ít nhất một kịch bản | 28/10/2026 | **Người dùng duyệt** |
| CR-13 | SRS-PERM-04; DV-08; PRD-PERM-04; SOW-3.1 | $k_{dt} \ge 1.20$ "dưới lưới 380 V ±10%"; DV-08 tính nhiệt ở 342 V | $k_{dt}$ tính ở lưới danh định 380 V; quá tải mô-men kiểm ở lưới −10% (`SRS-D02`, KT-05) | Đúng cách kiểm nghiệm động cơ trong bài giảng | 28/10/2026 | **Người dùng duyệt** |
| CR-14 | SOW QCD-Q02, SOW-3.1; PRD; Excel sheet `WCCA`; §6 | WCCA 8 trường hợp; dải $w_0$ = 0.015 ± 0.003, $F_c$ ± 420 N | WCCA còn WC-0 (danh định) và WC-1 (lưới −10%); bỏ dải $w_0$ và $F_c$ | Phân tích trường hợp xấu nhất vượt mức môn học | 28/10/2026 | **Người dùng duyệt** |
| CR-15 | `SRS-D14`, `SRS-D15`; Excel khối P, KT-37/38, `Mo_phong` | Giảm từ thông tính ở lưới −10% ($k_\psi$ = 0.804); biến `w_fw_min` | Giảm từ thông tính ở lưới danh định ($k_\psi$ = 0.893); bỏ `w_fw_min` | Lưới −10% chỉ kiểm quá tải bằng tính toán (CR-12, CR-13) | 28/10/2026 | **Người dùng duyệt** |
| CR-16 | Downstream #6 (SRS Baseline A §4); SAD §4.2; SOW QCD-Q02; PRD; RTM/DVP chi tiết | $F_{\max}$ = 9.22 kN, dải nghiệm thu [8.80; 9.70] kN | $F_{\max}$ = 9,218 N là giá trị tính toán; kiểm bằng lực kéo động cơ tạo được ≥ $F_{\max}$ (KT-06) | Dải dung sai gán cho giá trị tính, không còn căn cứ sau CR-14 | 28/10/2026 | **Người dùng duyệt** |
| CR-17 | Downstream #3; SAD; ICD IF-05; SOW QCD-Q04; `SRS-D05c` | Chopper ON 700 ± 20 V; trip 800 ± 10 V | 700 / 780 / 800 V là tham số mô hình Simulink, không gán dung sai | Ngưỡng firmware ACS380 chưa xác minh; dung sai không kiểm chứng được | 28/10/2026 | **Người dùng duyệt** |
| CR-18 | SSoT Phần 2 dòng 31 | $D \ge 10:1$ "chuyển sang Khối 3" (không có mã nhận) | Xóa | Không thuộc 8 yêu cầu SRS; điều chỉnh tốc độ đã có ở `SRS-D12` | 28/10/2026 | **Người dùng duyệt** |
| CR-19 | `SRS-FUNC-02`, `SRS-FUNC-03`, `SRS-PERM-03`, `SRS-PERM-04`, Downstream #1..#8 (SRS Baseline A §3–§4); lượng đặt $a^*$, $\rho^*$; thiết bị phần lực | $a^*$ = 0.45 m/s², $\rho^*$ = 1.8 m/s³; DRN80M4 0.75 kW + ACS380-03A3-4; PERM-03 đo $a(t)$, $\rho(t)$ thực tế; FUNC-02 có $\Delta s \le \pm 10$ mm; 8 Downstream cùng mức | $a^*$ = **0.10 m/s²**, $\rho^*$ = **0.40 m/s³** (giới hạn đề bài 0.5 / 2.0 giữ nguyên); **DRN71M4 0.37 kW + ACS380-04xS-01A8-4**, BE1 5 N·m, cầu chì gG 4 A (R87 $i$ = 155.34 và $R_h$ = 210 Ω giữ nguyên); PERM-03 gộp vào FUNC-03 (kiểm trên lượng đặt, đo trên mô phỏng là tùy chọn); FUNC-02 giữ logic khóa chéo và phanh, bỏ chỉ tiêu $\Delta s$; chọn động cơ theo hai tiêu chí ngang nhau: $k_{dt} \ge 1.20$ (PERM-04) và $k_\lambda \ge 1.20$ (Downstream #7 nâng lên); giữ Downstream #6, #7; hoãn #1, #2, #3, #4, #5, #8 sang khối điều khiển và mô phỏng | Xem "Giải thích CR-19" dưới bảng. Nguồn số: `Block 3/00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx` (19/19 KT đạt, v2.0.1) | 28/10/2026 | **Nhóm duyệt; hiệu lực từ bản v2.0 về sau** |

> ID khác của Baseline A (SRS-FUNC-01..04, SRS-PERM-01..03) **giữ nguyên**.

### Giải thích CR-19 — lượng đặt gia tốc, độ giật và chọn lại thiết bị

**1. Vì sao đổi lượng đặt.** $v_{\max}$ = 0.12 m/s, $a_{\max}$ = 0.5 m/s², $\rho_{\max}$ = 2.0 m/s³ là số liệu đề bài `[A]` và vẫn là **giới hạn trên** (CR-09). Lượng đặt $a^*$, $\rho^*$ là lựa chọn thiết kế `[C]`. So sánh trong Excel v2.0 (sheet `Chon_DC` mục B, đầy tải):

| $a^*$ (m/s²) | $\rho^*$ (m/s³) | $t_{acc}$ (s) | $M_{\max}$ (N·m) | Động cơ nhỏ nhất đạt $k_\lambda \ge 1.2$ và $k_{dt} \ge 1.2$ |
| :---: | :---: | :---: | :---: | :--- |
| 0.45 (cũ) | 1.8 | 0.52 | 9.93 | DRN80M4 0.75 kW |
| 0.30 | 1.2 | 0.65 | 7.24 | DRN80M4 0.75 kW |
| 0.20 | 0.8 | 0.85 | 5.45 | DRN80MK4 0.55 kW |
| **0.10 (mới)** | **0.4** | **1.45** | **3.66** | **DRN71M4 0.37 kW** |
| 0.06 | 0.24 | 2.25 | 2.95 | DRN71M4 0.37 kW |

- **Năng suất gần như không đổi:** mỗi hành trình 120 s chỉ chậm thêm ≈ 0.9 s (< 1%).
- **Lắc tải không xấu đi:** với mọi $t_{acc}$ ngắn hơn nhiều so với $T_p$ = 6.95 s, tải nhận gần như một bước vận tốc, góc lắc dư ≈ 0.6° ở cả $a^*$ = 0.45 và 0.10 (mô phỏng con lắc tuyến tính $\ddot\theta + \omega_p^2\theta = -a/h$). Tăng tốc mạnh không có lợi gì cho lắc tải.
- **Mô-men đỉnh giảm 2.7 lần** (9.93 → 3.66 N·m) ⇒ động cơ, biến tần nhỏ hơn; dự trữ bám tăng ($k_{bám}$ 1.52 → 3.74); mô-men ra hộp số 1,390 → 512 N·m.
- **Chọn động cơ trở lại đúng phương pháp bài giảng:** với $a^*$ = 0.45, động cơ bị định cỡ theo mô-men đỉnh nên dư nhiệt 3.6 lần (xung đột K11, QĐ-02). Với $a^*$ = 0.10, động cơ được chọn đồng thời theo nhiệt ($k_{dt}$ = 1.84, với $P_{đt} = M_{đt}\omega_m$ = 201 W) và quá tải ($k_\lambda$ = 1.40); động cơ nhỏ hơn một cấp (DRN71MS4 0.25 kW) trượt cả hai tiêu chí ($k_\lambda$ = 0.85; $M_c/M_N$ = 1.10).
- **Chọn $a^*$ = 0.10 thay vì 0.06 hoặc khớp $t_{acc} = T_p$:** 0.10 là giá trị tròn lớn nhất vẫn cho phép dùng DRN71M4; $t_{acc} = T_p$ (≈ 0.023 m/s²) chỉ triệt lắc khi đúng chiều dài cáp $h$, mà $h$ thay đổi khi nâng hạ — thuộc điều khiển chống lắc, ngoài phạm vi (SRS §1.2).
- **$\rho^*$ = 0.40:** giữ tỷ số $\rho^*/a^*$ = 4 s⁻¹ như bản cũ (đoạn tăng độ giật $T_j$ = 0.25 s); $a^{*2}/\rho^*$ = 0.025 m/s < $v_{\max}$ nên S-curve đủ 7 đoạn.

**2. Hệ quả hãm.** Ở $a^*$ = 0.10, khi giảm tốc đầy tải lực cản đủ hãm ($M_h$ = +0.08 N·m), không có năng lượng tái sinh; khi không tải chỉ có ≈ 30 W do quán tính rotor. $R_h$ vì vậy được kiểm cho **trường hợp giới hạn** giảm tốc với $a_{\max}$ = 0.5 m/s²: $P_{dc}$ = 494 W ≤ $P_{BR,\max}$ = 560 W của ACS380-01A8-4; $R_h$ = 210 Ω ∈ [99; 933] Ω.

**3. Thiết bị sau CR-19.** SEW DRN71M4 0.37 kW (phanh BE1 đặt 5 N·m, encoder ES7C) + hộp số R87 $i$ = 155.34 (có thể giảm cỡ, cần chạy lại SEW Drive Selection) + ABB ACS380-04xS-01A8-4 + $R_h$ Danotherm 210 Ω/200 W + cầu chì gG OFAF000H4 + contactor AF09. Quán tính $J_{BMot}$ của khung DRN71 chưa có trong kho; dùng giá trị của DRN80M4 (26.2×10⁻⁴ kg·m²) làm cận trên `[C]`.

**4. 14 tham số động cơ (DRN71M4).** Bộ 14 công thức lệch catalogue tới 22% ($\lambda_K$); bộ hiệu chỉnh $R_s$ = 17.25 Ω, $R_r'$ = 17.31 Ω, $L_{\sigma s} = L_{\sigma r}$ = 0.0731 H, $L_m$ = 0.905 H, sai số lớn nhất 1.9% (sheet `Tham_so_DC`).

**5. Phạm vi hiệu lực.** Áp dụng từ Excel v2.0 về sau. Các tài liệu Block 3 viết theo DRN80M4 (Thuyết minh, Sơ đồ mạch lực + BOM, SDD, mục `SRS-Dxx` ở §2 tài liệu này) và Excel v1.5 **giữ làm lịch sử, chưa cập nhật số** — cần sửa trước khi dùng cho mô phỏng.

---

## 2. DANH MỤC YÊU CẦU DẪN XUẤT `SRS-Dxx` (Checker K8)

Mọi mã có yêu cầu cha, bước tính sinh ra (ô Excel) và phép kiểm chứng. **Quy ước mã con:** một mã `SRS-Dxx` có thể gồm nhiều tham số; trong Excel và tài liệu thiết kế chúng được tách thành `SRS-Dxxa/b/c` (vd. `SRS-D05a` = $R_h$, `D05b` = $P_{dc}$, `D05c` = ngưỡng chopper, `D05d` = $P_{Rh}$) — mã con thừa kế yêu cầu cha và DV của mã gốc.

| Mã | Câu yêu cầu dẫn xuất (shall) | Giá trị / Ngưỡng | Cha | Bước tính | KC | DV |
| :---: | :--- | :--- | :---: | :--- | :---: | :---: |
| **SRS-D01** | Cụm động cơ–hộp số phải tạo được lực kéo tiếp tuyến ≥ $F_{\max}$ và bộ điều khiển phải giới hạn $\lvert i_{sq}\rvert \le i_{sq,\lim}$ để $F_k \le F_{\text{bám}}/1.2$ | $F_{\max} = 9,218$ N (khả năng 11,940 N ở −10% áp); $i_{sq,\lim} = 3.86$ A | SRS-PERM-01 | `Tính chọn` B, D, J | A | DV-05 |
| **SRS-D02** | Động cơ phải có $\lambda_K \ge 2.0$ và $\lambda_K (U_{\min}/U_N)^2 \ge M_{\max}/M_N$ | $M_{\max}/M_N = 2.19 \le \lambda_K(342/400)^2 = 2.485$ | SRS-PERM-01, -04 | `Tính chọn` D | A / I | DV-08 |
| **SRS-D03** | Mọi quy đổi tốc độ/mô-men phải dùng tỷ số truyền thực tế của hộp số; $i_{\text{thực}} \in [149.6; 165.3]$ | 155.34 (R87) | SRS-PERM-02 | `Tính chọn` C | I | DV-06 |
| **SRS-D04** | Động cơ $P_{đm}$ = 0.75 kW (S1) và biến tần $I_{Hd} \ge I_{N,\text{ĐC}}$, $1.5I_{Hd} \ge I_{\text{đỉnh}}$ | 0.75 kW; 2.6 A ≥ 1.75 A; 3.9 A ≥ 3.32 A | SRS-PERM-04 | `Tính chọn` F, G | A / I | DV-08 |
| **SRS-D05** | Nhánh hãm phải có $R_h \in [R_{\min}; \min(U_{chop}^2/P_{dc}; R_{\max})]$, chopper mở ở 700 V, giữ $U_{dc} \le 780$ V, ngắt ở 800 V (tham số mô hình, CR-17) | $R_h$ = 210 Ω ∈ [99; 428]; $P_{dc}$ = 436.5 W (công thức WORKFLOW §4.2-C4; kể $\delta$, $J_B$: 724 W ≤ 1,130 W — `Tính chọn` khối S, tham khảo); **D05d:** $P_{Rh}$ = 200 W ≥ $P_{Rh,tb}$ = 0.20 W (KT-42, `[W-09]`). $P_{dc}$ là giá trị định cỡ, **không phải ngưỡng PASS** của DV-04 (PASS: $U_{dc} \le 780$ V, không trip) | SRS-FUNC-04 | `Tính chọn` H, S; `GiaDinh_K3` D60 | A / I / S | DV-04 |
| **SRS-D06** | Bộ tạo quỹ đạo phải dùng $a^* = 0.45$ m/s², $\rho^* = 1.8$ m/s³ | $t_{acc}$ = 0.517 s | SRS-FUNC-03, SRS-PERM-03 | `Tính chọn` E | A / S | DV-03, DV-07 |
| **SRS-D07** | PI tốc độ chỉnh theo SO tại $J_{tune}$ phải cho $M_p \le 10\%$ ($v_{\text{peak}} \le 0.132$ m/s) | $J_{tune} = J_{rig}$; $K_{p,\omega}$ = 0.295 A·s/rad; $T_{i,\omega}$ = 13 ms; PM ≥ 31.6° (KT-23, 24, 36) | SRS-PERM-02 (Downstream #1) | `Tính chọn` L | S | DV-06 |
| **SRS-D08** | Sai lệch tốc độ xác lập $e_{xl} \le 5\%$ | khâu I ⇒ 0 (lý thuyết) | SRS-PERM-02 (Downstream #2) | SDD §4.3 | S | DV-06 |
| **SRS-D09** | PI dòng chỉnh theo MO phải cho $\Delta t_{torque} \le 10$ ms | $K_{p,I}$ = 76.6 V/A; $T_{i,I}$ = 3.98 ms; 1.76 ms | SRS-FUNC-01 (Downstream #4) | `Tính chọn` K | S / I | DV-01 |
| **SRS-D10** | FSM chỉ nhả phanh sau khi động cơ **đã phát và đo được** $M_e \ge 0.95\,M_{hold}$ trong 0.1 s khi phanh còn kẹp, $M_{hold}$ = 100% $M_N$ (trong [100; 150]%) | 4.95 N·m | SRS-FUNC-02 (Downstream #5) | SDD §5 | S | DV-02 |
| **SRS-D11** | FSM đóng phanh khi $\lvert v\rvert \le 0.005$ m/s; cấm chốt chiều mới khi $\lvert v\rvert > 0.002$ m/s; phân giải đo $\Delta v \le 2$ mm/s | 0.005 / 0.002 m/s; $\Delta v$ = 1.23 mm/s | SRS-FUNC-02 (Downstream #5) | SDD §5, `Tính chọn` M | S | DV-02 |
| **SRS-D12** | Cấp tốc độ bò $v_{creep}$ | 0.033 m/s (27.5%) | SRS-FUNC-03 (Downstream #8) | `Tính chọn` N | S | DV-06 |
| **SRS-D13** | Phanh cơ phải có $\max(k_p M_c;\ 1.2 M_{hold}) \le M_B \le F_{\text{bám}}k_{qđ}\eta$ | 7 N·m ∈ [5.94; 10.12] (cấp BE1 7 N·m — `[W-07]`) | SRS-FUNC-02 | `Tính chọn` I | A / I | DV-02 |
| **SRS-D14** | Bộ điều khiển phải giảm từ thông theo giới hạn điện áp nghịch lưu ($U_1 \le k_u U_{dc}/\sqrt2$) khi động cơ 400 V làm việc trên lưới danh định 380 V mà dòng vẫn trong giới hạn | $\psi_r^*/\psi_{rN}$ = 0.893 tại $v_{\max}$; $i_{sq}$ = 2.38 A ≤ $i_{sq,\lim}$ = 3.86 A (KT-37); $I_s$ = 1.95 A ≤ 3.9 A (KT-38) | SRS-PERM-02 | `Tính chọn` P | S | DV-06 |
| **SRS-D15** | Tốc độ động cơ bắt đầu giảm từ thông $\omega_{fw}$ (lưới danh định; mô phỏng tính trực tuyến theo $U_{dc}$ đo) | 133.2 rad/s | SRS-PERM-02 | `Tính chọn` P | S | DV-06 |

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
| PRD-PERM-03 | SRS-PERM-03 | D06 | SS-4, SS-6 | SDD §3.4 | DV-07 | A: $\theta$ chỉ quan sát, $\theta_{dư}$ ≤ 1.27° (KT-21 Không áp dụng, CR-10); KT-41 Đạt; S: chưa chạy |
| PRD-PERM-04 | SRS-PERM-04 (A.1) | D02, D04 | SS-2, SS-5 | Thuyết minh §4, §5, §7 | DV-08 | A/I: Đạt theo A.1 (KT-07, 09, 10, 38, 43); KT-08 Không áp dụng (CR-01) |

**Backward check:** mọi SRS-Dxx đều có cha thuộc 8 mã Baseline A; mọi DV-01..08 có ít nhất một SRS-Dxx → không có mã mồ côi.

---

## 4. DVP CẤP PHÂN HỆ (bổ sung cho DVP L0 v1.2 — không thay thế)

| Mã | Phân hệ | Bài kiểm chứng phân hệ | Phương pháp | Tín hiệu / Đại lượng | PASS | Liên kết DV L0 |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: |
| DVP-SS-01 | SS-4 | Đáp ứng bước $i_{sq}^*$ = 100% $i_{sq,N}$ khi $\omega = 0$ (rotor khóa) | S | $i_{sq}(t)$, $M_e(t)$ | Thời gian tăng ≤ 10 ms; quá điều chỉnh ≤ 10% | DV-01 |
| DVP-SS-02 | SS-4 | Đáp ứng vòng tốc độ với lượng đặt S-curve ở $J_{rig}$ (`TS-01a`) và ở $J_\Sigma$, $J_{\Sigma,0}$ (`TS-01c`) | S | $\omega_m(t)$, $v(t)$ | $M_p \le 10\%$, $e_{xl} \le 5\%$ | DV-06 |
| DVP-SS-03 | SS-4 | Khối S-curve độc lập: bước 0 → 0.12 → 0.033 → 0 → −0.12 | A / S | `a_ref`, `jerk_ref`, `v_ref` | $\lvert a\rvert \le 0.45$; $\lvert\rho\rvert \le 1.8$; mức bò xác lập ∈ [0.030; 0.036] m/s | DV-03, DV-06 |
| DVP-SS-04 | SS-4 (FSM) | Bảng chân lý chuyển trạng thái + lệnh đảo chiều khi $v = 0.1$ m/s | S | `state`, `dir`, `brake_cmd`, $M_e$, $v$ | Không đổi `dir` khi $\lvert v\rvert > 0.002$; `brake_cmd` chỉ = 1 sau khi $M_e \ge 0.95 M_{hold}$ (phanh kẹp); `brake_cmd` → 0 khi $\lvert v\rvert \le 0.005$; $\Delta s \le 10$ mm | DV-02 |
| DVP-SS-05 | SS-2/SS-3 | Giảm tốc đầy tải, mô hình khối cứng (`TS-01c`, lưới danh định) | S | $U_{dc}(t)$, $I_{Rh}(t)$ | $U_{dc} \le 780$ V; không trip (ngưỡng theo $U_{dc}$, không so công suất hãm đo được với $P_{dc}$ = 436.5 W của D05b) | DV-04 |
| DVP-SS-06 | SS-5 | *Tùy chọn (CR-12):* tăng tốc đầy tải ở lưới −10% (342 V) | S | $M_e(t)$, $i_s(t)$, $\psi_r(t)$, $i_{s,rms}$ | $M_e$ không bão hòa ở $M_K$; $i_s \le 1.5 I_{Hd}$; quá tải kiểm bằng tính toán (KT-05) | DV-05 |
| DVP-SS-07 | SS-4 | *Tùy chọn (CR-12):* độ nhạy RFOC với $R_r$ ±30% (nhiễu N-03) | S | $v(t)$, $\psi_r(t)$ | Vẫn đạt DV-06 | DV-06 |
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

## 6. WCCA RÚT GỌN (CR-14: hai trường hợp)

Hai trường hợp: WC-0 lưới danh định 380 V và WC-1 lưới −10% (342 V); các thông số khác lấy giá trị danh định. Nhiệt $k_{dt}$ tính ở lưới danh định (KT-07, CR-13); $U_{dc}$ khi lưới +10% kiểm ở KT-16.

| Chỉ tiêu | WC-0 | WC-1 | Ngưỡng | Kết luận |
| :--- | :---: | :---: | :---: | :---: |
| Biên quá tải $\lambda_K (U/U_N)^2/(M_{\max}/M_N)$, $U_N$ = 400 V | 1.40 | **1.14** | ≥ 1.0 | Đạt |
| $k_{\text{bám}}$ tại $a$ = 0.5 / $a^*$ = 0.45 | 1.516 / 1.643 | 1.516 / 1.643 | ≥ 1.20 | Đạt |
| $P_{dc,\text{hãm}}$ | 436.5 W | 436.5 W | ≤ $P_{BR,\max}$ 1,130 W | Đạt |
| $U_{dc0}$ khi đứng yên | 537 V | 484 V | < 680 V | Đạt |

---

## 7. CẬP NHẬT DFMEA XUỐNG CẤP PHÂN HỆ (từ DFMEA L1 v1.0)

| ID L1 | Biện pháp đã hiện thực trong Khối 3 | Bằng chứng | Trạng thái AP₁ |
| :---: | :--- | :--- | :---: |
| FM-01 | S-curve $a^* = 0.45$, $\rho^* = 1.8$ (xung giật cơ cấu); $\theta$ chỉ quan sát (CR-10) | SDD §3; KT-18..20 | L (chờ DV-07) |
| FM-02 | ACS380 chopper + $R_h$ = 210 Ω, 200 W `[W-09]` | KT-13..17, 39, 42 | L (chờ DV-04) |
| FM-03 | Thử mô-men giữ thật khi phanh còn kẹp (S3) rồi mới nhả (S3B) | SDD §5 (v1.1) | L (chờ DV-02) |
| FM-04 | Khóa chéo `dir` khi $\lvert v\rvert > 0.002$ | SDD §5.3; KT-25 | L (chờ DV-02) |
| FM-05 | $k_{dt}$ = 3.61; TF động cơ | KT-07 | L |
| FM-06 | $i_{sq,\lim}$ = 3.86 A; $k_{\text{bám}}$ = 1.516 | KT-02, 03 | L |
| FM-07 | Không áp dụng (QĐ-07): không xét dừng khẩn/mất điện; $M_B$ = 7 N·m ∈ [5.94; 10.12] | KT-27, 28 (KT-29: Không áp dụng) | — |
| FM-08 | `SRS-D03` dùng $i_{\text{thực}}$ = 155.34 | KT-31 Đạt (+1.1%) | L |
| FM-09 | $J_{tune} = J_{rig}$, $T_{\Sigma\omega}$ kể trễ vòng tốc độ rời rạc; PM ≥ 31.6° | KT-23, 24 | L (chờ DV-06) |
| FM-10 | ICD v1.0; bảng §6 SDD | Checker K9 | L |
| FM-11 | Chọn biến tần theo $1.5I_{Hd}$ | KT-11, 12 | L |
| FM-12 | Không áp dụng (QĐ-07): không xét sự cố phanh | — | — |
