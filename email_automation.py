
import time

def ai_email_dispatcher():
    print("🚀 INITIALIZING SAJJAD's AI EMAIL AUTOMATION ENGINE v1.0...")
    time.sleep(1)
    print("🔗 Connecting to Secure SMTP Mail Server... [OK]")
    print("📬 Dispatcher Core is Live! Scanning client database...\n")
    time.sleep(1.2)

    # شبیه‌سازی دیتابیس مشتریان شرکت (نام، ایمیل، وضعیت حساب، مبلغ بدهی)
    client_database = [
        {"name": "Ehsan", "email": "ehsan@example.com", "status": "VIP", "balance": 0},
        {"name": "Ali", "email": "ali@example.com", "status": "Regular", "balance": 4500000},
        {"name": "Sara", "email": "sara@example.com", "status": "VIP", "balance": 12000000},
        {"name": "Nima", "email": "nima@example.com", "status": "Regular", "balance": 0}
    ]

    emails_sent = 0

    # مغز اتوماسیون برای تفکیک و ساخت گزارش اختصاصی
    for client in client_database:
        print(f"🔎 Analysing account stats for: {client['name']}...")
        time.sleep(0.8)
        
        # سناریوی اول: مشتری بدهی سنگین دارد
        if client['balance'] > 0:
            print(f"   ⚠️ [ALERT] Account Balance Outstanding: {client['balance']:,} Toman")
            email_body = f"Dear {client['name']},\nThis is an automated reminder. Your outstanding balance is {client['balance']:,} Toman. Please settle it."
            
        # سناریوی دوم: مشتری VIP است و تسویه کامل
        elif client['status'] == "VIP":
            print(f"   👑 [PREMIUM] VIP Client with Clear Balance.")
            email_body = f"Dear VIP Client {client['name']},\nThank you for being a premium partner. Your annual business report is ready for review."
            
        # سناریوی سوم: مشتری معمولی و تسویه کامل
        else:
            print(f"   🔹 [STANDARD] Active Client with Clear Balance.")
            email_body = f"Dear {client['name']},\nYour monthly activity report has been generated successfully."

        # شبیه‌سازی شلیک و ارسال ایمیل به سرور
        print(f"   📧 Drafting Email to: {client['email']}")
        print(f"   📝 Content snippet: \"{email_body[:50]}...\"")
        print(f"   ⚡ Sending via Sajjad Mailer Server...")
        time.sleep(1)
        print("   ✅ [EMAIL DISPATCHED SUCCESSFULLY]")
        print("-" * 65)
        emails_sent += 1

    # چاپ گزارش نهایی سیستم برای کارفرما
    print("\n📊 ================== FINAL EMAIL ENGINE REPORT ==================")
    print(f"✅ Total Clients Scanned: {len(client_database)}")
    print(f"📨 Total Automated Emails Dispatched: {emails_sent}")
    print("==================================================================")
    print("✨ SUCCESS! All corporate communication streams handled perfectly.")
    
    # قفل نگه داشتن صفحه ترمینال
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    ai_email_dispatcher()
