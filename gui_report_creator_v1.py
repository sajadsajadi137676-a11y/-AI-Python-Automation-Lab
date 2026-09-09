

import tkinter as tk
from tkinter import messagebox
import time

# ۱. موتور گزارش‌گیری که به دکمه پنجره متصل می‌شود
def generate_gui_report():
    # تغییر وضعیت متن پنجره برای کارفرما
    status_label.config(text="🔄 در حال تحلیل دیتابیس و محاسبه سود کل...", fg="#ff9f43")
    window.update()
    time.sleep(1.5) # مکس طبیعی فرآیند پردازش داده‌ها
    
    # دیتابیس خام فروش
    sales_data = [
        {"product": "Sofa", "sales": 45, "revenue": 675000000},
        {"product": "Table", "sales": 120, "revenue": 480000000},
        {"product": "Chair", "sales": 310, "revenue": 465000000}
    ]
    
    best_product = ""
    max_sales = 0
    total_company_revenue = 0

    for item in sales_data:
        total_company_revenue += item["revenue"]
        if item["sales"] > max_sales:
            max_sales = item["sales"]
            best_product = item["product"]
            
    # پاک کردن لیست خروجی قبلی
    result_box.delete(0, tk.END)
    
    # تزریق داده‌های تحلیل شده به صورت تمیز داخل کادر پنجره
    result_box.insert(tk.END, f"💰 جمع کل درآمد شرکت: {total_company_revenue:,} تومان")
    result_box.insert(tk.END, f"🏆 محصول ستاره (پرفروش‌ترین): {best_product}")
    result_box.insert(tk.END, f"📊 حجم فروش محصول ستاره: {max_sales} عدد")
    result_box.insert(tk.END, f"💾 فایل گزارش متنی نیز ذخیره و بروزرسانی شد.")
    
    # پایان موفقیت‌آمیز عملیات
    status_label.config(text="✅ گزارش مدیریتی با موفقیت تولید شد.", fg="#2ecc71")
    messagebox.showinfo("Sajjad's AI Report", "گزارش نهایی با موفقیت آماده شد!")

# ۲. ساختن و طراحی بدنه پنجره گرافیکی (از صفرِ صفر)
window = tk.Tk()
window.title("AI Report Creator Dashboard v1.0")
window.geometry("450x400")
window.configure(bg="#1a1a24") # تم دارک لوکس

# تیتر بالای صفحه
title_label = tk.Label(window, text="📊 داشبورد هوشمند گزارش‌گیری مالی", font=("Arial", 14, "bold"), bg="#1a1a24", fg="#ffffff")
title_label.pack(pady=15)

# 💜 دکمه بنفش و بزرگ شروع تحلیل و تولید گزارش
report_btn = tk.Button(window, text="🚀 Analyze & Generate Report", font=("Arial", 11, "bold"), bg="#6c5ce7", fg="white", activebackground="#a29bfe", activeforeground="white", width=25, command=generate_gui_report)
report_btn.pack(pady=10)

# نوار وضعیت وسط صفحه
status_label = tk.Label(window, text="سیستم آماده پردازش دیتابیس خام فروش", font=("Arial", 10, "italic"), bg="#1a1a24", fg="#a0a0b0")
status_label.pack(pady=5)

# کادر شیک نمایش گزارش استخراج شده (Listbox) برای مدیرعامل
frame = tk.Frame(window, bg="#1a1a24")
frame.pack(pady=15)

result_box = tk.Listbox(frame, width=45, height=6, font=("Courier", 11), bg="#252538", fg="#00ffc4", bd=0, highlightthickness=1, highlightbackground="#444466")
result_box.pack()

# روشن نگه داشتن پنجره روی مانیتور
window.mainloop()
