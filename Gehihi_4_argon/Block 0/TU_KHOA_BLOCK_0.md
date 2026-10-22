# BẢN TÓM TẮT CỐT LÕI (CHEAT SHEET): LUỒNG TƯ DUY & TỪ KHÓA KHỐI 0 → KHỐI 1
**Đề tài:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Xe Con Cầu Trục ($x=2$) | **Nhóm:** 8.5-EMG

---

## 1. LUỒNG TƯ DUY TỔNG THỂ 5 BƯỚC (THEO CHU TRÌNH DMAIC)

| Bước DMAIC | Mục tiêu cốt lõi | Nội dung triển khai cụ thể cho Đề tài Xe con ($x=2$) |
| :--- | :--- | :--- |
| **BƯỚC 1: DEFINE**<br>*(Định nghĩa & Ranh giới)* | Xác định đối tượng thiết kế và khoanh vùng biên hệ thống | - **In-Scope:** Hệ truyền động điện kéo **xe con** chạy ngang trên dầm chính.<br>- **Out-of-Scope:** Không thiết kế cơ cấu nâng hạ, di chuyển dầm cầu, kết cấu cơ khí dầm.<br>- **Nguyên lý:** Chuỗi cơ khí ($\text{Động cơ} \to \text{Hộp số} \to \text{Bánh xe}$) + Điện 4 góc phần tư (chế độ $S3$). |
| **BƯỚC 2: MEASURE**<br>*(Lượng hóa PRD: PERM & FUNC)* | Chuyển hóa đầu bài thành chỉ số đo lường được (`PERM` & `FUNC`) + Giả định | - **PERM (Hiệu năng):** $Q = 12,222\text{ kg}$; $m_{nh} = 222\text{ kg}$; $h = 12\text{ m}$; $v_{\max} = 0.12\text{ m/s}$; $a_{\max} \le 0.5\text{ m/s}^2$; $\rho_{\max} \le 2\text{ m/s}^3$; $e_{xl} \le 5\%$; $M_p \le 10\%$; $P_{đm} \ge P_{hd}$; $M_{kđ} \ge M_{\max\_yc}$.<br>- **Giả định (từ phương trình $F_k, M_{qđ}$):** $m_{xc} = 3 \div 4\text{ tấn}$, $d = 0.25\text{ m}$, $\mu = 0.2$, $\eta = 0.96$, lưới 3 pha $380\text{V}/50\text{Hz}$, chế độ $S3$ (TCVN 4244:2005).<br>- **FUNC (Chức năng):** Chạy 2 chiều 4 góc phần tư, chỉnh tốc độ (định mức & bò), logic trạng thái (`STOP/READY/RUN`), phanh cơ khí, khóa chéo thuận/nghịch, Limit Switch, E-Stop (ISO 13850) & STO (IEC 61800-5-2). |
| **BƯỚC 3: ANALYZE**<br>*(Phân tích Case Study & Tech Gap)* | So sánh yêu cầu đề bài với Case Study cũ để chỉ ra khoảng trống công nghệ | - **Case 1 (Mita & Kanai, 1979):** Điều khiển Bang-Bang gia tốc $\to$ **Tech Gap 1:** Độ giật $\rho \to \infty$ (vi phạm $\rho \le 2\text{ m/s}^3$).<br>- **Case 2 (Feto et al., 2025):** Xe con $10\text{T}$ chọn động cơ $30\text{ kW}$ $\to$ **Tech Gap 2:** Dư thừa công suất, thiếu điều khiển vòng kín & hãm tái sinh.<br>- **Case 3 (Truyền thống $V/f$ vòng hở):** Sụt mô-men ở $0.12\text{ m/s}$ $\to$ **Tech Gap 3:** Không giữ nổi tải $12.2\text{T}$ khi nhả phanh, sai lệch tốc độ $> 5\%$. |
| **BƯỚC 4: IMPROVE / KAIZEN**<br>*(QFD/HoQ & Chấm điểm ICE)* | Đề xuất cải tiến lấp Tech Gap và chọn phương án tối ưu | - **QFD / HoQ:** Ánh xạ yêu cầu khách hàng (WHATs) sang đặc tính kỹ thuật (HOWs/CTQ).<br>- **Bộ 3 giải pháp Kaizen:** (1) Quỹ đạo S-Curve 7 đoạn; (2) Mạch Braking Chopper + Điện trở xả $R_h$; (3) Cấu trúc FOC vòng kín + Encoder (2 vòng PI).<br>- **Ma trận ICE (dựa trên QCD):** So sánh Solution A ($V/f$) vs. B (Sensorless) vs. C (FOC + Encoder) $\to$ **Chốt Baseline: SOLUTION C**. |
| **BƯỚC 5: CONTROL**<br>*(Khóa SOW, Sơ đồ khối & Nghiệm thu)* | Thiết lập chuẩn kiểm soát công việc, kiến trúc và kế hoạch kiểm thử | - **SOW:** Phân rã 4 giai đoạn công việc, Sản phẩm bàn giao, Tiêu chí nghiệm thu & Loại trừ.<br>- **Sơ đồ khối chuẩn IEC 61800:** Tách rõ nét vẽ Luồng công suất điện, Luồng cơ khí, Luồng tín hiệu.<br>- **Chuyển sang Khối 1:** Khóa `PRD (Frozen)` $\to$ Viết `SRS Baseline A`, `P-Diagram`, `RTM`, `DVP&R L0`. |

---

## 2. BẢNG TRA CỨU NHANH 10 TỪ KHÓA QUAN TRỌNG NHẤT

| STT | Từ khóa | Định nghĩa 1 dòng (Dùng khi trả lời vấn đáp) | Áp dụng trực tiếp vào Đề tài Xe con ($x=2$) |
| :---: | :--- | :--- | :--- |
| **1** | **PRD** | Tài liệu khóa đầu bài của khách hàng (*WHAT & WHY*), làm chuẩn tham chiếu gốc. | Chốt 2 nhóm yêu cầu `PERM` (6 số đề bài + $e_{xl}, M_p$) và `FUNC` (4 góc phần tư, logic, an toàn) + Bảng Giả định. |
| **2** | **SOW** | Tài liệu quy định gói công việc nhóm kỹ sư phải làm và sản phẩm bàn giao (*Deliverables*). | Suy từ tờ đề bài gốc + giới hạn 16 tuần môn học: Làm 4 giai đoạn tính toán & mô phỏng Simulink; loại trừ nâng hạ & dầm cầu. |
| **3** | **FUNC & PERM** | Sự tinh gọn (*Tailoring*) PRD: Chỉ giữ Yêu cầu Chức năng và Yêu cầu Hiệu năng. | Bỏ `ENVI`, `RELI`, IoT, SCADA vì không kiểm chứng được trên mô phỏng Simulink. |
| **4** | **DMAIC** | Chu trình 5 bước: *Define – Measure – Analyze – Improve – Control*. | Trục xương sống dẫn dắt từ định nghĩa xe con $\to$ thông số đề $\to$ phân tích Case Study $\to$ Kaizen $\to$ kiểm soát. |
| **5** | **Tech Gap** | Khoảng trống công nghệ mà các Case Study cũ chưa đáp ứng được yêu cầu đề bài. | Case cũ bị $\rho \to \infty$ (Bang-Bang), chọn sai công suất ($30\text{ kW}$), hoặc sụt mô-men ở tốc độ thấp ($V/f$). |
| **6** | **Kaizen** | Bước cải tiến kỹ thuật (trong chữ *Improve*) để lấp đầy *Tech Gap*. | Áp dụng bộ 3: **Quỹ đạo S-Curve** + **FOC có Encoder** + **Braking Chopper & $R_h$**. |
| **7** | **QCD** | Mục tiêu *Quality (Chất lượng) – Cost (Chi phí/Nguồn lực) – Delivery (Tiến độ)*. | Đạt chuẩn động học/điều khiển (Q), tối ưu cấu hình & sức làm của 6 người (C), kịp tiến độ tuần $10 \div 16$ & cuối kỳ (D). |
| **8** | **QFD / HoQ** | Phương pháp & Ma trận Ngôi nhà chất lượng dịch yêu cầu khách hàng (VOC) sang thông số kỹ thuật (CTQ). | Dịch mong muốn "chạy êm, không lắc tải, dừng chuẩn" thành $\rho \le 2\text{ m/s}^3$, $a \le 0.5\text{ m/s}^2$, $e_{xl} \le 5\%$, $M_{kđ} \ge 1.5 M_{đm}$. |
| **9** | **ICE** | Ma trận chấm điểm chọn phương án: $\text{Impact} \times \text{Confidence} \times \text{Ease}$. | Chấm điểm 3 phương án (A: $V/f$, B: Sensorless, C: FOC + Encoder) $\to$ Chọn **Solution C** vì điểm ICE cao nhất. |
| **10** | **Chuẩn Sơ đồ khối** | Biểu diễn kiến trúc hệ truyền động theo chuẩn IEC 61800 / SE Functional Block Diagram. | Tách 3 loại đường nét (Công suất điện 3 pha, Trục cơ khí, Tín hiệu điều khiển/phản hồi); có đủ $R_h$, Phanh từ, S-Curve, PI. |

---

## 3. CHECKLIST 5 ĐIỂM CẦN SỬA TRONG BÀI CŨ TRƯỚC KHI SANG KHỐI 1
1. **Đồng bộ ký hiệu:** Dùng duy nhất $\rho_{\max}$ cho độ giật cực đại (xóa bỏ `j_max` và lỗi gõ nhầm $a_{\max}$).
2. **Đưa tự trọng xe con ($m_{xc}$) vào bảng Giả định PRD:** Khai báo rõ $m_{xc}$ (kèm $d=0.25\text{ m}, \mu=0.2, \eta=0.96$) và ghi rõ nguồn tra cứu Catalogue / TCVN 4244:2005.
3. **Chuẩn hóa bảng Case Study:** Gắn tên tác giả/năm vào `[1], [2], [3], [4]`, thêm cột chỉ rõ **Tech Gap**, viết lại bằng thuật ngữ chuyên ngành Truyền động điện.
4. **Thống nhất thang điểm ICE:** Chọn 1 thang điểm duy nhất (thang 5 hoặc thang 10) đồng bộ giữa Slide và Báo cáo thuyết minh.
5. **Vẽ lại Sơ đồ khối hệ truyền động:** Bổ sung đầy đủ nguồn lưới, MCCB, Biến tần (Chỉnh lưu - DC Bus - Nghịch lưu), Chopper + $R_h$, Động cơ, Phanh điện từ, Hộp số, Bánh xe, Tải con lắc, Encoder, Cảm biến dòng, Khối Logic & S-Curve, 2 mạch vòng PI.