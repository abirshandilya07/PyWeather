import requests, json

api_key = "b53dbe23ace0c6f581504bdce13741f7"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

	y = x["main"]

	current_temperature = y["temp"]
	celsius_temp = current_temperature - 273
	celsius_temp = round(celsius_temp, 2)

	current_pressure = y["pressure"]

	current_humidiy = y["humidity"]

	z = x["weather"]

	weather_description = z[0]["description"]

	print(" Temperature (in celsius) = " +
					str(celsius_temp) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description))

else:
	print(" City Not Found ")
