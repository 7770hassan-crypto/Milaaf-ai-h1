from flask import Flask
from threading import Thread
import telebot # تأكد أن مكتبة pyTelegramBotAPI مثبتة

# --- السيرفر الوهمي لبقاء البوت نشطاً ---
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

# --- كود البوت الخاص بك ---
# ضع التوكن الخاص بك هنا بين علامتي التنصيص
API_TOKEN = '8692993746:AAG-A3Cp7jt-toEyC5a5kWrfe8FwyduXlF0'


bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك! ميلاف يعمل الآن بنجاح.")

# أي أوامر أخرى تضعها هنا...

# هذا السطر ضروري جداً ليعمل البوت باستمرار
bot.infinity_polling()
 
