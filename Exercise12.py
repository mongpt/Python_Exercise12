

#12.1
import json
import requests

request = "https://api.chucknorris.io/jokes/random"
result = requests.get(request).json()
print(result['value'])

#12.2
import json
import requests

cityName = input("\nPlease enter a city name to know the weather: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid=6b5e18c07f2ddb83b80e7aa7c04d5488"
result = requests.get(request).json()
fTemp = result['main']['temp']
celsius = round((fTemp - 273.15), 2)
#print(json.dumps(result, indent=2))
print('\nWeather condition is:',result['weather'][0]['main'])
print(f'Current temperature: {celsius} C')
