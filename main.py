import requests

# should check for file failure or invalid format
key_file = open("key", "r")
key = key_file.readlines()[0]
# print(key)

# should check for request failure
latlong = requests.get("https://ipinfo.io/loc")
print(latlong.text)

# should check for request failure
weather = requests.get(f"https://api.weatherapi.com/v1/current.json?key={key}&q={latlong.text}&aqi=no")
print(weather.text)