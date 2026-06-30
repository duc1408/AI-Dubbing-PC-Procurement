import re
import urllib.parse
from playwright.sync_api import sync_playwright
import statistics
import datetime
import os
import json

# Hàm tải danh sách linh kiện từ file JSON
def load_config():
    config_path = "danh_sach_linh_kien.json"
    if not os.path.exists(config_path):
        print(f"Không tìm thấy file cấu hình {config_path}")
        return [], {}
    with open(config_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    queries = []
    price_ranges = {}
    for item in data.get("linh_kien", []):
        queries.append(item["tu_khoa"])
        price_ranges[item["tu_khoa"]] = (item["gia_min"], item["gia_max"])
    return queries, price_ranges

def get_expected_range(query, price_ranges):
    for key, (min_p, max_p) in price_ranges.items():
        if key.lower() in query.lower():
            return min_p, max_p
    return 1_000_000, 200_000_000 # Mặc định

def extract_prices_from_text(text, query, price_ranges):
    min_p, max_p = get_expected_range(query, price_ranges)
    pattern = r'((?:\d{1,3}[.,])+\d{3})\s*(?:đ|d|₫|vnđ|vnd)'
    matches = re.findall(pattern, text.lower())
    prices = []
    
    for match in matches:
        clean_num = match.replace('.', '').replace(',', '')
        try:
            val = int(clean_num)
            if min_p <= val <= max_p:
                prices.append(val)
        except ValueError:
            pass
    return prices

def scrape_site(page, url_template, query, site_name, price_ranges):
    url = url_template.format(urllib.parse.quote_plus(query))
    print(f"▶ Đang truy cập {site_name}...")
    results = []
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=20000)
        
        for _ in range(2):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
            page.wait_for_timeout(1000)
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1000)
        
        body_text = page.inner_text("body")
        found_prices = extract_prices_from_text(body_text, query, price_ranges)
        
        unique_prices = sorted(list(set(found_prices)))
        
        if unique_prices:
            print(f"  => Đã tìm thấy {len(unique_prices)} mức giá CHUẨN trên trang:")
            for p in unique_prices[:3]:
                print(f"     - {p:,.0f} VNĐ".replace(',', '.'))
            results = [{"price": p, "site": site_name, "url": url} for p in unique_prices]
        else:
            print("  => Không tìm thấy mức giá hợp lệ trong biên độ quy định (Hoặc bị Captcha).")
            
    except Exception as e:
        print(f"  => Lỗi truy cập: {e}")
        
    return results

def calculate_build_estimates(scraped_data, timestamp_str):
    # Chi phí cố định ước tính
    FIXED_MIN = 11_500_000 # Tối thiểu: Main B, RAM 64GB, Nguồn 750W, Vỏ, Tản khí
    FIXED_BUDGET = 8_500_000 # Ép ngân sách: Main B, RAM 64GB, Nguồn Bronze, Vỏ rẻ, Tản rẻ
    FIXED_STD = 25_000_000 # Tiêu chuẩn: Main Z, RAM 128GB, Nguồn 1200W, Vỏ to, Tản AIO
    
    # Lấy giá trị rẻ nhất của từng linh kiện để tính toán (fallback về 0 nếu k cào đc)
    p_5060ti = scraped_data.get("rtx 5060 ti 16gb", 15000000)
    p_4090 = scraped_data.get("rtx 4090", 50000000)
    p_i5_13400f = scraped_data.get("core i5 13400f", 3500000)
    p_i5_13600k = scraped_data.get("core i5 13600k", 7000000)
    p_i7_14700k = scraped_data.get("core i7 14700k", 10000000)
    p_ssd_1tb = scraped_data.get("samsung 990 pro 1tb", 2500000)
    
    cost_min = p_5060ti + p_i5_13600k + p_ssd_1tb + FIXED_MIN
    cost_budget = p_5060ti + p_i5_13400f + p_ssd_1tb + FIXED_BUDGET
    cost_std = p_4090 + p_i7_14700k + (p_ssd_1tb * 3) + FIXED_STD
    
    lines = [
        "# DỰ TOÁN CẤU HÌNH PC AI DUBBING (TỰ ĐỘNG)",
        f"*Cập nhật tự động lúc: {timestamp_str} (Dựa trên giá thị trường realtime)*\n",
        "Tài liệu này thay thế cho bảng giá nội bộ cũ. Tổng giá trị được cộng dồn từ mức giá rẻ nhất quét được trên mạng cộng với một khoản ước tính chi phí cố định (RAM, Nguồn, Main, Vỏ, Tản nhiệt).\n",
        "## 1. CẤU HÌNH TỐI THIỂU (MỨC CƠ BẢN)",
        f"- **GPU:** RTX 5060 Ti 16GB ({p_5060ti:,.0f} đ)",
        f"- **CPU:** Core i5 13600K ({p_i5_13600k:,.0f} đ)",
        f"- **SSD:** 1x 1TB ({p_ssd_1tb:,.0f} đ)",
        f"- **Khác (Main/RAM/PSU...):** ~ {FIXED_MIN:,.0f} đ",
        f"- **=> TỔNG DỰ TOÁN:** **{cost_min:,.0f} VNĐ**\n".replace(',', '.'),
        
        "## 2. CẤU HÌNH TIÊU CHUẨN (HIỆU NĂNG CAO)",
        f"- **GPU:** RTX 4090 ({p_4090:,.0f} đ)",
        f"- **CPU:** Core i7 14700K ({p_i7_14700k:,.0f} đ)",
        f"- **SSD:** 3x 1TB ({(p_ssd_1tb * 3):,.0f} đ)",
        f"- **Khác (Main/RAM/PSU...):** ~ {FIXED_STD:,.0f} đ",
        f"- **=> TỔNG DỰ TOÁN:** **{cost_std:,.0f} VNĐ**\n".replace(',', '.'),
        
        "## 3. CẤU HÌNH ÉP NGÂN SÁCH (MAX TIẾT KIỆM)",
        f"- **GPU:** RTX 5060 Ti 16GB ({p_5060ti:,.0f} đ)",
        f"- **CPU:** Core i5 13400F ({p_i5_13400f:,.0f} đ)",
        f"- **SSD:** 1x 1TB ({p_ssd_1tb:,.0f} đ)",
        f"- **Khác (Main/RAM/PSU...):** ~ {FIXED_BUDGET:,.0f} đ",
        f"- **=> TỔNG DỰ TOÁN:** **{cost_budget:,.0f} VNĐ**\n".replace(',', '.')
    ]
    return "\n".join(lines).replace(',', '.')

def main():
    queries, price_ranges = load_config()
    if not queries:
        return
        
    sites = [
        {"name": "Nguyễn Công PC", "url": "https://nguyencongpc.vn/tim-kiem?q={}"},
        {"name": "An Phát PC", "url": "https://www.anphatpc.com.vn/tim?q={}"},
        {"name": "HACOM", "url": "https://hacom.vn/tim?q={}"},
        {"name": "GearVN", "url": "https://gearvn.com/search?type=product&q={}"},
        {"name": "KCCShop", "url": "https://kccshop.vn/tim-kiem?q={}"},
        {"name": "Hoàng Hà PC", "url": "https://hoanghapc.vn/tim?q={}"}
    ]
    
    print("="*70)
    print("🚀 HỆ THỐNG CÀO GIÁ VÀ TÍNH DỰ TOÁN V5 (SMART I/O)")
    print("="*70 + "\n")
    
    timestamp_str = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    file_suffix = datetime.datetime.now().strftime('%d_%m_%Y_%Hh%Mm')
    
    report_lines = []
    report_lines.append("# BÁO CÁO CÀO GIÁ LINH KIỆN PC TỰ ĐỘNG")
    report_lines.append(f"*Cập nhật tự động lúc: {timestamp_str}*\n")
    
    summary_table = [
        "## 📊 BẢNG TỔNG HỢP GIÁ",
        "| Linh kiện | Giá Sàn (Rẻ nhất) | Giá Phổ Biến | Cửa hàng rẻ nhất |",
        "| :--- | :--- | :--- | :--- |"
    ]
    
    scraped_lowest_prices = {}
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={"width": 1920, "height": 1080}
        )
        page = context.new_page()
        
        for q in queries:
            print(f"🔍 TÌM KIẾM LINH KIỆN: [{q.upper()}]")
            print("-" * 50)
            all_valid_prices = []
            
            for s in sites:
                prices = scrape_site(page, s['url'], q, s['name'], price_ranges)
                all_valid_prices.extend(prices)
                
            if all_valid_prices:
                raw_prices = [item["price"] for item in all_valid_prices]
                med = statistics.median(raw_prices)
                
                min_obj = min(all_valid_prices, key=lambda x: x["price"])
                min_p = min_obj["price"]
                min_site = min_obj["site"]
                min_url = min_obj["url"]
                
                # Lưu lại giá sàn để tính tổng dự toán PC
                scraped_lowest_prices[q.lower()] = min_p
                
                print(f"✅ THỐNG KÊ TOÀN THỊ TRƯỜNG CHO [{q.upper()}]:")
                print(f"   + Giá Sàn Rẻ Nhất: {min_p:,.0f} VNĐ (Tại {min_site})".replace(',', '.'))
                print(f"   + Giá Bán Phổ Biến (Trung Vị): {med:,.0f} VNĐ".replace(',', '.'))
                
                report_lines.append(f"## {q.upper()}")
                report_lines.append(f"- **Giá Sàn (Rẻ nhất):** {min_p:,.0f} VNĐ".replace(',', '.'))
                report_lines.append(f"  - *Nguồn để ép giá:* [{min_site}]({min_url})")
                report_lines.append(f"- **Giá Phổ Biến (Trung vị):** {med:,.0f} VNĐ".replace(',', '.'))
                report_lines.append("")
                
                summary_table.append(f"| **{q.upper()}** | {min_p:,.0f} đ | {med:,.0f} đ | [{min_site}]({min_url}) |".replace(',', '.'))
            else:
                report_lines.append(f"## {q.upper()}")
                report_lines.append(f"- Không thu thập được mức giá chuẩn (Có thể do thị trường hết hàng).")
                report_lines.append("")

            print("="*70 + "\n")
            
        browser.close()
        
    os.makedirs("data", exist_ok=True)
    
    # 1. Xuất file Báo cáo cào giá (Output 1)
    final_report = report_lines[:2] + summary_table + ["\n---\n"] + report_lines[2:]
    file1 = f"data/ket_qua_cao_gia_{file_suffix}.md"
    with open(file1, "w", encoding="utf-8") as f:
        f.write("\n".join(final_report))
        
    # 2. Xuất file Dự toán PC tổng thể (Output 2)
    file2 = f"data/gia_tham_chieu_tong_the_{file_suffix}.md"
    estimate_content = calculate_build_estimates(scraped_lowest_prices, timestamp_str)
    with open(file2, "w", encoding="utf-8") as f:
        f.write(estimate_content)
        
    print(f"\n=> [HOÀN TẤT] Đã xuất 2 file báo cáo vào thư mục data:")
    print(f"   1. {file1}")
    print(f"   2. {file2}")

if __name__ == "__main__":
    main()
