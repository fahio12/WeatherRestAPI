from flask import Flask,jsonify
from weather.weather import weather

app = Flask(__name__)
app.register_blueprint(weather,url_prefix="/weather")


@app.route("/")
def hello():
    return jsonify({"about":"Hello world"})
@app.route("/bye")
def bye():
    return jsonify({"about":"Bye world"})

if __name__ == '__main__':
    app.run(debug = True)
