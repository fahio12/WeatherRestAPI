import json

def getJson():
    with open("../json/example.json") as f:
        data = json.load(f)
    return data

# fix l8er
def getCityData(city):
    data = "str(data)"
    return data

# get long and lat FUTURE

# always getting temperature from the day NOT NIGHT
def cityJson(city):

    template = getJson()
    cityData = getCityData(city)
    tempProperties = template["features"][0]["properties"]
    print(type(cityData))
    print(cityData)
    for property in tempProperties:
        print(cityData[property])
        # property = cityData[property]

    print(template["features"][0]["properties"])
cityJson("Havana")
# print(cityJson("Miami"))
