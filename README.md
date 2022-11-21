# Python_Exercise12
## 12. Using external interfaces

1. Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here: https://api.chucknorris.io/. 
The user should only be shown the joke text.
```python
import requests

request = "https://api.chucknorris.io/jokes/random"
result = requests.get(request).json()
print(result['value'])
```
Output console:
```
How long is a piece of strChuck Norris.
```
2. Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a program that asks the user 
for the name of a municipality and then prints out the corresponding weather condition description text and temperature in Celsius degrees. Take a good 
look at the API documentation. You must register for the service to receive the API key required for making API requests. Furthermore, find out 
how you can convert Kelvin degrees into Celsius.
```python
import requests

cityName = input("\nPlease enter a city name to know the weather: ")
request = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid=6b5e18c07f2ddb83b80e7aa7c04d5488"
result = requests.get(request).json()
fTemp = result['main']['temp']
celsius = round((fTemp - 273.15), 2)
#print(json.dumps(result, indent=2))
print('\nWeather condition is:',result['weather'][0]['main'])
print(f'Current temperature: {celsius} C')
```
Output console:
```
Please enter a city name to know the weather: espoo

Weather condition is: Clouds
Current temperature: -2.18 C
```
