import json
import math
import matplotlib.pyplot as plt
import requests
import vector

print_debug = False

# should check for file failure or invalid format
key_file = open("key", "r")
key = key_file.readlines()[0]
if print_debug:
    print(f"API Key: {key}")

# should check for request failure
latlong = requests.get("https://ipinfo.io/loc")
if print_debug:
    print(f"Latitude & Longitude: {latlong.text}")

# should check for request failure
weather_request = requests.get(f"https://api.weatherapi.com/v1/current.json?key={key}&q={latlong.text}&aqi=no")
if print_debug:
    print(f"Weather Request JSON:\n{weather_request.text}")

weather = json.loads(weather_request.text)
wind_kph = weather["current"]["wind_kph"]
wind_heading = weather["current"]["wind_degree"]
print(f"Wind Speed {wind_kph:.1f} KM/H, Wind Heading {wind_heading:.1f}°")

disc_kph = float(input("Enter Disk Speed KM/H: "))
disc_heading = float(input("Enter Compass Heading (°): "))

if print_debug:
    print(f"Disc Speed {disc_kph:.1f} KM/H, Disc Heading {disc_heading:.1f}°")

wind = vector.Vector(wind_kph, wind_heading)
disc = vector.Vector(disc_kph, disc_heading)
uncorrected = wind.add(disc)

# ask user if they want a visual before plotting
if False:
    rect_wind = wind.as_rect()
    rect_disc = disc.as_rect()
    rect_uncorrected = uncorrected.as_rect()
    plt.quiver([0, 0, 0], [0, 0, 0], [rect_wind[0], rect_disc[0], rect_uncorrected[0]], [rect_wind[1], rect_disc[1], rect_uncorrected[0]], color=["g", "r", "b"], angles="xy", scale_units="xy", scale=1)
    max = max(max(rect_wind), max(rect_disc), max(rect_uncorrected))
    plt.xlim(-max, max)
    plt.ylim(-max, max)
    plt.show()

uncorrected_angle = math.degrees(uncorrected.degrees)
disc_angle = math.degrees(disc.degrees)

correction = disc_angle - uncorrected_angle
corrected_angle = disc_angle + correction
print(f"Heading Correction: {correction:.1f}°")
print(f"Corrected Heading: {corrected_angle:.1f}°")