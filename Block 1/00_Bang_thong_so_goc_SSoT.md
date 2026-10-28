# BẢNG THÔNG SỐ GỐC VÀ RÀ SOÁT SỐ LIỆU ĐẶC TẢ YÊU CẦU (SRS)

**Học phần:** Thiết kế hệ thống truyền động điện (ĐH Bách khoa Hà Nội)  
**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Đề tài:** Thiết kế hệ truyền động cơ cấu di chuyển xe con cầu trục dầm đôi (Động cơ KĐB rotor lồng sóc + Biến tần, điều khiển FOC, quỹ đạo S-curve)  
**Nhóm sinh viên thực hiện:** Nhóm 8.5-EMG (Đề bài ứng với STT 22: Nghiêm Trọng Đông, tham số $x = 2$)  
**Công cụ kiểm chứng duy nhất của nhóm:** Tính tay / bảng tính Excel, mô phỏng MATLAB/Simulink, tra cứu catalogue nhà sản xuất.  

---

## PHẦN 1: BẢNG THÔNG SỐ GỐC (SSoT)

> **Quy ước phân loại nguồn số liệu:**
> - **[A] Đề bài:** Số liệu do giảng viên giao trực tiếp trong đề bài tập dài.
> - **[B] Tính toán:** Số liệu tính ra từ các thông số [A] bằng công thức cơ học / truyền động điện rõ ràng.
> - **[C] Giả định của nhóm:** Số liệu nhóm tự chọn (lấy số tròn, có 1 câu lý do kỹ thuật và ghi rõ mốc kiểm tra lại ở các khối sau).

| Mã | Tên thông số | Ký hiệu | Giá trị | Đơn vị | Loại | Công thức hoặc Lý do chọn | Nguồn trích dẫn |
| :---: | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| **P-01** | Tải trọng nâng định mức | $Q$ | 12,222 | kg | **[A]** | Đề bài cho dạng $1x,xxx\text{ kg}$ với $x = 2$. | Đề bài tập dài TKTĐĐ (Đề 0~9) |
| **P-02** | Khối lượng cơ cấu nâng hạ | $m_{nh}$ | 222 | kg | **[A]** | Đề bài cho dạng $2xx\text{ kg}$ với $x = 2$. | Đề bài tập dài TKTĐĐ (Đề 0~9) |
| **P-03** | Khối lượng bản thân xe con | $m_{xc}$ | 1,800 | kg | **[C]** | Chọn số tròn ước lượng bằng khoảng $15\%$ tải định mức $Q$ theo dải xe con dầm đôi $12 \div 15\text{ tấn}$; kiểm tra lại ở Khối 2. | Tham khảo phân khúc xe con dầm đôi 15t / TCVN 4244 |
| **P-04** | Tổng khối lượng đầy tải | $M_{\Sigma}$ | 14,244 | kg | **[B]** | $M_{\Sigma} = Q + m_{nh} + m_{xc} = 12,222 + 222 + 1,800$ | Tính từ P-01, P-02, P-03 |
| **P-05** | Tổng khối lượng không tải | $m_{\text{tĩnh}}$ | 2,022 | kg | **[B]** | $m_{\text{tĩnh}} = m_{xc} + m_{nh} = 1,800 + 222$ | Tính từ P-02, P-03 |
| **P-06** | Chiều cao nâng (chiều dài cáp lớn nhất) | $h$ | 12 | m | **[A]** | Đề bài cho dạng $1x\text{ m}$ với $x = 2$. | Đề bài tập dài TKTĐĐ (Đề 0~9) |
| **P-07** | Tần số góc dao động riêng con lắc cáp | $\omega_p$ | 0.904 | rad/s | **[B]** | $\omega_p = \sqrt{g / h} = \sqrt{9.81 / 12} \approx 0.904$ | Mô hình con lắc đơn (P-06, P-18) |
| **P-08** | Chu kỳ dao động riêng con lắc cáp | $T_p$ | 6.95 | s | **[B]** | $T_p = \frac{2\pi}{\omega_p} = \frac{2\pi}{0.904} \approx 6.95$ | Tính từ P-07 |
| **P-09** | Vận tốc di chuyển ngang lớn nhất | $v_{\max}$ | 0.12 | m/s | **[A]** | Đề bài cho dạng $0.1x\text{ m/s}$ với $x = 2$ ($7.2\text{ m/phút}$). | Đề bài tập dài TKTĐĐ (Đề 0~9) |
| **P-10** | Gia tốc cực đại cho phép | $a_{\max}$ | 0.5 | m/s$^2$ | **[A]** | Đề bài cho giới hạn gia tốc chuyển động $a \le 0.5\text{ m/s}^2$. | Đề bài tập dài TKTĐĐ (Đề 0~9) |
| **P-11** | Độ giật cực đại cho phép | $\rho_{\max}$ | 2.0 | m/s$^3$ | **[A]** | Đề bài cho giới hạn đạo hàm gia tốc $\rho \le 2.0\text{ m/s}^3$. | Đề bài tập dài TKTĐĐ (Đề 0~9) |
| **P-12** | Đường kính bánh xe di chuyển | $D_{bx}$ | 0.25 | m | **[C]** | Chọn đường kính tiêu chuẩn $250\text{ mm}$ cho tải trọng trục khoảng $3.5\text{ tấn/bánh}$; kiểm tra lại ở Khối 2. | TCVN 4244 / Giáo trình Thiết bị nâng chuyển |
| **P-13** | Suất cản lăn riêng tương đương | $w_0$ | 0.015 | - | **[C]** | Bánh thép lăn trên ray thép có ổ lăn đỡ trục; tính kiểm bằng công thức cản di chuyển ở Phần 1b cho dải $0.013 \div 0.018$, chọn 0.015. | TCVN 4244 §2.4.7.2.2 (thành phần lực cản di chuyển) [R1]; phép tính kiểm Phần 1b |
| **P-14** | Hệ số bám dính bánh thép trên ray | $\varphi$ | 0.20 | - | **[C]** | Hệ số ma sát bám ray thép khô dùng kiểm tra điều kiện chống trượt bánh xe khi tăng/giảm tốc; kiểm tra lại ở Khối 2. | Bài giảng TKTĐĐ (TS. Nguyễn Duy Đỉnh, Bài 4, tr. 43) |
| **P-15** | Hiệu suất truyền động cơ khí | $\eta$ | 0.90 | - | **[C]** | Hiệu suất tổ hợp hộp giảm tốc bánh răng trụ 3 cấp kèm khớp nối và ổ lăn ngâm dầu; kiểm tra lại ở Khối 2. | Giáo trình Cơ sở thiết kế máy / Bài giảng TKTĐĐ |
| **P-16** | Tỷ số truyền sơ bộ hộp giảm tốc | $i$ | 150 | - | **[C]** | Ước tính từ tốc độ động cơ 4 cực ($1440\text{ vg/ph}$) và tốc độ bánh xe ($9.17\text{ vg/ph}$); kiểm tra lại ở Khối 2. | Tính sơ bộ từ P-09, P-12 |
| **P-17** | Chế độ làm việc định mức | Chế độ | S3 - 40% | - | **[C]** | Chế độ ngắn hạn lặp lại đặc trưng của cơ cấu xe con cầu trục theo tiêu chuẩn; kiểm tra lại ở Khối 2. | TCVN 4244:2005 / IEC 60034-1 |
| **P-18** | Gia tốc trọng trường | $g$ | 9.81 | m/s$^2$ | **[C]** | Hằng số trọng trường quy chuẩn tại Việt Nam; kiểm tra lại ở Khối 2. | Sổ tay Vật lý / TCVN |
| **P-19** | Nguồn điện lưới cấp vào | $U_{\text{lưới}}$ | 380 ± 10% / 50 | V / Hz | **[C]** | Nguồn hạ thế 3 pha công nghiệp tiêu chuẩn tại các nhà máy; kiểm tra lại ở Khối 2. | Tiêu chuẩn điện lực Việt Nam |
| **P-20** | Lực cản chuyển động tĩnh đầy tải | $F_{c.\text{đầy}}$ | 2,096 | N | **[B]** | $F_{c.\text{đầy}} = M_{\Sigma} \cdot g \cdot w_0 = 14,244 \cdot 9.81 \cdot 0.015 \approx 2,096\text{ N}$ | Tính từ P-04, P-13, P-18 |

---

## PHẦN 1b: CĂN CỨ CHO HAI GIẢ ĐỊNH ẢNH HƯỞNG LỚN (bổ sung 28/10/2026)

### a) Tính kiểm suất cản lăn $w_0$ (P-13)

$w_0$ là nguồn duy nhất của phụ tải tĩnh $F_c = M g w_0$ (P-20), từ đó ra mô-men tĩnh, công suất tĩnh, phần tính nhiệt $k_{dt}$ và năng lượng hãm — nên phải giữ. TCVN 4244:2005 §2.4.7.2.2 `[R1]` (tr.99) yêu cầu kể đến biến dạng mặt lăn và ma sát gờ bánh với ray; công thức cản di chuyển thông dụng của cơ cấu di chuyển máy trục:

$$w_0 = k_r \cdot \frac{\mu d + 2f}{D_{bx}}$$

| Đại lượng | Ký hiệu | Giá trị giả định `[C]` | Ghi chú |
| :--- | :---: | :---: | :--- |
| Hệ số ma sát ổ lăn quy về ngõng trục | $\mu$ | 0.015 | Ổ lăn |
| Đường kính ngõng trục bánh xe | $d$ | 0.08 m | ≈ $0.3 D_{bx}$ |
| Cánh tay đòn ma sát lăn bánh thép/ray thép | $f$ | 0.0005 m | 0.3 ÷ 0.6 mm |
| Hệ số kể ma sát gờ bánh và moay-ơ | $k_r$ | 1.5 ÷ 2.0 | Xe con trên ray |
| Đường kính bánh xe | $D_{bx}$ | 0.25 m | P-12 |

Kết quả: $\frac{0.015 \cdot 0.08 + 2 \cdot 0.0005}{0.25} = 0.0088$; nhân $k_r = 1.5 \div 2.0$ được $w_0 \approx 0.013 \div 0.018$. Giá trị chọn **0.015** nằm giữa dải. Các hệ số trong bảng là giả định nhóm, cần đối chiếu với giáo trình máy trục khi có tài liệu.

### b) Chu trình làm việc giả định cho chế độ S3-40% (P-17)

Chu kỳ chuẩn $T_{ck} = 600\text{ s}$, thời gian đóng điện $0.4 \cdot 600 = 240\text{ s}$: **1 hành trình đầy tải (Tiến) + 1 hành trình không tải (Lùi), mỗi hành trình 120 s**, nghỉ 360 s. Chiều dài hành trình suy ra $L_{ht} \approx 14.3\text{ m}$ (Excel v1.5, sheet `Tính chọn`). Đây là giả định `[C]` quyết định toàn bộ phép tính $M_{\text{đt}}$, $k_{dt}$; đồ thị phụ tải ở `Block 2/01_SAD_...` §5.4.

---

## PHẦN 2: RÀ SOÁT SRS CŨ (MỤC 2 VÀ MỤC 3)

| STT | Con số trong SRS cũ | Vị trí trong SRS cũ | Quyết định | Lý do (1 câu) |
| :---: | :--- | :--- | :---: | :--- |
| 1 | **$380\text{V AC} \pm 10\%, 50\text{Hz}$** | Mục 2.1 (Sơ đồ biên) & Mục 2.2 (Nhiễu N3) | **GIỮ** (Mã P-19) | Đây là điện áp lưới điện công nghiệp 3 pha danh định tiêu chuẩn tại Việt Nam. |
| 2 | **$342\text{V} \div 418\text{V AC}$** | Mục 2.1 (Sơ đồ biên) & Mục 2.2 (Nhiễu N3) | **GIỮ** (Tính từ P-19) | Dải dao động điện áp tính trực tiếp từ $380\text{V} \pm 10\%$. |
| 3 | **$Q = 12,222\text{ kg}$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-01) | **GIỮ** (Mã P-01) | Tải trọng nâng định mức lấy theo đúng số liệu đề bài giao với $x = 2$. |
| 4 | **$m_{nh} = 222\text{ kg}$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-01) | **GIỮ** (Mã P-02) | Khối lượng cụm nâng hạ lấy theo đúng số liệu đề bài giao với $x = 2$. |
| 5 | **$h = l \le 12\text{ m}$** | Mục 2.1 (Sơ đồ biên) & Mục 2.2 (Nhiễu N2) | **GIỮ** (Mã P-06) | Chiều cao nâng lớn nhất lấy theo đúng số liệu đề bài giao với $x = 2$. |
| 6 | **$\omega_p \approx 0.904\text{ rad/s}$** | Mục 2.1 (Sơ đồ biên) & Mục 2.2 (Nhiễu N2) | **GIỮ** (Mã P-07) | Tần số góc dao động con lắc cáp tính từ chiều cao nâng $h = 12\text{ m}$ theo công thức $\sqrt{g/h}$. |
| 7 | **$T_p \approx 6.95\text{ s}$** | Mục 2.2 (Nhiễu N2) & Mục 3.3 (SRS-PERM-06) | **GIỮ** (Mã P-08) | Chu kỳ dao động con lắc cáp tính trực tiếp từ tần số góc $\omega_p \approx 0.904\text{ rad/s}$. |
| 8 | **$\mu = 0.20$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-01) | **SỬA** (Mã P-13: $w_0 = 0.015$; P-14: $\varphi = 0.20$) | Bánh xe thép trên ray thép chỉ có hệ số cản lăn khoảng $0.01 \div 0.03$, không được nhầm với hệ số bám ray $\varphi = 0.20$. |
| 9 | **$F_{c.\text{đầy}} \approx 27,947\text{ N}$** | Mục 3.3 (SRS-PERM-01) | **SỬA** (Mã P-20: $F_{c.\text{đầy}} \approx 2,096\text{ N}$) | Con số cũ tính sai do dùng nhầm hệ số cản $\mu = 0.20$, sửa lại theo suất cản lăn $w_0 = 0.015$. |
| 10 | **$F_{c.\text{không}} \approx 3,967\text{ N}$** | Mục 3.3 (SRS-PERM-01) | **SỬA** (Thành $F_{c.\text{không}} \approx 298\text{ N}$) | Con số cũ tính sai do dùng $\mu = 0.20$, sửa lại theo suất cản lăn đúng $w_0 = 0.015$. |
| 11 | **$CD = 40\%$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-07) | **GIỮ** (Mã P-17) | Hệ số tiếp điện tương đối tiêu chuẩn cho chế độ làm việc ngắn hạn lặp lại S3 của xe con cầu trục. |
| 12 | **$k_{dt} \in [1.20;\ 1.50]$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-07) | **SỬA** (Giữ điều kiện $k_{dt} \ge 1.2$) | Bỏ việc ép cứng cận trên 1.50 để phù hợp với dải công suất động cơ tra được trên catalogue ở Khối 2. |
| 13 | **$\lambda \ge 2.0$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-07) | **SỬA** (Chuyển thành kiểm tra catalogue ở Khối 2) | Bội số quá tải mô-men phụ thuộc loại động cơ thực tế tra được trong catalogue, không ấn định cứng trong SRS. |
| 14 | **$780\text{ V}$ ($U_{\text{dc}} < 780\text{ V}$)** | Mục 2.1 (Sơ đồ biên), Mục 2.2 (CF4, CTQ-07) & Mục 3.2 (SRS-FUNC-06) | **XÓA** | Tuân thủ Luật 6, xóa bỏ chi tiết điện áp DC-link 780 V và chỉ giữ yêu cầu chức năng hãm tái sinh. |
| 15 | **$\eta = 0.96$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-01) | **SỬA** (Mã P-15: $\eta = 0.90$) | Hiệu suất cơ khí hộp giảm tốc bánh răng trụ 3 cấp kèm khớp nối và ổ trục trong giáo trình VN thường tính 0.90. |
| 16 | **$d = 0.25\text{ m}$ ($250\text{ mm}$)** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-01) | **GIỮ** (Mã P-12) | Đường kính bánh xe chọn theo dãy kích thước tiêu chuẩn cho tải trọng trục xe con. |
| 17 | **$m_{xc} = 1,800\text{ kg}$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-01) | **GIỮ** (Mã P-03) | Khối lượng xe con lấy số tròn ước lượng bằng 15% tải định mức theo catalogue pa lăng dầm đôi. |
| 18 | **$v_{\max} = 0.12\text{ m/s}$ ($7.2\text{ m/ph}$)** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-02) | **GIỮ** (Mã P-09) | Vận tốc di chuyển ngang lớn nhất lấy theo đúng số liệu đề bài giao với $x = 2$. |
| 19 | **$e_{xl} \le 5\%$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-03) | **SỬA** (Chuyển sang yêu cầu chất lượng điều khiển ở Khối 3) | Đây là chỉ tiêu tổng hợp của bộ điều khiển FOC vòng kín, sẽ kiểm chứng bằng mô phỏng Simulink. |
| 20 | **$M_p \le 10\%$** | Mục 2.1 (Sơ đồ biên) & Mục 3.3 (SRS-PERM-04) | **SỬA** (Chuyển sang yêu cầu chất lượng điều khiển ở Khối 3) | Đây là độ quá điều chỉnh tốc độ của mạch vòng điều khiển, sẽ kiểm chứng bằng mô phỏng Simulink. |
| 21 | **$v_{\text{creep}} \in [0.030;\ 0.036]\text{ m/s}$ ($25\% \div 30\% v_{\max}$)** | Mục 2.1 (Outputs) & Mục 3.2 (SRS-FUNC-04) | **SỬA** (Giữ yêu cầu chức năng chạy bò, kiểm tra lại ở Khối 3) | Tốc độ bò là tính năng công nghệ phục vụ căn chỉnh tải, không đưa dải số chi tiết vào bảng thông số gốc cơ khí. |
| 22 | **$|a(t)| \le 0.5\text{ m/s}^2$** | Mục 2.1 (Outputs) & Mục 3.3 (SRS-PERM-05) | **GIỮ** (Mã P-10) | Giới hạn gia tốc chuyển động lấy theo đúng số liệu đề bài giao. |
| 23 | **$|\rho(t)| \le 2.0\text{ m/s}^3$** | Mục 2.1 (Outputs) & Mục 3.3 (SRS-PERM-06) | **GIỮ** (Mã P-11) | Giới hạn độ giật chuyển động lấy theo đúng số liệu đề bài giao. |
| 24 | **$14,244\text{ kg}$** | Mục 2.2 (P-Diagram N1) & Mục 3.3 (SRS-PERM-01) | **GIỮ** (Mã P-04) | Tổng khối lượng đầy tải tính từ tải định mức, khối lượng cụm nâng và tự trọng xe con giả định. |
| 25 | **$2,022\text{ kg}$** | Mục 2.2 (P-Diagram N1) & Mục 3.3 (SRS-PERM-01) | **GIỮ** (Mã P-05) | Tổng khối lượng không tải tính từ tự trọng xe con giả định và cụm nâng hạ. |
| 26 | **$7.04\text{ lần}$** | Mục 2.2 (P-Diagram N1) | **GIỮ** (Tính từ P-04, P-05) | Tỷ số giữa tải đầy và không tải ($14,244 / 2,022 \approx 7.04$) thể hiện dải biến thiên quán tính hệ thống. |
| 27 | **$< 10\text{ ms}$** | Mục 3.2 (SRS-FUNC-01) | **XÓA** | Số liệu từ bài báo/catalogue biến tần cao cấp, nhóm không có thiết bị đo thực nghiệm để kiểm chứng. |
| 28 | **$4\text{ góc phần tư}$** | Mục 3.2 (SRS-FUNC-01) | **GIỮ** | Yêu cầu chức năng công nghệ bắt buộc đối với hệ truyền động đảo chiều có hãm tái sinh. |
| 29 | **$v(t) = 0\text{ m/s}$** | Mục 3.2 (SRS-FUNC-02) & Mục 3.2 (SRS-FUNC-07) | **GIỮ** | Điều kiện logic an toàn cấm đảo chiều khi cơ cấu chưa dừng hẳn và điều kiện đóng phanh cơ theo TCVN 4244. |
| 30 | **$7\text{ đoạn}$ (S-curve)** | Mục 3.2 (SRS-FUNC-03) | **GIỮ** | Quy luật tạo quỹ đạo tốc độ 7 đoạn để đảm bảo gia tốc biến thiên liên tục và triệt tiêu độ giật vô hạn. |
| 31 | **$D \ge 10:1$** | Mục 3.2 (SRS-FUNC-04) | **XÓA** (CR-18, 28/10/2026) | Không thuộc 8 yêu cầu SRS; chức năng điều chỉnh tốc độ đã thể hiện qua cấp tốc độ bò (`SRS-D12`). |
| 32 | **$01\text{ bộ mã hóa xung (Encoder)}$** | Mục 3.2 (SRS-FUNC-05) | **GIỮ** | Cấu hình cảm biến đo tốc độ trục động cơ để thực hiện điều khiển vector tựa từ thông FOC vòng kín. |
| 33 | **$0\text{ cảm biến trên cáp treo}$** | Mục 3.2 (SRS-FUNC-05) | **GIỮ** | Xác định rõ ranh giới thiết kế không sử dụng cảm biến góc lắc trên dây cáp ngoài hiện trường. |
| 34 | **$0\text{ rpm}$ & $M_{\text{hold}} \in [100\%; 150\%]\ M_{\text{đm}}$** | Mục 3.2 (SRS-FUNC-07) | **SỬA** (Giữ yêu cầu chức năng tạo đủ mô-men trước khi mở phanh) | Tránh ép số liệu chi tiết phần trăm khi chưa thiết kế thuật toán ở Khối 3. |
| 35 | **$\omega_{\text{bx}} = 0.96\text{ rad/s}$ ($9.17\text{ rpm}$)** | Mục 3.3 (SRS-PERM-02) | **GIỮ** (Tính từ P-09, P-12) | Tốc độ góc trục bánh xe tính trực tiếp từ vận tốc $v_{\max} = 0.12\text{ m/s}$ và đường kính bánh xe $D_{bx} = 0.25\text{ m}$. |
| 36 | **$v_{\text{xl}} \in [0.114;\ 0.126]\text{ m/s}$** | Mục 3.3 (SRS-PERM-03) | **SỬA** (Chuyển sang Khối 3) | Dải vận tốc tính theo $e_{xl} \le 5\%$, sẽ kiểm chứng trên Simulink ở Khối 3. |
| 37 | **$v_{\text{peak}} \le 0.132\text{ m/s}$** | Mục 3.3 (SRS-PERM-04) | **SỬA** (Chuyển sang Khối 3) | Vận tốc đỉnh tính theo $M_p \le 10\%$, sẽ kiểm chứng trên Simulink ở Khối 3. |
| 38 | **$\theta_0 \le 2.92^\circ$** | Mục 3.3 (SRS-PERM-05) | **GIỮ** (Tính từ P-10, P-18) | Góc lệch tĩnh cực đại của con lắc cáp treo do gia tốc lớn nhất gây ra ($\arctan(a_{\max}/g) \approx 2.92^\circ$). |

---

## PHẦN 3: DANH SÁCH CÂU HỎI NHÓM CẦN TỰ TRẢ LỜI

1. **Khối lượng bản thân xe con $m_{xc} = 1,800\text{ kg}$ ([C]) có phù hợp với thực tế không?**  
   Nhóm cần đối chiếu lại tự trọng này khi tra catalogue cụm pa lăng / xe con dầm đôi tải trọng $12 \div 15\text{ tấn}$ của các hãng chế tạo ở Khối 2 để đảm bảo không ước lượng quá nhẹ hoặc quá nặng.

2. **Tính lực cản di chuyển xe con nên dùng suất cản lăn tổng hợp $w_0$ hay công thức giải tích chi tiết?**  
   Nhóm cần làm rõ với bài giảng của Thầy Đỉnh xem nên dùng trực tiếp suất cản $w_0 = 0.015$ ($15\text{ kg/tấn}$) hay phải triển khai tính theo cánh tay đòn cản lăn $f$, đường kính ngỗng trục $d$ và hệ số ma sát ổ lăn $\mu_{ol}$.

3. **Với tỷ số truyền lớn ($i \approx 150 \div 180$), nhóm nên chọn cấu hình hộp số nào?**  
   Do vận tốc xe con rất thấp ($0.12\text{ m/s}$), nhóm cần quyết định chọn động cơ liền hộp giảm tốc (geared motor) hay động cơ rời kết hợp hộp giảm tốc bánh răng trụ 3 cấp tiêu chuẩn khi tra catalogue ở Khối 2.

4. **Phương pháp kiểm nghiệm phát nhiệt động cơ ở chế độ S3 - 40% thực hiện như thế nào khi catalogue chỉ ghi công suất S1?**  
   Nhóm cần vận dụng chính xác công thức quy đổi công suất tương đương giữa chế độ dài hạn S1 và chế độ ngắn hạn lặp lại S3 trong giáo trình Truyền động điện để chọn đúng dải công suất động cơ ở Khối 2.

5. **Thời gian tăng tốc của quỹ đạo S-curve có cần liên kết với chu kỳ lắc cáp treo $T_p \approx 6.95\text{ s}$ không?**  
   Nhóm cần xác định xem trong thuật toán tạo quỹ đạo S-curve ở Khối 3, thời gian tăng tốc có bắt buộc phải được điều chỉnh bằng hoặc là bội số của chu kỳ lắc tự nhiên để hỗ trợ triệt tiêu góc lắc dư khi dừng xe hay không.
