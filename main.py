import telebot
# ... بقية الـ imports

bot = telebot.TeleBot('8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw')

# هذا السطر يقتل أي اتصال قديم فوراً
bot.remove_webhook()

# ... ثم بقية الكود
