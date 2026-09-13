
import tkinter as tk
from tkinter import messagebox
import time

def start_auto_login():
    status_label.config(text="⚡ AI Authentication Handshake Live...", fg="#FFCC00")
    window.update()
    time.sleep(1)
    
    user_database = [
        {"username": "Sajjad_Professor", "role": "Admin", "password_status": "Strong"},
        {"username": "Reza_Dev", "role": "Developer", "password_status": "Strong"},
        {"username": "Maryam_Manager", "role": "Manager", "password_status": "Medium"},
        {"username": "Guest_User", "role": "Guest", "password_status": "Weak"}
    ]
    
    output_text.delete("1.0", tk.END)
    accounts_verified = 0
    
    for user in user_database:
        output_text.insert(tk.END, f"🔎 Injecting secure credentials for: {user['username']}...\n")
        window.update()
        time.sleep(0.5)
        
        if user['role'] == "Admin":
            output_text.insert(tk.END, f"   👑 [ADMIN ACCESS] -> Full Privileges Unlocked.\n")
            session_status = "SUPERUSER LIVE"
        else:
            output_text.insert(tk.END, f"   🔹 [STANDARD ACCESS] -> Restricted Role: {user['role']}\n")
            session_status = "REGULAR LIVE"
            
        output_text.insert(tk.END, f"   🔐 Autofilling... Password Security: {user['password_status']}\n")
        output_text.insert(tk.END, f"   🖥️ Dashboard Status: {session_status}\n")
        output_text.insert(tk.END, "   ✅ [AUTOMATED LOGIN SUCCESSFUL]\n")
        output_text.insert(tk.END, "-" * 45 + "\n")
        output_text.see(tk.END)
        window.update()
        accounts_verified += 1
        time.sleep(0.5)
    
    status_label.config(text="✨ All Automated Enterprise Logins Live!", fg="#00FF00")
    messagebox.showinfo("Professor Sajjad Login Matrix", 
                        f"✅ Access Granted!\n\n🔑 Active Cyber Sessions: {accounts_verified}")

# 🖥️ ساخت پنجره اصلی با تم دارک و بنفش سلطنتی
window = tk.Tk()
window.title("Sajjad's AI Auto-Login & Account Management System v1.0")
window.geometry("550x550")
window.configure(bg="#150E26")  # تم بنفش بسیار تیره و دارک

# عنوان بالای صفحه
title_label = tk.Label(window, text="🔑 AI AUTO-LOGIN SYSTEM", font=("Arial", 16, "bold"), fg="#D6C4FF", bg="#150E26")
title_label.pack(pady=15)

# دکمه بزرگ دودی خفن برای شلیک ورود خودکار
run_button = tk.Button(window, text="🚀 LAUNCH AUTO-LOGIN", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#3A3F47", activebackground="#2A2D32", activeforeground="#FFFFFF", width=25, height=2, command=start_auto_login)
run_button.pack(pady=10)

# متن وضعیت سیستم
status_label = tk.Label(window, text="🟢 Security Server Ready. Click Launch to Connect.", font=("Arial", 10), fg="#7A728A", bg="#150E26")
status_label.pack(pady=5)

# باکس مانیتورینگ متون
output_text = tk.Text(window, font=("Consolas", 10), fg="#A984FF", bg="#231A38", width=65, height=18, relief=tk.FLAT)
output_text.pack(pady=10)

window.mainloop()

