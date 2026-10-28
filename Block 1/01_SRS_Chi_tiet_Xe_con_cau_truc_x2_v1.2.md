# BÁO CÁO ĐẶC TẢ YÊU CẦU KỸ THUẬT HỆ THỐNG (SRS BASELINE A), SƠ ĐỒ RANH GIỚI (BOUNDARY DIAGRAM), SƠ ĐỒ THAM SỐ (P-DIAGRAM), MA TRẬN TRUY XUẤT RTM & DVP&R L0 (KHỐI 1 — EVT)

**Tên đề tài:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Di Chuyển Ngang Xe Con Cầu Trục ($x = 2$)  
**Mã tài liệu:** `SRS-8.5EMG-TROLLEY-v1.3` *(tên tệp giữ hậu tố v1.2)* | **Trạng thái:** `Baseline A — Frozen (Đồng bộ hóa 100% với Frozen Baseline A tại Block 1)`  
**Hạng mục công việc:** `WBS 1.0 (SOW-1.1, SOW-1.2, SOW-1.3 — Khối 1: Yêu cầu Hệ thống)`  
**Đường cơ sở đóng băng đối chiếu (SSoT):** [SRS Baseline A (Frozen)](file:///D:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Tiền%20khả%20thi/Block%201/01_SRS_Baseline_A.md) và [Bảng thông số gốc SSoT](file:///D:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Tiền%20khả%20thi/Block%201/00_Bang_thong_so_goc.md)  
**Bộ 3 Tài liệu Khối 0 Đầu vào Đã Khóa (`Frozen` tại Cổng `MCR`):**  
1. **PRD:** `PRD-8.5EMG-TROLLEY-v3.1 (Frozen)` — Tài liệu Yêu cầu Sản phẩm (`prd_xe_con_cau_truc_x2_nhom_8_5_emg.md`)  
2. **SOW:** `SOW-8.5EMG-TROLLEY-v1.1 (Completed / Frozen)` — Bản Tuyên bố & Phạm vi Công việc (`sow_xe_con_cau_truc_x2_nhom_8_5_emg.md`)  
3. **BCA / QFD / HoQ / ICE:** `BCA-QFD-8.5EMG-TROLLEY-v1.1 (Completed / Frozen)` — Báo cáo Khảo sát Case Study, Tech Gap, QFD/HoQ & Chốt `Solution C` (`bao_cao_case_study_qfd_hoq_ice_xe_con_x2_nhom_8_5_emg.md`)  

**Nhóm thực hiện:** Nhóm 8.5-EMG (Đề $x = 2$ — STT 22: Nghiêm Trọng Đông)  
**Phân công trách nhiệm (`R / A` theo SOW Khối 1):**  
* `SOW-1.1` (*Boundary Diagram & P-Diagram*): **R / A:** Nghiêm Trọng Đông (*PM / SE Lead*)  
* `SOW-1.2` (*Biên soạn & Đóng băng SRS Baseline A*): **R:** Nguyễn Hải Trung (*Doc Lead*) phối hợp Đặng Nguyên Bình (*PE-HW*), Trần Đỗ Khải (*PE-Control*), Nguyễn Bá Hưng (*PE-Logic*) | **A:** Nghiêm Trọng Đông (*SE Lead*)  
* `SOW-1.3` (*Lập Ma trận RTM & Kế hoạch kiểm chứng DVP&R L0*): **R:** Phạm Văn Hưng (*QE-Simulation*) & Nguyễn Hải Trung (*Doc Lead*) | **A:** Nghiêm Trọng Đông (*SE Lead*)  

**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Chuẩn tham chiếu:** Tiêu chuẩn Quốc tế ISO/IEC/IEEE 29148:2018 (*Systems and software engineering — Life cycle processes — Requirements engineering*), [R2, NASA SP-2007-6105 Rev1 §4.2, Table 6.7-5 & Phụ lục C, D], Quy trình Kỹ thuật Hệ thống `EVLEP003_HBK` (v1.8.2 — §5.2), [B, IEC 61800-2:1998], [B, IEC 60034-1] & [R1, TCVN 4244:2005]

### Lịch sử Phiên bản Tài liệu (Revision History)

| Phiên bản | Ngày cập nhật | Người thực hiện | Tóm tắt nội dung thay đổi chính |
| :---: | :---: | :--- | :--- |
| `v1.0` | 18/10/2026 | Nguyễn Hải Trung, Nghiêm Trọng Đông | Bản dự thảo SRS Baseline A ban đầu đệ trình Cổng SRR-EVT. |
| `v1.1` | 22/10/2026 | Nhóm 8.5-EMG | Cập nhật đồng bộ theo `PRD v3.1`, `SOW v1.1`, `BCA-QFD v1.1`; sửa triệt để lỗi vật lý: phân định suất cản lăn riêng $w_0 = 0.015$ (1.5%) [R1, §2.4.7.2.2] (trị số $w_0 = 0.015$ là giả định `[C]`) và hệ số bám dính ray thép $\varphi = 0.20$ [R5, Bài 4, tr.43]; bổ sung cột phân loại nguồn [A]/[B]/[C] và danh mục tài liệu tham khảo [1]..[10]. |
| `v1.2` | 24/10/2026 | Nhóm 8.5-EMG | **Đồng bộ hóa 100% với tài liệu SRS Baseline A đã đóng băng (`Tiền khả thi/Block 1/01_SRS_Baseline_A.md`) và `03_RTM_DVP.md`:**<br>1. Chuẩn hóa cấu trúc SRS Baseline A về đúng **8 yêu cầu kỹ thuật hệ thống chốt (`4 FUNC + 4 PERM`)**, thiết lập ánh xạ 1-1 trực tiếp với 8 yêu cầu cam kết từ `PRD v3.1` (`PRD-FUNC-01..04`, `PRD-PERM-01..04`).<br>2. Bổ sung Mục 4: **Bảng phân bổ thông số chuyển xuống các khối thiết kế chi tiết (*Downstream Design Allocation*)**, chính thức chuyển giao 8 thông số chi tiết ($M_p \le 10\%$, $e_{xl} \le 5\%$, $U_{\text{dc}} \le 780\text{V}$, Chopper $700\text{ V}$, $\Delta t_{\text{torque}} \le 10\text{ ms}$, $M_{\text{hold}}$ và ngưỡng $|v| \le 0.002 / 0.005\text{ m/s}$, $F_{\max} = 9.25\pm 0.45\text{ kN}$, $\lambda_{\max} \ge 2.0$, tốc độ bò) xuống Khối 2 và Khối 3 nhằm tuân thủ nguyên tắc *WHAT, not HOW* của ISO/IEC/IEEE 29148:2018 và NASA SE Handbook.<br>3. Chuẩn hóa toàn bộ số liệu SSoT theo `Block 1/00_Bang_thong_so_goc.md`: lực cản tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ (P-20), lực kéo cực đại $F_{\max} = 9,218\text{ N} \approx 9.22\text{ kN}$, hệ số an toàn bám $k_{\text{bám}} = 1.52 \ge 1.20$, hiệu suất truyền động cơ khí $\eta = 0.90$ (P-15).<br>4. Đồng bộ Ma trận RTM và Kế hoạch DVP&R L0 sang cấu trúc 8 bài đo (`DV-01` đến `DV-08` / `DVP-L0-01..08`), loại bỏ bài đo trùng lặp và phân công WBS rõ ràng. |
| `v1.3` | 26/10/2026 | Nhóm A duyệt | Tích hợp SRS Baseline A.1 đã ký: `SRS-PERM-04` và DV-08 dùng $k_{dt} \ge 1.20$ (CR-01), tiêu chí FAIL của DV-08 theo CR-02; $F_{\max}$ = 9.22 kN (dải [8.80; 9.70] kN giữ nguyên); §5.4 sửa công thức $a(t)$ sang mô hình 2 khối lượng (SDD v1.3 §2.1, hệ quả của thay đổi nhóm C ngày 26/10/2026). |
| `v1.4` | 28/10/2026 | Nhóm duyệt | Chốt phạm vi môn học (CR-08..CR-12): bỏ dung sai số liệu đầu vào (trừ $v_{\max}$ ±5%, lưới ±10%) và cận dưới gia tốc/độ giật; góc lắc chỉ quan sát; `SRS-PERM-04`, DV-08 tính $k_{dt}$ ở lưới danh định (CR-13); Downstream #3, #6 bỏ dung sai (CR-16, CR-17). |


## 1. LUỒNG PHƯƠNG PHÁP LUẬN CHUYỂN HÓA TỪ KHỐI 0 SANG KHỐI 1 (`WBS 1.0`)

### 1.1. Vai trò của Hồ sơ Khối 1 và Ranh giới Phạm vi Cam kết (`FUNC` & `PERM`)

Theo lưu đồ dự án 6 Khối – 7 Cổng trong `FLOW_REVIEW.md` (quy trình `EVLEP003_HBK` v1.8.2, §5.2) và [R2, NASA SP-2007-6105 Rev1 §4.2, Table 6.7-5, tr. 174], sau khi Nhóm 8.5-EMG hoàn thành Khối 0 (`Pre-A`) và vượt qua Cổng 1 (`MCR`) với quyết định chốt **Solution C (`Động cơ KĐB 3 pha chế độ S3 + Biến tần điều khiển Vector FOC + Encoder vòng kín đo thực tế + Bộ tạo quỹ đạo S-Curve 7 đoạn + Braking Chopper & Điện trở xả hãm Rh`)**, nhóm bước vào **Khối 1 (`EVT — Yêu cầu Hệ thống`)** để thiết lập **Đường cơ sở Kỹ thuật Cấp Hệ thống (`SRS Baseline A`)** trình duyệt qua **Cổng 2 (`SRR-EVT`)**.

Tuân thủ nghiêm ngặt chiến lược **Giới hạn phạm vi (*Scope Tailoring*)** đã thống nhất với Giảng viên hướng dẫn (TS. Nguyễn Duy Đỉnh) và khóa cứng tại Mục 1.1, Mục 1.2, Mục 1.3 (`SOW-1.1` $\to$ `SOW-1.3`) của `SOW-8.5EMG-TROLLEY-v1.1`:
* **Phạm vi thực hiện trong `SRS Baseline A` (*In-Scope*):** Chuyển hóa chính thức **2 nhóm yêu cầu cốt lõi của PRD** là **Nhóm 1 — Yêu cầu Chức năng Vận hành (`PRD-FUNC-01` $\to$ `PRD-FUNC-04`)** và **Nhóm 2 — Yêu cầu Hiệu năng Định lượng (`PRD-PERM-01` $\to$ `PRD-PERM-04`)** cùng **8 Đặc tính Kỹ thuật Hệ thống (`EC-01` $\to$ `EC-08`)** từ Ngôi nhà Chất lượng (`HoQ` trong `BCA-QFD-8.5EMG-TROLLEY-v1.1`).
* **Phạm vi loại trừ tuyệt đối khỏi `SRS Baseline A` (*Out-of-Scope*):** Không đưa 4 nhóm yêu cầu còn lại của PRD (`PRD-SAFE-01..04`, `PRD-INTF-01..03`, `PRD-ENVI-01..02`, `PRD-RELI-01..02`) vào danh mục yêu cầu kỹ thuật của `SRS Baseline A`, `RTM` và `DVP&R L0` (chỉ coi là ràng buộc biên thiết kế và điều kiện tiêu chuẩn nhà xưởng).

### 1.2. Giải thích Chi tiết Cơ sở Phân rã từ `8 Mã PRD` + `8 Mã EC (HoQ)` sang `8 Mã Yêu cầu Kỹ thuật Hệ thống SRS Baseline A` (Chuẩn 1-1 & Downstream Allocation)

Một vấn đề phương pháp luận cốt lõi tại Cổng `SRR-EVT` là: **Mối quan hệ ánh xạ giữa 8 mã yêu cầu khách hàng (`PRD-FUNC-01..04` và `PRD-PERM-01..04`), 8 Đặc tính Kỹ thuật (`EC-01..08` của HoQ) và 8 mã yêu cầu kỹ thuật hệ thống (`SRS-FUNC-01..04` và `SRS-PERM-01..04`) được thiết lập như thế nào?**

Trong giai đoạn dự thảo sơ bộ, nhóm từng cân nhắc phương án tách `PRD-PERM-02` thành 2 mã để cô lập chỉ tiêu độ quá điều chỉnh $M_p \le 10\%$. Tuy nhiên, khi đối chiếu nghiêm ngặt với chuẩn mực Kỹ thuật Hệ thống quốc tế **ISO/IEC/IEEE 29148:2018 (Mục 5.2.5)** và **NASA Systems Engineering Handbook (NASA SP-2007-6105 Rev1, Appendix C & D)**, Hội đồng kỹ thuật đã thống nhất **đóng băng SRS Baseline A ở đúng 8 mã yêu cầu hệ thống chốt (`4 FUNC + 4 PERM`) ánh xạ 1-1 với 8 mã PRD**, dựa trên 3 nguyên tắc nền tảng:

1. **Nguyên tắc "WHAT, not HOW" và Chống Quá Chi tiết hóa sớm (*Avoid Over-specification / Design Prejudgment*):**
   * Theo NASA SE Handbook (§4.2, p.41), tài liệu SRS cấp hệ thống ở giai đoạn SRR chỉ quy định hệ thống **phải làm được gì (*WHAT*)**, không được định trước các giải pháp cài đặt chi tiết của linh kiện hay tham số thuật toán nội bộ (*HOW*).
   * Ví dụ: Ngưỡng điện áp hãm $U_{\text{dc}} \le 780\text{V}$ hay ngưỡng chopper $700\text{ V}$ phụ thuộc trực tiếp vào dòng biến tần thương mại thực tế mà nhóm sẽ chọn ở Khối 2. Nếu áp cứng các con số này vào SRS cấp hệ thống sẽ vi phạm nguyên tắc thiết kế. Ở cấp SRS, hệ thống chỉ cần cam kết yêu cầu chức năng: *kích hoạt van xả hãm tiêu tán an toàn động năng hãm qua $R_h$ mà không gây ngắt quá áp khâu DC-link*.
2. **Phân bổ Chỉ tiêu Quá độ thành Mục tiêu Chỉnh định Bộ điều khiển (*Tuning Targets — Downstream Design Allocation*):**
   * Chỉ tiêu độ quá điều chỉnh $M_p \le 10.0\%$ và sai lệch xác lập tĩnh $e_{xl} \le 5.0\%$ thực chất là các mục tiêu tinh chỉnh chất lượng quá độ (*Tuning Targets*) của mạch vòng điều khiển kín tốc độ trên Simulink. Khi nhóm triển khai bộ tạo quỹ đạo S-curve 7 đoạn làm trơn lượng đặt ở Khối 3, tốc độ thực tế bám rất sát lượng đặt và độ vọt lố tự nhiên sẽ rất nhỏ; sai lệch tĩnh được triệt tiêu hoàn toàn nhờ khâu tích phân của bộ điều khiển PI.
   * Do đó, hai chỉ số này được tích hợp trọn vẹn trong dải dung sai vận tốc xác lập định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ của `SRS-PERM-02`, và được chuyển giao chính thức xuống **Khối 3 (`SOW-3.3`)** thành mục tiêu tối ưu đối xứng (*Symmetric Optimum*). Điều này giúp SRS Baseline A duy trì ánh xạ 1-1 hoàn hảo với `PRD-PERM-02`.
3. **Phân bổ Thông số Xuống Khối Thiết kế Chi tiết (*Allocation to Subsystems & Detail Design*):**
   * Toàn bộ 8 thông số chi tiết (vọt lố $M_p$, sai lệch tĩnh $e_{xl}$, ngưỡng điện áp DC-link, thời gian đáp ứng mô-men $\Delta t_{\text{torque}}$, mô-men giữ $M_{\text{hold}}$ và ngưỡng dừng, lực kéo đỉnh tăng tốc $F_{\max}$, hệ số quá tải $\lambda_{\max}$, cấp tốc độ bò) được quản lý minh bạch tại **Mục 4 — Bảng phân bổ thông số chuyển xuống các khối thiết kế chi tiết (Downstream Design Allocation)**, phân công rõ người nhận tại Khối 2 và Khối 3.

Bảng dưới đây giải trình tường minh phép ánh xạ 1-1 từ **8 mã `PRD v3.1` (`WHATs`) + 8 mã `EC` (`HOWs`)** sang **8 mã kỹ thuật hệ thống chốt của `SRS Baseline A` (`4 FUNC + 4 PERM`)**:

| Mã Yêu cầu Khách hàng (`PRD v3.1`) | Nội dung Gốc trong PRD (`WHATs`) | Các Đặc tính Kỹ thuật HoQ Tương ứng (`HOWs`) | Ánh xạ Mã SRS Baseline A (Đã Đóng băng) | Nội dung Kỹ thuật Hệ thống Chuẩn hóa (Kèm Dung sai Kỹ thuật & Căn cứ Phân bổ) | Loại nguồn |
| :---: | :--- | :--- | :---: | :--- | :---: |
| **`PRD-FUNC-01`** | Điều khiển xe con di chuyển 2 chiều (Tiến/Lùi) và làm việc đầy đủ trên cả 4 góc phần tư $(\omega, M)$. | • `EC-01` *(22.30%)*<br>• `EC-02` *(14.90%)*<br>• `EC-08` *(11.67%)* | **`SRS-FUNC-01`** | Vận hành hai chiều trên 4 góc phần tư I, II, III, IV và phản hồi Encoder vòng kín 0 cảm biến trên cáp treo. *(Chỉ tiêu $\Delta t_{\text{torque}} \le 10\text{ ms}$ chuyển giao sang Khối 3).* | `[B] [3, 6, 8]` |
| **`PRD-FUNC-04`** | Phối hợp đồng bộ phanh cơ điện từ với mô-men động cơ (mở khi đủ mô-men giữ; đóng khi xe dừng hẳn). | • `EC-03` *(8.19%)*<br>• `EC-01` *(22.30%)* | **`SRS-FUNC-02`** | Khóa chéo cấm đảo chiều khi $v \ne 0\text{ m/s}$ và đồng bộ đóng/mở phanh cơ điện từ, độ trôi dừng xe $\Delta s \le \pm 10\text{ mm}$ (danh định không trôi $\Delta s = 0\text{ mm}$). *(Ngưỡng $M_{\text{hold}}$ và $|v| \le 0.002 / 0.005\text{ m/s}$ chuyển giao sang FSM Khối 3).* | `[B] [2, 6]` |
| **`PRD-FUNC-02`** | Điều chỉnh tốc độ vô cấp và làm mềm quá trình tăng/giảm tốc liên tục từ $0\text{ m/s}$ đến $v_{\max} = 0.12\text{ m/s}$. | • `EC-04` *(11.32%)* | **`SRS-FUNC-03`** | Quy hoạch quỹ đạo tốc độ đặt liên tục theo đường cong S-Curve 7 đoạn khống chế gia tốc đặt $|a^*(t)| \le 0.50\text{ m/s}^2$ và độ giật đặt $|\rho^*(t)| \le 2.00\text{ m/s}^3$ (không có xung giật vô hạn). *(Đã chuyển giao tốc độ bò xuống Khối 3).* | `[B] [6, 9]` |
| **`PRD-FUNC-03`** | Hấp thụ và tiêu tán an toàn động năng hãm tái sinh trả về DC-Link (Góc II & IV). | • `EC-05` *(11.41%)* | **`SRS-FUNC-04`** | Tiêu tán năng lượng hãm tái sinh qua mạch van hãm (Braking Chopper) và điện trở xả hãm $R_h$ bảo vệ biến tần khỏi lỗi ngắt quá áp DC-link. *(Ngưỡng $780\text{V}$ và thông số $R_h$ chuyển giao sang Khối 2 & Khối 3).* | `[C] [6, 8]` |
| **`PRD-PERM-01`** | Sản sinh đủ lực kéo và mô-men truyền động để di chuyển ổn định xe con đầy tải ($14,244\text{ kg}$) và không tải ($2,022\text{ kg}$) với $w_0 = 0.015, \varphi = 0.20$. | • `EC-06` *(10.10%)*<br>• `EC-01` *(22.30%)* | **`SRS-PERM-01`** | Đáp ứng lực kéo, thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ (P-20) [B] (với $w_0 = 0.015$, $\eta = 0.90$) và đảm bảo hệ số an toàn bám chống trượt ray $k_{\text{bám}} \ge 1.20$ với $\varphi = 0.20$. *(Giá trị lực đỉnh $F_{\max} = 9.22\text{ kN}$ chuyển sang phần chọn động cơ Khối 2).* | `[A] [1] / [B] [2] / [C] [4, 5]` |
| **`PRD-PERM-02`** | Đạt vận tốc tối đa $v_{\max} = 0.12\text{ m/s}$ với sai lệch tốc độ xác lập $e_{xl} \le 5\%$ và độ quá điều chỉnh $M_p \le 10\%$. | • `EC-02` *(14.90%)*<br>• `EC-07` *(10.10%)*<br>• `EC-01` *(22.30%)* | **`SRS-PERM-02`** | Đạt vận tốc di chuyển ngang định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ ($[0.114;\ 0.126]\text{ m/s}$ hay $[6.84;\ 7.56]\text{ m/phút}$) theo cả hai chiều di chuyển. *(Các chỉ tiêu $M_p \le 10\%$ và $e_{xl} \le 5\%$ chuyển giao làm mục tiêu tinh chỉnh bộ PI ở Khối 3).* | `[A] [1] / [B] [3] / [C] [8]` |
| **`PRD-PERM-03`** | Giới hạn độ lớn gia tốc ngang $|a(t)| \le 0.5\text{ m/s}^2$ và độ lớn độ giật $|\rho(t)| \le 2.0\text{ m/s}^3$ với tải treo ở $h = 12\text{ m}$. | • `EC-04` *(11.32%)*<br>• `EC-08` *(11.67%)* | **`SRS-PERM-03`** | Khống chế đồng thời gia tốc ngang thực tế $|a(t)| \le 0.50\text{ m/s}^2$ (P-10) [A] và độ giật ngang thực tế $|\rho(t)| \le 2.00\text{ m/s}^3$ (P-11) [A] khi mang tải treo ở chiều cao cáp lớn nhất $h = 12.0\text{ m}$ (P-06) [A]. | `[A] [1] / [B] [2, 9]` |
| **`PRD-PERM-04`** | Đáp ứng chế độ làm việc ngắn hạn lặp lại $S3$ ($CD = 40\%$), hệ số dự trữ công suất $k_{dt} \ge 1.2$, nguồn 3 pha $380\text{V} \pm 10\% / 50\text{Hz}$. | • `EC-06` *(10.10%)* | **`SRS-PERM-04`** | Định cỡ công suất phát nhiệt chế độ $S3 - 40\%$ (P-17) [C] đạt hệ số dự trữ phát nhiệt $k_{dt} \ge 1.20$ ở lưới danh định $380\text{V} / 50\text{Hz}$ mà không bị quá nhiệt cuộn dây. *(Chỉ tiêu quá tải $\lambda_{\max} \ge 2.0$ chuyển giao đối chiếu catalogue Khối 2).* | `[B] [3] / [C] [8]` |
| **TỔNG CỘNG** | **8 Mã Yêu cầu PRD (`4 FUNC + 4 PERM`)** | **8 Mã Kỹ thuật HoQ (`EC-01..08`)** | **Ánh xạ 1–1 Hoàn hảo** | **8 Mã Kỹ thuật Hệ thống (`4 FUNC + 4 PERM`)** | **Đạt độ phủ 100% phạm vi SOW, bảo toàn nguyên tắc WHAT-not-HOW, 8 bài đo kiểm chứng DVP&R L0 Pass/Fail tuyệt đối.** | `[A] [1] / [B] [2, 3] / [C] [4..9]` |

> ### 📌 Chú dẫn Nguồn gốc Yêu cầu & Viện dẫn Tài liệu Tham khảo (Citations for Client Review)
> - **Ký hiệu Phân loại Nội bộ Nhóm Kỹ thuật Hệ thống (`Internal SE Classification`):**
>   - **`[A]` — Nguồn Đề bài / Khách hàng:** Giá trị và chỉ tiêu kỹ thuật bất biến giao trực tiếp từ đề bài gốc $x = 2$ (STT 22, ĐHBK Hà Nội).
>   - **`[B]` — Nguồn Tiêu chuẩn Kỹ thuật:** Tiêu chuẩn Quốc gia (TCVN), Tiêu chuẩn Quốc tế (IEC, ISO/IEEE) và quy chuẩn ngành bắt buộc tuân thủ.
>   - **`[C]` — Nguồn Giả định Kỹ thuật & Khảo sát:** Dữ liệu tính toán giải tích nội bộ của Nhóm 8.5-EMG, bài giảng chuyên khảo và thông số kiểm chứng từ Catalogue nhà sản xuất (Demag, Sungdo).
> - **Danh mục Viện dẫn Tài liệu Tham khảo Chuẩn hóa Quốc tế (Chi tiết tại Mục 7):**
>   - **`[1]`**: Đề bài tập lớn môn Thiết kế Hệ TĐĐ Kỳ 2023.1 — Đề số 8: Xe con cầu trục ($x = 2$, STT 22), Bộ môn TĐĐ, ĐHBK Hà Nội [R3].
>   - **`[2]`**: TCVN 4244:2005 — Thiết bị nâng: Thiết kế, chế tạo và kiểm tra kỹ thuật, Bộ Khoa học và Công nghệ [R1].
>   - **`[3]`**: IEC 61800-2:1998, IEC 60034-1, ISO/IEC/IEEE 29148:2018 — Tiêu chuẩn biến tần, động cơ điện & đặc tả yêu cầu hệ thống [B].
>   - **`[4]`**: TS. Nguyễn Duy Đỉnh, Tài liệu Bài giảng Thiết kế Hệ Truyền động Điện (Bài 4, tr. 43: $\varphi = 0.20$) & Tiêu chuẩn TĐĐ [R4, R5].
>   - **`[5]`**: Không có tài liệu — $D_{bx} = 0.25\text{ m}$, $w_0 = 0.015$ là giả định nhóm `[C]` (mã `[R9-10]` đã gỡ).
>   - **`[6]`**: Demag Cranes & Components, catalogue *Demag DR rope hoists*, ấn phẩm 213 133 44 [R9-07].
>   - **`[7]`**: Catalogue pa lăng cáp dầm đôi KG-Cranes / Sungdo [R9-08] (không có tệp trong kho; $m_{xc} = 1,800\text{ kg}$ là giả định `[C]`).
>   - **`[8]`**: Я. О. Шевченко (Y. O. Shevchenko) (2024), đồ án cử nhân *Hệ điều khiển tự động truyền động điện cầu trục kho hàng*, KPI Igor Sikorsky [R9-06].
>   - **`[9]`**: T. Mita & T. Kanai (1979) `[R9-01]`; Ho Duc Tho et al. (2020) `[R9-11]` — mô hình con lắc tải và quỹ đạo S-curve.
>   - **`[10]`**: NASA SP-2007-6105 Rev1 — Systems Engineering Handbook, NASA Headquarters, Washington, D.C. [R2].


## 2. SƠ ĐỒ RANH GIỚI HỆ THỐNG (BOUNDARY DIAGRAM) & SƠ ĐỒ THAM SỐ (P-DIAGRAM) (`SOW-1.1`)

Thực hiện gói công việc **`SOW-1.1`** do **Nghiêm Trọng Đông (*PM / SE Lead*)** chủ trì, phần này trình bày **Sơ đồ Ranh giới Hệ thống (*System Boundary Diagram*)** và **Sơ đồ Tham số (*Parameter Diagram — P-Diagram*)**, kèm theo thuyết minh chi tiết về **cơ sở phương pháp luận và nguồn tài liệu gốc** dùng để xây dựng từng phần tử trên hai sơ đồ.

### 2.1. Sơ đồ Ranh giới Hệ thống (System Boundary Diagram) và Cơ sở Nguồn Thiết lập

#### A. Cơ sở Phương pháp luận và Nguồn Tài liệu Dùng để Vẽ Sơ đồ Biên (*Why & From Where*)
1. **Khung Phương pháp luận Kỹ thuật Hệ thống (NASA SE & IEEE):**
* Căn cứ **Mục 4.2 (*Technical Requirements Definition*) và Phụ lục C, Phụ lục D** của [R2, NASA SP-2007-6105 Rev1 tr. 41–45 & tr. 279] cùng **Khối 1 (§5.2)** của quy trình `EVLEP003_HBK` trong `FLOW_REVIEW.md`: Để viết được các câu yêu cầu kỹ thuật hệ thống (`SRS`) không bị thiếu giao diện và không bị tràn sang hệ thống khác, bước đầu tiên bắt buộc là khoanh vùng **Ranh giới Hệ thống (*System Boundary*)** bằng đường nét đứt hoặc khung bao, chỉ rõ các thực thể bên ngoài (*External Entities*), các phân hệ bên trong (*Internal Subsystems*) và các luồng Năng lượng – Cơ học – Tín hiệu cắt qua biên.
2. **Tiêu chuẩn Kiến trúc Phân tầng Hệ Truyền động Điện Quốc tế:**
* Căn cứ **Hình 1 & Mục 4 (*System Architecture of a Power Drive System — PDS*)** của tiêu chuẩn quốc tế [B, IEC 61800-2:1998] và [B, IEC 61800-1] (đã được nhóm chuẩn hóa tại Mục 8.1 của báo cáo `BCA-QFD-8.5EMG-TROLLEY-v1.1`): Một hệ truyền động điện tiêu chuẩn công nghiệp được phân rã thành **Mô-đun truyền động hoàn chỉnh (`CDM` — gồm Biến tần `BDM`, Bộ điều khiển `CU`, Mạch hãm `Braking Chopper + Rh`)**, **Động cơ & Cảm biến (`Motor & Encoder`)** và **Thiết bị công tác được dẫn động (`Driven Equipment` — gồm Phanh cơ, Hộp giảm tốc, Bánh xe con)**.
3. **Phạm vi Cam kết Hợp đồng trong `SOW v1.1` (§1.1):**
* Hệ thống *In-Scope* của Nhóm 8.5-EMG gói gọn trong ranh giới truyền động xe con. Cơ cấu nâng hạ tải ($m_{nh} = 222\text{ kg}$), tải nâng ($Q = 12,222\text{ kg}$), kết cấu dầm chính và ray dầm cầu trục được xếp vào *Phụ tải ngoài tác động qua biên* (*Out-of-Scope Entity*).
4. **Nguồn Hồ sơ Học thuật & Catalogue Công nghiệp Thực tế (Case Studies `CS-01` $\to$ `CS-09`):**
* Chi tiết các khối phần tử bên trong và thông số giao diện qua biên được lấy trực tiếp từ: [R9-06, Shevchenko 2024] (cấu trúc RFOC + S-Curve + Braking Chopper $R_h$), [R9-07, Demag DR tr. 4 & tr. 8] (động cơ gắn sẵn Encoder xung, biến tần tích hợp điện trở xả hãm, phanh cơ điện từ thường đóng, hộp số 3 cấp $\eta = 0.90$, bánh xe $d = 0.25\text{ m}$), [R9-08, KG-Cranes] (tự trọng xe con $m_{xc} = 1,800\text{ kg}$, nguồn 3 pha $380\text{V} \pm 10\% / 50\text{Hz}$), [R9-09, Yuantai Crane] (chạy định mức $v_{\max} = 0.12\text{ m/s}$) và bài báo kinh điển [R9-01, Mita & Kanai 1979] (tương tác lực căng ngang của con lắc cáp treo chiều dài $h = 12\text{ m}$ lên xe con).

#### B. Sơ đồ Ranh giới Hệ thống (System Boundary Diagram — Chuẩn hóa theo `IEC 61800-2` & Phạm vi `FUNC + PERM`)

```text
╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                 SƠ ĐỒ RANH GIỚI HỆ THỐNG TRUYỀN ĐỘNG XE CON CẦU TRỤC                                ║
║                                  (SYSTEM BOUNDARY DIAGRAM — IEC 61800-2 & IEEE 29148)                               ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

   [THỰC THỂ NGOÀI 1: LƯỚI ĐIỆN HẠ THẾ]                 [THỰC THỂ NGOÀI 2: NGƯỜI VẬN HÀNH / PLC]
   ┌───────────────────────────────────┐                 ┌────────────────────────────────────┐
   │ 3 Pha AC 380V ± 10% / 50Hz        │                 │ Lệnh: Tiến / Lùi / Định mức / Dừng │
   │ [Nguồn: PRD Mục 3, Sungdo 15T]    │                 │ [Nguồn: PRD Mục 2.2, Demag DR]     │
   └─────────────────┬─────────────────┘                 └──────────────────┬─────────────────┘
                     │ [E1] Điện năng 3 pha                                 │ [I1] Lệnh điều khiển
                     │      (342V - 418V AC)                                │      (Tiến/Lùi/Dừng/0.12m/s)
                     ▼                                                      ▼
╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║ RANH GIỚI HỆ THỐNG TRUYỀN ĐỘNG XE CON (IN-SCOPE — NHÓM 8.5-EMG THIẾT KẾ & KIỂM CHỨNG)                              ║
║                                                                                                                     ║
║   ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐   ║
║   │ 1. PHÂN HỆ BIẾN TẦN & ĐIỀU KHIỂN (CDM — Complete Drive Module theo IEC 61800-2)                            │   ║
║   │                                                                                                             │   ║
║   │   ┌───────────────────────────┐      [E2] DC-Bus      ┌───────────────────────────┐                         │   ║
║   │   │ Khâu Chỉnh lưu Diode      │──────────────────────▶│ Khâu Nghịch lưu IGBT      │                         │   ║
║   │   │ + Tụ lọc DC-Link          │◀──────────────────────│ Điều chế Vector SVPWM     │                         │   ║
║   │   └─────────────┬─────────────┘      (Hãm tái sinh)   └─────────────┬─────────────┘                         │   ║
║   │                 │ [E3]                                              │ [E4] Điện áp 3 pha PWM                │   ║
║   │                 ▼                                                   │      U_uvw, f_uvw biến thiên          │   ║
║   │   ┌───────────────────────────┐                                     │                                       │   ║
║   │   │ Mạch Van Hãm & Điện trở Rh│                                     │                                       │   ║
║   │   │ (Braking Chopper + Rh)    │                                     │                                       │   ║
║   │   │ [Nguồn: CS-06, CS-07]     │                                     │                                       │   ║
║   │   └───────────────────────────┘                                     │                                       │   ║
║   │                                                                     ▼                                       │   ║
║   │   ┌─────────────────────────────────────────────────────────────────────────────────────────────────┐       │   ║
║   │   │ Khối Điều khiển Trung tâm (CU — Control Unit):                                                  │       │   ║
║   │   │  • Bộ tạo quỹ đạo S-Curve 7 đoạn (a* ≤ 0.5 m/s², ρ* ≤ 2.0 m/s³) [CS-01, CS-05]                  │       │   ║
║   │   │  • Thuật toán Vector RFOC tựa từ thông Rotor (Tách kênh isd, isq) [CS-06]                       │       │   ║
║   │   │  • Mạch vòng kép: PI dòng điện (MO) & PI tốc độ (SO) [CS-06]                                    │       │   ║
║   │   │  • Logic khóa chéo cấm đảo chiều khi v ≠ 0 & đồng bộ phanh cơ tại 0 rpm [CS-07, TCVN 4244]     │       │   ║
║   │   └───────────────────────────────────▲─────────────────────────────────────────────────────────────┘       │   ║
║   │                                       │ [I3] Phản hồi xung tốc độ A/B/Z (01 Pulse Encoder)                  │   ║
║   └───────────────────────────────────────┼─────────────────────────────────────────────────────────────────────┘   ║
║                                           │                                                                         ║
║   ┌───────────────────────────────────────┴─────────────────────────────────────────────────────────────────────┐   ║
║   │ 2. PHÂN HỆ ĐỘNG CƠ & CẢM BIẾN TRỤC (MOTOR & FEEDBACK UNIT)                                                  │   ║
║   │                                                                                                             │   ║
║   │   ┌────────────────────────────────────────────────────────┐       ┌────────────────────────────────────┐   │   ║
║   │   │ Động cơ KĐB 3 pha Rotor lồng sóc (S3 - 40%, IP54/IP55) │──────▶│ 01 Pulse Encoder gắn đuôi trục ĐC  │   │   ║
║   │   │ [Nguồn: IEC 60034-1, Demag DR tr.4, Sungdo 15T]        │       │ [Nguồn: Demag DR tr.4, CS-06]      │   │   ║
║   │   └───────────────────────────┬────────────────────────────┘       └────────────────────────────────────┘   │   ║
║   └───────────────────────────────┼─────────────────────────────────────────────────────────────────────────────┘   ║
║                                   │ [M1] Mô-men cơ học M_e(t), Tốc độ góc trục động cơ ω_m(t)                       ║
║                                   ▼                                                                                 ║
║   ┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────┐   ║
║   │ 3. PHÂN HỆ CƠ KHÍ & CHẤP HÀNH DI CHUYỂN (DRIVEN EQUIPMENT — MECHANICAL TRANSMISSION)                       │   ║
║   │                                                                                                             │   ║
║   │   ┌───────────────────────────┐      [M2] Trục        ┌───────────────────────────┐                         │   ║
║   │   │ Cụm Phanh Cơ Điện từ      │──────────────────────▶│ Hộp Giảm tốc Bánh răng trụ│                         │   ║
║   │   │ Thường đóng (Lò xo nén)   │      Mô-men hãm       │ 3 Cấp (Tỷ số truyền i=150)│                         │   ║
║   │   │ [Nguồn: TCVN 4244, Demag] │      M_phanh ≥ 1.1 Mđm│ (Hiệu suất η = 0.90)      │                         │   ║
║   │   └───────────────────────────┘                       └─────────────┬─────────────┘                         │   ║
║   │                                                                     │ [M3] Mô-men trục bánh xe M_bx, ω_bx   ║
║   │                                                                     ▼                                       │   ║
║   │                                                       ┌───────────────────────────┐                         │   ║
║   │                                                       │ Cụm 4 Bánh xe thép D=0.25m│                         │   ║
║   │                                                       │ (2 Bánh dẫn + 2 Bánh bị)  │                         │   ║
║   │                                                       │ Khung xe con m_xc=1,800kg │                         │   ║
║   │                                                       └─────────────┬─────────────┘                         │   ║
║   └─────────────────────────────────────────────────────────────────────┼───────────────────────────────────────┘   ║
╚═════════════════════════════════════════════════════════════════════════┼═════════════════════════════════════════════╝
                                                                          │ [M4] Lực kéo tiếp tuyến F_k(t)
                                                                          │      Phản lực cản lăn F_c(t)
                                                                          ▼
   [THỰC THỂ NGOÀI 3: RAY THÉP DẦM CHÍNH & TẢI TREO (OUT-OF-SCOPE)]
   ┌──────────────────────────────────────────────────────────────────────────────────────────────────────────┐
   │ • Ray dẫn hướng thép A54: Suất cản lăn w0 = 0.015, Hệ số bám ray thép khô φ = 0.20 [DIN 536, Thầy Đỉnh]  │
   │ • Lực cản lăn tĩnh đầy tải: F_c.đầy = 2,096 N (M_Σ = 14,244 kg = 12,222kg Q + 222kg m_nh + 1,800kg m_xc) │
   │ • Cụm móc nâng & Cáp dài h ≤ 12m: Gây dao động con lắc tự nhiên ω_p = √(g/h) ≈ 0.904 rad/s (Tp ≈ 6.95 s)  │
   └──────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

#### C. Bảng Truy xuất Nguồn Gốc Thiết lập Từng Khối và Giao diện trên Sơ đồ Biên (*Boundary Source Traceability*)

| Tên Khối / Giao diện Biên | Vị trí Phân định Phạm vi | Căn cứ Nguồn Trực tiếp (Tài liệu / Tiêu chuẩn) | Lý giải Kỹ thuật Hệ thống (*System Rationale*) |
| :--- | :---: | :--- | :--- |
| **1. Nguồn lưới 3 pha $380\text{V} \pm 10\% / 50\text{Hz}$ (`IF-PWR`)** | *External Entity* $\to$ *In-Boundary* | • `PRD v3.1` (Mục 3 — `ASM-04` & `PRD-PERM-04`)<br>• [R9-08, Sungdo Hoist] | Cung cấp năng lượng điện đầu vào với dải dao động điện áp $\pm 10\%$ ($342\text{V} \div 418\text{V AC}$) tác động lên thanh cái DC-Link của biến tần. |
| **2. Lệnh Vận hành Công nghệ (`IF-CMD`: Tiến, Lùi, Chạy định mức, Dừng)** | *External Entity* $\to$ *In-Boundary* | • `PRD v3.1` (Mục 2.2 ConOps & `PRD-FUNC-01`, `PRD-FUNC-02`)<br>• [R9-09, Yuantai Crane] | Xác định tập tín hiệu điều khiển đầu vào thuộc đúng phạm vi `FUNC` (đã lọc bỏ hoàn toàn các tín hiệu ngoài scope như `E-Stop` hay `Limit Switch` thuộc nhóm `SAFE`). |
| **3. Cơ cấu Nâng hạ ($m_{nh} = 222\text{ kg}$ `[A] [1]`), Tải nâng ($Q = 12,222\text{ kg}$ `[A] [1]`), Cáp ($h = 12\text{ m}$ `[A] [1]`) & Ray thép ($w_0 = 0.015$ `[C] [5]`, $\varphi = 0.20$ `[C] [4]`) (`IF-MECH-IN`)** | *Out-of-Scope Entity* tác động qua biên | • Đề bài gốc ($x = 2$, STT 22) `[A] [1]`<br>• [R1, TCVN 4244:2005 §1.3.3, §1.3.4, §1.3.7, tr. 4] `[B] [2]`<br>• [R1, §2.4.7.2.2] (trị số $w_0 = 0.015$ là giả định `[C]`) ($w_0 = 0.015$) `[C] [5]`<br>• [R5, Bài 4, tr.43] ($\varphi = 0.20$) `[C] [4]`<br>• [R9-01, Mita & Kanai 1979] `[B] [9]` | Theo `SOW v1.1` (Mục 1.1), nhóm không thiết kế tời nâng và dầm chính, nhưng khối lượng $Q + m_{nh} = 12,444\text{ kg}$ đè trực tiếp lên bánh xe con tạo lực cản tĩnh $F_{c.\text{đầy}} = 2,096\text{ N}$ (tính theo $w_0 = 0.015$ `[5]`), còn cáp $h = 12\text{ m}$ tạo dao động con lắc ($\omega_p \approx 0.904\text{ rad/s}$) truyền lực căng ngang qua biên vào xe con. Điều kiện chống trượt ray thép tuân theo $\varphi = 0.20$ `[4]`. |
| **4. Phân hệ Biến đổi Công suất & Điều khiển (`CDM`: Biến tần, Braking Chopper + $R_h$, Khối `CU`)** | *In-Boundary (In-Scope)* | • Tiêu chuẩn [B, IEC 61800-2:1998] (`BCA-QFD` Mục 8.1)<br>• [R9-06, Shevchenko 2024]<br>• [R9-07, Demag DR tr. 8] | Trái tim của **Solution C** đã chốt tại Cổng `MCR`: thực hiện điều khiển tách kênh từ thông – mô-men 4 góc phần tư, tạo quỹ đạo S-Curve 7 đoạn và băm xung xả năng lượng hãm tái sinh qua $R_h$. |
| **5. Phân hệ Chấp hành Điện – Cơ (Động cơ KĐB $S3$, Encoder xung, Phanh cơ, Hộp số $\eta = 0.90$, Bánh xe $d = 0.25\text{ m}$, Khung xe $m_{xc} = 1,800\text{ kg}$)** | *In-Boundary (In-Scope)* | • `PRD v3.1` (`ASM-01..04`)<br>• [R9-08, KG-Cranes 15T]<br>• [R9-07, Demag DR tr. 4] & [R9-02, Feto et al. 2025] | Chuyển hóa điện năng 3 pha PWM thành cơ năng kéo tổng khối lượng $M_\Sigma = 14,244\text{ kg}$ (đầy tải) hoặc $m_{\text{tĩnh}} = 2,022\text{ kg}$ (không tải) và gửi tín hiệu tốc độ thực tế $\omega(t)$ từ Encoder về khép kín vòng điều khiển. |

### 2.2. Sơ đồ Tham số Hệ thống (P-Diagram theo Six Sigma) và Cơ sở Nguồn Thiết lập

#### A. Cơ sở Phương pháp luận và Nguồn Tài liệu Dùng để Vẽ Sơ đồ P-Diagram (*Why & From Where*)
1. **Khung Phương pháp luận Six Sigma & NASA SE:**
* Căn cứ **Mục 3.2** của `tien_do_cap_nhat_khoi_0_mcr (1).md` và hướng dẫn Six Sigma DFSS (*Design for Six Sigma*): Sơ đồ Tham số (**P-Diagram**) là công cụ then chốt chuyển dịch từ Sơ đồ Biên sang các thông số toán học cụ thể, phân định rành mạch 5 thành phần: **Tín hiệu vào (*Signal Inputs*)**, **Yếu tố Nhiễu (*Noise Factors — N*)**, **Yếu tố Điều khiển (*Control Factors — CF*)**, **Đầu ra Mong muốn (*Ideal Outputs / CTQ*)** và **Trạng thái Lỗi (*Error States — E*)**.
2. **Nguồn Xác lập 4 Yếu tố Nhiễu (`N1` $\to$ `N4`):**
* `N1` (Biến thiên tải trọng): $2,022\text{ kg} \leftrightarrow 14,244\text{ kg}$ (gấp $7.04\text{ lần}$) — lấy từ `PRD-PERM-01`, `INP-01`, `INP-02`, `ASM-01` ([R9-08, KG-Cranes 15T]).
* `N2` (Dao động con lắc cáp treo): $h \le 12\text{ m}$, $\omega_p \approx 0.904\text{ rad/s}$, $T_p \approx 6.95\text{ s}$ — lấy từ `INP-03`, `PRD-PERM-03` và [R9-01, Mita & Kanai 1979].
* `N3` (Dao động điện áp lưới): $380\text{V} \pm 10\%$ ($342\text{V} \div 418\text{V AC}$) — lấy từ `ASM-04`, `PRD-PERM-04` và [R9-08, Sungdo Hoist].
* `N4` (Phát nhiệt cuộn dây chế độ $S3$): Làm trôi điện trở rotor $R_2$ — lấy từ [B, IEC 60034-1] và `BCA-QFD` Mục 8.4.
3. **Nguồn Xác lập 6 Yếu tố Điều khiển (`CF1` $\to$ `CF6`):**
* Lấy trực tiếp từ **8 Đặc tính Kỹ thuật `EC-01..08`** của HoQ (`BCA-QFD-8.5EMG-TROLLEY-v1.1`), cấu trúc 3 mạch vòng điều khiển của [R9-06, Shevchenko 2024] và **Sổ đăng ký rủi ro (`RRM-01..05`)**.

#### B. Sơ đồ Tham số Hệ thống (P-Diagram — Chuẩn hóa theo `tien_do_cap_nhat_khoi_0_mcr (1).md` Mục 3.2)

```text
╔═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                                  SƠ ĐỒ THAM SỐ HỆ THỐNG (PARAMETER DIAGRAM — P-DIAGRAM)                             ║
║                                        THEO PHƯƠNG PHÁP LUẬN SIX SIGMA & IEEE 29148                                ║
╚═════════════════════════════════════════════════════════════════════════════════════════════════════════════════════╝

                                        YẾU TỐ NHIỄU (NOISE FACTORS — N1..N4)
                                ┌───────────────────────────────────────────────────────────┐
                                │ • N1: Biến thiên tải trọng: m_tĩnh=2,022kg ↔ M_Σ=14,244kg │
                                │ • N2: Con lắc cáp h ≤ 12m (ω_p ≈ 0.904 rad/s, Tp ≈ 6.95s) │
                                │ • N3: Dao động lưới điện: 380V ± 10% (342V ÷ 418V AC)     │
                                │ • N4: Phát nhiệt cuộn dây S3 (CD=40%) làm trôi điện trở R2│
                                └─────────────────────────────┬─────────────────────────────┘
                                                              │
                                                              ▼
   TÍN HIỆU ĐẦU VÀO                     ┌───────────────────────────────────────────┐              ĐẦU RA MONG MUỐN
   (SIGNAL INPUTS — M)/LỆNH             │ HỆ TRUYỀN ĐỘNG DI CHUYỂN XE CON CẦU TRỤC  │              (IDEAL OUTPUTS — CTQ)
┌─────────────────────────────┐         │ (HỆ THỐNG CHUYỂN HÓA NĂNG LƯỢNG & TÍN HIỆU│         ┌─────────────────────────────┐
│ • Lệnh Tiến / Lùi           │────────▶│                                           │────────▶│ • CTQ-01: Vận hành 4Q ổn định│
│ • Vận tốc đặt: v* = 0.12 m/s│         │ • Động cơ KĐB 3 pha Rotor lồng sóc S3-40% │         │ • CTQ-02: v_max = 0.12 m/s  │
│ • Quỹ đạo tốc độ ω*(t)      │         │ • Biến tần FOC + Mạch hãm Chopper & Rh    │         │ • CTQ-03: Gia tốc a ≤ 0.5m/s²│
│ • Lệnh Dừng & Khóa phanh    │         │ • Hộp số 3 cấp (η=0.90) + 4 Bánh xe D=0.25│         │ • CTQ-04: Độ giật ρ ≤ 2.0m/s³│
└─────────────────────────────┘         └─────────────────────▲─────────────────────┘         │ • CTQ-05: k_bám ≥ 1.20      │
                                                              │                               │ • CTQ-06: U_dc an toàn qua Rh│
                                                              │                               │ • CTQ-07: Độ trôi Δs ≤ ±10mm │
                                                              │                               │ • CTQ-08: Nhiệt S3 kdt=1.2÷1.5
                                                              │                               └─────────────────────────────┘
                                                              │
                                ┌─────────────────────────────┴─────────────────────────────┐
                                │ • E1 (RRM-01): Lắc tải cáp mạnh / sốc cơ khí va đập hộp số │
                                │ • E2 (RRM-02): Quá áp DC-Link ngắt biến tần khi hãm tái sinh│
                                │ • E3 (RRM-03): Trượt quay bánh xe / trôi xe tự do khi phanh│
                                │ • E4 (RRM-04): Động cơ quá nhiệt cháy cuộn dây ở chế độ S3  │
                                └───────────────────────────────────────────────────────────┘
                                          TRẠNG THÁI LỖI CẦN TRIỆT TIÊU (ERROR STATES — E1..E4)

                                        YẾU TỐ ĐIỀU KHIỂN (CONTROL FACTORS — CF1..CF6)
                                ┌───────────────────────────────────────────────────────────┐
                                │ • CF1: Cấu trúc điều khiển Vector RFOC tựa từ thông Rotor │
                                │ • CF2: 01 Encoder xung gắn đồng trục phản hồi tốc độ vòng │
                                │ • CF3: Bộ tạo quỹ đạo S-Curve 7 đoạn khống chế a* và ρ*    │
                                │ • CF4: Mạch van hãm Braking Chopper xả động năng qua Rh   │
                                │ • CF5: Logic máy trạng thái khóa chéo v≠0 & đồng bộ phanh │
                                │ • CF6: Định cỡ công suất động cơ theo công suất đẳng trị S3│
                                └───────────────────────────────────────────────────────────┘
```

#### C. Bảng Giải trình Nguồn Gốc 5 Thành phần của P-Diagram và Ánh xạ sang Mã `SRS Baseline A`

| Khối Thành phần trong P-Diagram | Chi tiết Tham số Kỹ thuật | Nguồn Trích dẫn Trực tiếp (Tài liệu Khối 0 / Tiêu chuẩn / Case Study) | Ánh xạ sang Mã Yêu cầu Kỹ thuật (`SRS Baseline A`) |
| :--- | :--- | :--- | :---: |
| **1. Tín hiệu Đầu vào (*Input Signals*)** | Lệnh Tiến/Lùi, lệnh chạy định mức ($0.12\text{ m/s}$), lệnh dừng chu trình, quỹ đạo đặt $\omega^*(t)$. | • `tien_do_cap_nhat_khoi_0_mcr (1).md` (Mục 3.2 — `SOW-1.1`)<br>• `PRD v3.1` (Mục 2.2 ConOps & `PRD-FUNC-01`, `PRD-FUNC-02`)<br>• [R9-09, Yuantai Crane] | `SRS-FUNC-01` $\to$ `SRS-FUNC-03`, `SRS-PERM-02` |
| **2. Yếu tố Nhiễu (`N1` $\to$ `N4`)** | • `N1`: Tải thay đổi $2,022\text{ kg} \leftrightarrow 14,244\text{ kg}$.<br>• `N2`: Cáp treo $h \le 12\text{ m}$ ($\omega_p \approx 0.904\text{ rad/s}$).<br>• `N3`: Lưới $380\text{V} \pm 10\% / 50\text{Hz}$.<br>• `N4`: Nhiệt chu kỳ $S3$ ($CD = 40\%$) tăng $R_2$. | • `tien_do_cap_nhat_khoi_0_mcr (1).md` (Mục 3.2 — `SOW-1.1`)<br>• `PRD v3.1` (`INP-01..03`, `ASM-01..04`)<br>• [R9-01, Mita & Kanai 1979]; [B, IEC 60034-1] | Đưa trực tiếp vào vế `[Điều kiện vận hành / Trạng thái]` của `SRS-FUNC-01..04` và `SRS-PERM-01..04` |
| **3. Yếu tố Điều khiển (*Control Factors* `CF1` $\to$ `CF6`)** | Cấu trúc RFOC + Encoder, PI dòng điện (MO) & PI tốc độ (SO), bộ tạo S-Curve 7 đoạn ($a_{\max}, \rho_{\max}$), Braking Chopper + $R_h$, logic đồng bộ phanh tại $0\text{ rpm}$, định cỡ nhiệt $S3$. | • `BCA-QFD v1.1` (Mục 5.2 `EC-01..08` & Mục 8.2 Sơ đồ RFOC)<br>• [R9-06, Shevchenko 2024]<br>• [R9-11, S-Curve 2020] | `SRS-FUNC-01` $\to$ `SRS-FUNC-04` & Cột *Rationale* của `SRS-PERM-01..04` |
| **4. Đáp ứng Lý tưởng & Chỉ tiêu Trọng yếu (`CTQ-01` $\to$ `CTQ-08`)** | $v_{\max} = 0.12\text{ m/s} \pm 5\%$, $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$, $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$, $F_{c.\text{đầy}} = 2,096\text{ N}$, $k_{\text{bám}} \ge 1.20$, tiêu tán qua $R_h$ không quá áp, $\Delta s \le \pm 10\text{ mm}$, $k_{dt} \ge 1.20$ ở $S3 - 40\%$. | • `PRD v3.1` (Mục 3 `MOP-01..03`, `TPM-01..02` & Mục 4)<br>• `SOW v1.1` (Mục 2 `QCD-Q01..Q04`, `QCD-C01`)<br>• `BCA-QFD v1.1` (Mục 5.2 Giá trị đích `EC-01..08`) | Khoá cứng thành vế `[Ngưỡng định lượng ± Dung sai]` trong 8 câu lệnh `SRS Baseline A` |
| **5. Trạng thái Lỗi Cần Triệt tiêu (*Error States* `E1` $\to$ `E4`)** | Lắc tải mạnh / sốc cơ khí (`RRM-01`), quá áp DC-Link (`RRM-02`), trượt quay bánh xe / trôi tải khi mở phanh (`RRM-03`), quá nhiệt $S3$ hoặc dư công suất (`RRM-04`). | • `BCA-QFD v1.1` (Mục 4 `GAP-01..07` & Mục 8.4 Sổ đăng ký rủi ro `RRM-01..04`) | Dùng làm tiêu chí đánh trượt (*Fail Criteria*) trong bảng `DVP&R L0` cho 8 bài kiểm chứng |


## 3. ĐẶC TẢ YÊU CẦU KỸ THUẬT HỆ THỐNG — `SRS BASELINE A` (8 YÊU CẦU KỸ THUẬT HỆ THỐNG CHỐT: 4 FUNC + 4 PERM — `SOW-1.2`)

### 3.1. Công thức Cú pháp Câu lệnh Chuẩn ISO/IEC/IEEE 29148 & Quy định 8 Cột Metadata

Thực hiện gói công việc **`SOW-1.2`** do **Nguyễn Hải Trung (*Doc Lead*)** chủ trì phối hợp cùng **Đặng Nguyên Bình (*PE-HW*), Trần Đỗ Khải (*PE-Control*) và Nguyễn Bá Hưng (*PE-Logic*)**, toàn bộ 8 yêu cầu kỹ thuật trong `SRS Baseline A` đều được viết theo công thức cú pháp chuẩn của **ISO/IEC/IEEE 29148:2018**:

$$
\underbrace{[\text{Điều kiện vận hành / Trạng thái biên}]}_{\text{Condition / State}} + \underbrace{[\text{Chủ thể hệ thống / phân hệ}]}_{\text{Subject}} + \mathbf{\text{phải (shall)}} + \underbrace{[\text{Hành động / Chức năng}]}_{\text{Action}} + \underbrace{[\text{Đối tượng & Ngưỡng định lượng } \pm \text{ Dung sai}]}_{\text{Object & Measurable Target}}
$$

Mỗi câu lệnh trong Bảng 3.2 và Bảng 3.3 dưới đây được kiểm soát bằng **8 cột thuộc tính (*Requirements Metadata*)** theo chuẩn [R2, NASA SP-2007-6105 Rev1 Bảng 4.2-2, tr. 44]: (1) Mã `SRS ID`, (2) Truy xuất kép `PRD ID` & `HoQ EC ID`, (3) Tên yêu cầu, (4) Nội dung câu lệnh `Shall Statement`, (5) Lý giải kỹ thuật & định hướng thiết kế Khối 2–3 (*Rationale*), (6) Chỉ tiêu `CTQ` & Ngưỡng đo, (7) Phương pháp kiểm chứng (`A` — Analysis, `S` — Simulation, `I` — Inspection), và (8) Chủ sở hữu thiết kế (`Owner`).

### 3.2. Nhóm 1 — Yêu cầu Kỹ thuật Chức năng & Logic Vận hành Hệ thống (`SRS-FUNC-01` $\to$ `SRS-FUNC-04`)

| Mã SRS | Truy xuất Nguồn (`PRD` & `HoQ EC`) | Tên Yêu cầu Kỹ thuật | Nội dung Yêu cầu Kỹ thuật Hệ thống (`Shall Statement` chuẩn ISO/IEC/IEEE 29148) | Lý giải Kỹ thuật & Định hướng Thiết kế (`Rationale`) | Chỉ tiêu CTQ / Ngưỡng Đo Kèm Dung sai | Phương pháp V&V | Chủ sở hữu (`Owner`) | Loại nguồn |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| **`SRS-FUNC-01`** | • `PRD-FUNC-01`<br>• `PRD-FUNC-02`<br>• `EC-01` *(22.30%)*<br>• `EC-02` *(14.90%)*<br>• `EC-08` *(11.67%)* | **Vận hành hai chiều trên 4 góc phần tư và phản hồi Encoder** | Khi nhận lệnh điều khiển di chuyển ngang theo hai chiều Tiến (Forward) và Lùi (Reverse), **Hệ truyền động điện xe con phải (shall)** làm việc ổn định trên cả 4 góc phần tư của mặt phẳng Tốc độ – Mô-men $(\omega, M)$ và sử dụng tín hiệu từ 01 bộ mã hóa xung (Encoder) gắn đồng trục động cơ để phản hồi tốc độ khép kín mạch vòng điều khiển (0 cảm biến trên cáp treo). | • Giải quyết `GAP-02`, `GAP-03`, `GAP-05` và hiện thực hóa các đặc tính kỹ thuật trọng số cao trong HoQ (`EC-01`, `EC-02`, `EC-08`).<br>• *Định hướng Khối 2–3 (`SOW-3.3`):* Triển khai cấu trúc điều khiển Vector tựa từ thông rotor (**RFOC**) giữ từ thông rotor không đổi trên toàn dải tốc độ theo chuẩn [B, IEC 61800-2:1998], [R9-06, Shevchenko 2024] và Demag DR [R9-07, tr.4]. Tham số đáp ứng mô-men vi mô $\Delta t_{\text{torque}} \le 10\text{ ms}$ được chuyển giao xuống Khối 3. | • Bao phủ đủ 4 góc phần tư I, II, III, IV.<br>• Phản hồi tốc độ vòng kín từ 01 Encoder trên trục động cơ.<br>• 0 cảm biến lắc trên cáp treo. | **S** | Trần Đỗ Khải & Đặng Nguyên Bình | `[B] [3, 6, 8]` |
| **`SRS-FUNC-02`** | • `PRD-FUNC-04`<br>• `EC-03` *(8.19%)*<br>• `EC-01` *(22.30%)* | **Khóa chéo cấm đảo chiều khi $v \ne 0$ và đồng bộ đóng/mở phanh cơ điện từ** | Trong mọi chu trình chuyển động, **Khối điều khiển logic của hệ truyền động phải (shall)** thực hiện khóa chéo chỉ cho phép đảo chiều khi vận tốc xe con đã dừng hẳn về $v = 0\text{ m/s}$, đồng thời phối hợp điều khiển phanh cơ điện từ sao cho chỉ mở phanh khi động cơ đã sinh đủ mô-men giữ và tự động đóng phanh khi tốc độ giảm về dừng hẳn với độ trôi dừng xe sau khi đóng phanh $\Delta s \le \pm 10\text{ mm}$ (danh định không trôi $\Delta s = 0\text{ mm}$). | • Giải quyết `GAP-03`, kiểm soát rủi ro `RRM-03` và tuân thủ quy tắc cấm đảo chiều khi cơ cấu chưa dừng hẳn tại **Mục 1.5.7.2.9 (trang 21)** và phối hợp phanh **Mục 2.4.5.5.2 (trang 94)** của [R1, TCVN 4244:2005].<br>• *Định hướng Khối 3 (`SOW-3.4`):* Nguyễn Bá Hưng thiết kế máy trạng thái hữu hạn FSM. Tham số ngưỡng đóng/mở phanh ($M_{\text{hold}}$ và $|v| \le 0.002 / 0.005\text{ m/s}$) được chuyển giao xuống FSM Khối 3. | • Khóa chéo cấm đảo chiều khi $v \ne 0\text{ m/s}$.<br>• Mở phanh khi đủ mô-men giữ; đóng phanh khi dừng hẳn.<br>• Độ trôi dừng xe $\Delta s \le \pm 10\text{ mm}$ (danh định không trôi $\Delta s = 0\text{ mm}$). | **S** | Nguyễn Bá Hưng & Trần Đỗ Khải | `[B] [2, 6]` |
| **`SRS-FUNC-03`** | • `PRD-FUNC-02`<br>• `EC-04` *(11.32%)* | **Quy hoạch quỹ đạo tốc độ đặt liên tục theo đường cong S-Curve 7 đoạn** | Khi nhận lệnh thay đổi tốc độ mục tiêu (khởi động từ $0\text{ m/s}$ lên vận tốc định mức hoặc giảm tốc dừng về $0\text{ m/s}$), **Bộ tạo quỹ đạo của hệ truyền động phải (shall)** biến đổi lượng đặt tốc độ bậc thang thành quỹ đạo tốc độ tham chiếu liên tục theo quy luật đường cong chữ S 7 đoạn (**7-Segment S-Curve**) với biên dạng gia tốc đặt khống chế $\lvert a^*(t) \rvert \le 0.50\text{ m/s}^2$ (cận trên $+0\%$) và đạo hàm gia tốc đặt khống chế $\lvert \rho^*(t) \rvert \le 2.00\text{ m/s}^3$ (cận trên $+0\%$, không có xung giật vô hạn). | • Giải quyết `GAP-04` và kiểm soát rủi ro `RRM-01`: Loại bỏ hoàn toàn bộ tạo dốc tuyến tính (Linear Ramp) gây giật đứt gãy gia tốc tại các điểm uốn.<br>• *Định hướng Khối 3 (`SOW-3.3`):* Trần Đỗ Khải lập trình thuật toán giải tích 7 pha S-Curve. Cấp tốc độ bò ($25\% \div 30\% v_{\max}$) được xử lý linh hoạt bằng tham số đặt ở Khối 3 mà không cần lập mã SRS riêng biệt. | • Quỹ đạo đặt S-Curve 7 pha liên tục khả vi bậc 2.<br>• Gia tốc đặt $\lvert a^*(t) \rvert \le 0.50\text{ m/s}^2$ ($+0\%$).<br>• Độ giật đặt $\lvert \rho^*(t) \rvert \le 2.00\text{ m/s}^3$ ($+0\%$). | **A / S** | Trần Đỗ Khải (*PE-Control*) | `[B] [6, 9]` |
| **`SRS-FUNC-04`** | • `PRD-FUNC-03`<br>• `EC-05` *(11.41%)* | **Tiêu tán năng lượng hãm tái sinh qua điện trở xả hãm $R_h$ bảo vệ biến tần** | Trong các pha giảm tốc hãm tái sinh (Góc phần tư II và IV), **Hệ truyền động điện xe con phải (shall)** kích hoạt mạch van hãm (Braking Chopper) và điện trở xả hãm $R_h$ để tiêu tán an toàn năng lượng hãm cơ học trả về mà không gây lỗi quá áp khâu DC-link làm ngắt biến tần ở cả trạng thái đầy tải và không tải. | • Giải quyết `GAP-06`, kiểm soát rủi ro `RRM-02` theo Demag DR [R9-07, tr.8] và Shevchenko [R9-06].<br>• *Định hướng Khối 2 & 3 (`SOW-3.1`, `SOW-3.2`):* Đặng Nguyên Bình tính toán công suất hãm đỉnh và chọn giá trị $R_h$ phù hợp dòng biến tần chọn mua. Ngưỡng điện áp cụ thể ($U_{\text{dc}} \le 780\text{V}$, Chopper $700\text{ V}$) phụ thuộc catalogue biến tần và được chuyển giao xuống Khối 2/3. | • Năng lượng hãm tiêu tán an toàn qua $R_h$.<br>• Biến tần duy trì hoạt động bình thường, không báo lỗi ngắt mạch quá áp DC-link. | **A / S** | Đặng Nguyên Bình & Phạm Văn Hưng | `[C] [6, 8]` |

### 3.3. Nhóm 2 — Yêu cầu Kỹ thuật Hiệu năng Động lực học, Vận tốc & Chế độ Nhiệt $S3$ (`SRS-PERM-01` $\to$ `SRS-PERM-04`)

| Mã SRS | Truy xuất Nguồn (`PRD` & `HoQ EC`) | Tên Yêu cầu Kỹ thuật | Nội dung Yêu cầu Kỹ thuật Hệ thống (`Shall Statement` chuẩn ISO/IEC/IEEE 29148) | Lý giải Kỹ thuật & Định hướng Thiết kế (`Rationale`) | Chỉ tiêu CTQ / Ngưỡng Đo Kèm Dung sai | Phương pháp V&V | Chủ sở hữu (`Owner`) | Loại nguồn |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: | :---: | :---: |
| **`SRS-PERM-01`** | • `PRD-PERM-01`<br>• `EC-06` *(10.10%)*<br>• `EC-01` *(22.30%)* | **Đáp ứng lực kéo, thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ và chống trượt ray** | Khi di chuyển xe con trên ray ở cả hai trạng thái đầy tải $14,244\text{ kg}$ (P-04) [B] và không tải $2,022\text{ kg}$ (P-05) [B], **Hệ truyền động điện xe con phải (shall)** sinh đủ lực kéo tiếp tuyến và mô-men cơ học để thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ (P-20) [B] (với suất cản lăn $w_0 = 0.015$ (P-13) [C], hiệu suất truyền động cơ khí $\eta = 0.90$ (P-15) [C]) và đảm bảo hệ số an toàn chống trượt bánh dẫn trên ray đạt $k_{\text{bám}} \ge 1.20$ với hệ số bám $\varphi = 0.20$ (P-14) [C]. | • Đáp ứng trực tiếp thông số đề bài ($x=2$, `INP-01`, `INP-02`, `ASM-01`), TCVN 4244:2005 [R1, §1.3.3, §1.3.4, §2.4.7] và bài giảng [R5, Bài 4, tr.43].<br>• *Định hướng Khối 2 (`SOW-2.1`):* Đặng Nguyên Bình tính toán chọn động cơ. Giá trị lực kéo cực đại $F_{\max} = 9.22\text{ kN}$ được kiểm nghiệm trong báo cáo tính chọn động cơ ở Khối 2; điều kiện chống trượt ở SRS chỉ cần bảo đảm hệ số an toàn bám $k_{\text{bám}} \ge 1.20$ (danh định đạt $\approx 1.52$). | • Thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$.<br>• Hệ số an toàn bám chống trượt ray $k_{\text{bám}} \ge 1.20$ (danh định $\approx 1.52$).<br>• Không trượt quay bánh xe dẫn trên ray thép. | **A / S** | Đặng Nguyên Bình & Phạm Văn Hưng | `[A] [1] / [B] [2] / [C] [4, 5]` |
| **`SRS-PERM-02`** | • `PRD-PERM-02`<br>• `EC-02` *(14.90%)*<br>• `EC-07` *(10.10%)*<br>• `EC-01` *(22.30%)* | **Đạt vận tốc di chuyển ngang định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$** | Khi nhận lệnh chạy định mức ở cả hai chiều Tiến và Lùi trên toàn dải tải trọng ($2,022\text{ kg} \div 14,244\text{ kg}$), **Hệ truyền động điện xe con phải (shall)** đưa xe con đạt vận tốc dài xác lập định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ (dải $[0.114;\ 0.126]\text{ m/s}$ hay $[6.84;\ 7.56]\text{ m/phút}$, tương ứng tốc độ góc bánh xe $\omega_{\text{bx}} = 0.96\text{ rad/s} \pm 5.0\%$). | • Đáp ứng thông số đề bài ($x=2$, `MOP-01`, `TPM-01`, `TPM-02`), IEC 61800-2 Class 2 [B] và Demag DR [R9-07, tr.8].<br>• *Định hướng Khối 3 (`SOW-3.3`):* Trần Đỗ Khải tinh chỉnh tham số bộ điều khiển PI tốc độ. Độ quá điều chỉnh $M_p \le 10.0\%$ và sai lệch tĩnh $e_{xl} \le 5.0\%$ được chuyển giao thành mục tiêu chỉnh định tối ưu đối xứng tại Khối 3. | • Vận tốc dài xác lập định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ ($[0.114;\ 0.126]\text{ m/s}$) theo cả hai chiều di chuyển.<br>• Tốc độ góc bánh xe $\omega_{\text{bx}} = 0.96\text{ rad/s} \pm 5.0\%$. | **S** | Trần Đỗ Khải & Phạm Văn Hưng | `[A] [1] / [B] [3] / [C] [8]` |
| **`SRS-PERM-03`** | • `PRD-PERM-03`<br>• `EC-04` *(11.32%)*<br>• `EC-08` *(11.67%)* | **Khống chế gia tốc thực tế $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và độ giật thực tế $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$** | Trong mọi giai đoạn khởi động, tăng tốc, giảm tốc và dừng làm việc bình thường với tải treo ở chiều cao nâng lớn nhất $h = 12\text{ m}$ (P-06) [A], **Hệ truyền động điện xe con phải (shall)** khống chế đồng thời độ lớn gia tốc ngang thực tế $\lvert a(t) \rvert \le 0.50\text{ m/s}^2$ (P-10) [A] và độ lớn độ giật ngang thực tế $\lvert \rho(t) \rvert \le 2.00\text{ m/s}^3$ (P-11) [A]. | • Đáp ứng thông số đề bài ($x=2$, `MOP-02`, `MOP-03`, `INP-03`), mô hình con lắc Mita & Kanai (1979) [R9-01] và quỹ đạo S-Curve Tho et al. (2020) [R9-11]; bảo vệ cơ cấu cơ khí; góc lắc $\theta(t)$ quan sát và báo cáo, không nghiệm thu.<br>• *Định hướng Khối 5 (`SOW-5.1`):* Phạm Văn Hưng xây dựng mô hình con lắc cáp đơn và đo gia tốc/độ giật qua bộ lọc thực tế $G_d(s) = \frac{s}{T_f s + 1}$. | • Gia tốc thực tế $\lvert a(t) \rvert \le 0.50\text{ m/s}^2$.<br>• Độ giật thực tế $\lvert \rho(t) \rvert \le 2.00\text{ m/s}^3$ với cáp treo dài $h = 12\text{ m}$. | **A / S** | Trần Đỗ Khải & Phạm Văn Hưng | `[A] [1] / [B] [2, 9]` |
| **`SRS-PERM-04`** | • `PRD-PERM-04`<br>• `EC-06` *(10.10%)* | **Định cỡ công suất phát nhiệt chế độ $S3 - 40\%$ đạt $k_{dt} \ge 1.20$ ở lưới danh định $380\text{V}$** | Khi làm việc ở chế độ ngắn hạn lặp lại **S3 - 40%** (P-17) [C] (chu kỳ chuẩn $10\text{ phút}$, gồm $4.0\text{ phút}$ làm việc và $6.0\text{ phút}$ nghỉ) dưới nguồn điện lưới 3 pha danh định $380\text{ V}$, tần số $50\text{ Hz}$ (P-19) [C] (quá tải mô-men kiểm ở lưới $-10\%$ theo `SRS-D02`), **Các phần tử công suất của hệ truyền động (Động cơ KĐB 3 pha và Biến tần) phải (shall)** được định cỡ thỏa mãn hệ số dự trữ công suất phát nhiệt đẳng trị nằm trong dải $k_{dt} = \frac{P_{\text{đm}}}{P_{\text{đt}}} \ge 1.20$ mà không bị quá nhiệt cuộn dây. | • Giải quyết `GAP-01`, kiểm soát rủi ro `RRM-04` theo tiêu chuẩn IEC 60034-1 [B], Shevchenko [R9-06] và chỉ tiêu kinh tế kỹ thuật `QCD-C01`, `QCD-Q02`.<br>• *Định hướng Khối 2 (`SOW-2.1`):* Đặng Nguyên Bình tính công suất đẳng trị $P_{\text{đt}}$ và chọn mã động cơ theo catalogue. Bội số mô-men quá tải $\lambda_{\max} \ge 2.0$ được đối chiếu trực tiếp từ bảng thông số nhà sản xuất ở Khối 2. | • Chế độ $S3 - 40\%$ ($CD = 40\%$).<br>• Hệ số dự trữ nhiệt $k_{dt} \ge 1.20$ ở lưới danh định $380\text{V} / 50\text{Hz}$. | **A / I** | Đặng Nguyên Bình (*PE-HW*) | `[B] [3] / [C] [8]` |

> **Phân biệt phạm vi:** `SRS-FUNC-03` khống chế **lượng đặt đầu vào** của bộ tạo quỹ đạo S-curve ($a^*, \rho^*$), còn `SRS-PERM-03` kiểm soát **đáp ứng động lực học thực tế** của xe con và tải treo cáp ($a, \rho$). Hai yêu cầu độc lập, không trùng lặp.


## 4. THÔNG SỐ CHUYỂN XUỐNG CÁC KHỐI THIẾT KẾ CHI TIẾT (DOWNSTREAM DESIGN ALLOCATION)

Nhằm tuân thủ nguyên tắc *WHAT, not HOW* của kỹ thuật hệ thống theo tiêu chuẩn quốc tế ISO/IEC/IEEE 29148:2018 và NASA Systems Engineering Handbook (SP-2007-6105 Rev1), tránh bẫy quá chi tiết hóa (*Over-specification*) làm phức tạp việc nghiệm thu cấp hệ thống, các thông số kỹ thuật phụ thuộc vào linh kiện cụ thể hoặc tham số thuật toán điều khiển đã được loại bỏ khỏi SRS Baseline A và chuyển xuống các khối thiết kế chi tiết:

| STT | Thông số đã bỏ khỏi SRS cấp hệ thống | Khối tiếp nhận | Lý do chuyển giao (1 câu) |
| :---: | :--- | :---: | :--- |
| **1** | **Độ quá điều chỉnh tốc độ $M_p \le 10.0\%$** | **Khối 3** *(Điều khiển)* | Là chỉ tiêu chất lượng quá độ của mạch vòng tốc độ kín, chuyển thành mục tiêu tinh chỉnh bộ điều khiển PI (chuẩn tối ưu đối xứng) trên Simulink ở Khối 3. |
| **2** | **Sai lệch tốc độ xác lập tĩnh $e_{xl} \le 5.0\%$** | **Khối 3** *(Điều khiển)* | Đã được bao hàm trong dải dung sai vận tốc xác lập $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ của `SRS-PERM-02`, và được triệt tiêu hoàn toàn nhờ khâu tích phân của bộ điều khiển PI ở Khối 3. |
| **3** | **Điện áp DC-link $U_{\text{dc}} \le 780\text{ V}$ & Chopper $700\text{ V}$** | **Khối 2 & Khối 3** | Ngưỡng điện áp cụ thể phụ thuộc vào catalogue dòng biến tần thực tế được chọn ở Khối 2 và sơ đồ mạch hãm ở Khối 3, SRS chỉ cần yêu cầu chức năng xả hãm không ngắt lỗi quá áp. |
| **4** | **Thời gian đáp ứng mô-men $\Delta t_{\text{torque}} \le 10\text{ ms}$** | **Khối 3** *(Điều khiển)* | Là tham số động học vi mô của mạch vòng dòng điện trong cấu trúc RFOC, được kiểm chứng khi tổng hợp mạch vòng dòng điện (chuẩn tối ưu module) ở Khối 3. |
| **5** | **Mô-men giữ $M_{\text{hold}}$ & Ngưỡng $|v| \le 0.002 / 0.005\text{ m/s}$** | **Khối 3** *(Điều khiển)* | Là các tham số cài đặt của thuật toán máy trạng thái hữu hạn (FSM) điều khiển logic liên động phanh cơ và khóa chéo ở Khối 3, SRS chỉ cần giữ chỉ tiêu độ trôi dừng $\Delta s \le \pm 10\text{ mm}$. |
| **6** | **Lực kéo cực đại tăng tốc $F_{\max} = 9.22\text{ kN}$** | **Khối 2** *(Chọn động cơ)* | Là giá trị lực kéo tính toán phát sinh trong pha quá độ tăng tốc, được tính toán và kiểm tra trong phần chọn động cơ ở Khối 2; điều kiện chống trượt ở SRS chỉ cần bảo đảm hệ số an toàn bám $k_{\text{bám}} \ge 1.20$. |
| **7** | **Bội số mô-men cực đại $\lambda_{\max} \ge 2.0$** | **Khối 2** *(Chọn động cơ)* | Là thông số cơ điện sẵn có từ nhà sản xuất, được kiểm tra đối chiếu trực tiếp khi tra cứu bảng thông số catalogue động cơ ở Khối 2. |
| **8** | **Cấp tốc độ bò (Creep Speed $25\% \div 30\% v_{\max}$)** | **Khối 3** *(Điều khiển)* | Là tính năng công nghệ phục vụ căn chỉnh vị trí tải, được hiện thực hóa bằng việc thay đổi lượng đặt vận tốc trên biến tần ở Khối 3 mà không cần ép cứng thành một mã SRS riêng biệt. |


## 5. MA TRẬN TRUY XUẤT YÊU CẦU HAI CHIỀU (RTM) & KẾ HOẠCH KIỂM CHỨNG CẤP HỆ THỐNG (`DVP&R L0`) (`SOW-1.3`)

Thực hiện gói công việc **`SOW-1.3`** do **Phạm Văn Hưng (*QE-Simulation*)** và **Nguyễn Hải Trung (*Doc Lead*)** phụ trách, phần này thiết lập **Ma trận Truy xuất Yêu cầu Hai chiều (`Bidirectional RTM`)** và **Kế hoạch Kiểm chứng Cấp Hệ thống (`DVP&R L0`)** cho toàn bộ 8 yêu cầu kỹ thuật chốt của `SRS Baseline A`.

### 5.1. Ma trận Truy xuất Xuôi (`Forward RTM`: `PRD v3.1` $\leftrightarrow$ `HoQ EC` $\leftrightarrow$ `SRS Baseline A` $\leftrightarrow$ `SOW WBS` $\leftrightarrow$ `DVP&R L0`)

| Mã PRD | Nội dung Yêu cầu Khách hàng (`PRD v3.1`) | Các Đặc tính Kỹ thuật HoQ Tương ứng (`HOWs`) | Mã SRS Baseline A (Đã Đóng băng) | Tóm tắt Nội dung Yêu cầu Kỹ thuật Hệ thống | Chỉ tiêu Đo kiểm (`CTQ / CTS`) | Mã Công việc SOW Phụ trách | Mã Bài Kiểm chứng (`DVP&R L0`) | Loại nguồn |
| :---: | :--- | :--- | :---: | :--- | :--- | :--- | :---: | :---: |
| **`PRD-FUNC-01`** | Vận hành 4 góc phần tư & đảo chiều Tiến/Lùi dọc ray dầm chính | • `EC-01` *(22.30%)*<br>• `EC-02` *(14.90%)*<br>• `EC-08` *(11.67%)* | **`SRS-FUNC-01`** | Vận hành di chuyển 2 chiều Tiến/Lùi trên 4 góc phần tư, phản hồi vòng kín 01 Encoder gắn trục động cơ. | `CTQ-01`<br>`CTQ-02` | • `SOW-3.3` (*Trần Đỗ Khải — RFOC*)<br>• `SOW-5.1` (*Phạm Văn Hưng — Simulink*) | **`DVP-L0-01`** *(DV-01)* | `[B] [3, 6, 8]` |
| **`PRD-FUNC-04`** | Phối hợp đồng bộ phanh cơ và mô-men điện, cấm đảo chiều khi $v \ne 0$ | • `EC-03` *(8.19%)*<br>• `EC-01` *(22.30%)* | **`SRS-FUNC-02`** | Khóa chéo cấm đảo chiều khi $v \ne 0\text{ m/s}$ và đồng bộ đóng/mở phanh cơ điện từ, độ trôi dừng xe $\Delta s \le \pm 10\text{ mm}$. | `CTQ-07`<br>`CTS-03`<br>`CTS-04` | • `SOW-3.4` (*Nguyễn Bá Hưng — Logic*)<br>• `SOW-5.1` (*Phạm Văn Hưng — Simulink*) | **`DVP-L0-02`** *(DV-02)* | `[B] [2, 6]` |
| **`PRD-FUNC-02`** | Điều chỉnh tốc độ vô cấp & làm mềm quá trình tăng/giảm tốc | • `EC-04` *(11.32%)* | **`SRS-FUNC-03`** | Quy hoạch quỹ đạo đặt S-curve 7 đoạn liên tục với gia tốc đặt $\lvert a^* \rvert \le 0.50\text{ m/s}^2$ và độ giật đặt $\lvert \rho^* \rvert \le 2.00\text{ m/s}^3$. | `CTQ-06`<br>`CTS-01` | • `SOW-3.3` (*Trần Đỗ Khải — S-Curve*)<br>• `SOW-5.1` (*Phạm Văn Hưng — Simulink*) | **`DVP-L0-03`** *(DV-03)* | `[B] [6, 9]` |
| **`PRD-FUNC-03`** | Hấp thụ & tiêu tán năng lượng hãm tái sinh bảo vệ biến tần | • `EC-05` *(11.41%)* | **`SRS-FUNC-04`** | Tiêu tán năng lượng hãm tái sinh qua mạch van hãm và điện trở xả $R_h$, biến tần không ngắt lỗi quá áp DC-link. | `CTQ-07`<br>`CTS-02` | • `SOW-3.1` (*Đặng Nguyên Bình — $R_h$*)<br>• `SOW-5.1` (*Phạm Văn Hưng — Simulink*) | **`DVP-L0-04`** *(DV-04)* | `[C] [6, 8]` |
| **`PRD-PERM-01`** | Đáp ứng tải trọng kéo ngang định mức $M_{\Sigma} = 14,244\text{ kg}$ | • `EC-06` *(10.10%)*<br>• `EC-01` *(22.30%)* | **`SRS-PERM-01`** | Đủ lực kéo thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ (với $\eta = 0.90$) và đảm bảo hệ số an toàn bám chống trượt ray $k_{\text{bám}} \ge 1.20$. | `CTQ-01` | • `SOW-2.1` (*Đặng Nguyên Bình — Động cơ*)<br>• `SOW-5.1` (*Phạm Văn Hưng — Simulink*) | **`DVP-L0-05`** *(DV-05)* | `[A] [1] / [B] [2] / [C] [4, 5]` |
| **`PRD-PERM-02`** | Vận tốc định mức của xe con $v_{\max} = 0.12\text{ m/s}$ | • `EC-02` *(14.90%)*<br>• `EC-07` *(10.10%)*<br>• `EC-01` *(22.30%)* | **`SRS-PERM-02`** | Đưa xe con đạt vận tốc dài xác lập định mức $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ ($[0.114;\ 0.126]\text{ m/s}$) theo cả hai chiều di chuyển. | `CTQ-02`<br>`CTQ-03` | • `SOW-3.3` (*Trần Đỗ Khải — PI tốc độ*)<br>• `SOW-5.1` (*Phạm Văn Hưng — Simulink*) | **`DVP-L0-06`** *(DV-06)* | `[A] [1] / [B] [3] / [C] [8]` |
| **`PRD-PERM-03`** | Giới hạn gia tốc $\le 0.5\text{ m/s}^2$ & độ giật $\le 2.0\text{ m/s}^3$, cáp $h = 12\text{ m}$ | • `EC-04` *(11.32%)*<br>• `EC-08` *(11.67%)* | **`SRS-PERM-03`** | Khống chế chuyển động thực tế đạt gia tốc $\lvert a(t) \rvert \le 0.50\text{ m/s}^2$ và độ giật $\lvert \rho(t) \rvert \le 2.00\text{ m/s}^3$ với cáp treo dài $h = 12.0\text{ m}$. | `CTQ-05`<br>`CTQ-06`<br>`CTS-01` | • `SOW-3.3` (*Trần Đỗ Khải — Điều khiển*)<br>• `SOW-5.1` (*Phạm Văn Hưng — Simulink*) | **`DVP-L0-07`** *(DV-07)* | `[A] [1] / [B] [2, 9]` |
| **`PRD-PERM-04`** | Khả năng làm việc ở chế độ nhiệt $S3 - 40\%$ ở lưới danh định $380\text{V}$ | • `EC-06` *(10.10%)* | **`SRS-PERM-04`** | Đảm bảo hệ số dự trữ phát nhiệt $k_{dt} \ge 1.20$ ở chế độ S3 - 40% ở lưới danh định $380\text{V}$, không quá nhiệt cuộn dây. | `CTQ-08`<br>`CTS-05` | • `SOW-2.1` (*Đặng Nguyên Bình — Tính nhiệt*)<br>• `SOW-3.1` (*Đặng Nguyên Bình — BOM*) | **`DVP-L0-08`** *(DV-08)* | `[B] [3] / [C] [8]` |

### 5.2. Ma trận Truy xuất Ngược (`Backward RTM`: `DVP&R L0` $\to$ `SRS Baseline A` $\to$ `PRD v3.1` $\to$ `Owner`)

| Mã Bài kiểm chứng | Mã SRS gốc | Mã PRD gốc | Phương pháp | Khối thực hiện (Mã WBS) | Người phụ trách chính |
| :---: | :---: | :---: | :---: | :--- | :--- |
| **`DVP-L0-01`** *(DV-01)* | `SRS-FUNC-01` | `PRD-FUNC-01` | **S** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) | Trần Đỗ Khải (Điều khiển) & Phạm Văn Hưng (Mô phỏng) |
| **`DVP-L0-02`** *(DV-02)* | `SRS-FUNC-02` | `PRD-FUNC-04` | **S** | Khối 3 (SOW-3.4) & Khối 5 (SOW-5.1) | Nguyễn Bá Hưng (Logic) & Phạm Văn Hưng (Mô phỏng) |
| **`DVP-L0-03`** *(DV-03)* | `SRS-FUNC-03` | `PRD-FUNC-02` | **A / S** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) | Trần Đỗ Khải (Điều khiển) & Phạm Văn Hưng (Mô phỏng) |
| **`DVP-L0-04`** *(DV-04)* | `SRS-FUNC-04` | `PRD-FUNC-03` | **A / S** | Khối 3 (SOW-3.1) & Khối 5 (SOW-5.1) | Đặng Nguyên Bình (Phần cứng) & Phạm Văn Hưng (Mô phỏng) |
| **`DVP-L0-05`** *(DV-05)* | `SRS-PERM-01` | `PRD-PERM-01` | **A / S** | Khối 2 (SOW-2.1) & Khối 5 (SOW-5.1) | Đặng Nguyên Bình (Phần cứng) & Phạm Văn Hưng (Mô phỏng) |
| **`DVP-L0-06`** *(DV-06)* | `SRS-PERM-02` | `PRD-PERM-02` | **S** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) | Trần Đỗ Khải (Điều khiển) & Phạm Văn Hưng (Mô phỏng) |
| **`DVP-L0-07`** *(DV-07)* | `SRS-PERM-03` | `PRD-PERM-03` | **A / S** | Khối 3 (SOW-3.3) & Khối 5 (SOW-5.1) | Trần Đỗ Khải (Điều khiển) & Phạm Văn Hưng (Mô phỏng) |
| **`DVP-L0-08`** *(DV-08)* | `SRS-PERM-04` | `PRD-PERM-04` | **A / I** | Khối 2 (SOW-2.1) & Khối 3 (SOW-3.1) | Đặng Nguyên Bình (Phần cứng) |

### 5.3. Bảng Kế hoạch và Báo cáo Kiểm chứng Cấp Hệ thống (`DVP&R Level 0` — 8 Bài Kiểm chứng)

| Mã DV | Mã SRS | Phương pháp | Kịch bản Thử nghiệm & Điều kiện Tải | Tín hiệu Đo / Đại lượng Kiểm tra | Tiêu chí ĐẠT (PASS Criteria) | Tiêu chí BÁC BỎ (FAIL Criteria) | Kỹ sư Thực hiện | Trạng thái |
| :---: | :---: | :---: | :--- | :--- | :--- | :--- | :--- | :---: |
| **`DVP-L0-01`** *(DV-01)* | **`SRS-FUNC-01`** | **S** | Mô phỏng Simulink hệ truyền động chạy Tiến rồi phát lệnh đảo chiều sang Lùi ở cả hai trạng thái: đầy tải $14,244\text{ kg}$ (P-04) và không tải $2,022\text{ kg}$ (P-05). | • Tốc độ góc rotor $\omega(t)$<br>• Mô-men điện từ $M_e(t)$<br>• Tín hiệu xung phản hồi từ Encoder | **PASS khi:** Hệ thống vận hành ổn định trên cả 4 góc phần tư I, II, III, IV; mạch vòng FOC nhận phản hồi liên tục từ 01 Encoder để kiểm soát tốc độ. | **FAIL khi:** Mất đồng bộ điều khiển FOC, không tạo được mô-men hãm điện ở góc II/IV hoặc đứt tín hiệu Encoder. | Trần Đỗ Khải & Phạm Văn Hưng | `Planned (Baseline A)` |
| **`DVP-L0-02`** *(DV-02)* | **`SRS-FUNC-02`** | **S** | Mô phỏng Simulink phát lệnh đảo chiều đột ngột khi xe con đang chạy nhanh; tiếp tục quan sát chu trình giảm tốc về 0 m/s và kích hoạt phanh cơ ở đầy tải $14,244\text{ kg}$. | • Vận tốc dài xe con $v(t)$<br>• Lệnh logic khóa chéo đảo chiều<br>• Trạng thái đóng/mở phanh cơ<br>• Độ trôi dừng xe $\Delta s$ | **PASS khi:** Mạch khóa chéo ngăn đảo chiều khi $v \ne 0\text{ m/s}$; phanh cơ chỉ mở khi động cơ đã sinh mô-men giữ; độ trôi dừng xe sau khi đóng phanh thỏa mãn $\Delta s \le \pm 10\text{ mm}$ (danh định không trôi $\Delta s = 0$). | **FAIL khi:** Cho phép đảo chiều khi xe chưa dừng hẳn ($v \ne 0$), hoặc trôi xe tự do khi mở phanh, hoặc độ trôi dừng $\Delta s > 10\text{ mm}$. | Nguyễn Bá Hưng & Trần Đỗ Khải | `Planned (Baseline A)` |
| **`DVP-L0-03`** *(DV-03)* | **`SRS-FUNC-03`** | **A / S** | Tính toán giải tích thông số 7 đoạn S-curve; mô phỏng khối tạo quỹ đạo nạp lượng đặt tốc độ bậc thang từ $0 \to 0.12\text{ m/s}$ và trích xuất đường đặt thời gian thực. | • Quỹ đạo tốc độ đặt $\omega^*(t)$<br>• Gia tốc đặt $a^*(t)$<br>• Độ giật đặt $\rho^*(t) = \text{d}a^*/\text{d}t$ | **PASS khi:** Quỹ đạo gia tốc đặt $a^*(t)$ biến thiên liên tục hình thang, đạt đỉnh $\lvert a^*(t) \rvert \le 0.50\text{ m/s}^2$ và đạo hàm gia tốc đặt $\lvert \rho^*(t) \rvert \le 2.00\text{ m/s}^3$ (không có xung giật vô hạn). | **FAIL khi:** Xuất hiện bước nhảy gia tốc đột ngột hoặc $\lvert a^*(t) \rvert > 0.50\text{ m/s}^2$ hoặc $\lvert \rho^*(t) \rvert > 2.00\text{ m/s}^3$. | Trần Đỗ Khải (*PE-Control*) | `Planned (Baseline A)` |
| **`DVP-L0-04`** *(DV-04)* | **`SRS-FUNC-04`** | **A / S** | Tính toán giải tích công suất hãm cực đại; mô phỏng quá trình giảm tốc hãm tái sinh từ $0.12\text{ m/s}$ về $0\text{ m/s}$ khi mang đầy tải $14,244\text{ kg}$ (P-04) [B]. | • Điện áp khâu DC-link $U_{\text{dc}}(t)$<br>• Dòng xả qua điện trở hãm $I_{Rh}(t)$<br>• Trạng thái cờ ngắt lỗi biến tần | **PASS khi:** Toàn bộ động năng hãm được tiêu tán an toàn qua điện trở xả hãm $R_h$; biến tần duy trì hoạt động bình thường, không báo lỗi ngắt mạch quá áp khâu DC-link. | **FAIL khi:** Biến tần báo lỗi quá áp DC-link làm ngắt mạch lực trong quá trình giảm tốc hãm tái sinh đầy tải. | Đặng Nguyên Bình & Phạm Văn Hưng | `Planned (Baseline A)` |
| **`DVP-L0-05`** *(DV-05)* | **`SRS-PERM-01`** | **A / S** | Tính toán giải tích lực cản, lực kéo và mô phỏng xe con di chuyển trên ray ở đầy tải $14,244\text{ kg}$ ($w_0 = 0.015$, $\eta = 0.90$) và không tải $2,022\text{ kg}$; kiểm tra chống trượt ray khô ($\varphi = 0.20$). | • Lực kéo tiếp tuyến bánh xe $F_k(t)$<br>• Lực cản lăn tĩnh $F_{c.\text{đầy}}$<br>• Hệ số an toàn bám $k_{\text{bám}} = F_{\text{bám}} / F_{k,\max}$ | **PASS khi:** Hệ thống sản sinh đủ lực kéo thắng lực cản lăn tĩnh đầy tải $F_{c.\text{đầy}} = 2,096\text{ N}$ (P-20) [B]; hệ số an toàn bám chống trượt thỏa mãn $k_{\text{bám}} \ge 1.20$ ở mọi thời điểm gia tốc (danh định đạt $\approx 1.52$). | **FAIL khi:** Không thắng được lực cản tĩnh đầy tải hoặc $k_{\text{bám}} < 1.20$ gây trượt quay bánh xe dẫn hướng trên ray. | Đặng Nguyên Bình & Phạm Văn Hưng | `Planned (Baseline A)` |
| **`DVP-L0-06`** *(DV-06)* | **`SRS-PERM-02`** | **S** | Mô phỏng Simulink xe con chạy xác lập theo lệnh vận tốc định mức theo cả chiều Tiến và chiều Lùi trên toàn dải tải trọng ($2,022\text{ kg} \div 14,244\text{ kg}$). | • Vận tốc dài xác lập thực tế $v(t)$<br>• Tốc độ góc trục bánh xe $\omega_{\text{bx}}(t)$ | **PASS khi:** Vận tốc dài xác lập thực tế của xe con đạt mốc $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ (dải $[0.114;\ 0.126]\text{ m/s}$) theo cả hai chiều chuyển động ở mọi trạng thái tải. | **FAIL khi:** Vận tốc xác lập thực tế nằm ngoài dải quy chuẩn $[0.114;\ 0.126]\text{ m/s}$ (thiếu tốc độ hoặc vượt tốc). | Trần Đỗ Khải & Phạm Văn Hưng | `Planned (Baseline A)` |
| **`DVP-L0-07`** *(DV-07)* | **`SRS-PERM-03`** | **A / S** | Mô phỏng xe con mang tải treo cáp dài $12\text{ m}$ (P-06) [A] thực hiện toàn bộ chu trình tăng tốc và giảm tốc; đo gia tốc và độ giật thực tế qua bộ lọc đạo hàm $G_d(s) = \frac{s}{T_f s + 1}$. | • Gia tốc thực tế $a(t) = \text{d}v/\text{d}t$<br>• Độ giật thực tế $\rho(t) = \text{d}a/\text{d}t$<br>• Góc lắc tải treo $\theta(t)$ | **PASS khi:** Độ lớn gia tốc ngang thực tế khống chế $\lvert a(t) \rvert \le 0.50\text{ m/s}^2$ và độ giật ngang thực tế khống chế $\lvert \rho(t) \rvert \le 2.00\text{ m/s}^3$ trong mọi pha chuyển động bình thường. | **FAIL khi:** Gia tốc vượt ngưỡng $\lvert a(t) \rvert > 0.50\text{ m/s}^2$ hoặc độ giật vượt ngưỡng $\lvert \rho(t) \rvert > 2.00\text{ m/s}^3$. | Trần Đỗ Khải & Phạm Văn Hưng | `Planned (Baseline A)` |
| **`DVP-L0-08`** *(DV-08)* | **`SRS-PERM-04`** | **A / I** | Tính toán giải tích công suất phát nhiệt đẳng trị $P_{\text{đt}}$ theo chu kỳ làm việc $S3 - 40\%$ ($CD = 40\%$, $T_{\text{ck}} = 10\text{ phút}$) ở lưới danh định $380\text{ V}$ (quá tải mô-men kiểm ở $342\text{ V}$); đối chiếu với catalogue động cơ chọn ở Khối 2. | • Công suất đẳng trị tính toán $P_{\text{đt}}$<br>• Công suất định mức catalogue $P_{\text{đm}}$<br>• Hệ số dự trữ nhiệt $k_{dt} = P_{\text{đm}} / P_{\text{đt}}$ | **PASS khi:** Động cơ tra từ catalogue nhà sản xuất có công suất định mức thỏa mãn hệ số dự trữ phát nhiệt $k_{dt} \ge 1.20$ mà không bị quá nhiệt cuộn dây. | **FAIL khi:** Hệ số dự trữ nhiệt $k_{dt} < 1.20$ (nguy cơ quá nhiệt cháy động cơ) hoặc $\lambda_K (U_{\min}/U_N)^2 < M_{\max}/M_N$ (không đủ mô-men khi lưới −10% — SRS A.1, CR-02). | Đặng Nguyên Bình (*PE-HW*) | `Planned (Baseline A)` |

### 5.4. Quy chuẩn Thiết lập Môi trường Đo kiểm trên MATLAB/Simulink

Nhằm kiểm soát rủi ro **`RRM-05`** (*"Sai số đạo hàm độ giật* $\rho(t)$ *khi tích hợp Simulink do chọn bước lấy mẫu* $T_s$ *quá thô"*) và chuẩn bị cơ sở kỹ thuật cho gói công việc **`SOW-4.1`** tại Cổng `TRR-EVT`, kế hoạch `DVP&R L0` khóa cứng **3 quy tắc kỹ thuật đo kiểm bắt buộc** trên MATLAB/Simulink đối với bạn **Phạm Văn Hưng (*QE-Simulation*)**:

1. **Khóa Solver và Bước lấy mẫu ($T_s$):**
   * Sử dụng bộ giải bước cố định (*Fixed-step solver*: `ode4 (Runge-Kutta)`) hoặc bước biến thiên độ chính xác cao (`ode23tb` / `ode45` với `Max step size` $\le 10^{-4}\text{ s}$) và bước trích xuất dữ liệu đo kiểm $T_s \le 10^{-4}\text{ s}$ ($0.1\text{ ms}$) để bắt chính xác đáp ứng dòng điện và đạo hàm bậc cao.
2. **Quy tắc Trích xuất Gia tốc thực tế $a(t)$ và Độ giật $\rho(t)$:**
   * **Gia tốc ngang $a(t)$ (`DVP-L0-07`):** Trích xuất trực tiếp biến trạng thái gia tốc cơ học từ vế phải của phương trình động lực học xe con:
     $$a(t) = \frac{F_{\text{kéo}}(t) - F_{\text{cản}}(t) + F_{\text{lắc}}(t)}{m_{xc}},\quad F_{\text{lắc}} = (Q + m_{nh})\,g\,\theta,\quad F_{\text{cản}} = M_\Sigma\, g\, w_0$$
     *(Sửa 26/10/2026: mô hình 2 khối lượng theo SDD v1.3 §2.1 — tải treo không nằm trong khối lượng cứng; công thức cũ chia cho $M_\Sigma$ trong khi đã cộng $F_{\text{lắc}}$ nên tính khối lượng tải hai lần. Dấu $\theta$ theo ICD v1.2 IF-10.)*
   * **Độ giật ngang $\rho(t)$ (`DVP-L0-07`):** Áp dụng bộ lọc thông thấp quán tính bậc nhất kèm đạo hàm (*Filtered Derivative*) với hằng số thời gian lọc $T_f \in [0.005;\ 0.01]\text{ s}$:
     $$G_d(s) = \frac{s}{T_f s + 1}$$


## 6. ĐỐI CHIẾU CHECKLIST SOÁT XÉT ĐÓNG BĂNG SRS TẠI CỔNG `SRR-EVT`

Trước khi **Nghiêm Trọng Đông (*PM / SE Lead*)** ký biên bản thông qua **Cổng 2 (`SRR-EVT`)** để đóng băng `SRS Baseline A` (đạt $\text{TRL } 3$) và chuyển sang **Khối 2 (`PDR-EVT`)**, tài liệu này đã được kiểm tra đạt tuyệt đối **8/8 tiêu chí cổng kiểm soát**:

| STT | Câu hỏi Kiểm tra Cổng `SRR-EVT` (Theo `CAM_NANG_SRS_ieee_29148.md` & `FLOW_REVIEW.md`) | Kết quả | Minh chứng Xác thực trong Báo cáo `SRS-8.5EMG-TROLLEY-v1.2` |
| :-: | :--- | :---: | :--- |
| **1** | **Đã khóa PRD trước khi đóng băng SRS chưa?** | **ĐẠT (PASS)** | Bộ 3 tài liệu Khối 0 (`PRD v3.1`, `SOW v1.1`, `BCA-QFD v1.1`) đều đã được đóng băng (`Frozen`) tại Cổng 1 (`MCR`) trước khi lập bản SRS này. |
| **2** | **Đúng tuyệt đối bộ số liệu đề bài $x = 2$ và hằng số SSoT đã khóa chưa?** | **ĐẠT (PASS)** | Giữ chính xác tuyệt đối: $Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg}$, $m_{xc} = 1,800\text{ kg} \Rightarrow M_\Sigma = 14,244\text{ kg}$, $m_{\text{tĩnh}} = 2,022\text{ kg}$, $h = 12\text{ m}$, $v_{\max} = 0.12\text{ m/s}$, $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$, $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$, $D_{bx} = 0.25\text{ m}$, $w_0 = 0.015$, $\varphi = 0.20$, $\eta = 0.90$, $F_{c.\text{đầy}} = 2,096\text{ N}$, $k_{\text{bám}} \approx 1.52 \ge 1.20$. |
| **3** | **Tuân thủ 100% phạm vi cam kết `FUNC` & `PERM` trong `SOW v1.1` chưa?** | **ĐẠT (PASS)** | Toàn bộ 8 mã (`SRS-FUNC-01..04` và `SRS-PERM-01..04`) nằm trọn trong phạm vi 2 nhóm `PRD-FUNC` và `PRD-PERM`; đã loại bỏ 100% các yếu tố ngoài phạm vi (`SAFE`, `INTF`, `ENVI`, `RELI`). |
| **4** | **100% câu lệnh có từ khóa `phải (shall)` và ngưỡng định lượng đo được chưa?** | **ĐẠT (PASS)** | Cả 8/8 câu lệnh tại Mục 3.2 và Mục 3.3 đều tuân thủ công thức cú pháp 5 thành phần của ISO/IEC/IEEE 29148 có từ khóa **`phải (shall)`** kèm ngưỡng số học cụ thể. |
| **5** | **Đảm bảo tính Nguyên tử (*Singular / Atomic*) và thực hiện đúng Downstream Allocation chưa?** | **ĐẠT (PASS)** | Mục 1.2 và Mục 4 đã giải thích chi tiết cơ chế phân bổ thiết kế chi tiết: chuyển 8 thông số quá độ ($M_p, e_{xl}$) và linh kiện ($U_{\text{dc}}, \Delta t_{\text{torque}}, M_{\text{hold}}, F_{\max}, \lambda_{\max}$, Creep) xuống Khối 2 và Khối 3, giữ SRS ở đúng 8 mã chốt ánh xạ 1-1 với PRD. |
| **6** | **Đã dựng Boundary Diagram, P-Diagram và trích dẫn rõ nguồn thiết lập chưa?** | **ĐẠT (PASS)** | Mục 2.1 và Mục 2.2 đã thiết lập đầy đủ **Boundary Diagram** và **P-Diagram** (4 nhiễu $N_1 \div N_4$), kèm bảng giải trình rõ nguồn tiêu chuẩn ([B, IEC 61800-2:1998], [R1, TCVN 4244:2005], [R2, NASA SP-2007-6105 Rev1], Case Studies `CS-01..09`) dùng để vẽ từng khối. |
| **7** | **Mọi câu SRS đều có cột Lý giải (*Rationale*), giữ đúng *WHAT vs. HOW* và có phương pháp kiểm chứng chưa?** | **ĐẠT (PASS)** | Không nhét yêu cầu công việc SOW vào SRS; các phương pháp tổng hợp chi tiết (*PI-MO/SO*) được đặt ở cột *Rationale*; toàn bộ 8 mã đều có kịch bản kiểm chứng trong `DVP&R L0` (`DVP-L0-01..08`). |
| **8** | **Truy xuất hai chiều 100% giữa `PRD` $\leftrightarrow$ `HoQ EC` $\leftrightarrow$ `SRS` $\leftrightarrow$ `DVP&R L0` chưa?** | **ĐẠT (PASS)** | Ma trận `RTM` tại Mục 5.1 và 5.2 ánh xạ khép kín 100% giữa 8 mã `PRD`, 8 mã `EC` (HoQ), 8 mã `SRS Baseline A` và 8 bài đo `DVP&R L0`, không có yêu cầu mồ côi. |


## 7. TÀI LIỆU THAM KHẢO

| Viện dẫn [x] | Mã thống nhất | Tài liệu | Tệp trong kho | Trạng thái |
| :---: | :---: | :--- | :--- | :--- |
| **[1]** | `[R3]` | Bộ môn Tự động hóa CN — ĐHBK Hà Nội, *Đề bài tập dài Thiết kế hệ truyền động điện* (Đề 0~9, $x = 2$) | Không có | Số liệu [A] theo đề nhóm được giao |
| **[2]** | `[R1]` | Bộ KH&CN, *TCVN 4244:2005 — Thiết bị nâng: Thiết kế, chế tạo và kiểm tra kỹ thuật* | `tcvn-4244-2005.pdf` (scan) | Đã đối chiếu các điều được trích (xem danh mục thống nhất) |
| **[3]** | — | IEC 61800-2, IEC 60034-1, ISO/IEC/IEEE 29148:2018 | Không có toàn văn (IEC 60034-1 trích qua `[R4]` tr.23) | Dùng theo hiểu biết chung |
| **[4]** | `[R4]`, `[R5]` | TS. Nguyễn Duy Đỉnh, *Tiêu chuẩn VN và quốc tế*; PGS.TS. Bùi Quốc Khánh, TS. Nguyễn Duy Đỉnh, *Bài giảng Thiết kế hệ truyền động điện* | `Thầy Đỉnh/` | Có tệp; trích theo tên tệp + slide |
| **[5]** | — | *Không có tài liệu.* $D_{bx} = 0.25$ m và $w_0 = 0.015$ là giả định nhóm `[C]` (kiểm tra $w_0$ bằng công thức ở SSoT P-13). Mã `[R9-10]` "DIN 536 / A54.pdf" đã gỡ vì `A54.pdf` là bài báo Valtchev et al. 2024 | — | Đã gỡ |
| **[6]** | `[R9-07]` | Demag Cranes & Components, *Demag DR rope hoists — for load capacities up to 50 t*, ấn phẩm 213 133 44 | `Dầm đôi_cấu trúc truyền động_Đức.pdf` | Có tệp |
| **[7]** | `[R9-08]` | Catalogue pa lăng cáp dầm đôi KG-Cranes / Sungdo | Không có | Chỉ tham khảo; $m_{xc}$ là giả định `[C]` |
| **[8]** | `[R9-06]` | Я. О. Шевченко, *Hệ điều khiển tự động truyền động điện cầu trục kho hàng* (đồ án cử nhân), KPI Igor Sikorsky, 2024 | `Shevchenko_bakalavr.pdf` | Có tệp |
| **[9]** | `[R9-01]`, `[R9-11]` | T. Mita, T. Kanai, *Optimal Control of the Crane System Using the Maximum Speed of the Trolley*, Trans. SICE 15(6), 1979; Ho Duc Tho, A. Kaneshige, K. Terashima, *Minimum-time S-curve commands…*, Control Eng. Practice 98 (2020) 104390 | `Crane trolley Nhật Bổn.pdf`, `S-curve.pdf` | Có tệp |
| **[10]** | `[R2]` | NASA, *Systems Engineering Handbook*, NASA/SP-2007-6105 Rev 1, 2007 | Không có | — |
| **[11]** | `[R6]` | PRD mẫu môn Thiết kế TĐĐ | Không có | — |
| **[12]** | `[R7]` | SOW mẫu môn Thiết kế TĐĐ | Không có | — |
| **[13]** | `[R8]` | Nhóm 2, *Thiết kế truyền động xe con cầu trục* (slide sinh viên) | `Bản sao của [NHÓM 2] …pptx.pdf` | Có tệp |
| **[14]** | `[R9-02]` | P. G. Feto, Wartono, Sutrisna, *Perencanaan Sistem Trolley dan Bridge Pada Overhead Travelling Crane Beban Angkat 10 Ton*, Jurnal Cendekia 6(2), 2025 | `Cầu trục_Indo.pdf` | Có tệp |
| **[15]** | `[R9-03]` | S. Ö. Doğan, *Design and analysis of double girder overhead crane system*, J. Radiation Research and Applied Sciences 16 (2023) 100701 | `Thiết kế cầu trục dầm đôi_Thổ.pdf` | Có tệp |
| **[16]** | `[R9-04]` | S. Valtchev et al., *Increasing the Damping Capacity of Crane Electric Drive Systems When Moving Cargo with a Flexible Suspension*, DAS 2024 (IEEE) | `A54.pdf` | Có tệp |
| **[17]** | `[R9-05]` | F. Zheng et al., *Vision-based Fuzzy PID Tracking Control Scheme for Gantry Crane System*, Sensors and Materials 33(9), 2021 | `SM2693.pdf` | Có tệp |
| **[18]** | `[R9-09]` | Catalogue cầu trục dầm đôi Yuantai / Konecranes | Không có | Chỉ tham khảo |

Thông tin đầy đủ và bảng đổi mã: `Tài liệu tham khảo/00_Danh_muc_tai_lieu_tham_khao.md`.


## 8. GIẢ ĐỊNH & VẤN ĐỀ MỞ (OPEN ISSUES)

Dưới đây là danh mục các giả định kỹ thuật và các điểm cần xin ý kiến tham vấn hoặc kiểm chứng với Giảng viên hướng dẫn (TS. Nguyễn Duy Đỉnh):

| STT | Vấn đề / Giả định | Phân loại & Viện dẫn | Hiện trạng trong SRS v1.2 | Cơ sở đề xuất của Nhóm 8.5-EMG | Kế hoạch kiểm chứng / Xin ý kiến GVHD |
| :-: | :--- | :---: | :--- | :--- | :--- |
| **1** | **Khối lượng xe con $m_{xc} = 1,800\text{ kg}$** | `[C] [7]` | Giả định nhóm chọn $m_{xc} = 1,800\text{ kg}$ theo tỉ lệ $14.7\%$ tổng tải nâng | Căn cứ catalogue pa lăng dầm đôi 15 tấn KG-Cranes / Sungdo [7] ($1,650 \div 1,900\text{ kg}$) | Xin ý kiến GVHD tại Cổng SRR-EVT; kiểm chứng lại khi nhận bản vẽ cơ khí chi tiết ở Khối 3. |
| **2** | **Đường kính bánh xe $d = 0.25\text{ m}$** | `[C] [5]` | Khóa cố định $d = 0.25\text{ m}$ (bán kính $R = 0.125\text{ m}$) | Giả định `[C]` theo dải bánh xe thông dụng cho tải trọng trục $\approx 35.6\text{ kN/bánh}$ | Kiểm tra bền tiếp xúc ray theo TCVN 4244:2005 §2.4 [2] tại Khối 3. |
| **3** | **Suất cản lăn riêng $w_0 = 0.015$ (1.5%)** | `[C] [2, 5]` | Suất cản lăn riêng ray thép $w_0 = 0.015$ ($15\text{ kg/tấn}$) | Căn cứ TCVN 4244:2005 §2.4.7.2.2 [2] và phép tính kiểm ở SSoT P-13 (giả định `[C]`) | Chưa có tài liệu nguồn trong kho; kiểm chứng lại với tình trạng bảo dưỡng ray thực tế. |
| **4** | **Hệ số bám dính ray thép $\varphi = 0.20$** | `[C] [4]` | Hệ số bám dính chống trượt bánh xe trên ray thép $\varphi = 0.20$ | Căn cứ Bài giảng TĐĐ (Thầy Đỉnh) [4, Bài 4, tr. 43] | Đã xác minh trong bài giảng [4]; hệ số an toàn bám $k_{\text{bám}} \approx 1.52 \ge 1.20$. |
| **5** | **Hiệu suất truyền động cơ khí $\eta = 0.90$** | `[C] [4]` | Chuẩn hóa $\eta = 0.90$ (P-15) | Hộp giảm tốc bánh răng trụ 3 cấp kèm khớp nối và ổ lăn ngâm dầu; kiểm tra lại ở Khối 2. | Đo đạc hoặc tra bảng chính thức nhà sản xuất hộp số tại Khối 2/Khối 3 (`SOW-2.1`, `SOW-3.1`). |
| **6** | **Thời gian đáp ứng mô-men $< 10\text{ ms}$** | `[C] [3, 8]` | Đã chuyển giao xuống Khối 3 (`Downstream Allocation`) | Năng lực biến tần công nghiệp điều khiển Vector RFOC (IEC 61800-2 [3], Shevchenko 2024 [8]) | Kiểm chứng qua mô phỏng mạch vòng dòng điện trên MATLAB/Simulink tại Khối 3/Khối 5. |
| **7** | **Điện áp DC-link $U_{\text{dc}} \le 780\text{ V}$ & Chopper** | `[C] [6, 8]` | Đã chuyển giao xuống Khối 2 & 3 (`Downstream Allocation`) | Dải điện áp DC tiêu chuẩn của biến tần $380\text{V AC}$ (đóng chopper tại $680\text{V} \div 720\text{V}$, trip tại $800\text{V}$) | Xác minh thông số kỹ thuật bộ biến tần cụ thể chọn mua tại Khối 2 & Khối 3 (`SOW-2.1`, `SOW-3.1`). |

> *Ghi chú quản lý rủi ro kỹ thuật:* Toàn bộ các giả định kỹ thuật `[C]` mang mã viện dẫn `[2], [3], [4], [5], [6], [7], [8]` ở trên đều có kế hoạch đóng băng hoặc kiểm chứng thực nghiệm tại Cổng Soát xét Thiết kế Sơ bộ (PDR) và Thử nghiệm Mô phỏng (Khối 4/5).
