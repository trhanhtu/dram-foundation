# Bill of Materials (BOM) & Vietnam Sourcing: Gen 1 Photoresist Spin Coater

- **Thiết bị**: Máy phủ màng cảm quang ly tâm (DIY Semiconductor Spin Coater)
- **Mục tiêu kỹ thuật**: Dải tốc độ quay 500 - 6,000 RPM; Độ ổn định vận tốc $\le \pm 2\%$; Mâm hút chân không giữ chắc phiến wafer
- **Chuẩn ứng dụng**: Phủ đều chất cảm quang photoresist (Shipley 1813 / SU-8) đạt độ dày màng $1.2\ \mu\text{m} \pm 15\text{ nm}$ trên phiến 2-inch / 4-inch
- **Ngân sách ước tính**: ~620.000 - 890.000 VNĐ (~$25 - $36 USD)

---

## 1. Bảng Linh Kiện Chi Tiết (Chi phí & Nguồn cung ứng tại Việt Nam)

| STT | Tên linh kiện & Quy cách kỹ thuật | Số lượng | Đơn giá ước tính (VNĐ) | Thành tiền (VNĐ) | Kênh mua sắm / Nhà cung cấp tại Việt Nam | Ghi chú kỹ thuật |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **1** | **Động cơ không chổi than BLDC A2212 (930KV / 1000KV)** trục 3.17mm | 1 cái | 75.000 | 75.000 | • Shop máy bay mô hình RC (Hà Nội, Sài Gòn)<br>• Shopee / Lazada VN (Tìm: `Motor A2212 1000KV`) | Động cơ outrunner 3 pha không chổi than, tuổi thọ cao, không sinh tia lửa điện làm cháy dung môi dễ bay hơi. |
| **2** | **Mạch điều tốc ESC 30A (SimonK / BLHeli)** | 1 cái | 65.000 | 65.000 | • Các shop RC Quadcopter / Shopee VN | Nhận tín hiệu xung PWM (1000us - 2000us) từ ESP32 để điều chỉnh tốc độ motor mượt mà. |
| **3** | **Máy bơm hút chân không mini 12V DC (5L/phút, áp suất hút -65 kPa)** | 1 cái | 95.000 | 95.000 | • Shop máy lọc nước, phụ kiện thủy sinh, Shopee | Tạo lực hút qua mâm quay để giữ chặt tấm wafer silicon không bị văng ở tốc độ 5,000 RPM. |
| **4** | **Cảm biến quang đĩa encoder hồng ngoại (Tachometer LM393)** | 1 cái | 18.000 | 18.000 | • HShop.vn, TheGioiIC, BanLinhKien VN | Đọc xung quang từ đĩa encoder 20 khe gắn trên trục động cơ để hồi tiếp vòng lặp PID thời gian thực. |
| **5** | **Mạch vi điều khiển ESP32 DevKit V1** (30 pin) | 1 cái | 85.000 | 85.000 | • HShop, TheGioiIC, Shopee | Chạy thuật toán điều khiển PID vận tốc vòng kín và tự động hóa chu trình quay 2 giai đoạn. |
| **6** | **Mâm xoay chân không (Vacuum Chuck) nhôm phi 45mm** | 1 cái | 85.000 | 85.000 | • Xưởng tiện cơ khí Chợ Trời/Nhật Tảo hoặc in 3D nhựa cứng PETG | Tiện lỗ thông khí ở giữa và rãnh chứa gioăng cao su O-ring silicone phi 25mm để làm kín khí. |
| **7** | **Khớp xoay khí nén quay (Pneumatic Rotary Union / Khớp nối xoay chân không)** | 1 cái | 65.000 | 65.000 | • Cửa hàng khí nén Tạ Uyên (Q5, HCM) / Chợ Giời (HN) | Cho phép truyền áp suất hút chân không từ bơm cố định vào trục mâm đang quay tốc độ cao. |
| **8** | **Buồng chống văng dung môi (Splash Bowl Inox 304 phi 22cm)** | 1 cái | 45.000 | 45.000 | • Cửa hàng đồ gia dụng inox / Chợ dân sinh | Khoét lỗ phi 50mm ở đáy gắn motor. Inox 304 kháng hoàn toàn dung môi Acetone, IPA, PGMEA, MEK. |
| **9** | **Công tắc hành trình an toàn nắp đậy (Lid Safety Switch)** | 1 cái | 12.000 | 12.000 | • Các tiệm điện dân dụng / Shopee | Khóa liên động an toàn: ngắt motor ngay lập tức khi người vận hành mở nắp buồng quay. |
| **10** | **Nguồn tổ ong 12V 10A DC** | 1 cái | 110.000 | 110.000 | • Chợ Nhật Tảo, Chợ Trời, Shopee | Cấp điện 12V cho ESC, động cơ BLDC và máy bơm hút chân không. |
| **11** | **Màn hình OLED 0.96 inch I2C (SSD1306)** | 1 cái | 42.000 | 42.000 | • HShop, MakerLab, BanLinhKien | Hiển thị RPM thực tế, thời gian đếm ngược và trạng thái chu trình phủ màng. |
| **12** | **Bộ nút nhấn công nghiệp, núm xoay chiết áp (Potentiometer) & cọc đấu dây** | 1 bộ | 25.000 | 25.000 | • Cửa hàng linh kiện điện tử | Nút bấm START/STOP và chiết áp chỉnh tốc độ quay. |
| **TỔNG** | **Tổng chi phí chế tạo hoàn chỉnh máy Spin Coater** | | | **722.000 VNĐ** | *(Tương đương ~29 USD - Kháng dung môi, vòng lặp kín PID)* |

---

## 2. Quy Chuẩn Công Nghệ Phủ Màng 2 Giai Đoạn (Semiconductor Spin Recipe)

1. **Giai đoạn 1: Trải đều cảm quang (Spread Phase)**:
   - **Tốc độ**: $500\text{ RPM} \pm 20\text{ RPM}$
   - **Thời gian**: $5\text{ giây}$
   - **Mục tiêu**: Nhỏ 1.0 - 2.0 mL dung dịch Shipley 1813 lên tâm wafer; lực ly tâm chậm giúp giọt keo lan đều ra khắp rìa đĩa mà không bị văng bắn.
2. **Giai đoạn 2: Dàn phẳng màng & bay hơi dung môi (High-Speed Thinning Phase)**:
   - **Tốc độ**: $3,000 - 4,500\text{ RPM} \pm 30\text{ RPM}$ (gia tốc $10,000\text{ RPM/giây}^2$)
   - **Thời gian**: $30\text{ giây}$
   - **Mục tiêu**: Độ dày màng tuân theo định luật Emslie-Bonner-Peck ($d \propto \omega^{-1/2}$). Đạt độ dày phẳng chuẩn $1.2\ \mu\text{m}$.
3. **Giai đoạn 3: Hãm phanh mềm (Soft Deceleration)**:
   - Giảm tốc êm trong 3 giây để tránh làm rách màng cảm quang còn ướt.

---

## 3. Tiêu Chí Thẩm Định Thực Tế (Bits-to-Atoms Checklist)

- [ ] **Tiêu chí 1 (Lực giữ chân không)**: Đặt wafer lên mâm, bật bơm: áp kế đo đạt áp suất chân không $\le -50\text{ kPa}$. Dùng tay nhấc thử: wafer dính chặt cứng, không xê dịch khi rung lắc.
- [ ] **Tiêu chí 2 (Độ ổn định vòng quay RPM)**: Ở mức đặt 4,000 RPM, đọc cảm biến quang trong 30 giây: tốc độ dao động không vượt quá $\pm 1.5\%$ (trong dải $3,940 - 4,060\text{ RPM}$).
- [ ] **Tiêu chí 3 (Khóa an toàn nắp buồng)**: Khi motor đang quay 4,000 RPM, mở hé nắp buồng $\ge 5\text{ mm}$: công tắc an toàn ngắt tín hiệu PWM, motor dừng quay hoàn toàn trong vòng $\le 2\text{ giây}$.
- [ ] **Tiêu chí 4 (Đo độ phẳng màng quang khắc)**: Màng sau khi sấy Softbake 90°C/60s đưa vào máy đo quang phổ ellipsometer hoặc kính hiển vi giao thoa: bề mặt đều màu một dải (không có vân lượn sóng hoặc mắt cá cá cặn bụi).
