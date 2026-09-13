
import tkinter as tk
from tkinter import messagebox
import time

def start_web_scraping():
    status_label.config(text="⚡ AI Cloud Scraper Engine Initializing... Please Wait.", fg="#FFCC00")
    window.update()
    time.sleep(1)
    
    scraped_products = [
        {"id": "PROD-99", "name": "AI Automation System Laptop", "market_price": 45000000, "competitor_price": 38000000},
        {"id": "PROD-102", "name": "Premium mechanical Keyboard", "market_price": 3500000, "competitor_price": 3400000},
        {"id": "PROD-105", "name": "4K UltraSharp Developer Monitor", "market_price": 28000000, "competitor_price": 19500000},
        {"id": "PROD-110", "name": "Ergonomic Engineering Chair", "market_price": 8500000, "competitor_price": 8200000}
    ]
    
    output_text.delete("1.0", tk.END)
    items_processed = 0
    
    for product in scraped_products:
        output_text.insert(tk.END, f"🔎 Connection established -> Extracting HTML from: {product['name']}...\n")
        window.update()
        time.sleep(0.5)
        
        price_diff = product['market_price'] - product['competitor_price']
        
        if price_diff >= 3000000:
            output_text.insert(tk.END, f"   🔥 [MEGA DISCOUNT DETECTED] -> Profit Opportunity!\n")
            output_text.insert(tk.END, f"   💰 Competitor Price Dropped by: {price_diff:,} Toman\n")
        else:
            output_text.insert(tk.END, f"   🔹 [STANDARD PRICE] -> Stable Market Value.\n")
            
        output_text.insert(tk.END, f"   📊 Market: {product['market_price']:,} | Competitor: {product['competitor_price']:,}\n")
        output_text.insert(tk.END, "   ✅ [DATA EXTRACTION TERMINATED WITH SUCCESS]\n")
        output_text.insert(tk.END, "-" * 45 + "\n")
        output_text.see(tk.END)
        window.update()
        items_processed += 1
        time.sleep(0.5)
    
    status_label.config(text="✨ Web Scraping & Market Analysis Finished!", fg="#00FF00")
    messagebox.showinfo("Professor Sajjad Scraper Core", 
                        f"✅ Success!\n\n📂 Total Products Tracked: {items_processed}")

# 🖥️ ساخت پنجره اصلی با تم دارک و لوکس
window = tk.Tk()
window.title("Sajjad's AI Web Scraper & Price Monitor v1.0")
window.geometry("550x550")
window.configure(bg="#1E1E1E")

title_label = tk.Label(window, text="🌐 AI WEB DATA SCRAPER", font=("Arial", 16, "bold"), fg="#FFFFFF", bg="#1E1E1E")
title_label.pack(pady=15)

# دکمه بزرگ فیروزه‌ای شیک برای حس مدرن و هکری
run_button = tk.Button(window, text="🚀 LAUNCH WEB SCRAPER", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#00A3A3", activebackground="#007A7A", activeforeground="#FFFFFF", width=25, height=2, command=start_web_scraping)
run_button.pack(pady=10)

status_label = tk.Label(window, text="🟢 Scraper Core Ready. Click Launch to Scan Web.", font=("Arial", 10), fg="#858585", bg="#1E1E1E")
status_label.pack(pady=5)

# باکس مانیتورینگ با رنگ سبز فسفری
output_text = tk.Text(window, font=("Consolas", 10), fg="#39FF14", bg="#2D2D2D", width=65, height=18, relief=tk.FLAT)
output_text.pack(pady=10)

window.mainloop()

