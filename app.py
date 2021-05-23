from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>The index page</p>"

@app.route("/buy")
def buy():
    return "<p>buy</p>"

@app.route("/sell")
def sell():
    return "<p>sell</p>"

@app.route("/settings")
def settings():
    return "<p>settings</p>"