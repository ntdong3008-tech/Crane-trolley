# BÁO CÁO CHECKER LƯỢT 2 — KIỂM LẠI EXCEL v1.4 VÀ TÀI LIỆU SAU KHI SỬA THEO LƯỢT 1 (27/10/2026)

> Lượt Checker riêng, chỉ đọc (`WORKFLOW_RULES.md` §1, §8, §9). Không sửa file nào trong thư mục dự án. Mọi số dưới đây lấy từ file thật hoặc do Checker tự kiểm lại bằng script; mục nào không kiểm được thì ghi rõ. Lời khai của Writer không được dùng làm bằng chứng.

## 1. Phiên bản đã kiểm

- **Ngày kiểm:** 27/10/2026.
- **Baseline đối chiếu:** `SSoT-8.5EMG-v1.2` (P-01..P-20), `SRS Baseline A v1.2` + A.1 (CR-01..07), QĐ-01..08, nhóm C (duyệt 26/10/2026). Mục đã chốt không bị báo lỗi. K6-2 (η cho năng lượng rotor) chờ người dùng quyết định, chỉ ghi nhận.
- **Excel sau sửa:** `Block 3/00_Tinh_toan_Xe_con_x2_v1.4.xlsx` (Info A3: "Checker lượt 1 … đã sửa theo báo cáo; chờ Checker lượt 2"), chép vào `scratchpad\checker2\in\v14_after.xlsx`.
- **Excel trước sửa (bản lượt 1 đã kiểm):** `scratchpad\fix\v14_before.xlsx`. Checker xác minh bản này **trùng MD5** với bản lượt 1 đã kiểm (`scratchpad\checker\in\v14.xlsx`, MD5 `7b658551…`), nên diff dưới đây so đúng với bản đã kiểm.
- **Báo cáo lượt 1 lưu trong dự án** (`Block 3/05_Bao_cao_Checker_Excel_v1.4_luot1.md`): **trùng từng byte** với báo cáo gốc trong scratchpad (MD5 `5fced56a…`). Lời khai "bản sao nguyên văn" là đúng.
- **Tính lại:** chép thêm một bản rồi tính lại bằng Microsoft Excel qua COM (`CalculateFull`, không lưu):
  - **0 ô lỗi `#…`.**
  - 2,632 ô công thức (lượt 1: 2,627, tăng 5 ô = Tong_hop D23/D28/D36/D37 + Dẫn xuất C24). Cache gốc khớp giá trị Excel tính lại: **0 ô lệch**.
  - **2 biểu đồ** (COM `ChartObjects` = 2, đều ở Quy_dao). Vùng dữ liệu biểu đồ không đổi.
- **Tài liệu đã kiểm:** Thuyết minh (`01_…`, dòng 5, 11, 13, 95, §8.1, §8.2); SDD (`03_…`, dòng 4–5, 296, 316); ICD (`Block 2/02_…`, dòng 5, 86); doc 04 SRS-A1 (toàn bộ 126 dòng); README (dòng 44–56); danh mục `[W-09]`; grep chéo toàn bộ `*.md`.
- **Simulink / `init_params.m`:** chưa có (Khối 4). Không có kết quả mô phỏng nào để kiểm.

## 2. Diff Excel trước và sau sửa (đầy đủ)

So từng ô (cả công thức lẫn giá trị) trên mọi sheet. Thêm phần so XML gói: chỉ khác ở `core.xml` (ngày lưu), `calcChain`, `sharedStrings`, `workbook.xml` (đường dẫn lưu và mã phiên bản), 2 file biểu đồ (tiêu đề) và các sheet có ô sửa.

| Sheet | Ô | Thay đổi | Có trong khai báo? |
|---|---|---|---|
| Info | A3 | Trạng thái: "Checker lượt 1 … chờ Checker lượt 2" | Có |
| Info | A4 | Thêm "PE-HW", đoạn "Thay đổi phụ không đổi số" (F81, E41, chèn A22–A23) và đoạn "Sửa sau Checker lượt 1" | Có |
| Info | A22 | "Mọi ô số liệu và ngưỡng là công thức; tên thiết bị, đơn vị, mã KT là chữ." | Có |
| Tong_hop | A2 | Câu mô tả tương tự A22 | Có |
| Tong_hop | D23, D28, D36, D37 | Chữ gõ tay → công thức ghép chuỗi (`Params!C20`, `GiaDinh_K3!D5`, `Params!C14`, `Params!C15`, `'Kiểm tra'!D8`, `'Kiểm tra'!D3`) | Có |
| Tính chọn | A232, G233:G236 | Nguồn "WORKFLOW §4.2-B4 (δ, J_B) + §4.2-C4" (thay "Tự dẫn") | Có |
| Kiểm tra | G43 | Ghi chú năng lượng xung `[W-09]` | Có |
| Dẫn xuất | A24:H24 | Hàng mới `SRS-D05d`, C24 = `GiaDinh_K3!$D$60` (200 W), cha SRS-FUNC-04, KC I/A, DV-04 | Có |
| Mo_phong | G1 | "% Dòng lệnh MATLAB (v1.4) — chép G2:G76 vào init_params.m" | Có |
| Quy_dao | C4, C5 | "s — tham số hiển thị [C]" | Có |
| Quy_dao | Biểu đồ 1 | Tiêu đề thêm "(mô hình khối cứng)" | Có |
| Quy_dao | Biểu đồ 2 | Tiêu đề "Gia tốc và vận tốc" → "Gia tốc và vận tốc đặt (S-curve)" | Có ("tiêu đề 2 biểu đồ") |

- **Không có thay đổi nào ngoài khai báo.**
- **Giá trị số:** không ô số nào đổi. Có hai ô kiểu chữ đổi giá trị hiển thị:
  - Tong_hop A2 (câu mô tả);
  - Tong_hop D28: "w₀ = 0.015 (không dùng φ)" → "w₀ = 0.015 (không dùng φ = 0.2)".
- D23, D36, D37 ra **đúng chuỗi cũ** ("3 pha 380 V ±10%", "≥ 1.20 (SRS A.1)", "≥ 1.20").
- Params, GiaDinh_K3, Catalogue, WCCA: 0 thay đổi.
- Tính chọn D74/D75 (công thức khóa §4.2-C4): không đổi.

**Lời khai "không đổi giá trị số nào so với bản đã kiểm ở lượt 1": ĐÚNG.**

## 3. Phát hiện lượt 1 → trạng thái lượt 2

| Mã lượt 1 | Mức lượt 1 | Trạng thái lượt 2 | Bằng chứng kiểm lại |
|---|---|---|---|
| **K6-1** "Mọi ô là công thức" chưa đúng | CẢNH BÁO (nhẹ) | **Đã xử lý** | Tong_hop A2 và Info A22 đã sửa câu. D23/D28/D36/D37 đã là công thức và cho đúng chuỗi cũ. Tên thiết bị (B18, B20, B22, B23, B24) giữ chữ, khớp câu mới. Còn một chỗ nhỏ chưa nối công thức, xem **N-1**. |
| **K6-2** E_Rh cho năng lượng rotor đi qua η hộp số | GHI NHẬN | **Còn tồn, chờ người dùng** (không phải lỗi mới) | `Tính chọn!D82` không đổi; E_Rh = 59.4149 J. |
| **K6-3** Quy_dao có 4 hằng gõ tay | GHI NHẬN | **Đã xử lý** | C4/C5 ghi "tham số hiển thị [C]". D14 = E14 = 0 là điều kiện đầu v(0) = s(0) = 0, tự giải thích được, không cần nguồn. |
| **K11-1** SRS-D05b 436.5 W không bảo thủ so với khối S; ngưỡng PASS của DV-04 | GHI NHẬN | **Đã xử lý** | Doc 04 §2 hàng D05: "$P_{dc}$ là giá trị định cỡ, **không phải ngưỡng PASS** của DV-04". §4 DVP-SS-05: "không so công suất hãm đo được với $P_{dc}$ = 436.5 W của D05b". Lượt 1 đề xuất ghi ở D05b **hoặc** DVP-SS-05; Writer ghi ở DVP-SS-05, thế là đủ. |
| **K7-1** SRS-D14, D15 chưa có trong doc 04 và README | GHI NHẬN | **Đã xử lý** | Doc 04 dòng 45–46 có D14/D15 khớp Excel (0.804; i_sq 2.98 ≤ 3.52 A; I_s 2.25 ≤ 3.9 A; ω_fw 133.2 / 119.9 rad/s, đối chiếu Tính chọn D199..D208). README dòng 54: "SRS-D01..D15 (+ D05d)". |
| **K8-1** P_Rh = 200 W chưa có mã SRS-Dxx | CẢNH BÁO | **Đã xử lý** | Dẫn xuất hàng 24 `SRS-D05d` = `GiaDinh_K3!$D$60` = 200 W, cha SRS-FUNC-04, F24 truy về D82/D83/KT-42, DV-04. Doc 04 §2 (quy ước mã con, hàng D05), §3 RTM "D05 (a–d)", §7 FM-02 đều đã đồng bộ. Hàng 24 nằm sau D15 (xem **N-4**, chỉ là thẩm mỹ). |
| **K8-2** Khối S thiếu "Nguồn công thức" | GHI NHẬN | **Đã xử lý** | A232 và G233:G236 = "WORKFLOW §4.2-B4 (δ, J_B) + §4.2-C4". |
| **K8-3** Khối S không vi phạm §10 | (kết quả tốt) | **Không áp dụng**, vẫn đúng | D74/D75 không đổi. KT-15 = `'Tính chọn'!$D$75/1000`, Dẫn xuất C8, WCCA hàng 15, Tong_hop B39 vẫn dùng D75. |
| **K8-4** KT-42 chưa kiểm khả năng chịu xung | GHI NHẬN | **Đã xử lý** (bằng ghi chú) | Kiểm tra G43 và Thuyết minh §8.1 dòng 168: 2.6 kW × 10 s ≈ 26 kJ ≫ 59 J. Checker đối chiếu danh mục `[W-09]`, có nguyên văn "2,6kW 10s every 120s". Đây là ghi chú, không phải phép kiểm `IF`; lượt 1 đã cho phép cách này. |
| **K9-1** Mo_phong G1 gây lỗi cú pháp khi chép cả cột | GHI NHẬN | **Đã xử lý** | G1 bắt đầu bằng `%`, ghi "chép G2:G76". Chép cả cột G vẫn là MATLAB hợp lệ. Lưu ý Unicode trong chú thích (chỉ là thông tin) vẫn giữ, chấp nhận được. |
| **K10-1** Lịch sử phiên bản tài liệu chưa đồng bộ | CẢNH BÁO (nhẹ) | **Đã xử lý** | Thuyết minh dòng 13: "v1.3 (27/10/2026, nguồn số Excel v1.4, góp ý đồng nghiệp PE-HW — file v3)". Excel Info A4: "góp ý đồng nghiệp PE-HW (file v3, …)", nay đã thống nhất. ICD dòng 5 có ghi chú 27/10 kèm lý do không nâng phiên bản theo §6. SDD dòng 4 có mục v1.4. Thuyết minh vẫn giữ mã `…-v1.0` và Ngày 24/10/2026 ở dòng 3–4; SDD và doc 04 cũng làm vậy, nên đây là quy ước chung của nhóm. Chỉ ghi nhận. |
| **K10-2** Diff ngoài khai báo chưa ghi vào Info A4 | GHI NHẬN | **Đã xử lý** | Info A4 có "Thay đổi phụ không đổi số: Tính chọn F81 …; Kiểm tra E41 … 0.000000001; Info chèn 2 dòng A22–A23". Mục "Sửa sau lượt 1" chưa kể hết các ô chữ đã sửa (xem **N-5**, mức nhỏ). |
| **K10-3** Tài liệu trỏ Excel cũ: SAD 214/216 | GHI NHẬN | **Còn tồn** (Writer cố ý giữ, chờ người dùng) | SAD dòng 216 vẫn trỏ `…_v1.2.xlsx`. Số trích vẫn đúng ở v1.4. |
| K10-3: BOM chính thức dòng 6 | GHI NHẬN | **Còn tồn** (cố ý, chờ người dùng) | Vẫn trỏ `…_v1.2.xlsx`. Số trích vẫn đúng. |
| K10-3: doc 04 dòng 5 trỏ v1.2, thiếu KT-34..43 và D14/D15 | **CẢNH BÁO** (nhẹ) | **Đã xử lý** | Dòng 5 trỏ v1.4. RTM có KT-33..43, V-model ghi "KT-01..43". Mọi số trong doc 04 §2 và §6 khớp Excel v1.4 (Checker đối chiếu từng số: D01 11,940 N; D02 2.19/2.485; D04; D05 210 Ω, [99; 428], 436.5/724/1,130 W, 200/0.20 W; D06 0.517 s; D07 0.714/7 ms/34.6°; D09 108.4/5.55 ms/1.76 ms; D11 1.23 mm/s; D13 [5.94; 10.12]; WCCA 1.02, 1.450, 499 W, 591 V, 2.51, 1.137/1.232). |
| K10-3: SDD dòng 296 "Excel v1.3" | GHI NHẬN | **Đã xử lý** | "Excel v1.4 (giá trị như v1.3; … chép vùng G2:G76)". |
| K10-3: SDD dòng 316 "≈ 60 J" | GHI NHẬN | **Đã xử lý** | "≈ 59 J (khối H, Excel v1.4)". |
| K10-3: Thuyết minh dòng 11 "(Excel v1.2)" | Chấp nhận | **Không áp dụng** | Ghi chú lịch sử 25/10, Writer cố ý giữ. |
| K10-3: README dòng 54 "D01..D13" | GHI NHẬN | **Đã xử lý** | Xem K7-1. |
| **K12-1** Thuyết minh §8.1 còn lời "chưa xác minh … ≥ 100 W … tr.25" | **CẢNH BÁO** | **Đã xử lý** | Dòng 168: "200 W @40 °C … xung 2.6 kW trong 10 s mỗi 120 s (`[W-09]`, … `[W-05]` tr.24)". Không còn "100 W" hay "tr.25" trong Thuyết minh (grep). Khớp GiaDinh_K3 D60/F60, Info A34 và danh mục `[W-09]` ("Power resistor 200W (Pn @ 40°C)", ABB liệt kê mã này ở `[W-05]` tr.24). |
| **K12-2** BE1 7 N·m ghi "chưa xác minh" | GHI NHẬN | **Đã xử lý** | §8.2 dòng 183: "(cấp BE1 10/7/5 N·m — đã xác minh `[W-07]`)", khớp GiaDinh_K3 F20 và Info A32. Thuyết minh không còn chỗ nào ghi BE1 "chưa xác minh". |
| **K12-3** Danh sách sheet thiếu Mo_phong, Info | GHI NHẬN | **Đã xử lý** | Dòng 5 liệt kê đủ 11 sheet, đúng thứ tự trong workbook. |
| Quy_dao: tiêu đề biểu đồ 1 không ghi "khối cứng" | GHI NHẬN | **Đã xử lý** | Biểu đồ 1: "Biểu đồ phụ tải trên trục động cơ (mô hình khối cứng)". Vùng dữ liệu vẫn là F14:F254 và G14:G254. |
| Tong_hop: vùng `'Kiểm tra'!$A$2:$A$44` cố định | GHI NHẬN | **Còn tồn** (chấp nhận) | Không đổi. Vẫn đúng với 43 mã hiện có (40/43 Đạt, 2 Không áp dụng, 1 TBD, 0 Không đạt; WCCA 8/8). Chỉ phải sửa tay nếu thêm KT-44. |

**Tổng hợp:** 2 CẢNH BÁO của lượt 1 (K8-1, K12-1) và 3 CẢNH BÁO nhẹ (K6-1, K10-1, K10-3 doc 04) đều **đã xử lý**. Còn tồn: K6-2, SAD 214/216, BOM dòng 6 (đều cố ý chờ người dùng) và vùng cố định trong Tong_hop (chấp nhận được).

## 4. Ma trận khớp (§9.2)

Ma trận này kế thừa từ lượt 1. Cột SRS-Dxx và Report đã cập nhật theo Excel và doc 04 sau sửa.

| PRD | SRS (+Downstream / SRS-Dxx) | Phân hệ (Khối 2) | Thiết kế (Khối 3) | DV | Report |
|---|---|---|---|---|---|
| PRD-FUNC-01 | SRS-FUNC-01; #4 → D09 | SS-4, SS-5, SS-2 | SDD §4.2, §5.4 | DV-01 | A: KT-22 Đạt; S: chưa chạy |
| PRD-FUNC-04 | SRS-FUNC-02; #5 → D10, D11; D13 | SS-4 (FSM), SS-5 | SDD §5; Thuyết minh §8.2 | DV-02 | A: KT-25/27/28/30 Đạt; KT-29 Không áp dụng (QĐ-07); S: chưa chạy |
| PRD-FUNC-02 | SRS-FUNC-03; D06; #8 → D12 | SS-4 | SDD §3; Quy_dao | DV-03 | A: KT-18..20, 26 Đạt; S: chưa chạy |
| PRD-FUNC-03 | SRS-FUNC-04; #3 → D05a/b/c, **D05d** | SS-2, SS-3 | Thuyết minh §8.1; khối H, S | DV-04 | A: KT-13..17, 39, 42 Đạt; S: chưa chạy |
| PRD-PERM-01 | SRS-PERM-01; #6 → D01; #7 → D02 | SS-5, SS-6 | Thuyết minh §1, §5 | DV-05 | A: KT-02..06, 11, 12, 33, 37 Đạt; S: chưa chạy |
| PRD-PERM-02 | SRS-PERM-02; #1 → D07; #2 → D08; D03, D14, D15 (D12 qua DV-06) | SS-4, SS-6 | SDD §4 | DV-06 | A: KT-23, 24, 31, 35, 36 Đạt; S: chưa chạy |
| PRD-PERM-03 | SRS-PERM-03; D06 | SS-4, SS-6 | SDD §3.4 | DV-07 | A: KT-21 (tham khảo), KT-41 Đạt; S: chưa chạy |
| PRD-PERM-04 | SRS-PERM-04 (A.1); D02, D04 | SS-2, SS-5 | Thuyết minh §4, §5, §7 | DV-08 | A/I: KT-07, 09, 10, 38, 43 Đạt; KT-08 Không áp dụng (CR-01) |

- Không có ô **trống**. KT-32 (DV-01..07, phương pháp S) = "TBD — Report: chưa chạy".
- D12 (cha SRS-FUNC-03) cũng xuất hiện ở hàng PRD-PERM-02 của doc 04 §3 vì DV của nó là DV-06 (`Dẫn xuất!H20`). Truy ngược vẫn nhất quán, **không phải lỗi**.

## 5. Phát hiện mới ở lượt 2

Thứ tự theo §9.3. **Không có XUNG ĐỘT. Không có CẢNH BÁO mới.** Tất cả phát hiện mới đều ở mức GHI NHẬN.

### K6 — Số liệu và đơn vị

- **N-1 — GHI NHẬN. Ngưỡng 5% gõ cứng trong chuỗi công thức của Tong_hop.**
  - Vị trí: `Tong_hop!D31` = `="Δv = "&TEXT('Tính chọn'!$D$21,"0.0%")&" (≤ 5%)"`.
  - Vì sao: A2 và Info A22 nay khẳng định "Mọi ô số liệu và **ngưỡng** là công thức". Ô D31 là công thức, nhưng phần ngưỡng "≤ 5%" là chữ gõ tay, không trỏ về `'Kiểm tra'!$D$32` (KT-31 = 0.05). Lượt 1 không nêu ô này trong danh sách ví dụ.
  - Không ảnh hưởng kết quả: KT-31 vẫn tính bằng D32.
  - Các chữ số còn lại trong Tong_hop đều thuộc tên hoặc mã thiết bị, chấp nhận theo câu mới: B17 "400 V/50 Hz", D19 "(cấp 10/7/5)", B23 "gG 6 A", B54 "/ 8". Ngoài ra D28 hiện "φ = 0.2"; SSoT viết 0.20, chỉ khác cách hiển thị.
  - Đề xuất (tùy chọn): `" (≤ "&TEXT('Kiểm tra'!$D$32,"0%")&")"`; có thể thêm `TEXT(Params!$C$15,"0.00")` ở D28.

### K7, K8 — Phân bổ và yêu cầu dẫn xuất

- **N-4 — GHI NHẬN. Vị trí hàng SRS-D05d.**
  - Vị trí: `Dẫn xuất!A24`.
  - D05d nằm sau D15, không liền với D05a..c (hàng 7–9). Không có công thức nào tham chiếu theo dải sheet `Dẫn xuất` (Checker đã quét toàn workbook), nên không gây sai.
  - Đề xuất (tùy chọn, lần sửa sau): chèn D05d liền sau hàng 9.

### K9 — Giao diện

- Không có phát hiện mới. Cột A–F của Mo_phong không đổi; ICD dòng 86 vẫn đúng.

### K10 — Phiên bản

- **N-2 — GHI NHẬN. README mô tả trạng thái Excel đã cũ.**
  - Vị trí: `README.md` dòng 47, nguyên văn: "… sheet Tong_hop & Quy_dao (chưa qua Checker)".
  - Vì sao lệch: Excel Info A3 nay ghi đã qua Checker lượt 1 và chờ lượt 2.
  - Đề xuất: cập nhật sau khi có kết luận lượt 2, ví dụ "(Checker lượt 1–2: 27/10/2026)".
- **N-5 — GHI NHẬN. Mục "Sửa sau Checker lượt 1" trong Info A4 chưa kể hết các ô chữ đã sửa.**
  - Vị trí: `Info!A4`.
  - A4 có kể D05d, K6-1, K8-2, K8-4, K9-1 và tiêu đề biểu đồ khối cứng. A4 không kể: Quy_dao C4/C5, tiêu đề biểu đồ 2, Info A3/A22, Tong_hop A2.
  - Không đổi số. Đề xuất: thêm một cụm ngắn nếu muốn lịch sử đầy đủ.
- **N-3 — GHI NHẬN (tồn từ 25/10/2026, không do đợt sửa này gây ra). Lệnh LaTeX `\text` bị hỏng thành ký tự TAB.**
  - Nguyên văn hiển thị là `$i_{<TAB>ext{thực}}$`. Ký tự TAB thay cho `\t` nên công thức không hiển thị đúng.
  - Vị trí:
    - `Block 3/03_SDD_…` dòng 4, trong đoạn "v1.2 (25/10/2026 …)";
    - `Block 2/01_SAD_…` dòng 214;
    - `Block 3/01_Thuyet_minh_…` dòng 95.
  - Có thể kết luận lỗi có từ trước: file SAD không bị sửa trong đợt này mà vẫn có lỗi giống hệt.
  - Writer có sửa SDD dòng 4 (thêm mục v1.4) nhưng không đụng tới chỗ này.
  - Đề xuất: thay ký tự TAB bằng `\t` (`\text{thực}`) ở cả 3 chỗ, khi người dùng cho phép sửa SAD.

### K11 — Xung đột thiết kế

- Không có xung đột mới. Mọi số đều không đổi so với lượt 1: P_dc,hãm = 436.488 W; khối S 724.486 W; biên 1.5597 / 3.2207; cửa sổ R_h [99; 428] Ω; WC-5 1.02365; k_dt 3.60886; E_Rh 59.4149 J; P_Rh,tb 0.19805 W.

### K12 — Nguồn và catalogue

- Không có phát hiện mới.
  - `[W-09]`: 200 W @40 °C và xung 2.6 kW/10 s/120 s khớp nguyên văn trong danh mục.
  - `[W-07]` BE1 10/7/5 N·m khớp Info A32.
  - Tong_hop E22 ghi `[W-05] tr.24, [W-09]`.

## 6. Giả định [C] / TBD / chưa chạy / chưa xác minh

- **[C] không đổi so với lượt 1:**
  - P-03, P-12..P-19; GiaDinh_K3 hàng 8–36 và 44–58;
  - Khối S giả định a_max xảy ra đúng lúc v = v_max;
  - Tham số hiển thị Quy_dao (T_đều = 1 s, bước 0.01 s; nay đã gắn nhãn ở C4/C5);
  - K6-2 (η cho năng lượng rotor), chờ người dùng.
- **Chưa xác minh:**
  - Ngưỡng chopper trong firmware ACS380;
  - C_dc = 220 µF;
  - Tham số mạch thay thế động cơ (cần ID-run);
  - Tổ hợp R87 với khung DRN80 (cần SEW xác nhận);
  - Hiệu suất riêng của hộp số SEW (Thuyết minh dòng 127).
- **Chưa chạy:** DV-01..07 (S), DVP-SS-01..08, KT-32. Chưa có Simulink hay `init_params.m`, nên không kiểm được K9 phía Simulink và K10 phần kết quả.

## 7. Kết luận

| Kiểm | Kết luận lượt 2 | Lý do chính |
|---|---|---|
| K6 | **Đạt** | K6-1 đã xử lý; mọi số không đổi và khớp SSoT; chỉ còn ngưỡng chữ ở Tong_hop D31 (N-1, GHI NHẬN); K6-2 chờ người dùng |
| K7 | **Đạt** | D14, D15 và D05d đã có trong doc 04 và README; 8/8 SRS và 8/8 Downstream được phủ |
| K8 | **Đạt** | SRS-D05d có mã, có cha, có KC/DV; khối S có nguồn công thức; §4.2-C4 giữ nguyên |
| K9 | **Đạt** | Mo_phong G1 đã sửa; tên biến và giá trị ICD không đổi |
| K10 | **Đạt** (có ghi nhận) | Lịch sử Thuyết minh/SDD/ICD/doc 04 đã đồng bộ; còn README dòng 47 (N-2), A4 chưa kể hết (N-5), TAB trong LaTeX (N-3, có từ trước); SAD/BOM trỏ v1.2 là cố ý |
| K11 | **Đạt** | Không có xung đột mới; DV-04 đã ghi rõ ngưỡng PASS |
| K12 | **Đạt** | K12-1/2/3 đã xử lý và khớp `[W-07]`, `[W-09]` |

**Mức khớp tổng (§9.5): Tốt.**
- Mọi CẢNH BÁO của lượt 1 đã được xử lý đúng.
- Việc sửa không làm đổi số nào và không làm hỏng công thức hay biểu đồ: 0 lỗi, 0 ô cache lệch, 2 biểu đồ.
- Không có XUNG ĐỘT và không có CẢNH BÁO mới; chỉ có 5 GHI NHẬN nhỏ (N-1..N-5).

## 8. Câu hỏi cho Người dùng

1. K6-2: E_Rh có tách η riêng cho phần năng lượng rotor ½J_B·ω_m² hay không? (Nếu tách thì E_Rh = 61.76 J thay vì 59.41 J; kết luận KT-39/KT-42 không đổi.)
2. Có cho phép sửa SAD dòng 214/216 và BOM dòng 6 (trỏ Excel v1.4, đồng thời sửa lỗi `\text` ở N-3) không, hay giữ nguyên làm hồ sơ lịch sử?
