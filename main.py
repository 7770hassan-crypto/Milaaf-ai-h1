import telebot
from flask import Flask
import threading

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def home():
    return "Milaaf is running!"

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ميلاف يعمل الآن!")

# تشغيل البوت في الخلفية
def run_bot():
    bot.remove_webhook()
    bot.infinity_polling()

if __name__ == '__main__':
    # تشغيل البوت في خيط (Thread) منفصل
    threading.Thread(target=run_bot).start()
    # تشغيل سيرفر Flask لترضية رندر
    app.run(host='0.0.0.0', port=5000)
