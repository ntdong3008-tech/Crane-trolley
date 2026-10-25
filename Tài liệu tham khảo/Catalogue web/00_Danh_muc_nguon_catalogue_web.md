# DANH MỤC NGUỒN CATALOGUE WEB `[W-01..W-10]` — KHỐI 2 & KHỐI 3

**Lập ngày:** 25/10/2026 — Theo `WORKFLOW_RULES.md` §0.3 và §8 (K12): mọi thông số thiết bị phải truy được về nguồn lưu trong `Tài liệu tham khảo/`.
Các tài liệu PDF lưu trong thư mục này. Với trang web không in được sang PDF (bị chặn truy cập tự động hoặc là công cụ tính trực tuyến), dữ liệu dùng trong đồ án được **chép nguyên văn** vào mục 2 kèm URL và ngày truy cập.

## 1. Tệp PDF đã lưu

| Mã | Tệp | Nguồn gốc | Nội dung dùng |
| :---: | :--- | :--- | :--- |
| `[W-01]` | `W-01_SEW_DRN-Gearmotors-IE3_24832936_tr866.pdf` | SEW-EURODRIVE, Catalog *DRN.. Gearmotors (IE3)*, 24832936/EN – 09/2018, tr.866 (bản trích 1 trang, tải từ máy chủ bên thứ ba match.kheoos.com — bản gốc SEW trả về 403) | Thông số động cơ DRN.. 400 V/50 Hz 4 cực |
| `[W-02]` | `W-02_SEW_EDRN-IE3-Gearmotors-60Hz-Revision_24772933.pdf` | SEW, *(E)DRN.. (IE3) Gearmotors – 60 Hz, Revision*, 24772933/EN – 01/2018 (download.sew-eurodrive.com) | $J_{Mot}$, $J_{BMot}$, loại phanh BE; bảng chọn R..DRN |
| `[W-03]` | `W-03_SEW_DRN-Gearmotors-IE3-Addendum-2-6-pole_22866450.pdf` | SEW, Addendum *DRN.. Gearmotors (IE3) 2-/6-pole*, 22866450/EN – 06/2016 | Cấp mô-men phanh BE2 (bảng động cơ 2/6 cực) |
| `[W-04]` | `W-04_SEW_ES7C-EV7C-encoder.pdf` | SEW, tài liệu trực tuyến *ES7C, EV7C* (in từ trang HTML ngày 25/10/2026) | Encoder ES7C: HTL/TTL, 1024 chu kỳ/vòng |
| `[W-05]` | `W-05_ABB_ACS380-catalog_3AUA0000187460-RevD.pdf` | ABB, *ACS380 machinery drives catalog*, 3AUA0000187460 REV D EN 22.9.2020 | tr.10 thông số chung; **tr.12 bảng định mức** ($I_N, I_{Hd}, I_{\max}$); **tr.24 bảng chopper** ($R_{\min}, R_{\max}, P_{BR}$, điện trở mẫu Danotherm) — đã đối chiếu bằng ảnh trang |
| `[W-07]` | `W-07_SEW_Technical-Note-B-107-04_BE-brake-torques.pdf` | SEW-EURODRIVE Technical Note B-107-04 *BE Brake – Torques / Spring Combinations / Air Gap* (bản do nhà phân phối SEW Ukraina eurodrive.ua đăng) | **BE1 (DR71/DR80/DR90): 10 N·m (6 lò xo thường), 7 N·m (4 thường + 2 xanh), 5 N·m (3 thường)**; BE2: 20/14/10/7/5 N·m |
| `[W-08]` | `W-08_ABB_ACS380-quick-installation-guide_QISG-F.pdf` | ABB, *ACS380 drives quick installation and start-up guide* (library.e.abb.com) | Bảng cầu chì: **ACS380-04xx-03A3-4 → gG OFAF000H6 (6 A)**, cáp 3×1.5 + 1.5 mm², khung R1 |

## 2. Dữ liệu chép từ trang web (không có PDF)

### `[W-06]` SEW Drive Selection — công cụ chọn truyền động trực tuyến của SEW

- URL: <https://kz.sew-eurodrive.com/os/ds/> (ứng dụng "Тележка" — xe con), truy cập 25/10/2026.
- Dữ liệu nhập: khối lượng 14,244 kg; đường kính bánh 250 mm; v = 0.12 m/s; a = 0.5 m/s²; suất cản lăn riêng 147.15 N/t (tương ứng $w_0 = 0.015$); hiệu suất hệ 90%; chạy bằng biến tần; hộp số đồng trục, lắp chân đế, trục đặc; có phanh; lưới IEC 400 V/50 Hz.
- Tải SEW tự tính: công suất tĩnh 0.279 kW; công suất cực đại 1.23 kW; mô-men tĩnh 291 N·m; mô-men cực đại trên trục ra 1,280 N·m; tốc độ ra 9.17 vg/ph (**khớp với Excel của nhóm**).
- Đề xuất của SEW: **R87DRN90L4/BE2/TF** — *Общее передат.число* (tỷ số truyền tổng) **155.34**; mô-men ra 1,520 N·m; **mô-men ra cho phép lớn nhất 1,550 N·m**; hệ số làm việc SEW 1; **tải hướng kính cho phép trên trục ra 17,100 N**; trục ra 50×100 mm; mức sử dụng hộp số 83%.
- Ghi chú: SEW đề xuất động cơ 1.5 kW vì công cụ giả định biến tần cùng cỡ với động cơ (giới hạn khoảng 150% dòng). Nhóm đã chốt DRN80M4 0.75 kW với biến tần lớn hơn một cấp (QĐ-04), nên chỉ lấy **hộp số R87, i = 155.34** từ kết quả này. Tổ hợp R87 với động cơ khung DRN80 cần xác nhận lại khi đặt hàng (bộ cấu hình không cho đổi động cơ trong phiên truy cập ẩn danh).

### `[W-09]` Danotherm CBH 360 C T 406 210R — điện trở hãm

- URL: <https://partco.shop/product/brake-resistor-200w-cbh-360-ct-406-210r-10469> (nhà phân phối Partco, Phần Lan), truy cập 25/10/2026.
- Nguyên văn: *"Power resistor 200W (Pn @ 40°C); resistance value 210 Ω +/- 10%; dimensions 360x60x31 mm; weight 1,3kg; built-in temperature monitor; cables 300mm. Pulse load / ambient temp. 40°C: 25,6kW 1s every 120s; 5,2kW 5s every 120s; 2,6kW 10s every 120s; 0,7 kW 40s every 120s."*
- ABB liệt kê đúng mã này làm điện trở mẫu cho ACS380-04xx-01A8-4 … 05A6-4 (`[W-05]` tr.24).

### `[W-10]` ABB AF09-30-10-13 (1SBL137001R1310) — contactor

- URL: <https://plc-direct.com/products/1sbl137001r1310> (nhà phân phối), truy cập 25/10/2026; nguồn gốc dữ liệu: catalog ABB 1SBC100214C0202.
- Nguyên văn: 3 tiếp điểm chính NO + 1 tiếp điểm phụ NO; *"Rated Operational Current AC-3 (Ie): (380 / 400 V) 60 °C 9 A"*; *"AC-1 (Ie): (690 V) 40 °C 25 A"*; điện áp làm việc 690 V; IEC/EN 60947-4-1.
- Hậu tố "-13": cuộn hút 100–250 V AC/DC (theo nhà phân phối Lakeland Engineering — chưa đối chiếu catalog ABB gốc).
