# 🚀 AI Dubbing PC Procurement Workflow

Chào mừng bạn đến với Quy trình Mua sắm và Lắp ráp máy tính (PC) chuyên nghiệp dành riêng cho hệ thống AI Dubbing (Hoạt động độc lập 24/7). 

Dự án này là một quy trình khép kín gồm 4 bước để bảo vệ bạn khỏi những chiêu trò lừa đảo của giới bán lẻ phần cứng.

## 🗂️ Cấu Trúc Kho Mã Nguồn

| Thư mục | Chức năng | Phân loại |
| :--- | :--- | :--- |
| `01_TieuChuan_PhanCung` | Nắm rõ luật chơi. Tiêu chuẩn phần cứng và công thức chia ngân sách (Weightage). | **Lý thuyết** |
| `02_ThamChieu_Gia` | Công cụ tự động quét giá (Scraping) từ 6 trang bán lẻ lớn nhất VN để làm bằng chứng mặc cả. | **Công cụ AI** |
| `03_BaoGia_CuaHang` | Mẫu báo giá "sát thủ" gửi cho cửa hàng. Có sẵn điều khoản ép linh kiện và chống tráo đồ. | **Thực chiến** |
| `04_NghiemThu_PhanCung` | Công cụ tự động soi linh kiện ẩn sâu trong hệ điều hành Windows + Hướng dẫn đối chiếu. | **Nghiệm thu** |

## ⚡ Hướng Dẫn Kích Hoạt Cloud Execution (Thực thi trên mây)

Điểm sức mạnh lớn nhất của dự án này nằm ở thư mục `04`. Khi mang PC về, bạn **không cần mang theo USB**.
Chỉ cần cắm Internet cho PC, mở PowerShell và gõ dòng lệnh "hút" kịch bản từ kho mã nguồn này về:

```powershell
irm https://raw.githubusercontent.com/duc1408/AI-Dubbing-PC-Procurement/main/04_NghiemThu_PhanCung/script_kiem_tra_linh_kien.ps1 | iex
```

Hệ thống sẽ ngay lập tức đối chiếu và xuất file biên bản bảo hành ra Desktop.

---
*Dự án này được tối ưu hóa kĩ thuật để đảm bảo máy móc hoạt động bền bỉ trong môi trường công nghiệp.*
