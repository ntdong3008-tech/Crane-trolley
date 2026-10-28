# MA TRẬN TRUY XUẤT YÊU CẦU (RTM) VÀ KẾ HOẠCH KIỂM CHỨNG THIẾT KẾ (DVP)

**Học phần:** Thiết kế hệ thống truyền động điện (ĐH Bách khoa Hà Nội)  
**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Đề tài:** Hệ truyền động di chuyển xe con cầu trục dầm đôi (Động cơ KĐB rotor lồng sóc + Biến tần, điều khiển FOC, quỹ đạo S-curve)  
**Nhóm sinh viên thực hiện:** Nhóm 8.5-EMG (Đề bài ứng với STT 22, tham số $x = 2$)  
**Nguồn số liệu duy nhất:** `Block 1/00_Bang_thong_so_goc.md` và `Block 1/01_SRS_Baseline_A.md` (Đã duyệt)  
**Công cụ kiểm chứng:** Phân tích giải tích / Excel (A), Mô phỏng MATLAB/Simulink (S), Tra cứu catalogue nhà sản xuất (I).  
**Lịch sử:** **v1.4 (28/10/2026, Người dùng duyệt)** chốt phạm vi môn học (CR-08..CR-13); DV-08 tính $k_{dt}$ ở lưới danh định · v1.2 (24/10/2026) đóng băng tại SRR · **v1.3 (26/10/2026, Người dùng duyệt nhóm A)** tích hợp SRS Baseline A.1: RTM và DV-08 dùng $k_{dt} \ge 1.20$ (CR-01), tiêu chí FAIL của DV-08 theo CR-02. *(Tên tệp giữ hậu tố v1.2.)*

---

## 1. NGUYÊN TẮC QUẢN LÝ DỮ LIỆU VÀ PHƯƠNG PHÁP KIỂM CHỨNG

### 1.1. Phân loại nguồn số liệu bắt buộc
- **[A] Đề bài:** Số liệu do giảng viên giao trực tiếp trong đề bài tập lớn ($x = 2$).
- **[B] Tính toán từ [A]:** Số liệu tính từ các thông số [A] bằng công thức cơ học / truyền động điện rõ ràng.
- **[C] Giả định của nhóm:** Số liệu nhóm tự chọn (lấy số tròn, kèm 1 câu lý do kỹ thuật và ghi rõ mốc kiểm tra lại ở các khối sau).

### 1.2. Bảng thông số kỹ thuật gốc sử dụng trong kiểm chứng (SSoT)

| Mã | Tên thông số | Ký hiệu | Giá trị | Đơn vị | Loại | Căn cứ xác định / Công thức |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **P-01** | Tải trọng nâng định mức | $Q$ | 12,222 | kg | **[A]** | Đề bài giao ($x = 2$) |
| **P-02** | Khối lượng cơ cấu nâng hạ | $m_{nh}$ | 222 | kg | **[A]** | Đề bài giao ($x = 2$) |
| **P-03** | Khối lượng bản thân xe con | $m_{xc}$ | 1,800 | kg | **[C]** | Giả định bằng ~15% tải định mức; kiểm tra lại ở Khối 2 |
| **P-04** | Tổng khối lượng đầy tải | $M_\Sigma$ | 14,244 | kg | **[B]** | $M_\Sigma = Q + m_{nh} + m_{xc} = 12,222 + 222 + 1,800$ (P-01 + P-02 + P-03) |
| **P-05** | Tổng khối lượng không tải | $m_{\text{tĩnh}}$ | 2,022 | kg | **[B]** | $m_{\text{tĩnh}} = m_{xc} + m_{nh} = 1,800 + 222$ (P-03 + P-02) |
| **P-06** | Chiều cao nâng lớn nhất (chiều dài cáp) | $h$ | 12 | m | **[A]** | Đề bài giao ($x = 2$) |
| **P-07** | Tần số góc dao động riêng cáp | $\omega_p$ | 0.904 | rad/s | **[B]** | $\omega_p = \sqrt{g / h} = \sqrt{9.81 / 12}$ (P-18, P-06) |
| **P-08** | Chu kỳ dao động riêng cáp | $T_p$ | 6.95 | s | **[B]** | $T_p = 2\pi / \omega_p = 2\pi / 0.904$ (P-07) |
| **P-09** | Vận tốc di chuyển ngang lớn nhất | $v_{\max}$ | 0.12 | m/s | **[A]** | Đề bài giao ($x = 2$, tương đương $7.2\text{ m/phút}$) |
| **P-10** | Gia tốc cực đại cho phép | $a_{\max}$ | 0.5 | m/s$^2$ | **[A]** | Đề bài giao ($x = 2$) |
| **P-11** | Độ giật cực đại cho phép | $\rho_{\max}$ | 2.0 | m/s$^3$ | **[A]** | Đề bài giao ($x = 2$) |
| **P-12** | Đường kính bánh xe di chuyển | $D_{bx}$ | 0.25 | m | **[C]** | Chọn theo đường kính tiêu chuẩn tải trục 3.5 tấn/bánh; kiểm tra lại ở Khối 2 |
| **P-13** | Suất cản lăn riêng tương đương | $w_0$ | 0.015 | - | **[C]** | Bánh thép trên ray thép có ổ lăn đỡ trục; kiểm tra lại ở Khối 2 |
| **P-14** | Hệ số bám dính bánh thép trên ray | $\varphi$ | 0.20 | - | **[C]** | Hệ số ma sát bám ray thép khô kiểm tra chống trượt; kiểm tra lại ở Khối 2 |
| **P-15** | Hiệu suất truyền động cơ khí | $\eta$ | 0.90 | - | **[C]** | Hộp giảm tốc bánh răng trụ 3 cấp kèm khớp nối và ổ lăn; kiểm tra lại ở Khối 2 |
| **P-16** | Tỷ số truyền sơ bộ hộp số | $i$ | 150 | - | **[C]** | Ước tính từ tốc độ động cơ 1440 vg/ph và bánh xe 9.17 vg/ph; kiểm tra lại ở Khối 2 |
| **P-17** | Chế độ làm việc định mức | Chế độ | S3 - 40% | - | **[C]** | Chế độ ngắn hạn lặp lại đặc trưng của xe con cầu trục; kiểm tra lại ở Khối 2 |
| **P-18** | Gia tốc trọng trường | $g$ | 9.81 | m/s$^2$ | **[C]** | Hằng số trọng trường quy chuẩn tại Việt Nam; kiểm tra lại ở Khối 2 |
| **P-19** | Nguồn điện lưới cấp vào | $U_{\text{lưới}}$ | 380 ± 10% / 50 | V / Hz | **[C]** | Lưới điện hạ thế công nghiệp tiêu chuẩn; kiểm tra lại ở Khối 2 |
| **P-20** | Lực cản chuyển động tĩnh đầy tải | $F_{c.\text{đầy}}$ | 2,096 | N | **[B]** | $F_{c.\text{đầy}} = M_\Sigma \cdot g \cdot w_0 = 14,244 \cdot 9.81 \cdot 0.015 \approx 2,096\text{ N}$ |

### 1.3. Ba phương pháp kiểm chứng được phép áp dụng
1. **Phân tích giải tích (A - Analysis):** Tính toán bằng công thức giải tích cơ học, truyền động điện trên giấy hoặc bảng tính Excel.
2. **Mô phỏng Simulink (S - Simulation):** Xây dựng mô hình toán trên phần mềm MATLAB/Simulink và chạy mô phỏng theo kịch bản để trích xuất đáp ứng thời gian thực.
3. **Kiểm tra catalogue (I - Inspection):** Soát xét, đối chiếu trực tiếp thông số kỹ thuật động cơ, biến tần, phanh cơ trong tài liệu chính thức của nhà sản xuất.

---

## 2. MA TRẬN TRUY XUẤT YÊU CẦU HAI CHIỀU (BIDIRECTIONAL RTM)

Ma trận RTM thiết lập mối liên kết hai chiều chặt chẽ ánh xạ **1-1 giữa 8 mã yêu cầu kỹ thuật hệ thống (`SRS Baseline A`) với 8 bài kiểm chứng thiết kế (`DV-01` $\to$ `DV-08`)** và các gói công việc WBS tương ứng.

### 2.1. Chiều truy xuất xuôi (Forward Traceability: PRD → SRS → DV → Khối thực hiện)

| Mã PRD | Tên yêu cầu sản phẩm | Mã SRS | Tóm tắt nội dung yêu cầu kỹ thuật hệ thống | Bài kiểm chứng | Khối thực hiện (Mã WBS) |
| :---: | :--- | :---: | :--- | :---: | :--- |
| **PRD-FUNC-01** | Vận hành 4 góc phần tư & di chuyển 2 chiều | **SRS-FUNC-01** | Vận hành di chuyển 2 chiều Tiến/Lùi trên 4 góc phần tư, phản hồi vòng kín 01 Encoder gắn trục động cơ. | **DV-01** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) |
| **PRD-FUNC-04** | Phối hợp phanh cơ khí và mô-men điện | **SRS-FUNC-02** | Khóa chéo cấm đảo chiều khi $v \ne 0$ và đồng bộ đóng/mở phanh cơ điện từ, độ trôi dừng xe $\Delta s \le \pm 10\text{ mm}$. | **DV-02** | Khối 3 (SOW-3.4) & Khối 5 (SOW-5.1) |
| **PRD-FUNC-02** | Điều chỉnh tốc độ & làm mềm chuyển động | **SRS-FUNC-03** | Quy hoạch quỹ đạo đặt S-curve 7 đoạn liên tục với gia tốc đặt $\lvert a^* \rvert \le 0.5\text{ m/s}^2$ và độ giật đặt $\lvert \rho^* \rvert \le 2.0\text{ m/s}^3$. | **DV-03** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) |
| **PRD-FUNC-03** | Hấp thụ và tiêu tán năng lượng hãm | **SRS-FUNC-04** | Tiêu tán năng lượng hãm tái sinh qua mạch van hãm và điện trở xả $R_h$, biến tần không ngắt lỗi quá áp DC-link. | **DV-04** | Khối 3 (SOW-3.1) & Khối 5 (SOW-5.1) |
| **PRD-PERM-01** | Đáp ứng tải trọng kéo ngang định mức | **SRS-PERM-01** | Đủ lực kéo thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ (với $\eta = 0.90$) và đảm bảo hệ số an toàn bám chống trượt ray $k_{\text{bám}} \ge 1.20$. | **DV-05** | Khối 2 (SOW-2.1) & Khối 5 (SOW-5.1) |
| **PRD-PERM-02** | Vận tốc định mức của xe con | **SRS-PERM-02** | Đưa xe con đạt vận tốc dài xác lập định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ ($[0.114;\ 0.126]\text{ m/s}$) theo cả hai chiều di chuyển. | **DV-06** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) |
| **PRD-PERM-03** | Giới hạn gia tốc & độ giật chống lắc | **SRS-PERM-03** | Khống chế chuyển động thực tế đạt gia tốc $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và độ giật $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$ với cáp treo dài $h = 12\text{ m}$. | **DV-07** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) |
| **PRD-PERM-04** | Khả năng làm việc ở chế độ nhiệt S3 | **SRS-PERM-04** | Đảm bảo hệ số dự trữ phát nhiệt $k_{dt} \ge 1.20$ ở chế độ S3 - 40% ở lưới danh định $380\text{ V}$, không quá nhiệt cuộn dây. | **DV-08** | Khối 2 (SOW-2.1) & Khối 3 (SOW-3.1) |

---

### 2.2. Chiều truy xuất ngược (Backward Traceability: DV → SRS → PRD → Người phụ trách)

| Bài kiểm chứng | Mã SRS gốc | Mã PRD gốc | Phương pháp | Khối thực hiện (Mã WBS) | Người phụ trách chính |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **DV-01** | SRS-FUNC-01 | PRD-FUNC-01 | **S** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) | Trần Đỗ Khải (Điều khiển) & Phạm Văn Hưng (Mô phỏng) |
| **DV-02** | SRS-FUNC-02 | PRD-FUNC-04 | **S** | Khối 3 (SOW-3.4) & Khối 5 (SOW-5.1) | Nguyễn Bá Hưng (Logic) & Phạm Văn Hưng (Mô phỏng) |
| **DV-03** | SRS-FUNC-03 | PRD-FUNC-02 | **A / S** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) | Trần Đỗ Khải (Điều khiển) & Phạm Văn Hưng (Mô phỏng) |
| **DV-04** | SRS-FUNC-04 | PRD-FUNC-03 | **A / S** | Khối 3 (SOW-3.1) & Khối 5 (SOW-5.1) | Đặng Nguyên Bình (Phần cứng) & Phạm Văn Hưng (Mô phỏng) |
| **DV-05** | SRS-PERM-01 | PRD-PERM-01 | **A / S** | Khối 2 (SOW-2.1) & Khối 5 (SOW-5.1) | Đặng Nguyên Bình (Phần cứng) & Phạm Văn Hưng (Mô phỏng) |
| **DV-06** | SRS-PERM-02 | PRD-PERM-02 | **S** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) | Trần Đỗ Khải (Điều khiển) & Phạm Văn Hưng (Mô phỏng) |
| **DV-07** | SRS-PERM-03 | PRD-PERM-03 | **A / S** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) | Trần Đỗ Khải (Điều khiển) & Phạm Văn Hưng (Mô phỏng) |
| **DV-08** | SRS-PERM-04 | PRD-PERM-04 | **A / I** | Khối 2 (SOW-2.1) & Khối 3 (SOW-3.1) | Đặng Nguyên Bình (Phần cứng) |

---

## 3. KẾ HOẠCH KIỂM CHỨNG THIẾT KẾ CẤP HỆ THỐNG (DVP — 8 BÀI KIỂM CHỨNG)

Tài liệu DVP là nơi đặc tả chi tiết kịch bản kiểm thử, điều kiện tải, tín hiệu đo và tiêu chí Pass/Fail định lượng tuyệt đối cho từng yêu cầu kỹ thuật của hệ thống.

### 3.1. Bảng kế hoạch kiểm chứng thiết kế cấp hệ thống (DVP Table)

| Mã DV | Mã SRS | Phương pháp | Kịch bản thử nghiệm & Điều kiện tải | Tín hiệu đo / Đại lượng kiểm tra | Tiêu chí ĐẠT (PASS Criteria) | Tiêu chí BÁC BỎ (FAIL Criteria) |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- |
| **DV-01** | **SRS-FUNC-01** | **S** | Mô phỏng Simulink hệ truyền động chạy Tiến rồi phát lệnh đảo chiều sang Lùi ở cả hai trạng thái: đầy tải $14,244\text{ kg}$ (P-04) và không tải $2,022\text{ kg}$ (P-05). | • Tốc độ góc rotor $\omega(t)$<br>• Mô-men điện từ $M_e(t)$<br>• Tín hiệu xung phản hồi từ Encoder | **PASS khi:** Hệ thống vận hành ổn định trên cả 4 góc phần tư I, II, III, IV; mạch vòng FOC nhận phản hồi liên tục từ 01 Encoder để kiểm soát tốc độ. | **FAIL khi:** Mất đồng bộ điều khiển FOC, không tạo được mô-men hãm điện ở góc II/IV hoặc đứt tín hiệu Encoder. |
| **DV-02** | **SRS-FUNC-02** | **S** | Mô phỏng Simulink phát lệnh đảo chiều đột ngột khi xe con đang chạy nhanh; tiếp tục quan sát chu trình giảm tốc về 0 m/s và kích hoạt phanh cơ ở đầy tải $14,244\text{ kg}$. | • Vận tốc dài xe con $v(t)$<br>• Lệnh logic khóa chéo đảo chiều<br>• Trạng thái đóng/mở phanh cơ<br>• Độ trôi dừng xe $\Delta s$ | **PASS khi:** Mạch khóa chéo ngăn đảo chiều khi $v \ne 0\text{ m/s}$; phanh cơ chỉ mở khi động cơ đã sinh mô-men giữ; độ trôi dừng xe sau khi đóng phanh thỏa mãn $\Delta s \le \pm 10\text{ mm}$ (danh định không trôi $\Delta s = 0$). | **FAIL khi:** Cho phép đảo chiều khi xe chưa dừng hẳn ($v \ne 0$), hoặc trôi xe tự do khi mở phanh, hoặc độ trôi dừng $\Delta s > 10\text{ mm}$. |
| **DV-03** | **SRS-FUNC-03** | **A / S** | Tính toán giải tích thông số 7 đoạn S-curve; mô phỏng khối tạo quỹ đạo nạp lượng đặt tốc độ bậc thang từ $0 \to 0.12\text{ m/s}$ và trích xuất đường đặt thời gian thực. | • Quỹ đạo tốc độ đặt $\omega^*(t)$<br>• Gia tốc đặt $a^*(t)$<br>• Độ giật đặt $\rho^*(t) = \text{d}a^*/\text{d}t$ | **PASS khi:** Quỹ đạo gia tốc đặt $a^*(t)$ biến thiên liên tục hình thang, đạt đỉnh $\lvert a^*(t) \rvert \le 0.5\text{ m/s}^2$ và đạo hàm gia tốc đặt $\lvert \rho^*(t) \rvert \le 2.0\text{ m/s}^3$ (không có xung giật vô hạn). | **FAIL khi:** Xuất hiện bước nhảy gia tốc đột ngột hoặc $\lvert a^*(t) \rvert > 0.5\text{ m/s}^2$ hoặc $\lvert \rho^*(t) \rvert > 2.0\text{ m/s}^3$. |
| **DV-04** | **SRS-FUNC-04** | **A / S** | Tính toán giải tích công suất hãm cực đại; mô phỏng quá trình giảm tốc hãm tái sinh từ $0.12\text{ m/s}$ về $0\text{ m/s}$ khi mang đầy tải $14,244\text{ kg}$ (P-04) [B]. | • Điện áp khâu DC-link $U_{\text{dc}}(t)$<br>• Dòng xả qua điện trở hãm $I_{Rh}(t)$<br>• Trạng thái cờ ngắt lỗi biến tần | **PASS khi:** Toàn bộ động năng hãm được tiêu tán an toàn qua điện trở xả hãm $R_h$; biến tần duy trì hoạt động bình thường, không báo lỗi ngắt mạch quá áp khâu DC-link. | **FAIL khi:** Biến tần báo lỗi quá áp DC-link làm ngắt mạch lực trong quá trình giảm tốc hãm tái sinh đầy tải. |
| **DV-05** | **SRS-PERM-01** | **A / S** | Tính toán giải tích lực cản, lực kéo và mô phỏng xe con di chuyển trên ray ở đầy tải $14,244\text{ kg}$ ($w_0 = 0.015$, $\eta = 0.90$) và không tải $2,022\text{ kg}$; kiểm tra chống trượt ray khô ($\varphi = 0.20$). | • Lực kéo tiếp tuyến bánh xe $F_k(t)$<br>• Lực cản lăn tĩnh $F_{c.\text{đầy}}$<br>• Hệ số an toàn bám $k_{\text{bám}} = F_{\text{bám}} / F_{k,\max}$ | **PASS khi:** Hệ thống sản sinh đủ lực kéo thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ (P-20) [B]; hệ số an toàn bám chống trượt thỏa mãn $k_{\text{bám}} \ge 1.20$ ở mọi thời điểm gia tốc. | **FAIL khi:** Không thắng được lực cản tĩnh đầy tải hoặc $k_{\text{bám}} < 1.20$ gây trượt quay bánh xe dẫn hướng trên ray. |
| **DV-06** | **SRS-PERM-02** | **S** | Mô phỏng Simulink xe con chạy xác lập theo lệnh vận tốc định mức theo cả chiều Tiến và chiều Lùi trên toàn dải tải trọng ($2,022\text{ kg} \div 14,244\text{ kg}$). | • Vận tốc dài xác lập thực tế $v(t)$<br>• Tốc độ góc trục bánh xe $\omega_{\text{bx}}(t)$ | **PASS khi:** Vận tốc dài xác lập thực tế của xe con đạt mốc $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ (dải $[0.114;\ 0.126]\text{ m/s}$) theo cả hai chiều chuyển động ở mọi trạng thái tải. | **FAIL khi:** Vận tốc xác lập thực tế nằm ngoài dải quy chuẩn $[0.114;\ 0.126]\text{ m/s}$ (thiếu tốc độ hoặc vượt tốc). |
| **DV-07** | **SRS-PERM-03** | **A / S** | Mô phỏng xe con mang tải treo cáp dài $12\text{ m}$ (P-06) [A] thực hiện toàn bộ chu trình tăng tốc và giảm tốc; đo gia tốc và độ giật thực tế qua bộ lọc đạo hàm $G_d(s) = \frac{s}{T_f s + 1}$. | • Gia tốc thực tế $a(t) = \text{d}v/\text{d}t$<br>• Độ giật thực tế $\rho(t) = \text{d}a/\text{d}t$<br>• Góc lắc tải treo $\theta(t)$ | **PASS khi:** Độ lớn gia tốc ngang thực tế khống chế $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và độ giật ngang thực tế khống chế $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$ trong mọi pha chuyển động bình thường. | **FAIL khi:** Gia tốc vượt ngưỡng $\lvert a(t) \rvert > 0.5\text{ m/s}^2$ hoặc độ giật vượt ngưỡng $\lvert \rho(t) \rvert > 2.0\text{ m/s}^3$. |
| **DV-08** | **SRS-PERM-04** | **A / I** | Tính toán giải tích công suất phát nhiệt đẳng trị $P_{\text{đt}}$ theo chu kỳ làm việc $S3 - 40\%$ ($CD = 40\%$, $T_{\text{ck}} = 10\text{ phút}$) ở lưới danh định $380\text{ V}$ (quá tải mô-men kiểm ở $342\text{ V}$); đối chiếu với catalogue động cơ chọn ở Khối 2. | • Công suất đẳng trị tính toán $P_{\text{đt}}$<br>• Công suất định mức catalogue $P_{\text{đm}}$<br>• Hệ số dự trữ nhiệt $k_{dt} = P_{\text{đm}} / P_{\text{đt}}$ | **PASS khi:** Động cơ tra từ catalogue nhà sản xuất có công suất định mức thỏa mãn hệ số dự trữ phát nhiệt $k_{dt} \ge 1.20$ mà không bị quá nhiệt cuộn dây. | **FAIL khi:** Hệ số dự trữ nhiệt $k_{dt} < 1.20$ (nguy cơ quá nhiệt cháy động cơ) hoặc $\lambda_K (U_{\min}/U_N)^2 < M_{\max}/M_N$ (không đủ mô-men khi lưới −10% — SRS A.1, CR-02). |

---

### 3.2. Kịch bản mô phỏng tích hợp trên một mô hình Simulink

Toàn bộ 7 bài kiểm chứng mô phỏng (**DV-01 đến DV-07**) được tích hợp và kiểm chứng đồng thời trên **một mô hình Simulink duy nhất**, giảm thiểu tối đa khối lượng thiết lập mô phỏng cho sinh viên:

1. **Cấu trúc mô hình Simulink hợp nhất:**
   - **Khối Nguồn & Biến tần:** Khâu trung gian DC-link, bộ nghịch lưu IGBT điều chế SVPWM và mạch van xả hãm qua điện trở $R_h$ (**DV-04**).
   - **Khối Động cơ KĐB & Cảm biến:** Mô hình động cơ không đồng bộ rotor lồng sóc trong hệ tọa độ tựa từ thông rotor (RFOC) kết hợp 01 Encoder đo góc quay và tốc độ trục rotor (**DV-01**).
   - **Khối Điều khiển FOC & Quỹ đạo S-curve:** Bộ tạo quỹ đạo S-curve 7 đoạn làm trơn lượng đặt gia tốc và tốc độ (**DV-03**) kết hợp hai mạch vòng dòng điện $i_d, i_q$ và mạch vòng tốc độ $\omega$ (**DV-06**).
   - **Khối Logic Vận hành & Phanh cơ:** Khối máy trạng thái FSM điều khiển 4 góc phần tư, kích hoạt mở phanh khi có mô-men giữ, đóng phanh khi tốc độ dừng và khóa chéo cấm đảo chiều khi $v \ne 0$ (**DV-01, DV-02**).
   - **Khối Cơ cấu Cơ khí & Tải treo:** Mô hình cơ cấu bánh xe lăn trên ray ($w_0 = 0.015, \eta = 0.90, \varphi = 0.20$) mang tải trọng chuyển động ngang (**DV-05**) và mô hình con lắc cáp đơn có chiều dài lớn nhất $h = 12\text{ m}$ (**DV-07**).

2. **Quy trình chạy kịch bản thử nghiệm hợp nhất (Một lần Run mô phỏng):**
   - **Pha 1 (Khởi hành đầy tải chiều Tiến):** Nạp đầy tải $14,244\text{ kg}$ (P-04) [B]. Động cơ kích từ tạo mô-men giữ rồi mở phanh cơ an toàn (**DV-02**); bộ tạo S-curve tăng tốc lượng đặt (**DV-03**) khống chế gia tốc thực tế $\le 0.5\text{ m/s}^2$ và độ giật thực tế $\le 2.0\text{ m/s}^3$ (**DV-07**); hệ thống sản sinh lực kéo thắng lực cản lăn tĩnh $F_{c.\text{đầy}} = 2,096\text{ N}$ mà không bị trượt bánh xe ray ($k_{\text{bám}} \ge 1.20$) (**DV-05**); xe con đạt vận tốc xác lập định mức $0.12\text{ m/s} \pm 5\%$ (**DV-06**).
   - **Pha 2 (Đảo chiều đột ngột & Hãm tái sinh):** Khi xe đang chạy Tiến ở vận tốc $0.12\text{ m/s}$, phát lệnh đảo chiều sang Lùi. Mạch khóa chéo ngăn đảo chiều ngay lập tức (**DV-02**); hệ thống chuyển sang chế độ hãm tái sinh (Góc phần tư II), tiêu tán năng lượng qua điện trở hãm $R_h$ bảo vệ biến tần không ngắt quá áp DC-link (**DV-04**); khi tốc độ xe con giảm về dừng hẳn thì phanh cơ tự động đóng kẹp trục an toàn với độ trôi $\Delta s \le \pm 10\text{ mm}$ (**DV-02**).
   - **Pha 3 (Chạy Lùi không tải & Hoàn tất chu trình 4Q):** Chuyển sang trạng thái không tải $2,022\text{ kg}$ (P-05) [B]. Hệ thống mở phanh, tăng tốc chạy Lùi (Góc phần tư III) đạt vận tốc xác lập danh định $-0.12\text{ m/s} \pm 5\%$ (**DV-01, DV-06**); sau đó hãm tái sinh dừng xe (Góc phần tư IV) (**DV-01, DV-04**) và đóng phanh cơ khóa cứng trục kết thúc chu trình.

---

## 4. PHÂN CÔNG TRÁCH NHIỆM VÀ PHỐI HỢP SOW

Danh mục 8 bài kiểm chứng thiết kế (**DV-01 đến DV-08**) được phân công rõ ràng cho các thành viên nhóm theo đúng cấu trúc WBS của dự án:

1. **Phần cứng công suất & Cơ điện (Đặng Nguyên Bình):**
   - Chịu trách nhiệm chính bài **DV-04** (tính chọn điện trở hãm $R_h$ ở `SOW-3.1`), bài **DV-05** (tính chọn động cơ thắng lực cản $2,096\text{ N}$ ở `SOW-2.1`) và bài **DV-08** (kiểm nghiệm phát nhiệt $S3 - 40\%$ theo catalogue động cơ ở `SOW-2.1` & `SOW-3.1`).
2. **Thuật toán điều khiển FOC & S-curve (Trần Đỗ Khải):**
   - Chịu trách nhiệm chính bài **DV-01** (tổng hợp điều khiển vector RFOC ở `SOW-3.3`), bài **DV-03** (thiết kế thuật toán tạo quỹ đạo S-curve 7 đoạn ở `SOW-3.3`), bài **DV-06** (chỉnh định mạch vòng tốc độ đạt $v_{\max} = 0.12\text{ m/s} \pm 5\%$ ở `SOW-3.3`) và bài **DV-07** (khống chế gia tốc và độ giật chống rung lắc ở `SOW-3.3`).
3. **Logic chuyển trạng thái & Phối hợp an toàn (Nguyễn Bá Hưng):**
   - Chịu trách nhiệm chính bài **DV-02** (thiết kế khối logic khóa chéo đảo chiều và phối hợp đóng/mở phanh cơ ở `SOW-3.4`).
4. **Mô phỏng tích hợp Simulink & Báo cáo DVP&R (Phạm Văn Hưng):**
   - Chịu trách nhiệm xây dựng mô hình Simulink hợp nhất, chạy kịch bản thử nghiệm và trích xuất dữ liệu nghiệm thu cho 7 bài mô phỏng (**DV-01 đến DV-07**) tại Khối 5 (`SOW-5.1` & `SOW-5.2`).

---

## 5. TÀI LIỆU THAM KHẢO

1. Bộ môn Tự động hóa Xí nghiệp Công nghiệp, *Đề bài tập lớn môn Thiết kế hệ truyền động điện (Học kỳ 2023.1, Đề 0~9, STT 22, tham số $x = 2$)*, Trường ĐH Bách khoa Hà Nội, 2023.
2. TS. Nguyễn Duy Đỉnh, *Bài giảng Thiết kế hệ truyền động điện (Bài 4: Hệ truyền động cơ cấu di chuyển xe con cầu trục)*, Trường ĐH Bách khoa Hà Nội, 2021.
3. PGS.TS. Bùi Quốc Khánh, TS. Nguyễn Phùng Quang, *Điều chỉnh tự động truyền động điện*, NXB Khoa học và Kỹ thuật, Hà Nội.
4. Bộ Khoa học và Công nghệ, *TCVN 4244:2005: Thiết bị nâng - Thiết kế, chế tạo và kiểm tra kỹ thuật*, Hà Nội, 2005.
5. Tiêu chuẩn quốc tế IEC 60034-1, *Rotating electrical machines - Part 1: Rating and performance* (Quy chuẩn chế độ làm việc ngắn hạn lặp lại S3).
6. Tiêu chuẩn quốc tế ISO/IEC/IEEE 29119:2022, *Software and systems engineering - Software testing*.
7. Tiêu chuẩn quốc tế ISO/IEC/IEEE 29148:2018, *Systems and software engineering - Life cycle processes - Requirements engineering*.
