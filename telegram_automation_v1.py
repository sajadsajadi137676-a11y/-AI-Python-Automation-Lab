

import time
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# توکن طلایی سجاد
BOT_TOKEN = "8800340919:AAF59Nk86DLSLpTCpijbvZDTF6GKeP5gVdE"

print("🚀 Sajjad's AI Telegram Bot is starting up...")

# ۱. دستور /start وقتی مشتری وارد ربات می‌شود
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.from_user.first_name
    await update.message.reply_text(f"Hello {user_name}! Welcome to AI Customer Support. How can I help you today?")

# ۲. خواندن پیام مشتری در تلگرام و تحلیل لحن
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    print(f"📩 New Message from customer: {user_message}")
    
    angry_keywords = ["broken", "late", "bad", "worst", "angry", "delay"]
    is_angry = any(word in user_message.lower() for word in angry_keywords)
    
    if is_angry:
        ai_reply = "⚠️ Status: CRITICAL\nDear Customer, we sincerely apologize! Our manager has been notified and will contact you immediately."
    else:
        ai_reply = "✅ Status: NORMAL\nThank you for your message. We have successfully received your inquiry!"
        
    await update.message.reply_text(ai_reply)
    print("✨ AI response sent back to Telegram successfully.")

if __name__ == '__main__':
    # ساخت برنامه ربات با روش استاندارد و بدون تداخل آدرس
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🟢 Bot is Online! Waiting for customer messages...")
    
    while True:
        try:
            app.run_polling(close_loop=False, timeout=20)
        except Exception as e:
            print("🔄 Reconnecting to Telegram server...")
            time.sleep(3)
