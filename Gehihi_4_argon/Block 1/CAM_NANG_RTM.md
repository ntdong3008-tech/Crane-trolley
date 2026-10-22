# CẨM NANG XÂY DỰNG VÀ QUẢN TRỊ MA TRẬN TRUY XUẤT YÊU CẦU (RTM)
**Dự án áp dụng:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Xe Con Cầu Trục ($x = 2$)  
**Nhóm thực hiện:** 8.5-EMG | **Phụ trách chính:** Nguyễn Hải Trung (*Doc Lead*) & Nghiêm Trọng Đông (*PM/SE Lead*)  
**Tiêu chuẩn áp dụng:** *NASA Systems Engineering Handbook* (Mục 6.2 & Phụ lục D), ISO/IEC/IEEE 29148, `EVLEP003_HBK`

---

## 1. BẢN CHẤT VÀ VAI TRÒ SỐNG CÒN CỦA RTM TRONG KỸ THUẬT HỆ THỐNG

Trong quy trình `EVLEP003_HBK`, **RTM (Requirements Traceability Matrix — Ma trận Truy xuất Yêu cầu)** là công cụ xương sống kết nối toàn bộ các khối công việc từ **Khối 1 (§5.2)**, **Khối 3 (§5.4)** đến **Khối 5 (§5.6)**:
* **Tại Khối 1 (Cổng SRR-EVT):** Yêu cầu bắt buộc là *"Lập DVP&R L0 + RTM ánh xạ $100\%$ yêu cầu"* và *"truy xuất SRS $\to$ PRD"*.
* **Tại Khối 3 (Cổng CDR-EVT):** Yêu cầu bắt buộc là *"RTM bao phủ $100\%$* và *"Nộp bảng ánh xạ V-Model: mỗi khối có phép thử đối xứng"*.
* **Tại Khối 5 (Cổng SIR-EVT):** Yêu cầu bắt buộc là *"Đóng hết NCR trọng yếu chu kỳ A; cập nhật RTM, ICD"*.

---

## 2. NGUYÊN LÝ TRUY XUẤT HAI CHIỀU (BIDIRECTIONAL TRACEABILITY)

Theo **Mục 6.2.1.2 (Requirements Traceability)** trong *NASA Systems Engineering Handbook*, một ma trận RTM chuẩn phải đảm bảo khả năng dò tìm theo cả **hai chiều ngược nhau**:

```
       CHIỀU TRUY XUẤT XUÔI (FORWARD TRACEABILITY: Đảm bảo độ phủ 100% đầu bài)
  ──────────────────────────────────────────────────────────────────────────────────►
  [Đề bài gốc x=2 / TCVN 4244] ──► [Mã PRD] ──► [Mã SRS] ──► [Khối Kiến trúc / Simulink] ──► [Mã Test DVP&R]
  ◄──────────────────────────────────────────────────────────────────────────────────
       CHIỀU TRUY XUẤT NGƯỢC (BACKWARD TRACEABILITY: Chống vẽ thừa / Gold-plating)
```

### A. Truy xuất xuôi (Forward Traceability: Từ Nhu cầu $\to$ Kiểm thử)
* **Mục đích:** Chứng minh rằng **mọi thông số trong tờ đề bài gốc ($x=2$)** ($Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg}$, $h = 12\text{ m}$, $v_{\max} = 0.12\text{ m/s}$, $a_{\max} \le 0.5\text{ m/s}^2$, $\rho_{\max} \le 2\text{ m/s}^3$) và mọi yêu cầu của môn học đều đã được chuyển hóa thành yêu cầu kỹ thuật (`SRS`), được phân bổ vào một khối tính toán/mô phỏng cụ thể và có ít nhất một kịch bản kiểm thử (`DVP&R`) kiểm chứng.
* **Ứng dụng khi có thay đổi (Impact Analysis):** Nếu giảng viên hướng dẫn yêu cầu thay đổi một giả định (ví dụ đổi hệ số ma sát ray hoặc thời gian dừng), nhìn theo chiều xuôi của RTM sẽ chỉ ra ngay những câu SRS nào, những công thức tính nào của Bình/Khải và những kịch bản Simulink nào của P.V.Hưng cần chạy lại.

### B. Truy xuất ngược (Backward Traceability: Từ Kiểm thử & Thiết kế $\to$ Nhu cầu gốc)
* **Mục đích:** Chứng minh rằng mọi linh kiện trong bảng BOM, mọi mạch vòng điều khiển trong Simulink và mọi bài test đều phục vụ cho một yêu cầu chính đáng ở cấp cao hơn.
* **Quản lý Yêu cầu Phái sinh (Derived Requirements):**
  * Trong quá trình phân rã kỹ thuật ở Khối 1 và Khối 2, sẽ có những yêu cầu kỹ thuật không nằm trực tiếp trong câu chữ của tờ đề bài gốc nhưng bắt buộc phải sinh ra do lựa chọn giải pháp công nghệ (ví dụ: Nhóm chọn **Concept C — Biến tần FOC + Động cơ KĐB** thì sinh ra yêu cầu phái sinh là phải khống chế từ thông $\psi_{rd}$ ổn định ở định mức và phải có mạch Chopper + điện trở xả $R_h$ bảo vệ quá áp DC-bus).
  * Trên RTM, các yêu cầu này không được để trống cột nguồn mà phải ghi rõ **`Derived (từ Concept C / PRD-xx)`** kèm lý giải kỹ thuật để SE Lead phê duyệt.

---

## 3. ÁNH XẠ ĐỐI XỨNG TRÊN MÔ HÌNH CHỮ V (V-MODEL SYMMETRIC MAPPING)

Để đáp ứng yêu cầu tại **Khối 3 (§5.4)**: *"Nộp bảng ánh xạ V-Model: mỗi khối có phép thử đối xứng"*, ma trận RTM của nhóm 8.5-EMG phải thể hiện rõ sự đối xứng giữa nhánh trái (Phân rã thiết kế) và nhánh phải (Tích hợp & Kiểm chứng):

| Tầng trên V-Model | Nhánh Trái: Đặc tả & Thiết kế (Left Wing) | $\leftrightarrow$ | Nhánh Phải: Kiểm chứng & Nghiệm thu (Right Wing) | Phụ trách đối xứng (Thiết kế $\leftrightarrow$ Kiểm thử) |
| :---: | :--- | :---: | :--- | :--- |
| **Tầng 0: Nhu cầu & Khái niệm** | Đề bài gốc ($x=2$) + **PRD (Frozen)** + ConOps | $\leftrightarrow$ | **Nghiệm thu Sản phẩm (System Validation):** Bảo vệ đồ án & Đánh giá thỏa mãn đề bài gốc | Nghiêm Trọng Đông $\leftrightarrow$ TS. Nguyễn Duy Đỉnh |
| **Tầng 1: Cấp Hệ thống (L0)** | **SRS Baseline A** (18 yêu cầu: `F`, `L`, `S`, `P`, `E`) | $\leftrightarrow$ | **DVP&R Level 0 (System Verification):** Chạy kịch bản tổng thể trên Simulink đo $v, a, \rho, e_{xl}, \sigma\%, t_{stop}$ | Nguyễn Hải Trung $\leftrightarrow$ Phạm Văn Hưng |
| **Tầng 2: Cấp Kiến trúc (L1)** | **SAD & ICD** (Sơ đồ cấu trúc truyền động FOC, Đồ thị phụ tải 4 góc phần tư, Giao diện cơ-điện) | $\leftrightarrow$ | **Integration Test (SIR-EVT):** Kiểm tra ghép nối mạch lực - bộ điều khiển - tải cơ học 4 góc phần tư | Đặng Nguyên Bình & Nguyễn Bá Hưng $\leftrightarrow$ Phạm Văn Hưng |
| **Tầng 3: Cấp Phân hệ Chi tiết (L2)** | **Thiết kế chi tiết:** 14 tham số động cơ, Bộ PI dòng ($i_d, i_q$), Bộ PI tốc độ ($\omega$), Quỹ đạo S-Curve, Điện trở $R_h$ | $\leftrightarrow$ | **Subsystem / Unit Verification (DVP&R L1/L2):** Kiểm nghiệm đáp ứng bước nhảy dòng điện $i_q$, kiểm tra nhiệt $R_h$ | Trần Đỗ Khải & Đặng Nguyên Bình $\leftrightarrow$ Phạm Văn Hưng |

---

## 4. CẤU TRÚC BẢNG RTM CHUẨN ÁP DỤNG CHO NHÓM 8.5-EMG (18 YÊU CẦU)

Dưới đây là cấu trúc bảng RTM chuẩn hóa mà **Nguyễn Hải Trung (Doc Lead)** sử dụng để quản lý toàn bộ 18 yêu cầu của dự án:

| Mã RTM | Nguồn Gốc (Đề bài / TCVN) | Mã PRD (`PRD-ID`) | Mã SRS (`SRS-ID`) | Tóm tắt Yêu cầu Kỹ thuật | Phân bổ Kiến trúc / Phân hệ (SAD / Module) | Mục Báo cáo / Khối Simulink thực thi | Mã Kiểm chứng (`DVP-ID`) | Phương pháp V&V | Chủ sở hữu (R) | Trạng thái cổng |
| :---: | :--- | :---: | :---: | :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **`RTM-01`** | Đề $0\sim 9$ ($x=2$): Tải trọng định mức | `PRD-01` | `SRS-F01` | Mang tải định mức $Q = 12,222\text{ kg}$ | Động cơ KĐB + Hộp giảm tốc + Cụm bánh xe | Mục tính chọn công suất & Khối tải cơ học Simulink | `DVP-L0-01` | A + S | Đ.N. Bình | Frozen (SRR) |
| **`RTM-02`** | Đề $0\sim 9$ ($x=2$): Khối lượng nâng hạ | `PRD-01` | `SRS-F02` | Mang khối lượng cơ cấu nâng $m_{nh} = 222\text{ kg}$ | Động cơ KĐB + Hộp giảm tốc ($J_{qđ}, M_{qđ}$) | Công thức quy đổi quán tính & lực cản tĩnh $F_c$ | `DVP-L0-01` | A + S | Đ.N. Bình | Frozen (SRR) |
| **`RTM-03`** | Đề $0\sim 9$ ($x=2$): Tốc độ tối đa | `PRD-02` | `SRS-F03` | Vận tốc di chuyển tối đa $v_{\max} = 0.12\text{ m/s}$ | Biến tần FOC + Động cơ + Hộp số ($i \approx 100$) | Khối tạo tốc độ đặt & Mạch vòng PI tốc độ $\omega$ | `DVP-L0-02` | S | T.Đ. Khải | Frozen (SRR) |
| **`RTM-04`** | Đề $0\sim 9$ ($x=2$): Gia tốc cực đại | `PRD-03` | `SRS-F04` | Giới hạn gia tốc cực đại $a_{\max} \le 0.5\text{ m/s}^2$ | Khối tạo quỹ đạo mềm S-Curve + Bộ PI tốc độ | Khối S-Curve Ramp Generator trên Simulink | `DVP-L0-03` | S | N.B. Hưng & T.Đ. Khải | Frozen (SRR) |
| **`RTM-05`** | Đề $0\sim 9$ ($x=2$): Độ giật cực đại | `PRD-04` | `SRS-F05` | Giới hạn độ giật cực đại $\rho_{\max} \le 2\text{ m/s}^3$ | Khối tạo quỹ đạo mềm S-Curve (giới hạn $\text{d}a/\text{d}t$) | Khối S-Curve & Khối đạo hàm kiểm tra $\rho(t)$ | `DVP-L0-04` | S | N.B. Hưng | Frozen (SRR) |
| **`RTM-06`** | Đề $0\sim 9$ ($x=2$): Chiều cao nâng $h=12\text{ m}$ | `PRD-05` | `SRS-P03` | Kháng nhiễu lắc tải với chiều dài cáp $h = 12\text{ m}$ | Mạch vòng tốc độ PI (Tối ưu Đối xứng) + S-Curve | Khối nhiễu mô-men tải phụ thuộc góc lắc cáp | `DVP-L0-08` | S | T.Đ. Khải & P.V. Hưng | Frozen (SRR) |
| **`RTM-07`** | Yêu cầu đề: Thiết kế logic hoạt động | `PRD-06` | `SRS-L01` | Chu trình chuyển trạng thái `Ready`, `Run`, `Braking`, `Fault` | Khối Logic điều khiển trung tâm (Stateflow / Logic) | Sơ đồ trạng thái & Khối Logic trên Simulink | `DVP-L0-09` | D + S | N.B. Hưng | Frozen (SRR) |
| **`RTM-08`** | $TCVN\ 4244:2005$ & An toàn | `PRD-06` | `SRS-S01` | Dừng khẩn cấp E-Stop trong thời gian $\le 2.0\text{ s}$ | Mạch an toàn E-Stop + Phanh cơ + Xả hãm $R_h$ | Kịch bản kích xung `E-Stop` ở $v = 0.12\text{ m/s}$ | `DVP-L0-06` | S + D | N.B. Hưng & Đ.N. Bình | Frozen (SRR) |

---

## 5. CÁC LỖI SAI TRÊN RTM KHIẾN CỔNG SRR-EVT VÀ CDR-EVT ĐÁNH TRƯỢT

1. **Lỗi Yêu cầu Mồ côi (Orphan Requirements):** Có câu `SRS` nhưng cột `PRD-ID` bị bỏ trống và cũng không có giải trình `Derived`.
2. **Lỗi Đứt gãy Kiểm chứng (Unverified Requirements):** Có câu `SRS` nhưng không gắn với bất kỳ mã `DVP-ID` nào (độ phủ kiểm chứng $< 100\%$).
3. **Lỗi Lệch Mã Định Danh (Broken Links):** Sửa mã hoặc nội dung trong file `SRS` nhưng quên cập nhật sang bảng `RTM` và `DVP&R L0`, dẫn đến cùng một mã `SRS-F03` nhưng ở hai file lại ghi hai nội dung khác nhau.
4. **Lỗi Phân bổ Mơ hồ (Vague Allocation):** Cột "Phân bổ Kiến trúc" chỉ ghi chung chung là *"Hệ thống"* thay vì chỉ đích danh phân hệ chịu trách nhiệm (ví dụ: *Bộ điều khiển PI dòng $i_q$*, *Khối S-Curve*, hay *Cụm điện trở xả hãm $R_h$*).