
import tkinter as tk
from tkinter import messagebox
import time

def start_email_dispatch():
    status_label.config(text="⚡ AI Email Core Dispatched... Please Wait.", fg="#FFCC00")
    window.update()
    time.sleep(1)
    
    client_database = [
        {"name": "Ehsan", "email": "ehsan@example.com", "status": "VIP", "balance": 0},
        {"name": "Ali", "email": "ali@example.com", "status": "Regular", "balance": 4500000},
        {"name": "Sara", "email": "sara@example.com", "status": "VIP", "balance": 12000000},
        {"name": "Nima", "email": "nima@example.com", "status": "Regular", "balance": 0}
    ]
    
    output_text.delete("1.0", tk.END)
    emails_sent = 0
    
    for client in client_database:
        output_text.insert(tk.END, f"🔎 Analysing stats for: {client['name']}...\n")
        window.update()
        time.sleep(0.5)
        
        if client['balance'] > 0:
            output_text.insert(tk.END, f"   ⚠️ [ALERT] Outstanding: {client['balance']:,} Toman\n")
        elif client['status'] == "VIP":
            output_text.insert(tk.END, f"   👑 [PREMIUM] VIP Client | Clear Balance.\n")
        else:
            output_text.insert(tk.END, f"   🔹 [STANDARD] Active Client | Clear Balance.\n")
            
        output_text.insert(tk.END, f"   📧 Dispatching Email to: {client['email']}...\n")
        output_text.insert(tk.END, "   ✅ [EMAIL DISPATCHED SUCCESSFULLY]\n")
        output_text.insert(tk.END, "-" * 45 + "\n")
        output_text.see(tk.END)
        window.update()
        emails_sent += 1
        time.sleep(0.5)
    
    status_label.config(text="📨 All Corporate Emails Dispatched!", fg="#00FF00")
    messagebox.showinfo("Professor Sajjad Email Core", 
                        f"✨ Success!\n\n📨 Total Automated Emails: {emails_sent}")

# 🖥️ ساخت پنجره اصلی با تم دارک
window = tk.Tk()
window.title("Sajjad's AI Email Dispatcher v1.0")
window.geometry("550x550")
window.configure(bg="#1E1E1E")

title_label = tk.Label(window, text="📬 AI EMAIL AUTOMATION CORE", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#1E1E1E")
title_label.pack(pady=15)

run_button = tk.Button(window, text="🚀 RUN EMAIL DISPATCHER", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#E51A4C", activebackground="#B3153B", activeforeground="#FFFFFF", width=25, height=2, command=start_email_dispatch)
run_button.pack(pady=10)

status_label = tk.Label(window, text="🟢 Mailer Engine Ready. Click Run to Start.", font=("Arial", 10), fg="#858585", bg="#1E1E1E")
status_label.pack(pady=5)

output_text = tk.Text(window, font=("Consolas", 10), fg="#00FF00", bg="#2D2D2D", width=65, height=18, relief=tk.FLAT)
output_text.pack(pady=10)

window.mainloop()
