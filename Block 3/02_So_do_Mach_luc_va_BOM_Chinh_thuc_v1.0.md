# SƠ ĐỒ NGUYÊN LÝ MẠCH ĐỘNG LỰC & DANH MỤC THIẾT BỊ CHÍNH THỨC (BOM) — XE CON ($x = 2$)

**Mã tài liệu:** `BOM-F-8.5EMG-TROLLEY-v1.2` (25/10/2026: chốt hộp số, phanh, R_h, F1, KM1) + `DWG-PWR-8.5EMG-v1.0` — Gói `SOW-3.2` (Khối 3) — hồ sơ `CDRL-03`  
**Ngày:** 24/10/2026 — **Trạng thái:** **ĐÃ DUYỆT — Cổng G4 (`CDR-EVT`) đóng ngày 24/10/2026**  
**Bản vẽ:** [`02_So_do_Nguyen_ly_Mach_luc_v1.0.svg`](02_So_do_Nguyen_ly_Mach_luc_v1.0.svg) (nguyên lý — không phải bản vẽ lắp đặt)  
**Căn cứ số liệu:** `00_Tinh_toan_Xe_con_x2_v1.2.xlsx` (sheet `Catalogue`, `Tính chọn`), thuyết minh `01_Thuyet_minh_Tinh_chon_Phan_luc_v1.0.md`

---

## 1. MÔ TẢ SƠ ĐỒ NGUYÊN LÝ MẠCH ĐỘNG LỰC

Chuỗi công suất (theo kiến trúc SAD §2, giao diện ICD):

`Lưới 3~ 380 V ±10%/50 Hz (IF-01)` → **F1** (cầu chì gG 3×6 A ABB OFAF000H6) → **KM1** (contactor nguồn) → **U1 ACS380** [chỉnh lưu diode → DC-link $C$ → nghịch lưu IGBT SVPWM; **Braking Chopper tích hợp** nối ra cực R+/R−] → **M1** DRN80M4 (IF-04) → **YB** phanh BE1 → hộp số R ($i \approx 157$) → trục ngang → 2 bánh dẫn (IF-09).

Nhánh hãm: **R+/R− → R1** ($R_h = 210\ \Omega$, có tiếp điểm nhiệt về DI7) — IF-05.

Mạch phanh: **RO1** của biến tần (lệnh `brake_cmd` do FSM phát) → **K2** → cấp nguồn bộ chỉnh lưu phanh **G1** (BG/BGE*) → cuộn hút phanh. Mất điện / `brake_cmd = 0` ⇒ phanh kẹp (fail-safe) — IF-06.

Phản hồi: **B1** encoder ES7C (A, Ā, B, B̄, C) → module **A1 BTAC-02** — IF-07. Tiếp điểm nhiệt TF của động cơ → DI6.

An toàn: **E-STOP / STO / SS1 — Không áp dụng vì điều kiện vận hành lý tưởng (QĐ-07)**. ACS380 vẫn có sẵn đầu vào STO (*"Safe torque off (STO) … SIL 3"* [W-05] tr.10) nếu sau này cần bổ sung.

> Ký hiệu thiết bị theo IEC 81346 kiểu rút gọn (QF, KM, U, M, YB, B, A, G, K, R) — *quy ước đặt tên, không phải yêu cầu chuẩn của đồ án*.

---

## 2. BOM CHÍNH THỨC 3 CẤP (phương án đã chốt `sel = 1` — QĐ-04)

**QĐ-04 (Người dùng, 24/10/2026): CHỐT ứng viên 1 — SEW DRN80M4 0.75 kW + ABB ACS380-04xS-03A3-4; chấp nhận biên quá tải 1.03 ở tổ hợp xấu nhất WC-5** (lưới −10%, $w_0$ = 0.018, $m_{xc}$ +20%, $\eta$ = 0.85).

Cột trạng thái: **XM** — đã xác minh thông số từ nguồn `[W-xx]`; **XM\*** — đã xác minh nhưng bảng PDF trích văn bản lệch cột, cần đối chiếu bản gốc; **CXM** — chưa xác minh; **TBD** — chưa xác định.

### Cấp 1 — `L1-00` Hệ truyền động di chuyển xe con cầu trục dầm đôi $x = 2$ (01 bộ)

#### Cấp 2 — `L2-01` Phân hệ phần lực

| TT | Ký hiệu | Tên thiết bị | Mã hiệu / Đặc tính kỹ thuật | Hãng | SL | Nguồn | Trạng thái |
| :---: | :---: | :--- | :--- | :---: | :---: | :--- | :---: |
| 1 | F1 (QF1) | Bộ cầu chì bảo vệ đầu vào 3P | **3 × cầu chì gG 6 A, ABB OFAF000H6** (cỡ NH000) trong đế/cầu dao cầu chì 3 cực; cáp vào 3×1.5 + 1.5 mm²; dòng vào biến tần ≈ 4.8 A | ABB | 1 bộ | [W-08] (bảng cầu chì ACS380) | XM (cầu chì); đế cầu chì: chọn theo cỡ NH000 |
| 2 | KM1 | Contactor nguồn 3P | **ABB AF09-30-10-13** (1SBL137001R1310): 3NO + 1NO phụ; AC-3 9 A @400 V; AC-1 25 A; cuộn 100–250 V AC/DC | ABB | 1 | [W-10] | XM\* (dữ liệu từ nhà phân phối) |
| 3 | U1 | Biến tần (BDM) | **ACS380-04xS-03A3-4**: 3~ 380–480 V; $I_N$ 3.3 A / $P_N$ 1.1 kW; $I_{Hd}$ 2.6 A / $P_{Hd}$ 0.75 kW; $I_{\max}$ 4.7 A; f_sw 1–12 kHz (mặc định 4); chopper tích hợp $R_{\min}$ 99 Ω, $R_{\max}$ 428 Ω, $P_{BR,\text{cont}}$ 0.75 kW, $P_{BR,\max}$ 1.13 kW; STO SIL 3; IP20 | ABB | 1 | [W-05] tr.10, 12, 24 (đã đối chiếu ảnh trang) | XM |
| 4 | R1 | Điện trở xả hãm | **Danotherm CBH 360 C T 406 210R**: 210 Ω ±10% (189–231 Ω ∈ [99; 428]), 200 W @40 °C, xung 2.6 kW/10 s mỗi 120 s, công tắc nhiệt tích hợp (→ DI7) | Danotherm | 1 | [W-05] tr.24 (điện trở mẫu ABB); [W-09] | XM |

#### Cấp 2 — `L2-02` Phân hệ cơ điện (geared motor)

| TT | Ký hiệu | Tên thiết bị | Mã hiệu / Đặc tính kỹ thuật | Hãng | SL | Nguồn | Trạng thái |
| :---: | :---: | :--- | :--- | :---: | :---: | :--- | :---: |
| 5 | M1 | Động cơ KĐB 3 pha rotor lồng sóc IE3 | **DRN80M4**: 0.75 kW, 4.95 N·m, 1440 vg/ph, 1.75 A (400 V), cosφ 0.74, η 82.9%, $I_A/I_N$ 6.7, $M_A/M_N$ 3.1, $M_K/M_N$ 3.4, $M_H/M_N$ 2.7; $J_{\text{Mot}}$ 24.7×10⁻⁴ kg·m²; tiếp điểm nhiệt TF | SEW-EURODRIVE | 1 | [W-01] tr.866; [W-02] tr.24 | XM |
| 6 | YB | Phanh đĩa điện từ thường đóng | **BE1** (lắp trên DRN80M4); $J_{\text{BMot}}$ 26.2×10⁻⁴ kg·m²; mô-men đặt **7 N·m** = cấp chuẩn của BE1 (4 lò xo thường + 2 lò xo xanh; các cấp 10/7/5 N·m); cửa sổ yêu cầu [5.94; 10.12] N·m | SEW-EURODRIVE | 1 | [W-02] tr.24; [W-07] | XM |
| 7 | G1 | Bộ chỉnh lưu phanh | BG/BGE (điện áp cuộn phanh TBD), cắt phía DC để kẹp nhanh | SEW-EURODRIVE | 1 | — | CXM |
| 8 | — | Hộp giảm tốc bánh răng trụ (liền khối) | **SEW R87**, tỷ số truyền tổng **$i$ = 155.34**; $M_{a,\max}$ = 1,550 N·m ≥ 1,286 N·m (đỉnh); $F_{Ra}$ = 17,100 N; trục đặc 50×100 mm, lắp chân đế (R..) | SEW-EURODRIVE | 1 | [W-06] | XM (hộp số); tổ hợp với khung DRN80: SEW xác nhận khi đặt hàng |
| 9 | B1 | Encoder tương đối gắn ngoài | **ES7C**: HTL/TTL (RS422), 1024 chu kỳ/vòng, DC 4.75–30 V, 6000 min⁻¹, cho DRN71–315 | SEW-EURODRIVE | 1 | [W-04] | XM |
| 10 | — | Trục ngang, khớp nối, 2 bánh dẫn $D$ 0.25 m, 2 bánh bị dẫn, khung xe con | Theo SSoT P-03, P-12 | — | 1 bộ | SSoT `[C]` | CXM (Out-of-Scope chế tạo) |

#### Cấp 2 — `L2-03` Phân hệ điều khiển & giám sát

| TT | Ký hiệu | Tên thiết bị | Mã hiệu / Đặc tính kỹ thuật | Hãng | SL | Nguồn | Trạng thái |
| :---: | :---: | :--- | :--- | :---: | :---: | :--- | :---: |
| 11 | A1 | Module giao tiếp encoder + 24 V ngoài | **BTAC-02** (option +L535, mã 3AXD50000022163) | ABB | 1 | [W-05] tr.24 (danh mục option) | XM |
| 12 | K2 | Rơ-le trung gian phanh | Cuộn 24 V DC, tiếp điểm phù hợp dòng chỉnh lưu phanh | TBD | 1 | — | TBD |
| 13 | S1–S6 | Tay bấm | FWD, REV, FAST/CREEP, STOP, RESET (E-STOP: Không áp dụng — QĐ-07) | TBD | 1 | — | TBD |
| 14 | — | Bộ điều khiển CU (S-curve, RFOC, FSM) | Hiện thực trên MATLAB/Simulink (Khối 4–5); trên thiết bị thật: firmware biến tần + logic | — | — | SDD | `Không áp dụng vì đồ án mô phỏng` (phần cứng CU) |

### Phương án dự phòng (`sel = 2`)

| Thay đổi | Mã hiệu | Ghi chú |
| :--- | :--- | :--- |
| Động cơ | SEW **DRN90S4** 1.1 kW, 7.2 N·m, 1455 vg/ph, 2.55 A, $M_K/M_N$ 3.3; $J_{\text{BMot}}$ 58.7×10⁻⁴ | [W-01], [W-02] |
| Phanh | BE2 — cấp 20/14/10/7/5 N·m `[W-07]` → chọn cấp 7 hoặc 10 N·m (≤ giới hạn không trượt 10.12 N·m với $i$ = 155.34) | Hết xung đột K11-6 |
| Biến tần | ACS380-04xS-**04A0-4**: $I_N$ 4.0 A, $I_{Hd}$ 3.3 A, $I_{\max}$ 5.9 A, $R_h \in [99; 285]\ \Omega$ | [W-05] |

---

## 3. TỔNG HỢP TRẠNG THÁI NGUỒN (Checker K12) — cập nhật 25/10/2026

| Trạng thái | Mục |
| :---: | :--- |
| XM | F1 (cầu chì), U1, R1, M1, YB (loại + cấp 7 N·m), hộp số R87 ($i$ = 155.34), B1, A1 |
| XM\* | KM1 (dữ liệu ABB qua nhà phân phối) |
| CXM | G1 (điện áp cuộn phanh); tổ hợp R87 + khung DRN80 (SEW xác nhận khi đặt hàng); mục 10 (giả định SSoT `[C]`) |
| TBD | K2, S1–S5 (khí cụ điều khiển 24 V thông dụng — không ảnh hưởng tính toán) |

**Đã hoàn thành ngày 25/10/2026:** (1) lưu PDF nguồn `[W-01..W-08]` và tệp ghi nhận `[W-06]`, `[W-09]`, `[W-10]` vào `Tài liệu tham khảo/Catalogue web/` (bản gốc SEW của [W-01] trả về 403 nên giữ bản trích 1 trang); (2) chốt hộp số SEW R87, $i$ = 155.34 qua SEW Drive Selection — ô `i_in` của Excel đã cập nhật; (3) xác minh BE1 có cấp 7 N·m; (4) đối chiếu bảng định mức ACS380 bằng ảnh trang gốc; (5) chọn F1 (cầu chì gG 6 A OFAF000H6) theo ABB và KM1 (AF09-30-10-13).
**Còn lại:** điện áp cuộn phanh/bộ chỉnh lưu G1, rơ-le K2, tay bấm; xác nhận với SEW cuộn dây 380 V/50 Hz cho DRN80M4 (Checker K11-7) và tổ hợp R87 + DRN80 khi đặt hàng.
