import telebot
TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "منصة ميلاف جاهزة ومستعدة للعمل!")

print("البوت يعمل الآن...")
bot.infinity_polling()
