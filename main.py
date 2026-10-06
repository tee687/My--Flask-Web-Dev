from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hi, my name is Tendai, a web dev!</h1>"

if __name__ == "__main__":
    app.run(debug=True)