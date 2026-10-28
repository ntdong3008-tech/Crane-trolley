# ĐẶC TẢ YÊU CẦU KỸ THUẬT HỆ THỐNG (SRS BASELINE A)

**Học phần:** Thiết kế hệ thống truyền động điện (ĐH Bách khoa Hà Nội)  
**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Đề tài:** Hệ truyền động di chuyển xe con cầu trục dầm đôi (Động cơ KĐB rotor lồng sóc + Biến tần, điều khiển FOC, quỹ đạo S-curve)  
**Nhóm sinh viên thực hiện:** Nhóm 8.5-EMG (Đề bài ứng với STT 22, tham số $x = 2$)  
**Nguồn số liệu duy nhất:** `Block 1/00_Bang_thong_so_goc.md` (Đã duyệt)  
**Công cụ kiểm chứng:** Phân tích giải tích / Excel (A), Mô phỏng MATLAB/Simulink (S), Kiểm tra catalogue nhà sản xuất (I).  
**Lịch sử:** v1.2 (24/10/2026) Baseline A đóng băng tại SRR · **v1.3 (26/10/2026, Người dùng duyệt nhóm A)** tích hợp SRS Baseline A.1 đã ký: `SRS-PERM-04` $k_{dt} \ge 1.20$ (CR-01, bỏ cận trên 1.50); Downstream #6 $F_{\max}$ = 9.22 kN (số 9.25 kN cũ suy từ lực cản tính sai 2,120 N; dải [8.80; 9.70] kN giữ nguyên). **v1.4 (28/10/2026, Người dùng duyệt)** chốt phạm vi môn học: bổ sung hai mục Ngoài phạm vi ở §1.2 (CR-08..CR-12); `SRS-PERM-04`: $k_{dt}$ tính ở lưới danh định 380 V, quá tải mô-men kiểm ở lưới −10% (CR-13); Downstream #3, #6 bỏ dung sai (CR-16, CR-17). Nhật ký CR đầy đủ: `Block 3/04_SRS_A1_Dan_xuat_RTM_DVP_WCCA_v1.0.md` §1. *(Tên tệp giữ hậu tố v1.2 để không gãy liên kết.)*

---

## 1. PHẠM VI HỆ THỐNG

### 1.1. Trong phạm vi (In-Scope)
- Thiết kế hệ truyền động điện điều khiển di chuyển ngang xe con 2 chiều (Tiến/Lùi) hoạt động trên 4 góc phần tư của mặt phẳng Tốc độ – Mô-men.
- Bộ biến tần điều khiển vector tựa từ thông rotor (FOC) kết hợp bộ tạo quỹ đạo tốc độ hình chữ S 7 đoạn (7-segment S-curve).
- Mạch van hãm (Braking Chopper) và điện trở xả hãm $R_h$ tiêu tán năng lượng tái sinh bảo vệ biến tần khỏi sự cố quá áp.
- Khối logic chuyển trạng thái phối hợp an toàn: khóa chéo cấm đảo chiều khi cơ cấu chưa dừng hẳn và điều khiển đồng bộ phanh cơ điện từ với mô-men động cơ.
- Tính chọn động cơ KĐB rotor lồng sóc làm việc ở chế độ ngắn hạn lặp lại S3 - 40%, hộp giảm tốc và kiểm tra điều kiện chống trượt bánh xe trên ray.

### 1.2. Ngoài phạm vi (Out-of-Scope)
- Cơ cấu nâng hạ tải (động cơ nâng hạ, tang cuốn cáp, cụm móc treo).
- Kết cấu cơ khí dầm chính cầu trục và ray dẫn hướng nhà xưởng.
- Cơ cấu di chuyển dầm cầu trục dọc nhà xưởng.
- Điều khiển chống lắc tải (vòng kín hoặc hở). S-curve chỉ giới hạn gia tốc và độ giật; góc lắc $\theta(t)$ được quan sát và báo cáo, không là tiêu chí nghiệm thu; 0 cảm biến trên cáp treo.
- Kiểm chứng độ bền vững theo dung sai số liệu đầu vào, khảo sát độ nhạy tham số động cơ, mô phỏng chu trình S3 đầy đủ và mô phỏng ở lưới ±10% (dao động lưới ±10% và chu trình nhiệt S3 được kiểm bằng tính toán).
- Thiết kế chi tiết mạch điện tử, mạch điều khiển vi xử lý hoặc bo mạch van công suất bán dẫn IGBT của biến tần.

---

## 2. BẢNG TRA CỨU SỐ LIỆU ĐẦU VÀO ĐÃ DUYỆT (SSoT)

*(Nguồn số liệu duy nhất trích xuất từ `Block 1/00_Bang_thong_so_goc.md`)*

| Mã | Tên thông số | Ký hiệu | Giá trị | Đơn vị | Loại | Căn cứ xác định / Công thức |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **P-01** | Tải trọng nâng định mức | $Q$ | 12,222 | kg | **[A]** | Đề bài giao ($x = 2$) |
| **P-02** | Khối lượng cơ cấu nâng hạ | $m_{nh}$ | 222 | kg | **[A]** | Đề bài giao ($x = 2$) |
| **P-03** | Khối lượng bản thân xe con | $m_{xc}$ | 1,800 | kg | **[C]** | Giả định bằng ~15% tải định mức theo pa lăng 15t; kiểm tra lại ở Khối 2 |
| **P-04** | Tổng khối lượng đầy tải | $M_\Sigma$ | 14,244 | kg | **[B]** | $M_\Sigma = Q + m_{nh} + m_{xc} = 12,222 + 222 + 1,800$ (P-01 + P-02 + P-03) |
| **P-05** | Tổng khối lượng không tải | $m_{\text{tĩnh}}$ | 2,022 | kg | **[B]** | $m_{\text{tĩnh}} = m_{xc} + m_{nh} = 1,800 + 222$ (P-03 + P-02) |
| **P-06** | Chiều cao nâng lớn nhất (chiều dài cáp) | $h$ | 12 | m | **[A]** | Đề bài giao ($x = 2$) |
| **P-07** | Tần số góc dao động riêng con lắc cáp | $\omega_p$ | 0.904 | rad/s | **[B]** | $\omega_p = \sqrt{g / h} = \sqrt{9.81 / 12}$ (P-18, P-06) |
| **P-08** | Chu kỳ dao động riêng con lắc cáp | $T_p$ | 6.95 | s | **[B]** | $T_p = 2\pi / \omega_p = 2\pi / 0.904$ (P-07) |
| **P-09** | Vận tốc di chuyển ngang lớn nhất | $v_{\max}$ | 0.12 | m/s | **[A]** | Đề bài giao ($x = 2$, tương đương $7.2\text{ m/phút}$) |
| **P-10** | Gia tốc cực đại cho phép | $a_{\max}$ | 0.5 | m/s$^2$ | **[A]** | Đề bài giao ($x = 2$) |
| **P-11** | Độ giật cực đại cho phép | $\rho_{\max}$ | 2.0 | m/s$^3$ | **[A]** | Đề bài giao ($x = 2$) |
| **P-12** | Đường kính bánh xe di chuyển | $D_{bx}$ | 0.25 | m | **[C]** | Tiêu chuẩn đường kính bánh xe cho tải trọng trục ~3.5 tấn/bánh; kiểm tra lại ở Khối 2 |
| **P-13** | Suất cản lăn riêng tương đương | $w_0$ | 0.015 | - | **[C]** | Bánh thép trên ray thép có ổ lăn đỡ trục; kiểm tra lại ở Khối 2 |
| **P-14** | Hệ số bám dính bánh thép trên ray | $\varphi$ | 0.20 | - | **[C]** | Hệ số ma sát bám ray thép khô kiểm tra chống trượt; kiểm tra lại ở Khối 2 |
| **P-15** | Hiệu suất truyền động cơ khí | $\eta$ | 0.90 | - | **[C]** | Hộp giảm tốc bánh răng trụ 3 cấp kèm khớp nối và ổ lăn; kiểm tra lại ở Khối 2 |
| **P-16** | Tỷ số truyền sơ bộ hộp số | $i$ | 150 | - | **[C]** | Ước tính từ tốc độ động cơ 1440 vg/ph và bánh xe 9.17 vg/ph; kiểm tra lại ở Khối 2 |
| **P-17** | Chế độ làm việc định mức | Chế độ | S3 - 40% | - | **[C]** | Chế độ ngắn hạn lặp lại đặc trưng của xe con cầu trục; kiểm tra lại ở Khối 2 |
| **P-18** | Gia tốc trọng trường | $g$ | 9.81 | m/s$^2$ | **[C]** | Hằng số trọng trường quy chuẩn tại Việt Nam; kiểm tra lại ở Khối 2 |
| **P-19** | Nguồn điện lưới cấp vào | $U_{\text{lưới}}$ | 380 ± 10% / 50 | V / Hz | **[C]** | Lưới điện hạ thế công nghiệp tiêu chuẩn; kiểm tra lại ở Khối 2 |
| **P-20** | Lực cản chuyển động tĩnh đầy tải | $F_{c.\text{đầy}}$ | 2,096 | N | **[B]** | $F_{c.\text{đầy}} = M_\Sigma \cdot g \cdot w_0 = 14,244 \cdot 9.81 \cdot 0.015 \approx 2,096\text{ N}$ |

---

## 3. ĐẶC TẢ YÊU CẦU KỸ THUẬT HỆ THỐNG (SRS BASELINE A — 8 MÃ CHỐT)

Toàn bộ 8 yêu cầu kỹ thuật trong `SRS Baseline A` được cấu trúc chặt chẽ theo công thức câu lệnh chuẩn của **ISO/IEC/IEEE 29148:2018**:
$$\underbrace{[\text{Điều kiện / Trạng thái}]}_{\text{Condition}} + \underbrace{[\text{Chủ thể}]}_{\text{Subject}} + \mathbf{\text{phải (shall)}} + \underbrace{[\text{Hành động}]}_{\text{Action}} + \underbrace{[\text{Ngưỡng định lượng } \pm \text{ Dung sai}]}_{\text{Target \& Tolerance}}$$

*Quy ước:* Giới hạn một phía ($\le$, $\ge$) chỉ ghi cận xác định, không tự gán dải dưới/dải trên. Cột kiểm chứng (KC) chỉ ghi phương pháp (A / S / I), nội dung chi tiết kịch bản và tín hiệu đo được chuyển giao toàn bộ sang DVP.

| Mã yêu cầu | Truy vết PRD | Tên yêu cầu kỹ thuật | Câu yêu cầu kỹ thuật (*Shall Statement* chuẩn ISO/IEC/IEEE 29148) | Ngưỡng chỉ tiêu định lượng | Phương pháp KC |
| :---: | :---: | :--- | :--- | :--- | :---: |
| **SRS-FUNC-01** | `PRD-FUNC-01` | **Vận hành hai chiều trên 4 góc phần tư và phản hồi Encoder** | Khi nhận lệnh điều khiển di chuyển ngang theo hai chiều Tiến và Lùi, **Hệ truyền động điện xe con phải (shall)** làm việc ổn định trên cả 4 góc phần tư của mặt phẳng Tốc độ – Mô-men $(\omega, M)$ và sử dụng tín hiệu từ 01 bộ mã hóa xung (Encoder) gắn đồng trục động cơ để phản hồi tốc độ khép kín mạch vòng điều khiển (0 cảm biến trên cáp treo). | Bao phủ đủ 4 góc phần tư I, II, III, IV; phản hồi tốc độ vòng kín từ 01 Encoder. | **S** |
| **SRS-FUNC-02** | `PRD-FUNC-04` | **Khóa chéo cấm đảo chiều khi $v \ne 0$ và đồng bộ đóng/mở phanh cơ điện từ** | Trong mọi chu trình chuyển động, **Khối điều khiển logic của hệ truyền động phải (shall)** thực hiện khóa chéo chỉ cho phép đảo chiều khi vận tốc xe con đã dừng hẳn về $v = 0\text{ m/s}$, đồng thời phối hợp điều khiển phanh cơ điện từ sao cho chỉ mở phanh khi động cơ đã sinh đủ mô-men giữ và tự động đóng phanh khi tốc độ giảm về dừng hẳn với độ trôi dừng xe sau khi đóng phanh $\Delta s \le \pm 10\text{ mm}$ (danh định không trôi $\Delta s = 0\text{ mm}$). | Khóa chéo cấm đảo chiều khi $v \ne 0$; mở phanh khi đủ mô-men giữ; độ trôi dừng xe $\Delta s \le \pm 10\text{ mm}$. | **S** |
| **SRS-FUNC-03** | `PRD-FUNC-02` | **Quy hoạch quỹ đạo tốc độ đặt liên tục theo đường cong S-Curve 7 đoạn** | Khi nhận lệnh thay đổi tốc độ mục tiêu, **Bộ tạo quỹ đạo của hệ truyền động phải (shall)** biến đổi lượng đặt tốc độ bậc thang thành quỹ đạo tốc độ tham chiếu liên tục theo quy luật đường cong chữ S 7 đoạn với biên dạng gia tốc đặt khống chế $\lvert a^*(t) \rvert \le 0.5\text{ m/s}^2$ và đạo hàm gia tốc đặt khống chế $\lvert \rho^*(t) \rvert \le 2.0\text{ m/s}^3$ (không có xung giật vô hạn). | Quỹ đạo đặt S-curve 7 pha liên tục; gia tốc đặt $\lvert a^*(t) \rvert \le 0.5\text{ m/s}^2$; độ giật đặt $\lvert \rho^*(t) \rvert \le 2.0\text{ m/s}^3$. | **A / S** |
| **SRS-FUNC-04** | `PRD-FUNC-03` | **Tiêu tán năng lượng hãm tái sinh qua điện trở xả hãm $R_h$ bảo vệ biến tần** | Trong các pha giảm tốc hãm tái sinh (Góc phần tư II và IV), **Hệ truyền động điện xe con phải (shall)** kích hoạt mạch van hãm (Braking Chopper) và điện trở xả hãm $R_h$ để tiêu tán an toàn năng lượng hãm cơ học trả về mà không gây lỗi quá áp khâu DC-link làm ngắt biến tần ở cả trạng thái đầy tải và không tải. | Năng lượng hãm tiêu tán an toàn qua $R_h$; biến tần không báo lỗi ngắt mạch quá áp DC-link. | **A / S** |
| **SRS-PERM-01** | `PRD-PERM-01` | **Đáp ứng lực kéo, thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ và chống trượt ray** | Khi di chuyển xe con trên ray ở cả hai trạng thái đầy tải $14,244\text{ kg}$ (P-04) [B] và không tải $2,022\text{ kg}$ (P-05) [B], **Hệ truyền động điện xe con phải (shall)** sinh đủ lực kéo tiếp tuyến và mô-men cơ học để thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ (P-20) [B] (với $w_0 = 0.015$ (P-13) [C], hiệu suất cơ khí $\eta = 0.90$ (P-15) [C]) và đảm bảo hệ số an toàn chống trượt bánh dẫn trên ray đạt $k_{\text{bám}} \ge 1.20$ với hệ số bám $\varphi = 0.20$ (P-14) [C]. | Thắng lực cản tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$; hệ số an toàn bám $k_{\text{bám}} \ge 1.20$ không trượt bánh xe. | **A / S** |
| **SRS-PERM-02** | `PRD-PERM-02` | **Đạt vận tốc di chuyển ngang định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$** | Khi nhận lệnh chạy định mức ở cả hai chiều Tiến và Lùi trên toàn dải tải trọng ($2,022\text{ kg} \div 14,244\text{ kg}$), **Hệ truyền động điện xe con phải (shall)** đưa xe con đạt vận tốc dài xác lập định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ (dải $[0.114;\ 0.126]\text{ m/s}$ hay $[6.84;\ 7.56]\text{ m/phút}$, tương ứng tốc độ góc bánh xe $\omega_{\text{bx}} = 0.96\text{ rad/s} \pm 5.0\%$). | Vận tốc dài xác lập định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ ($[0.114;\ 0.126]\text{ m/s}$) theo cả hai chiều di chuyển. | **S** |
| **SRS-PERM-03** | `PRD-PERM-03` | **Khống chế gia tốc thực tế $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và độ giật thực tế $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$** | Trong mọi giai đoạn khởi động, tăng tốc, giảm tốc và dừng làm việc bình thường với tải treo ở chiều cao nâng lớn nhất $h = 12\text{ m}$ (P-06) [A], **Hệ truyền động điện xe con phải (shall)** khống chế đồng thời độ lớn gia tốc ngang thực tế $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ (P-10) [A] và độ lớn độ giật ngang thực tế $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$ (P-11) [A]. | Gia tốc thực tế $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$; độ giật thực tế $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$ với cáp treo dài $h = 12\text{ m}$. | **A / S** |
| **SRS-PERM-04** | `PRD-PERM-04` | **Định cỡ công suất phát nhiệt chế độ $S3 - 40\%$ đạt $k_{dt} \ge 1.20$ ở lưới danh định $380\text{V}$** | Khi làm việc ở chế độ ngắn hạn lặp lại **S3 - 40%** (P-17) [C] (chu kỳ chuẩn $10\text{ phút}$, gồm $4.0\text{ phút}$ làm việc và $6.0\text{ phút}$ nghỉ) dưới nguồn điện lưới 3 pha danh định $380\text{ V}$, tần số $50\text{ Hz}$ (P-19) [C] (quá tải mô-men kiểm ở lưới $-10\%$ theo `SRS-D02`), **Các phần tử công suất của hệ truyền động (Động cơ KĐB 3 pha và Biến tần) phải (shall)** được định cỡ thỏa mãn hệ số dự trữ công suất phát nhiệt đẳng trị nằm trong dải $k_{dt} = \frac{P_{\text{đm}}}{P_{\text{đt}}} \ge 1.20$ mà không bị quá nhiệt cuộn dây (SRS A.1, CR-01). | Chế độ $S3 - 40\%$; hệ số dự trữ nhiệt $k_{dt} \ge 1.20$ ở lưới danh định $380\text{V} / 50\text{Hz}$. | **A / I** |

> **Phân biệt phạm vi:** `SRS-FUNC-03` khống chế **lượng đặt đầu vào** của bộ tạo quỹ đạo S-curve ($a^*, \rho^*$), còn `SRS-PERM-03` kiểm soát **đáp ứng động lực học thực tế** của xe con và tải treo cáp ($a, \rho$). Hai yêu cầu độc lập, không trùng lặp.

---

## 4. THÔNG SỐ CHUYỂN XUỐNG KHỐI THIẾT KẾ (DOWNSTREAM DESIGN ALLOCATION)

Nhằm tuân thủ nguyên tắc *WHAT, not HOW* của kỹ thuật hệ thống và tránh bẫy quá chi tiết hóa (*Over-specification*) làm phức tạp việc nghiệm thu cấp hệ thống, các thông số kỹ thuật phụ thuộc vào linh kiện cụ thể hoặc tham số thuật toán điều khiển đã được loại bỏ khỏi Baseline A và chuyển xuống các khối thiết kế chi tiết:

| STT | Thông số đã bỏ khỏi SRS | Khối tiếp nhận | Lý do chuyển giao (1 câu) |
| :---: | :--- | :---: | :--- |
| 1 | **Độ quá điều chỉnh tốc độ $M_p \le 10.0\%$** | **Khối 3** *(Điều khiển)* | Là chỉ tiêu chất lượng quá độ của mạch vòng tốc độ kín, chuyển thành mục tiêu tinh chỉnh bộ điều khiển PI (chuẩn tối ưu đối xứng) trên Simulink ở Khối 3. |
| 2 | **Sai lệch tốc độ xác lập tĩnh $e_{xl} \le 5.0\%$** | **Khối 3** *(Điều khiển)* | Đã được bao hàm trong dải dung sai vận tốc xác lập $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ của `SRS-PERM-02`, và được triệt tiêu hoàn toàn nhờ khâu tích phân của bộ điều khiển PI ở Khối 3. |
| 3 | **Điện áp DC-link $U_{\text{dc}} \le 780\text{ V}$ & Chopper $700\text{ V}$** | **Khối 2 & Khối 3** | Ngưỡng điện áp cụ thể phụ thuộc vào catalogue dòng biến tần thực tế được chọn ở Khối 2 và sơ đồ mạch hãm ở Khối 3, SRS chỉ cần yêu cầu chức năng xả hãm không ngắt lỗi quá áp. Giá trị 700 / 780 / 800 V là tham số mô hình Simulink, không gán dung sai (CR-17). |
| 4 | **Thời gian đáp ứng mô-men $\Delta t_{\text{torque}} \le 10\text{ ms}$** | **Khối 3** *(Điều khiển)* | Là tham số động học vi mô của mạch vòng dòng điện trong cấu trúc RFOC, được kiểm chứng khi tổng hợp mạch vòng dòng điện (chuẩn tối ưu module) ở Khối 3. |
| 5 | **Mô-men giữ $M_{\text{hold}}$ & Ngưỡng $|v| \le 0.002 / 0.005\text{ m/s}$** | **Khối 3** *(Điều khiển)* | Là các tham số cài đặt của thuật toán máy trạng thái hữu hạn (FSM) điều khiển logic liên động phanh cơ và khóa chéo ở Khối 3, SRS chỉ cần giữ chỉ tiêu độ trôi dừng $\Delta s \le \pm 10\text{ mm}$. |
| 6 | **Lực kéo cực đại tăng tốc $F_{\max} = 9.22\text{ kN}$** | **Khối 2** *(Chọn động cơ)* | Là giá trị lực kéo tính toán phát sinh trong pha quá độ tăng tốc, được tính toán và kiểm tra trong phần chọn động cơ ở Khối 2; điều kiện chống trượt ở SRS chỉ cần bảo đảm hệ số an toàn bám $k_{\text{bám}} \ge 1.20$. Là giá trị tính toán, kiểm bằng lực kéo động cơ tạo được ≥ $F_{\max}$; không gán dải nghiệm thu (CR-16). |
| 7 | **Bội số mô-men cực đại $\lambda_{\max} \ge 2.0$** | **Khối 2** *(Chọn động cơ)* | Là thông số cơ điện sẵn có từ nhà sản xuất, được kiểm tra đối chiếu trực tiếp khi tra cứu bảng thông số catalogue động cơ ở Khối 2. |
| 8 | **Cấp tốc độ bò (Creep Speed $25\% \div 30\% v_{\max}$)** | **Khối 3** *(Điều khiển)* | Là tính năng công nghệ phục vụ căn chỉnh vị trí tải, được hiện thực hóa bằng việc thay đổi lượng đặt vận tốc trên biến tần ở Khối 3 mà không cần ép cứng thành một mã SRS riêng biệt. |

---

## 5. CHECKLIST RÚT GỌN THEO TIÊU CHUẨN ISO/IEC/IEEE 29148

| Mã yêu cầu | Đúng 1 ý nghĩa (Singular) | Đo được (Measurable) | Kiểm chứng được (Verifiable) | Không mâu thuẫn (Consistent) | Khả thi kỹ thuật (Feasible) | Đánh giá chung |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **SRS-FUNC-01** | ✔ | ✔ | ✔ | ✔ | ✔ | **ĐẠT** |
| **SRS-FUNC-02** | ✔ | ✔ | ✔ | ✔ | ✔ | **ĐẠT** |
| **SRS-FUNC-03** | ✔ | ✔ | ✔ | ✔ | ✔ | **ĐẠT** |
| **SRS-FUNC-04** | ✔ | ✔ | ✔ | ✔ | ✔ | **ĐẠT** |
| **SRS-PERM-01** | ✔ | ✔ | ✔ | ✔ | ✔ | **ĐẠT** |
| **SRS-PERM-02** | ✔ | ✔ | ✔ | ✔ | ✔ | **ĐẠT** |
| **SRS-PERM-03** | ✔ | ✔ | ✔ | ✔ | ✔ | **ĐẠT** |
| **SRS-PERM-04** | ✔ | ✔ | ✔ | ✔ | ✔ | **ĐẠT** |

---

## 6. TÀI LIỆU THAM KHẢO

1. Bộ môn Tự động hóa Xí nghiệp Công nghiệp, *Đề bài tập lớn môn Thiết kế hệ truyền động điện (Học kỳ 2023.1, Đề 0~9, tham số $x = 2$)*, Trường ĐH Bách khoa Hà Nội, 2023.
2. TS. Nguyễn Duy Đỉnh, *Bài giảng Thiết kế hệ truyền động điện (Bài 4: Hệ truyền động cơ cấu di chuyển xe con cầu trục)*, Trường ĐH Bách khoa Hà Nội, 2021.
3. PGS.TS. Bùi Quốc Khánh, TS. Nguyễn Phùng Quang, *Điều chỉnh tự động truyền động điện*, NXB Khoa học và Kỹ thuật, Hà Nội.
4. Bộ Khoa học và Công nghệ, *TCVN 4244:2005: Thiết bị nâng - Thiết kế, chế tạo và kiểm tra kỹ thuật*, Hà Nội, 2005.
5. Tiêu chuẩn quốc tế IEC 60034-1, *Rotating electrical machines - Part 1: Rating and performance* (Quy chuẩn chế độ làm việc ngắn hạn lặp lại S3).
6. Tiêu chuẩn quốc tế ISO/IEC/IEEE 29148:2018, *Systems and software engineering - Life cycle processes - Requirements engineering*.
