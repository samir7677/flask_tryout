from flask import Flask
app = Flask(__name__)

@app.route("/")
def hallo():
    return"<p>welkom bij NHA!</p>"
