
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Hello World!"

@app.route("/greeting")
def greeting():
    name = request.args.get("name", "????")
    return f"Hello Hello {name}!"

@app.route("/data.json")
def data():
    return {
        "data": [1, 2, 3],
        "status": "good",
    }

if __name__ == "__main__":
    # by default runs at http://127.0.0.1:5000/
    app.run()
