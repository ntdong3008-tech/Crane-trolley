# CẨM NANG XÂY DỰNG SRS BASELINE A THEO CHUẨN ISO/IEC/IEEE 29148
**Dự án áp dụng:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Xe Con Cầu Trục ($x = 2$)  
**Nhóm thực hiện:** 8.5-EMG | **Phụ trách chính:** Nguyễn Hải Trung (*Doc Lead*) & Nghiêm Trọng Đông (*SE Lead*)  
**Tiêu chuẩn áp dụng:** ISO/IEC/IEEE 29148, *NASA Systems Engineering Handbook* (Mục 4.2 & Phụ lục C), `EVLEP003_HBK` (§5.2)

---

## 1. VAI TRÒ CỦA SRS BASELINE A TẠI KHỐI 1 & CỔNG SRR-EVT

Trong lưu đồ `EVLEP003_HBK`, tại **Khối 1 (EVT — Yêu cầu hệ thống — §5.2)**, tài liệu **SRS (System Requirements Specification — Baseline A)** đóng vai trò là **Functional Baseline** của toàn dự án:
* **Đầu vào bắt buộc:** Bản **PRD đã khóa (Frozen)**, **Sơ đồ biên (Boundary Diagram)** và **P-Diagram** (chốt sơ bộ CTQ/CTS).
* **Nhiệm vụ cốt lõi:** Dịch toàn bộ mong đợi của khách hàng trong PRD thành **18 câu lệnh kỹ thuật định lượng (`Shall statements`)** có thể đo lường và kiểm chứng được.
* **Cổng kiểm soát:** **Cổng SRR-EVT (SE Lead)** xét duyệt câu hỏi: *"Yêu cầu đã đủ & đo được chưa? $\to$ Đóng băng SRS"*. Nếu thiếu ngưỡng định lượng hoặc đứt gãy truy xuất, hồ sơ bị trả về theo nhánh `KHÔNG ĐẠT — sửa SRS / RTM`.

---

## 2. QUY CHUẨN VIẾT YÊU CẦU THEO TIÊU CHUẨN ISO/IEC/IEEE 29148

### A. 9 Thuộc tính của một Câu Yêu cầu Đơn lẻ Chuẩn (Individual Requirement Attributes)
Theo **ISO/IEC/IEEE 29148**, mỗi câu lệnh trong SRS Baseline A phải thỏa mãn đồng thời 9 tiêu chí:

1. **Necessary (Cần thiết):** Nếu bỏ yêu cầu này đi, hệ thống sẽ không thỏa mãn được PRD hoặc vi phạm tiêu chuẩn $TCVN\ 4244:2005$.
2. **Implementation-Free / Abstract (Độc lập giải pháp chi tiết):** Nêu **WHAT** (hệ thống phải đạt chỉ tiêu gì), không áp đặt **HOW** (cách lập trình hay chọn linh kiện chi tiết ở cấp thấp), trừ các ràng buộc kiến trúc cấp hệ thống đã chốt tại MCR.
3. **Unambiguous (Không mơ hồ):** Chỉ có duy nhất một cách hiểu. Tuyệt đối cấm các tính từ/trạng từ định tính như *"ổn định"*, *"nhanh"*, *"an toàn"*, *"chính xác cao"*, *"xấp xỉ"* mà không có con số đi kèm.
4. **Consistent (Nhất quán):** Không mâu thuẫn với các câu SRS khác; dùng đồng nhất ký hiệu toán học ($Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg}$, $v_{\max} = 0.12\text{ m/s}$, $a_{\max} \le 0.5\text{ m/s}^2$, $\rho_{\max} \le 2\text{ m/s}^3$).
5. **Complete (Hoàn chỉnh):** Câu lệnh tự chứa đủ thông tin về điều kiện biên, giá trị mục tiêu và **dung sai (Tolerance)** mà không cần đọc đoán thêm.
6. **Singular / Atomic (Đơn nghĩa / Nguyên tử):** Mỗi mã SRS chỉ chứa **một yêu cầu duy nhất** (một chủ ngữ, một vị ngữ `phải / shall`). Không dùng từ nối *"và/hoặc"* để ghép nhiều chỉ tiêu kỹ thuật vào cùng một câu.
7. **Feasible (Khả thi):** Có thể thực hiện được bằng công nghệ truyền động Động cơ KĐB 3 pha + Biến tần FOC + Encoder trong giới hạn vật lý của nhà xưởng.
8. **Traceable (Truy xuất được):** Có mã định danh duy nhất và liên kết ngược về ít nhất một mã `PRD-xx` hoặc giải trình rõ là yêu cầu phái sinh (*Derived Requirement*).
9. **Verifiable (Kiểm chứng được):** Có thể chứng minh tính tuân thủ thông qua ít nhất 1 trong 4 phương pháp: **Analysis (A)**, **Simulation/Test (S/T)**, **Inspection (I)**, hoặc **Demonstration (D)**.

### B. 5 Thuộc tính của Toàn bộ Tập hợp SRS (Set of Requirements Attributes)
Khi ghép cả 18 câu yêu cầu lại với nhau, tập SRS Baseline A phải đạt:
* **Complete (Đầy đủ độ phủ):** Bao quát 100% các kịch bản vận hành (ConOps), các giao diện qua biên (Boundary) và các yếu tố nhiễu ($N_1 \div N_5$ trong P-Diagram).
* **Consistent (Đồng bộ nội tại):** Không có hai câu yêu cầu nào xung đột nhau (ví dụ: thời gian dừng khẩn cấp $\le 2\text{ s}$ phải tương thích vật lý với giới hạn gia tốc hãm khẩn cấp).
* **Affordable / Bounded (Phù hợp nguồn lực):** Nằm trong phạm vi tính toán và mô phỏng MATLAB/Simulink của nhóm 6 thành viên.

### C. Cấu trúc Cú pháp Câu lệnh Mẫu (IEEE 29148 Requirement Boilerplate)
Mọi câu lệnh trong SRS của nhóm 8.5-EMG đều được viết theo công thức chuẩn hóa:

$$[\text{Điều kiện vận hành / Trạng thái}] + [\text{Chủ thể hệ thống/phân hệ}] + \mathbf{\text{PHẢI (SHALL)}} + [\text{Hành động / Chức năng}] + [\text{Đối tượng}] + [\text{Ngưỡng định lượng} \pm \text{Dung sai}]$$

* **Ví dụ áp dụng chuẩn IEEE 29148 cho đề $x=2$:**
  > *"Khi vận hành ở chế độ xác lập với tải trọng trong dải từ không tải ($Q = 0\text{ kg}, m_{nh} = 222\text{ kg}$) đến đầy tải định mức ($Q = 12,222\text{ kg}, m_{nh} = 222\text{ kg}$), **Hệ truyền động xe con phải** duy trì vận tốc di chuyển dài ở mức $0.12\text{ m/s}$ với sai số xác lập tĩnh $e_{xl} \le 5\%$."*

---

## 3. KHUNG PHÂN LOẠI 5 NHÓM YÊU CẦU SRS BASELINE A (18 YÊU CẦU CỦA NHÓM 8.5-EMG)

Dựa trên Mục 3 trong `TOM_TAT_TAI_LIEU.md`, bộ 18 yêu cầu kỹ thuật của hệ truyền động xe con cầu trục ($x=2$) được tổ chức thành 5 nhóm:

| Nhóm yêu cầu | Dải mã số | Nội dung kỹ thuật trọng tâm | Thành viên nhận phân bổ thiết kế |
| :--- | :---: | :--- | :--- |
| **1. Chức năng & Động học**<br>*(Functional Requirements)* | **`SRS-F01` $\div$ `SRS-F08`** | Khả năng mang tải $Q = 12,222\text{ kg}$, khối lượng cơ cấu nâng $m_{nh} = 222\text{ kg}$; vận tốc tối đa $v_{\max} = 0.12\text{ m/s}$; giới hạn gia tốc $a_{\max} \le 0.5\text{ m/s}^2$; giới hạn độ giật $\rho_{\max} \le 2\text{ m/s}^3$; làm việc 4 góc phần tư; khởi động/dừng theo quỹ đạo mềm S-Curve. | Đặng Nguyên Bình (*PE-Hardware*) & Nguyễn Bá Hưng (*PE-Logic*) |
| **2. Logic & Chuyển trạng thái**<br>*(Logical & Mode Requirements)* | **`SRS-L01` $\div$ `SRS-L03`** | Máy trạng thái hữu hạn (`Ready`, `Run Forward`, `Run Reverse`, `Braking`, `Fault`); khóa chéo (Interlock) chống kích trùng lệnh Tiến/Lùi; trình tự phối hợp nhả/đóng phanh cơ điện từ với mô-men từ hóa của biến tần. | Nguyễn Bá Hưng (*PE-Logic*) |
| **3. An toàn & Bảo vệ**<br>*(Safety Requirements)* | **`SRS-S01` $\div$ `SRS-S04`** | Dừng khẩn cấp (E-Stop) hoàn toàn trong thời gian $\le 2\text{ s}$; ngắt chuyển động khi chạm công tắc hành trình giới hạn (Limit Switch); mạch Chopper và điện trở xả hãm $R_h$ khống chế điện áp DC-bus khi hãm tái sinh tải $12,222\text{ kg}$; bảo vệ quá dòng/mất pha. | Đặng Nguyên Bình (*PE-Hardware*) & Nguyễn Bá Hưng (*PE-Logic*) |
| **4. Hiệu năng Điều khiển**<br>*(Performance Requirements)* | **`SRS-P01` $\div$ `SRS-P03`** | Cấu trúc điều khiển Vector tựa từ thông (FOC vòng kín + Encoder); mạch vòng dòng điện ($i_d, i_q$ - Tối ưu Module) và mạch vòng tốc độ ($\omega$ - Tối ưu Đối xứng) đảm bảo độ quá điều chỉnh tốc độ $\sigma\% \le 10\%$, sai số xác lập $e_{xl} \le 5\%$ và kháng nhiễu lắc tải ở chiều cao cáp $h = 12\text{ m}$. | Trần Đỗ Khải (*PE-Control loop*) |
| **5. Môi trường, Nguồn & Giao diện**<br>*(Environmental & Interface)* | **`SRS-E01` $\div$ `SRS-E04`** | Vận hành ổn định dưới lưới điện 3 pha $380\text{V}/50\text{Hz}$ biến thiên $\pm 10\%$ ($342\text{V} \div 418\text{V}$); đáp ứng chế độ nhiệt ngắn hạn lặp lại $S3$; làm việc tin cậy khi hệ số ma sát ray biến thiên $\mu \in [0.15; 0.25]$; tuân thủ tiêu chuẩn $TCVN\ 4244:2005$. | Đặng Nguyên Bình (*PE-Hardware*) & Trần Đỗ Khải (*PE-Control*) |

---

## 4. MẪU BẢNG ĐẶC TẢ CHI TIẾT YÊU CẦU TRONG SRS (METADATA TABLE)

Theo **Bảng 4.2-2 (Requirements Metadata)** trong *NASA SE Handbook* và chuẩn **IEEE 29148**, mỗi câu yêu cầu trong SRS phải được trình bày kèm đầy đủ các trường thuộc tính (Metadata) như mẫu chuẩn dưới đây:

| Mã SRS | Nguồn (Parent ID) | Nội dung Yêu cầu Kỹ thuật (`Shall Statement`) | Lý giải Kỹ thuật & Giả định (Rationale) | Chỉ tiêu CTQ / Ngưỡng đo | Phương pháp V&V | Chủ sở hữu (Owner) |
| :---: | :---: | :--- | :--- | :--- | :---: | :---: |
| **`SRS-F01`** | `PRD-01` | Hệ truyền động điện xe con **phải** tạo ra lực kéo và mô-men điện từ đủ để di chuyển tải trọng nâng định mức $Q = 12,222\text{ kg}$ cùng cơ cấu nâng hạ $m_{nh} = 222\text{ kg}$. | Đảm bảo khả năng mang tải đúng thông số đề bài gốc với $x = 2$ mà không bị quá tải cơ-nhiệt. | $Q = 12,222\text{ kg}$<br>$m_{nh} = 222\text{ kg}$ | **A + S** | Đặng Nguyên Bình |
| **`SRS-F02`** | `PRD-02` | Khi nhận lệnh đặt tốc độ tối đa, Hệ truyền động xe con **phải** đạt vận tốc dài xác lập $v_{\max} = 0.12\text{ m/s}$ theo cả hai chiều Tiến và Lùi. | Tương đương $7.2\text{ m/phút}$, phù hợp dải vận tốc xe con cầu trục công nghiệp tải trên $10\text{ tấn}$. | $v_{\max} = 0.12\text{ m/s}$ | **S** | Trần Đỗ Khải |
| **`SRS-F03`** | `PRD-03` | Trong mọi quá trình khởi động, tăng tốc, giảm tốc và đảo chiều bình thường, Hệ truyền động xe con **phải** giới hạn gia tốc dài cực đại ở mức $\|a(t)\| \le 0.5\text{ m/s}^2$. | Chống trượt trơn bánh xe trên ray ($\mu = 0.15 \div 0.25$) và hạn chế biên độ góc lắc cáp ở chiều cao $h = 12\text{ m}$. | $\|a\|_{\max} \le 0.5\text{ m/s}^2$ | **S** | Nguyễn Bá Hưng & Trần Đỗ Khải |
| **`SRS-F04`** | `PRD-04` | Bộ tạo quỹ đạo đặt tốc độ của hệ thống **phải** giới hạn độ giật cực đại ở mức $\|\rho(t)\| = \|\text{d}a/\text{d}t\| \le 2\text{ m/s}^3$. | Làm mềm đạo hàm gia tốc bằng đường cong S-Curve để triệt tiêu xung lực cơ khí lên hộp giảm tốc và dầm cầu. | $\|\rho\|_{\max} \le 2\text{ m/s}^3$ | **S** | Nguyễn Bá Hưng |
| **`SRS-S01`** | `PRD-06` | Khi tín hiệu dừng khẩn cấp (`E-Stop`) được kích hoạt ở vận tốc $v_{\max} = 0.12\text{ m/s}$, Hệ truyền động **phải** đưa vận tốc xe con về $0\text{ m/s}$ trong thời gian $t_{stop} \le 2.0\text{ s}$. | Đảm bảo an toàn tính mạng và thiết bị trong tình huống khẩn cấp theo quy phạm $TCVN\ 4244:2005$. | $t_{stop} \le 2.0\text{ s}$ | **S + D** | Nguyễn Bá Hưng & Đặng Nguyên Bình |
| **`SRS-P01`** | `PRD-05`<br>*(Derived)* | Mạch vòng điều chỉnh tốc độ ($\omega$) **phải** đảm bảo độ quá điều chỉnh (Overshoot) $\sigma\% \le 10\%$ và sai số tốc độ xác lập tĩnh $e_{xl} \le 5\%$ khi tải biến thiên từ $0\text{ kg}$ đến $12,222\text{ kg}$. | Yêu cầu phái sinh từ cấu trúc FOC vòng kín tổng hợp theo chuẩn Tối ưu Đối xứng để kháng nhiễu tải lớn. | $\sigma\% \le 10\%$<br>$e_{xl} \le 5\%$ | **S** | Trần Đỗ Khải |

---

## 5. CHECKLIST SOÁT XÉT ĐÓNG BĂNG SRS TẠI CỔNG SRR-EVT

Trước khi **Nghiêm Trọng Đông (SE Lead)** ký biên bản **ĐẠT** tại Cổng `SRR-EVT`, bản SRS Baseline A phải vượt qua 8 câu hỏi kiểm tra sau:

1. **Đã khóa PRD chưa?** Bản PRD có trạng thái `Frozen` trước thời điểm đóng băng SRS hay chưa?
2. **Đúng số liệu $x = 2$ chưa?** Các con số $Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg}$, $h = 12\text{ m}$, $v_{\max} = 0.12\text{ m/s}$, $a \le 0.5\text{ m/s}^2$, $\rho \le 2\text{ m/s}^3$ đã chính xác tuyệt đối chưa (không làm tròn $12,000\text{ kg}$)?
3. **100% câu lệnh có từ khóa `phải (shall)` và con số đo được chưa?** Có còn câu nào viết chung chung không thể kiểm chứng trên MATLAB/Simulink không?
4. **Đảm bảo tính Nguyên tử (Singular) chưa?** Mỗi mã `SRS-xx` đã tách riêng thành 1 yêu cầu đơn lẻ để dễ chấm Pass/Fail độc lập chưa?
5. **Đã bao phủ hết 5 yếu tố nhiễu ($N_1 \div N_5$) từ P-Diagram chưa?** Các điều kiện biên về tải ($0 \div 12,222\text{ kg}$), ma sát ($\mu = 0.15 \div 0.25$), lưới điện ($380\text{V} \pm 10\%$), nhiệt độ chế độ $S3$ và chiều dài cáp $h = 12\text{ m}$ đã được đưa vào điều kiện kiểm tra của SRS chưa?
6. **Mọi câu SRS đều có cột Lý giải (Rationale) rõ ràng chưa?**
7. **Mọi câu SRS đều được gán Phương pháp kiểm chứng (A / S / I / D) chưa?**
8. **Truy xuất $100\%$ sang PRD và RTM chưa?** Không có yêu cầu mồ côi (Orphan) nào thiếu giải trình `Derived`.