# Hướng Dẫn Cài Đặt PC Ban Đầu (Cho Hệ Thống 24/7)

Khi chạy hệ thống render AI, việc máy tự động vào chế độ ngủ (Sleep) hoặc Windows tự động khởi động lại (Restart) để cập nhật giữa đêm sẽ làm hỏng toàn bộ mẻ render, gây lãng phí hàng chục giờ đồng hồ.

## Tự động hóa thiết lập (1 Click)
Thay vì phải cấu hình thủ công trong Control Panel, bạn chỉ cần chạy Script sau bằng quyền Quản trị viên.

**Cách thực hiện:**
1. Click chuột phải vào file **`setup_windows_24_7.ps1`**
2. Chọn **`Run with PowerShell`**
3. Nếu Windows yêu cầu quyền Administrator, bấm **Yes**
4. Chờ script chạy (mất 2 giây) và báo hoàn tất.

**Script này sẽ tự động làm gì?**
- Tắt chế độ Sleep / Tắt màn hình
- Tắt tính năng ngủ đông (Hibernate) tiết kiệm hàng chục GB dung lượng ổ C:
- Ép Windows sử dụng cấu hình điện High Performance
- Cấm Windows Update tự động khởi động lại máy.

## Lời khuyên tối ưu hiệu năng bổ sung

### 1. Cài đặt Driver NVIDIA
Khi tải Driver cho Card đồ họa từ trang chủ NVIDIA, hệ thống thường gợi ý bản `Game Ready Driver`. 
👉 **HÃY CHUYỂN SANG BẢN `NVIDIA STUDIO DRIVER`.**
Bản Studio được tối ưu hóa đặc biệt cho các tác vụ render, Blender, và AI. Nó ít cập nhật hơn nhưng hoạt động ổn định và cực kỳ lỳ lợm khi treo máy 24/7, ít gặp lỗi văng phần mềm hơn bản Game.

### 2. Giám sát nhiệt độ
Bạn nên tải phần mềm **HWiNFO64** miễn phí và cấu hình tính năng `Alert` (Cảnh báo). 
Hãy thiết lập để phần mềm phát âm thanh cảnh báo hoặc gửi thông báo nếu `GPU Temperature` (Nhiệt độ Card đồ họa) **vượt quá 85°C**. Điều này giúp bạn cứu được Card trước khi nó bị cháy do quạt tản nhiệt trong case vô tình bị hỏng.
