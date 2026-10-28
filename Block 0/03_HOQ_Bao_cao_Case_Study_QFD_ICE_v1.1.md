# BÁO CÁO KHẢO SÁT CASE STUDY, PHÂN TÍCH TECH GAP, MA TRẬN QFD/HoQ VÀ LỰA CHỌN PHƯƠNG ÁN TRUYỀN ĐỘNG THEO ICE (KHỐI 0 — PRE-A)

**Tên đề tài:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Di Chuyển Ngang Xe Con Cầu Trục ($x = 2$)

**Mã tài liệu:** `BCA-QFD-8.5EMG-TROLLEY-v1.2` *(tên tệp giữ hậu tố v1.1 để không gãy liên kết)* | **Hạng mục công việc:** `SOW-0.2 (Khối 0 — Đệ trình Cổng MCR)`

**Tài liệu đầu vào tham chiếu:** `PRD-8.5EMG-TROLLEY-v3.1 (Baseline Frozen)` & `SOW-8.5EMG-TROLLEY-v1.1 (Baseline Frozen)`

**Nhóm thực hiện:** Nhóm 8.5-EMG (Đề $x = 2$ — STT 22: Nghiêm Trọng Đông)

**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh

**Trạng thái phạm vi (28/10/2026):** tài liệu giữ nguyên làm hồ sơ Cổng MCR. Phạm vi nghiệm thu hiện hành theo PRD v3.3, SOW v1.4 và SRS Baseline A v1.4 (CR-08..CR-15): không gán dung sai cho số liệu đầu vào; gia tốc và độ giật chỉ giữ cận trên; góc lắc chỉ quan sát, không nghiệm thu; $k_{dt}$ tính ở lưới danh định.

---

### BẢNG LỊCH SỬ PHIÊN BẢN (DOCUMENT REVISION HISTORY)

| Phiên bản | Ngày ban hành | Người thực hiện | Tóm tắt các nội dung thay đổi chính | Trạng thái |
| :---: | :---: | :--- | :--- | :---: |
| **`v1.0`** | 14/10/2026 | Nhóm 8.5-EMG | Khởi tạo báo cáo khảo sát Case Study, Tech Gap, ma trận QFD/HoQ và lựa chọn phương án theo ICE tại Khối 0. | Khóa sơ bộ |
| **`v1.1`** | 22/10/2026 | Ban Kỹ thuật Hệ thống 8.5-EMG | **Đồng bộ toàn diện theo tài liệu PRD v3.1 và SOW v1.1 sau kiểm toán kỹ thuật:**<br>• Cập nhật tài liệu đầu vào tham chiếu thành `PRD v3.1` và `SOW v1.1`.<br>• Xóa sạch 100% các liên kết tìm kiếm ngoài mạng không chính thống; thay bằng mã viện dẫn tài liệu nội bộ chuẩn `[Rx, §mục, tr.số (PDF tr.số)]`.<br>• **Khắc phục lỗi cản chuyển động vật lý:** Cập nhật suất cản lăn riêng $w_0 = 0.015$ (1.5%) [R1, §2.4.7.2.2] (trị số $w_0 = 0.015$ là giả định `[C]`) và hệ số bám dính ray $\varphi = 0.20$ [R5, Bài 4, tr.43]. Cập nhật lực cản tĩnh $F_c = 2.12\text{ kN}$, công suất tĩnh $P_{\text{tĩnh}} = 0.27\text{ kW}$, lực kéo cực đại $F_{\max} = 9.25\text{ kN}$, công suất đỉnh khi tăng tốc $P_{\max} = 1.16\text{ kW}$.<br>• **Đồng bộ nhãn phân loại nguồn gốc `[A] / [B] / [C]`** cho 8 yêu cầu WHATs và các đặc tính HOWs.<br>• **Cập nhật trạng thái xác minh các hồ sơ hãng sản xuất:** Demag Cranes EZDR [R9-07] là `ĐÃ XÁC MINH`, Sungdo và Yuantai là `(Tham khảo, chưa xác minh bản gốc)`.<br>• Đồng bộ hóa kiến trúc phân lớp PDS (IEC 61800-2 & [R5, Bài 4, tr.4–10]) và cấu trúc FOC vòng kín. | **Cũ** |
| **`v1.2`** | 26/10/2026 | Nhóm A duyệt | **Hiệu đính số liệu theo SSoT v1.2 và SRS Baseline A.1:**<br>• §2: $F_c$ 2.12 kN → **2,096 N** (sửa cả $w_0$ ghi nhầm 0.0152 → 0.015), $\eta$ 0.96 → **0.90**, $P_{\text{tĩnh}}$ → 0.28 kW, $F_{\max}$ → 9.22 kN, $P_{\max}$ → 1.23 kW; sơ đồ khối: $\eta$ = 0.90, $w_0$ = 0.015 thay $\mu$ = 0.2.<br>• $k_{dt} \in [1.2;\ 1.5]$ → $k_{dt} \ge 1.20$ (CR-01); `QCD-C01` hiểu là $P_{đm} \le 1.5\,P_{\max}$ ≈ 1.84 kW (QĐ-08).<br>• `GAP-01`, Solution C: thay dải ước lượng 1.5 ÷ 3.7 kW bằng kết quả Khối 3 (0.75 kW, QĐ-04).<br>• Thêm bảng đối chiếu mã viện dẫn `[R9-xx]` với `WORKFLOW_RULES.md` §4.1 (sau bảng lịch sử). | **Chính thức (Baseline Frozen)** |

> **Mã viện dẫn (cập nhật 28/10/2026):** tài liệu này dùng bộ mã thống nhất `[R1..R10]`, `[R9-01..R9-14]` của `Tài liệu tham khảo/00_Danh_muc_tai_lieu_tham_khao.md` (đã đổi từ danh mục `[R9-xx]` riêng của Khối 0 — bảng đổi mã ở mục 3 của danh mục).

---

## 1. LUỒNG PHƯƠNG PHÁP LUẬN TÍCH HỢP CHUẨN DMAIC & NASA SE TẠI KHỐI 0 (`SOW-0.2`)

Để tránh việc đề xuất các phương án truyền động một cách cảm tính hoặc nhảy cóc từ phân tích tài liệu sang chốt giải pháp, quy trình nghiên cứu tiền khả thi tại **Khối 0 (`Pre-A` — `SOW-0.2`)** của Nhóm 8.5-EMG được thiết lập chặt chẽ qua **6 bước nối tiếp nhau tích hợp trực tiếp chu trình 5 pha `DMAIC` (*Define – Measure – Analyze – Improve/Kaizen – Control*)** theo chuẩn NASA Systems Engineering Handbook (§4.3 & §6.8) [R2]:

| Bước SE & Pha DMAIC | Tên Bước Thực hiện trong Quy trình SE & DMAIC | Đầu vào (Inputs) | Hoạt động Phân tích & Biến đổi (Process) | Đầu ra (Outputs) — Cầu nối sang Bước tiếp theo | 
| ----- | ----- | ----- | ----- | ----- | 
| **Bước 1**<br>*(Pha D — Define & Pha M — Measure)* | **Khóa Bài toán, Ranh giới Biên & Lượng hóa Chỉ tiêu Đầu vào (*Problem Definition & CTQ Measurement*)** | `PRD v3.1 (Baseline Frozen)` & `SOW v1.1 (Baseline Frozen)` | Tổng hợp 8 yêu cầu khách hàng trong phạm vi SOW (`PRD-FUNC-01..04`, `PRD-PERM-01..04`) và bộ thông số biên của đề $x = 2$. | Bộ tiêu chí đầu bài **WHATs** (Tiếng nói khách hàng — *Voice of Customer*) và điều kiện biên vật lý. | 
| **Bước 2**<br>*(Pha A — Analyze: Cơ sở)* | **Khảo sát Case Studies Học thuật & Công nghiệp (*Benchmarking*)** | 6 bài báo khoa học/đồ án quốc tế & 3 Catalogue hãng cầu trục | Phân tích mô hình toán, công thức tính chọn phần lực, cấu trúc biến tần – động cơ và thuật toán điều khiển trong từng nghiên cứu. | Tập hợp các **Mảnh ghép Công nghệ (*Technology Building Blocks*)** đã được kiểm chứng trên thế giới. | 
| **Bước 3**<br>*(Pha A — Analyze: Trọng tâm)* | **Phân tích Khoảng trống Công nghệ (*Tech Gap Analysis*)** | Kết quả Bước 1 + Bước 2 | Đối chiếu trực tiếp từng Case Study với yêu cầu của đề bài $x = 2$ ($M_\Sigma = 14,244\text{ kg}, v_{\max} = 0.12\text{ m/s}, h = 12\text{ m}$) để tìm ra điểm chưa đáp ứng hoặc dư thừa. | Danh mục **7 Khoảng trống Công nghệ (`GAP-01`** $\to$ **`GAP-07`)** mà thiết kế của nhóm bắt buộc phải lấp đầy. | 
| **Bước 4**<br>*(Pha I — Improve / Kaizen: Bước 1)* | **Triển khai QFD & Xây dựng Ngôi nhà Chất lượng (*House of Quality — HoQ*)** | 8 mã `PRD` (WHATs) + 7 mã `Tech Gap` | Dịch các yêu cầu khách hàng (`WHATs`) sang **8 Đặc tính Kỹ thuật Hệ thống (`HOWs` / `EC-01..08`)**, đánh giá tương quan và tính trọng số ưu tiên kỹ thuật. | **Trọng số tầm quan trọng kỹ thuật ($w_j$ tính theo %)** của từng thông số và ma trận mâu thuẫn kỹ thuật trên mái nhà HoQ. | 
| **Bước 5**<br>*(Pha I — Improve / Kaizen: Bước 2)* | **Tổ hợp Hình thái các Phương án Ứng viên (*Morphological & Kaizen Synthesis*)** | 8 Đặc tính Kỹ thuật `EC-01..08` + Các mảnh ghép công nghệ từ Case Studies | Lập bảng hình thái học (*Morphological Box*) kết hợp các lựa chọn của Động cơ + Bộ biến đổi + Phản hồi + Quỹ đạo thành các cấu hình hoàn chỉnh. | **4 Phương án Cấu hình Hệ truyền động (`Solution A`, `Solution B`, `Solution C`, `Solution D`)** phân hóa rõ theo cấp độ công nghệ. | 
| **Bước 6**<br>*(Pha I — Improve & Pha C — Control)* | **Đánh giá Đa tiêu chí bằng Ma trận ICE, Chốt Sơ đồ Chuẩn & Thiết lập Cơ chế Kiểm soát (Control)** | 4 Phương án (`Solution A..D`) + Trọng số từ HoQ + Ràng buộc SOW | Chấm điểm **Impact** (từ trọng số HoQ), **Confidence** (từ bằng chứng Case Study/TRL) và **Ease** (từ khả năng thực thi/mô phỏng Simulink). | Chốt **Phương án tối ưu (`Solution C`)** và xác lập **Sơ đồ Cấu trúc Hệ truyền động Tiêu chuẩn** theo IEC 61800-2. | 

## 2. TÓM LƯỢC YÊU CẦU & RÀNG BUỘC ĐẦU VÀO TỪ PRD & SOW (BƯỚC 1)

Căn cứ Mục 1.1 của `SOW-8.5EMG-TROLLEY-v1.1` và Mục 3, Mục 4 của `PRD-8.5EMG-TROLLEY-v3.1`, phương án truyền động được lựa chọn tại Khối 0 phải giải quyết bài toán di chuyển ngang xe con cầu trục dầm đôi ($x = 2$) với các ràng buộc định lượng sau:

1. **Ràng buộc về Phụ tải & Điều kiện biên vật lý:**

   * Tải trọng nâng định mức: $Q = 12,222\text{ kg}$; khối lượng cơ cấu nâng hạ: $m_{nh} = 222\text{ kg}$; tự trọng bản thân xe con dầm đôi: $m_{xc} = 1,800\text{ kg}$ (Catalogue KG-Cranes Hàn Quốc 15 tấn (Tham khảo, chưa xác minh bản gốc)).

   * Tổng khối lượng dịch chuyển khi đầy tải: $M_\Sigma = Q + m_{nh} + m_{xc} = 14,244\text{ kg}$; tổng khối lượng khi chạy không tải: $m_{\text{tĩnh}} = m_{nh} + m_{xc} = 2,022\text{ kg}$ (tỷ số biến thiên khối lượng giữa đầy tải và không tải lên tới $14,244 / 2,022 \approx 7.04\text{ lần}$).

   * Đường kính bánh xe con: $d = 0.25\text{ m}$ (`[C] Giả định nhóm 8.5-EMG` ); suất cản lăn riêng: $w_0 = 0.015$ (1.5%) (`[C] Giả định nhóm 8.5-EMG` theo [R1, §2.4.7.2.2, tr.99–101] (trị số $w_0 = 0.015$ là giả định `[C]`)); hệ số bám dính ray thép: $\varphi = 0.20$ (`[C]` theo [R5, Bài 4, tr.43]); hiệu suất truyền động cơ khí: $\eta = 0.90$ (`[C]` SSoT P-15: hộp giảm tốc 3 cấp + khớp nối + ổ lăn).
   * Lực cản tĩnh đầy tải: $F_c = w_0 \cdot M_{\Sigma} \cdot g = 0.015 \cdot 14,244 \cdot 9.81 \approx 2,096\text{ N}$; Công suất tĩnh: $P_{\text{tĩnh}} = \frac{F_c \cdot v_{\max}}{\eta} = \frac{2,096 \cdot 0.12}{0.90} \approx 279.5\text{ W} \approx 0.28\text{ kW}$.
   * Lực kéo cực đại khi tăng tốc ($a = 0.5\text{ m/s}^2$): $F_{\max} = F_c + F_{qt} = 2,096 + 14,244 \cdot 0.5 = 9,218\text{ N} \approx 9.22\text{ kN}$; Công suất đỉnh gia tốc: $P_{\max} = \frac{9,218 \cdot 0.12}{0.90} \approx 1,229\text{ W} \approx 1.23\text{ kW}$.

   * Chiều cao nâng tối đa (chiều dài cáp treo tải): $h = l \le 12\text{ m}$, tạo thành hệ con lắc đơn điểm treo di động có tần số góc dao động riêng $\omega_p = \sqrt{g/l} = \sqrt{9.81/12} \approx 0.904\text{ rad/s}$ (chu kỳ dao động tự nhiên $T_p = 2\pi/\omega_p \approx 6.95\text{ s}$) (Mita & Kanai, 1979 [R9-01]).

2. **8 Yêu cầu Khách hàng Cốt lõi trong Phạm vi SOW (*Customer Requirements — WHATs*):**

   * **`PRD-FUNC-01` (Vận hành 4 góc phần tư & Đảo chiều):** Làm việc đầy đủ trên cả 4 góc phần tư $(\omega, M)$ ở hai chiều Tiến/Lùi (IEC 61800-2).

   * **`PRD-FUNC-02` (Điều chỉnh tốc độ êm & Cấp tốc độ bò):** Thay đổi tốc độ liên tục từ $0$ đến $v_{\max} = 0.12\text{ m/s}$ và có cấp tốc độ bò định vị (*Creep speed* bằng 25% $\div$ 30% $v_{\max}$ ($\approx 0.030 \div 0.036\text{ m/s}$)) (Yuantai Full VFD Dual-Speed Crane (Tham khảo, chưa xác minh bản gốc)).

   * **`PRD-FUNC-03` (Tiêu tán năng lượng hãm tái sinh):** Hấp thụ và tiêu tán an toàn động năng của khối lượng $14,244\text{ kg}$ trả ngược về mạch lực khi hãm giảm tốc ở góc phần tư II và IV (Catalogue Demag DR, tr. 8 [R9-07]).

   * **`PRD-FUNC-04` (Phối hợp đồng bộ Phanh cơ và Mô-men điện):** Chỉ mở phanh cơ thường đóng khi động cơ đã tạo đủ mô-men giữ tải và đóng phanh khóa trục ngay khi $v = 0\text{ m/s}$ (TCVN 4244:2005, Mục 1.5.3.3.3 [R1]).

   * **`PRD-PERM-01` (Đáp ứng tải trọng kéo ngang định mức):** Đủ lực kéo và mô-men cho cả trạng thái đầy tải ($14,244\text{ kg}$) và không tải ($2,022\text{ kg}$).

   * **`PRD-PERM-02` (Vận tốc định mức & Độ chính xác tốc độ):** Đạt $v_{\max} = 0.12\text{ m/s}$ ($7.2\text{ m/phút}$) với sai lệch xác lập $e_{xl} \le 5$% và độ quá điều chỉnh $M_p \le 10$% (IEC 61800-2).

   * **`PRD-PERM-03` (Giới hạn Gia tốc & Độ giật chống lắc tải):** Giữ $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và $\lvert \rho(t) \rvert = \lvert \text{d}a/\text{d}t \rvert \le 2.0\text{ m/s}^3$ trong mọi pha tăng/giảm tốc làm việc bình thường (ResearchGate, 2020 [R9-11]).

   * **`PRD-PERM-04` (Đáp ứng chế độ nhiệt** $S3$**):** Làm việc ở chế độ ngắn hạn lặp lại $S3$ ($CD = 40$%) với hệ số dự trữ công suất phát nhiệt $k_{dt} \ge 1.2$ (cận trên 1.5 của v1.1 đã bỏ theo SRS A.1, CR-01; biên kinh tế `QCD-C01` là $P_{đm} \le 1.5\,P_{\max} \approx 1.84\text{ kW}$ theo QĐ-08), nguồn 3 pha $380\text{V}$ ($\pm 10$%) / $50\text{Hz}$ (IEC 60034-1 [R4, tr.23]).

## 3. KHẢO SÁT CÁC CASE STUDIES THỰC TẾ VÀ BÀI BÁO KHOA HỌC (BƯỚC 2)

Nhóm 8.5-EMG đã thu thập và phân tích sâu **6 công trình nghiên cứu học thuật quốc tế (Case Studies 1–6)** kết hợp với **3 hồ sơ kỹ thuật công nghiệp (Industrial Cases 7–9)** có đối tượng và thông số gần sát với đề bài $x = 2$:

### 3.1. Phân tích Chi tiết 6 Bài báo / Đồ án Nghiên cứu Học thuật

| Mã Case Study | Tên Công trình, Tác giả, Năm & Nguồn Công bố | Thông số Hệ thống trong Nghiên cứu | Vấn đề Giải quyết & Phương pháp Kỹ thuật Cốt lõi | Kết quả Đạt được & Giá trị Tham chiếu cho Nhóm 8.5-EMG | 
| ----- | ----- | ----- | ----- | ----- | 
| **`CS-01`**  *(Nhật Bản, 1979)* | **Optimal Control of the Crane System Using the Maximum Speed of the Trolley**  • *Tác giả:* T. Mita & T. Kanai (ĐH Chiba, Nhật Bản) | • Ví dụ tính toán: $v_{\max} = 15\text{ m/s}$, $a_{\max} = 3\text{ m/s}^2$, cáp $l = 3\text{ m}$ ($K_m = 9$).  • Mô hình thực nghiệm: Tải $2.1\text{ kg}$, cáp $l = 1\text{ m}$, vi xử lý 12-bit Toshiba TLCS-12A. | • **Vấn đề:** Giải bài toán mâu thuẫn giữa di chuyển xe con nhanh nhất và triệt tiêu góc lắc tải $\theta$ tại điểm đích.  • **Phương pháp:** Thiết lập phương trình vi phân con lắc $\ddot{\theta} + (g/l)\theta = \ddot{X}/l$; chia hành trình thành **3 giai đoạn** (Tăng tốc – Chạy đều – Giảm tốc) và dùng nguyên lý cực đại Pontryagin tìm luật điều khiển gia tốc **Bang-Bang** ($\pm \alpha_m$) theo tham số $K_m = X_m\sqrt{g/l}/\alpha_m$. | • **Kết quả:** Góc lắc dư sau khi dừng $< \pm 0.2^\circ$.  • **Kế thừa:** Cung cấp phương trình toán học chuẩn của tải treo cáp và tư duy chia chu trình vận hành 3 pha (vì ở pha chạy đều $a = 0$ không sinh thêm kích thích dao động). | 
| **`CS-02`**  *(Indonesia, 2025)* | **Perencanaan Sistem Trolley dan Bridge Pada Overhead Travelling Crane Beban Angkat 10 Ton** [R9-02]  • *Tác giả:* P. G. Feto, Wartono, Sutrisna (ITNY, Indonesia — *Cendekia Mekanika*) | • Tải nâng + móc: $Q = 10,047\text{ kg}$ ($\approx 10\text{ tấn}$).  • Tự trọng xe con: $G_t = 4,000\text{ kg}$.  • Tốc độ xe con: $15\text{ m/phút}$ ($0.25\text{ m/s}$).  • Số bánh xe: $4$ bánh ($P_{\max} = 3,511\text{ kg/bánh}$). | • **Vấn đề:** Tính toán thiết kế chuỗi truyền động cơ khí từ trục động cơ (quay nhanh $970\text{ rpm}$) xuống bánh xe con (quay chậm $9.55\text{ rpm}$).  • **Phương pháp:** Thiết kế hộp giảm tốc bánh răng trụ **3 cấp** ($i_{\text{tổng}} = 101.6$, mỗi cấp $i \approx 4.66$), tính bền trục thép S45C, khớp nối bích và phanh cơ theo tiêu chuẩn Rudenko (hệ số an toàn phanh $v = 3$). | • **Kết quả:** Xác lập quy trình tính chọn cơ khí tuần tự từ Động cơ $\to$ Hộp số 3 cấp $\to$ Trục $\to$ Khớp nối $\to$ Phanh.  • **Kế thừa:** Giải thích rõ cơ sở chọn hộp giảm tốc 3 cấp tỷ số truyền lớn cho xe con chạy chậm và nguyên lý phanh cơ giữ tải an toàn khi mất điện. | 
| **`CS-03`**  *(Thổ Nhĩ Kỳ, 2023)* | **Design and Analysis of Double Girder Overhead Crane System** [R9-03]  • *Tác giả:* Serap Özhan Doğan (ĐH Beykent, Istanbul — *Elsevier JRRAS*) | • Tải nâng thiết kế: $10,000\text{ kg}$ **($10\text{ tấn}$)** (cuộn tôn mạ kẽm $2 \div 6\text{ tấn}$).  • Chiều cao nâng: $5\text{ m}$; nhịp dầm: $6\text{ m}$.  • Động cơ nâng: $65\text{ kW}$; động cơ dầm cầu: $10\text{ kW}$.  • **Động cơ kéo xe con (*Car*):** $4\text{ kW}, 1000\text{ rpm}$. | • **Vấn đề:** Phân tích tải trọng tĩnh, tải trọng động và kiểm nghiệm độ bền kết cấu cầu trục dầm đôi theo tiêu chuẩn Châu Âu `TS EN 13001-3-2`.  • **Phương pháp:** Tính toán lý thuyết có nhân hệ số động lực học ($1.14 \div 1.15$), tính lực quán tính ngang khi tăng/giảm tốc và mô phỏng phần tử hữu hạn (FEM) trên SolidWorks + ANSYS. | • **Kết quả:** Chứng minh kết cấu cầu trục dầm đôi $10\text{ tấn}$ an toàn ở cả vị trí đầu dầm và giữa dầm.  • **Kế thừa:** Cung cấp số liệu thực tế cực kỳ quý giá: Với tải $10\text{ tấn}$, công suất động cơ kéo ngang xe con chỉ cần $4\text{ kW}$ (nhỏ hơn rất nhiều so với động cơ nâng hạ $65\text{ kW}$). | 
| **`CS-04`**  *(IEEE DAS, 2024)* | **Increasing the Damping Capacity of Crane Electric Drive Systems When Moving Cargo with a Flexible Suspension** [R9-04]  • *Tác giả:* S. Valtchev, E. Gracheva, A. Sinyukov, R. Miceli et al. (*IEEE DAS 2024*, Romania) | • Khối lượng tải: $M = 5\text{ tấn}$ **($5,000\text{ kg}$)**.  • Chiều dài cáp treo mềm: $l = 5\text{ m}$ **và** $l = 10\text{ m}$ (rất sát với $h = 12\text{ m}$ của nhóm).  • Truyền động: Động cơ KĐB 3 pha + **Biến tần điều khiển Vector**. | • **Vấn đề:** Chứng minh bằng mô phỏng rằng hệ truyền động chỉ dùng bộ tạo dốc tuyến tính (*Linear Ramp / Intensity controller*) làm tải lắc biên độ lớn ($\theta_{\max} \approx 0.4\text{ rad} \approx 23^\circ$) và không tự tắt khi chạy đều hay khi dừng.  • **Phương pháp:** Giữ nguyên mạch vòng **Vector Control** của biến tần và bổ sung khối điều khiển mờ (**Fuzzy Logic Controller**) nhận phản hồi góc lệch $\theta$ và vận tốc góc $\dot{\theta}$ để sinh tín hiệu bù gia tốc $\Delta a$. | • **Kết quả:** Giảm hơn 50% biên độ lắc khi khởi động ($\theta_{\max} \approx 0.18\text{ rad}$) và dập tắt hoàn toàn dao động dư ngay khi dừng ở cả $l = 5\text{ m}$ và $10\text{ m}$.  • **Kế thừa:** Khẳng định bắt buộc phải dùng **Biến tần Vector** và phải loại bỏ bộ tạo dốc tuyến tính *Linear Ramp* thông thường. | 
| **`CS-05`**  *(Sensors & Materials, 2021)* | **Vision-based Fuzzy Proportional–Integral–Derivative Tracking Control Scheme for Gantry Crane System** [R9-05]  • *Tác giả:* F. Zheng, C.-H. Yang, G. Hao et al. (ĐH Tam Minh — *Sensors & Materials*, Vol. 33) | • Hệ cầu trục **2 bậc tự do (2-DOF)**: Xe con chạy ngang $q_1(t)$ ($0 \to 1.0\text{ m}$) đồng thời thu ngắn cáp $q_2(t) = l(t)$ ($1.0 \to 0.5\text{ m}$).  • Đo lường bằng Camera tốc độ cao xử lý ảnh biên cạnh (*Edge Detection*). | • **Vấn đề:** Khi chiều dài cáp $l(t)$ thay đổi, tần số riêng $\omega_0(t) = \sqrt{g/l(t)}$ biến thiên liên tục khiến bộ điều khiển PID thông số cố định bị **vọt lố vị trí** $> 8$% và góc lắc lớn ($\approx 7.5^\circ$).  • **Phương pháp:** Thiết lập hệ phương trình Lagrange 2-DOF và thuật toán **PID mờ thích nghi vũ trụ biến thiên (VUFAPID)** tự co giãn miền xác định theo hàm mũ $\alpha(e) = 1 - 0.6\exp(-0.5e^2)$. | • **Kết quả:** Triệt tiêu hoàn toàn vọt lố (**Overshoot** $= 0$%), thời gian xác lập nhanh nhất ($< 2.8\text{ s}$) và góc lắc cực đại $< 3.5^\circ$.  • **Kế thừa:** Cung cấp luận cứ khoa học về ảnh hưởng của chiều dài cáp $l \le 12\text{ m}$ và chứng minh PID cổ điển không đáp ứng được nếu thiếu quy hoạch quỹ đạo êm. | 
| **`CS-06`**  *(ĐH Bách Khoa Kiev — KPI, 2024)* | **Система автоматичного керування електроприводом мостового крана складського комплексу** [R9-06]  • *Tác giả:* Y. O. Shevchenko; *GVHD:* PGS.TS. B. I. Pryymak (NTUU KPI, Ukraine, 06/2024) | • Tải nâng: $G_{\text{nom}} = 74,500\text{ N}$ ($\approx 7.6\text{ tấn}$); Xe con: $29,400\text{ N}$ ($\approx 3.0\text{ tấn}$).  • Vận tốc: $v_{\text{nom}} = 0.9\text{ m/s}$; Gia tốc: $a = 0.25\text{ m/s}^2$.  • Chế độ: $S3$ ($CD = 25$%), $60\text{ lần/giờ}$.  • Bánh xe $D_k = 0.6\text{ m}$, $i_p = 15, \eta_M = 0.80$. | • **Vấn đề:** Thiết kế trọn vẹn hệ truyền động điện cơ cấu di chuyển cầu trục từ tính chọn phần lực đến tổng hợp mạch vòng điều khiển và mô phỏng Simulink.  • **Phương pháp:**    1. *Phần lực:* Tính lực cản tĩnh $W_{\text{tĩnh}}$, mô-men tĩnh $M_{c.\text{tĩnh}}$, quán tính quy đổi $J_\Sigma$, biểu đồ phụ tải 4 giai đoạn chu kỳ $S3$ và mô-men đẳng trị nhiệt $M_{đt} = \sqrt{\sum M_i^2 t_i / \sum t_i}$. Chọn động cơ KĐB 3 pha **4A180M8U3** ($15\text{ kW}, 380\text{V}, n_0 = 750\text{ rpm}$) và biến tần **ABB ACS380** tích hợp **Braking Chopper + Điện trở xả hãm**.    2. *Phần điều khiển:* Thiết kế hệ **Vector tựa từ thông rotor (RFOC)** có **Encoder** với **Bộ tạo quỹ đạo S-Curve** hạn chế đạo hàm gia tốc, **2 mạch vòng PI dòng điện ($i_d, i_q$)** tổng hợp theo **Tối ưu Module (MO)** và **1 mạch vòng PI tốc độ ($\omega$)** tổng hợp theo **Tối ưu Đối xứng (SO)**. | • **Kết quả:** Dòng khởi động được khóa chặt $\le 1.5 I_{\text{nom}}$, từ thông rotor giữ phẳng tuyệt đối, tốc độ bám sát đường cong S-Curve không vọt lố, nhiệt độ cuộn dây nằm trong giới hạn chế độ $S3$.  • **Kế thừa:** Đây là **Bản thiết kế mẫu hạt nhân (Core Reference)** khớp gần như hoàn toàn về quy trình tính chọn phần lực chế độ $S3$, cấu trúc biến tần – điện trở hãm và sơ đồ khối điều khiển Vector FOC 3 mạch vòng trên MATLAB/Simulink. | 

### 3.2. Tổng hợp 3 Hồ sơ Công nghiệp Thực tế từ Catalogue Hãng (Đã khóa tại PRD Mục 1.2)

Bên cạnh 6 bài báo học thuật, nhóm kết hợp 3 hồ sơ kỹ thuật từ các nhà sản xuất cầu trục công nghiệp hàng đầu để đảm bảo phương án chọn bám sát thực tiễn sản xuất:

1. **`CS-07` — Catalogue Demag Cranes (Đức) — Dòng EZDR 10 & EZDR 20 Double-Rail Crab (12.5t – 20t) [R9-07]:** Chuẩn công nghiệp Châu Âu cho xe con dầm đôi cấp tải $12.5 \div 20\text{ tấn}$ sử dụng **Động cơ KĐB lồng sóc gắn sẵn Encoder xung tiêu chuẩn (*Pulse encoder as standard*, tr. 4)**, **Biến tần di chuyển ngang tích hợp sẵn Điện trở xả hãm trong tủ điện (*Cross-travel inverter and braking resistor integrated*, tr. 8)** và **Phanh đĩa điện từ một chiều tự động đóng nhanh khi mất điện** (hệ số an toàn $\ge 1.8$).

2. **`CS-08` — Catalogue KG-Cranes / Sungdo (Hàn Quốc) — Pa lăng cáp điện dầm đôi 10t – 15t – 20t (Tham khảo, chưa xác minh bản gốc):** Cung cấp cơ sở thực nghiệm để khóa giả định tự trọng xe con $m_{xc} = 1,800\text{ kg}$ (model $15\text{ tấn}, h = 12\text{ m}$ có tổng khối lượng cụm xe con $1,820\text{ kg}$), nguồn cấp 3 pha $380\text{V}/50\text{Hz}$ và cấp bảo vệ động cơ $\text{IP54}$ (Catalogue Sungdo (Tham khảo, chưa xác minh bản gốc)).

3. **`CS-09` — Catalogue Cầu trục Dầm đôi Biến tần Yuantai / Konecranes (10t – 15t, ISO M5) (Tham khảo, chưa xác minh bản gốc):** Khẳng định cơ cấu di chuyển ngang xe con $10 \div 15\text{ tấn}$ dùng biến tần điều khiển đa cấp tốc độ (có cấp **tốc độ bò định vị** để lắp đặt tải nặng chính xác) và chỉ cần công suất động cơ rất nhỏ từ $1.1 \div 2.2\text{ kW}$ nhờ hộp giảm tốc tỷ số truyền lớn.

## 4. PHÂN TÍCH KHOẢNG TRỐNG CÔNG NGHỆ — TECH GAP ANALYSIS (BƯỚC 3)

Khi đem các mô hình và giải pháp trong 9 Case Studies ở Mục 3 đối chiếu trực tiếp với **8 yêu cầu `PRD-FUNC` / `PRD-PERM`** và **bộ thông số đầu bài** $x = 2$ của Nhóm 8.5-EMG, chúng ta nhận diện được **7 Khoảng trống Công nghệ (`GAP-01`** $\to$ **`GAP-07`)**. Bảng dưới đây phân tích bản chất vật lý của từng khoảng trống và định hướng giải pháp lấp đầy:

| Mã Tech Gap | Hạng mục Kỹ thuật & Mã PRD Liên quan | Giải pháp / Thông số trong các Case Studies Gốc | Khoảng trống Công nghệ (*Tech Gap*) khi Áp vào Đề bài $x = 2$ của Nhóm 8.5-EMG | Định hướng Giải pháp Kỹ thuật để Lấp đầy Khoảng trống | 
| ----- | ----- | ----- | ----- | ----- | 
| **`GAP-01`** | **Quy đổi Công suất Động cơ theo Vận tốc & Tải trọng**  (`PRD-PERM-01`, `PRD-PERM-04`, `QCD-C01`) | • `CS-06` (Shevchenko KPI, 2024 [R9-06]): Tải $7.6\text{ tấn}$, xe $3\text{ tấn}$ nhưng chạy rất nhanh ($v = 0.9\text{ m/s}$) $\to$ Chọn động cơ $15\text{ kW}$.  • `CS-02` (Feto, 2025 [R9-02]): Chọn động cơ $30\text{ kW}$. | • Đề bài nhóm ($x = 2$) có tổng khối lượng đầy tải lớn hơn ($M_\Sigma = 14,244\text{ kg}$ so với $10,600\text{ kg}$ của Shevchenko), nhưng vận tốc tối đa $v_{\max} = 0.12\text{ m/s}$ **chậm hơn** $7.5\text{ lần}$ so với Shevchenko ($0.9\text{ m/s}$).  • Vì công suất cản tĩnh và công suất tăng tốc tỉ lệ thuận với vận tốc dài ($P = F \cdot v$), nếu nhóm sao chép máy móc động cơ $15\text{ kW}$ của Shevchenko sẽ bị dư thừa công suất gấp $5 \div 7\text{ lần}$, vi phạm nghiêm trọng chỉ tiêu kinh tế `QCD-C01` ($P_{đm} \le 1.5\,P_{\max} \approx 1.84\text{ kW}$, QĐ-08). | • Kế thừa **trọn vẹn phương pháp và công thức tính chọn đẳng trị nhiệt chế độ** $S3$ của `CS-06`, nhưng thay bộ thông số của nhóm ($M_\Sigma = 14,244\text{ kg}, v_{\max} = 0.12\text{ m/s}$, $CD = 40$%) để định cỡ lại động cơ và biến tần (kết quả Khối 3: chốt SEW DRN80M4 $0.75\text{ kW}$ theo QĐ-04; dải ước lượng $1.5 \div 3.7\text{ kW}$ của v1.1 đã bỏ; đối chứng với `CS-03` Doğan $4\text{ kW}$ [R9-03] và `CS-09` Yuantai $1.1 \div 2.2\text{ kW}$ (Tham khảo, chưa xác minh bản gốc)). | 
| **`GAP-02`** | **Độ chính xác Tốc độ ở Vùng Tốc độ Thấp & Chế độ Bò**  (`PRD-PERM-02`, `PRD-FUNC-02`) | • Hệ truyền động truyền thống hoặc biến tần vô hướng $U/f = \text{const}$ vòng hở không có phản hồi tốc độ.  • Biến tần Vector không cảm biến (*Sensorless*) ước lượng tốc độ qua mô hình toán stator. | • Xe con đề bài chạy rất chậm ($v_{\max} = 0.12\text{ m/s}$) và khi xuống **cấp tốc độ bò định vị (bằng 25% $v_{\max} = 0.03\text{ m/s}$)**, tần số điện áp cấp vào động cơ hạ xuống rất thấp ($f \approx 10 \div 15\text{ Hz}$, thậm chí $< 5\text{ Hz}$ lúc khởi hành).  • Ở vùng tần số thấp và khi khối lượng tải thay đổi gấp $7.04\text{ lần}$ (từ $2,022\text{ kg}$ lên $14,244\text{ kg}$), điều khiển $U/f$ bị sụt từ thông do sụt áp trên điện trở stator $R_1$ và trượt tốc độ lớn ($s > 5$%), còn *Sensorless Vector* bị sai lệch ước lượng khi $\omega \to 0$, không thể đảm bảo chắc chắn $e_{xl} \le 5$% và $M_p \le 10$%. | • Bắt buộc trang bị **Cảm biến phản hồi tốc độ thực tế (Encoder xung)** gắn trên trục động cơ kết hợp cấu trúc **Điều khiển Vector tựa từ thông rotor vòng kín (Closed-loop RFOC)** như trong `CS-06` (Shevchenko, 2024 [R9-06]) và `CS-07` (Demag DR, tr. 4 [R9-07]). | 
| **`GAP-03`** | **Sinh Mô-men Giữ ở Tốc độ** $0\text{ rpm}$ **& Phối hợp Mở Phanh cơ**  (`PRD-FUNC-04`, `PRD-FUNC-01`) | • `CS-06` (Shevchenko, 2024 [R9-06]) tập trung vào mạch vòng liên tục, chưa mô tả chi tiết máy trạng thái phối hợp phanh cơ điện từ.  • Các hệ không có Encoder không thể tạo đủ mô-men giữ tĩnh định mức tại $\omega = 0\text{ rad/s}$. | • Yêu cầu `PRD-FUNC-04` và TCVN 4244:2005 (Mục 1.5.3.3.3) [R1] đòi hỏi chỉ được mở phanh cơ khi động cơ đã thiết lập đủ mô-men giữ tải (*Zero-speed holding torque*) và phải khóa phanh cơ ngay khi $v = 0\text{ m/s}$ trước khi cắt dòng kích từ.  • Nếu dùng biến tần vòng hở hoặc thiếu khối logic phối hợp, xe con sẽ bị giật cục lúc nhả phanh hoặc bị trượt trôi khi dừng. | • Sử dụng **Vector FOC có Encoder** để tách biệt hoàn toàn dòng từ hóa $i_{sd}$ (tạo từ thông định mức ngay từ khi $\omega = 0$) và dòng sinh mô-men $i_{sq}$, kết hợp thiết kế **Khối Logic Vận hành 4 góc phần tư & Điều khiển Phanh cơ** riêng biệt ở Khối 3 (`SOW-3.4`). | 
| **`GAP-04`** | **Giới hạn Độ giật** $\rho_{\max} \le 2.0\text{ m/s}^3$ **& Chống sốc Cơ khí**  (`PRD-PERM-03`, `PRD-FUNC-02`) | • `CS-01` (Mita & Kanai, 1979 [R9-01]) dùng điều khiển gia tốc **Bang-Bang** (nhảy bậc tức thời giữa $+\alpha_m$ và $-\alpha_m$).<br>• Hệ truyền thống trong `CS-04` dùng bộ tạo dốc tuyến tính **Linear Ramp** (gia tốc nhảy bậc hình chữ nhật tại đầu và cuối dốc). | • Khi gia tốc $a(t)$ thay đổi nhảy bậc (hàm *Step* trong Bang-Bang hoặc Linear Ramp), đạo hàm của gia tốc theo thời gian là **độ giật** $\rho(t) = \text{d}a/\text{d}t \to \infty$, vi phạm trực tiếp chỉ tiêu cứng `PRD-PERM-03` ($\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$, $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$), gây xung lực va đập răng hộp số 3 cấp và kích thích dao động lắc tải cáp $h = 12\text{ m}$. | • Thực hiện **Kaizen (Cải tiến)** bằng cách thay thế bộ tạo dốc tuyến tính bằng **Bộ tạo quỹ đạo S-Curve 7 đoạn (*7-Segment S-Curve Trajectory Generator*)** đặt trước mạch vòng tốc độ (ResearchGate, 2020 [R9-11]; `CS-06` Shevchenko, 2024 [R9-06]) để khóa chặt $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$ trên toàn chu trình. |
| **`GAP-05`** | **Mô hình hóa Phụ tải Treo mềm** $h = 12\text{ m}$ **trong Kiểm chứng Simulink**  (`PRD-PERM-03`, `SOW-5.1`) | • `CS-06` (Shevchenko, 2024 [R9-06]) quy đổi toàn bộ khối lượng tải thành mô-men quán tính cứng $J_\Sigma$ trên trục động cơ, chưa nối với phương trình dao động góc lắc $\theta(t)$. | • Với chiều cao nâng $h = 12\text{ m}$ và khối lượng hàng $Q = 12,222\text{ kg}$ của đề bài $x = 2$, tải treo cáp dao động như con lắc đơn ($\omega_p \approx 0.904\text{ rad/s}$) và tạo lực căng ngang tác động ngược lại xe con.  • Nếu chỉ mô phỏng quán tính cứng như Shevchenko thì chưa trực quan hóa được hiệu quả giảm lắc của quỹ đạo S-Curve. | • Kết hợp mô hình truyền động điện **RFOC + S-Curve** của `CS-06` với **phương trình vi phân con lắc điểm treo di động** $\ddot{\theta} + (g/l)\theta = a_t/l$ của `CS-01` (Mita & Kanai, 1979 [R9-01]) và `CS-04` (Valtchev et al., 2024 [R9-04]) trong mô hình kiểm chứng MATLAB/Simulink. | 
| **`GAP-06`** | **Xử lý Năng lượng Hãm Tái sinh ở Góc phần tư II & IV**  (`PRD-FUNC-03`, `PRD-FUNC-01`) | • Các bài báo thuần túy về lý thuyết điều khiển (`CS-01`, `CS-05`) chỉ xét lực kéo toán học $F(t)$ mà bỏ qua cấu trúc biến đổi năng lượng của mạch một chiều trung gian (DC-Link) trong biến tần. | • Khi tổng khối lượng $M_\Sigma = 14,244\text{ kg}$ giảm tốc từ $v_{\max} = 0.12\text{ m/s}$ về $0\text{ m/s}$ với $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ ở góc phần tư II và IV, động năng tích lũy của hệ chuyển thành điện năng bơm ngược về tụ DC-Link của biến tần (do chỉnh lưu cầu diode đầu vào không trả năng lượng về lưới được), gây nguy cơ quá áp DC-bus ($U_{\text{dc}} > 800\text{ V DC}$) và ngắt lỗi bảo vệ. | • Kế thừa cấu trúc phần lực công nghiệp của `CS-06` (Shevchenko, 2024 [R9-06]) và `CS-07` (Catalogue Demag DR, tr. 8 [R9-07]): Tích hợp **Bộ băm xung áp một chiều (*Braking Chopper*)** và **Điện trở xả năng lượng hãm tái sinh ($R_h$)** nối trực tiếp trên thanh cái DC-Link để tiêu tán nhiệt an toàn. |
| **`GAP-07`** | **Tính Khả thi của Cảm biến Đo góc lắc & Ranh giới Phạm vi SOW**  (`SOW Mục 1.1`, `QCD-C02`, `QCD-D01`) | • `CS-04` (Valtchev et al., 2024 [R9-04]) đòi hỏi đo góc lệch cáp $\theta, \dot{\theta}$ đưa vào bộ điều khiển Mờ.  • `CS-05` (Zheng et al., 2021 [R9-05]) dùng Camera công nghiệp xử lý ảnh thời gian thực và thuật toán VUFAPID. | • Trong môi trường nhà xưởng công nghiệp nặng (nhiều bụi kim loại, độ cao $12\text{ m}$, ánh sáng thay đổi), cảm biến góc cơ khí gắn trên puly cáp hoặc hệ thống Camera Vision rất dễ bị nhiễu, đắt tiền và đòi hỏi hiệu chỉnh luật mờ phức tạp.  • Mặt khác, `SOW-8.5EMG-TROLLEY-v1.1` quy định chỉ sử dụng cảm biến phản hồi tốc độ trên trục động cơ và giới hạn số vòng lặp thiết kế $\le 2$. | • Không sử dụng cảm biến đo góc cáp ngoài hay Camera Vision trong cấu hình chuẩn; thay vào đó, giải quyết bài toán chống lắc ngay từ gốc bằng **Bộ tạo quỹ đạo S-Curve giới hạn độ giật** kết hợp **vòng kín tốc độ/dòng điện RFOC có Encoder** (độ tin cậy công nghiệp cao nhất và hoàn toàn khả thi trong phạm vi SOW). | 

## 5. TRIỂN KHAI CHỨC NĂNG CHẤT LƯỢNG (QFD) & NGÔI NHÀ CHẤT LƯỢNG (HoQ) (BƯỚC 4)

### 5.1. Cơ sở Lý thuyết QFD & Vai trò của Ngôi nhà Chất lượng (HoQ)

Theo NASA Systems Engineering Toolbox (Mục 7.12, tr. 7-51) [R2] và Hướng dẫn Công cụ Phân tích Quyết định của NASA [R2], **QFD (*Quality Function Deployment* — Triển khai chức năng chất lượng)** là phương pháp luận có cấu trúc nhằm chuyển hóa các yêu cầu của khách hàng (*Customer Needs*) thành các đặc tính kỹ thuật cụ thể của hệ thống. Trong quy trình QFD, **Ngôi nhà Chất lượng (*House of Quality — HoQ*)** là ma trận trung tâm thực hiện nhiệm vụ cầu nối giữa **Không gian Bài toán (*Problem Space* — PRD/SOW)** và **Không gian Giải pháp (*Solution Space* — Các phương án cấu hình truyền động)**:

* **Phần Tường trái (*Left Wall — WHATs & Customer Importance*** $d_i$**):** Gồm **8 mã yêu cầu khách hàng trong phạm vi SOW** (`PRD-FUNC-01..04` và `PRD-PERM-01..04`), được gán trọng số ưu tiên của khách hàng $d_i \in \{1 \dots 5\}$ (trong đó $5$ là yêu cầu sống còn bắt buộc — *Critical to Quality / Safety*, $4$ là rất quan trọng, $3$ là quan trọng tiêu chuẩn).

* **Phần Trần nhà (*Ceiling — HOWs / Engineering Characteristics*** $\text{EC}_j$**):** Gồm **8 Đặc tính Kỹ thuật Hệ thống (`EC-01`** $\to$ **`EC-08`)** kèm hướng tối ưu hóa ($\uparrow$: càng lớn càng tốt; $\downarrow$: càng nhỏ càng tốt; $\odot$: đạt đích danh định) được thiết lập để giải quyết trực tiếp 7 khoảng trống công nghệ (`GAP-01..07`).

* **Phần Phòng chính (*Relationship Matrix —*** $R_{ij}$**):** Đánh giá mức độ tác động của đặc tính kỹ thuật $\text{EC}_j$ lên khả năng thỏa mãn yêu cầu khách hàng $\text{PRD}_i$ theo thang điểm chuẩn QFD:

  * $\bullet = 9$ **điểm:** Tương quan **Mạnh (*Strong*)** — Đặc tính kỹ thuật quyết định trực tiếp việc đạt hay trượt yêu cầu PRD.

  * $\circ = 3$ **điểm:** Tương quan **Trung bình (*Moderate*)** — Đặc tính kỹ thuật hỗ trợ quan trọng cho yêu cầu PRD.

  * $\triangle = 1$ **điểm:** Tương quan **Yếu (*Weak*)** — Có ảnh hưởng gián tiếp.

  * **`Không (0)`** $= 0$ **điểm:** Không có tương quan trực tiếp (ghi rõ `Không (0)` trong ô để tránh ô trống).

* **Phần Mái nhà (*Roof Correlation Matrix*):** Phân tích sự tương hỗ hoặc xung đột giữa các đặc tính kỹ thuật $\text{EC}_j$ với nhau (`++`: Đồng thuận mạnh; `+`: Đồng thuận; `-`: Xung đột/Mâu thuẫn cần trade-off).

* **Phần Móng nhà (*Foundation — Technical Importance Weight*** $W_j$ ***&*** $w_j$ (%)**):** Tính điểm tầm quan trọng tuyệt đối và tỷ lệ phần trăm của từng đặc tính kỹ thuật theo công thức: 

  $$
  W_j = \sum_{i=1}^{8} d_i \cdot R_{ij} \quad \Longrightarrow \quad w_j(\%) = \frac{W_j}{\sum_{k=1}^{8} W_k} \times 100\%
  $$

### 5.2. Định nghĩa 8 Đặc tính Kỹ thuật Hệ thống (`HOWs` / `EC-01` $\to$ `EC-08`)

Bảng dưới đây định nghĩa tường minh 8 Đặc tính Kỹ thuật Hệ thống (`EC-01..08`) trên phần Trần nhà của HoQ và truy xuất trực tiếp tới các mã `Tech Gap` ở Bước 3:

| Mã EC (HOWs) | Tên Đặc tính Kỹ thuật Hệ thống (*Engineering Characteristic*) | Hướng Tối ưu | Giá trị Đích Kỹ thuật (*Target Value*) | Giải quyết Mã Tech Gap | 
| ----- | ----- | ----- | ----- | ----- | 
| **`EC-01`** | **Khả năng điều khiển tách kênh độc lập Mô-men & Từ thông trên 4 góc phần tư** ($\psi_r, M_e$) | $\odot$ *(Đích danh định)* | Điều khiển độc lập dòng từ hóa $i_{sd}$ và dòng mô-men $i_{sq}$ trên cả 4 góc phần tư $(\omega, M)$; thời gian đáp ứng mô-men $< 10\text{ ms}$. | `GAP-02`, `GAP-03` | 
| **`EC-02`** | **Độ chính xác phản hồi & điều khiển vòng kín tốc độ** ($e_{xl}, M_p$) | $\downarrow$ | Có phản hồi tốc độ thực tế; sai lệch tốc độ xác lập $e_{xl} \le 5$% và độ quá điều chỉnh $M_p \le 10$% từ không tải đến đầy tải. | `GAP-02` | 
| **`EC-03`** | **Khả năng sinh mô-men giữ tải tại tốc độ bằng không & đồng bộ phanh cơ** ($M_{\text{hold}}(0\text{ rpm})$) | $\uparrow$ | Tạo được từ 100% đến 150% $M_{\text{đm}}$ **tại tốc độ** $0\text{ rpm}$ trước khi nhả phanh cơ điện từ và khóa phanh đúng lúc $v = 0\text{ m/s}$. | `GAP-03` | 
| **`EC-04`** | **Khả năng quy hoạch quỹ đạo S-Curve 7 đoạn giới hạn gia tốc & độ giật** ($\lvert a_{\max} \rvert, \lvert \rho_{\max} \rvert$) | $\downarrow$ | Quy hoạch quỹ đạo S-Curve 7 đoạn khóa chặt $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và $\lvert \rho(t) \rvert = \lvert \text{d}a/\text{d}t \rvert \le 2.0\text{ m/s}^3$ giúp hạn chế góc lắc tải cáp $h = 12\text{ m}$. | `GAP-04`, `GAP-05` |
| **`EC-05`** | **Năng lực băm xung và tiêu tán công suất hãm tái sinh trên thanh cái DC-Link** ($P_{\text{br}}, U_{\text{dc}}$) | $\uparrow$ | Tích hợp mạch *Braking Chopper* và điện trở xả hãm $R_h$ giữ điện áp DC-bus $U_{\text{dc}} < 780\text{ V DC}$ trong suốt pha giảm tốc tải $14,244\text{ kg}$. | `GAP-06` | 
| **`EC-06`** | **Công suất định mức & Biên dự trữ phát nhiệt chế độ ngắn hạn lặp lại** $S3$ ($k_{dt}$) | $\odot$ *(Đích danh định)* | Tính chọn theo công suất đẳng trị chế độ $S3$ ($CD = 40$%) đạt hệ số dự trữ $k_{dt} \ge 1.20$ (SRS A.1) và quá tải mô-men $\lambda_{\max} \ge 2.0$. | `GAP-01` | 
| **`EC-07`** | **Độ rộng dải điều chỉnh tốc độ ổn định phục vụ cấp tốc độ bò** ($D = \omega_{\max}/\omega_{\min}$) | $\uparrow$ | Dải điều chỉnh tốc độ ổn định mô-men $D \ge 10:1$ (đáp ứng mượt cấp tốc độ bò 25% $\div$ 30% $v_{\max}$ và vùng khởi hành). | `GAP-02`, `GAP-03` | 
| **`EC-08`** | **Độ tin cậy cấu trúc phần cứng nhà xưởng & Tính khả thi mô phỏng Simulink** | $\uparrow$ | Số lượng cảm biến ngoài tối thiểu (không lắp cảm biến trên dây cáp treo), chuẩn hóa trên thư viện MATLAB/Simulink trong $\le 2$ vòng lặp. | `GAP-05`, `GAP-07` | 

### 5.3. Ma trận Ngôi nhà Chất lượng (House of Quality — HoQ) Hoàn chỉnh

Bảng dưới đây trình bày ma trận tính toán định lượng của **Ngôi nhà Chất lượng (HoQ)** chuyển hóa 8 mã yêu cầu `PRD-FUNC` / `PRD-PERM` sang 8 đặc tính kỹ thuật `EC-01..08`:

| Mã Yêu cầu Khách hàng (WHATs — Phạm vi SOW) | Trọng số $d_i$ | `EC-01`  Tách kênh $(\psi, M)$ 4 góc | `EC-02`  Vòng kín tốc độ ($e_{xl}, M_p$) | `EC-03`  Mô-men giữ $0\text{ rpm}$ & Phanh | `EC-04`  Quỹ đạo giới hạn $(a, \rho)$ | `EC-05`  Xả hãm DC-Link ($R_h$) | `EC-06`  Định cỡ nhiệt $S3$ ($k_{dt}$) | `EC-07`  Dải tốc độ bò ($D \ge 10:1$) | `EC-08`  Độ tin cậy & Simulink | 
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
| **`PRD-FUNC-01`:** Vận hành 4 góc phần tư & đảo chiều Tiến/Lùi | $5$ | $\bullet$ **(9)** | $\circ$ (3) | $\circ$ (3) | $\triangle$ (1) | $\bullet$ **(9)** | $\circ$ (3) | $\triangle$ (1) | $\circ$ (3) |
| **`PRD-FUNC-02`:** Điều chỉnh tốc độ êm & có cấp tốc độ bò định vị | $4$ | $\circ$ (3) | $\bullet$ **(9)** | $\triangle$ (1) | $\bullet$ **(9)** | $\triangle$ (1) | Không (0) | $\bullet$ **(9)** | $\circ$ (3) |
| **`PRD-FUNC-03`:** Hấp thụ và tiêu tán năng lượng hãm tái sinh | $5$ | $\bullet$ **(9)** | Không (0) | $\triangle$ (1) | $\circ$ (3) | $\bullet$ **(9)** | $\circ$ (3) | $\triangle$ (1) | $\circ$ (3) |
| **`PRD-FUNC-04`:** Phối hợp đồng bộ phanh cơ và mô-men điện | $5$ | $\bullet$ **(9)** | $\circ$ (3) | $\bullet$ **(9)** | $\triangle$ (1) | $\triangle$ (1) | Không (0) | $\circ$ (3) | $\circ$ (3) |
| **`PRD-PERM-01`:** Đáp ứng tải trọng kéo ngang ($M_\Sigma = 14,244\text{ kg}$) | $5$ | $\bullet$ **(9)** | $\circ$ (3) | $\circ$ (3) | $\triangle$ (1) | $\triangle$ (1) | $\bullet$ **(9)** | $\triangle$ (1) | $\triangle$ (1) |
| **`PRD-PERM-02`:** Đạt $v_{\max} = 0.12\text{ m/s}$, $e_{xl} \le 5$%, $M_p \le 10$% | $5$ | $\bullet$ **(9)** | $\bullet$ **(9)** | $\triangle$ (1) | $\circ$ (3) | Không (0) | $\triangle$ (1) | $\bullet$ **(9)** | $\circ$ (3) |
| **`PRD-PERM-03`:** Giới hạn $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$, $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$ ($h = 12\text{ m}$) | $5$ | $\circ$ (3) | $\bullet$ **(9)** | $\triangle$ (1) | $\bullet$ **(9)** | $\circ$ (3) | Không (0) | $\triangle$ (1) | $\bullet$ **(9)** |
| **`PRD-PERM-04`:** Đáp ứng chế độ nhiệt $S3$ ($CD = 40$%, $k_{dt} \ge 1.2$) | $4$ | $\triangle$ (1) | Không (0) | Không (0) | $\triangle$ (1) | $\circ$ (3) | $\bullet$ **(9)** | Không (0) | $\circ$ (3) |
| **Điểm Tầm quan trọng Tuyệt đối ($W_j = \sum d_i R_{ij}$)** | **Tổng $d_i = 38$** | **$256$** | **$171$** | **$94$** | **$130$** | **$131$** | **$116$** | **$116$** | **$134$** |
| **Trọng số Kỹ thuật Tương đối ($w_j$ tính theo %, với $\sum W_j = 1,148$)** | **Tổng = 100%** | **22.30%** | **14.90%** | **8.19%** | **11.32%** | **11.41%** | **10.10%** | **10.10%** | **11.67%** |
| **Xếp hạng Ưu tiên Kỹ thuật (Rank)** | **Hạng 1–8** | **Hạng 1** | **Hạng 2** | **Hạng 8** | **Hạng 5** | **Hạng 4** | **Hạng 6 (Đồng hạng)** | **Hạng 6 (Đồng hạng)** | **Hạng 3** |

### 5.4. Phân tích Ma trận Tương quan Mái nhà HoQ (*Roof Correlation & Trade-offs*)

Trên phần Mái nhà của HoQ, mối tương quan vật lý giữa các đặc tính kỹ thuật `EC-01..08` chỉ ra **3 cặp đồng thuận kỹ thuật mạnh (`++`)** và **3 cặp mâu thuẫn kỹ thuật (`-`)** cần giải quyết khi chọn phương án:

1. **Các cặp đồng thuận mạnh (`++` — Synergy):**

   * **`EC-01` (Tách kênh từ thông & mô-men)** $\leftrightarrow$ **`EC-02` (Vòng kín tốc độ) & `EC-03` (Mô-men giữ tại** $0\text{ rpm}$**):** Khi sử dụng cấu trúc điều khiển Vector tựa từ thông rotor (RFOC) kết hợp phản hồi từ Encoder thực tế, hệ thống vừa khử được độ trượt tốc độ ($e_{xl} \to 0$), vừa giữ được từ thông rotor $\psi_r = \text{const}$ ngay tại tốc độ $\omega = 0$ để sinh đủ mô-men giữ tải định mức trước khi nhả phanh cơ.

   * **`EC-04` (Quỹ đạo giới hạn** $a, \rho$**)** $\leftrightarrow$ **`EC-05` (Giảm áp lực xả hãm DC-Link) & `EC-06` (Giảm phát nhiệt** $S3$**):** Việc giới hạn gia tốc $\lvert a \rvert \le 0.5\text{ m/s}^2$ và độ giật $\lvert \rho \rvert \le 2.0\text{ m/s}^3$ bằng đường cong S-Curve giúp cắt bỏ các gai dòng điện quá độ lúc khởi động và lúc phanh, từ đó giảm tổn hao đồng $\Delta P_{Cu} \propto I^2 R$ trong chu kỳ $S3$ và giảm công suất đỉnh đổ về điện trở xả hãm $R_h$.

2. **Các cặp mâu thuẫn kỹ thuật (`-` — Engineering Trade-offs):**

   * **Mâu thuẫn 1 (`EC-04` Giới hạn gia tốc/độ giật** $\leftrightarrow$ **Thời gian đáp ứng nhanh của `EC-02`):** Nếu làm trơn quỹ đạo quá mức (chọn $a_{\max}$ và $\rho_{\max}$ quá nhỏ), thời gian tăng tốc sẽ kéo dài làm chậm chu kỳ bốc dỡ hàng; ngược lại nếu tăng tốc quá gắt để bám nhanh sẽ vi phạm $\rho_{\max} \le 2.0\text{ m/s}^3$ và làm lắc tải cáp $12\text{ m}$. *Giải pháp Trade-off:* Đặt bộ tạo quỹ đạo **S-Curve tối ưu thời gian** (ResearchGate, 2020 [R9-11]) ở phía trước mạch vòng tốc độ: bộ S-Curve đảm nhận làm mượt lượng đặt $\omega^*(t)$ đúng ngưỡng $a_{\max} = 0.5\text{ m/s}^2, \rho_{\max} = 2.0\text{ m/s}^3$, còn mạch vòng PI tốc độ bên trong được chỉnh định băng thông cao theo chuẩn *Tối ưu Đối xứng (SO)* để bám sát đường cong S-Curve mà không làm méo biên dạng.

   * **Mâu thuẫn 2 (`EC-02` / `EC-04` Chống lắc & độ chính xác cao** $\leftrightarrow$ **`EC-08` Độ đơn giản phần cứng & khả thi Simulink):** Nếu muốn dập tắt dao động chủ động khi có nhiễu ngoài như `CS-04` (Valtchev et al., 2024 [R9-04]) hoặc `CS-05` (Zheng et al., 2021 [R9-05]), hệ thống phải lắp thêm cảm biến góc lắc hoặc Camera Vision, làm tăng độ phức tạp phần cứng và giảm mạnh điểm `EC-08`. *Giải pháp Trade-off:* Đưa các cấu hình này vào Bước 5 & Bước 6 để đánh giá định lượng qua ma trận ICE.

## 6. TỔ HỢP HÌNH THÁI HỌC CÁC PHƯƠNG ÁN TRUYỀN ĐỘNG (BƯỚC 5 — CẦU NỐI TỪ HoQ SANG CÁC SOLUTION)

Từ **8 Đặc tính Kỹ thuật (`EC-01`** $\to$ **`EC-08`)** đã xác lập ở Bước 4 và **các mảnh ghép công nghệ** rút ra từ 9 Case Studies ở Bước 2, nhóm thực hiện lập **Bảng Hình thái học (*Morphological Box*)** để tổ hợp các thành phần phần cứng và điều khiển thành **4 Phương án Hệ truyền động Ứng viên (`Solution A`, `Solution B`, `Solution C`, `Solution D`)**:

| Phân hệ Chức năng (Theo `EC-01..08`) | **Solution A**  *(Truyền động Biến tần Vô hướng Vòng hở)* | **Solution B**  *(Truyền động Biến tần Vector Không cảm biến)* | **Solution C (Đề xuất Chọn)**  *(Động cơ KĐB + Vector FOC + Encoder Vòng kín đo thực tế)* | **Solution D**  *(Vector FOC + Encoder + Đóng vòng Góc lắc bằng Mờ / Thị giác Máy tính)* | 
| ----- | ----- | ----- | ----- | ----- | 
| **1. Động cơ truyền động (`EC-06`)** | Động cơ KĐB 3 pha rotor lồng sóc chế độ $S3$ | Động cơ KĐB 3 pha rotor lồng sóc chế độ $S3$ | **Động cơ KĐB 3 pha rotor lồng sóc chuyên dụng cầu trục chế độ** $S3$ ($CD = 40$%) | Động cơ KĐB 3 pha rotor lồng sóc chế độ $S3$ | 
| **2. Luật điều khiển Biến tần (`EC-01`, `EC-07`)** | Điều khiển vô hướng $U/f = \text{const}$ (Không tách kênh từ thông và mô-men) | Điều khiển **Sensorless Vector FOC** (Tách kênh $i_d, i_q$ dựa trên bộ quan sát ước lượng từ thông) | **Điều khiển Vector tựa từ thông rotor (RFOC) chuẩn 3 mạch vòng PI (**$i_{sd}, i_{sq}$ **theo MO;** $\omega$ **theo SO)** | Điều khiển Vector RFOC kết hợp bộ điều khiển thích nghi **Fuzzy / VUFAPID** | 
| **3. Thiết bị phản hồi vòng kín (`EC-02`, `EC-08`)** | **Không có Encoder** (Chạy vòng hở hoàn toàn) | **Không có Encoder** (Ước lượng tốc độ từ dòng/áp stator, suy giảm độ chính xác khi $f < 2\text{ Hz}$) | **Có gắn Encoder xung thực tế trên trục động cơ** (Vòng kín đo tốc độ & vị trí góc thực tế chính xác tuyệt đối) | Encoder trục động cơ **+** Cảm biến đo góc lệch cáp $\theta$ hoặc **Camera công nghiệp tốc độ cao** | 
| **4. Quy hoạch quỹ đạo & Chống lắc (`EC-04`)** | Bộ tạo dốc tuyến tính (**Linear Ramp** — gia tốc hình chữ nhật, $\rho \to \infty$ tại điểm gãy) | Bộ tạo quỹ đạo **S-Curve** giới hạn gia tốc & độ giật ($a_{\max}, \rho_{\max}$) | **Bộ tạo quỹ đạo S-Curve 7 đoạn giới hạn chặt** $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ **và** $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$ | Bộ tạo quỹ đạo + **Mạch vòng bù gia tốc chủ động theo góc lắc** $\Delta a(\theta, \dot{\theta})$ | 
| **5. Hãm tái sinh & Phối hợp phanh cơ (`EC-03`, `EC-05`)** | Braking Chopper + Điện trở $R_h$; đóng/mở phanh theo ngưỡng tần số ước chừng (dễ giật/trôi tải) | Braking Chopper + Điện trở $R_h$; mở phanh theo ước lượng dòng (kém tin cậy ở tốc độ $0\text{ rpm}$) | **Braking Chopper + Điện trở xả hãm** $R_h$ **+ Logic tạo mô-men giữ tại** $0\text{ rpm}$ **đồng bộ mở/khóa phanh cơ** | Braking Chopper + Điện trở xả hãm $R_h$ + Logic phanh cơ | 
| **6. Nguồn Case Study Tham chiếu Chính** | Cấu hình đối chứng cơ bản trong `CS-04` (Valtchev et al., 2024 [R9-04]) & `CS-09` (Yuantai VFD (Tham khảo, chưa xác minh bản gốc)) | Biến thể rút gọn cảm biến của hệ truyền động công nghiệp | **`CS-06` (Shevchenko KPI, 2024 [R9-06]) + `CS-07` (Catalogue Demag DR [R9-07]) + S-Curve (2020)** | `CS-04` (Valtchev et al., IEEE 2024 [R9-04]) & `CS-05` (Zheng et al., 2021 [R9-05]) | 

## 7. ĐÁNH GIÁ VÀ LỰA CHỌN PHƯƠNG ÁN CUỐI CÙNG THEO MA TRẬN ICE (BƯỚC 6)

### 7.1. Quy tắc Chấm điểm Ma trận ICE Kết nối Trực tiếp với Kết quả HoQ

Để lựa chọn phương án tối ưu nhất cho Khối 0 (`SOW-0.2`), cả 4 phương án (`Solution A`, `Solution B`, `Solution C`, `Solution D`) được đánh giá định lượng theo mô hình **ICE (*Impact – Confidence – Ease*)** trên thang điểm từ $1$ đến $10$ cho mỗi tiêu chí:

1. **Impact (**$I \in [1;\ 10]$ **— Mức độ tác động / Đáp ứng yêu cầu kỹ thuật):** Không chấm cảm tính mà được tính bằng **điểm trung bình có trọng số theo tỷ lệ** $w_j$ (%) **của 8 Đặc tính Kỹ thuật (`EC-01..08`) từ Ngôi nhà Chất lượng HoQ** (Mục 5.3). Phương án nào thỏa mãn trọn vẹn các đặc tính có trọng số cao nhất (`EC-01` chiếm 22.30%, `EC-02` chiếm 14.90%, `EC-08` chiếm 11.67%, `EC-05` chiếm 11.41%, `EC-04` chiếm 11.32%) sẽ đạt điểm *Impact* cao nhất.

2. **Confidence (**$C \in [1;\ 10]$ **— Độ tin cậy & Bằng chứng thực chứng):** Đánh giá dựa trên mức độ sẵn sàng công nghệ (**TRL**), sự đầy đủ của công thức toán học và bằng chứng kiểm nghiệm thành công trong các Case Studies / Catalogue công nghiệp (ví dụ: có đồ án mẫu `CS-06` và Catalogue thương mại `CS-07` chứng minh).

3. **Ease (**$E \in [1;\ 10]$ **— Độ dễ thực thi & Phù hợp ràng buộc SOW):** Đánh giá mức độ phù hợp với nguồn lực 6 thành viên của Nhóm 8.5-EMG, khả năng tính toán tổng hợp tham số tường minh (theo chuẩn MO/SO), sự sẵn có của các khối chuẩn trong thư viện MATLAB/Simulink và giới hạn $\le 2$ vòng lặp thiết kế (`QCD-C02`, `QCD-D01`).

4. **Điểm tổng hợp ICE:** Tính theo cả hai chỉ số chuẩn là **Trung bình cộng** $\text{ICE}_{\text{avg}} = (I + C + E)/3$ và **Tích số** $\text{ICE}_{\text{prod}} = I \times C \times E$ (thang tối đa $1,000\text{ điểm}$).

### 7.2. Bảng Phân tích & Chấm điểm ICE cho 4 Phương án Truyền động

| Phương án Ứng viên | Phân tích Ưu điểm & Hạn chế Kỹ thuật Đối chiếu với HoQ (`EC-01..08`) và SOW | Điểm **Impact ($I$)**  *(Theo HoQ)* | Điểm **Confidence ($C$)**  *(Theo Case Study)* | Điểm **Ease ($E$)**  *(Theo SOW)* | $\text{ICE}_{\text{avg}}$  *(Thang 10)* | $\text{ICE}_{\text{prod}}$  *($I \times C \times E$)* | Kết luận Xét duyệt | 
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
| **Solution A:**  Động cơ KĐB + Biến tần Vô hướng $U/f$ (Vòng hở, không Encoder) + Linear Ramp | • **Ưu điểm:** Cấu trúc đơn giản nhất, không cần cảm biến phản hồi, dễ nối dây.  • **Hạn chế chí mạng:**    1. Không tách kênh được từ thông và mô-men (`EC-01` kém); khi tải thay đổi từ $2,022\text{ kg}$ lên $14,244\text{ kg}$ ở tốc độ thấp $0.12\text{ m/s}$ và tốc độ bò $0.03\text{ m/s}$, độ trượt tốc độ vượt quá ngưỡng $e_{xl} \le 5$% (`PRD-PERM-02`).    2. Không tạo được mô-men giữ định mức tại tốc độ $0\text{ rpm}$ để phối hợp mở phanh cơ an toàn (`PRD-FUNC-04`).    3. Bộ tạo dốc tuyến tính *Linear Ramp* có độ giật $\rho \to \infty$ tại điểm gãy, gây lắc tải mạnh như đã chứng minh trong `CS-04` (Valtchev et al., 2024 [R9-04]). | $4.5 / 10$ | $6.0 / 10$ | $8.5 / 10$ | $6.33$ | $230$ | **LOẠI**  *(Trượt yêu cầu `PRD-PERM-02`, `PERM-03`, `FUNC-04`)* | 
| **Solution B:**  Động cơ KĐB + Biến tần Sensorless Vector (Ước lượng, không Encoder) + S-Curve | • **Ưu điểm:** Cải thiện khả năng điều khiển mô-men so với $U/f$ nhờ mô hình toán học tách kênh ước lượng; có bộ tạo quỹ đạo S-Curve giảm độ giật.  • **Hạn chế:**    1. Do không có Encoder đo tốc độ thực tế (`EC-02`, `EC-03`), bộ quan sát từ thông dựa trên sức điện động cảm ứng bị suy giảm độ chính xác nghiêm trọng ở vùng tốc độ gần $0\text{ rpm}$ (lúc khởi hành mở phanh cơ và lúc dừng khóa phanh cơ) và khi nhiệt độ cuộn dây làm thay đổi điện trở $R_1, R_2$ trong chu kỳ $S3$.    2. Khó cam kết chắc chắn sai số tốc độ xác lập $e_{xl} \le 5$% ở chế độ bò định vị $0.03\text{ m/s}$ khi kéo tải nặng $14.24\text{ tấn}$. | $7.0 / 10$ | $7.0 / 10$ | $7.5 / 10$ | $7.17$ | $368$ | **LOẠI**  *(Rủi ro cao ở vùng tốc độ* $0\text{ rpm}$ *và cấp tốc độ bò)* | 
| **Solution C:**  **Động cơ KĐB + Vector FOC + Encoder (Vòng kín đo thực tế)** + S-Curve + Điện trở xả hãm $R_h$ | • **Ưu điểm vượt trội (Đáp ứng trọn vẹn HoQ & SOW):**    1. **Đạt tuyệt đối `EC-01`, `EC-02`, `EC-03`, `EC-07`:** Nhờ có **Encoder xung đo tốc độ thực tế** kết hợp cấu trúc **Vector FOC 3 mạch vòng PI (dòng điện** $i_d, i_q$ **theo MO; tốc độ** $\omega$ **theo SO)**, hệ thống giữ từ thông rotor không đổi trên toàn dải tốc độ, sinh đủ từ 100% đến 150% mô-men giữ tại $0\text{ rpm}$ để mở phanh cơ êm ái (`PRD-FUNC-04`) và giữ sai số xác lập $e_{xl} \approx 0$% (nhỏ hơn rất nhiều so với ngưỡng $5$%) ngay cả ở tốc độ bò (`PRD-PERM-02`).    2. **Đạt tuyệt đối `EC-04`, `EC-05`, `EC-06`:** Bộ tạo quỹ đạo **S-Curve** khóa chặt $\lvert a \rvert \le 0.5\text{ m/s}^2, \lvert \rho \rvert \le 2.0\text{ m/s}^3$ (`PRD-PERM-03`); nhánh **Chopper + Điện trở xả** $R_h$ tiêu tán trọn vẹn năng lượng hãm tái sinh (`PRD-FUNC-03`).    3. **Confidence & Ease cao nhất:** Được bảo chứng trực tiếp bởi đồ án mẫu `CS-06` (Shevchenko KPI, 2024 [R9-06]) và chuẩn công nghiệp `CS-07` (Demag DR [R9-07]), có đầy đủ công thức tổng hợp giải tích để triển khai trên MATLAB/Simulink. | $9.5 / 10$ | $9.5 / 10$ | $9.0 / 10$ | $9.33$ | $812$ | **CHỐT CHỌN**  *(Đạt điểm ICE cao nhất — Vượt cổng `MCR`)* | 
| **Solution D:**  Động cơ KĐB + Vector FOC + Encoder + Đóng vòng Góc lắc bằng Fuzzy / Camera Vision | • **Ưu điểm:** Khả năng dập tắt dao động con lắc chủ động rất cao ngay cả khi chiều dài cáp thay đổi liên tục hoặc có nhiễu ngoại lực (`CS-04` Valtchev et al., 2024 [R9-04] và `CS-05` Zheng et al., 2021 [R9-05]).  • **Hạn chế trong khuôn khổ dự án:**    1. Đòi hỏi lắp đặt cảm biến góc lệch cáp $\theta$ hoặc Camera tốc độ cao xử lý ảnh biên cạnh — kém bền vững trong môi trường bụi bẩn trên cao độ dầm cầu trục nhà xưởng (`EC-08` thấp).    2. Việc thiết kế tập mờ co giãn VUFAPID không có công thức tổng hợp giải tích chuẩn hóa như PI-MO/SO, làm tăng nguy cơ vượt quá giới hạn $\le 2$ vòng lặp thiết kế trong `SOW` (`QCD-C02`). | $9.0 / 10$ | $6.5 / 10$ | $4.5 / 10$ | $6.67$ | $263$ | **LOẠI**  *(Điểm Ease thấp, vượt phạm vi cảm biến của SOW)* | 

> **Quyết định Kỹ thuật tại Cổng `MCR` (`SOW-0.2`):** Nhóm 8.5-EMG chính thức chốt lựa chọn **Solution C: Hệ truyền động Động cơ Không đồng bộ 3 pha rotor lồng sóc chế độ** $S3$ **+ Biến tần điều khiển Vector tựa từ thông rotor (FOC) + Cảm biến Encoder (Vòng kín đo thực tế)**, kết hợp **Bộ tạo quỹ đạo S-Curve giới hạn độ giật**, **Khối Logic 4 góc phần tư phối hợp phanh cơ điện từ** và **Bộ băm xung áp + Điện trở xả năng lượng hãm tái sinh ($R_h$)** (đạt $\text{ICE}_{\text{avg}} = 9.33/10$, $\text{ICE}_{\text{prod}} = 812/1000$, mức sẵn sàng công nghệ $\text{TRL } 2$ tại cổng `MCR`).

## 8. SƠ ĐỒ CẤU TRÚC HỆ TRUYỀN ĐỘNG TIÊU CHUẨN CHO PHƯƠNG ÁN ĐƯỢC CHỌN (SOLUTION C)

Để giải quyết triệt để nhu cầu về một **Sơ đồ hệ truyền động đúng tiêu chuẩn quốc tế** làm cơ sở cho cả báo cáo Khối 0 (`MCR`) và Tài liệu Mô tả Kiến trúc Hệ thống `SAD/ICD` ở Khối 2 (`SOW-2.1` — Cổng `PDR-EVT`), cấu trúc của **Solution C** được chuẩn hóa thành **2 sơ đồ chuẩn mực** dưới đây dựa trên tiêu chuẩn IEC 61800-2, IEC 61800-1, Catalogue Demag DR [R9-07] và Chương 3–5 của Đồ án Shevchenko (KPI, 2024) [R9-06]:

### 8.1. Sơ đồ Phân lớp Kiến trúc Hệ thống Truyền động Điện theo Tiêu chuẩn Quốc tế `IEC 61800-2` (PDS Architecture)

Theo tiêu chuẩn IEC 61800-2, một Hệ thống Truyền động Điện Điều chỉnh Tốc độ (**PDS — *Power Drive System***) tiêu chuẩn công nghiệp phải phân định rõ ranh giới giữa **Mô-đun truyền động cơ bản (BDM)**, **Mô-đun truyền động hoàn chỉnh (CDM)**, **Động cơ & Cảm biến** và **Thiết bị công tác được dẫn động (*Driven Equipment*)**, đồng thời tách bạch **Luồng công suất (nét liền đậm `═══►`)** với **Luồng tín hiệu điều khiển & phản hồi (nét đứt `---►`)**:

```
╔══════════════════════════════════════════════════════════════════════════════════════════════════════════════╗
║                        RANH GIỚI HỆ THỐNG TRUYỀN ĐỘNG ĐIỆN (PDS — THEO CHUẨN IEC 61800-2)                    ║
║                                                                                                              ║
║  ┌─────────────────────────────────────────────────────────────────────────┐                                 ║
║  │            MÔ-ĐUN TRUYỀN ĐỘNG HOÀN CHỈNH (CDM — Complete Drive Module)   │                                 ║
║  │                                                                         │                                 ║
║  │  [Nguồn lưới 3 Pha]                                                     │                                 ║
║  │   380V ±10%, 50Hz                                                       │                                 ║
║  │         ║                                                               │                                 ║
║  │         ▼                                                               │                                 ║
║  │  ┌──────────────┐     ┌──────────────────────────────────────────────┐  │      ┌───────────────────────┐  ║
║  │  │ Khí cụ Đóng  │     │    MÔ-ĐUN BIẾN ĐỔI CƠ BẢN (BDM — Inverter)   │  │      │   CỤM ĐỘNG CƠ & ĐO    │  ║
║  │  │ cắt & Bảo vệ │════►│  ┌──────────┐   ┌─────────┐   ┌───────────┐  │  │      │                       │  ║
║  │  │ (MCCB, MC,   │     │  │Chỉnh lưu │   │ DC-Link │   │ Nghịch lưu│  │3 Pha PWM│  ┌─────────────────┐  │  ║
║  │  │  Bộ lọc)     │     │  │ Cầu 3 pha╞══►│  Tụ C   ╞══►│  IGBT VSI ╞══╪═════════╪═►│ Động cơ KĐB 3~  │  │  ║
║  │  └──────────────┘     │  └──────────┘   └────╥────┘   └─────▲─────┘  │  │      │  │ Lồng sóc (S3)   │  │  ║
║  │                       │                      ║              │        │  │      │  └────────╥────────┘  │  ║
║  │                       │              ┌───────╨───────┐      │Xung    │  │      │           ║ Trục ĐC   │  ║
║  │  ┌──────────────┐     │              │Braking Chopper│      │SVPWM   │  │      │  ┌────────╨────────┐  │  ║
║  │  │ Điện trở xả  │     │              │  (IGBT Hãm)   │      │        │  │      │  │ Encoder Xung    │  │  ║
║  │  │ hãm tái sinh │◄════╪══════════════╡ (Góc II & IV) │      │        │  │      │  │ Đo ω thực tế    │  │  ║
║  │  │     (Rh)     │     │              └───────────────┘      │        │  │      │  └────────┬────────┘  │  ║
║  │  └──────────────┘     │                                     │        │  │      └───────────┼───────────┘  ║
║  │                       │  ┌──────────────────────────────────┴─────┐  │  │                  │              ║
║  │  [Lệnh Vận hành]      │  │     KHỐI ĐIỀU KHIỂN TRUNG TÂM (CU)     │  │  │                  │              ║
║  │  • Tiến / Lùi   ─────►│  │ • Khối Logic Trạng thái 4 Góc & Phanh  │  │  │  Phản hồi ω(t)   │              ║
║  │  • Chạy nhanh / Bò    │  │ • Bộ tạo quỹ đạo S-Curve (|a|,|ρ| max) │◄─┼──┼──────────────────┘              ║
║  │  • Dừng / E-Stop      │  │ • Mạch vòng Tốc độ (PI-SO) & Dòng (MO) │  │  │  (Vòng kín thực tế)             ║
║  │                       │  └───────────────────┬────────────────────┘  │  │                                 ║
║  └───────────────────────┴──────────────────────┼───────────────────────┘  │                                 ║
║                                                 │ Lệnh Đóng/Mở Phanh cơ    │                                 ║
╚═════════════════════════════════════════════════╪══════════════════════════╪═════════════════════════════════╝
                                                  │ (Đồng bộ mô-men 0 rpm)   ║ Mô-men cơ học M_đc, ω_đc
                                                  ▼                          ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                     THIẾT BỊ CÔNG TÁC ĐƯỢC DẪN ĐỘNG (DRIVEN EQUIPMENT — CƠ CẤU XE CON)                       │
│                                                                                                              │
│   ┌────────────────────────┐      ┌────────────────────────┐      ┌─────────────────────┐      ┌──────────┐  │
│   │ Phanh cơ Điện từ       │      │ Hộp giảm tốc 3 cấp     │      │ Bánh xe con d=0.25m │      │ Tải treo │  │
│   │ Thường đóng (Fail-safe)╞═════►│ & Khớp nối (η = 0.90)  ╞═════►│ Lăn ray (w0 = 0.015)╞═════►│ Cáp h=12m│  │
│   └────────────────────────┘      └────────────────────────┘      └─────────────────────┘      └──────────┘  │
│                                                                    (M_Σ = 14,244 kg; v_max = 0.12 m/s)       │
└──────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

```

### 8.2. Sơ đồ Cấu trúc Mạch vòng Điều khiển Vector FOC + Encoder + Quỹ đạo S-Curve (Chuẩn Simulink — Kế thừa `CS-06` Shevchenko 2024)

Đi sâu vào bên trong **Khối Điều khiển Trung tâm (CU)** của **Solution C**, cấu trúc điều khiển nhiều mạch vòng lồng nhau (*Cascaded Control Loops*) trên hệ tọa độ tựa theo từ thông rotor ($dq$) được thiết kế chuẩn hóa như sau để triển khai ở Khối 3 (`SOW-3.3`, `SOW-3.4`) và mô phỏng trên MATLAB/Simulink ở Khối 5 (`SOW-5.1`):

```
                      ┌──────────────────────────────────────────────────────────────┐
                      │         KHỐI LOGIC VẬN HÀNH & PHỐI HỢP PHANH (SOW-3.4)       │
[Lệnh Tiến/Lùi/Bò] ──►│ • Kiểm tra khóa chéo Tiến/Lùi (chỉ đảo chiều khi v = 0)      ├───► [Đóng/Mở Phanh Cơ]
                      │ • Tạo mô-men giữ tại 0 rpm trước khi mở phanh (PRD-FUNC-04) │
                      └──────────────────────────────┬───────────────────────────────┘
                                                     │ Lượng đặt tốc độ đích (±v_max hoặc ±v_creep)
                                                     ▼
                      ┌──────────────────────────────────────────────────────────────┐
                      │         BỘ TẠO QUỸ ĐẠO S-CURVE GIỚI HẠN ĐỘ GIẬT (SOW-3.3)    │
                      │ • Giới hạn đạo hàm gia tốc: |ρ(t)| = |da/dt| ≤ 2.0 m/s³      │
                      │ • Giới hạn gia tốc ngang:   |a(t)| = |dv/dt| ≤ 0.5 m/s²      │
                      └──────────────────────────────┬───────────────────────────────┘
                                                     │ Quỹ đạo tốc độ góc đặt mượt ω*(t)
                                                     ▼
                                                   ┌───┐   e_ω   ┌───────────────────┐  i_sq*
                                              ────►│ + ├────────►│ BỘ ĐIỀU KHIỂN PI  ├─────────┐
                                                 ─ └─┬┘         │ MẠCH VÒNG TỐC ĐỘ  │         │
                                                      │          │ (Tối ưu Đối xứng) │         ▼
                                                      │          └───────────────────┘       ┌───┐  e_iq  ┌──────────────┐  u_sq*
                                                      │                                      │ + ├───────►│ PI DÒNG i_sq ├───┐
                                                      │                                    ─ └─┬┘        │ (Tối ưu MO)  │   │
                                                      │                                         │         └──────────────┘   │
                                                      │          ┌───────────────────┐  i_sd* ┌───┐  e_id  ┌──────────────┐   │
                                      [Từ thông đặt] ─┼─────────►│ TÍNH DÒNG TỪ HÓA  ├───────►│ + ├───────►│ PI DÒNG i_sd ├──┐│
                                          Ψ_r*        │          │   i_sd* = Ψ_r*/Lm │      ─ └─┬┘        │ (Tối ưu MO)  │  ││
                                                      │          └───────────────────┘          │          └──────────────┘  ││
                                                      │                                         │                            ▼▼
                                                      │                                         │         ┌──────────────────────┐
                                                      │                                         │         │ BIẾN ĐỔI NGƯỢC PARK  │
                                                      │                                         │         │  (dq → αβ / abc) &   │
                                                      │                                         │         │  ĐIỀU CHẾ XUNG SVPWM │
                                                      │                                         │         └──────────┬───────────┘
                                                      │                                         │                    │ Xung kích IGBT
                                                      │                                         │                    ▼
                                                      │                                         │         ┌──────────────────────┐
                                                      │                                         │         │ BIẾN TẦN + CHOPPER   │
                                                      │                                         │         │ & ĐIỆN TRỞ XẢ HÃM Rh │
                                                      │                                         │         └──────────┬───────────┘
                                                      │                                         │                    ║ i_a, i_b, i_c
                                                      │                                         │         ┌──────────╨───────────┐
                                                      │                                         └─────────┤ BIẾN ĐỔI CLARKE/PARK │
                                                      │                                      i_sd, i_sq   │ (Đo dòng 3 pha + θ_e)│
                                                      │                                                   └──────────▲───────────┘
                                                      │                                                              │ Góc từ thông θ_e
                                                      │          ┌───────────────────┐         ┌─────────────────────┴───────────┐
                                                      └──────────┤   ENCODER XUNG    │◄════════╡ ĐỘNG CƠ KĐB 3 PHA CHẾ ĐỘ S3     │
                                                    ω(t) đo thực │ (Vòng kín thực tế)│  Trục   │ + HỘP SỐ + XE CON & TẢI (h=12m) │
                                                                 └───────────────────┘         └─────────────────────────────────┘

```

### 8.3. Bảng Truy xuất Khép kín từ Phương án Chốt (`Solution C`) sang Đầu việc các Khối Tiếp theo

Bảng dưới đây xác nhận **Solution C (`Động cơ KĐB + Vector FOC + Encoder — Vòng kín đo thực tế`)** giải quyết trọn vẹn toàn bộ yêu cầu của Cổng 1 (`MCR`) và sẵn sàng chuyển giao làm đầu vào cho Khối 1 đến Khối 5 theo `SOW-8.5EMG-TROLLEY-v1.1`:

| Thành phần trong Solution C | Đáp ứng Mã Yêu cầu PRD (WHATs) | Đáp ứng Mã Kỹ thuật HoQ (HOWs) | Lấp đầy Mã Tech Gap | Bàn giao sang Đầu việc SOW ở các Khối tiếp theo | 
| ----- | ----- | ----- | ----- | ----- | 
| **1. Động cơ KĐB 3 pha rotor lồng sóc chế độ** $S3$ ($CD = 40$%) **+ Hộp giảm tốc 3 cấp** | `PRD-PERM-01`, `PRD-PERM-04` | `EC-06` (10.10%) | `GAP-01` | • **Khối 1 (`SOW-1.2`):** Chốt ngưỡng công suất và nhiệt trong `SRS Baseline A`.  • **Khối 3 (`SOW-3.1` — Đặng Nguyên Bình):** Tính $F_c, M_{qđ}, J_{qđ}, P_{hd}$ và chọn mã động cơ thực tế với $k_{dt} \ge 1.20$ (SRS A.1) và kiểm tra quá tải $\lambda$ (kết quả: SEW DRN80M4 0.75 kW, QĐ-04). | 
| **2. Biến tần Vector FOC (RFOC) + Cảm biến Encoder vòng kín đo thực tế** | `PRD-FUNC-01`, `PRD-FUNC-02`, `PRD-PERM-02` | `EC-01` (22.30%), `EC-02` (14.90%), `EC-07` (10.10%) | `GAP-02`, `GAP-07` | • **Khối 2 (`SOW-2.1`, `SOW-2.2`):** Đưa vào kiến trúc `SAD/ICD` và bảng `BOM` 3 cấp.  • **Khối 3 (`SOW-3.3` — Trần Đỗ Khải):** Tính 5 tham số mạch thay thế chữ $\Gamma$ và tổng hợp bộ điều khiển PI dòng điện (MO) + PI tốc độ (SO). | 
| **3. Bộ tạo quỹ đạo S-Curve 7 đoạn giới hạn gia tốc & độ giật ($\lvert a \rvert \le 0.5\text{ m/s}^2, \lvert \rho \rvert \le 2.0\text{ m/s}^3$)** | `PRD-PERM-03`, `PRD-FUNC-02` | `EC-04` (11.32%), `EC-08` (11.67%) | `GAP-04`, `GAP-05` | • **Khối 3 (`SOW-3.3` — Trần Đỗ Khải):** Thiết kế khối tạo quỹ đạo S-Curve đầu vào.  • **Khối 5 (`SOW-5.1` — Phạm Văn Hưng):** Mô phỏng kiểm chứng biên dạng $v(t), a(t), \rho(t)$ và góc lắc tải cáp $h = 12\text{ m}$. | 
| **4. Bộ băm xung áp (*Braking Chopper*) + Điện trở xả năng lượng hãm tái sinh ($R_h$)** | `PRD-FUNC-03`, `PRD-FUNC-01` | `EC-05` (11.41%) | `GAP-06` | • **Khối 3 (`SOW-3.1`, `SOW-3.2` — Đặng Nguyên Bình):** Tính công suất hãm tái sinh ở góc phần tư II, IV và chọn thông số $\Omega / \text{W}$ của điện trở xả $R_h$. | 
| **5. Khối Logic Trạng thái 4 góc phần tư & Phối hợp đồng bộ Phanh cơ điện từ tại** $0\text{ rpm}$ | `PRD-FUNC-04`, `PRD-FUNC-01`, `PRD-FUNC-02` | `EC-03` (8.19%) | `GAP-03` | • **Khối 3 (`SOW-3.4` — Nguyễn Bá Hưng):** Thiết kế lưu đồ thuật toán tạo mô-men giữ trước khi mở phanh cơ, chuyển cấp tốc độ bò và khóa phanh khi $v = 0\text{ m/s}$. |

### 8.4. Thiết lập Cơ chế Kiểm soát (Pha C — Control trong DMAIC) & Sổ Đăng ký 5 Rủi ro Cốt lõi (`RRM`) tại Cổng `MCR`

Để khép kín hoàn chỉnh chu trình **5 pha `DMAIC` (*Define – Measure – Analyze – Improve/Kaizen – Control*)** định hướng tại `TIEN_DO.md` và đáp ứng điều kiện bắt buộc tại Cổng 1 (`MCR`) của `FLOW_REVIEW.md` (*"Ghi tối thiểu 5 rủi ro kỹ thuật / tiến độ vào sổ RRM"*), phương án được chọn (**Solution C**) thiết lập cơ chế kiểm soát vận hành – mô phỏng và bảng quản trị 5 rủi ro cốt lõi sau đây:

1. **Ba cơ chế bảo vệ & liên khóa vận hành cốt lõi trong phạm vi `FUNC` & `PERM` (Control Mechanisms):**
   * **Liên khóa đồng bộ Phanh cơ điện từ – Mô-men giữ tại $0\text{ rpm}$ (`PRD-FUNC-04`):** Bộ điều khiển chỉ xuất lệnh nhả phanh cơ sau khi mạch vòng dòng điện $i_{sd}, i_{sq}$ đã thiết lập đủ từ thông và mô-men giữ tải tại $\omega = 0$; khi dừng, phanh cơ khóa chặt trục ngay tại thời điểm $v(t) = 0\text{ m/s}$ trước khi ngắt dòng kích từ.
   * **Liên khóa khóa chéo Tiến/Lùi chống đảo chiều đột ngột (`PRD-FUNC-01` & TCVN 4244:2005 Mục 1.5.7.2.9):** Khối logic trạng thái (`SOW-3.4`) khóa chéo hai lệnh Tiến và Lùi, chỉ cho phép đảo chiều sau khi quỹ đạo S-Curve 7 đoạn đã đưa vận tốc xe con về $v(t) = 0\text{ m/s}$.
   * **Kiểm soát giới hạn động học chống lắc tải & giới hạn áp DC-Link (`PRD-PERM-03`, `PRD-FUNC-03`):** Bộ tạo quỹ đạo S-Curve 7 đoạn kẹp cứng $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$ ở đầu vào; mạch *Braking Chopper* + điện trở xả $R_h$ tự động băm xung xả năng lượng khi $U_{\text{dc}}$ vượt ngưỡng để giữ $U_{\text{dc}} < 780\text{ V DC}$.

2. **Sổ Đăng ký 5 Rủi ro Kỹ thuật & Tiến độ Cốt lõi (`RRM` Sơ bộ Đệ trình Cổng `MCR`):**

| Mã Rủi ro (`RRM ID`) | Mô tả Rủi ro Kỹ thuật / Tiến độ (Tại Khối 0 — `Pre-A`) | Nguyên nhân Gốc rễ (Root Cause) | Biện pháp Kiểm soát & Giảm thiểu trong Solution C (Mitigation & Control) | Chủ thể Kiểm soát (`R / A`) |
| :---: | :--- | :--- | :--- | :--- |
| **`RRM-01`** | **Lắc tải biên độ lớn khi khởi động và phanh dừng** với kiện hàng $Q = 12,222\text{ kg}$ treo trên cáp dài $h = 12\text{ m}$ ($\omega_p \approx 0.904\text{ rad/s}$). | Gia tốc biến thiên nhảy bậc ($\rho \to \infty$) nếu dùng dốc tuyến tính *Linear Ramp* hoặc điều khiển *Bang-Bang*. | Áp dụng **Bộ tạo quỹ đạo S-Curve 7 đoạn** khóa chặt $\lvert a(t) \rvert \le 0.5\text{ m/s}^2$ và $\lvert \rho(t) \rvert \le 2.0\text{ m/s}^3$; kiểm chứng góc lắc $\theta(t)$ trên Simulink (`SOW-3.3`, `SOW-5.1`). | Trần Đỗ Khải (*PE-Control*) / Nghiêm Trọng Đông (*SE*) |
| **`RRM-02`** | **Quá áp thanh cái một chiều (`DC-Link Overvoltage`)** gây ngắt lỗi biến tần khi hãm giảm tốc tổng khối lượng $M_\Sigma = 14,244\text{ kg}$ ở góc phần tư II & IV. | Động năng của khối tải trả ngược về tụ DC-bus nhưng bộ chỉnh lưu diode đầu vào không trả về lưới được. | Tính chọn và tích hợp **Bộ băm xung áp (*Braking Chopper*) + Điện trở xả hãm tái sinh $R_h$** đủ công suất đỉnh và công suất trung bình chu kỳ $S3$ (`SOW-3.1`, `SOW-3.2`). | Đặng Nguyên Bình (*PE-HW*) / Nghiêm Trọng Đông (*SE*) |
| **`RRM-03`** | **Trượt tốc độ, hụt mô-men hoặc giật/trôi xe con** khi mở phanh cơ ở $0\text{ rpm}$ và khi chạy cấp tốc độ bò định vị ($0.03\text{ m/s}$) dưới sự thay đổi tải gấp $7.04\text{ lần}$. | Sụt áp trên điện trở stator $R_1$ ở tần số thấp và sai số ước lượng nếu dùng biến tần vòng hở hoặc *Sensorless*. | Chốt cấu hình **Vector FOC (RFOC) có gắn Encoder xung thực tế** kết hợp **Khối Logic đồng bộ phanh cơ tại $0\text{ rpm}$** (`SOW-3.3`, `SOW-3.4`). | Trần Đỗ Khải & Nguyễn Bá Hưng / Nghiêm Trọng Đông |
| **`RRM-04`** | **Định cỡ sai công suất động cơ ($k_{dt} < 1.2$ gây quá nhiệt $S3$, hoặc $P_{đm} > 1.5\,P_{\max}$ gây lãng phí — `QCD-C01` theo QĐ-08)** do sao chép máy móc công suất của Case Study khác. | Không quy đổi lại theo vận tốc thực tế $v_{\max} = 0.12\text{ m/s}$ (chậm hơn $7.5\text{ lần}$ so với đồ án mẫu `CS-06`). | Tính toán độc lập lực cản $F_c$, mô-men đẳng trị nhiệt $M_{\text{đt}}$ ở chế độ $S3$ ($CD = 40$%) và kiểm soát biên kinh tế `QCD-C01` ($P_{đm} \le 1.5\,P_{\max} \approx 1.84\text{ kW}$, QĐ-08) cùng $k_{dt} \ge 1.20$ (SRS A.1) (`SOW-3.1`). | Đặng Nguyên Bình (*PE-HW*) / Nghiêm Trọng Đông (*SE*) |
| **`RRM-05`** | **Lệch giao diện tín hiệu/đơn vị hoặc sai số đạo hàm độ giật $\rho(t)$ khi tích hợp Simulink**, dẫn tới nguy cơ vượt quá giới hạn $\le 2$ vòng lặp thiết kế (`QCD-C02`). | Ba tiểu ban thiết kế rời rạc không khóa giao diện `ICD` ở Khối 2 hoặc chọn bước lấy mẫu $T_s$ quá thô ở Khối 4. | Khóa chặt tài liệu giao diện `SAD/ICD` tại cổng `PDR-EVT` (`SOW-2.1`), chuẩn hóa *Solver* / $T_s$ và ký xác nhận cấu hình tại cổng `TRR-EVT` (`SOW-4.1`, `SOW-4.2`). | Phạm Văn Hưng (*QE*) & Nghiêm Trọng Đông (*PM/SE*) |

