# PHIẾU YÊU CẦU BÁO GIÁ - HỆ THỐNG PC AI DUBBING 24/7

**Ghi chú quan trọng dành cho Sale / Kỹ thuật viên build máy:**
Hệ thống này được sử dụng để chạy các mô hình Trí tuệ nhân tạo (AI Local Models) sinh âm thanh và dịch thuật, yêu cầu **vận hành full-load 100% qua đêm (24/7)**. 
Tư duy build máy cho hệ thống này khác hoàn toàn với PC Gaming. Kính đề nghị cửa hàng tuân thủ tuyệt đối "Trọng số ưu tiên ngân sách" (Tổng 100%) bên dưới cho cả 8 thành phần cấu tạo.
❌ **TUYỆT ĐỐI KHÔNG TỰ Ý HẠ CẤP các linh kiện có trọng số sinh tử (như GPU, Nguồn, SSD) để nâng cấp CPU hay LED RGB.**

---

## 1. CẤU HÌNH TỐI THIỂU (MỨC CƠ BẢN)
*Quy mô: Phục vụ chạy tuần tự 1 luồng tác vụ.*

| Linh Kiện | Trọng Số | Yêu Cầu Kỹ Thuật Chi Tiết (Vui lòng báo giá sát thông số) |
| :--- | :---: | :--- |
| **1. GPU (Card Đồ Họa)** | **45%** | **1x NVIDIA RTX 4060 Ti - BẢN 16GB VRAM**.<br>*(Lưu ý: Bắt buộc bản 16GB VRAM. Tuyệt đối không lấy bản 8GB. Không thay bằng card AMD).* |
| **2. Nguồn (PSU)** | **12%** | **750W chuẩn 80 Plus Gold** (Chuẩn ATX 3.0 càng tốt). Yêu cầu các hãng Tier A (Corsair, Seasonic, FSP) để tránh sập nguồn đêm. |
| **3. RAM** | **10%** | **64GB DDR5** (2 thanh x 32GB). Bus 5600 hoặc 6000MHz. Ưu tiên dung lượng khổng lồ để dự phòng tràn VRAM. Không cần Bus cao. |
| **4. Storage (Ổ cứng)** | **10%** | **1TB NVMe SSD Gen 4**.<br>*(Bắt buộc báo giá dòng có chỉ số độ bền TBW > 1000 như Samsung 990 Pro, WD SN850X vì AI ghi/xoá file rác cường độ rất cao).* |
| **5. CPU** | **8%** | Intel Core i5-13600K hoặc AMD Ryzen 5 7600X. |
| **6. Tản nhiệt & Quạt gió** | **8%** | Tản nhiệt CPU tháp đôi (VD: Noctua NH-D15, Thermalright FC140) + Gắn tối đa quạt hút/thổi cho Case. |
| **7. Mainboard** | **5%** | B760 (Intel) hoặc B650 (AMD). Yêu cầu bản có tản nhiệt VRM tốt (như dòng Mortar, TUF, Aorus). |
| **8. Vỏ Case (Chassis)** | **2%** | Dòng Mid-Tower mặt lưới (Mesh) thật thoáng. KHÔNG CẦN mặt kính cường lực hay LED. |

---

## 2. CẤU HÌNH TIÊU CHUẨN (HIỆU NĂNG / GIÁ THÀNH TỐT NHẤT)
*Quy mô: Phục vụ xử lý đa luồng, chạy song song nhiều mô hình lớn.*

| Linh Kiện | Trọng Số | Yêu Cầu Kỹ Thuật Chi Tiết (Vui lòng báo giá sát thông số) |
| :--- | :---: | :--- |
| **1. GPU (Card Đồ Họa)** | **45%** | **1x NVIDIA RTX 4090 24GB**.<br>*(Ghi chú: Có thể báo giá thêm phương án RTX 3090 24GB cũ nếu cửa hàng có sẵn hàng bảo hành 1 đổi 1 tốt).* |
| **2. Nguồn (PSU)** | **12%** | **1000W đến 1200W chuẩn 80 Plus Platinum / Gold** của hãng lớn. Đảm bảo chịu được Power Spike. |
| **3. RAM** | **10%** | **128GB DDR5** (4 thanh x 32GB). |
| **4. Storage (Ổ cứng)** | **10%** | **TỔNG 3TB NVMe Gen 4 (Yêu cầu chia làm 2 ổ vật lý):**<br>- Ổ 1: 1TB NVMe Gen 4 (Cài Hệ điều hành & Kho Models AI).<br>- Ổ 2: 2TB NVMe Gen 4 có TBW siêu cao (Làm ổ Cache/Workspace cày file rác). |
| **5. CPU** | **8%** | Intel Core i7-14700K hoặc AMD Ryzen 9 7900X / 7950X. |
| **6. Tản nhiệt & Quạt gió** | **8%** | Tản nhiệt nước AIO 360mm uy tín (Corsair, NZXT, Deepcool) + Bộ 6-9 quạt thông gió vỏ case (Airflow chuyên dụng). |
| **7. Mainboard** | **5%** | Z790 (Intel) hoặc X670 (AMD). Hỗ trợ dàn Phase điện (VRM) mạnh mẽ để chịu tải cày qua đêm. |
| **8. Vỏ Case (Chassis)** | **2%** | Dòng Mid/Full-Tower mặt lưới (Mesh) thật thoáng. Phải có thanh chống VGA chống xệ card. |

---

## 3. CẤU HÌNH CAO CẤP (XƯỞNG SẢN XUẤT CÔNG NGHIỆP)
*Quy mô: Phục vụ chạy farm tự động hàng loạt tốc độ siêu tốc.*

| Linh Kiện | Trọng Số | Yêu Cầu Kỹ Thuật Chi Tiết (Vui lòng báo giá sát thông số) |
| :--- | :---: | :--- |
| **1. GPU (Card Đồ Họa)** | **45%** | **2x NVIDIA RTX 4090 24GB (Chạy Dual - Tổng 48GB VRAM)** hoặc **1x RTX 6000 Ada (48GB)**.<br>*(Lưu ý cực kỳ quan trọng: Nếu build 2 card RTX 4090, bắt buộc khoảng cách khe PCIe X16 trên Main phải rất xa nhau để hút khí).* |
| **2. Nguồn (PSU)** | **12%** | **1600W chuẩn 80 Plus Titanium** (VD: Corsair AX1600i). Chịu tải "Peak Power" khi 2 VGA cùng full-load. |
| **3. RAM** | **10%** | **192GB hoặc 256GB DDR5**. |
| **4. Storage (Ổ cứng)** | **10%** | **Hệ thống 3 cấp lưu trữ:**<br>- Ổ 1: 2TB NVMe Gen 4 cao cấp (Cài OS/Models).<br>- Ổ 2: 4TB NVMe Gen 4 (Raid 0 nếu cần tốc độ cực hạn, làm Workspace xử lý).<br>- Ổ 3: 16TB - 22TB HDD dòng Enterprise (Để lưu trữ thành phẩm). |
| **5. CPU** | **8%** | AMD Ryzen Threadripper PRO 7000 Series (VD: 7960WX) hoặc dòng Intel Xeon tương đương.<br>*(Mục đích chính: Cung cấp đủ băng thông làn PCIe rộng mở cho 2 Card đồ họa chạy hết công suất).* |
| **6. Tản nhiệt & Quạt gió** | **8%** | Tản nhiệt nước Custom Water Cooling ốp block trực tiếp cho cả khối CPU và 2 VGA hoặc hệ thống quạt hút gió công nghiệp cực mạnh. |
| **7. Mainboard** | **5%** | Bo mạch chủ dòng Workstation (VD: W790 hoặc TRX50). |
| **8. Vỏ Case (Chassis)** | **2%** | Case thiết kế Full-Tower khổng lồ. Khung thép siêu chịu lực đỡ 2 card đồ họa. |

---

## 4. CẤU HÌNH ĐẶC BIỆT: TỐI ƯU ÉP NGÂN SÁCH (DƯỚI 35 TRIỆU)
*Quy mô: Đảm bảo "sống sót" chạy AI tốt với VRAM 16GB, nhưng ép tối đa các thông số phụ trợ để ép giá xuống mức thấp nhất có thể.*

| Linh Kiện | Trọng Số | Yêu Cầu Kỹ Thuật Chi Tiết (Vui lòng báo giá sát thông số) |
| :--- | :---: | :--- |
| **1. GPU (Card Đồ Họa)** | **45%** | **1x NVIDIA RTX 4060 Ti - BẢN 16GB VRAM**. <br>*(Bắt buộc giữ nguyên để đảm bảo chạy được AI, không được hạ xuống bản 8GB).* |
| **2. Nguồn (PSU)** | **12%** | **750W chuẩn 80 Plus Bronze / Gold** (VD: Deepcool PK750D, MSI MAG A750BN). |
| **3. RAM** | **10%** | **64GB DDR5** (Ưu tiên bus 5200MHz để tối ưu chi phí). |
| **4. Storage (Ổ cứng)** | **10%** | **1TB NVMe SSD Gen 4** có TBW cao (Quyết không cắt giảm ổ cứng để bảo vệ dữ liệu AI). |
| **5. CPU** | **8%** | Intel Core i5-13400F hoặc i5-12400F hoặc Ryzen 5 7600.<br>*(Ép giá sâu nhất ở phần CPU này vì tác vụ AI không cần chip mạnh).* |
| **6. Tản nhiệt & Quạt gió** | **8%** | Tản nhiệt khí đơn (VD: Thermalright Assassin X 120, ID-Cooling SE-214-XT) + 3 quạt case. |
| **7. Mainboard** | **5%** | B760M (Intel) hoặc B650M (AMD). Chọn dòng giá rẻ có tản VRM cơ bản. |
| **8. Vỏ Case (Chassis)** | **2%** | Dòng Mid-Tower mặt lưới (Mesh) thông gió tốt, không cần kính, không cần LED. |

---

## 5. ĐIỀU KHOẢN NGHIỆM THU VÀ BÀN GIAO KỸ THUẬT (BẮT BUỘC)
*Để tiết kiệm thời gian làm việc cho cả 2 bên, kính đề nghị quý cửa hàng/đại lý lưu ý các tiêu chuẩn nghiệm thu "cứng" sau đây trước khi xuất báo giá. Chúng tôi sẽ từ chối nhận máy nếu vi phạm:*

1. **Minh bạch mã linh kiện:** Báo giá phải ghi chính xác tên Hãng và Mã Hậu Tố của linh kiện (Ví dụ: Main B760M *Mortar*, SSD 1TB *Samsung 990 Pro*). Tuyệt đối từ chối các báo giá ghi chung chung kiểu "Main B760M" hay "SSD 1TB Gen 4".
2. **Tiêu chuẩn Nguồn (PSU) & Ổ cứng:** Trái tim của hệ thống AI là Nguồn và SSD. Bắt buộc sử dụng Nguồn chuẩn 80 Plus Gold/Platinum từ các hãng Tier A (Corsair, FSP, Seasonic...). Tuyệt đối không sử dụng nguồn cỏ, nguồn công suất ảo. Ổ cứng phải là dòng có chỉ số TBW cao.
3. **Không đánh tráo khái niệm:** Khách hàng hiểu rõ sức mạnh thế hệ phần cứng. Tuyệt đối không tư vấn "hạ cấp" Card đồ họa (GPU) để lấy ngân sách đập vào CPU i7/i9 đời cũ. 
4. **Thẩm mỹ & Tản nhiệt:** Máy đặt tại xưởng cày 24/7. Yêu cầu KHÔNG lắp kính cường lực, KHÔNG gắn quạt LED RGB loè loẹt để tránh rủi ro chập cháy tĩnh điện. Thay vào đó, dồn toàn bộ ngân sách vào Quạt thông gió công suất lớn (Airflow) và tản nhiệt khí nhôm khối.
5. **Nghiệm thu phần cứng:** Đối với linh kiện mua mới, khách hàng sẽ tự tay rạch Seal Card đồ họa (GPU) và CPU tại chỗ. Đối với phương án dùng Card cũ (như RTX 3090), cửa hàng phải có biên bản cam kết **bảo hành lỗi 1 đổi 1 nhanh chóng** để không làm gián đoạn tiến độ render công nghiệp của xưởng.
