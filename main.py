import telebot
from flask import Flask
from threading import Thread

# --- إعداد السيرفر الوهمي ---
app = Flask('')
@app.route('/')
def home():
    return "Milaaf AI is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

keep_alive()

# --- إعداد البوت ---
API_TOKEN = '8692993746:AAG-A3Cp7jt-toEyC5a5kWrfe8FwyduXlF0'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً يا أبا عامر! البوت يعمل الآن بشكل ممتاز.")

# --- التشغيل ---
if __name__ == "__main__":
    bot.infinity_polling()
 
