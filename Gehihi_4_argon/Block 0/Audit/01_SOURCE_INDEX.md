# CHỈ MỤC TÀI LIỆU NGUỒN XÁC MINH (SOURCE INDEX)
**Dự án:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Di Chuyển Ngang Xe Con Cầu Trục ($x = 2$)  
**Mã tài liệu:** `AUDIT-01-SOURCE-INDEX` | **Giai đoạn:** Pha 1 — Lập chỉ mục nguồn  
**Thư mục gốc:** `D:\Tài liệu học tập\Kỳ 2026.1\Thiết Kế TĐĐ\Project`  
**Nguyên tắc kiểm toán:** "Không có bằng chứng thì không khẳng định. Chỉ trích dẫn khi đã tự đọc trực tiếp trong phiên này."

---

## 1. BẢNG TỔNG QUAN HỆ THỐNG TÀI LIỆU (R1 — R9)

| Mã R | Tên đầy đủ tài liệu | Năm / Phiên bản | Đường dẫn nội bộ (tương đối từ ROOT) | Số trang | Khả năng đọc text | Ghi chú kiểm toán |
| :---: | :--- | :---: | :--- | :---: | :---: | :--- |
| **`R1`** | **TCVN 4244:2005** — Thiết bị nâng: Thiết kế, chế tạo và kiểm tra kỹ thuật | 2005 (XB lần 2, 2006) | `Case study\tcvn-4244-2005.pdf` | 169 | **Scan (Đọc qua Vision/Multimodal)** | Bản scan 100%, không có text layer nhúng. Đã đọc trực tiếp toàn bộ 169 trang qua module thị giác máy (Vision/OCR). |
| **`R2`** | **NASA Systems Engineering Handbook** (NASA/SP-2007-6105 Rev1) | 2007 (Rev 1) | `Tai_lieu_tham_khao\NASA_SP-2007-6105_Rev_1.pdf` | 360 | **Text OK** | File PDF gốc chất lượng cao, có bản tách trang nhỏ trong cùng thư mục. |
| **`R3`** | **Đề bài tập lớn Truyền động điện** (Học kỳ 2023.1) | 2023 | `Tai_lieu_du_an\De bai tap dai 2023.1 1.pdf` | 9 | **Text OK** | Trang 1 quy định Đề 0~9 (Cơ cấu xe con cầu trục), tính theo $x$. |
| **`R4`** | **Tiêu chuẩn VN và Quốc tế phục vụ thiết kế TĐĐ** (Tài liệu Thầy Đỉnh) | 2015-2018 | `Thầy Đỉnh\TIÊU CHUẨN VN VÀ QUỐC TẾ.pdf` | 147 | **Text OK** | Thư mục mang tên `Thầy Đỉnh`. Tổng hợp các chuẩn IEC/TCVN: IP, Motor S1-S10, MBA, EMC, Khí cụ. |
| **`R5`** | **Bộ slide bài giảng Thiết kế TĐĐ** (PGS.TS. Bùi Quốc Khánh, TS. Nguyễn Duy Đỉnh) | 2021 | `Thầy Đỉnh\Bài 1.pdf`, `Bài 2.1.pdf`, `Bài 2.2.pdf`, `Bài 2.3.pdf`, `Bài 3.pdf`, `Bài 4.pdf` | 271 | **Text OK** | Trọng tâm là `Bài 4.pdf` (99 trang): Cơ cấu xe con cầu trục, cấu trúc biến tần - IM, hãm điện trở, S-curve. |
| **`R6`** | **PRD mẫu tham khảo** | 2023 | `Tai_lieu_du_an\PRD .pdf` | 22 | **Text OK** | Tài liệu hướng dẫn khung PRD chung của môn học. |
| **`R7`** | **SOW mẫu tham khảo** (Sinh viên Hưng NB) | 2023 | `Tai_lieu_du_an\SOW_HungNB.docx.pdf` | 4 | **Text OK** | Bản phạm vi công việc cơ cấu xe con cầu trục mẫu. |
| **`R8`** | **BTL Nhóm 4 khóa trước** (Bơm nước sinh hoạt) | 2023 | `Tai_lieu_du_an\BTL-TKTDD-Nhóm-4.pdf` | 45 | **Text OK** | Tham khảo format báo cáo đồ án của Thầy Đỉnh. |
| **`R9-01`** | **Demag DR rope hoists catalogue** (Dầm đôi_cầu trục truyền động_Đức.pdf) | 11/2011 (Demag Cranes) | `Case study\Dầm đôi_cầu trục truyền động_Đức.pdf` | 16 | **Text OK** | Thông số palăng cáp dầm đôi EZDR 10/20, motor IP55, phanh hệ số 1.8, biến tần, encoder xung. |
| **`R9-02`** | **Mita & Kanai (1979)** — Optimal Control of Crane System (Nhật Bản) | 10/1979 (SICE Japan) | `Case study\Crane trolley Nhật Bổn.pdf` | 6 | **Text OK** | Bài báo gốc về điều khiển tối ưu xe con cầu trục triệt tiêu dao động tải con lắc. |
| **`R9-03`** | **Feto, Wartono, Sutrisna (2025)** — Thiết kế xe con cầu trục 10T (Indonesia) | 02/2025 (Cendekia) | `Case study\Cầu trục_Indo.pdf` | 7 | **Text OK** | Tính toán cơ khí xe con 10 tấn, dầm 20m, vận tốc 15 m/phút. |
| **`R9-04`** | **Serap Özhan Doğan (2023)** — Thiết kế & FEM cầu trục dầm đôi (Thổ Nhĩ Kỳ) | 10/2023 (Elsevier) | `Case study\Thiết kế cầu trục dầm đôi_Thổ.pdf` | 4 | **Text OK** | Mô hình hóa dầm đôi, xe con cuộn tôn thép, phần mềm ANSYS/SolidWorks. |
| **`R9-05`** | **Tho, Kaneshige, Terashima (2020)** — Quy hoạch quỹ đạo S-curve chống lắc | 2020 (Elsevier CEP) | `Case study\S-curve.pdf` | 12 | **Text OK** | Đồ thị S-curve giới hạn độ giật ($\rho$) và gia tốc ($a$) để vận chuyển không rung lắc. |
| **`R9-06`** | **Marian Blejan & Robert Blejan (2020)** — Máy tạo quỹ đạo S-curve thời gian thực | 2020 (Hidraulica) | `Case study\S-curve-simulation.pdf` | 19 | **Text OK** | Phương trình toán học 7 pha chuyển động S-curve khống chế jerk. |
| **`R9-07`** | **A.A. Reutov (2021)** — Mô phỏng điều khiển xe con giảm lắc tải (Nga) | 2021 (IOP Conf. Series) | `Case study\Simulation_of_Crane_Trolley_Motion_Control_to_Redu_Nga.pdf` | 10 | **Text OK** | Mô hình động học 2D xe con và con lắc tải trên MATLAB/Simulink. |
| **`R9-08`** | **Sensors and Materials S&M 2693** — Điều khiển mờ thị giác chống lắc | 2021 (MYU Tokyo) | `Case study\SM2693.pdf` | 12 | **Text OK** | Điều khiển xe con dùng camera quan sát góc lắc và logic mờ (Fuzzy). |
| **`R9-09`** | **Stanimir Valtchev (2024)** — Damping Capacity of Crane Drive (IEEE) | 2024 (IEEE) | `Case study\A54.pdf` | 6 | **Text OK** | Nâng cao khả năng dập tắt dao động của hệ truyền động xe con bằng điều khiển thích nghi. |
| **`R9-10`** | **Yana Shevchenko (2024)** — Đồ án tốt nghiệp ĐH Bách khoa Kiev (KPI) | 06/2024 (NTUU KPI) | `Case study\Shevchenko_bakalavr.pdf` | 79 | **Text OK** | Thiết kế toàn diện hệ truyền động xe con cầu trục: Động cơ S3, biến tần FOC, S-curve, Simulink. |
| **`R9-11`** | **Slide Báo cáo Nhóm 2 khóa trước** — Thiết kế TĐĐ xe con cầu trục | 2023 | `Case study\Bản sao của [NHÓM 2] Thiết kế truyền động xe con cầu trục 2.pptx.pdf` | 38 | **Text OK** | Tham khảo bài toán cùng đề tài của sinh viên ĐHBK Hà Nội. |
| **`R9-12`** | **Báo cáo định hướng thiết kế xe con 12.2T** (Case_study.docx) | 2024 | `Case study\Case_study.docx` | 79 đoạn | **Text OK** | Phân tích cơ sở thực tiễn lựa chọn dẫn động riêng 2 động cơ và kiểm tra bám ray. |
| **`R9-13`** | **Dynamic crane trolley.pdf** | — | `Case study\Dynamic crane trolley.pdf` | 46 | **Lỗi Font (CID/Encoding)** | Không trích xuất được chữ dạng thông thường do font nhúng bị mã hóa sai bảng mã. |

---

## 2. CHỈ MỤC CHI TIẾT TIÊU CHUẨN TCVN 4244:2005 (`R1`)

> **Nguồn xác minh:** `ROOT\Case study\tcvn-4244-2005.pdf` (169 trang, đã đọc thị giác toàn văn).  
> **Lưu ý đánh số trang:** Trang in trên tài liệu bắt đầu từ trang 7 (Chương 1) tương ứng trang PDF số 3. Công thức: `Trang PDF = Trang in - 4`.

### 2.1. Mục lục Hệ thống TCVN 4244:2005

| Số mục | Tiêu đề điều khoản | Trang in | Trang PDF | Nội dung kỹ thuật cốt lõi |
| :--- | :--- | :---: | :---: | :--- |
| **1** | **QUI ĐỊNH CHUNG** | **7** | **3** | |
| 1.1 | Qui định chung (1.1.1 Phạm vi áp dụng; 1.1.2; 1.1.3) | 7 | 3 | Áp dụng cho cần trục, cầu trục, cổng trục, xe tời chạy theo ray trên cao, palăng điện. |
| 1.2 | Tài liệu viện dẫn | 7 | 3 | Liệt kê ISO 4309, ISO 2408, IEC 34-5 (IP code), IEC 341. |
| 1.3 | Các định nghĩa | 8–9 | 4–5 | Định nghĩa 17 thuật ngữ then chốt của thiết bị nâng. |
| 1.3.3 | Tải trọng làm việc an toàn (SWL) | 8 | 4 | Khối lượng hàng lớn nhất được phép nâng kể cả bộ phận dùng để nâng (gàu ngoạm, móc, cáp, xà...). |
| 1.3.4 | Tải trọng tĩnh | 8 | 4 | Khối lượng bản thân của các bộ phận cấu thành tác động lên bộ phận đang xét, ngoại trừ tải trọng làm việc. |
| 1.3.7 | Các cơ cấu | 8 | 4 | Cơ cấu nâng hàng, cơ cấu nâng cần, cơ cấu quay và cơ cấu di chuyển (bao gồm cả các tời). |
| 1.3.11 | Thiết bị cảnh báo và bảo vệ an toàn | 8 | 4 | Thiết bị cảnh báo tự động và thiết bị bảo vệ tự động tạm dừng hoạt động. |
| 1.3.12 | Hệ số an toàn phanh | 8 | 4 | Tỷ số giữa mômen tĩnh do phanh sinh ra với mômen tĩnh trên trục phanh dưới tác dụng của tải trọng tính toán. |
| 1.3.14 | Phanh thường đóng | 9 | 5 | "Loại phanh chỉ mở khi được cấp năng lượng." |
| 1.3.16 | Phanh tự động | 9 | 5 | "Loại phanh tự động đóng khi ngắt nguồn năng lượng cho động cơ của cơ cấu bố trí phanh đó." |
| 1.4 | Hồ sơ kỹ thuật (1.4.1 – 1.4.4) | 9 | 5 | Yêu cầu về thuyết minh, bản vẽ tổng thể, sơ đồ nguyên lý điện/thủy lực/khí nén. |
| 1.5 | Yêu cầu chung về an toàn kỹ thuật | 9–22 | 5–18 | |
| 1.5.1 | Đóng dấu và gắn nhãn hàng hoá (1.5.1.1, 1.5.1.2, 1.5.1.3 Biển cảnh báo) | 9–10 | 5–6 | Ghi sức nâng (kg/tấn), biển "Không được đứng dưới tải nâng", biển khu vực nguy hiểm. |
| 1.5.2 | Các yêu cầu an toàn về kết cấu (1.5.2.1 Khoảng trống; 1.5.2.2 Kim loại) | 10–14 | 6–10 | Khe hở an toàn; cabin điều khiển; lan can, sàn; cầu thang và thang. |
| 1.5.3 | Thiết bị cơ khí | 14–16 | 10–12 | Dẫn động cáp xích; móc cẩu; cơ cấu phanh. |
| **1.5.3.3** | **Phanh** | **15–16** | **11–12** | **Quy định bắt buộc về cơ cấu phanh:** |
| 1.5.3.3.1 | Yêu cầu chung về phanh | 15 | 11 | Lắp đặt phanh cơ; lò xo nén; phanh hiệu chỉnh được; má phanh thay thế được. |
| 1.5.3.3.2 | Phanh cơ cấu nâng | 15 | 11 | Phanh tự động; hệ số an toàn phanh tối thiểu 1.6 lần tải nâng. |
| **1.5.3.3.3** | **Phanh cơ cấu di chuyển thiết bị nâng và xe tời** | **15** | **11** | Phanh tự động đóng khi mất điện; dừng trong thời gian thích hợp; giữ cố định trong mọi trạng thái; hệ số an toàn phanh không nhỏ hơn 1.1 lần lực tác dụng lớn nhất khi không hoạt động. |
| 1.5.4 | Thiết bị thuỷ lực (1.5.4.1 – 1.5.4.11) | 16 | 12 | Ống chịu áp, van xả khí, chất lỏng thủy lực. |
| **1.5.4.10** | **Chống khởi động không cố ý** | **16** | **12** | "Khởi động không cố ý các dẫn động sau khi có điện trở lại hoặc khi đóng cầu nguồn của cần trục cần phải được phòng ngừa." |
| 1.5.5 | Thiết bị an toàn | 16–18 | 12–14 | Giới hạn hành trình, giảm chấn, chống lật, thiết bị cảnh báo. |
| **1.5.5.1.2**| **Thiết bị giới hạn và giảm chấn cơ cấu di chuyển** | **17** | **13** | Đệm giảm chấn hấp thụ 50% động năng ở tốc độ định mức; gia tốc giảm tốc lớn nhất trong cabin $\le 2.5\text{ m/s}^2$ (hoặc $\le 5\text{ m/s}^2$ nếu thường xuyên giới hạn tốc độ); thiết bị gạt chướng ngại vật trên ray. |
| **1.5.5.2.1**| **An toàn chống trật bánh, sụt bánh và chống lật** | **18** | **14** | Thiết bị an toàn chống trật bánh: độ sụt lớn nhất giới hạn đến 3 cm và ngăn ngừa đổ, lật. |
| **1.5.5.3** | **Thiết bị cảnh báo** | **18** | **14** | Tín hiệu ánh sáng và âm thanh khi bắt đầu nâng hàng, khi đang di chuyển. |
| 1.5.6 | Sự lão hoá của thiết bị nâng | 18 | 14 | Mỏi, ăn mòn, quá tải, bảo dưỡng. |
| 1.5.7 | Yêu cầu an toàn trong lắp đặt và sử dụng | 18–22 | 14–18 | An toàn lắp đặt (1.5.7.1) và an toàn sử dụng (1.5.7.2). |
| **1.5.7.2.9**| **Các hành vi nghiêm cấm trong sử dụng** | **21** | **17** | Cấm chuyển hướng chuyển động (đảo chiều) khi cơ cấu chưa ngừng hẳn. |
| **2** | **THIẾT KẾ** | **23–109**| **19–105**| |
| 2.1 | Phân nhóm và tải trọng tác dụng | 23–57 | 19–53 | Phân nhóm thiết bị (A1-A8) và cơ cấu (M1-M8); tải trọng tĩnh, động, gió. |
| 2.1.1.2.2 | Các cấp sử dụng thiết bị nâng | 23 | 19 | Bảng 2.1.1.2.2: U0 đến U9 theo tổng số chu kỳ nâng ($n_{\max}$). |
| 2.1.1.2.3 | Phổ tải thiết bị nâng | 24–25 | 20–21 | Bảng 2.1.1.2.3: Hệ số phổ tải $K_p$, cấp Q1 đến Q4. |
| 2.1.1.2.4 | Bảng phân nhóm thiết bị nâng tổng thể | 26 | 22 | Bảng 2.1.1.2.4: Nhóm A1 đến A8 (kết hợp U0-U9 và Q1-Q4). |
| 2.1.1.3.2 | Các cấp sử dụng của các cơ cấu | 28 | 24 | Bảng 2.1.1.3.2: Cấp T0 đến T9 theo tổng thời gian sử dụng $T$ (giờ). |
| 2.1.1.3.3 | Phổ tải của các cơ cấu | 28–29 | 24–25 | Bảng 2.1.1.3.3: Hệ số phổ tải $K_m$, cấp L1 đến L4. |
| 2.1.1.3.4 | Bảng phân nhóm các cơ cấu riêng biệt | 29 | 25 | Bảng 2.1.1.3.4: Nhóm M1 đến M8 (kết hợp T0-T9 và L1-L4). |
| **2.1.1.3.5**| **Hướng dẫn phân nhóm các cơ cấu thiết bị nâng** | **30** | **26** | Bảng 2.1.1.3.5: Cần trục trong phân xưởng: Cơ cấu di chuyển xe con phân nhóm **M4**; Bãi kho dùng móc cẩu: di chuyển xe con **M4 – M5**. |
| 2.1.2.3.1 | Tải trọng do tăng tốc/giảm tốc chuyển động ngang | 41–42 | 37–38 | Bảng 2.1.2.3.1.1: Bảng thời gian gia tốc và giá trị gia tốc thiết kế. Giới hạn lực ngang $1/30 \le F_h \le 1/4$ tải bánh dẫn động. |
| 2.3.2.4 | Chọn các bánh xe chạy trên ray | 80–83 | 76–79 | Bánh xe thép, ứng suất tiếp xúc Hertz, bảng hệ số tốc độ $c_1$ và hệ số nhóm $c_2$. |
| 2.4 | Thiết bị điện | 84–107| 80–103| Cấp điện, sụt áp $\le 5\%$, thanh dẫn, cáp dẹt treo trượt. |
| 2.4.3 | Thiết bị bảo vệ và an toàn điện | 90 | 86 | Bảo vệ động cơ S1-S2, S3-S8; bảo vệ mất pha, đảo pha; nút dừng khẩn cấp. |
| **2.4.4.1.3**| **Công tắc giới hạn hành trình xe con** | **91** | **87** | Bắt buộc giới hạn chuyển động xe con ngay trước khi tới đầu mút ray (áp dụng cho xe có $v > 0.4\text{ m/s}$ hoặc tải $> 1000\text{ kg}$). |
| **2.4.5.4.3**| **Điều khiển từ sàn & Nút dừng khẩn cấp** | **94** | **90** | Bàn phím tay bấm nút màu đỏ ngắt toàn bộ chuyển động, cấp bảo vệ tối thiểu IP43 (trong nhà) / IP55 (ngoài trời). |
| **2.4.5.5.2**| **Phối hợp liên động Phanh cơ khí và Phanh điện** | **94** | **90** | Khi dùng phanh điện, phanh cơ chỉ tác dụng sau khi phanh điện tác dụng; không được phanh cơ khi động cơ đang được cấp điện. |
| 2.4.7.1 | Tiêu chuẩn lựa chọn động cơ điện | 95 | 91 | Định nghĩa theo IEC 34-1 / IEC 341. |
| 2.4.7.2.1.2| Tính toán phát nhiệt động cơ nâng (S3, S4, S5) | 97–98 | 93–94 | Hệ số thời gian hoạt động $ED = [t_{\text{chạy}} / (t_{\text{chạy}} + t_{\text{nghỉ}})] \times 100\%$. Bảng 2.4.7.2.1.2.a. |
| **2.4.7.2.2.1**| **Chế độ làm việc động cơ chuyển động ngang** | **101** | **97** | Bảng 2.4.7.2.2.1: Nhóm M4 có cấp khởi động 150 lần/h, hệ số tiếp điện $ED = 35\%$; Nhóm M5 có cấp khởi động 180 lần/h, hệ số tiếp điện $ED = 30\%$. |
| **2.4.7.2.2**| **Tính toán chọn động cơ di chuyển ngang** | **99–101**| **95–97**| Công thức lực cản $W$, mô-men cản quy đổi, chọn động cơ theo chế độ ngắn hạn lặp lại **S3**. |
| **3** | **VẬT LIỆU VÀ HÀN** | **110–121**| **106–117**| Chọn chất lượng thép kết cấu, mối hàn góc, mối hàn đối đầu, kiểm tra NDT. |
| **4** | **KIỂM TRA VÀ THỬ** | **122–124**| **118–120**| Thử tĩnh ($125\%\text{ SWL}$ trong 10 phút), thử động ($110\%\text{ SWL}$). |
| **Phụ lục**| **Phụ lục 1 đến Phụ lục 21** | **125–173**| **121–169**| Dung sai đường ray (Phụ lục 5, tr. 139–144), kiểm tra móc treo, puly, cáp thép, mối ghép bu lông. |

---

### 2.2. Bằng chứng Trích dẫn Nguyên văn Các Điều khoản Cốt lõi TCVN 4244:2005

1. **Phân loại cơ cấu di chuyển xe con:**
   * **Vị trí:** [R1, §1.3.7, tr.8 (PDF tr.4)]
   * **Trích nguyên văn:** *"Cơ cấu nâng hàng, cơ cấu nâng cần, cơ cấu quay và cơ cấu di chuyển của cần trục bao gồm cả các tời của chúng."*
2. **Nhóm chế độ làm việc cơ cấu xe con:**
   * **Vị trí:** [R1, §2.1.1.3.5, Bảng 2.1.1.3.5, tr.30 (PDF tr.26)]
   * **Trích nguyên văn:** *"Các cần trục trong phân xưởng: Di chuyển xe con M4... Các thiết bị nâng dùng để vận chuyển vật liệu tại các bãi kho - Dùng móc cẩu: Di chuyển xe con M4 - M5."*
3. **Phanh cơ cấu di chuyển — Kiểu phanh và Hệ số an toàn:**
   * **Vị trí:** [R1, §1.5.3.3.3, tr.15 (PDF tr.11)]
   * **Trích nguyên văn:** *"Thiết bị dẫn động di chuyển thiết bị nâng và xe tời hoạt động điện phải trang bị phanh tự động, hoặc phanh có thể hoạt động từ vị trí điều khiển... Phanh phải được thiết kế sao cho thiết bị nâng hoặc xe tời có thể dừng trong một thời gian thích hợp và giữ cố định trong mọi trạng thái hoạt động... Phanh tự động hoặc thiết bị chống bão của cơ cấu di chuyển phải được thiết kế với hệ số an toàn không nhỏ hơn 1,1 lần lực tác dụng lớn nhất trong điều kiện thiết bị nâng không hoạt động."*
   * *Định nghĩa phanh thường đóng:* [R1, §1.3.14, tr.9 (PDF tr.5)]: *"Loại phanh chỉ mở khi được cấp năng lượng."*
   * *Định nghĩa phanh tự động:* [R1, §1.3.16, tr.9 (PDF tr.5)]: *"Loại phanh tự động đóng khi ngắt nguồn năng lượng cho động cơ của cơ cấu bố trí phanh đó."*
4. **Chống tự khởi động lại ngẫu nhiên:**
   * **Vị trí:** [R1, §1.5.4.10, tr.16 (PDF tr.12)]
   * **Trích nguyên văn:** *"Khởi động không cố ý các dẫn động sau khi có điện trở lại hoặc khi đóng cầu nguồn của cần trục cần phải được phòng ngừa."*
5. **Công tắc giới hạn hành trình và Đệm giảm chấn:**
   * **Vị trí:** [R1, §1.5.5.1.2, tr.17 (PDF tr.13)]
   * **Trích nguyên văn:** *"Thiết bị nâng và xe tời hoạt động điện phải được trang bị các thiết bị như phanh guốc, đệm giảm chấn kiểu cao su, lò xo hoặc thuỷ lực hoặc các thiết bị đặc biệt khác có khả năng hấp thụ một nửa động năng của các khối lượng đang chuyển động tại tốc độ di chuyển định mức và sao cho sự giảm tốc lớn nhất trong cabin điều khiển không vượt quá 2,5 m/s². Nếu thường xuyên phải giới hạn tốc độ di chuyển trong quá trình hoạt động thông thường thì sự giảm tốc lớn nhất trong cabin điều khiển phải không vượt quá 5 m/s²."*
   * *Công tắc giới hạn hành trình điện:* [R1, §2.4.4.1.3, tr.91 (PDF tr.87)]: *"Trong trường hợp cần cẩu được trang bị xe con chạy trên cần, thì chuyển động của xe con phải được giới hạn ngay trước khi xe con chạy tới các đầu cuối của cần."*
6. **Chống trật bánh, độ sụt bánh xe và chống lật:**
   * **Vị trí:** [R1, §1.5.5.2.1, tr.18 (PDF tr.14)]
   * **Trích nguyên văn:** *"Thiết bị nâng và xe tời phải được thiết kế... trong trường hợp trật bánh khỏi đường ray hoặc có sự hư hỏng của bánh xe hoặc trục hoặc ổ đỡ bánh xe, thì độ sụt lớn nhất dưới giới hạn đến 3cm và sự đổ và lật được ngăn ngừa."*
7. **Tín hiệu cảnh báo di chuyển:**
   * **Vị trí:** [R1, §1.5.5.3, tr.18 (PDF tr.14)]
   * **Trích nguyên văn:** *"Các thiết bị nâng phải được trang bị các thiết bị phát tín hiệu ánh sáng và âm thanh khi các cơ cấu hoạt động có thể gây nguy hiểm cho người xung quanh... khi cần trục đang di chuyển..."*
8. **Quy tắc cấm đảo chiều đột ngột khi chưa dừng hẳn:**
   * **Vị trí:** [R1, §1.5.7.2.9, tr.21 (PDF tr.17)]
   * **Trích nguyên văn:** *"Trong quá trình sử dụng thiết bị nâng, không cho phép: ... Chuyển hướng chuyển động của các cơ cấu khi cơ cấu chưa ngừng hẳn..."*
9. **Định nghĩa Tải trọng làm việc an toàn (SWL) và Tải trọng tĩnh:**
   * **Vị trí:** [R1, §1.3.3 & §1.3.4, tr.8 (PDF tr.4)]
   * **Trích nguyên văn SWL:** *"Khối lượng hàng lớn nhất được phép nâng kể cả các bộ phận dùng để nâng hàng như: gàu ngoạm, móc, cáp, xà, khung cẩu, ..v..v. ở mã hàng được nâng."*
   * **Trích nguyên văn Tải tĩnh:** *"Khối lượng bản thân của các bộ phận cấu thành tác động lên bộ phận đang xét, ngoại trừ tải trọng làm việc."*
10. **Phối hợp liên động Phanh cơ khí và Phanh điện:**
    * **Vị trí:** [R1, §2.4.5.5.2, tr.94 (PDF tr.90)]
    * **Trích nguyên văn:** *"Khi sử dụng phanh điện, thì phanh cơ chỉ tác dụng sau khi phanh điện tác dụng. Ngoại trừ các trạng thái chuyển tiếp, cơ cấu phanh không được tác dụng khi động cơ được kích hoạt."*
11. **Quy định chọn động cơ theo chế độ S3:**
    * **Vị trí:** [R1, §2.4.7.2.2.1, Bảng 2.4.7.2.2.1, tr.101 (PDF tr.97) & §2.4.7.2.1.2, tr.100 (PDF tr.96)]
    * **Trích nguyên văn:** *"Động cơ phải được chọn sao cho mômen quay định mức của động cơ trong chế độ hoạt động S3 đối với hệ số hoạt động được xem là lớn hơn hoặc bằng mômen quay tương đương trung bình."*

---

## 3. CHỈ MỤC XÁC MINH NASA SYSTEMS ENGINEERING HANDBOOK (`R2`)

> **Nguồn xác minh:** `ROOT\Tai_lieu_tham_khao\NASA_SP-2007-6105_Rev_1.pdf` (360 trang).  
> **Lưu ý đánh số trang:** Trang in của tài liệu bắt đầu từ trang 1 tại PDF trang 19. Công thức: `Trang PDF = Trang in + 18`.

| Mục nội dung | Trang in trên sách | Trang trong file PDF | Bằng chứng trích dẫn nguyên văn & Tóm tắt nội dung xác minh |
| :--- | :---: | :---: | :--- |
| **§4.1 Stakeholder Expectations Definition** | **33 – 39** | **51 – 57** | **Trích nguyên văn (tr. 33 / PDF 51):** *"The Stakeholder Expectations Definition Process is the initial process within the SE engine that establishes the foundation from which the system is designed and the product is realized. The main purpose of this process is to identify who the stakeholders are and how they intend to use the product."*<br>• *Xác minh ConOps:* Mục 4.1.1.2 (tr. 35–38 / PDF 53–56) quy định xây dựng Concept of Operations (ConOps) và Operational Scenarios. |
| **§4.2 Technical Requirements Definition** | **40 – 48** | **58 – 66** | **Trích nguyên văn (tr. 40 / PDF 58):** *"The Technical Requirements Definition Process transforms the stakeholder expectations into a definition of the problem and then into a complete set of validated technical requirements expressed as 'shall' statements that can be used for defining a design solution..."* |
| **Mục xuất bản Technical Measures (MOE / MOP / TPM)** | **41** | **59** | **Trích nguyên văn (tr. 41 / PDF 59):** *"Technical Measures: An established set of measures based on the expectations and requirements that will be tracked and assessed to determine overall system or product effectiveness and customer satisfaction. Common terms for these measures are Measures of Effectiveness (MOEs), Measures of Performance (MOPs), and Technical Performance Measures (TPMs). See Section 6.7 for further details."* |
| **Định nghĩa chi tiết & Khung liên kết MOE / MOP / TPM** | **191 – 195** | **209 – 213** | **Vị trí:** §6.7.2.2 *Technical Measures—MOEs, MOPs, and TPMs*.<br>• **MOE (tr. 191 / PDF 209):** *"MOEs are the 'operational' measures of success that are closely related to the achievement of the mission or operational objective... MOEs should be independent of any particular solution."*<br>• **MOP (tr. 192 / PDF 210):** *"MOPs are the measures that characterize physical or functional attributes... An MOE represents a stakeholder expectation or operational objective... An MOP is a quantitative measure that characterizes the system."*<br>• **TPM (tr. 192 / PDF 210):** *"TPMs are critical or key mission success or performance parameters that are tracked and assessed during the design and development cycle... When a TPM value falls outside of an acceptable threshold, this indicates that the system development effort is in trouble..."*<br>• **Hình 6.7-4 (tr. 192 / PDF 210):** *"Figure 6.7-4 Relationships of MOEs, MOPs, and TPMs"*. |
| **Appendix C: How to Write a Good Requirement** | **279 – 281** | **297 – 299** | **Trích nguyên văn (tr. 279 / PDF 297):** *"Appendix C: How to Write a Good Requirement... Requirements should state WHAT is needed, NOT HOW to provide... Use of Correct Terms: Shall = an imperative; Will = a statement of fact or declaration of purpose; Should = a goal or statement of intention."* |

---

## 4. CHỈ MỤC XÁC MINH ĐỀ BÀI TẬP LỚN (`R3`)

> **Nguồn xác minh:** `ROOT\Tai_lieu_du_an\De bai tap dai 2023.1 1.pdf` (Trang 1, Đề 0~9).

### 4.1. Trích nguyên văn Đề bài Đề 0~9 (Trang 1)

```text
Đề 0~9
Thiết kế hệ truyền động cơ cấu xe con cầu trục với thông số như sau:
- Tải trọng định mức         : 1x,xxx kg
- Khối lượng cơ cấu nâng hạ  : 2xx kg
- Chiều cao nâng             : h = 1x m
- Tốc độ tối đa              : v = 0.1x m/s
- Gia tốc cực đại            : a ≤ 0.5 m/s2
- Độ giật cực đại            : 𝜌 ≤ 2 m/s3

Yêu cầu:
- Mô tả nguyên lý, công nghệ
- Xây dựng yêu cầu truyền động, cấu trúc hệ truyền động
- Tính chọn công suất động cơ
- Thiết kế các mạch vòng điều chỉnh
- Thiết kế logic hoạt động của hệ thống
- Mô phỏng kiểm chứng theo ít nhất một kịch bản làm việc

Ghi chú: x = hàng đơn vị của số thứ tự trong danh sách lớp
```

### 4.2. Bảng đối chiếu số liệu cụ thể cho nhóm ($x = 2$, STT 22: Nghiêm Trọng Đông)

| Thông số | Công thức đề bài giao | Giá trị tính ra ($x = 2$) | Trạng thái đề bài | Phân loại kiểm toán |
| :--- | :---: | :---: | :---: | :---: |
| **Tải trọng định mức ($Q$)** | $1x,xxx\text{ kg}$ | **$12,222\text{ kg}$** | **ĐỀ BÀI CHO SẴN** | **[A] Đề bài** |
| **Khối lượng cơ cấu nâng hạ ($m_{nh}$)** | $2xx\text{ kg}$ | **$222\text{ kg}$** | **ĐỀ BÀI CHO SẴN** | **[A] Đề bài** |
| **Chiều cao nâng ($h$)** | $1x\text{ m}$ | **$12\text{ m}$** | **ĐỀ BÀI CHO SẴN** | **[A] Đề bài** |
| **Vận tốc di chuyển tối đa ($v_{\max}$)** | $0.1x\text{ m/s}$ | **$0.12\text{ m/s}$** | **ĐỀ BÀI CHO SẴN** | **[A] Đề bài** |
| **Gia tốc cực đại ($a_{\max}$)** | $a \le 0.5\text{ m/s}^2$ | **$\le 0.5\text{ m/s}^2$** | **ĐỀ BÀI CHO SẴN** | **[A] Đề bài** |
| **Độ giật cực đại ($\rho_{\max}$)** | $\rho \le 2\text{ m/s}^3$ | **$\le 2.0\text{ m/s}^3$** | **ĐỀ BÀI CHO SẴN** | **[A] Đề bài** |

### 4.3. Xác nhận các thông số ĐỀ BÀI KHÔNG CHO (Bắt buộc là Giả định nhóm [C])

Đề bài gốc **HOÀN TOÀN KHÔNG CHO** các thông số sau:
1. **Sai lệch tốc độ xác lập ($e_{xl}$):** Đề bài không quy định $\to$ PRD tự đặt $\le 5\%$ (Phải chuyển sang [C] Giả định nhóm, kiểm chứng qua mô phỏng).
2. **Độ quá điều chỉnh tốc độ ($M_p$):** Đề bài không quy định $\to$ PRD tự đặt $\le 10\%$ (Phải chuyển sang [C] Giả định nhóm).
3. **Thời gian dừng khẩn cấp ($t_{\text{stop}}$):** Đề bài không quy định $\to$ PRD tự đặt $\le 2.0\text{ s}$ (Phải chuyển sang [C] Giả định nhóm).
4. **Khối lượng bản thân xe con ($m_{xc}$):** Đề bài không quy định $\to$ Phải giả định dựa trên kết cấu xe dầm đôi thực tế.
5. **Đường kính bánh xe con ($d$):** Đề bài không quy định $\to$ Phải tính chọn/giả định theo tiêu chuẩn đường kính bánh xe cầu trục (TCVN 4244 mục 2.3.2.4).
6. **Hệ số cản chuyển động ($\mu$ hoặc $w_0$):** Đề bài không quy định $\to$ Phải tính theo công thức cản lăn cơ khí, không được tùy tiện gán $\mu = 0.20$.
7. **Hiệu suất cơ khí ($\eta$) & Hệ số dự trữ ($k_{dt}$):** Đề bài không quy định $\to$ Giả định kỹ thuật của nhóm.
8. **Chế độ làm việc động cơ ($S3$, $CD\%$):** Đề bài không quy định $\to$ Giả định chuẩn công nghiệp cho cơ cấu di chuyển cầu trục (TCVN 4244 Bảng 2.4.7.2.2.1 chọn $S3 - 30\%$ hoặc $40\%$).

---

## 5. CHỈ MỤC TÀI LIỆU GIẢNG DẠY CỦA THẦY ĐỈNH (`R4`, `R5`)

### 5.1. File `Thầy Đỉnh\TIÊU CHUẨN VN VÀ QUỐC TẾ.pdf` (`R4`, 147 trang)

| Tiêu chuẩn được trích dẫn | Vị trí trang | Nội dung chính xác được giảng dạy trong tài liệu |
| :--- | :---: | :--- |
| **Bản vẽ kỹ thuật điện & Tag thiết bị (IEC 750 / ANSI)** | Trang 1 – 15 | Quy chuẩn vẽ sơ đồ nguyên lý: Tọa độ lưới (Cross Reference), ký hiệu -KM, -Q, -M. |
| **Cấp bảo vệ vỏ ngoài (Mã IP): TCVN 4255:2008 / IEC 60529:2001** | Trang 16 – 17 | Định nghĩa mã IP (chống bụi, chống nước). Quy định tối thiểu IP43 (trong nhà) / IP55 (ngoài trời). |
| **Tiêu chuẩn Hiệu suất năng lượng: TCVN 7540-1:2013** | Trang 18 – 22 | Phân cấp hiệu suất động cơ điện 3 pha lồng sóc (IE1, IE2, IE3). |
| **Tiêu chuẩn Động cơ điện: IEC 60034 series & IEC 60085** | Trang 23 – 29 | • **10 chế độ vận hành (S1 – S10):** S1 (liên tục), S2 (ngắn hạn), S3 (ngắn hạn lặp lại theo chu kỳ), S4 (kèm khởi động).<br>• **Cấp cách điện:** B ($130^\circ\text{C}$), F ($155^\circ\text{C}$), H ($180^\circ\text{C}$).<br>• **Cấp làm mát IC:** IC411 (làm mát bằng cánh quạt liền trục). |
| **Máy biến áp lực: TCVN 6306:2015 / IEC 60076:2011** | Trang 30 – 76 | Quy định định mức, độ tăng nhiệt và thử nghiệm máy biến áp. |
| **Tương thích điện từ (EMC): TCVN 7909-1-1:2008 / IEC/TR 61000-1-1** | Trang 77 – 102 | Giới hạn sóng hài và nhiễu điện từ trong lưới điện công nghiệp. |
| **Khí cụ đóng cắt & Điều khiển hạ áp: TCVN 6592-1:2009 / IEC 60947-1** | Trang 103 – 147 | Cầu dao, contactor, aptomat, rơle nhiệt, thử nghiệm ngắn mạch và phát nhiệt. |

### 5.2. Bộ Slide Bài giảng Thầy Đỉnh (`R5`)

| Tên bài giảng | Số trang | Nội dung chuyên môn liên quan trực tiếp đến đề tài Xe con cầu trục |
| :--- | :---: | :--- |
| **Bài 1.pdf** — Khái quát thiết kế TĐĐ | 18 | Quy trình thiết kế 6 bước: Yêu cầu công nghệ $\to$ Cấu trúc $\to$ Chọn động cơ $\to$ Mạch vòng $\to$ Mô phỏng $\to$ Kiểm chứng. |
| **Bài 2.1.pdf** — Cấu trúc điều khiển nối tầng | 30 | Cấu trúc điều khiển vòng kín nhiều mạch vòng nối tầng: Mạch vòng dòng điện (bên trong) và mạch vòng tốc độ (bên ngoài). |
| **Bài 2.2.pdf** — Hệ TĐĐ động cơ một chiều | 20 | Nguyên lý và điều khiển động cơ DC (không áp dụng trực tiếp cho phương án AC lồng sóc). |
| **Bài 2.3.pdf** — Hệ TĐĐ động cơ không đồng bộ 3 pha | 66 | Điều khiển biến tần - IM: FOC (Field-Oriented Control), DTC, nghịch lưu áp PWM, sơ đồ thay thế động cơ. |
| **Bài 3.pdf** — Tải của truyền động điện | 38 | Quy đổi mô-men quán tính $J_{qđ}$, mô-men cản $M_c$, tính toán phát nhiệt động cơ. |
| **Bài 4.pdf** — Phương pháp thiết kế | 99 | **Nội dung mấu chốt về xe con cầu trục:**<br>• **Trang 43:** Truyền động kéo BT-IM xe con cầu trục: lực ma sát trượt $F_k = f \cdot G$, mô-men mở máy lớn cần thắng ma sát nghỉ gấp 1.5 - 2 lần.<br>• **Trang 44:** Sơ đồ biến tần một động cơ, nguồn 3 pha qua thanh góp, hãm điện dùng điện trở xả hãm $R_h$.<br>• **Trang 46:** Quy luật vận hành S-curve: giới hạn gia tốc $a(t)$ và độ giật $\rho = da/dt$ qua các pha mở máy, chạy đều, hãm bò, dừng.<br>• **Trang 51–52:** Khẳng định cầu trục có 3 cơ cấu độc lập (xe cầu, xe con, nâng hạ); xe con dùng BT-IM với 2 mạch vòng PI nối tầng. |

---

## 6. CHỈ MỤC TÓM TẮT TÀI LIỆU CASE STUDY THỰC TẾ (`R9`)

| Mã tài liệu | Tên file | Tác giả / Hãng sản xuất & Năm | Tóm tắt thông số kỹ thuật đã đọc & Trang xác minh |
| :---: | :--- | :--- | :--- |
| **`R9-01`** | `Dầm đôi_cầu trục truyền động_Đức.pdf` | **Demag Cranes & Components GmbH (Đức)** (11/2011) | • **Dòng sản phẩm:** Palăng cáp dầm đôi EZDR 10 & EZDR 20.<br>• **Cấp tải SWL:** $12.5\text{ tấn}$ (DR 10) và $20\text{ tấn} \div 50\text{ tấn}$ (DR 20) (tr. 9 & 13).<br>• **Thông số cơ điện:** Động cơ lồng sóc có sẵn **Encoder xung** đo tốc độ và chiều quay, bảo vệ **IP55** (tr. 4). Phanh đĩa DC đóng nhanh với hệ số an toàn tối thiểu **$\ge 1.8$** (tr. 4). Hộp giảm tốc 3 cấp bánh răng trụ bôi trơn trọn đời (tr. 4).<br>• **Truyền động di chuyển xe con:** Biến tần vô cấp (*cross-travel inverter*) tích hợp sẵn **điện trở xả hãm** trong tủ điện (tr. 8); có thanh kẹp chống trật ray và chống nhấc bánh xe (tr. 9). |
| **`R9-02`** | `Crane trolley Nhật Bổn.pdf` | **Tsutomu Mita & Takashi Kanai** (Đại học Chiba, Nhật Bản — 10/1979) | • **Tên bài báo:** "トロリーの最大速度に注目したクレーンの最適運転法" (Optimal Control of the Crane System Using the Maximum Speed of the Trolley), SICE Japan, Vol. 15, No. 6, tr. 833–839.<br>• **Nội dung:** Bài báo kinh điển giải quyết mô hình toán học xe con kéo tải con lắc đơn dây treo cáp $l$. Chứng minh quy luật điều khiển vận tốc tối ưu triệt tiêu góc lắc dư khi dừng tại đích. |
| **`R9-03`** | `Cầu trục_Indo.pdf` | **Petrus Gregorius Feto, Wartono, Sutrisna** (Yogyakarta, Indonesia — 02/2025) | • **Tên bài báo:** "Perencanaan Sistem Trolley dan Bridge Pada Overhead Travelling Crane Beban Angkat 10 Ton", Tạp chí Cendekia, Vol. 6, No. 2, tr. 66–72.<br>• **Thông số thiết kế:** Tải trọng $Q = 10\text{ tấn}$, khẩu độ dầm $L = 20\text{ m}$, vận tốc di chuyển xe con $v = 15\text{ m/phút}$ ($0.25\text{ m/s}$).<br>• Tính toán chi tiết tải trọng bánh xe và lực cản di chuyển xe con. |
| **`R9-04`** | `Thiết kế cầu trục dầm đôi_Thổ.pdf` | **Serap Özhan Doğan** (Đại học Beykent, Thổ Nhĩ Kỳ — 10/2023) | • **Tên bài báo:** "Design and analysis of double girder overhead crane system", Elsevier JRRAS 16 (2023) 100701.<br>• **Thông số:** Cầu trục dầm đôi vận chuyển cuộn tôn $2 \div 6\text{ tấn}$ trong nhà máy thép. Phân tích kết cấu dầm và xe con bằng phương pháp phần tử hữu hạn (ANSYS / SolidWorks). Có đề cập yêu cầu soft-start / soft-stop giảm sốc tải (tr. 2). |
| **`R9-05`** | `S-curve.pdf` | **H.D. Tho, A. Kaneshige, K. Terashima** (Đại học Công nghệ Toyohashi, Nhật Bản — 2020) | • **Tên bài báo:** "Minimum-time S-curve commands for vibration-free transportation of an overhead crane with actuator limits", Control Engineering Practice 98 (2020) 104390.<br>• **Nội dung:** Thiết kế lệnh điều khiển quỹ đạo dạng S-curve thời gian tối thiểu có khống chế gia tốc cực đại $a_{\max}$ và độ giật cực đại $\rho_{\max}$ để vận chuyển hàng không lắc trên cầu trục. |
| **`R9-06`** | `S-curve-simulation.pdf` | **Marian Blejan & Robert Blejan** (Rumani — 2020) | • **Tên bài báo:** "Mathematics for Real-Time S-Curve Profile Generator", Tạp chí Hidraulica No. 4/2020, tr. 7–25.<br>• **Nội dung:** Thiết lập hệ phương trình toán học giải tích cho bộ tạo quỹ đạo S-curve 7 pha thời gian thực (Jerk, Acceleration, Velocity, Position). |
| **`R9-07`** | `Simulation_of_Crane_Trolley_Motion_Control_to_Redu_Nga.pdf` | **A.A. Reutov** (Nga — 2021) | • **Tên bài báo:** "Simulation of Crane Trolley Motion Control to Reduce Load Sway", IOP Conf. Series: Materials Science and Engineering / JPCS 2096 (2021) 012004.<br>• **Nội dung:** Xây dựng mô hình động lực học xe con và tải lắc trên MATLAB/Simulink; so sánh đáp ứng tốc độ và góc lắc khi dùng các thuật toán hạn chế rung động. |
| **`R9-08`** | `SM2693.pdf` | **Zhixiong Shen et al.** (Sensors and Materials, Tokyo — 2021) | • **Tên bài báo:** "Anti-sway Control of Crane System with Flexible Wire Rope and Vision Feedback", Sensors and Materials, Vol. 33, No. 9 (2021) 3333–3344.<br>• **Nội dung:** Đo góc lắc bằng camera công nghiệp (thị giác máy) và áp dụng giải thuật điều khiển mờ (Fuzzy Control) để khử lắc cho xe con cầu trục. |
| **`R9-09`** | `A54.pdf` | **Stanimir Valtchev** (IEEE — 2024) | • **Tên bài báo:** "Increasing the Damping Capacity of Crane Electric Drive Systems When Moving Cargo with a Flexible Suspension", Kỷ yếu hội nghị IEEE 2024.<br>• **Nội dung:** Nghiên cứu thuật toán điều khiển thích nghi cho biến tần để tăng khả năng cản dịu dao động cơ học của tải treo cáp mềm. |
| **`R9-10`** | `Shevchenko_bakalavr.pdf` | **Yana Oleksandrivna Shevchenko** (ĐH Bách khoa Kiev — KPI, Ukraine — 06/2024) | • **Đề tài:** "Система автоматичного керування електроприводом мостового крана складського комплексу" (Hệ thống điều khiển tự động TĐĐ cầu trục kho bãi), Thuyết minh 79 trang.<br>• **Thông số:** Tải nâng $7.6\text{ tấn}$, tự trọng xe con $3.0\text{ tấn}$, dầm cầu $18\text{ tấn}$, vận tốc xe con $0.9\text{ m/s}$, gia tốc $0.25\text{ m/s}^2$.<br>• **Công thức cản lăn kinh điển (tr. 15):** Suất lực cản $w_0 = \frac{2f + \mu \cdot d_{ts}}{D_k} \cdot k_p$ với cánh tay đòn cản lăn thép/thép $f = 0.0005\text{ m}$, ma sát ổ lăn $\mu = 0.015$, đường kính bánh xe $D_k = 0.6\text{ m}$, hệ số gờ bánh $k_p = 2.0 \div 2.5$. Suất cản lăn chỉ khoảng **$0.007 \div 0.010\text{ N/N}$** ($0.7\% \div 1.0\%$ trọng lượng)!<br>• **Hệ truyền động:** Động cơ không đồng bộ 3 pha chế độ $S3 - 25\%$, biến tần ABB ACS380 điều khiển vector FOC, có điện trở xả hãm, mô phỏng Simulink. |
| **`R9-11`** | `Bản sao của [NHOM 2] Thiết kế truyền động xe con cầu trục 2.pptx.pdf` | **Nhóm 2 sinh viên ĐHBK Hà Nội** (2023) | • **Nội dung:** Slide báo cáo đồ án thiết kế xe con cầu trục dầm đôi: Chọn cấu trúc biến tần - IM, tính phụ tải, mô phỏng Simulink. |
| **`R9-12`** | `Case_study.docx` | **Nhóm tác giả nội bộ** (2024) | • **Nội dung:** Báo cáo phân tích định hướng thiết kế hệ truyền động xe con cầu trục $12.2\text{ tấn}$, giải thích cơ chế dẫn động riêng 2 cụm động cơ bánh xe, điều kiện chống trượt bánh xe $F_{\text{kéo}} \le \varphi \cdot G_{\text{bánh chủ động}}$. |
| **`R9-13`** | `Dynamic crane trolley.pdf` | — | • **Tình trạng:** File gồm 46 trang nhưng bảng mã font nhúng bị lỗi (CID corrupted), không trích xuất văn bản tự động được; xếp loại tài liệu dự phòng không dùng làm căn cứ chính thức. |

---

## 7. MỤC "KHÔNG TÌM THẤY TRONG HỆ THỐNG" (UNVERIFIED / MISSING SOURCES)

Qua rà soát toàn bộ thư mục gốc `Project` và đối chiếu với các nguồn PRD bản cũ đang viện dẫn, các tài liệu sau **HOÀN TOÀN KHÔNG CÓ TRONG THƯ MỤC DỰ ÁN**:

1. **Catalogue Sungdo / KG-Cranes (Hàn Quốc):** PRD cũ dẫn link tìm kiếm google `anthinhcorp.com.vn` và `tongkhocautruc.com` để lấy tự trọng xe con $1,820\text{ kg} \div 2,030\text{ kg}$. Trong ROOT không có catalogue gốc này. *(Đề xuất: Chuyển $m_{xc} = 1,800\text{ kg}$ thành [C] Giả định kỹ thuật của nhóm hoặc đối chiếu với catalogue Demag EZDR).*
2. **Tài liệu Yuantai / Konecranes Full VFD Dual-Speed Crane:** PRD cũ dẫn link tìm kiếm google `eotcranekit.com` và `konecranes.com` để lấy công suất $1.1 \div 2.2\text{ kW}$. Trong ROOT không có brochure này. *(Đề xuất: Căn cứ vào công thức tính công suất cơ cấu của TCVN 4244 hoặc slide Bài 4 Thầy Đỉnh).*
3. **File `TOM_TAT_TAI_LIEU.md`:** PRD dòng 59 viện dẫn *"Căn cứ Mục 2 của TOM_TAT_TAI_LIEU.md"*. File này hoàn toàn không tồn tại trong thư mục `Block 0` cũng như toàn bộ `Project`.
4. **Tiêu chuẩn EN IEC 61800-5-3:2023:** PRD dòng 53 trích dẫn link có mã UUID trùng hệt với IEC 61800-5-2 (`9d2e-4771-9e3e-06aa795de80d`). Không có tài liệu này trong ROOT.
5. **Bài viết Industrial Monitor Direct:** PRD dòng 111 dẫn link tìm kiếm google `industrialmonitordirect.com` về chống lắc 3 tấn. Không có file trong ROOT (đây là blog thương mại ngoài mạng).
6. **Bài viết ICIE Panca Budi:** PRD dòng 47 & 105 dẫn link bài báo về hư hỏng nhiệt động cơ cầu trục. Không có trong ROOT.

---
**KẾT THÚC BÁO CÁO CHỈ MỤC NGUỒN PHA 1.**  
*Tài liệu này là căn cứ duy nhất để thực hiện kiểm toán Claim Audit tại Pha 2.*
