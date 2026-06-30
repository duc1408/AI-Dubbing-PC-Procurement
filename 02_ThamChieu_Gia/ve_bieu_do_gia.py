import os
import re
import datetime
import matplotlib.pyplot as plt

def parse_price(price_str):
    clean = re.sub(r'[^\d]', '', price_str)
    return int(clean) if clean else None

def main():
    data_dir = "data"
    if not os.path.exists(data_dir):
        print("❌ Chưa có thư mục data. Hãy chạy công cụ cào giá trước!")
        return
        
    files = [f for f in os.listdir(data_dir) if f.startswith("ket_qua_cao_gia_") and f.endswith(".md")]
    if not files:
        print("❌ Chưa có dữ liệu báo cáo nào trong thư mục data.")
        return
        
    history = {}
    
    print(f"📊 Đang phân tích {len(files)} file báo cáo lịch sử...")
    
    # ket_qua_cao_gia_30_06_2026_09h13m.md
    for filename in files:
        match = re.search(r'ket_qua_cao_gia_(\d{2})_(\d{2})_(\d{4})_(\d{2})h(\d{2})m', filename)
        if match:
            d, m, y, h, mn = match.groups()
            dt = datetime.datetime(int(y), int(m), int(d), int(h), int(mn))
            
            filepath = os.path.join(data_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            # Trích xuất giá sàn của từng linh kiện
            sections = re.findall(r'##\s*(.*?)\n- \*\*Giá Sàn.*?:\*\*\s*([0-9.,]+)', content)
            for comp_name, price_str in sections:
                comp_name = comp_name.strip()
                price = parse_price(price_str)
                if price:
                    if comp_name not in history:
                        history[comp_name] = []
                    history[comp_name].append((dt, price))
                    
    if not history:
        print("❌ Không tìm thấy dữ liệu giá hợp lệ để vẽ biểu đồ.")
        return
        
    # Sắp xếp theo dòng thời gian
    for comp in history:
        history[comp].sort(key=lambda x: x[0])
        
    # Vẽ biểu đồ
    plt.figure(figsize=(14, 8))
    
    for comp, data_points in history.items():
        dates = [dp[0] for dp in data_points]
        # Quy đổi ra đơn vị Triệu VNĐ cho dễ nhìn
        prices = [dp[1] / 1_000_000 for dp in data_points] 
        
        plt.plot(dates, prices, marker='o', linestyle='-', linewidth=2, markersize=8, label=comp)
        
    plt.title("Biểu Đồ Biến Động Giá Sàn - Linh Kiện PC AI Dubbing", fontsize=18, fontweight='bold', pad=20)
    plt.xlabel("Thời gian khảo sát", fontsize=12, fontweight='bold')
    plt.ylabel("Giá Sàn Rẻ Nhất (Triệu VNĐ)", fontsize=12, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Format trục X
    plt.gcf().autofmt_xdate()
    
    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
    plt.tight_layout()
    
    out_path = os.path.join(data_dir, "bieu_do_gia.png")
    plt.savefig(out_path, dpi=300)
    print(f"✅ Đã vẽ xong biểu đồ xu hướng giá!")
    print(f"   => Hình ảnh được lưu tại: {out_path}")
    
if __name__ == "__main__":
    main()
