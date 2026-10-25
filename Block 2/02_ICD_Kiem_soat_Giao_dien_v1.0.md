# TÀI LIỆU KIỂM SOÁT GIAO DIỆN (ICD) — HỆ TRUYỀN ĐỘNG XE CON CẦU TRỤC DẦM ĐÔI ($x = 2$)

**Mã tài liệu:** `ICD-8.5EMG-TROLLEY-v1.1` — Gói `SOW-2.1` (Khối 2) — *(tên tệp giữ hậu tố v1.0 để không gãy liên kết)*  
**Ngày:** 24/10/2026 — **Trạng thái:** **ĐÃ DUYỆT — Cổng G3 (`PDR-EVT`) đóng ngày 24/10/2026** (Người dùng duyệt kiến trúc: 1 động cơ đặt giữa dẫn 2 bánh qua trục ngang, encoder ES7C)  
**Lịch sử:** v1.0 (24/10/2026) bản đầu · v1.1 (24/10/2026) xử lý Checker K6-1 (định nghĩa $U_{dc}$), K6-2/K9 (IF-04 theo lưới 380 V), K9 (thêm `cmd_reset`, bỏ `ramp_enable`, `Ts_ctrl` → `Ts_I`, đăng ký tên biến §4.1)  
**Kế thừa:** `02_Boundary_va_P_Diagram.md` (IF-01..IF-10), `SSoT v1.2`, `SRS Baseline A v1.2`; kiến trúc `01_SAD_Kien_truc_He_thong_v1.0.md`  
**Mục đích:** Khóa **ký hiệu – đơn vị – chiều – dải giá trị** của mọi tín hiệu giữa Phần lực, Phần điều khiển và Cơ khí để Khối 3 (công thức, SDD, FSM) và Khối 4 (Simulink, `init_params.m`) dùng thống nhất (Checker `K9`, rủi ro `RRM-05`).

---

## 1. QUY ƯỚC CHUNG

1. **Hệ đơn vị SI**; góc tính bằng rad, tốc độ góc rad/s (vg/ph chỉ dùng để đối chiếu catalogue).
2. **Chiều dương:** chiều **Tiến (FWD)**. $v > 0, \omega_m > 0$ khi chạy Tiến; mô-men $M_e > 0$ theo chiều Tiến. Góc phần tư: I ($\omega>0, M>0$), II ($\omega>0, M<0$), III ($\omega<0, M<0$), IV ($\omega<0, M>0$).
3. **Hệ quy chiếu dq:** biến đổi Park **bảo toàn biên độ** (amplitude-invariant): $i_{sd}, i_{sq}$ là biên độ; $M_e = \frac{3}{2} p \frac{L_m}{L_r} \psi_{rd} i_{sq}$ (`WORKFLOW_RULES.md` §4.2-D2).
4. **Quan hệ quy đổi bắt buộc dùng chung:** $k_{qđ} = \dfrac{D_{bx}}{2\,i}$ [m/rad]; $v = k_{qđ}\,\omega_m$; $F = \dfrac{M\,\eta}{k_{qđ}}$ (động cơ kéo) hoặc $F = \dfrac{M}{k_{qđ}\,\eta}$ (năng lượng ngược từ tải về động cơ).
5. **Tên biến Simulink / `init_params.m`** (cột "Tên biến") là tên duy nhất được phép dùng ở Khối 3–5. Mọi hằng số lấy từ `Params` (Excel) — không gõ tay trong block.
6. Giá trị phụ thuộc thiết bị chưa chốt (G4) ghi `TBD@G4`; giá trị chưa có nguồn catalogue ghi `chưa xác minh`.

---

## 2. GIAO DIỆN NGOÀI (kế thừa IF-01..IF-10 của Khối 1, bổ sung thuộc tính)

| Mã IF | Từ → Đến | Loại | Tên biến | Đại lượng | Đơn vị | Dải danh định / giới hạn | Nguồn / Ràng buộc |
| :---: | :--- | :---: | :--- | :--- | :---: | :--- | :--- |
| **IF-01** | Lưới → SS-1 → SS-2 | Điện | `U_grid`, `f_grid` | Điện áp dây, tần số | V, Hz | $380 \pm 10\%$ → **[342; 418] V**; 50 Hz | P-19 [C]; ACS380 chấp nhận 380–480 V +10%/−15% [W-05] tr.10 |
| **IF-02** | Tay bấm → SS-4 | Tín hiệu số | `cmd_fwd`, `cmd_rev`, `cmd_fast`, `cmd_stop`, `cmd_reset` | Lệnh logic | bool (24 V DC) | 0/1; `cmd_fwd ∧ cmd_rev` = lỗi tay bấm → coi như STOP; `cmd_reset` xóa FAULT khi $\lvert v\rvert \le v_{rev}$ | SRS-FUNC-01/02; E-STOP/STO: Không áp dụng (QĐ-07) |
| **IF-03** | S-curve → RFOC (nội bộ SS-4) | Tín hiệu | `v_ref`, `a_ref`, `jerk_ref`, `w_ref` | $v^*, a^*, \rho^*, \omega^* = v^*/k_{qđ}$ | m/s, m/s², m/s³, rad/s | $\lvert v^* \rvert \le 0.12$; $\lvert a^* \rvert \le a_{\text{set}} \le 0.5$; $\lvert \rho^* \rvert \le \rho_{\text{set}} \le 2.0$ | SRS-FUNC-03; $a_{\text{set}}, \rho_{\text{set}}$ = `SRS-D06` (Khối 3) |
| **IF-04** | SS-2 → SS-5 (Động cơ) | Điện | `u_abc`, `i_abc` | Điện áp/dòng 3 pha PWM | V, A | $U_1 \in [0;\ U_{\text{lưới}}]$ = tối đa 342 ÷ 418 V (biến tần không tăng áp); $f_1 \in [0; \approx 52]$ Hz; $I \le I_{\max,\text{inv}}$. Động cơ định mức 400 V/50 Hz ⇒ khi lưới < 400 V, từ thông giảm nhẹ gần 50 Hz (tối thiểu ≈ 85.5% ở 342 V) | f_sw mặc định 4 kHz [W-05] tr.10; [W-01] |
| **IF-05** | DC-link → Chopper → $R_h$ | Điện | `Udc`, `I_Rh`, `chop_on` | Điện áp DC-link, dòng xả | V, A, bool | Quy ước: **không tải** $U_{dc0} = \sqrt{2}\,U_{\text{lưới}}$ = [484; 591] V (danh định 537 V); **có tải** $U_{dc} \approx 1.35\,U_{\text{lưới}}$ = [462; 564] V (danh định 513 V); Chopper ON $700 \pm 20$ V; $U_{dc} \le 780$ V; trip $800 \pm 10$ V | Downstream #3; ngưỡng thật của ACS380 `chưa xác minh` |
| **IF-06** | SS-4 (FSM) → Phanh cơ BE | Tín hiệu + điện | `brake_cmd`, `brake_open` | Lệnh nhả phanh / trạng thái | bool | 1 = cấp điện cuộn hút (nhả); 0 = phanh kẹp (fail-safe) | SRS-FUNC-02; thời gian nhả/kẹp `TBD@G4` |
| **IF-07** | Encoder ES7C → SS-4 (qua BTAC-02) | Tín hiệu | `enc_A`, `enc_B`, `w_m` | Xung A/B (+ C) → $\omega_m$ | xung, rad/s | 1024 chu kỳ/vòng (4096 sườn); $\lvert \omega_m \rvert \le 6000$ min⁻¹ cơ khí; HTL 24 V | [W-04]; [W-05] tr.24 |
| **IF-08** | Trục ĐC → Hộp số (trong geared motor) | Cơ | `Me`, `w_m` | Mô-men điện từ, tốc độ góc ĐC | N·m, rad/s | $\lvert M_e \rvert \le M_{\max}$ (`TBD@G4`); $\omega_{m,N} \approx 151$ rad/s | P-15, P-16 |
| **IF-09** | Bánh dẫn ↔ Ray | Cơ | `F_k`, `v`, `F_c` | Lực kéo tiếp tuyến, vận tốc dài, lực cản lăn | N, m/s, N | $F_c \in \{298; 2,096\}$; $\lvert F_k \rvert \le F_{\text{bám}} = 13,973$ N (đầy) / $1,984$ N (không tải) | P-12..P-14, P-20 |
| **IF-10** | Tải treo ↔ Khung xe con | Cơ | `theta`, `F_sway` | Góc lắc, phản lực ngang của cáp | rad, N | $\lvert\theta\rvert \le 0.051$ rad (2.92°); $F_{\text{lắc}} \approx (Q+m_{nh}) g \theta$ | P-06..P-08; `WORKFLOW_RULES.md` §4.2-D3 |

---

## 3. GIAO DIỆN NỘI BỘ BỔ SUNG Ở KHỐI 2 (IF-11..IF-16)

| Mã IF | Từ → Đến | Tên biến | Đại lượng | Đơn vị | Dải / Ghi chú |
| :---: | :--- | :--- | :--- | :---: | :--- |
| **IF-11** | SS-4 → SS-2 | `S_abc` | Xung kích 6 IGBT (SVPWM) | bool | f_sw = 4 kHz (`f_sw`), thời gian chết `TBD` (`Không áp dụng` trong mô hình trung bình) |
| **IF-12** | SS-2 → SS-4 | `Udc_meas` | Đo điện áp DC-link | V | [0; 900] V; chu kỳ lấy mẫu `Ts_I` = 250 µs |
| **IF-13** | SS-2 → SS-4 | `isa`, `isb` | Đo dòng 2 pha | A | $\lvert i \rvert \le I_{\max,\text{inv}}$ |
| **IF-14** | FSM → S-curve | `v_target`, `dir` | Tốc độ đích, chiều | m/s, {−1,0,+1} | $v_{\text{target}} \in \{0, \pm v_{\text{creep}}, \pm v_{\max}\}$ |
| **IF-15** | FSM ↔ RFOC | `drive_enable`, `flux_ok`, `torque_ok`, `isq_lim` | Cho phép điều chế, xác nhận từ thông/mô-men, giới hạn dòng mô-men | bool, A | `flux_ok`: $\psi_r \ge 0.95\,\psi_r^*$; `torque_ok`: $M_e$ **đo được** $\ge 0.95\,M_{\text{hold}}$ khi phanh còn kẹp (SDD §5) |
| **IF-16** | Bảo vệ → FSM | `flt_ov`, `flt_oc`, `flt_enc`, `flt_oh` | Cờ lỗi quá áp, quá dòng, mất encoder, quá nhiệt ĐC/$R_h$ | bool | Bất kỳ cờ = 1 → trạng thái FAULT, `brake_cmd = 0` |

---

## 4. BẢNG ĐẠI LƯỢNG ĐIỀU KHIỂN DÙNG CHUNG (khóa ký hiệu cho SDD & Simulink)

| Ký hiệu | Tên biến | Ý nghĩa | Đơn vị | Xuất xứ |
| :---: | :--- | :--- | :---: | :--- |
| $i_{sd}^*, i_{sq}^*$ | `isd_ref`, `isq_ref` | Lượng đặt dòng từ hóa / dòng mô-men (biên độ dq) | A | SDD §3 |
| $u_{sd}^*, u_{sq}^*$ | `usd_ref`, `usq_ref` | Điện áp đặt dq | V | Đầu ra PI dòng – MO |
| $\psi_r$ | `psi_r` | Từ thông rotor (biên độ) | Wb | Mô hình từ thông |
| $\theta_s$ | `theta_s` | Góc vector từ thông rotor | rad | $\theta_s = \int (p\,\omega_m + \omega_{sl})\,dt$ |
| $M_e, M_c$ | `Me`, `Mc` | Mô-men điện từ / cản quy đổi | N·m | §1 quy ước 4 |
| $J_\Sigma$ | `J_sum` | Quán tính tổng quy về trục ĐC | kg·m² | $J_{\text{ĐC+phanh}} + \delta M k_{qđ}^2$ |
| $k_{qđ}$ | `k_qd` | Hệ số quy đổi tịnh tiến – quay | m/rad | $D_{bx}/(2i)$ |
| $T_f$ | `Tf_jerk` | Hằng số thời gian khâu lọc đạo hàm $G_d(s) = \frac{s}{T_f s+1}$ | s | [0.005; 0.01] (SRS chi tiết §5.4) |
| $T_s$ | `Ts_sim` | Bước giải Simulink | s | $\le 10^{-4}$ |

### 4.1. Đăng ký tên biến tham số (bổ sung v1.1 — dùng cho `init_params.m`)

| Nhóm | Tên biến | Ý nghĩa (đơn vị) |
| :--- | :--- | :--- |
| Cơ | `M_full`, `M_empty`, `D_bx`, `w0`, `phi`, `eta`, `g`, `h`, `k_qd`, `i_gear`, `delta` | Khối lượng (kg), đường kính (m), hệ số (-), g (m/s²), dài cáp (m), quy đổi (m/rad), tỷ số truyền thực (-), hệ số quán tính (-) |
| Động cơ | `Rs`, `Rr`, `Lls`, `Llr`, `Lm`, `pp`, `J_Bmot` | Ω, Ω, H, H, H, số đôi cực, kg·m² (rotor **kèm phanh**) |
| Biến tần | `f_sw`, `Udc_chop_on`, `Udc_max`, `Udc_trip`, `Rh` | Hz, V, V, V, Ω |
| S-curve | `a_set`, `rho_set`, `v_max`, `v_creep` | Giới hạn đặt: m/s², m/s³; m/s |
| PI | `Kp_i`, `Ti_i`, `Kp_w`, `Ti_w`, `T_pre`, `isq_lim` | V/A, s, A·s/rad, s, s, A |
| FSM | `v_stop`, `v_rev`, `M_hold`, `t_test`, `t_mag`, `t_open`, `t_close`, `M_B` | m/s, m/s, N·m, s, s, s, s, N·m |
| Đo / mô phỏng | `Ts_sim`, `Ts_I`, `Ts_w`, `Tf_jerk`, `N_enc` | s, s, s, s, xung/vòng |

---

## 5. MA TRẬN GIAO DIỆN N² (rút gọn)

| | SS-1 | SS-2 | SS-3 | SS-4 | SS-5 | SS-6 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **SS-1** | — | IF-01 (điện) | | — | | |
| **SS-2** | | — | IF-05 | IF-12, IF-13 | IF-04 | |
| **SS-3** | | | — | `flt_oh` (IF-16) | | |
| **SS-4** | `KM1` cmd | IF-11 | | — | IF-06 | |
| **SS-5** | | | | IF-07 | — | IF-08 |
| **SS-6** | | | | | (phản lực) | — ; IF-09 ray, IF-10 tải |

---

## 6. KIỂM SOÁT THAY ĐỔI GIAO DIỆN

- Mọi thay đổi ký hiệu/đơn vị/dải trong bảng trên phải nâng phiên bản ICD (`v1.0 → v1.1`) và cập nhật đồng bộ: Excel `Params`/`Dẫn xuất`, SDD, `init_params.m`, RTM/DVP (`WORKFLOW_RULES.md` §10).
- Các mục `TBD@G4` sẽ được điền tại Khối 3 sau khi Người dùng chốt thiết bị ở cổng G4.
