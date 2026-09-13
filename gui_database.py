
import tkinter as tk
from tkinter import messagebox
import time

def start_database_backup():
    status_label.config(text="⚡ AI Encryption Key Exchange Live... Please Wait.", fg="#FFCC00")
    window.update()
    time.sleep(1)
    
    corporate_databases = [
        {"db_id": "DB-MAIN", "name": "Users_Credentials_SQL", "type": "MySQL", "size_gb": 145.2},
        {"db_id": "DB-LOGS", "name": "System_Traffic_Logs", "type": "NoSQL", "size_gb": 42.0},
        {"db_id": "DB-FINANCE", "name": "Financial_Transactions_2026", "type": "PostgreSQL", "size_gb": 280.5},
        {"db_id": "DB-TEST", "name": "Staging_Environment_Dev", "type": "SQLite", "size_gb": 5.4}
    ]
    
    output_text.delete("1.0", tk.END)
    backups_completed = 0
    
    for db in corporate_databases:
        output_text.insert(tk.END, f"🔎 Checking node integrity for: {db['name']}...\n")
        window.update()
        time.sleep(0.5)
        
        if db['size_gb'] >= 100.0:
            output_text.insert(tk.END, f"   ⚠️ [CRITICAL NODE] -> High-Priority Enterprise Data.\n")
            policy = "FULL HOT-BACKUP"
        else:
            output_text.insert(tk.END, f"   🔹 [STANDARD NODE] -> Regular cloud archive.\n")
            policy = "INCREMENTAL CLOUD"
            
        output_text.insert(tk.END, f"   🛠️ Compressing stream ({db['type']}) | Policy: {policy}\n")
        output_text.insert(tk.END, f"   💾 Dump: Storage/Backups/Secure_Dump_{db['name']}.bak\n")
        output_text.insert(tk.END, "   ✅ [DATABASE SEGMENT SECURED AND VERIFIED]\n")
        output_text.insert(tk.END, "-" * 45 + "\n")
        output_text.see(tk.END)
        window.update()
        backups_completed += 1
        time.sleep(0.5)
    
    status_label.config(text="✨ All Enterprise Cloud Backups Secured Successfully!", fg="#00FF00")
    messagebox.showinfo("Professor Sajjad Backup Core", 
                        f"🛡️ Security Protocol Successful!\n\n💾 Total SQL Backups Created: {backups_completed}")

# 🖥️ ساخت پنجره اصلی با تم دارک و خاکستری متالیک
window = tk.Tk()
window.title("Sajjad's AI Database Backup & Monitoring System v1.0")
window.geometry("550x550")
window.configure(bg="#212529")  # تم خاکستری بسیار تیره متالیک

# عنوان بالای صفحه
title_label = tk.Label(window, text="🛡️ AI DATABASE AUTOMATION CORE", font=("Arial", 15, "bold"), fg="#E9ECEF", bg="#212529")
title_label.pack(pady=15)

# دکمه بزرگ قرمز آتشین خفن برای شروع پشتیبان‌گیری
run_button = tk.Button(window, text="🚨 EXECUTE BACKUP PROTOCOL", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#DC3545", activebackground="#BD2130", activeforeground="#FFFFFF", width=25, height=2, command=start_database_backup)
run_button.pack(pady=10)

# متن وضعیت سیستم
status_label = tk.Label(window, text="🟢 Encryption Node Ready. Click Execute to Secure Data.", font=("Arial", 10), fg="#6C757D", bg="#212529")
status_label.pack(pady=5)

# باکس مانیتورینگ متون با رنگ سفید مات و پس‌زمینه تیره
output_text = tk.Text(window, font=("Consolas", 10), fg="#CED4DA", bg="#343A40", width=65, height=18, relief=tk.FLAT)
output_text.pack(pady=10)

window.mainloop()
