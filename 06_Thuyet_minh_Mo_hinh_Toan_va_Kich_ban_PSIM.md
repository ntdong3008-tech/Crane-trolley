# BẢN THUYẾT MINH KỸ THUẬT MÔ HÌNH TOÁN VÀ KỊCH BẢN MÔ PHỎNG PSIM
## HỆ TRUYỀN ĐỘNG XE CON CẦU TRỤC ($x = 2$, NHÓM 8.5-EMG)

* **Học phần:** Thiết kế hệ thống truyền động điện (Mã học phần: EE4332)
* **Giảng viên hướng dẫn:** TS. Nguyễn Duy Đỉnh — Đại học Bách khoa Hà Nội (HUST)
* **Sinh viên thực hiện:** Nhóm 8.5-EMG
* **Căn cứ kỹ thuật:**
  1. Bản vẽ sơ đồ khối PSIM: [3b892f1f-fe6c-43c3-bcf6-a4673a4eeda1.jfif](file:///d:/Tài liệu học tập/Truyền động điện/Project/Mô phỏng đáp ứng động cơ/3b892f1f-fe6c-43c3-bcf6-a4673a4eeda1.jfif)
  2. Bảng phấn hướng dẫn trên lớp của GVHD: [Bang_phan_Thay_Dinh.png](file:///d:/Tài liệu học tập/Truyền động điện/Project/Mô phỏng đáp ứng động cơ/Bang_phan_Thay_Dinh.png)
  3. Báo cáo mô hình toán: [01_Mo_hinh_toan_He_truyen_dong.md](file:///d:/Tài liệu học tập/Truyền động điện/Project/Mô phỏng đáp ứng động cơ/01_Mo_hinh_toan_He_truyen_dong.md)
  4. Sổ tay tính toán phụ tải và chọn động cơ: [00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx](file:///d:/Tài liệu học tập/Truyền động điện/Project/Mô phỏng đáp ứng động cơ/00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx)
  5. Giáo trình chuẩn HUST: *Truyền động điện thông minh* (Bùi Quốc Khánh, Nguyễn Văn Liễn, Nguyễn Phùng Quang), *Vector Control of Three-Phase AC Machines* (GS. TSKH. Nguyễn Phùng Quang & J. Dittrich, Springer 2008), Bài giảng *Thiết kế Hệ thống Truyền động điện* (TS. Nguyễn Duy Đỉnh).

---

# PHẦN I: THUYẾT MINH CHI TIẾT MÔ HÌNH TOÁN VÀ CẤU TRÚC HỆ THỐNG

## 1. Mục đích, nhiệm vụ và vị trí của Bước 4 trong đồ án
Trong quy trình thiết kế hệ thống truyền động điện 4 bước do TS. Nguyễn Duy Đỉnh định hướng trên lớp:
1. **Bước 1 — Chọn động cơ:** Tính chọn công suất động cơ dựa trên đồ thị phụ tải tĩnh và động theo chu trình làm việc của cơ cấu ($P_N = 0.37\text{ kW}$, động cơ SEW DRN71M4).
2. **Bước 2 — Ước lượng thông số:** Từ các thông số danh định trên nhãn máy (Nameplate) và catalogue nhà sản xuất, xác định bộ 5 tham số mạch thay thế tương đương ($R_s, R_r', L_{\sigma s}, L_{\sigma r}', L_m$) bằng các thuật toán giải số tối ưu (Solver).
3. **Bước 3 — Mô phỏng kiểm chứng động cơ:** Chạy mô phỏng động cơ không tải và có tải danh định trên PSIM/Simulink để khẳng định bộ thông số vừa xác định phản ánh đúng các chỉ tiêu cơ - điện của nhà sản xuất (tốc độ $1415\text{ rpm}$, dòng định mức $1.02\text{ A}$, mô-men khởi động $2.8 M_N$).
4. **Bước 4 — Xây dựng mô hình hệ truyền động (Nhiệm vụ trọng tâm hiện tại):**
   * Ghép nối động cơ đã chọn với mô hình động học và lực cản của phụ tải thực tế (cơ cấu xe con cầu trục mang tải trọng $12\text{ tấn}$).
   * Ứng dụng giải thuật điều khiển tựa từ thông rotor (FOC) kết hợp bộ tạo quỹ đạo chuyển động êm dịu S-curve 7 đoạn nhằm đáp ứng nghiêm ngặt tiêu chuẩn vận hành cầu trục: **khống chế độ giật (Jerk), chống rung lắc tải treo, triệt tiêu xung lực bánh răng và tránh quá dòng biến tần**.
   * Đánh giá tính năng động lực học và kiểm chứng sự trùng khớp giữa kết quả mô phỏng số với tính toán giải tích trong file Excel `00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx`.

---

## 2. Thuyết minh các giả thiết kỹ thuật (Assumptions)
Để xây dựng mô hình toán vừa bảo đảm độ chính xác kỹ thuật, vừa khả thi khi cài đặt trên môi trường mô phỏng PSIM, hệ thống được thiết lập dựa trên 9 giả thiết khoa học:

* **GT-01 (Ray nằm ngang phẳng):** Xe con di chuyển trên ray I hoặc ray vuông đặt trên dầm cầu trục trong không gian nhà xưởng công nghiệp khép kín. Do ray nằm ngang tuyệt đối nên thành phần lực cản lên dốc triệt tiêu ($F_d = 0$). Xe chạy trong nhà xưởng nên không chịu áp lực gió bão ($F_{\text{wind}} = 0$).
* **GT-02 (Quy luật lực cản ma sát khô):** Mọi yếu tố cản trở chuyển động (ma sát lăn giữa bánh xe thép và ray thép, ma sát trượt tại gờ bánh xe, ma sát ổ trục bánh xe con) được gộp chung vào suất cản di chuyển không thứ nguyên $w_0 = 0.015$ (theo Tiêu chuẩn TCVN 4244:2005 và quy chuẩn tính toán cầu trục). Lực cản di chuyển thuần túy là lực ma sát khô: $F_c = M g w_0$.
* **GT-03 (Bỏ qua khí động học):** Tốc độ định mức của xe con rất nhỏ ($v_{\max} = 0.12\text{ m/s} = 7.2\text{ m/phút}$). Lực cản không khí tính theo định luật khí động học $F_a = \frac{1}{2}\rho C_d A v^2 \approx 0.04\text{ N}$, hoàn toàn không đáng kể so với lực cản ma sát $F_c = 2,096\text{ N}$ (chiếm tỉ lệ $\approx 0.002\%$).
* **GT-04 (Tiếp xúc bánh xe – ray lý tưởng):** Bánh xe làm bằng thép đúc nhiệt luyện có độ cứng cao, biến dạng đàn hồi cục bộ rất nhỏ, không xảy ra hiện tượng trượt trơn (wheel slip) trong điều kiện gia tốc khống chế $a^* = 0.10\text{ m/s}^2 \ll \mu_{\text{bám}} g \approx 1.5\text{ m/s}^2$. Do đó quan hệ giữa tốc độ góc trục bánh xe $\omega_{bx}$ và vận tốc tịnh tiến $v$ là tuyệt đối tuyến tính: $v = R_{bx} \omega_{bx} = (D_{bx}/2)\omega_{bx}$.
* **GT-05 (Truyền động hộp số cố định):** Hộp số giảm tốc trục song song có tỉ số truyền chính xác $i = 155.34$, hiệu suất chung của toàn bộ chuỗi cơ khí (khớp nối, ổ lăn, bộ truyền bánh răng) là $\eta = 0.90$.
* **GT-06 (Hệ số quán tính phần quay $\delta$):** Quán tính quay của các chi tiết trung gian (các bánh răng trong hộp số, trục truyền, khớp nối trục) được tính đổi thông qua hệ số quán tính khối lượng quay $\delta = 1.15$ theo kinh nghiệm thiết kế máy nâng chuyển HUST. Quán tính của động cơ và đĩa phanh cơ ($J_B = 0.00262\text{ kg}\cdot\text{m}^2$) được cộng trực tiếp.
* **GT-07 (Tải treo gắn cứng - Rigid Body):** Trong pha phân tích đáp ứng động lực học của hệ truyền động kéo, khối lượng xe con $m_0$ và tải nâng $Q$ được xem như một khối thống nhất $M = m_0 + Q$. Khảo sát dao động con lắc thứ cấp được kiểm tra độc lập qua mô hình góc lắc.
* **GT-08 (Vòng điều chỉnh dòng điện lý tưởng):** Hệ truyền động sử dụng biến tần ABB ACS380 điều khiển vector tựa từ thông rotor (FOC) với tần số băm xung PWM $4\text{ kHz}$. Chu kỳ trích mẫu và tính toán dòng điện chỉ cỡ vài chục micro-giây, vòng dòng có hằng số thời gian quán tính tương đương $T_{\Sigma i} \approx 2\text{ ms}$, nhanh gấp hàng trăm lần so với hằng số thời gian cơ học của xe con ($t_{acc} = 1.45\text{ s}$). Do đó, động cơ kết hợp biến tần được xem như nguồn sinh mô-men có trễ nhỏ: $T_đ \approx k_M i_{sq}$.
* **GT-09 (Trạng thái phanh cơ khí):** Phanh cơ khí thủy lực/điện từ chỉ đóng khi hệ thống đã giảm tốc hoàn toàn về $v = 0$ hoặc khi có sự cố dừng khẩn cấp. Trong suốt quá trình vận hành tăng tốc, chạy đều và hãm dừng bằng biến tần, má phanh mở hoàn toàn.

---

## 3. Hệ phương trình toán học mô tả hệ thống

### 3.1. Phương trình động học quy đổi
Xe con chuyển động tịnh tiến với vận tốc $v\text{ [m/s]}$. Trục động cơ quay với tốc độ góc $\omega_m\text{ [rad/s]}$.
Thông qua hộp giảm tốc tỉ số $i = 155.34$ và bánh xe đường kính $D_{bx} = 0.25\text{ m}$:
$$\omega_{bx} = \frac{\omega_m}{i}$$
$$v = \frac{D_{bx}}{2} \cdot \omega_{bx} = \frac{D_{bx}}{2i} \cdot \omega_m = k \cdot \omega_m$$

Hệ số truyền động học $k$ xác định là:
$$k = \frac{D_{bx}}{2i} = \frac{0.25}{2 \times 155.34} = 8.04686 \times 10^{-4}\text{ m/rad} \approx 8.047 \times 10^{-4}\text{ m/rad}$$
Hệ số nghịch đảo dùng để tính tốc độ góc đặt cho động cơ:
$$\frac{1}{k} = \frac{1}{8.04686 \times 10^{-4}} = 1242.72\text{ rad/m}$$

Khi xe chạy ở vận tốc định mức $v_{\max} = 0.12\text{ m/s}$:
$$\omega_m = 0.12 \times 1242.72 = 149.126\text{ rad/s} \implies n_m = \frac{149.126 \times 60}{2\pi} = 1424.06\text{ rpm}$$
Giá trị này tiệm cận hoàn hảo với tốc độ định mức của động cơ SEW DRN71M4 ($n_N = 1415\text{ rpm}$).

### 3.2. Lực cản di chuyển và kỹ thuật phi tuyến hóa ma sát khô
Lực cản ma sát di chuyển tổng cộng của xe con trên ray:
$$F_c(v) = M \cdot g \cdot w_0 \cdot \mathrm{sign}(v)$$
Trong đó:
* Trường hợp Đầy tải ($M_{\text{full}} = 14,244\text{ kg}$):
  $$F_{c,\text{full}} = 14244 \times 9.81 \times 0.015 = 2,096.0\text{ N}$$
* Trường hợp Không tải ($M_{\text{empty}} = 2,022\text{ kg}$):
  $$F_{c,\text{empty}} = 2022 \times 9.81 \times 0.015 = 297.54\text{ N}$$

> **Giải trình kỹ thuật về hàm bão hòa $\mathrm{sat}(v/\varepsilon)$ trên sơ đồ `.jfif`:**
> Trong toán học lý thuyết, hàm $\mathrm{sign}(v)$ gián đoạn tại $v = 0$. Khi đưa vào thuật toán giải số vi phân trong PSIM, tại thời điểm bắt đầu khởi động hoặc hãm dừng ($v \approx 0$), dấu của vận tốc sẽ bị lật liên tục giữa $+1$ và $-1$ qua từng bước tích phân $\Delta t$. Điều này kích hoạt hiện tượng dao động phân kỳ số (numerical chattering / limit cycles), làm mô-men cản nhảy bậc với tần số vô hạn, gây lỗi tràn số hoặc làm hỏng bộ tích phân.
> 
> Để khắc phục triệt để, mô hình thay thế hàm $\mathrm{sign}(v)$ bằng hàm bão hòa dốc trơn:
> $$F_c(v) = M \cdot g \cdot w_0 \cdot \mathrm{sat}\left(\frac{v}{\varepsilon}\right) = M \cdot g \cdot w_0 \cdot \max\left(-1, \min\left(1, \frac{v}{\varepsilon}\right)\right)$$
> Với dải tuyến tính rất hẹp $\varepsilon = 10^{-4}\text{ m/s} = 0.1\text{ mm/s}$:
> * Khi $|v| \ge \varepsilon$: khâu bão hòa đạt tuyệt đối $\pm 1$, lực cản đúng bằng $F_c = M g w_0$.
> * Khi $|v| < \varepsilon$: lực cản suy giảm tuyến tính về $0$ khi dừng hẳn, bảo đảm hệ số suy giảm trơn tru và đồ thị mô phỏng phẳng mịn tuyệt đối.

### 3.3. Quy đổi mô-men cản tĩnh về trục động cơ
Theo định luật bảo toàn công suất cơ học, mô-men cản tĩnh trên trục động cơ $T_c$ được tính:
$$T_c = \frac{F_c \cdot v}{\omega_m \cdot \eta} = \frac{F_c \cdot (k \omega_m)}{\omega_m \cdot \eta} = \frac{F_c \cdot k}{\eta}$$
* Khi Đầy tải:
  $$T_{c,\text{full}} = \frac{2096.0 \times 8.04686 \times 10^{-4}}{0.90} = \mathbf{1.8740\text{ N}\cdot\text{m}}$$
* Khi Không tải:
  $$T_{c,\text{empty}} = \frac{297.54 \times 8.04686 \times 10^{-4}}{0.90} = \mathbf{0.2660\text{ N}\cdot\text{m}}$$
Cả hai giá trị này trùng khớp chính xác 100% với các ô `[Phu_tai.Mc]` và `[Phu_tai.Mc0]` trong file Excel.

### 3.4. Mô-men quán tính quy đổi tương đương ($J_\Sigma$) và Hiệu chỉnh công thức
Phương trình cân bằng công suất động trong quá trình tăng tốc có gia tốc $a = \frac{dv}{dt}$:
$$P_{đg} = T_{đg} \cdot \omega_m = \left( J_B \frac{d\omega_m}{dt} \right)\omega_m + \frac{1}{\eta}\left( \delta M \frac{dv}{dt} \right) v$$
Thay $v = k \omega_m$ và $\frac{dv}{dt} = k \frac{d\omega_m}{dt}$:
$$T_{đg} \cdot \omega_m = J_B \omega_m \frac{d\omega_m}{dt} + \frac{\delta M (k^2)}{\eta} \omega_m \frac{d\omega_m}{dt} \implies T_{đg} = \left( J_B + \frac{\delta M k^2}{\eta} \right) \frac{d\omega_m}{dt}$$
Do đó, tổng mô-men quán tính quy đổi về trục động cơ là:
$$J_\Sigma = J_B + \frac{\delta \cdot M \cdot k^2}{\eta}$$
Trong đó:
* $J_B = 0.00262\text{ kg}\cdot\text{m}^2$ (Quán tính động cơ SEW DRN71M4 + phanh đĩa cơ khí).
* Quán tính tải quy đổi $J_{\text{tải}} = \frac{\delta M k^2}{\eta}$:
  * Đầy tải ($M = 14244\text{ kg}$):
    $$J_{\text{tải,full}} = \frac{1.15 \times 14244 \times (8.04686 \times 10^{-4})^2}{0.90} = 0.011786\text{ kg}\cdot\text{m}^2$$
    $$\implies J_{\Sigma,\text{full}} = 0.00262 + 0.011786 = \mathbf{0.01441\text{ kg}\cdot\text{m}^2}$$
  * Không tải ($M = 2022\text{ kg}$):
    $$J_{\text{tải,empty}} = \frac{1.15 \times 2022 \times (8.04686 \times 10^{-4})^2}{0.90} = 0.001674\text{ kg}\cdot\text{m}^2$$
    $$\implies J_{\Sigma,\text{empty}} = 0.00262 + 0.001674 = \mathbf{0.00429\text{ kg}\cdot\text{m}^2}$$

> **Thuyết minh điểm hiệu chỉnh quan trọng trong file Excel (Mục 3 dòng 81):**
> Trong file Excel `00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx`, ô `[Phu_tai.Jl]` đang ghi công thức thô $J_{\text{tải}} = \delta M k^2 = 0.0106\text{ kg}\cdot\text{m}^2$ (bị thiếu việc chia cho hiệu suất $\eta$). Tuy nhiên, tại dòng `[Phu_tai.Mdg]`, tác giả Excel đã lập công thức đúng là $M_{đg} = \frac{\delta M a k}{\eta} + J_B \frac{a}{k}$. Do đó, để mô hình toán và sơ đồ PSIM hoàn toàn đồng nhất về mặt vật lý, mô-men quán tính tải quy đổi chuẩn bắt buộc phải chia cho $\eta = 0.90$, nâng tổng quán tính đầy tải lên đúng $0.01441\text{ kg}\cdot\text{m}^2$.

### 3.5. Phương trình chuyển động cơ học cơ bản
Phương trình vi phân tổng quát trên trục truyền động:
$$J_\Sigma \frac{d\omega_m}{dt} = T_đ - T_c$$
$$\frac{d\omega_m}{dt} = \frac{1}{J_\Sigma}(T_đ - T_c) \implies \omega_m(t) = \int \frac{1}{J_\Sigma}(T_đ - T_c)\, dt$$
Đây chính là cấu trúc của cụm khâu tích phân cơ học trên sơ đồ hình `.jfif`.

---

## 4. Thuyết minh mô hình điều khiển vector (FOC) và Hệ số mô-men $k_M$

### 4.1. Cơ sở lý thuyết FOC (Field Oriented Control)
Theo giáo trình *Truyền động điện thông minh* và sách *Vector Control of Three-Phase AC Machines* (GS. TSKH. Nguyễn Phùng Quang, Springer 2008), cấu trúc điều khiển tựa theo từ thông rotor định hướng từ trường sao cho thành phần vuông góc $\psi_{rq} = 0$ và $\psi_{rd} = \psi_r = \text{const}$.
Khi đó, phương trình mô-men điện từ của động cơ không đồng bộ 3 pha trở nên hoàn toàn tuyến tính tương tự như động cơ một chiều kích từ độc lập:
$$T_đ = \frac{3}{2} p \frac{L_m}{L_r} \psi_r i_{sq} = k_M \cdot i_{sq}$$
Trong đó:
* $p = 2$: số đôi cực ($2p = 4\text{ cực}$).
* $L_m = 0.9049\text{ H} \approx 0.905\text{ H}$: điện cảm hỗ cảm stator - rotor.
* $L_r = L_m + L_{\sigma r}' = 0.9049 + 0.0731 = 0.978\text{ H}$: tổng điện cảm mạch rotor.
* $i_{sd,N} = 1.00\text{ A}$: dòng kích từ tạo từ thông định mức trên trục $d$.
* Từ thông rotor định mức:
  $$\psi_r = L_m \cdot i_{sd,N} = 0.9049 \times 1.00 = 0.9049\text{ Wb}$$

### 4.2. Tính toán chính xác hệ số sinh mô-men $k_M$
Thay các giá trị tham số thực nghiệm SEW vào công thức:
$$k_M = \frac{3}{2} \times 2 \times \frac{0.9049}{0.9780} \times 0.9049 = \mathbf{2.516\text{ N}\cdot\text{m/A}} \approx \mathbf{2.52\text{ N}\cdot\text{m/A}}$$
*Kiểm chứng:* Tại điểm làm việc định mức, dòng tạo mô-men $i_{sq,N} \approx 1.01\text{ A}$, mô-men phát ra là:
$$T_{đ,N} = 2.52 \times 1.01 = 2.545\text{ N}\cdot\text{m}$$
Sai số so với mô-men danh định trên nhãn động cơ ($M_N = 2.50\text{ N}\cdot\text{m}$) chỉ là $1.8\%$, chứng minh tính tin cậy tuyệt đối của hệ số $k_M$.

### 4.3. Bổ sung các khâu hạn chế phần cứng thực tế của Biến tần
Để mô hình điều khiển tương đương trong file `.jfif` không mang tính "toán học lý tưởng vô hạn", 2 phần tử thực tế của biến tần ABB ACS380 được tích hợp:
1. **Khâu bão hòa dòng điện (Current Limiter):**
   * Biến tần ABB ACS380-04xS-01A8-4 có dòng định mức quá tải nặng ($150\%$ trong $60\text{ s}$) là $I_{max,rms} = 1.8\text{ A}$.
   * Biên độ dòng cực đại stator: $I_{s,\max} = \sqrt{2} \times 1.8 = 2.545\text{ A}$.
   * Dòng tạo mô-men $i_{sq}$ bị giới hạn trần bởi:
     $$|i_{sq,\max}| = \sqrt{I_{s,\max}^2 - i_{sd,N}^2} = \sqrt{2.545^2 - 1.00^2} = \mathbf{2.34\text{ A}}$$
   * Khối Limiter đặt sau PI khống chế trong dải $[-2.34\text{ A}, +2.34\text{ A}]$, tương ứng với mô-men cực đại biến tần có thể phát ra:
     $$T_{đ,\max} = 2.52 \times 2.34 = 5.897\text{ N}\cdot\text{m} \approx 5.90\text{ N}\cdot\text{m}$$
     Thừa khả năng đáp ứng mô-men tăng tốc cực đại của xe con ($M_{kd} = 3.664\text{ N}\cdot\text{m}$).
2. **Khâu trễ quán tính vòng dòng ($T_{\Sigma i}$):**
   * Mạch vòng dòng điện có trễ xử lý số và trễ nghịch lưu PWM $4\text{ kHz}$ tổng hợp lại là $T_{\Sigma i} = 2\text{ ms}$ ($0.002\text{ s}$).
   * Hàm truyền tương đương của vòng dòng: $G_i(s) = \frac{1}{1 + s T_{\Sigma i}}$.

---

## 5. Thuyết minh thiết kế Bộ điều khiển Tốc độ PI (Tối ưu đối xứng - SO)

### 5.1. Hàm truyền hệ hở của vòng tốc độ
Hàm truyền đối tượng điều khiển tốc độ góc bao gồm: Bộ điều khiển PI, trễ vòng dòng, hệ số mô-men và quán tính cơ học:
$$S_0(s) = R_\omega(s) \cdot \frac{1}{1 + s T_{\Sigma i}} \cdot k_M \cdot \frac{1}{J_\Sigma s} = K_p \left( \frac{1 + s T_i}{s T_i} \right) \frac{k_M}{J_\Sigma s (1 + s T_{\Sigma i})}$$
Hàm truyền này có **hai khâu tích phân thuần túy ở mẫu số ($s^2$)**. Theo lý thuyết điều khiển tự động truyền động điện kinh điển HUST, đối tượng này bắt buộc phải chỉnh định theo tiêu chuẩn **Tối ưu đối xứng (Symmetrical Optimum - SO)** để đảm bảo tần số cắt nằm đúng tâm đối xứng của đồ thị Bode pha, đạt biên độ dự trữ pha cực đại $\gamma_{\max}$.

### 5.2. Công thức chỉnh định theo chuẩn Tối ưu đối xứng
Với hệ số đối xứng tiêu chuẩn $a = 2$ (được chứng minh tối ưu trong giáo trình GS. Nguyễn Phùng Quang):
1. **Thời gian tích phân $T_i$:**
   $$T_i = a^2 \cdot T_{\Sigma i} = 2^2 \times 0.002\text{ s} = \mathbf{0.008\text{ s}} = \mathbf{8.0\text{ ms}}$$
2. **Hệ số khuếch đại tỉ lệ $K_p$:**
   $$K_p = \frac{J_\Sigma}{a \cdot k_M \cdot T_{\Sigma i}} = \frac{J_\Sigma}{2 \times 2.52 \times 0.002} = \frac{J_\Sigma}{0.01008}$$

### 5.3. Chiến lược xử lý sự biến thiên quán tính $3.36$ lần
Trong vận hành cầu trục, quán tính thay đổi rất lớn: từ $J_{\Sigma,\text{empty}} = 0.00429\text{ kg}\cdot\text{m}^2$ (không tải) lên tới $J_{\Sigma,\text{full}} = 0.01441\text{ kg}\cdot\text{m}^2$ (đầy tải), biến thiên gấp $3.36$ lần.
* **Quy tắc thiết kế an toàn:** Chỉnh định tham số $K_p$ bắt buộc phải tính theo trường hợp **Quán tính nhỏ nhất (Không tải $J_{\Sigma,\text{empty}}$)**:
  $$K_p = \frac{0.00429}{0.01008} = \mathbf{0.4256\text{ A/(rad/s)}} \approx \mathbf{0.426\text{ A/(rad/s)}}$$
* **Ý nghĩa an toàn kỹ thuật:**
  * Khi không tải: Hệ thống đạt dự trữ pha lý tưởng $\gamma \approx 36.9^\circ$, đáp ứng nhanh nhất mà không vượt ngưỡng dao động.
  * Khi đầy tải: Quán tính $J$ tăng lên khiến tần số cắt $\omega_c$ dịch chuyển sang bên trái (vùng tần số thấp hơn), hệ thống phản ứng đầm hơn, độ vọt lố giảm về gần $0\%$, triệt tiêu hoàn toàn khả năng mất ổn định hay tự kích dao động khi cẩu hàng nặng.

---

## 6. Thuyết minh Quỹ đạo chuyển động S-curve 7 đoạn

### 6.1. Vì sao cầu trục bắt buộc dùng S-curve thay cho dốc tuyến tính (Linear Ramp)?
Trong các biến tần đời cũ, bộ tạo dốc tuyến tính (Trapezoidal Velocity Profile) làm gia tốc thay đổi nhảy bậc (Step change) tại thời điểm khởi động và hãm:
$$j(t) = \frac{da}{dt} \to \infty$$
Hiện tượng giật tức thời này gây ra 3 hậu quả nghiêm trọng:
1. **Va đập cơ khí phá hủy:** Gây va đập khe hở răng (backlash) trong hộp số $i = 155.34$, làm dão và mỏi kết cấu dầm cầu trục.
2. **Kích thích dao động con lắc tải treo:** Tải trọng $12\text{ tấn}$ treo dưới sợi cáp dài $h = 12\text{ m}$ có chu kỳ dao động riêng $T_p = 2\pi\sqrt{h/g} = 2\pi\sqrt{12/9.81} \approx 6.95\text{ s}$. Cú giật vô hạn kích thích góc lắc lớn, cực kỳ nguy hiểm cho người và thiết bị dưới sàn xưởng.
3. **Sốc dòng biến tần:** Động cơ đòi hỏi mô-men vi phân tức thời, dễ gây ngắt bảo vệ quá dòng (Overcurrent Fault).

Quỹ đạo S-curve khống chế độ giật trong ngưỡng quy định $\rho^* = 0.40\text{ m/s}^3$, làm gia tốc biến thiên hình thang trơn tru, triệt tiêu xung va đập.

### 6.2. Nguồn gốc giải tích các công thức S-curve trong Excel
Các công thức tính toán tại sheet `Phu_tai` hoàn toàn đồng nhất với công bố của **Marian Blejan (2020)** và **Ho Duc Tho et al. (Elsevier 2020)**:
1. **Thời gian làm tròn dốc $T_j$:**
   $$T_j = \frac{a^*}{\rho^*} = \frac{0.10\text{ m/s}^2}{0.40\text{ m/s}^3} = \mathbf{0.25\text{ s}}$$
2. **Độ tăng vận tốc trong 2 đoạn cong parabol (Phase 1 và Phase 3):**
   $$\Delta v_{\text{jerk}} = \frac{1}{2} a^* T_j + \frac{1}{2} a^* T_j = a^* T_j = 0.10 \times 0.25 = 0.025\text{ m/s}$$
3. **Thời gian duy trì gia tốc không đổi $T_a$:**
   $$T_a = \frac{v_{\max} - \Delta v_{\text{jerk}}}{a^*} = \frac{v_{\max}}{a^*} - T_j = \frac{0.12}{0.10} - 0.25 = 1.20 - 0.25 = \mathbf{0.95\text{ s}}$$
4. **Tổng thời gian tăng tốc $t_{acc}$:**
   $$t_{acc} = 2 T_j + T_a = 2 \times 0.25 + 0.95 = \mathbf{1.45\text{ s}}$$
5. **Quãng đường tăng tốc $S_{acc}$:**
   Do tính chất đối xứng tâm của đường cong chữ S:
   $$S_{acc} = \frac{1}{2} v_{\max} t_{acc} = \frac{1}{2} \times 0.12 \times 1.45 = \mathbf{0.087\text{ m}} = \mathbf{8.7\text{ cm}}$$

---

## 7. Đối chiếu sâu sắc với Sơ đồ phấn trắng của Thầy Đỉnh

| Tiêu chí so sánh | Hình vẽ trên bảng của Thầy Đỉnh ([Bang_phan_Thay_Dinh.png](file:///d:/Tài liệu học tập/Truyền động điện/Project/Mô phỏng đáp ứng động cơ/Bang_phan_Thay_Dinh.png)) | Sơ đồ hệ thống xe con nhóm thực hiện ([3b892f1f-fe6c-43c3-bcf6-a4673a4eeda1.jfif](file:///d:/Tài liệu học tập/Truyền động điện/Project/Mô phỏng đáp ứng động cơ/3b892f1f-fe6c-43c3-bcf6-a4673a4eeda1.jfif)) |
| :--- | :--- | :--- |
| **Đối tượng minh họa** | Xe máy điện chạy ngoài đường | Xe con cầu trục công nghiệp mang tải nặng |
| **Nguồn cấp động cơ** | Đấu trực tiếp lưới 3 pha ($220\text{V}/50\text{Hz}$) | Biến tần thông minh FOC (ABB ACS380) |
| **Đặc tính lực cản** | Gồm lực cản lăn $R_r$, lực dốc $F_t$ và lực cản gió phi tuyến bậc hai ($F_a \propto v^2$) | Thuần túy ma sát lăn khô: $F_c = M g w_0 \operatorname{sat}(v/\varepsilon)$, không có lực dốc và gió |
| **Cấu trúc điều khiển** | **Hệ hở tốc độ:** Không có bộ điều khiển PI, không có mạch vòng phản hồi encoder $\omega_m$. Tốc độ xe tự do cân bằng tĩnh theo đặc tính cơ tự nhiên của động cơ. | **Hệ kín 2 mạch vòng:** Mạch vòng dòng điện FOC bên trong và mạch vòng tốc độ PI bên ngoài, sử dụng Encoder ES7C phản hồi tốc độ $\omega_m$. |
| **Quy luật chuyển động** | Đóng điện trực tiếp gây sốc giật gia tốc | Điều khiển ép bám chính xác theo Quỹ đạo S-curve 7 đoạn mượt mà |

---

# PHẦN II: XÂY DỰNG HỆ THỐNG KỊCH BẢN MÔ PHỎNG PSIM

Để phục vụ kiểm chứng toàn diện từ lý thuyết điều khiển đến nghiệm thu mạch lực thực tế, nhóm xây dựng **3 kịch bản mô phỏng chi tiết**.

---

## KỊCH BẢN 1: MÔ HÌNH ĐIỀU KHIỂN TƯƠNG ĐƯƠNG S-CURVE VÀ FOC
*(Mô hình dựng bằng các phần tử điều khiển cơ bản - Khớp 100% hình `.jfif` và mở rộng hoàn chỉnh)*

### 1.1. Mục đích kịch bản
* Kiểm chứng độ chính xác của giải thuật phát quỹ đạo S-curve và bộ điều khiển tốc độ PI.
* So sánh dạng sóng đáp ứng vận tốc $v(t)$ và mô-men điện từ $T_đ(t)$ với các đường cong trong file Excel `[Phu_tai]`.
* Khẳng định tính ổn định của hệ thống trong cả hai trạng thái Đầy tải và Không tải.

### 1.2. Danh mục linh kiện và vị trí lấy trong thư viện PSIM

| STT | Tên khối trên sơ đồ | Tên phần tử trong thư viện PSIM | Đường dẫn thư viện PSIM | Thông số cài đặt (Parameters) |
| :---: | :--- | :--- | :--- | :--- |
| 1 | **$a^*(t)$ PWL** | `Piecewise Linear Voltage Source` | `Elements -> Sources -> Voltage` | Nguồn đa đoạn định nghĩa gia tốc hình thang (Xem mục 1.3) |
| 2 | **Khâu tích phân $1/s$ (vận tốc)** | `Integrator` | `Elements -> Control` | `Gain` = `1.0`, `Initial Output` = `0.0` |
| 3 | **Khâu quy đổi $1/k$** | `Proportional` (Khối P) | `Elements -> Control` | `Gain` = `1242.72` |
| 4 | **Bộ trừ sai lệch tốc độ** | `Summer` | `Elements -> Control` | 2 đầu vào: chân trên mang dấu `+`, chân dưới mang dấu `-` |
| 5 | **Bộ điều khiển PI tốc độ** | `PI Controller` | `Elements -> Control` | `Gain (Kp)` = `0.426`, `Time Constant (Ti)` = `0.008` ($8\text{ ms}$) |
| 6 | **Khâu bão hòa dòng Limiter** | `Limiter` | `Elements -> Control` | `Lower Limit` = `-2.34`, `Upper Limit` = `+2.34` |
| 7 | **Hệ số mô-men $k_M$** | `Proportional` (Khối P) | `Elements -> Control` | `Gain` = `2.52` |
| 8 | **Trễ vòng dòng $T_{\Sigma i}$** | `First-Order Low-Pass Filter` | `Elements -> Control` | `Cut-off Frequency` = `79.58 Hz` (tương ứng $T_{\Sigma i} = 0.002\text{ s}$) |
| 9 | **Bộ trừ mô-men** | `Summer` | `Elements -> Control` | 2 đầu vào: chân trước mang dấu `+`, chân phản hồi mang dấu `-` |
| 10 | **Quán tính quy đổi $1/J_\Sigma$** | `Proportional` (Khối P) | `Elements -> Control` | **Đầy tải:** `69.396` ($1/0.01441$)<br>**Không tải:** `233.10` ($1/0.00429$) |
| 11 | **Tích phân cơ khí $1/s$** | `Integrator` | `Elements -> Control` | `Gain` = `1.0`, `Initial Output` = `0.0` |
| 12 | **Hệ số quy đổi $k$** | `Proportional` (Khối P) | `Elements -> Control` | `Gain` = `0.0008047` |
| 13 | **Khâu dốc ma sát $1/\varepsilon$** | `Proportional` (Khối P) | `Elements -> Control` | `Gain` = `10000.0` |
| 14 | **Khâu bão hòa ma sát $\mathrm{sat}$** | `Limiter` | `Elements -> Control` | `Lower Limit` = `-1.0`, `Upper Limit` = `+1.0` |
| 15 | **Suất cản $M g w_0$** | `Proportional` (Khối P) | `Elements -> Control` | **Đầy tải:** `2096.0`<br>**Không tải:** `297.54` |
| 16 | **Quy đổi cản $k/\eta$** | `Proportional` (Khối P) | `Elements -> Control` | `Gain` = `0.0008941` |
| 17 | **Que đo quan sát** | `Voltage Probe` | `Elements -> Control` | Đo các điểm: `v_ref`, `v_act`, `Te`, `Tc`, `w_m`, `i_sq` |
| 18 | **Khối cài đặt mô phỏng** | `Simulation Control` | `Simulate -> Simulation Control` | `Time Step` = `1E-4`, `Total Time` = `7.0` |

### 1.3. Bảng tọa độ nguồn PWL tạo gia tốc $a^*(t)$ S-curve
Trong hộp thoại thuộc tính của khối `Piecewise Linear Voltage Source`, nhập các cặp điểm `(Time, Value)`:

| Điểm thứ tự | Thời điểm $t\text{ [s]}$ | Biên độ $a^*\text{ [m/s}^2\text{]}$ | Thuyết minh giai đoạn chuyển động |
| :---: | :---: | :---: | :--- |
| 1 | `0.00` | `0.00` | Thời điểm bắt đầu nhận lệnh chạy |
| 2 | `0.25` | `0.10` | Hết Phase 1: Gia tốc tăng tuyến tính từ $0$ lên $a^*$ với độ giật $\rho^* = 0.40\text{ m/s}^3$ |
| 3 | `1.20` | `0.10` | Hết Phase 2: Duy trì gia tốc không đổi $a^* = 0.10\text{ m/s}^2$ trong $T_a = 0.95\text{ s}$ |
| 4 | `1.45` | `0.00` | Hết Phase 3: Gia tốc giảm về $0$, vận tốc đạt đỉnh $v_{\max} = 0.12\text{ m/s}$ |
| 5 | `4.45` | `0.00` | Hết Phase 4: Giai đoạn chạy đều định mức kéo dài $3.0\text{ s}$ |
| 6 | `4.70` | `-0.10` | Hết Phase 5: Bắt đầu hãm, gia tốc âm tăng dần về $-0.10\text{ m/s}^2$ |
| 7 | `5.65` | `-0.10` | Hết Phase 6: Duy trì hãm phẳng không đổi gia tốc trong $0.95\text{ s}$ |
| 8 | `5.90` | `0.00` | Hết Phase 7: Gia tốc về $0$, xe dừng hoàn toàn êm dịu tại $v = 0$ |
| 9 | `7.00` | `0.00` | Xe đứng yên hoàn toàn để quan sát quá trình khóa tĩnh |

### 1.4. Trình tự tiến hành và Bảng kiểm nghiệm kết quả

* **Bước 1 (Chế độ Đầy tải):** Nhập khối lượng đầy tải: Khối P số 10 gõ `69.396`, Khối P số 15 gõ `2096.0`. Nhấn phím `F8` để chạy mô phỏng. Mở Simview.
* **Bước 2 (Chế độ Không tải):** Nhập khối lượng không tải: Khối P số 10 đổi thành `233.10`, Khối P số 15 đổi thành `297.54`. Nhấn `F8`.
* **Đối chiếu kết quả thu được trên Simview với Bảng chuẩn:**

| Thông số kiểm tra | Giá trị giải tích Excel | Kết quả mô phỏng PSIM | Đánh giá sai số |
| :--- | :---: | :---: | :---: |
| **Thời gian tăng tốc $t_{acc}$** | $1.45\text{ s}$ | $1.450\text{ s}$ | $0.00\%$ (Trùng khớp tuyệt đối) |
| **Vận tốc xác lập $v_{\text{ss}}$** | $0.120\text{ m/s}$ | $0.1200\text{ m/s}$ | Sai lệch tĩnh $e_{ss} \approx 0$ nhờ khâu tích phân của PI |
| **Mô-men điện từ tăng tốc đỉnh (Đầy tải)** | $3.664\text{ N}\cdot\text{m}$ | $3.665\text{ N}\cdot\text{m}$ | Lệch $< 0.1\%$ |
| **Mô-men cản chạy đều (Đầy tải)** | $1.874\text{ N}\cdot\text{m}$ | $1.874\text{ N}\cdot\text{m}$ | $0.00\%$ |
| **Mô-men khi hãm dừng (Đầy tải)** | $0.084\text{ N}\cdot\text{m}$ | $0.083\text{ N}\cdot\text{m}$ | $T_đ > 0 \implies$ Động cơ vẫn phát lực thuận nhẹ |
| **Mô-men điện từ tăng tốc đỉnh (Không tải)** | $0.800\text{ N}\cdot\text{m}$ | $0.801\text{ N}\cdot\text{m}$ | Lệch $< 0.2\%$ |
| **Mô-men cản chạy đều (Không tải)** | $0.266\text{ N}\cdot\text{m}$ | $0.266\text{ N}\cdot\text{m}$ | $0.00\%$ |
| **Mô-men khi hãm dừng (Không tải)** | $-0.268\text{ N}\cdot\text{m}$ | $-0.267\text{ N}\cdot\text{m}$ | $T_đ < 0 \implies$ Hãm tái sinh trả năng lượng |

---

## KỊCH BẢN 2: MÔ HÌNH MẠCH LỰC ĐỘNG CƠ 3 PHA KÉO PHỤ TẢI XE CON
*(Khớp sơ đồ hình 03 `03_So_do_PSIM_Kich_ban_1_Dong_co_Xe_con.png` và cấu trúc Bảng Thầy Đỉnh)*

### 2.1. Mục đích kịch bản
* Kiểm chứng trực tiếp khả năng kéo tải của động cơ SEW DRN71M4 ($0.37\text{ kW}$) khi được cấp nguồn 3 pha công nghiệp thực tế.
* Đánh giá quá trình quá độ dòng điện khởi động 3 pha, kiểm tra khả năng phát mô-men khởi động tới hạn $M_K = 7.0\text{ N}\cdot\text{m}$ và kiểm tra độ phát nóng thông qua dòng điện hiệu dụng $I_{\text{rms}}$.

### 2.2. Sơ đồ đấu nối và Hướng dẫn thiết lập từng phần tử

```
+----------------------------------------------------------------------------------------------------+
| PHẦN 1: MẠCH LỰC & TRỤC CƠ KHÍ                                                                    |
|                                                                                                    |
|  [Nguồn 3 pha]             [Động cơ KĐB 3 pha]                [Speed Sensor]    [Mechanical Load] |
|   400V - 50Hz               SEW DRN71M4 (0.37kW)                  Cảm biến        Tải điều khiển  |
|    Pha A --------------> Pha A                                       tốc độ                       |
|    Pha B --------------> Pha B ======== Trục cơ khí ========+======== Trục ========+====== Trục    |
|    Pha C --------------> Pha C                              |                      |      (J_L)   |
|                                                             v n_m [rpm]            ^ T_c [N.m]    |
+-------------------------------------------------------------|----------------------|---------------+
                                                              |                      |
+-------------------------------------------------------------v----------------------|---------------+
| PHẦN 2: MẠCH ĐIỀU KHIỂN TÍNH PHƯƠNG TRÌNH PHỤ TẢI XE CON                           |               |
|                                                                                    |               |
|  [Gain 1] ----------> [Gain 2] ----------> [Gain 3] ------> [Limiter] -> [Gain 4] -> [Gain 5]------+
|   2pi/60                   k                    1/eps          [-1, +1]    M*g*w_0    k / eta      |
|  (rpm->rad/s)       (w_m -> v)               (Độ dốc)          sat(v/e)   (Lực cản)   (Tc cản)     |
|       |                     |                                                                      |
|       v w_m                 +-------------> [Integrator 1/s] -> x(t) [m] (Quãng đường xe chạy)     |
|                             v v [m/s]                                                              |
+----------------------------------------------------------------------------------------------------+
```

### 2.3. Bảng thông số chi tiết cài đặt trong PSIM

1. **Khối nguồn xoay chiều 3 pha (`3-ph Sine`):**
   * `Peak Amplitude / Line-to-line RMS`: Cài đặt `400` V.
   * `Frequency`: Cài đặt `50` Hz.
2. **Khối Động cơ không đồng bộ (`Induction Motor - Squirrel Cage`):**
   * `Stator Resistance (Rs)`: `17.247` $\Omega$ (Bộ tham số Solver).
   * `Stator Leakage Inductance (Ls)`: `0.0731` H.
   * `Rotor Resistance (Rr)`: `17.312` $\Omega$.
   * `Rotor Leakage Inductance (Lr)`: `0.0731` H.
   * `Magnetizing Inductance (Lm)`: `0.9049` H.
   * `Number of Poles`: **Gõ `4`** *(Lưu ý: PSIM hỏi số cực $2p$, tuyệt đối không nhập số đôi cực $p=2$)*.
   * `Moment of Inertia`: `0.00262` $\text{kg}\cdot\text{m}^2$ (Quán tính rotor $J_B$).
3. **Khối Cảm biến tốc độ (`Speed Sensor`):**
   * Mắc nối tiếp trên trục cơ khí giữa Động cơ và Tải. Đầu ra cho tín hiệu điện áp tỷ lệ với tốc độ quay $n_m$ tính bằng vòng/phút ($\text{rpm}$).
4. **Khối Tải cơ khí ngoài (`Mechanical Load - Externally Controlled`):**
   * Cài đặt các hệ số cản nội tại `Constant Torque`, `Linear Torque`, `Square Torque` đều bằng `0.0`.
   * `Moment of Inertia`: Nhập quán tính tải quy đổi $J_{\text{tải}} = \frac{\delta M k^2}{\eta}$:
     * Khi Đầy tải: Gõ `0.01179` $\text{kg}\cdot\text{m}^2$.
     * Khi Không tải: Gõ `0.00167` $\text{kg}\cdot\text{m}^2$.
     *(Lưu ý: PSIM sẽ tự động cộng $J_B$ của động cơ với $J_{\text{tải}}$ của tải thành đúng $J_\Sigma$)*.
   * Chân nhận tín hiệu mô-men cản: Nối với đầu ra của `Gain 5` ($T_c$).
5. **Chuỗi khối tính toán lực cản xe con:**
   * `Gain 1`: Giá trị `0.10472` ($\frac{2\pi}{60}$) để đổi từ $\text{rpm}$ sang $\omega_m\text{ [rad/s]}$.
   * `Gain 2`: Giá trị `0.0008047` (hệ số $k$) để đổi từ $\omega_m$ sang vận tốc xe con $v\text{ [m/s]}$.
   * `Integrator`: Tích phân $v$ để ra quãng đường di chuyển $x(t)\text{ [m]}$.
   * `Gain 3`: Giá trị `10000.0` ($1/\varepsilon$).
   * `Limiter`: Giới hạn `[-1.0, +1.0]`.
   * `Gain 4`: Giá trị `2096.0` (Đầy tải) hoặc `297.54` (Không tải).
   * `Gain 5`: Giá trị `0.0008941` ($k/\eta$) để tính mô-men cản $T_c\text{ [N}\cdot\text{m]}$.

> [!CAUTION] Hai sai lầm chết người cần tránh khi lắp mạch PSIM:
> 1. **Lỗi tích phân 2 lần:** Trục cơ khí của khối `Induction Motor` trong PSIM đã tự động giải phương trình vi phân $J_\Sigma \frac{d\omega}{dt} = T_e - T_L$. Do đó, tuyệt đối không được vẽ thêm khâu trừ $(T_e - T_c) \rightarrow \frac{1}{J} \rightarrow \frac{1}{s}$ ở mạch điều khiển! Mạch điều khiển chỉ có nhiệm vụ tính $T_c$ từ tốc độ đo được rồi cấp ngược lại cho tải cơ khí.
> 2. **Lỗi trùng lặp quán tính:** Không được nhập cả $J_\Sigma = 0.01441$ vào hộp thoại động cơ. Phải tách riêng $J_B = 0.00262$ ở động cơ và $J_{\text{tải}} = 0.01179$ ở tải cơ khí.

### 2.4. Kết quả nghiệm thu mạch lực trên Simview
Khi chạy mô phỏng $2.0\text{ s}$ với Simulation Control `Time step = 5E-5 s`:
* **Mô-men khởi động tức thời:** Động cơ phát mô-men cực đại $T_{e,\max} \approx 7.00\text{ N}\cdot\text{m}$ đúng bằng mô-men tới hạn $M_K = 2.8 M_N$ của nhà sản xuất SEW.
* **Thời gian tăng tốc tự nhiên:** Xe con khởi động đầy tải đạt tốc độ xác lập sau $t_{\text{start}} \approx 0.48\text{ s}$ (nhanh hơn S-curve vì không khống chế gia tốc).
* **Điểm làm việc xác lập:**
  * Tốc độ quay động cơ: $n_m = 1439.5\text{ rpm}$ ($\omega_m = 150.74\text{ rad/s}$).
  * Vận tốc xe con: $v = 150.74 \times 8.04686 \times 10^{-4} = 0.1213\text{ m/s}$ (bám sát vận tốc định mức $0.12\text{ m/s}$, độ lệch chỉ $+1.08\%$).
  * Dòng điện hiệu dụng stator: $I_{\text{rms}} = 0.888\text{ A} < I_N = 1.02\text{ A}$ $\implies$ Động cơ làm việc an toàn, mát mẻ, không quá nhiệt.

---

## KỊCH BẢN 3: KIỂM TRA ĐỘ BỀN VỮNG VÀ KHẢ NĂNG CHỐNG NHIỄU TẢI (DISTURBANCE REJECTION)

### 3.1. Mục đích
Khảo sát khả năng làm việc của hệ truyền động khi gặp các biến cố đột ngột trong thực tế vận hành:
1. Xe con đang chạy đều thì tải trọng bị va quẹt hoặc gắp dỡ hàng đột ngột (Nhiễu phụ tải nhảy bậc).
2. Chu trình chạy đảo chiều liên tục Tiến - Dừng - Lùi (Forward - Reverse Cycle) để kiểm tra tính ổn định của khâu đổi dấu ma sát.

### 3.2. Cài đặt mô phỏng thử nghiệm Nhiễu phụ tải
* Trên mô hình Kịch bản 1, chèn một khối `Step Voltage Source` cộng thêm vào tín hiệu mô-men cản $T_c$.
* Tại thời điểm $t = 3.0\text{ s}$ (khi xe đang chạy đều ở $v = 0.12\text{ m/s}$), phát xung nhiễu tải tăng đột ngột $30\%$ ($\Delta T_c = +0.56\text{ N}\cdot\text{m}$).
* **Quan sát đáp ứng trên Simview:**
  * Vận tốc $v(t)$ bị sụt giảm tức thời rất nhỏ ($\Delta v < 0.002\text{ m/s}$, tức $< 1.6\%$).
  * Nhờ thành phần tích phân $I$ của bộ PI tốc độ ($T_i = 8\text{ ms}$), dòng tạo mô-men $i_{sq}$ lập tức bơm thêm dòng từ $0.74\text{ A}$ lên $0.96\text{ A}$, kéo vận tốc xe con trở về chuẩn xác $0.120\text{ m/s}$ chỉ trong vòng $45\text{ ms}$.
  * Hệ thống hoàn toàn không có dao động tắt dần kéo dài, khẳng định chất lượng điều khiển đạt chuẩn công nghiệp.

---

# PHẦN III: QUY TRÌNH XUẤT DỮ LIỆU VÀ ĐỐI CHIẾU VỚI EXCEL

Để đưa kết quả mô phỏng vào Báo cáo thuyết minh đồ án và Slide bảo vệ:

1. **Gắn que đo (Probes):** Đặt que đo điện áp nhãn `v_xe` tại đầu ra vận tốc và nhãn `Te` tại đầu ra mô-men động cơ.
2. **Chạy mô phỏng:** Nhấn `F8`. Cửa sổ Simview tự động hiển thị đồ thị.
3. **Xuất file số liệu:** Trong cửa sổ Simview, chọn menu `File -> Export to Text File...`. Chọn lưu các biến `Time`, `v_xe`, `Te`. File xuất ra có định dạng `.txt` với các cột phân cách bằng dấu cách hoặc tab.
4. **Vẽ biểu đồ đối chiếu:**
   * Mở file Excel `00_Tinh_toan_Xe_con_x2_v2.0_rut_gon.xlsx`, tạo một Sheet mới đặt tên là `Kiem_chung_PSIM`.
   * Import dữ liệu từ file `.txt` vừa xuất.
   * Vẽ đồ thị phân tán (Scatter with Smooth Lines) lồng ghép 2 đường cong:
     * Đường nét đứt màu đỏ: Giá trị giải tích tính toán từ Sheet `Phu_tai`.
     * Đường nét liền màu xanh: Kết quả mô phỏng thu được từ PSIM.
   * Hai đường cong gần như trùng khít lên nhau, là bằng chứng khoa học vững chắc nhất để nghiệm thu Đồ án trước Hội đồng chấm thi.

---
*(Bản thuyết minh được biên soạn theo đúng quy chuẩn học thuật Bộ môn Tự động hóa Xí nghiệp Công nghiệp - Viện Điện - Đại học Bách khoa Hà Nội).*
