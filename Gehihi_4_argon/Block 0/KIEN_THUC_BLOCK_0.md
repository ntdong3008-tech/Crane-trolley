# TỔNG HỢP KIẾN THỨC, TỪ KHÓA KỸ THUẬT HỆ THỐNG (SE) VÀ LUỒNG TƯ DUY THIẾT KẾ (KHỐI 0 → KHỐI 1)
**Đề tài:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Xe Con Cầu Trục ($x=2$) | **Nhóm:** 8.5-EMG | **GVHD:** TS. Nguyễn Duy Đỉnh

---

## PHẦN I. LUỒNG TƯ DUY CHO SINH VIÊN KHI TIẾP CẬN ĐỀ BÀI TỪ CON SỐ 0

Khi đứng trước tờ đề bài chỉ có 6 thông số thô ($Q = 12,222\text{ kg}$, $m_{nh} = 222\text{ kg}$, $h = 12\text{ m}$, $v_{\max} = 0.12\text{ m/s}$, $a_{\max} \le 0.5\text{ m/s}^2$, $\rho_{\max} \le 2\text{ m/s}^3$), luồng tư duy chuẩn của một Kỹ sư Hệ thống gồm **5 bước**:

### Bước 1: Hình dung vật lý & Khoanh vùng biên giới (Boundary Thinking)
* **Bóc tách 3 chuyển động của cầu trục dầm đôi (theo hệ trục $Oxyz$):**
  1. *Di chuyển dầm cầu (Bridge travel - trục $Ox$):* Cả dầm chính chạy dọc nhà xưởng.
  2. *Di chuyển xe con (Trolley travel - trục $Oy$):* Xe con chạy ngang trên ray đặt trên mặt dầm chính $\to$ **ĐÂY LÀ ĐỐI TƯỢNG THIẾT KẾ CỦA ĐỀ BÀI (In-Scope)**.
  3. *Nâng hạ hàng (Hoisting - trục $Oz$):* Tời cuốn/nhả cáp đưa móc câu lên xuống $\to$ **Nằm ngoài phạm vi thiết kế (Out-of-Scope)**, nhưng đóng vai trò là **tải trọng mang theo** ($Q + m_{nh}$) và **chiều dài dây cáp con lắc** ($h = 12\text{ m}$) gây nhiễu lắc tải khi xe con tăng/giảm tốc.

### Bước 2: Giải mã ý nghĩa vật lý & Lý giải (Rationale) của 6 con số đề bài ($x=2$)
| Mã số | Thông số đề bài | Giá trị ($x=2$) | Ý nghĩa vật lý & Lý giải kỹ thuật (Rationale) |
| :---: | :--- | :---: | :--- |
| **1** | **Tải trọng nâng định mức ($Q$)** | **$12,222\text{ kg}$** | Xác định cấp tải công nghiệp nặng ($\approx 12.22\text{ tấn}$, thuộc phân khúc chuẩn $12.5 \div 15\text{ tấn}$). Treo tải nặng trên cao đòi hỏi ưu tiên tuyệt đối về độ êm và an toàn chống rơi/văng tải. |
| **2** | **Khối lượng cơ cấu nâng hạ ($m_{nh}$)** | **$222\text{ kg}$** | Khối lượng cụm móc cẩu, puly và cáp treo. Khi xe con chạy ở chế độ "không tải" ($Q = 0$), hệ truyền động vẫn phải kéo khối lượng $m_{nh} = 222\text{ kg}$ này cộng với tự trọng xe con. |
| **3** | **Chiều cao nâng ($h$)** | **$12\text{ m}$** | Đóng vai trò là chiều dài dây treo cực đại của con lắc đơn ($l \le 12\text{ m}$), có tần số dao động riêng $\omega_0 = \sqrt{g/l} \approx 0.904\text{ rad/s}$ (chu kỳ lắc $T \approx 6.95\text{ s}$). Dùng để phân tích góc lắc tải $\theta$. |
| **4** | **Tốc độ di chuyển tối đa ($v_{\max}$)** | **$0.12\text{ m/s}$** | Tương đương $7.2\text{ m/phút}$. Phù hợp chuẩn công nghiệp (Demag/ABUS) cho xe con tải $>10\text{ tấn}$ di chuyển ngang trên dầm ngắn để công nhân căn chỉnh vị trí đặt tải chính xác. |
| **5** | **Gia tốc cực đại ($a_{\max}$)** | **$\le 0.5\text{ m/s}^2$** | Ràng buộc động học trọng yếu nhằm: (1) Giới hạn góc lắc tĩnh ban đầu của tải ($\theta_{\max} \approx a_{\max}/g \approx 2.9^\circ$); (2) Đảm bảo bánh xe thép không bị trượt quay (spin) trên ray thép. |
| **6** | **Độ giật cực đại ($\rho_{\max}$)** | **$\le 2\text{ m/s}^3$** | Đạo hàm của gia tốc theo thời gian ($\rho = \text{d}a/\text{d}t$). Tránh thay đổi lực kéo đột ngột gây va đập gãy răng hộp số cơ khí và kích thích dao động con lắc tần số cao. Bắt buộc dùng quỹ đạo **S-Curve**. |

### Bước 3: Truy ngược công thức vật lý (First-Principles) để tìm ra các "Thông số ẩn" cần Giả định
Muốn tính chọn được Động cơ và Biến tần, ta phải viết phương trình tính **Lực kéo ($F_k$)**, **Mô-men quy đổi ($M_{qđ}$)** và **Mô-men quán tính quy đổi ($J_{qđ}$)**:
$$F_k = F_{ms} + F_{qt} = \mu \cdot (Q + m_{nh} + m_{xc}) \cdot g + (Q + m_{nh} + m_{xc}) \cdot a$$
$$M_{qđ} = \frac{F_k \cdot d}{2 \cdot i \cdot \eta} \quad ; \quad \omega_{đc} = \frac{2 \cdot v \cdot i}{d}$$
Từ hai phương trình cơ bản này, sinh viên phát hiện ra **6 thông số ẩn bắt buộc phải thiết lập Giả định (Assumptions)** vì tờ đề bài không cho:
1. **Khối lượng bản thân xe con ($m_{xc}$):** Khung thép xe con + hộp số + động cơ + cụm tời đặt trên xe con (thường từ $1,500\text{ kg} \div 3,500\text{ kg}$ với cấp tải $12.5 \div 15\text{ tấn}$).
2. **Đường kính bánh xe di chuyển ($d$):** Thường chọn $d = 0.25\text{ m}$ ($250\text{ mm}$) hoặc $0.315\text{ m}$ theo catalogue.
3. **Hệ số cản chuyển động / ma sát quy đổi ($\mu$):** Xét ma sát lăn bánh xe + ma sát ổ trục + ma sát thành ray (hoặc hệ số bám trượt $\mu = 0.15 \div 0.2$).
4. **Hiệu suất truyền động cơ khí ($\eta$) và Tỷ số truyền hộp giảm tốc ($i$):** $\eta \approx 0.94 \div 0.96$; $i \approx 100 \div 150$ để hạ tốc độ động cơ ($\sim 960 \div 1450\text{ rpm}$) xuống tốc độ bánh xe ($\sim 9.17\text{ rpm}$).
5. **Nguồn điện lưới ($U_{grid}/f$):** Lưới công nghiệp 3 pha $380\text{V}/50\text{Hz} \pm 10\%$.
6. **Chế độ làm việc chuẩn máy trục:** Ngắn hạn lặp lại **S3** (hoặc S4), hệ số tiếp điện $CD\% = 25\% \div 40\%$ theo **TCVN 4244:2005**.

### Bước 4: Bộ 4 Công cụ tra cứu để bảo vệ các con số Giả định trước Hội đồng
1. **Catalogue công nghiệp (Industrial Benchmarking):** Tra datasheet xe con dầm đôi $12.5\text{T} \div 15\text{T}$ của *Demag, ABUS, Konecranes, KG Crane / HKTC*.
2. **Tiêu chuẩn kỹ thuật & Giáo trình:** *TCVN 4244:2005* (Thiết bị nâng), *IEC 60204-32* (An toàn điện máy nâng), *ISO 13850* (E-Stop), *IEC 61800-5-2* (STO biến tần), sách *Cơ sở truyền động điện* (Bùi Quốc Khánh).
3. **Case Study học thuật (Google Scholar):** Các bài báo nghiên cứu điều khiển chống lắc và tính toán thiết kế cơ khí cầu trục.
4. **Cơ chế quản lý TBR (To Be Resolved) / Assumptions trong SE:** Ghi rõ giá trị giả định kèm cột *Nguồn tham chiếu / Lý giải (Source/Rationale)* trong PRD.

---

## PHẦN II. GIẢI MÃ TOÀN BỘ TỪ KHÓA & PHƯƠNG PHÁP LUẬN CỦA GIẢNG VIÊN

### 1. Khái niệm cốt lõi: PRD vs. SOW vs. SRS
* **PRD (Product Requirements Document — Tài liệu Yêu cầu Sản phẩm):** Bản "khóa đầu bài của khách hàng" (Problem Space). Trả lời câu hỏi **WHAT & WHY**: Sản phẩm giải quyết vấn đề gì, chạy trong kịch bản vận hành (ConOps) nào, và phải đạt các yêu cầu **Chức năng (`FUNC`)** cùng **Hiệu năng (`PERM`)** nào để được khách hàng nghiệm thu.
* **SOW (Scope of Work / Statement of Work — Phạm vi Công việc):** Bản "hợp đồng giao việc cho nhóm kỹ sư". Trả lời câu hỏi **WORK & DELIVERABLES**: Để tạo ra sản phẩm trong PRD, nhóm kỹ sư sẽ thực hiện những gói công việc nào (WBS 4 giai đoạn), bàn giao hồ sơ gì (Thuyết minh, File tính, Bản vẽ, Simulink, BOM), không làm những gì (Loại trừ cơ cấu nâng hạ, kết cấu dầm, thi công tủ thật) và kiểm soát theo mục tiêu **QCD** nào.
  * *Lưu ý về nguồn gốc SOW:* Phạm vi giới hạn trong SOW không phải tự bịa tùy tiện, mà được suy xuất từ: (1) **Tờ đề bài gốc** (chỉ giao thiết kế truyền động xe con và 6 gạch đầu dòng yêu cầu), (2) **Ràng buộc môn học** (16 tuần, nghiệm thu bằng tính toán & mô phỏng Simulink), và (3) **Cấu trúc sản phẩm PBS** đã chốt.
* **SRS (System Requirements Specification — Đặc tả Yêu cầu Hệ thống):** Bản dịch từ PRD sang ngôn ngữ kỹ thuật thuần túy ở Khối 1 (Solution Space) bằng các câu lệnh định lượng nghiêm ngặt (*Shall statements*) để giao cho thiết kế kiến trúc và chi tiết.

### 2. Tinh gọn (Tailoring) PRD cho Đồ án Môn học: Chỉ tập trung vào `FUNC` và `PERM`
Vì đồ án nghiệm thu trên bản tính toán và mô phỏng MATLAB/Simulink (không chế tạo tủ điện vật lý ngoài xưởng), thầy hướng dẫn cắt bỏ các nhóm yêu cầu không thể kiểm chứng bằng mô phỏng (`ENVI` - nhiệt độ/độ ẩm/bụi IP54, `RELI` - độ tin cậy tuổi thọ), và quy toàn bộ yêu cầu PRD về **2 trụ cột**:
1. **`FUNC` (Functional Requirements — Yêu cầu Chức năng):**
   * Điều khiển chuyển động xe con 2 chiều (Tiến / Lùi), làm việc ở **4 góc phần tư** (chế độ động cơ khi tăng tốc/chạy đều và chế độ máy phát hãm tái sinh/động năng khi giảm tốc).
   * Điều chỉnh tốc độ linh hoạt (chạy tốc độ định mức và tốc độ bò định vị tải).
   * Thực thi đầy đủ **Logic vận hành & Liên khóa an toàn (Interlock & Safety Logic)**: Chuyển trạng thái (`STOP`, `READY`, `START/ACCEL`, `CONSTANT SPEED`, `DECEL`), phối hợp đóng/mở phanh điện từ khi động cơ đủ mô-men, khóa chéo thuận/nghịch, ngắt chuyển động khi chạm công tắc giới hạn hành trình (*Limit Switch*), dừng khẩn cấp (*E-Stop*) và ngắt bảo vệ khi quá dòng/quá tải/quá áp DC-bus.
2. **`PERM` (Performance Requirements — Yêu cầu Hiệu năng định lượng):**
   * **Hiệu năng tải trọng:** Kéo tải định mức $Q = 12,222\text{ kg}$, cơ cấu nâng $m_{nh} = 222\text{ kg}$ (cáp dài $h = 12\text{ m}$) và tự trọng xe con $m_{xc}$.
   * **Hiệu năng động học:** $v_{\max} = 0.12\text{ m/s}$, $a_{\max} \le 0.5\text{ m/s}^2$, $\rho_{\max} \le 2\text{ m/s}^3$.
   * **Hiệu năng năng lượng & Điều khiển:** Công suất động cơ $P_{đm} \ge P_{hd}$, mô-men mở máy $M_{kđ} \ge M_{\max\_yc}$; sai lệch tốc độ xác lập $e_{xl} \le 5\%$, độ quá điều chỉnh tốc độ $M_p \le 10\%$.

### 3. Chuỗi công cụ tư duy: `DMAIC` $\to$ `Case Study` $\to$ `Tech Gap` $\to$ `Kaizen` $\to$ `QCD / QFD / HoQ / ICE`

1. **[D - DEFINE]:** Định nghĩa bài toán Xe con cầu trục & Nguyên lý công nghệ 4 góc phần tư.
2. **[M - MEASURE]:** Lượng hóa yêu cầu đầu bài thành các chỉ số đo được (`FUNC` & `PERM`).
3. **[A - ANALYZE]:** Khảo sát Case Study thực tế $\to$ Phát hiện **TECH GAP** (Khoảng trống công nghệ) mà các Case Study cũ không đáp ứng được đề bài.
4. **[I - IMPROVE (KAIZEN)]:** Đề xuất giải pháp cải tiến để lấp Tech Gap:
   * Dùng **QFD / HoQ** chuyển hóa yêu cầu khách hàng (VOC) thành đặc tính kỹ thuật (CTQ).
   * Đưa ra 3 phương án (Solutions A, B, C) & chấm điểm bằng ma trận **ICE** (dựa trên **QCD**).
   * Chốt Baseline: **Solution C** (Động cơ KĐB + Biến tần FOC + Encoder + S-Curve + $R_h$).
5. **[C - CONTROL]:** Thiết lập tiêu chí kiểm soát chất lượng, logic bảo vệ & kế hoạch nghiệm thu mô phỏng (DVP&R).

* **Giải nghĩa chi tiết từng từ khóa trong chuỗi:**
  * **`DMAIC` (Define - Measure - Analyze - Improve - Control):** Khung xương sống 5 bước của Six Sigma dùng để trình bày mạch logic từ lúc nhận đề bài (Define, Measure), phân tích cái cũ (Analyze), cải tiến đưa ra cái mới (Improve/Kaizen) đến kiểm soát nghiệm thu (Control).
  * **`Tech Gap` (Khoảng trống công nghệ):** Là khoảng vênh giữa **Yêu cầu khắt khe của đề bài ($x=2$)** và **Khả năng đáp ứng thực tế của các Case Study sẵn có**. Cụ thể:
    1. *Tech Gap từ Case Study 1 (Mita & Kanai, 1979):* Dùng điều khiển tối ưu thời gian đóng ngắt gia tốc đột ngột (Bang-Bang) trên động cơ DC $\to$ Độ giật $\rho \to \infty$, **vi phạm ràng buộc $\rho_{\max} \le 2\text{ m/s}^3$** của đề bài.
    2. *Tech Gap từ Case Study 2 (Feto et al., 2025):* Tính toán cơ khí cho cầu trục $10\text{ tấn}$ nhưng chọn động cơ xe con tới $30\text{ kW}$ (sai lệch thực tế chuyển động ngang) và **thiếu hoàn toàn cấu trúc điều khiển biến tần vòng kín cũng như mạch xả hãm tái sinh**.
    3. *Tech Gap từ Truyền động cầu trục truyền thống ($V/f$ vòng hở):* Ở tốc độ thấp $v_{\max} = 0.12\text{ m/s}$ (và tốc độ bò), phương pháp $V/f$ bị sụt mô-men nghiêm trọng do rơi áp trên điện trở stator $R_s$, không kiểm soát được sai lệch tốc độ $\le 5\%$ khi tải thay đổi từ không tải ($222\text{ kg}$) lên đầy tải ($12,444\text{ kg}$).
  * **`Kaizen` (Cải tiến liên tục trong bước Improve):** Từ 3 Tech Gap trên, nhóm thực hiện 3 cải tiến kỹ thuật (Kaizen) tạo nên Solution C:
    1. *Kaizen 1:* Đưa **Bộ tạo quỹ đạo S-Curve 7 đoạn** vào đầu vào bộ điều khiển để giới hạn đồng thời $a \le 0.5\text{ m/s}^2$ và $\rho \le 2\text{ m/s}^3$.
    2. *Kaizen 2:* Tính chọn chuẩn xác lại công suất động cơ KĐB 3 pha theo công suất đẳng trị chu kỳ $S3$ và bổ sung **Mạch hãm động năng (Braking Chopper + Điện trở xả $R_h$)** trên DC-Bus.
    3. *Kaizen 3:* Áp dụng cấu trúc **Điều khiển Vector tựa từ thông rotor (FOC) vòng kín có Encoder** với 2 mạch vòng PI nối tầng (dòng điện $i_d, i_q$ tối ưu Module và tốc độ $\omega$ tối ưu Đối xứng).
  * **`QCD` (Quality - Cost - Delivery):** Bộ 3 mục tiêu quản trị dự án:
    * *Quality (Chất lượng):* Đạt $100\%$ chỉ tiêu `FUNC` và `PERM` ($a \le 0.5\text{ m/s}^2$, $\rho \le 2\text{ m/s}^3$, $e_{xl} \le 5\%$, $M_p \le 10\%$).
    * *Cost (Chi phí / Nguồn lực):* Tối ưu cấu hình phần cứng hợp lý và vừa sức thực hiện của nhóm 6 sinh viên.
    * *Delivery (Tiến độ):* Hoàn thành đúng hạn bảo vệ Giữa kỳ (tuần $10 \div 16$) và nộp thuyết minh Cuối kỳ.
  * **`QFD` (Quality Function Deployment) & `HoQ` (House of Quality - Ngôi nhà chất lượng):** Công cụ ma trận dịch từ **Tiếng nói khách hàng (VOC / WHATs trong PRD)** sang **Đặc tính kỹ thuật (Engineering Characteristics / HOWs)**, chỉ ra sự đánh đổi (Trade-off trên mái nhà HoQ, ví dụ: tăng gia tốc $a$ thì giảm thời gian di chuyển nhưng làm tăng góc lắc $\theta$ và công suất đỉnh $P_{\max}$) và xác định các thông số **CTQ (Critical-to-Quality)**.
  * **`ICE` (Impact - Confidence - Ease):** Công cụ chấm điểm lựa chọn phương án (Trade Study) giữa Solution A ($V/f$), Solution B (Sensorless Vector) và Solution C (FOC + Encoder):
    * *Impact (I):* Mức độ đáp ứng các chỉ tiêu chất lượng CTQ (mô-men ở tốc độ thấp $0.12\text{ m/s}$, độ bám S-Curve).
    * *Confidence (C):* Độ tin cậy thành công (nhờ mô hình toán FOC tường minh, có Case Study và đồ án mẫu kiểm chứng).
    * *Ease (E):* Độ thuận lợi khi xây dựng mô hình và chạy kiểm thử trên MATLAB/Simulink trong thời gian môn học (FOC có Encoder đo trực tiếp nên dễ hội tụ hơn việc thiết kế bộ quan sát phi tuyến của Sensorless ở vùng tốc độ gần $0$).

---

## PHẦN III. TỔNG HỢP NHẬN XÉT & BẮT LỖI BỘ TÀI LIỆU CŨ CỦA NHÓM

### 1. Đánh giá 3 bản Word `PRD .pdf` (`PRD_V1`, `PRD_V2_16/9`, `PRD_V3`)
* **Lỗi 1 — Dùng nhầm Template PRD của ngành Phần mềm/App:** `PRD_V1` và `V2` lấy cấu trúc PRD phần mềm nên đưa vào hàng loạt tính năng ngoài phạm vi (IoT, SCADA, Predictive Maintenance, bảo mật chống truy cập mạng, mở rộng đường ray nhà xưởng).
* **Lỗi 2 — Vi phạm ranh giới hệ thống (In-Scope vs. Out-of-Scope):** Liệt kê cả cơ cấu nâng hạ (động cơ nâng, tang cuốn, cáp thép, móc câu, giới hạn hành trình nâng/hạ) vào tính năng sản phẩm; lấy ví dụ tải $5\text{ tấn}$ lệch với đề bài $12,222\text{ kg}$.
* **Lỗi 3 — Cắt gọt quá đà ở `PRD_V3`:** Khi sang `V3`, nhóm xóa bỏ được các phần lan man của `V1/V2` nhưng lại xóa mất luôn bảng thông số kỹ thuật, bảng giả định, mã định danh yêu cầu và các chỉ số định lượng điều khiển ($e_{xl} \le 5\%, M_p \le 10\%$).
* **Lỗi 4 — Sai sót chế bản & công thức:** Công thức hiệu suất ở `V1` viết ngược ($\eta = P_{in}/P_{out}$ thay vì $P_{out}/P_{in}$); ký hiệu độ giật ở bảng `V2` ghi nhầm thành $a_{\max}$; thiếu đơn vị $\text{m/s}$ ở tốc độ $0.12$.

### 2. Đánh giá Slide `Mô tả nguyên lý công nghệ.pptx` & `Pitching 1_10_final.pptx`
* **Điểm mạnh rất đáng khen:**
  * Đã có tư duy trích dẫn số liệu tai nạn lao động cầu trục (BLS) để làm lý giải (*Rationale*) cho yêu cầu an toàn và chống lắc tải.
  * Đã định hình được bảng mã hóa `XC-001` $\to$ `XC-006`, khung SOW 4 góc phần tư kèm bộ tiêu chuẩn chuyên ngành (`TCVN 4244:2005`, `IEC 60204-32`, `ISO 13850`, `IEC 61800-5-2`), bảng rút trích bài học Case Study và bảng chấm điểm `ICE` cho 3 phương án.
* **Các lỗi cần sửa ngay theo góp ý của Giảng viên:**
  1. **Sơ đồ khối hệ truyền động (Slide 6 Pitching) quá sơ sài và không theo chuẩn:**
     * *Hiện trạng:* Chỉ vẽ 5 ô chữ nhật nối đơn giản (`Biến tần` $\to$ `Động cơ` $\to$ `Hộp giảm tốc` $\to$ `Bánh xe` và `Cảm biến`), không phân biệt luồng công suất và luồng tín hiệu.
     * *Cách sửa chuẩn IEC 61800 / SE:* Phải vẽ sơ đồ cấu trúc phân tầng gồm:
       - **Luồng công suất điện (Nét đậm/đôi):** Nguồn 3 pha $380\text{V}/50\text{Hz} \to \text{MCCB/Contactor} \to \text{Biến tần (Chỉnh lưu + DC-Link + Nghịch lưu IGBT)} \to \text{Động cơ KĐB 3 pha}$; kèm nhánh rẽ trên DC-Link vào **Bộ băm xung áp (Braking Chopper) + Điện trở xả hãm ($R_h$)**.
       - **Luồng cơ khí (Nét trục cơ học):** $\text{Trục động cơ (gắn Phanh điện từ)} \to \text{Khớp nối} \to \text{Hộp giảm tốc } (i, \eta) \to \text{Bánh xe } (d) \to \text{Khung xe con } (m_{xc}) + \text{Cơ cấu nâng } (m_{nh}) + \text{Tải treo lắc } (Q, h)$.
       - **Luồng điều khiển & Phản hồi (Nét mảnh/đứt):** $\text{Lệnh vận hành + Công tắc hành trình + Nút E-Stop (STO)} \to \text{Khối Logic & Tạo quỹ đạo S-Curve } (a \le 0.5\text{ m/s}^2, \rho \le 2\text{ m/s}^3) \to \text{Bộ điều khiển FOC (Vòng PI tốc độ } \omega + \text{Vòng PI dòng điện } i_d, i_q) \to \text{Khâu điều chế SVPWM}$; nhận phản hồi từ **Encoder ($\omega$)** và **Cảm biến dòng 3 pha ($i_{abc}$)**.
  2. **Bảng Case Study (Slide 5 Pitching) thiếu tính học thuật:** Cần ghi rõ tên tài liệu ứng với `[1], [2], [3], [4]`, bổ sung cột chỉ rõ **Tech Gap**, và thay toàn bộ từ ngữ đời thường ("dễ nổ biến tần", "quay rất nhanh") bằng thuật ngữ chuyên ngành Truyền động điện.
  3. **Bảng PRD (Slide 3 Pitching) mới chỉ có 6 thông số đề bài:** Cần gom đầy đủ thành 2 nhóm yêu cầu **`PERM`** và **`FUNC`** kèm bảng **Giả định kỹ thuật** (khai báo rõ tự trọng xe con $m_{xc}$, $d = 0.25\text{ m}$, $\mu = 0.2$, $\eta = 0.96$).