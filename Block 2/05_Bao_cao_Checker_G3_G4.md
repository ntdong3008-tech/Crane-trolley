# BÁO CÁO RÀ SOÁT — KIỂM KHỚP K6–K12 CHO CỔNG G3 (KHỐI 2) VÀ G4 (KHỐI 3)

> **Nguồn:** lượt rà soát độc lập, chỉ đọc (`WORKFLOW_RULES.md` §1, §8, §9), chạy ngày 24/10/2026 trên các bản **v1.0**. Nội dung dưới đây được lưu **nguyên văn**. Phần xử lý của người soạn sau khi nhận báo cáo nằm ở **Phụ lục A** cuối tài liệu (người soạn không tự duyệt — nhóm duyệt tại cổng).

## 1. Phiên bản đã kiểm
- **Ngày kiểm:** 24/10/2026. Người rà soát chỉ đọc, chạy lượt riêng, không sửa file nào.
- **Baseline đối chiếu:** `SSoT-8.5EMG-v1.2` (P-01..P-20), `SRS Baseline A v1.2`, `02_Boundary_va_P_Diagram.md`, `RTM-DVP v1.2`, `SOW v1.2` (SOW-2.x/3.x, QCD-Q02/Q03/Q04/C01).
- **Khối 2 (G3):** `01_SAD_..._v1.0`, `02_ICD_..._v1.0`, `03_BOM_So_bo_3_cap_v1.0`, `04_DFMEA_L1_v1.0`.
- **Khối 3 (G4):** `00_Tinh_toan_Xe_con_x2_v1.0.xlsx`. Sheet Info ghi "v1.0 — 24/10/2026". Người rà soát đọc file 2 lần: lấy công thức và lấy giá trị cache, `sel = 1`. Các tài liệu kèm theo: `01_Thuyet_minh_..._v1.0`, `02_So_do_Mach_luc_va_BOM_Chinh_thuc_v1.0` (+ `.svg`), `03_SDD_..._v1.0`, `04_SRS_A1_..._v1.0`.
- **Simulink / `init_params.m`:** chưa có (thuộc G5).

## 2. Ma trận khớp

| PRD | SRS (+Downstream/SRS-Dxx) | Phân hệ (K2) | Thiết kế (K3) | DV | Report |
|---|---|---|---|---|---|
| PRD-FUNC-01 | SRS-FUNC-01; #4 → D09 | SS-4 P; SS-2, SS-5 c | SDD §4.2, §5.4 | DV-01, DVP-SS-01 | A: KT-22 Đạt; S: chưa chạy |
| PRD-FUNC-04 | SRS-FUNC-02; #5 → D10, D11; D13 | SS-4 P (FSM); SS-5 | SDD §5; Thuyết minh §8.2 | DV-02, DVP-SS-04 | A: KT-27/28/30 Đạt, KT-29 Không đạt có chủ đích; S: chưa chạy |
| PRD-FUNC-02 | SRS-FUNC-03; D06; #8 → D12 | SS-4 | SDD §3 | DV-03, DVP-SS-03 | A: KT-18..20 Đạt; S: chưa chạy |
| PRD-FUNC-03 | SRS-FUNC-04; #3 → D05 | SS-2, SS-3 | Thuyết minh §8.1; DWG | DV-04, DVP-SS-05 | A: KT-13..17 Đạt; S: chưa chạy |
| PRD-PERM-01 | SRS-PERM-01; #6 → D01; #7 → D02 | SS-5, SS-6 | Thuyết minh §1, §5 | DV-05, DVP-SS-06 | A: KT-02..06 Đạt; S: chưa chạy |
| PRD-PERM-02 | SRS-PERM-02; #1 → D07; #2 → D08; D03 | SS-4, SS-6 | SDD §4.3; Thuyết minh §2, §6 | DV-06, DVP-SS-02/07 | KT-31 TBD; S: chưa chạy |
| PRD-PERM-03 | SRS-PERM-03; D06 | SS-4, SS-6 | SDD §3.4 | DV-07, DVP-SS-08 | A: KT-21 (tham khảo); S: chưa chạy |
| PRD-PERM-04 | SRS-PERM-04 (A.1 chờ ký); D02, D04 | SS-2, SS-5 | Thuyết minh §4, §5, §7 | DV-08 | A/I: KT-07 Đạt, KT-08 Không đạt (đã có QĐ-02) |

Không có ô **trống** ở chiều xuôi. Cột Report cho phương pháp S: **chưa chạy**.

## 3. Danh sách cảnh báo

### K6 — Số liệu/đơn vị so với SSoT
**Kết quả tốt (nói ngắn):**
- Các giá trị Q, M_Σ, m_tĩnh, h, v_max, a_max, ρ_max, D_bx, w₀, φ, η, F_c = 2,096 N, S3-40%, 380 V/50 Hz khớp tuyệt đối giữa Params, SAD, ICD, BOM, Thuyết minh và SDD.
- Không nhầm w₀ với φ.
- Người rà soát tự tính lại độc lập (Python), tất cả khớp Excel và văn bản: F_max 9,218 N; k_bám 1.516 (đầy và không tải); i_yc 157.08/158.72; M_max 10.741/12.728 N·m; M_max/M_N 2.170/1.768; M_đt 1.3633/1.3750 N·m; k_dt 3.648/5.250; I_đỉnh 3.293/3.978 A; P_dc,hãm 436.5 W; cửa sổ R_h [99; 428] Ω (U²/P = 1,123 Ω); cửa sổ M_B [2.32; 10.01] N·m, không tải 1.42; 5 tham số ĐC cho cả 2 ứng viên; K_p,I 108.36 V/A, T_i,I 5.55 ms; K_p,ω 0.7053, T_i,ω 7 ms; PM 34.68° ở cả 2 trạng thái tải; κ = 3.18 cho PM 29.50°.
- Các bảng WC-1..WC-7 cũng khớp khi tính lại.

**Cảnh báo:**
- ⚠ **K6-1 — Điện áp DC-link danh định lệch nhau.**
  - ICD IF-05 (`02_ICD`) ghi: "$U_{dc,0} \approx 1.35\,U_{\text{lưới}}$ = [462; 564] V".
  - Excel `'Tính chọn'!D84` dùng `=SQRT(2)*Params!$C$20*(1+...)` → 591 V; Thuyết minh §9 ghi 537 / 484 V; SVG ghi "DC+ (U_dc ≈ 540 V)".
  - Hai hệ số (1.35·U và √2·U) cho hai dải khác nhau.
  - Hướng sửa: chọn một định nghĩa (√2·U khi không tải, 1.35·U khi có tải) rồi đồng bộ ICD, SVG và Excel.
- ⚠ **K6-2 — Gốc điện áp động cơ 400 V chưa quy về lưới 380 V (P-19).**
  - `GiaDinh_K3`: "U_N | 400 | V | DRN 400 V/50 Hz". `'Tính chọn'!D36` = λ_K·(1−0.1)² = 2.754. ICD IF-04 ghi "$U_1 \in [0; 400]$ V; $f_1 \in [0; \approx 52]$ Hz". SDD §4.1 ghi "không giảm từ thông vì $f_1 \le 52$ Hz".
  - Hệ số 0.9² lấy theo 380 V, nhưng động cơ định mức 400 V. Lưới thấp nhất 342 V so với 400 V cho λ khả dụng = 3.4·(342/400)² = **2.485**. Biên ở WC-5 giảm từ 1.14 xuống **1.03**.
  - Biến tần cấp từ 380 V không xuất được 400 V ở khoảng 50–52 Hz, nên gần v_max hệ sẽ bị giới hạn điện áp.
  - Hướng sửa: nêu rõ gốc điện áp, tính lại KT-05 và WCCA (xem K11-7).
- ⚠ **K6-3 — Gia tốc phanh cơ bỏ qua quán tính quay.**
  - Thuyết minh §8.2 ghi "0.64 / 1.13 m/s²" và "Quãng dừng khẩn … 17.3 mm". Công thức `'Tính chọn'!D89` = (F_B + F_c)/M_Σ, không có δ và J_BMot.
  - Cách làm này không nhất quán với M_max (có kể δ và J_B). Tính lại có quán tính: a_B ≈ 0.44 m/s², s_B ≈ 22.3 mm.
  - Không làm hỏng SRS-FUNC-02 (Δs chỉ tính sau khi đóng phanh), nhưng con số chưa bảo vệ được.
  - Hướng sửa: dùng chung quy ước δ·M + J_B/k².
- ⚠ **K6-4 — Bảng WCCA không nằm trong Excel.**
  - Thuyết minh dòng 9 ghi: "Mọi số dưới đây là **kết quả công thức Excel**". Nhưng bảng §9 WC-1..WC-7 (và doc 04 §6) không có trong sheet nào. Cột ứng viên 2 (sel = 2) cũng không có giá trị cache.
  - Trái quy tắc §6.2. Số tính lại thì đúng.
  - Hướng sửa: thêm khối/sheet `WCCA` bằng công thức.
- ℹ **K6-5 — Mô-men pha giảm tốc dùng quy ước "kéo".**
  - Thuyết minh §4 ghi "$M_c - M_{đg}$ = **−6.15**", tức chia η thay cho M_c,hãm (nhân η) của §4.2-B4.
  - Thiên về an toàn cho tính nhiệt. Nên ghi chú lý do.

### K11 — Xung đột thiết kế
1. ⚠ **XUNG ĐỘT k_dt (đã nêu và đã có quyết định QĐ-02).** KT-08 trả về "Không đạt (XUNG ĐỘT đã trình QĐ-02)" với k_dt = 3.65. A.1 CR-01/CR-02 vẫn "chờ ký duyệt".
   - Lỗ hổng còn lại: nhật ký CR chưa liệt kê **QCD-Q02** ("$k_{dt} \in [1.20;\ 1.50]$"), mệnh đề k_dt trong **SOW-3.1**, và WORKFLOW §3/§5.
   - Phương án: (a) bổ sung các mục này vào CR-01/CR-03; (b) giữ nguyên và ghi độ lệch.
2. ⚠ **SOW-3.1 ghi "chọn dải $1.5 \div 2.2$ kW", còn thiết kế chọn 0.75 kW** (CR-03, chờ nhóm xác nhận).
3. ⚠ **QCD-C01 ghi "không vượt quá 150% công suất tính toán yêu cầu".** Có 2 cách hiểu: so với P_đt 0.206 kW thì 0.75 kW bằng 364% (vi phạm); so với P_max 1.23 kW thì bằng 61% (đạt). KT-09 chỉ kiểm trần 2.2 kW.
   - Phương án: nhóm chốt cách hiểu, hoặc đưa vào CR.
4. ⚠ **P-16: i = 150 so với i_yc = 157.08** (Δv = +4.72%, sát ngưỡng ±5%). i_thực của SEW vẫn TBD (KT-31). CR-04 đã ghi nhận. Cần bảng tổ hợp SEW trước khi khóa.
5. ⚠ **KT-29 "Không đạt — trượt khi phanh khẩn không tải".** Mâu thuẫn vật lý: giới hạn không trượt khi không tải là 1.42 N·m, nhỏ hơn mức tối thiểu 2.32 N·m.
   - Phương án: (a) nhóm chấp nhận rủi ro tồn dư với SS1; (b) phanh 2 cấp hoặc phanh điều khiển được; (c) tăng k_dẫn (dẫn động 4 bánh).
6. ⚠ **Phanh BE2 của ứng viên 2:** "cấp đã xác minh 14 / 20 N·m [W-03] > giới hạn không trượt 9.9 N·m" (doc 02). Nếu chọn sel = 2 thì xung đột. Lưu ý thêm: [W-03] là phụ lục cho động cơ 2/6 cực (xem K12).
7. ⚠ **Mới, người soạn chưa nêu: động cơ 400 V trên lưới 380 V ±10%** (xem K6-2).
   - Phương án: (a) xác minh SEW có cuộn dây 380 V/50 Hz cho DRN80M4; (b) tính lại λ theo (U_min/U_N)²; (c) chấp nhận giảm từ thông gần v_max và đưa vào DVP-SS-06; (d) chuyển sang DRN90S4.
8. ℹ Ngưỡng chopper 700/780/800 V chưa đối chiếu firmware ACS380 (người soạn đã gắn nhãn `chưa xác minh`).
9. ℹ P-03 m_xc = 1,800 kg vẫn chưa có catalogue đối chứng (câu hỏi mở số 1 của SSoT). WC-3 (+20%) mới chỉ bao một phần.

### K7/K8 — Phân bổ và yêu cầu dẫn xuất
- **Kết quả tốt:** 8/8 SRS và 8/8 Downstream đều có phân hệ chủ trì P (SAD §4), có thiết kế ở Khối 3 và có DV.
- ⚠ **K7-1 — Thứ tự nhả phanh trong FSM.**
  - SDD §5.2 ghi "S3_TORQUE_PROVE --> S4_RUN: torque_ok ∧ t ≥ t_open (brake_cmd = 1 từ khi vào S3)". Công thức `torque_ok` chỉ kiểm khả năng ($k_M i_{sq,\lim}\psi_r/\psi_r^* \ge M_{hold}$).
  - SRS-FUNC-02 và IF-06 Khối 1 yêu cầu "chỉ mở phanh khi động cơ đã sinh đủ mô-men giữ"; Downstream #5 yêu cầu M_hold(0 rpm) ∈ [100; 150]%. Thiết kế hiện tại nhả phanh trước khi xác nhận mô-men thực.
  - Hướng sửa: cho phát mô-men thử M_hold khi phanh còn kẹp, đo i_sq, rồi mới đặt brake_cmd = 1. Đây là lựa chọn của nhóm (câu hỏi 3).
- ⚠ **K7-2 — Tiêu chí PASS của DVP cấp phân hệ còn thiếu.**
  - DVP-SS-04 chỉ có "Không đổi `dir` khi |v| > 0.002", thiếu ngưỡng đóng phanh 0.005 m/s và M_hold.
  - Chưa DVP nào kiểm v_creep ∈ [0.030; 0.036] (DVP-SS-03 chỉ kiểm a*, ρ*).
  - DV-08 yêu cầu kiểm nhiệt ở 342 V, nhưng Excel chỉ tính ở điện áp danh định.
- ⚠ **K8-1 — Yêu cầu cha của SRS-D02 không khớp.** Excel `'Dẫn xuất'!E3` = "SRS-PERM-01", còn doc 04 ghi "SRS-PERM-01, -04". Mã này gắn DV-08, mà DV-08 lại thuộc SRS-PERM-04.
- ℹ **K8-2 — Mã con chưa được khai báo quy ước.** Excel dùng D04a/b, D05a/b/c, D06a/b, D07a/b, D09a/b, D11a/b; doc 04 dùng D04..D11 không tách; Thuyết minh/SDD trích D05a, D05c, D06a, D11b. Nên ghi quy ước mã con trong doc 04 §2.
- ℹ **K8-3 — Hằng số và ngưỡng chưa có nguồn.** `'Dẫn xuất'!C14` gõ số 0.05. Ngưỡng PM ≥ 30° (KT-23/24) chưa có yêu cầu cha; nên định danh thành SRS-Dxx hoặc đánh dấu [C].
- ℹ **K8-4 — Công thức K_p,ω lệch §4.2-D2 có lý do.** người soạn dùng J_tune thay J_Σ (SDD §4.3 đã giải thích). Nên ghi đây là bước dẫn xuất.

### K9 — Giao diện ICD
- ⚠ **Tên biến `J_mot` mơ hồ.** Bảng init SDD §6 ghi `J_mot` = 26.2e-4, nhưng đó là J_BMot. Catalogue C14 "J_Mot" = 24.7e-4. ICD chưa định nghĩa biến này.
- ⚠ **Thiếu `reset` trong ICD IF-02.** ICD chỉ có "`cmd_fwd`, `cmd_rev`, `cmd_fast`, `cmd_stop`, `estop`", trong khi FSM dùng RESET và SVG/BOM có nút "DI5 RESET".
- ⚠ **IF-04 "0–400 V"** không đạt được từ lưới 380 V (xem K6-2).
- ℹ Biến `Ts_ctrl` (IF-12) không có trong SDD/Excel, vốn dùng `Ts_w` và T_s,I. Biến `ramp_enable` (IF-14) không được SDD sử dụng.
- ℹ Bảng init SDD §6 có nhiều tên chưa có trong ICD §4 (`M_full`, `i_gear`, `delta`, `pp`, `Kp_i`…) trong khi ICD tuyên bố "là tên duy nhất được phép". Nên nâng ICD lên v1.1.
- ℹ Mâu thuẫn thời gian giữ: SDD §5.2 ghi "t ≥ t_close + 0.05 s", còn §5.5 ghi "giữ ω* = 0 thêm 0.1 s". Ký hiệu a* vừa dùng cho trạng thái vừa dùng cho giới hạn (ICD gọi giới hạn là `a_set`).

### K10 — Mô phỏng và phiên bản
- **Kết quả tốt:** không có kết quả mô phỏng nào bị khẳng định. "chưa chạy" được ghi đúng ở SDD, doc 04 §3/§4, Excel KT-32. AP₁ trong DFMEA được ghi là "dự kiến".
- ℹ Không tài liệu nào có bảng **lịch sử phiên bản** (chỉ có v1.0 + ngày). Doc 04 §1 có nhật ký CR; ICD §6 có quy định kiểm soát thay đổi.
- ℹ Khối 3 được lập khi G3 chưa duyệt (Thuyết minh tự nêu). Cần duyệt G3 trước hoặc cùng lúc với G4.

### K12 — Nguồn trích dẫn
- **Kết quả tốt:** rà soát kiểm tra PDF và xác nhận đúng các khẳng định của người soạn về lỗi trích dẫn trong baseline:
  - `A54.pdf` là bài Valtchev et al., IEEE DAS 2024 (6 trang), không có DIN 536 hay w₀.
  - [R4]: tr.23 là phần IEC cho động cơ; tr.85–92 là nội dung EMC; toàn văn không có chuỗi "61800".
  - Bài 2.1 slide 26–29 là MO/SO. Bài 2.3 là FOC cho ĐC KĐB (slide 33, 37 mạch vòng dòng; slide 56, 58 hãm). Bài 3 là "Tải của TĐĐ". Bài 4 là "Phương pháp thiết kế" (slide 43–44 truyền động xe con).
  - TCVN 4244 là bản scan, gần như không trích được chữ.
  - [R9-07] tr.4, tr.8, tr.9 (khoảng cách ray 1,400/2,240/2,800 mm) đúng.
- ⚠ Các PDF [W-01..W-05] **chưa lưu** vào `Tài liệu tham khảo/`, nên rà soát không đối chiếu được trị số catalogue. [W-01] lấy từ máy chủ bên thứ ba (kheoos), nên thay bằng bản chính hãng SEW.
- ⚠ [W-03] là phụ lục "2- and 6-pole", nhưng được dùng làm căn cứ cấp mô-men BE2 cho động cơ 4 cực DRN90S4. Cần nguồn đúng loại.
- ⚠ Trạng thái nguồn biến tần lệch nhau: BOM sơ bộ L3-04 ghi "XM [W-05]", còn BOM chính thức U1 ghi "XM\*" (bảng trích lệch cột).
- ℹ Các mục chưa có mã [W] hoặc chưa kiểm được: ACS380 HW manual 3AXD50000029274 (không có mã [W]); mã BTAC-02 3AXD50000022163; f_sw 1–12 kHz; "Danotherm 210R"; "Torque step rise time < 10 ms". Các mục BE1 5 N·m, R1, G1 và hộp số đã được gắn đúng nhãn CXM/TBD.

## 4. Giả định [C] / TBD / chưa chạy / chưa xác minh
- **[C] của SSoT:** P-03, P-12, P-13, P-14, P-15, P-16, P-17, P-18, P-19. Nguồn của w₀ và D_bx thực tế chưa có trong kho.
- **[C] phát sinh ở Khối 3 (`GiaDinh_K3`):** δ = 1.15; k_dẫn = 0.5; chu trình n_ht = 2 (L_ht = 14.34 m); a* = 0.45; ρ* = 1.8; η_inv = 0.97; k_p = 1.25; t_close = 0.05 s; t_open = 0.10 s; t_mag = 0.5 s; k_μ = 1.5; T_fω = 1 ms; T_s,ω = 1 ms; k_Fe = 0.3; k_σ = 0.5; ζ = 0; T_f = 5 ms; r_creep = 0.275; J_tune.
- **TBD:** i_thực (KT-31); cỡ hộp số và M_a,max; QF1, KM1, K2, S1–S6; điện áp cuộn phanh; G1.
- **Chưa xác minh:** cấp BE1 5 N·m; công suất và mã R1; bảng định mức ACS380 (XM\*); ngưỡng chopper trong firmware; J_BMot; 5 tham số ĐC (cần ID-run); điện áp cuộn dây động cơ 380 V hay 400 V; thuật ngữ IEC 61800-2 (PDS/BDM/CDM); các điều khoản TCVN; quy tắc AIAG–VDA.
- **Chưa chạy:** DV-01..07 (S), DVP-SS-01..08, KT-32. A.1 (CR-01..04) chưa ký duyệt.

## 5. Kết luận
- **G3 (Khối 2): Mức khớp: Có chỗ lệch** (mức nhẹ). Kiến trúc, phân bổ K7 và DFMEA (AP và RPN tính đúng) đều tốt. Phần lệch nằm ở ICD (U_dc, IF-04 0–400 V, thiếu RESET) và nguồn [W] chưa lưu, [W-03] dùng sai loại động cơ.
- **G4 (Khối 3): Mức khớp: Có chỗ lệch.** Số liệu và công thức khớp và tính lại đúng. Phần cần xử lý trước khi khóa: gốc điện áp 400 V so với 380 V, WCCA ngoài Excel, gia tốc phanh, thứ tự nhả phanh trong FSM, yêu cầu cha của SRS-D02. Các xung đột đã biết (k_dt, SOW-3.1, KT-29, i_thực) vẫn chờ nhóm quyết định.

## 6. Câu hỏi cho nhóm tại cổng
1. Động cơ DRN80M4 định mức 400 V chạy trên lưới 380 V ±10%: nhóm sẽ xác minh cuộn dây 380 V/50 Hz, chấp nhận tính lại λ theo (342/400)² (biên WC-5 còn khoảng 1.03), hay chuyển sang DRN90S4?
2. Khi ký A.1, có mở rộng CR-01/CR-03 sang QCD-Q02 và mệnh đề k_dt của SOW-3.1 không? Hiểu "150% công suất tính toán" trong QCD-C01 là so với P_đt hay P_max? Có chấp nhận rủi ro tồn dư KT-29 với biện pháp SS1 không?
3. Bước TORQUE_PROVE: giữ như thiết kế (chỉ kiểm khả năng, nhả phanh ngay khi vào S3), hay bắt buộc phát mô-men thử M_hold khi phanh còn kẹp rồi mới nhả, theo đúng câu chữ của SRS-FUNC-02 và IF-06?

---

## PHỤ LỤC A — PHẢN HỒI CỦA NGƯỜI SOẠN (24/10/2026, sau lượt rà soát)

> người soạn không tự duyệt: các mục "Đã sửa" dưới đây **chưa được rà soát kiểm lại** (cần một lượt rà soát v1.1 trước khi nhóm ký cổng).

| Cảnh báo | Xử lý | Vị trí |
| :--- | :--- | :--- |
| K6-1 $U_{dc}$ | Đã sửa: quy ước không tải $\sqrt{2}U$ = [484; 591] V (danh định 537 V), có tải $1.35U$ = [462; 564] V; Excel thêm ô `Udc_ld` | ICD v1.1 IF-05; Excel `Tính chọn` H; SVG |
| K6-2 / K11-7 (400 V trên lưới 380 V) | Đã sửa tính toán: $\lambda$ khả dụng = $\lambda_K(342/400)^2$ = 2.485 ≥ 2.17 (biên 1.15; WC-5 còn 1.03). **Lựa chọn thiết bị (cuộn 380 V / DRN90S4) để nhóm quyết** | Excel v1.1; Thuyết minh §5, §9; ICD IF-04; DVP-SS-06 |
| K6-3 gia tốc phanh | Đã sửa: kể $\delta M$ và $J_B/(k^2\eta)$ → $a_B$ = 0.566 m/s², $s_B$ = 18.7 mm (với $M_B$ = 7 N·m) | Excel `Tính chọn` I; Thuyết minh §8.2 |
| K6-4 WCCA ngoài Excel | Đã sửa: thêm sheet `WCCA` (8 kịch bản, công thức), file đổi tên `00_Tinh_toan_Xe_con_x2_v1.1.xlsx` | Excel v1.1 |
| K6-5 quy ước mô-men giảm tốc | Ghi chú lý do (an toàn cho tính nhiệt) | Thuyết minh §4 |
| K7-1 thứ tự nhả phanh | Đã sửa theo câu chữ SRS-FUNC-02: S3 phát và đo $M_{hold}$ khi phanh còn kẹp, S3B mới nhả phanh. Hệ quả: $M_B \ge 1.2M_{hold}$ = 5.94 N·m → $M_B$ = 7 N·m. **Nhóm đã chốt giữ bước thử (QĐ-05, 24/10/2026)** | SDD v1.1 §5; Excel; SRS-D10, D13 |
| K7-2 tiêu chí DVP | Đã bổ sung PASS cho DVP-SS-03 (mức bò), DVP-SS-04 (ngưỡng 0.005, $M_{hold}$, $\Delta s$), DVP-SS-06 (nhiệt ở 342 V) | Doc 04 §4 |
| K8-1 cha SRS-D02 | Đã sửa: "SRS-PERM-01, SRS-PERM-04" | Excel `Dẫn xuất` |
| K8-2 mã con | Đã ghi quy ước `SRS-Dxxa/b/c` | Doc 04 §2 |
| K8-3 hằng số | `e_xl,max` và `PM_min` đưa vào `GiaDinh_K3` | Excel |
| K8-4 $J_{tune}$ | Đã giải thích ở SDD §4.3 (bước dẫn xuất) — giữ nguyên | — |
| K9 tên biến | Đã sửa: `J_Bmot`, `cmd_reset`, bỏ `ramp_enable`, `Ts_ctrl` → `Ts_I`, thời gian giữ thống nhất 0.1 s, đăng ký tên biến ICD v1.1 §4.1 | ICD v1.1; SDD v1.1 |
| K10 lịch sử phiên bản | Đã thêm dòng lịch sử ở Excel (Info), ICD, Thuyết minh, SDD, doc 04 | — |
| K11-1, K11-3 | CR-01 mở rộng sang QCD-Q02 và SOW-3.1; cách hiểu QCD-C01 **đã chốt: so với $P_{\max}$ (QĐ-08, 24/10/2026)** | Doc 04 §1 |
| K11-5 KT-29 | **Không áp dụng (QĐ-07, 24/10/2026)**: đồ án chỉ xét điều kiện vận hành lý tưởng (không mất điện, không dừng khẩn); thay thế QĐ-06 | Thuyết minh §8.2; doc 04 CR-07 |
| K12 nguồn web | BOM sơ bộ L3-04 đổi thành XM\*; ghi chú [W-03] là bảng 2/6 cực; việc lưu PDF [W-01..05] và thay [W-01] bằng bản SEW là **việc của nhóm** | BOM sơ bộ, BOM chính thức §3 |

---

## PHỤ LỤC B — ĐÓNG CỔNG (24/10/2026)

- **G3 (`PDR-EVT`) đã đóng:** nhóm duyệt kiến trúc 1 động cơ đặt giữa dẫn 2 bánh qua trục ngang, encoder SEW ES7C.
- **G4 (`CDR-EVT`) đã đóng:** nhóm ký **SRS Baseline A.1** (CR-01..CR-07) cùng các quyết định QĐ-04 (DRN80M4 + ACS380-04xS-03A3-4, biên quá tải 1.03), QĐ-05 (thử mô-men giữ, $M_B$ = 7 N·m), QĐ-07 (phạm vi vận hành lý tưởng), QĐ-08 (QCD-C01 so với $P_{\max}$).
- **Ghi chú trung thực:** các sửa đổi ở Phụ lục A (bản v1.1) **chưa có lượt rà soát kiểm lại**; nhóm quyết định đóng cổng trên cơ sở báo cáo này. Các mục TBD còn mở được mang sang Khối 4: $i_{\text{thực}}$ hộp số SEW, cấp mô-men BE1, mã/công suất $R_h$, QF1/KM1, lưu PDF `[W-01..W-05]`.

---

## PHỤ LỤC C — ĐÓNG CÁC MỤC TBD CATALOGUE (25/10/2026)

- $i_{\text{thực}}$ = **155.34** — hộp số SEW **R87** (`[W-06]` SEW Drive Selection); $M_{a,\max}$ 1,550 N·m ≥ 1,286 N·m (KT-33 Đạt); sai lệch vận tốc ở 50 Hz +1.1% (KT-31 Đạt).
- Phanh **BE1 cấp 7 N·m** có trong danh mục 10/7/5 N·m (`[W-07]`); BE2 có cấp 7/10 N·m → hết cảnh báo K11-6.
- $R_h$: **Danotherm CBH 360 C T 406 210R**, 200 W (`[W-05]` tr.24, `[W-09]`); bảng định mức ACS380 đối chiếu ảnh trang gốc (`[W-05]` tr.12) → U1 chuyển từ XM\* sang XM.
- Bảo vệ đầu vào: cầu chì **gG 6 A OFAF000H6** (`[W-08]`); KM1: **ABB AF09-30-10-13** (`[W-10]`).
- PDF/ghi nhận nguồn lưu tại `Tài liệu tham khảo/Catalogue web/` (bản gốc SEW của [W-01] trả về 403 — giữ bản trích 1 trang).
- Ảnh hưởng tính toán (Excel v1.2, 0 lỗi): $M_{\max}/M_N$ 2.17 → 2.19; biên quá tải WC-5 1.03 → **1.02**; $k_{dt}$ 3.65 → 3.61; $K_{p,\omega}$ 0.705 → 0.714 A·s/rad; PM 34.6°. Các thay đổi này **chưa có lượt rà soát kiểm lại**.
