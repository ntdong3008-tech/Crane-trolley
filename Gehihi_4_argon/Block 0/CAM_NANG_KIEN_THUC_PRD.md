# CẨM NANG KIẾN THỨC & PHƯƠNG PHÁP VIẾT TÀI LIỆU YÊU CẦU SẢN PHẨM (PRD)
**Áp dụng cho Đồ án Hệ truyền động điện Cơ cấu Xe con Cầu trục (Nhóm 8.5-EMG — $x = 2$)**  
*Tài liệu tổng hợp theo chuẩn Kỹ thuật Hệ thống (NASA Systems Engineering Handbook, ISO/IEC/IEEE 29148) và Quy trình `EVLEP003_HBK`*

---

## I. ĐỊNH NGHĨA NGẮN GỌN: PRD LÀ GÌ?

Khi trình bày hoặc bảo vệ trước Hội đồng / Giảng viên hướng dẫn, cần nắm vững 3 ý cốt lõi:

1. **Bản chất (Nó là gì?):**
   PRD (*Product/Project Requirements Document* — Tài liệu Yêu cầu Sản phẩm/Dự án) là bản **"khóa đầu bài của khách hàng"**. Tài liệu này đứng ở góc nhìn của **Người dùng / Khách hàng / Bài toán thực tế (Problem Space)** để định nghĩa **WHAT & WHY**: Tại sao phải làm sản phẩm này, ai là người vận hành, sản phẩm hoạt động trong kịch bản nào (*ConOps*), phạm vi gồm những gì và phải đạt được những thông số/tiêu chí nghiệm thu nào.  
   *(Lưu ý: PRD tuyệt đối không đi sâu vào giải pháp thiết kế chi tiết hay công thức tính toán — phần "HOW" đó thuộc về SRS và Thiết kế kiến trúc/chi tiết).*

2. **Vai trò trong luồng dự án (`EVLEP003_HBK`):**
   * **Khối 0 (Tiền khả thi - Pre-A):** Khởi tạo **PRD dự thảo (Draft)** từ yêu cầu đầu bài (`RFQ · SOR · VOC` hoặc đề giao của giảng viên).
   * **Khối 1 (Yêu cầu hệ thống - EVT §5.2):** Bắt buộc **Khóa PRD (Frozen)** làm chuẩn tham chiếu bất biến trước khi đóng băng **SRS Baseline A**.
   * **Truy xuất nguồn gốc:** Mọi yêu cầu kỹ thuật trong SRS (`SRS → PRD`) và mọi kịch bản kiểm thử trong `DVP&R L0` / `RTM` đều phải truy xuất ngược về các mã yêu cầu trong PRD để đảm bảo **"làm đúng thứ khách hàng cần" (Validation)** trước khi **"làm cho đúng kỹ thuật" (Verification)**.

3. **Sự khác biệt cốt lõi giữa PRD và SRS:**

| Tiêu chí | PRD (Product Requirements Document) | SRS (System Requirements Specification) |
| :--- | :--- | :--- |
| **Góc nhìn** | Khách hàng, Người vận hành, Chủ đầu tư (*Problem Space*). | Kỹ sư Hệ thống, Kỹ sư Phần cứng / Điều khiển (*Solution Space*). |
| **Câu hỏi trả lời** | Khách hàng cần giải quyết bài toán gì? Vận hành ra sao? Tiêu chí nghiệm thu tổng thể là gì? | Hệ thống phải đạt các chỉ số kỹ thuật định lượng nào (dòng, áp, mô-men, băng thông, logic) để thỏa mãn PRD? |
| **Ví dụ (Đề $x=2$)** | Xe con di chuyển tải $12,222\text{ kg}$ êm ái, không gây lắc tải nguy hiểm, gia tốc $a \le 0.5\text{ m/s}^2$, độ giật $\rho \le 2\text{ m/s}^3$. | Bộ tạo quỹ đạo S-Curve giới hạn $\text{d}a/\text{d}t \le 2\text{ m/s}^3$; mạch vòng tốc độ FOC đạt sai lệch xác lập $e_{xl} \le 5\%$, quá điều chỉnh $M_p \le 10\%$. |

---

## II. NGUYÊN TẮC VIẾT PRD CHUẨN KỸ THUẬT HỆ THỐNG (NASA SE HANDBOOK)

Dựa trên *Mục 4.1 (Stakeholder Expectations Definition)*, *Mục 4.2 (Technical Requirements Definition)* và *Phụ lục C (How to Write a Good Requirement)* của NASA SE Handbook:

### 1. Quy trình 4 bước chuyển hóa thành PRD
1. **Xác định các bên liên quan (Stakeholders) & Mong đợi (Expectations):**
   * *Khách hàng / Chủ đầu tư:* Giảng viên hướng dẫn (TS. Nguyễn Duy Đỉnh) / Chủ nhà máy công nghiệp nặng.
   * *Người vận hành (Operator):* Công nhân điều khiển cầu trục dưới sàn nhà xưởng (qua tay bấm có dây hoặc Remote từ xa).
   * *Kỹ sư bảo trì & Cơ quan đăng kiểm an toàn:* Đòi hỏi tuân thủ nghiêm ngặt quy chuẩn an toàn thiết bị nâng Việt Nam (**TCVN 4244:2005**).
2. **Xây dựng Kịch bản vận hành (ConOps — Concept of Operations):**
   * Mô tả chu trình hoạt động thực tế của xe con ở chế độ ngắn hạn lặp lại (**S3**): `STOP / READY` $\to$ `Tăng tốc có tải` ($Q = 12,222\text{ kg} + m_{nh} = 222\text{ kg}$) $\to$ `Chạy ổn định` ($v = 0.12\text{ m/s}$) $\to$ `Giảm tốc & Dừng chính xác` $\to$ `Đảo chiều chạy không tải` ($m_{nh} = 222\text{ kg}$) $\to$ `Dừng khẩn cấp (E-Stop)` hoặc `Chạm công tắc hành trình (Limit Switch)`.
3. **Thiết lập Hệ thống Đo lường Kỹ thuật (Technical Measures):**
   * **MOEs (*Measures of Effectiveness*):** Thước đo hiệu quả tổng thể ở góc độ khách hàng (VD: Nâng cao năng suất bốc dỡ, triệt tiêu lắc tải gây tai nạn lao động, vận hành bền bỉ trong môi trường xưởng bụi/nóng).
   * **MOPs (*Measures of Performance*):** Thông số hiệu năng vật lý định lượng ($Q = 12,222\text{ kg}$, $v_{\max} = 0.12\text{ m/s}$, $a_{\max} \le 0.5\text{ m/s}^2$, $\rho_{\max} \le 2\text{ m/s}^3$).
   * **TPMs (*Technical Performance Measures*):** Các thông số kỹ thuật trọng yếu cần theo dõi sát qua các cổng xét duyệt (`MCR`, `SRR`, `PDR`, `CDR`) như: Sai lệch tốc độ xác lập ($e_{xl} \le 5\%$), Độ quá điều chỉnh ($M_p \le 10\%$), Công suất xả hãm tái sinh trên điện trở $R_h$.
4. **Phân loại đầy đủ các nhóm yêu cầu:**
   * Yêu cầu Chức năng (*Functional*), Hiệu năng (*Performance*), Giao diện (*Interface*), Môi trường & Vận hành (*Environmental & Operational*), Độ tin cậy (*Reliability*) và An toàn (*Safety*).

### 2. Quy tắc Ngữ pháp & "Editorial Checklist" (Phụ lục C — NASA SE)
* **Từ khóa pháp lý kỹ thuật:**
  * **`Shall` (Phải):** Yêu cầu bắt buộc phải thực hiện và phải được kiểm chứng (*Requirement*).
  * **`Will` (Sẽ):** Tuyên bố mục đích hoặc sự kiện hiển nhiên của môi trường/hệ thống ngoài (*Facts / Declaration of purpose*).
  * **`Should` (Nên):** Mục tiêu khuyến khích hướng tới (*Goal*).
  * *Tuyệt đối tránh:* Dùng từ "must" hoặc các từ định tính mơ hồ không đo kiểm được như *"nhanh chóng"*, *"tối ưu"*, *"bám sát tuyệt đối"*, *"v.v."*, *"khi cần thiết"*.
* **Nguyên tắc "WHAT, not HOW" (Free of Implementation):**
  * Yêu cầu trong PRD phải nêu **kết quả/ràng buộc cần đạt**, không áp đặt giải pháp mạch chi tiết (trừ khi khách hàng chỉ định thành Ràng buộc thiết kế — *Design Constraint*).
* **Kèm theo Lý giải (*Rationale*) và Quản lý Giả định (*Assumptions / TBR*):**
  * Mọi con số yêu cầu đều phải có cột **Rationale** giải thích tại sao cần ngưỡng đó.
  * Các thông số đề bài chưa cho sẵn nhưng bắt buộc phải có để tính toán (như tự trọng xe con $m_{xc}$, đường kính bánh xe $d$, hệ số ma sát $\mu$) phải được đưa vào bảng **Giả định (Assumptions) / TBR (To Be Resolved)** kèm theo nguồn trích dẫn uy tín (Catalogue hãng, TCVN 4244:2005).

---

## III. LUỒNG TƯ DUY 5 BƯỚC CHO SINH VIÊN KHI ĐỨNG TRƯỚC ĐỀ BÀI MỚI

Khi chỉ có 6 dòng thông số thô ($x=2$), hãy áp dụng 5 bước tư duy từ nguyên lý gốc (*First-Principles Thinking*):

### Bước 1: Hình dung vật lý & Khoanh vùng biên (Boundary Diagram)
* Cầu trục có 3 chuyển động ($Oxyz$): Di chuyển dầm cầu (*Bridge*), Di chuyển xe con (*Trolley*), và Nâng hạ móc câu (*Hoist*).
* **Khoanh vùng In-Scope:** Chỉ thiết kế hệ truyền động điện kéo **xe con chạy ngang trên ray dầm chính**.
* **Khoanh vùng Out-of-Scope:** Không thiết kế cơ cấu nâng hạ và dầm cầu. Chiều cao nâng $h = 12\text{ m}$ và khối lượng cụm móc $m_{nh} = 222\text{ kg}$ chỉ đóng vai trò là **tham số đầu vào/nhiễu** (tạo thành con lắc đơn chiều dài $l \le 12\text{ m}$ treo dưới xe con).

### Bước 2: Giải mã ý nghĩa vật lý (Rationale) của 6 con số đề bài ($x=2$)

| Thông số | Giá trị ($x=2$) | Ý nghĩa vật lý & Lý giải kỹ thuật (Rationale đưa vào PRD) |
| :--- | :---: | :--- |
| **Tải trọng định mức ($Q$)** | **$12,222\text{ kg}$** | Cấp tải công nghiệp nặng ($\approx 12.22\text{ tấn}$). Không được làm tròn thành $12,000\text{ kg}$. Đòi hỏi ưu tiên số 1 là an toàn và chống lắc tải. |
| **KL cơ cấu nâng ($m_{nh}$)** | **$222\text{ kg}$** | Khối lượng cụm móc cẩu và cáp treo. Khi chạy "không tải" ($Q=0$), xe con vẫn phải mang tải tĩnh tối thiểu này. |
| **Chiều cao nâng ($h$)** | **$12\text{ m}$** | Chiều dài dây cáp treo tải ($l \le 12\text{ m}$). Quyết định tần số dao động riêng của con lắc tải $\omega_p = \sqrt{g/l}$ khi xe con tăng/giảm tốc. |
| **Tốc độ tối đa ($v_{\max}$)** | **$0.12\text{ m/s}$** | Tương đương $7.2\text{ m/phút}$. Phù hợp chuẩn công nghiệp (Demag/ABUS) cho xe con $>10\text{ tấn}$ để người vận hành căn chỉnh vị trí đặt tải chính xác. |
| **Gia tốc cực đại ($a_{\max}$)** | **$\le 0.5\text{ m/s}^2$** | Giới hạn góc lắc ban đầu của tải ($\theta \approx a/g$) và ngăn hiện tượng trượt quay bánh xe thép trên ray thép. |
| **Độ giật cực đại ($\rho_{\max}$)** | **$\le 2\text{ m/s}^3$** | Đạo hàm của gia tốc ($\rho = \text{d}a/\text{d}t$). Ngăn sốc cơ khí lên hộp giảm tốc và ép hệ điều khiển phải làm mềm quỹ đạo tốc độ (S-Curve). |

### Bước 3: Truy ngược từ Công thức Vật lý để tìm các thông số "Ẩn" cần Giả định
Viết phương trình cơ học cơ bản để biết mình còn thiếu số nào:
1. **Lực kéo trên ray:** $F_{\text{kéo}} = (Q + m_{nh} + m_{xc}) \cdot (\mu \cdot g \pm a)$  
   $\to$ Phát hiện thiếu: **Khối lượng bản thân xe con ($m_{xc}$)** và **Hệ số cản chuyển động/ma sát ($\mu$)**.
2. **Mô-men và Tốc độ quy đổi về trục động cơ:** $M_{qđ} = \frac{F_{\text{kéo}} \cdot d}{2 \cdot i \cdot \eta}$ ; $n_{đc} = \frac{60 \cdot v \cdot i}{\pi \cdot d}$  
   $\to$ Phát hiện thiếu: **Đường kính bánh xe ($d$)**, **Hiệu suất truyền động cơ khí ($\eta$)**, **Tỷ số truyền ($i$)**.
3. **Nguồn và Chế độ nhiệt:** Công suất hiệu dụng đẳng trị $P_{hd}$ phụ thuộc vào chu kỳ làm việc.  
   $\to$ Phát hiện thiếu: **Nguồn lưới ($380\text{V}/50\text{Hz}$)**, **Chế độ làm việc ngắn hạn lặp lại ($S3$, $CD\% = 25\% \div 40\%$)**, **Nhiệt độ môi trường & Cấp bảo vệ IP**.

### Bước 4: Tra cứu từ 3 nguồn chuẩn (Benchmarking) để lấy số Giả định
1. **Catalogue hãng cầu trục (Demag, ABUS, Konecranes, KG Crane):** Tra cấp tải $12.5\text{ tấn} \div 15\text{ tấn}$ để lấy tự trọng xe con $m_{xc}$ ($\approx 1,500 \div 3,500\text{ kg}$), đường kính bánh xe $d = 0.25\text{ m}$, công suất động cơ tham chiếu ($1.5 \div 3.7\text{ kW}$).
2. **Tiêu chuẩn Quốc gia & Giáo trình:** Tra **TCVN 4244:2005** và sách *Cơ sở truyền động điện*, *Thiết bị nâng* để chốt $\mu = 0.15 \div 0.2$, $\eta = 0.96$, $k_{dt} = 1.2$, cấp bảo vệ $\ge \text{IP54}$.
3. **Case Studies (Bài báo khoa học):**
   * *Case Study 1 (Mita & Kanai, 1979):* Cơ sở lý thuyết cho bài toán điều khiển quỹ đạo tốc độ có ràng buộc gia tốc để triệt tiêu góc lắc dư ($< \pm 0.2^\circ$).
   * *Case Study 2 (Feto et al., 2025):* Tham khảo cấu hình chuỗi cơ khí (Động cơ $\to$ Khớp nối $\to$ Hộp số $\to$ Bánh xe) và quy trình kiểm nghiệm áp lực bánh xe.

### Bước 5: Đóng gói thành Cấu trúc 8 Mục của PRD (Frozen)

---

## IV. KHUNG CẤU TRÚC 8 MỤC CHUẨN CỦA BẢN PRD (DÙNG ĐỂ SOẠN THẢO CHÍNH THỨC)

| Mục | Tên phần trong PRD | Nội dung cốt lõi cần trình bày | Người phụ trách (CFT) |
| :---: | :--- | :--- | :--- |
| **1** | **Quản lý tài liệu & Phê duyệt** | Mã tài liệu, Phiên bản (`v3.0 - Frozen`), Lịch sử sửa đổi (`V1 -> V2 -> V3`), Bảng chữ ký RACI. | Nguyễn Hải Trung (*Doc Lead*) & Nghiêm Trọng Đông (*PM/SE*) |
| **2** | **Tổng quan & Mục tiêu sản phẩm** | Bối cảnh an toàn cầu trục (thống kê tai nạn lắc tải); mục tiêu thiết kế hệ truyền động xe con; định nghĩa MOEs / MOPs / TPMs. | Nghiêm Trọng Đông & Nguyễn Hải Trung |
| **3** | **Các bên liên quan & ConOps** | Danh sách Stakeholders; mô tả chu trình công nghệ 4 góc phần tư ở chế độ $S3$ (Tăng tốc, Chạy đều, Tốc độ bò định vị, Hãm dừng, E-Stop). | Nguyễn Bá Hưng (*PE-Logic*) & Nguyễn Hải Trung |
| **4** | **Phạm vi sản phẩm (Product Scope)** | Bảng phân định rạch ròi **In-Scope** (Phần lực + Phần điều khiển xe con) và **Out-of-Scope** (Cơ cấu nâng, dầm cầu, IoT, SCADA, dự toán thương mại). | Nghiêm Trọng Đông (*SE Lead*) |
| **5** | **Danh mục Yêu cầu Sản phẩm (`PRD-xx`)** | Bảng yêu cầu đánh mã định danh (`PRD-01` $\to$ `PRD-12`) chia theo nhóm: Thông số động học, Chức năng vận hành, An toàn & Bảo vệ, Môi trường. Có cột **Rationale** đi kèm. | Toàn bộ CFT (Bình, B.Hưng, Khải, Đông, Trung) |
| **6** | **Giả định Kỹ thuật & Ràng buộc** | Bảng chốt các thông số giả định có trích dẫn nguồn: $m_{xc}$, $d = 0.25\text{ m}$, $\mu = 0.2$, $\eta = 0.96$, $k_{dt} = 1.2$, nguồn $380\text{V} \pm 10\%$, chế độ $S3$. | Đặng Nguyên Bình (*PE-HW*) & Trần Đỗ Khải (*PE-Control*) |
| **7** | **Tiêu chí Nghiệm thu (Acceptance Criteria)** | Các ngưỡng định lượng để nghiệm thu: $P_{đm} \ge P_{hd}$, $M_{kđ} \ge M_{\max}$, $a \le 0.5\text{ m/s}^2$, $\rho \le 2\text{ m/s}^3$, $e_{xl} \le 5\%$, $M_p \le 10\%$, dừng E-Stop $\le 2\text{s}$. | Phạm Văn Hưng (*QE-Simulation*) |
| **8** | **Ma trận Truy xuất Nguồn gốc Đầu vào** | Bảng ánh xạ từ Đề bài gốc ($x=2$) / Tiêu chuẩn `TCVN 4244:2005` / Case Study $\to$ Mã yêu cầu `PRD-xx`. | Nguyễn Hải Trung (*Doc Lead*) |

---

## V. CHECKLIST RÀ SOÁT LỖI TRƯỚC KHI ĐÓNG BĂNG PRD (RÚT RA TỪ BẢN NHÁP V1, V2, V3 CỦA NHÓM)

Trước khi chuyển sang viết **SRS Baseline A**, hãy dùng danh sách kiểm tra này để đảm bảo không bị đánh trượt tại cổng **SRR-EVT**:

- [x] **Loại bỏ hoàn toàn các tính năng "Template Phần mềm/App":** Đã xóa bỏ IoT, SCADA, Bảo trì dự đoán (PdM), Bảo mật mạng, Mở rộng ray nhà xưởng (vốn xuất hiện ở `PRD_V1` và `PRD_V2`).
- [x] **Không xâm phạm ranh giới Cơ cấu nâng hạ:** Đã loại bỏ động cơ nâng, tang cuốn cáp, móc câu, bảo vệ quá tải nâng 5 tấn ra khỏi phạm vi thiết kế của xe con.
- [x] **Khai báo tường minh Khối lượng bản thân xe con ($m_{xc}$):** Không để xảy ra tình trạng bảng PRD chỉ ghi $12,222\text{ kg} + 222\text{ kg}$ nhưng phần tính toán sau lại xuất hiện tổng khối lượng $\sim 16\text{ tấn}$ mà không rõ nguồn gốc $m_{xc}$.
- [x] **Chuẩn hóa ký hiệu & đơn vị vật lý:**
  - Độ giật cực đại dùng đúng ký hiệu $\rho_{\max} \le 2\text{ m/s}^3$ (sửa lỗi gõ nhầm thành $a_{\max}$ trong bảng `PRD_V2`).
  - Vận tốc tối đa ghi đủ đơn vị $v_{\max} = 0.12\text{ m/s}$ (sửa lỗi thiếu đơn vị ở `PRD_V2`).
  - Gia tốc và độ giật dùng đúng dấu bất đẳng thức $\le$ thay vì dấu $=$ cứng nhắc.
  - Công thức hiệu suất (nếu ghi) phải là $\eta = P_{\text{out}} / P_{\text{in}}$ (sửa lỗi viết ngược $P_{\text{in}} / P_{\text{out}}$ ở `PRD_V1`).
- [x] **Thống nhất dải nhiệt độ môi trường:** Chốt đồng nhất một dải (ví dụ $10 \div 40^\circ\text{C}$, độ ẩm $\le 85\%$, tủ điện $\ge \text{IP54}$) xuyên suốt PRD, SOW và Slide, xóa bỏ các chữ `xx dB` chưa điền số.
- [x] **Khôi phục các chỉ tiêu chất lượng điều khiển định lượng:** Đưa lại chỉ tiêu sai lệch tốc độ xác lập $e_{xl} \le 5\%$ và độ quá điều chỉnh $M_p \le 10\%$ từ `PRD_V1` vào mục Tiêu chí nghiệm thu (thay cho cụm từ mơ hồ *"bám sát tuyệt đối"*).
- [x] **Đánh mã định danh duy nhất (`PRD-01`, `PRD-02`...):** Đảm bảo 100% yêu cầu có mã ID để nối sang bảng `SRS Baseline A` và `RTM`.
