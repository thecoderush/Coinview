from flask import Flask, render_template
import config, csv
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

client = Client(config.API_KEY, config.API_SECRET)

@app.route("/")
def index():

    title = 'CoinView'

    account = client.get_account()

    balances = account['balances']

    exchange_info = client.get_exchange_info()

    symbols = exchange_info['symbols']

    # print(client)
    # print(account)
    # print(balances)
    print(exchange_info)

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

@app.route("/buy", methods=['post'])
def buy():
    order = client.create_order(
        symbol='LTC',
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=0.3,
        #price='0.00001'
        )

    return "<p>buy</p>"

@app.route("/sell")
def sell():
    return "<p>sell</p>"

@app.route("/settings")
def settings():
    return "<p>settings</p>"