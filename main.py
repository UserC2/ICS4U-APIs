import json
import math
import matplotlib.pyplot as plt
import requests
import vector

print_debug = False

def try_request(request):
    try:
        return requests.get(request)
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# should check for file failure or invalid format
key_file = open("key", "r")
key = key_file.readlines()[0]
if print_debug:
    print(f"API Key: {key}")

latlong = try_request("https://ipinfo.io/loc")
if print_debug:
    print(f"Latitude & Longitude: {latlong.text}")

weather_request = try_request(f"https://api.weatherapi.com/v1/current.json?key={key}&q={latlong.text}&aqi=no")
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

if input("Show plot (Y/N)? ").lower().strip() == 'y':
    plotable_wind = wind.as_plotable().as_rect()
    plotable_disc = disc.as_plotable().as_rect()
    plotable_uncorrected = uncorrected.as_plotable().as_rect()
    v1 = plt.quiver(0, 0, plotable_wind[0], plotable_wind[1], color="b", label="Wind", angles="xy", scale_units="xy", scale=1)
    v2 = plt.quiver(0, 0, plotable_disc[0], plotable_disc[1], color="orange", label="Disc", angles="xy", scale_units="xy", scale=1)
    v3 = plt.quiver(0, 0, plotable_uncorrected[0], plotable_uncorrected[1], color="r", label="Uncorrected Path", angles="xy", scale_units="xy", scale=1)
    max = max(max(plotable_wind), max(plotable_disc), max(plotable_uncorrected))
    plt.xlim(-max, max)
    plt.ylim(-max, max)
    plt.legend()
    plt.show()

correction = disc.degrees - uncorrected.degrees
corrected_angle = disc.degrees + correction
print(f"Heading Correction: {correction:.1f}°")
print(f"Corrected Heading: {corrected_angle:.1f}°")