import telebot
import pyowm

# подключения
owm = pyowm.OWM('5aa741a37ff6512516bcb3da3ea973f0' language = 'ru')
bot = telebot.TeleBot("5572774169:AAEZ-w-yQEe9xCIccRmNNuKmkJoaxan8ybk")

@bot.massage_handler(content_types=['text'])
def send_echo(massage):
	odservation = own.weather_at_place(massage.text )
	w = odservation.get_weather()
	temp = w.get_temperature ('celsius')["temp"]

	answer = "На улице города" + massage.text + "сейчас" + w.get_detailed_status() + "\n"
	answer += "Температура сейчас" + str(temp) + "\n\n"

	if temp < 10:
		answer += "сейчас очень холодно, надень куртку и шапку не забудь"
	elif temp < 20:
		 answer += "сейчас очень холодно, надень куртку"
	elif temp < 23:
		 answer += "сейчас достаточно прохладно, подумай надевать ли кофту"
	elif temp < 25:
		 answer += "сейчас замечательная погода, кайфуй"
	elif temp < 27:
		 answer += "сегодня будет жарковато думаю стоит надеть шорты"
	else:
		answer += "Будет жарко как в духовке готовся"
    

	bot.send_massage(message.chat.id, answer)

bot.polling( none_stop = True )

