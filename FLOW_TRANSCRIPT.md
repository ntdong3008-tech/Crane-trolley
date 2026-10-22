# BẢN CHÉP NGUYÊN VĂN LƯU ĐỒ DỰ ÁN (FLOW TRANSCRIPT)
*Nguồn trích xuất: `Tai_lieu_du_an\Lưu đồ dự án.jpg` (đối chiếu phóng to chi tiết với bản gốc độ phân giải cao `Công việc phân chia\Lưu đồ dự án.png` qua phân mảnh Python PIL).*

---

## I. THÔNG TIN CHUNG & KHUNG ĐỊNH DANH

### 1. Tiêu đề chính & Tiêu đề phụ (Góc trên bên trái)
- **Tiêu đề chính:**  
  `EVLEP003_HBK — CHI TIẾT LUỒNG PRE-A → EVT: TỪ KHỞI ĐỘNG ĐẾN CỔNG SAR-EVT`
- **Tiêu đề phụ:**  
  `6 nhóm công việc cốt lõi (đọc độc lập) · 7 cổng soát xét · tra cứu HBK §/Bảng/Phụ lục A khi cần tiêu chí định lượng và biểu mẫu`

### 2. Quy chuẩn kỹ thuật bản vẽ (Góc trên bên phải)
- `NÉT VẼ: ISO 128-2:2020 · CHỮ: ISO 3098`
- `KHUNG & LƯỚI VÙNG: ISO 5457 · KHUNG TÊN: ISO 7200`
- **Lưới tọa độ vùng (Grid Coordinates):**
  - Cột (ngang): `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`
  - Hàng (dọc): `A`, `B`, `C`, `D`, `E`, `F`

### 3. Khung tên (Title Block - Góc dưới bên phải [F6–F8])
- **Đơn vị:** `EVSELab JSC` / `Bộ phận Kỹ thuật`
- **Mã tài liệu:** `EVLEP003_HBK`
- **Phiên bản:** `v1.8.2 — Chờ duyệt`
- **Tên bản vẽ:**  
  `SƠ ĐỒ CHI TIẾT PRE-A → EVT`  
  `(MCR → SRR → PDR → CDR → TRR → SIR → SAR-EVT)`
- **Chuỗi cổng:** `MCR → SRR → PDR → CDR → TRR → SIR → SAR-EVT`
- **Ngày phát hành:** `24.08.2026`
- **Soạn thảo:** `N. D. Đỉnh`
- **Soát xét:** `QE Lead · [chờ ký]`
- **Phê duyệt:** `CTO · [chờ ký]`
- **Khổ giấy:** `A3 (ngang)`
- **Tỷ lệ:** `N/A`
- **Trang:** `1/1`
- **Bảo mật:** `Nội bộ (Internal)`

---

## II. CHÚ GIẢI & GHI CHÚ

### 1. CHÚ GIẢI — QUY ƯỚC NÉT (ISO 128-2:2020) [F1–F2]
- `01.2 · liền đậm 0,5 mm — dòng quy trình chính`
- `02.1 · đứt mảnh 0,25 mm — vòng lặp KHÔNG ĐẠT / Hủy`
- `04.1 · gạch–chấm mảnh — khung ghi chú, tham chiếu`
- `Giao cắt không nối — cung vượt (line jump)`

### 2. GHI CHÚ — TRA CỨU THÊM (không bắt buộc để vận hành) [F3–F5]
- `(1) Bảng 7 quy định bốn kết quả cổng: Thông qua · Thông qua có điều kiện · KHÔNG ĐẠT (soát xét lại, §8.2) · Hủy dự án (§8.4). Nhánh Hủy áp dụng tại mọi cổng do CTO quyết định; bản vẽ chỉ thể hiện tại Cổng SAR-EVT để giữ độ rõ.`
- `(2) Thẩm quyền ghi trong hình lấy theo Bảng 5. Lưu ý §5.2.2(d) và §5.3.2(h) còn quy định chữ ký CTO tại SRR-EVT / PDR-EVT — cần đối chiếu khi ký biên bản.`
- `(3) Vòng lặp mẫu EVT ≤ 2 (Bảng 2); mỗi vòng mới phải mở ECR trình CCB (§9). Vượt ngưỡng, CTO đánh giá lại tính khả thi (§4.1.5c).`
- `(4) TRL theo cổng: MCR 1–2 → SRR 3 → PDR 3–4 → CDR/TRR 4 → SIR 4–5 → SAR-EVT 5. Danh mục kiểm tra chi tiết: Phụ lục A.`

---

## III. NGUYÊN VĂN TỪNG KHỐI CÔNG VIỆC (BLOCKS)

### 1. Điểm khởi động [A1–A2]
- **Hình dạng:** Hình oval (khối bắt đầu).
- **Nội dung chữ:**  
  `KHỞI ĐỘNG`  
  `Nhu cầu thị trường`
- **Đầu ra:** Mũi tên nét liền đậm dẫn sang Khối 0.
- **Nhãn trên đường dẫn:**  
  `I: RFQ · SOR · VOC`  
  `hoặc ý tưởng nội bộ`

---

### 2. Khối 0 [A3–A4]
- **Tên khối & Điều khoản:**  
  `0 · TIỀN KHẢ THI (Pre-A) — §4.2, §4.3, §5.1`
- **Các gạch đầu dòng:**
  - `· Đăng ký mã dự án · CTO ký quyết định lập CFT`
  - `· Lập BCA sơ bộ kèm TRL và tuyên bố khả thi SX kèm MRL`
  - `· Soạn PRD dự thảo · Điều lệ & SOW có mục tiêu QCD đo được`
  - `· Ghi tối thiểu 5 rủi ro kỹ thuật / tiến độ vào sổ RRM`
- **Đầu vào:**
  - Mũi tên nét liền đậm từ khối `KHỞI ĐỘNG` đi vào cạnh trái.
  - Mũi tên nét đứt mảnh từ nhánh `KHÔNG ĐẠT` của Cổng `MCR (CTO)` đi vào cạnh đáy.
- **Đầu ra:**
  - Mũi tên nét liền đậm từ cạnh phải dẫn sang Cổng `MCR (CTO)`.

---

### 3. Khối 1 [A7–A8]
- **Tên khối & Điều khoản:**  
  `1 · EVT — YÊU CẦU HỆ THỐNG — §5.2`
- **Các gạch đầu dòng:**
  - `· Viết SRS baseline A — mọi yêu cầu phải đo được`
  - `· Khóa PRD trước khi đóng băng SRS; truy xuất SRS → PRD`
  - `· Lập DVP&R L0 + RTM ánh xạ 100 % yêu cầu`
  - `· Dựng sơ đồ biên & P-Diagram; chốt sơ bộ CTQ / CTS`
- **Đầu vào:**
  - Mũi tên nét liền đậm từ nhánh `ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN` của Cổng `MCR (CTO)` đi vào cạnh trái.
  - Mũi tên nét đứt mảnh từ nhánh `KHÔNG ĐẠT` của Cổng `SRR-EVT (SE Lead)` đi vào cạnh phải.
- **Đầu ra:**
  - Mũi tên nét liền đậm từ cạnh đáy đi xuống Cổng `SRR-EVT (SE Lead)`.

---

### 4. Khối 2 [B5–B6 / C5–C6]
- **Tên khối & Điều khoản:**  
  `2 · EVT — KIẾN TRÚC — §5.3`
- **Các gạch đầu dòng:**
  - `· Lập SAD + ICD thể hiện đủ 7 sơ đồ kỹ thuật cốt lõi`
  - `· Dựng BOM sơ bộ 3 cấp; chốt linh kiện độc cung, đặt long-lead`
  - `· Chạy DFMEA L1 — xử lý hết hạng mục AP = Cao`
  - `· Phân tích trade-off kiến trúc và Creepage / Clearance`
- **Đầu vào:**
  - Mũi tên nét liền đậm từ nhánh `ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN` của Cổng `SRR-EVT (SE Lead)` đi vào cạnh phải.
  - Mũi tên nét đứt mảnh từ nhánh `KHÔNG ĐẠT` của Cổng `PDR-EVT (SE Lead)` đi vào cạnh đáy.
- **Đầu ra:**
  - Mũi tên nét liền đậm từ cạnh trái đi sang Cổng `PDR-EVT (SE Lead)`.

---

### 5. Khối 3 [B1–B2 / C1–C2]
- **Tên khối & Điều khoản:**  
  `3 · EVT — THIẾT KẾ CHI TIẾT — §5.4`
- **Các gạch đầu dòng:**
  - `· Ra Schematic, Gerber, 3D vỏ & đồ gá, SDD, HSI`
  - `· Chứng minh biên an toàn: WCCA, SI/PI, mô phỏng nhiệt`
  - `· Hạ DFMEA và DVP&R xuống cấp phân hệ; RTM bao phủ 100 %`
  - `· Nộp bảng ánh xạ V-Model: mỗi khối có phép thử đối xứng`
- **Đầu vào:**
  - Mũi tên nét liền đậm từ nhánh `ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN` của Cổng `PDR-EVT (SE Lead)` đi vào cạnh phải.
  - Mũi tên nét đứt mảnh góc dưới bên trái từ nhánh `KHÔNG ĐẠT` của Cổng `CDR-EVT (PE Lead)`.
  - Mũi tên nét đứt mảnh phần giữa cạnh đáy từ nhánh `KHÔNG ĐẠT` của Cổng `SAR-EVT (CTO)` (kèm nhãn `KHÔNG ĐẠT — sửa thiết kế chi tiết`).
- **Đầu ra:**
  - Mũi tên nét liền đậm từ cạnh đáy đi xuống Cổng `CDR-EVT (PE Lead)`.

---

### 6. Khối 4 [C3–C4 / D3–D4]
- **Tên khối & Điều khoản:**  
  `4 · EVT — CHUẨN BỊ THỬ NGHIỆM — §5.5`
- **Các gạch đầu dòng:**
  - `· Lập kế hoạch thử chi tiết; hiệu chuẩn toàn bộ thiết bị đo`
  - `· Nghiệm thu đồ gá và kiểm kê đủ số lượng mẫu thử`
  - `· Đánh giá rủi ro thử nghiệm + kế hoạch dự phòng sự cố`
  - `· PE Lead ký xác nhận cấu hình mẫu đúng baseline đã khóa`
- **Đầu vào:**
  - Mũi tên nét liền đậm từ nhánh `ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN` của Cổng `CDR-EVT (PE Lead)` đi vào cạnh trái.
  - Mũi tên nét đứt mảnh từ nhánh `KHÔNG ĐẠT` của Cổng `TRR-EVT (QE Lead)` đi vào cạnh đáy.
- **Đầu ra:**
  - Mũi tên nét liền đậm từ cạnh phải dẫn sang Cổng `TRR-EVT (QE Lead)`.

---

### 7. Khối 5 [C7–C8 / D7–D8]
- **Tên khối & Điều khoản:**  
  `5 · EVT — TÍCH HỢP & THỬ NGHIỆM — §5.6`
- **Các gạch đầu dòng:**
  - `· Chế tạo, tích hợp mẫu EVT; chạy bench test theo DVP&R`
  - `· Chạy liên tục không lỗi ≥ T_min giờ; đo hotspots thực tế`
  - `· Tiền kiểm SFC và EMC pre-scan đạt biên ≥ 6 dB`
  - `· Đóng hết NCR trọng yếu chu kỳ A; cập nhật RTM, ICD`
- **Đầu vào:**
  - Mũi tên nét liền đậm từ nhánh `ĐẠT — được phép bắt đầu đo kiểm` của Cổng `TRR-EVT (QE Lead)` đi vào cạnh trái.
  - Mũi tên nét đứt mảnh từ nhánh `KHÔNG ĐẠT` của Cổng `SIR-EVT (PM)` đi vào cạnh phải.
- **Đầu ra:**
  - Mũi tên nét liền đậm từ cạnh đáy đi xuống Cổng `SIR-EVT (PM)`.

---

### 8. Các khối kết thúc luồng (Hình Oval)
- **Khối chuyển giai đoạn [E2–E3]:**  
  `GIAI ĐOẠN DVT`  
  `Mẫu chu kỳ B`  
  *(Nhận mũi tên nét liền đậm từ nhánh ĐẠT của Cổng SAR-EVT)*
- **Khối dừng / hủy [E1–E2]:**  
  `TẠM DỪNG / HỦY DỰ ÁN`  
  `§8.3 · §8.4`  
  *(Nhận mũi tên nét đứt mảnh từ nhánh HỦY DỰ ÁN của Cổng SAR-EVT)*

---

## IV. NGUYÊN VĂN TỪNG CỔNG SOÁT XÉT (GATES)

### 1. Cổng MCR (CTO) [A5–B5]
- **Tên cổng & Người phê duyệt:** `MCR (CTO)`
- **Câu hỏi xét duyệt:**  
  `Bài toán KD có`  
  `đáng đầu tư?`  
  `→ Điều lệ hiệu lực`
- **Các nhánh rẽ:**
  - **Nhánh ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN:**  
    - Nhãn chữ: `ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN — Điều lệ có hiệu lực`
    - Dạng nét: Nét liền đậm 0,5 mm.
    - Điểm xuất phát: Đỉnh bên phải hình thoi.
    - Hướng dẫn: Đi thẳng sang phải, cắm vào cạnh trái của Khối `1 · EVT — YÊU CẦU HỆ THỐNG — §5.2`.
  - **Nhánh KHÔNG ĐẠT:**  
    - Nhãn chữ: `KHÔNG ĐẠT — cập nhật BCA / Điều lệ`
    - Dạng nét: Nét đứt mảnh 0,25 mm.
    - Điểm xuất phát: Đỉnh đáy hình thoi.
    - Hướng dẫn: Đi xuống, rẽ trái chạy ngang dưới Khối 0, rồi rẽ lên cắm vào cạnh đáy Khối `0 · TIỀN KHẢ THI (Pre-A) — §4.2, §4.3, §5.1`.
  - **Nhánh HỦY:**  
    - *Ghi chú bản vẽ:* Theo Ghi chú (1), áp dụng tại mọi cổng do CTO quyết định, nhưng trên hình chỉ vẽ tường minh tại SAR-EVT để giữ độ rõ.

---

### 2. Cổng SRR-EVT (SE Lead) [B7–C7]
- **Tên cổng & Người phê duyệt:** `SRR-EVT (SE Lead)`
- **Câu hỏi xét duyệt:**  
  `Yêu cầu đã đủ &`  
  `đo được chưa?`  
  `→ Đóng băng SRS`
- **Các nhánh rẽ:**
  - **Nhánh ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN:**  
    - Nhãn chữ: `ĐẠT hoặc` / `ĐẠT CÓ ĐIỀU KIỆN`
    - Dạng nét: Nét liền đậm 0,5 mm.
    - Điểm xuất phát: Đỉnh bên trái hình thoi.
    - Hướng dẫn: Đi sang trái, cắm vào cạnh phải của Khối `2 · EVT — KIẾN TRÚC — §5.3`.
  - **Nhánh KHÔNG ĐẠT:**  
    - Nhãn chữ: `KHÔNG ĐẠT — sửa SRS / RTM`
    - Dạng nét: Nét đứt mảnh 0,25 mm.
    - Điểm xuất phát: Đỉnh bên phải hình thoi.
    - Hướng dẫn: Đi sang phải, rẽ lên trên, rẽ trái cắm vào cạnh phải của Khối `1 · EVT — YÊU CẦU HỆ THỐNG — §5.2`.

---

### 3. Cổng PDR-EVT (SE Lead) [B3–C4]
- **Tên cổng & Người phê duyệt:** `PDR-EVT (SE Lead)`
- **Câu hỏi xét duyệt:**  
  `Kiến trúc đã chốt`  
  `& khả thi chưa?`  
  `→ Đóng băng SAD/ICD`
- **Các nhánh rẽ:**
  - **Nhánh ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN:**  
    - Nhãn chữ: `ĐẠT hoặc` / `ĐẠT CÓ ĐIỀU KIỆN`
    - Dạng nét: Nét liền đậm 0,5 mm.
    - Điểm xuất phát: Đỉnh bên trái hình thoi.
    - Hướng dẫn: Đi sang trái, cắm vào cạnh phải của Khối `3 · EVT — THIẾT KẾ CHI TIẾT — §5.4`.
  - **Nhánh KHÔNG ĐẠT:**  
    - Nhãn chữ: `KHÔNG ĐẠT — sửa kiến trúc / tối ưu BOM`
    - Dạng nét: Nét đứt mảnh 0,25 mm.
    - Điểm xuất phát: Đỉnh đáy hình thoi.
    - Hướng dẫn: Đi xuống, rẽ phải chạy ngang, rẽ lên cắm vào cạnh đáy của Khối `2 · EVT — KIẾN TRÚC — §5.3`.

---

### 4. Cổng CDR-EVT (PE Lead) [C1–D2]
- **Tên cổng & Người phê duyệt:** `CDR-EVT (PE Lead)`
- **Câu hỏi xét duyệt:**  
  `Đủ chín để đặt`  
  `chế tạo mẫu chưa?`  
  `→ Đóng băng TK chi tiết`
- **Các nhánh rẽ:**
  - **Nhánh ĐẠT hoặc ĐẠT CÓ ĐIỀU KIỆN:**  
    - Nhãn chữ: `ĐẠT hoặc` / `ĐẠT CÓ ĐIỀU KIỆN`
    - Dạng nét: Nét liền đậm 0,5 mm.
    - Điểm xuất phát: Đỉnh bên phải hình thoi.
    - Hướng dẫn: Đi sang phải (vượt qua đường đứt mảnh bằng cung vượt - line jump), cắm vào cạnh trái của Khối `4 · EVT — CHUẨN BỊ THỬ NGHIỆM — §5.5`.
  - **Nhánh KHÔNG ĐẠT:**  
    - Dạng nét: Nét đứt mảnh 0,25 mm.
    - Điểm xuất phát: Đỉnh bên trái hình thoi.
    - Hướng dẫn: Đi sang trái, rẽ lên trên, cắm vào cạnh đáy góc bên trái của Khối `3 · EVT — THIẾT KẾ CHI TIẾT — §5.4`.
    - *Lưu ý về nhãn chữ:* ⚠ Tại đỉnh trái nhánh này không có nhãn chữ trực tiếp ngay sát đỉnh, nhưng tại cạnh đáy Khối 3 có nhãn `KHÔNG ĐẠT — sửa thiết kế chi tiết` nằm cạnh đường đứt mảnh hồi tiếp vào Khối 3.

---

### 5. Cổng TRR-EVT (QE Lead) [C5–D6]
- **Tên cổng & Người phê duyệt:** `TRR-EVT (QE Lead)`
- **Câu hỏi xét duyệt:**  
  `Đủ điều kiện an toàn`  
  `để bắt đầu đo?`  
  `→ Cấp quyền đo kiểm`
- **Các nhánh rẽ:**
  - **Nhánh ĐẠT:**  
    - Nhãn chữ: `ĐẠT — được phép` / `bắt đầu đo kiểm` *(Lưu ý: Không có chữ "ĐẠT CÓ ĐIỀU KIỆN")*
    - Dạng nét: Nét liền đậm 0,5 mm.
    - Điểm xuất phát: Đỉnh bên phải hình thoi.
    - Hướng dẫn: Đi sang phải, cắm vào cạnh trái của Khối `5 · EVT — TÍCH HỢP & THỬ NGHIỆM — §5.6`.
  - **Nhánh KHÔNG ĐẠT:**  
    - Nhãn chữ: `KHÔNG ĐẠT — hiệu chuẩn lại, bổ sung đồ gá`
    - Dạng nét: Nét đứt mảnh 0,25 mm.
    - Điểm xuất phát: Đỉnh đáy hình thoi.
    - Hướng dẫn: Đi xuống, rẽ trái chạy ngang dưới Khối 4, rẽ lên cắm vào cạnh đáy của Khối `4 · EVT — CHUẨN BỊ THỬ NGHIỆM — §5.5`.

---

### 6. Cổng SIR-EVT (PM) [E7–E8]
- **Tên cổng & Người phê duyệt:** `SIR-EVT (PM)`
- **Câu hỏi xét duyệt:**  
  `Tích hợp đã đạt`  
  `tiền kiểm chưa?`  
  *(Lưu ý: Không có dòng mũi tên `→ ...` như các cổng khác).*
- **Các nhánh rẽ:**
  - **Nhánh ĐẠT:**  
    - Nhãn chữ: `ĐẠT`
    - Dạng nét: Nét liền đậm 0,5 mm.
    - Điểm xuất phát: Đỉnh bên trái hình thoi.
    - Hướng dẫn: Đi sang trái, cắm vào đỉnh bên phải của Cổng `SAR-EVT (CTO)`.
  - **Nhánh KHÔNG ĐẠT:**  
    - Nhãn chữ: `KHÔNG ĐẠT — sửa mạch / FW,` / `tích hợp và tiền kiểm lại`
    - Dạng nét: Nét đứt mảnh 0,25 mm.
    - Điểm xuất phát: Đỉnh bên phải hình thoi.
    - Hướng dẫn: Đi sang phải, rẽ lên trên chạy dọc bên phải Khối 5, rẽ trái cắm vào cạnh phải của Khối `5 · EVT — TÍCH HỢP & THỬ NGHIỆM — §5.6`.

---

### 7. Cổng SAR-EVT (CTO) [D4–E5]
- **Tên cổng & Người phê duyệt:** `SAR-EVT (CTO)`
- **Câu hỏi xét duyệt:**  
  `Nghiệm thu EVT,`  
  `cho sang DVT?`
- **Các nhánh rẽ:**
  - **Nhánh ĐẠT:**  
    - Nhãn chữ: `ĐẠT — nghiệm thu` / `mẫu EVT`
    - Dạng nét: Nét liền đậm 0,5 mm.
    - Điểm xuất phát: Đỉnh bên trái hình thoi.
    - Hướng dẫn: Đi sang trái, cắm vào cạnh phải của oval `GIAI ĐOẠN DVT / Mẫu chu kỳ B`.
  - **Nhánh KHÔNG ĐẠT:**  
    - Nhãn chữ:  
      - Tại đoạn rẽ ngang phía dưới: `KHÔNG ĐẠT — sửa thiết kế, chế tạo lại mẫu, đo lại từ TRR`  
      - Tại đoạn rẽ đứng đi vào đáy Khối 3: `KHÔNG ĐẠT — sửa thiết kế chi tiết`
    - Dạng nét: Nét đứt mảnh 0,25 mm.
    - Điểm xuất phát: Đỉnh trên (đỉnh ngọn) hình thoi.
    - Hướng dẫn: Đi lên trên, rẽ trái chạy ngang dài bên dưới Khối 4, rẽ lên qua cung vượt (giao cắt không nối với đường CDR-EVT → Khối 4), rẽ trái rồi rẽ lên cắm vào cạnh đáy Khối `3 · EVT — THIẾT KẾ CHI TIẾT — §5.4`.
  - **Nhánh HỦY DỰ ÁN:**  
    - Nhãn chữ: `HỦY DỰ ÁN — CTO quyết định`
    - Dạng nét: Nét đứt mảnh 0,25 mm.
    - Điểm xuất phát: Đỉnh đáy hình thoi.
    - Hướng dẫn: Đi xuống, rẽ trái chạy ngang dài sát mép trên khung ghi chú ở đáy bản vẽ, rẽ lên cắm vào cạnh đáy của oval `TẠM DỪNG / HỦY DỰ ÁN / §8.3 · §8.4`.

---

## V. ĐỐI CHIẾU CÁC ĐIỂM NGHI VẤN / ĐÁNH DẤU CẢNH BÁO ⚠

1. **⚠ Ký hiệu `T_min` tại Khối 5:**
   - Text trên hình: `Chạy liên tục không lỗi ≥ T_min giờ; đo hotspots thực tế`
   - Nhận định: Dấu gạch dưới `_` nối giữa `T` và `min` (`T_min`), ký hiệu thời gian thử nghiệm tối thiểu.

2. **⚠ Biên độ EMC tại Khối 5:**
   - Text trên hình: `Tiền kiểm SFC và EMC pre-scan đạt biên ≥ 6 dB`
   - Phương án đọc khả dĩ: Biên an toàn (margin) EMC $\ge 6\text{ dB}$.

3. **⚠ Nhãn nhánh KHÔNG ĐẠT tại Cổng CDR-EVT và đường vào Khối 3:**
   - Tại đỉnh trái Cổng CDR-EVT: Nét đứt rẽ trái rồi đi thẳng lên cắm vào đáy bên trái Khối 3 không có dòng chữ chú thích nằm ngay trên cung rẽ trái.
   - Tại điểm cắm vào đáy Khối 3 (ở giữa-phải): Có nhãn `KHÔNG ĐẠT — sửa thiết kế chi tiết`. Nét này nối thông từ đường hồi tiếp của Cổng SAR-EVT (`KHÔNG ĐẠT — sửa thiết kế, chế tạo lại mẫu, đo lại từ TRR`).
   - Phương án đọc: Nhãn `KHÔNG ĐẠT — sửa thiết kế chi tiết` là mô tả nội dung công việc khi quay lại Khối 3 (áp dụng cho cả sửa từ CDR hoặc sửa vòng lặp lớn từ SAR).
