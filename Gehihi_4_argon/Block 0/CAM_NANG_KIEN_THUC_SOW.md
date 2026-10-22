# CẨM NANG KIẾN THỨC & PHƯƠNG PHÁP LUẬN VỀ SOW (STATEMENT / SCOPE OF WORK)
**Dự án áp dụng:** Thiết kế Hệ truyền động điện Cơ cấu Xe con Cầu trục ($x=2$)  
**Nhóm thực hiện:** 8.5-EMG | **GVHD:** TS. Nguyễn Duy Đỉnh  
**Tài liệu tham chiếu gốc:** *NASA Systems Engineering Handbook (Mục 7.1.3.2, Bảng 7.1-2, Phụ lục P)* & Quy trình `EVLEP003_HBK` (Khối 0 — Pre-A).

---

## I. BẢN CHẤT CỦA SOW & GIẢI MÃ THUẬT NGỮ "STATEMENT OF WORK" VS. "SCOPE OF WORK"

### 1. Vị trí của SOW trong luồng Kỹ thuật Hệ thống (`EVLEP003_HBK`)
Trong sơ đồ luồng dự án `EVLEP003_HBK`, **SOW** được khởi tạo ngay tại **Khối 0 (Tiền khả thi — Pre-A — §4.2, §4.3, §5.1)** với yêu cầu bắt buộc:
> *"Soạn PRD dự thảo · Điều lệ & SOW có mục tiêu QCD đo được"*

SOW cùng với Project Charter (Điều lệ dự án) và BCA (Báo cáo khả thi sơ bộ) là bộ hồ sơ đầu vào để trình **CTO** phê duyệt tại **Cổng MCR (Mission Concept Review)**. Nếu SOW không rõ phạm vi, thiếu phân công hoặc không có chỉ tiêu QCD đo lường được, dự án sẽ bị đánh trượt theo nhánh `KHÔNG ĐẠT — cập nhật BCA / Điều lệ` về lại Khối 0.

---

### 2. So sánh "Statement of Work" và "Scope of Work"
Trong thực tế công nghiệp và làm đồ án, viết tắt **SOW** thường được gọi theo 2 cách. Dưới đây là sự phân biệt chuẩn xác:

| Tiêu chí | Statement of Work (Bản tuyên bố công việc) | Scope of Work (Bản phạm vi công việc) |
| :--- | :--- | :--- |
| **Nguồn gốc chuẩn mực** | Chuẩn học thuật và quản trị dự án quốc tế (*NASA SE Handbook*, *PMI PMBOK*, *IEEE*, hợp đồng EPC). | Thuật ngữ thông dụng trong triển khai kỹ thuật nội bộ, gói thầu nhỏ hoặc đồ án môn học. |
| **Độ rộng nội dung** | **Rộng hơn (Toàn diện):** Bao gồm cả Phạm vi công việc (*Scope*) + Yêu cầu nhiệm vụ theo WBS + Lịch trình & Cổng xét duyệt + Danh mục sản phẩm bàn giao (*Deliverables*) + Tiêu chuẩn áp dụng + Tiêu chí nghiệm thu **QCD**. | **Hẹp hơn (Tập trung vào ranh giới):** Chủ yếu định nghĩa *Làm cái gì (In-Scope)*, *Không làm cái gì (Out-of-Scope)* và danh sách các đầu việc chính. |
| **Mối quan hệ** | **Bao hàm Scope of Work** (Theo *NASA SE Handbook* Bảng 7.1-2, *Define Scope* chính là Bước 1.1 nằm trong *Statement of Work*). | Là **chương mở đầu quan trọng nhất** nằm bên trong một bản *Statement of Work* hoàn chỉnh. |

> **Kết luận thực chiến cho nhóm 8.5-EMG:**  
> Nhóm hoàn toàn có thể giữ tên gọi tiếng Việt trên Slide là **"Phạm vi công việc triển khai (SOW)"** để đồng bộ thuật ngữ, nhưng **ruột bên trong của tài liệu SOW bắt buộc phải viết theo chuẩn đầy đủ của một Statement of Work** (có gắn nhân sự RACI theo WBS và có mục tiêu QCD đo được) để vượt qua Cổng MCR của lưu đồ `EVLEP003_HBK`.

---

## II. PHÂN BIỆT RẠCH RÒI SOW VỚI PRD VÀ SRS (QUY TẮC VÀNG PHỤ LỤC P)

Theo *NASA Systems Engineering Handbook* (Mục 7.1.3.2 & Phụ lục P, mục 7), lỗi nặng nhất khi viết SOW là **trộn lẫn thông số kỹ thuật của sản phẩm vào câu lệnh công việc của con người**.

| Tiêu chí đối chiếu | SOW (Statement / Scope of Work) | PRD / SRS (Tài liệu Yêu cầu Sản phẩm / Hệ thống) |
| :--- | :--- | :--- |
| **Đối tượng điều chỉnh** | **Con người / Nhóm dự án / Nhà thầu** (*The Team / Contractor*). | **Hệ thống kỹ thuật / Sản phẩm** (*The System / Trolley Drive*). |
| **Câu hỏi cốt lõi** | **Ai** phải thực hiện công việc gì? **Giao nộp** hồ sơ gì? **Khi nào** xong? **Đánh giá** công việc thế nào? | Hệ thống phải đạt **thông số kỹ thuật, chức năng, hiệu năng** gì trong môi trường nào? |
| **Cấu trúc câu lệnh (`Shall`)** | `"Thành viên / Tiểu ban [X] phải (shall) [động từ hành động: tính toán, thiết kế, mô phỏng, bàn giao]..."` | `"Hệ truyền động xe con phải (shall) [động từ trạng thái/đặc tính: di chuyển, duy trì, giới hạn, chịu được]..."` |
| **Nội dung KHÔNG ĐƯỢC đưa vào** | Không đưa bảng thông số đề bài chi tiết ($Q, v, a, \rho$) làm trọng tâm; không viết sẵn công thức giải ($F_c, M_{qđ}, J_{qđ}$) vào SOW. | Không giao việc cho cá nhân hay quy định ngày nộp báo cáo Word/Slide trong SRS. |
| **Ví dụ ĐÚNG chuẩn SE** | *"Nhóm 1 (PE-Hardware - Đặng Nguyên Bình) phải tính chọn động cơ KĐB 3 pha, biến tần AC và bàn giao Bảng BOM L1/L2 trước cổng PDR-EVT."* | *"Hệ truyền động xe con phải di chuyển tải trọng định mức $Q = 12,222\text{ kg}$ với vận tốc tối đa $v_{\max} = 0.12\text{ m/s}$ và gia tốc $a \le 0.5\text{ m/s}^2$."* |

---

## III. QUY TRÌNH 3 BƯỚC XÂY DỰNG SOW CHUẨN NASA SE HANDBOOK

Căn cứ **Mục 7.1.3.2 (Develop the Statement of Work)**, **Hình 7.1-2** và **Bảng 7.1-2 (Steps in the Requirements Development Process)** trong tài liệu *NASA SE Handbook*, quy trình viết SOW gồm 3 bước:

```
[Bước 1: Phân tích Công việc] ──► [Bước 2: Phân tích Hiệu suất (QCD)] ──► [Bước 3: Phân tích Dữ liệu & Bàn giao]
  • Định nghĩa Scope (In/Out)        • Quality (Độ bao phủ RTM, Pass Sim)     • Chỉ định Tiêu chuẩn (TCVN, ISO, IEC)
  • Tổ chức theo WBS / PBS           • Cost (Giờ công CFT, tối ưu BOM)        • Lập danh mục Deliverables (CDRL)
  • Viết câu lệnh "Team shall..."    • Delivery (Mốc Cổng MCR -> SAR-EVT)     • Quy định định dạng file (.docx, .slx)
```

### Bước 1: Phân tích Công việc (Step 1: Analyze the Work)
1. **Xác định Phạm vi (Define Scope):** Nêu rõ bối cảnh đề tài và tách bạch **Ranh giới thiết kế (In-Scope)** với **Ranh giới loại trừ (Out-of-Scope)**.
2. **Tổ chức SOW theo WBS (Organize SOW):** Cấu trúc các mục công việc trong SOW phải bám sát **Cấu trúc phân rã công việc (WBS)** và **6 khối công việc (`Khối 0 → Khối 5`)** của dự án.
3. **Viết yêu cầu công việc (Write SOW Requirements):** Bao phủ cả 2 mảng:
   * Hoạt động kỹ thuật phát triển sản phẩm (Tính động lực học, chọn thiết bị lực, thiết kế FOC, mô phỏng Simulink).
   * Hoạt động quản trị & kiểm soát kỹ thuật hệ thống (Lập PRD/SRS, duy trì RTM, lập DVP&R, tổ chức họp cổng xét duyệt).
4. **Ghi chú lý giải (Document Rationale):** Lưu lại lý do vì sao đưa vào hoặc loại trừ một số hạng mục công việc đặc thù.

### Bước 2: Phân tích Tiêu chuẩn Hiệu suất (Step 2: Analyze Performance — Mục tiêu QCD)
Thiết lập các thước đo định lượng để đánh giá công việc của nhóm có đạt yêu cầu hay không (đáp ứng điều khoản **mục tiêu QCD đo được** tại Khối 0 `EVLEP003_HBK`):
* **Q — Quality (Chất lượng):** $100\%$ yêu cầu SRS truy xuất được về PRD; $100\%$ phép thử trong DVP&R L0 có kết quả kiểm chứng; mô hình Simulink chạy ổn định ở cả 4 góc phần tư, đạt các ngưỡng CTQ ($a \le 0.5\text{ m/s}^2$, $\rho \le 2\text{ m/s}^3$, độ quá điều chỉnh $\le 10\%$, sai số xác lập $\le 5\%$).
* **C — Cost (Chi phí & Nguồn lực):** Kiểm soát tổng ngân sách giờ công của 6 thành viên; lựa chọn thiết bị phần lực (Động cơ, Biến tần) có hệ số dự trữ hợp lý ($k_{dt} = 1.2 \div 1.5$), không chọn dư thừa công suất gây đội giá BOM.
* **D — Delivery (Tiến độ bàn giao):** Hoàn thành đúng hạn các mốc cổng nội bộ (`MCR → SAR-EVT`) và 2 mốc cứng của học phần: **Bảo vệ Giữa kỳ (Tuần 10–16)** và **Nộp báo cáo đồ án Cuối kỳ tại phòng thi**.

### Bước 3: Phân tích Dữ liệu & Hồ sơ bàn giao (Step 3: Analyze Data)
1. **Chỉ định Tiêu chuẩn áp dụng (Identify Standards):** Liệt kê các tiêu chuẩn kỹ thuật và quy chuẩn trình bày bắt buộc tuân thủ:
   * Tiêu chuẩn thiết kế thiết bị nâng Việt Nam: **$TCVN\ 4244:2005$**.
   * Tiêu chuẩn bản vẽ và ký hiệu điện quốc tế: **$ISO\ 128-2:2020$, $IEC\ 60617$, $IEC\ 60034$**.
   * Tiêu chuẩn quy trình SE nội bộ: **`EVLEP003_HBK`**.
2. **Định nghĩa Danh mục Bàn giao (Define Deliverables):** Mọi sản phẩm đầu ra (Bản thuyết minh, Bảng tính, Sơ đồ nguyên lý, File mô phỏng, Slide) phải gắn liền với một yêu cầu thực hiện trong SOW, ghi rõ định dạng file điện tử và người phê duyệt.

---

## IV. CHECKLIST 12 TIÊU CHÍ SOÁT XÉT SOW (PHỤ LỤC P — NASA SE HANDBOOK)

Trước khi đệ trình SOW qua cổng **MCR**, PM/SE Lead dùng bảng kiểm 12 điểm sau đây để rà soát chất lượng văn bản:

- [ ] **1. Đúng mẫu câu giao việc (`Who shall do What`):** Mọi câu yêu cầu công việc phải chỉ rõ chủ thể thực hiện (VD: *"PE-Hardware phải..."*, *"Doc Lead phải..."*).
- [ ] **2. Câu đơn — Mỗi câu 1 nhiệm vụ:** Tách các câu ghép nhiều việc thành các câu/gạch đầu dòng đơn lẻ để dễ nghiệm thu từng việc.
- [ ] **3. Đoạn văn mạch lạc theo chủ đề:** Mỗi mục chỉ giải quyết một gói công việc thuộc WBS.
- [ ] **4. Đánh mã định danh duy nhất (Unique ID):** Mỗi đầu việc có mã số riêng (VD: `SOW-1.1`, `SOW-2.1`) để truy xuất sang lịch trình và bảng phân công RACI.
- [ ] **5. Dùng thể chủ động (Active Voice):** Tuyệt đối không dùng câu bị động vô chủ ngữ (Không viết: *"Động cơ sẽ được tính chọn..."* $\to$ Phải viết: *"Đặng Nguyên Bình (PE-Hardware) phải tính chọn động cơ..."*).
- [ ] **6. Diễn đạt khẳng định (Positive Statement):** Nêu rõ việc phải làm thay vì chỉ liệt kê phủ định *"shall not"* (trừ mục Ranh giới loại trừ).
- [ ] **7. Chuẩn ngữ pháp & thuật ngữ kỹ thuật:** Không sai lỗi câu, thống nhất tên gọi các biến và thiết bị.
- [ ] **8. Không có lỗi chính tả & ký hiệu đơn vị:** Kiểm tra kỹ các ký hiệu vật lý và đơn vị chuẩn SI.
- [ ] **9. Giải thích từ viết tắt (Acronyms):** Định nghĩa rõ các từ viết tắt (SOW, PRD, SRS, FOC, VFD, BOM, RTM, DVP&R...) ngay lần đầu xuất hiện hoặc lập bảng thuật ngữ.
- [ ] **10. Rõ số lượng, lịch nộp & phương thức bàn giao:** Mỗi Deliverable phải có mốc thời gian (Tuần / Cổng) rõ ràng.
- [ ] **11. Quy định rõ cấu trúc của tài liệu bàn giao:** Chỉ rõ thuyết minh, bảng tính hay slide gồm những nội dung cốt lõi nào.
- [ ] **12. Quy định rõ định dạng file điện tử (File Format):** Ghi cụ thể `.docx`, `.pdf`, `.xlsx`, `.pptx`, `.slx` (MATLAB/Simulink).

---

## V. CHẨN ĐOÁN BẢN `SOW_HungNB.docx.pdf` HIỆN TẠI & HƯỚNG CẢI TỔ CHO NHÓM 8.5-EMG

Khi chiếu bản `SOW_HungNB.docx.pdf` (và Slide 18–22) vào bộ tiêu chuẩn trên, chúng ta nhận diện được **4 điểm cần bóc tách và nâng cấp**:

| STT | Vấn đề trong bản `SOW_HungNB.docx.pdf` hiện tại | Tác động / Rủi ro tại Cổng xét duyệt | Giải pháp chuẩn hóa (Refactoring) |
| :-: | :--- | :--- | :--- |
| **1** | **Đặt nhầm Bảng thông số đầu bài vào Mục 2 của SOW** ($Q=12,222\text{ kg}, m_c=222\text{ kg}, h=12\text{ m}, v, a, \rho, d, \mu, \eta$). | Vi phạm mục 7 Phụ lục P (lẫn lộn giữa yêu cầu sản phẩm PRD và phạm vi công việc SOW). | Rút Bảng thông số ở Mục 2 sang đặt làm trọng tâm của **Tài liệu PRD (Khối 1)**. Trong SOW chỉ dẫn chiếu ngắn gọn đến mã đề $x=2$ và tài liệu PRD. |
| **2** | **Đưa công thức tính toán chi tiết vào Mục 3 của SOW** ($F_2, F_{t1}, F_{g2}, M_{qđ}, J_{qđ}$) và **quên khối lượng bản thân xe con $m_{xc}$** trong công thức $(Q+m_c)$. | Mâu thuẫn trực tiếp với Slide 15–16 (nơi ghi xe con nặng $3\div 4\text{ tấn}$, tổng tải $\sim 16\text{ tấn}$); đồng thời vi phạm nguyên tắc SOW không viết sẵn lời giải chi tiết. | Chuyển các công thức sang **Thuyết minh tính toán (Khối 2)** và bổ sung $m_{xc}$ vào tổng khối lượng $M_{\Sigma} = Q + m_{nh} + m_{xc}$. Trong SOW chỉ quy định đầu việc: *"Thực hiện tính toán lực cản và quy đổi mô-men/quán tính của toàn bộ hệ xe con mang tải về trục động cơ"*. |
| **3** | **Lỗi gõ máy ký hiệu & đơn vị ở Mục 2:**<br>- $v_{\max} = 0.12$ (thiếu đơn vị `m/s`).<br>- Độ giật cực đại ký hiệu nhầm là $a_{\max}$ thay vì $\rho_{\max}$. | Bị bắt lỗi cẩu thả kỹ thuật ngay tại cổng `MCR` / `SRR-EVT`. | Sửa chuẩn: $v_{\max} = 0.12\text{ m/s}$; Độ giật cực đại ký hiệu $\rho_{\max}$ với ràng buộc $\rho \le 2\text{ m/s}^3$. |
| **4** | **Thiếu Phân công nhân sự (6 thành viên) & Mục tiêu QCD đo được.** | Không đạt tiêu chí bắt buộc của **Khối 0 (`EVLEP003_HBK`)**: *"Điều lệ & SOW có mục tiêu QCD đo được"*. | Bổ sung bảng ánh xạ **WBS — RACI cho 6 thành viên** (Đông, Trung, Bình, B.Hưng, Khải, P.V.Hưng) và mục **Chỉ tiêu QCD + Lịch trình 7 cổng (`MCR → SAR-EVT`)**. |

---

## VI. KHUNG MẪU SOW CHUẨN HÓA (TEMPLATE ÁP DỤNG NGAY CHO NHÓM 8.5-EMG)

Dưới đây là khung xương sống 7 mục của bản SOW mới sau khi đã chuẩn hóa theo cả *NASA SE Handbook* và lưu đồ `EVLEP003_HBK`:

1. **Mục 1 — Thông tin chung & Mục tiêu Dự án (Project Overview & Objectives):** Định danh đề tài ($x=2$), nhóm 8.5-EMG, GVHD TS. Nguyễn Duy Đỉnh, mục tiêu tổng quát của hệ truyền động xe con cầu trục.
2. **Mục 2 — Phạm vi Công việc (Scope of Work — In-Scope & Out-of-Scope):**
   * *2.1. Ranh giới thực hiện (In-Scope):* Quản trị SE, Phần lực, Phần điều khiển & Cảm biến, Mô phỏng kiểm chứng.
   * *2.2. Ranh giới loại trừ (Out-of-Scope):* Kết cấu cơ khí dầm/khung/cáp, cơ cấu nâng hạ, gia công tủ điện thực tế, báo giá thương mại.
3. **Mục 3 — Tài liệu & Tiêu chuẩn Áp dụng (Applicable Documents & Standards):** Đề bài gốc (`De bai tap dai 2023.1`), $TCVN\ 4244:2005$, `EVLEP003_HBK`, $ISO\ 128-2:2020$, $IEC\ 60617$.
4. **Mục 4 — Phân rã Công việc (WBS) & Giao nhiệm vụ theo CFT (`"Who shall do What"`):**
   * *Giai đoạn 0 & 1 (Quản trị SE & Yêu cầu - Nhóm 3: Nghiêm Trọng Đông, Nguyễn Hải Trung).*
   * *Giai đoạn 2 (Động lực học, Phần lực & Logic - Nhóm 1: Đặng Nguyên Bình, Nguyễn Bá Hưng).*
   * *Giai đoạn 3 (Điều khiển FOC & Mô phỏng Kiểm thử - Nhóm 2: Trần Đỗ Khải, Phạm Văn Hưng).*
   * *Giai đoạn 4 (Đóng gói Thuyết minh & Bảo vệ - Toàn nhóm, Nguyễn Hải Trung chủ trì).*
5. **Mục 5 — Mục tiêu QCD Đo lường được (Measurable QCD Targets):**
   * *5.1. Chỉ tiêu Chất lượng (Quality).*
   * *5.2. Chỉ tiêu Chi phí & Nguồn lực (Cost).*
   * *5.3. Chỉ tiêu Tiến độ & Cổng xét duyệt (Delivery — Giữa kỳ Tuần 10–16 & Cuối kỳ).*
6. **Mục 6 — Danh mục Hồ sơ & Sản phẩm Bàn giao (Deliverables & CDRL):** Bảng quy định Mã hồ sơ, Tên sản phẩm, Định dạng file, Cổng nộp, Người lập (R), Người kiểm tra (QE) và Người duyệt (A).
7. **Mục 7 — Tiêu chí Nghiệm thu Công việc (Work Acceptance Criteria):** Điều kiện đủ về mặt tính toán công suất/mô-men, biến tần/bảo vệ, đáp ứng động học Simulink và tính toàn vẹn của hồ sơ SE.