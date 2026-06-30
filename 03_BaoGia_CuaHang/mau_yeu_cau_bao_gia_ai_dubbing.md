# PHIẾU YÊU CẦU BÁO GIÁ - HỆ THỐNG PC AI DUBBING 24/7

**Ghi chú quan trọng dành cho Sale / Kỹ thuật viên build máy:**
Hệ thống này được sử dụng để chạy các mô hình Trí tuệ nhân tạo (AI Local Models) sinh âm thanh và dịch thuật, yêu cầu **vận hành full-load 100% qua đêm (24/7)**. 
Tư duy build máy cho hệ thống này khác hoàn toàn với PC Gaming. Kính đề nghị cửa hàng tuân thủ tuyệt đối "Trọng số ưu tiên ngân sách" (Tổng 100%) bên dưới cho cả 8 thành phần cấu tạo.
❌ **TUYỆT ĐỐI KHÔNG TỰ Ý HẠ CẤP các linh kiện có trọng số sinh tử (như GPU, Nguồn, SSD) để nâng cấp CPU hay LED RGB.**

---

## 1. CẤU HÌNH TỐI THIỂU - PHIÊN BẢN 1 (VGA 16GB THẾ HỆ 5)
*Quy mô: Phục vụ chạy tuần tự 1 luồng tác vụ. Tối ưu điện năng.*

| Linh Kiện | Trọng Số | Yêu Cầu Kỹ Thuật Chi Tiết (Vui lòng báo giá sát thông số) |
| :--- | :---: | :--- |
| **1. GPU (Card Đồ Họa)** | **45%** | **1x NVIDIA RTX 5060 Ti - BẢN 16GB VRAM**.<br>*(Lưu ý: Nếu không có hàng có thể lấy tạm RTX 4060 Ti 16GB. Bắt buộc bản 16GB VRAM. Tuyệt đối không lấy bản 8GB. Không thay bằng card AMD).* |
| **2. Nguồn (PSU)** | **12%** | **750W chuẩn 80 Plus Gold** (Chuẩn ATX 3.0 càng tốt). Yêu cầu các hãng Tier A (Corsair, Seasonic, FSP) để tránh sập nguồn đêm. |
| **3. RAM** | **10%** | **64GB DDR5** (2 thanh x 32GB). Bus 5600 hoặc 6000MHz. Ưu tiên dung lượng khổng lồ để dự phòng tràn VRAM. Không cần Bus cao. |
| **4. Storage (Ổ cứng)** | **10%** | **1TB NVMe SSD Gen 4**.<br>*(Bắt buộc báo giá dòng có chỉ số độ bền TBW > 1000 như Samsung 990 Pro, WD SN850X vì AI ghi/xoá file rác cường độ rất cao).* |
| **5. CPU** | **8%** | Intel Core i5-13600K hoặc AMD Ryzen 5 7600X (Hoặc thấp hơn như i5-13400F để ép ngân sách). |
| **6. Tản nhiệt & Quạt gió** | **8%** | Tản nhiệt CPU tháp đôi (VD: Noctua NH-D15, Thermalright FC140) + Gắn tối đa quạt hút/thổi cho Case. |
| **7. Mainboard** | **5%** | B760 (Intel) hoặc B650 (AMD). Yêu cầu bản có tản nhiệt VRM tốt (như dòng Mortar, TUF, Aorus). |
| **8. Vỏ Case (Chassis)** | **2%** | Dòng Mid-Tower mặt lưới (Mesh) thật thoáng. KHÔNG CẦN mặt kính cường lực hay LED. |

---

## 2. CẤU HÌNH TỐI THIỂU - PHIÊN BẢN 2 (VGA 24GB THẾ HỆ 3 CŨ)
*Quy mô: Phục vụ chạy các mô hình ngôn ngữ lớn (LLMs) cần rất nhiều VRAM. Chấp nhận rủi ro hao điện và linh kiện cũ.*

| Linh Kiện | Trọng Số | Yêu Cầu Kỹ Thuật Chi Tiết (Vui lòng báo giá sát thông số) |
| :--- | :---: | :--- |
| **1. GPU (Card Đồ Họa)** | **45%** | **1x NVIDIA RTX 3090 24GB (HÀNG CŨ / LIKE NEW)**.<br>*(Bắt buộc bản 24GB VRAM. Yêu cầu Card đã được tra lại keo tản nhiệt và test nhiệt độ full-load không quá 80 độ C).* |
| **2. Nguồn (PSU)** | **12%** | **1000W chuẩn 80 Plus Gold / Platinum**. Yêu cầu hãng Tier A. <br>*(Card 3090 chịu Power Spike rất gắt, tuyệt đối không dùng nguồn dưới 1000W để tránh cháy nổ ban đêm).* |
| **3. RAM** | **10%** | **64GB DDR5** (2 thanh x 32GB). |
| **4. Storage (Ổ cứng)** | **10%** | **1TB NVMe SSD Gen 4** (Samsung 990 Pro hoặc tương đương dòng độ bền siêu cao). |
| **5. CPU** | **8%** | Intel Core i5-13600K hoặc Core i7-13700K. |
| **6. Tản nhiệt & Quạt gió** | **8%** | Tản nhiệt nước AIO 360mm hoặc Khí Tháp Đôi loại cực lớn. <br>*(Do 3090 tỏa nhiệt như lò sưởi, phải lắp full quạt Airflow công nghiệp cho vỏ Case).* |
| **7. Mainboard** | **5%** | Z790 (Intel) hoặc X670 (AMD). Hỗ trợ dàn Phase điện (VRM) mạnh mẽ chịu tải qua đêm. |
| **8. Vỏ Case (Chassis)** | **2%** | Dòng Full-Tower hoặc Mid-Tower siêu lớn mặt lưới (Mesh). Phải có thanh chống VGA chống xệ card. |

---

## 3. ĐIỀU KHOẢN NGHIỆM THU VÀ BÀN GIAO KỸ THUẬT (BẮT BUỘC)
*Để tiết kiệm thời gian làm việc cho cả 2 bên, kính đề nghị quý cửa hàng/đại lý lưu ý các tiêu chuẩn nghiệm thu "cứng" sau đây trước khi xuất báo giá. Chúng tôi sẽ từ chối nhận máy nếu vi phạm:*

1. **Minh bạch mã linh kiện:** Báo giá phải ghi chính xác tên Hãng và Mã Hậu Tố của linh kiện (Ví dụ: Main B760M *Mortar*, SSD 1TB *Samsung 990 Pro*). Tuyệt đối từ chối các báo giá ghi chung chung kiểu "Main B760M" hay "SSD 1TB Gen 4".
2. **Tiêu chuẩn Nguồn (PSU) & Ổ cứng:** Trái tim của hệ thống AI là Nguồn và SSD. Bắt buộc sử dụng Nguồn chuẩn 80 Plus Gold/Platinum từ các hãng Tier A (Corsair, FSP, Seasonic...). Tuyệt đối không sử dụng nguồn cỏ, nguồn công suất ảo. Ổ cứng phải là dòng có chỉ số TBW cao.
3. **Không đánh tráo khái niệm:** Khách hàng hiểu rõ sức mạnh thế hệ phần cứng. Tuyệt đối không tư vấn "hạ cấp" Card đồ họa (GPU) để lấy ngân sách đập vào CPU i7/i9 đời cũ. 
4. **Thẩm mỹ & Tản nhiệt:** Máy đặt tại xưởng cày 24/7. Yêu cầu KHÔNG lắp kính cường lực, KHÔNG gắn quạt LED RGB loè loẹt để tránh rủi ro chập cháy tĩnh điện. Thay vào đó, dồn toàn bộ ngân sách vào Quạt thông gió công suất lớn (Airflow) và tản nhiệt khí nhôm khối.
5. **Nghiệm thu phần cứng:** Đối với linh kiện mua mới, khách hàng sẽ tự tay rạch Seal Card đồ họa (GPU) và CPU tại chỗ. Đối với phương án dùng Card cũ (như RTX 3090), cửa hàng phải cam kết:
   - **Bảo hành tối thiểu 6 tháng** (Không nhận hàng bảo hành 1-3 tháng)
   - **Xử lý sự cố trong vòng tối đa 3 ngày làm việc** (Đổi trả/Cho mượn ngay tại chỗ, không nhận hình thức "Gửi đi hãng chờ 2 tuần")
6. **Chế tài vi phạm:** Nếu qua quá trình chạy Script kiểm tra phần cứng phát hiện linh kiện cũ (ổ cứng cày coin), sai mã, giả BIOS, hoặc cố tình tráo đổi linh kiện không thông báo trước, bên mua có quyền **ĐƠN PHƯƠNG HỦY GIAO DỊCH** và từ chối nhận máy. Bên bán phải chịu toàn bộ trách nhiệm và chi phí vận chuyển 2 chiều.

---

## 4. PHÍ ẨN VÀ PHỤ KIỆN
*Cửa hàng vui lòng báo rõ các chi phí sau (nếu có):*
- **Phí lắp ráp:** (Yêu cầu miễn phí khi mua trọn bộ)
- **Bản quyền Windows:** (Tùy chọn, bên mua có thể tự trang bị)
- **Cáp kết nối & Phụ kiện nhỏ:** Phải bao gồm theo chuẩn của nhà sản xuất, không phụ thu.

## 5. BỘ LƯU ĐIỆN (UPS) - KHUYẾN NGHỊ BẮT BUỘC
*Máy AI render 24/7 tuyệt đối không được mất điện đột ngột gây hỏng file model.*
- Cửa hàng vui lòng báo giá thêm 01 Bộ lưu điện (UPS) công suất tối thiểu **1500VA - 2000VA**.
- Yêu cầu dòng Line-Interactive hoặc Online (VD: APC, Santak, CyberPower).
