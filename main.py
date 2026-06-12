import os
import telebot
from flask import Flask
import threading

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# هذا السطر يقتل أي اتصال قديم فوراً
bot.remove_webhook()

@app.route('/')
def home():
    return "Milaaf-ai is running!"

def start_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    # تشغيل البوت في مسار منفصل
    threading.Thread(target=start_bot).start()
    # تشغيل Flask ليستقبل اتصالات رندر (يمنع خطأ No open ports)
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
