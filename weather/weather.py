from flask import Blueprint,jsonify,request
from weather import helper

weather = Blueprint("weather",__name__)

@weather.route("/")
def home():
    return jsonify({"about":"Welcome to the weather api add a city to get results"})

@weather.route("/<city>")
def city(city):
    try:
        unit = request.args['unit']
    except KeyError as e:
        unit = "imperial"
    data = helper.cityJson(city,unit)
    return jsonify(data)
