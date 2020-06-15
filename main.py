from flask import Flask,jsonify
from weather.weather import weather
import json

app = Flask(__name__)
app.register_blueprint(weather,url_prefix="/weather")


@app.route("/help")
def help():
    with open("./json/instructions.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/")
def home():
    with open("./json/home.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"Error":"URL not found"}), 404

if __name__ == '__main__':
    app.run(debug = True)
