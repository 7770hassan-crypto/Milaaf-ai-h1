import telebot

# ضع هنا التوكن الخاص بك بين علامات التنصيص
TOKEN = '8692993746:AAG-A3Cp7jt-toEyC5a5kWrfe8FwyduXlF0
'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً يا أبا عامر، ميلاف جاهز للعمل!")

print("Milaaf AI is running...")
bot.infinity_polling()
