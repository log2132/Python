import telebot

bot = telebot.TeleBot("5572774169:AAEZ-w-yQEe9xCIccRmNNuKmkJoaxan8ybk")

@bot.massage_handler(content_types=['text'])
def send_echo(massage):
	bot.send_message(massage.shat.id, massage.text)

bot.polling( none_stop = True )