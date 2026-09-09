

import time

def ai_pricing_bot():
    print("🔥 INITIALIZING SAJJAD's AI PRICING ENGINE v1.0...")
    time.sleep(1)
    print("📦 Loading Digital Price List... [OK]")
    print("🌐 Bot is Online! Waiting for customer price inquiries...\n")
    time.sleep(1)

    # ۱. لیست قیمت محصولات بیزینس (دیتابیس کوچک ما)
    products_price = {"sofa": 15000000, "table": 4000000, "chair": 1500000}

    # ۲. پیام‌های فرضی که مشتریان در دایرکت یا سایت می‌فرستند
    incoming_messages = [
        "سلام قیمت sofa چقدر هست؟",
        "تخفیف هم میدید روی قیمت table؟",
        "هزینه ارسال chair چقدر میشه؟"
    ]

    for message in incoming_messages:
        print(f"📩 New Message: \"{message}\"")
        msg_lower = message.lower()
        
        # ۳. مغز هوش مصنوعی برای پیدا کردن نام محصول و کلمه تخفیف
        found_product = None
        for product in products_price:
            if product in msg_lower:
                found_product = product
                break
        
        # ۴. تصمیم‌گیری و تولید پاسخ هوشمند بر اساس درخواست مشتری
        if found_product:
            actual_price = products_price[found_product]
            
            if "تخفیف" in msg_lower or "off" in msg_lower:
                # اگر مشتری تخفیف خواست، سیستم خودکار ۱۰ درصد کم می‌کند!
                discounted_price = int(actual_price * 0.9)
                ai_reply = f"مشتری گرامی، قیمت اصلی {found_product} برابر {actual_price:,} تومان است. اما به عنوان تخفیف ویژه امروز، می‌توانید آن را با قیمت {discounted_price:,} تومان تهیه کنید!"
            elif "ارسال" in msg_lower or "پست" in msg_lower:
                ai_reply = f"مشتری گرامی، قیمت {found_product} برابر {actual_price:,} تومان است و ارسال آن به سراسر کشور کاملاً رایگان می‌باشد."
            else:
                ai_reply = f"سلام و احترام، قیمت {found_product} در حال حاضر {actual_price:,} تومان می‌باشد."
        else:
            ai_reply = "سلام و احترام، پیام شما دریافت شد. لطفاً نام محصول مدنظر خود را ارسال کنید تا قیمت دقیق برای شما بفرستیم."

        print(f"✍️ AI Generated Reply:\n   \"{ai_reply}\"")
        print("-" * 65)
        time.sleep(2)

    print("✨ SUCCESS! All price inquiries answered perfectly.")
    
    # ۵. ترمز جادویی سجاد برای قفل نگه داشتن صفحه مشکی ترمینال
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    ai_pricing_bot()
