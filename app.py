from flask import Flask, render_template
import config, csv
from binance.client import Client

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET)

@app.route("/")
def index():
    # return "<p>The index page</p>"
    title = 'CoinView'

    info = client.get_account()

    balances = info['balances']

    # print(client)
    print(info)
    print(balances)

    return render_template('index.html', title=title, my_balances=balances)

@app.route("/buy")
def buy():
    return "<p>buy</p>"

@app.route("/sell")
def sell():
    return "<p>sell</p>"

@app.route("/settings")
def settings():
    return "<p>settings</p>"