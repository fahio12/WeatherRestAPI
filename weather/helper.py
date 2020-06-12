import json
import requests

API_KEY = "7d3cfc90f1c59c1c1d4ea25b4116156c"
API_SITE = "http://api.openweathermap.org/data/2.5/weather?"
# make units dinamic
API = f"{API_SITE}appid={API_KEY}&units=imperial&q="


def getJson():
    with open("../json/example.json") as f:
        data = json.load(f)
    return data

# fix l8er
def getCityData(city):
    data = requests.get(API+city).json()
    return data

# get long and lat FUTURE

# always getting temperature from the day NOT NIGHT
def cityJson(city):

    template = getJson()
    cityData = getCityData(city)
    tempProperties = template["features"][0]["properties"]
    print(cityData["main"])
    # for property in tempProperties:
    #     for segment in cityData:
    #         property = ci
    #     print(property)
        # property = cityData[property]

    print(template["features"][0]["properties"])
cityJson("Miami")
# print(cityJson("Miami"))
