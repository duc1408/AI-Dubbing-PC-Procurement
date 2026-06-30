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
    
    fixed_costs = data.get("chi_phi_co_dinh", {
        "option1_16gb": 11500000,
        "option2_24gb": 15500000
    })
    return queries, price_ranges, fixed_costs

def get_expected_range(query, price_ranges):
    for key, (min_p, max_p) in price_ranges.items():
        if key.lower() in query.lower():
            return min_p, max_p
    return 1_000_000, 200_000_000 # Mặc định

def extract_prices_from_elements(elements, query, price_ranges):
    min_p, max_p = get_expected_range(query, price_ranges)
    prices = []
    
    for el in elements:
        text = el.inner_text().strip()
        # Loại bỏ các ký tự không phải số
        clean_num = re.sub(r'[^\d]', '', text)
        if clean_num:
            try:
                val = int(clean_num)
                # Đảm bảo giá trị nằm trong biên độ kỳ vọng
                if min_p <= val <= max_p:
                    prices.append(val)
            except ValueError:
                pass
    return prices

def scrape_site(page, site_config, query, price_ranges):
    url_template = site_config['url']
    site_name = site_config['name']
    selectors = site_config.get('selectors', ['.price', '.product-price', '.current-price', '.special-price', 'span.price'])

    url = url_template.format(urllib.parse.quote_plus(query))
    print(f"▶ Đang truy cập {site_name}...")
    results = []
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=20000)
        
        # Cuộn trang để tải lazy loading
        for _ in range(2):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
            page.wait_for_timeout(1000)
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1000)
        
        # Thử từng CSS selector để tìm giá
        found_prices = []
        for selector in selectors:
            elements = page.query_selector_all(selector)
            if elements:
                extracted = extract_prices_from_elements(elements, query, price_ranges)
                if extracted:
                    found_prices.extend(extracted)
                    break # Nếu đã tìm thấy bằng selector này thì dừng
        
        # Fallback: Nếu không tìm thấy bằng selector, thử regex trên toàn bộ body
        if not found_prices:
            body_text = page.inner_text("body")
            pattern = r'((?:\d{1,3}[.,])+\d{3})' # Mở rộng pattern, không bắt buộc phải có đ/vnd ngay sát
            matches = re.findall(pattern, body_text)
            for match in matches:
                clean_num = match.replace('.', '').replace(',', '')
                try:
                    val = int(clean_num)
                    min_p, max_p = get_expected_range(query, price_ranges)
                    if min_p <= val <= max_p:
                        found_prices.append(val)
                except ValueError:
                    pass

        unique_prices = sorted(list(set(found_prices)))
        
        if unique_prices:
            print(f"  => Đã tìm thấy {len(unique_prices)} mức giá CHUẨN trên trang:")
            for p in unique_prices[:3]:
                print(f"     - {p:,.0f} VNĐ".replace(',', '.'))
            results = [{"price": p, "site": site_name, "url": url} for p in unique_prices]
        else:
            print("  => Không tìm thấy mức giá hợp lệ trong biên độ quy định (Hoặc bị Captcha/Hết hàng).")
            
    except Exception as e:
        print(f"  => Lỗi truy cập: {e}")
        
    return results

def calculate_budget_allocation(total_budget):
    weights = {
        "1. GPU (Card Đồ Họa)": 0.45,
        "2. Nguồn (PSU)": 0.12,
        "3. RAM (Bộ nhớ)": 0.10,
        "4. Storage (Ổ cứng NVMe)": 0.10,
        "5. CPU (Vi xử lý)": 0.08,
        "6. Tản nhiệt & Quạt Case": 0.08,
        "7. Motherboard (Mainboard)": 0.05,
        "8. Vỏ Case (Chassis)": 0.02
    }
    lines = ["## 4. BẢNG PHÂN BỔ NGÂN SÁCH CHI TIẾT (Theo % Tiêu Chuẩn)"]
    lines.append(f"*(Dành cho ngân sách tổng {total_budget:,.0f} VNĐ)*\n".replace(',', '.'))
    for component, weight in weights.items():
        allocated = total_budget * weight
        lines.append(f"- **{component}** ({weight*100:02.0f}%): ~ {allocated:,.0f} đ".replace(',', '.'))
    return lines

def calculate_build_estimates(scraped_data, timestamp_str, fixed_costs):
    # Chi phí cố định ước tính
    FIXED_OPT1 = fixed_costs.get("option1_16gb", 11500000) # Option 1 (16GB): Main B, RAM 64GB, Nguồn 750W, Vỏ Mid, Tản khí
    FIXED_OPT2 = fixed_costs.get("option2_24gb", 15500000) # Option 2 (24GB): Main Z/B Xịn, RAM 64GB, Nguồn 1000W, Vỏ to, Tản xịn
    
    # Lấy giá trị rẻ nhất của từng linh kiện để tính toán
    p_5060ti = scraped_data.get("rtx 5060 ti 16gb", 15000000)
    p_3090 = scraped_data.get("rtx 3090 24gb", 18000000)
    p_i5_13600k = scraped_data.get("core i5 13600k", 7000000)
    p_ssd_1tb = scraped_data.get("samsung 990 pro 1tb", 2500000)
    
    cost_opt1 = p_5060ti + p_i5_13600k + p_ssd_1tb + FIXED_OPT1
    cost_opt2 = p_3090 + p_i5_13600k + p_ssd_1tb + FIXED_OPT2
    
    # Thêm 10% dự phòng rủi ro/UPS
    cost_opt1_safe = cost_opt1 * 1.1
    cost_opt2_safe = cost_opt2 * 1.1
    
    lines = [
        "# DỰ TOÁN CẤU HÌNH PC AI DUBBING (TỰ ĐỘNG)",
        f"*Cập nhật tự động lúc: {timestamp_str} (Dựa trên giá thị trường realtime)*\n",
        "> [!IMPORTANT]",
        "> Tổng giá trị được cộng dồn từ mức giá rẻ nhất quét được trên mạng cộng với khoản chi phí cố định ước tính.",
        "> **Bắt buộc chuẩn bị thêm 10% Ngân sách dự phòng** cho: Phí vận chuyển, Lắp ráp, Cáp kết nối và UPS (Bộ lưu điện).\n",
        
        "## 1. CẤU HÌNH TỐI THIỂU - PHIÊN BẢN 1 (VGA 16GB THẾ HỆ 5)",
        f"- **GPU:** RTX 5060 Ti 16GB ({p_5060ti:,.0f} đ)",
        f"- **CPU:** Core i5 13600K ({p_i5_13600k:,.0f} đ)",
        f"- **SSD:** 1x 1TB Samsung 990 Pro ({p_ssd_1tb:,.0f} đ)",
        f"- **Khác (Main/RAM/Nguồn 750W...):** ~ {FIXED_OPT1:,.0f} đ",
        f"- **=> TỔNG DỰ TOÁN:** **{cost_opt1:,.0f} VNĐ** (An toàn: {cost_opt1_safe:,.0f} VNĐ)\n".replace(',', '.'),
        
        "## 2. CẤU HÌNH TỐI THIỂU - PHIÊN BẢN 2 (VGA 24GB THẾ HỆ 3 CŨ)",
        f"- **GPU:** RTX 3090 24GB Cũ ({p_3090:,.0f} đ)",
        f"- **CPU:** Core i5 13600K ({p_i5_13600k:,.0f} đ)",
        f"- **SSD:** 1x 1TB Samsung 990 Pro ({p_ssd_1tb:,.0f} đ)",
        f"- **Khác (Main/RAM/Nguồn 1000W...):** ~ {FIXED_OPT2:,.0f} đ",
        f"- **=> TỔNG DỰ TOÁN:** **{cost_opt2:,.0f} VNĐ** (An toàn: {cost_opt2_safe:,.0f} VNĐ)\n".replace(',', '.')
    ]
    
    # Tính bảng phân bổ cho cấu hình Option 1 (làm mẫu chuẩn)
    budget_lines = calculate_budget_allocation(cost_opt1)
    lines.extend(budget_lines)
    
    return "\n".join(lines).replace(',', '.')

def main():
    import sys
    if sys.stdout.encoding.lower() != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            pass

    queries, price_ranges, fixed_costs = load_config()
    if not queries:
        return
        
    sites = [
        {"name": "Nguyễn Công PC", "url": "https://nguyencongpc.vn/tim-kiem?q={}", "selectors": ['.product-price', '.price-now', '.price']},
        {"name": "An Phát PC", "url": "https://www.anphatpc.com.vn/tim?q={}", "selectors": ['.p-price', '.price']},
        {"name": "HACOM", "url": "https://hacom.vn/tim?q={}", "selectors": ['.p-price', '.price']},
        {"name": "GearVN", "url": "https://gearvn.com/search?type=product&q={}", "selectors": ['.product-price', '.price']},
        {"name": "KCCShop", "url": "https://kccshop.vn/tim-kiem?q={}", "selectors": ['.price-now', '.p-price', '.price']},
        {"name": "Hoàng Hà PC", "url": "https://hoanghapc.vn/tim?q={}", "selectors": ['.p-price', '.price']}
    ]
    
    print("="*70)
    print("🚀 HỆ THỐNG CÀO GIÁ VÀ TÍNH DỰ TOÁN V6 (CSS SELECTOR + REGEX FALLBACK)")
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
                prices = scrape_site(page, s, q, price_ranges)
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
    estimate_content = calculate_build_estimates(scraped_lowest_prices, timestamp_str, fixed_costs)
    with open(file2, "w", encoding="utf-8") as f:
        f.write(estimate_content)
        
    print(f"\n=> [HOÀN TẤT] Đã xuất 2 file báo cáo vào thư mục data:")
    print(f"   1. {file1}")
    print(f"   2. {file2}")

if __name__ == "__main__":
    main()
