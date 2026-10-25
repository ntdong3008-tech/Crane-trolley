# LƯU ĐỒ DỰ ÁN — HỆ TRUYỀN ĐỘNG DI CHUYỂN XE CON CẦU TRỤC DẦM ĐÔI ($x = 2$)

**Học phần:** Thiết kế hệ thống truyền động điện (ĐH Bách khoa Hà Nội)  
**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Đề tài:** Hệ truyền động cơ cấu di chuyển xe con cầu trục dầm đôi (Động cơ KĐB rotor lồng sóc + Biến tần, điều khiển FOC, quỹ đạo S-curve)  
**Nhóm sinh viên thực hiện:** Nhóm 8.5-EMG (STT 22, tham số $x = 2$)  
**Quy chuẩn áp dụng:** NASA SP-2007-6105 Rev 1, ISO/IEC/IEEE 29148:2018, TCVN 4244:2005, IEC 60034-1, IEC 61800-2, DIN 536  
**Quy tắc thực thi & Kiểm khớp AI (từ Khối 2 $\to$ Khối 5):** [`WORKFLOW_RULES.md`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/WORKFLOW_RULES.md)

---

## 1. CẤU TRÚC THƯ MỤC DỰ ÁN & KHO TÀI LIỆU

Thư mục **`Lưu đồ dự án`** lưu trữ quy tắc thực thi (`WORKFLOW_RULES.md`), kho tài liệu tham khảo chuẩn (`Tài liệu tham khảo/`) và toàn bộ các sản phẩm kết quả của từng giai đoạn kỹ thuật hệ thống:

```
Lưu đồ dự án/
├── WORKFLOW_RULES.md        # Quy tắc thực thi, công thức chuẩn & bộ kiểm khớp Checker (Bắt đầu từ Khối 2)
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
│   └── 05_Bao_cao_Checker_G3_G4.md               # Báo cáo Checker K6–K12 (lượt kiểm riêng)
│
├── Block 3/                 # Khối 3: Thiết kế Chi tiết — Cổng G4 CDR-EVT [ĐÃ DUYỆT & ĐÓNG 24/10/2026]
│   ├── 00_Tinh_toan_Xe_con_x2_v1.2.xlsx          # CDRL-02: Params, GiaDinh_K3, Catalogue, Tính chọn, Kiểm tra, Dẫn xuất
│   ├── 01_Thuyet_minh_Tinh_chon_Phan_luc_v1.0.md # Động cơ, hộp số, biến tần, R_h, phanh, WCCA
│   ├── 02_So_do_Nguyen_ly_Mach_luc_v1.0.svg      # Bản vẽ nguyên lý mạch động lực
│   ├── 02_So_do_Mach_luc_va_BOM_Chinh_thuc_v1.0.md # Thuyết minh sơ đồ + BOM chính thức
│   ├── 03_SDD_Thiet_ke_Dieu_khien_va_Logic_v1.0.md # Tham số ĐC, S-curve, PI MO/SO, FSM 4Q
│   └── 04_SRS_A1_Dan_xuat_RTM_DVP_WCCA_v1.0.md   # SRS Baseline A.1 (đã ký), SRS-D01..D13, RTM/DVP phân hệ, V-model
│
└── Tài liệu tham khảo/      # Kho tiêu chuẩn, bài giảng và Case Studies gốc đã xác minh
    ├── Catalogue web/                            # [W-01..W-10] Catalogue SEW, ABB, Danotherm cho Khối 2–3 (+ danh mục nguồn)
    ├── Thầy Đỉnh/                                # Bài giảng TKTĐĐ (Bài 1..4) & Tiêu chuẩn VN-Quốc tế
    ├── tcvn-4244-2005.pdf                        # [R1] TCVN 4244:2005 — Thiết bị nâng
    ├── A54.pdf                                   # [R9-10] Tiêu chuẩn ray A54 & bánh xe thép (DIN 536)
    ├── Dầm đôi_cấu trúc truyền động_Đức.pdf      # [R9-07] Catalogue Demag DR/EZDR Double-Rail Crab
    ├── Shevchenko_bakalavr.pdf                   # [R9-06] Đồ án TĐĐ Cầu trục ĐH Bách khoa Kiev (KPI, 2024)
    ├── S-curve.pdf & S-curve-simulation.pdf      # [R9-11] Quy hoạch quỹ đạo S-Curve 7 đoạn (Tho et al., 2020)
    ├── Crane trolley Nhật Bổn.pdf                # [R9-01] Mô hình con lắc tải cầu trục (Mita & Kanai, 1979)
    ├── Cầu trục_Indo.pdf & Dynamic crane trolley.pdf # [R9-02] Thiết kế cơ khí xe con 10t (Feto et al., 2025)
    ├── Thiết kế cầu trục dầm đôi_Thổ.pdf         # [R9-03] Cầu trục dầm đôi 10t (Doğan, 2023)
    ├── Simulation_of_Crane_Trolley_..._Nga.pdf   # [R9-04] Mô phỏng giảm lắc tải treo mềm (Valtchev et al., 2024)
    ├── SM2693.pdf                                # [R9-05] Điều khiển cầu trục 2-DOF (Zheng et al., 2021)
    └── Bản sao của [NHÓM 2] ... pptx.pdf         # [R8] Slide báo cáo tham khảo sinh viên
```

---

## 2. LỘ TRÌNH THỰC HIỆN & BẢNG TRA CỨU CÁC KHỐI DỰ ÁN

### 2.1. Các Khối Đã Hoàn Thành & Đóng Băng (`Block 0` & `Block 1`)

| Khối | Sản phẩm | Mã tài liệu / Phiên bản | Tên tệp trong thư mục | Mô tả nội dung cốt lõi |
| :---: | :---: | :---: | :--- | :--- |
| **Block 0** | **PRD** | `PRD-8.5EMG-TROLLEY-v3.1` | [`01_PRD_Yeu_cau_san_pham_v3.1.md`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Block%200/01_PRD_Yeu_cau_san_pham_v3.1.md) | 8 yêu cầu khách hàng In-Scope (`PRD-FUNC-01..04`, `PRD-PERM-01..04`), ConOps 6 pha, MOEs/MOPs/TPMs. |
| **Block 0** | **SOW** | `SOW-8.5EMG-TROLLEY-v1.2` | [`02_SOW_Pham_vi_cong_viec_v1.2.md`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Block%200/02_SOW_Pham_vi_cong_viec_v1.2.md) | WBS 6 khối (`SOW-0.1` $\to$ `SOW-5.3`), RACI, QCD, 5 gói sản phẩm giao nộp `CDRL-01..05`. |
| **Block 0** | **HOQ** | `BCA-QFD-8.5EMG-TROLLEY-v1.1` | [`03_HOQ_Bao_cao_Case_Study_QFD_ICE_v1.1.md`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Block%200/03_HOQ_Bao_cao_Case_Study_QFD_ICE_v1.1.md) | 9 Case Studies, 7 Tech Gaps, ma trận HoQ trọng số `EC-01..08`, chấm điểm ICE chọn `Solution C` (812 đ). |
| **Block 1** | **SSoT** | `SSoT-8.5EMG-v1.2` | [`00_Bang_thong_so_goc_SSoT.md`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Block%201/00_Bang_thong_so_goc_SSoT.md) | 20 thông số kỹ thuật gốc `P-01..P-20`: $Q=12,222\text{ kg}, M_\Sigma=14,244\text{ kg}, F_{c.\text{đầy}}=2,096\text{ N}, \eta=0.90$. |
| **Block 1** | **SRS** | `SRS-8.5EMG-TROLLEY-v1.2` | [`01_SRS_Baseline_A_v1.2.md`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Block%201/01_SRS_Baseline_A_v1.2.md) | 8 yêu cầu hệ thống chuẩn (`4 FUNC + 4 PERM`) + Bảng phân bổ 8 thông số Downstream Design Allocation. |
| **Block 1** | **DVP & RTM** | `RTM-DVP-8.5EMG-v1.2` | [`03_RTM_DVP_Ma_tran_truy_xuat_va_Kiem_chung_v1.2.md`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Block%201/03_RTM_DVP_Ma_tran_truy_xuat_va_Kiem_chung_v1.2.md) | Ma trận truy xuất hai chiều (Forward/Backward) & 8 bài đo kiểm chứng `DV-01..08` (`DVP-L0-01..08`). |

> **Cập nhật 24/10/2026:** **Cổng G3 (Khối 2) và G4 (Khối 3) đã duyệt và đóng.** Baseline hiện hành: `SSoT v1.2` + **SRS Baseline A.1** (ký 24/10/2026; `SRS-PERM-04`: $k_{dt} \ge 1.20$). Thiết bị chốt: SEW DRN80M4 0.75 kW (geared motor, phanh BE1 $M_B$ = 7 N·m, encoder ES7C) + ABB ACS380-04xS-03A3-4 + $R_h$ = 210 Ω. Phạm vi: chỉ vận hành lý tưởng (QĐ-07). Quyết định QĐ-01..QĐ-08 ghi trong `Block 2/01_SAD_...` §0 và `Block 3/04_SRS_A1_...` §1. Cập nhật 25/10/2026: đã chốt hộp số SEW R87 ($i$ = 155.34), phanh BE1 7 N·m, điện trở Danotherm CBH 360 C T 406 210R, cầu chì gG 6 A OFAF000H6, contactor ABB AF09-30-10-13; nguồn lưu tại `Tài liệu tham khảo/Catalogue web/`; Excel nâng lên v1.2..W-05]`. Tiếp theo: **G5 (Khối 4)** — `init_params.m` + mô hình Simulink. Kết quả mô phỏng: chưa chạy.

### 2.2. Các Khối Tiếp Theo Cần Triển Khai (Theo [`WORKFLOW_RULES.md`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/WORKFLOW_RULES.md))

| Cổng | Khối & Mã WBS | Các sản phẩm cần thực hiện | Điều kiện qua cổng |
| :---: | :--- | :--- | :--- |
| **G3** (`PDR-EVT`) | **Block 2: Kiến trúc Hệ thống** (`SOW-2.1` $\to$ `SOW-2.3`) | • Tài liệu Kiến trúc Hệ thống (**SAD**) & Trade-off cấu hình.<br>• Tài liệu Kiểm soát Giao diện (**ICD**) theo cấu trúc PDS **IEC 61800-2**.<br>• Bảng phân bổ `8 SRS` + `8 Downstream Allocation` $\to$ các phân hệ.<br>• Danh mục thiết bị **BOM sơ bộ 3 cấp** & Phân tích lỗi **DFMEA L1**. | Checker kiểm khớp K6–K9, K12 $\to$ **Người dùng duyệt** phương án kiến trúc & thiết bị sơ bộ. |
| **G4** (`CDR-EVT`) | **Block 3: Thiết kế Chi tiết** (`SOW-3.1` $\to$ `SOW-3.5`) | • File tính toán **Excel** (`Params`, `Tính chọn`, `Kiểm tra`, `Dẫn xuất`).<br>• Thuyết minh tính chọn động cơ ($S3-40\%, k_{dt} \in [1.20; 1.50]$), hộp số, biến tần, điện trở xả hãm $R_h$, quy đổi $M/J$.<br>• Sơ đồ nguyên lý mạch động lực & **BOM chính thức**.<br>• Đặc tả thuật toán điều khiển (**SDD**): 5 tham số ĐC, quỹ đạo **S-curve 7 đoạn**, bộ điều khiển PI dòng điện (MO) & PI tốc độ (SO) **RFOC**, lưu đồ & hàm logic **FSM 4 góc phần tư**.<br>• Cập nhật yêu cầu dẫn xuất `SRS-Dxx`, RTM/DVP phân hệ & WCCA rút gọn. | Checker kiểm khớp K6–K12 $\to$ **Người dùng duyệt** thông số thiết kế chi tiết. |
| **G5** (`TRR-EVT`) | **Block 4: Chuẩn bị Thử nghiệm** (`SOW-4.1` $\to$ `SOW-4.2`) | • Script khởi tạo thông số `init_params.m` (đồng bộ 100% với Excel & SSoT).<br>• Mô hình tích hợp trên **MATLAB/Simulink** (`.slx`), bước giải $T_s \le 10^{-4}\text{ s}$, bộ lọc đạo hàm $G_d(s) = \frac{s}{T_f s + 1}$.<br>• Các script kịch bản thử `TS-01..03` (`DV-01..08`) & khóa phiên bản trong `RUN_LOG.md`. | Sẵn sàng chạy mô phỏng, không chứa hằng số gõ tay. |
| **G6** (`SIR/SAR`) | **Block 5: Tích hợp, Kiểm chứng & Bàn giao** (`SOW-5.1` $\to$ `SOW-5.3`) | • Đồ thị và dữ liệu log chạy mô phỏng thực tế.<br>• Báo cáo kết quả kiểm chứng **`DVP&R Level 0 Report`** (điền cột `Report` cho `DV-01..08`) & NCR rút gọn (nếu có).<br>• Thuyết minh đồ án tổng hợp & Slide bảo vệ cuối kỳ. | Checker chạy kiểm toán cuối cùng $\to$ Hoàn tất hồ sơ bảo vệ. |

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

| Mã viện dẫn | Tệp lưu trữ trong `Lưu đồ dự án/Tài liệu tham khảo/` | Nội dung & Công thức tham chiếu chính |
| :---: | :--- | :--- |
| **`[R1]`** | [`tcvn-4244-2005.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/tcvn-4244-2005.pdf) | **TCVN 4244:2005**: Nhóm cơ cấu ISO M5 (§2.1.1.3), phanh cơ thường đóng (§1.5.3.3), cấm đảo chiều khi $v \ne 0$ (§1.5.7.2.9), liên khóa phanh điện-cơ (§2.4.5.5.2), lực cản di chuyển xe con (§2.4.7.2.2). |
| **`[R4]`** | [`Thầy Đỉnh/TIÊU CHUẨN VN VÀ QUỐC TẾ.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/TIÊU%20CHUẨN%20VN%20VÀ%20QUỐC%20TẾ.pdf) | **IEC 60034-1** (chế độ nhiệt S3, tr.23), **IEC 61800-2** (kiến trúc PDS `CDM/CU/M` & dung sai Class 2, tr.85–92), **IEC 60529** (cấp bảo vệ IP54/IP55, tr.16–17). |
| **`[R5]`** | [`Thầy Đỉnh/Bài 1.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%201.pdf), [`Bài 2.1.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%202.1.pdf), [`Bài 2.2.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%202.2.pdf), [`Bài 2.3.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%202.3.pdf), [`Bài 3.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%203.pdf), [`Bài 4.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Thầy%20Đỉnh/Bài%204.pdf) | **Bài giảng Thiết kế Hệ TĐĐ (TS. Nguyễn Duy Đỉnh)**: Quy đổi mô-men/quán tính, tính công suất đẳng trị nhiệt S3 (Bài 2), tổng hợp bộ điều khiển PI dòng điện MO & tốc độ SO trong RFOC (Bài 3), điều kiện bám ray $\varphi = 0.20$ & tính điện trở hãm $R_h$ (Bài 4). |
| **`[R9-06]`** | [`Shevchenko_bakalavr.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Shevchenko_bakalavr.pdf) | **Đồ án mẫu ĐH Bách khoa Kiev (KPI, 2024)**: Quy trình tính chọn phần lực chế độ S3, biến tần + Braking Chopper + $R_h$, xác định tham số mạch thay thế ĐC và mô phỏng RFOC + S-Curve trên Simulink. |
| **`[R9-07]`** | [`Dầm đôi_cấu trúc truyền động_Đức.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Dầm%20đôi_cấu%20trúc%20truyền%20động_Đức.pdf) | **Catalogue Demag DR/EZDR**: Cấu hình xe con dầm đôi công nghiệp dùng động cơ KĐB gắn sẵn Pulse Encoder, biến tần tích hợp điện trở xả hãm và phanh đĩa điện từ. |
| **`[R9-10]`** | [`A54.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/A54.pdf) | **Tiêu chuẩn DIN 536 (Ray A54 & Bánh xe)**: Đường kính bánh xe $D_{bx} = 0.25\text{ m}$ và suất cản lăn riêng $w_0 = 0.015$ (tr.15). |
| **`[R9-11]`** | [`S-curve.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/S-curve.pdf) & [`S-curve-simulation.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/S-curve-simulation.pdf) | **Tho et al. (2020)**: Phương trình giải tích quy hoạch quỹ đạo S-Curve 7 đoạn giới hạn vận tốc, gia tốc và độ giật. |
| **`[R9-01..05]`** | [`Crane trolley Nhật Bổn.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Crane%20trolley%20Nhật%20Bổn.pdf), [`Cầu trục_Indo.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Cầu%20trục_Indo.pdf), [`Dynamic crane trolley.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Dynamic%20crane%20trolley.pdf), [`Thiết kế cầu trục dầm đôi_Thổ.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Thiết%20kế%20cầu%20trục%20dầm%20đôi_Thổ.pdf), [`Simulation_of_Crane_Trolley_Motion_Control_to_Redu_Nga.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/Simulation_of_Crane_Trolley_Motion_Control_to_Redu_Nga.pdf), [`SM2693.pdf`](file:///d:/Tài%20liệu%20học%20tập/Kỳ%202026.1/Thiết%20Kế%20TĐĐ/Project/Lưu%20đồ%20dự%20án/Tài%20liệu%20tham%20khảo/SM2693.pdf) | Mô hình con lắc tải treo cáp ($\ddot{\theta} + (g/h)\theta = a/h$), thiết kế hộp số 3 cấp và đối chứng công suất động cơ xe con thực tế. |
