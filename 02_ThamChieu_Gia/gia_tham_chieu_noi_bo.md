# BẢNG GIÁ THAM CHIẾU NỘI BỘ [ĐÃ LỖI THỜI - DEPRECATED]

> [!WARNING]
> TÀI LIỆU NÀY ĐÃ BỊ KHAI TỬ (DEPRECATED)
> Bảng giá tĩnh (hardcoded) trong file này không còn chính xác do giá linh kiện máy tính biến động mỗi ngày.

**Cập nhật hệ thống (Phiên bản V5):**
Hệ thống báo giá của dự án hiện tại đã được **Tự Động Hóa 100%**. Kịch bản Python `cong_cu_cao_gia_tu_dong.py` sẽ tự động:
1. Đọc danh sách linh kiện cần cào từ file `danh_sach_linh_kien.json`.
2. Truy cập 6 siêu thị PC lớn nhất Việt Nam để tìm giá Sàn.
3. Tự động tính toán cộng dồn "Dự toán PC" theo từng Cấu hình (Tối thiểu, Tiêu chuẩn, Ép ngân sách).

## 📂 Xem Báo Giá Mới Nhất Ở Đâu?
Toàn bộ Báo cáo giá linh kiện lẻ và Dự toán tổng thể PC sẽ được hệ thống sinh tự động và lưu vào thư mục:
`02_ThamChieu_Gia/data/`

Hãy mở thư mục đó và tìm các file có tiền tố `gia_tham_chieu_tong_the_[Ngày_Giờ].md` để có con số chính xác nhất cho ngày hôm nay!
