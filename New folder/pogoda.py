import pyowm

city = input('kakoj gorod interesujet? :')

owm = pyowm.OWM('51225eb0116354499cb3811aa3e68092')
mgr = owm.weather_manager()



observation = mgr.weather_at_place(city)
weather = observation.weather
w = observation.weather
temp = w.temperature('celsius')['temp']


print("temperatura " + str(temp) )

print("V ukazannom gorode " + weather.detailed_status )