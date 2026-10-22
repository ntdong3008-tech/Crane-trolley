# CẨM NANG DỰNG SƠ ĐỒ BIÊN (BOUNDARY DIAGRAM) VÀ SƠ ĐỒ THAM SỐ (P-DIAGRAM)
**Dự án áp dụng:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Xe Con Cầu Trục ($x = 2$)  
**Nhóm thực hiện:** 8.5-EMG | **Phụ trách chính:** Nghiêm Trọng Đông (*PM / SE Lead*)  
**Tài liệu tham chiếu:** `EVLEP003_HBK` (§5.2), Chuẩn DFMEA AIAG & VDA, Design for Six Sigma (DFSS), $TCVN\ 4244:2005$

---

## PHẦN I. SƠ ĐỒ BIÊN HỆ THỐNG (SYSTEM BOUNDARY DIAGRAM)

### 1. Mục đích Kỹ thuật tại Khối 1 (§5.2)
Trong luồng `EVLEP003_HBK`, **Boundary Diagram** là công cụ trực quan hóa phạm vi kỹ thuật của dự án trước khi đóng băng SRS tại cổng **SRR-EVT**:
* **Khoanh vùng trách nhiệm thiết kế:** Xác định rõ những phần tử thuộc **In-Scope** (nhóm 8.5-EMG phải tính chọn, thiết kế điều khiển và mô phỏng) và những phần tử thuộc **Out-of-Scope** (môi trường hoặc hệ thống lân cận chỉ đóng vai trò tác nhân giao tiếp).
* **Nhận diện 100% các giao diện (Interfaces):** Mọi đường cắt qua ranh giới biên hệ thống (*System Boundary*) tạo thành các yêu cầu giao diện bên ngoài (`SRS-E01..E04`), còn các đường nối giữa các khối bên trong tạo thành cơ sở lập tài liệu **ICD (Interface Control Document)** ở Khối 2.

---

### 2. Quy chuẩn 4 Loại Đường Tương Tác Vật Lý Trên Sơ Đồ Biên
Khi vẽ Boundary Diagram, mọi mũi tên nối giữa các khối phải được gắn nhãn theo 4 loại trao đổi vật lý chuẩn SE:
* **`[P]` — Physical / Mechanical (Cơ học / Kết cấu):** Truyền mô-men xoắn ($M$), lực kéo tiếp tuyến ($F_k$), lực cản tĩnh ($F_c$), liên kết gá lắp cơ khí, tiếp xúc lăn kèm ma sát ($\mu$).
* **`[E]` — Energy / Electrical Power (Năng lượng / Điện năng):** Nguồn xoay chiều 3 pha $380\text{V}/50\text{Hz}$, dòng điện 3 pha cấp cho stato động cơ, công suất hãm tái sinh truyền về DC-bus và xả qua điện trở $R_h$.
* **`[I]` — Information / Signal (Thông tin / Tín hiệu điều khiển):** Lệnh đặt vận tốc $v_{ref}$, lệnh chọn chiều Tiến/Lùi, tín hiệu nút dừng khẩn cấp (`E-Stop`), tín hiệu công tắc hành trình (`Limit Switch`), xung phản hồi tốc độ từ `Encoder`.
* **`[M]` — Material / Thermal (Nhiệt lượng / Môi trường):** Nhiệt lượng tổn hao ($\Delta P$) tỏa ra môi trường xung quanh từ cuộn dây động cơ và cụm điện trở xả hãm $R_h$ trong chế độ làm việc $S3$.

---

### 3. Cấu Trúc Sơ Đồ Biên Chuẩn Của Hệ Truyền Động Xe Con Cầu Trục ($x = 2$)

```
  [NGƯỜI VẬN HÀNH (OPERATOR)]                        [LƯỚI ĐIỆN CÔNG NGHIỆP 3 PHA]
   (Out-of-Scope)                                     380V / 50Hz +/- 10% (Out-of-Scope)
         │                                                          │
         │ [I1]: Lệnh tốc độ v_ref, Tiến/Lùi, E-Stop                │ [E1]: Nguồn 3 pha 380VAC
         ▼                                                          ▼
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║ ĐƯỜNG BIÊN HỆ THỐNG (SYSTEM BOUNDARY: HỆ TRUYỀN ĐỘNG ĐIỆN XE CON CẦU TRỤC - IN-SCOPE)    ║
║                                                                                          ║
║  ┌──────────────────────────────┐     [I3]: Lệnh điều khiển     ┌─────────────────────┐  ║
║  │ 1. KHỐI LOGIC AN TOÀN &      │ ────────────────────────────► │ 2. BIẾN TẦN AC      │  ║
║  │    TẠO QUỸ ĐẠO MỀM (S-CURVE) │                               │    (Mạch lực + FOC) │  ║
║  └──────────────────────────────┘                               └─────────────────────┘  ║
║         ▲                  │                                       │       ▲       │     ║
║         │ [I2]             │ [I4]: Lệnh đóng/nhả phanh        [E2] │  [I5] │  [E3] │     ║
║  ┌──────┴───────────┐      ▼                                       ▼       │       ▼     ║
║  │ 7. CÔNG TẮC      │  ┌────────────────────┐      [P1]     ┌─────────────────┐ ┌──────┐ ║
║  │    HÀNH TRÌNH    │  │ 5. PHANH ĐIỆN TỪ   │ ────────────► │ 3. ĐỘNG CƠ KĐB  │ │ 6.R_h│ ║
║  └──────────────────┘  └────────────────────┘               │    3 PHA +      │ │ Xả   │ ║
║         ▲                                                   │    ENCODER      │ │ Hãm  │ ║
║         │ [P4]: Chạm cữ hai đầu dầm                         └─────────────────┘ └──────┘ ║
║         │                                                          │               │     ║
║         │                                                     [P2] │ Mô-men trục   │[M1] ║
║         │                                                          ▼               │     ║
║         │                                                   ┌─────────────────┐    │     ║
║         │                                                   │ 4. HỘP GIẢM TỐC │    │     ║
║         │                                                   │    & BÁNH XE    │    │     ║
║         │                                                   └─────────────────┘    │     ║
╚═════════╪══════════════════════════════════════════════════════════╪═══════════════╪═════╝
          │                                                          │               │
          │                       [P3]: Lực kéo, Ma sát ray (mu),    │               ▼
          │                             Lực cản tĩnh & Nhiễu lắc tải │        [MÔI TRƯỜNG]
          ▼                                                          ▼        Tỏa nhiệt S3
  [DẦM CHÍNH CẦU TRỤC & ĐƯỜNG RAY]         [CƠ CẤU NÂNG HẠ (m_nh = 222 kg, h = 12 m)
   (Out-of-Scope: Hệ số ma sát 0.15-0.25)   & TẢI TRỌNG NÂNG ĐỊNH MỨC (Q = 12,222 kg)]
                                            (Out-of-Scope: Đóng vai trò tạo tải & quán tính)
```

### 4. Bảng Phân Định Ranh Giới Phạm Vi (Scope Definition Table)

| Phân loại | Các phần tử bao gồm | Vai trò và Cách xử lý trong Đồ án ($x = 2$) |
| :--- | :--- | :--- |
| **Trong phạm vi**<br>*(In-Scope)* | 1. Khối Logic an toàn & Bộ tạo quỹ đạo S-Curve<br>2. Biến tần AC tích hợp thuật toán điều khiển FOC<br>3. Động cơ KĐB 3 pha roto lồng sóc<br>4. Hộp giảm tốc ($i \approx 100$) và cụm bánh xe di chuyển<br>5. Phanh cơ điện từ thường đóng<br>6. Mạch Chopper & Điện trở xả hãm $R_h$<br>7. Cảm biến tốc độ (Encoder) & Công tắc hành trình | Nhóm 8.5-EMG chịu trách nhiệm **tính chọn công suất, xác định 14 tham số động cơ, tổng hợp bộ điều khiển PI (Module & Đối xứng), thiết kế logic trạng thái và mô phỏng kiểm chứng** $100\%$ trên MATLAB/Simulink. |
| **Ngoài phạm vi**<br>*(Out-of-Scope)* | 1. Lưới điện nhà xưởng 3 pha $380\text{V}/50\text{Hz}$<br>2. Kết cấu thép dầm cầu trục và đường ray xe con<br>3. Cơ cấu nâng hạ ($m_{nh} = 222\text{ kg}$, cáp dài $h = 12\text{ m}$)<br>4. Tải trọng nâng ($Q = 12,222\text{ kg}$)<br>5. Hệ thống chống lắc chủ động bằng camera quang học | Không thiết kế kết cấu dầm hay hệ truyền động nâng hạ; chỉ quy đổi chúng thành **điều kiện biên và nhiễu đầu vào** (lực cản tĩnh $F_c$, mô-men cản $M_c$, mô-men quán tính quy đổi $J_{qđ}$ và nhiễu dao động con lắc đơn chiều dài $h = 12\text{ m}$). |

---

## PHẦN II. SƠ ĐỒ THAM SỐ P-DIAGRAM (PARAMETER DIAGRAM — SIX SIGMA)

### 1. Mục đích Kỹ thuật tại Khối 1 (§5.2)
**P-Diagram** (Parameter Diagram) là công cụ cốt lõi của phương pháp **Thiết kế Bền vững (Robust Design / Design for Six Sigma)** nhằm mục đích:
1. Liệt kê đầy đủ **5 yếu tố nhiễu ($N_1 \div N_5$)** tác động lên hệ truyền động xe con trong thực tế.
2. Xác định rõ các **Biến điều khiển (Control Factors / CTS — Critical-to-System)** mà kỹ sư có thể tinh chỉnh để hệ thống luôn đạt **Đầu ra mong muốn (CTQ — Critical-to-Quality)** bất chấp nhiễu.
3. Dự báo trước các **Trạng thái lỗi (Error States)** để chuyển giao sang phân tích **DFMEA L1** ở Khối 2.

---

### 2. Sơ Đồ Cấu Trúc P-Diagram Của Hệ Truyền Động Xe Con Cầu Trục ($x = 2$)

```
                 ┌──────────────────────────────────────────────────────────┐
                 │           3. CÁC YẾU TỐ NHIỄU (NOISE FACTORS)            │
                 │ - N1 (Biến thiên tải): Q thay đổi từ 0 kg đến 12,222 kg  │
                 │       (kèm cơ cấu nâng m_nh = 222 kg)                    │
                 │ - N2 (Nhiễu động học): Lắc tải trên cáp dài h = 12 m     │
                 │ - N3 (Ma sát tiếp xúc): Hệ số ma sát ray mu = 0.15..0.25 │
                 │ - N4 (Nhiễu nguồn cấp): Điện áp lưới 380V +/- 10%        │
                 │ - N5 (Nhiệt độ S3): Trôi điện trở R_s, R_r khi phát nhiệt│
                 └────────────────────────────┬─────────────────────────────┘
                                              │
                                              ▼
┌────────────────────────────┐   ╔═════════════════════════╗   ┌───────────────────────────────────┐
│ 1. TÍN HIỆU VÀO (INPUTS)   │   ║                         ║   │ 4. ĐẦU RA MONG MUỐN (CTQ)         │
│ - Lệnh đặt tốc độ:         │   ║   HỆ TRUYỀN ĐỘNG ĐIỆN   ║   │ - CTQ-1: v_max = 0.12 m/s         │
│   v_ref (0 -> 0.12 m/s)    ├──►║    XE CON CẦU TRỤC      ├──►│          (sai số tĩnh e_xl <= 5%) │
│ - Lệnh chiều chuyển động:  │   ║   (3 pha KĐB + Biến tần ║   │ - CTQ-2: Gia tốc |a| <= 0.5 m/s^2 │
│   Tiến (Fwd) / Lùi (Rev)   │   ║    FOC + Encoder)       ║   │ - CTQ-3: Độ giật |rho| <= 2 m/s^3 │
│ - Tín hiệu an toàn:        │   ║                         ║   │ - CTQ-4: Quá điều chỉnh <= 10%    │
│   E-Stop, Limit Switch     │   ╚═════════════════════════╝   │ - CTQ-5: Dừng E-Stop <= 2.0 s     │
└────────────────────────────┘                ▲                └───────────────────────────────────┘
                                              │                                  │
                 ┌────────────────────────────┴─────────────────────────────┐    │ (Nếu mất kiểm soát)
                 │        2. CÁC BIẾN ĐIỀU KHIỂN (CONTROL FACTORS / CTS)    │    ▼
                 │ - CTS-1: Tham số quỹ đạo S-Curve (giới hạn dốc a, rho)   │  ┌───────────────────────────────────┐
                 │ - CTS-2: Bộ điều khiển PI dòng i_d, i_q (Tối ưu Module)  │  │ 5. TRẠNG THÁI LỖI (ERROR STATES)  │
                 │ - CTS-3: Bộ điều khiển PI tốc độ omega (Tối ưu Đối xứng) │  │ - Vọt lố tốc độ (> 10%), sai số   │
                 │ - CTS-4: Tỷ số truyền hộp số (i) & Công suất động cơ P_đm│  │ - Giật cơ khí, trượt bánh trên ray│
                 │ - CTS-5: Giá trị điện trở xả hãm R_h & Ngưỡng Chopper    │  │ - Dao động lắc tải biên độ lớn    │
                 └──────────────────────────────────────────────────────────┘  │ - Quá áp DC-bus, quá nhiệt S3     │
                                                                               └───────────────────────────────────┘
```

---

### 3. Bảng Chốt Sơ Bộ Chỉ Tiêu CTQ Và CTS (Mối Liên Hệ Giữa Khối 1 Và Khối 2/3)

Tại **Khối 1 (§5.2)**, yêu cầu công việc thứ tư quy định phải **"chốt sơ bộ CTQ / CTS"**. Bảng dưới đây thiết lập ma trận ánh xạ giữa các chỉ tiêu chất lượng đầu ra (**CTQ**) và các thông số thiết kế hệ thống (**CTS**) tương ứng:

| Mã CTQ | Chỉ tiêu Chất lượng Đầu ra (CTQ - Critical to Quality) | Ngưỡng nghiệm thu bắt buộc ($x = 2$) | Mã CTS đối ứng | Thông số Thiết kế Hệ thống kiểm soát (CTS - Critical to System) | Thành viên chịu trách nhiệm tính chọn |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **`CTQ-1`** | Vận tốc di chuyển ngang xác lập và sai số tĩnh | $v_{\max} = 0.12\text{ m/s}$<br>$e_{xl} \le 5\%$ | **`CTS-3`**<br>**`CTS-4`** | Thành phần tích phân của bộ điều khiển PI tốc độ ($\omega$); độ phân giải Encoder; tỷ số truyền hộp giảm tốc $i$. | Trần Đỗ Khải & Đặng Nguyên Bình |
| **`CTQ-2`** | Gia tốc dài cực đại khi khởi động, hãm và đảo chiều | $\|a(t)\|_{\max} \le 0.5\text{ m/s}^2$ | **`CTS-1`**<br>**`CTS-4`** | Hệ số giới hạn độ dốc gia tốc trong bộ tạo quỹ đạo S-Curve; giới hạn mô-men/dòng điện đỉnh $i_{q\_\max}$ của biến tần. | Nguyễn Bá Hưng & Trần Đỗ Khải |
| **`CTQ-3`** | Độ giật cơ học cực đại (đạo hàm gia tốc) | $\|\rho(t)\|_{\max} \le 2.0\text{ m/s}^3$ | **`CTS-1`** | Tham số thời gian làm trơn góc uốn (Jerk time constant) của bộ tạo quỹ đạo S-Curve. | Nguyễn Bá Hưng |
| **`CTQ-4`** | Độ quá điều chỉnh tốc độ (Overshoot) trước nhiễu tải $Q = 12,222\text{ kg}$ và ma sát $\mu = 0.15 \div 0.25$ | $\sigma\% \le 10\%$ | **`CTS-2`**<br>**`CTS-3`** | Bộ tham số $K_{p\_i}, T_{i\_i}$ mạch vòng dòng điện (Tối ưu Module) và $K_{p\_\omega}, T_{i\_\omega}$ mạch vòng tốc độ (Tối ưu Đối xứng). | Trần Đỗ Khải |
| **`CTQ-5`** | Thời gian dừng khẩn cấp E-Stop & An toàn điện áp DC-bus khi hãm tái sinh | $t_{stop} \le 2.0\text{ s}$<br>$U_{dc} \le U_{dc\_\max}$ | **`CTS-5`** | Giá trị điện trở xả hãm $R_h$ ($\Omega$), công suất chịu nhiệt của $R_h$ ($\text{kW}$), mô-men giữ của phanh điện từ và logic cắt khẩn cấp. | Đặng Nguyên Bình & Nguyễn Bá Hưng |