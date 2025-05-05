from flask import flask
app = flask(__name__)

@app.rout("/")
def hallo():
    return"<p>halloworld!</p>"
