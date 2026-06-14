import telebot
import os

# ضع التوكين الخاص بك هنا بين علامتي التنصيص
TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'

# إنشاء كائن البوت (هذا السطر هو الذي يحل مشكلة NameError)
bot = telebot.TeleBot(TOKEN)

# تنظيف أي اتصالات قديمة تسبب خطأ 409
bot.remove_webhook()

# تشغيل البوت
if __name__ == '__main__':
    print("البوت يعمل الآن يا أبا عامر...")
    bot.infinity_polling(none_stop=True, skip_pending=True)
