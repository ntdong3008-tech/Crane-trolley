# TỔNG HỢP BÀI GIẢNG & LÝ GIẢI CHI TIẾT 6 KHỐI – 7 CỔNG (`FLOW_REVIEW.md`)
**Tài liệu gốc:** `Lưu đồ dự án.jpg` (`EVLEP003_HBK` v1.8.2) & `NASA/SP-2007-6105 Rev1`  
**Dự án áp dụng:** Thiết kế Hệ Truyền động Điện Cơ cấu Xe con Cầu trục ($x = 2$, Nhóm 8.5-EMG)  
**Thông số chốt ($x=2$):** $Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg}$, $h = 12\text{ m}$ (*Out-of-Scope*), $v_{\max} = 0.12\text{ m/s}$, $a_{\max} \le 0.5\text{ m/s}^2$, $\rho_{\max} \le 2\text{ m/s}^3$, nguồn 3 pha $380\text{V} \pm 10\% / 50\text{Hz}$, chế độ $S3$, chuẩn $TCVN\ 4244:2005$.

---

## KHỐI 0 · TIỀN KHẢ THI (Pre-A) (§4.2, §4.3, §5.1) & CỔNG MCR (CTO)
* **Nguồn:** `[Nội bộ: FLOW_TRANSCRIPT.md, Mục III.2, IV.1]` & `[Chuẩn: NASA SP-2007-6105 Rev1, Table 6.7-4, p.173]`

### 1. Khối này để làm gì?
Biến ý tưởng hoặc đề bài ban đầu thành một dự án chính thức có tên tuổi, có nhóm phụ trách và mục tiêu rõ ràng. Kiểm tra xem giải pháp dự kiến có làm được không, tốn bao nhiêu công sức và có những nguy cơ gì. Giúp cấp trên quyết định có duyệt cho nhóm bắt đầu bắt tay vào thiết kế hay bắt làm lại từ đầu.

### 2. Phân tích từng gạch đầu dòng & Cổng bắt lỗi
* **Đăng ký mã dự án · CTO ký quyết định lập CFT:** Định danh dự án và lập nhóm liên chức năng (CFT) để rõ ai làm việc gì; thiếu sẽ bị **MCR** chặn vì chưa có tổ chức hợp lệ.
* **Lập BCA sơ bộ kèm TRL (1–2) & tuyên bố khả thi SX kèm MRL:** Chứng minh bài toán đáng đầu tư và công nghệ sẵn sàng; thiếu sẽ trượt câu hỏi *"Bài toán KD có đáng đầu tư?"* tại **MCR**.
* **Soạn PRD dự thảo · Điều lệ & SOW có mục tiêu QCD đo được:** Nêu đích đến sản phẩm (PRD) và cam kết Chất lượng – Chi phí – Tiến độ (SOW/Điều lệ); thiếu hoặc viết mơ hồ sẽ bị **MCR** trả về (`KHÔNG ĐẠT — cập nhật BCA / Điều lệ`) và làm **SRR-EVT** sau đó không có PRD để khóa.
* **Ghi tối thiểu 5 rủi ro kỹ thuật / tiến độ vào sổ RRM:** Lường trước tối thiểu 5 nguy cơ lớn; nếu ghi $<5$ sẽ bị **MCR** bắt lỗi theo tiêu chí rủi ro đầu vào.

### 3. Ví dụ áp dụng trên đề Xe con cầu trục ($x=2$, nhóm 8.5-EMG)
* **PRD dự thảo & SOW (mục tiêu QCD đo được):**
  * *Quality (Q):* Hệ truyền động kéo tải $Q = 12,222\text{ kg}$ + cơ cấu nâng $m_{nh} = 222\text{ kg}$, đạt $v_{\max} = 0.12\text{ m/s}$, gia tốc $a \le 0.5\text{ m/s}^2$, độ giật $\rho \le 2\text{ m/s}^3$.
  * *Cost & Delivery (C & D):* Dùng cấu hình phổ thông (Động cơ KĐB 3 pha $380\text{V}$ + Biến tần); thuyết trình giữa kỳ tuần 10–16, nộp báo cáo cuối kỳ tại phòng thi.
* **Sổ RRM ($\ge 5$ rủi ro):** (1) Tải $12,222\text{ kg}$ treo ở độ cao $h=12\text{ m}$ bị lắc mạnh khi phanh; (2) Quá áp DC-bus biến tần khi hãm tái sinh; (3) Trượt bánh xe trên ray; (4) Trễ tiến độ ghép nối Simulink giữa PE và QE; (5) Chọn sai tỷ số truyền hộp số.

### 4. Lỗi người mới hay mắc
Viết mục tiêu QCD trong Điều lệ/SOW bằng từ định tính như *"chạy êm, an toàn, đúng hạn"* (thiếu con số đo được như $a \le 0.5\text{ m/s}^2$, $\rho \le 2\text{ m/s}^3$), hoặc nhảy vào tính chọn động cơ ngay khi chưa chốt PRD dự thảo và chưa qua cổng MCR.

### 5. Điểm chốt câu hỏi ôn tập tại Cổng MCR
* **Nếu KHÔNG ĐẠT:** Quay về Khối 0 để **`cập nhật BCA / Điều lệ`**.
* **Nếu ĐẠT (hoặc ĐẠT CÓ ĐIỀU KIỆN):** **`Điều lệ có hiệu lực`**, cho phép chuyển sang Khối 1.

---

## KHỐI 1 · EVT — YÊU CẦU HỆ THỐNG (§5.2) & CỔNG SRR-EVT (SE Lead)
* **Nguồn:** `[Nội bộ: FLOW_TRANSCRIPT.md, Mục III.3, IV.2]` & `[Chuẩn: NASA SP-2007-6105 Rev1, §4.2, Table 6.7-5, Appendix C & D]`

### 1. Khối này để làm gì?
Chuyển toàn bộ mong muốn của đề bài thành một bảng danh sách các yêu cầu kỹ thuật cụ thể bằng con số để anh em kỹ sư thiết kế không hiểu sai ý nhau. Vẽ ranh giới rõ ràng xem hệ thống của nhóm gồm những phần nào và chịu những tác động gì từ bên ngoài. Lên sẵn kế hoạch kiểm tra cho từng yêu cầu trước khi khóa sổ để chuyển sang vẽ kiến trúc.

### 2. Phân tích từng gạch đầu dòng & Cổng bắt lỗi
* **Viết SRS baseline A — mọi yêu cầu phải đo được:** Bản đặc tả yêu cầu hệ thống dùng cấu trúc *"shall"* kèm ngưỡng số học; nếu viết định tính (không đo được) sẽ trượt câu hỏi *"Yêu cầu đã đủ & đo được chưa?"* tại **SRR-EVT**.
* **Khóa PRD trước khi đóng băng SRS; truy xuất SRS $\to$ PRD:** Chốt cứng đầu bài của khách hàng (PRD) rồi mới khóa yêu cầu kỹ thuật hệ thống (SRS), đảm bảo mọi dòng SRS đều phục vụ PRD; thiếu truy xuất sẽ bị **SRR-EVT** trả về (`KHÔNG ĐẠT — sửa SRS / RTM`).
* **Lập DVP&R L0 + RTM ánh xạ 100 % yêu cầu:** Ma trận truy xuất (RTM) nối 100% yêu cầu SRS sang Kế hoạch kiểm chứng cấp hệ thống (DVP&R L0); nếu sót (< 100%) sẽ bị bắt lỗi tại **SRR-EVT**, **CDR-EVT** và không có căn cứ chạy test ở **Khối 5 (SIR-EVT)**.
* **Dựng sơ đồ biên (Boundary Diagram) & P-Diagram; chốt sơ bộ CTQ / CTS:** Xác định ranh giới hệ thống (*In/Out-of-Scope*), biến nhiễu và thông số sống còn về Chất lượng/An toàn (CTQ/CTS); thiếu sẽ làm thiết kế sót giao diện ở **PDR-EVT**.

### 3. Ví dụ áp dụng trên đề Xe con cầu trục ($x=2$, nhóm 8.5-EMG)
* **SRS baseline A + RTM + DVP&R L0 (ánh xạ 1-1):**
  * `PRD-01` (Tốc độ & chống giật theo đề $x=2$) $\leftarrow$ `SRS-F01`: *"Hệ truyền động xe con **phải (shall)** đạt tốc độ xác lập $v_{\max} = 0.12\text{ m/s}$ với sai số tĩnh $\le 5\%$, gia tốc $a \le 0.5\text{ m/s}^2$ và độ giật $\rho \le 2\text{ m/s}^3$ khi mang tải định mức $Q = 12,222\text{ kg}$ và cơ cấu nâng $m_{nh} = 222\text{ kg}$"* $\rightarrow$ `DVP&R-L0-01`: Kiểm chứng bằng **Mô phỏng (Simulation)** trên MATLAB/Simulink ở chế độ $S3$, đo đồ thị $v(t), a(t), \rho(t)$.
* **Sơ đồ biên & P-Diagram (CTQ/CTS):** Chiều cao nâng $h = 12\text{ m}$ thuộc cơ cấu nâng (*Out-of-Scope*), nhưng đóng vai trò là **Nhiễu (Noise)** gây lắc tải tác động qua ranh giới vào bánh xe con (*In-Scope*); từ đó chốt **CTQ** là $a_{\max} \le 0.5\text{ m/s}^2$ và $\rho_{\max} \le 2\text{ m/s}^3$.

### 4. Lỗi người mới hay mắc
Nhét luôn giải pháp thiết kế chi tiết vào SRS (ví dụ: viết *"phải dùng PI tối ưu đối xứng"* ngay trong SRS thay vì để sang Khối 2–3), hoặc quên khóa PRD trước khi đóng băng SRS khiến đầu bài thay đổi liên tục làm vỡ RTM.

### 5. Điểm chốt câu hỏi ôn tập tại Cổng SRR-EVT
* **Thẩm quyền ký:** **SE Lead** chủ trì duyệt để **Đóng băng SRS** (TRL 3), nhưng theo **Ghi chú (2) (`§5.2.2(d)`)** cần đối chiếu thêm chữ ký của **CTO** khi ký biên bản.
* **Lý do khóa PRD trước khi đóng băng SRS:** PRD định nghĩa đầu bài/nhu cầu sản phẩm gốc; phải cố định đầu bài thì bản dịch kỹ thuật (SRS) và ma trận truy xuất (RTM) mới không bị trôi.

---

## KHỐI 2 · EVT — KIẾN TRÚC (§5.3) & CỔNG PDR-EVT (SE Lead)
* **Nguồn:** `[Nội bộ: FLOW_TRANSCRIPT.md, Mục III.4, IV.3]` & `[Chuẩn: NASA SP-2007-6105 Rev1, §4.3, §6.8, Table 6.7-8]`

### 1. Khối này để làm gì?
Vẽ ra bức tranh tổng thể xem hệ thống gồm những khối thiết bị lớn nào và chúng nối dây, truyền lực hay trao đổi tín hiệu với nhau ra sao. So sánh các phương án cấu hình để chọn ra phương án tối ưu nhất, lên danh sách vật tư sơ bộ và tìm sẵn các nguy cơ hỏng hóc lớn để phòng tránh. Chốt khung sườn kiến trúc khả thi trước khi chia cho anh em đi tính toán mạch và thuật toán chi tiết.

### 2. Phân tích từng gạch đầu dòng & Cổng bắt lỗi
* **Lập SAD + ICD thể hiện đủ 7 sơ đồ kỹ thuật cốt lõi:** Tài liệu kiến trúc (SAD) và kiểm soát giao diện giữa các khối (ICD); thiếu sẽ bị **PDR-EVT** chặn không cho đóng băng SAD/ICD, và tới **SIR-EVT (Khối 5)** khi ghép nối các khối sẽ bị lệch nhau.
* **Dựng BOM sơ bộ 3 cấp; chốt linh kiện độc cung, đặt long-lead:** Lập danh mục vật tư 3 cấp (Hệ thống $\to$ Phân hệ $\to$ Cụm thiết bị) và đặt sớm linh kiện giao hàng lâu; thiếu sẽ bị **PDR-EVT** trả về (`KHÔNG ĐẠT — sửa kiến trúc / tối ưu BOM`) hoặc trễ mẫu ở **Khối 4 (TRR-EVT)**.
* **Chạy DFMEA L1 — xử lý hết hạng mục AP = Cao:** Phân tích các kiểu lỗi thiết kế ở cấp hệ thống (L1) và hạ hết các rủi ro có mức ưu tiên hành động (AP) Cao; còn sót `AP = Cao` sẽ trượt câu hỏi *"Kiến trúc đã chốt & khả thi chưa?"* tại **PDR-EVT**.
* **Phân tích trade-off kiến trúc và Creepage / Clearance:** Cân đong đo đếm chọn phương án tối ưu (trade-off) và tính khoảng cách rò/phóng điện an toàn; thiếu sẽ bị **PDR-EVT** bắt lỗi (`sửa kiến trúc`) hoặc mất an toàn đo kiểm ở **TRR-EVT**.

### 3. Ví dụ áp dụng trên đề Xe con cầu trục ($x=2$, nhóm 8.5-EMG)
* **Trade-off kiến trúc + SAD/ICD + BOM sơ bộ (Bình, Khải & Đông phối hợp):**
  * *Trade-off:* So sánh điều khiển $U/f$ vòng hở với **FOC vòng kín có Encoder** $\to$ chọn **Động cơ KĐB 3 pha $380\text{V}$ + Biến tần AC (FOC) + Encoder + Điện trở xả hãm $R_h$ + Phanh cơ điện từ** để kiểm soát chính xác mô-men ở tốc độ thấp $v_{\max} = 0.12\text{ m/s}$ và giữ $a \le 0.5\text{ m/s}^2, \rho \le 2\text{ m/s}^3$.
  * *ICD (Giao diện):* Khóa rõ giao diện Cơ khí (Trục motor $\leftrightarrow$ Khớp nối $\leftrightarrow$ Hộp số $\leftrightarrow$ Bánh xe kéo tải $Q = 12,222\text{ kg} + m_{nh} = 222\text{ kg}$), Điện lực ($380\text{V AC}$, DC-bus nối $R_h$) và Tín hiệu (xung Encoder, lệnh Run/E-stop/Limit switch vào Biến tần).
* **DFMEA L1 (xử lý AP = Cao):** Lỗi *"Quá áp DC-bus biến tần khi xe con mang tải $12,222\text{ kg}$ giảm tốc dừng ở chế độ $S3$"* (`AP = Cao`) $\to$ Biện pháp thiết kế: Bổ sung mạch Chopper + Điện trở xả hãm $R_h$ và bộ tạo quỹ đạo S-Curve giới hạn $a \le 0.5\text{ m/s}^2$ để hạ AP xuống Trung bình/Thấp.

### 4. Lỗi người mới hay mắc
Chia việc cho các thành viên về tự tính toán độc lập mà **không chốt ICD (giao diện)** trước ở Khối 2 — dẫn đến người tính công suất/tỷ số truyền (Bình), người thiết kế logic quỹ đạo (Bá Hưng) và người làm vòng điều khiển FOC (Khải) dùng khác ký hiệu, khác đơn vị hoặc lệch dải tín hiệu khi ghép vào Simulink ở Khối 5.

### 5. Điểm chốt câu hỏi ôn tập tại Cổng PDR-EVT
* **Rủi ro chi phí ở vòng lặp PDR-EVT $\to$ Khối 2:** Dù mới ở giai đoạn kiến trúc trên giấy (TRL 3–4), nhưng vì trong Khối 2 đã có bước **"đặt long-lead"** (mua trước linh kiện giao hàng lâu) nên nếu kiến trúc bị đánh trượt phải thay đổi tại PDR-EVT thì dự án có thể mất tiền oan cho các linh kiện đã trót đặt.

---

## KHỐI 3 · EVT — THIẾT KẾ CHI TIẾT (§5.4) & CỔNG CDR-EVT (PE Lead)
* **Nguồn:** `[Nội bộ: FLOW_TRANSCRIPT.md, Mục III.5, IV.4]` & `[Chuẩn: NASA SP-2007-6105 Rev1, Table 6.7-9, p.178]`

### 1. Khối này để làm gì?
Từ khung kiến trúc đã chốt, anh em kỹ sư bắt tay vào tính toán ra từng con số cụ thể, vẽ chi tiết từng sơ đồ mạch điện, bản vẽ cơ khí và viết thuật toán điều khiển. Chạy các bài tính kiểm tra giới hạn chịu đựng và mô phỏng trước trên máy tính để chắc chắn thiết kế không bị cháy nổ hay sai lệch. Khóa toàn bộ hồ sơ thiết kế chi tiết để sẵn sàng đem đi chế tạo hoặc dựng mô hình thử nghiệm hoàn chỉnh.

### 2. Phân tích từng gạch đầu dòng & Cổng bắt lỗi
* **Ra Schematic, Gerber, 3D vỏ & đồ gá, SDD, HSI:** Bộ hồ sơ thiết kế phần cứng (sơ đồ nguyên lý, mạch in, cơ khí 3D), phần mềm/thuật toán (SDD) và giao diện phần cứng – phần mềm (HSI); thiếu sẽ bị **CDR-EVT** chặn vì chưa *"Đủ chín để đặt chế tạo mẫu chưa?"*.
* **Chứng minh biên an toàn: WCCA, SI/PI, mô phỏng nhiệt:** Tính toán trường hợp xấu nhất (WCCA), toàn vẹn tín hiệu/nguồn (SI/PI) và phát nhiệt; thiếu sẽ trượt **CDR-EVT** và dễ gây quá nhiệt (hotspots) hoặc cháy mạch ở **Khối 5 (SIR-EVT)**.
* **Hạ DFMEA và DVP&R xuống cấp phân hệ; RTM bao phủ 100 %:** Soi lỗi (DFMEA) và lập bài đo (DVP&R) chi tiết tới từng khối nhỏ, đảm bảo RTM không sót yêu cầu nào; thiếu sẽ bị **CDR-EVT** bắt lỗi hồ sơ kiểm chứng.
* **Nộp bảng ánh xạ V-Model: mỗi khối có phép thử đối xứng:** Ghép cặp từng phần thiết kế (nhánh trái chữ V) với bài kiểm tra tương ứng (nhánh phải chữ V); thiếu sẽ không có kịch bản đo chuẩn ở **Khối 4 & Khối 5**.

### 3. Ví dụ áp dụng trên đề Xe con cầu trục ($x=2$, nhóm 8.5-EMG)
* **Thiết kế chi tiết phần cứng, SDD & chứng minh biên an toàn (Bình, Bá Hưng, Khải):**
  * *Phần cứng & Biên nhiệt (WCCA/Nhiệt):* Bình tính lực cản $F_c$, quy đổi $M_{qđ}, J_{qđ}$ với tải $Q = 12,222\text{ kg} + m_{nh} = 222\text{ kg}$, vẽ sơ đồ nguyên lý mạch lực $380\text{V}$, chọn mã Động cơ KĐB, Biến tần, tính giá trị $\Omega/\text{W}$ của điện trở hãm $R_h$ và kiểm nghiệm phát nhiệt ở chế độ $S3$.
  * *SDD (Thuật toán & Điều khiển):* Khải tính 14 tham số động cơ, tổng hợp bộ điều khiển PI dòng điện ($i_d, i_q$ - Tối ưu Module) và PI tốc độ ($\omega$ - Tối ưu Đối xứng); Bá Hưng thiết kế logic trạng thái (Ready, Run, E-stop, Limit switch) và quỹ đạo làm mềm giữ $a \le 0.5\text{ m/s}^2, \rho \le 2\text{ m/s}^3$.
* **Bảng ánh xạ V-Model & DVP&R cấp phân hệ (Đông & Văn Hưng):**
  * *Phân hệ vòng dòng điện ($i_d, i_q$):* Đối xứng với bài test đáp ứng bậc thang dòng điện trên Simulink.
  * *Phân hệ vòng tốc độ & tạo quỹ đạo:* Đối xứng với bài test chạy chu trình 4 góc phần tư $M_c(t)$, đo trực tiếp $v_{\max} = 0.12\text{ m/s}, a \le 0.5\text{ m/s}^2, \rho \le 2\text{ m/s}^3$.

### 4. Lỗi người mới hay mắc
Tính xong công thức chọn động cơ và bộ điều khiển PI trên giấy là vội đem lắp ghép chạy thử toàn hệ thống ngay mà **bỏ qua kiểm nghiệm biên an toàn (WCCA/nhiệt)** và **không lập DVP&R cấp phân hệ** (không test riêng từng mạch vòng dòng điện, tốc độ, khối tạo quỹ đạo trước), khiến lúc ghép chung bị vọt lố hoặc lỗi thì không biết lỗi nằm ở khối nào.

### 5. Điểm chốt câu hỏi ôn tập tại Khối 3 & Cổng CDR-EVT
* **Hai vòng lặp cùng quay về đáy Khối 3:**
  1. **Từ cổng CDR-EVT quay về Khối 3 (`sửa thiết kế chi tiết`):** Vòng lặp ngắn và **rẻ** vì vẫn đang ở bước bản vẽ/mô phỏng, chưa chế tạo mẫu vật lý.
  2. **Từ cổng cuối SAR-EVT quay ngược về Khối 3 (`sửa thiết kế, chế tạo lại mẫu, đo lại từ TRR`):** Vòng lặp dài và **đắt nhất dự án** vì đã chế tạo mẫu và đo đạc xong hết mới phát hiện lỗi thiết kế, phải đập đi làm lại mẫu, đo lại từ TRR và tốn hạn mức vòng lặp mẫu EVT ($\le 2$ vòng, phải mở ECR trình CCB theo Ghi chú 3).

---

## KHỐI 4 · EVT — CHUẨN BỊ THỬ NGHIỆM (§5.5) & CỔNG TRR-EVT (QE Lead)
* **Nguồn:** `[Nội bộ: FLOW_TRANSCRIPT.md, Mục III.6, IV.5]` & `[Chuẩn: NASA SP-2007-6105 Rev1, Table 6.7-12, p.181]`

### 1. Khối này để làm gì?
Trước khi đóng điện bấm nút chạy thử (hoặc chạy kịch bản mô phỏng nghiệm thu chính thức), nhóm phải soạn sẵn kịch bản đo từng bước, kiểm tra dụng cụ đo xem có chuẩn không và chuẩn bị sẵn phương án xử lý nếu có sự cố. Đặc biệt, kỹ sư thiết kế phải ký cam kết rằng mẫu đem đi đo đúng y hệt như bản thiết kế đã chốt ở Khối 3. Giúp người phụ trách chất lượng (QE Lead) yên tâm cấp phép cho bắt đầu đo kiểm.

### 2. Phân tích từng gạch đầu dòng & Cổng bắt lỗi
* **Lập kế hoạch thử chi tiết; hiệu chuẩn toàn bộ thiết bị đo:** Quy trình đo từng bước (Test Plan/Procedure) và đảm bảo thiết bị đo không bị lệch số; thiếu sẽ bị **TRR-EVT** trả về (`KHÔNG ĐẠT — hiệu chuẩn lại, bổ sung đồ gá`) vì đo bằng máy lệch thì kết quả ở Khối 5 vô giá trị.
* **Nghiệm thu đồ gá và kiểm kê đủ số lượng mẫu thử:** Kiểm tra bàn gá lắp mẫu và số lượng mẫu cần đo; thiếu sẽ bị **TRR-EVT** chặn không cấp quyền đo kiểm.
* **Đánh giá rủi ro thử nghiệm + kế hoạch dự phòng sự cố:** Lường trước nguy cơ cháy nổ, giật điện, văng tải khi thử nghiệm và cách ngắt khẩn cấp; thiếu sẽ trượt câu hỏi *"Đủ điều kiện an toàn để bắt đầu đo?"* tại **TRR-EVT**.
* **PE Lead ký xác nhận cấu hình mẫu đúng baseline đã khóa:** Trưởng nhóm thiết kế (PE Lead) đối chiếu và ký biên bản cam kết mẫu thử khớp 100% với bản vẽ đã đóng băng tại CDR-EVT (*As-built vs. As-designed*); thiếu chữ ký này, **TRR-EVT** cấm đo vì nếu mẫu lắp sai bản vẽ thì đo Đạt hay Trượt đều vô nghĩa.

### 3. Ví dụ áp dụng trên đề Xe con cầu trục ($x=2$, nhóm 8.5-EMG)
* **Kế hoạch thử chi tiết & Hiệu chuẩn công cụ đo (Văn Hưng – *QE-Simulation* chủ trì):**
  * Lập kịch bản test trên MATLAB/Simulink theo sát `DVP&R L0`: Kịch bản 1 (Chạy không tải), Kịch bản 2 (Kéo tải định mức $Q = 12,222\text{ kg} + m_{nh} = 222\text{ kg}$ theo chu trình 4 góc phần tư $M_c(t)$ ở chế độ $S3$), Kịch bản 3 (Nhấn E-stop / chạm Limit switch khi đang chạy ở $v_{\max} = 0.12\text{ m/s}$).
  * "Hiệu chuẩn" môi trường Simulink: Chốt cố định bộ giải (*Solver*), bước lấy mẫu (*Sample time* $T_s$), đặt đúng các khối *Scope / To Workspace* đo $v(t), a(t), \rho(t), i_d(t), i_q(t), U_{dc}(t)$.
* **PE Lead ký xác nhận cấu hình mẫu đúng baseline đã khóa (Bình, Bá Hưng, Khải ký bàn giao cho Văn Hưng):**
  * Các bạn PE ký xác nhận file Simulink đem đi test đã nhập chính xác 14 tham số động cơ, đúng thông số $M_{qđ}, J_{qđ}$ ứng với $x=2$ ($Q=12,222\text{ kg}$, không phải số làm tròn $12,000\text{ kg}$), đúng thông số $K_p, K_i$ và $R_h$ đã khóa ở CDR-EVT.

### 4. Lỗi người mới hay mắc
Kỹ sư thiết kế (PE) vừa sửa trộm thông số trong file mô phỏng giờ chót rồi tự bấm chạy lấy đồ thị đem nộp luôn mà **không bàn giao cấu hình đã khóa cho QE kiểm tra độc lập**, hoặc cài bước thời gian (*step size*) trong Simulink quá thô làm gai nhọn đạo hàm độ giật $\rho = \text{d}a/\text{d}t$ bị tính sai dẫn đến kết luận nhầm là trượt yêu cầu $\rho_{\max} \le 2\text{ m/s}^3$.

### 5. Điểm chốt câu hỏi ôn tập tại Cổng TRR-EVT
* **Vai trò ký duyệt:** Do **QE Lead** chốt độc lập với PE Lead để đảm bảo khách quan và an toàn đo kiểm.
* **Điểm khác biệt trên nhánh kết quả:** Từ cổng **TRR-EVT** (và SIR-EVT, SAR-EVT), trên lưu đồ chỉ ghi nhận nhánh **`ĐẠT`** (không có *"ĐẠT CÓ ĐIỀU KIỆN"* như 4 cổng MCR, SRR, PDR, CDR) vì bước cấp phép an toàn đo kiểm và nghiệm thu mẫu không chấp nhận nợ điều kiện.

---

## KHỐI 5 · EVT — TÍCH HỢP & THỬ NGHIỆM (§5.6) & CỔNG SIR-EVT (PM) + CỔNG SAR-EVT (CTO)
* **Nguồn:** `[Nội bộ: FLOW_TRANSCRIPT.md, Mục III.7, IV.6, IV.7]` & `[Chuẩn: NASA SP-2007-6105 Rev1, Table 6.7-11 & 6.7-13, p.180–182]`

### 1. Khối này để làm gì?
Lắp ghép toàn bộ các phần cứng, thuật toán điều khiển và logic bảo vệ thành một hệ thống hoàn chỉnh rồi cho chạy thử nghiệm thực tế (hoặc mô phỏng tổng hợp) theo đúng kịch bản đã duyệt. Đo đạc các thông số vận hành liên tục, kiểm tra an toàn khi có lỗi, xử lý dứt điểm mọi điểm không đạt và cập nhật lại hồ sơ thực tế. Trình Quản lý dự án (PM) nghiệm thu tích hợp tại **SIR-EVT**, sau đó trình **CTO** tại **SAR-EVT** để quyết định cho lên giai đoạn tiếp theo (DVT) hay bắt làm lại / hủy dự án.

### 2. Phân tích từng gạch đầu dòng & Cổng bắt lỗi
* **Chế tạo, tích hợp mẫu EVT; chạy bench test theo DVP&R:** Ghép nối toàn hệ thống và đo kiểm từng bài theo DVP&R; thiếu hoặc trượt sẽ bị **SIR-EVT** trả về Khối 5 (`KHÔNG ĐẠT — sửa mạch / FW, tích hợp và tiền kiểm lại`).
* **Chạy liên tục không lỗi $\ge T_{\min}$ giờ; đo hotspots thực tế:** Kiểm tra độ bền vận hành liên tục và điểm phát nhiệt nóng nhất; trượt sẽ bị **SIR-EVT** và **SAR-EVT** bắt lỗi độ tin cậy.
* **Tiền kiểm SFC và EMC pre-scan đạt biên $\ge 6\text{ dB}$:** Kiểm tra an toàn khi xảy ra lỗi đơn điểm (*Single Fault Condition* / *Safety Function Check*) và nhiễu điện từ; trượt sẽ bị chặn tại **SIR-EVT / SAR-EVT**.
* **Đóng hết NCR trọng yếu chu kỳ A; cập nhật RTM, ICD:** Giải quyết sạch các báo cáo lỗi không phù hợp (NCR) và cập nhật kết quả thực tế vào RTM, ICD; còn nợ NCR trọng yếu sẽ bị **CTO** đánh trượt tại **SAR-EVT** (quay về tận Khối 3 hoặc **Hủy dự án**).

### 3. Ví dụ áp dụng trên đề Xe con cầu trục ($x=2$, nhóm 8.5-EMG)
* **Tích hợp mẫu EVT & chạy bench test theo DVP&R + Tiền kiểm SFC (Văn Hưng, Khải, Bá Hưng):**
  * Ghép nối hoàn chỉnh khối Cơ khí ($Q = 12,222\text{ kg}, m_{nh} = 222\text{ kg}$) + Biến tần FOC (14 tham số) + Quỹ đạo S-Curve + Logic bảo vệ trên MATLAB/Simulink; chạy liên tục nhiều chu kỳ chế độ $S3$ và điền kết quả vào cột *Report* của `DVP&R L0` ($v_{\max} = 0.12\text{ m/s}$, $a_{\max} \le 0.5\text{ m/s}^2$, $\rho_{\max} \le 2\text{ m/s}^3$, quá điều chỉnh $\le 10\%$).
  * *Tiền kiểm SFC (An toàn lỗi đơn):* Giả lập sự cố quá tải hoặc nhấn E-stop / chạm công tắc hành trình (Limit switch) khi xe đang chạy full tải $\to$ hệ thống phải kích hoạt phanh cơ điện từ và dừng an toàn trong $\le 2\text{ s}$.
* **Đóng NCR & cập nhật RTM, ICD (Đông – *PM/SE Lead* & Trung – *Doc Lead*):**
  * Nếu chạy thử phát hiện vọt lố tốc độ $> 10\%$ hoặc quá áp DC-bus, Văn Hưng mở phiếu **NCR** $\to$ Khải/Bình tinh chỉnh lại PI hoặc $R_h$ (vòng lặp ngắn SIR-EVT $\to$ Khối 5), test lại đạt **PASS** để đóng NCR, rồi Trung cập nhật thông số cuối vào RTM/ICD và đóng gói thuyết minh cuối kỳ.

### 4. Lỗi người mới hay mắc
Khi chạy tích hợp ở Khối 5 phát hiện lỗi phải chỉnh sửa lại thông số giao diện hoặc mạch/thuật toán nhưng **chỉ sửa trong file Simulink mà quên cập nhật ngược lại vào RTM và ICD** (làm bản vẽ một đằng, mô hình chạy một nẻo), hoặc để lỗi thiết kế nghiêm trọng lọt qua SIR-EVT lên tới tận SAR-EVT khiến phải quay về làm lại từ Khối 3.

### 5. Điểm chốt câu hỏi ôn tập tại Cổng SIR-EVT & SAR-EVT
* **Vì sao SIR-EVT (PM) nối thẳng sang SAR-EVT (CTO) không qua khối công việc trung gian?**
  * Đó là cơ chế **rà soát kép (double-check) tách biệt 2 tầng Quản lý dự án và Quản trị cấp cao**: Tại **SIR-EVT**, **PM** nghiệm thu nội bộ xem việc tích hợp kỹ thuật và tiền kiểm của nhóm đã đạt chưa (nếu chưa đạt thì cho anh em quay lại Khối 5 sửa nhanh mạch/FW). Khi bộ kết quả Khối 5 đã hoàn tất sạch sẽ, PM đệ trình nguyên bộ hồ sơ nghiệm thu đó lên **SAR-EVT** để **CTO** ra quyết định chiến lược ở cấp công ty: chính thức nghiệm thu mẫu EVT (TRL 5) cho phép đầu tư chuyển sang giai đoạn **DVT (Mẫu chu kỳ B)**.
* **Điều gì xảy ra nếu trượt SAR-EVT quá 2 vòng lặp (`vòng lặp mẫu EVT ≤ 2` theo Ghi chú 3)?**
  * Mỗi vòng lặp mẫu mới bắt buộc phải mở **ECR (Engineering Change Request)** trình hội đồng **CCB (§9)**. Nếu vượt ngưỡng 2 vòng lặp mà vẫn không đạt, **CTO sẽ đánh giá lại tính khả thi của toàn bộ dự án (`§4.1.5c`)** và có toàn quyền kích hoạt nhánh **`HỦY DỰ ÁN — CTO quyết định`** để đưa về trạng thái **`TẠM DỪNG / HỦY DỰ ÁN (§8.3 · §8.4)`**.
