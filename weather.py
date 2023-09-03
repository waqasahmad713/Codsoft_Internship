import requests
import os
from datetime import datetime

api_key = "9c2cf80b712337fad081ab45ec787751"
location = input("\nEnter the city name: ")

complete_api_link = (
    "https://api.openweathermap.org/data/2.5/weather?q="
    + location
    + ",pk&appid="
    + api_key
)
api_link = requests.get(complete_api_link)
api_data = api_link.json()

try:
    temp_city = (api_data["main"]["temp"]) - 273.15
    weather_desc = api_data["weather"][0]["description"]
    hmdt = api_data["main"]["humidity"]
    wind_spd = api_data["wind"]["speed"]
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    with open("weatherinfo.txt", "w+") as f:
        f.write("-------------------------------------------------------------\n")
        f.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
        f.write("-------------------------------------------------------------\n")
        f.write("\tCurrent temperature is : {:.2f} °C\n".format(temp_city))
        f.write("\tCurrent weather desc   : " + weather_desc + "\n")
        f.write("\tCurrent Humidity       : {} %\n".format(hmdt))
        f.write("\tCurrent wind speed     : {} km/h \n".format(wind_spd))
    print("Current temperature is: {:.2f} °C".format(temp_city))
    print("Current weather desc  : " + weather_desc)
    print("Current Humidity      :", hmdt, "%")
    print("Current wind speed    :", wind_spd, "km/h")

except KeyError:
    print("Enter a valid city")
