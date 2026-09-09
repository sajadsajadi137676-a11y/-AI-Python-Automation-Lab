

import tkinter as tk
from tkinter import messagebox
import time

# ۱. موتور پردازش جیمیل شما که حالا به دکمه پنجره وصل شده است
def start_gmail_automation():
    # تغییر متن نوار وضعیت برای گزارش به کارفرما
    status_label.config(text="🔄 Scanning Live Inbox, please wait...", fg="#ff9f43")
    window.update()
    time.sleep(1.5) # شبیه‌سازی زمان اتصال
    
    # ایمیل‌های دریافتی مشتریان
    sample_emails = [
        {"sender": "alice.smith@gmail.com", "msg": "Broken item received! Worst delivery experience."},
        {"sender": "karim.ahmadi@yahoo.com", "msg": "سلام، قیمت مبل‌های راحتی جدیدتون چقدر هست؟"},
        {"sender": "david.miller@outlook.com", "msg": "Amazing Product! The quality is absolutely perfect."}
    ]
    
    # پاک کردن لیست قبلی در پنجره (اگر وجود داشته باشد)
    result_box.delete(0, tk.END)
    
    for email in sample_emails:
        text_to_analyze = email["msg"].lower()
        
        if "broken" in text_to_analyze or "worst" in text_to_analyze:
            sentiment = "🔴 CRITICAL"
            reply = "Apology sent to manager."
        elif "amazing" in text_to_analyze or "perfect" in text_to_analyze:
            sentiment = "🟢 HAPPY"
            reply = "Thank you email sent."
        else:
            sentiment = "🔵 NORMAL"
            reply = "Price list sent."
            
        # چاپ ردیف به ردیف نتایج در کادر شیک پنجره گرافیکی
        result_box.insert(tk.END, f"📩 From: {email['sender']}")
        result_box.insert(tk.END, f"📊 AI Sentiment: {sentiment} | ✍️ Action: {reply}")
        result_box.insert(tk.END, "-" * 55)
        window.update()
        time.sleep(1) # مکس طبیعی پردازش
        
    # پایان موفقیت‌آمیز عملیات
    status_label.config(text="✅ Success! All emails processed successfully.", fg="#2ecc71")
    messagebox.showinfo("Sajjad's AI Engine", "Congratulations Sajjad!\nGmail Automation Complete.")

# ۲. طراحی بدنه و ظاهر پنجره (تم لوکس دارک)
window = tk.Tk()
window.title("AI Gmail Automation Dashboard v2.0")
window.geometry("500x450")
window.configure(bg="#1a1a24") # رنگ پس‌زمینه بسیار شیک دارک هکربار

# تیتر بالای صفحه
title_label = tk.Label(window, text="📧 AI Gmail Automation Hub", font=("Arial", 16, "bold"), bg="#1a1a24", fg="#ffffff")
title_label.pack(pady=15)

# 💜 دکمه بنفش و بزرگ شروع اتوماسیون
start_btn = tk.Button(window, text="🚀 Fetch & Process Emails", font=("Arial", 12, "bold"), bg="#6c5ce7", fg="white", activebackground="#a29bfe", activeforeground="white", width=24, command=start_gmail_automation)
start_btn.pack(pady=10)

# نوار وضعیت وسط صفحه
status_label = tk.Label(window, text="System Ready", font=("Arial", 11, "italic"), bg="#1a1a24", fg="#a0a0b0")
status_label.pack(pady=5)

# کادر شیک نمایش گزارش‌ها (Listbox) برای کارفرما
frame = tk.Frame(window, bg="#1a1a24")
frame.pack(pady=15)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
result_box = tk.Listbox(frame, width=52, height=10, font=("Courier", 10), bg="#252538", fg="#00ffc4", yscrollcommand=scrollbar.set, bd=0, highlightthickness=1, highlightbackground="#444466")

scrollbar.config(command=result_box.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# روشن نگه داشتن پنجره
window.mainloop()
