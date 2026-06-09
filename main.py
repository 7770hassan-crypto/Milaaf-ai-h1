import os
import telebot
from flask import Flask
from threading import Thread

# هذا الجزء يفتح منفذ (Port) ليرضي Render
app = Flask('')

@app.route('/')
def home():
    return "Milaaf AI is running!"

def run():
    # Render يخصص دائماً متغير اسمه PORT، نستخدمه هنا
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

# تشغيل السيرفر في الخلفية
t = Thread(target=run)
t.start()

# --- كود البوت ---
API_TOKEN = '8692993746:AAG-A3Cp7jt-toEyC5a5kWrfe8FwyduXlF0' 
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً يا أبا عامر! ميلاف يعمل الآن بنجاح.")

# تشغيل البوت
bot.infinity_polling()
