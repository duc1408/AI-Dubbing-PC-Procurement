# ✅ CHECKLIST NHANH — MUA PC AI DUBBING (Dành cho người không rành kỹ thuật)

> **Cầm file này theo điện thoại khi đi cửa hàng. 4 bước, không cần hiểu kỹ thuật.**

---

## 📅 BƯỚC 1 — TRƯỚC KHI ĐI (Làm ở nhà, ~10 phút)

- [ ] Mở thư mục `02_ThamChieu_Gia/` → click đúp vào file **`CHAY_NGAY.bat`**
- [ ] Chọn tùy chọn **[3] Cào giá + Vẽ biểu đồ**. Chờ chương trình chạy xong (~5-10 phút)
- [ ] Mở file mới nhất trong thư mục `02_ThamChieu_Gia/data/` tên `gia_tham_chieu_tong_the_...md`
- [ ] **Ghi lại (hoặc chụp màn hình)** 2 con số dự toán:
  - Cấu hình Tối thiểu (Phiên bản 1 - 16GB): ~___ triệu
  - Cấu hình Tối thiểu (Phiên bản 2 - 24GB): ~___ triệu

> 💡 **Đây là vũ khí đàm phán của bạn.** Cửa hàng sẽ không thể hét giá cao hơn con số này.

---

## 🏪 BƯỚC 2 — XIN BÁO GIÁ VÀ THẨM ĐỊNH (Cực kỳ quan trọng)

Thay vì mang tiền ra ngay cửa hàng, hãy gửi file **Yêu cầu Báo Giá** (thư mục `03_BaoGia_CuaHang`) cho Sale qua Zalo/Facebook trước. Khi nhận được ảnh báo giá từ họ:

- [ ] **BẮT BUỘC:** Đọc hướng dẫn trong file `04_ThamDinh_BaoGia/huong_dan_tham_dinh.md` để tự kiểm tra hoặc nhờ AI soi hộ các "cờ đỏ" (nhét đồ cũ, cắt xén RAM, hạ SSD).
- [ ] So sánh Tổng giá trị báo giá với con số Dự toán ở BƯỚC 1.
- [ ] Chỉ đi đến cửa hàng khi tờ Báo Giá đã **PASS (Đạt)** tất cả các tiêu chí.

---

## 🏪 BƯỚC 3 — Ở CỬA HÀNG (Lấy máy và chốt đơn)

### Câu hỏi bắt buộc cuối cùng:
1. **"Card đồ họa bản này có đúng 16GB (hoặc 24GB) VRAM không? Cho tôi xem thùng hộp."**
   - ⛔ Nếu Sale nói "8GB vẫn tốt" → **Từ chối ngay.**
2. **"Nguồn điện này có phải hãng Tier A chuẩn Gold không?"**
3. **"Phí lắp ráp có miễn phí không?"**

### 🚩 Dấu hiệu "đỏ" phút chót:
- Sale báo "Hết hàng" và dụ đổi sang đồ khác kém hơn báo giá đã chốt → **Từ chối**
- Sale không cho tự tay rạch Seal GPU/CPU → **Từ chối**

---

## 🖥️ BƯỚC 4 — NGHIỆM THU PHẦN CỨNG (Chưa thanh toán)

### 4A. Yêu cầu bắt buộc trước khi test:
- [ ] Yêu cầu **chưa đóng nắp hông case** — nhìn vào bên trong kiểm tra sơ bộ
- [ ] Tự tay **rạch seal (niêm phong)** thùng hộp Card đồ họa và CPU — không để thợ làm hộ
- [ ] Nhìn tên hãng và watt trên **tem nhãn nguồn điện** bằng đèn pin điện thoại

### 4B. Chạy script kiểm tra tự động:
Cắm internet cho máy mới → mở PowerShell (phím Windows → gõ "PowerShell") → copy dán lệnh sau:

```powershell
irm https://raw.githubusercontent.com/duc1408/AI-Dubbing-PC-Procurement/main/05_NghiemThu_PhanCung/script_kiem_tra_linh_kien.ps1 | iex
```

Chờ script chạy xong → file **`BienBan_NghiemThu_AI_Dubbing.txt`** sẽ xuất hiện trên Desktop.

### 4C. Đọc kết quả (đơn giản):
Mở file biên bản, tìm các dòng màu ĐỎ bắt đầu bằng `=> CANH BAO`:

| Nếu thấy cảnh báo về... | Ý nghĩa | Làm gì |
|------------------------|---------|--------|
| VRAM Card đồ họa thấp hơn đặt hàng | Bị tráo Card kém hơn | ⛔ Từ chối nhận máy |
| RAM chỉ 1 thanh (Single Channel) | Hiệu năng giảm, không đúng hợp đồng | ⛔ Yêu cầu lắp đủ 2 thanh |
| Windows cài > 30 ngày trước | Có thể là ổ cứng cũ | ⛔ Yêu cầu giải thích hoặc từ chối |
| RAM bus > 5600MHz (XMP bật) | Dễ bị màn hình xanh khi chạy 24/7 | ⚠️ Yêu cầu tắt XMP trong BIOS |
| CPU sai mã | Bị tráo CPU cũ hơn | ⛔ Từ chối nhận máy |

### 4D. Test vật lý bắt buộc (nhờ kỹ thuật viên cửa hàng làm):
- [ ] Chạy **FurMark** hoặc **OCCT** (stress test card đồ họa) **15 phút**
  - ✅ PASS: Máy không sập nguồn, màn hình không rác/nhấp nháy
  - ⛔ FAIL: Máy tắt đột ngột = **nguồn yếu hoặc card lỗi**

---

## 💳 BƯỚC 5 — THANH TOÁN (Chỉ sau khi mọi thứ PASS)

- [ ] File biên bản không có dòng CANH BAO màu đỏ nào về CPU/RAM/GPU
- [ ] Test FurMark 15 phút: máy không sập
- [ ] Nhận **biên bản bảo hành có chữ ký và đóng dấu** của cửa hàng
- [ ] ✅ **Lúc này mới thanh toán**

---

## 📞 Nếu cần tư vấn thêm
Tham chiếu chi tiết kỹ thuật: xem thư mục `01_TieuChuan_PhanCung/`
Mẫu báo giá gửi cửa hàng: xem thư mục `03_BaoGia_CuaHang/`
