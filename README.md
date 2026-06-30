# 🚀 AI Dubbing PC Procurement Workflow (Phiên bản V6)

Chào mừng bạn đến với Quy trình Mua sắm và Lắp ráp máy tính (PC) chuyên nghiệp dành riêng cho hệ thống AI Dubbing (Hoạt động độc lập 24/7). 

Dự án này là một quy trình khép kín gồm 6 bước để bảo vệ bạn khỏi những chiêu trò lừa đảo của giới bán lẻ phần cứng, đảm bảo bạn mua được dàn máy AI mạnh mẽ nhất với giá tốt nhất mà **không cần rành về kỹ thuật**.

## 📌 Checklist Nhanh Dành Cho Người Mới
> Bắt đầu ngay tại file: **`00_CHECKLIST_NHANH.md`**
> Đây là bản tóm tắt 1 trang, hướng dẫn bạn chi tiết những gì cần nói và cần làm khi đi ra cửa hàng.

## 🗂️ Cấu Trúc Kho Mã Nguồn

| Thư mục | Chức năng | Phân loại |
| :--- | :--- | :--- |
| `01_TieuChuan_PhanCung` | Nắm rõ luật chơi. Tiêu chuẩn phần cứng và công thức chia ngân sách (Weightage). | **Lý thuyết** |
| `02_ThamChieu_Gia` | Công cụ tự động quét giá (Scraping) từ 6 trang bán lẻ lớn nhất VN để làm bằng chứng mặc cả. | **Công cụ AI** |
| `03_BaoGia_CuaHang` | Mẫu báo giá "sát thủ" gửi cho cửa hàng. Có sẵn điều khoản ép linh kiện, UPS và chống tráo đồ. | **Thực chiến** |
| `04_ThamDinh_BaoGia` | Chốt chặn kiểm duyệt báo giá bằng AI (Prompt có sẵn) để loại bỏ cửa hàng xả rác tồn kho. | **Kiểm duyệt** |
| `05_NghiemThu_PhanCung` | Công cụ tự động soi linh kiện ẩn sâu trong hệ điều hành Windows + Hướng dẫn đối chiếu bằng mắt thường. | **Nghiệm thu** |
| `06_CaiDat_BanDau` | Script cài đặt 1-click chặn Windows tự restart và tối ưu điện năng cho việc treo máy 24/7. | **Vận hành** |

## ⚡ Hướng Dẫn Sử Dụng Công Cụ

### 1. Công cụ Cào Giá (Thư mục 02)
Chỉ cần chạy file `CHAY_NGAY.bat`, hệ thống sẽ tự động tổng hợp bảng giá thấp nhất thị trường và xuất ra bảng dự toán chi tiết + vẽ biểu đồ xu hướng giá. Bạn dùng bảng này để gửi cho Sale ép giá.

### 2. Kích Hoạt Cloud Execution (Nghiệm thu - Thư mục 05)
Khi mang PC về, bạn **không cần mang theo USB**.
Chỉ cần cắm Internet cho PC, mở PowerShell và gõ dòng lệnh "hút" kịch bản từ kho mã nguồn này về:

```powershell
irm https://raw.githubusercontent.com/duc1408/AI-Dubbing-PC-Procurement/main/05_NghiemThu_PhanCung/script_kiem_tra_linh_kien.ps1 | iex
```

Hệ thống sẽ ngay lập tức đối chiếu, cảnh báo các linh kiện bị tráo, và xuất file biên bản bảo hành ra Desktop.

---
*Dự án này được tối ưu hóa kĩ thuật để đảm bảo máy móc hoạt động bền bỉ trong môi trường công nghiệp.*
