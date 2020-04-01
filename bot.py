import telebot

bot =  telebot.TeleBot("1057152705:AAGVuAgE5GpsiIkBLI78FxyavtJhVxyVQB4")

@bot.message_handler( commands= ['start', ' help'])
def send_welcome( message):
 bot.reply_to(message, "Привет "chat_id"! Я Бот-Эхо!")

@bot.message_handler( func= lambda message: True)
def echo_all( message):
 bot.reply_to(message, message.text)

bot.polling(none_stop=True, interval=0)
