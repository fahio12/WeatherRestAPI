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


# always getting temperature from the day NOT NIGHT
def cityJson(city):
    # gets template and updates it with the data from the api
    template = getJson()
    cityData = getCityData(city)
    tempProperties = template["features"][0]["properties"]
    for properties in tempProperties:
        for (key,value) in cityData.items():
            if type(value) == dict:
                for segment in value:
                    if properties == segment :
                        tempProperties[properties] = value[segment]
            elif properties == key:
                tempProperties[properties] = value
    # exempt
    tempProperties["description"] = cityData["weather"][0]["description"]
    # lon and lat
    template["features"][0]["geometry"]["coordinates"][0] = cityData["coord"]["lon"]
    template["features"][0]["geometry"]["coordinates"][1] = cityData["coord"]["lat"]
    # update properties
    template["features"][0]["properties"] = tempProperties

    return template

cityJson("Madrid")
# print(cityJson("Miami"))
