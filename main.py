import json
import math
import matplotlib.pyplot as plt
import requests

# move to seperate file for organization
def to_rect(r, angle):
    angle = math.radians(angle)
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    return [x, y]

def add_vect(a, b):
    x = a[0] + b[0]
    y = a[1] + b[1]
    return [x, y]

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
print(f"Wind Speed {wind_kph:.1f} KM/H, Wind Heading {wind_heading:.1f}°")

disc_kph = float(input("Enter Disk Speed KM/H: "))
disc_heading = float(input("Enter Compass Heading (°): "))

# print(f"Disc Speed {disc_kph:.1f} KM/H, Disc Heading {disc_heading:.1f}°")

wind = to_rect(wind_kph, wind_heading)
disc = to_rect(disc_kph, disc_heading)
uncorrected = add_vect(disc, wind)

if False:
    plt.quiver([0, 0, 0], [0, 0, 0], [wind[0], disc[0], uncorrected[0]], [wind[1], disc[1], uncorrected[0]], color=["g", "r", "b"], angles="xy", scale_units="xy", scale=1)
    max = max(max(wind), max(disc), max(uncorrected))
    plt.xlim(-max, max)
    plt.ylim(-max, max)
    plt.show()

uncorrected_angle = math.degrees(math.atan2(uncorrected[1], uncorrected[0]))
disc_angle = math.degrees(math.atan2(disc[1], disc[0]))

correction = disc_angle - uncorrected_angle
corrected_angle = disc_angle + correction
print(f"Heading Correction: {correction:.1f}°")
print(f"Corrected Heading: {corrected_angle:.1f}°")