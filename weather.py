from pyowm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import config
from pyowm.utils import timestamps
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()


print( Fore.GREEN )
config_dict = get_default_config()
place = input(" Укажите город: ")
#api from openweathermap.org
owm = OWM('api', config_dict)
config_dict['language'] = 'ru'
mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather
temp = w.temperature('celsius')["temp"]


print(" В городе " + place + " сейчас " + str(w.detailed_status))
print(" температура " + str(temp))

if temp < 10:
    print (" Одевай шубу " )
elif temp < 20:
    print (" Одевай теплую одежду " )
else:
    print( "Одевай что угодно" )

input()