

import time

def ai_report_creator():
    print("🔥 INITIALIZING SAJJAD's AI REPORT CREATOR v1.0...")
    time.sleep(1)
    print("📊 Loading Raw Sales Database... [OK]")
    print("🌐 Analytics Engine is Live! Generating summary...\n")
    time.sleep(1.0)

    # ۱. دیتابیس خام از فروش ماهانه شرکت (شامل نام محصول و تعداد فروش)
    sales_data = [
        {"product": "Sofa", "sales": 45, "revenue": 675000000},
        {"product": "Table", "sales": 120, "revenue": 480000000},
        {"product": "Chair", "sales": 310, "revenue": 465000000}
    ]

    # ۲. مغز هوش مصنوعی برای پیدا کردن پرفروش‌ترین محصول بر اساس تعداد
    best_product = ""
    max_sales = 0
    total_company_revenue = 0

    for item in sales_data:
        total_company_revenue += item["revenue"]
        if item["sales"] > max_sales:
            max_sales = item["sales"]
            best_product = item["product"]

    # ۳. ثبت خودکار گزارش نهایی در یک فایل متنی برای مدیرعامل
    report_file = "Executive_Sales_Report.txt"
    with open(report_file, "w", encoding="utf-8") as file:
        file.write("=== EXECUTIVE SALES REPORT ===\n")
        file.write(f"Generated Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f"Total Company Revenue: {total_company_revenue:,} Toman\n")
        file.write(f"Top Selling Product by Volume: {best_product} ({max_sales} units)\n")
        file.write("==============================\n")

    # ۴. چاپ گزارش در ترمینال مرکزی
    print("🎯 [AI REPORT GENERATION SUCCESS]")
    print(f"   💰 Total Revenue: {total_company_revenue:,} Toman")
    print(f"   🏆 Star Product: {best_product} ({max_sales} units)")
    print(f"   💾 Saved Report File: {report_file}")
    print("-" * 65)
    time.sleep(1)

    print("✨ SUCCESS! Executive data report created perfectly.")
    
    # ⚡ ترمز جادویی سجاد برای قفل نگه داشتن صفحه مشکی ترمینال
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    ai_report_creator()
