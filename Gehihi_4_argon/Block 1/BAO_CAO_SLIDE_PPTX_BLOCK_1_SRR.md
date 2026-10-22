# BÁO CÁO KỊCH BẢN SLIDE POWERPOINT KHỐI 1 (CỔNG 2: SRR-EVT) — NHÓM 8.5-EMG (ĐỀ $x = 2$)

> **Tên file `.pptx` xuất ra:** `Bao_cao_Tien_do_Khoi_1_SRR_Nhom_8_5_EMG.pptx`  
> **Template gốc kế thừa:** `Báo cáo hàng tuần\Mô tả nguyên lý công nghệ.pptx` (kết hợp trích xuất sơ đồ từ `Báo cáo hàng tuần\SRS-diagram.pptx`)  
> **Hồ sơ kỹ thuật gốc ánh xạ 100%:**
> 1. `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md` (`SRS-8.5EMG-TROLLEY-v1.1 — Baseline A`)
> 2. `rtm_dvp_xe_con_cau_truc_x2_nhom_8_5_emg.md` (`RTM-DVP-8.5EMG-TROLLEY-v1.1 — Baseline A`)
> 3. `00_Bang_thong_so_goc.md` (SSoT) & `SLIDE_PPTX_RULES_SE.md` (Đề $x = 2$: $Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg} \pm 2\%$, $m_{xc} = 1,800\text{ kg} \pm 5\% \Rightarrow M_\Sigma = 14,244\text{ kg} \pm 4.5\%$, $m_{\text{tĩnh}} = 2,022\text{ kg} \pm 4.5\%$, $h = 12.0\text{ m} \pm 0.1\text{ m}$, $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$, $D \ge 10:1$, $|a(t)| \le 0.50\text{ m/s}^2$ [$+0\% / -10\%$], $|\rho(t)| \le 2.00\text{ m/s}^3$ [$+0\% / -10\%$], $e_{xl} \le 5.0\%$, $M_p \le 10.0\%$, $w_0 = 0.015 \pm 0.003$, $\varphi = 0.20$, $\eta \ge 0.94$, $U_{\text{dc}} \le 780\text{ V DC}$, $S3\text{--}40\% \pm 2\%$, $k_{dt} \in [1.20;\ 1.50]$, $\lambda_{\max} \ge 2.0$).
> **Cấu trúc bộ Slide (22 Slides = 16 Main Slides + 6 Backup Slides `B1-1..B1-6`):** Cô đọng tối đa chữ trên mặt slide ($\le 14$ từ/ô, 0% tràn khung), nhúng trực tiếp hình ảnh thật từ `SRS-diagram.pptx` & `Mô tả nguyên lý công nghệ.pptx`, vẽ sơ đồ khối bằng Native PowerPoint Shapes và đặt toàn bộ lời giải thích chi tiết vào `Speaker Notes`.

---

## PHẦN A: 16 SLIDE CHÍNH THỨC (`MAIN DECK`: SLIDE 01 $\to$ SLIDE 16)

### SLIDE 01: TRANG BÌA (TITLE SLIDE — KẾ THỪA TEMPLATE ĐHBKHN)
* **Tiêu đề chính:** `THIẾT KẾ HỆ TRUYỀN ĐỘNG CƠ CẤU XE CON CẦU TRỤC`
* **Phụ đề Báo cáo Cổng 2 (`SRR-EVT`):** `BÁO CÁO TIẾN ĐỘ KHỐI 1 (GATE SRR-EVT): SƠ ĐỒ BIÊN, P-DIAGRAM, CHỈ TIÊU CTQ/CTS, ĐẶC TẢ SRS BASELINE A, MA TRẬN RTM & KẾ HOẠCH DVP&R L0 (ĐỀ X = 2)`
* **Nhóm thực hiện:** `NHÓM 8.5-EMG` — Nguyễn Bá Hưng (`20232107`), Đặng Nguyên Bình (`20231937`), Trần Đỗ Khải (`20232131`), Phạm Văn Hưng (`20232109`), Nguyễn Hải Trung (`20232344`), Nghiêm Trọng Đông (`20232001` — PM/SE Lead, STT 22 $\to x=2$).
* **Giảng viên hướng dẫn:** `TS. Nguyễn Duy Đỉnh`.

### SLIDE 02: TỔNG QUAN TIẾN ĐỘ KHỐI 1 (`WBS 1.0`) & LUỒNG CHUYỂN HÓA TỪ KHỐI 0 (`MCR` $\to$ `SRR-EVT`)
* **Header:** `MỞ ĐẦU: TỔNG QUAN KHỐI 1 (WBS 1.0) | CỔNG 2: SRR-EVT`
* **Action Title:** `Khối 1 chuyển hóa 8 mã PRD & Solution C thành 9 yêu cầu kỹ thuật hệ thống (4 FUNC + 5 PERM), khóa CTQ/CTS, RTM và DVP&R L0 có dung sai chuẩn hóa`
* **Bố cục:**
  - Trên: Lưu đồ chuỗi 5 bước chuyển hóa vẽ bằng **Native Chevron/Rounded Shapes** (`Khối 0: 8 PRD + 8 HoQ EC + Solution C` $\to$ `SOW-1.1: Boundary & P-Diagram (N1..N4)` $\to$ `SOW-1.1: 8 CTQ + 5 CTS` $\to$ `SOW-1.2: 9 SRS Kỹ thuật Hệ thống (4 FUNC + 5 PERM)` $\to$ `SOW-1.3: RTM 2 chiều + 9 DVP-L0 (3 TS)`).
  - Dưới: Bảng tổng hợp kết quả hoàn thành 3 gói công việc `SOW-1.1`, `SOW-1.2`, `SOW-1.3` kèm 4 thẻ chỉ số KPI nổi bật (`9 SRS Kỹ thuật Hệ thống`, `8 CTQ & 5 CTS có dung sai`, `100% RTM 2 chiều`, `9 Bài đo DVP-L0`).

### SLIDE 03: PHẦN 1 (`SOW-1.1`) — SƠ ĐỒ RANH GIỚI HỆ THỐNG TỔNG THỂ (`SYSTEM BOUNDARY DIAGRAM`)
* **Header:** `1. SƠ ĐỒ RANH GIỚI HỆ THỐNG (BOUNDARY DIAGRAM) | GÓI SOW-1.1`
* **Action Title:** `Sơ đồ Ranh giới khoanh vùng rõ Hệ truyền động Xe con In-Scope (FUNC & PERM) với 3 thực thể ngoài qua biên`
* **Bố cục 2 Cột (Nhúng ảnh thật + Bảng nguồn gốc):**
  - **Cột Trái:** Nhúng trực tiếp hình ảnh **Sơ đồ Ranh giới Hệ thống tổng thể** từ `Slide 5` của `SRS-diagram.pptx` (`srs_s05_sh2.png`), giữ nguyên tỷ lệ khung hình sắc nét.
  - **Cột Phải:** Bảng 5 thành phần / phân vùng trên Sơ đồ Biên (`1. Lưới điện 380V±10% / 50Hz±2%`, `2. Người vận hành (Tiến/Lùi/Chạy định mức/Dừng)`, `3. Cơ cấu nâng Q=12,222 kg, m_nh=222 kg, cáp h=12 m & Ray w_0=0.015, phi=0.20`, `4. Phân hệ CDM Biến tần + Chopper Rh + CU`, `5. Phân hệ Chấp hành ĐC KĐB S3 + Encoder + Phanh + Hộp số η=0.96 + Bánh xe d=0.25 m`).

### SLIDE 04: PHẦN 1 (`SOW-1.1`) — BÓC TÁCH 3 PHÂN VÙNG BIÊN & 10 GIAO DIỆN VẬT LÝ (`[P], [E], [I], [M]`)
* **Header:** `1. SƠ ĐỒ RANH GIỚI HỆ THỐNG | 10 GIAO DIỆN VẬT LÝ QUA BIÊN ([P], [E], [I], [M])`
* **Action Title:** `Bóc tách 3 phân vùng ranh giới và định lượng hóa 10 giao diện Vật lý [P], Năng lượng [E], Thông tin [I], Cơ học [M]`
* **Bố cục 2 Cột:**
  - **Cột Trái:** Nhúng 3 hình cắt lớp 3 phân vùng từ `Slide 6, 7, 8` của `SRS-diagram.pptx` (Môi trường ngoài $\to$ Hệ truyền động In-Scope $\to$ Khung tải & Hàng hóa).
  - **Cột Phải:** Bảng đặc tả 10 giao diện qua biên và nội bộ (`IF-01..10`) phân loại chuẩn `[P], [E], [I], [M]` theo `CAM_NANG_boundary_v_p_diagram.md` & `SRS Baseline A` §2.1.

### SLIDE 05: PHẦN 1 (`SOW-1.1`) — SƠ ĐỒ THAM SỐ HỆ THỐNG (`P-DIAGRAM`) THEO CHUẨN SIX SIGMA
* **Header:** `1. SƠ ĐỒ THAM SỐ HỆ THỐNG (PARAMETER DIAGRAM — P-DIAGRAM) | GÓI SOW-1.1`
* **Action Title:** `P-Diagram mô hình hóa 4 yếu tố nhiễu qua biên (N1..N4) và 6 yếu tố điều khiển (CF1..CF6) để triệt tiêu 4 lỗi (E1..E4)`
* **Bố cục 2 Cột (Nhúng ảnh thật + Bảng 5 khối P-Diagram):**
  - **Cột Trái:** Nhúng trực tiếp hình ảnh **Sơ đồ Tham số P-Diagram** từ `Slide 9` của `SRS-diagram.pptx` (`srs_s09_sh3.png`), giữ đúng tỷ lệ gốc.
  - **Cột Phải:** Bảng 5 thành phần chuẩn của P-Diagram từ `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md` §2.2:
    1. **Tín hiệu vào (`Input Signals`):** Lệnh Tiến/Lùi, cấp tốc độ Chạy định mức ($0.12\text{ m/s} \pm 5\%$) / Dừng chu trình, quỹ đạo đặt $\omega^*(t)$.
    2. **4 Yếu tố Nhiễu (`N1..N4`):** `N1` (Tải đổi $7.04\times$: $2,022 \pm 4.5\% \leftrightarrow 14,244 \pm 4.5\%\text{ kg}$); `N2` (Con lắc cáp $h = 12.0 \pm 0.1\text{ m}, \omega_p \in [0.899;\ 0.909]\text{ rad/s}$); `N3` (Lưới $380\text{V} \pm 10\%, 50\text{Hz} \pm 2\%$); `N4` (Nhiệt chu kỳ $S3\text{--}40\% \pm 2\%$ tăng $R_2$).
    3. **6 Yếu tố Điều khiển (`CF1..CF6`):** `CF1` (RFOC + 01 Encoder); `CF2` (PI dòng MO & PI tốc độ SO); `CF3` (S-Curve 7 đoạn $|a|\le 0.50, |\rho|\le 2.00$); `CF4` (Chopper + $R_h$ giữ $U_{\text{dc}} \le 780\text{V}$); `CF5` (Khóa chéo đảo chiều khi $|v| \le 0.002\text{ m/s}$ & giữ mô-men $0\text{ rpm}$); `CF6` (Định cỡ nhiệt $S3$, $k_{dt} \in [1.20;\ 1.50]$).
    4. **Đáp ứng Lý tưởng (`CTQ-01..08`):** Đạt $v_{\max}=0.12\text{ m/s} \pm 5\%$, $e_{xl}\le 5.0\%$, $M_p\le 10.0\%$, $|a|\le 0.50\text{ m/s}^2$, $|\rho|\le 2.00\text{ m/s}^3$, $U_{\text{dc}}\le 780\text{V}$, độ trôi dừng xe $\Delta s \le \pm 10\text{ mm}$.
    5. **4 Trạng thái Lỗi (`E1..E4`):** `E1` (Lắc tải / sốc hộp số — `RRM-01`); `E2` (Quá áp DC-Link — `RRM-02`); `E3` (Trượt tốc / trôi phanh — `RRM-03`); `E4` (Quá nhiệt $S3$ / dư công suất — `RRM-04`).

### SLIDE 06: PHẦN 1 (`SOW-1.1`) — CHỐT SƠ BỘ 8 CHỈ TIÊU CHẤT LƯỢNG (`CTQ-01..08`) & 5 AN TOÀN (`CTS-01..05`)
* **Header:** `1. CHỐT SƠ BỘ CHỈ TIÊU TRỌNG YẾU (CTQ & CTS) | GÓI SOW-1.1`
* **Action Title:** `Từ Sơ đồ Biên & P-Diagram, khóa cứng 8 chỉ tiêu chất lượng (CTQ-01..08) và 5 giới hạn an toàn vận hành (CTS-01..05) kèm dung sai định lượng`
* **Bố cục 2 Bảng Song song (Trái: 8 CTQ | Phải: 5 CTS):**
  - **Cột Trái:** Bảng 8 mã `CTQ-01..08` kèm ngưỡng dung sai khóa cứng và ánh xạ sang `SRS Baseline A` (`rtm_dvp_xe_con_cau_truc_x2_nhom_8_5_emg.md` §1.2).
  - **Cột Phải:** Bảng 5 mã `CTS-01..05` (An toàn vận hành chức năng & năng lượng trong phạm vi `FUNC & PERM`: `CTS-01` chống lắc & trượt bánh $k_{\text{bám}} \ge 1.20$, danh định $\approx 1.51$; `CTS-02` kẹp áp $U_{\text{dc}} \le 780\text{V}$; `CTS-03` giữ mô-men $0\text{ rpm}$ mở/khóa phanh tại $|v| \le 0.005\text{ m/s}, \Delta s \le \pm 10\text{ mm}$; `CTS-04` khóa chéo cấm đảo chiều khi $|v| > 0.002\text{ m/s}$; `CTS-05` biên nhiệt $S3$ $k_{dt}\in[1.20;1.50], \lambda_{\max}\ge 2.0$) (`rtm_dvp...md` §1.3).

### SLIDE 07: PHẦN 2 (`SOW-1.2`) — PHƯƠNG PHÁP LUẬN PHÂN RÃ `8 PRD + 8 HoQ EC` $\to$ `9 MÃ SRS KỸ THUẬT HỆ THỐNG`
* **Header:** `2. ĐẶC TẢ YÊU CẦU KỸ THUẬT HỆ THỐNG (SRS BASELINE A) | PHÂN RÃ NGUYÊN TỬ (SOW-1.2)`
* **Action Title:** `Áp dụng 3 quy tắc ISO/IEC/IEEE 29148 để phân rã 8 mã PRD & 8 mã HoQ EC thành đúng 9 yêu cầu kỹ thuật hệ thống (4 FUNC + 5 PERM)`
* **Bố cục:**
  - Trên: Hộp công thức cú pháp 5 thành phần chuẩn IEEE 29148 (`[Điều kiện biên] + [Chủ thể] + phải (shall) + [Hành động] + [Ngưỡng định lượng ± Dung sai]`).
  - Dưới: Bảng giải trình phép ánh xạ và phân rã từ 8 mã `PRD-FUNC-01..04` & `PRD-PERM-01..04` sang 9 mã `SRS-FUNC-01..04` & `SRS-PERM-01..05` từ `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md` §1.2.

### SLIDE 08: PHẦN 2 (`SOW-1.2`) — ĐẶC TẢ 4 YÊU CẦU KỸ THUẬT CHỨC NĂNG & LOGIC (`SRS-FUNC-01..04`)
* **Header:** `2. ĐẶC TẢ SRS BASELINE A | NHÓM 1: 4 YÊU CẦU CHỨC NĂNG & LOGIC (SRS-FUNC-01..04)`
* **Action Title:** `4 mã SRS-FUNC-01..04 khóa chặt điều khiển tách kênh 4 góc phần tư, quỹ đạo S-Curve 7 đoạn, phanh cơ & liên khóa logic, mạch xả hãm Rh`
* **Bố cục:**
  - Bảng 4 dòng (`SRS-FUNC-01` đến `SRS-FUNC-04`) cô đọng sắc nét theo đúng Bảng 3.2 của `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md` (kèm dung sai thời gian đáp ứng mô-men $\le 10\text{ ms}$, ngưỡng dừng phanh $\le 0.005\text{ m/s}$, độ trôi $\le \pm 10\text{ mm}$, áp hãm $\le 780\text{V}$).
  - Dưới: Sơ đồ chuỗi phối hợp đồng bộ **Mô-men giữ tại $0\text{ rpm}$ & Phanh cơ điện từ + Khóa chéo $|v| \le 0.002\text{ m/s}$** vẽ bằng **Native PowerPoint Shapes**.

### SLIDE 09: PHẦN 2 (`SOW-1.2`) — ĐẶC TẢ 5 YÊU CẦU KỸ THUẬT HIỆU NĂNG ĐỊNH LƯỢNG (`SRS-PERM-01..05`)
* **Header:** `2. ĐẶC TẢ SRS BASELINE A | NHÓM 2: 5 YÊU CẦU HIỆU NĂNG ĐỊNH LƯỢNG (SRS-PERM-01..05)`
* **Action Title:** `5 mã SRS-PERM-01..05 định lượng 100% lực kéo 14,244 kg, vận tốc 0.12 m/s ± 5%, sai lệch ≤ 5%, vọt lố ≤ 10%, |a| ≤ 0.50, |ρ| ≤ 2.00 và nhiệt S3`
* **Bố cục:**
  - Bảng 5 dòng (`SRS-PERM-01` đến `SRS-PERM-05`) cô đọng sắc nét theo đúng Bảng 3.3 của `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md`.
  - Dưới: 3 Thẻ kiểm chứng toán học nhanh (`Lực cản & Bám ray: F_c = 2.12 kN ± 0.42 kN, F_max = 9.25 kN ± 0.45 kN, k_bám = 1.51 > 1.20`, `Động học S-Curve: a ≤ 0.50 m/s², ρ ≤ 2.00 m/s³, góc lệch tĩnh θ_0 ≤ 2.92°`, `Định cỡ Nhiệt S3-40%: 1.20 ≤ k_dt ≤ 1.50, quá tải λ_max ≥ 2.0`).

### SLIDE 10: PHẦN 3 (`SOW-1.3`) — MA TRẬN TRUY XUẤT YÊU CẦU HAI CHIỀU: CHIỀU XUÔI (`FORWARD RTM`)
* **Header:** `3. MA TRẬN TRUY XUẤT YÊU CẦU HAI CHIỀU (BIDIRECTIONAL RTM) | CHIỀU XUÔI (SOW-1.3)`
* **Action Title:** `Ma trận RTM Chiều xuôi chứng minh 100% (8/8 mã PRD & 8/8 mã HoQ EC) được hiện thực hóa thành 9 mã SRS và 9 bài đo DVP-L0`
* **Bố cục:**
  - Trái (`w = 3.80"`): Sơ đồ Phễu Truy xuất 4 Tầng vẽ bằng **Native PowerPoint Shapes** (`8 PRD (4 FUNC + 4 PERM)` $\leftrightarrow$ `8 HoQ EC (w_j%)` $\leftrightarrow$ `9 SRS Kỹ thuật Hệ thống (8 CTQ + 5 CTS)` $\leftrightarrow$ `9 Bài đo DVP-L0 (3 TS)`) + Thẻ kiểm toán `0 Yêu cầu Mồ côi (Zero Orphan) & 0 Yêu cầu Thừa (Zero Gold-Plating)`.
  - Phải (`w = 8.70"`): Bảng 8 dòng Ma trận Truy xuất Xuôi (`Forward RTM` — Bảng 2.2 của `rtm_dvp_xe_con_cau_truc_x2_nhom_8_5_emg.md`).

### SLIDE 11: PHẦN 3 (`SOW-1.3`) — MA TRẬN TRUY XUẤT NGƯỢC & LIÊN KẾT CHUỖI `DMAIC` (`BACKWARD RTM`)
* **Header:** `3. MA TRẬN TRUY XUẤT YÊU CẦU HAI CHIỀU | CHIỀU NGƯỢC & CHUỖI DMAIC (SOW-1.3)`
* **Action Title:** `Ma trận RTM Chiều ngược kết nối khép kín 9 mã SRS với Tech Gaps (GAP-01..07), P-Diagram (N1..N4, CF1..CF6), Sổ rủi ro RRM và WBS`
* **Bố cục:**
  - Bảng tổng hợp truy xuất ngược theo cụm phân hệ (`SOW-3.1 Phần lực`, `SOW-3.3 Điều khiển RFOC & S-Curve`, `SOW-3.4 Logic & Phanh cơ`, `SOW-5.1 Mô phỏng con lắc`) thể hiện rõ sợi dây liên kết: `SRS ID` $\leftarrow$ `HoQ EC (w_j%)` $\leftarrow$ `GAP-01..07` $\leftarrow$ `Noise N1..N4 & Control CF1..CF6` $\leftarrow$ `RRM-01..05` $\to$ `Owner & DVP-L0` (Bảng 9 dòng đầy đủ nằm tại Backup `B1-4` & `B1-5`).

### SLIDE 12: PHẦN 4 (`SOW-1.3`) — PHƯƠNG PHÁP KIỂM CHỨNG (`A, S, I`) & 3 KỊCH BẢN TÍCH HỢP (`TS-01..03`)
* **Header:** `4. KẾ HOẠCH KIỂM CHỨNG CẤP HỆ THỐNG (DVP&R LEVEL 0) | 3 KỊCH BẢN TS-01..03 (SOW-1.3)`
* **Action Title:** `9 bài kiểm chứng DVP-L0 được tổ chức vào 3 kịch bản mô phỏng tích hợp (TS-01..03) có tiêm đủ 4 yếu tố nhiễu N1..N4`
* **Bố cục 2 Cột (Bảng 3 Kịch bản + Nhúng 2 Đồ thị Chuẩn):**
  - **Cột Trái:** 3 Thẻ phương pháp `A (Analysis — CDRL-01/02)`, `S (Simulation — CDRL-05)`, `I (Inspection — CDRL-03/04)` + Bảng 3 Kịch bản thử nghiệm tích hợp (`TS-01: Chu trình chuẩn S3-40% đủ 4 góc phần tư dưới N1 & N2`, `TS-02: Cưỡng bức đảo chiều đột ngột khi xe đang chạy v = +0.12 m/s`, `TS-03: Đối chứng Kaizen S-Curve 7 đoạn vs Linear Ramp ở cáp h = 12 m`).
  - **Cột Phải:** Nhúng trực tiếp 2 hình ảnh đồ thị chuẩn từ `Mô tả nguyên lý công nghệ.pptx`: **Hình 3.2 (Quỹ đạo S-curve 7 pha $s, v, a, \rho$)** và **Hình 3.3 (Đặc tính vận hành 4 góc phần tư & xả hãm $R_h$)**.

### SLIDE 13: PHẦN 4 (`SOW-1.3`) — BẢNG KẾ HOẠCH & TIÊU CHÍ NGHIỆM THU `DVP&R LEVEL 0` (`DVP-L0-01..09`)
* **Header:** `4. KẾ HOẠCH KIỂM CHỨNG (DVP&R LEVEL 0) | TIÊU CHÍ PASS / FAIL KHÓA CỨNG KÈM DUNG SAI`
* **Action Title:** `Mỗi bài đo DVP-L0-01..09 đều khóa cứng đại lượng trích xuất và ngưỡng nghiệm thu Pass/Fail kèm dung sai kỹ thuật định lượng`
* **Bố cục:**
  - Chia 2 bảng song song (Trái: 4 bài đo Chức năng `DVP-L0-01..04` | Phải: 5 bài đo Hiệu năng `DVP-L0-05..09`) hiển thị trọn vẹn 9/9 bài kiểm chứng trên mặt slide với câu chữ cô đọng (`Mã DVP`, `Mã SRS & PP`, `Đại lượng đo`, `Ngưỡng PASS kèm Dung sai khóa cứng`), đảm bảo cỡ chữ rõ ràng và không tràn khung.

### SLIDE 14: PHẦN 4 (`SOW-1.3`) — QUY CHUẨN KỸ THUẬT ĐO KIỂM SIMULINK & BỘ LỌC ĐẠO HÀM ĐỘ GIẬT $\rho(t)$
* **Header:** `4. KẾ HOẠCH KIỂM CHỨNG (DVP&R L0) | QUY CHUẨN ĐO GIA TỐC a(t) & ĐỘ GIẬT ρ(t) TRÊN SIMULINK`
* **Action Title:** `Khóa 3 quy tắc kỹ thuật Simulink (Solver Ts ≤ 10⁻⁴ s & Bộ lọc vi phân thực tế Gd(s)) để kiểm soát triệt để rủi ro RRM-05`
* **Bố cục:**
  - Trái: Hộp cảnh báo kỹ thuật giải thích tại sao cấm dùng khối `Derivative` thuần túy ($\text{d}/\text{d}t$) sau nhiễu xung PWM IGBT $f_{\text{PWM}} \ge 2\text{ kHz}$ (gây gai đạo hàm giả làm sai lệch bài đo độ giật).
  - Phải: 3 Quy tắc bắt buộc từ Mục 3.4 của `rtm_dvp_xe_con_cau_truc_x2_nhom_8_5_emg.md`:
    1. **Quy tắc 1 (`Solver & Sample Time`):** Dùng `ode4` / `ode23tb` với bước lấy mẫu $T_s \le 10^{-4}\text{ s}$ ($0.1\text{ ms}$).
    2. **Quy tắc 2 (`Trích xuất a(t) & Lọc thực tế ρ(t)`):** Lấy $a(t) = \frac{F_{\text{kéo}} - F_{\text{cản}} - F_{\text{lắc cáp}}}{m_{xc} + m_{nh}}$ trước khâu tích phân; đo độ giật thực tế qua khâu lọc vi phân chuẩn $G_d(s) = \frac{s}{T_f s + 1}$ ($T_f = 0.005 \div 0.01\text{ s}$).
    3. **Quy tắc 3 (`Post-Processing .m Script`):** Xuất `Structure with Time` ra MATLAB Workspace để chấm điểm tự động.
  - Dưới: Sơ đồ khối trích xuất $a(t)$ và $\rho(t)$ vẽ bằng **Native PowerPoint Shapes**.

### SLIDE 15: TỔNG KẾT ĐỐI CHIẾU CHECKLIST NGHIỆM THU CỔNG 2 (`SRR-EVT`) & BÀN GIAO SANG KHỐI 2 (`PDR-EVT`)
* **Header:** `5. TỔNG KẾT & CHECKLIST NGHIỆM THU CỔNG 2 (SRR-EVT) | MỞ KHÓA KHỐI 2 (PDR-EVT)`
* **Action Title:** `Hồ sơ Khối 1 hoàn thành 100% tiêu chí Cổng SRR-EVT (FLOW_REVIEW.md §5.2 & NASA Table 6.7-5), sẵn sàng đóng băng Baseline A`
* **Bố cục:**
  - Bảng đối chiếu 6 tiêu chí nghiệm thu Cổng 2 (`SRR-EVT`) từ Mục 4 của `rtm_dvp_xe_con_cau_truc_x2_nhom_8_5_emg.md` & Mục 5 của `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md`.
  - Hộp Quyết định Đóng cổng `SRR-EVT` (`FROZEN SRS BASELINE A`) và bàn giao đầu vào sang **Khối 2 (`WBS 2.0 — Kiến trúc Sơ bộ SAD/ICD, BOM & DFMEA`)**.

### SLIDE 16: TÀI LIỆU THAM KHẢO & THANK YOU ! (`slideLayout4`)
* **Tiêu đề Slide:** `TÀI LIỆU VIỆN DẪN THAM KHẢO & LỜI CẢM ƠN`
* **Nội dung hiển thị trên mặt Slide:** Liệt kê chuẩn hóa 10 Danh mục Tài liệu Viện dẫn Quốc tế phục vụ Báo cáo Hội đồng & Khách hàng giả định:
  1. `[1]` **Đề bài tập lớn Thiết kế TĐĐ Kỳ 2023.1** — Đề số 8: Xe con cầu trục ($x = 2$, STT 22), ĐHBK Hà Nội.
  2. `[2]` **TCVN 4244:2005** — Thiết bị nâng: Thiết kế, chế tạo và kiểm tra kỹ thuật (Bộ KH&CN).
  3. `[3]` **IEC 61800-2:1998 / IEC 60034-1 / ISO/IEC/IEEE 29148:2018** — Tiêu chuẩn biến tần, động cơ & đặc tả SRS.
  4. `[4]` **TS. Nguyễn Duy Đỉnh (2023)** — Bài giảng Thiết kế Hệ TĐĐ (Bài 4, tr. 43: $\varphi = 0.20$) & Tiêu chuẩn TĐĐ.
  5. `[5]` **Tiêu chuẩn Ray A54 & Bánh xe thép DIN 536** ($w_0 = 0.015 \pm 0.003$, đường kính bánh xe $d = 0.25\text{ m} \pm 1\text{ mm}$).
  6. `[6]` **Demag Cranes & Components (2011)** — Catalogue Demag DR/EZDR Rope Hoists and Double-Girder Trolley (Đức).
  7. `[7]` **Sungdo Hoist / KG-Cranes (2020)** — Hồ sơ Kỹ thuật Pa lăng và Xe con Dầm đôi 15 Tấn ($m_{xc} = 1,800\text{ kg} \pm 5\%$).
  8. `[8]` **Shevchenko O. O. (2024)** — Hệ truyền động điện cơ cấu di chuyển xe con cầu trục dầm đôi, NTUU KPI.
  9. `[9]` **T. Mita & T. Kanai (1979) / Tho et al. (2020)** — Điều khiển chống lắc cáp $h = 12.0\text{ m} \pm 0.1\text{ m}$ & Quỹ đạo S-Curve 7 đoạn.
  10. `[10]` **NASA SP-2007-6105 Rev1** — NASA Systems Engineering Handbook (Quy trình SE, RTM & DVP&R).
* **Danh mục Slide Phụ lục Phòng thủ Hội đồng:** Bao gồm 6 Slide Backup `B1-1 .. B1-6` tra cứu chi tiết.

---

## PHẦN B: 6 SLIDE PHỤ LỤC PHÒNG THỦ HỘI ĐỒNG (`BACKUP DECK`: SLIDE 17 $\to$ SLIDE 22)

1. **SLIDE 17 (`BACKUP B1-1`):** Bảng tra cứu nguyên bản 4 Yêu cầu Chức năng `SRS-FUNC-01..04` kèm đầy đủ 8 cột Metadata (`Shall Statement`, `Rationale`, `CTQ kèm Dung sai`, `V&V`, `Owner`).
2. **SLIDE 18 (`BACKUP B1-2`):** Bảng tra cứu nguyên bản 5 Yêu cầu Hiệu năng `SRS-PERM-01..05` kèm đầy đủ 8 cột Metadata (`Shall Statement`, `Rationale`, `CTQ kèm Dung sai`, `V&V`, `Owner`).
3. **SLIDE 19 (`BACKUP B1-3`):** Danh mục 11/19 mã yêu cầu `PRD v3.1` thuộc diện Loại trừ có kiểm soát (*Out-of-Scope Tailoring*: `PRD-SAFE-01..04`, `PRD-INTF-01..03`, `PRD-ENVI-01..02`, `PRD-RELI-01..02`) và lý do kỹ thuật không đưa vào `SRS Baseline A`.
4. **SLIDE 20 (`BACKUP B1-4`):** Ma trận Truy xuất Ngược & Chuỗi `DMAIC` chi tiết — Phần 1: 4 hàng `SRS-FUNC-01..04` nối với `HoQ EC`, `PRD`, `Tech Gap`, `P-Diagram`, `RRM`, `WBS`, `DVP-L0`.
5. **SLIDE 21 (`BACKUP B1-5`):** Ma trận Truy xuất Ngược & Chuỗi `DMAIC` chi tiết — Phần 2: 5 hàng `SRS-PERM-01..05` nối với `HoQ EC`, `PRD`, `Tech Gap`, `P-Diagram`, `RRM`, `WBS`, `DVP-L0`.
6. **SLIDE 22 (`BACKUP B1-6`):** Bảng Cấu trúc Kép `DVP&R Level 0` (*Plan & Report*) và Phân tích sâu 3 kịch bản nhiễu `TS-01..03` trên Simulink.
