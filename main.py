import os
import telebot
from flask import Flask, request

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
URL = 'https://milaaf-ai-h1-nnec.onrender.com' # هذا رابطك في رندر

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# هذا المسار يستقبل الرسائل من تليجرام فور وصولها
@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_str = request.stream.read().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "ميلاف يعمل الآن عبر الويب هوك!")

if __name__ == '__main__':
    # 1. نحذف أي اتصال قديم (عشان الـ 409)
    bot.remove_webhook()
    # 2. نحدد الرابط الجديد
    bot.set_webhook(url=URL + '/' + TOKEN)
    # 3. نشغل السيرفر
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
