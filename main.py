import telebot

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً يا أبا عامر، ميلاف جاهز للعمل!")

print("Milaaf AI is running...")
bot.infinity_polling()
