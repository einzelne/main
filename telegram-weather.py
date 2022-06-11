from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language']="ru"
import telebot

# api openweathermap.org
owm = OWM('api')
# api telegram
bot = telebot.TeleBot('api')


@bot.message_handler(content_types=['text'])
def send_echo(message):
	mgr = owm.weather_manager()
	observation = mgr.weather_at_place(message.text)
	w = observation.weather
	temp = w.temperature('celsius')["temp"]


	answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
	answer += "Температура в районе " + str(temp) + "\n\n"

	if temp < 10:
		answer += "Одевай шубу "
	elif temp < 20:
		answer += "Одевай теплую одежду "
	else:
		answer += "Одевай что угодно "

	bot.send_message(message.chat.id, answer)

bot.infinity_polling()

