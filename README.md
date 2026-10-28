# LƯU ĐỒ DỰ ÁN — HỆ TRUYỀN ĐỘNG DI CHUYỂN XE CON CẦU TRỤC DẦM ĐÔI ($x = 2$)

**Học phần:** Thiết kế hệ thống truyền động điện (ĐH Bách khoa Hà Nội)  
**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Đề tài:** Hệ truyền động cơ cấu di chuyển xe con cầu trục dầm đôi (Động cơ KĐB rotor lồng sóc + Biến tần, điều khiển FOC, quỹ đạo S-curve)  
**Nhóm sinh viên thực hiện:** Nhóm 8.5-EMG (STT 22, tham số $x = 2$)  
**Quy chuẩn áp dụng:** NASA SP-2007-6105 Rev 1, ISO/IEC/IEEE 29148:2018, TCVN 4244:2005, IEC 60034-1, IEC 61800-2, DIN 536  
**Quy tắc thực thi & Kiểm khớp AI (từ Khối 2 $\to$ Khối 5):** [`WORKFLOW_RULES.md`](WORKFLOW_RULES.md)

---

## 1. CẤU TRÚC THƯ MỤC DỰ ÁN & KHO TÀI LIỆU

Thư mục **`Lưu đồ dự án`** lưu trữ quy tắc thực thi (`WORKFLOW_RULES.md`), kho tài liệu tham khảo chuẩn (`Tài liệu tham khảo/`) và toàn bộ các sản phẩm kết quả của từng giai đoạn kỹ thuật hệ thống:

```
Lưu đồ dự án/
├── WORKFLOW_RULES.md        # Quy tắc thực thi, công thức chuẩn & bộ kiểm khớp rà soát (Bắt đầu từ Khối 2)
├── README.md                # Tài liệu hướng dẫn, mục lục tổng thể và tóm tắt công thức/thông số gốc
│
├── Block 0/                 # Khối 0: Tiền khả thi (Pre-A) — Cổng MCR [ĐÃ HOÀN THÀNH & ĐÓNG BĂNG]
│   ├── 01_PRD_Yeu_cau_san_pham_v3.1.md           # Product Requirements Document (PRD v3.1)
│   ├── 02_SOW_Pham_vi_cong_viec_v1.2.md          # Statement of Work (SOW v1.2)
│   ├── 03_HOQ_Bao_cao_Case_Study_QFD_ICE_v1.1.md # House of Quality, QFD & ICE Analysis (v1.1)
│   └── 04_BAO_CAO_SLIDE_PPTX_BLOCK_0_MCR.md      # Báo cáo Slide bảo vệ Cổng MCR
│
├── Block 1/                 # Khối 1: Yêu cầu Hệ thống (EVT) — Cổng SRR [ĐÃ HOÀN THÀNH & ĐÓNG BĂNG]
│   ├── 00_Bang_thong_so_goc_SSoT.md              # Bảng thông số gốc duy nhất (Single Source of Truth)
│   ├── 01_SRS_Baseline_A_v1.2.md                 # SRS Baseline A chuẩn (8 yêu cầu: 4 FUNC + 4 PERM)
│   ├── 01_SRS_Chi_tiet_Xe_con_cau_truc_x2_v1.2.md# SRS đặc tả chi tiết cơ cấu xe con x = 2
│   ├── 02_Boundary_va_P_Diagram.md               # Sơ đồ ranh giới hệ thống & Sơ đồ tham số P-Diagram
│   ├── 02_Boundary_Diagram_16x9.svg              # Bản vẽ vector Sơ đồ ranh giới tỉ lệ 16:9
│   ├── 03_RTM_DVP_Ma_tran_truy_xuat_va_Kiem_chung_v1.2.md # RTM & Kế hoạch kiểm chứng DVP L0
│   ├── 03_RTM_DVP_Chi_tiet_Xe_con_cau_truc_x2_v1.2.md     # RTM & DVP đặc tả chi tiết kịch bản TS-01..03
│   ├── 04_Bao_cao_Giai_trinh_Toan_dien_SRR.md    # Báo cáo giải trình toàn diện bảo vệ Cổng SRR-EVT
│   ├── 05_Bao_cao_Tien_do_Khoi_1_SRR.md          # Báo cáo tiến độ hoàn thành Khối 1
│   └── 06_Bao_cao_Kiem_toan_Dong_bo_DVP_RTM_PRD_SOW_HOQ.md # Báo cáo kiểm toán đối chiếu chéo toàn diện
│
├── Block 2/                 # Khối 2: Kiến trúc Hệ thống — Cổng G3 PDR-EVT [ĐÃ DUYỆT & ĐÓNG 24/10/2026]
│   ├── 01_SAD_Kien_truc_He_thong_v1.0.md         # Kiến trúc PDS, 5 trade-off, phân bổ 8 SRS + 8 Downstream
│   ├── 02_ICD_Kiem_soat_Giao_dien_v1.0.md        # IF-01..IF-16: ký hiệu, đơn vị, dải, tên biến Simulink
│   ├── 03_BOM_So_bo_3_cap_v1.0.md                # BOM sơ bộ 3 cấp + trạng thái nguồn catalogue
│   ├── 04_DFMEA_L1_v1.0.md                       # 12 dạng lỗi, AP trước/sau biện pháp
│   ├── 05_Bao_cao_Checker_G3_G4.md               # Báo cáo rà soát K6–K12 (lượt kiểm riêng)
│   └── 06_Do_thi_phu_tai_mot_hanh_trinh.png      # Đồ thị phụ tải một hành trình (SAD §5.4)
│
├── Block 3/                 # Khối 3: Thiết kế Chi tiết — Cổng G4 CDR-EVT [ĐÃ DUYỆT & ĐÓNG 24/10/2026]
│   ├── 00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx  # CDRL-02 HIỆN HÀNH (CR-19): bản rút gọn chỉ gồm chọn thiết bị — phụ tải, chọn động cơ (DRN71M4 0.37 kW), 14 tham số + hiệu chỉnh, biến tần ACS380-01A8-4, R_h, phanh; 18 mục kiểm tra
│   ├── 00_Tinh_toan_Xe_con_x2_v1.5.xlsx          # CDRL-02 bản trước (DRN80M4, a* = 0.45), giữ lịch sử: như v1.4 + sheet UocLuong_TS (14 công thức + hiệu chỉnh tham số ĐC, KT-44), vòng tốc độ chỉnh theo J_rig, WCCA 2 trường hợp, khối P ở lưới danh định (CR-08..CR-18)
│   ├── 00_Tinh_toan_Xe_con_x2_v1.4.xlsx          # CDRL-02 bản trước: như v1.3 + E_đ theo ω_m, KT-42/43, khối S, sheet Tong_hop & Quy_dao (rà soát lượt 1–2 ngày 27/10/2026: không XUNG ĐỘT/CẢNH BÁO)
│   ├── 00_Tinh_toan_Xe_con_x2_v1.3.xlsx          # CDRL-02 bản trước: như v1.2 + khối O–R & sheet Mo_phong (bộ thông số mô phỏng)
│   ├── 00_Tinh_toan_Xe_con_x2_v1.2.xlsx          # CDRL-02 bản trước (lưu lịch sử; số liệu tính chọn giống v1.3)
│   ├── 01_Thuyet_minh_Tinh_chon_Phan_luc_v1.0.md # Động cơ, hộp số, biến tần, R_h, phanh, WCCA
│   ├── 02_So_do_Nguyen_ly_Mach_luc_v1.0.svg      # Bản vẽ nguyên lý mạch động lực
│   ├── 02_So_do_Mach_luc_va_BOM_Chinh_thuc_v1.0.md # Thuyết minh sơ đồ + BOM chính thức
│   ├── 03_SDD_Thiet_ke_Dieu_khien_va_Logic_v1.0.md # Tham số ĐC, S-curve, PI MO/SO, FSM 4Q
│   ├── 04_SRS_A1_Dan_xuat_RTM_DVP_WCCA_v1.0.md   # SRS Baseline A.1 (đã ký), SRS-D01..D15 (+ D05d), RTM/DVP phân hệ, V-model
│   ├── 05_Bao_cao_Checker_Excel_v1.4_luot1.md    # rà soát K6–K12 cho Excel v1.4 (lượt 1, 27/10/2026)
│   └── 06_Bao_cao_Checker_Excel_v1.4_luot2.md    # rà soát K6–K12 kiểm lại sau khi sửa (lượt 2)
│
└── Tài liệu tham khảo/      # Kho tiêu chuẩn, bài giảng và Case Studies gốc đã xác minh
    ├── 00_Danh_muc_tai_lieu_tham_khao.md            # Danh mục thống nhất mã [R..], trạng thái đối chiếu từng tài liệu
    ├── Catalogue web/                            # [W-01..W-10] Catalogue SEW, ABB, Danotherm cho Khối 2–3 (+ danh mục nguồn)
    ├── Thầy Đỉnh/                                # Bài giảng TKTĐĐ (Bài 1..4) & Tiêu chuẩn VN-Quốc tế
    ├── tcvn-4244-2005.pdf                        # [R1] TCVN 4244:2005 — Thiết bị nâng
    ├── A54.pdf                                   # [R9-04] Valtchev et al., DAS 2024 (tên tệp không phản ánh nội dung — không phải DIN 536)
    ├── Dầm đôi_cấu trúc truyền động_Đức.pdf      # [R9-07] Catalogue Demag DR/EZDR Double-Rail Crab
    ├── Shevchenko_bakalavr.pdf                   # [R9-06] Đồ án TĐĐ Cầu trục ĐH Bách khoa Kiev (KPI, 2024)
    ├── S-curve.pdf & S-curve-simulation.pdf      # [R9-11] Tho et al. (2020); [R9-12] Blejan & Blejan (2020)
    ├── Crane trolley Nhật Bổn.pdf                # [R9-01] Mô hình con lắc tải cầu trục (Mita & Kanai, 1979)
    ├── Cầu trục_Indo.pdf                         # [R9-02] Thiết kế xe con & cầu trục 10 t (Feto et al., 2025)
    ├── Dynamic crane trolley.pdf                 # [R9-14] Tổng quan động lực học & điều khiển cầu trục (Abdel-Rahman et al., 2003)
    ├── Thiết kế cầu trục dầm đôi_Thổ.pdf         # [R9-03] Cầu trục dầm đôi 10t (Doğan, 2023)
    ├── Simulation_of_Crane_Trolley_..._Nga.pdf   # [R9-13] Mô phỏng điều khiển xe con giảm lắc (Reutov, 2021)
    ├── SM2693.pdf                                # [R9-05] Điều khiển cầu trục 2-DOF (Zheng et al., 2021)
    └── Bản sao của [NHÓM 2] ... pptx.pdf         # [R8] Slide báo cáo tham khảo sinh viên
```

---

## 2. LỘ TRÌNH THỰC HIỆN & BẢNG TRA CỨU CÁC KHỐI DỰ ÁN

### 2.1. Các Khối Đã Hoàn Thành & Đóng Băng (`Block 0` & `Block 1`)

| Khối | Sản phẩm | Mã tài liệu / Phiên bản | Tên tệp trong thư mục | Mô tả nội dung cốt lõi |
| :---: | :---: | :---: | :--- | :--- |
| **Block 0** | **PRD** | `PRD-8.5EMG-TROLLEY-v3.1` | [`01_PRD_Yeu_cau_san_pham_v3.1.md`](Block%200/01_PRD_Yeu_cau_san_pham_v3.1.md) | 8 yêu cầu khách hàng In-Scope (`PRD-FUNC-01..04`, `PRD-PERM-01..04`), ConOps 6 pha, MOEs/MOPs/TPMs. |
| **Block 0** | **SOW** | `SOW-8.5EMG-TROLLEY-v1.2` | [`02_SOW_Pham_vi_cong_viec_v1.2.md`](Block%200/02_SOW_Pham_vi_cong_viec_v1.2.md) | WBS 6 khối (`SOW-0.1` $\to$ `SOW-5.3`), RACI, QCD, 5 gói sản phẩm giao nộp `CDRL-01..05`. |
| **Block 0** | **HOQ** | `BCA-QFD-8.5EMG-TROLLEY-v1.1` | [`03_HOQ_Bao_cao_Case_Study_QFD_ICE_v1.1.md`](Block%200/03_HOQ_Bao_cao_Case_Study_QFD_ICE_v1.1.md) | 9 Case Studies, 7 Tech Gaps, ma trận HoQ trọng số `EC-01..08`, chấm điểm ICE chọn `Solution C` (812 đ). |
| **Block 1** | **SSoT** | `SSoT-8.5EMG-v1.2` | [`00_Bang_thong_so_goc_SSoT.md`](Block%201/00_Bang_thong_so_goc_SSoT.md) | 20 thông số kỹ thuật gốc `P-01..P-20`: $Q=12,222\text{ kg}, M_\Sigma=14,244\text{ kg}, F_{c.\text{đầy}}=2,096\text{ N}, \eta=0.90$. |
| **Block 1** | **SRS** | `SRS-8.5EMG-TROLLEY-v1.2` | [`01_SRS_Baseline_A_v1.2.md`](Block%201/01_SRS_Baseline_A_v1.2.md) | 8 yêu cầu hệ thống chuẩn (`4 FUNC + 4 PERM`) + Bảng phân bổ 8 thông số Downstream Design Allocation. |
| **Block 1** | **DVP & RTM** | `RTM-DVP-8.5EMG-v1.2` | [`03_RTM_DVP_Ma_tran_truy_xuat_va_Kiem_chung_v1.2.md`](Block%201/03_RTM_DVP_Ma_tran_truy_xuat_va_Kiem_chung_v1.2.md) | Ma trận truy xuất hai chiều (Forward/Backward) & 8 bài đo kiểm chứng `DV-01..08` (`DVP-L0-01..08`). |

> **Cập nhật 28/10/2026 (CR-19):** lượng đặt S-curve đổi thành $a^*$ = 0.10 m/s², $\rho^*$ = 0.40 m/s³ (giới hạn đề bài giữ nguyên); thiết bị chọn lại: **SEW DRN71M4 0.37 kW + ABB ACS380-04xS-01A8-4**, phanh BE1 5 N·m, $R_h$ = 210 Ω, hộp số R87 $i$ = 155.34. Nguồn số: `Block 3/00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx`. Lý do: `Block 3/04_SRS_A1_...` §1 "Giải thích CR-19". Các tài liệu Block 3 khác còn theo DRN80M4 (lịch sử, chưa cập nhật).

> **Cập nhật 24/10/2026:** **Cổng G3 (Khối 2) và G4 (Khối 3) đã duyệt và đóng.** Baseline hiện hành: `SSoT v1.2` + **SRS Baseline A.1** (ký 24/10/2026; `SRS-PERM-04`: $k_{dt} \ge 1.20$). Thiết bị chốt: SEW DRN80M4 0.75 kW (geared motor, phanh BE1 $M_B$ = 7 N·m, encoder ES7C) + ABB ACS380-04xS-03A3-4 + $R_h$ = 210 Ω. Phạm vi: chỉ vận hành lý tưởng (QĐ-07). Quyết định QĐ-01..QĐ-08 ghi trong `Block 2/01_SAD_...` §0 và `Block 3/04_SRS_A1_...` §1. Cập nhật 25/10/2026: đã chốt hộp số SEW R87 ($i$ = 155.34), phanh BE1 7 N·m, điện trở Danotherm CBH 360 C T 406 210R, cầu chì gG 6 A OFAF000H6, contactor ABB AF09-30-10-13; nguồn lưu tại `Tài liệu tham khảo/Catalogue web/`; Excel nâng lên v1.2 (nguồn `[W-01..W-10]`). Tiếp theo: **G5 (Khối 4)** — `init_params.m` + mô hình Simulink. Kết quả mô phỏng: chưa chạy. Cập nhật 28/10/2026: chốt phạm vi môn học CR-08..CR-18 (nhật ký tại `Block 3/04_SRS_A1_...` §1) — bỏ dung sai số liệu đầu vào và dải nghiệm thu gán cho giá trị tính; gia tốc, độ giật chỉ giữ cận trên; góc lắc chỉ quan sát; $k_{dt}$ tính ở lưới danh định; mô phỏng kịch bản rút gọn ở lưới danh định; Excel nâng lên v1.5 (14 công thức ước lượng tham số động cơ, WCCA 2 trường hợp). Cập nhật 26/10/2026 (nhóm C): Excel v1.3 thêm bộ thông số mô phỏng (sheet `Mo_phong`) — mô hình 2 khối lượng xe con + con lắc, giảm từ thông do động cơ 400 V chạy lưới 380 V, biến tần mô hình trung bình + DC-link, kịch bản TS-01/TS-02 rút gọn ≈ 45 s; ICD v1.2, SDD v1.3, `WORKFLOW_RULES.md` §7.2 sửa tương ứng.

### 2.2. Các Khối Tiếp Theo Cần Triển Khai (Theo [`WORKFLOW_RULES.md`](WORKFLOW_RULES.md))

| Cổng | Khối & Mã WBS | Các sản phẩm cần thực hiện | Điều kiện qua cổng |
| :---: | :--- | :--- | :--- |
| **G3** (`PDR-EVT`) | **Block 2: Kiến trúc Hệ thống** (`SOW-2.1` $\to$ `SOW-2.3`) | • Tài liệu Kiến trúc Hệ thống (**SAD**) & Trade-off cấu hình.<br>• Tài liệu Kiểm soát Giao diện (**ICD**) theo cấu trúc PDS **IEC 61800-2**.<br>• Bảng phân bổ `8 SRS` + `8 Downstream Allocation` $\to$ các phân hệ.<br>• Danh mục thiết bị **BOM sơ bộ 3 cấp** & Phân tích lỗi **DFMEA L1**. | rà soát kiểm khớp K6–K9, K12 $\to$ **Nhóm duyệt** phương án kiến trúc & thiết bị sơ bộ. |
| **G4** (`CDR-EVT`) | **Block 3: Thiết kế Chi tiết** (`SOW-3.1` $\to$ `SOW-3.5`) | • File tính toán **Excel** (`Params`, `Tính chọn`, `Kiểm tra`, `Dẫn xuất`).<br>• Thuyết minh tính chọn động cơ ($S3-40\%, k_{dt} \ge 1.20$ theo SRS A.1), hộp số, biến tần, điện trở xả hãm $R_h$, quy đổi $M/J$.<br>• Sơ đồ nguyên lý mạch động lực & **BOM chính thức**.<br>• Đặc tả thuật toán điều khiển (**SDD**): 5 tham số ĐC, quỹ đạo **S-curve 7 đoạn**, bộ điều khiển PI dòng điện (MO) & PI tốc độ (SO) **RFOC**, lưu đồ & hàm logic **FSM 4 góc phần tư**.<br>• Cập nhật yêu cầu dẫn xuất `SRS-Dxx`, RTM/DVP phân hệ & WCCA rút gọn. | rà soát kiểm khớp K6–K12 $\to$ **Nhóm duyệt** thông số thiết kế chi tiết. |
| **G5** (`TRR-EVT`) | **Block 4: Chuẩn bị Thử nghiệm** (`SOW-4.1` $\to$ `SOW-4.2`) | • Script khởi tạo thông số `init_params.m` (đồng bộ 100% với Excel & SSoT).<br>• Mô hình tích hợp trên **MATLAB/Simulink** (`.slx`), bước giải $T_s \le 10^{-4}\text{ s}$, bộ lọc đạo hàm $G_d(s) = \frac{s}{T_f s + 1}$.<br>• Các script kịch bản thử `TS-01..03` (`DV-01..08`) & khóa phiên bản trong `RUN_LOG.md`. | Sẵn sàng chạy mô phỏng, không chứa hằng số gõ tay. |
| **G6** (`SIR/SAR`) | **Block 5: Tích hợp, Kiểm chứng & Bàn giao** (`SOW-5.1` $\to$ `SOW-5.3`) | • Đồ thị và dữ liệu log chạy mô phỏng thực tế.<br>• Báo cáo kết quả kiểm chứng **`DVP&R Level 0 Report`** (điền cột `Report` cho `DV-01..08`) & NCR rút gọn (nếu có).<br>• Thuyết minh đồ án tổng hợp & Slide bảo vệ cuối kỳ. | rà soát chạy kiểm toán cuối cùng $\to$ Hoàn tất hồ sơ bảo vệ. |

---

## 3. THÔNG SỐ VẬT LÝ GỐC DUY NHẤT (SSoT KHÓA CỨNG: `P-01` $\to$ `P-20`)

Toàn bộ các tài liệu và bảng tính trong `Lưu đồ dự án` tuân thủ nghiêm ngặt các giá trị chuẩn sau:
- **Tải nâng định mức (`P-01` `[A]`):** $Q = 12,222\text{ kg}$ ($x = 2$, STT 22)
- **Khối lượng cơ cấu nâng hạ (`P-02` `[A]`):** $m_{nh} = 222\text{ kg}$
- **Tự trọng bản thân xe con (`P-03` `[C]`):** $m_{xc} = 1,800\text{ kg}$
- **Tổng khối lượng đầy tải (`P-04` `[B]`):** $M_\Sigma = Q + m_{nh} + m_{xc} = 14,244\text{ kg}$
- **Tổng khối lượng không tải (`P-05` `[B]`):** $m_{\text{tĩnh}} = m_{nh} + m_{xc} = 2,022\text{ kg}$ (tỷ số biến thiên tải $7.04\text{ lần}$)
- **Chiều cao nâng lớn nhất (`P-06` `[A]`, `P-07`, `P-08` `[B]`):** $h = 12\text{ m}$ ($\omega_p = \sqrt{g/h} \approx 0.904\text{ rad/s}, T_p \approx 6.95\text{ s}$)
- **Vận tốc di chuyển định mức (`P-09` `[A]`):** $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ ($[0.114;\ 0.126]\text{ m/s}$ hay $7.2\text{ m/phút}$)
- **Gia tốc cực đại cho phép (`P-10` `[A]`):** $a_{\max} \le 0.50\text{ m/s}^2$
- **Độ giật cực đại cho phép (`P-11` `[A]`):** $\rho_{\max} \le 2.00\text{ m/s}^3$
- **Đường kính bánh xe (`P-12` `[C]`):** $D_{bx} = 0.25\text{ m}$ ($\omega_{\text{bx}} = 0.96\text{ rad/s} \approx 9.17\text{ vg/ph}$)
- **Suất cản lăn riêng (`P-13` `[C]`):** $w_0 = 0.015$ (1.5%)
- **Hệ số bám dính bánh thép trên ray thép (`P-14` `[C]`):** $\varphi = 0.20$
- **Hiệu suất truyền động cơ khí (`P-15` `[C]`):** $\eta = 0.90$ (tỷ số truyền sơ bộ `P-16`: $i \approx 150$)
- **Chế độ làm việc & Nguồn lưới (`P-17`, `P-19` `[C]`):** $S3 - 40\%$ (chu kỳ $10\text{ phút}$) dưới nguồn 3 pha $380\text{V} \pm 10\% / 50\text{Hz}$
- **Lực cản lăn tĩnh đầy tải (`P-20` `[B]`):** $F_{c.\text{đầy}} = M_\Sigma \cdot g \cdot w_0 = 14,244 \cdot 9.81 \cdot 0.015 \approx 2,096\text{ N}$ (không tải $F_{c.\text{không}} \approx 298\text{ N}$)
- **Công suất tĩnh định mức:** $P_{\text{tĩnh}} = \frac{F_{c.\text{đầy}} \cdot v_{\max}}{\eta} = \frac{2,096 \cdot 0.12}{0.90} \approx 0.28\text{ kW}$
- **Lực kéo cực đại khi gia tốc:** $F_{\max} = F_{c.\text{đầy}} + M_\Sigma \cdot a_{\max} = 2,096 + 7,122 = 9,218\text{ N} \approx 9.22\text{ kN}$ ($P_{\max} = \frac{F_{\max} \cdot v_{\max}}{\eta} \approx 1.23\text{ kW}$)
- **Hệ số an toàn bám chống trượt (2/4 bánh chủ động):** $k_{\text{bám}} = \frac{F_{\text{bám}}}{F_{\max}} = \frac{0.20 \cdot 0.50 \cdot 14,244 \cdot 9.81}{9,218} = \frac{13,973}{9,218} \approx 1.52 \ge 1.20$

---

## 4. HỆ THỐNG TÀI LIỆU THAM KHẢO & TIÊU CHUẨN ÁP DỤNG (`Tài liệu tham khảo/`)

Danh mục đầy đủ (thông tin xuất bản, trạng thái đối chiếu, bảng đổi mã cũ của Khối 0): [`Tài liệu tham khảo/00_Danh_muc_tai_lieu_tham_khao.md`](Tài%20liệu%20tham%20khảo/00_Danh_muc_tai_lieu_tham_khao.md).

| Mã viện dẫn | Tệp lưu trữ trong `Lưu đồ dự án/Tài liệu tham khảo/` | Nội dung & Công thức tham chiếu chính |
| :---: | :--- | :--- |
| **`[R1]`** | [`tcvn-4244-2005.pdf`](Tài%20liệu%20tham%20khảo/tcvn-4244-2005.pdf) | **TCVN 4244:2005**: Nhóm cơ cấu ISO M5 (§2.1.1.3), phanh cơ thường đóng (§1.5.3.3), cấm đảo chiều khi $v \ne 0$ (§1.5.7.2.9), liên khóa phanh điện-cơ (§2.4.5.5.2), lực cản di chuyển xe con (§2.4.7.2.2). |
| **`[R4]`** | [`Thầy Đỉnh/TIÊU CHUẨN VN VÀ QUỐC TẾ.pdf`](Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/TIÊU%20CHUẨN%20VN%20VÀ%20QUỐC%20TẾ.pdf) | **IEC 60034-1** (chế độ nhiệt S3, tr.23), **IEC 60529** (cấp bảo vệ IP, tr.16–17). Tài liệu **không có IEC 61800-2** (tr.85–92 là EMC) — thuật ngữ PDS/BDM/CDM dùng theo hiểu biết chung. |
| **`[R5]`** | [`Thầy Đỉnh/Bài 1.pdf`](Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%201.pdf), [`Bài 2.1.pdf`](Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%202.1.pdf), [`Bài 2.2.pdf`](Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%202.2.pdf), [`Bài 2.3.pdf`](Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%202.3.pdf), [`Bài 3.pdf`](Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%203.pdf), [`Bài 4.pdf`](Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%204.pdf) | **Bài giảng Thiết kế Hệ TĐĐ (TS. Nguyễn Duy Đỉnh)**: Quy đổi mô-men/quán tính, tính công suất đẳng trị nhiệt S3 (Bài 2), tổng hợp bộ điều khiển PI dòng điện MO & tốc độ SO trong RFOC (Bài 3), điều kiện bám ray $\varphi = 0.20$ & tính điện trở hãm $R_h$ (Bài 4). |
| **`[R9-06]`** | [`Shevchenko_bakalavr.pdf`](Tài%20liệu%20tham%20khảo/Shevchenko_bakalavr.pdf) | **Đồ án mẫu ĐH Bách khoa Kiev (KPI, 2024)**: Quy trình tính chọn phần lực chế độ S3, biến tần + Braking Chopper + $R_h$, xác định tham số mạch thay thế ĐC và mô phỏng RFOC + S-Curve trên Simulink. |
| **`[R9-07]`** | [`Dầm đôi_cấu trúc truyền động_Đức.pdf`](Tài%20liệu%20tham%20khảo/Dầm%20đôi_cấu%20trúc%20truyền%20động_Đức.pdf) | **Catalogue Demag DR/EZDR**: Cấu hình xe con dầm đôi công nghiệp dùng động cơ KĐB gắn sẵn Pulse Encoder, biến tần tích hợp điện trở xả hãm và phanh đĩa điện từ. |
| **`[R9-04]`** | [`A54.pdf`](Tài%20liệu%20tham%20khảo/A54.pdf) | **Valtchev et al. (DAS 2024)** — tăng khả năng dập dao động của hệ truyền động cầu trục khi tải treo mềm. *Tên tệp không phản ánh nội dung; kho không có tiêu chuẩn DIN 536 — $D_{bx}$ và $w_0$ là giả định `[C]` (tính kiểm $w_0$ ở SSoT Phần 1b).* |
| **`[R9-11]`**, **`[R9-12]`** | [`S-curve.pdf`](Tài%20liệu%20tham%20khảo/S-curve.pdf), [`S-curve-simulation.pdf`](Tài%20liệu%20tham%20khảo/S-curve-simulation.pdf) | **Ho Duc Tho et al. (2020)**, *Control Engineering Practice* 98: lệnh S-curve thời gian tối thiểu không gây dao động; **Blejan & Blejan (2020)**, *Hidraulica* 4/2020: toán học bộ tạo S-curve thời gian thực. |
| **`[R9-01]`, `[R9-02]`, `[R9-03]`, `[R9-05]`, `[R9-13]`, `[R9-14]`** | [`Crane trolley Nhật Bổn.pdf`](Tài%20liệu%20tham%20khảo/Crane%20trolley%20Nhật%20Bổn.pdf), [`Cầu trục_Indo.pdf`](Tài%20liệu%20tham%20khảo/Cầu%20trục_Indo.pdf), [`Thiết kế cầu trục dầm đôi_Thổ.pdf`](Tài%20liệu%20tham%20khảo/Thiết%20kế%20cầu%20trục%20dầm%20đôi_Thổ.pdf), [`SM2693.pdf`](Tài%20liệu%20tham%20khảo/SM2693.pdf), [`Simulation_of_Crane_Trolley_..._Nga.pdf`](Tài%20liệu%20tham%20khảo/Simulation_of_Crane_Trolley_Motion_Control_to_Redu_Nga.pdf), [`Dynamic crane trolley.pdf`](Tài%20liệu%20tham%20khảo/Dynamic%20crane%20trolley.pdf) | Lần lượt: Mita & Kanai (1979) — mô hình con lắc tải; Feto et al. (2025) — thiết kế xe con 10 t; Doğan (2023) — cầu trục dầm đôi; Zheng et al. (2021) — điều khiển fuzzy PID cầu trục; Reutov (2021) — mô phỏng giảm lắc; Abdel-Rahman et al. (2003) — tổng quan động lực học cầu trục. |
