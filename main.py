import telebot
import os

TOKEN = '8692993746:AAFNiVzogov6a7KJUHzRkpiBUffh-GXZenw'
bot = telebot.TeleBot(TOKEN)

# هذا السطر هو الحل السحري لمشكلة الـ 409
# يقوم بمسح أي "ويب هوك" أو اتصال قديم عالق قبل البدء
bot.remove_webhook()

# ثم كمل كود البوت الخاص بك هنا...
