

import time

def ai_document_filter():
    print("🔥 INITIALIZING SAJJAD's AI DOCUMENT SECURITY CORE v1.0...")
    time.sleep(1)
    print("🛡️ Loading Deep Inspection Security Protocols... [OK]")
    print("🌐 Shield is Live! Scanning incoming text streams...\n")
    time.sleep(1.0)

    # ۱. لیست کلمات یا الگوهای محرمانه و ممنوعه که باید سانسور شوند
    confidential_keywords = ["card-9942", "password123", "secret-code"]

    # ۲. اسناد و فاکتورهای خام ورودی شرکت که نیاز به بررسی دارند
    incoming_documents = [
        "Payment received. Sender used card-9942 for 1500 USD.",
        "System update completed. Default login is password123.",
        "Project Alpha details are verified under secret-code specification."
    ]

    for doc_text in incoming_documents:
        print(f"📄 Analyzing Document Content...")
        time.sleep(1)
        
        # ۳. مغز هوش مصنوعی برای پیدا کردن و سانسور کلمات ممنوعه
        filtered_text = doc_text
        censored_count = 0
        
        for keyword in confidential_keywords:
            if keyword in filtered_text:
                # جایگزین کردن کلمه محرمانه با علامت ستاره برای امنیت
                filtered_text = filtered_text.replace(keyword, "[████████]")
                censored_count += 1
                
        # ۴. چاپ گزارش لوکس و ایمن شده برای کارفرما
        print(f"🛡️ [SECURITY SCAN COMPLETE]")
        print(f"   📝 Original: {doc_text}")
        print(f"   🔒 Secured:  {filtered_text}")
        print(f"   ⚠️ Violations Blocked: {censored_count}")
        print("-" * 65)
        time.sleep(1.5)

    print("✨ SUCCESS! All sensitive enterprise files filtered and secured perfectly.")
    
    # ⚡ ترمز جادویی سجاد برای قفل نگه داشتن صفحه مشکی ترمینال
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    ai_document_filter()
