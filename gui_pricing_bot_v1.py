

import tkinter as tk
from tkinter import messagebox
import time

# ۱. موتور محاسبات و قیمت‌دهی که به دکمه پنجره وصل می‌شود
def calculate_and_price():
    # خواندن متنی که کاربر در کادر ورودی پنجره تایپ کرده است
    user_input = entry_box.get()
    msg_lower = user_input.lower()
    
    # دیتابیس کوچک قیمت محصولات ما
    products_price = {"sofa": 15000000, "table": 4000000, "chair": 1500000}
    
    found_product = None
    for product in products_price:
        if product in msg_lower:
            found_product = product
            break
            
    if found_product:
        actual_price = products_price[found_product]
        
        # اگر کلمه تخفیف یا off در کادر ورودی پیدا شود
        if "تخفیف" in msg_lower or "off" in msg_lower:
            discounted_price = int(actual_price * 0.9)
            reply = f"قیمت اصلی {found_product}: {actual_price:,} تومان\n🔥 قیمت با ۱۰٪ تخفیف ویژه: {discounted_price:,} تومان"
        else:
            reply = f"سلام، قیمت {found_product} در حال حاضر {actual_price:,} تومان می‌باشد."
    else:
        reply = "❌ محصولی پیدا نشد! لطفا نام محصول (sofa, table, chair) را وارد کنید."
        
    # نمایش پاسخ هوشمند در کادر وضعیت پایین پنجره
    result_label.config(text=reply, fg="#00ffc4")
    messagebox.showinfo("Sajjad's AI Pricing", "عملیات محاسبه قیمت با موفقیت انجام شد!")

# ۲. ساختن و طراحی اتاق گرافیکی پنجره (از صفرِ صفر)
window = tk.Tk()
window.title("AI Pricing Assistant v1.0")
window.geometry("450x350")
window.configure(bg="#1e1e2a") # رنگ پس‌زمینه بسیار لوکس دارک

# تیتر بالای صفحه
title_label = tk.Label(window, text="💰 AI Pricing Dashboard", font=("Arial", 16, "bold"), bg="#1e1e2a", fg="#ffffff")
title_label.pack(pady=15)

# متن راهنمای کاربر
info_label = tk.Label(window, text="متن درخواست مشتری را اینجا وارد کنید:", font=("Arial", 11), bg="#1e1e2a", fg="#a0a0b0")
info_label.pack(pady=5)

# کادر ورودی متنی (جایی که متن مشتری را تایپ می‌کنیم)
entry_box = tk.Entry(window, width=40, font=("Arial", 11), bg="#2d2d3f", fg="#ffffff", insertbackground="white", bd=0, highlightthickness=1, highlightbackground="#444466")
entry_box.pack(pady=5)
entry_box.insert(0, "سلام قیمت sofa با تخفیف چنده؟") # متن پیش‌فرض برای تست سریع

# 💜 دکمه بنفش و بزرگ شروع محاسبات قیمت
calc_btn = tk.Button(window, text="🚀 Calculate Price & Discount", font=("Arial", 11, "bold"), bg="#6c5ce7", fg="white", activebackground="#a29bfe", activeforeground="white", width=25, command=calculate_and_price)
calc_btn.pack(pady=15)

# کادر نمایش خروجی نهایی به کاربر
result_label = tk.Label(window, text="منتظر دستور شما...", font=("Arial", 11, "bold"), bg="#1e1e2a", fg="#ff9f43", justify=tk.CENTER)
result_label.pack(pady=20)

# روشن نگه داشتن پنجره روی مانیتور
window.mainloop()
