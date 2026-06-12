import os
import telebot
from flask import Flask
import threading

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# نغلق أي ويب هوك قديم
bot.remove_webhook()

@app.route('/')
def home():
    return "Milaaf-ai is running!"

# دالة تشغيل البوت
def run_bot():
    print("البوت يبدأ الآن...")
    bot.infinity_polling(none_stop=True)

if __name__ == '__main__':
    # تشغيل البوت في الخلفية
    t = threading.Thread(target=run_bot)
    t.start()
    
    # تشغيل Flask على المنفذ الصحيح الذي يتوقعه رندر
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
