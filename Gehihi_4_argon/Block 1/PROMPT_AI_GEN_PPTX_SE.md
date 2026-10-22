# MASTER PROMPT & HƯỚNG DẪN SINH SLIDE POWERPOINT (`.PPTX`) CHUẨN NGƯỜI LÀM — NHÓM 8.5-EMG (ĐỀ $x = 2$)

> **Mục đích tài liệu:** Đây là **Master Prompt & Quy chuẩn Kỹ thuật Sinh Slide (`v3.0 — Human-Crafted Edition`)** dùng để điều khiển script Python (`python-pptx`) tạo ra các bản thuyết trình PowerPoint (`.pptx`) cho dự án **Thiết Kế Hệ Truyền Động Điện Cơ Cấu Di Chuyển Ngang Xe Con Cầu Trục ($x = 2$)** của **Nhóm 8.5-EMG — Đại học Bách Khoa Hà Nội (HUST)**, đảm bảo **khớp 100% dữ liệu gốc $x=2$, nhúng trực tiếp hình ảnh thật, cô đọng câu chữ trên slide (không tràn khung 100%) và đặt phần giải thích sâu vào Speaker Notes**.

---

## 1. BỘ THÔNG SỐ PHÁP LÝ GỐC ĐỀ BÀI ($x = 2$) & NHÂN SỰ NHÓM 8.5-EMG (CẤM BỊA ĐẶT / CẤM LỆCH SỐ)

### 1.1. Danh sách 6 Thành viên Nhóm Liên chức năng (`CFT 8.5-EMG`)
1. **Nguyễn Bá Hưng** — MSSV: `20232107` (*PE-Logic: Đồ thị phụ tải 4 góc phần tư, Máy trạng thái logic, Khóa chéo $v=0$ & Đồng bộ phanh cơ*).
2. **Đặng Nguyên Bình** — MSSV: `20231937` (*PE-Hardware / Power: Tính phụ tải $F_c, M_{qđ}, J_{qđ}$, Chọn ĐC KĐB $S3$, Biến tần, Điện trở xả hãm $R_h$, Mạch lực & `BOM`*).
3. **Trần Đỗ Khải** — MSSV: `20232131` (*PE-Control Loop: Tính 14 tham số ĐC, Thiết kế cấu trúc Vector `RFOC + Encoder`, S-Curve 7 đoạn, Tổng hợp PI dòng `MO` & PI tốc độ `SO`*).
4. **Phạm Văn Hưng** — MSSV: `20232109` (*QE-Simulation: Lập kế hoạch `DVP&R L0`, Chuẩn hóa môi trường Simulink `Solver`, lọc độ giật $\rho(t)$, chạy 4 kịch bản `TS-01..04`*).
5. **Nguyễn Hải Trung** — MSSV: `20232344` (*Doc Lead: Chuẩn hóa hồ sơ `PRD v3.0`, `SOW v1.0`, `SRS Baseline A`, `RTM` & Đóng gói `CDRL`*).
6. **Nghiêm Trọng Đông** — MSSV: `20232001` (*PM / SE Lead — STT 22 $\Rightarrow x = 2$: Quản trị WBS, RACI, Sơ đồ Ranh giới, P-Diagram, chốt `CTQ/CTS` & Phê duyệt cổng `A`*).
- **Giảng viên hướng dẫn:** **TS. Nguyễn Duy Đỉnh**.

### 1.2. Bộ Thông số Kỹ thuật Khóa cứng xuyên suốt 6 Khối ($x = 2$)
- **Thông số đề bài ($x = 2$):**
  - Tải nâng định mức: $Q = 10,000 + 1,111 \times 2 = \mathbf{12,222\text{ kg}}$ (`INP-01` — tuyệt đối không làm tròn thành 10 tấn hay 12 tấn).
  - Khối lượng cơ cấu nâng hạ đi cùng xe con: $m_{nh} = 200 + 11 \times 2 = \mathbf{222\text{ kg}}$ (`INP-02`).
  - Chiều cao nâng tối đa (chiều dài cáp treo): $h = 10 + 2 = \mathbf{12\text{ m}}$ (`INP-03` — *Out-of-Scope* tính động cơ nâng; đóng vai trò chiều dài con lắc đơn $\omega_p = \sqrt{g/h} \approx \mathbf{0.904\text{ rad/s}}$, chu kỳ $T_p \approx \mathbf{6.95\text{ s}}$).
  - Vận tốc di chuyển ngang tối đa: $v_{\max} = 0.1 + 0.01 \times 2 = \mathbf{0.12\text{ m/s}}$ ($7.2\text{ m/phút}$ — `MOP-01`).
  - Gia tốc ngang cực đại: $\mathbf{|a(t)| = |dv/dt| \le 0.50\text{ m/s}^2}$ (`MOP-02`).
  - Độ giật ngang cực đại: $\mathbf{|\rho(t)| = |da/dt| \le 2.00\text{ m/s}^3}$ (`MOP-03`).
- **Thông số giả định từ 3 hãng cầu trục (`KG-Cranes/Sungdo`, `Demag`, `Yuantai`) & Tiêu chuẩn (`TCVN 4244:2005`, `IEC 61800-2`, `IEC 60034-1`):**
  - Tự trọng bản thân xe con dầm đôi: $m_{xc} = \mathbf{1,800\text{ kg}}$ (`ASM-01`) $\Rightarrow$ Tổng khối lượng đầy tải $\mathbf{M_\Sigma = 14,244\text{ kg}}$ ($F_{c.\text{đầy}} \approx \mathbf{27,947\text{ N}}$), không tải $\mathbf{m_{\text{tĩnh}} = 2,022\text{ kg}}$ ($F_{c.\text{không}} \approx \mathbf{3,967\text{ N}}$) $\Rightarrow$ Biến thiên tải **$7.04\text{ lần}$**.
  - Đường kính bánh xe con: $d = \mathbf{0.25\text{ m}}$ ($250\text{ mm} \Rightarrow \omega_{\text{bx}} = 0.96\text{ rad/s} \approx 9.17\text{ rpm}$ — `ASM-02`).
  - Hệ số cản chuyển động quy đổi: $\mathbf{\mu = 0.20}$ (`ASM-03`); Hiệu suất truyền động cơ khí hộp giảm tốc 3 cấp: $\mathbf{\eta = 0.96}$ (`ASM-04`).
  - Nguồn lưới công nghiệp: 3 pha $\mathbf{380\text{V} \pm 10\% / 50\text{Hz}}$ ($342\text{V} \div 418\text{V AC}$ — `CON-01`); Chế độ làm việc: $\mathbf{S3\text{--}40\%}$ (`ISO M5 / FEM 2m` — `CON-02`).
  - Chỉ tiêu chất lượng điều khiển & định cỡ: Cấp tốc độ bò định vị $v_{\text{creep}} \in \mathbf{[0.030;\ 0.036]\text{ m/s}}$ ($25\% \div 30\%\ v_{\max}$), dải điều chỉnh $\mathbf{D \ge 10:1}$, sai lệch tốc độ tĩnh $\mathbf{e_{xl} \le 5.0\%}$, độ quá điều chỉnh $\mathbf{M_p \le 10.0\%}$, dự trữ công suất nhiệt $\mathbf{k_{dt} \in [1.20;\ 1.50]}$, bội số quá tải mô-men $\mathbf{\lambda_{\max} \ge 2.0}$, điện áp thanh cái DC-Link khi hãm tái sinh $\mathbf{U_{\text{dc}}(t) < 780\text{ V DC}}$, mô-men giữ tại $0\text{ rpm}$ trước khi mở phanh $\mathbf{M_{\text{hold}} \in [100\%;\ 150\%]\ M_{\text{đm}}}$.

---

## 2. QUY TẮC THIẾT KẾ SLIDE "CHUẨN NGƯỜI LÀM" & CHỐNG TRÀN CHỮ TUYỆT ĐỐI (`ZERO-OVERFLOW`)

1. **Nguyên tắc Cô đọng Nội dung trên Mặt Slide & Đẩy Giải thích vào Speaker Notes:**
   - **Trên mặt Slide (Bảng & Hộp Card):** Chỉ giữ lại **Từ khóa cốt lõi + Con số định lượng + Mã truy xuất** (mỗi ô bảng tối đa **1–2 dòng**, $\le 14$ từ/ô). Sử dụng cú pháp `**...**` để tô đậm đúng cụm từ khóa/con số quan trọng trong câu thay vì viết tràn lan.
   - **Trong Speaker Notes (`slide.notes_slide`):** Chứa toàn bộ lời thuyết trình hoàn chỉnh (60–90 giây/slide), giải thích lý do vật lý, phương trình toán học, trích dẫn nguồn (`[Nội bộ: ...]`, tiêu chuẩn `TCVN 4244`, `IEC 61800-2`, `NASA SE Handbook`) và câu trả lời phản biện tại Cổng.
2. **Kiểm soát Tọa độ Khung & Chiều cao Bảng (`13.333" × 7.500"` — Widescreen 16:9):**
   - **Slide 01 (Trang bìa ĐHBKHN):** Giữ nguyên Slide 1 từ `Mô tả nguyên lý công nghệ.pptx`, nâng nhẹ hộp Tiêu đề chính lên `top = 1.62", height = 1.35"` để không chạm vào hộp Phụ đề báo cáo cổng đặt tại `top = 3.12", height = 0.52"` (`15.5pt Bold`), giữ khoảng cách thoáng với dòng `NHÓM 8.5-EMG` tại `top = 3.79"`.
   - **Thanh Header Xanh (`top = 0.08", height = 0.50"`):** `Arial 21pt Bold, Trắng #FFFFFF`.
   - **Dòng Action Title (`top = 0.85", height = 0.48"`):** `Arial 15.5pt Bold, Đỏ #C00000`, viết gọn trên **1 dòng duy nhất** ($\le 105$ ký tự) để không bao giờ tràn xuống vùng nội dung!
   - **Vùng Nội dung An toàn (`Safe Content Zone`):** Từ `y = 1.42"` đến `y = 6.82"` (chiều cao tối đa `5.40"`). Mọi bảng và thẻ Card khi render thực tế trong PowerPoint phải có đáy `est_bottom <= 6.82"`, tuyệt đối không chạm vào đường kẻ đỏ chân trang (`y = 6.95"`) và Footer (`y = 7.08"`).
3. **Nhúng Trực tiếp Hình ảnh Thật & Vẽ Sơ đồ Khối bằng Native PowerPoint Shapes:**
   - **Tự động trích xuất và nhúng ảnh thật** từ `Báo cáo hàng tuần\Mô tả nguyên lý công nghệ.pptx` (Hình cấu tạo xe con, Thống kê tai nạn BLS, Mô hình con lắc Mita 1979, Bảng hộp số 3 cấp Feto 2025, Hình 3.1 Chuỗi động học, Hình 3.2 Quỹ đạo S-curve 7 pha, Hình 3.3 Đặc tính 4 góc phần tư) và từ `Báo cáo hàng tuần\SRS-diagram.pptx` (Sơ đồ Ranh giới Hệ thống tổng thể, 3 phân vùng cắt lớp, và Sơ đồ Tham số P-Diagram), giữ nguyên tỷ lệ khung hình (*Aspect Ratio*) kèm viền thẻ và chú thích ảnh chuẩn.
   - **Tuyệt đối cấm vẽ sơ đồ bằng ký tự ASCII (`──►`, `━━►`, `║`) trong Textbox!** Mọi lưu đồ cổng, sơ đồ kiến trúc `IEC 61800-2`, sơ đồ vòng điều khiển `RFOC + S-Curve`, phễu truy xuất `RTM` và sơ đồ bộ lọc đạo hàm Simulink phải được vẽ bằng các khối hình học thật của PowerPoint (`MSO_SHAPE.ROUNDED_RECTANGLE`, `CHEVRON`, `RIGHT_ARROW`, `DOWN_ARROW`) có phân màu trực quan.
