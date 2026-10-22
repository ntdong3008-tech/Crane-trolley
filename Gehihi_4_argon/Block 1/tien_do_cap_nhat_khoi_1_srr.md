# BÁO CÁO TIẾN ĐỘ CẬP NHẬT KHỐI 1 (CỔNG SRR-EVT) — NHÓM 8.5-EMG (ĐỀ $x = 2$)

> **Tên đề tài:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Di Chuyển Ngang Xe Con Cầu Trục ($x = 2$)  
> **Mã giai đoạn:** `WBS 1.0 (SOW-1.1, SOW-1.2, SOW-1.3 — Khối 1: Yêu cầu Hệ thống)`  
> **Cổng soát xét:** **Cổng 2 — `SRR-EVT` (*System Requirements Review — Engineering Verification Test*)**  
> **Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
> **Nhóm thực hiện:** Nhóm 8.5-EMG (Nguyễn Bá Hưng, Đặng Nguyên Bình, Trần Đỗ Khải, Phạm Văn Hưng, Nguyễn Hải Trung, Nghiêm Trọng Đông — STT 22 $\Rightarrow x = 2$)

---

## 1. TỔNG QUAN KẾT QUẢ HOÀN THÀNH KHỐI 1 (`WBS 1.0`)

Tiếp nối bộ hồ sơ **Khối 0 (`Gate MCR`)** đã khóa cứng thông số đề bài $x = 2$ ($Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg}$, $m_{xc} = 1,800\text{ kg} \Rightarrow M_\Sigma = 14,244\text{ kg}$, $m_{\text{tĩnh}} = 2,022\text{ kg}$, $h = 12\text{ m}$, $v_{\max} = 0.12\text{ m/s}$, $|a(t)| \le 0.50\text{ m/s}^2$, $|\rho(t)| \le 2.00\text{ m/s}^3$, $w_0 = 0.015$, $\varphi = 0.20$, $\eta = 0.96$, $F_c \approx 2.12\text{ kN}$, $P_{\text{tĩnh}} \approx 0.27\text{ kW}$, $F_{\max} \approx 9.25\text{ kN}$, $P_{\max} \approx 1.16\text{ kW}$) và chốt phương án cấu hình **`Solution C`** (`ĐC KĐB 3 pha S3--40% + Biến tần Vector RFOC + 01 Encoder vòng kín + Bộ tạo quỹ đạo S-Curve 7 đoạn + Braking Chopper & Điện trở xả hãm Rh`, đạt `812/1000` điểm ICE), Nhóm 8.5-EMG đã hoàn thành **100% 3 gói công việc của Khối 1 (`SOW-1.1`, `SOW-1.2`, `SOW-1.3`)**:

| Mã Gói WBS | Nội dung Công việc theo `SOW v1.1` | Thành viên Phụ trách (`R / A`) | Hồ sơ Minh chứng Đã Khóa (`Frozen`) | Trạng thái |
| :---: | :--- | :--- | :--- | :---: |
| **`SOW-1.1`** | Thiết lập **Sơ đồ Ranh giới Hệ thống (*Boundary Diagram*)**, **Sơ đồ Tham số (*P-Diagram*)** và chốt sơ bộ danh mục **`8 CTQ` + `5 CTS`**. | **R / A:** Nghiêm Trọng Đông (*PM / SE Lead*) | • `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md` (§2)<br>• `rtm_dvp_xe_con_cau_truc_x2_nhom_8_5_emg.md` (§1)<br>• `SRS-diagram.pptx` (Slide 5–9) | **100% (`PASS`)** |
| **`SOW-1.2`** | Phân rã từ `8 PRD + 8 HoQ EC` và biên soạn **Đường cơ sở Yêu cầu Kỹ thuật Hệ thống (`SRS Baseline A`)** gồm **9 yêu cầu kỹ thuật hệ thống (`4 FUNC + 5 PERM`)** theo chuẩn ISO/IEC/IEEE 29148:2018 (đã loại bỏ hoàn toàn cấp tốc độ bò, chỉ giữ 1 cấp làm việc định mức $v_{\max} = 0.12\text{ m/s}$). | **R:** Nguyễn Hải Trung (*Doc Lead*) phối hợp Bình, Khải, Bá Hưng<br>**A:** Nghiêm Trọng Đông | • `srs_xe_con_cau_truc_x2_nhom_8_5_emg (1).md` (§1 & §3: `SRS-FUNC-01..04` & `SRS-PERM-01..05`) | **100% (`PASS`)** |
| **`SOW-1.3`** | Thiết lập **Ma trận Truy xuất Yêu cầu Hai chiều (`Bidirectional RTM`)** (Xuôi 8 dòng & Ngược chuỗi `DMAIC` 9 dòng) và **Kế hoạch Kiểm chứng Cấp Hệ thống (`DVP&R Level 0`)** (**9 bài đo `DVP-L0-01..09`** qua **3 kịch bản `TS-01..03`**; chuyển $R_h$ và nhiệt $S3$ sang phương pháp Giải tích & Kiểm tra bản vẽ/BOM `A + I`). | **R:** Phạm Văn Hưng (*QE-Simulation*) & Nguyễn Hải Trung<br>**A:** Nghiêm Trọng Đông | • `rtm_dvp_xe_con_cau_truc_x2_nhom_8_5_emg.md` (§2, §3, §4) | **100% (`PASS`)** |

---

## 2. TÓM TẮT CÁC KẾT QUẢ KỸ THUẬT CỐT LÕI KHÓA TẠI CỔNG `SRR-EVT`

1. **Sơ đồ Ranh giới (*Boundary Diagram*) & Giao diện Vật lý:**
   - Phân định rạch ròi 3 phân vùng: **(1) Thực thể ngoài cấp nguồn & lệnh** (Lưới 3 pha $380\text{V} \pm 10\% / 50\text{Hz}$, Người vận hành cấp lệnh Tiến/Lùi/Chạy định mức/Dừng) $\leftrightarrow$ **(2) Hệ truyền động điện xe con *In-Scope*** (Mô-đun biến tần `CDM` theo chuẩn IEC 61800-2 có `Braking Chopper + Rh`, Khối điều khiển `CU` chứa `S-Curve 7 đoạn + RFOC + Logic phanh`, Động cơ KĐB $S3\text{--}40\%$, 01 `Pulse Encoder`, Phanh cơ thường đóng, Hộp giảm tốc 3 cấp $\eta = 0.96$, Bánh xe $d = 0.25\text{ m}$, Khung xe $m_{xc} = 1,800\text{ kg}$) $\leftrightarrow$ **(3) Phụ tải ngoài & Đường ray *Out-of-Scope*** (Tải nâng $Q = 12,222\text{ kg}$ + Cụm móc cáp $m_{nh} = 222\text{ kg}$ treo trên cáp dài $h = 12\text{ m}$ có tần số lắc tự nhiên $\omega_p \approx 0.904\text{ rad/s}$, hai ray thép $w_0 = 0.015$, hệ số bám chống trượt ray $\varphi = 0.20$).
2. **Sơ đồ Tham số (*P-Diagram Six Sigma*):**
   - Khóa cứng **4 yếu tố nhiễu tác động qua biên (`N1..N4`)**:
     - `N1`: Biến thiên khối lượng tải $7.04\text{ lần}$ ($m_{\text{tĩnh}} = 2,022\text{ kg} \leftrightarrow M_\Sigma = 14,244\text{ kg}$).
     - `N2`: Dao động con lắc cáp treo $h \le 12\text{ m}$ ($\omega_p \approx 0.904\text{ rad/s}, T_p \approx 6.95\text{ s}$).
     - `N3`: Dao động điện áp lưới 3 pha $380\text{V} \pm 10\%$ ($342\text{V} \div 418\text{V AC}$).
     - `N4`: Phát nhiệt cuộn dây chu kỳ lặp lại $S3$ ($CD = 40\%$) làm tăng điện trở rotor $R_2$.
   - Đối kháng bằng **6 yếu tố điều khiển (`CF1..CF6`)** để bảo vệ **8 chỉ tiêu chất lượng (`CTQ-01..08`)**, **5 chỉ tiêu an toàn trong phạm vi (`CTS-01..05`)** và triệt tiêu **4 trạng thái lỗi (`E1..E4` ứng với `RRM-01..04`)**.
3. **9 Yêu cầu Kỹ thuật Hệ thống (`SRS Baseline A` — Chuẩn ISO/IEC/IEEE 29148):**
   - Phân rã từ `8 mã PRD` (`PRD-FUNC-01..04`, `PRD-PERM-01..04`) + `8 mã HoQ EC` (`EC-01..08`) thành **4 mã chức năng (`SRS-FUNC-01..04`)** và **5 mã hiệu năng (`SRS-PERM-01..05`)**.
   - Chuẩn hóa toàn bộ hệ thống viện dẫn cho khách hàng giả định: bổ sung ký hiệu số `[1] .. [10]` song hành cùng mã phân loại nội bộ `[A], [B], [C]` và chèn khung chú dẫn tài liệu tham khảo ngay sau mọi bảng biểu.
4. **Ma trận Truy xuất Hai chiều (`Bidirectional RTM`) & Kế hoạch Kiểm chứng (`DVP&R Level 0`):**
   - Độ phủ truy xuất xuôi (*Forward*) đạt **100% (8/8 mã PRD)** và truy xuất ngược (*Backward DMAIC*) đạt **100% (9/9 mã SRS nối khép kín với `CTQ/CTS`, `P-Diagram`, `GAP-01..07`, `RRM-01..05`, `SOW WBS`)**.
   - Thiết lập **9 bài đo chuẩn (`DVP-L0-01..09`)** tổ chức trong **3 Kịch bản thử nghiệm tích hợp (`TS-01..03`)**, kèm quy chuẩn kỹ thuật Simulink: bước giải $T_s \le 10^{-4}\text{ s}$ và khâu lọc đạo hàm thực tế $G_d(s) = \frac{s}{T_f s + 1}$ ($T_f = 0.005 \div 0.01\text{ s}$) khi đo độ giật $\rho(t)$.
5. **Quy chuẩn Dung sai Kỹ thuật Định lượng (Standard Engineering Tolerance Specifications):**
   - Bổ sung 100% dung sai kỹ thuật định lượng theo các tiêu chuẩn chuyên ngành **TCVN 4244:2005**, **IEC 61800-2:1998**, **IEC 60034-1**, **ISO/IEC/IEEE 29148:2018** và **DIN 536** cho 20 thông số SSoT, 8 CTQ, 5 CTS, 9 câu lệnh SRS Baseline A và 9 bài đo DVP&R L0:
     - **Vận tốc di chuyển định mức:** $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ ($[0.114;\ 0.126]\text{ m/s}$ hay $[6.84;\ 7.56]\text{ m/phút}$) per IEC 61800-2 Class 2 & TCVN 4244 §1.5.5.
     - **Gia tốc ngang cực đại:** $|a(t)| \le 0.50\text{ m/s}^2$ ($+0.0\% / -10.0\%$, dải nghiệm thu $[0.45;\ 0.50]\text{ m/s}^2$).
     - **Độ giật ngang cực đại:** $|\rho(t)| \le 2.00\text{ m/s}^3$ ($+0.0\% / -10.0\%$, dải nghiệm thu $[1.80;\ 2.00]\text{ m/s}^3$).
     - **Lực cản tĩnh đầy tải & Lực kéo đỉnh:** $F_{c.\text{đầy}} = 2.12\text{ kN} \pm 0.42\text{ kN}$ ($[1.70;\ 2.54]\text{ kN}$), $F_{\max} = 9.25\text{ kN} \pm 0.45\text{ kN}$ ($[8.80;\ 9.70]\text{ kN} \le F_{\text{bám}} = 13.97\text{ kN}$ với hệ số an toàn bám $k_{\text{bám}} \ge 1.20$, danh định đạt $\approx 1.51$).
     - **Độ chính xác xác lập & Quá độ:** Sai lệch tĩnh $e_{xl} \le 5.0\%$ ($+0\%$), độ quá điều chỉnh $M_p \le 10.0\%$ ($+0\%$, $v_{\text{peak}} \le 0.132\text{ m/s}$).
     - **Mạch hãm DC-Link:** $U_{\text{dc}}(t) \le 780\text{ V DC}$ (băm Chopper tại $700\text{V} \pm 20\text{V}$, trip bảo vệ tại $800\text{V} \pm 10\text{V}$).
     - **Phối hợp phanh & Vùng chết logic:** Mở phanh tại $M_{\text{hold}}(0\text{ rpm}) \in [100\%;\ 150\%] M_{\text{đm}}$, đóng phanh tại $|v(t)| \le 0.005\text{ m/s}$, độ trôi dừng xe $\Delta s \le \pm 10\text{ mm}$ (danh định $\Delta s = 0\text{ m}$); cấm đảo chiều khi $|v(t)| > 0.002\text{ m/s}$.
     - **Chế độ nhiệt $S3$ & Điện lưới:** $CD = 40\% \pm 2.0\%$, $T_{\text{ck}} = 10\text{ phút} \pm 30\text{ s}$, $k_{dt} \in [1.20;\ 1.50]$, $\lambda_{\max} \ge 2.0$ dưới nguồn $380\text{V} \pm 10.0\% / 50\text{Hz} \pm 2.0\%$.
