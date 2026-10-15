# Bill of Materials (BOM) & Vietnam Sourcing: Gen 2 Quartz Tube Thermal Oxidation Furnace

- **Thiết bị**: Lò ống thạch anh oxy hóa nhiệt độ cao (Deal-Grove Thermal Oxidation Furnace)
- **Mục tiêu kỹ thuật**: Nhiệt độ vận hành $800^\circ\text{C} - 1,150^\circ\text{C}$; Vùng đẳng nhiệt $\pm 2^\circ\text{C}$ trên chiều dài $150\text{ mm}$; Điều khiển khí $O_2 / N_2$ có khóa van
- **Chuẩn ứng dụng**: Phát triển màng oxit cách điện cổng (Gate Oxide $SiO_2 \sim 20 - 50\text{ nm}$) và oxit trường (Field Oxide $\sim 300 - 500\text{ nm}$) trên phiến silicon 2-inch / 4-inch
- **Ngân sách ước tính**: ~3.200.000 - 4.600.000 VNĐ (~$130 - $185 USD) *(Thay vì lò công nghiệp giá $40.000 USD)*

---

## 1. Bảng Linh Kiện Chi Tiết (Chi phí & Nguồn cung ứng tại Việt Nam)

| STT | Tên linh kiện & Quy cách kỹ thuật | Số lượng | Đơn giá ước tính (VNĐ) | Thành tiền (VNĐ) | Kênh mua sắm / Nhà cung cấp tại Việt Nam | Ghi chú kỹ thuật |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **1** | **Ống thạch anh quang học chịu nhiệt (Fused Quartz Tube)** (Phi ngoài 50mm, phi trong 44mm, dài 1,000mm, độ tinh khiết 99.99% $SiO_2$) | 1 ống | 1.450.000 | 1.450.000 | • Cty Thiết Bị Hóa Chất Tân Phú Lập / VinaChems (HN, HCM)<br>• Cửa hàng vật tư thí nghiệm ĐH KHTN / Shopee | Điểm mềm hóa nhiệt $> 1,600^\circ\text{C}$. Không chứa tạp chất ion kim loại nặng làm nhiễm độc màng cổng bán dẫn. |
| **2** | **Dây điện trở đốt nóng Kanthal A1 (FeCrAl) phi 1.2mm** (chịu nhiệt liên tục $1,300^\circ\text{C}$, công suất 2,500W) | 15 mét | 12.000 | 180.000 | • Chợ Trời (Hà Nội, phố Nguyễn Công Trứ) / Chợ Dân Sinh (HCM)<br>• Các shop máy hàn nhiệt, lò nung gốm sứ | Quấn dạng lò xo xoắn ốc đều bước quanh ống gốm Alumina chịu nhiệt để tản nhiệt bức xạ đồng đều. |
| **3** | **Bông gốm ceramic cách nhiệt Ceramic Fiber Blanket** (Dày 25mm, tỷ trọng 128 kg/m3, chịu nhiệt $1,260^\circ\text{C}$) | 2 mét | 85.000 | 170.000 | • Cửa hàng vật liệu chịu lửa đường Nguyễn Trãi (Thanh Xuân, HN) hoặc Q5 (HCM) | Quấn 3 - 4 lớp quanh buồng đốt để vỏ ngoài lò chỉ ấm $< 45^\circ\text{C}$, tiết kiệm điện và chống bỏng. |
| **4** | **Can nhiệt bọc sứ chịu nhiệt cao (Thermocouple Type K hoặc Type S)** dài 300mm | 1 cái | 145.000 | 145.000 | • Các cửa hàng thiết bị đo nhiệt độ công nghiệp / TheGioiIC | Đặt đầu cảm biến tiếp xúc trực tiếp giữa thành ngoài ống thạch anh tại tâm vùng đẳng nhiệt. |
| **5** | **Rơ-le bán dẫn SSR-40DA (Solid State Relay 40A AC kèm đế nhôm tản nhiệt)** | 1 bộ | 75.000 | 75.000 | • Linh kiện điện tử Minh Hà, BanLinhKien, Shopee | Đóng cắt điện trở 220V không phát ra tiếng ồn cơ khí, tuổi thọ hàng triệu chu kỳ đóng cắt PID. |
| **6** | **Mạch điều khiển ESP32 + Module đọc can nhiệt MAX6675 / MAX31855 SPI** | 1 bộ | 135.000 | 135.000 | • HShop.vn, TheGioiIC, Cytron | Đo nhiệt độ chính xác đến $0.25^\circ\text{C}$, xuất xung PID điều khiển SSR và ghi log đồ thị nung qua Serial/Web. |
| **7** | **Lưu lượng kế khí Rotameter có van kim chỉnh lưu lượng (0.1 - 2.0 Lít/phút)** | 2 cái | 165.000 | 330.000 | • Cửa hàng thiết bị khí nén & oxy y tế (Phố Tràng Thi, HN hoặc Tạ Uyên, HCM) | Dùng 1 cái cho bình khí $N_2$ (khí trơ bảo vệ/ủ) và 1 cái cho bình khí $O_2$ tinh khiết (khí oxy hóa). |
| **8** | **Van điện từ khí nén 12V 2 ngã chịu khí tinh khiết (Solenoid Valve)** | 2 cái | 65.000 | 130.000 | • Cửa hàng khí nén công nghiệp | ESP32 tự động đảo van chuyển từ môi trường thổi $N_2$ sang $O_2$ khi lò đạt đúng $1000^\circ\text{C}$. |
| **9** | **Bộ bích làm kín 2 đầu ống thạch anh (Vacuum/Gas Quick Flange)** inox 304 | 2 bộ | 210.000 | 420.000 | • Xưởng tiện cơ khí hoặc đặt gia công CNC theo bản vẽ | Có gioăng cao su silicone/viton chịu nhiệt và đầu nối nhanh ống khí phi 6mm. |
| **10** | **Thuyền nạp wafer thạch anh (Quartz Wafer Boat 2-inch)** | 1 cái | 220.000 | 220.000 | • Đại lý thiết bị thí nghiệm thạch anh / Shopee | Chứa 10 - 25 phiến wafer đặt đứng vuông góc với dòng khí oxy hóa. |
| **11** | **Vỏ lò nung kim loại tấm sơn tĩnh điện** ($300 \times 300 \times 600\text{ mm}$) | 1 vỏ | 250.000 | 250.000 | • Xưởng gia công tôn/kim loại tấm | Chứa toàn bộ buồng đốt và lớp bông gốm cách nhiệt an toàn. |
| **TỔNG** | **Tổng chi phí chế tạo hoàn chỉnh lò nung thạch anh** | | | **3.505.000 VNĐ** | *(Tương đương ~140 USD - Vùng nhiệt 1100°C chuẩn Deal-Grove)* |

---

## 2. Quy Trình Nung Oxy Hóa Khô Deal-Grove ($1000^\circ\text{C}$)

1. **Chuẩn bị bề mặt**:
   - Phiến silicon sau khi rửa sạch chuẩn RCA-1/RCA-2 và nhúng BOE khử oxit tự nhiên, sấy khô bằng khí $N_2$.
   - Xếp wafer vào thuyền thạch anh. Dùng que đẩy thạch anh đưa nhẹ nhàng thuyền vào tâm vùng đẳng nhiệt của lò.
2. **Kịch bản gia nhiệt 6 bước tự động trên ESP32**:
   - **Bước 1 (Đuổi khí trơ $N_2$)**: Mở khí $N_2$ lưu lượng $1.0\text{ L/phút}$ trong 15 phút tại nhiệt độ phòng để tống sạch không khí và hơi ẩm ra khỏi ống.
   - **Bước 2 (Nâng nhiệt Ramp Up)**: Tăng nhiệt độ từ phòng lên $1,000^\circ\text{C}$ với tốc độ kiểm soát $10^\circ\text{C}/\text{phút}$ (chống sốc nhiệt gây nứt vỡ ống thạch anh). Môi trường vẫn duy trì $N_2$.
   - **Bước 3 (Oxy hóa nhiệt Dry Ox)**: Khi lò ổn định tại $1,000^\circ\text{C} \pm 1^\circ\text{C}$, ngắt $N_2$, mở van $O_2$ siêu tinh khiết lưu lượng $1.2\text{ L/phút}$. Ngâm nhiệt (Soak) trong đúng **60 phút**.
   - **Bước 4 (Ủ thụ động Anneal)**: Khóa van $O_2$, chuyển lại sang dòng $N_2$ ủ trong 15 phút để giảm thiểu mật độ bẫy điện tích giao diện ($D_{it}$).
   - **Bước 5 (Hạ nhiệt Ramp Down)**: Giảm nhiệt từ $1,000^\circ\text{C}$ xuống $400^\circ\text{C}$ với tốc độ $5^\circ\text{C}/\text{phút}$.
   - **Bước 6 (Lấy mẫu)**: Khi nhiệt độ dưới $100^\circ\text{C}$, rút thuyền thạch anh ra ngoài và chuyển wafer vào hộp kín $N_2$.

---

## 3. Tiêu Chí Nghiệm Thu Vật Lý Thực Tế (Bits-to-Atoms Checklist)

- [ ] **Tiêu chí 1 (Độ phẳng vùng đẳng nhiệt)**: Dùng can nhiệt di chuyển dọc tâm ống: trên đoạn dài $150\text{ mm}$ ở giữa lò, nhiệt độ chênh lệch không vượt quá $\pm 2.0^\circ\text{C}$ ở mức $1,000^\circ\text{C}$.
- [ ] **Tiêu chí 2 (Độ kín khí)**: Bịt kín một đầu, cấp khí nén $0.5\text{ bar}$: sau 10 phút áp suất tụt không quá $0.02\text{ bar}$ (chứng minh không bị rò lọt oxy tạp ngoài ý muốn).
- [ ] **Tiêu chí 3 (Đo độ dày màng $SiO_2$ mọc thực tế)**: Wafer sau 60 phút ở $1,000^\circ\text{C}$ dry ox: đo bằng máy phân tích quang phổ ellipsometer hoặc phổ đo màu giao thoa màu sắc (màu vàng rơm đặc trưng của màng $45\text{ nm}$):
  $$\text{Độ dày lý thuyết Deal-Grove: } x_0^2 + A x_0 = B(t + \tau) \implies x_0 \approx 45\text{ nm} \pm 3.5\text{ nm}$$
- [ ] **Tiêu chí 4 (Đo điện dung C-V màng oxit)**: Bốc bay cực nhôm tạo tụ MOS $Al / SiO_2 / Si$, đo đường cong $C-V$ ở tần số $1\text{ MHz}$:
  $$C_{ox} = \frac{\varepsilon_{ox} \cdot \varepsilon_0 \cdot \text{Area}}{t_{ox}} \approx 76.7\text{ nF/cm}^2 \implies \text{Xác nhận chất lượng cách điện cổng}.$$
