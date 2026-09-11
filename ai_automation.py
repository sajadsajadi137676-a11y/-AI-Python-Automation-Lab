
import time

def ai_excel_analyzer():
    print("🔥 INITIALIZING SAJJAD's AI EXCEL ANALYTICS CORE v1.0...")
    time.sleep(1)
    print("📊 Loading Data Processing Matrix... [OK]\n")
    time.sleep(1)

    # شبیه‌سازی ردیف‌های مالی یک فایل اکسل شرکت
    excel_rows = [
        {"customer": "Alireza", "product": "AI Automation Bot", "amount": 15000000},
        {"customer": "Morteza", "product": "Sleek Python GUI", "amount": 8500000},
        {"customer": "Zahra", "product": "Database Reporting Engine", "amount": 22000000},
        {"customer": "Hassan", "product": "Simple Script", "amount": 3000000}
    ]

    vip_count = 0
    total_vip_revenue = 0

    for row in excel_rows:
        print(f"🔎 Scanning row for Customer: {row['customer']}...")
        time.sleep(0.8)
        
        # فیلتر فاکتورهای بالای ۱۰ میلیون تومان
        if row['amount'] >= 10000000:
            print(f"   ⭐ [VIP TRANSACTION DETECTED] 💰 Value: {row['amount']:,} Toman")
            vip_count += 1
            total_vip_revenue += row['amount']
        else:
            print(f"   🔹 Regular Transaction. Value: {row['amount']:,} Toman")
        print("-" * 50)

    print("\n📊 ================== FINAL EXCEL REPORT ==================")
    print(f"⚠️ High-Value VIP Clients Found: {vip_count}")
    print(f"💵 Total VIP Revenue Secured: {total_vip_revenue:,} Toman")
    print("===========================================================")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    ai_excel_analyzer()
