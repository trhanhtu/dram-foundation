# Bill of Materials (BOM) & Vietnam Sourcing: Gen 1 Macroscopic Lithography Stage

- **Thiết bị**: Bàn trượt quang khắc 1 trục tuyến tính độ chính xác cao (Gen 1 Linear Stage)
- **Mục tiêu độ chính xác**: Sai số hành trình $\le \pm 0.05\text{ mm}$ (50 $\mu$m); Độ phân giải điều khiển vi bước $\le 0.1\ \mu\text{m}$
- **Chuẩn ứng dụng**: Di chuyển phiến bán dẫn (Wafer 2"/4" hoặc kính hiển vi) dưới nguồn sáng UV 365nm / 405nm
- **Ngân sách ước tính**: ~850.000 - 1.150.000 VNĐ (~$35 - $48 USD)

---

## 1. Bảng Linh Kiện Chi Tiết (Chi phí & Nguồn cung ứng tại Việt Nam)

| STT | Tên linh kiện & Quy cách kỹ thuật | Số lượng | Đơn giá ước tính (VNĐ) | Thành tiền (VNĐ) | Kênh mua sắm / Nhà cung cấp tại Việt Nam | Ghi chú kỹ thuật |
| :--- | :--- | :---: | :---: | :---: | :--- | :--- |
| **1** | **Khung nhôm định hình 2020 V-Slot** (dài 300mm x 2 thanh, 200mm x 2 thanh, nhôm anodized đen) | 1 bộ | 110.000 | 110.000 | • Xưởng nhôm CNC (Shopee / Lazada)<br>• Cửa hàng cơ khí Minh An / Nhôm Định Hình VN | Cắt vuông góc 90° bằng máy cưa tua chậm để đảm bảo độ phẳng đế khung. |
| **2** | **Ray trượt tuyến tính MGN12H + Con trượt** (chiều dài ray 250mm, thép chịu lực mạ crom) | 1 bộ | 195.000 | 195.000 | • LinhKien3D, HShop, MakerLab<br>• Shopee VN (Tìm: `Ray trượt MGN12H 250mm`) | Rửa sạch dầu chống rỉ bằng cồn IPA, tra mỡ silicon trắng hoặc mỡ bò chịu nhiệt trước khi lắp ráp. |
| **3** | **Trục vít me bi T8 bước 2mm (Lead 2mm)** dài 250mm + Đai ốc đồng khử rơ (Anti-Backlash Nut) | 1 bộ | 75.000 | 75.000 | • Các shop máy in 3D / CNC mini tại Hà Nội & TP.HCM (LinhKienCNC, BanLinhKien) | Chọn loại **Lead 2mm** (1 vòng quay tịnh tiến 2mm) thay vì Lead 8mm để tăng độ phân giải cơ học gấp 4 lần. |
| **4** | **Động cơ bước NEMA 17** (Model 17HS4401, góc bước 1.8°, mô-men xoắn 40 N.cm, trục 5mm) | 1 cái | 115.000 | 115.000 | • Chợ Trời (Phố Huế, HN) / Chợ Dân Sinh (Q1, HCM)<br>• NSHOP, TheGioiIC, Shopee | Động cơ 2 pha 4 dây lưỡng cực (bipolar). Dây nối 4-pin XH2.54. |
| **5** | **Khớp nối mềm nhôm D19L25 (5mm sang 8mm)** | 1 cái | 25.000 | 25.000 | • Cửa hàng phụ kiện máy in 3D / Shopee | Khớp nối hoa mận hoặc rãnh lò xo giúp bù góc lệch giữa trục motor và vít me. |
| **6** | **Gối đỡ trục vít me KP08 / KFL08** (đường kính trong 8mm) | 2 cái | 20.000 | 40.000 | • LinhKienCNC / BanLinhKien VN | Cố định hai đầu trục vít me, triệt tiêu độ rơ dọc trục. |
| **7** | **Mạch điều khiển ESP32 DevKit V1** (30 chân, Dual-Core 240MHz, tích hợp WiFi/BLE) | 1 cái | 85.000 | 85.000 | • HShop.vn, TheGioiIC, Cytron VN, Shopee | Nạp firmware qua cổng Micro-USB / Type-C. Chạy vòng lặp điều khiển thời gian thực. |
| **8** | **Module điều khiển động cơ bước TMC2209 V1.3** (kèm miếng tản nhiệt nhôm) | 1 cái | 75.000 | 75.000 | • LinhKien3D, MakerLab, HShop VN | Hỗ trợ vi bước lên tới **1/256 microstep**, chạy siêu êm bằng công nghệ StealthChop2, không rung lắc làm vỡ vạch quang khắc. |
| **9** | **Cảm biến quang học hành trình (Optical Endstop)** | 1 cái | 18.000 | 18.000 | • Các shop linh kiện máy in 3D RepRap VN | Cảm biến quang chặn tia hồng ngoại, không có tiếp điểm cơ khí, độ lặp lại vị trí home $< 5\ \mu\text{m}$. |
| **10** | **Nguồn tổ ong 24V 5A DC** (vỏ nhôm tổ ong) | 1 cái | 125.000 | 125.000 | • Chợ Trời, Chợ Nhật Tảo, Điện Tử Minh Hà, Shopee | Cấp điện áp 24V giúp động cơ bước đạt gia tốc cao mà không bị mất bước (skip step). |
| **11** | **Module hạ áp DC-DC LM2596** (24V xuống 5V 2A cấp nguồn cho ESP32) | 1 cái | 18.000 | 18.000 | • Các shop điện tử cơ bản VN | Điều chỉnh biến trở về chính xác 5.0V trước khi cắm vào chân Vin của ESP32. |
| **12** | **Bộ ốc vít, tán nhôm chữ T (T-nut M4/M3, ốc lục giác chìm inox 304)** | 1 túi | 40.000 | 40.000 | • Cửa hàng kim khí chợ trời / Shopee | Bắt ray trượt MGN12 vào rãnh nhôm 2020. |
| **13** | **Bàn gá wafer nhôm tấm 5mm** (kích thước 80x80mm) | 1 tấm | 45.000 | 45.000 | • Xưởng cắt nhôm phay CNC theo yêu cầu / In 3D nhựa PETG | Có lỗ ren M3 để bắt kẹp giữ phiến silicon / tấm kính mang mẫu. |
| **TỔNG** | **Tổng chi phí chế tạo hoàn chỉnh bàn trượt** | | | **866.000 VNĐ** | *(Tương đương ~36 USD - Đầy đủ linh kiện điện cơ)* |

---

## 2. Quy Trình Lắp Ráp Cơ Khí & Căn Chỉnh Hình Học

1. **Khung đế nhôm định hình**:
   - Dùng 4 ke góc nhôm đúc và tán T bắt vuông góc 4 thanh nhôm 2020 thành khung chữ nhật $300\text{ mm} \times 200\text{ mm}$.
   - Dùng thước vuông góc cơ khí (Precision Square 90°) kiểm tra góc chéo để không bị vặn xoắn.
2. **Lắp ray trượt tuyến tính MGN12H**:
   - Đặt thanh ray MGN12H vào rãnh nhôm giữa.
   - Vặn nhẹ các ốc M3 vào tán T, chưa siết chặt.
   - Dùng đồng hồ so (Dial Indicator) rà dọc hành trình ray trượt: độ lệch song song $\le 0.02\text{ mm}$ dọc chiều dài 250mm.
   - Siết chặt các ốc theo thứ tự từ giữa ra hai đầu.
3. **Lắp trục vít me và động cơ NEMA 17**:
   - Gắn giá đỡ motor NEMA 17 vào đầu khung nhôm.
   - Nối trục động cơ 5mm với vít me bi T8 qua khớp nối mềm nhôm D19L25.
   - Luồn đai ốc đồng khử rơ (anti-backlash nut) vào vít me và siết vào bàn gá.
   - Khóa đầu còn lại của vít me bằng gối đỡ KP08. Dùng tay quay thử trục: bàn trượt phải lướt êm ái, không bị kẹt hay bó cứng ở bất kỳ điểm nào.
4. **Gắn cảm biến quang học hành trình (Optical Endstop)**:
   - Gắn endstop tại vị trí đầu hành trình (Home Position).
   - Bắt một lá cờ chắn sáng mỏng (bằng nhôm hoặc nhựa đen) vào bàn trượt sao cho khi bàn lùi về sát mép sẽ cắt dứt khoát tia hồng ngoại của cảm biến.

---

## 3. Tiêu Chí Nghiệm Thu Vật Lý Thực Tế (Bits-to-Atoms Checklist)

Theo đúng quy chuẩn nghiệm thu của Knowledge OS:
- [ ] **Tiêu chí 1 (Độ phẳng & song song)**: Dùng đồng hồ so cơ khí rà bề mặt bàn gá wafer: độ võng mặt phẳng không vượt quá $\pm 0.03\text{ mm}$ trên hành trình $100\text{ mm}$.
- [ ] **Tiêu chí 2 (Độ lặp lại vị trí - Repeatability)**: Dùng thước kẹp điện tử điện tử (Digital Caliper 0.01mm) đo điểm dừng sau 1,000 chu kỳ tịnh tiến tới-lui: sai số vị trí $\le \pm 0.02\text{ mm}$.
- [ ] **Tiêu chí 3 (Độ ổn định nhiệt động cơ)**: Chạy liên tục trong 4 giờ với dòng $1.0\text{ A}$ (TMC2209 StealthChop): nhiệt độ vỏ motor đo bằng súng hồng ngoại $\le 55^\circ\text{C}$.
- [ ] **Tiêu chí 4 (Độ rung động cơ học)**: Đặt chén nước nhỏ lên bàn gá khi chạy vi bước 1/256: mặt nước phẳng lặng, không xuất hiện vân sóng giao thoa cộng hưởng cơ học.
