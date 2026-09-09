

import tkinter as tk
from tkinter import messagebox
import time

# ۱. موتور استخراج متنی که به دکمه پنجره متصل می‌شود
def start_pdf_extraction():
    # دیتای فرضی شبیه‌سازی شده از یک فایل PDF ورودی
    sample_pdf_data = "Invoice ID: #99421 | Customer: Alice Smith | Total Amount: 1,500 USD | Status: Paid"
    
    # تغییر وضعیت متن پنجره برای کارفرما
    status_label.config(text="🔄 در حال اسکن و خواندن فایل PDF...", fg="#ff9f43")
    window.update()
    time.sleep(1.5) # مکس طبیعی فرآیند باز کردن فایل
    
    # مغز هوش مصنوعی سجاد برای تکه‌تکه کردن داده‌ها
    parts = sample_pdf_data.split(" | ")
    
    invoice_id = parts[0].split(": ")[1]
    customer_name = parts[1].split(": ")[1]
    amount = parts[2].split(": ")[1]
    status = parts[3].split(": ")[1]
    
    # پاک کردن لیست خروجی قبلی
    result_box.delete(0, tk.END)
    
    # تزریق داده‌های استخراج شده به صورت تمیز داخل کادر پنجره
    result_box.insert(tk.END, f"🆔 شماره فاکتور: {invoice_id}")
    result_box.insert(tk.END, f"👤 نام مشتری: {customer_name}")
    result_box.insert(tk.END, f"💰 مبلغ کل: {amount}")
    result_box.insert(tk.END, f"🚨 وضعیت فاکتور: {status}")
    
    # پایان موفقیت‌آمیز عملیات
    status_label.config(text="✅ استخراج اطلاعات با موفقیت پایان یافت.", fg="#2ecc71")
    messagebox.showinfo("Sajjad's AI PDF", "اطلاعات فاکتور از فایل PDF استخراج شد!")

# ۲. ساختن و طراحی بدنه پنجره گرافیکی (از صفرِ صفر)
window = tk.Tk()
window.title("AI PDF Data Extractor Dashboard v1.0")
window.geometry("450x400")
window.configure(bg="#1c1c24") # تم دارک هکری لوکس

# تیتر بالای صفحه
title_label = tk.Label(window, text="📊 داشبورد هوشمند استخراج از PDF", font=("Arial", 15, "bold"), bg="#1c1c24", fg="#ffffff")
title_label.pack(pady=15)

# 💜 دکمه بنفش و بزرگ شروع استخراج دیتای فایل
extract_btn = tk.Button(window, text="🚀 Select & Extract PDF Data", font=("Arial", 11, "bold"), bg="#6c5ce7", fg="white", activebackground="#a29bfe", activeforeground="white", width=25, command=start_pdf_extraction)
extract_btn.pack(pady=10)

# نوار وضعیت وسط صفحه
status_label = tk.Label(window, text="سیستم آماده دریافت فایل پی‌دی‌اف", font=("Arial", 10, "italic"), bg="#1c1c24", fg="#a0a0b0")
status_label.pack(pady=5)

# کادر شیک نمایش دیتای استخراج شده (Listbox) برای کارفرما
frame = tk.Frame(window, bg="#1c1c24")
frame.pack(pady=15)

result_box = tk.Listbox(frame, width=45, height=6, font=("Courier", 11), bg="#252538", fg="#00ffc4", bd=0, highlightthickness=1, highlightbackground="#444466")
result_box.pack()

# روشن نگه داشتن پنجره روی مانیتور
window.mainloop()
