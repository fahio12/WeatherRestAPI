from flask import Blueprint,jsonify

weather = Blueprint("weather",__name__)

@weather.route("/")
def home():
    return jsonify({"about":"Welcome to the weather api"})
