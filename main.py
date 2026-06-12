import os
import telebot
from flask import Flask
import threading

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# هذا السطر ضروري جداً لإنهاء التضارب (Conflict 409)
bot.remove_webhook()

@app.route('/')
def home():
    return "Milaaf-ai is running!"

def start_bot():
    # استخدام infinity_polling للبوت
    bot.infinity_polling()

if __name__ == '__main__':
    # تشغيل البوت في خيط (Thread) منفصل
    threading.Thread(target=start_bot).start()
    
    # تشغيل الـ Flask لاستقبال طلبات الـ Port من Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
