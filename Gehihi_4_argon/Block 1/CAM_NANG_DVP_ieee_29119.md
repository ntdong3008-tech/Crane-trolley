# CẨM NANG LẬP DVP&R L0 THEO CHUẨN QUỐC TẾ ISO/IEC/IEEE 29119
**Dự án áp dụng:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Xe Con Cầu Trục ($x = 2$)  
**Nhóm thực hiện:** 8.5-EMG | **Phụ trách chính:** Phạm Văn Hưng (*QE-Simulation*) & Nghiêm Trọng Đông (*SE Lead*)  
**Tiêu chuẩn áp dụng:** ISO/IEC/IEEE 29119 (Parts 1–4), *NASA Systems Engineering Handbook* (Mục 5.3 & Phụ lục D), `EVLEP003_HBK`

---

## 1. BẢN CHẤT CỦA DVP&R L0 TRONG LUỒNG DỰ ÁN `EVLEP003_HBK`

**DVP&R L0 (Design Verification Plan & Report — Level 0)** là tài liệu Kế hoạch và Báo cáo Kiểm chứng Thiết kế ở **Cấp Hệ thống (System Level - Level 0)**:
* **Tại sao gọi là Level 0 (L0)?** Ở **Khối 1 (§5.2)**, hệ thống truyền động xe con được nhìn như một thể thống nhất để kiểm chứng 18 yêu cầu đầu ra cấp hệ thống trong SRS Baseline A (như vận tốc dài $v$, gia tốc $a$, độ giật $\rho$, thời gian dừng E-Stop). Khi sang **Khối 3 (§5.4 - Thiết kế chi tiết)**, DVP&R mới được hạ xuống cấp phân hệ (**L1, L2** — kiểm chứng riêng từng mạch vòng dòng điện $i_d, i_q$, khâu biến đổi Park/Clarke, mạch xả $R_h$).
* **Chu trình sống của DVP&R qua các Cổng kỹ thuật:**
  1. **Khối 1 $\to$ Cổng SRR-EVT:** Lập nửa **"DVP" (Design Verification Plan)** — xác định phương pháp, kịch bản, điều kiện biên và tiêu chí Pass/Fail cho 100% yêu cầu SRS.
  2. **Khối 4 $\to$ Cổng TRR-EVT (QE Lead):** Chuẩn bị mô hình MATLAB/Simulink, kiểm tra cấu hình 14 tham số động cơ và các khối đo (Scope / To Workspace) để cấp quyền bắt đầu đo kiểm.
  3. **Khối 5 $\to$ Cổng SIR-EVT & SAR-EVT:** Chạy mô phỏng theo đúng kịch bản DVP, trích xuất đồ thị và điền số liệu thực tế vào nửa **"&R" (Report)** để kết luận `PASS / FAIL`.

---

## 2. ÁP DỤNG TIÊU CHUẨN ISO/IEC/IEEE 29119 VÀO THIẾT KẾ DVP&R L0

Bộ tiêu chuẩn **ISO/IEC/IEEE 29119** cung cấp khung phương pháp luận kiểm thử chặt chẽ giúp **Phạm Văn Hưng (QE-Simulation)** thiết kế bảng DVP&R L0 chuẩn công nghiệp:

### A. Cấu trúc Tài liệu Kiểm thử theo IEEE 29119-3 (Test Documentation)
Một kế hoạch và báo cáo kiểm chứng chuẩn IEEE 29119-3 phải định nghĩa rõ:
1. **Test Item (Đối tượng kiểm thử):** Hệ truyền động điện cơ cấu xe con cầu trục (Bản tính toán thiết kế mạch lực và Mô hình mô phỏng tổng thể trên MATLAB/Simulink).
2. **Features to be Tested (Các đặc tính cần kiểm thử):** Toàn bộ 18 yêu cầu trong SRS Baseline A (`F01-F08`, `L01-L03`, `S01-S04`, `P01-P03`, `E01-E04`), tập trung vào các chỉ tiêu CTQ.
3. **Features Not to be Tested (Đặc tính ngoài phạm vi kiểm thử):** Độ bền mỏi kết cấu thép dầm cầu trục, truyền động cơ cấu nâng hạ ($h = 12\text{ m}$), hệ thống chống lắc chủ động bằng camera (*Out-of-Scope* trên Boundary Diagram).
4. **Gate Entry & Exit Criteria (Tiêu chí Vào / Ra cổng kiểm thử):**
   * *Entry Criteria (Tại Cổng TRR-EVT):* Đã đóng băng thiết kế chi tiết tại CDR-EVT; đầy đủ 14 tham số động cơ KĐB, tham số PI dòng điện ($i_d, i_q$), PI tốc độ ($\omega$), bộ tạo quỹ đạo S-Curve và sơ đồ logic trạng thái; mô hình Simulink chạy không báo lỗi đại số (Algebraic loop / Singularity).
   * *Exit Criteria (Tại Cổng SIR-EVT / SAR-EVT):* $100\%$ các bài kiểm thử trong DVP&R L0 được thực thi; $100\%$ chỉ tiêu CTQ đạt `PASS`; không còn báo cáo lỗi không phù hợp (NCR) trọng yếu nào chưa đóng.

### B. Kỹ thuật Thiết kế Kịch bản Kiểm thử theo IEEE 29119-4 (Test Techniques)
Thay vì chỉ chạy mô phỏng ở một điều kiện danh định lý tưởng, IEEE 29119-4 yêu cầu áp dụng 3 kỹ thuật thiết kế ca kiểm thử để "ép tải" hệ thống:

1. **Equivalence Partitioning & Boundary Value Analysis (Phân vùng tương đương & Phân tích giá trị biên):**
   Đặt mô hình chạy ngay tại các điểm biên khắc nghiệt nhất (Worst-Case) lấy từ 5 yếu tố nhiễu của P-Diagram:
   * **Biên tải trọng ($N_1$):** Kiểm thử tại **Biên dưới (Không tải):** $Q = 0\text{ kg}, m_{nh} = 222\text{ kg}$ (dễ vọt lố tốc độ nhất do quán tính nhỏ) và **Biên trên (Đầy tải định mức):** $Q = 12,222\text{ kg}, m_{nh} = 222\text{ kg}$ (dễ sụt tốc độ, quá dòng và quá áp DC-bus khi hãm nhất).
   * **Biên hệ số ma sát ray ($N_3$):** Kiểm thử tại $\mu_{\min} = 0.15$ (ray trơn, dễ trượt bánh xe khi gia tốc lớn) và $\mu_{\max} = 0.25$ (ray khô/bẩn, lực cản tĩnh $F_c$ cực đại).
   * **Biên điện áp lưới ($N_4$):** Kiểm thử tại $U_{\min} = 380\text{V} - 10\% = 342\text{V}$ và $U_{\max} = 380\text{V} + 10\% = 418\text{V}$.

2. **State Transition Testing (Kiểm thử chuyển trạng thái):**
   Kiểm thử toàn bộ các nhánh chuyển đổi hợp lệ và bất hợp lệ trên sơ đồ logic của Nguyễn Bá Hưng:
   * Chu trình chuẩn 4 góc phần tư: `Ready` $\to$ `Tăng tốc Tiến (Góc I)` $\to$ `Chạy xác lập 0.12 m/s` $\to$ `Hãm tái sinh Tiến (Góc II)` $\to$ `Đảo chiều Tăng tốc Lùi (Góc III)` $\to$ `Hãm tái sinh Lùi (Góc IV)` $\to$ `Stop`.
   * Chu trình cắt ngang khẩn cấp: Đang chạy ở $v = 0.12\text{ m/s}$ $\to$ Tác động xung `E-Stop = 1` hoặc `Limit_Switch = 1` $\to$ Chuyển ngay về trạng thái hãm cưỡng bức / ngắt lệnh theo chiều tương ứng.

3. **Fault Injection / Negative Testing (Kiểm thử tiêm lỗi / Nhiễu đột biến):**
   Đóng/cắt tải bước nhảy hoặc giả lập nhiễu mô-men lắc tải tuần hoàn từ cáp treo dài $h = 12\text{ m}$ tác động vào trục quy đổi để đánh giá khả năng kháng nhiễu của bộ điều khiển PI Tối ưu Đối xứng.

---

## 3. BỐN PHƯƠNG PHÁP KIỂM CHỨNG CHUẨN SE (VERIFICATION METHODS)

Theo *NASA SE Handbook* (Mục 5.3.1.2 & Phụ lục D), mỗi dòng trong DVP&R L0 phải chỉ định rõ phương pháp kiểm chứng:

| Ký hiệu | Phương pháp | Định nghĩa & Cách áp dụng trong dự án Xe con cầu trục ($x = 2$) |
| :---: | :--- | :--- |
| **`A`** | **Analysis**<br>*(Phân tích / Tính toán)* | Kiểm chứng bằng công thức lý thuyết, tính toán giải tích và bảng tính kỹ thuật (tính lực cản $F_c$, công suất tĩnh, kiểm nghiệm quá tải mô-men, chọn điện trở xả $R_h$, tính tham số PI). |
| **`S` / `T`** | **Simulation / Test**<br>*(Mô phỏng định lượng)* | Thực thi kịch bản thời gian thực trên mô hình **MATLAB/Simulink**, trích xuất dữ liệu số từ Scope/Workspace để đo chính xác $v_{\max}, a_{\max}, \rho_{\max}, \sigma\%, e_{xl}, t_{stop}$. |
| **`I`** | **Inspection**<br>*(Kiểm tra hồ sơ / Bản vẽ)* | Soát xét trực tiếp bảng BOM, Datasheet động cơ/biến tần, sơ đồ nguyên lý mạch lực 3 pha $380\text{V}$ và cấu hình khối Simulink xem có khớp tiêu chuẩn $TCVN\ 4244:2005$ không. |
| **`D`** | **Demonstration**<br>*(Trình diễn hành vi)* | Chạy thử nghiệm định tính để chứng minh hệ thống chuyển trạng thái logic đúng quy định (khóa chéo Tiến/Lùi, ngắt khi chạm hành trình). |

---

## 4. CẤU TRÚC BẢNG DVP&R L0 MẪU (THEO CHUẨN IEEE 29119-3 & NASA TABLE D-1)

Mỗi ca kiểm thử trong bảng DVP&R L0 phải tách bạch rõ **Điều kiện tiên quyết (Preconditions)**, **Tác động đầu vào (Test Actions)**, **Tiêu chí Đạt định lượng (Expected Results)** và **Kết quả đo thực tế (Actual Report)**:

| Mã Test (`DVP-ID`) | Truy xuất (`SRS-ID`) | Phương pháp | Điều kiện biên & Kịch bản kiểm thử (Preconditions & Test Actions - IEEE 29119) | Tiêu chí Nghiệm thu Đạt (Acceptance Criteria / Target) | Phụ trách (Thiết kế $\to$ QE) | Kết quả thực tế & Đánh giá (Report - Điền ở Khối 5) |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- |
| **`DVP-L0-01`** | `SRS-F01`<br>`SRS-E02` | **A + S** | **Điều kiện:** Đầy tải $Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg}$, ma sát biên trên $\mu = 0.25$, chế độ $S3$.<br>**Hành động:** Tính công suất tĩnh/động; chạy mô phỏng chu trình đầy tải liên tục. | $P_{đm\_motor} \ge P_{yc}$; Mô-men điện từ $M_đ$ đáp ứng đủ $M_{qđ}$ mà dòng stato không vượt ngưỡng cắt bảo vệ quá tải. | Đ.N. Bình $\to$ P.V. Hưng | *Số liệu:* $P_{đm} = \dots\text{ kW}$<br>*Đánh giá:* `[PASS / FAIL]` |
| **`DVP-L0-02`** | `SRS-F02`<br>`SRS-P02` | **S** | **Điều kiện:** Chạy ở 2 biên tải ($Q = 0\text{ kg}$ và $Q = 12,222\text{ kg}$), lưới $380\text{V} \pm 10\%$.<br>**Hành động:** Đặt lệnh vận tốc $v_{ref} = \pm 0.12\text{ m/s}$ (Tiến và Lùi). | Vận tốc dài xác lập đạt $v_{xl} \in [0.114; 0.126]\text{ m/s}$ (tương ứng sai số xác lập tĩnh $e_{xl} \le 5\%$). | T.Đ. Khải $\to$ P.V. Hưng | *Số liệu:* $e_{xl} = \dots\%$<br>*Đánh giá:* `[PASS / FAIL]` |
| **`DVP-L0-03`** | `SRS-F03` | **S** | **Điều kiện:** Đầy tải $Q = 12,222\text{ kg}$ và Không tải $Q = 0\text{ kg}$, cáp $h = 12\text{ m}$.<br>**Hành động:** Tăng tốc từ $0 \to 0.12\text{ m/s}$ và đảo chiều từ $+0.12 \to -0.12\text{ m/s}$. | Giá trị đỉnh tuyệt đối của gia tốc dài trong toàn chu trình bình thường: $\max(\|a(t)\|) \le 0.50\text{ m/s}^2$. | N.B. Hưng & T.Đ. Khải $\to$ P.V. Hưng | *Số liệu:* $a_{\max} = \dots\text{ m/s}^2$<br>*Đánh giá:* `[PASS / FAIL]` |
| **`DVP-L0-04`** | `SRS-F04` | **S** | **Điều kiện:** Kích hoạt khối S-Curve ở mọi điểm chuyển tiếp gia tốc.<br>**Hành động:** Đo đạo hàm bậc nhất của gia tốc $\rho(t) = \text{d}a/\text{d}t$ trên Simulink. | Giá trị đỉnh tuyệt đối của độ giật trong toàn chu trình: $\max(\|\rho(t)\|) \le 2.00\text{ m/s}^3$. | N.B. Hưng $\to$ P.V. Hưng | *Số liệu:* $\rho_{\max} = \dots\text{ m/s}^3$<br>*Đánh giá:* `[PASS / FAIL]` |
| **`DVP-L0-05`** | `SRS-P01` | **S** | **Điều kiện:** Chạy không tải ($Q = 0\text{ kg}, m_{nh} = 222\text{ kg}, \mu = 0.15$) và đóng tải định mức $Q = 12,222\text{ kg}$.<br>**Hành động:** Đo đáp ứng quá độ tốc độ $\omega(t)$ và $v(t)$. | Độ quá điều chỉnh tốc độ cực đại: $\sigma\% = \frac{v_{\text{peak}} - v_{xl}}{v_{xl}} \times 100\% \le 10.0\%$. | T.Đ. Khải $\to$ P.V. Hưng | *Số liệu:* $\sigma\% = \dots\%$<br>*Đánh giá:* `[PASS / FAIL]` |
| **`DVP-L0-06`** | `SRS-S01` | **S + D** | **Điều kiện:** Xe con đang di chuyển ở $v = 0.12\text{ m/s}$ mang tải cực đại $Q = 12,222\text{ kg} + m_{nh} = 222\text{ kg}$.<br>**Hành động:** Kích xung `E-Stop = 1` tại $t = t_0$. | Khoảng thời gian từ $t_0$ đến khi vận tốc xe con về $v = 0\text{ m/s}$ hoàn toàn: $\Delta t_{stop} \le 2.00\text{ s}$. | N.B. Hưng & Đ.N. Bình $\to$ P.V. Hưng | *Số liệu:* $t_{stop} = \dots\text{ s}$<br>*Đánh giá:* `[PASS / FAIL]` |
| **`DVP-L0-07`** | `SRS-S03` | **A + S** | **Điều kiện:** Hãm tái sinh và đảo chiều khi mang tải $Q = 12,222\text{ kg}$ (Góc phần tư II và IV).<br>**Hành động:** Quan sát điện áp DC-bus và dòng qua điện trở xả $R_h$. | Mạch Chopper kích dẫn đúng ngưỡng; điện áp DC-bus được kẹp trong vùng an toàn của biến tần, không báo lỗi Overvoltage. | Đ.N. Bình $\to$ P.V. Hưng | *Số liệu:* $U_{dc\_\max} = \dots\text{ V}$<br>*Đánh giá:* `[PASS / FAIL]` |

---

## 5. NGUYÊN TẮC KIỂM SOÁT ĐỘC LẬP CỦA QE-SIMULATION (PHẠM VĂN HƯNG)

1. **Tách biệt người thiết kế và người nghiệm thu:** Các thành viên thiết kế (Bình, B.Hưng, Khải) bàn giao thông số và khối chức năng, nhưng **Phạm Văn Hưng (QE-Simulation)** là người độc lập thiết lập kịch bản test biên trên Simulink và trích xuất số liệu vào cột Report.
2. **Không sửa tiêu chí Pass/Fail để "ép" kết quả Đạt:** Nếu kết quả mô phỏng cho thấy $a_{\max} = 0.62\text{ m/s}^2 > 0.5\text{ m/s}^2$, QE phải đánh dấu `FAIL` (mở NCR tại Khối 5) để nhóm điều khiển/logic tinh chỉnh lại độ dốc S-Curve hoặc bộ PI, tuyệt đối không tự ý nới ngưỡng trong DVP&R.
3. **Lưu trữ bằng chứng khách quan (Objective Evidence):** Mỗi dòng kết luận `PASS` trong DVP&R L0 phải chỉ rõ tham chiếu đến **Hình ảnh đồ thị Scope số mấy** hoặc **Bảng tính mục nào** trong thuyết minh đồ án.