import os
import telebot
from flask import Flask, request

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# هذا المسار لاستقبال تحديثات تليجرام
@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    json_str = request.stream.read().decode('utf-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

# إجبار تليجرام على إلغاء أي اتصال قديم (وهو سبب الـ 409)
bot.remove_webhook()
bot.set_webhook(url='https://milaaf-ai-h1-nnec.onrender.com/' + TOKEN)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
