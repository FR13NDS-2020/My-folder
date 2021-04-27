from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. russkij
owm = OWM('51225eb0116354499cb3811aa3e68092', config_dict)
city = input('kakoj gorod interesujet? :')
mgr = owm.weather_manager()



observation = mgr.weather_at_place(city)
weather = observation.weather
w = observation.weather
temp = w.temperature('celsius')['temp']


print("temperatura " + str(temp) )

print("V ukazannom gorode " + weather.detailed_status )