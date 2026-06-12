import os
import telebot
from flask import Flask

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# هذا السطر هو "السر" الذي ينهي مشكلة الـ 409 Conflict
bot.remove_webhook()

@app.route('/')
def home():
    return "Milaaf-ai is running!"

if __name__ == '__main__':
    # البوت سيعمل الآن بدون تضارب
    # ملاحظة: إذا كنت تستخدم Render كـ Web Service، يجب أن يعمل الـ Flask 
    # في الخلفية، وسنستخدم الـ Polling.
    import threading
    def run_bot():
        bot.infinity_polling()
    
    threading.Thread(target=run_bot).start()
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
