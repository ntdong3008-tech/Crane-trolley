# PHÂN TÍCH DẠNG LỖI THIẾT KẾ CẤP HỆ THỐNG (DFMEA L1) — XE CON CẦU TRỤC ($x = 2$)

**Mã tài liệu:** `DFMEA-L1-8.5EMG-TROLLEY-v1.1` — Gói `SOW-2.3` (Khối 2) — Chủ trì: Nghiêm Trọng Đông & Phạm Văn Hưng *(tên tệp giữ hậu tố v1.0 để không gãy liên kết)*  
**Ngày:** 28/10/2026 — **Trạng thái:** **ĐÃ DUYỆT — Cổng G3 (`PDR-EVT`) đóng ngày 24/10/2026**; v1.1 do Người dùng duyệt ngày 28/10/2026  
**Lịch sử:** v1.0 (24/10/2026) bản đầu, có cập nhật QĐ-07 · **v1.1 (28/10/2026)** trình bày lại theo phạm vi môn học (CR-08..CR-18): FM-01 đổi từ "lắc tải" sang "xung giật cơ cấu" (CR-10); FM-02 sửa cửa sổ $R_h$ theo biến tần đã chốt; FM-05 bỏ cờ `flt_oh` (QĐ-07); FM-09 chỉnh SO theo quán tính chốt ở Khối 3; FM-07, FM-12 tách sang §3  
**Đầu vào:** `RRM-01..05` (HOQ §8.4), `E-01..E-04` & `N-01..N-04` (P-Diagram Khối 1), rủi ro kiến trúc `RA-01..02` (SAD §7)  
**Tiêu chí cổng (SOW-2.3):** mọi dạng lỗi có `AP = Cao (H)` phải được hạ xuống `Trung bình (M)` hoặc `Thấp (L)` bằng biện pháp thiết kế trước PDR-EVT.

---

## 1. THANG ĐÁNH GIÁ VÀ QUY TẮC AP

- **S (Severity), O (Occurrence), D (Detection):** thang 1–10 (10 = nghiêm trọng nhất / hay xảy ra nhất / khó phát hiện nhất). D đánh giá theo khả năng phát hiện **trong quá trình thiết kế** bằng 3 phương pháp: A (giải tích/Excel), S (Simulink), I (catalogue).
- **Quy tắc AP rút gọn của nhóm:**
  - **H** nếu ($S \ge 7$ và $O \ge 5$) hoặc ($S \ge 9$ và $O \ge 3$);
  - **M** nếu ($S \ge 7$ và $O \ge 3$) hoặc ($S \ge 5$ và $O \ge 4$);
  - **L** cho các trường hợp còn lại.
- **RPN = S × O × D** ghi kèm để tham khảo.
- **Phạm vi (QĐ-07):** chỉ xét điều kiện vận hành lý tưởng — không mất điện, không dừng khẩn, không xét sự cố thiết bị.

---

## 2. BẢNG DFMEA L1 (10 dạng lỗi trong phạm vi)

| ID | Chức năng / SRS | Dạng lỗi tiềm ẩn | Hậu quả | S | Nguyên nhân (RRM/E) | O₀ | Kiểm soát phát hiện | D₀ | AP₀ / RPN₀ | Biện pháp thiết kế (phòng ngừa) | O₁ | D₁ | AP₁ / RPN₁ | Mã dẫn xuất / DV |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| **FM-01** | Làm trơn chuyển động — SRS-FUNC-03, SRS-PERM-03 | Xung giật cơ cấu khi khởi hành/dừng ($\rho \to \infty$) | Sốc hộp số, trượt bánh dẫn, kích thích lắc tải | 7 | Lượng đặt bậc thang hoặc dốc tuyến tính (`RRM-01`, `E-02`) | 6 | S: đo $a(t)$, $\rho(t)$ | 6 | **H** / 252 | S-curve 7 đoạn $a^* = 0.45$, $\rho^* = 1.8$ (dự trữ 10% dưới giới hạn đề bài); góc lắc $\theta(t)$ quan sát, không nghiệm thu (CR-10) | 2 | 3 | **L** / 42 | `SRS-D06` / DV-03, DV-07 |
| **FM-02** | Hãm tái sinh — SRS-FUNC-04 | Quá áp DC-link, biến tần ngắt khi giảm tốc đầy tải | Mất mô-men giữa chừng | 7 | Không có đường xả năng lượng (`RRM-02`, `E-03`) | 7 | A: $P_{\text{hãm}}$; S: $U_{dc}(t)$ | 5 | **H** / 245 | Chopper tích hợp ACS380 + $R_h$ = 210 Ω ∈ [99; 428] Ω; $P_{BR,\max}$ = 1.13 kW ≫ $P_{\text{hãm}}$ ≈ 0.44 kW | 2 | 3 | **L** / 42 | `SRS-D05` / DV-04 |
| **FM-03** | Mở phanh an toàn — SRS-FUNC-02 | Trôi/giật xe khi mở phanh ở 0 rpm | Va chạm, xung lực lên cơ cấu | 8 | Chưa đủ từ thông/mô-men khi nhả phanh (`RRM-03`) | 5 | S: $v(t)$ quanh lúc mở phanh | 6 | **H** / 240 | RFOC + encoder 1024 chu kỳ/vòng; FSM: từ hóa → `flux_ok` → thử mô-men giữ khi phanh còn kẹp (`torque_ok`) → nhả phanh | 2 | 3 | **L** / 48 | `SRS-D10` / DV-02 |
| **FM-04** | Khóa chéo đảo chiều — SRS-FUNC-02 | Đảo chiều khi $v \ne 0$ | Xoắn trục, sốc mô-men | 8 | Logic thiếu khóa chéo (`RRM-03`) | 5 | S: kịch bản `TS-02` | 4 | **H** / 160 | FSM chỉ chốt chiều mới khi $\lvert v \rvert \le 0.002$ m/s (phân giải encoder 1.23 mm/s) | 2 | 3 | **L** / 48 | `SRS-D11` / DV-02 |
| **FM-05** | Định cỡ nhiệt — SRS-PERM-04 | Quá nhiệt cuộn dây hoặc chọn sai công suất | Hỏng cách điện / lãng phí | 6 | Sao chép công suất Case Study (`RRM-04`, `E-04`) | 5 | A: $M_{đt}$, $k_{dt}$ | 4 | **M** / 120 | Tính $M_{đt}$ theo chu trình S3-40% ở lưới danh định; $k_{dt} \ge 1.20$ (A.1, CR-13) | 2 | 3 | **L** / 36 | `SRS-D04` / DV-08 |
| **FM-06** | Kéo không trượt — SRS-PERM-01 | Trượt quay bánh dẫn khi tăng tốc | Mất kiểm soát vận tốc, mòn ray | 6 | $F_k > F_{\text{bám}}$ (`E-02`) | 4 | A: $k_{\text{bám}}$ | 4 | **M** / 96 | $k_{\text{bám}} = 1.516$; giới hạn $\lvert i_{sq} \rvert$ tương ứng $F_k \le F_{\text{bám}}/1.2$ | 2 | 3 | **L** / 36 | `SRS-D01` / DV-05 |
| **FM-08** | Vận tốc định mức — SRS-PERM-02 | $v_{xl}$ ngoài [0.114; 0.126] m/s | Lệch nghiệm thu | 5 | Dùng $i = 150$ (`P-16 [C]`) thay $i_{\text{thực}}$ trong quy đổi; trượt ĐC (`E-01`) | 6 | S: $v(t)$ | 4 | **M** / 120 | Quy đổi bằng $i_{\text{thực}}$ = 155.34 (`SRS-D03`); vòng kín tốc độ có khâu I | 2 | 3 | **L** / 30 | `SRS-D03`, `SRS-D08` / DV-06 |
| **FM-09** | Chất lượng điều khiển — Downstream #1 | Quá điều chỉnh $M_p > 10\%$, dao động | Vượt tốc | 5 | Hệ số vòng tốc độ chọn không theo quán tính thực mà vòng điều khiển nhìn thấy (`RA-02`, `N-01`) | 5 | S: $v(t)$ hai trạng thái tải | 5 | **M** / 125 | Chỉnh SO theo quán tính chốt ở Khối 3 (SDD §4.3), kể trễ đo tốc độ; lượng đặt đi qua S-curve; kiểm PM ở $J_\Sigma$ và $J_{\Sigma,0}$ | 3 | 4 | **L** / 60 | `SRS-D07` / DV-06 |
| **FM-10** | Tích hợp mô hình — toàn hệ | Lệch đơn vị/ký hiệu, gai đạo hàm $\rho(t)$ | Kết luận kiểm chứng sai | 5 | Không khóa ICD, $T_s$ thô (`RRM-05`) | 6 | Checker K9 | 5 | **M** / 150 | ICD khóa tên biến; $T_s \le 10^{-4}$ s; $G_d(s) = \frac{s}{T_f s + 1}$, $T_f \in [5; 10]$ ms | 2 | 3 | **L** / 30 | — / DV-07 |
| **FM-11** | Cấp dòng — SRS-PERM-01 | Biến tần quá dòng khi tăng tốc đầy tải | Ngắt, mất mô-men | 6 | Chọn biến tần theo $P_N$ thay vì dòng đỉnh | 4 | A: $I_{\text{đỉnh}}$ | 4 | **M** / 96 | Chọn theo $1.5\,I_{Hd} \ge I_{\text{đỉnh}}$ ([W-05] tr.12) | 2 | 3 | **L** / 36 | `SRS-D04` / DV-08 |

---

## 3. DẠNG LỖI NGOÀI PHẠM VI (QĐ-07)

| ID | Dạng lỗi | Lý do không áp dụng |
| :---: | :--- | :--- |
| **FM-07** | Trượt bánh khi phanh cơ kẹp lúc xe không tải đang chạy (dừng khẩn) | Dừng khẩn, mất điện ngoài phạm vi; vận hành bình thường phanh chỉ kẹp khi $\lvert v \rvert \le 0.005$ m/s. Cửa sổ $M_B$ = 7 N·m ∈ [5.94; 10.12] N·m vẫn kiểm ở KT-27, KT-28 |
| **FM-12** | Phanh không nhả (hỏng cuộn hút/chỉnh lưu phanh) | Sự cố thiết bị ngoài phạm vi |

---

## 4. TỔNG HỢP KẾT QUẢ (10 dạng lỗi trong phạm vi)

| Mức AP | Trước biện pháp (AP₀) | Sau biện pháp (AP₁) |
| :---: | :---: | :---: |
| **H** | 4 (FM-01, 02, 03, 04) | **0** |
| **M** | 6 | 0 |
| **L** | 0 | 10 |

**Tiêu chí SOW-2.3 đạt ở mức thiết kế:** không còn dạng lỗi AP = H. Hiệu lực các biện pháp được kiểm chứng ở Khối 5 (cột DV); trước khi chạy mô phỏng, mọi O₁/D₁ là giá trị dự kiến (`Report: chưa chạy`).

## 5. CHUYỂN TIẾP SANG KHỐI 3

- DFMEA được cập nhật xuống cấp phân hệ trong `Block 3/04_SRS_A1_Dan_xuat_RTM_DVP_WCCA_v1.0.md` (`SOW-3.5`).
- Mã `SRS-D01..D15` được định danh và gắn yêu cầu cha tại Khối 3.
