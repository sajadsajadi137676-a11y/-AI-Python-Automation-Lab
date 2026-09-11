
import tkinter as tk
from tkinter import messagebox
import time

def start_analysis():
    # ۱. تغییر متن دکمه و وضعیت سیستم
    status_label.config(text="⚡ AI Core Initializing... Please Wait.", fg="#FFCC00")
    window.update()
    time.sleep(1)
    
    # ۲. دیتای خام فایل اکسل مالی
    excel_rows = [
        {"customer": "Alireza", "product": "AI Automation Bot", "amount": 15000000},
        {"customer": "Morteza", "product": "Sleek Python GUI", "amount": 8500000},
        {"customer": "Zahra", "product": "Database Reporting Engine", "amount": 22000000},
        {"customer": "Hassan", "product": "Simple Script", "amount": 3000000}
    ]
    
    # ۳. پردازش و فیلتر هوشمند ردیف‌ها
    output_text.delete("1.0", tk.END)
    vip_count = 0
    total_vip_revenue = 0
    
    for row in excel_rows:
        output_text.insert(tk.END, f"🔎 Scanning: {row['customer']}...\n")
        window.update()
        time.sleep(0.5)
        
        if row['amount'] >= 10000000:
            output_text.insert(tk.END, f"   ⭐ [VIP DETECTED] -> 💰 {row['amount']:,} Toman\n")
            vip_count += 1
            total_vip_revenue += row['amount']
        else:
            output_text.insert(tk.END, f"   🔹 Regular Row -> {row['amount']:,} Toman\n")
        output_text.insert(tk.END, "-" * 40 + "\n")
        output_text.see(tk.END)
        window.update()
    
    # ۴. نمایش گزارش نهایی لوکس
    status_label.config(text="📊 Analysis Completed Successfully!", fg="#00FF00")
    messagebox.showinfo("Professor Sajjad AI Engine", 
                        f"✅ Scan Complete!\n\n⚠️ VIP Clients: {vip_count}\n💵 Total Revenue: {total_vip_revenue:,} Toman")

# 🖥️ ساخت پنجره اصلی با تم دارک و لوکس
window = tk.Tk()
window.title("Sajjad's AI Excel Analyzer v1.0")
window.geometry("550x550")
window.configure(bg="#1E1E1E")  # رنگ پس‌زمینه دارک هکری

# عنوان بالای صفحه
title_label = tk.Label(window, text="📊 AI SMART EXCEL ANALYZER", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#1E1E1E")
title_label.pack(pady=15)

# دکمه بزرگ و شیک برای شروع اتوماسیون
run_button = tk.Button(window, text="🚀 RUN AI AUTOMATION", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#007ACC", activebackground="#005999", activeforeground="#FFFFFF", width=25, height=2, command=start_analysis)
run_button.pack(pady=10)

# متن وضعیت سیستم
status_label = tk.Label(window, text="🟢 System Ready. Click Run to Start.", font=("Arial", 10), fg="#858585", bg="#1E1E1E")
status_label.pack(pady=5)

# باکس نمایش دیتای آنلاین و مانیتورینگ
output_text = tk.Text(window, font=("Consolas", 10), fg="#00FF00", bg="#2D2D2D", width=65, height=18, relief=tk.FLAT)
output_text.pack(pady=10)

window.mainloop()
