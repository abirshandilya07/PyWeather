# PyWeather
This project uses OpenWeatherMap's free API to get the weather of any city given by the user 
---
This project uses 2 modules:
1. requests
2. json

OpenWeatherMap's API can only be accessed by creating a free account here: https://home.openweathermap.org/users/sign_up 
If you create the account successfully you will get an API key on your gmail and then you can start using this API
So lets jump on the code part..
```
import requests, json

api_key = "YOUR API KEY HERE"

base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter city name : ")

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()
```
In the above code block we first import the libraries requests, json and then specify the api key..
The base url to use the api in specified and then we can add on to it by using our api_key and the city name which the user provides through the input() function then we go to the compplete url and get the results in a variable x
```
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
 ```
 In this code block we check for the 404 error page and get the atmospheric pressure, humidity, temperature which convert in celsius and then print the results
 
 
```
else:
	print(" City Not Found ")
```
And if the error page comes then the print City not found 
