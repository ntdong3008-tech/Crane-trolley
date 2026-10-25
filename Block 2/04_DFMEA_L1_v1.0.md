# PHÂN TÍCH DẠNG LỖI THIẾT KẾ CẤP HỆ THỐNG (DFMEA L1) — XE CON CẦU TRỤC ($x = 2$)

**Mã tài liệu:** `DFMEA-L1-8.5EMG-TROLLEY-v1.0` — Gói `SOW-2.3` (Khối 2) — Chủ trì: Nghiêm Trọng Đông & Phạm Văn Hưng  
**Ngày:** 24/10/2026 — **Trạng thái:** **ĐÃ DUYỆT — Cổng G3 (`PDR-EVT`) đóng ngày 24/10/2026** (Người dùng duyệt kiến trúc: 1 động cơ đặt giữa dẫn 2 bánh qua trục ngang, encoder ES7C)  
**Đầu vào:** `RRM-01..05` (HOQ v1.1 §8.4), `E-01..E-04` & `N-01..N-04` (P-Diagram Khối 1), rủi ro kiến trúc `RA-01..02` (SAD §7)  
**Tiêu chí cổng (SOW-2.3):** mọi dạng lỗi có `AP = Cao (H)` phải được hạ xuống `Trung bình (M)` hoặc `Thấp (L)` bằng biện pháp thiết kế trước PDR-EVT.

---

## 1. THANG ĐÁNH GIÁ VÀ QUY TẮC AP

- **S (Severity), O (Occurrence), D (Detection):** thang 1–10 (10 = nghiêm trọng nhất / hay xảy ra nhất / khó phát hiện nhất). D đánh giá theo khả năng phát hiện **trong quá trình thiết kế** bằng 3 phương pháp được phép: A (giải tích/Excel), S (Simulink), I (catalogue).
- **Quy tắc AP rút gọn do nhóm áp dụng** (tham khảo cách tiếp cận Action Priority của AIAG–VDA FMEA 2019 — *tài liệu gốc chưa có trong kho, chưa xác minh*):
  - **H** nếu ($S \ge 7$ và $O \ge 5$) hoặc ($S \ge 9$ và $O \ge 3$);
  - **M** nếu ($S \ge 7$ và $O \ge 3$) hoặc ($S \ge 5$ và $O \ge 4$);
  - **L** cho các trường hợp còn lại.
- **RPN = S × O × D** ghi kèm để tham khảo (Slide MCR đã cam kết định lượng RPN ở Khối 2).

---

## 2. BẢNG DFMEA L1

| ID | Chức năng / SRS | Dạng lỗi tiềm ẩn | Hậu quả | S | Nguyên nhân (RRM/E) | O₀ | Kiểm soát phát hiện | D₀ | AP₀ / RPN₀ | Biện pháp thiết kế (phòng ngừa) | O₁ | D₁ | AP₁ / RPN₁ | Mã dẫn xuất / DV |
| :---: | :--- | :--- | :--- | :---: | :--- | :---: | :--- | :---: | :---: | :--- | :---: | :---: | :---: | :--- |
| **FM-01** | Làm trơn chuyển động — SRS-FUNC-03, SRS-PERM-03 | Lắc tải biên độ lớn khi khởi hành/dừng | Va đập, mất an toàn tải 12,222 kg, sốc hộp số | 7 | Lượng đặt dốc tuyến tính, $\rho \to \infty$ (`RRM-01`, `E-02`) | 6 | S: đo $\theta(t)$ | 6 | **H** / 252 | S-curve 7 đoạn $a^* = 0.45$, $\rho^* = 1.8$ (dự trữ 10% so với giới hạn); góc lắc dư ước lượng $\theta_{\text{dư}} \approx v\omega_p/g = 0.63°$ | 2 | 3 | **L** / 42 | `SRS-D06` / DV-03, DV-07 |
| **FM-02** | Hãm tái sinh — SRS-FUNC-04 | Quá áp DC-link, biến tần trip khi giảm tốc đầy tải | Mất mô-men giữa chừng, phanh cơ kẹp ở tốc độ cao | 7 | Không có đường xả năng lượng (`RRM-02`, `E-03`) | 7 | A: $P_{\text{hãm}}$; S: $U_{dc}(t)$ | 5 | **H** / 245 | Chopper tích hợp ACS380 + $R_h \in [99; 285]\ \Omega$; $P_{BR,\max}$ biến tần (1.13 ÷ 1.65 kW) ≫ $P_{\text{hãm}} \approx 0.45$ kW | 2 | 3 | **L** / 42 | `SRS-D05` / DV-04 |
| **FM-03** | Mở phanh an toàn — SRS-FUNC-02 | Trôi/giật xe khi mở phanh ở 0 rpm | Va chạm, lắc tải | 8 | Chưa đủ từ thông/mô-men khi nhả phanh; ước lượng tốc độ sai ở tần số thấp (`RRM-03`) | 5 | S: $v(t)$ quanh lúc mở phanh | 6 | **H** / 240 | RFOC + encoder 1024 xung; FSM: từ hóa → xác nhận `flux_ok`, `torque_ok` → mới nhả phanh | 2 | 3 | **L** / 48 | `SRS-D10` / DV-02 |
| **FM-04** | Khóa chéo đảo chiều — SRS-FUNC-02 | Đảo chiều khi $v \ne 0$ | Xoắn trục, sốc mô-men, vi phạm TCVN 4244 §1.5.7.2.9 (theo Baseline) | 8 | Logic thiếu khóa chéo (`RRM-03`) | 5 | S: kịch bản DV-02 | 4 | **H** / 160 | FSM chỉ cho phép đổi chiều khi $\lvert v \rvert \le 0.002$ m/s (phân giải encoder 1.22 mm/s) | 2 | 3 | **L** / 48 | `SRS-D11` / DV-02 |
| **FM-05** | Định cỡ nhiệt — SRS-PERM-04 | Quá nhiệt cuộn dây hoặc chọn sai công suất | Cháy ĐC / lãng phí | 6 | Sao chép công suất Case Study (`RRM-04`, `E-04`) | 5 | A: $M_{đt}$, $k_{dt}$ | 4 | **M** / 120 | Tính $M_{đt}$ theo chu trình S3-40%; $k_{dt} \ge 1.20$ (A.1); tiếp điểm nhiệt TF của ĐC → `flt_oh` | 2 | 3 | **L** / 36 | `SRS-D04` / DV-08 |
| **FM-06** | Kéo không trượt — SRS-PERM-01 | Trượt quay bánh dẫn khi tăng tốc | Mất kiểm soát vận tốc, mòn ray | 6 | $F_k > F_{\text{bám}}$ (`E-02`) | 4 | A: $k_{\text{bám}}$ | 4 | **M** / 96 | $k_{\text{bám}} = 1.516$; giới hạn $\lvert i_{sq} \rvert$ tương ứng $F_k \le F_{\text{bám}}/1.2$ | 2 | 3 | **L** / 36 | `SRS-D01` / DV-05 |
| **FM-07** | **Không áp dụng (QĐ-07)** — Dừng khẩn — SRS-FUNC-02 | Trượt bánh khi phanh cơ kẹp ở tốc độ, xe không tải | Quãng dừng dài, mòn bánh | 6 | $F_{\text{bám,0}} = 1,984$ N nhỏ; phanh giữ đầy tải quá mạnh với xe rỗng (`RA-01`) | 4 | A: $a_{\text{phanh}}$ | 5 | **M** / 120 | Dừng thường bằng điện; dừng khẩn SS1 (giảm tốc điện → STO); chọn $M_B$ trong cửa sổ [$k_p M_c$; giới hạn bám đầy tải] | 3 | 4 | **L** / 72 | `SRS-D13` / DV-02 |
| **FM-08** | Vận tốc định mức — SRS-PERM-02 | $v_{xl}$ ngoài [0.114; 0.126] m/s | Sai năng suất, lệch nghiệm thu | 5 | Dùng $i = 150$ (`P-16 [C]`) thay $i_{\text{thực}}$ trong quy đổi; trượt ĐC (`E-01`) | 6 | S: $v(t)$ | 4 | **M** / 120 | Quy đổi bằng $i_{\text{thực}}$ của hộp số (`SRS-D03`); vòng kín tốc độ có khâu I | 2 | 3 | **L** / 30 | `SRS-D03`, `SRS-D08` / DV-06 |
| **FM-09** | Chất lượng điều khiển — Downstream #1 | Quá điều chỉnh $M_p > 10\%$, dao động khi $J_\Sigma$ đổi 3.2 lần | Vượt tốc, lắc tải | 5 | SO chỉnh cho một giá trị $J$ (`RA-02`, `N-01`) | 5 | S: $v(t)$ hai trạng thái tải | 5 | **M** / 125 | Chỉnh SO ở $J_{\max}$; lượng đặt đi qua S-curve; kiểm tra PM ở $J_{\min}$ (SDD) | 3 | 4 | **L** / 60 | `SRS-D07` / DV-06 |
| **FM-10** | Tích hợp mô hình — toàn hệ | Lệch đơn vị/ký hiệu, gai đạo hàm $\rho(t)$ | Kết luận kiểm chứng sai | 5 | Không khóa ICD, $T_s$ thô (`RRM-05`) | 6 | Checker K9 | 5 | **M** / 150 | ICD v1.0 khóa tên biến; $T_s \le 10^{-4}$ s; $G_d(s) = \frac{s}{T_f s + 1}$, $T_f \in [5; 10]$ ms | 2 | 3 | **L** / 30 | — / DV-07 |
| **FM-11** | Cấp dòng — SRS-PERM-01 | Biến tần quá dòng khi tăng tốc đầy tải ở −10% áp lưới | Trip, mất mô-men | 6 | Chọn biến tần theo $P_N$ thay vì dòng đỉnh | 4 | A: $I_{\text{đỉnh}}$ | 4 | **M** / 96 | Chọn theo $1.5\,I_{Hd} \ge I_{\text{đỉnh}}$ (định nghĩa $I_{Hd}$ [W-05] tr.12) | 2 | 3 | **L** / 36 | `SRS-D04` / DV-08 |
| **FM-12** | **Không áp dụng (QĐ-07)** — Phanh cơ — SRS-FUNC-02 | Phanh không nhả (cuộn hút/chỉnh lưu hỏng) | ĐC kéo chống phanh → quá dòng, quá nhiệt | 6 | Hỏng cuộn hút | 4 | — | 5 | **M** / 120 | Giám sát dòng mô-men khi $v \approx 0$ sau lệnh nhả > $t_{\text{nhả}}$ → FAULT | 3 | 3 | **L** / 54 | `SRS-D10` / DV-02 |

---

## 3. TỔNG HỢP KẾT QUẢ

| Mức AP | Trước biện pháp (AP₀) | Sau biện pháp (AP₁) |
| :---: | :---: | :---: |
| **H** | 4 (FM-01, 02, 03, 04) | **0** |
| **M** | 8 | 0 |
| **L** | 0 | 12 |

> **Cập nhật theo QĐ-07 (24/10/2026):** FM-07 (dừng khẩn/mất điện) và FM-12 (phanh hỏng không nhả) thuộc tình huống sự cố, ngoài phạm vi điều kiện vận hành lý tưởng → `Không áp dụng`; giữ lại trong bảng để tham khảo. Các dạng lỗi còn hiệu lực: 10.

→ **Tiêu chí SOW-2.3 đạt ở mức thiết kế**: không còn dạng lỗi AP = H. Hiệu lực các biện pháp phải được **kiểm chứng ở Khối 5** (cột DV); trước khi chạy, mọi O₁/D₁ là *dự kiến* (`Report: chưa chạy`).

## 4. CHUYỂN TIẾP SANG KHỐI 3

- DFMEA được cập nhật xuống cấp phân hệ trong `Block 3/04_SRS_A1_Dan_xuat_RTM_DVP_WCCA_v1.0.md` (`SOW-3.5`).
- Mã `SRS-D01..D13` được định danh và gắn yêu cầu cha tại Khối 3.
