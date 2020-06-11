from flask import Blueprint,jsonify
from weather import helper

weather = Blueprint("weather",__name__)

@weather.route("/")
def home():
    return jsonify({"about":"Welcome to the weather api"})

@weather.route("/<city>")
def city(city):
    return jsonify({"city":city})
