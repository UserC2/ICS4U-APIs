import json
import requests

# should check for file failure or invalid format
key_file = open("key", "r")
key = key_file.readlines()[0]
# print(key)

# should check for request failure
latlong = requests.get("https://ipinfo.io/loc")
# print(latlong.text)

# should check for request failure
weather_request = requests.get(f"https://api.weatherapi.com/v1/current.json?key={key}&q={latlong.text}&aqi=no")
# print(weather_request.text)

weather = json.loads(weather_request.text)
wind_kph = weather["current"]["wind_kph"]
wind_heading = weather["current"]["wind_degree"]
print(f"Wind Speed KM/H {wind_kph}, Wind Heading {wind_heading}°")