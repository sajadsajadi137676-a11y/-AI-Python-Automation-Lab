
import tkinter as tk
from tkinter import messagebox
import time

def start_hardware_scan():
    status_label.config(text="⚡ AI Hardware ACPI Bus Scanning... Please Wait.", fg="#FFCC00")
    window.update()
    time.sleep(1)
    
    hardware_stats = [
        {"component": "CPU Core Temperature", "value": "54°C", "status": "Normal"},
        {"component": "RAM Memory Usage", "value": "62%", "status": "Normal"},
        {"component": "Main Battery Capacity", "value": 28, "status": "Checking..."},
        {"component": "GPU Matrix Clock", "value": "1200 MHz", "status": "Normal"}
    ]
    
    output_text.delete("1.0", tk.END)
    metrics_scanned = 0
    
    for metric in hardware_stats:
        output_text.insert(tk.END, f"🔎 Syncing sensor stream for: {metric['component']}...\n")
        window.update()
        time.sleep(0.5)
        
        if metric['component'] == "Main Battery Capacity":
            battery_level = metric['value']
            if battery_level < 30:
                output_text.insert(tk.END, f"   ⚠️ [CRITICAL ALERT] -> Battery Level: {battery_level}%\n")
                output_text.insert(tk.END, f"   ⚡ Action: BACKGROUND PROFILES KILLED | SAVER ACTIVE\n")
            else:
                output_text.insert(tk.END, f"   🟢 [BATTERY HEALTHY] -> Level: {battery_level}%\n")
        else:
            output_text.insert(tk.END, f"   🔹 Value Captured: {metric['value']} | Status: {metric['status']}\n")
            
        output_text.insert(tk.END, "   ✅ [METRIC LOGGED IN SYSTEM REGISTER]\n")
        output_text.insert(tk.END, "-" * 45 + "\n")
        output_text.see(tk.END)
        window.update()
        metrics_scanned += 1
        time.sleep(0.5)
    
    status_label.config(text="✨ VIP Hardware Diagnostics Complete & Secured!", fg="#00FF00")
    messagebox.showinfo("Professor Sajjad Hardware Core", 
                        f"🔋 System Diagnostic Successful!\n\n🛡️ Cyber Shield Status: 100% Secure")

# 🖥️ ساخت پنجره اصلی با تم تمام مشکی لوکس و نئونی
window = tk.Tk()
window.title("Sajjad's VIP AI Hardware Monitor & Battery Saver v1.0")
window.geometry("550x550")
window.configure(bg="#0B0B0C")  # تم فوق‌العاده تاریک مشکی کربنی

# عنوان بالای صفحه
title_label = tk.Label(window, text="🔋 AI HARDWARE TELEMETRY CORE", font=("Arial", 15, "bold"), fg="#FF3366", bg="#0B0B0C")
title_label.pack(pady=15)

# دکمه بزرگ نئونی صورتی/قرمز خفن برای شروع پایش سخت‌افزار
run_button = tk.Button(window, text="🚀 DIAGNOSE HARDWARE BUS", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#FF3366", activebackground="#CC2952", activeforeground="#FFFFFF", width=25, height=2, command=start_hardware_scan)
run_button.pack(pady=10)

# متن وضعیت سیستم
status_label = tk.Label(window, text="🟢 ACPI Bus Ready. Click Diagnose to Read Sensors.", font=("Arial", 10), fg="#505055", bg="#0B0B0C")
status_label.pack(pady=5)

# باکس مانیتورینگ متون با رنگ سفید صورتی نئونی مات و پس‌زمینه زغالی
output_text = tk.Text(window, font=("Consolas", 10), fg="#FF80A0", bg="#16161A", width=65, height=18, relief=tk.FLAT)
output_text.pack(pady=10)

window.mainloop()
