import telebot

# التوكن الخاص بك
TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)

# ترحيب عند بدء البوت
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "أهلاً بك يا أبا عامر في ميلاف AI. أنا جاهز للخدمة!")

# رد تلقائي على أي رسالة
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "أبشر، وصلتني رسالتك يا أبا عامر، سأعالجها قريباً.")

print("البوت يعمل الآن...")
bot.infinity_polling() 
