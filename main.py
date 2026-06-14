import telebot
import os

# التوكين هنا (ضع التوكين الجديد)
TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'

# تعريف البوت
bot = telebot.TeleBot(TOKEN)

# إيقاف أي تداخل في الاتصال
bot.remove_webhook()

# تشغيل البوت مع ضمان عدم التكرار
if __name__ == '__main__':
    print("البوت جاهز للعمل")
    bot.infinity_polling(none_stop=True, skip_pending=True)
