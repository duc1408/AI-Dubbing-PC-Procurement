import re
import urllib.parse
from playwright.sync_api import sync_playwright
import statistics
import datetime
# Bộ lọc giá thông minh (Dynamic Price Filtering)
# Dùng để loại bỏ các phụ kiện rẻ tiền hoặc những bộ PC ráp sẵn giá chát chúa
PRICE_RANGES = {
    "rtx 4060 ti 16gb": (10_000_000, 16_000_000),
    "rtx 4090": (45_000_000, 85_000_000),
    "core i5 13400f": (3_000_000, 5_500_000),
    "core i5 13600k": (6_500_000, 9_500_000),
    "core i7 14700k": (9_000_000, 13_000_000),
    "samsung 990 pro 1tb": (2_000_000, 4_000_000)
}

def get_expected_range(query):
    for key, (min_p, max_p) in PRICE_RANGES.items():
        if key in query.lower():
            return min_p, max_p
    return 1_000_000, 200_000_000 # Mặc định

def extract_prices_from_text(text, query):
    min_p, max_p = get_expected_range(query)
    pattern = r'((?:\d{1,3}[.,])+\d{3})\s*(?:đ|d|₫|vnđ|vnd)'
    matches = re.findall(pattern, text.lower())
    prices = []
    
    for match in matches:
        clean_num = match.replace('.', '').replace(',', '')
        try:
            val = int(clean_num)
            # Tối ưu kỹ thuật: Bộ lọc thông minh loại bỏ rác
            if min_p <= val <= max_p:
                prices.append(val)
        except ValueError:
            pass
    return prices

def scrape_site(page, url_template, query, site_name):
    url = url_template.format(urllib.parse.quote_plus(query))
    print(f"▶ Đang truy cập {site_name}...")
    results = []
    try:
        page.goto(url, wait_until="domcontentloaded", timeout=20000)
        
        # Cuộn nhiều lần để kích hoạt lazy load triệt để
        for _ in range(2):
            page.evaluate("window.scrollTo(0, document.body.scrollHeight / 2)")
            page.wait_for_timeout(1000)
            page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            page.wait_for_timeout(1000)
        
        body_text = page.inner_text("body")
        found_prices = extract_prices_from_text(body_text, query)
        
        # Lọc ra các mức giá duy nhất và hợp lý
        unique_prices = sorted(list(set(found_prices)))
        
        if unique_prices:
            print(f"  => Đã tìm thấy {len(unique_prices)} mức giá CHUẨN trên trang:")
            for p in unique_prices[:3]: # Hiển thị 3 mức giá rẻ nhất (giá sàn)
                print(f"     - {p:,.0f} VNĐ".replace(',', '.'))
            results = [{"price": p, "site": site_name, "url": url} for p in unique_prices]
        else:
            print("  => Không tìm thấy mức giá hợp lệ trong biên độ quy định (Hoặc bị Captcha).")
            
    except Exception as e:
        print(f"  => Lỗi truy cập: {e}")
        
    return results

def main():
    queries = [
        "rtx 4060 ti 16gb",
        "rtx 4090",
        "core i5 13400f",
        "core i5 13600k",
        "core i7 14700k",
        "samsung 990 pro 1tb"
    ]
    
    # Bổ sung 6 nguồn bán lẻ PC uy tín nhất Việt Nam
    sites = [
        {"name": "Nguyễn Công PC", "url": "https://nguyencongpc.vn/tim-kiem?q={}"},
        {"name": "An Phát PC", "url": "https://www.anphatpc.com.vn/tim?q={}"},
        {"name": "HACOM", "url": "https://hacom.vn/tim?q={}"},
        {"name": "GearVN", "url": "https://gearvn.com/search?type=product&q={}"},
        {"name": "KCCShop", "url": "https://kccshop.vn/tim-kiem?q={}"},
        {"name": "Hoàng Hà PC", "url": "https://hoanghapc.vn/tim?q={}"}
    ]
    
    print("="*70)
    print("🚀 HỆ THỐNG CÀO GIÁ NÂNG CẤP V2 (ĐA NGUỒN & SMART FILTER)")
    print("="*70 + "\n")
    
    report_lines = []
    report_lines.append("# BÁO CÁO CÀO GIÁ LINH KIỆN PC TỰ ĐỘNG")
    report_lines.append(f"*Cập nhật tự động lúc: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}*\n")
    
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
                prices = scrape_site(page, s['url'], q, s['name'])
                all_valid_prices.extend(prices)
                
            if all_valid_prices:
                # Tính toán thống kê từ TẤT CẢ các nguồn
                raw_prices = [item["price"] for item in all_valid_prices]
                med = statistics.median(raw_prices)
                
                # Lấy chi tiết nguồn của mức giá rẻ nhất
                min_obj = min(all_valid_prices, key=lambda x: x["price"])
                min_p = min_obj["price"]
                min_site = min_obj["site"]
                min_url = min_obj["url"]
                
                print(f"✅ THỐNG KÊ TOÀN THỊ TRƯỜNG CHO [{q.upper()}]:")
                print(f"   + Giá Sàn Rẻ Nhất: {min_p:,.0f} VNĐ (Tại {min_site})".replace(',', '.'))
                print(f"   + Giá Bán Phổ Biến (Trung Vị): {med:,.0f} VNĐ".replace(',', '.'))
                
                report_lines.append(f"## {q.upper()}")
                report_lines.append(f"- **Giá Sàn (Rẻ nhất):** {min_p:,.0f} VNĐ".replace(',', '.'))
                report_lines.append(f"  - *Nguồn để ép giá:* [{min_site}]({min_url})")
                report_lines.append(f"- **Giá Phổ Biến (Trung vị):** {med:,.0f} VNĐ".replace(',', '.'))
                report_lines.append("")
            else:
                report_lines.append(f"## {q.upper()}")
                report_lines.append(f"- Không thu thập được mức giá chuẩn (Có thể do Cloudflare chặn Bot hoặc thị trường hết hàng).")
                report_lines.append("")

            print("="*70 + "\n")
            
        browser.close()
        
    filename = f"ket_qua_cao_gia_{datetime.datetime.now().strftime('%d_%m_%Y')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))
    print(f"\n=> Đã lưu báo cáo chi tiết ra file: {filename}")

if __name__ == "__main__":
    main()
