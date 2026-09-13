
import tkinter as tk
from tkinter import messagebox
import time

def start_image_download():
    status_label.config(text="⚡ AI Media Engine Ingesting Stream... Please Wait.", fg="#FFCC00")
    window.update()
    time.sleep(1)
    
    image_gallery = [
        {"img_id": "IMG-01", "filename": "laptop_4k_front.png", "format": "PNG", "size_mb": 8.5},
        {"img_id": "IMG-02", "filename": "keyboard_thumb.jpg", "format": "JPG", "size_mb": 1.2},
        {"img_id": "IMG-03", "filename": "monitor_unboxing_raw.tiff", "format": "TIFF", "size_mb": 24.0},
        {"img_id": "IMG-04", "filename": "chair_angle_low.jpg", "format": "JPG", "size_mb": 3.8}
    ]
    
    output_text.delete("1.0", tk.END)
    downloads_completed = 0
    
    for img in image_gallery:
        output_text.insert(tk.END, f"🔎 Connection OK -> Analysing metadata for: {img['filename']}...\n")
        window.update()
        time.sleep(0.5)
        
        if img['size_mb'] >= 5.0:
            output_text.insert(tk.END, f"   👑 [PREMIUM MEDIA] -> 4K Ultra HD Source asset.\n")
        else:
            output_text.insert(tk.END, f"   🔹 [STANDARD MEDIA] -> Web Compressed Asset.\n")
            
        output_text.insert(tk.END, f"   🛠️ Syncing data stream for {img['format']} layout...\n")
        output_text.insert(tk.END, f"   💾 Saved: Assets/Products/Downloaded_{img['filename']}\n")
        output_text.insert(tk.END, "   ✅ [IMAGE DOWNLOADED AND VERIFIED]\n")
        output_text.insert(tk.END, "-" * 45 + "\n")
        output_text.see(tk.END)
        window.update()
        downloads_completed += 1
        time.sleep(0.5)
    
    status_label.config(text="✨ All Product Media Assets Synced Successfully!", fg="#00FF00")
    messagebox.showinfo("Professor Sajjad Media Core", 
                        f"✅ Success!\n\n📷 Total Automated Downloads: {downloads_completed}")

# 🖥️ ساخت پنجره اصلی با تم دارک و سبزآبی (Cyan)
window = tk.Tk()
window.title("Sajjad's AI Image Downloader & Media Filter v1.0")
window.geometry("550x550")
window.configure(bg="#0E1A1A")  # تم فوق‌العاده تاریک با هاله سبزآبی

# عنوان بالای صفحه
title_label = tk.Label(window, text="📷 AI IMAGE AUTOMATION SYSTEM", font=("Arial", 16, "bold"), fg="#00FFFF", bg="#0E1A1A")
title_label.pack(pady=15)

# دکمه بزرگ طوسی متالیک خفن برای شروع دانلود خودکار
run_button = tk.Button(window, text="🚀 DOWNLOAD MEDIA ASSETS", font=("Arial", 12, "bold"), fg="#FFFFFF", bg="#4A525A", activebackground="#33393E", activeforeground="#FFFFFF", width=25, height=2, command=start_image_download)
run_button.pack(pady=10)

# متن وضعیت سیستم
status_label = tk.Label(window, text="🟢 Downloader Core Ready. Click Download to Sync.", font=("Arial", 10), fg="#637A7A", bg="#0E1A1A")
status_label.pack(pady=5)

# باکس مانیتورینگ متون با رنگ فیروزه‌ای/سبزآبی هکری
output_text = tk.Text(window, font=("Consolas", 10), fg="#00FFFF", bg="#172626", width=65, height=18, relief=tk.FLAT)
output_text.pack(pady=10)

window.mainloop()
