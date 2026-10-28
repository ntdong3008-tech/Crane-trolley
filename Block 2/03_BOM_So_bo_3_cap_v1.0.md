# DANH MỤC THIẾT BỊ & VẬT TƯ SƠ BỘ 3 CẤP (BOM SƠ BỘ) — XE CON CẦU TRỤC ($x = 2$)

**Mã tài liệu:** `BOM-P-8.5EMG-TROLLEY-v1.0` — Gói `SOW-2.2` (Khối 2) — Phụ trách: Đặng Nguyên Bình (PE-HW)  
**Ngày:** 24/10/2026 (v1.1: 28/10/2026 — L3-16 theo QĐ-07) — **Trạng thái:** **ĐÃ DUYỆT — Cổng G3 (`PDR-EVT`) đóng ngày 24/10/2026** (nhóm duyệt kiến trúc: 1 động cơ đặt giữa dẫn 2 bánh qua trục ngang, encoder ES7C)  
**Căn cứ:** `01_SAD_Kien_truc_He_thong_v1.0.md` (§2, §3, §5), SSoT v1.2, nguồn catalogue `[W-01..W-05]` (SAD §8.1)  
**Ghi chú:** BOM sơ bộ chỉ chốt **loại thiết bị + dải định cỡ + ứng viên**; mã đặt hàng chính thức nằm ở BOM chính thức Khối 3 (`SOW-3.2`). Cột "Trạng thái nguồn": **XM** = đã xác minh từ catalogue `[W-xx]`; **CXM** = chưa xác minh; **TBD** = chưa xác định.

---

## Cấp 1 — `L1-00` Hệ truyền động di chuyển xe con cầu trục dầm đôi (01 bộ)

### Cấp 2 — `L2-01` Phân hệ phần lực (Power Subsystem)

| Mã L3 | Thiết bị | SL | Yêu cầu định cỡ sơ bộ (từ SAD §5) | Ứng viên sơ bộ | Trạng thái nguồn |
| :---: | :--- | :---: | :--- | :--- | :---: |
| `L3-01` | Aptomat MCCB/Motor-protection `QF1` | 1 | 3 cực, $U_e \ge 400$ V; $I_n \approx 1.2 \div 1.5 \times I_{\text{vào,inv}}$ (≈ 4 ÷ 10 A); cắt ngắn mạch theo khuyến cáo biến tần | TBD (chọn theo hướng dẫn cầu chì/MCB của ACS380 HW manual 3AXD50000029274) | TBD |
| `L3-02` | Contactor nguồn `KM1` | 1 | AC-1, $I_e \ge I_{\text{vào,inv}}$; cuộn 24 V DC hoặc 230 V AC | TBD | TBD |
| `L3-03` | Cuộn kháng / bộ lọc EMC đầu vào | 0–1 | Tùy chọn; ACS380 có lọc EMC C2 tích hợp (option) | `Không áp dụng vì đồ án mô phỏng` (chỉ ghi chú) | — |
| `L3-04` | Biến tần (BDM) có **Braking Chopper tích hợp** | 1 | 3 pha 380–480 V; dòng heavy-duty $I_{Hd} \ge I_{N,\text{ĐC}}$; $1.5\,I_{Hd} \ge I_{\text{đỉnh}}$ khi tăng tốc; hỗ trợ vector có encoder | **ABB ACS380-04xS-03A3-4** (cho ĐC 0.75 kW) hoặc **-04A0-4** (cho ĐC 1.1 kW) | XM\* [W-05] tr.10, 12 (bảng trích văn bản lệch cột — đối chiếu bản gốc) |
| `L3-05` | Điện trở xả hãm $R_h$ | 1 | $R_{\min,\text{inv}} \le R_h \le \min(R_{\max,\text{inv}};\ U_{\text{chop}}^2/P_{\text{hãm,max}})$; $P_{\text{hãm,max}} \approx 0.45$ kW (SAD §5) | Theo bảng chopper ACS380: $R_{\min} = 99\ \Omega$, $R_{\max} = 428$ (-03A3) / 285 Ω (-04A0) | XM [W-05] tr.25; điện trở cụ thể TBD |
| `L3-06` | Cáp động lực, cáp $R_h$ | — | Tiết diện theo $I_N$ | `Không áp dụng vì đồ án mô phỏng` | — |

### Cấp 2 — `L2-02` Phân hệ cơ điện (Geared motor + cơ khí xe con)

| Mã L3 | Thiết bị | SL | Yêu cầu định cỡ sơ bộ | Ứng viên sơ bộ | Trạng thái nguồn |
| :---: | :--- | :---: | :--- | :--- | :---: |
| `L3-07` | Động cơ KĐB 3 pha rotor lồng sóc 4 cực (IE3) — phần động cơ của geared motor | 1 | $\lambda_K (U_{\min}/U_N)^2 \ge M_{\max}/M_N$ ($U_N$ = 400 V) với $M_{\max} \approx 10.7 \div 12.7$ N·m; $P_{đm}/P_{đt} \ge 1.20$ (đề xuất A.1) | **SEW DRN80M4** (0.75 kW, 4.95 N·m, 1440 vg/ph, 1.75 A, $M_K/M_N = 3.4$) hoặc **DRN90S4** (1.1 kW, 7.2 N·m, 1455 vg/ph, 2.55 A, $M_K/M_N = 3.3$) | XM [W-01] tr.866 |
| `L3-08` | Hộp giảm tốc bánh răng trụ (liền khối với ĐC) | 1 | $i \approx 157 \div 159$; $M_{a,\max} \ge F_{\max} D_{bx}/2 = 1,152$ N·m (đầu ra, dẫn 2 bánh) | SEW họ R (cỡ R67/R77) — **cỡ và $i$ chính xác TBD** (cần bảng tổ hợp SEW) | CXM |
| `L3-09` | Phanh đĩa điện từ thường đóng + bộ chỉnh lưu phanh | 1 | $k_p M_c \le M_B \le$ giới hạn bám (giới hạn bám đầy tải); nhả khi cấp điện | SEW BE1 (DRN80) / BE2 (DRN90) — cấp $M_B$ chọn ở Khối 3 | XM loại phanh [W-02] tr.24; cấp $M_B$ TBD |
| `L3-10` | Encoder xung tương đối | 1 | ≥ 1024 chu kỳ/vòng (phân giải $\Delta v \le 2$ mm/s, SAD §3.4); HTL/TTL | **SEW ES7C** | XM [W-04] |
| `L3-11` | Trục truyền ngang + 2 khớp nối + 2 bánh dẫn $D = 0.25$ m | 1 bộ | Truyền $M_{a,\max}$; 2/4 bánh dẫn | Out-of-Scope chế tạo — chỉ dùng $D_{bx}$, $\eta$ | P-12 [C], P-15 [C] |
| `L3-12` | Khung xe con + 2 bánh bị dẫn | 1 | $m_{xc} = 1,800$ kg (`P-03 [C]`) | Đối chiếu catalogue xe con dầm đôi 12–15 t: **chưa có dữ liệu trong kho** | CXM |

> **Cập nhật sau G4 (25/10/2026) cho `L3-08`:** đã chốt **SEW R87, $i$ = 155.34**, $M_{a,\max}$ = 1,550 N·m, $F_{Ra}$ = 17,100 N (`[W-06]`) — xem BOM chính thức ở Khối 3. Dòng trên giữ nguyên là yêu cầu sơ bộ tại G3.

### Cấp 2 — `L2-03` Phân hệ điều khiển & giám sát

| Mã L3 | Thiết bị | SL | Yêu cầu | Ứng viên sơ bộ | Trạng thái nguồn |
| :---: | :--- | :---: | :--- | :--- | :---: |
| `L3-13` | Module giao tiếp encoder | 1 | HTL/TTL, cấp nguồn encoder | ABB **BTAC-02** (option +L535) | XM [W-05] tr.24 |
| `L3-14` | Bộ điều khiển trung tâm CU (S-curve, RFOC, FSM) | 1 | Chu kỳ dòng ≤ 250 µs, tốc độ ≤ 1 ms | Firmware biến tần + logic (đồ án: **hiện thực trên Simulink**) | — |
| `L3-15` | Tay bấm 5 nút (FWD/REV/FAST/STOP/RESET) | 1 | 24 V DC; E-STOP: Không áp dụng (QĐ-07) | TBD | TBD |
| `L3-16` | Rơ-le nhiệt/tiếp điểm nhiệt cho $R_h$ và ĐC (TF/TH) | 1 bộ | Bảo vệ nhiệt phần cứng; không đưa vào FSM (`flt_oh` Không áp dụng, QĐ-07) | Công tắc nhiệt có sẵn trên $R_h$ Danotherm [W-09] | XM ($R_h$) |

---

## Tổng hợp trạng thái nguồn BOM sơ bộ

| Trạng thái | Số mục | Mã mục |
| :---: | :---: | :--- |
| XM / XM\* (đã xác minh loại & thông số chính) | 6 | L3-04 (XM\*), L3-05 (giới hạn R), L3-07, L3-09 (loại), L3-10, L3-13 |
| CXM | 3 | L3-08, L3-12, L3-11 (giả định `[C]`) |
| TBD | 5 | L3-01, L3-02, L3-15, L3-16, cấp $M_B$ (L3-09) |
| Không áp dụng | 2 | L3-03, L3-06 |
