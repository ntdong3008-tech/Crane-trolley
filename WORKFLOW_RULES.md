# WORKFLOW_RULES.md — AI thực hiện & kiểm tra lưu đồ dự án (Bắt đầu từ Khối 2)

Căn cứ: `FLOW_REVIEW.md` (6 khối – 7 cổng), toàn bộ hồ sơ đã khóa cứng tại **`Block 0`** (Cổng `MCR`) & **`Block 1`** (Cổng `SRR-EVT`), và kho tài liệu thực tế trong **`Lưu đồ dự án/Tài liệu tham khảo/`**. File này quy định AI **làm gì, làm theo thứ tự nào, dùng công thức & tiêu chuẩn nào, kiểm ra sao từ Khối 2 đến Khối 5**. Phạm vi thực tế tiếp theo của nhóm: thiết kế kiến trúc hệ thống → tính chọn động cơ/biến tần/điện trở hãm → thiết kế điều khiển FOC & S-curve & logic FSM → mô phỏng MATLAB/Simulink.

---

## 0. Nguyên tắc chung
1. **Kế thừa tuyệt đối Baseline Khối 0 & Khối 1.** Toàn bộ tài liệu ở `Block 0` (`PRD v3.1`, `SOW v1.2`, `HOQ v1.1`) và `Block 1` (`00_Bang_thong_so_goc_SSoT.md`, `01_SRS_Baseline_A_v1.2.md`, `02_Boundary_va_P_Diagram.md`, `03_RTM_DVP_..._v1.2.md`) đã được kiểm toán đồng bộ 100% và đóng băng (**Frozen Baseline**). Không viết lại hay sửa đổi tự ý Khối 0 và Khối 1.
2. **Mềm nhưng trung thực.** Chỉ cảnh báo, không chặn cứng. Phần thuộc chuẩn công nghiệp mà sinh viên không làm thì ghi một dòng `Không áp dụng vì …`, không bị phạt.
3. **Không bịa.** Số liệu, số hiệu chuẩn, điều khoản, thông số catalogue, kết quả mô phỏng chỉ được nêu khi có nguồn trong `Tài liệu tham khảo/` hoặc có dữ liệu thật. Thiếu thì ghi `TBD` hoặc `chưa xác minh`.
4. **Mọi con số truy được** về mã thông số SSoT (`P-01..P-20`), ID yêu cầu (`PRD-xx`, `SRS-FUNC/PERM-xx`), hoặc tệp tài liệu trong `Tài liệu tham khảo/` kèm trang/mục và đơn vị.
5. **AI nêu vấn đề, người quyết định.** Xung đột yêu cầu, chọn phương án thiết bị/kiến trúc, đổi baseline: AI trình bày lựa chọn, không tự chọn.
6. **Người dùng phải hiểu và bảo vệ được từng con số.** Mỗi file tính toán kèm mục `Giải thích ngắn: vì sao tính như vậy`.

---

## 1. Vai trò
| Vai | Việc | Ràng buộc |
|---|---|---|
| **Writer** | Tra cứu tài liệu trong `Tài liệu tham khảo/`, viết tài liệu Khối 2–5, tính toán, sinh script | Không tự duyệt sản phẩm của mình |
| **Checker** | Chạy bộ kiểm khớp (mục 8) đối chiếu với Baseline Khối 0 & 1 | Chạy ở **lượt/model riêng**, chỉ đọc, không sửa hộ |
| **Người duyệt** (người dùng) | Duyệt tại các cổng từ G3 trở đi (mục 3) | Là bên duy nhất đổi baseline |

---

## 2. Hệ thống ID, Phiên bản & Quy chuẩn đã khóa (từ Khối 0 & Khối 1)
- **Mã thông số gốc (SSoT):** `P-01` $\to$ `P-20` kèm phân loại nguồn `[A]` (Đề bài $x=2$), `[B]` (Tính toán từ `[A]`), `[C]` (Giả định kỹ thuật kiểm tra lại ở Khối 2/3) theo đúng `Block 1/00_Bang_thong_so_goc_SSoT.md`.
- **Mã yêu cầu sản phẩm (Khối 0):** 8 mã cốt lõi In-Scope: `PRD-FUNC-01..04` và `PRD-PERM-01..04` (ánh xạ cùng `EC-01..08` trong HoQ và phương án chốt `Solution C`).
- **Mã gói công việc (SOW v1.2):** `SOW-0.1..0.3` (Đã xong), `SOW-1.1..1.3` (Đã xong), tiếp tục thực hiện `SOW-2.1..2.3` (Khối 2), `SOW-3.1..3.5` (Khối 3), `SOW-4.1..4.2` (Khối 4), `SOW-5.1..5.3` (Khối 5).
- **Mã yêu cầu hệ thống gốc (Khối 1 — SRS Baseline A v1.2):** 8 mã nguyên tử theo chuẩn **ISO/IEC/IEEE 29148:2018**:
  - Chức năng: `SRS-FUNC-01`, `SRS-FUNC-02`, `SRS-FUNC-03`, `SRS-FUNC-04`.
  - Hiệu năng: `SRS-PERM-01`, `SRS-PERM-02`, `SRS-PERM-03`, `SRS-PERM-04`.
- **Mã yêu cầu dẫn xuất & Phân bổ thiết kế (`SRS-Dxx` / Downstream Allocation):**
  - Kế thừa trực tiếp **8 thông số Downstream Design Allocation** đã chuyển từ Mục 4 của `01_SRS_Baseline_A_v1.2.md` xuống Khối 2 và Khối 3:
    1. Độ quá điều chỉnh tốc độ: $M_p \le 10.0\%$ (`Khối 3 - SOW-3.3`)
    2. Sai lệch tốc độ xác lập tĩnh: $e_{xl} \le 5.0\%$ (`Khối 3 - SOW-3.3`)
    3. Điện áp DC-link & Ngưỡng băm Chopper: $U_{\text{dc}} \le 780\text{ V DC}$, đóng Chopper tại $700\text{ V}$, trip tại $800\text{ V}$ (`Khối 2 & 3 - SOW-2.1, SOW-3.1`)
    4. Thời gian đáp ứng mô-men: $\Delta t_{\text{torque}} \le 10\text{ ms}$ (`Khối 3 - SOW-3.3`)
    5. Mô-men giữ mở phanh & Ngưỡng tốc độ logic: $M_{\text{hold}}(0\text{ rpm}) \in [100\%; 150\%] M_{\text{đm}}$, đóng phanh tại $|v| \le 0.005\text{ m/s}$, cấm đảo chiều khi $|v| > 0.002\text{ m/s}$ (`Khối 3 - SOW-3.4`)
    6. Lực kéo cực đại khi tăng tốc: $F_{\max} = 9,218\text{ N} \approx 9.22\text{ kN}$ (`Khối 2 & 3 - SOW-2.1, SOW-3.1`)
    7. Bội số mô-men cực đại động cơ: $\lambda_{\max} = M_{\max}/M_{\text{đm}} \ge 2.0$ (`Khối 2 & 3 - SOW-2.1, SOW-3.1`)
    8. Cấp tốc độ bò định vị (Creep speed): $v_{\text{creep}} = (25\% \div 30\%) v_{\max} = 0.030 \div 0.036\text{ m/s}$ (`Khối 3 - SOW-3.3`)
  - Các ràng buộc thiết kế mới phát sinh khi tính chọn ở Khối 2 & 3 được gán mã `SRS-Dxx`, **bắt buộc có yêu cầu cha** (`Cha: SRS-FUNC/PERM-xx`) và bước tính sinh ra nó.
  - Phiên bản SRS khi cập nhật yêu cầu dẫn xuất: `Baseline A (v1.2)` $\to$ `A.1` $\to$ `A.2`; mỗi lần đổi ghi **lý do, ngày, ID bị ảnh hưởng**.
- **Mã kiểm chứng (DVP&R L0 v1.2):** 8 bài đo `DV-01` $\to$ `DV-08` (tương ứng `DVP-L0-01..08`) tổ chức trong 3 kịch bản tích hợp `TS-01..03`, dùng 3 phương pháp: `A` (Analysis/Excel), `S` (Simulation/Simulink), `I` (Inspection/Catalogue).

---

## 3. Quy trình & Cổng duyệt (Bắt đầu thực thi từ Cổng G3 — Khối 2)
```
[ĐÃ HOÀN THÀNH & ĐÓNG BĂNG]
✔ G0 (Khối 0 - MCR)     : PRD v3.1 + SOW v1.2 + HOQ/ICE v1.1 (Chốt Solution C, thông số x = 2)
✔ G1 (Tiêu chuẩn & SSoT): Hệ thống chuẩn trong Tài liệu tham khảo + Bảng SSoT 20 thông số (P-01..P-20)
✔ G2 (Khối 1 - SRR-EVT) : SRS Baseline A v1.2 (8 mã) + Boundary/P-Diagram + RTM & DVP L0 v1.2

[BẮT ĐẦU THỰC HIỆN TỪ ĐÂY]
➔ G3 (Khối 2 - PDR-EVT) : Kiến trúc hệ thống (SOW-2.1..2.3): SAD, Trade-off cấu hình, ICD (PDS theo IEC 61800-2),
                          bảng phân bổ SRS & 8 Downstream Allocation → phân hệ, BOM sơ bộ 3 cấp, DFMEA L1
                          → Checker chạy kiểm khớp → NGƯỜI DÙNG DUYỆT phương án kiến trúc & thiết bị sơ bộ.
➔ G4 (Khối 3 - CDR-EVT) : Thiết kế chi tiết (SOW-3.1..3.5):
                          • Phần lực: Tính chọn động cơ (S3-40%, k_dt ≥ 1.20 theo SRS A.1, λ_max ≥ 2.0), hộp số, biến tần,
                            điện trở xả hãm R_h, quy đổi M/J, sơ đồ nguyên lý mạch lực & BOM chính thức.
                          • Phần điều khiển & Logic: Tham số động cơ, tổng hợp mạch vòng dòng điện (MO) & tốc độ (SO) FOC,
                            quỹ đạo S-curve 7 đoạn, máy trạng thái FSM 4 góc phần tư & logic phanh cơ.
                          • Sinh SRS-Dxx → cập nhật SRS (A.1…) / RTM / DVP cấp phân hệ & WCCA rút gọn.
➔ G5 (Khối 4 - TRR-EVT) : Chuẩn bị thử nghiệm (SOW-4.1..4.2): Xây dựng mô hình Simulink tích hợp, cấu hình solver
                          (T_s ≤ 10^-4 s, bộ lọc đạo hàm G_d(s)), kịch bản TS-01..03 (DV-01..08) → khóa phiên bản mô hình.
➔ G6 (Khối 5 - SIR/SAR) : Tích hợp & mô phỏng (SOW-5.1..5.3): Chạy Simulink, điền kết quả thật vào cột Report của DVP&R L0,
                          xử lý NCR rút gọn (nếu có) → Checker chạy K6–K12 → Thuyết minh tổng hợp & Slide bảo vệ.
```
Dừng lại hỏi người dùng **bắt buộc** tại: **G3 (PDR-EVT)**, **G4 (CDR-EVT)**, và bất cứ khi nào Checker báo **XUNG ĐỘT**. Các bước khác chạy liền, chỉ dừng khi có cảnh báo ⚠.

---

## 4. Danh mục Tài liệu Tham khảo, Tiêu chuẩn & Công thức Tính toán Cốt lõi
Toàn bộ các tệp PDF/PPTX đã có sẵn trong thư mục **`Lưu đồ dự án/Tài liệu tham khảo/`** (Mức truy cập: **Toàn văn đọc được — Đã xác minh**). Khi viết Khối 2 – Khối 5, AI và nhóm bắt buộc trích dẫn đúng mã và công thức từ các tệp này:

### 4.1. Bảng ánh xạ Kho tài liệu trong `Lưu đồ dự án/Tài liệu tham khảo/`
| Mã trích dẫn | Tệp trong `Lưu đồ dự án/Tài liệu tham khảo/` | Tên Tiêu chuẩn / Tài liệu & Tác giả | Nội dung áp dụng cho Khối 2 – Khối 5 |
| :---: | :--- | :--- | :--- |
| **`[R1]`** | `tcvn-4244-2005.pdf` | **TCVN 4244:2005** — Thiết bị nâng: Thiết kế, chế tạo và kiểm tra kỹ thuật | • Nhóm chế độ làm việc cơ cấu **ISO M5 / FEM 2m** (§2.1.1.3, tr.28–30).<br>• Phanh tự động thường đóng, hệ số an toàn phanh $k_p \ge 1.1 \div 1.25$ (§1.5.3.3, tr.14–15).<br>• Cấm đảo chiều khi $v \ne 0$ (§1.5.7.2.9, tr.21) & liên khóa phanh điện–cơ (§2.4.5.5.2, tr.94).<br>• Công thức tính lực cản di chuyển xe con $W_t$ (§2.4.7.2.2, tr.99–101). |
| **`[R4]`** | `Thầy Đỉnh/TIÊU CHUẨN VN VÀ QUỐC TẾ.pdf` | **Tiêu chuẩn VN và Quốc tế phục vụ Thiết kế TĐĐ** (TS. Nguyễn Duy Đỉnh) | • Chế độ ngắn hạn lặp lại **S3** ($CD = 40\%$, chu kỳ $10\text{ phút}$) theo **IEC 60034-1** (tr.23).<br>• Kiến trúc hệ truyền động điện biến tần **PDS** (`CDM`, `BDM`, `CU`, `M`) và cấp chất lượng theo **IEC 61800-2** (tr.85–92).<br>• Cấp bảo vệ vỏ **IEC 60529** $\ge \text{IP54}$ (tr.16–17). |
| **`[R5-B1]`** | `Thầy Đỉnh/Bài 1.pdf` & `Class_1_Introduction.pptx` | **Bài 1: Tổng quan Thiết kế Hệ TĐĐ** (TS. Nguyễn Duy Đỉnh) | Quy trình thiết kế hệ truyền động điện, phân tích yêu cầu công nghệ và cấu trúc chung. |
| **`[R5-B2]`** | `Thầy Đỉnh/Bài 2.1.pdf`, `Bài 2.2.pdf`, `Bài 2.3.pdf` | **Bài 2: Tính chọn công suất động cơ & Quy đổi cơ học** (TS. Nguyễn Duy Đỉnh) | • Quy đổi lực cản, mô-men cản tĩnh $M_c$ và mô-men quán tính $J_{\Sigma}$ về trục động cơ.<br>• Phương pháp mô-men/công suất đẳng trị nhiệt ($M_{\text{đt}}, P_{\text{đt}}$) cho chế độ ngắn hạn lặp lại **S3**.<br>• Kiểm nghiệm quá tải mô-men ($\lambda_{\max}$), khởi động và phát nhiệt. |
| **`[R5-B3]`** | `Thầy Đỉnh/Bài 3.pdf` & `Class_3_AC_Motor_Drive.pptx` | **Bài 3: Điều khiển Truyền động điện Xoay chiều (FOC)** (TS. Nguyễn Duy Đỉnh) | • Mô hình toán học động cơ KĐB 3 pha trên hệ tọa độ từ thông rotor $(d, q)$.<br>• Cấu trúc điều khiển Vector tựa từ thông rotor (**RFOC**).<br>• Tổng hợp bộ điều khiển PI mạch vòng dòng điện theo **Tối ưu Module (MO)** và PI mạch vòng tốc độ theo **Tối ưu Đối xứng (SO)**. |
| **`[R5-B4]`** | `Thầy Đỉnh/Bài 4.pdf` & `Class_2_Elevator.pptx` | **Bài 4: Hệ TĐĐ Cầu trục & Thang máy** (TS. Nguyễn Duy Đỉnh) | • Đặc tính cơ 4 góc phần tư của cầu trục.<br>• Điều kiện bám dính chống trượt bánh xe thép trên ray thép ($\varphi = 0.20$, $F_{\max} \le F_{\text{bám}}$, tr.43–52).<br>• Tính toán mạch hãm tái sinh và điện trở xả hãm $R_h$. |
| **`[R9-01]`** | `Crane trolley Nhật Bổn.pdf` | **Mita & Kanai (1979)** — *Optimal Control of the Crane System* | Phương trình vi phân dao động con lắc tải treo cáp $\ddot{\theta} + (g/l)\theta = a(t)/l$ và phân tích động học 3 pha. |
| **`[R9-02]`** | `Cầu trục_Indo.pdf` | **Feto et al. (2025)** — *Overhead Travelling Crane 10 Ton* | Thiết kế chuỗi truyền động cơ khí: động cơ, hộp giảm tốc, khớp nối, bánh xe, phanh cơ. |
| **`[R9-03]`** | `Thiết kế cầu trục dầm đôi_Thổ.pdf` | **Doğan (2023)** — *Double Girder Overhead Crane 10t* | Đối chứng công suất động cơ di chuyển xe con tải 10–15t thực tế ($\sim 1.5 \div 4\text{ kW}$) và hệ số động lực học theo TS EN 13001. |
| **`[R9-04]`** | `A54.pdf` (tên tệp không phản ánh nội dung) | **Valtchev et al. (2024)** — *DAS 2024* | Tăng khả năng dập dao động của hệ truyền động cầu trục khi tải treo mềm. |
| **`[R9-05]`** | `SM2693.pdf` | **Zheng et al. (2021)** — *Sensors & Materials* | Mô hình động lực học 2 bậc tự do (2-DOF) xe con – tải treo cáp và phân tích vọt lố. |
| **`[R9-06]`** | `Shevchenko_bakalavr.pdf` | **Y. O. Shevchenko (KPI, 2024)** — *Đồ án TĐĐ Cầu trục (Core Reference)* | **Tài liệu mẫu hạt nhân cho Khối 2 & 3:** Công thức tính chọn phần lực chế độ S3, chọn biến tần + Braking Chopper + $R_h$, tính 5 tham số mạch thay thế ĐC KĐB, tổng hợp bộ điều khiển PI dòng điện (MO) & PI tốc độ (SO) trong RFOC và sơ đồ Simulink. |
| **`[R9-07]`** | `Dầm đôi_cấu trúc truyền động_Đức.pdf` | **Catalogue Demag DR/EZDR** — *Double-Rail Crab* | Chuẩn cấu hình công nghiệp Châu Âu: Động cơ KĐB gắn sẵn Pulse Encoder (tr.4), biến tần tích hợp điện trở xả hãm (tr.8), phanh đĩa điện từ. |
| **`[R9-10]`** | — | *Không sử dụng* | Kho không có tiêu chuẩn DIN 536/ray A54; $D_{bx} = 0.25$ m, $w_0 = 0.015$ là giả định `[C]` (tính kiểm $w_0$ ở SSoT Phần 1b). |
| **`[R9-11]`**, **`[R9-12]`** | `S-curve.pdf`, `S-curve-simulation.pdf` | **Ho Duc Tho et al. (2020)**; **Blejan & Blejan (2020)** | Quy hoạch quỹ đạo **S-Curve** giới hạn đồng thời vận tốc, gia tốc và độ giật. Thêm `[R9-13]` Reutov (2021) và `[R9-14]` Abdel-Rahman et al. (2003) — xem `Tài liệu tham khảo/00_Danh_muc_tai_lieu_tham_khao.md`. |
| **`[R8]`** | `Bản sao của [NHÓM 2] Thiết kế truyền động xe con cầu trục 2.pptx.pdf` | **Báo cáo tham khảo sinh viên (Nhóm 2)** | Tài liệu tham khảo nội bộ về bố cục trình bày slide/báo cáo môn học (chỉ tham khảo cấu trúc, không chép số liệu). |

---

### 4.2. Bộ Công thức Tính toán Chuẩn (Áp dụng thống nhất cho Khối 2, Khối 3 & Excel/Simulink)

Để đảm bảo nguyên tắc **"Người dùng hiểu và bảo vệ được từng con số"** và nhất quán 100% với `SSoT v1.2`, mọi tính toán ở Khối 2 & Khối 3 phải sử dụng bộ công thức chuẩn dưới đây:

#### A. Nhóm công thức Động học & Phụ tải Tĩnh (`[R1, §2.4.7.2.2]`, `[R5-B2]`; $w_0$: giả định `[C]`, tính kiểm ở SSoT Phần 1b)
1. **Tổng khối lượng dịch chuyển:**
   - Đầy tải (`P-04`): $M_\Sigma = Q + m_{nh} + m_{xc} = 12,222 + 222 + 1,800 = 14,244\text{ kg}$
   - Không tải (`P-05`): $m_{\text{tĩnh}} = m_{nh} + m_{xc} = 222 + 1,800 = 2,022\text{ kg}$
2. **Tốc độ góc và tốc độ vòng trục bánh xe (`P-09`, `P-12`):**
   $$\omega_{\text{bx}} = \frac{2 \cdot v_{\max}}{D_{bx}} = \frac{2 \cdot 0.12}{0.25} = 0.96\text{ rad/s}, \quad n_{\text{bx}} = \frac{60 \cdot \omega_{\text{bx}}}{2\pi} \approx 9.17\text{ vg/ph}$$
3. **Lực cản chuyển động tĩnh (Cản lăn trên ray ngang, độ dốc $= 0$, trong nhà xưởng không gió):**
   - Đầy tải (`P-20`):
     $$F_{c.\text{đầy}} = M_\Sigma \cdot g \cdot w_0 = 14,244 \cdot 9.81 \cdot 0.015 \approx 2,096\text{ N}$$
   - Không tải:
     $$F_{c.\text{không}} = m_{\text{tĩnh}} \cdot g \cdot w_0 = 2,022 \cdot 9.81 \cdot 0.015 \approx 298\text{ N}$$
   *(Ghi chú bảo vệ tại Cổng G3/G4: Trong `[R1, TCVN 4244 §2.4.7.2.2]`, suất cản lăn có thể viết dạng chi tiết $w_0 = k_{\text{gờ}} \cdot \frac{2f + \mu_{ol} \cdot d_{\text{trục}}}{D_{bx}}$; giá trị quy chuẩn cho bánh xe thép $D_{bx}=0.25\text{ m}$ dùng ổ lăn trên ray A54 là $w_0 = 0.015$).
4. **Công suất cản tĩnh yêu cầu trên trục động cơ (với hiệu suất cơ khí $\eta = 0.90$, `P-15`):**
   $$P_{\text{tĩnh,đầy}} = \frac{F_{c.\text{đầy}} \cdot v_{\max}}{\eta} = \frac{2,096 \cdot 0.12}{0.90} \approx 279.5\text{ W} \approx 0.28\text{ kW}$$

#### B. Nhóm công thức Động lực học Quá độ, Chống trượt & Quy đổi về Trục Động cơ (`[R5-B2]`, `[R5-B4, tr.43–52]`, `[R9-06]`)
1. **Lực quán tính & Lực kéo tiếp tuyến cực đại khi tăng tốc đầy tải ($a_{\max} = 0.50\text{ m/s}^2$, `P-10`):**
   $$F_{qt,\max} = M_\Sigma \cdot a_{\max} = 14,244 \cdot 0.50 = 7,122\text{ N}$$
   $$F_{\max} = F_{c.\text{đầy}} + F_{qt,\max} = 2,096 + 7,122 = 9,218\text{ N} \approx 9.22\text{ kN}$$
2. **Công suất cơ học đỉnh trong giai đoạn gia tốc đầy tải:**
   $$P_{\max} = \frac{F_{\max} \cdot v_{\max}}{\eta} = \frac{9,218 \cdot 0.12}{0.90} \approx 1,229\text{ W} \approx 1.23\text{ kW}$$
3. **Kiểm tra điều kiện bám chống trượt bánh xe chủ động trên ray thép khô (`[R5-B4, tr.43]`, $\varphi = 0.20$, giả sử 2/4 bánh xe là bánh chủ động chịu 50% trọng lượng bám $k_{\text{dẫn}} = 0.5$):**
   $$F_{\text{bám}} = \varphi \cdot k_{\text{dẫn}} \cdot M_\Sigma \cdot g = 0.20 \cdot 0.50 \cdot 14,244 \cdot 9.81 \approx 13,973\text{ N}$$
   $$k_{\text{bám}} = \frac{F_{\text{bám}}}{F_{\max}} = \frac{13,973}{9,218} \approx 1.52 \ge 1.20 \quad (\text{ĐẠT chuẩn SRS-PERM-01})$$
   *(Trường hợp không tải $m_{\text{tĩnh}} = 2,022\text{ kg}$ cũng cần kiểm tra lại tương tự trong Excel ở Khối 3).*
4. **Quy đổi Mô-men cản tĩnh và Mô-men quán tính về trục động cơ (với tỷ số truyền hộp số $i$, tốc độ góc động cơ $\omega_m = i \cdot \omega_{\text{bx}}$):**
   - Khi động cơ kéo tải (Góc phần tư I, III):
     $$M_{c,\text{kéo}} = \frac{F_c \cdot D_{bx}}{2 \cdot i \cdot \eta}$$
   - Khi động cơ hãm tái sinh (Góc phần tư II, IV — năng lượng truyền ngược từ tải về động cơ):
     $$M_{c,\text{hãm}} = \frac{F_c \cdot D_{bx} \cdot \eta}{2 \cdot i}$$
   - Mô-men quán tính tổng quy đổi về trục động cơ (hệ số $\delta \approx 1.1 \div 1.2$ kể đến quán tính các chi tiết quay của hộp số và khớp nối):
     $$J_\Sigma = J_{\text{đc}} + \delta \cdot M_\Sigma \cdot \left(\frac{v_{\max}}{\omega_m}\right)^2 = J_{\text{đc}} + \delta \cdot M_\Sigma \cdot \left(\frac{D_{bx}}{2 \cdot i}\right)^2$$

#### C. Nhóm công thức Định cỡ Nhiệt Chế độ $S3 - 40\%$, Phanh cơ & Điện trở Xả hãm $R_h$ (`[R4, tr.23]`, `[R5-B2]`, `[R5-B4]`, `[R9-06]`)
1. **Mô-men và Công suất đẳng trị nhiệt trong chu kỳ ngắn hạn lặp lại $S3$ ($CD = 40\%$, chu kỳ chuẩn $T_{\text{ck}} = 10\text{ phút} = 600\text{ s}$, tổng thời gian động cơ đóng điện $\sum t_{\text{lv}} = 240\text{ s}$, thời gian nghỉ $\sum t_0 = 360\text{ s}$):**
   $$M_{\text{đt}} = \sqrt{\frac{\sum_{k} M_k^2 \cdot t_k}{\sum_{k} t_{\text{lv},k}}}, \quad P_{\text{đt}} = M_{\text{đt}} \cdot \omega_{\text{đm}}$$
2. **Quy đổi chọn động cơ theo Catalogue và Hệ số dự trữ phát nhiệt (`SRS-PERM-04`, `QCD-C01`):**
   - Nếu chọn động cơ chuyên dụng cầu trục có ghi trực tiếp công suất định mức ở chế độ $S3 - 40\%$: dùng trực tiếp $P_{\text{đm}(S3-40\%)}$.
   - Nếu tra catalogue động cơ công nghiệp tiêu chuẩn chỉ ghi công suất dài hạn $S1$ ($P_{\text{đm}(S1)}$), công suất cho phép ở chế độ $S3$ ($CD = 40\%$) được quy đổi hoặc kiểm tra qua hệ số quá tải nhiệt. Hệ số dự trữ phát nhiệt phải thỏa mãn:
     $$k_{dt} = \frac{P_{\text{đm}}}{P_{\text{đt}}} \ge 1.20$$
     *(Sửa 26/10/2026 theo SRS Baseline A.1, CR-01: bỏ cận trên 1.50 vì với xe con chạy chậm, khối lượng lớn, động cơ được định cỡ theo mô-men đỉnh $\lambda$ nên $k_{dt}$ thường lớn hơn nhiều so với 1.5. Chống chọn dư công suất bằng `QCD-C01`: $P_{\text{đm}} \le 1.5\,P_{\max}$ (QĐ-08).)*
   - Kiểm tra khả năng quá tải mô-men khi sụt áp lưới $-10\%$ ($U_{\min} = 0.9 U_{\text{đm}}$):
     $$\lambda_{\max,\text{catalogue}} \cdot (0.9)^2 \ge \frac{M_{\max}}{M_{\text{đm}}} \quad (\text{với } \lambda_{\max,\text{catalogue}} \ge 2.0)$$
3. **Kiểm tra Mô-men giữ của Phanh cơ điện từ thường đóng (`[R1, TCVN 4244 §1.5.3.3]`):**
   $$M_{\text{phanh}} \ge k_p \cdot M_{c,\text{đầy}} \quad (\text{hoặc } M_{\text{phanh}} \ge 1.5 \div 1.8\, M_{\text{đm}} \text{ theo chuẩn Demag } \text{[R9-07]})$$
4. **Tính chọn Bộ băm xung áp (Braking Chopper) và Điện trở xả hãm tái sinh $R_h$ (`[R5-B4]`, `[R9-06]`):**
   - Công suất hãm cực đại trả về trục động cơ và thanh cái DC-link khi giảm tốc đầy tải với $|a_{\max}| = 0.50\text{ m/s}^2$:
     $$F_{\text{hãm},\max} = M_\Sigma \cdot a_{\max} - F_{c.\text{đầy}} = 7,122 - 2,096 = 5,026\text{ N}$$
     $$P_{\text{dc,hãm},\max} \approx F_{\text{hãm},\max} \cdot v_{\max} \cdot \eta_{\text{cơ}} \cdot \eta_{\text{đc}} \cdot \eta_{\text{inv}}$$
   - Giá trị điện trở xả hãm $R_h$ (để hấp thụ được công suất đỉnh $P_{\text{dc,hãm},\max}$ tại ngưỡng điện áp mở Chopper $U_{\text{chop}} \approx 700\text{ V DC}$ mà không để $U_{\text{dc}}$ chạm ngưỡng bảo vệ $U_{\max} = 780\text{ V DC}$, đồng thời không vượt dòng đỉnh $I_{\text{chop},\max}$ của IGBT hãm):
     $$\frac{U_{\text{chop}}}{I_{\text{chop},\max}} \le R_h \le \frac{U_{\text{chop}}^2}{P_{\text{dc,hãm},\max}}$$

#### D. Nhóm công thức Quỹ đạo S-Curve 7 đoạn, Tổng hợp Điều khiển RFOC & Mô hình Con lắc (`[R5-B3]`, `[R9-01]`, `[R9-06]`, `[R9-11]`)
1. **Quy hoạch quỹ đạo tốc độ S-Curve 7 đoạn (`[R9-11, Tho et al. 2020]`):**
   - Với $v_{\max} = 0.12\text{ m/s}$, $a_{\max} = 0.50\text{ m/s}^2$, $\rho_{\max} = 2.00\text{ m/s}^3$:
   - Kiểm tra điều kiện đạt đỉnh gia tốc $a_{\max}$: do $v_{\max} = 0.12\text{ m/s} \le \frac{a_{\max}^2}{\rho_{\max}} = \frac{0.50^2}{2.00} = 0.125\text{ m/s}$, khi tăng tốc từ $0 \to 0.12\text{ m/s}$:
     - Nếu thiết kế giữ đúng $\rho^* = 2.00\text{ m/s}^3$, gia tốc đạt đỉnh $a_{\text{peak}} = \sqrt{v_{\max} \cdot \rho^*} = \sqrt{0.12 \cdot 2.00} \approx 0.49\text{ m/s}^2 \le 0.50\text{ m/s}^2$ (suy biến pha gia tốc hằng $T_a = 0$, thời gian tăng độ giật $T_j = a_{\text{peak}}/\rho^* \approx 0.245\text{ s}$, tổng thời gian tăng tốc $t_{\text{acc}} = 2 T_j \approx 0.49\text{ s}$).
     - Nếu chọn $\rho^* \le 2.00\text{ m/s}^3$ và $a^* \le 0.45 \div 0.48\text{ m/s}^2$ để có đủ cả 3 đoạn trong quá trình tăng tốc (tăng jerk $T_j$ – giữ gia tốc không đổi $T_a > 0$ – giảm jerk $T_j$), thì chọn $a^*$ và $\rho^*$ thỏa mãn $v_{\max} > \frac{(a^*)^2}{\rho^*}$, khi đó:
       $$T_j = \frac{a^*}{\rho^*}, \quad T_a = \frac{v_{\max}}{a^*} - T_j, \quad t_{\text{acc}} = 2 T_j + T_a$$
2. **Tổng hợp Bộ điều khiển Dòng điện và Tốc độ trong RFOC (`[R5-B3]`, `[R9-06, Shevchenko 2024]`):**
   - Mô-men điện từ động cơ KĐB khi định hướng theo từ thông rotor ($\psi_{rq} = 0, \psi_{rd} = \psi_r = L_m i_{sd}$):
     $$M_e = \frac{3}{2} p \frac{L_m}{L_r} \psi_r i_{sq} = k_M \cdot i_{sq}$$
   - **Mạch vòng dòng điện ($i_{sd}, i_{sq}$) — Chuẩn Tối ưu Module (MO):** Bù hằng số thời gian điện từ tương đương $T_{\sigma}$ bằng phần tử tích phân $T_{i,I} = T_{\sigma}$, hệ số khuếch đại $K_{p,I} = \frac{L_{\sigma}}{2 \cdot T_{\mu i}}$ (với $T_{\mu i}$ là hằng số thời gian nhỏ không bù của mạch biến tần & lấy mẫu, đảm bảo $\Delta t_{\text{torque}} \le 10\text{ ms}$).
   - **Mạch vòng tốc độ ($\omega$) — Chuẩn Tối ưu Đối xứng (SO):** Tổng hợp bộ điều khiển PI tốc độ với $T_{i,\omega} = 4 T_{\Sigma\omega}$ và $K_{p,\omega} = \frac{J_\Sigma}{2 \cdot k_M \cdot T_{\Sigma\omega}}$ (kèm bộ lọc đầu vào hoặc kết hợp quỹ đạo S-Curve để giữ độ quá điều chỉnh $M_p \le 10.0\%$ và sai lệch xác lập $e_{xl} = 0\% \le 5.0\%$).
3. **Phương trình động lực học Con lắc Tải treo Cáp dài $h = 12\text{ m}$ (`[R9-01, Mita & Kanai 1979]`, `[R9-04]`):**
   $$\ddot{\theta}(t) + 2\zeta\omega_p\dot{\theta}(t) + \frac{g}{h}\sin\theta(t) = \frac{a(t)}{h}\cos\theta(t) \quad \left(\text{Tuyến tính hóa góc nhỏ: } \ddot{\theta}(t) + \omega_p^2 \theta(t) = \frac{a(t)}{h}, \text{ với } \omega_p = \sqrt{\frac{g}{h}} \approx 0.904\text{ rad/s}\right)$$
   - Phản lực ngang của cáp tác dụng ngược lên xe con: $F_{\text{lắc cáp}}(t) \approx (Q + m_{nh}) \cdot g \cdot \theta(t)$.

---

## 5. Phạm vi từng khối (Trạng thái & Giữ / Bỏ từ Khối 2 đến Khối 5)
| Khối | Trạng thái | GIỮ (Thực hiện đầy đủ) | BỎ (Ghi `Không áp dụng vì đồ án mô phỏng`) |
|---|:---:|---|---|
| **0 PRD/SOW/HOQ** | **ĐÃ XONG (`Frozen`)** | Giữ nguyên `Block 0/01..04` (`PRD v3.1`, `SOW v1.2`, `HOQ v1.1`, Slide MCR) | Đã phân định rõ Out-of-Scope trong `SOW v1.2` |
| **1 SRS/RTM/DVP** | **ĐÃ XONG (`Frozen`)** | Giữ nguyên `Block 1/00..06` (`SSoT`, `SRS Baseline A v1.2`, `Boundary/P-Diagram`, `RTM/DVP v1.2`) | Đã chuyển 8 thông số chi tiết xuống Khối 2 & 3 qua Downstream Allocation |
| **2 Kiến trúc (`WBS 2.0`)** | **BẮT ĐẦU LÀM** | • Tài liệu kiến trúc **SAD** & sơ đồ khối theo chuẩn PDS **IEC 61800-2** (`[R4]`: `CDM`, `CU`, Động cơ, Hộp số, Phanh, Encoder).<br>• Trade-off ngắn cho cấu hình chi tiết (ví dụ: động cơ liền hộp số vs rời, phương án bố trí dẫn động 2 bánh).<br>• **ICD** (tín hiệu, đơn vị, dải giá trị giữa Phần lực – Điều khiển – Cơ khí).<br>• Bảng phân bổ `8 SRS Baseline A` + `8 Downstream Allocation` $\to$ các phân hệ.<br>• **BOM sơ bộ 3 cấp** (`SOW-2.2`) & **DFMEA L1** (`SOW-2.3`) cho các lỗi cốt lõi (`RRM-01..04`). | Long-lead items mua sắm thực tế, khoảng cách rò điện Creepage/Clearance trên PCB, thiết kế vỏ tủ cơ khí 3D. |
| **3 Thiết kế chi tiết (`WBS 3.0`)** | **TIẾP THEO** | • Tính chọn động cơ chế độ $S3-40\%$ ($k_{dt} \ge 1.20$ theo SRS A.1, $\lambda_{\max} \ge 2.0$), kiểm tra bám $k_{\text{bám}} \ge 1.20$, quy đổi $M/J$ về trục động cơ, chọn biến tần & tính điện trở xả hãm $R_h$ theo mục 4.2 (`SOW-3.1`).<br>• Sơ đồ nguyên lý mạch động lực & **BOM chính thức** có mã catalogue (`SOW-3.2`).<br>• Tham số mô hình toán ĐC, thiết kế quỹ đạo **S-curve 7 đoạn**, tổng hợp bộ điều khiển dòng điện (MO) & tốc độ (SO) của **RFOC** (`SOW-3.3`).<br>• Lưu đồ & hàm logic **FSM 4 góc phần tư**, khóa chéo cấm đảo chiều khi $v \ne 0$, đồng bộ phanh cơ (`SOW-3.4`).<br>• Sinh `SRS-Dxx`, cập nhật RTM/DVP phân hệ, WCCA rút gọn (đầy tải $14,244\text{ kg}$ + sụt áp $-10\%$) (`SOW-3.5`). | Bản vẽ layout PCB/Gerber, phân tích SI/PI, mô phỏng nhiệt FEM 3D chi tiết, gia công phôi cơ khí. |
| **4 Chuẩn bị thử (`WBS 4.0`)** | **TIẾP THEO** | • Mô hình MATLAB/Simulink hoàn chỉnh nối với `init_params.m` (`SOW-4.1`).<br>• Thiết lập 3 kịch bản tích hợp `TS-01..03` bao phủ `DV-01..08`, cấu hình solver bước nhỏ $T_s \le 10^{-4}\text{ s}$, khâu lọc đạo hàm đo độ giật $G_d(s) = \frac{s}{T_f s + 1}$, khóa phiên bản mô hình (`SOW-4.2`). | Hiệu chuẩn thiết bị đo vật lý, đồ gá thử tải xưởng, kiểm kê mẫu phần cứng, kế hoạch an toàn điện trường thử. |
| **5 Tích hợp & thử (`WBS 5.0`)** | **TIẾP THEO** | • Chạy mô phỏng, trích xuất đồ thị $v(t), a(t), \rho(t), M_e(t), U_{dc}(t), I_{Rh}(t), \theta(t)$ (`SOW-5.1`).<br>• Điền kết quả thực tế vào cột `Report` của `DVP&R L0 Report` (`DV-01..08`), lập NCR rút gọn nếu có chỉ tiêu lệch (`SOW-5.2`).<br>• Đóng gói Thuyết minh tổng hợp, Bảng tính, BOM, Bản vẽ mạch lực & Slide bảo vệ (`SOW-5.3`). | Chạy bền $T_{\min}$ giờ thực tế, đo ảnh nhiệt hồng ngoại hotspot, đo bức xạ EMC pre-scan, hội đồng ECR/CCB công nghiệp. |

---

## 6. Quy tắc file Excel (Tính toán ở Khối 2 & Khối 3)
1. Một sheet `Params` duy nhất chứa trọn vẹn **20 thông số gốc `P-01..P-20`** từ `Block 1/00_Bang_thong_so_goc_SSoT.md`: cột `Mã P-xx | Ký hiệu | Giá trị | Đơn vị | Loại [A/B/C] | ID yêu cầu | Nguồn`. Các sheet khác **tham chiếu bằng công thức**, tuyệt đối không gõ lại số hằng.
2. Công thức tính chọn (theo đúng **Mục 4.2** ở trên: lực cản, công suất tĩnh $P_{\text{tĩnh}} \approx 0.28\text{ kW}$, lực kéo cực đại $F_{\max} = 9,218\text{ N}$, công suất cực đại $P_{\max} \approx 1.23\text{ kW}$, công suất đẳng trị $P_{\text{đt}}$ chế độ $S3-40\%$, quy đổi mô-men/quán tính, điện trở hãm $R_h$, tham số PI MO/SO) dùng công thức Excel thật. Mỗi khối tính có ô `Nguồn công thức` (`[R1]`, `[R5-B2]`, `[R5-B3]`, `[R5-B4]`, `[R9-06]`, `[R9-11]`).
3. Mỗi đại lượng có đơn vị rõ ràng; Checker bắt lỗi lệch đơn vị hoặc nhầm lẫn giữa $w_0 = 0.015$ và $\varphi = 0.20$.
4. Sheet `Kiểm tra` so kết quả tính với ngưỡng `SRS Baseline A` và `Downstream Allocation` ($k_{\text{bám}} \ge 1.20$, $k_{dt} \ge 1.20$ (SRS A.1), $\lambda_{\max} \ge 2.0$, $U_{\text{dc}} \le 780\text{ V}$...): trả về `Đạt/Không đạt/TBD` bằng công thức `IF`.
5. Sheet `Dẫn xuất`: mọi con số sinh ra ràng buộc thiết kế mới (công suất định mức động cơ chọn $P_{\text{đm}}$, tỷ số truyền thực tế $i_{\text{thực}}$, dòng định mức biến tần, giá trị $R_h, P_{Rh}$, thông số $K_p, T_i$...) kèm mã `SRS-Dxx` đề xuất và link tới yêu cầu cha.
6. Ghi phiên bản Excel (`v1.0`, ngày) ở sheet đầu.

---

## 7. Quy tắc MATLAB/Simulink (Khối 3, Khối 4 & Khối 5)
1. **Một nguồn thông số duy nhất**: script `init_params.m` đọc từ sheet `Params` / `Dẫn xuất` (hoặc đồng bộ 100% với `00_Bang_thong_so_goc_SSoT.md`). Mô hình Simulink dùng biến workspace, không chứa hằng số gõ tay trong block.
2. **Cấu hình cố định theo chuẩn DVP v1.2**:
   - Bước giải cố định (`ode4`) hoặc bước tối đa $T_s \le 10^{-4}\text{ s}$ ghi rõ trong `init_params.m`.
   - Gia tốc thực tế trích từ phương trình động lực học **2 khối lượng** (sửa 26/10/2026, nhóm C — SDD v1.3 §2.1): $a(t) = (F_k(t) - F_c(t) + F_{\text{lắc}}(t))/m_{xc}$ với $F_{\text{lắc}} = (Q + m_{nh})\,g\,\theta$ (quy ước dấu ICD IF-10), quy về trục động cơ bằng $J_{rig}$. Không chia cho $M_\Sigma$ khi đã cộng $F_{\text{lắc}}$ (sẽ tính khối lượng tải hai lần). $F_c$ vẫn bằng $M_\Sigma g w_0$. Mô hình khối cứng ($M_\Sigma$, không có $F_{\text{lắc}}$) chỉ dùng khi `mech_model` = 1 (DV-04 bảo thủ). Block 1 đã sửa đồng bộ ngày 26/10/2026 (SRS chi tiết v1.3 §5.4, RTM/DVP chi tiết v1.3 §3.4).
   - Phép đo độ giật thực tế $\rho(t) = \text{d}a/\text{d}t$ bắt buộc đi qua khâu lọc đạo hàm thực tế $G_d(s) = \frac{s}{T_f s + 1}$ với hằng số thời gian lọc $T_f = 0.005 \div 0.01\text{ s}$ (đúng quy định tại `Block 1/01_SRS_Chi_tiet_..._v1.2.md` §5.4) để tránh gai nhiễu số giả tạo.
3. **Kịch bản thử** được viết thành các script riêng (`test_TS01.m`, `test_TS02.m`, `test_TS03.m` hoặc `test_DV01.m`..`test_DV08.m`) ứng với 3 kịch bản tích hợp `TS-01..03` và 8 bài đo `DV-01..08` trong `03_RTM_DVP_..._v1.2.md`, tự động xuất log (`.mat`/`.csv`) các tín hiệu cần đo.
4. **Khóa phiên bản**: tên file mô hình (`.slx`) + ngày + phiên bản bộ tham số ghi trong `RUN_LOG.md`.
5. **AI không được khẳng định kết quả mô phỏng** nếu chưa có dữ liệu chạy thật do người dùng cung cấp. Trước khi chạy thật, cột kết quả trong DVP bắt buộc ghi `Report: chưa chạy`. Khi có log/đồ thị từ người dùng, AI mới điền số liệu đo thực tế, đánh giá `PASS/FAIL` và so với ngưỡng SRS.
6. AI sinh script/cấu hình/mô hình, người dùng chạy hoặc phối hợp chạy; nếu AI không trực tiếp chạy được MATLAB trong môi trường hiện tại thì nêu rõ điều đó.

---

## 8. Bộ kiểm khớp của Checker (Áp dụng từ Khối 2 đến Khối 5)
Mức: **⚠ Cảnh báo** (lệch, nên sửa) · **ℹ Gợi ý**.
*(Lưu ý: Các mục K1–K5 cho bản thân nội bộ Khối 0 & Khối 1 đã đạt 100% tại `Block 1/06_Bao_cao_Kiem_toan_Dong_bo_DVP_RTM_PRD_SOW_HOQ.md`. Từ Khối 2 trở đi, Checker tập trung kiểm tra sự kế thừa và nhất quán từ Khối 0/1 xuống Khối 2–5).*

| # | Kiểm | Mức |
|---|---|---|
| **K6** | **Nhất quán số liệu/đơn vị (SSoT `P-01..P-20`)**: Mọi đại lượng vật lý ($Q=12,222\text{ kg}$, $M_\Sigma=14,244\text{ kg}$, $m_{\text{tĩnh}}=2,022\text{ kg}$, $h=12\text{ m}$, $v_{\max}=0.12\text{ m/s}$, $a_{\max}\le 0.5\text{ m/s}^2$, $\rho_{\max}\le 2.0\text{ m/s}^3$, $D_{bx}=0.25\text{ m}$, $w_0=0.015$, $\varphi=0.20$, $\eta=0.90$, $F_{c.\text{đầy}}=2,096\text{ N}$, $S3-40\%$, $380\text{V}/50\text{Hz}$) phải khớp tuyệt đối từ `SSoT/SRS` sang `SAD/ICD (Khối 2)` – `Tính chọn/SDD/Excel (Khối 3)` – `Simulink (Khối 4–5)` | **⚠ (Ưu tiên cao nhất)** |
| **K7** | **Độ phủ phân bổ kiến trúc & mô phỏng**: Cả 8 mã `SRS Baseline A` (`SRS-FUNC-01..04`, `SRS-PERM-01..04`) và **8 thông số Downstream Design Allocation** đều phải được phân bổ rõ vào các phân hệ ở Khối 2 (SAD/ICD), được thiết kế chi tiết ở Khối 3, và có bài kiểm chứng đối ứng trong `DV-01..08` | ⚠ |
| **K8** | **Quản lý yêu cầu dẫn xuất (`SRS-Dxx`)**: Con số sinh ra từ tính chọn/thiết kế ở Khối 2–3 dùng làm ràng buộc (công suất ĐC, tỷ số truyền thực, ngưỡng băm Chopper, thông số PI...) phải được định danh `SRS-Dxx`, có yêu cầu cha (`SRS-FUNC/PERM-xx`), đúng công thức ở Mục 4.2 và có phép kiểm chứng | ⚠ |
| **K9** | **Khớp giao diện `ICD`**: Ký hiệu biến, đơn vị, chiều tín hiệu và dải giá trị phải khớp 100% giữa Sơ đồ khối SAD/ICD (Khối 2) ↔ Công thức tính chọn & SDD điều khiển/FSM (Khối 3) ↔ Khối vào/ra trên Simulink (Khối 4) | ⚠ |
| **K10** | **Kiểm chứng kết quả mô phỏng & Phiên bản**: Đối chiếu kết quả mô phỏng (Khối 5) với ngưỡng PASS/FAIL của `DV-01..08` và 8 thông số Downstream Allocation ($M_p \le 10\%$, $e_{xl} \le 5\%$, $U_{\text{dc}} \le 780\text{V}$, $\Delta s \le \pm 10\text{ mm}$...); báo rõ các mục `chưa chạy`; kiểm tra việc ghi lịch sử phiên bản khi cập nhật tài liệu | ⚠/ℹ |
| **K11** | **Phát hiện xung đột thiết kế**: Xung đột giữa thiết bị chọn/kết quả tính ở Khối 2–3 với yêu cầu gốc Khối 1 (ví dụ: động cơ chọn có $k_{dt} < 1.20$ hoặc vượt trần `QCD-C01` $P_{\text{đm}} \le 1.5\,P_{\max}$ (SRS A.1, QĐ-08), hoặc tỷ số truyền thực tế của hộp số catalogue làm lệch vận tốc quá $\pm 5\%$, hoặc giả định `[C]` bị thay đổi) → báo **XUNG ĐỘT**, nêu các phương án xử lý, không tự ý sửa SSoT | ⚠ |
| **K12** | **Tính hợp lệ của dẫn nguồn & Catalogue**: Kiểm tra việc trích dẫn đúng các file trong `Lưu đồ dự án/Tài liệu tham khảo/` (`[R1]..[R9-11]`); bất kỳ thông số động cơ, biến tần, hộp số nào đưa vào BOM/tính toán mà chưa có nguồn catalogue xác thực phải gắn nhãn `chưa xác minh` / `TBD` | ⚠ |

---

## 9. Định dạng đầu ra của Checker
1. **Phiên bản đã kiểm**: Đối chiếu tài liệu Khối 2/3/4/5 bản nào với `SSoT v1.2` & `SRS Baseline A v1.2`, Excel/Simulink bản nào, ngày kiểm.
2. **Ma trận khớp**: `PRD-xx ↔ SRS-xx (kèm Downstream Allocation / SRS-Dxx) ↔ Phân hệ (Khối 2) ↔ Thiết kế (Khối 3) ↔ DV-xx ↔ Report`, ô trống ghi rõ `trống`.
3. **Danh sách cảnh báo**, thứ tự ưu tiên: lệch số liệu SSoT (K6) → xung đột thiết kế (K11) → thiếu phân bổ/dẫn xuất (K7, K8) → lệch giao diện ICD (K9) → nguồn catalogue/chuẩn (K12). Mỗi dòng gồm: mã kiểm, **trích nguyên văn dòng lỗi + ID + tên file**, vì sao lệch, gợi ý hướng sửa (không sửa hộ).
4. **Danh sách giả định `[C]` cần xác nhận lại / TBD / chưa chạy / chưa xác minh** để nhóm theo dõi.
5. **Kết luận**: `Mức khớp: Tốt / Có chỗ lệch / Lệch nhiều`. Không dùng từ “Không đạt”.
6. Tối đa 2–3 câu hỏi làm rõ cho người dùng để chốt quyết định kỹ thuật tại cổng.

---

## 10. Cấm
- Tự ý sửa đổi các con số đã khóa trong `Block 0` và `Block 1` (`SSoT P-01..P-20`, `SRS Baseline A v1.2`, `RTM/DVP v1.2`) khi chưa có lệnh duyệt đổi Baseline từ người dùng.
- Bịa số hiệu chuẩn, điều khoản, mã hiệu/thông số catalogue động cơ – biến tần – hộp số, hoặc kết quả mô phỏng chưa chạy.
- Tự chọn phương án cấu hình hoặc tự đổi thông số khi phát sinh xung đột.
- Writer tự duyệt sản phẩm của mình.
- Sửa một thông số thiết kế ở Khối 2/3 mà không cập nhật đồng bộ sang Excel, ICD, `init_params.m` và RTM/DVP.
- Phạt các hạng mục đã được khai báo `Out-of-Scope` trong `SOW v1.2` hoặc `Không áp dụng`.

---

## 11. Điểm mở (Người dùng quyết định khi triển khai Khối 2 & Khối 3)
- **Cấu trúc thư mục & tài liệu:** Tạo tiếp thư mục `Lưu đồ dự án/Block 2/` (cho SAD, ICD, BOM sơ bộ, DFMEA L1) và `Lưu đồ dự án/Block 3/` tách biệt theo đúng cấu trúc `Block 0`, `Block 1` hiện có, hay gộp chung?
- **Vị trí ghi yêu cầu dẫn xuất (`SRS-Dxx`):** Ghi thành bảng tổng hợp trong tài liệu thiết kế Khối 2/3 (SAD/SDD) và phụ lục cập nhật `SRS Baseline A.1`, hay cập nhật trực tiếp vào bản copy của SRS?
- **Xác nhận 4 câu hỏi mở từ SSoT (Phần 3 của `00_Bang_thong_so_goc_SSoT.md`) khi bước vào Khối 2:**
  1. Đối chiếu lại tự trọng xe con $m_{xc} = 1,800\text{ kg}$ (`P-03 [C]`) với catalogue thực tế.
  2. Giữ nguyên cách tính lực cản theo suất cản lăn tổng hợp $w_0 = 0.015$ (`P-13 [C]`) như đã khóa ở Khối 1 hay trình bày kèm công thức giải tích ổ lăn từ `[R1, TCVN 4244 §2.4.7.2.2]`.
  3. Lựa chọn cấu hình truyền động cơ khí (`P-16 [C]`, $i \approx 150$): Động cơ liền hộp giảm tốc (*Geared Motor*) hay Động cơ rời + Hộp giảm tốc 3 cấp.
  4. Công thức quy đổi công suất tương đương giữa chế độ `S3 - 40%` (`P-17 [C]`) và công suất định mức `S1` trên catalogue theo `[R5-B2]` và `[R9-06]`.
