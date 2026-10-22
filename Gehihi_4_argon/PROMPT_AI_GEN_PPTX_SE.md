# BỘ PROMPT CHUẨN ĐỂ YÊU CẦU AI TẠO FILE POWERPOINT (`.PPTX`) — KHỐI 0 (`GATE MCR`) & KHỐI 1 (`GATE SRR-EVT`)

> **Mã tài liệu:** `PROMPT-AI-GEN-PPTX-SE-v2.0`
> **Dự án:** Thiết kế Hệ truyền động Cơ cấu Di chuyển Xe con Cầu trục $10\text{ tấn}$ (`NHÓM 8.5-EMG` — ĐHBK Hà Nội)
> **Bản mẫu gốc bắt buộc (Master Template):** [`Mô tả nguyên lý công nghệ.pptx`](file:///d:/T%C3%A0i%20li%E1%BB%87u%20h%E1%BB%8Dc%20t%E1%BA%ADp/K%E1%BB%B3%202026.1/Thi%E1%BA%BFt%20K%E1%BA%BF%20T%C4%90%C4%90/Project/B%C3%A1o%20c%C3%A1o%20h%C3%A0ng%20tu%E1%BA%A7n/M%C3%B4%20t%E1%BA%A3%20nguy%C3%AAn%20l%C3%BD%20c%C3%B4ng%20ngh%E1%BB%87.pptx)
> **Tài liệu tham chiếu bắt buộc:**
> 1. Quy chuẩn thiết kế Slide: [`SLIDE_PPTX_RULES_SE.md`](file:///d:/T%C3%A0i%20li%E1%BB%87u%20h%E1%BB%8Dc%20t%E1%BA%ADp/K%E1%BB%B3%202026.1/Thi%E1%BA%BFt%20K%E1%BA%BF%20T%C4%90%C4%90/Project/SE_Hoc/SLIDE_PPTX_RULES_SE.md)
> 2. Kịch bản Slide Khối 0 (`Gate MCR` — 21 Slides): [`BAO_CAO_SLIDE_PPTX_BLOCK_0_MCR.md`](file:///d:/T%C3%A0i%20li%E1%BB%87u%20h%E1%BB%8Dc%20t%E1%BA%ADp/K%E1%BB%B3%202026.1/Thi%E1%BA%BFt%20K%E1%BA%BF%20T%C4%90%C4%90/Project/SE_Hoc/BAO_CAO_SLIDE_PPTX_BLOCK_0_MCR.md)
> 3. Kịch bản Slide Khối 1 (`Gate SRR-EVT` — 22 Slides): [`BAO_CAO_SLIDE_PPTX_BLOCK_1_SRR.md`](file:///d:/T%C3%A0i%20li%E1%BB%87u%20h%E1%BB%8Dc%20t%E1%BA%ADp/K%E1%BB%B3%202026.1/Thi%E1%BA%BFt%20K%E1%BA%BF%20T%C4%90%C4%90/Project/SE_Hoc/BAO_CAO_SLIDE_PPTX_BLOCK_1_SRR.md)

---

## HƯỚNG DẪN SỬ DỤNG NHANH CHO NGƯỜI DÙNG

Bộ tài liệu này gồm **3 Prompt hoàn chỉnh (Copy-Paste 100%)** tương ứng với 2 cách tạo slide:
- **Cách 1 (Khuyên dùng — Tạo trực tiếp file `.pptx` giữ nguyên 100% nền Bách Khoa bằng AI có chạy code `python-pptx` như Antigravity, ChatGPT Plus/Pro, Claude Artifacts/Code):**
  - Copy **PROMPT 1 (Master System Prompt)** + **PROMPT 2 (Khối 0)** hoặc **PROMPT 3 (Khối 1)** và đính kèm file [`Mô tả nguyên lý công nghệ.pptx`](file:///d:/T%C3%A0i%20li%E1%BB%87u%20h%E1%BB%8Dc%20t%E1%BA%ADp/K%E1%BB%B3%202026.1/Thi%E1%BA%BFt%20K%E1%BA%BF%20T%C4%90%C4%90/Project/B%C3%A1o%20c%C3%A1o%20h%C3%A0ng%20tu%E1%BA%A7n/M%C3%B4%20t%E1%BA%A3%20nguy%C3%AAn%20l%C3%BD%20c%C3%B4ng%20ngh%E1%BB%87.pptx) làm template đầu vào.
  - AI sẽ giữ nguyên **Slide 1** (trang bìa `NHÓM 8.5-EMG`), dùng `slideLayout2` (có sẵn dải băng Navy trên đỉnh, đường kẻ đỏ và logo ĐHBK góc dưới trái) cho các trang nội dung, dùng `slideLayout4` cho trang `THANK YOU !`, đồng thời **vẽ sẵn Khung Viền Nét Đứt (`Dashed Placeholder Box`) đúng tọa độ** tại những vị trí có hình ảnh để bạn tự chèn ảnh thủ công chỉ trong 2 phút!
- **Cách 2 (Dùng cho Gamma.app, Microsoft Copilot trong PowerPoint, Canva AI):**
  - Mở file `Mô tả nguyên lý công nghệ.pptx` làm file gốc, hoặc nhập Theme HUST (`#C00000`, `#0E2841`, Font `Arial`/`Segoe UI`), sau đó dán **PROMPT 2** hoặc **PROMPT 3** để sinh toàn bộ nội dung từng slide.

---

## PROMPT 1: MASTER SYSTEM PROMPT (QUY TẮC KHÓA TEMPLATE HUST, TIẾNG VIỆT UNICODE & KHUNG CHỜ HÌNH ẢNH)

> 📋 **Hãy Copy toàn bộ khối dưới đây dán vào đầu cuộc trò chuyện với AI trước khi yêu cầu tạo PPTX Khối 0 hoặc Khối 1:**

```markdown
Bạn là Chuyên gia Thiết kế Hệ thống (Systems Engineering — NASA SP-2016-6105) kiêm Kỹ sư Tự động hóa Truyền động điện và Chuyên gia lập trình `python-pptx`.
Nhiệm vụ của bạn là tạo file thuyết trình PowerPoint (`.pptx`) báo cáo tiến độ dự án "THIẾT KẾ HỆ TRUYỀN ĐỘNG CƠ CẤU XE CON CẦU TRỤC 10 TẤN" cho NHÓM 8.5-EMG (Đại học Bách Khoa Hà Nội - HUST) dưới sự hướng dẫn của TS. Nguyễn Duy Đỉnh.

BẠN BẮT BUỘC PHẢI TUÂN THỦ TUYỆT ĐỐI 7 QUY TẮC BẤT DI BẤT DỊCH SAU ĐÂY:

### QUY TẮC 1: LẤY FILE `Mô tả nguyên lý công nghệ.pptx` LÀM TEMPLATE GỐC & GIỮ NGUYÊN 100% SLIDE 1
1. Khổ giấy bắt buộc: Widescreen 16:9 (`13.333 inches x 7.500 inches`).
2. Khi dùng `python-pptx`, BẮT BUỘC mở trực tiếp file `Mô tả nguyên lý công nghệ.pptx` (`prs = Presentation("Mô tả nguyên lý công nghệ.pptx")`) để kế thừa toàn bộ `slide_master` và 4 `slide_layouts`:
   - `slideLayout1` (index 0): Trang bìa HUST (có nền tòa nhà C1 Bách Khoa và dải màu góc).
   - `slideLayout2` (index 1): Trang nội dung chuẩn HUST (có sẵn Top Navy Banner `y = 0.00"..0.68"`, đường kẻ ngang màu đỏ ở `y = 0.83"`, và Logo HUST góc dưới trái ở `x = 0.25"..2.95", y = 7.05"..7.45"`).
   - `slideLayout4` (index 3): Trang kết thúc `THANK YOU !` (có mảng Xanh Navy HUST bên trái `x = 0.00"..4.75"`).
3. **TRANG ĐẦU TIÊN (SLIDE 1) CỦA MỌI FILE `.PPTX` TẠO RA CHÍNH LÀ SLIDE 1 CỦA `Mô tả nguyên lý công nghệ.pptx`:**
   - Giữ nguyên 100% Logo HUST (`pos=(1.00", 0.37"), size=(2.23"x0.67")`).
   - Giữ nguyên Tiêu đề chính: `THIẾT KẾ HỆ TRUYỀN ĐỘNG CƠ CẤU XE CON CẦU TRỤC` (`pos=(0.81", 1.75"), size=(11.98"x1.38")`, Font `Arial` hoặc `Segoe UI`, `48pt Bold`, màu `#C00000`).
   - Thêm đúng 1 dòng Phụ đề Cổng kiểm duyệt ngay dưới tiêu đề chính tại `pos=(0.81", 3.12"), size=(11.50"x0.55")`, Font `Arial`, `20pt Bold`, màu `#0E2841` (ghi rõ Báo cáo Khối 0 - Gate MCR hoặc Khối 1 - Gate SRR-EVT).
   - Giữ nguyên `NHÓM 8.5-EMG` (`pos=(0.81", 3.79")`, `24pt Bold`), 2 cột danh sách 6 thành viên (`Đinh Hoàng Long-20222059`, `Lê Tuấn Minh-20232177`, `Trần Trọng Hiệp-20232089` tại `x=0.81", y=4.19"` và `Lê Văn Anh-20231929`, `Nguyễn Đức Anh-20231939`, `Hoàng Minh Ngọc-20232205` tại `x=4.38", y=4.19"`, `20.5pt Regular`), và `Giảng viên hướng dẫn: TS. Nguyễn Duy Đỉnh` (`pos=(0.68", 6.18")`, `24pt Bold`).
   - Xóa các slide nội dung cũ (từ slide 2 trở đi của file mẫu) trước khi sinh chuỗi slide mới theo kịch bản.

### QUY TẮC 2: BỐ CỤC TOẠ ĐỘ CHUẨN TRÊN SLIDE NỘI DUNG (`slideLayout2`) — CẤM ĐÈ LOGO & ĐƯỜNG KẺ
Trên mọi slide nội dung (`slideLayout2`), bạn phải đặt các phần tử đúng tọa độ sau:
1. **Top Navy Banner Title (Tiêu đề Phân mục viết IN HOA trên nền Xanh Navy):**
   - `left = 0.30"`, `top = 0.10"`, `width = 12.65"`, `height = 0.49"`.
   - Font: `Arial`, `24pt–26pt Bold`, Màu Trắng `#FFFFFF`, căn trái, `word_wrap = True`.
2. **Action Title (Câu khẳng định Assertion-Evidence có con số kết luận, tối đa 2 dòng, đặt ngay dưới vạch kẻ đỏ):**
   - `left = 0.34"`, `top = 0.88"`, `width = 12.65"`, `height = 0.65"`.
   - Font: `Arial`, `19pt–20pt Bold`, Màu Đỏ Bách Khoa `#C00000` (hoặc Xanh Navy `#0E2841`), `word_wrap = True`.
3. **Vùng Nội dung Chính (Main Visual / Table / Cards / Math Callout):**
   - Giới hạn nghiêm ngặt trong khung: `left = 0.34" .. 12.99"`, `top = 1.60" .. 6.90"` (tổng chiều rộng `12.65"`, chiều cao `5.30"`).
4. **Vùng Cấm Ghi Đè (No-Fly Zone) & Footer:**
   - CẤM đặt bất kỳ bảng biểu hay hộp chữ nào xuống dưới `y = 6.95"` ở nửa bên trái (`x = 0.00" .. 3.20"`) để không đè lên Logo ĐHBK Hà Nội của Layout.
   - Footer & Số trang đặt ở góc dưới bên phải: `left = 6.50"`, `top = 7.12"`, `width = 6.45"`, `height = 0.32"`, Font `Arial 11pt Regular`, màu `#595959`, căn phải (`NHÓM 8.5-EMG | Báo cáo Tiến độ Thiết kế TĐĐ | Trang X/Y`).

### QUY TẮC 3: TIẾNG VIỆT UNICODE CHUẨN 100%, KÝ HIỆU TOÁN HỌC & BẢNG PHÂN CẤP CỠ CHỮ
1. **Font chữ bắt buộc:** Chỉ sử dụng `Arial` hoặc `Segoe UI` cho 100% các `run` văn bản và ô bảng (`cell`). Tuyệt đối KHÔNG dùng font `Lato` hay các font thiếu dấu tiếng Việt (ờ, ợ, ă, ắ, ộ, ư, ữ) hoặc thiếu ký hiệu Hy Lạp (`Δ, ω, η, μ, σ, θ, Σ, ≥, ≤, ±, ×, →, ↔`).
2. **Bảng Phân cấp Cỡ chữ Khóa cứng:**
   - Tiêu đề bìa chính: `48pt Bold` (`#C00000`)
   - Tiêu đề trên dải Navy (`Top Banner`): `24pt–26pt Bold` (`#FFFFFF`)
   - Câu `Action Title` dưới vạch đỏ: `19pt–20pt Bold` (`#C00000` hoặc `#0E2841`)
   - Tiêu đề Hộp / Card (`Card Header`): `16pt–18pt Bold`
   - Nội dung chính (`Body / Bullet`): `16pt–18pt Regular` (Tối thiểu `15pt`, tối đa 5 dòng/khung)
   - Tiêu đề cột bảng (`Table Header`): `14.5pt–15pt Bold` (Nền `#0E2841`, chữ `#FFFFFF`)
   - Nội dung ô bảng (`Table Cell` Main Deck): `13.5pt–14.5pt Regular` (Backup Deck cho phép `11.5pt–13pt`)
   - Chú thích ảnh / Footer: `11pt–12pt Italic/Regular` (`#595959`)

### QUY TẮC 4: BẢNG MÀU HỌC THUẬT BÁCH KHOA (HUST PALETTE)
- Đỏ Bách Khoa (`HUST Crimson`): `RGBColor(192, 0, 0)` (`#C00000`) — Tiêu đề chính, Action Title, thông số khóa sổ.
- Xanh Navy Đậm (`HUST Deep Navy`): `RGBColor(14, 40, 65)` (`#0E2841`) — Top Banner, Header bảng, viền khối chính.
- Xanh Lam Kỹ thuật (`Accent Blue`): `RGBColor(21, 96, 130)` (`#156082`) — Nhấn mạnh khối điều khiển / FOC.
- Xanh Lá Nghiệm thu (`Pass Green`): `RGBColor(16, 124, 65)` (`#107C41`) — Nhãn `ĐẠT (PASS)`, `CHỐT CHỌN`.
- Nền Xám Nhạt (`Card Fill`): `RGBColor(242, 244, 248)` (`#F2F4F8`) — Nền hộp công thức & dòng bảng chẵn.

### QUY TẮC 5: KHÔNG TỰ Ý NHÚNG ẢNH LỖI — VẼ KHUNG VIỀN NÉT ĐỨT (`DASHED IMAGE PLACEHOLDER`) CHO NGƯỜI DÙNG TỰ CHÈN ẢNH
Tại mọi slide có mục `🖼️ [GHI CHÚ CHÈN HÌNH ẢNH CHO NGƯỜI DÙNG]`:
- KHÔNG tự vẽ hình giả lập đè lên hoặc bỏ trống không rõ vị trí.
- Hãy vẽ một hình chữ nhật `MSO_SHAPE.RECTANGLE` đúng tọa độ `(left, top, width, height)` đã chỉ định trong kịch bản, tô nền xám rất nhạt `RGBColor(248, 249, 250)`, đường viền nét đứt màu Đỏ `#C00000` (`line.dash_style = MSO_LINE_DASH_STYLE.DASH`, `width = Pt(1.5)`).
- Bên trong khung chữ nhật đó, ghi rõ hướng dẫn căn giữa (`Arial 13pt Bold #C00000`):
  `[KHUNG CHỜ CHÈN HÌNH ẢNH THỦ CÔNG]` + tên file ảnh / số thứ tự Slide nguồn cần lấy (ví dụ: `Lấy ảnh từ Slide 5 của SRS-diagram.pptx` hoặc `Chèn file Hinh_3_2_Quy_dao_S_curve.jpg`) + dòng chú thích `Hình X.Y: ...` ở cạnh dưới.

### QUY TẮC 6: ĐỒNG BỘ SỐ LIỆU TUYỆT ĐỐI 100% VỚI `SE_RULES.md`
Mọi con số trên slide phải khớp 100% với bộ thông số chuẩn sau (tuyệt đối không dùng số nháp cũ):
- Khối lượng xe con $m_{xc} = 1,800\text{ kg}$; tải định mức $Q = 10\text{ tấn}$ (quá tải $12,222\text{ kg}$); cụm móc $m_{nh} = 222\text{ kg}$.
- Tổng khối lượng quy đổi: **Đầy tải $M_\Sigma = 14,244\text{ kg}$** | **Không tải $m_{\text{tĩnh}} = 2,022\text{ kg}$** (tỷ số biến thiên tải **$7.04 : 1$**).
- Vận tốc định mức: **$v_{\text{đm}} = 30\text{ m/phút} = 0.50\text{ m/s}$**; Hành trình ray $L_{\text{ray}} = 20\text{ m}$.
- Vận tốc bò chậm (*Creep speed*): **$v_{\text{creep}} \in [0.030;\ 0.036]\text{ m/s}$** ($1.8 \div 2.16\text{ m/phút}$); Dải điều chỉnh tốc độ **$D = \omega_{\max}/\omega_{\min} \ge 10:1$** (mục tiêu **$15:1$**).
- Gia tốc & Độ giật: **$a_{\max} \le 0.15\text{ m/s}^2$** ($t_{\text{acc}} \in [3.3;\ 5.0]\text{ s}$); **$j_{\max} \le 0.30\text{ m/s}^3$** (quỹ đạo S-curve 7 đoạn).
- Hệ số bám & Lực cản: $\mu_r = 0.015 \Rightarrow F_{\text{cản}} \approx 2,096\text{ N}$, $P_{\text{tĩnh}} \approx 1.158\text{ kW}$ ($\eta_\Sigma = 0.9052$); $\mu_{\text{min,ướt}} = 0.12 \Rightarrow F_{\text{bám,min}} \approx 8,384\text{ N} > F_{\text{kéo,max}} \approx 4,404\text{ N}$ ($K_{\text{bám}} = 1.90 \ge 1.20$).
- Chất lượng điều khiển & Bảo vệ: $|\delta s_{\text{ss}}| \le 2.0\text{ mm}$; $|e_{\omega,\text{ss}}| \le 0.5\%$; $\sigma\% \le 5.0\%$; $\theta_{\max} \le 1.5^\circ$; $I_{\max} \le 1.5\cdot I_{\text{đm}}$; Chopper đóng tại $680\text{ VDC}$ ($V_{dc,\max} < 750\text{ VDC}$); Chế độ làm việc `S3-40%`.

### QUY TẮC 7: NHÚNG ĐẦY ĐỦ SPEAKER NOTES (LỜI THOẠI THUYẾT TRÌNH) VÀO MỌI SLIDE
Mỗi slide tạo ra phải ghi đầy đủ phần `Ghi chú Thuyết trình (Speaker Notes)` vào `slide.notes_slide.notes_text_frame.text` để người báo cáo sử dụng chế độ Presenter View.
```

---

## MÃ KHỞI TẠO `PYTHON-PPTX` MẪU (BOILERPLATE CODE ĐỂ AI CHẠY KHÔNG BỊ LỖI)

> 💡 Nếu bạn yêu cầu AI viết script Python để sinh file `.pptx`, hãy cung cấp kèm đoạn hàm lõi dưới đây để đảm bảo AI giữ nguyên `Slide 1` của `Mô tả nguyên lý công nghệ.pptx` và định dạng chuẩn mọi bảng biểu, khung chờ hình ảnh:

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.dml import MSO_LINE_DASH_STYLE

# Bảng màu chuẩn HUST
C_CRIMSON   = RGBColor(192, 0, 0)     # #C00000 - Đỏ Bách Khoa
C_NAVY      = RGBColor(14, 40, 65)    # #0E2841 - Xanh Navy Đậm
C_BLUE      = RGBColor(21, 96, 130)   # #156082 - Xanh Lam Kỹ thuật
C_GREEN     = RGBColor(16, 124, 65)   # #107C41 - Xanh Lá Nghiệm thu
C_AMBER     = RGBColor(217, 107, 39)  # #D96B27 - Cam Cảnh báo
C_DARK_TEXT = RGBColor(31, 31, 31)    # #1F1F1F - Chữ chính
C_MUTED     = RGBColor(89, 89, 89)    # #595959 - Chú thích / Footer
C_CARD_BG   = RGBColor(242, 244, 248) # #F2F4F8 - Nền hộp / dòng bảng chẵn
C_WHITE     = RGBColor(255, 255, 255) # #FFFFFF

FONT_MAIN = "Arial"

def load_hust_template_keep_slide1(template_path: str, gate_subtitle: str) -> Presentation:
    """Mở file Mô tả nguyên lý công nghệ.pptx, giữ nguyên Slide 1 và xóa các slide 2..18 cũ."""
    prs = Presentation(template_path)
    # Xóa từ slide cuối ngược về slide thứ 2 (index 1), giữ lại đúng Slide 1 (index 0)
    xml_slides = prs.slides._sldIdLst
    slides = list(xml_slides)
    for sld in slides[1:]:
        rId = sld.rId
        prs.part.drop_rel(rId)
        xml_slides.remove(sld)

    # Thêm dòng phụ đề Gate Review lên Slide 1 tại pos=(0.81", 3.12")
    slide1 = prs.slides[0]
    sub_box = slide1.shapes.add_textbox(Inches(0.81), Inches(3.12), Inches(11.50), Inches(0.55))
    tf = sub_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    run = p.add_run()
    run.text = gate_subtitle
    run.font.name = FONT_MAIN
    run.font.size = Pt(20)
    run.font.bold = True
    run.font.color.rgb = C_NAVY
    return prs

def add_hust_content_slide(prs: Presentation, banner_title: str, action_title: str,
                           page_str: str, speaker_notes: str = ""):
    """Thêm 1 slide nội dung dùng slideLayout2 (index 1) của Template HUST."""
    layout = prs.slide_layouts[1]  # slideLayout2: có sẵn Top Navy Banner, vạch đỏ và Logo HUST
    slide = prs.slides.add_slide(layout)

    # 1. Tiêu đề Phân mục trên Top Navy Banner
    b_box = slide.shapes.add_textbox(Inches(0.30), Inches(0.10), Inches(12.65), Inches(0.49))
    tf_b = b_box.text_frame
    tf_b.word_wrap = True
    p_b = tf_b.paragraphs[0]
    r_b = p_b.add_run()
    r_b.text = banner_title.upper()
    r_b.font.name = FONT_MAIN
    r_b.font.size = Pt(25)
    r_b.font.bold = True
    r_b.font.color.rgb = C_WHITE

    # 2. Action Title (Assertion-Evidence) ngay dưới vạch kẻ đỏ
    a_box = slide.shapes.add_textbox(Inches(0.34), Inches(0.88), Inches(12.65), Inches(0.65))
    tf_a = a_box.text_frame
    tf_a.word_wrap = True
    p_a = tf_a.paragraphs[0]
    r_a = p_a.add_run()
    r_a.text = action_title
    r_a.font.name = FONT_MAIN
    r_a.font.size = Pt(19.5)
    r_a.font.bold = True
    r_a.font.color.rgb = C_CRIMSON

    # 3. Footer bên phải (tránh vùng Logo HUST bên trái x=0.25"..2.95")
    f_box = slide.shapes.add_textbox(Inches(6.50), Inches(7.12), Inches(6.45), Inches(0.32))
    tf_f = f_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.alignment = PP_ALIGN.RIGHT
    r_f = p_f.add_run()
    r_f.text = f"NHÓM 8.5-EMG | Thiết kế Hệ truyền động Xe con Cầu trục 10 tấn | {page_str}"
    r_f.font.name = FONT_MAIN
    r_f.font.size = Pt(11)
    r_f.font.color.rgb = C_MUTED

    # 4. Speaker Notes
    if speaker_notes:
        slide.notes_slide.notes_text_frame.text = speaker_notes
    return slide

def add_image_placeholder(slide, left: float, top: float, width: float, height: float,
                          source_instruction: str, caption: str):
    """Vẽ khung chờ nét đứt màu đỏ để người dùng tự chèn hình ảnh thủ công."""
    shape = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height)
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(248, 249, 250)
    shape.line.color.rgb = C_CRIMSON
    shape.line.width = Pt(1.5)
    shape.line.dash_style = MSO_LINE_DASH_STYLE.DASH

    tf = shape.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p1 = tf.paragraphs[0]
    p1.alignment = PP_ALIGN.CENTER
    r1 = p1.add_run()
    r1.text = f"🖼️ [CHÈN HÌNH ẢNH TẠI ĐÂY]\n{source_instruction}\n(Kích thước khung: {width:.2f}\" x {height:.2f}\")"
    r1.font.name = FONT_MAIN
    r1.font.size = Pt(13)
    r1.font.bold = True
    r1.font.color.rgb = C_CRIMSON

    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    r2 = p2.add_run()
    r2.text = f"\n{caption}"
    r2.font.name = FONT_MAIN
    r2.font.size = Pt(11.5)
    r2.font.italic = True
    r2.font.color.rgb = C_MUTED
    return shape
```

---

## PROMPT 2: PROMPT TẠO SLIDE PPTX CHO KHỐI 0 — ĐỊNH NGHĨA HỆ THỐNG & LỰA CHỌN PHƯƠNG ÁN (`GATE MCR` — 21 SLIDES)

> 📋 **Sau khi gửi PROMPT 1, hãy Copy khối PROMPT 2 dưới đây (kèm file `BAO_CAO_SLIDE_PPTX_BLOCK_0_MCR.md` và `Mô tả nguyên lý công nghệ.pptx`) để yêu cầu AI xuất file `Bao_cao_Tien_do_Khoi_0_MCR_Nhom_8_5_EMG.pptx`:**

```markdown
Hãy đọc toàn bộ nội dung file kịch bản chi tiết `BAO_CAO_SLIDE_PPTX_BLOCK_0_MCR.md` và sử dụng file `Mô tả nguyên lý công nghệ.pptx` làm Template gốc để tạo file PowerPoint hoàn chỉnh tên là:
`Bao_cao_Tien_do_Khoi_0_MCR_Nhom_8_5_EMG.pptx` (Tổng cộng **21 Slides = 15 Main Deck Slides + 6 Backup Slides**).

YÊU CẦU THỰC THI CHI TIẾT TỪNG SLIDE:

1. **Slide 01 (Trang bìa — Giữ nguyên Slide 1 của `Mô tả nguyên lý công nghệ.pptx`):**
   - Giữ nguyên toàn bộ nền, Logo HUST, tiêu đề `THIẾT KẾ HỆ TRUYỀN ĐỘNG CƠ CẤU XE CON CẦU TRỤC`, danh sách 6 thành viên `NHÓM 8.5-EMG` và `Giảng viên hướng dẫn: TS. Nguyễn Duy Đỉnh`.
   - Thêm dòng phụ đề tại `pos=(0.81", 3.12")`: `BÁO CÁO TIẾN ĐỘ KHỐI 0 (GATE MCR): NGUYÊN LÝ CÔNG NGHỆ, ĐỊNH NGHĨA HỆ THỐNG (PRD, SOW) & LỰA CHỌN PHƯƠNG ÁN (HOQ, PUGH, ICE)`.

2. **Slide 02 đến Slide 14 (13 Slide Nội dung chính dùng `slideLayout2`):**
   - **Slide 02 (`TỔNG QUAN CẤU TRÚC & PHÂN TÁCH 3 CƠ CẤU CẦU TRỤC`):** Cột trái đặt Khung chờ hình ảnh `pos=(0.34", 1.65"), size=(5.60"x4.90")` (hướng dẫn lấy cụm ảnh cầu trục từ Slide 2 của `Mô tả nguyên lý công nghệ.pptx`); cột phải đặt Bảng so sánh 3 cơ cầu (Di chuyển cầu trục / Di chuyển xe con - Trọng tâm Đề tài 8.5 / Nâng hạ hàng) + Hộp thông số đầu vào ($Q=10\text{ tấn}$, $M_\Sigma=14,244\text{ kg}$, $m_{\text{tĩnh}}=2,022\text{ kg}$, $v_{\text{đm}}=0.5\text{ m/s}$).
   - **Slide 03 (`KẾT CẤU CƠ KHÍ & SƠ ĐỒ TRUYỀN ĐỘNG CƠ CẤU XE CON`):** Cột trái đặt Khung chờ hình ảnh `pos=(0.34", 1.65"), size=(5.80"x4.90")` (hướng dẫn lấy ảnh cụm xe con từ Slide 6 của `Mô tả nguyên lý công nghệ.pptx`); cột phải vẽ chuỗi truyền động 5 khối (`Biến tần 4Q -> Động cơ KĐB 3 pha -> Khớp nối & Phanh điện từ -> Hộp giảm tốc -> Bánh xe chủ động`) và 3 thẻ vật lý ($\mu_r=0.015$, $\mu_{\text{ướt}}=0.12$, $\eta_\Sigma=0.9052$).
   - **Slide 04 (`ĐỘNG LỰC HỌC & RÀO CHẮN VẬT LÝ CỦA TẢI TRỌNG`):** Cột trái đặt Khung chờ hình ảnh `pos=(0.34", 1.65"), size=(5.50"x4.85")` (hướng dẫn lấy ảnh lực tác dụng từ Slide 9 của `Mô tả nguyên lý công nghệ.pptx`); cột phải trình bày 3 hộp công thức đóng khung: (1) Biến thiên khối lượng $7.04:1$ ($14,244\text{ kg}$ vs $2,022\text{ kg}$), (2) Rào chắn bám ray ướt $\mu=0.12 \Rightarrow a_{\max} \le 0.15\text{ m/s}^2$, (3) Bài toán lắc tải $\theta_{\max} \le 1.5^\circ \Rightarrow$ Quỹ đạo S-curve $j_{\max} \le 0.30\text{ m/s}^3$.
   - **Slide 05 (`CHU TRÌNH VẬN HÀNH 4 GIAI ĐOẠN & 4 GÓC PHẦN TƯ (4Q)`):** Nửa trên vẽ 4 thẻ giai đoạn nối tiếp (`GĐ1 Khởi động S-curve -> GĐ2 Chạy đều 0.5 m/s -> GĐ3 Giảm tốc 4Q + Creep 0.030-0.036 m/s -> GĐ4 Khóa phanh tại v=0`); nửa dưới đặt Khung chờ hình ảnh `pos=(0.34", 3.95"), size=(6.00"x2.75")` (lấy sơ đồ từ Slide 12 `Mô tả nguyên lý công nghệ.pptx`) và Bảng 4 góc phần tư `Q1..Q4`.
   - **Slide 06 (`CASE STUDY THỰC TẾ & TỔNG HỢP THÔNG SỐ ĐẦU VÀO KHÓA SỔ`):** Cột trái đặt Khung chờ hình ảnh `pos=(0.34", 1.65"), size=(5.50"x4.95")` (lấy ảnh xe con thực tế từ Slide 15–16 `Mô tả nguyên lý công nghệ.pptx`); cột phải đặt Bảng 8 thông số kỹ thuật khóa sổ (đã hiệu đính chuẩn 100% theo `SE_RULES.md`: $M_\Sigma=14,244\text{ kg}$, $m_{\text{tĩnh}}=2,022\text{ kg}$, $D \ge 10:1$, $v_{\text{creep}} \in [0.030;\ 0.036]\text{ m/s}$, $|\delta s_{\text{ss}}| \le 2.0\text{ mm}$).
   - **Slide 07 (`PHÁT BIỂU BÀI TOÁN & 5 NỖI ĐAU KỸ THUẬT CỐT LÕI (PRD)`):** Bảng 5 nỗi đau kỹ thuật (`Trượt bánh xe ray ướt`, `Lắc tải con lắc`, `Trôi vị trí khi đóng phanh`, `Quá áp DC-Link khi hãm tái sinh`, `Biến thiên tải 7.04 lần & tăng R_r +35%`) đối chiếu với Yêu cầu rào chắn định lượng.
   - **Slide 08 (`PHẠM VI CÔNG VIỆC (SOW) & CẤU TRÚC PHÂN RÃ (WBS 5 KHỐI)`):** Nửa trên vẽ sơ đồ 5 hộp ngang `WBS Khối 0 -> Khối 1 -> Khối 2 -> Khối 3 -> Khối 4`; nửa dưới vẽ 2 hộp đối lập `TRONG PHẠM VI (IN-SCOPE)` (viền xanh lá `#107C41`) và `NGOÀI PHẠM VI (OUT-OF-SCOPE)` (viền đỏ `#C00000`).
   - **Slide 09 (`TIẾNG NÓI KHÁCH HÀNG (VOC) & NGÔI NHÀ CHẤT LƯỢNG (QFD / HOQ)`):** Cột trái vẽ Biểu đồ Thanh ngang xếp hạng tỷ trọng 6 đặc tính kỹ thuật `EC` (`EC3 Sai số dừng & tốc độ: 21.8%`, `EC2 Gia tốc & Jerk S-curve: 19.4%`, `EC1 Dải điều chỉnh D>=10:1: 17.5%`, `EC4 Hãm 4Q: 15.2%`, `EC5 Quá tải 1.5x: 13.6%`, `EC6 Chi phí & Độ tin cậy: 12.5%`); cột phải là Bảng Top 5 cặp tương tác kỹ thuật trong HoQ.
   - **Slide 10 (`MA TRẬN QUYẾT ĐỊNH PUGH — LỰA CHỌN PHƯƠNG ÁN ĐỘNG CƠ`):** Bảng so sánh 4 phương án động cơ (`PA1 DC kích từ độc lập - Datum 0`, `PA2 KĐB 3 pha Rô-to dây quấn: -3`, `PA3 KĐB 3 pha Rô-to lồng sóc: +11 CHỐT CHỌN`, `PA4 PMSM: +3`). Tô nền xanh lá `#E8F5E9` cho cột `PA3`.
   - **Slide 11 (`PHÂN TÍCH ĐA TIÊU CHÍ ICE — LỰA CHỌN PHƯƠNG ÁN BIẾN TẦN`):** Bảng điểm `ICE` (`Impact x Confidence x Ease`) cho 4 phương án điều khiển (`BB1 Điện trở phụ: 140`, `BB2 Khởi động mềm: 216`, `BB3 Biến tần V/f vòng hở: 384`, `BB4 Biến tần 4Q điều khiển Vector FOC có Encoder + R_brake: 720 CHỐT CHỌN`).
   - **Slide 12 (`KIẾN TRÚC TỔNG THỂ HỆ TRUYỀN ĐỘNG CHỐT CHỌN`):** Cột trái đặt Khung chờ hình ảnh `pos=(0.34", 1.65"), size=(5.60"x3.20")` (lấy ảnh tủ biến tần & động cơ từ Slide 17 `Mô tả nguyên lý công nghệ.pptx`); cột phải và bên dưới vẽ Sơ đồ khối kiến trúc điều khiển 3 vòng (`S-Curve Generator -> Vòng Vị trí P -> Vòng Tốc độ PI/PID có lọc N -> Vòng Dòng điện FOC (i_sd=const, i_sq) -> Biến tần 4Q + Chopper 680V -> Động cơ KĐB + Encoder 1024 PPR`).
   - **Slide 13 (`MA TRẬN PHÒNG THỦ RỦI RO KỸ THUẬT (TOP 5 RISKS)`):** Bảng 5 rủi ro kỹ thuật (`R1 Trượt bánh ray ướt`, `R2 Nổ tụ DC-Link khi hãm`, `R3 Lệch vị trí do trễ phanh cơ`, `R4 Lệch thông số R_r +35%`, `R5 Gai dòng điện do đạo hàm nhiễu Encoder`) kèm Giải pháp khóa cứng ngay từ thiết kế.
   - **Slide 14 (`KIỂM ĐỊNH CỔNG MCR (EXIT CRITERIA) & BÀN GIAO SANG KHỐI 1`):** Bảng 6 tiêu chí cổng `MCR-01..MCR-06` đạt `100% PASS` + Thanh quyết định màu xanh lá bàn giao sang Khối 1 (`Gate SRR-EVT`).

3. **Slide 15 (Trang Kết thúc Main Deck — Dùng `slideLayout4` của Template HUST):**
   - Khung trên bên phải (`pos=(5.20", 0.65"), size=(7.70"x2.35")`): Danh mục 4 Tài liệu tham khảo chuẩn (Sách Cơ sở TĐĐ, Điều chỉnh tự động TĐĐ, NASA SP-2016-6105, TCVN 4244:2005).
   - Giữa bên phải (`pos=(5.72", 3.12")`): Chữ `THANK YOU !` (`Arial 56pt Bold #C00000`).
   - Dưới chữ `THANK YOU !`: Dòng chữ mời Hội đồng đặt câu hỏi (`18pt Bold #0E2841`).

4. **Slide 16 đến Slide 21 (6 Slide Phụ lục Bảo vệ Hội đồng `B0-1` đến `B0-6` dùng `slideLayout2`):**
   - `B0-1`: Bảng đầy đủ 14 Nhu cầu Khách hàng (`Need #1..#14`) & 21 Thông số Đích (`Target Specs`).
   - `B0-2`: Bảng tính chi tiết Ma trận Ngôi nhà Chất lượng `HoQ` đầy đủ.
   - `B0-3`: Bảng điểm chi tiết Ma trận `Pugh` 8 tiêu chí cho 4 phương án động cơ.
   - `B0-4`: Bảng chấm điểm chi tiết `ICE` & phân tích ưu/nhược điểm 4 phương án biến tần.
   - `B0-5`: Chứng minh công thức quy đổi Lực cản tĩnh ($F_{\text{cản}}=2,096\text{ N}$), Công suất tĩnh ($P_{\text{tĩnh}}=1.158\text{ kW}$) và điều kiện chống trượt bánh xe ($K_{\text{bám}}=1.90$).
   - `B0-6`: Cấu trúc WBS chi tiết 5 khối và Lộ trình 5 Cổng kiểm duyệt (`MCR -> SRR -> PDR -> CDR -> SAR`).
```

---

## PROMPT 3: PROMPT TẠO SLIDE PPTX CHO KHỐI 1 — PHÂN TÍCH YÊU CẦU KỸ THUẬT & RÀO CHẮN VẬT LÝ (`GATE SRR-EVT` — 22 SLIDES)

> 📋 **Sau khi gửi PROMPT 1, hãy Copy khối PROMPT 3 dưới đây (kèm file `BAO_CAO_SLIDE_PPTX_BLOCK_1_SRR.md` và `Mô tả nguyên lý công nghệ.pptx`) để yêu cầu AI xuất file `Bao_cao_Tien_do_Khoi_1_SRR_Nhom_8_5_EMG.pptx`:**

```markdown
Hãy đọc toàn bộ nội dung file kịch bản chi tiết `BAO_CAO_SLIDE_PPTX_BLOCK_1_SRR.md` và sử dụng file `Mô tả nguyên lý công nghệ.pptx` làm Template gốc để tạo file PowerPoint hoàn chỉnh tên là:
`Bao_cao_Tien_do_Khoi_1_SRR_Nhom_8_5_EMG.pptx` (Tổng cộng **22 Slides = 16 Main Deck Slides + 6 Backup Slides**).

YÊU CẦU THỰC THI CHI TIẾT TỪNG SLIDE:

1. **Slide 01 (Trang bìa — Giữ nguyên Slide 1 của `Mô tả nguyên lý công nghệ.pptx`):**
   - Giữ nguyên 100% nền, Logo HUST, tiêu đề `THIẾT KẾ HỆ TRUYỀN ĐỘNG CƠ CẤU XE CON CẦU TRỤC`, danh sách 6 thành viên `NHÓM 8.5-EMG` và `Giảng viên hướng dẫn: TS. Nguyễn Duy Đỉnh`.
   - Thêm dòng phụ đề tại `pos=(0.81", 3.12")`: `BÁO CÁO TIẾN ĐỘ KHỐI 1 (GATE SRR-EVT): ĐẶC TẢ YÊU CẦU HỆ THỐNG (SRS), SƠ ĐỒ RANH GIỚI, P-DIAGRAM, RTM & DVP&R`.

2. **Slide 02 đến Slide 15 (14 Slide Nội dung chính dùng `slideLayout2`):**
   - **Slide 02 (`I. TỔNG QUAN KHỐI 1 — KIẾN TRÚC RÀO CHẮN KỸ THUẬT (SRR-EVT)`):** Hàng trên vẽ 4 Thẻ KPI (`26 REQ 100% Định lượng`, `12 Luồng ICD Khóa 3 Phân vùng`, `6 Nhiễu N1..N6 trên P-Diagram`, `14 Bài Test DV & 100% RTM`); hàng dưới vẽ sơ đồ chuỗi liên kết 7 văn kiện Khối 1 (`SRS -> Boundary -> P-Diagram -> RTM -> DVP&R -> Simulink Pre-Audit -> Gate SRR-EVT`).
   - **Slide 03 (`II. SƠ ĐỒ RANH GIỚI HỆ THỐNG (SYSTEM BOUNDARY DIAGRAM)`):** Giữa slide vẽ Khung chờ hình ảnh lớn `pos=(0.50", 1.62"), size=(12.30"x4.20")` (ghi rõ hướng dẫn: `Copy cụm hình Sơ đồ Ranh giới tổng thể ở Slide 5 của file SRS-diagram.pptx dán vào đây`); phía dưới (`y=6.00"`) đặt 3 hộp tóm tắt 3 phân vùng (`Môi trường ngoài` / `Hệ truyền động xe con IN-SCOPE` / `Phần tải EXTERNAL LOAD 14,244 kg`).
   - **Slide 04 (`II. SƠ ĐỒ RANH GIỚI HỆ THỐNG — GIAO DIỆN VẬT LÝ (ICD)`):** Cột trái đặt 3 Khung chờ hình ảnh xếp dọc tại `pos=(0.34", 1.65"/3.30"/5.05"), size=(5.00"x1.55")` (ghi rõ hướng dẫn lấy 3 ảnh cắt phóng to từ **Slide 6, Slide 7, Slide 8 của file `SRS-diagram.pptx`**); cột phải đặt Bảng 6 luồng giao diện `ICD` cốt lõi (`IF-E01`, `IF-E02`, `IF-M01`, `IF-M02`, `IF-S01`, `IF-S02`).
   - **Slide 05 (`III. ĐẶC TẢ YÊU CẦU KỸ THUẬT (SRS) — NHÓM A & NHÓM B`):** Bảng 7 mã yêu cầu `REQ-A01..A05` và `REQ-B01..B02` (Khối lượng $14,244\text{ kg}$ / $2,022\text{ kg}$, $v_{\text{đm}}=0.5\text{ m/s}$, $a_{\max} \le 0.15\text{ m/s}^2$, $j_{\max} \le 0.30\text{ m/s}^3$, $K_{\text{bám}} \ge 1.20$, $F_{\text{cản}} \approx 2,096\text{ N}$, $P_{\text{tĩnh}} \approx 1.158\text{ kW}$) + Hộp công thức kiểm chứng chống trượt bánh xe ($K_{\text{bám}} = 8,384 / 4,404 = 1.90 \ge 1.20$).
   - **Slide 06 (`III. ĐẶC TẢ YÊU CẦU KỸ THUẬT (SRS) — NHÓM C & NHÓM D`):** Bảng 7 mã yêu cầu `REQ-C01..C04` và `REQ-D01..D03` (Dải điều chỉnh $D \ge 10:1$, mục tiêu $15:1$; $v_{\text{creep}} \in [0.030;\ 0.036]\text{ m/s}$; độ cứng $\Delta\omega_{\text{ss}} \le 0.5\%$; sai số dừng vị trí $|\delta s_{\text{ss}}| \le 2.0\text{ mm}$; quá điều chỉnh $\sigma\% \le 5.0\%$) + Hộp lý giải toán học vì sao phải có `Creep Speed` để bù trễ đóng phanh cơ khí $50\text{ ms}$.
   - **Slide 07 (`III. ĐẶC TẢ YÊU CẦU KỸ THUẬT (SRS) — NHÓM E (4Q & QUÁ TẢI)`):** Bảng 5 mã yêu cầu `REQ-E01..E05` (Vận hành 4 góc phần tư `4Q`, trần quá tải $T_{\max} \le 1.5\cdot T_{\text{đm}}$ & $I_{s,\max} \le 1.5\cdot I_{\text{đm}}$, Chopper đóng tại $680\text{ VDC}$ giữ $V_{dc,\max} < 750\text{ VDC}$, chế độ `S3-40%`, kiểm nghiệm nhiệt $T_{\text{rms}} \le T_{\text{đm}}$) + 4 Hộp trạng thái năng lượng `Q1, Q2, Q3, Q4`.
   - **Slide 08 (`III. ĐẶC TẢ YÊU CẦU KỸ THUẬT (SRS) — NHÓM F & NHÓM G`):** Bảng 7 mã yêu cầu `REQ-F01..F04` và `REQ-G01..G03` (Phối hợp phanh `Zero-Speed` $\Delta t_{\text{hold}}=100\text{–}200\text{ ms}$, góc lắc $\theta_{\max} \le 1.5^\circ$, bền vững khi sụt áp $-15\%$ & $R_r +35\%$, bảo vệ liên động, chuẩn vỏ tủ `IP54`, Encoder `1024 PPR`) + Sơ đồ quy trình khóa phanh `Zero-Speed Servo Lock`.
   - **Slide 09 (`IV. PHÂN TÍCH BỀN VỮNG — SƠ ĐỒ THAM SỐ (P-DIAGRAM)`):** Giữa slide vẽ Khung chờ hình ảnh lớn `pos=(0.50", 1.62"), size=(12.30"x4.35")` (ghi rõ hướng dẫn: `Copy tổ hợp 5 hình P-Diagram ở Slide 9 của file SRS-diagram.pptx dán vào đây`); phía dưới đặt 5 ô tóm tắt (`Tín hiệu vào M`, `Nhiễu N1..N6`, `Tham số Điều khiển C1..C6`, `Đáp ứng Lý tưởng Y`, `Trạng thái Lỗi E`).
   - **Slide 10 (`IV. PHÂN TÍCH BỀN VỮNG — MA TRẬN ĐỐI KHÁNG NHIỄU (ROBUSTNESS MATRIX)`):** Bảng 6 dòng đối kháng trực tiếp giữa 6 yếu tố nhiễu cực đoan `N1..N6` (`Biến thiên tải 7.04x`, `Ray ướt mu=0.12`, `Dao động lắc cáp`, `Tăng R_r +35%`, `Sụt áp -15% & Hãm tái sinh`, `Nhiễu lượng tử hóa Encoder & Trễ phanh`) với 6 cơ chế điều khiển đối kháng `C1..C6`.
   - **Slide 11 (`V. MA TRẬN TRUY XUẤT NGUỒN GỐC 2 CHIỀU (BI-DIRECTIONAL RTM)`):** Cột trái vẽ Sơ đồ Phễu Truy xuất 4 tầng (`14 Needs <-> 26 SRS REQs <-> 21 Target Specs <-> 14 DV Tests`) và 4 Hộp KPI đạt `100%` (`0% Orphan / 0% Gold-Plating`); cột phải đặt Bảng 6 tuyến truy xuất xương sống.
   - **Slide 12 (`VI. KẾ HOẠCH KIỂM CHỨNG (DVP&R) — 4 KỊCH BẢN MÔ PHỎNG (TS-01..TS-04)`):** Cột trái đặt Bảng 4 kịch bản mô phỏng chuẩn hóa (`TS-01 Định vị & Creep 25s`, `TS-02 Đảo chiều 4Q 30s`, `TS-03 Bền vững nhiễu R_r +35% 20s`, `TS-04 Phối hợp phanh Zero-Speed 10s`); cột phải đặt 2 Khung chờ hình ảnh xếp dọc tại `pos=(7.65", 1.65"), size=(5.30"x2.35")` (chèn file `Hinh_3_2_Quy_dao_S_curve.jpg`) và `pos=(7.65", 4.25"), size=(5.30"x2.35")` (chèn file `Hinh_3_3_Dac_tinh_4_goc_phan_tu.jpg`).
   - **Slide 13 (`VI. KẾ HOẠCH KIỂM CHỨNG (DVP&R) — TIÊU CHÍ ĐẠT / KHÔNG ĐẠT (PASS/FAIL)`):** Bảng 7 bài kiểm thử sát hạch gắt nhất (`DV-02, DV-03, DV-05, DV-06, DV-08, DV-09, DV-12`) với 2 cột đối lập rõ ràng: `Ngưỡng Đạt (PASS Criteria)` (chữ xanh lá `#107C41`) và `Ngưỡng Bác bỏ (FAIL Criteria)` (chữ đỏ `#C00000`).
   - **Slide 14 (`VII. TIỀN KIỂM TOÁN MÔ PHỎNG SIMULINK (SIMULINK PRE-AUDIT)`):** Chia 2 khung đối lập: Cột trái (viền đỏ `#C00000`, nền `#FFF5F5`) trình bày Cạm bẫy Đạo hàm lý tưởng $K_d\cdot s$ khuếch đại nhiễu lượng tử hóa Encoder làm vọt dòng $I_{\text{peak}} \gg 1.5\cdot I_{\text{đm}}$; Cột phải (viền xanh lá `#107C41`, nền `#E8F5E9`) trình bày Rào chắn Toán học bắt buộc: Bộ lọc Đạo hàm `Derivative Filter` $G_c(s) = K_p + K_i/s + K_d \cdot N/(1 + N/s)$ với $N \in [20;\ 100]\text{ rad/s}$ kèm `Anti-Windup` và tiền lọc `S-Curve`.
   - **Slide 15 (`VIII. KIỂM ĐỊNH CỔNG SRR-EVT (EXIT CRITERIA) & BÀN GIAO SANG KHỐI 2`):** Bảng nghiệm thu `11/11` tiêu chí (`SRR-01..05` và `EVT-01..04`) đạt `PASS 100%` + Thanh quyết định màu xanh lá đóng băng `SRS Baseline` và mở khóa Khối 2.

3. **Slide 16 (Trang Kết thúc Main Deck — Dùng `slideLayout4` của Template HUST / Slide 10 `SRS-diagram.pptx`):**
   - Khung trên bên phải (`pos=(5.20", 0.65"), size=(7.70"x2.35")`): Danh mục 4 Tài liệu tham khảo chuẩn.
   - Giữa bên phải (`pos=(5.72", 3.12")`): Chữ `THANK YOU !` (`Arial 56pt Bold #C00000`).
   - Dưới chữ `THANK YOU !`: Dòng chữ cảm ơn và mời Hội đồng đặt câu hỏi (`18pt Bold #0E2841`).

4. **Slide 17 đến Slide 22 (6 Slide Phụ lục Bảo vệ Hội đồng `B1-1` đến `B1-6` dùng `slideLayout2`):**
   - `B1-1`: Bảng đầy đủ Đặc tả Yêu cầu Kỹ thuật `SRS` — Phần 1 (`REQ-A01` đến `REQ-D03`, 15 mã đầu).
   - `B1-2`: Bảng đầy đủ Đặc tả Yêu cầu Kỹ thuật `SRS` — Phần 2 (`REQ-E01` đến `REQ-G03`, 11 mã cuối).
   - `B1-3`: Bảng đầy đủ 12 luồng giao diện vật lý `ICD` trên Sơ đồ Ranh giới.
   - `B1-4`: Phân tích định lượng sâu phương trình vật lý của 6 nguồn nhiễu `N1..N6` trên `P-Diagram`.
   - `B1-5`: Bảng Ma trận Truy xuất Nguồn gốc `RTM` đầy đủ 26 dòng (`14 Needs <-> 26 REQs <-> 21 Specs <-> 14 DVs`).
   - `B1-6`: Bảng Danh mục đầy đủ 14 bài kiểm thử `DV-01` đến `DV-14` (`DVP&R`).
```
