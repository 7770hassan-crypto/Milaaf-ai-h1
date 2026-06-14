import telebot
import os

# 1. أولاً: تعريف التوكين (تأكد أنك وضعته في Environment Variables في رندر)
TOKEN = os.getenv('TOKEN') 

# 2. ثانياً: إنشاء كائن البوت (هنا يتم تعريف 'bot')
bot = telebot.TeleBot(TOKEN)

# 3. ثالثاً: الآن يمكنك استخدام 'bot'
bot.remove_webhook()

# 4. رابعاً: تشغيل البوت
if __name__ == '__main__':
    bot.infinity_polling(none_stop=True, skip_pending=True)
