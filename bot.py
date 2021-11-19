import telebot
import conf

bot = telebot.TeleBot(conf.KEY)

@bot.message_handler(content_types=['text'])
def get_messages(message):

    if message.text == "/create":
        bot.send_message(message.from_user.id, f"create")

    elif message.text == "/read":
        bot.send_message(message.from_user.id, "read")

    elif message.text == "/update":
        bot.send_message(message.from_user.id, "update")

    elif message.text == "/delete":
        bot.send_message(message.from_user.id, "delete")

    
    elif message.text == "/help":
        bot.send_message(message.from_user.id,
                         "/create, /read, /update, /delete")

    else:
        bot.send_message(message.from_user.id, "use /help.")


bot.polling(none_stop=True, interval=0)
