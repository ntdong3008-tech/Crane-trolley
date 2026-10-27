# BÁO CÁO CHECKER — KIỂM KHỚP K6–K12 CHO EXCEL v1.4 VÀ 4 TÀI LIỆU SỬA NGÀY 27/10/2026

> Lượt Checker độc lập, chỉ đọc (`WORKFLOW_RULES.md` §1, §8, §9). Không sửa file nào trong thư mục dự án. Mọi số dưới đây lấy từ file thật hoặc do Checker tự tính lại bằng Python; mục nào không kiểm được thì ghi rõ.

## 1. Phiên bản đã kiểm

- **Ngày kiểm:** 27/10/2026.
- **Baseline đối chiếu:** `SSoT-8.5EMG-v1.2` (P-01..P-20), `SRS Baseline A v1.2` và A.1 (CR-01..07), các quyết định QĐ-01..08 và nhóm C (duyệt 26/10/2026). Các mục đã chốt không bị báo là lỗi.
- **Excel:** `Block 3/00_Tinh_toan_Xe_con_x2_v1.4.xlsx` (Info A3: "v1.4 — 27/10/2026 … chưa qua Checker"), đối chiếu với `…_v1.3.xlsx`.
- **Cách đọc Excel:** chép cả hai file vào `scratchpad\checker\in\`. Đọc công thức và giá trị bằng openpyxl. Tính lại cả hai bản sao bằng Microsoft Excel qua COM (`CalculateFull`) rồi lưu thành `v13_calc.xlsx` và `v14_calc.xlsx`.
  - v1.4: **0 ô lỗi `#…`** trên 11 sheet. Giá trị cache gốc khớp 100% với giá trị Excel tính lại (2,627 ô công thức, **0 ô lệch**), nên cache là thật.
  - v1.3: 0 ô lỗi sau khi tính lại. File gốc v1.3 không có cache.
- **Tài liệu đã kiểm:**
  - `Block 3/01_Thuyet_minh_Tinh_chon_Phan_luc_v1.0.md` (dòng 5, dòng 13, §8.1 dòng 150–170)
  - `Block 3/03_SDD_Thiet_ke_Dieu_khien_va_Logic_v1.0.md` (dòng 5)
  - `Block 2/02_ICD_Kiem_soat_Giao_dien_v1.0.md` (dòng 86, §4.1)
  - `README.md` (dòng 47–49)
  - Đối chiếu chéo thêm: SAD, BOM chính thức, doc 04 SRS-A1, danh mục `[W-09]`.
- **Simulink / `init_params.m`:** chưa có (thuộc Khối 4). Không có kết quả mô phỏng nào để kiểm.

## 2. Diff v1.4 so với v1.3 (công thức và giá trị)

Checker so từng ô trên toàn bộ vùng dữ liệu của mọi sheet chung. So cả chuỗi công thức lẫn giá trị sau khi Excel tính lại. Danh sách dưới đây là **đầy đủ**.

| Sheet | Ô | Thay đổi | Có trong khai báo? |
|---|---|---|---|
| Info | A3, A4, A17, A21 | Sửa nội dung (phiên bản, lịch sử, mô tả khối S, cột G của Mo_phong) | Có |
| Info | A22, A23 | Chèn 2 dòng mới (mô tả Tong_hop, Quy_dao) | Có |
| Info | A24–A46 | Nội dung cũ A23–A44 **dời xuống 2 dòng**, giống hệt bản cũ (đã kiểm) | Hệ quả của chèn dòng, không khai báo riêng |
| GiaDinh_K3 | A59 (tiêu đề), A60:G60 | `P_Rh` = 200 W, nguồn `[W-09]` | Có |
| Tính chọn | D81 | `$D$18^2` → `$D$191^2`; giá trị 147.7292 → **147.0730** J | Có |
| Tính chọn | F81 | Thêm ghi chú "ω_m tại v_max (D191); v1.3 dùng ω_N (sửa v1.4)" | Đi kèm D81, không khai báo riêng |
| Tính chọn | D82, D83 | Công thức không đổi. Giá trị 59.8898 → **59.4149** J; 0.19963 → **0.19805** W | Có |
| Tính chọn | A232:G236 | Khối S (tiêu đề và 4 dòng: F_hãm,δ; P_dc,hãm,δ; 2 tỷ số biên) | Có |
| Kiểm tra | C40 (KT-39) | Công thức không đổi; giá trị 59.89 → 59.41 (kết quả vẫn "Đạt") | Hệ quả của D82, không khai báo riêng |
| Kiểm tra | **E41 (KT-40)** | Chuỗi công thức đổi `1E-9` → `0.000000001` (2 chỗ). Tương đương về toán; kết quả không đổi | **Không** khai báo |
| Kiểm tra | A43:G44 | KT-42, KT-43 mới | Có |
| Mo_phong | G1:G76 | Cột G mới (tiêu đề + 75 dòng công thức) | Có |
| WCCA | B15:I15 | Bọc `MAX(0,·)`; 8 giá trị không đổi (đều dương) | Có |
| Tong_hop, Quy_dao | — | Sheet mới (Quy_dao có 2 biểu đồ) | Có |

**Không thay đổi:** Params, Catalogue, Dẫn xuất; Tính chọn ngoài D81:D83 và khối S; Kiểm tra ngoài C40, E41 và hàng 43–44; cột A–F của Mo_phong; WCCA ngoài hàng 15. Số hiệu KT-01..KT-41 giữ nguyên. Tên biến trong cột B của Mo_phong giữ nguyên.

**Kết luận diff:** lời khai "không đổi số nào khác" của Writer **đúng về giá trị**. Có 4 điểm ngoài danh sách khai báo, đều không làm đổi kết quả:
1. Kiểm tra!E41: chuỗi công thức `1E-9` đổi thành `0.000000001`.
2. Kiểm tra!C40 đổi giá trị theo D82.
3. Tính chọn!F81 có thêm ghi chú.
4. Info A24–A46 dời dòng.

Ngoài ra, v1.4 được lưu bằng Excel (có cache, `calcChain`, `sharedStrings`), còn v1.3 lưu không có cache. Đây không phải thay đổi nội dung.

## 3. Tính lại độc lập (Python, đầu vào gõ lại từ SSoT/GiaDinh/Catalogue)

Tất cả các đại lượng dưới đây khớp Excel với sai số tương đối dưới 1e-15.

| Đại lượng | Python = Excel | Ô |
|---|---|---|
| F_c | 2,096.0046 N | D5 |
| F_max | 9,218.0046 N | D10 |
| P_max | 1,229.07 W | D11 |
| k_qđ | 8.046865e-4 m/rad | D23 |
| M_c,kéo | 1.87403 N·m | D25 |
| M_max | 10.8249 N·m | D33 |
| M_max/M_N | 2.18685 | D35 |
| λ ở 342 V (quy về 400 V) | 2.48548 (biên 1.137) | D36 |
| M_đt | 1.37816 N·m | D58 |
| k_dt | 3.60886 | D60 |
| I_đỉnh | 3.31604 A | D71 |
| P_dc,hãm (§4.2-C4) | 436.488 W | D75 |
| U_chop²/P | 1,122.6 Ω | D76 |
| Cửa sổ R_h | [99; 428] Ω | D78, D77 |
| ω_m tại v_max | 149.1264 rad/s | D191 |
| E_đ | 147.0730 J | D81 |
| E_Rh | 59.4149 J (công thức v1.3 cho 59.8898 J, đúng với giá trị cũ) | D82 |
| P_Rh,tb | 0.19805 W | D83 |
| F_hãm,δ | 6,094.30 N | D233 |
| P_dc,hãm,δ | 724.486 W | D234 |
| P_BR,max / P_dc,δ | 1.5597 | D235 |
| (U²/R_h) / P_dc,δ | 3.2207 | D236 |
| Cửa sổ M_B | [5.94; 10.12] N·m | D88, D89 |
| K_p,I / T_i,I | 108.364 V/A / 5.5500 ms | D128, D129 |
| K_p,ω / T_i,ω | 0.714484 A·s/rad / 7.000 ms | D135, D136 |

WCCA: biên quá tải nhỏ nhất là 1.02365 (WC-5), khớp `Tong_hop!B55`.

## 4. Ma trận khớp

Ma trận này kế thừa từ báo cáo 05. Cột Report cập nhật theo `Kiểm tra` v1.4.

| PRD | SRS (+Downstream / SRS-Dxx) | Phân hệ (Khối 2) | Thiết kế (Khối 3) | DV | Report |
|---|---|---|---|---|---|
| PRD-FUNC-01 | SRS-FUNC-01; #4 → D09 | SS-4 | SDD §4.2 | DV-01 | A: KT-22 Đạt; S: chưa chạy |
| PRD-FUNC-04 | SRS-FUNC-02; #5 → D10, D11; D13 | SS-4 (FSM), SS-5 | SDD §5; Thuyết minh §8.2 | DV-02 | A: KT-25/27/28/30 Đạt, KT-29 Không áp dụng (QĐ-07); S: chưa chạy |
| PRD-FUNC-02 | SRS-FUNC-03; D06; #8 → D12 | SS-4 | SDD §3; Quy_dao (mới) | DV-03 | A: KT-18..20, KT-26 Đạt; S: chưa chạy |
| PRD-FUNC-03 | SRS-FUNC-04; #3 → D05 | SS-2, SS-3 | Thuyết minh §8.1; khối H, S | DV-04 | A: KT-13..17, KT-39, **KT-42** Đạt; S: chưa chạy |
| PRD-PERM-01 | SRS-PERM-01; #6 → D01; #7 → D02 | SS-5, SS-6 | Thuyết minh §1, §5 | DV-05 | A: KT-02..06, 11, 12, 33, 37 Đạt; S: chưa chạy |
| PRD-PERM-02 | SRS-PERM-02; #1 → D07; #2 → D08; D03, D14, D15 | SS-4, SS-6 | SDD §4 | DV-06 | A: KT-23, 24, 31, 35, 36 Đạt; S: chưa chạy |
| PRD-PERM-03 | SRS-PERM-03; D06 | SS-4, SS-6 | SDD §3.4 | DV-07 | A: KT-21 (tham khảo), KT-41 Đạt; S: chưa chạy |
| PRD-PERM-04 | SRS-PERM-04 (A.1); D02, D04 | SS-2, SS-5 | Thuyết minh §4, §5, §7 | DV-08 | A/I: KT-07, 09, 10, 38, **KT-43** Đạt; KT-08 Không áp dụng (CR-01) |

Không có ô **trống** ở chiều xuôi. KT-32 (DV-01..07, phương pháp S) ghi "TBD — Report: chưa chạy".

## 5. Danh sách phát hiện

Thứ tự theo §9.3: K6 → K11 → K7/K8 → K9 → K12, thêm K10. Không có mục nào ở mức **XUNG ĐỘT**.

### K6 — Số liệu và đơn vị so với SSoT

**Kết quả tốt:**
- Tong_hop trích đúng Q, m_nh, m_xc, h, v_max, a_max, ρ_max, S3-40%, F_c, F_max, P_max; tất cả bằng công thức trỏ về Params.
- Không nhầm w₀ với φ.
- Quy_dao dùng a* = 0.45 và ρ* = 1.8 (GiaDinh_K3 D11, D12) và v_max = 0.12 (qua T_j, T_a, t_acc ở D39..D41). Max |ρ| = 1.8, max |a| = 0.45, max v = 0.12000 (`Quy_dao!H4:H6`).
- Đơn vị của KT-42 (W/W), KT-43 (N·m/N·m) và khối S (W, tỷ số không thứ nguyên) đều đúng.

**Phát hiện:**
- **K6-1 — CẢNH BÁO (nhẹ). Câu "Mọi ô là công thức" chưa đúng nguyên văn.**
  - Vị trí: `Tong_hop!A2` và `Info!A22`.
  - Bằng chứng: Tong_hop có 57 ô công thức và 68 ô gõ tay ở cột B–E. Phần lớn là đơn vị, nhãn nguồn và mã KT (chấp nhận được). Nhưng một số ô gõ tay mang số SSoT hoặc ngưỡng:
    - `D23` = "3 pha 380 V ±10%" (P-19)
    - `D28` = "w₀ = 0.015 (không dùng φ)" (P-13)
    - `D36` = "≥ 1.20 (SRS A.1)"; `D37` = "≥ 1.20"
    - Tên thiết bị gõ tay: `B18` "SEW R87 (trụ đồng trục)", `B20`, `B22`, `B23`, `B24`
  - Vì sao lệch: trái §6.1 ("tuyệt đối không gõ lại số hằng"). Nếu SSoT hoặc A.1 đổi thì các ô này không tự cập nhật.
  - Đề xuất: sửa câu thành "mọi ô số liệu là công thức", hoặc ghép chuỗi từ `Params!C20`, `Params!C14` và ô ngưỡng của `Kiểm tra` (`D3`, `D8`).
- **K6-2 — GHI NHẬN. E_Rh cho năng lượng rotor đi qua hiệu suất hộp số.**
  - Vị trí: `Tính chọn!D82` = `(E_đ − F_c·s_acc)·η·η_đc·η_inv`.
  - Phần ½J_B·ω_m² nằm trên trục động cơ, không đi qua hộp số. Nếu không nhân η cho phần này thì E_Rh = 61.76 J thay vì 59.41 J.
  - Không đổi kết luận KT-39 (E_Rh > E_C = 15.46 J) hay KT-42. Đây là cách làm đã có từ v1.0, không phải lỗi mới của v1.4.
  - Đề xuất: ghi chú là gần đúng, hoặc tách η riêng cho từng phần.
- **K6-3 — GHI NHẬN. Quy_dao có 4 hằng gõ tay:** `B4` = 1 s (T_đều hiển thị), `B5` = 0.01 s (bước), `D14` = `E14` = 0 (điều kiện đầu). Đây là tham số hiển thị, không phải số SSoT, nên chấp nhận được. Nên ghi nguồn hoặc lý do ở cột C.

### K11 — Xung đột thiết kế

- **Không có XUNG ĐỘT mới.**
  - Khối S cho P_dc,hãm,δ = 724.5 W, tức **1.66 lần** giá trị 436.5 W theo §4.2-C4 (không kể δ và J_B). Biên vẫn đủ: P_BR,max/P_dc,δ = 1.56; (U²/R_h)/P_dc,δ = 3.22; U_chop²/P_dc,δ = 676 Ω > R_max = 428 Ω, nên cửa sổ R_h [99; 428] Ω và R_h = 210 Ω không đổi.
  - Checker tính thêm (không có trong Excel) cho tổ hợp hãm WC-7 có kể δ (w₀ = 0.012, η = 0.95): khoảng 792 W, vẫn dưới 1,130 W.
- **K11-1 — GHI NHẬN. Biên quá tải và giá trị SRS-D05b.**
  - P_dc,δ = 724 W chỉ dưới P_BRcont = 750 W (`Catalogue!F26`) với biên khoảng 1.04. Không phải điều kiện ràng buộc vì xung hãm chỉ dài khoảng 0.5 s.
  - `SRS-D05b` (`Dẫn xuất!C8` = 436.5 W) là giá trị **không bảo thủ** so với khối S. Nếu DV-04 dùng con số này làm ngưỡng PASS cho công suất hãm đo được trên Simulink (với `mech_model` = 1) thì có thể FAIL giả.
  - Đề xuất: ghi chú tại D05b hoặc DVP-SS-05 rằng ngưỡng là P_BR,max, không phải 436.5 W.

### K7 — Độ phủ phân bổ

- **Đạt.** KT-42 có cha SRS-FUNC-04, KT-43 có cha SRS-PERM-04; cả hai thuộc phân hệ đã có. 8/8 SRS và 8/8 Downstream vẫn được phủ.
- **K7-1 — GHI NHẬN (tồn từ v1.3, không do v1.4 gây ra). SRS-D14, D15 chưa có trong sổ đăng ký A.1.**
  - SRS-D14 và D15 (`Dẫn xuất!A22:A23`) chỉ xuất hiện ở ICD và SDD.
  - `Block 3/04_SRS_A1_…` không có D14 và D15. `README.md` dòng 54 vẫn ghi "SRS-D01..D13".
  - Đề xuất: bổ sung vào doc 04 §2 và README.

### K8 — Yêu cầu dẫn xuất

- **K8-1 — CẢNH BÁO. P_Rh = 200 W chưa được định danh SRS-Dxx.**
  - Vị trí: `GiaDinh_K3!D60` và `Kiểm tra!C43` (KT-42). `Dẫn xuất` chỉ có D05a (R_h = 210 Ω), D05b (P_dc,hãm 436.5 W), D05c (U_chop).
  - Bằng chứng: WORKFLOW §6.5 liệt kê rõ "giá trị R_h, P_Rh" phải nằm ở sheet `Dẫn xuất` kèm mã SRS-Dxx.
  - Đề xuất: thêm một mã con, ví dụ `SRS-D05d` (P_Rh ≥ P_Rh,tb; cha SRS-FUNC-04; KC: I/A; DV-04). Đồng bộ doc 04.
- **K8-2 — GHI NHẬN. Khối S thiếu ô "Nguồn công thức".**
  - Vị trí: `Tính chọn!G233:G236` = "Tự dẫn"; tiêu đề `A232` không trích nguồn, trong khi các khối khác đều có (§6.2).
  - Đề xuất: ghi "WORKFLOW §4.2-B4 (δ, J_B) + §4.2-C4".
- **K8-3 — Khối S không vi phạm §10.**
  - Công thức khóa §4.2-C4 vẫn nằm nguyên ở `D74`/`D75`. KT-15 (`Kiểm tra!D16` = `'Tính chọn'!$D$75/1000`), `Dẫn xuất!C8`, WCCA hàng 15 và Tong_hop B39 vẫn dùng D75.
  - Khối S chỉ là dòng tham khảo, được dán nhãn rõ (`F235`: "Chỉ tham khảo: KT-15 vẫn dùng D75 (công thức khóa)").
  - Không có số Block 0/1 nào bị sửa.
- **K8-4 — GHI NHẬN. KT-42 dễ thỏa nhưng chưa phải phép kiểm có ý nghĩa nhất.**
  - Biên là khoảng 1,010 lần (200 W so với 0.198 W). KT-42 không kiểm khả năng chịu xung.
  - Danh mục `[W-09]` đã có số liệu xung "2,6 kW 10 s every 120 s" (BOM chính thức dòng 43). Năng lượng xung cho phép khoảng 26 kJ, so với E_Rh = 59 J.
  - Đề xuất (tùy chọn): thêm phép kiểm năng lượng xung, hoặc ghi chú trong KT-42.

### K9 — Giao diện ICD và Mo_phong

- **Đạt.**
  - Mo_phong có 75 tên biến (B2:B76), không trùng, đều là tên MATLAB hợp lệ.
  - Tập tên **trùng khớp với ICD §4.1** (76 tên). Tên duy nhất của ICD không có trong Mo_phong là `psi_ref`; đây là tín hiệu tính trực tuyến, không phải tham số, nên hợp lý.
  - Đơn vị ở cột D khớp ICD.
  - Mọi ô C2:C76 là công thức và trả về số (không có chuỗi).
- **Cột G** = `B&" = "&C&";   % "&D&IF(F="",""," — "&F)`, sinh 75 dòng dạng `ten = so;   % don_vi — ghi chú`.
  - Checker phân tích lại cả 75 dòng: đúng cú pháp gán MATLAB, không mất biến.
  - Số in ra 15 chữ số có nghĩa; sai số tương đối so với giá trị double ≤ 4.7e-15 (ví dụ `k_qd = 0.000804686494141882`). Không có dạng `E` gây lỗi (`Ts_sim = 0.00005`, `C_dc = 0.00022`).
- **K9-1 — GHI NHẬN. Hướng dẫn chép cột dễ gây lỗi cú pháp.**
  - `Mo_phong!G1` ghi "chép nguyên cột vào init_params.m", nhưng chính ô G1 là văn bản tiếng Việt, không phải lệnh MATLAB. Chép cả cột sẽ gây lỗi cú pháp ở dòng đầu.
  - Ghi chú có ký tự Unicode (²·Ω−√≤|). MATLAB R2020a trở lên đọc UTF-8 bình thường; bản cũ hơn có thể hiển thị lỗi phông (chỉ ảnh hưởng chú thích).
  - Đề xuất: ghi "chép G2:G76", hoặc cho G1 bắt đầu bằng `%`.
- **ICD dòng 86:** câu "v1.4 không đổi tên biến hay giá trị nào của sheet này so với v1.3" **đã xác minh đúng** (diff cột A–F của Mo_phong bằng 0).

### K10 — Phiên bản và kết quả mô phỏng

- **Kết quả tốt:**
  - Không khẳng định kết quả mô phỏng nào. KT-32 = "TBD — Report: chưa chạy"; Tong_hop B56 ghi "kiểm chứng S (KT-32) chờ Khối 4–5".
  - Excel Info A3/A4 có lịch sử v1.4.
  - README dòng 47–49 mô tả đúng v1.4/v1.3/v1.2 (v1.3 đúng là chỉ thêm khối O–R và Mo_phong).
- **K10-1 — CẢNH BÁO (nhẹ). Lịch sử phiên bản tài liệu chưa đồng bộ.**
  - `01_Thuyet_minh…` dòng 13: mục 27/10/2026 **không có số phiên bản tài liệu**. Header dòng 3–4 vẫn là "v1.0 — Ngày 24/10/2026". Nguồn góp ý ghi "góp ý PE-HW", còn Excel Info A4 ghi "góp ý đồng nghiệp (file v3, 27/10/2026)", tức không thống nhất.
  - `02_ICD…`: dòng 86 đã sửa sang Excel v1.4, nhưng lịch sử dòng 5 (v1.0/v1.1/v1.2) không có mục 27/10. §6 của ICD chỉ bắt buộc nâng phiên bản khi đổi ký hiệu/đơn vị/dải, nên đây chỉ là thiếu ghi lịch sử.
  - `03_SDD…`: dòng 5 đã sửa sang v1.4, nhưng dòng 4 (lịch sử v1.0..v1.3) không có mục 27/10.
  - Đề xuất: thêm một mục lịch sử ngắn (ngày, nội dung đổi, ID ảnh hưởng) cho cả 3 tài liệu; thống nhất cách ghi nguồn góp ý.
- **K10-2 — GHI NHẬN. Có điểm diff ngoài khai báo** (xem §2): Kiểm tra!E41 đổi dạng hằng số, F81 có ghi chú, Info dời dòng. Không đổi số, nhưng lời khai "chỉ các ô sau thay đổi" chưa đầy đủ. Nên ghi thêm vào Info A4.
- **K10-3 — ĐÁNH GIÁ các tài liệu còn trỏ Excel cũ:**

| Tài liệu / dòng | Trỏ tới | Số trích còn đúng ở v1.4? | Mức |
|---|---|---|---|
| `Block 2/01_SAD…` dòng 214, 216 | v1.2 | Đúng (M_max/M_N 2.19, k_dt 3.61 không đổi) | GHI NHẬN — bản lịch sử, nên thêm "(v1.4 không đổi)" |
| `Block 3/02_So_do_Mach_luc_va_BOM…` dòng 6 | v1.2 | Đúng (BOM không trích E_Rh hay số nào đã đổi) | GHI NHẬN |
| `Block 3/04_SRS_A1…` dòng 5 | v1.2 (`Dẫn xuất`, `Kiểm tra`, `WCCA`) | Số trích vẫn đúng, nhưng `Kiểm tra` đã có thêm KT-34..43 và `Dẫn xuất` có thêm D14, D15 mà doc 04 chưa phản ánh | **CẢNH BÁO** (nhẹ) — đây là sổ đăng ký SRS-Dxx/RTM chính thức |
| `Block 3/03_SDD…` dòng 296 | "Mo_phong của Excel v1.3" | Đúng (giá trị bằng nhau) | GHI NHẬN |
| `Block 3/03_SDD…` dòng 316 | "≈ 60 J (khối H)" | 59.4 J, vẫn hợp lý khi làm tròn | GHI NHẬN |
| `Block 3/01_Thuyet_minh…` dòng 11 | "(Excel v1.2)" trong ghi chú cập nhật 25/10 | Ghi chú lịch sử | Chấp nhận |
| `README.md` dòng 54 | "SRS-D01..D13" | Thiếu D14, D15 | GHI NHẬN (xem K7-1) |

Không còn tài liệu nào trích số E_Rh cũ 59.9 J (đã grep toàn bộ `*.md`).

### K12 — Nguồn và catalogue

- **Kết quả tốt:**
  - `GiaDinh_K3!G60` trỏ `[W-09]`. Checker mở `Tài liệu tham khảo/Catalogue web/00_Danh_muc_nguon_catalogue_web.md`: mục `[W-09]` trích nguyên văn "Power resistor 200W (Pn @ 40°C)", khớp P_Rh = 200 W.
  - Tong_hop ghi đúng mã [W-xx] cho từng thiết bị.
- **K12-1 — CẢNH BÁO. Đoạn giải thích trong Thuyết minh §8.1 còn lời cũ, mâu thuẫn với chính bảng vừa sửa.**
  - Vị trí: `01_Thuyet_minh…` dòng 168 ("Giải thích ngắn" ngay dưới bảng §8.1).
  - Nguyên văn: "Công suất định mức của điện trở 210 Ω (ví dụ loại Danotherm trong [W-05] tr.25) **chưa xác minh** — đề xuất chọn loại ≥ 100 W có tiếp điểm nhiệt".
  - Vì sao lệch:
    - Dòng 162 cùng bảng ghi "200 W ≥ 0.20 W | KT-42 ✓".
    - GiaDinh_K3 D60 = 200 W `[W-09]`; BOM chính thức dòng 43 ghi 200 W @40 °C.
    - Ở chỗ khác số trang là `[W-05] tr.24`, không phải tr.25.
  - Đề xuất: sửa đoạn giải thích thành "200 W @40 °C [W-09], xung 2.6 kW/10 s mỗi 120 s" và bỏ chữ "chưa xác minh".
- **K12-2 — GHI NHẬN (tồn từ trước). Trạng thái phanh BE1 7 N·m chưa cập nhật.**
  - `01_Thuyet_minh…` dòng 181: "**7 N·m** (cấp BE1 — *chưa xác minh catalogue*)".
  - Mâu thuẫn với `GiaDinh_K3!F20` ("đã xác minh" `[W-07]`) và Phụ lục C của báo cáo 05.
- **K12-3 — GHI NHẬN. Danh sách sheet trong Thuyết minh thiếu.** Dòng 5 liệt kê sheet nhưng thiếu `Mo_phong` (và `Info`). Nhỏ.

### Kiểm tra riêng theo yêu cầu

- **Quy_dao:**
  - Quỹ đạo đúng a* = 0.45, ρ* = 1.8, v_max = 0.12. Điểm mốc t₁..t₇ là công thức trỏ về `Tính chọn` D39..D41 (T_j = 0.25 s, T_a = 0.0167 s, t_acc = 0.5167 s).
  - v và s tích phân hình thang; s cuối = 0.181995 m, bằng 2·s_acc + v·1 s.
  - Công thức 7 cột trên 241 hàng **đồng nhất** (đã kiểm từng hàng).
  - **Quy ước mô-men đúng:**
    - (F_c + δMa) ≥ 0 thì chia η (góc I); ngược lại thì nhân η (góc II), đúng §4.2-B4.
    - Số hạng J_B·a/k cộng ngoài η (đúng, vì quán tính rotor nằm trên trục động cơ).
    - M max = 9.930 N·m (= D62); M min = −5.286 N·m. Tính tay: −5,275·k·0.9 − 1.465 = −5.286 ✓.
    - A2 giải thích vì sao M min khác D63 (−6.18 theo quy ước kéo cho tính nhiệt).
  - Nhãn `A2` ghi rõ "Mô hình khối cứng như khối D/F (M_Σ gắn cứng)" và hệ số khoảng 0.48 so với 2 khối lượng (= D188).
  - Biểu đồ 1 tham chiếu đúng F14:F254 và G14:G254; biểu đồ 2 tham chiếu C14:C254 và D14:D254. **GHI NHẬN:** tiêu đề biểu đồ "Biểu đồ phụ tải trên trục động cơ" không ghi "khối cứng"; nên thêm.
- **Tong_hop:**
  - Mã KT trích **đúng ý nghĩa** ở cả 15 dòng: KT-01 (F_c), KT-06 (F_max), KT-31 (Δv), KT-05 (λ 342 V), KT-07 (k_dt), KT-02/03 (bám), KT-11 (I_đỉnh), KT-15 (P_dc), KT-13/14 (R_h), KT-39 (E_Rh > E_C), KT-27/28 (M_B), KT-18..20 (S-curve), KT-22 (Δt_torque), KT-23/24 (PM), KT-37/38 (giảm từ thông).
  - Phép đếm đúng: 40 Đạt / 43 mã, 2 "Không áp dụng" (KT-08, KT-29), 1 TBD (KT-32), 0 "Không đạt", WCCA 8/8 Đạt. Checker đã đếm tay từ cột E của Kiểm tra.
  - Câu "mọi ô là công thức" chưa đúng nguyên văn (xem K6-1).
  - GHI NHẬN: các vùng `'Kiểm tra'!$A$2:$A$44` và `$E$2:$E$44` là dải cố định, phải sửa tay nếu thêm KT-44.
- **KT-42/KT-43:**
  - KT-42 = `IF(GiaDinh_K3!D60 ≥ 'Tính chọn'!D83)`, tức 200 W ≥ 0.198 W, đơn vị W, nguồn [W-09], cha SRS-FUNC-04.
  - KT-43 = `IF('Tính chọn'!D25 ≤ Catalogue!F5)`, tức 1.874 ≤ 4.95 N·m, cha SRS-PERM-04.
  - Cả hai đúng công thức và đơn vị. Xem thêm K8-1 và K8-4.

## 6. Giả định [C] / TBD / chưa chạy / chưa xác minh

- **[C] mới hoặc ẩn trong v1.4:**
  - Khối S giả định a_max xảy ra đúng lúc v = v_max (bảo thủ).
  - Thông số hiển thị của Quy_dao: T_đều = 1 s, bước 0.01 s.
  - E_Rh cho năng lượng rotor đi qua η hộp số (K6-2).
- **[C] cũ không đổi:** P-03, P-12..P-19; GiaDinh_K3 hàng 8–36 và 44–58 (C_dc = 220 µF chưa xác minh, η_inv = 0.97, t_close/t_open…).
- **Chưa xác minh:** ngưỡng chopper trong firmware ACS380; C_dc; tham số mạch thay thế động cơ (cần ID-run); tổ hợp R87 với khung DRN80 (cần SEW xác nhận khi đặt hàng).
- **Chưa chạy:** DV-01..07 (S), DVP-SS-01..08, KT-32. Chưa có Simulink hay `init_params.m`, nên không kiểm được K9 phía Simulink và K10 phần kết quả.

## 7. Kết luận

| Kiểm | Kết luận | Lý do chính |
|---|---|---|
| K6 | **Đạt** (có ghi nhận) | Mọi số khớp SSoT và tính lại độc lập; chỉ có text gõ tay trong Tong_hop (K6-1) |
| K7 | **Đạt** | KT-42/43 có cha; D14/D15 chưa có ở doc 04 là tồn từ v1.3 |
| K8 | **Đạt có điều kiện** | P_Rh chưa có mã SRS-Dxx (K8-1); khối S không vi phạm §10 |
| K9 | **Đạt** | Mo_phong khớp ICD §4.1; cột G đúng cú pháp; chỉ có lưu ý G1 |
| K10 | **Đạt có điều kiện** | Thiếu mục lịch sử ở ICD/SDD; Thuyết minh thiếu số phiên bản; diff ngoài khai báo nhỏ; doc 04 vẫn trỏ v1.2 |
| K11 | **Đạt** | Không có xung đột mới; biên công suất hãm kể δ = 1.56 |
| K12 | **Đạt có điều kiện** | Thuyết minh §8.1 dòng 168 mâu thuẫn với [W-09] và dòng 162 |

**Mức khớp tổng (theo §9.5): Tốt, có vài chỗ lệch nhẹ về tài liệu.** Excel v1.4 đúng số và đúng công thức; các thay đổi khai báo đều xác minh được. Không có XUNG ĐỘT nên không bắt buộc dừng tại cổng.

## 8. Câu hỏi cho Người dùng

1. Có định danh P_Rh = 200 W thành mã dẫn xuất (ví dụ `SRS-D05d`) và cập nhật doc 04 (kèm D14, D15, nguồn Excel v1.4) không?
2. Ngưỡng PASS công suất hãm của DV-04 dùng P_BR,max = 1,130 W hay giá trị 436.5 W (SRS-D05b)? Khối S cho thấy 436.5 W thấp hơn mức thực tế khoảng 1.66 lần.
