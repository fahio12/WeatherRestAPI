from flask import Blueprint,jsonify,request
from weather import helper

weather = Blueprint("weather",__name__)

@weather.route("/")
def home():
    return jsonify({"about":"Welcome to the weather api"})

@weather.route("/<city>")
def city(city):
    unit = request.args['unit']
    data = helper.cityJson(city,unit)
    return jsonify(data)
