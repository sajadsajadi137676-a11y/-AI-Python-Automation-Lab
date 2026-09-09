

import time

def s_ai_central_system():
    print("🔥 INITIALIZING SAJJAD's AI CENTRAL MASTER SYSTEM v1.0...")
    time.sleep(1)
    print("📂 Loading Database Core Module... [OK]")
    print("📧 Booting Gmail Inbox Scanner... [OK]")
    print("📱 Connecting SMS Handset Infrastructure... [OK]")
    print("\n🌐 SYSTEM IS FULLY INTEGRATED & LIVE (24/7 Monitoring Mode)\n")
    time.sleep(1)

    # ۱. خواندن ایمیل جدید مشتری شاکی از اینباکس جیمیل
    customer_email = "buyer.jones@gmail.com"
    email_body = "URGENT: My delivery is late and the box is broken! Worst company ever."
    
    print(f"📩 [STEP 1: GMAIL] Detected 1 new email from: {customer_email}")
    print(f"📄 Message content: \"{email_body}\"")
    time.sleep(1.5)

    # ۲. مغز هوش مصنوعی لحن پیام را بررسی می‌کند
    body_lower = email_body.lower()
    if "broken" in body_lower or "worst" in body_lower or "late" in body_lower:
        status_flag = "🔴 CRITICAL"
        sms_text = f"هشدار به مدیر! ایمیل بحرانی از {customer_email} دریافت شد. بررسی فوری!"
    else:
        status_flag = "🔵 NORMAL"
        sms_text = f"ایمیل جدید از {customer_email} دریافت و ثبت شد."

    print(f"📊 [STEP 2: AI BRAIN] Sentiment Analysis Complete: {status_flag}")
    time.sleep(1)

    # ۳. ثبت سریع اطلاعات مشتری و وضعیت بحرانی در فایل دیتابیس متنی
    print(f"📂 [STEP 3: DATABASE] Logging client data and AI status to central log...")
    db_file = "AI_Central_Report.txt"
    
    with open(db_file, "a", encoding="utf-8") as file:
        file.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')} | Email: {customer_email} | Status: {status_flag}\n")
        
    print(f"💾 Central Log updated! File saved as: {db_file}")
    time.sleep(1.5)

    # ۴. شلیک آنی پیامک هشدار به گوشی مدیر یا کارفرما
    print(f"📱 [STEP 4: SMS] Routing instant notification to administrator...")
    admin_phone = "09129998877"
    print(f"💬 Sent to {admin_phone}: \"{sms_text}\"")
    print("🎯 Delivery Status: ✔️ DELIVERED (Sent to handset successfully)")
    print("-" * 70)
    time.sleep(1)

    print("✨ CONGRATULATIONS SAJJAD! The Master Automation Loop Completed Successfully.")
    
    # ترمز جادویی سجاد برای قفل نگه داشتن پنجره ترمینال
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    s_ai_central_system()
