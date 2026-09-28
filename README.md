# Tổng hợp kiến thức: Thiết kế Hệ truyền động Xe con Cầu trục

> Tài liệu này tổng hợp toàn bộ quá trình tư duy từ đề bài đến định hình giải pháp.  
> Mục tiêu: Bất kỳ ai trong nhóm đọc vào cũng hiểu được **tại sao** nhóm làm từng bước, không chỉ **cái gì**.

---

## I. BÀI TOÁN GỐC

**Đề bài (x = 2):**

| Thông số | Giá trị |
|---|---|
| Tải trọng định mức Q | 12.222 kg |
| Khối lượng cơ cấu nâng hạ m_c | 222 kg |
| Tổng khối lượng di chuyển | **12.444 kg** |
| Tốc độ tối đa v_max | 0,12 m/s |
| Gia tốc cực đại a_max | ≤ 0,5 m/s² |
| Độ giật cực đại ρ_max | ≤ 2 m/s³ |
| Chiều cao nâng h | 12 m |

**Phạm vi thiết kế:** Nhóm thiết kế **hệ truyền động của xe con**, không phải toàn bộ cầu trục.  
Cơ cấu nâng, dầm, ray là **đầu vào** ảnh hưởng đến tính toán tải, không nằm trong phạm vi thiết kế chi tiết.

```
Nguồn điện → Biến tần → Motor → Hộp giảm tốc → Bánh xe → Xe con + Tải
                          ↑
          Điều khiển | Cảm biến | Hãm | Logic an toàn
```

---

## II. TẠI SAO BÀI TOÁN NÀY KHÓ? — HIỂU ĐÚNG NỖI ĐAU

Nhiều người nhầm rằng thách thức là "vác nặng 12 tấn".  
**Sai.** Thách thức thực sự là: **12 tấn treo trên dây là một con lắc khổng lồ.**

> Giống như lái xe tải chở đầy nước: bạn không cần xe mạnh nhất —  
> bạn cần người lái **nhấn ga và đạp phanh cực kỳ từ từ** để nước không sóng sánh.

Vì vậy, các yêu cầu **phân biệt** (yêu cầu khiến giải pháp A hoạt động còn giải pháp B thất bại) là:

| # | Yêu cầu phân biệt | Vật lý phía sau |
|---|---|---|
| R1 | a ≤ 0,5 m/s² | Giới hạn góc lắc tải treo — an toàn |
| R2 | ρ ≤ 2 m/s³ | Ngay cả quá trình tăng tốc cũng phải từ từ |
| R3 | Creep speed (v rất thấp khi áp tầng) | Đủ lực kéo ở tốc độ gần 0 |
| R4 | Đảo chiều Tiến/Lùi mượt | Không giật khi đổi chiều |
| R5 | Hãm dừng có kiểm soát | Xả năng lượng không giật |

Các yêu cầu còn lại (tải trọng, nguồn điện, IP54) là **ràng buộc môi trường** — dùng để loại trừ, không phải để so sánh solutions.

---

## III. LUỒNG TƯ DUY: PRD → SOW → CASE STUDY → SOLUTIONS

### 3.1 PRD — Hệ phải làm gì và đạt mức nào?

PRD chỉ được chứa **WHAT** (cái gì), không được chứa **HOW** (làm thế nào).

**Tiêu chí một câu yêu cầu PRD tốt:**
- ✅ Đo lường được (có số liệu và dung sai)
- ✅ Độc lập với giải pháp (không nhắc tên công nghệ cụ thể)
- ✅ Mỗi câu chỉ một ý, một từ "shall"

| | Ví dụ |
|---|---|
| ❌ Sai — không đo được | *"Xe con phải dừng an toàn"* |
| ❌ Sai — chứa giải pháp | *"Phải dùng biến tần FOC"* |
| ✅ Đúng | *"Gia tốc trong mọi quá trình chuyển trạng thái không vượt quá 0,5 m/s²"* |

### 3.2 SOW — Nhóm làm đến đâu, ràng buộc gì, bàn giao gì?

SOW khóa **phạm vi**, **tiêu chuẩn**, **đầu vào**, **đầu ra** và **tiêu chí nghiệm thu**.

> **Quan trọng:** SOW **không được** khóa sớm kiến trúc kỹ thuật cụ thể nếu nhóm vẫn đang ở bước đánh giá solutions. SOW hiện tại của nhóm (đã ghi KĐB + FOC + encoder + 2 vòng PI) đã nhảy qua bước này.

**SOW đúng nên ghi:** *"Lựa chọn và luận giải kiến trúc truyền động phù hợp nhất"* — không ghi thẳng FOC.

### 3.3 Case Study — Ví dụ và bài học từ hệ tương tự

Case study không phải là solutions. Nó là nguồn để nhóm *tạo ra* các phương án phù hợp.

| Nguồn | Giải pháp họ dùng | Bài học cho nhóm |
|---|---|---|
| Nhật Bản (1979) | Bang-Bang control + Servo tốc độ + Bù quan sát | Bài toán chống lắc là bài toán kiểm soát **profil gia tốc** |
| Nga/Ukraine (2021) | Profil tốc độ hình sin + PD phản hồi góc lắc | **Chiến lược profil** quan trọng không kém loại drive |
| Thổ Nhĩ Kỳ (2023) | Motor 4kW + hộp giảm tốc SEW (chú trọng cơ khí) | Không nhất thiết phải phức tạp về điều khiển |
| Indonesia | Liệt kê 3 họ: Open-loop, Closed-loop, Combined | Cần xét cả phần cứng VÀ thuật toán |

### 3.4 Solutions — Phương án kiến trúc hoàn chỉnh ở mức concept

Solutions không chỉ là "chọn loại động cơ". Một solution đầy đủ phải bao gồm:

```
Motor + Drive + Phương pháp điều khiển + Cảm biến + Hãm + Chiến lược profil + An toàn
```

---

## IV. CÂY PHÂN LOẠI HỆ TRUYỀN ĐỘNG ĐIỆN

```
Hệ truyền động điện (Electric Drive)
│
├── DC Drive (Một chiều)
│   └── Motor DC + Thyristor Rectifier
│       → Kiểm soát tốt, nhưng bảo trì chổi than, công nghệ lỗi thời
│
└── AC Drive (Xoay chiều) ← Xu hướng hiện đại
    │
    ├── Motor KĐB + Khởi động trực tiếp (DOL)
    │   → Bật/tắt thô bạo → Vi phạm R1, R2 → LOẠI
    │
    ├── Motor KĐB + Khởi động mềm (Soft Starter)
    │   → Không điều chỉnh tốc độ vô cấp → LOẠI
    │
    ├── Motor KĐB + Biến tần (VFD) ← ỨNG VIÊN CHÍNH
    │   └── Phương pháp điều khiển bên trong:
    │       ├── V/f (Scalar): Đơn giản, mô-men giảm ở tốc độ thấp
    │       ├── Vector Sensorless: Tốt hơn V/f, không cần encoder
    │       ├── FOC (Field Oriented Control): Mô-men đầy đủ từ v=0, cần encoder
    │       └── DTC (Direct Torque Control): Phản ứng nhanh, không cần encoder
    │
    └── Servo Motor + Servo Drive
        → Chính xác cao, đắt → Overkill cho crane trolley công nghiệp thông thường
```

> **Ghi chú:** **FOC là phương pháp điều khiển** bên trong biến tần–motor KĐB. Câu hỏi đúng: *"FOC có cần thiết không so với V/f hay Vector Sensorless?"* Câu trả lời phải đến từ **tính toán**, không phải giả định.

---

## V. HAI LỚP QUYẾT ĐỊNH — ĐỪNG NHẦM LẪN

```
LỚP 1 — KIẾN TRÚC DRIVE (Phần cứng)
"Dùng bộ dẫn động nào để tạo ra lực kéo?"
→ Loại motor, loại drive, có encoder không, hướng hãm

LỚP 2 — CHIẾN LƯỢC PROFIL (Phần mềm / Thuật toán)
"Lập trình drive chạy theo profil tốc độ nào?"
→ Linear ramp | S-curve | Sinusoidal | Bang-Bang
```

> Cả hai lớp đều ảnh hưởng đến a và ρ. V/f + S-curve tốt **có thể** tốt hơn FOC + profil tuyến tính thô. "V/f có đủ không?" phải đến từ tính toán, không phải giả định.

---

## VI. QUY TRÌNH THIẾT KẾ ĐÚNG THEO MÔN HỌC

```
1. Phân tích yêu cầu công nghệ    ← Đọc PRD, nhận diện yêu cầu phân biệt
         ↓
2. Xây dựng phương án kỹ thuật    ← Liệt kê các concept đủ tiêu chí
         ↓
3. Chọn loại truyền động          ← DC/AC, Motor KĐB/Servo, Biến tần/DOL
         ↓
4. Chọn phương pháp điều khiển    ← V/f, Vector, FOC, DTC + profil S-curve
         ↓
5. Tính chọn phần lực             ← Công suất, motor, biến tần, hộp số, trở hãm
         ↓
6. Thiết kế điều khiển            ← Cấu trúc vòng PI, tham số K_p, K_i
         ↓
7. Thiết kế logic / an toàn       ← State machine, interlock, E-stop, phanh
         ↓
8. Mô phỏng kiểm chứng            ← MATLAB/Simulink, verify a và ρ
```

**Nhóm hiện đang ở giữa Bước 2–3.** Bước 5–8 là việc của sau khi chốt concept.

---

## VII. 4 SOLUTIONS ĐỀ XUẤT ĐỂ SO SÁNH

### Solution 1 — Motor KĐB + Biến tần V/f + S-curve
- **Ưu:** Rẻ, đơn giản, không cần encoder, biến tần nào cũng hỗ trợ
- **Nhược:** Mô-men giảm ở tốc độ thấp → rủi ro R3
- **Câu hỏi cần tính:** Mô-men V/f ở v_creep có ≥ mô-men cản không?

### Solution 2 — Motor KĐB + Biến tần Vector Sensorless + S-curve
- **Ưu:** Mô-men tốt hơn V/f ở tốc độ thấp, không cần encoder vật lý
- **Nhược:** Ở tốc độ rất thấp (gần 0) vẫn kém FOC với encoder thực
- **Phù hợp:** Cầu trục hạng trung

### Solution 3 — Motor KĐB + Biến tần FOC + Encoder + S-curve
*(Concept trong SOW hiện tại của nhóm)*
- **Ưu:** Mô-men đầy đủ từ v = 0, phản ứng nhanh, kiểm soát chính xác nhất
- **Nhược:** Cần encoder (thêm chi phí, thêm điểm hỏng), phức tạp khi mô phỏng
- **Phù hợp:** Tải nặng, yêu cầu chính xác cao

### Solution 4 — Servo Motor + Servo Drive + Encoder + S-curve
- **Ưu:** Chính xác nhất, dải tốc độ rộng nhất
- **Nhược:** Đắt nhất, không phổ biến cho crane trolley, khó mô phỏng hơn
- **Phù hợp:** Robot, CNC — overkill cho bài này

---

## VIII. MA TRẬN ĐÁNH GIÁ CÓ TRỌNG SỐ

> Chỉ cần **một** ma trận quyết định. Không cần dùng đồng thời HoQ, QFD, RICE và ICE.  
> HoQ/QFD: ánh xạ nhu cầu khách hàng → thông số kỹ thuật.  
> RICE/ICE: công cụ của Product Manager phần mềm — **không phù hợp** ở đây.

| Tiêu chí | Trọng số | Sol 1 V/f | Sol 2 Sensorless | Sol 3 FOC | Sol 4 Servo |
|---|:---:|:---:|:---:|:---:|:---:|
| Bám quỹ đạo a, ρ (R1, R2) | 30% | 2 | 3 | 5 | 5 |
| Mô-men ở tốc độ thấp (R3) | 25% | 2 | 3 | 5 | 5 |
| Hãm an toàn (R5) | 20% | 3 | 3 | 4 | 4 |
| Khả năng mô phỏng trong môn | 15% | 4 | 3 | 4 | 2 |
| Chi phí / Độ phức tạp | 10% | 5 | 4 | 3 | 1 |
| **Tổng điểm** | **100%** | **2,75** | **3,15** | **4,35** | **3,80** |

*Điểm 1–5 (5 là tốt nhất). Đây là ước lượng định tính — điều chỉnh sau khi tính toán.*

> **Lưu ý:** Nếu tính toán ở Bước 5 cho thấy V/f **đủ** mô-men ở creep speed → khoảng cách Sol 1 vs Sol 3 hẹp lại. Nếu **không đủ** → Sol 3 thắng rõ ràng. Kết luận phải từ số, không từ giả định.

---

## IX. KẾT QUẢ CẦN CÓ SAU BUỔI PITCHING 5 PHÚT

Nhóm không cần trả lời hết mọi thứ. Chỉ cần trình bày được:

1. **Sơ đồ khối** của 2–3 concept *(vẽ tay hoặc block diagram)*
2. **Mô tả vận hành ngắn** của concept được ưu tiên
3. **Ma trận đánh giá** với lý do chọn concept tạm thời
4. **Danh sách câu hỏi mở** cần tính ở bước tiếp

---

## X. PHÂN VIỆC SAU KHI CHỐT CONCEPT

| Vai trò | Người | Công việc |
|---|---|---|
| PE-Hardware/Power | Nguyên Bình | Tính phụ tải, chọn motor, biến tần, hộp số, trở hãm |
| PE-Control loop | Đỗ Khải | Mô hình FOC, thiết kế vòng PI, S-curve |
| PE-Logic | Bá Hưng | State machine, interlock, E-stop, phanh |
| QE-Simulation | Văn Hưng | Xây model Simulink, verify a và ρ |
| Doc Lead | Hải Trung | Báo cáo, slide, chuẩn hóa tài liệu |
| PM/SE Lead | Trọng Đông | WBS, truy xuất yêu cầu, cổng kiểm duyệt |

---

## XI. CÁC LỖI TƯ DUY CẦN TRÁNH

- **Lỗi 1 — Nhảy cóc:** Chốt FOC/biến tần trong SOW mà chưa qua bước đánh giá solutions.
- **Lỗi 2 — Nhầm tầng:** Nghĩ FOC là "toàn bộ hệ truyền động". FOC chỉ là phương pháp điều khiển bên trong biến tần.
- **Lỗi 3 — Yêu cầu không đo được trong PRD:**  
  - ❌ *"Xe con phải dừng an toàn"*  
  - ✅ *"Hệ thống phanh hãm dừng xe trong quãng đường ≤ X mm khi mất điện đột ngột"*
- **Lỗi 4 — Dùng sai công cụ:** RICE/ICE dành cho Product Manager phần mềm. Bài toán phần cứng dùng Weighted Scoring hoặc Pugh Matrix.
- **Lỗi 5 — Giả định thay vì tính toán:** "V/f không đủ mô-men" là giả định chưa chứng minh. Cần tính: $F_{cản} \rightarrow M_{tải} \rightarrow$ so với $M_{motor(V/f)}$ tại $v_{creep}$.

---

*Tổng hợp từ thảo luận nhóm ngày 28/09/2026 — Phiên bản 1.0*
