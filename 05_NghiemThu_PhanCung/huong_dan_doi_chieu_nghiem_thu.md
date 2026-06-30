# Hướng Dẫn Đối Chiếu Kịch Bản Nghiệm Thu & Yêu Cầu Lắp Máy

Tài liệu này hướng dẫn bạn cách "soi" dữ liệu xuất ra từ kịch bản kiểm tra phần cứng (`script_kiem_tra_linh_kien.ps1`) và so sánh nó với báo giá gốc.

## Quy Trình 4 Bước Nghiệm Thu

1. Mở file `mau_yeu_cau_bao_gia_ai_dubbing.md` trên điện thoại hoặc máy tính khác để xem cấu hình bạn đã chốt.
2. Tại máy tính mới, chạy kịch bản PowerShell. Chờ kịch bản quét xong toàn bộ linh kiện.
3. Đối chiếu chéo 6 hạng mục theo bảng dưới đây:

## Bảng So Sánh Bắt Quả Tang

| Linh kiện | Chỉ số trên File Báo Giá | Chỉ số lấy từ Script PowerShell | Tiêu chí đạt (PASS) |
| :--- | :--- | :--- | :--- |
| **CPU** | Mã i5/i7 (VD: i5-13600K) | **Ten CPU** & **So Nhan (Cores)** | Mã CPU phải khớp. Chú ý số nhân/luồng phải cao (VD: 14 nhân, 20 luồng). Nếu tụt xuống 8 nhân là bị tráo đời cũ. |
| **Mainboard** | Hãng và Hậu tố (VD: B760M Mortar) | **Hang san xuat** & **Ma san pham** | Phải hiện đúng tên Hãng. Mã sản phẩm phải chứa hậu tố xịn (Mortar, TUF, Aorus). Nếu hiện "B760M-K" là bị tráo bản cắt giảm. |
| **RAM** | Tổng GB, Tốc độ MHz | **Toc do** & **TONG DUNG LUONG** | Tốc độ MHz phải bằng hoặc cao hơn báo giá (VD: 5200 MHz). RAM phải báo chạy Dual Channel. Không được bật XMP. |
| **Ổ cứng** | Tên hãng, Chuẩn Gen 4, Dung lượng | **Ma Model** & **Tinh trang SMART** | Xem thư mục CrystalDiskInfo vừa tải: Check thông số `Power On Hours` phải dưới 50 giờ và `Total Host Writes` phải gần bằng 0 để đảm bảo ổ mới tinh. Chú ý cảnh báo Windows cài quá 30 ngày. |
| **GPU** | RTX 4060Ti/4090, Dung lượng VRAM | **Ten Card** & **VRAM thuc te tu NVIDIA** | Lệnh NVIDIA phải báo thông số VRAM thực tế khớp với file yêu cầu (VD: `16384 MiB` cho Card 16GB). Cảnh báo nếu WMI báo VRAM ảo. |

4. **Bước 4 (Quan trọng nhất): Test Ép Tải (Stress Test) Card Đồ Họa**
- Yêu cầu kỹ thuật viên tải phần mềm **Furmark** hoặc **OCCT** (phần VRAM Test).
- Chạy fulload Card trong 15 phút.
- **PASS:** Máy không bị sập nguồn (chứng tỏ PSU đủ điện tải vọt), màn hình không bị rác/chớp đen (chứng tỏ VRAM không bị lỗi bóng).

## ⚠️ Lưu Ý Cực Kỳ Quan Trọng (Làm Thủ Công)
Như đã nhắc nhở ở bước báo giá, 3 linh kiện sau không có cổng giao tiếp dữ liệu nên **KHÔNG THỂ** dùng phần mềm để đọc thông số:
1. **Nguồn (PSU) - BẮT BUỘC KIỂM TRA BẰNG MẮT TRƯỚC KHI ĐÓNG NẮP CASE:**
   - Dùng đèn pin rọi vào đít máy, nhìn xem tem nhãn có ghi hãng nổi tiếng (Corsair/FSP/Seasonic) và có logo `80 Plus Gold` không.
   - Nguồn thật của Corsair/Seasonic có Serial Number có thể tra cứu trên web hãng.
   - ⛔ **Cảnh giác:** Nguồn "cỏ" kém chất lượng thường có vỏ nhựa bóng bẩy và quạt tản nhiệt to bất thường (14-15cm).
2. **Tản nhiệt:** Nhìn xem thợ lắp tản khí hay nước. Nếu là tản khí nhôm khối thì pass.
3. **Vỏ Case:** Đảm bảo vỏ lưới thông thoáng, không kính cường lực và quạt gió quay mạnh, không gắn LED lòe loẹt sai yêu cầu.

Nếu tất cả các chỉ số đều khớp 100%, bạn có thể tự tin thanh toán và mang hệ thống AI Dubbing về xưởng!
