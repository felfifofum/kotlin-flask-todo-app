from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'this is the home page'

@app.route("/add", methods=["POST"])
def debug():
    text = request.form["sample"]
    print(text)
    return "received"

@app.route("/complete", methods=["POST"])
def debug():
    text = request.form["sample"]
    print(text)
    return "received"

@app.route("/delete", methods=["POST"])
def debug():
    text = request.form["sample"]
    print(text)
    return "received"

if __name__ == "__main__":
    app.run(debug=True)