

import tkinter as tk
from tkinter import messagebox
import time

# ۱. موتور پایش و سانسور که به دکمه پنجره متصل می‌شود
def start_security_scan():
    # خواندن متنی که کاربر در کادر بزرگ وارد کرده است
    raw_text = text_box.get("1.0", tk.END).strip()
    
    if not raw_text:
        messagebox.showwarning("⚠️ هشدار سیستم", "لطفاً ابتدا متنی را برای اسکن وارد کنید.")
        return
        
    status_label.config(text="🔄 در حال اسکن عمیق لایه‌های امنیتی...", fg="#ff9f43")
    window.update()
    time.sleep(1.2) # مکس طبیعی فرآیند آنالیز فایل
    
    # لیست کلمات محرمانه
    confidential_keywords = ["card-9942", "password123", "secret-code"]
    
    filtered_text = raw_text
    censored_count = 0
    
    for keyword in confidential_keywords:
        if keyword in filtered_text:
            filtered_text = filtered_text.replace(keyword, "[████████]")
            censored_count += 1
            
    # پاک کردن کادر متنی و تزریق متن امن شده جدید
    text_box.delete("1.0", tk.END)
    text_box.insert("1.0", filtered_text)
    
    # پایان موفقیت‌آمیز عملیات
    status_label.config(text=f"✅ پایش کامل شد. {censored_count} مورد امنیتی سانسور شد.", fg="#2ecc71")
    messagebox.showinfo("Sajjad's AI Shield", "اسناد شما با موفقیت ایمن‌سازی و فیلتر شدند!")

# ۲. ساختن و طراحی بدنه پنجره گرافیکی (از صفرِ صفر)
window = tk.Tk()
window.title("AI Document Security Core v1.0")
window.geometry("500x450")
window.configure(bg="#12121a") # تم فوق دارک امنیتی

# تیتر بالای صفحه
title_label = tk.Label(window, text="🔒 سپر هوشمند پایش و فیلتر اسناد", font=("Arial", 14, "bold"), bg="#12121a", fg="#ffffff")
title_label.pack(pady=15)

# نوار وضعیت وسط صفحه
status_label = tk.Label(window, text="متن فاکتور یا سند خام را در کادر زیر وارد کنید:", font=("Arial", 10, "italic"), bg="#12121a", fg="#a0a0b0")
status_label.pack(pady=5)

# کادر بزرگ متنی (Text) برای ورود اسناد چند خطی
frame = tk.Frame(window, bg="#12121a")
frame.pack(pady=10)

text_box = tk.Text(frame, width=50, height=8, font=("Courier", 11), bg="#1e1e2d", fg="#ffffff", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#333344")
text_box.pack()
# تزریق یک متن تست پیش‌فرض حاوی کلمه ممنوعه برای راحتی کار شما
text_box.insert("1.0", "Payment complete. User data verified via password123 security key.")

# 💜 دکمه بنفش و بزرگ شروع پایش امنیتی
scan_btn = tk.Button(window, text="🛡️ Run Deep Security Scan", font=("Arial", 12, "bold"), bg="#6c5ce7", fg="white", activebackground="#a29bfe", activeforeground="white", width=25, command=start_security_scan)
scan_btn.pack(pady=20)

# روشن نگه داشتن پنجره روی مانیتور
window.mainloop()
