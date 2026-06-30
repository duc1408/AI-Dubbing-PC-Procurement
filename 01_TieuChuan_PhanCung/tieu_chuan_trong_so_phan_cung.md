# Bảng Trọng Số Ưu Tiên Cấu Hình PC - AI Video Dubbing (24/7)

Dựa trên việc bóc tách chi tiết toàn bộ các linh kiện cấu thành nên một thùng máy (Case) và triết lý **"Ưu tiên VRAM và Sự ổn định tuyệt đối"** trong quá trình vận hành liên tục qua đêm, dưới đây là bảng đánh giá trọng số đầu tư cho hệ thống PC làm Video Dubbing tự động.

Bảng được rà soát và sắp xếp theo mức độ ưu tiên ngân sách từ **CAO XUỐNG THẤP**.

---

## Tổng Quan Bảng Phân Bổ Trọng Số (Tổng 100%)

| Mức Độ Ưu Tiên | Tham Số Cấu Hình | Trọng Số | Lý Do Quan Trọng Nhất |
| :---: | :--- | :---: | :--- |
| 1 | **GPU (Card Đồ Họa / VRAM)** | **45%** | Tham số sinh tử của AI. VRAM quyết định việc có load được model hay không. |
| 2 | **Nguồn (PSU)** | **12%** | "Trái tim bơm máu". Treo máy 24/7 đòi hỏi nguồn cực tốt để không sập khi Card vọt công suất. |
| 3 | **RAM (Bộ nhớ hệ thống)** | **10%** | Vùng đệm sống còn khi VRAM đầy. Phải có dung lượng lớn để tránh lỗi văng phần mềm. |
| 4 | **Storage (Ổ cứng NVMe)** | **10%** | Chịu trách nhiệm ghi/xóa dữ liệu rác cường độ rất cao. Yêu cầu độ bền TBW lớn. |
| 5 | **Tản nhiệt (CPU & Quạt vỏ máy)** | **8%** | Ngăn hiện tượng quá nhiệt (Thermal Throttling) làm giảm tốc độ render. |
| 6 | **CPU (Vi xử lý)** | **8%** | Gần như không dùng để tính toán AI (đã nhường cho GPU). Chỉ dùng điều phối dữ liệu. |
| 7 | **Motherboard (Bo mạch chủ)** | **5%** | Nền móng kết nối. Yêu cầu VRM tản nhiệt tốt để cấp điện ổn định. |
| 8 | **Vỏ Case (Chassis)** | **2%** | Không cần kính cường lực hay LED RGB, chỉ cần mặt lưới (Mesh) thông thoáng khí. |

---

## Phân Tích Chi Tiết & Khuyến Nghị Từng Hạng Mục

### 1. GPU (Card Đồ Họa) - Trọng số: 45% (TỐI QUAN TRỌNG)
**Giải thích:** Linh hồn của hệ thống AI. **VRAM là Vua**. Mua card có VRAM càng lớn càng tốt để nhét vừa model. Bắt buộc dùng NVIDIA vì tương thích chuẩn CUDA.
*   **Tối thiểu:** 1x NVIDIA RTX 5060 Ti **16GB** (Vua hiệu năng/giá thành thế hệ mới, ưu tiên số 1) hoặc RTX 4060 Ti **16GB** nếu tiết kiệm (Tuyệt đối chống chỉ định các bản 8GB).
*   **Tiêu chuẩn:** 1x NVIDIA RTX 4090 **24GB** (Có thể tối ưu chi phí bằng RTX 3090 24GB cũ).
*   **Cao cấp:** **2x** NVIDIA RTX 4090 24GB (Tổng 48GB VRAM) hoặc RTX 6000 Ada (48GB VRAM chuyên nghiệp). Cấu hình này biến máy tính thành một xưởng cày thuê khổng lồ.

### 2. Nguồn (PSU) - Trọng số: 12%
**Giải thích:** Máy AI sẽ duy trì công suất tối đa liên tục, và đôi khi vọt công suất trong vài mili-giây (Peak Power). Nguồn yếu sẽ gây sập (Restart máy). Nên chọn nguồn dư 20-30% công suất thực tế hệ thống yêu cầu.
*   **Tối thiểu:** Nguồn 750W chuẩn 80 Plus Gold ATX 3.0 (Corsair, Seasonic).
*   **Tiêu chuẩn:** Nguồn 1000W - 1200W chuẩn 80 Plus Platinum.
*   **Cao cấp:** Nguồn 1600W chuẩn 80 Plus Titanium (VD: Corsair AX1600i).

### 3. RAM (Bộ nhớ hệ thống) - Trọng số: 10%
**Giải thích:** Phao cứu sinh chống lỗi `Out-Of-Memory`. Ưu tiên dung lượng khổng lồ. Tuyệt đối không bật XMP (Ép xung RAM lên bus quá cao) khi chạy AI 24/7 vì rất dễ gây lỗi màn hình xanh (BSOD) vào ban đêm.
*   **Tối thiểu:** 64GB DDR5 (2x32GB).
*   **Tiêu chuẩn:** 128GB DDR5 (4x32GB).
*   **Cao cấp:** 192GB hoặc 256GB DDR5.

### 4. Storage (Ổ cứng NVMe SSD) - Trọng số: 10%
**Giải thích:** Các mô hình tách/ghép nhạc (UVR/FFMPEG) cày nát ổ cứng bằng file nháp mỗi phút. Bắt buộc để ý chỉ số TBW (Độ bền ghi/xoá).
*   **Tối thiểu:** 1TB NVMe Gen 4 (TBW > 1000 như Samsung 990 Pro).
*   **Tiêu chuẩn:** Tách 2 ổ: 1TB NVMe Gen 4 (Hệ điều hành) + 2TB NVMe Gen 4 (Làm Workspace/Cache xóa file rác).
*   **Cao cấp:** 2TB NVMe (OS) + 4TB NVMe (Workspace chạy Raid 0 tốc độ siêu cao) + 16-22TB HDD Enterprise (Lưu file thành phẩm).

### 5. Tản nhiệt (Khí / Nước & Quạt gió) - Trọng số: 8%
**Giải thích:** Máy tính ngắt hoặc chạy chậm khi nóng là cơ chế tự bảo vệ. Ở tải AI 100%, máy sinh nhiệt như lò sưởi. Tản nhiệt ở đây không chỉ là tản cho CPU, mà bao gồm cả dàn Quạt hút/đẩy của Vỏ case để đẩy khí nóng ra ngoài nhanh nhất.
*   **Tối thiểu:** Tản nhiệt khí tháp đôi loại xịn (Noctua NH-D15, Thermalright FC140) + Gắn đủ 3 quạt trước hút vào, 1 quạt sau đẩy ra.
*   **Tiêu chuẩn:** Tản nhiệt nước AIO 360mm uy tín (Corsair, Deepcool) + Lắp tối đa số quạt thông gió vỏ case cho phép.
*   **Cao cấp:** Hệ thống tản nhiệt Custom Water Cooling (Cho khối CPU và 2 GPU) hoặc tản nhiệt cấp độ server với quạt công nghiệp (Noctua industrialPPC 3000rpm).

### 6. CPU (Vi xử lý) - Trọng số: 8%
**Giải thích:** AI xử lý ảnh, giọng nói, văn bản 90% bằng tập lệnh CUDA trên GPU NVIDIA. CPU chỉ dùng gộp file FFMPEG và chạy script điều phối. Đừng dồn tiền vào đây.
*   **Tối thiểu:** Intel Core i5-13600K hoặc AMD Ryzen 5 7600X.
*   **Tiêu chuẩn:** Intel Core i7-14700K hoặc AMD Ryzen 9 7900X (Hỗ trợ mở nhiều luồng Python hơn).
*   **Cao cấp:** AMD Ryzen Threadripper PRO (VD: 7960WX). Chọn CPU này không phải vì nó tính toán nhanh, mà vì nó cung cấp rất nhiều làn PCIe để nuôi dàn 2-4 chiếc GPU Full băng thông.

### 7. Motherboard (Bo mạch chủ) - Trọng số: 5%
**Giải thích:** Quyết định độ bền mạch điện (dàn Phase VRM). Nguồn cấp có tốt đến mấy mà Mainboard tản nhiệt VRM kém thì bo mạch vẫn sẽ cháy.
*   **Tối thiểu:** B760 (Intel) hoặc B650 (AMD). Mua bản có lá nhôm tản nhiệt linh kiện to bản (như dòng Mortar, TUF).
*   **Tiêu chuẩn:** Z790 (Intel) hoặc X670 (AMD). Đảm bảo cổng kết nối M.2 cho 2 ổ cứng chuẩn Gen 4.
*   **Cao cấp:** Dòng Workstation (W790 hoặc TRX50). Mấu chốt là khoảng cách các khe PCIe X16 phải rất xa nhau để cắm 2-4 Card 4090 mà không bị ốp sát vào nhau (gây ngạt khí).

### 8. Vỏ Case (Chassis) - Trọng số: 2%
**Giải thích:** Trong môi trường xưởng AI/farm, vẻ đẹp của kính cường lực và LED RGB là vô nghĩa và tốn kém. Case chỉ cần đảm bảo 2 yếu tố: Mặt trước đục lỗ lưới (Mesh) hút được nhiều gió, và khung thép cứng cáp để đỡ sức nặng của các dòng Card đồ họa cực lớn.
*   **Tối thiểu:** Case Mid-Tower mặt lưới, không cần kính cường lực. Có kèm sẵn lưới lọc bụi (treo máy 24/7 hút rất nhiều bụi).
*   **Tiêu chuẩn:** Case Mid-Tower / Full-Tower không gian đi dây (cable management) thật rộng. Cần có thêm khung/giá đỡ GPU (VGA Holder) để card không bị xệ gãy chân PCIe.
*   **Cao cấp:** Case Full-Tower siêu lớn (VD: Corsair 1000D), thép siêu cứng để chứa được 2 Card 4090 và dàn tản nhiệt nước Custom.
