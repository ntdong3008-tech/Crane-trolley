# QUY CHUẨN THIẾT KẾ SLIDE POWERPOINT BÁO CÁO TIẾN ĐỘ & SOÁT XÉT CỔNG KỸ THUẬT HỆ THỐNG (`SLIDE_PPTX_RULES_SE.md`)

**Dự án áp dụng:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Di Chuyển Ngang Xe Con Cầu Trục ($x = 2$)  
**Nhóm thực hiện:** Nhóm 8.5-EMG | **PM / SE Lead:** Nghiêm Trọng Đông (MSSV: 20232001) | **Doc Lead:** Nguyễn Hải Trung (MSSV: 20232344)  
**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Template PowerPoint chuẩn bắt buộc:** `D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project\Báo cáo hàng tuần\Mô tả nguyên lý công nghệ.pptx` (Template ĐHBKHN 16:9)  
**Phạm vi áp dụng:** Chuẩn hóa phương pháp chuyển đổi các báo cáo kỹ thuật dài (`.md` / `.pdf`: `PRD`, `SOW`, `BCA/QFD/HoQ/ICE`, `SRS Baseline A`, `Boundary & P-Diagram`, `RTM & DVP&R L0`) thành bộ Slide PowerPoint (`.pptx`) báo cáo tiến độ và bảo vệ qua các cổng **Khối 0 (`MCR`)** và **Khối 1 (`SRR-EVT`)**.

---

## 1. TẠI SAO BÁO CÁO GỐC RẤT DÀI NHƯNG SLIDE PHẢI CÔ ĐỌNG? (BẢN CHẤT CỦA GATE REVIEW DECK)

Trong Kỹ thuật Hệ thống (*Systems Engineering — SE*), người mới thường mắc lỗi **"Slideument"** (biến Slide PowerPoint thành file Word dán lên màn chiếu): copy nguyên văn các đoạn văn dài và các bảng 15–20 dòng từ báo cáo `.md` sang PowerPoint. Hậu quả là Hội đồng nghiệm thu / Giảng viên hướng dẫn không thể đọc kịp trong 1–2 phút/slide, còn người thuyết trình lại rơi vào thế "đọc lại chữ trên màn hình".

Để giải quyết triệt để mâu thuẫn giữa **Báo cáo kỹ thuật gốc rất dài (đầy đủ minh chứng)** và **Slide thuyết trình phải súc tích, dễ theo dõi**, tài liệu quy chuẩn này tích hợp **4 hệ tiêu chuẩn quốc tế** cùng **Template chuẩn Đại học Bách Khoa Hà Nội (`Mô tả nguyên lý công nghệ.pptx`)**:

1. **Chuẩn Soát xét Cổng Vòng đời Dự án của NASA & INCOSE:**
   * `[Chuẩn: NASA Systems Engineering Handbook (NASA/SP-2016-6105 Rev 2), Section 6.7 & Appendix G, https://soma.larc.nasa.gov/lws/pdf_files/12%20NASA_SP-2016-6105%20Rev%202.pdf]`
   * `[Chuẩn: NASA/SP-2007-6105 Rev 1, Section 6.7, Table 6.7-4 (MCR) & Table 6.7-5 (SRR), https://ntrs.nasa.gov/api/citations/20080008301/downloads/20080008301.pdf]`
   * `[Chuẩn: NASA NPR 7120.5F & NPR 7123.1D — Systems Engineering Processes and Requirements, https://nodis3.gsfc.nasa.gov/displayDir.cfm?t=NPR&c=7123&s=1B]`
   * `[Nội bộ: FLOW_REVIEW.md, Khối 0 (MCR) & Khối 1 (SRR-EVT)]`
   * **Nguyên lý cốt lõi:** Báo cáo tiến độ ở cuối mỗi Khối không phải là "kể lể nhóm đã viết bao nhiêu trang", mà là buổi **Soát xét Qua Cổng (*Gate Review*)** để chứng minh dự án đã hoàn thành 100% gạch đầu dòng công việc của Khối và thỏa mãn bộ **Tiêu chí Đóng Cổng (*Exit / Success Criteria*)** nhằm xin chữ ký **`ĐẠT (PASS)`** chuyển sang Khối tiếp theo.
2. **Mô hình *Assertion-Evidence (Khẳng định – Minh chứng)* trong Thuyết trình Kỹ thuật:**
   * `[Chuẩn: GS. Michael Alley (Penn State University) — The Craft of Scientific Presentations / Assertion-Evidence Approach, https://www.craftscicom.org/ & https://writing.engr.psu.edu/speaking.html]`
   * **Nguyên lý cốt lõi:** Mỗi slide kỹ thuật chỉ gồm **2 phần chính trong vùng nội dung**:
     * **Assertion (Câu khẳng định Action Title đặt ngay dưới vạch kẻ đỏ của Template ĐHBKHN):** Một câu hoàn chỉnh (Chủ ngữ + Động từ + Ngưỡng số học/Kết luận, tối đa 2 dòng) nêu bật thông điệp cốt lõi của slide.
     * **Visual Evidence (Minh chứng trực quan ở Thân slide):** Sơ đồ khối, lưu đồ, hình ảnh minh họa hoặc bảng ma trận đã tinh gọn; hạn chế tối đa gạch đầu dòng văn xuôi (*bullet points*).
3. **Nguyên lý Kim Tự Tháp Minto (*Minto Pyramid Principle*) & *Action Titles*:**
   * `[Chuẩn: Barbara Minto — The Pyramid Principle / McKinsey Action Title Methodology]`
   * **Nguyên lý cốt lõi (BLUF — *Bottom Line Up Front*):** Luôn đưa **Kết luận / Con số chốt** lên đầu tiên (ở dòng Action Title và dòng tổng hợp trên cùng), sau đó mới phân rã thành 3–4 trụ cột chứng minh bên dưới. Khi đọc lướt liên tiếp tất cả các dòng Action Title từ Slide 2 đến Slide cuối, người chấm phải nắm được trọn vẹn 100% mạch câu chuyện (*Horizontal Storyline*) mà chưa cần đọc thân slide.
4. **Quy tắc Phân tầng Hồ sơ 80/20 (*Two-Tier Deck: Main Deck vs. Backup/Appendix Deck*):**
   * `[Chuẩn: NASA Project Lifecycle Reviews Reference Guide (2024), https://www.nasa.gov/wp-content/uploads/2024/12/project-lifecycle-reviews-2024-fnl-11272024.pdf]`
   * **Nguyên lý cốt lõi:** Không bỏ đi bất kỳ dữ liệu quý nào của báo cáo `.md`, nhưng **tách bộ Slide thành 2 tầng**:
     * **Tầng 1 — Main Review Deck (`14–16 Slides`, kết thúc bằng Slide `THANK YOU !` Layout 4 của ĐHBKHN):** Dành cho 15–20 phút thuyết trình chính thức. Chỉ đưa lên mặt slide **Sơ đồ tổng hợp, Top các chỉ tiêu quan trọng nhất, Quy luật phân rã và Bảng tóm tắt $\le 7\text{--}8$ hàng**.
     * **Tầng 2 — Backup / Appendix Deck (`6 Slides` đặt ngay sau Slide `THANK YOU !`):** Chứa các bảng tra cứu đầy đủ đã chia nhỏ vừa màn hình (như bảng 9 Case Studies, ma trận HoQ 8×8, nguyên văn 14 câu `SRS`, chi tiết 14 bài đo `DVP&R L0`, công thức lọc đạo hàm $\rho(t)$). Khi Giảng viên / Hội đồng hỏi xoáy vào một chi tiết cụ thể, nhóm bấm nhảy ngay tới Slide Backup tương ứng để bảo vệ.

---

## 2. MƯỜI HAI QUY TẮC ĐỊNH LƯỢNG BẮT BUỘC KHI THIẾT KẾ SLIDE (12 GOLDEN RULES)

### Quy tắc 1: Kế thừa 100% Template ĐHBKHN (`Mô tả nguyên lý công nghệ.pptx`) & Cấu trúc 4 Layout Gốc
`[Nội bộ: Báo cáo hàng tuần\Mô tả nguyên lý công nghệ.pptx & SRS-diagram.pptx]`
Mọi file PowerPoint tạo ra cho **Khối 0 (`Gate MCR`)** và **Khối 1 (`Gate SRR-EVT`)** bắt buộc lấy trực tiếp file `Mô tả nguyên lý công nghệ.pptx` làm **Template gốc** với kích thước màn hình rộng **16:9 (`13.33 in × 7.50 in` = `12192000 × 6858000 EMU`)** và sử dụng đúng **4 Slide Layouts của ĐHBKHN**:

| Mã Layout trong Template | Tên Layout (`cSld name`) | Ảnh nền tích hợp (`ppt/media/`) | Công năng bắt buộc trong Báo cáo Gate Review |
| :--- | :--- | :--- | :--- |
| **`slideLayout1.xml`** | `1_Title and Content` | `image1.png` *(Nền trắng, vòng tròn chấm đỏ ĐHBKHN bên phải, chữ "ONE LOVE. ONE FUTURE." góc dưới trái)* + Logo `image5.png` | **Chỉ dùng cho Slide 1 (Trang Bìa):** Giữ nguyên 100% bố cục, màu sắc (`#C00000`), Logo ĐHBKHN, tên đề tài, tên nhóm `NHÓM 8.5-EMG`, danh sách 6 thành viên + MSSV và GVHD `TS. Nguyễn Duy Đỉnh` của Slide 1 gốc; chỉ bổ sung 1 dòng phụ đề nhỏ ghi tên Khối/Gate. |
| **`slideLayout2.xml`** | `1_Section Header` | `image2.png` *(Thanh Header Xanh Navy `#0E2841` trên cùng, vạch kẻ đỏ `#C00000` dưới Header, nền trắng ở giữa, góc dưới trái có Logo + Tên trường ĐHBKHN và vạch kẻ đỏ ngang)* | **Dùng cho các Slide Nội dung Chính (`Slide 2 .. N-1`) và các Slide Backup (`B-01 .. B-06`):** Hiển thị tiêu đề phần trên thanh xanh và nội dung 1 cột hoặc 2 cột bên dưới. |
| **`slideLayout3.xml`** | `1_Comparison` | `image3.png` *(Tương tự `slideLayout2` nhưng tối ưu cho bố cục đối sánh 2 cột / trích dẫn)* | **Dùng thay thế linh hoạt với `slideLayout2`** cho các slide so sánh 2 bên (In-Scope vs. Out-of-Scope, Mô tả công nghệ + Hình ảnh, Tài liệu tham khảo). |
| **`slideLayout4.xml`** | `1_Content with Caption` | `image4.png` *(1/3 bên trái là mảng Xanh Navy đậm `#0E2841` kèm vòng tròn chấm đỏ + chữ `HUST` trắng + `hust.edu.vn`; 2/3 bên phải nền trắng)* | **Chỉ dùng cho Slide Kết thúc Main Deck (`THANK YOU !` & `Q&A`):** Đặt ngay trước phân vùng `Backup / Appendix Slides`. |

---

### Quy tắc 2: Quy chuẩn Bắt buộc cho `Slide 1 (Trang Bìa)` — Clone 100% từ `Mô tả nguyên lý công nghệ.pptx`
`[Nội bộ: Mô tả nguyên lý công nghệ.pptx, ppt/slides/slide1.xml]`
Trang đầu tiên (`Slide 1`) của mọi báo cáo `.pptx` phải giữ nguyên **chính xác toạ độ, danh sách thành viên và định dạng** của Slide 1 trong file `Mô tả nguyên lý công nghệ.pptx`:
1. **Logo ĐHBKHN (`image5.png`):** Đặt tại `pos = (1.00", 0.37")`, `size = (2.23" × 0.67")`.
2. **Tiêu đề Đề tài Chính (`Shape 102`):** Đặt tại `pos = (0.81", 1.75")`, `size = (9.71" × 1.40")`, chữ **IN HOA ĐẬM (`44pt–48pt Bold`)**, màu Đỏ Bách Khoa **`#C00000`**:
   * Nội dung: **`THIẾT KẾ HỆ TRUYỀN ĐỘNG CƠ CẤU XE CON CẦU TRỤC`**
3. **Dòng Phụ đề Định danh Khối & Cổng (`Subtitle Box` bổ sung ngay dưới tiêu đề chính):** Đặt tại `pos = (0.81", 3.18")`, `size = (9.71" × 0.48")`, cỡ chữ **`20pt–22pt Bold`**, màu Xanh Navy ĐHBKHN **`#0E2841`**:
   * Với Khối 0: **`BÁO CÁO TIẾN ĐỘ KHỐI 0 — SOÁT XÉT CỔNG MCR (PRD, CASE STUDY, SOW & QFD/HoQ/ICE)`**
   * Với Khối 1: **`BÁO CÁO TIẾN ĐỘ KHỐI 1 — SOÁT XÉT CỔNG SRR-EVT (SRS BASELINE A, BOUNDARY/P-DIAGRAM & RTM/DVP&R L0)`**
4. **Tên Nhóm (`Shape 106`):** Đặt tại `pos = (0.81", 3.79")`, `size = (4.29" × 0.39")`, cỡ chữ **`20pt Bold`**, màu **`#C00000`**:
   * Nội dung: **`NHÓM 8.5-EMG`** *(Phương án 8 — Biến số $x = 2$: $Q = 12,222\text{ kg}$)*
5. **Danh sách 6 Thành viên (`Shape 103`) & Cột MSSV (`Shape 104`):** Đặt song song tại `pos_name = (0.81", 4.19"), size = (3.50" × 1.65")` và `pos_id = (4.38", 4.19"), size = (1.60" × 1.65")`, cỡ chữ **`20pt`**, màu **`#C00000`**, giữ nguyên thứ tự 6 thành viên:
   * `Nguyễn Bá Hưng` — `20232107`
   * `Đặng Nguyên Bình` — `20231937`
   * `Trần Đỗ Khải` — `20232131`
   * `Phạm Văn Hưng` — `20232109`
   * `Nguyễn Hải Trung` — `20232344`
   * `Nghiêm Trọng Đông` — `20232001`
6. **Giảng viên Hướng dẫn (`Shape 105`):** Đặt tại `pos = (0.68", 6.18")`, `size = (6.50" × 0.55")`, cỡ chữ **`20pt Bold`**, màu **`#C00000`**:
   * Nội dung: **`Giảng viên hướng dẫn: TS. Nguyễn Duy Đỉnh`**

---

### Quy tắc 3: Cấu trúc Khung 4 Vùng trên Các Slide Nội Dung (`Slide 2 .. N`) theo Template ĐHBKHN
`[Chuẩn: Assertion-Evidence & Template ĐHBKHN slideLayout2/slideLayout3]`
Để không đè lên dải băng xanh trên cùng (`y = 0.00"–0.68"`), vạch kẻ đỏ (`y ≈ 0.80"`) và Logo ĐHBKHN ở góc dưới trái (`y = 6.85"–7.45"`) của ảnh nền `image2.png`/`image3.png`, mọi slide nội dung bắt buộc tuân thủ toạ độ **4 vùng cố định** sau:

1. **Vùng 1 — Thanh Header Xanh Đậm Trên Cùng (`Top Navy Banner`, `pos = (0.30", 0.10")`, `size = (12.65" × 0.49")`):**
   * Nằm gọn trong dải băng màu xanh đậm `#0E2841` trên cùng của Template.
   * Định dạng: Chữ **IN HOA ĐẬM (`24pt–28pt Bold`)**, màu **Trắng (`#FFFFFF` / `scheme:lt1`)**, chỉ **1 dòng duy nhất**.
   * Cấu trúc nội dung: **`[SỐ THỨ TỰ MỤC]. [TÊN PHẦN BÁO CÁO IN HOA] | [MÃ CỔNG / MÃ SOW]`**
   * *Ví dụ Khối 0:* `1. TÀI LIỆU YÊU CẦU SẢN PHẨM (PRD) | GATE MCR` hoặc `4. PHÂN TÍCH QFD, MA TRẬN HOQ & LỰA CHỌN PHƯƠNG ÁN (ICE)`
   * *Ví dụ Khối 1:* `1. SƠ ĐỒ BIÊN (BOUNDARY) & P-DIAGRAM | GATE SRR-EVT` hoặc `2. ĐẶC TẢ YÊU CẦU HỆ THỐNG (SRS BASELINE A)`
2. **Vùng 2 — Dòng Action Title Khẳng Định Ngay Dưới Vạch Đỏ (`Assertion Banner`, `pos = (0.34", 0.88")`, `size = (12.65" × 0.65")`):**
   * Đặt ngay bên dưới đường kẻ ngang màu đỏ của Template ĐHBKHN.
   * Định dạng: Cỡ chữ **`20pt–22pt Bold`**, màu **Đỏ Bách Khoa (`#C00000`)** hoặc **Xanh Navy (`#0E2841`)**, tối đa **`2 dòng (≤ 22 từ)`**.
   * ❌ **Cấm viết kiểu nhãn đề mục cụt lủn:** *"Chấm điểm Ma trận ICE"* hay *"Sơ đồ P-Diagram"*.
   * ✅ **Bắt buộc viết câu khẳng định hoàn chỉnh có số liệu (Assertion-Evidence):** *"Chấm điểm ICE (gắn trọng số HoQ) chốt chọn Solution C (KĐB + FOC + Encoder + S-Curve) đạt 812/1000 điểm"*.
3. **Vùng 3 — Thân Slide / Minh Chứng Trực Quan (`Visual Evidence Zone`, `pos_y = 1.58" .. 6.65"`, chiều rộng `12.65"` từ `x = 0.34"` đến `x = 12.99"`):**
   * Chiếm 70% diện tích trung tâm trên nền trắng của slide.
   * Bố trí theo **1 trong 3 dạng lưới chuẩn**:
     * **Lưới 2 Cột (`Split 50/50` hoặc `55/45`):** Cột trái (`x = 0.34", w = 5.90"`) chứa Bảng tinh gọn / Luận điểm kỹ thuật; Cột phải (`x = 6.40", w = 6.50"`) chứa Hình ảnh minh họa / Sơ đồ khối kèm chú thích `Hình X. ...` ở `y = 6.15"–6.60"`.
     * **Lưới Bảng Tổng Hợp + Hộp Chốt (`Table + Takeaway Box`):** Phía trên (`y = 1.58"–5.65"`) là Bảng ma trận $\le 7\text{--}8$ hàng rộng `12.65"`; phía dưới (`y = 5.75"–6.60"`) là Hộp kết luận viền đỏ/xanh ghi ý nghĩa vật lý & truy vết.
     * **Lưới 3 Thẻ Ngang (`3-Card Grid`):** 3 hộp nội dung đặt cạnh nhau (`w = 4.05"` mỗi hộp) dùng cho phân tích `ConOps`, `3 Câu hỏi nghiên cứu Case Study (CQ1, CQ2, CQ3)` hoặc `4 Kịch bản DVP&R (TS-01..04)`.
4. **Vùng 4 — Chân Trang Phải & Số Trang (`Right Footer & Slide Number`, `pos = (6.50", 7.12")`, `size = (6.45" × 0.35")`):**
   * **Lưu ý cực kỳ quan trọng:** Góc dưới bên trái của nền `slideLayout2` và `slideLayout3` (`x = 0.25" .. 2.95", y = 6.85" .. 7.45"`) **đã in sẵn Logo và tên trường ĐẠI HỌC BÁCH KHOA HÀ NỘI**, kèm đường kẻ đỏ chạy ngang từ `x = 3.03"` đến `12.98"` ở `y ≈ 7.05"`.
   * Do đó, **tuyệt đối không đặt hộp chữ Footer đè lên góc dưới bên trái!** Thông tin quản lý cấu hình và số trang phải đặt gọn ở **nửa bên phải phía trên/dưới vạch đỏ (`x = 6.50" .. 12.95"`)** hoặc trong ô `sldNum` (`pos = (10.01", 7.19")`):
     * Mẫu hiển thị góc dưới phải: `Nhóm 8.5-EMG (x=2) | Gate MCR/SRR | Slide X / N [Backup: B-xx]` (cỡ chữ `11pt–12pt`).

---

### Quy tắc 4: Quy chuẩn Font Chữ Tiếng Việt Chống Lỗi Dấu & Bảng Phân Cấp Cỡ Chữ (`Typography & Vietnamese Font Safety`)
`[Nội bộ: Khắc phục lỗi nhảy font Lato/Arial trong Mô tả nguyên lý công nghệ.pptx]`

#### 4.1. Nguyên nhân lỗi Font tiếng Việt và Quy định Font chuẩn bắt buộc
Trong file `Mô tả nguyên lý công nghệ.pptx` gốc (xuất từ Google Slides), một số hộp chữ dùng font **`Lato`** trong khi Theme gốc (`theme1.xml`) khai báo **`Arial`**. Trên nhiều máy tính Windows, bản cài đặt `Lato` không chứa đủ bảng mã Unicode Tiếng Việt tổ hợp (`ă, â, đ, ê, ô, ơ, ư` kèm 5 dấu thanh) và thiếu các ký hiệu toán học kỹ thuật (`≤, ≥, ≠, ±, Δ, ω, ρ, η, λ, Σ`), dẫn đến PowerPoint tự động nhảy chữ cao chữ thấp sang font khác.

Để **chống lỗi dấu Tiếng Việt và lỗi ký hiệu toán học 100%** trên mọi máy tính của Hội đồng và GVHD:
1. **Font Chính Bắt Buộc (`Primary Font` — Mặc định khi tạo `.pptx`):** **`Arial`** hoặc **`Segoe UI`**
   * *Lý do:* Có sẵn 100% trong nhân Windows & Microsoft Office, khớp trực tiếp với `majorFont = Arial` / `minorFont = Arial` trong `theme1.xml` của `Mô tả nguyên lý công nghệ.pptx`, hiển thị sắc nét tuyệt đối cả dấu Tiếng Việt lẫn công thức vật lý (`v = 0,12 m/s`, `a ≤ 0,50 m/s²`, `ρ ≤ 2,00 m/s³`, `M_Σ = 14.244 kg`).
2. **Font Thay Thế Hiện Đại (Chỉ dùng khi máy trình chiếu đã cài đặt sẵn Font):** **`Roboto`** hoặc **`Be Vietnam Pro`** (tuyệt đối không dùng font `Lato` cho các đoạn nội dung tiếng Việt có chứa công thức toán học).
3. **Font Mã Định Danh Kỹ Thuật (`PRD-FUNC-01`, `SRS-PERM-03`, `DVP-L0-01`):** **`Arial Bold`** hoặc **`Consolas Bold`**.

#### 4.2. Bảng Phân Cấp Cỡ Chữ Khóa Cứng (`Locked Font-Size Hierarchy`)
Không một slide nào được phép dùng cỡ chữ tùy tiện ngoài bảng chuẩn dưới đây:

| Thành phần trên Slide | Vị trí / Vùng hiển thị | Font & Kiểu chữ (`Style`) | Cỡ chữ chuẩn (`pt`) | Màu chữ chuẩn (`Hex`) | Giới hạn dòng / Quy tắc bắt buộc |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **1. Tên Đề Tài Chính (Slide 1)** | Giữa trái Trang bìa (`pos=(0.81", 1.75")`) | `Arial` / `Segoe UI` **Bold, ALL CAPS** | **`44pt – 48pt`** | Đỏ ĐHBKHN **`#C00000`** | Tối đa 2–3 dòng |
| **2. Phụ Đề Khối / Gate (Slide 1)** | Ngay dưới tên đề tài (`pos=(0.81", 3.18")`) | `Arial` / `Segoe UI` **Bold** | **`20pt – 22pt`** | Xanh Navy **`#0E2841`** | Tối đa 1–2 dòng |
| **3. Nhóm, Thành Viên, MSSV, GVHD (Slide 1)** | Nửa dưới Trang bìa (`y = 3.79" .. 6.18"`) | `Arial` / `Segoe UI` **Regular / Bold** | **`20pt`** | Đỏ ĐHBKHN **`#C00000`** | Giữ nguyên 6 thành viên & MSSV |
| **4. Tiêu Đề Thanh Header Xanh (`Section Header`)** | Trên dải băng xanh (`pos=(0.30", 0.10")`) | `Arial` / `Segoe UI` **Bold, ALL CAPS** | **`24pt – 28pt`** | Trắng **`#FFFFFF`** | **Đúng 1 dòng duy nhất** |
| **5. Câu Khẳng Định `Action Title` (`Assertion`)** | Ngay dưới vạch đỏ (`pos=(0.34", 0.88")`) | `Arial` / `Segoe UI` **Bold** | **`20pt – 22pt`** | Đỏ **`#C00000`** hoặc Xanh **`#0E2841`** | **Tối đa 2 dòng ($\le 22$ từ)** |
| **6. Tiêu Đề Mục Con / Nhãn Khối (`Sub-heading`)** | Đầu cột hoặc đầu hộp (`Visual Zone`) | `Arial` / `Segoe UI` **Bold** | **`18pt – 20pt`** | Xanh đậm **`#0E2841`** / **`#156082`** | Ngắn gọn $\le 8$ từ |
| **7. Văn Bản Thân Bài (`Body Bullet Text`)** | Trong các cột nội dung hoặc hộp | `Arial` / `Segoe UI` **Regular** (in đậm từ khóa) | **`16pt – 18pt`** | Đen **`#000000`** / Xám đậm **`#202122`** | **Cấm nhỏ hơn `16pt`**; mỗi ý $\le 2$ dòng |
| **8. Tiêu Đề Bảng (`Table Header Row`)** | Hàng đầu tiên của bảng dữ liệu | `Arial` / `Segoe UI` **Bold** | **`15pt – 16pt`** | Chữ Trắng **`#FFFFFF`** trên nền **`#0E2841`** | Căn giữa hoặc căn trái rõ ràng |
| **9. Nội Dung Ô Trong Bảng (`Table Data Cell`)** | Các hàng dữ liệu của bảng ($\le 7\text{--}8$ hàng) | `Arial` / `Segoe UI` **Regular / Bold** | **`14pt – 15pt`** | Đen **`#000000`** (Tô nền vàng `#FEF9E7` hàng chốt) | **Cấm nhỏ hơn `14pt`**; mỗi ô $\le 10$ từ |
| **10. Chú Thích Hình Ảnh / Bảng (`Figure Caption`)** | Ngay dưới khung hình ảnh (`Hình X. ...`) | `Arial` / `Segoe UI` **Italic / Bold** | **`14pt – 16pt`** | Xanh đậm **`#0E2841`** / Đen **`#000000`** | Ghi rõ `Hình X. [Tên hình] (Nguồn: ...)` |
| **11. Chân Trang Phải & Số Trang (`Slide Number`)** | Góc dưới phải (`pos=(6.50"..12.95", 7.12")`) | `Arial` / `Segoe UI` **Regular** | **`11pt – 13pt`** | Xám đậm **`#595959`** / Đỏ **`#C00000`** | Không chạm vào Logo ĐHBKHN bên trái |
| **12. Chữ `THANK YOU !` (Slide Kết thúc)** | Bên phải `slideLayout4` (`pos=(6.39", 3.30")`) | `Arial` / `Segoe UI` **Bold** | **`54pt – 60pt`** | Đỏ ĐHBKHN **`#C00000`** | Kèm dòng phụ `Q&A — Hội đồng Gate Review` (`22pt`) |

---

### Quy tắc 5: Quy chuẩn Khung Chờ Tự Chèn Hình Ảnh (`[GHI CHÚ CHÈN HÌNH ẢNH CHO NGƯỜI DÙNG]`)
`[Nội bộ: Yêu cầu cá nhân hóa của User — Để trống khung Placeholder kèm chỉ dẫn rõ ràng để tự chèn ảnh]`
Trong cả báo cáo kịch bản `.md` lẫn khi yêu cầu AI sinh file `.pptx`, **không tự ý nhét hình vẽ sai lệch hoặc làm vỡ bố cục**, mà bắt buộc tuân thủ cơ chế **Khung Chờ Chèn Ảnh (`Image Placeholder Box`)**:
1. **Trong file Báo cáo Kịch bản Slide (`.md`):** Tại mỗi slide có hình ảnh hoặc sơ đồ, phải có một mục riêng biệt đánh dấu bằng biểu tượng **`🖼️ [GHI CHÚ CHÈN HÌNH ẢNH CHO NGƯỜI DÙNG]`** ghi rõ 3 thông tin:
   * **Tên & Chú thích hình (`Caption`):** Ví dụ `Hình 3.1. Mô hình động lực học xe con và tải treo con lắc`.
   * **Nguồn lấy ảnh có sẵn trong máy:** Chỉ đích danh đường dẫn file ảnh rời (ví dụ `Báo cáo hàng tuần\Hinh_3_1_Co_cau_xe_con.jpg`), hoặc copy từ Slide số mấy của file `Mô tả nguyên lý công nghệ.pptx` (Hình 1 đến Hình 12 tại các Slide 3, 4, 5, 6, 8, 11, 12, 13, 14, 15, 16, 17) hay `SRS-diagram.pptx` (các ảnh cắt Sơ đồ biên & P-Diagram tại các Slide 5, 6, 7, 8, 9).
   * **Vị trí & Kích thước Khung chờ trên Slide (`pos` & `size`):** Ví dụ `pos = (6.40", 1.60")`, `size = (6.50" × 4.30")` kèm hộp chú thích ở `pos = (6.40", 6.00")`.
2. **Khi AI tạo file `.pptx` tự động:** AI phải vẽ tại đúng toạ độ đó một **Khung chữ nhật nền xám nhạt (`#F8F9FA`), viền nét đứt màu Đỏ/Xanh (`1.5pt Dashed Border`)**, bên trong ghi rõ dòng nhắc: `[CHÈN HÌNH X TẠI ĐÂY — Nguồn: ...]` và đặt sẵn hộp chữ `Hình X. ...` ở ngay bên dưới để người dùng chỉ cần click chuột phải $\to$ *Change Picture* hoặc Paste ảnh vào là khớp 100%.

---

### Quy tắc 6: Kế thừa Mạch Nội dung `Mô tả nguyên lý công nghệ.pptx` & Hiệu đính 100% Số liệu Lệch theo `SE_RULES.md`
`[Nội bộ: Đối chiếu Mô tả nguyên lý công nghệ.pptx với PRD v3.0, SRS Baseline A v1.0 & SE_RULES.md]`
Qua rà soát kỹ thuật file `Mô tả nguyên lý công nghệ.pptx` (24 slides) và `SRS-diagram.pptx` (10 slides) trong thư mục `Báo cáo hàng tuần`, có **6 điểm lệch hoặc thiếu dữ liệu** giữa bản nháp hàng tuần và bộ hồ sơ chuẩn `SE_Hoc` mà **bắt buộc phải hiệu đính khi lên Slide Gate Review**:

| STT | Nội dung trong file `.pptx` tuần cũ (`Báo cáo hàng tuần`) | Điểm lệch / Lỗi tiềm ẩn khi xét duyệt Gate Review | Chuẩn hóa bắt buộc trong Báo cáo Slide `SE_Hoc` (`Block 0` & `Block 1`) |
| :---: | :--- | :--- | :--- |
| **1** | **Slide 15 & 16 (`Mô tả nguyên lý công nghệ.pptx`):** Ghi khối lượng xe con là *`3 – 4 tấn`*, hàng hóa treo móc cáp là *`12,444 kg`*, tổng hệ khối lượng là *`~16 tấn`*. | Mâu thuẫn trực tiếp với `PRD v3.0`, `BCA/QFD/HoQ` và `SRS Baseline A` (nơi tự trọng xe con đã khóa theo Catalogue KG-Cranes/Sungdo 15t là $m_{xc} = 1,800\text{ kg}$). Hội đồng sẽ bắt lỗi "Tại sao mỗi nơi một số?". | **Hiệu đính thống nhất 100%:** Tải định mức $Q = 12,222\text{ kg}$, bộ phận mang tải $m_{nh} = 222\text{ kg}$ ($\Rightarrow$ tổng khối lượng treo cáp $m_{\text{treo}} = 12,444\text{ kg}$), tự trọng xe con $m_{xc} = 1,800\text{ kg} \Longrightarrow$ **Tổng khối lượng chuyển động đầy tải $M_\Sigma = 14,244\text{ kg}$** ($F_{c.\text{đầy}} \approx 27,947\text{ N}$) và **không tải $m_{\text{tĩnh}} = 2,022\text{ kg}$** ($F_{c.\text{không}} \approx 3,967\text{ N}$, tỷ số biến thiên tải $7.04\text{ lần}$). |
| **2** | **Slide 16 (`Mô tả nguyên lý công nghệ.pptx`):** Ghi tốc độ bò định vị là *`v_min ≈ 0.01 – 0.02 m/s`*. | Lệch với ngưỡng đã khóa tại `PRD-FUNC-03`, `EC-02` và `SRS-FUNC-02` ($v_{\text{creep}} \in [0.030;\ 0.036]\text{ m/s}$, tương ứng $25\% \div 30\%\ v_{\max}$ với dải điều chỉnh $D \ge 10:1$). | **Hiệu đính thống nhất 100%:** Ghi rõ tốc độ định mức $v_{\max} = 0.12\text{ m/s}$ ($7.2\text{ m/phút}$), cấp **tốc độ bò định vị $v_{\text{creep}} \in [0.030;\ 0.036]\text{ m/s}$** ($25\% \div 30\%\ v_{\max}$) và **dải điều chỉnh tốc độ $D = \omega_{\max}/\omega_{\min} \ge 10:1$** ($v_{\min.\text{ổn định}} \le 0.012\text{ m/s}$). |
| **3** | **Slide 4 & Slide 9 (`Mô tả nguyên lý công nghệ.pptx`):** Nêu thông số *`Động cơ nâng hạ`* và *`Chiều cao nâng h = 12 m`* nhưng chưa ghi chú rõ ranh giới loại trừ trên cùng slide. | Rơi thẳng vào **Bẫy trượt Cổng MCR & SRR** trong `FLOW_REVIEW.md`: *"Đưa chiều cao nâng $h = 12\text{ m}$ thành yêu cầu thiết kế cơ cấu nâng hạ"*. | **Khóa nhãn `[OUT-OF-SCOPE / BOUNDARY NOISE N2]`** ngay cạnh thông số $h = 12\text{ m}$ và cụm nâng hạ: Không tính chọn động cơ nâng hạ; $h = 12\text{ m}$ chỉ đóng vai trò tay đòn con lắc $\omega_p = \sqrt{g/h} \approx 0.904\text{ rad/s}$ ($T_p \approx 6.95\text{ s}$) để áp đặt ràng buộc $\lvert a \rvert \le 0.50\text{ m/s}^2$ và $\lvert \rho \rvert \le 2.00\text{ m/s}^3$. |
| **4** | **Slide 7 (`Mô tả nguyên lý công nghệ.pptx`):** Đưa *`Giới hạn hành trình`* và *`Nút Dừng khẩn cấp (E-Stop)`* vào yêu cầu chức năng chính mà không phân tách ranh giới `Tailoring`. | Mâu thuẫn với `SOW v1.0` và `PRD v3.0` (chỉ thực hiện nhóm `FUNC` và `PERM`, còn `SAFE/INTF/ENVI/RELI` thuộc nhóm *Out-of-Scope* của học phần). | **Phân tách rõ:** Giữ phần bảo vệ **quá dòng/quá tải mô-men ($\lambda_{\max} \ge 2.0$) và kẹp áp thanh cái DC-Link ($U_{\text{dc}} < 780\text{ V DC}$)** trong phạm vi *In-Scope (`PERM`)*; đánh dấu rõ công tắc hành trình vật lý & mạch phần cứng E-Stop thuộc giao diện biên/ngoài phạm vi thiết kế chi tiết (*Out-of-Scope Tailoring*). |
| **5** | **Toàn bộ file `Mô tả nguyên lý công nghệ.pptx`:** Có `PRD`, `Case Study 1 & 2`, `Mô tả nguyên lý công nghệ`, `SOW` nhưng **chưa có `QFD / House of Quality (HoQ 8×8)` và `Ma trận quyết định ICE`**. | Thiếu 50% tiêu chí qua cổng `MCR` theo `FLOW_REVIEW.md` (Pha `Measure`, `Analyze`, `Improve` của chuỗi `DMAIC`). | **Tích hợp trọn vẹn:** Giữ nguyên tinh hoa `Case Study 1 (Mita & Kanai 1979)`, `Case Study 2 (Feto 2025)` và `3 slide Mô tả nguyên lý công nghệ (Hình 3.1, 3.2, 3.3)` của nhóm, đồng thời nối liền mạch vào **Ma trận HoQ (`8 WHATs × 8 HOWs`)**, **Bảng Hình thái học & Điểm `ICE` chốt `Solution C` ($812/1000$)** và **Sổ rủi ro `RRM-01..05`**. |
| **6** | **File `SRS-diagram.pptx` (10 slides):** Đã có Slide 1 chuẩn ĐHBKHN và 5 slide cắt hình `Boundary Diagram` & `P-Diagram` (Slides 5–9), nhưng Slide 3 (`1. SRS`) và Slide 4 (`2. DVP&R`) đang để chữ placeholder copy từ bài tổng quan cầu trục. | Slide 3 và Slide 4 trong `SRS-diagram.pptx` chưa có dữ liệu thật của `14 mã SRS Baseline A`, `8 CTQ / 5 CTS`, `Ma trận RTM` và `14 bài đo DVP&R L0`. | **Kế thừa & Hoàn thiện:** Tận dụng toàn bộ bộ ảnh cắt `Boundary Diagram` (3 vùng) và `P-Diagram` ở Slides 5–9 của `SRS-diagram.pptx`, đồng thời điền đầy đủ nội dung chuẩn của **14 mã `SRS` (`7 FUNC + 7 PERM`)**, **`8 CTQ / 5 CTS`**, **Phễu truy vết `RTM`** và **`14 bài đo DVP&R L0` (`TS-01..04`)**. |

---

### Quy tắc 7: Giới hạn Mật độ Bảng Biểu trên Mặt Slide Chính (*Table Density Limits*)
`[Chuẩn: Assertion-Evidence — Michael Alley, Penn State]`
* **Số hàng tối đa trên 1 Slide chính:** **Tối đa 5 đến 7 hàng dữ liệu** (+ 1 hàng tiêu đề = tổng cộng $\le 8$ hàng).
  * *Cách xử lý bảng dài trong báo cáo `.md`:*
    * Nếu bảng có **8 hàng** (như 8 mã `PRD`, 8 mã `EC` của HoQ, 8 chỉ tiêu `CTQ-01..08`): Cho phép giữ bảng 8 hàng nhưng phải **rút gọn chữ trong mỗi ô xuống $\le 8\text{--}10$ từ** (chỉ giữ Mã ID, Tên ngắn, Công thức/Ngưỡng số học và Mã truy xuất), hoặc tách theo nhóm logic (ví dụ: 4 mã `FUNC` + 4 mã `PERM`).
    * Nếu bảng có **14 hàng** (như 14 mã `SRS Baseline A` và 14 bài đo `DVP&R L0`): **Tuyệt đối cấm nhét 14 hàng vào 1 slide!** Bắt buộc chia thành **2 Slide đối xứng (7 hàng/slide)**: 1 Slide cho Nhóm Chức năng (`SRS-FUNC-01..07` / `DVP-L0-01..07`) và 1 Slide cho Nhóm Hiệu năng (`SRS-PERM-01..07` / `DVP-L0-08..14`).
* **Số cột tối đa trên 1 Slide chính:** **4 đến 6 cột**. Không đưa cột văn xuôi dài ("Lý giải chi tiết 10 dòng") lên bảng trên mặt slide; cột lý giải dài phải đẩy xuống **Speaker Notes** và **Slide Backup**.
* **Kỹ thuật Highlight Pre-attentive (Thu hút thị giác trong 3 giây):** Trong mỗi bảng trên slide, phải tô nền nổi bật (màu vàng nhạt `#FEF9E7` viền đỏ `#C00000` hoặc chữ xanh đậm `#196B24`) cho **1–2 hàng quan trọng nhất** (ví dụ: tô nổi bật hàng **`Solution C`** trong bảng ICE, hàng **`EC-01 (22.30%)` & `EC-02 (14.90%)`** trong bảng HoQ, hoặc hàng **`SRS-PERM-05/06`** về gia tốc/độ giật chống lắc tải $h = 12\text{ m}$).

---

### Quy tắc 8: Công thức Chuyển đổi Câu Yêu cầu `Shall Statement` từ Báo cáo `.md` lên Slide Chính
`[AI bổ sung – dựa trên ISO/IEC/IEEE 29148 & Assertion-Evidence]`
Trong file `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md`, mỗi câu `SRS` được viết theo cú pháp 5 thành phần của ISO/IEC/IEEE 29148 dài khoảng 60–90 chữ. Khi đưa lên **Main Slide (Khối 1)**:
* **Trên mặt Main Slide:** Chuyển thành **4 cột tinh gọn**: `[Mã SRS & Truy xuất PRD/EC]` | `[Chức năng / Đại lượng kiểm soát]` | `[Ngưỡng Định lượng Shall (Số học + Đơn vị)]` | `[Phương pháp V&V & Owner]`.
* **Trong phần Speaker Notes & Slide Backup (`B1-3`, `B1-4`):** Giữ nguyên văn câu phát biểu *"Khi [Điều kiện], [Chủ thể] phải (shall) [Hành động] đạt [Ngưỡng]..."* để đọc/chiếu khi GVHD kiểm tra cú pháp IEEE 29148.

---

### Quy tắc 9: Trình tự Logic Bắt buộc của Một Bộ Slide Báo cáo Khối (*Gate Review Storyline*)
`[Nội bộ: FLOW_REVIEW.md & Mô tả nguyên lý công nghệ.pptx]` & `[Chuẩn: NASA SP-2007-6105 Rev 1, §6.7]`
Mỗi bộ Slide báo cáo tiến độ của một Khối (Block 0 hoặc Block 1) bắt buộc đi theo **5 hồi (5 Acts)** kết hợp mạch thuyết trình truyền thống của nhóm với cấu trúc xét duyệt cổng của `FLOW_REVIEW.md`:
* **Hồi 1 — Trang Bìa ĐHBKHN, Định vị Cổng & Bản Đồ Nội Dung (Slides 1–2):**
  * `Slide 1`: Trang bìa chuẩn ĐHBKHN (`slideLayout1`) giữ nguyên 100% thông tin nhóm + dòng phụ đề tên Khối/Gate.
  * `Slide 2`: Bản đồ Nội dung chính (`Agenda`) gắn với tiến độ các gói công việc `SOW WBS` và mục tiêu xét duyệt cổng (`Gate MCR` hoặc `Gate SRR-EVT`).
* **Hồi 2 — Bối cảnh Công nghệ, Giải mã Đầu bài $x=2$ & Phạm vi Ranh giới (Slides 3–6/7):**
  * *Ở Block 0 (`MCR`):* Tổng quan cấu tạo xe con & bài toán an toàn lắc tải (`PRD`) $\to$ Khóa bảng 6 thông số đề bài $x=2$ & 6 giả định kỹ thuật + 8 mã `PRD` (`4 FUNC + 4 PERM`) $\to$ Phân tích Case Study thực chứng (CQ1, CQ2, CQ3: Nhật Bản 1979 & Indonesia 2025) $\to$ Mô tả nguyên lý công nghệ (Chuỗi động học con lắc $h=12\text{ m}$, Quỹ đạo S-curve 7 pha, Đặc tính 4 góc phần tư).
  * *Ở Block 1 (`SRR-EVT`):* Phương pháp phân rã nguyên tử IEEE 29148 (`8 PRD + 8 EC` $\to$ `14 SRS`) $\to$ Sơ đồ Biên hệ thống 3 vùng (`Boundary Diagram` kế thừa từ `SRS-diagram.pptx` Slides 5–8) $\to$ Sơ đồ Tham số `P-Diagram` (`4 Nhiễu N1..N4`, `6 Biến điều khiển CF1..CF6`, `4 Lỗi E1..E4`) $\to$ Khóa 8 chỉ tiêu `CTQ-01..08` và 5 chỉ tiêu `CTS-01..05`.
* **Hồi 3 — Phân tích Kỹ thuật Chuyên sâu, Quản trị SOW & Truy vết V&V (Slides 8–14):**
  * *Ở Block 0 (`MCR`):* Phạm vi công việc `SOW` (CFT & RACI, Ranh giới In/Out-of-Scope, WBS 4 giai đoạn, 7 chỉ tiêu `QCD`) $\to$ 7 Khoảng trống công nghệ (`GAP-01..07`) $\to$ Ngôi nhà chất lượng `QFD/HoQ` (Xếp hạng Pareto 8 `EC-01..08`) $\to$ Ma trận hình thái & Chấm điểm `ICE` chốt `Solution C` ($812/1000$) $\to$ Kiến trúc `Solution C` (Sơ đồ `PDS IEC 61800-2` & `RFOC + S-Curve`) + Sổ 5 rủi ro `RRM-01..05`.
  * *Ở Block 1 (`SRR-EVT`):* Bảng 7 yêu cầu chức năng `SRS-FUNC-01..07` $\to$ Bảng 7 yêu cầu hiệu năng `SRS-PERM-01..07` $\to$ Phễu truy vết hai chiều `Bidirectional RTM` ($100\%$ độ phủ, $0$ mồ côi) $\to$ Chiến lược kiểm chứng `V&V` & 4 kịch bản tích hợp `TS-01..04` $\to$ Kế hoạch kiểm thử `DVP&R Level 0` (`DVP-L0-01..14`) $\to$ Quy chuẩn kỹ thuật đo đạo hàm gia tốc $a(t)$ & độ giật $\rho(t)$ trên Simulink.
* **Hồi 4 — Đối chiếu Checklist Qua Cổng (`FLOW_REVIEW.md`) & Slide `THANK YOU !` (2 Slides cuối Main Deck):**
  * 1 Slide Bảng đối chiếu toàn bộ tiêu chí bắt lỗi của `FLOW_REVIEW.md` kèm trạng thái **`ĐẠT (PASS)`** để xin phê duyệt đóng băng Baseline.
  * 1 Slide **`THANK YOU !`** (`slideLayout4` chuẩn ĐHBKHN) mở phiên Hỏi – Đáp (`Q&A`).
* **Hồi 5 — Hệ thống Slide Phụ lục Phòng thủ (`Backup Slides B-01 -> B-06`):** Đặt ngay sau Slide `THANK YOU !` để bật lên khi trả lời câu hỏi phản biện của Hội đồng.

---

### Quy tắc 10: Đồng nhất Tuyệt đối Bộ Hằng số Vật lý Đề $x = 2$ trên Mọi Slide
`[Nội bộ: TOM_TAT_TAI_LIEU.md, PRD v3.0, SRS Baseline A v1.0]`
Không một slide nào được phép làm tròn sai lệch hoặc dùng ký hiệu khác với bộ số đã khóa:
* **Tải trọng & Khối lượng:** $Q = 12,222\text{ kg}$ (cấm ghi $12,000\text{ kg}$); $m_{nh} = 222\text{ kg}$ ($\Rightarrow$ tổng khối lượng treo cáp $m_{\text{treo}} = Q + m_{nh} = 12,444\text{ kg}$); tự trọng xe con giả định từ Catalogue KG-Cranes 15t: $m_{xc} = 1,800\text{ kg} \Longrightarrow$ Tổng khối lượng đầy tải $M_\Sigma = 14,244\text{ kg}$ ($F_{c.\text{đầy}} \approx 27,947\text{ N}$), không tải $m_{\text{tĩnh}} = 2,022\text{ kg}$ ($F_{c.\text{không}} \approx 3,967\text{ N}$), tỷ số biến thiên tải $7.04\text{ lần}$.
* **Hình học & Cơ khí:** Chiều dài cáp treo $h = l \le 12\text{ m}$ (tần số góc lắc riêng $\omega_p = \sqrt{g/l} \approx 0.904\text{ rad/s}$, chu kỳ $T_p \approx 6.95\text{ s}$); bánh xe $d = 0.25\text{ m}$; hệ số cản $\mu = 0.20$; hiệu suất cơ khí $\eta = 0.96$.
* **Động học & Chất lượng điều khiển:** $v_{\max} = 0.12\text{ m/s}$ ($7.2\text{ m/phút}$, $\omega_{\text{bx}} = 0.96\text{ rad/s} \approx 9.17\text{ rpm}$); cấp tốc độ bò $v_{\text{creep}} \in [0.030;\ 0.036]\text{ m/s}$ ($25\% \div 30\%\ v_{\max}$); dải điều chỉnh $D \ge 10:1$; sai số xác lập tĩnh $e_{xl} \le 5.0\%$; quá điều chỉnh $M_p \le 10.0\%$; gia tốc $\lvert a(t) \rvert \le 0.50\text{ m/s}^2$; độ giật $\lvert \rho(t) \rvert \le 2.00\text{ m/s}^3$ (dùng thống nhất ký hiệu $\rho$, không dùng $j$).
* **Năng lượng & Nhiệt:** Nguồn 3 pha $380\text{V} \pm 10\% / 50\text{Hz}$; chế độ $S3$ ($CD = 40\%$); dự trữ công suất nhiệt $k_{dt} \in [1.20;\ 1.50]$; quá tải mô-men $\lambda_{\max} \ge 2.0$; áp thanh cái khi hãm tái sinh $U_{\text{dc}}(t) < 780\text{ V DC}$; mô-men giữ mở phanh $M_{\text{hold}}(0\text{ rpm}) \in [100\%;\ 150\%]\ M_{\text{đm}}$.

---

### Quy tắc 11: Quy chuẩn Bảng Màu ĐHBKHN (`theme1.xml`) & Mã Màu Kỹ Thuật
`[Nội bộ: Mô tả nguyên lý công nghệ.pptx, ppt/theme/theme1.xml]`
Sử dụng đồng bộ bảng màu chuẩn của Template ĐHBKHN kết hợp màu phân loại kỹ thuật:
* **Đỏ Bách Khoa (`#C00000`):** Dùng cho Tiêu đề Slide 1, Câu khẳng định `Action Title`, đường viền nhấn và chữ `THANK YOU !`.
* **Xanh Navy Đậm ĐHBKHN (`#0E2841` — `dk2` & `#156082` — `accent1`):** Dùng cho Thanh Header trên cùng, tiêu đề bảng (`Table Header Fill`), tiêu đề mục con và khung hệ thống *In-Scope*.
* **Cam Nhấn (`#E97132` — `accent2`):** Dùng cho cảnh báo Nhiễu biên (`N1..N4`), Khoảng trống công nghệ (`GAP-01..07`) và Rủi ro (`RRM-01..05`).
* **Xanh Lục Đạt Chuẩn (`#196B24` — `accent3`):** Dùng cho huy hiệu trạng thái **`ĐẠT (PASS) / FROZEN`** và phương án thắng cuộc **`Solution C`** (kết hợp nền vàng nhạt `#FEF9E7`).

---

### Quy tắc 12: Tuân thủ Quy định Nhãn Nguồn Bắt buộc của `SE_RULES.md`
`[Nội bộ: SE_RULES.md, Mục 3]`
Trong mọi kịch bản slide (đặc biệt ở phần **Chú thích chân bảng** trên mặt slide và phần **Speaker Notes**), bắt buộc gắn đúng 3 nhãn nguồn:
1. `[Nội bộ: tên file, mục]` — Ví dụ: `[Nội bộ: FLOW_REVIEW.md, Khối 0]`, `[Nội bộ: PRD-8.5EMG-TROLLEY-v3.0, Mục 3.2]`, `[Nội bộ: Mô tả nguyên lý công nghệ.pptx, Slide 15]`.
2. `[Chuẩn: tên chuẩn, mục, URL]` — Ví dụ: `[Chuẩn: TCVN 4244:2005, Mục 1.5.3.3.3]`, `[Chuẩn: ISO/IEC/IEEE 29148:2018, §5.2.5]`, `[Chuẩn: IEC 61800-2:1998]`.
3. `[AI bổ sung – cần kiểm]` — Dùng cho các gợi ý bố cục thiết kế đồ họa hoặc câu hỏi giả định phản biện thêm.

---

## 3. PLAYBOOK CHUYỂN ĐỔI TỪNG LOẠI TÀI LIỆU `.MD` & `.PPTX` SANG SLIDE GATE REVIEW

Bảng dưới đây là **"Cẩm nang tra cứu nhanh"** chỉ rõ cách cắt lọc từng tài liệu trong `Block 0` và `Block 1` (kết hợp với tài sản sẵn có trong thư mục `Báo cáo hàng tuần`) để đưa vào Slide chính và Slide Backup:

| Tài liệu Gốc (`.md` & `.pptx`) | Những gì ĐƯA LÊN MAIN DECK (Slide chính) | Những gì ĐẨY XUỐNG BACKUP DECK & SPEAKER NOTES | Nguồn Hình Ảnh Gợi Ý Tự Chèn (`🖼️`) |
| :--- | :--- | :--- | :--- |
| **1. `PRD v3.0` + Phần 1 `Mô tả nguyên lý công nghệ.pptx`** | • **Tổng quan cầu trục, cấu tạo xe con & bài toán an toàn lắc tải**.<br>• **Bảng khóa 6 thông số đề bài $x=2$ + 6 giả định kỹ thuật** ($Q=12,222\text{ kg}, m_{nh}=222\text{ kg}, m_{xc}=1,800\text{ kg}, M_\Sigma=14,244\text{ kg}$).<br>• **Danh mục 8 mã yêu cầu cốt lõi (`4 FUNC + 4 PERM`)** kèm ngưỡng số học. | • Chi tiết 6 pha vận hành `ConOps` đưa vào **Slide Backup `B0-1`**.<br>• 11 mã yêu cầu ngoài phạm vi (`SAFE`, `INTF`, `ENVI`, `RELI`) đưa vào **Slide Backup `B0-6`**. | • `Hình 1` (Slide 3), `Hình 2` (Slide 4), `Hình 5` thống kê BLS (Slide 6) trong `Mô tả nguyên lý công nghệ.pptx`. |
| **2. `Case Study & Nguyên lý Công nghệ` (`BCA v1.0` + Phần 2 & 3 `Mô tả nguyên lý công nghệ.pptx`)** | • **3 câu hỏi nghiên cứu (`CQ1, CQ2, CQ3`) + Bảng tổng hợp 9 Case Studies (`CS-01..09`)**.<br>• **Phân tích sâu Case 1 (Mita & Kanai 1979 — chống lắc tải) & Case 2 (Feto 2025 — chuỗi truyền động 3 cấp)**.<br>• **Mô tả nguyên lý công nghệ (Chuỗi động học $M_\Sigma=14,244\text{ kg}$, Quỹ đạo S-curve 7 pha, Đặc tính 4 góc phần tư)**.<br>• **Bảng 7 Khoảng trống Công nghệ (`GAP-01..07`)**. | • Bảng phân tích chi tiết 6 bài báo khoa học (`CS-01..06`) và 3 Catalogue (`CS-07..09`) đưa vào **Slide Backup `B0-2`**. | • `Hình 6, 7` (Case 1 — Slides 11–12), `Hình 8, 9` (Case 2 — Slides 13–14).<br>• 3 ảnh rời chất lượng cao: `Hinh_3_1_Co_cau_xe_con.jpg`, `Hinh_3_2_Quy_dao_S_curve.jpg`, `Hinh_3_3_Dac_tinh_4_goc_phan_tu.jpg`. |
| **3. `SOW v1.0` + Phần 4 `Mô tả nguyên lý công nghệ.pptx`** | • **Cơ cấu tổ chức CFT 6 thành viên** (3 tiểu ban) & Ma trận trách nhiệm `RACI` (`SOW-0.1`).<br>• **Ranh giới thiết kế (*In-Scope*: Phần lực + Phần điều khiển FOC/S-curve vs. *Out-of-Scope*: Nâng hạ, dầm cầu, PLC/chi phí)**.<br>• **Khối lượng công việc 4 giai đoạn (`WBS`), sản phẩm bàn giao (`CDRL-01..05`) & 7 chỉ tiêu nghiệm thu `QCD`**. | • Toàn văn 18 câu lệnh giao việc chủ động (`SOW-0.1` $\to$ `SOW-5.3`) và bảng đối chiếu 12/12 tiêu chí Phụ lục P của NASA SE Handbook đưa vào **Slide Backup `B0-5`**. | • Sơ đồ phân rã `WBS 4 giai đoạn` (bố cục 2 cột như Slide 19 của `Mô tả nguyên lý công nghệ.pptx`). |
| **4. `QFD / HoQ / ICE & RRM` (`BCA_QFD_HoQ_ICE_...md`)** | • **Bảng xếp hạng Pareto 8 Đặc tính Kỹ thuật HoQ (`EC-01..08`)** theo trọng số $w_j\%$.<br>• **Bảng so sánh 4 Phương án (`Solution A..D`) & Điểm `ICE`** chốt `Solution C` ($812/1000$).<br>• **2 Sơ đồ chuẩn của `Solution C`** (`PDS IEC 61800-2` & `3 mạch vòng RFOC + S-Curve`) + **Sổ 5 rủi ro `RRM-01..05`**. | • Ma trận đầy đủ 8×8 của Ngôi nhà Chất lượng (`HoQ`) và Mái nhà mâu thuẫn kỹ thuật đưa vào **Slide Backup `B0-3`**.<br>• Bảng Hình thái học (*Morphological Box*) đầy đủ đưa vào **Slide Backup `B0-4`**. | • Biểu đồ Pareto trọng số `EC-01..08` và Sơ đồ khối `PDS IEC 61800-2` / `RFOC + S-Curve`. |
| **5. `Boundary Diagram & P-Diagram` (`srs_...md` + `SRS-diagram.pptx`)** | • **Sơ đồ Ranh giới Hệ thống 3 vùng (`Boundary Diagram`)**: Môi trường ngoài (*Out-of-Scope*), Hệ truyền động xe con (*In-Scope*: 7 phần tử), Phần tải (*Out-of-Scope*: $Q=12,222\text{ kg}, h=12\text{ m}$) và 10 luồng giao diện `[P]`, `[E]`, `[I]`, `[M]`.<br>• **Sơ đồ Tham số (`P-Diagram` 5 hộp chuẩn DFSS)**: Tín hiệu vào $\to$ 4 Nhiễu `N1..N4` $\to$ 6 Biến điều khiển `CF1..CF6` $\to$ Đáp ứng lý tưởng vs. 4 Lỗi `E1..E4`.<br>• **Bảng khóa 8 chỉ tiêu `CTQ-01..08` và 5 chỉ tiêu `CTS-01..05`**. | • Giải trình 4 nguồn pháp lý/học thuật thiết lập sơ đồ biên đưa vào **Slide Backup `B1-1`**.<br>• Bảng đặc tả chi tiết 10 giao diện qua biên đưa vào **Slide Backup `B1-2`**. | • Bộ ảnh cắt Sơ đồ Biên 3 vùng tại **Slides 5, 6, 7, 8** và bộ ảnh cắt **P-Diagram tại Slide 9** của file `Báo cáo hàng tuần\SRS-diagram.pptx`. |
| **6. `SRS Baseline A v1.0` (`srs_...md`)** | • **Phương pháp luận Phân rã Nguyên tử (`ISO/IEC/IEEE 29148`)**: Sơ đồ ánh xạ từ `8 PRD + 8 EC` $\to$ `14 mã SRS nguyên tử`.<br>• **Bảng tóm tắt 7 mã Chức năng (`SRS-FUNC-01..07`)**.<br>• **Bảng tóm tắt 7 mã Hiệu năng (`SRS-PERM-01..07`)**. | • Toàn văn câu phát biểu chuẩn 5 thành phần (*Full Shall Statements*) và cột Lý giải chi tiết của 14 mã `SRS` đưa vào **Slide Backup `B1-3` & `B1-4`**. | • Sơ đồ cây phân rã `8 PRD + 8 EC -> 14 SRS` (vẽ bằng bảng/lưu đồ trực tiếp trên slide). |
| **7. `RTM & DVP&R Level 0 v1.0` (`rtm_dvp_...md`)** | • **Sơ đồ Phễu Truy xuất Hai chiều (`Bidirectional RTM Funnel`) + Bảng ánh xạ 8 luồng chính** (độ phủ 100%, 0 yêu cầu mồ côi).<br>• **Chiến lược V&V (`A/S/I`) & 4 Kịch bản Tích hợp (`TS-01..04`)**.<br>• **2 Slides Kế hoạch `DVP&R L0` (`DVP-L0-01..07` và `DVP-L0-08..14`)**.<br>• **Quy chuẩn Kỹ thuật Đo đạo hàm $a(t), \rho(t)$ trên Simulink** (khóa `Solver` $T_s \le 10^{-4}\text{ s}$ và bộ lọc $G_d(s)$). | • Bảng Ma trận Truy xuất Ngược (`Backward RTM`) 14 hàng nối chuỗi `DMAIC` đưa vào **Slide Backup `B1-5`**.<br>• Chi tiết các bước chạy từng kịch bản `TS-01..04` và MATLAB Script tự động chấm điểm đưa vào **Slide Backup `B1-6`**. | • Hình `Hinh_3_2_Quy_dao_S_curve.jpg` và `Hinh_3_3_Dac_tinh_4_goc_phan_tu.jpg` minh họa cho kịch bản `TS-01..03` & khối lọc đạo hàm Simulink. |

---

## 4. MẪU KHUNG 6 THÀNH PHẦN CHO MỖI SLIDE TRONG BÁO CÁO KỊCH BẢN `.MD`

Mọi Slide trong hai file báo cáo `BAO_CAO_SLIDE_PPTX_BLOCK_0_MCR.md` và `BAO_CAO_SLIDE_PPTX_BLOCK_1_SRR.md` đều phải tuân thủ đúng **Khung 6 thành phần (6-Part HUST-NASA Slide Blueprint)** dưới đây (bổ sung mục **🖼️ Ghi chú chèn hình ảnh cho người dùng** và **Thông số Layout/Cỡ chữ Template ĐHBKHN**):

```markdown
## SLIDE [Số thứ tự]: [Tên Ngắn Định Danh Slide]
* **1. Cấu hình Template ĐHBKHN, Header Xanh, Action Title & Footer:**
  * **Layout gốc sử dụng:** `slideLayout2` (`1_Section Header`) / `slideLayout3` (`1_Comparison`) / `slideLayout1` (Trang bìa) / `slideLayout4` (`THANK YOU !`)
  * **Thanh Header Xanh Trên Cùng (`pos=(0.30", 0.10")`, `Arial/Segoe UI 26pt Bold, Trắng #FFFFFF`):** `[SỐ MỤC. TÊN PHẦN BÁO CÁO IN HOA | GATE XXX]`
  * **Dòng Action Title Dưới Vạch Đỏ (`pos=(0.34", 0.88")`, `Arial/Segoe UI 20pt Bold, Đỏ #C00000`):** *"[Câu khẳng định hoàn chỉnh ≤ 22 từ nêu kết luận định lượng của slide]"*
  * **Chân trang phải (`pos=(6.50", 7.12")`, `Arial/Segoe UI 12pt`):** `Nhóm 8.5-EMG (Đề x=2) | Mã tài liệu | Phụ trách (R/A) | Slide X/N | Backup: [B-xx]`
* **2. Hướng dẫn Bố cục Trực quan & Cỡ chữ Tiếng Việt (Visual Layout & Font Size Guide):**
  * Mô tả cách chia cột/vùng trên màn hình 16:9, cỡ chữ từng thành phần (`Body 16–18pt`, `Table Header 15pt`, `Table Cell 14pt`), và vị trí cần tô màu nhấn (*Highlight*).
* **3. 🖼️ [GHI CHÚ CHÈN HÌNH ẢNH CHO NGƯỜI DÙNG] (Image Placeholder Guide):**
  * Chỉ rõ slide này có cần chèn ảnh hay không; nếu có thì lấy ảnh nào từ `Báo cáo hàng tuần\` (`Mô tả nguyên lý công nghệ.pptx`, `SRS-diagram.pptx`, `Hinh_3_1..3_3.jpg`), đặt vào toạ độ nào và ghi dòng Caption `Hình X. ...` gì.
* **4. Nội dung Hiển thị Trực tiếp trên Mặt Slide (On-Slide Copy-Paste Ready):**
  * Chỉ chứa Bảng cô đọng (≤ 7-8 hàng), Sơ đồ khối chuẩn hóa và Hộp kết luận ngắn gọn — sẵn sàng copy-paste hoặc để AI nạp thẳng vào PowerPoint mà không sợ tràn chữ hay lỗi font tiếng Việt.
* **5. Lời dẫn Thuyết trình (Speaker Notes — 60–90 giây) & Nhãn Nguồn (`SE_RULES.md`):**
  * Lời thoại mạch lạc dành cho người thuyết trình giải thích ý nghĩa vật lý/kỹ thuật đằng sau các con số trên slide, kèm nhãn nguồn `[Nội bộ: ...]`, `[Chuẩn: ...]`.
* **6. Điểm Bắt lỗi tại Cổng (`FLOW_REVIEW.md`) & Câu hỏi Phản biện Dự kiến:**
  * Nêu rõ câu hỏi mà CTO / SE Lead / GVHD thường hỏi xoáy tại slide này, câu trả lời ngắn gọn và chỉ dẫn bật **Slide Backup `[B-xx]`** nào để chứng minh.
```
