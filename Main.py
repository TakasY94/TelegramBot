import telebot

bot = telebot.TeleBot("768815545:AAEX1cz0EKOmoW1CTDh9e51X7F6rbGa64-k")
id = "122730291"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(id, message.text)

bot.polling()