import os
import telebot
from flask import Flask
import threading

# هذا هو التوكين الخاص بك
TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# هذا السطر هو الأهم: يمسح أي اتصال سابق بتليجرام
bot.remove_webhook()

@app.route('/')
def home():
    return "Milaaf-ai is running!"

def start_bot():
    # هنا تم إضافة الإعدادات التي تمنع التداخل
    bot.infinity_polling(none_stop=True, interval=0, timeout=20)

if __name__ == '__main__':
    # تشغيل البوت في الخلفية
    threading.Thread(target=start_bot).start()
    # تشغيل السيرفر ليستقبل طلبات رندر
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
