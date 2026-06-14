# بدلاً من تشغيله بالطريقة العادية، استخدم هذا الكود:
if __name__ == '__main__':
    # هذا السطر يقتل أي اتصال قديم معلق بتليجرام
    bot.remove_webhook()
    
    # skip_pending=True هي التي ستنهي الـ 409
    bot.infinity_polling(none_stop=True, skip_pending=True)
