# BÁO CÁO BẢN TUYÊN BỐ VÀ PHẠM VI CÔNG VIỆC (STATEMENT OF WORK — SOW)

**Tên đề tài:** Thiết Kế Hệ Truyền Động Điện Cơ Cấu Di Chuyển Ngang Xe Con Cầu Trục ($x = 2$)  
**Mã tài liệu:** `SOW-8.5EMG-TROLLEY-v1.1` | **Trạng thái:** `Baseline Frozen (Đồng bộ PRD v3.1)`  
**Tài liệu đầu vào tham chiếu:** `PRD-8.5EMG-TROLLEY-v3.1 (Baseline Frozen)`  
**Nhóm thực hiện:** Nhóm 8.5-EMG (Đề $x = 2$ — STT 22: Nghiêm Trọng Đông)  
**Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh  
**Chuẩn tham chiếu:** [R2, §7.1.3.2, Bảng 7.1-2, tr.189–191 (PDF tr.207–209) & Phụ lục P, tr.313–315 (PDF tr.331–333)], Quy trình Kỹ thuật Hệ thống `EVLEP003_HBK` (v1.8.2), [R1, TCVN 4244:2005], [R4], [R5, Bài 4]

---

### BẢNG LỊCH SỬ PHIÊN BẢN (DOCUMENT REVISION HISTORY)

| Phiên bản | Ngày ban hành | Người thực hiện | Tóm tắt các nội dung thay đổi chính | Trạng thái |
| :---: | :---: | :--- | :--- | :---: |
| **`v1.0`** | 14/10/2026 | Nhóm 8.5-EMG | Khởi tạo bản Tuyên bố Phạm vi Công việc (SOW) ban đầu theo quy chuẩn NASA SE Handbook và lưu đồ dự án 6 Khối. | Khóa sơ bộ |
| **`v1.1`** | 22/10/2026 | Ban Kỹ thuật Hệ thống 8.5-EMG | **Đồng bộ toàn diện theo tài liệu PRD v3.1 sau kiểm toán kỹ thuật:**<br>• Cập nhật tài liệu đầu vào tham chiếu thành `PRD-8.5EMG-TROLLEY-v3.1 (Baseline Frozen)`.<br>• Xóa sạch 100% các liên kết tìm kiếm ngoài mạng không chính thống; thay thế bằng hệ thống trích dẫn nội bộ chuẩn xác `[Rx, §mục, tr.số (PDF tr.số)]`.<br>• **Đồng bộ thông số vật lý và công suất tính chọn:** Cập nhật suất cản lăn riêng $w_0 = 0.015$ (1.5%) [R1, §2.4.7.2.2] & [R9-10, tr.15] và hệ số bám dính ray $\varphi = 0.20$ [R5, Bài 4, tr.43].<br>• **Định danh minh bạch các chỉ tiêu chất lượng:** Xác lập rõ $e_{xl} \le 5\%$, $M_p \le 10\%$, $d = 0.25\text{ m}$, $m_{xc} = 1,800\text{ kg}$ là `[C] Giả định nhóm 8.5-EMG` cần kiểm chứng tại các khối WBS tương ứng. | **Cũ** |
| **`v1.2`** | 24/10/2026 | Ban Kỹ thuật Hệ thống 8.5-EMG | **Đồng bộ hóa 100% theo SRS Baseline A v1.2 và RTM/DVP v1.2:**<br>• Đồng bộ hóa chuẩn xác 8 yêu cầu kỹ thuật hệ thống (`4 FUNC + 4 PERM`) ánh xạ 1-1 với 8 yêu cầu PRD.<br>• Bổ sung cơ chế **Downstream Design Allocation** chuyển giao 8 thông số chi tiết ($M_p, e_{xl}, U_{\text{dc}}, \text{Chopper}, \Delta t_{\text{torque}}, M_{\text{hold}}, F_{\max}, \lambda_{\max}$) xuống Khối 2 và Khối 3.<br>• Chuẩn hóa SSoT: $F_{c.\text{đầy}} = 2,096\text{ N}$, $\eta = 0.90$, $P_{\text{tĩnh}} \approx 0.28\text{ kW}$, $F_{\max} = 9,218\text{ N} \approx 9.22\text{ kN}$, $k_{\text{bám}} \approx 1.52 \ge 1.20$.<br>• Chuẩn hóa 8 bài đo kiểm chứng cấp hệ thống `DVP-L0-01` $\to$ `DVP-L0-08`. | **Chính thức (Baseline Frozen)** |

---

## BẢNG GIẢI THÍCH TỪ VIẾT TẮT & THUẬT NGỮ (ACRONYMS & DEFINITIONS)

Tuân thủ Tiêu chí số 9 tại Phụ lục P của NASA Systems Engineering Handbook [R2, Phụ lục P, tr.314 (PDF tr.332)], bảng dưới đây định nghĩa tường minh toàn bộ các từ viết tắt được sử dụng xuyên suốt tài liệu:

| Từ viết tắt | Thuật ngữ Tiếng Anh | Giải thích Ý nghĩa Kỹ thuật trong Đồ án |
| :--- | :--- | :--- |
| **SOW** | *Statement of Work* | Bản tuyên bố phạm vi công việc quy định các gói nhiệm vụ, sản phẩm bàn giao và tiêu chuẩn hiệu suất mà nhóm kỹ sư cam kết thực hiện. |
| **PRD** | *Product Requirements Document* | Tài liệu yêu cầu sản phẩm xuất phát từ không gian bài toán (*Problem Space*), mô tả nhu cầu khách hàng, kịch bản ConOps và 6 nhóm yêu cầu sản phẩm. |
| **SRS** | *System Requirements Specification* | Bản đặc tả yêu cầu kỹ thuật hệ thống ở không gian giải pháp (*Solution Space*), làm cơ sở thiết kế kiến trúc và mạch vòng điều khiển. |
| **WBS** | *Work Breakdown Structure* | Cấu trúc phân rã công việc chia nhỏ toàn bộ dự án thành các gói công việc cụ thể theo từng khối kỹ thuật. |
| **RACI** | *Responsible – Accountable – Consulted – Informed* | Ma trận phân bổ trách nhiệm nhân sự cho từng gói công việc trong nhóm liên chức năng CFT 8.5-EMG. |
| **CDRL** | *Contract Data Requirements List* | Danh mục các hồ sơ, tài liệu và mô hình kỹ thuật bắt buộc phải bàn giao để nghiệm thu. |
| **QCD** | *Quality – Cost – Delivery* | Bộ ba tiêu chuẩn đánh giá hiệu suất hoàn thành công việc về Chất lượng kỹ thuật, Chi phí định cỡ và Tiến độ nộp bài. |
| **MCR** | *Mission Concept Review* | Cổng xét duyệt khái niệm nhiệm vụ tại Khối 0, đánh giá tính khả thi của PRD, SOW và lựa chọn phương án sơ bộ. |
| **SRR-EVT** | *System Requirements Review — Engineering Verification Test* | Cổng xét duyệt yêu cầu hệ thống tại Khối 1, thẩm định SRS Baseline A, sơ đồ biên, P-Diagram và kế hoạch DVP&R L0. |
| **PDR-EVT** | *Preliminary Design Review — EVT* | Cổng xét duyệt thiết kế sơ bộ tại Khối 2, đánh giá kiến trúc hệ thống SAD, danh mục BOM sơ bộ và phân tích lỗi DFMEA L1. |
| **CDR-EVT** | *Critical Design Review — EVT* | Cổng xét duyệt thiết kế chi tiết tại Khối 3, kiểm tra tính chọn công suất động cơ/biến tần, thiết kế mạch vòng điều khiển và logic vận hành. |
| **TRR-EVT** | *Test Readiness Review — EVT* | Cổng xét duyệt sẵn sàng thử nghiệm tại Khối 4, kiểm tra kịch bản kiểm thử mô phỏng và bộ dữ liệu tiêm nhiễu trên MATLAB/Simulink. |
| **SIR / SAR** | *System Integration Review / Acceptance Review* | Các cổng xét duyệt tích hợp hệ thống và nghiệm thu chấp thuận sản phẩm cuối cùng tại Khối 5. |
| **DFMEA** | *Design Failure Mode and Effects Analysis* | Phương pháp phân tích các dạng hư hỏng tiềm ẩn và tác động trong thiết kế hệ thống. |
| **DVP&R** | *Design Verification Plan and Report* | Kế hoạch và báo cáo kiểm chứng thiết kế, đối chiếu kết quả đo kiểm với tiêu chuẩn nghiệm thu. |
| **RTM** | *Requirements Traceability Matrix* | Ma trận truy xuất nguồn gốc yêu cầu hai chiều kết nối từ PRD $\to$ SOW $\to$ SRS $\to$ CDRL $\to$ DVP&R. |
| **FOC** | *Field Oriented Control* | Thuật toán điều khiển định hướng từ thông cho động cơ xoay chiều biến tần nhằm điều khiển độc lập mô-men và từ thông. |

---

## 1. PHÂN TÍCH CÔNG VIỆC (STEP 1: ANALYZE THE WORK)

Căn cứ Mục 7.1.3.2 và Bảng 7.1-2 (*Steps in the Requirements Development Process*) của NASA Systems Engineering Handbook [R2, §7.1.3.2, tr.189–191 (PDF tr.207–209)], Bước 1 của quá trình xây dựng SOW bao gồm: xác định phạm vi thực hiện và loại trừ (*Define Scope*), tổ chức SOW theo cấu trúc phân rã công việc (*Organize SOW*), viết các câu lệnh yêu cầu công việc (*Write SOW Requirements*) và ghi chú lý giải (*Document Rationale*).

### 1.1. Xác định Phạm vi Công việc & Chiến lược Tùy biến từ PRD sang SOW (Define Scope & Tailoring)

Tại tài liệu `PRD-8.5EMG-TROLLEY-v3.1 (Baseline Frozen)`, nhóm 8.5-EMG đã khảo sát và ghi nhận đầy đủ bức tranh tổng thể của sản phẩm xe con cầu trục công nghiệp thực tế bao gồm **6 nhóm yêu cầu** (`PRD-FUNC`, `PRD-PERM`, `PRD-SAFE`, `PRD-INTF`, `PRD-ENVI`, `PRD-RELI` với 19 mã yêu cầu). Khi chuyển sang tài liệu **SOW (Statement of Work)** để quy định gói công việc mà nhóm sinh viên trực tiếp thực hiện trong học phần, phạm vi công việc được **tùy biến tinh gọn (Tailoring)** dựa trên hai căn cứ:

1. **Giới hạn theo 6 yêu cầu bắt buộc của đề bài học phần [R3, tr.1]:**
   * Mô tả nguyên lý, công nghệ;
   * Xây dựng yêu cầu truyền động, cấu trúc hệ truyền động;
   * Tính chọn công suất động cơ;
   * Thiết kế các mạch vòng điều chỉnh;
   * Thiết kế logic hoạt động của hệ thống;
   * Mô phỏng kiểm chứng theo ít nhất một kịch bản làm việc.
2. **Giới hạn theo nhóm yêu cầu PRD đã thống nhất với Giảng viên hướng dẫn (TS. Nguyễn Duy Đỉnh):** Nhóm tập trung thực hiện phân tích, thiết kế, tính toán và mô phỏng kiểm chứng đối với **2 nhóm yêu cầu cốt lõi** trong PRD là **Nhóm 1 — Yêu cầu Chức năng Vận hành (`PRD-FUNC-01` $\to$ `PRD-FUNC-04`)** và **Nhóm 2 — Yêu cầu Hiệu năng Định lượng (`PRD-PERM-01` $\to$ `PRD-PERM-04`)**.

Bảng dưới đây xác lập ranh giới phân định rạch ròi giữa **Phạm vi thực hiện (In-Scope)** và **Phạm vi loại trừ (Out-of-Scope)** của Nhóm 8.5-EMG:

| Phân loại Ranh giới | Các Hạng mục & Nhóm Yêu cầu Cụ thể | Lý giải Kỹ thuật & Quản trị Dự án (Rationale) |
| :--- | :--- | :--- |
| **1. Phạm vi Thực hiện (*In-Scope*)** | • **Đối tượng thiết kế:** Hệ truyền động điện cơ cấu di chuyển ngang của Xe con cầu trục dầm đôi ($x = 2$).<br>• **6 Hạng mục công việc theo đề bài:**<br>  1. Mô tả nguyên lý hoạt động và công nghệ truyền động xe con cầu trục.<br>  2. Xây dựng bộ yêu cầu truyền động và thiết kế cấu trúc hệ truyền động.<br>  3. Phân tích phụ tải, quy đổi cơ học và tính chọn công suất động cơ, biến tần, điện trở xả hãm.<br>  4. Thiết kế các mạch vòng điều chỉnh (mạch vòng dòng điện/mô-men, mạch vòng tốc độ và bộ tạo quỹ đạo giới hạn gia tốc/độ giật S-curve).<br>  5. Thiết kế logic hoạt động của hệ thống theo các trạng thái vận hành trên 4 góc phần tư.<br>  6. Xây dựng mô hình trên MATLAB/Simulink và mô phỏng kiểm chứng theo kịch bản làm việc.<br>• **Nhóm yêu cầu PRD cam kết thực hiện (8/19 mã):**<br>  + Toàn bộ **Nhóm 1 — Chức năng vận hành (`PRD-FUNC-01` $\to$ `PRD-FUNC-04`)**: Vận hành 4 góc phần tư & đảo chiều Tiến/Lùi; Điều chỉnh tốc độ vô cấp & làm mềm quá trình tăng/giảm tốc; Hấp thụ và tiêu tán năng lượng hãm tái sinh; Phối hợp đồng bộ phanh cơ khí và mô-men điện.<br>  + Toàn bộ **Nhóm 2 — Hiệu năng định lượng (`PRD-PERM-01` $\to$ `PRD-PERM-04`)**: Đáp ứng tải trọng kéo ngang định mức ($M_{\Sigma} = 14,244\text{ kg}, w_0 = 0.015$); Đạt vận tốc định mức $0.12\text{ m/s}$ & độ chính xác điều khiển tốc độ ($e_{xl} \le 5\%, M_p \le 10\%$); Giới hạn gia tốc & độ giật chống lắc tải ($a_{\max} \le 0.5\text{ m/s}^2, \rho_{\max} \le 2.0\text{ m/s}^3$); Đáp ứng chế độ nhiệt ngắn hạn lặp lại $S3$ ($CD = 40\%, k_{dt} \ge 1.2$). | • Bám sát trọn vẹn yêu cầu đề bài gốc ($x = 2$) và thống nhất trực tiếp với Giảng viên hướng dẫn.<br>• Hai nhóm `PRD-FUNC` và `PRD-PERM` chứa toàn bộ các chỉ tiêu vật lý, động lực học, năng lượng và thuật toán điều khiển có thể tính toán lý thuyết và mô phỏng kiểm chứng chính xác trên phần mềm MATLAB/Simulink.<br>• Tập trung nguồn lực kỹ thuật của 6 thành viên trong 8 tuần để giải quyết triệt để bài toán chất lượng cao, tránh dàn trải hình thức. |
| **2. Phạm vi Loại trừ (*Out-of-Scope*)** | • **Loại trừ các cơ cấu ngoài ranh giới xe con:** Không thiết kế cơ cấu nâng hạ hàng và cơ cấu di chuyển dầm cầu.<br>• **Loại trừ 4 nhóm yêu cầu PRD phần cứng/thực địa:**<br>  - **Nhóm 3 — An toàn & Bảo vệ (`PRD-SAFE-01..04`):** Không gia công cơ khí đệm giảm chấn cao su/thủy lực, không lắp đặt công tắc hành trình vật lý, không chế tạo mạch rơ-le an toàn phần cứng (chỉ giữ làm ràng buộc logic an toàn mô phỏng).<br>  - **Nhóm 4 — Giao diện hệ thống (`PRD-INTF-01..03`):** Không chế tạo tay bấm HMI cầm tay vỏ nhựa, không mua sắm cáp dẹt sâu đo thực tế, không gia công phôi đúc bánh xe thép (chỉ mô hình hóa tín hiệu điều khiển và bánh xe $d = 0.25\text{ m}$).<br>  - **Nhóm 5 — Môi trường vận hành (`PRD-ENVI-01..02`):** Không thử nghiệm sấy nhiệt độ xưởng, không thí nghiệm phun nước kiểm tra cấp bảo vệ $\text{IP54/IP55}$ (được đáp ứng bằng việc chọn thiết bị thương mại có sẵn chứng chỉ IP).<br>  - **Nhóm 6 — Độ tin cậy & Bảo trì (`PRD-RELI-01..02`):** Không đo kiểm mỏi kim loại thực tế qua hàng chục nghìn chu kỳ (chỉ tính toán lý thuyết nhóm cơ cấu ISO M5 theo TCVN 4244 [R1, §2.1.1.3.5, tr.30]).<br>• **Loại trừ việc chế tạo phần cứng thật:** Không mua sắm thiết bị thực tế, không đấu nối tủ điện thật và không thử nghiệm tải thật trên nhà xưởng. | • Đồ án môn học là đồ án thiết kế kỹ thuật và mô phỏng kiểm chứng (*Engineering Design & Simulation*), không được cấp kinh phí và thời gian chế tạo mẫu thử công nghiệp.<br>• Việc loại trừ được tuyên bố minh bạch trong SOW để bảo vệ nhóm kỹ sư khỏi rủi ro quá tải phạm vi (*Scope Creep*), đồng thời thể hiện tư duy Kỹ thuật Hệ thống chuyên nghiệp theo chuẩn NASA [R2, §7.1.3.2]. |

---

### 1.2. Tổ chức SOW theo Cấu trúc Phân rã Công việc (WBS) Bám sát 6 Khối (`FLOW_REVIEW.md`)

Căn cứ lưu đồ dự án 6 Khối – 7 Cổng trong `FLOW_REVIEW.md` (quy trình `EVLEP003_HBK` v1.8.2 & NASA SE Handbook [R2, tr.190–191]), cấu trúc SOW được tổ chức thành **6 gói công việc lớn (WBS 0.0 $\to$ WBS 5.0)** tương ứng với 6 khối kỹ thuật:

| Gói Công việc (WBS) & Tên Khối Kỹ thuật | Mã WBS | Ánh xạ sang 6 Yêu cầu Đề bài & Lưu đồ 6 Khối | Đầu ra Kỹ thuật Cốt lõi & Cổng Xét duyệt |
| :--- | :---: | :--- | :--- |
| **Khối 0: Tiền khả thi (`Pre-A` — §4.2, §4.3, §5.1)** | **`WBS 0.0`** | • **Yêu cầu 1:** Mô tả nguyên lý hoạt động, công nghệ.<br>• Thực hiện các bước DMAIC: Define, Measure, Analyze. | Hồ sơ `PRD v3.1`, `SOW v1.1`, Báo cáo Case Study, Ma trận QFD/HoQ, chấm điểm ICE.<br>$\to$ **Cổng `MCR`** |
| **Khối 1: Yêu cầu Hệ thống (`EVT` — §5.2)** | **`WBS 1.0`** | • **Yêu cầu 2a:** Xây dựng yêu cầu truyền động.<br>• Phân rã yêu cầu sang Solution Space. | Hồ sơ `SRS Baseline A`, Sơ đồ biên (*Boundary Diagram*), Sơ đồ tham số (*P-Diagram*), ma trận `RTM` và `DVP&R L0`.<br>$\to$ **Cổng `SRR-EVT`** |
| **Khối 2: Kiến trúc Hệ thống (`EVT` — §5.3)** | **`WBS 2.0`** | • **Yêu cầu 2b:** Xây dựng cấu trúc hệ truyền động.<br>• Phân bổ kiến trúc phần lực và phần điều khiển. | Tài liệu Mô tả Kiến trúc Hệ thống (**SAD**), Tài liệu Kiểm soát Giao diện (**ICD**), danh mục BOM sơ bộ 3 cấp, phân tích `DFMEA L1`.<br>$\to$ **Cổng `PDR-EVT`** |
| **Khối 3: Thiết kế Chi tiết (`EVT` — §5.4)** | **`WBS 3.0`** | • **Yêu cầu 3:** Tính chọn công suất động cơ.<br>• **Yêu cầu 4:** Thiết kế các mạch vòng điều chỉnh.<br>• **Yêu cầu 5:** Thiết kế logic hoạt động của hệ thống. | Thuyết minh tính chọn công suất động cơ/biến tần/điện trở hãm ($F_{c.\text{đầy}} = 2,096\text{ N}, P_{\text{tĩnh}} \approx 0.28\text{ kW}, F_{\max} = 9,218\text{ N} \approx 9.22\text{ kN}, P_{\max} \approx 1.23\text{ kW}$), bản vẽ sơ đồ nguyên lý mạch động lực, SDD thiết kế mạch vòng FOC và bộ tạo quỹ đạo S-curve, lưu đồ FSM logic 4 góc phần tư.<br>$\to$ **Cổng `CDR-EVT`** |
| **Khối 4: Chuẩn bị Thử nghiệm (`EVT` — §5.5)** | **`WBS 4.0`** | • Chuẩn bị mô hình mô phỏng kiểm chứng.<br>• Thiết lập môi trường đo kiểm và tiêm nhiễu. | Mô hình khối mô phỏng trên MATLAB/Simulink, kịch bản thử nghiệm tiêm nhiễu tải trọng và sụt áp lưới.<br>$\to$ **Cổng `TRR-EVT`** |
| **Khối 5: Tích hợp, Kiểm chứng & Bàn giao (`EVT` — §5.6)** | **`WBS 5.0`** | • **Yêu cầu 6:** Mô phỏng kiểm chứng theo kịch bản.<br>• Tổng hợp đồ án và nghiệm thu chấp thuận. | Báo cáo kiểm chứng `DVP&R L0 Report`, tập đồ thị mô phỏng 4 góc phần tư, Thuyết minh Đồ án tổng hợp và Slide báo cáo bảo vệ.<br>$\to$ **Cổng `SIR-EVT` & `SAR-EVT`** |

---

### 1.3. Chi tiết Yêu cầu Công việc (`Write SOW Requirements`) & Ghi chú Lý giải (`Document Rationale`) theo 6 Khối

Tuân thủ Quy tắc vàng tại Phụ lục P của NASA Systems Engineering Handbook [R2, tr.313–315 (PDF tr.331–333)], toàn bộ 18 yêu cầu công việc cụ thể (`SOW-0.1` $\to$ `SOW-5.3`) được soạn thảo theo cấu trúc bắt buộc: **Chủ thể thực hiện (Ai) + phải (shall) + Hành động kỹ thuật cụ thể (Làm gì) + Đầu ra có thể kiểm chứng được (Sản phẩm nào)**:

#### Khối 0 — Tiền khả thi (`Pre-A` — §4.2, §4.3, §5.1) & Cổng `MCR`

| Mã WBS / ID | Chủ thể Thực hiện (R / A) | Nội dung Yêu cầu Công việc (*Shall Statement*) | Ghi chú Lý giải Kỹ thuật & Quản trị (*Rationale*) |
| :---: | :--- | :--- | :--- |
| **`SOW-0.1`** | • **R:** Nghiêm Trọng Đông (*PM/SE Lead*)<br>• **A:** Nghiêm Trọng Đông (*PM/SE Lead*) | **Nghiêm Trọng Đông (PM/SE Lead) phải (shall)** phân tích đề bài gốc ($x = 2$, STT 22), thiết lập ma trận phân công trách nhiệm RACI cho nhóm 6 thành viên, xây dựng cấu trúc phân rã công việc WBS 6 Khối và lập kế hoạch tiến độ tổng thể bám sát 2 mốc học phần. | Xác lập bộ máy quản trị dự án, phân định trách nhiệm cá nhân, ngăn ngừa sự chồng chéo hoặc đùn đẩy công việc trong suốt 8 tuần thực hiện đồ án. |
| **`SOW-0.2`** | • **R:** Đặng Nguyên Bình, Trần Đỗ Khải & Nguyễn Bá Hưng<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Tiểu ban Thiết kế (Bình, Khải, Bá Hưng) phải (shall)** khảo sát tối thiểu 3 hồ sơ công nghiệp thực tế từ các hãng sản xuất uy tín (Demag DR [R9-01], Sungdo, Yuantai) và 6 bài báo/đồ án khoa học chuyên ngành [R9-02, R9-04, R9-05, R9-06, R9-07, R9-10], xây dựng ma trận QFD / Ngôi nhà chất lượng (HoQ) chuyển dịch mong đợi người dùng thành 8 đặc tính kỹ thuật (`EC-01` $\to$ `EC-08`), thiết lập bảng hình thái học các phương án truyền động và áp dụng ma trận ICE để lựa chọn phương án tối ưu. | Thực hiện trực tiếp **Yêu cầu 1 trong đề bài (*"Mô tả nguyên lý hoạt động, công nghệ"* )**; khắc phục lỗi chọn phương án cảm tính, đảm bảo phương án chốt (Động cơ không đồng bộ + Biến tần VSI + Hãm tái sinh/điện trở + FOC + S-curve) có luận chứng khoa học vững chắc. |
| **`SOW-0.3`** | • **R:** Nguyễn Hải Trung (*Doc Lead*) & Nghiêm Trọng Đông (*PM/SE Lead*)<br>• **A:** TS. Nguyễn Duy Đỉnh (*GVHD*) | **Nguyễn Hải Trung (Doc Lead) và Nghiêm Trọng Đông (PM/SE Lead) phải (shall)** biên soạn, rà soát và đệ trình phê duyệt bộ đôi tài liệu nền tảng gồm Tài liệu Yêu cầu Sản phẩm (**`PRD-8.5EMG-TROLLEY-v3.1`**) và Bản Tuyên bố Phạm vi Công việc (**`SOW-8.5EMG-TROLLEY-v1.1`**), đảm bảo vượt qua Cổng xét duyệt **MCR**. | Đóng băng chính thức đầu vào (*Baseline D & M trong DMAIC*), tạo cơ sở pháp lý và kỹ thuật duy nhất để chuyển sang thiết kế hệ thống ở các khối sau. |

---

#### Khối 1 — Yêu cầu Hệ thống (`EVT` — §5.2) & Cổng `SRR-EVT`

| Mã WBS / ID | Chủ thể Thực hiện (R / A) | Nội dung Yêu cầu Công việc (*Shall Statement*) | Ghi chú Lý giải Kỹ thuật & Quản trị (*Rationale*) |
| :---: | :--- | :--- | :--- |
| **`SOW-1.1`** | • **R:** Nghiêm Trọng Đông (*SE Lead*) & Nguyễn Hải Trung (*Doc Lead*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Nghiêm Trọng Đông (SE Lead) và Nguyễn Hải Trung (Doc Lead) phải (shall)** thiết lập Sơ đồ Ranh giới Hệ thống (**Boundary Diagram**) xác định các luồng Năng lượng, Tín hiệu, Vật lý qua biên hệ thống, và xây dựng Sơ đồ Tham số (**P-Diagram theo Six Sigma**) phân định rõ Tín hiệu vào, Yếu tố nhiễu (Nhiễu tải trọng, Nhiễu sụt áp, Nhiễu ma sát ray), Yếu tố điều khiển, Đầu ra mong muốn và Trạng thái lỗi. | Thể hiện tư duy Kỹ thuật Hệ thống chuyên nghiệp, làm rõ các điều kiện biên và rào chắn vật lý tác động lên hệ truyền động xe con trước khi viết yêu cầu kỹ thuật. |
| **`SOW-1.2`** | • **R:** Nguyễn Hải Trung (*Doc Lead*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Nguyễn Hải Trung (Doc Lead) dưới sự chủ trì của Nghiêm Trọng Đông (SE Lead) phải (shall)** phân rã 8 yêu cầu cam kết từ PRD (`PRD-FUNC-01..04` và `PRD-PERM-01..04`) thành Bản Đặc tả Yêu cầu Kỹ thuật Hệ thống (**`SRS Baseline A`**) gồm đúng 8 yêu cầu kỹ thuật hệ thống (`4 FUNC + 4 PERM`) theo chuẩn ISO/IEC/IEEE 29148 với cấu trúc câu mệnh lệnh *"phải (shall)"* kèm metadata 8 cột và Bảng phân bổ thông số chuyển xuống các khối thiết kế chi tiết (Downstream Design Allocation cho 8 thông số). | Thực hiện trực tiếp **Yêu cầu 2a trong đề bài (*"Xây dựng yêu cầu truyền động"*)**; chuyển dịch bài toán từ ngôn ngữ người dùng (*Problem Space*) sang ngôn ngữ kỹ thuật định lượng (*Solution Space*). |
| **`SOW-1.3`** | • **R:** Phạm Văn Hưng (*QE-Simulation*) & Nghiêm Trọng Đông (*SE Lead*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Phạm Văn Hưng (QE-Simulation) và Nghiêm Trọng Đông (SE Lead) phải (shall)** thiết lập Ma trận Truy xuất Yêu cầu Hai chiều (**RTM**) phản ánh chuỗi ánh xạ xuôi và ngược hai chiều đầy đủ giữa `SRS Baseline A` với `PRD-FUNC` / `PRD-PERM`, đồng thời xây dựng Kế hoạch Kiểm chứng Cấp Hệ thống (**`DVP&R L0`**) quy định phương pháp kiểm chứng (*Analysis / Simulation*) và ngưỡng Pass/Fail cho từng yêu cầu. | Đáp ứng điều kiện qua cổng **SRR-EVT** trong `FLOW_REVIEW.md`, đảm bảo mọi yêu cầu `FUNC` và `PERM` đều có bài đo kiểm chứng tương ứng ở Khối 5. |

---

#### Khối 2 — Kiến trúc Hệ thống (`EVT` — §5.3) & Cổng `PDR-EVT`

| Mã WBS / ID | Chủ thể Thực hiện (R / A) | Nội dung Yêu cầu Công việc (*Shall Statement*) | Ghi chú Lý giải Kỹ thuật & Quản trị (*Rationale*) |
| :---: | :--- | :--- | :--- |
| **`SOW-2.1`** | • **R:** Nghiêm Trọng Đông (*SE Lead*), Đặng Nguyên Bình (*PE-HW*) & Trần Đỗ Khải (*PE-Control*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Tiểu ban Thiết kế (Đặng Nguyên Bình, Trần Đỗ Khải) dưới sự chủ trì của Nghiêm Trọng Đông (SE Lead) phải (shall)** thực hiện phân tích lựa chọn cấu hình (*Architecture Trade-off*) và lập Tài liệu Mô tả Kiến trúc Hệ thống (**SAD**) kèm Tài liệu Kiểm soát Giao diện (**ICD**) theo cấu trúc PDS của IEC 61800-2 [R4, tr.85–92] & [R5, Bài 4, tr.4–10], thể hiện rõ sự tách biệt và ghép nối giữa chuỗi công suất và chuỗi điều khiển. | Thực hiện trực tiếp **Yêu cầu 2b trong đề bài (*"Xây dựng cấu trúc hệ truyền động"*)**, khóa chặt các biến giao diện giữa 3 tiểu ban trước khi đi vào tính toán chi tiết ở Khối 3. |
| **`SOW-2.2`** | • **R:** Đặng Nguyên Bình (*PE-Hardware*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Đặng Nguyên Bình (PE-Hardware) phải (shall)** xây dựng Danh mục Thiết bị & Vật tư (**BOM**) sơ bộ 3 cấp (Cấp 1: Hệ truyền động xe con; Cấp 2: Phân hệ phần lực và Phân hệ điều khiển; Cấp 3: Các cụm thiết bị chính gồm Động cơ điện, Biến tần, Cụm xả hãm, Phanh điện từ, Cảm biến tốc độ và Khí cụ đóng cắt) làm cơ sở định cỡ tại Khối 3. | Chuẩn bị khung dữ liệu cho hồ sơ bàn giao *Danh mục Thiết bị & Vật tư* theo yêu cầu đề bài. |
| **`SOW-2.3`** | • **R:** Toàn bộ CFT 8.5-EMG (Đông & Văn Hưng chủ trì)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Nhóm 8.5-EMG phải (shall)** thực hiện Phân tích các kiểu lỗi thiết kế và tác động ở cấp hệ thống (**`DFMEA L1`**) đối với các chức năng thuộc nhóm `PRD-FUNC` và `PRD-PERM`, đề xuất biện pháp phòng ngừa trong thiết kế để hạ toàn bộ các rủi ro có mức ưu tiên hành động `AP = Cao` xuống mức `Trung bình` hoặc `Thấp` trước cổng **PDR-EVT**. | Đáp ứng tiêu chí qua cổng **PDR-EVT**, ngăn ngừa sớm các lỗi kiến trúc như thiếu nhánh xả năng lượng hãm tái sinh hoặc thiếu bộ giới hạn độ giật. |

---

#### Khối 3 — Thiết kế Chi tiết (`EVT` — §5.4) & Cổng `CDR-EVT`

| Mã WBS / ID | Chủ thể Thực hiện (R / A) | Nội dung Yêu cầu Công việc (*Shall Statement*) | Ghi chú Lý giải Kỹ thuật & Quản trị (*Rationale*) |
| :---: | :--- | :--- | :--- |
| **`SOW-3.1`** | • **R:** Đặng Nguyên Bình (*PE-Hardware*)<br>• **A:** Đặng Nguyên Bình & Nghiêm Trọng Đông | **Đặng Nguyên Bình (PE-Hardware) phải (shall)** thực hiện phân tích phụ tải xe con cầu trục sử dụng suất cản lăn riêng $w_0 = 0.015 \pm 0.003$ ($[0.012;\ 0.018]$) [R1, §2.4.7.2.2] & [R9-10, tr.15], hệ số bám ray $\varphi = 0.20$ [R5, Bài 4, tr.43] và hiệu suất truyền động $\eta = 0.90$, tính toán lực cản tĩnh $F_{c.\text{đầy}} = 2,096\text{ N} \pm 420\text{ N}$ ứng với tổng khối lượng đầy tải $M_\Sigma = 14,244\text{ kg}$ (chạy không tải khối lượng tĩnh $m_{\text{tĩnh}} = 2,022\text{ kg}$), quy đổi mô-men cản tĩnh ($P_{\text{tĩnh}} \approx 0.28\text{ kW}$), mô-men quán tính của hệ ($F_{qt} \approx 7,122\text{ N}, F_{\max} = 9,218\text{ N} \approx 9.22\text{ kN}, P_{\max} \approx 1.23\text{ kW}$) về trục động cơ, xây dựng biểu đồ phụ tải toàn chu trình và tính chọn công suất định mức của động cơ điện (chọn dải $1.5 \div 2.2\text{ kW}$), biến tần cùng điện trở xả hãm, kiểm nghiệm điều kiện quá tải ($\lambda_{\max} \ge 2.0$) và phát nhiệt ở chế độ $S3$ ($CD = 40\% \pm 2.0\%$, $k_{dt} \in [1.20;\ 1.50]$) dưới lưới $380\text{V} \pm 10.0\% / 50\text{Hz} \pm 2.0\%$. | Thực hiện trọn vẹn **Yêu cầu 3 trong đề bài (*"Tính chọn công suất động cơ"*)**; khắc phục triệt để lỗi phóng đại công suất do dùng $\mu = 0.20$ trong phiên bản cũ. |
| **`SOW-3.2`** | • **R:** Đặng Nguyên Bình (*PE-Hardware*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Đặng Nguyên Bình (PE-Hardware) phải (shall)** thiết kế bản vẽ sơ đồ nguyên lý mạch động lực của hệ truyền động và lập bảng tổng hợp mã hiệu, thông số kỹ thuật cùng hãng sản xuất của toàn bộ thiết bị đã chọn vào *Danh mục Thiết bị & Vật tư (BOM)* chính thức. | Tạo lập trực tiếp 2 hồ sơ bàn giao bắt buộc theo đề bài là *Hồ sơ Bản vẽ Kỹ thuật* và *Danh mục Thiết bị & Vật tư*. |
| **`SOW-3.3`** | • **R:** Trần Đỗ Khải (*PE-Control Loop*)<br>• **A:** Trần Đỗ Khải & Nghiêm Trọng Đông | **Trần Đỗ Khải (PE-Control Loop) phải (shall)** xác định bộ tham số mô hình toán học của động cơ đã chọn, thiết kế thuật toán quy hoạch quỹ đạo chuyển động S-curve giới hạn gia tốc ($a_{\max} \le 0.50\text{ m/s}^2$) và độ giật ($\rho_{\max} \le 2.00\text{ m/s}^3$) theo Tho et al. (2020) [R9-05], đồng thời thiết kế cấu trúc và tổng hợp tham số các bộ điều khiển cho mạch vòng dòng điện và mạch vòng tốc độ FOC đảm bảo sai lệch xác lập $e_{xl} \le 5.0\%$ và độ quá điều chỉnh $M_p \le 10.0\%$ ($v_{\text{peak}} \le 0.132\text{ m/s}$). | Thực hiện trực tiếp **Yêu cầu 4 trong đề bài (*"Thiết kế các mạch vòng điều chỉnh"*)** và hoàn thiện phần đặc tả thiết kế thuật toán điều khiển (*SDD*). |
| **`SOW-3.4`** | • **R:** Nguyễn Bá Hưng (*PE-Logic*)<br>• **A:** Nguyễn Bá Hưng & Nghiêm Trọng Đông | **Nguyễn Bá Hưng (PE-Logic) phải (shall)** thiết kế lưu đồ thuật toán và hàm logic điều khiển trình tự vận hành của hệ thống trên cả 4 góc phần tư (chờ, khởi động tạo mô-men giữ đồng bộ mở phanh cơ [R1, §2.4.5.5.2], tăng tốc, chạy xác lập, giảm tốc hãm tái sinh, đóng phanh cơ khi tốc độ về không và cấm đảo chiều khi $v \ne 0$ [R1, §1.5.7.2.9]) đáp ứng đầy đủ nhóm `PRD-FUNC-01` $\to$ `PRD-FUNC-04`. | Thực hiện trực tiếp **Yêu cầu 5 trong đề bài (*"Thiết kế logic hoạt động của hệ thống"*)** trong phạm vi nhóm yêu cầu Chức năng vận hành. |
| **`SOW-3.5`** | • **R:** Phạm Văn Hưng (*QE-Simulation*) & Nghiêm Trọng Đông (*SE Lead*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Phạm Văn Hưng (QE-Simulation) và Nghiêm Trọng Đông (SE Lead) phải (shall)** cập nhật phân tích lỗi `DFMEA` và kế hoạch kiểm thử `DVP&R` xuống cấp phân hệ, đồng thời lập bảng ánh xạ đối xứng **V-Model** đảm bảo tất cả các khối thiết kế thuộc phạm vi `FUNC` & `PERM` đều có phép thử mô phỏng tương ứng trước cổng **CDR-EVT**. | Đáp ứng điều kiện qua cổng **CDR-EVT**, hoàn thiện khung truy xuất khép kín giữa yêu cầu và kiểm chứng. |

---

#### Khối 4 — Chuẩn bị Thử nghiệm (`EVT` — §5.5) & Cổng `TRR-EVT`

| Mã WBS / ID | Chủ thể Thực hiện (R / A) | Nội dung Yêu cầu Công việc (*Shall Statement*) | Ghi chú Lý giải Kỹ thuật & Quản trị (*Rationale*) |
| :---: | :--- | :--- | :--- |
| **`SOW-4.1`** | • **R:** Phạm Văn Hưng (*QE-Simulation*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Phạm Văn Hưng (QE-Simulation) phải (shall)** xây dựng mô hình mô phỏng hoàn chỉnh hệ truyền động xe con trên MATLAB/Simulink bao gồm: khối nguồn lưới & chỉnh lưu, khối nghịch lưu IGBT và mạch xả năng lượng hãm, mô hình động cơ không đồng bộ 3 pha, mô hình cơ cấu cơ khí xe con mang tải con lắc đơn chiều dài $12\text{ m}$ [R9-02], phân hệ điều khiển véc-tơ FOC và khối logic điều khiển FSM. | Tạo lập môi trường thử nghiệm số tích hợp hoàn chỉnh để kiểm chứng toàn bộ các chỉ tiêu kỹ thuật đã thiết kế. |
| **`SOW-4.2`** | • **R:** Phạm Văn Hưng (*QE-Simulation*) & Trần Đỗ Khải (*PE-Control*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Phạm Văn Hưng (QE-Simulation) và Trần Đỗ Khải (PE-Control) phải (shall)** thiết lập kịch bản mô phỏng kiểm thử toàn diện theo chu trình làm việc ngắn hạn lặp lại $S3$ trên cả 4 góc phần tư, tích hợp các khối tiêm nhiễu đầu vào (nhiễu đầy tải $Q = 12,222\text{ kg}$, nhiễu chạy không tải $Q = 0$, dao động chiều dài cáp treo $l = 12\text{ m}$) trước cổng **TRR-EVT**. | Đảm bảo hệ thống được thử nghiệm trong điều kiện khắc nghiệt nhất theo đúng yêu cầu kiểm định kỹ thuật hệ thống. |

---

#### Khối 5 — Tích hợp, Mô phỏng Kiểm chứng & Bàn giao (`EVT` — §5.6) & Cổng `SIR-EVT` / `SAR-EVT`

| Mã WBS / ID | Chủ thể Thực hiện (R / A) | Nội dung Yêu cầu Công việc (*Shall Statement*) | Ghi chú Lý giải Kỹ thuật & Quản trị (*Rationale*) |
| :---: | :--- | :--- | :--- |
| **`SOW-5.1`** | • **R:** Phạm Văn Hưng (*QE-Simulation*) & Trần Đỗ Khải (*PE-Control*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Phạm Văn Hưng (QE-Simulation) và Trần Đỗ Khải (PE-Control) phải (shall)** thực hiện mô phỏng kiểm chứng mô hình trên MATLAB/Simulink, trích xuất đầy đủ các đồ thị thời gian: vận tốc $v(t)$, gia tốc $a(t)$, độ giật $\rho(t)$, mô-men điện từ $M_{đt}(t)$, mô-men cản $M_c(t)$, dòng điện stator $i_s(t)$, góc lắc tải $\theta(t)$, đối chiếu với ngưỡng nghiệm thu trong `DVP&R L0`. | Thực hiện trực tiếp **Yêu cầu 6 trong đề bài (*"Mô phỏng kiểm chứng theo ít nhất một kịch bản làm việc"*)**; chứng minh bằng số liệu định lượng rằng hệ thống đạt toàn bộ các chỉ tiêu kỹ thuật cam kết. |
| **`SOW-5.2`** | • **R:** Phạm Văn Hưng (*QE-Simulation*)<br>• **A:** Nghiêm Trọng Đông (*SE Lead*) | **Phạm Văn Hưng (QE-Simulation) phải (shall)** tổng hợp kết quả đo kiểm vào Báo cáo Kế hoạch & Kết quả Kiểm chứng Thiết kế Cấp Hệ thống (**`DVP&R Level 0 Report`**), xác nhận trạng thái Đạt (Pass) cho toàn bộ 8 bài đo kiểm chứng (`DVP-L0-01` $\to$ `DVP-L0-08`) thuộc phạm vi cam kết trước cổng **SIR-EVT**. | Cung cấp bằng chứng thực nghiệm số khép kín chuỗi kiểm định theo mô hình V-Model. |
| **`SOW-5.3`** | • **R:** Toàn bộ 6 thành viên CFT 8.5-EMG (Nguyễn Hải Trung chủ trì tổng hợp)<br>• **A:** Nghiêm Trọng Đông (*PM/SE Lead*) & TS. Nguyễn Duy Đỉnh (*GVHD*) | **Toàn bộ Nhóm 8.5-EMG dưới sự chủ trì của Nguyễn Hải Trung (Doc Lead) phải (shall)** đóng gói đầy đủ Hồ sơ bàn giao đồ án (Thuyết minh kỹ thuật, Bảng tính phụ tải, Danh mục BOM, Tập bản vẽ sơ đồ nguyên lý mạch động lực và Slide báo cáo bảo vệ), nộp nghiệm thu chính thức trước Cổng **SAR-EVT** và bảo vệ trước Hội đồng nghiệm thu học thuật. | Hoàn thành toàn diện nghĩa vụ bàn giao của đồ án môn học, đảm bảo đầy đủ cả 4 hồ sơ bắt buộc của đề bài. |

---

## 2. PHÂN TÍCH TIÊU CHUẨN HIỆU SUẤT (STEP 2: ANALYZE PERFORMANCE — MỤC TIÊU QCD ĐO LƯỜNG ĐƯỢC)

Theo Bước 2 trong Bảng 7.1-2 của NASA Systems Engineering Handbook [R2, tr.190], hệ thống tiêu chuẩn hiệu suất thực hiện hợp đồng đồ án được cụ thể hóa thành các chỉ số **QCD (Quality – Cost – Delivery)** đo lường được:

| Mã Chỉ số | Hạng mục Tiêu chuẩn Hiệu suất | Chỉ tiêu Đo lường Cụ thể & Ngưỡng Nghiệm thu (Target / Threshold) | Phương pháp Đo lường & Minh chứng Nghiệm thu |
| :---: | :--- | :--- | :--- |
| **`QCD-Q01`** | **Quality (Chất lượng Quản trị SE)** | **Độ bao phủ truy xuất yêu cầu & Kiểm chứng đạt $100\%$:**<br>• $100\%$ yêu cầu `SRS Baseline A` truy xuất được ngược về `PRD-FUNC` và `PRD-PERM`.<br>• $100\%$ yêu cầu `SRS` có bài đo kiểm chứng tương ứng trong `DVP&R L0`. | Kiểm tra ma trận `RTM` hai chiều và bảng ánh xạ V-Model tại cổng **SRR-EVT** và **CDR-EVT**; không có yêu cầu nào bị mồ côi (*No orphan requirements*). |
| **`QCD-Q02`** | **Quality (Chất lượng Tính chọn Phần lực)** | **Độ chính xác tính chọn công suất, kiểm nghiệm nhiệt và chống trượt:**<br>• Suất cản lăn riêng $w_0 = 0.015 \pm 0.003$ ($[0.012;\ 0.018]$) cho lực cản tĩnh $F_{c.\text{đầy}} = 2,096\text{ N} \pm 420\text{ N}$ ($[1.68;\ 2.52]\text{ kN}$) và $P_{\text{tĩnh}} \approx 0.28\text{ kW}$ (với $\eta = 0.90$).<br>• Lực kéo tăng tốc cực đại $F_{\max} = 9,218\text{ N} \approx 9.22\text{ kN}$ ($[8.80;\ 9.70]\text{ kN}$) cho $P_{\max} \approx 1.23\text{ kW}$.<br>• Công suất động cơ chọn dự trữ $k_{dt} \in [1.20;\ 1.50]$ ở chế độ $S3$ ($CD = 40\% \pm 2.0\%$, chu kỳ $10\text{ phút} \pm 30\text{ s}$).<br>• Kiểm tra điều kiện không bị trượt trơn bánh xe chủ động: $F_{\max} \le F_{\text{bám}} = 13,973\text{ N}$ ($k_{\text{bám}} \ge 1.20$, danh định $\approx 1.52$) với $\varphi = 0.20$ [R5, Bài 4, tr.43]. | Đối chiếu công thức trong file tính toán `CDRL-02` với Bảng phụ tải chu trình và kết quả mô phỏng dòng điện/phát nhiệt tại Khối 5. |
| **`QCD-Q03`** | **Quality (Chất lượng Điều khiển & Động học)** | **Chất lượng đáp ứng tốc độ, gia tốc và chống lắc tải:**<br>• Vận tốc xác lập: $v_{\max} = 0.12\text{ m/s} \pm 5.0\%$ ($[0.114;\ 0.126]\text{ m/s}$ hay $[6.84;\ 7.56]\text{ m/phút}$), sai lệch xác lập $e_{xl} \le 5.0\%$ ($+0\%$), độ quá điều chỉnh $M_p \le 10.0\%$ ($+0\%$, $v_{\text{peak}} \le 0.132\text{ m/s}$).<br>• Gia tốc ngang cực đại: $\lvert a(t) \rvert \le 0.50\text{ m/s}^2$ ($[0.45;\ 0.50]\text{ m/s}^2$).<br>• Độ giật cực đại: $\lvert \rho(t) \rvert \le 2.00\text{ m/s}^3$ ($[1.80;\ 2.00]\text{ m/s}^3$).<br>• Góc lắc danh nghĩa của con lắc cáp $h = 12.0\text{ m} \pm 0.1\text{ m}$: $\theta_0 \le 2.92^\circ$. | Trích xuất đồ thị mô phỏng $v(t)$, $a(t)$, $\rho(t)$, $\theta(t)$ trên MATLAB/Simulink trong báo cáo `DVP&R L0 Report` (`CDRL-05`). |
| **`QCD-Q04`** | **Quality (Chất lượng Logic Vận hành)** | **Tính toàn vẹn của logic vận hành 4 góc phần tư:**<br>• $0$ hiện tượng trôi tải hoặc giật phanh: mở phanh khi $M_{\text{hold}}(0\text{ rpm}) \in [100\%;\ 150\%] M_{\text{đm}}$ và đóng phanh tại $\lvert v \rvert \le 0.005\text{ m/s}$, độ trôi dừng xe $\Delta s \le \pm 10\text{ mm}$ (danh định không trôi $\Delta s = 0\text{ m}$).<br>• Khóa liên động cấm đảo chiều khi $\lvert v \rvert > 0.002\text{ m/s}$ [R1, §1.5.7.2.9] hoạt động chính xác.<br>• Mạch xả hãm tái sinh giữ điện áp DC-link $U_{\text{dc}}(t) \le 780\text{ V DC}$ (cận trên $+0\text{ V}$; băm $700\text{V} \pm 20\text{V}$, trip $800\text{V} \pm 10\text{V}$). | Kiểm tra bằng đồ thị trạng thái FSM và dạng sóng mô phỏng $U_{dc}(t)$ khi hãm dừng từ $v_{\max}$ về $0$. |
| **`QCD-C01`** | **Cost (Chi phí Định cỡ Thiết bị BOM)** | **Biên độ tối ưu kinh tế – kỹ thuật khi chọn thiết bị:**<br>• Công suất động cơ chọn không vượt quá $150\%$ công suất tính toán yêu cầu ($P_{đm} \le 2.2\text{ kW}$).<br>• Dải điện áp và dòng điện định mức của biến tần, contactor, aptomat khớp sát phụ tải tính toán, tránh lãng phí chi phí đầu tư. | Đối chiếu thông số trong *Danh mục Thiết bị & Vật tư (BOM)* (`CDRL-03`) với catalogue thực tế của các hãng sản xuất. |
| **`QCD-D01`** | **Delivery (Tiến độ Bàn giao Đồ án)** | **Tuân thủ $100\%$ các mốc tiến độ học phần và cổng xét duyệt:**<br>• Vượt qua Cổng **MCR** đúng tuần 3.<br>• Hoàn thành **Mốc 1 (Báo cáo sơ bộ)** đúng tuần 5.<br>• Hoàn thành nghiệm thu **Mốc 2 (Bảo vệ đồ án)** đúng tuần 8. | Biên bản xét duyệt các cổng kỹ thuật có chữ ký xác nhận của GVHD (TS. Nguyễn Duy Đỉnh). |

---

## 3. PHÂN TÍCH DỮ LIỆU & HỒ SƠ BÀN GIAO (STEP 3: ANALYZE DATA & DELIVERABLES)

Căn cứ Bước 3 trong Bảng 7.1-2 của NASA Systems Engineering Handbook [R2, tr.191], mục này xác lập danh mục tiêu chuẩn kỹ thuật áp dụng và danh mục các hồ sơ dữ liệu bàn giao (CDRL).

### 3.1. Hệ thống Tiêu chuẩn Kỹ thuật và Quy chuẩn Áp dụng (Applicable Standards)

1. **Tiêu chuẩn Quốc gia về Thiết bị nâng:**
   * **[R1] TCVN 4244:2005** — Thiết bị nâng: Thiết kế, chế tạo và kiểm tra kỹ thuật:
     - Phân nhóm chế độ làm việc cơ cấu di chuyển xe con: Nhóm **ISO M5 (FEM 2m)** theo cấp sử dụng $T0 \div T9$ và phổ tải $L1 \div L4$ [R1, §2.1.1.3, tr.28–30 (PDF tr.24–26)].
     - Yêu cầu phanh tự động thường đóng và hệ số an toàn phanh tĩnh $k_p \ge 1.1$ [R1, §1.5.3.3.1 & §1.5.3.3.3, tr.14–15 (PDF tr.10–11)].
     - Quy tắc chống tự khởi động lại ngẫu nhiên [R1, §1.5.4.10, tr.16 (PDF tr.12)].
     - Công tắc giới hạn hành trình [R1, §2.4.4.1.3, tr.91 (PDF tr.87)] và đệm giảm chấn [R1, §1.5.5.1.2, tr.17 (PDF tr.13)].
     - Gờ an toàn chống trật bánh (độ sụt $\le 3\text{ cm}$) [R1, §1.5.5.2.1, tr.18 (PDF tr.14)] và cảnh báo di chuyển [R1, §1.5.5.3, tr.18 (PDF tr.14)].
     - Quy tắc cấm đảo chiều đột ngột khi $v \ne 0$ [R1, §1.5.7.2.9, tr.21 (PDF tr.17)].
     - Phối hợp liên khóa phanh điện và phanh cơ [R1, §2.4.5.5.2, tr.94 (PDF tr.90)].
     - Công thức xác định lực cản di chuyển cơ cấu xe con [R1, §2.4.7.2.2, tr.99–101 (PDF tr.95–97)].
2. **Tiêu chuẩn & Giáo trình Quốc tế về Hệ Truyền động Điện:**
   * **[R4] Tiêu chuẩn VN và Quốc tế phục vụ Thiết kế TĐĐ** (TS. Nguyễn Duy Đỉnh):
     - Chế độ làm việc ngắn hạn lặp lại **S3** theo IEC 60034-1 [R4, tr.23 (PDF tr.23)].
     - Cấu trúc hệ truyền động xoay chiều biến tần PDS theo IEC 61800-2 [R4, tr.85–92 (PDF tr.85–92)].
     - Cấp bảo vệ vỏ thiết bị điện $\ge \text{IP54}$ theo IEC 60529 [R4, tr.16–17 (PDF tr.16–17)].
   * **[R5] Bài giảng Thiết kế Hệ truyền động điện** (PGS.TS. Bùi Quốc Khánh, TS. Nguyễn Duy Đỉnh):
     - Cấu trúc biến tần nguồn áp và động cơ không đồng bộ [R5, Bài 4, tr.4–10].
     - Chế độ làm việc S3, đồ thị tiếp điện $CD\%$ [R5, Bài 4, tr.18].
     - Phương trình chuyển động 4 góc phần tư, điều kiện bám dính bánh xe trên ray thép ($F_k \le \varphi \cdot G_{\text{bám}}$) [R5, Bài 4, tr.43–52].
3. **Tiêu chuẩn Quản trị Kỹ thuật Hệ thống & Công nghệ Tham chiếu:**
   * **[R2] NASA Systems Engineering Handbook** (NASA/SP-2007-6105 Rev 1): Quy trình quản trị yêu cầu, WBS, RACI, DVP&R, và 12 tiêu chí soát xét SOW theo Phụ lục P.
   * **[R9-01] Demag DR rope hoists catalogue** (EZDR Double-rail crab): Minh chứng cấu hình xe con dầm đôi tải nặng, phanh đĩa đệm từ, encoder xung và biến tần tích hợp điện trở hãm [R9-01, tr.4–13].
   * **[R9-02] Mita & Kanai (1979)**: Mô hình con lắc tải cầu trục [R9-02, tr.833].
   * **[R9-05] Tho et al. (2020)**: Quy hoạch quỹ đạo S-curve khống chế jerk chống lắc [R9-05, tr.1–3].
   * **[R9-10] Shevchenko (2024)**: Tính toán suất trở lực lăn $w_0$ và mô phỏng FOC xe con cầu trục [R9-10, tr.15].

---

### 3.2. Danh mục Hồ sơ và Sản phẩm Bàn giao (Deliverables & CDRL)

Bám sát các yêu cầu của đề bài học phần [R3, tr.1], nhóm 8.5-EMG cam kết bàn giao đầy đủ **5 gói sản phẩm kỹ thuật (CDRL-01 $\to$ CDRL-05)**:

| Mã CDRL | Tên Hồ sơ / Sản phẩm Bàn giao | Mô tả Chi tiết Nội dung & Cấu trúc Hồ sơ | Định dạng Bàn giao | Ánh xạ Mã WBS Thực hiện | Cổng Xét duyệt & Thời hạn Nộp | Nhân sự Phụ trách (R / A) |
| :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| **`CDRL-01`** | **Bản Thuyết minh Đồ án Tổng hợp** | • Thuyết minh kỹ thuật hoàn chỉnh gồm 5 chương: Tổng quan công nghệ xe con cầu trục; Yêu cầu và kiến trúc hệ truyền động; Tính chọn công suất động cơ, biến tần và cụm xả hãm; Thiết kế mạch vòng FOC, bộ tạo quỹ đạo S-curve và logic FSM 4 góc phần tư; Báo cáo kết quả mô phỏng kiểm chứng DVP&R L0.<br>• Tích hợp đầy đủ các sơ đồ kiến trúc, bảng phụ tải và đồ thị trích xuất từ Simulink. | `.docx` & `.pdf` *(Đóng quyển chuẩn A4)* | `SOW-0.1` $\to$ `SOW-5.3` (Toàn bộ WBS) | • Sơ bộ: **Tuần 5** (Mốc 1)<br>• Chính thức: **Tuần 8** (SAR-EVT) | • **R (Chủ trì):** Nguyễn Hải Trung (*Doc Lead*)<br>• **C:** Toàn bộ thành viên CFT<br>• **A (Phê duyệt):** Nghiêm Trọng Đông (*PM*) |
| **`CDRL-02`** | **File Tính toán & Kiểm nghiệm Thiết bị** | • Bảng tính chi tiết lưu lại các công thức phụ tải, quy đổi mô-men, quán tính và kiểm nghiệm nhiệt/quá tải động cơ theo chế độ ngắn hạn lặp lại $S3$ ($CD = 40\%$).<br>• Sử dụng suất cản lăn riêng $w_0 = 0.015$ (1.5%) [R1, §2.4.7.2.2] và kiểm tra điều kiện bám ray $\varphi = 0.20$ [R5, Bài 4, tr.43].<br>• Cho phép kiểm tra chéo công thức toán học và cập nhật linh hoạt tham số khi thay đổi tải trọng. | `.xlsx` *(Excel có công thức động)* | `SOW-3.1` | • Sơ bộ: `CDR-EVT`<br>• Chính thức: `SAR-EVT` | • **R (Thực hiện):** Đặng Nguyên Bình (*PE-HW*)<br>• **A (Phê duyệt):** Nghiêm Trọng Đông (*PM*) |
| **`CDRL-03`** | **Hồ sơ Bản vẽ Kỹ thuật & Danh mục BOM** | • Bản vẽ sơ đồ nguyên lý mạch động lực và mạch điều khiển hệ truyền động điện xe con.<br>• Danh mục Thiết bị & Vật tư (BOM) chi tiết 3 cấp: mã hiệu, thông số định mức, nhà sản xuất và số lượng của Động cơ, Biến tần, Điện trở hãm, Phanh điện từ, Cảm biến encoder xung và khí cụ đóng cắt bảo vệ. | • Bản vẽ: `.dwg` / `.pdf`<br>• BOM: `.xlsx` / `.pdf` | `SOW-2.2`, `SOW-3.2` | • Sơ bộ: `CDR-EVT`<br>• Chính thức: `SAR-EVT` | • **R (Thực hiện):** Đặng Nguyên Bình (*PE-HW*)<br>• **A (Phê duyệt):** Nghiêm Trọng Đông (*PM*) |
| **`CDRL-04`** | **Slide Báo cáo Bảo vệ Đồ án** | • Bộ slide thuyết trình tổng hợp cô đọng toàn bộ quá trình thực hiện đồ án từ Khối 0 đến Khối 5.<br>• Trình bày rõ: Rào chắn vật lý và bài toán đề bài ($x = 2$); Lựa chọn phương án theo QFD/HoQ/ICE; Kết quả tính chọn phần lực; Thuật toán điều khiển FOC và quỹ đạo S-curve; Kết quả mô phỏng kiểm chứng kịch bản chu trình $S3$ trên 4 góc phần tư. | `.pptx` & `.pdf` | `SOW-5.3` | • Báo cáo cổng: `MCR`, `SRR`, `PDR`, `CDR`<br>• Bảo vệ cuối kỳ: **Tuần 8** | • **R (Chủ trì):** Nguyễn Hải Trung & Nghiêm Trọng Đông<br>• **A (Báo cáo chính):** Toàn bộ CFT 8.5-EMG |
| **`CDRL-05`** | **Mô hình Mô phỏng & Kế hoạch DVP&R L0 Report** | • File mô hình mô phỏng hoàn chỉnh hệ truyền động xe con trên MATLAB/Simulink.<br>• Báo cáo Kế hoạch & Kết quả Kiểm chứng Thiết kế Cấp Hệ thống (`DVP&R Level 0 Report`) xác nhận trạng thái Pass cho 8 bài đo kiểm chứng (`DVP-L0-01` $\to$ `DVP-L0-08`, tương đương `DV-01` $\to$ `DV-08`).<br>• Bộ đồ thị xuất kết quả kiểm chứng: vận tốc $v(t)$, gia tốc $a(t)$, độ giật $\rho(t)$, mô-men điện từ & mô-men cản $M(t)$, dòng điện stator $i_s(t)$, góc lắc tải $\theta(t)$. | `.slx`, `.mat` / `.fig` *(MATLAB/Simulink)* & `.pdf` | `SOW-4.1`, `SOW-4.2`, `SOW-5.1`, `SOW-5.2` | • Sẵn sàng đo: `TRR-EVT`<br>• Nghiệm thu: `SIR-EVT` & `SAR-EVT` | • **R (Thực hiện):** Phạm Văn Hưng (*QE*), Trần Đỗ Khải & Nguyễn Bá Hưng<br>• **C (Kiểm tra):** Đặng Nguyên Bình (*PE-HW*)<br>• **A (Phê duyệt):** Nghiêm Trọng Đông (*PM*) |

---

## 4. ĐỐI CHIẾU CHECKLIST 12 TIÊU CHÍ SOÁT XÉT SOW (PHỤ LỤC P — NASA SE HANDBOOK)

Để đảm bảo tài liệu `SOW-8.5EMG-TROLLEY-v1.1` đủ điều kiện vượt qua cổng xét duyệt **MCR** và làm cơ sở vững chắc cho các khối tiếp theo, bảng dưới đây ghi nhận kết quả tự rà soát theo 12 tiêu chí của Phụ lục P ([R2, Phụ lục P, tr.313–315 (PDF tr.331–333)]):

| STT | Tiêu chí Soát xét theo Phụ lục P (NASA SE Handbook) | Trạng thái | Minh chứng Thực hiện trong Bản SOW Này |
| :-: | :--- | :---: | :--- |
| **1** | **Đúng mẫu câu giao việc (`Who shall do What`)** | **ĐẠT** | Toàn bộ 18 câu yêu cầu công việc (`SOW-0.1` $\to$ `SOW-5.3`) tại Mục 1.3 đều mở đầu bằng tên cá nhân/tiểu ban phụ trách kèm từ khóa bắt buộc *"phải (shall)"*. |
| **2** | **Câu đơn — Mỗi câu/mã định danh giải quyết 1 gói nhiệm vụ rõ ràng** | **ĐẠT** | Tách bạch từng nhiệm vụ độc lập cho từng vai trò (`PE-Hardware`, `PE-Control`, `PE-Logic`, `QE-Simulation`, `Doc Lead`, `PM/SE Lead`). |
| **3** | **Đoạn văn và bảng biểu mạch lạc theo chủ đề** | **ĐẠT** | Tổ chức phân tầng chặt chẽ theo 6 Khối công việc của lưu đồ `FLOW_REVIEW.md` (`Khối 0` $\to$ `Khối 5`). |
| **4** | **Đánh mã định danh duy nhất (Unique ID)** | **ĐẠT** | Mọi đầu việc đều có mã ID duy nhất (`SOW-0.1` $\to$ `SOW-5.3`), mọi chỉ tiêu hiệu suất có mã `QCD-Q01..D01`, mọi hồ sơ bàn giao có mã `CDRL-01..05`. |
| **5** | **Dùng thể chủ động (Active Voice)** | **ĐẠT** | Toàn bộ 18 câu lệnh giao việc đều dùng thể chủ động gắn với chủ thể chịu trách nhiệm (`R` và `A`), không dùng câu bị động vô chủ ngữ. |
| **6** | **Diễn đạt khẳng định (Positive Statement) & Tách rõ Out-of-Scope** | **ĐẠT** | Các yêu cầu trong bảng công việc đều là câu khẳng định; toàn bộ các hạng mục không thực hiện được tách riêng vào Mục 1.1 (*Out-of-Scope*) và dòng *Ghi chú loại trừ* ở cuối mỗi khối. |
| **7** | **Không trộn lẫn lời giải/công thức chi tiết vào câu lệnh SOW** | **ĐẠT** | Không chép các công thức tính chi tiết vào câu lệnh giao việc; chỉ dẫn chiếu tới mã yêu cầu `PRD-FUNC` và `PRD-PERM`. |
| **8** | **Không có lỗi chính tả & chuẩn hóa đồng bộ ký hiệu đơn vị SI** | **ĐẠT** | Thống nhất tuyệt đối ký hiệu độ giật $\rho_{\max} \le 2.0\text{ m/s}^3$, gia tốc $a_{\max} \le 0.5\text{ m/s}^2$, vận tốc $v_{\max} = 0.12\text{ m/s}$, tự trọng xe con $m_{xc} = 1,800\text{ kg}$, tổng khối lượng có tải $M_{\Sigma} = 14,244\text{ kg}$, suất cản lăn $w_0 = 0.015$, hệ số bám ray $\varphi = 0.20$. |
| **9** | **Giải thích đầy đủ các từ viết tắt (Acronyms)** | **ĐẠT** | Đã lập Bảng giải thích từ viết tắt ngay tại đầu tài liệu. |
| **10** | **Rõ số lượng, lịch nộp & cổng xét duyệt bàn giao** | **ĐẠT** | Quy định rõ các cổng xét duyệt (`MCR` $\to$ `SAR-EVT`) và 2 mốc cứng học phần tại Mục 2 (`QCD-D01`) và Mục 3.2. |
| **11** | **Quy định rõ cấu trúc nội dung của từng tài liệu bàn giao** | **ĐẠT** | Mục 3.2 mô tả chi tiết cấu trúc nội dung của cả 4 hồ sơ bắt buộc của đề bài (`CDRL-01` $\to$ `CDRL-04`) và hồ sơ mô phỏng (`CDRL-05`). |
| **12** | **Quy định rõ định dạng file điện tử (File Format)** | **ĐẠT** | Chỉ rõ định dạng `.docx`, `.pdf`, `.xlsx`, `.dwg`/`.pdf`, `.pptx`, `.slx` cho từng hồ sơ trong bảng CDRL. |
