# BẢNG THÔNG SỐ GỐC VÀ RÀ SOÁT SỐ LIỆU ĐẶC TẢ YÊU CẦU (SRS)

**Học phần:** Thiết kế hệ thống truyền động điện (ĐH Bách khoa Hà Nội)  
**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Đề tài:** Thiết kế hệ truyền động cơ cấu di chuyển xe con cầu trục dầm đôi (Động cơ KĐB rotor lồng sóc + Biến tần, điều khiển FOC, quỹ đạo S-curve)  
**Nhóm sinh viên thực hiện:** Nhóm 8.5-EMG (Đề bài ứng với STT 22: Nghiêm Trọng Đông, tham số $x = 2$)  
**Công cụ kiểm chứng duy nhất của nhóm:** Tính tay / bảng tính Excel, mô phỏng MATLAB/Simulink, tra cứu catalogue nhà sản xuất.  

---

## PHẦN 1: BẢNG THÔNG SỐ GỐC (SSoT)

> **Quy ước phân loại nguồn số liệu & Viện dẫn chuẩn:**
> - **[A] Đề bài [1]:** Số liệu do giảng viên giao trực tiếp trong đề bài tập lớn ($x = 2$, STT 22, ĐHBK Hà Nội).
> - **[B] Tính toán & Tiêu chuẩn [2, 3]:** Số liệu tính ra từ các thông số [A] bằng công thức cơ học / truyền động điện rõ ràng theo TCVN 4244:2005 & IEC.
> - **[C] Giả định của nhóm & Khảo sát [4..9]:** Số liệu nhóm tự chọn căn cứ giáo trình ĐHBKHN [4], tiêu chuẩn ray A54 [5] và catalogue công nghiệp Demag [6], Sungdo [7], Shevchenko [8].

| Mã | Tên thông số | Ký hiệu | Giá trị danh định | Đơn vị | Dung sai quy chuẩn (Tolerance) | Dải giá trị nghiệm thu thực tế | Loại | Công thức hoặc Lý do chọn | Căn cứ Tiêu chuẩn & Nguồn trích dẫn |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- |
| **P-01** | Tải trọng nâng định mức | $Q$ | 12,222 | kg | $\pm 0\%$ (Danh định)<br>Thử tĩnh: $+25\%$<br>Thử động: $+10\%$ | Danh định: $12,222\text{ kg}$<br>Thử tĩnh: $15,277.5\text{ kg} \pm 1\%$<br>Thử động: $13,444.2\text{ kg} \pm 1\%$ | **[A] [1]** | Đề bài cho dạng $1x,xxx\text{ kg}$ với $x = 2$. Khối lượng nâng hạ danh định phục vụ kiểm tra kéo và quá tải. | Đề bài tập lớn TKTĐĐ [1]; TCVN 4244:2005 §1.3.3 & §1.3.4 [2] |
| **P-02** | Khối lượng cơ cấu nâng hạ | $m_{nh}$ | 222 | kg | $\pm 2.0\%$ | $[217.6;\ 226.4]\text{ kg}$ | **[A] [1]** | Đề bài cho dạng $2xx\text{ kg}$ với $x = 2$. Cụm móc cẩu, ròng rọc cáp luôn gắn liền cùng xe con. | Đề bài tập lớn TKTĐĐ [1]; TCVN 4244:2005 §1.3.4 [2] |
| **P-03** | Khối lượng bản thân xe con | $m_{xc}$ | 1,800 | kg | $\pm 5.0\%$ | $[1,710;\ 1,890]\text{ kg}$ | **[C] [7]** | Chọn số tròn ước lượng bằng khoảng $15\%$ tải định mức $Q$ theo dải xe con dầm đôi $12 \div 15\text{ tấn}$; kiểm tra lại ở Khối 2. | Tham khảo xe con dầm đôi 15t Sungdo/KG-Cranes [7]; TCVN 4244 [2] |
| **P-04** | Tổng khối lượng đầy tải | $M_{\Sigma}$ | 14,244 | kg | $\pm 4.5\%$ | $[13,600;\ 14,885]\text{ kg}$ | **[B] [1]** | $M_{\Sigma} = Q + m_{nh} + m_{xc} = 12,222 + 222 + 1,800$. Biến thiên tích lũy theo dung sai thành phần. | Tính từ P-01, P-02, P-03 [1, 2] |
| **P-05** | Tổng khối lượng không tải | $m_{\text{tĩnh}}$ | 2,022 | kg | $\pm 4.5\%$ | $[1,930;\ 2,113]\text{ kg}$ | **[B] [1]** | $m_{\text{tĩnh}} = m_{xc} + m_{nh} = 1,800 + 222$. Tải tĩnh xe con khi chạy về vị trí xuất phát. | Tính từ P-02, P-03 [1, 2] |
| **P-06** | Chiều cao nâng (chiều dài cáp lớn nhất) | $h$ | 12.0 | m | $\pm 0.1\text{ m}$ ($\pm 0.83\%$) | $[11.9;\ 12.1]\text{ m}$ | **[A] [1]** | Đề bài cho dạng $1x\text{ m}$ với $x = 2$. Quyết định chiều dài con lắc cáp treo đơn. | Đề bài tập lớn TKTĐĐ [1]; Mita & Kanai (1979) [9] |
| **P-07** | Tần số góc dao động riêng con lắc cáp | $\omega_p$ | 0.904 | rad/s | $\pm 0.005\text{ rad/s}$ | $[0.899;\ 0.909]\text{ rad/s}$ | **[B] [1]** | $\omega_p = \sqrt{g / h} = \sqrt{9.81 / 12} \approx 0.904\text{ rad/s}$. Xác định tần số cộng hưởng lắc tải. | Mô hình con lắc đơn (P-06, P-18) [9] |
| **P-08** | Chu kỳ dao động riêng con lắc cáp | $T_p$ | 6.95 | s | $\pm 0.04\text{ s}$ | $[6.91;\ 6.99]\text{ s}$ | **[B] [1]** | $T_p = \frac{2\pi}{\omega_p} = \frac{2\pi}{0.904} \approx 6.95\text{ s}$. Cơ sở phối hợp chu kỳ tăng tốc S-Curve. | Tính từ P-07 [9] |
| **P-09** | Vận tốc di chuyển ngang lớn nhất | $v_{\max}$ | 0.12 | m/s | $\mathbf{\pm 5.0\%}$ ($\pm 0.006\text{ m/s}$) | $\mathbf{[0.114;\ 0.126]\text{ m/s}}$ ($[6.84;\ 7.56]\text{ m/ph}$) | **[A] [1]** | Đề bài cho dạng $0.1x\text{ m/s}$ với $x = 2$ ($7.2\text{ m/phút}$). Tốc độ làm việc định mức duy nhất. | Đề bài [1]; IEC 61800-2 Class 2 [3]; TCVN 4244 §1.5.5 [2] |
| **P-10** | Gia tốc cực đại cho phép | $a_{\max}$ | 0.50 | m/s$^2$ | $\mathbf{+0.0\% / -10.0\%}$ (Chặn trên $\le 0.50$) | $\mathbf{[0.45;\ 0.50]\text{ m/s}^2}$ | **[A] [1]** | Đề bài cho giới hạn gia tốc chuyển động $a \le 0.5\text{ m/s}^2$. Chống trượt bánh dẫn và hạn chế góc lắc. | Đề bài [1]; TCVN 4244:2005 §1.5.5.1.2 [2] |
| **P-11** | Độ giật cực đại cho phép | $\rho_{\max}$ | 2.00 | m/s$^3$ | $\mathbf{+0.0\% / -10.0\%}$ (Chặn trên $\le 2.00$) | $\mathbf{[1.80;\ 2.00]\text{ m/s}^3}$ | **[A] [1]** | Đề bài cho giới hạn đạo hàm gia tốc $\rho \le 2.0\text{ m/s}^3$. Làm mềm lực quán tính, bảo vệ hộp giảm tốc. | Đề bài [1]; Tho et al. (2020) [9]; Mita & Kanai (1979) [9] |
| **P-12** | Đường kính bánh xe di chuyển | $D_{bx}$ | 0.25 | m | Chế tạo: $\pm 1.0\text{ mm}$<br>Lệch 2 bánh: $\le 0.25\text{ mm}$<br>Mòn tối đa: $-5.0\text{ mm}$ | Mới: $[249.0;\ 251.0]\text{ mm}$<br>Mòn cho phép: $D \ge 245.0\text{ mm}$ | **[C] [5]** | Chọn đường kính tiêu chuẩn $250\text{ mm}$ cho tải trọng trục khoảng $3.5\text{ tấn/bánh}$; kiểm tra lại ở Khối 2. | TCVN 4244:2005 §2.4.7.1 [2]; Tiêu chuẩn Ray DIN 536 / A54 [5] |
| **P-13** | Suất cản lăn riêng tương đương | $w_0$ | 0.015 | - | $\pm 20.0\%$ (Dải khảo sát thực tế) | $[0.012;\ 0.018]$ ($[1.2\% \div 1.8\%]$) | **[C] [2, 5]** | Bánh thép lăn trên ray thép có ổ lăn đỡ trục, lấy giá trị trung bình $15\text{ kg/tấn}$; kiểm tra lại ở Khối 2. | TCVN 4244:2005 §2.4.7.2.2 [2]; Tiêu chuẩn Ray A54 tr. 15 [5] |
| **P-14** | Hệ số bám dính bánh thép trên ray | $\varphi$ | 0.20 | - | Chặn dưới $k_{\text{bám}} \ge 1.20$ (Cận dưới $-0\%$) | $k_{\text{bám}} \ge 1.20$ (Danh định đạt $\approx 1.51$) | **[C] [4]** | Hệ số ma sát bám ray thép khô dùng kiểm tra điều kiện chống trượt bánh xe khi tăng/giảm tốc; kiểm tra lại ở Khối 2. | Bài giảng TKTĐĐ (Thầy Đỉnh, Bài 4, tr. 43) [4]; TCVN 4244 [2] |
| **P-15** | Hiệu suất truyền động cơ khí | $\eta$ | 0.96 | - | $+0.00 / -0.02$ (Chặn dưới $\eta \ge 0.94$) | $[0.94;\ 0.96]$ | **[C] [4]** | Hiệu suất tổ hợp hộp giảm tốc bánh răng trụ 3 cấp kèm khớp nối và ổ lăn ngâm dầu; kiểm tra lại ở Khối 2. | Giáo trình Cơ sở thiết kế máy / Bài giảng TKTĐĐ [4]; Demag DR [6] |
| **P-16** | Tỷ số truyền sơ bộ hộp giảm tốc | $i$ | 150 | - | $\pm 10.0\%$ | $[135;\ 165]$ | **[C] [4]** | Ước tính từ tốc độ động cơ 4 cực ($1440\text{ vg/ph}$) và tốc độ bánh xe ($9.17\text{ vg/ph}$); kiểm tra lại ở Khối 2. | Tính sơ bộ từ P-09, P-12 [4] |
| **P-17** | Chế độ làm việc định mức | Chế độ | S3 - 40% | - | Chu kỳ $T_{\text{ck}} = 10\text{ phút} \pm 30\text{ s}$<br>$CD = 40\% \pm 2.0\%$ | $T_{\text{ck}} \in [9.5;\ 10.5]\text{ phút}$<br>$t_{\text{lv}} = 4.0\text{ phút} \pm 12\text{ s}$<br>$t_n = 6.0\text{ phút} \pm 18\text{ s}$ | **[C] [3]** | Chế độ ngắn hạn lặp lại đặc trưng của cơ cấu xe con cầu trục theo tiêu chuẩn; kiểm tra lại ở Khối 2. | IEC 60034-1 [3]; TCVN 4244:2005 §2.4.5.1 [2] |
| **P-18** | Gia tốc trọng trường | $g$ | 9.81 | m/s$^2$ | $\pm 0.01\text{ m/s}^2$ | $[9.80;\ 9.82]\text{ m/s}^2$ | **[C] [1]** | Hằng số trọng trường quy chuẩn tại Việt Nam; kiểm tra lại ở Khối 2. | Sổ tay Vật lý / TCVN |
| **P-19** | Nguồn điện lưới cấp vào | $U_{\text{lưới}}$ | 380 / 50 | V / Hz | Điện áp: $\mathbf{\pm 10.0\%}$<br>Tần số: $\mathbf{\pm 2.0\%}$ | $U \in \mathbf{[342;\ 418]\text{V AC}}$<br>$f \in \mathbf{[49.0;\ 51.0]\text{ Hz}}$ | **[C] [3]** | Nguồn hạ thế 3 pha công nghiệp tiêu chuẩn tại các nhà máy; kiểm tra lại ở Khối 2. | QCVN QTĐ-5:2009; Thông tư 39/2015/TT-BCT; IEC 60034-1 [3] |
| **P-20** | Lực cản chuyển động tĩnh đầy tải | $F_{c.\text{đầy}}$ | 2,120 | N | Biến thiên theo $w_0$ ($\pm 20.0\%$) | $[1.70;\ 2.54]\text{ kN}$ ($P_{\text{tĩnh}} \in [0.21;\ 0.32]\text{ kW}$) | **[B] [1, 5]** | $F_{c.\text{đầy}} = M_{\Sigma} \cdot g \cdot w_0 = 14,244 \cdot 9.81 \cdot 0.015 \approx 2.12\text{ kN}$ ($P_{\text{tĩnh}} \approx 0.27\text{ kW}$). Lực kéo cực đại: $F_{\max} = 9.25\text{ kN} \pm 0.45\text{ kN}$ ($[8.80;\ 9.70]\text{ kN}$, $P_{\max} \approx 1.16\text{ kW}$), thỏa mãn $F_{\max} \le F_{\text{bám}} = 13.97\text{ kN}$ ($k_{\text{bám}} \approx 1.51 > 1.20$). | Tính từ P-04, P-13, P-18 [1, 5] |

> ### 📌 Chú dẫn Nguồn gốc & Viện dẫn Tài liệu Tham khảo (Citations for Client Review)
> - **Ký hiệu Phân loại Nội bộ Nhóm Kỹ thuật Hệ thống (`Internal SE Classification`):**
>   - **`[A]` — Nguồn Đề bài / Khách hàng:** Giá trị và chỉ tiêu kỹ thuật bất biến giao trực tiếp từ đề bài gốc $x = 2$ (STT 22, ĐHBK Hà Nội).
>   - **`[B]` — Nguồn Tiêu chuẩn Kỹ thuật:** Tiêu chuẩn Quốc gia (TCVN), Tiêu chuẩn Quốc tế (IEC, ISO/IEEE) và quy chuẩn ngành bắt buộc tuân thủ.
>   - **`[C]` — Nguồn Giả định Kỹ thuật & Khảo sát:** Dữ liệu tính toán giải tích nội bộ của Nhóm 8.5-EMG, bài giảng chuyên khảo và thông số kiểm chứng từ Catalogue nhà sản xuất (Demag, Sungdo, Ray A54).
> - **Danh mục Viện dẫn Tài liệu Tham khảo Chuẩn hóa Quốc tế (Chi tiết tại Mục Tài liệu Tham khảo và Slide Tham khảo):**
>   - **`[1]`**: Đề bài tập lớn môn Thiết kế Hệ TĐĐ Kỳ 2023.1 — Đề số 8: Xe con cầu trục ($x = 2$, STT 22), Bộ môn TĐĐ, ĐHBK Hà Nội [R3].
>   - **`[2]`**: TCVN 4244:2005 — Thiết bị nâng: Thiết kế, chế tạo và kiểm tra kỹ thuật, Bộ Khoa học và Công nghệ [R1].
>   - **`[3]`**: IEC 61800-2:1998, IEC 60034-1, ISO/IEC/IEEE 29148:2018 — Tiêu chuẩn biến tần, động cơ điện & đặc tả yêu cầu hệ thống [B].
>   - **`[4]`**: TS. Nguyễn Duy Đỉnh, Tài liệu Bài giảng Thiết kế Hệ Truyền động Điện (Bài 4, tr. 43: $\varphi = 0.20$) & Tiêu chuẩn TĐĐ [R4, R5].
>   - **`[5]`**: Tiêu chuẩn Ray A54 & Bánh xe thép ($w_0 = 0.015$, $d = 0.25\text{ m}$), DIN 536 / Hồ sơ kỹ thuật ray [R9-10].
>   - **`[6]`**: Demag Cranes & Components (2011), Catalogue Demag DR/EZDR Rope Hoists & Double-Girder Trolley, Wetter, Đức [R9-07].
>   - **`[7]`**: Sungdo Hoist / KG-Cranes (2020), Hồ sơ Kỹ thuật Pa lăng và Xe con Dầm đôi 15 Tấn ($m_{xc} = 1,800\text{ kg}$) [R9-08].
>   - **`[8]`**: Shevchenko O. O. (2024), Bakalaurska Robota: Hệ truyền động điện cơ cấu di chuyển xe con cầu trục dầm đôi, NTUU KPI [R9-06].
>   - **`[9]`**: T. Mita & T. Kanai (1979) / Tho et al. (2020), Điều khiển chống lắc con lắc cáp ($h = 12\text{ m}$) & Quỹ đạo S-Curve 7 đoạn [R9-01, R9-05, R9-11].
>   - **`[10]`**: NASA SP-2007-6105 Rev1 — Systems Engineering Handbook, NASA Headquarters, Washington, D.C. [R2].

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
| 31 | **$D \ge 10:1$** | Mục 3.2 (SRS-FUNC-04) | **SỬA** (Chuyển sang yêu cầu kiểm chứng biến tần ở Khối 3) | Dải điều chỉnh tốc độ là chỉ tiêu chất lượng của hệ truyền động biến tần, kiểm chứng qua mô phỏng. |
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
