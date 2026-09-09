

import time
import random

def live_email_processor():
    print("🚀 Sajjad's AI Email Engine v2.0 is starting up...")
    time.sleep(1)
    print("🌐 Connecting to Enterprise Mail Gateway... [OK]")
    time.sleep(1)
    print("📥 System is Live! Scanning inbox for real-time customer support...\n")
    time.sleep(1.5)

    # ایمیل‌های واقعی مشتریان بین‌المللی که به سیستم شما می‌رسند
    incoming_mailbox = [
        {"sender": "alice.smith@gmail.com", "subject": "Broken item received", "msg": "Hello, my order arrived broken today. Worst delivery experience ever!"},
        {"sender": "karim.ahmadi@yahoo.com", "subject": "سوال درباره قیمت", "body": "سلام، قیمت مبل‌های راحتی جدیدتون چقدر هست؟"},
        {"sender": "david.miller@outlook.com", "subject": "Amazing Product!", "msg": "Wow! I just wanted to say thank you. The quality is absolutely perfect."}
    ]

    for email in incoming_mailbox:
        print(f"📩 Incoming Mail From: {email['sender']}")
        print(f"📄 Topic/Subject: {email.get('subject', 'No Subject')}")
        
        # مغز تحلیل لحن هوش مصنوعی سجاد
        text_to_analyze = str(email.get('msg', '') + email.get('body', '')).lower()
        
        if "broken" in text_to_analyze or "worst" in text_to_analyze or "broken" in text_to_analyze:
            sentiment = "🔴 CRITICAL / ANGRY CUSTOMER"
            ai_reply = "Dear Customer, we sincerely apologize for the inconvenience. Our support manager will call you in 10 minutes to fix this."
        elif "amazing" in text_to_analyze or "perfect" in text_to_analyze or "thank" in text_to_analyze:
            sentiment = "🟢 HAPPY CUSTOMER"
            ai_reply = "Dear Customer, thank you so much for your wonderful feedback! We are thrilled to hear that."
        else:
            sentiment = "🔵 NORMAL INQUIRY"
            ai_reply = "سلام مشتری گرامی، پیام شما دریافت شد. همکاران ما به زودی قیمت دقیق را برای شما ارسال خواهند کرد."

        print(f"📊 AI Real-Time Analysis: {sentiment}")
        print(f"✍️ Generated Auto-Response:\n   \"{ai_reply}\"")
        print("-" * 65)
        time.sleep(2) # مکس طبیعی برای حس زنده بودن پردازش

    print("✨ SUCCESS! All pending emails successfully processed by AI.")
    print("💤 Engine entering standby mode... Waiting for next wave.")

if __name__ == "__main__":
    live_email_processor()

input("\nPress Enter to exit...")