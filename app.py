from flask import Flask, render_template, request, jsonify
from chat import get_response, predict_class, intents

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chat():
    msg = request.json.get("message")
    ints = predict_class(msg)
    res = get_response(ints, intents)
    return jsonify({"response": res})

if __name__ == "__main__":
    app.run(debug=True)