from flask import Flask,jsonify
app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify({"about":"Hello world"})
@app.route("/bye")
def bye():
    return jsonify({"about":"Bye world"})

if __name__ == '__main__':
    app.run(debug = True)
