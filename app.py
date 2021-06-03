from flask import Flask, render_template, request, flash, redirect, jsonify
import config, csv
from binance.client import Client
from binance.enums import *

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8zn/.xec]/9fH*5@q8X'

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
    # print(exchange_info)

    return render_template('index.html', title=title, my_balances=balances, symbols=symbols)

@app.route("/buy", methods=['post'])
def buy():
    print(request.form)
    try:
        order = client.create_order(
            symbol=request.form['symbol'],
            side=SIDE_BUY,
            type=ORDER_TYPE_LIMIT,
            # timeInForce=TIME_IN_FORCE_GTC,
            quantity=request.form['quantity'],
            #price='0.00001'
        )
    except Exception as e:
        flash(e.message, "error")

    return redirect('/')

@app.route("/sell")
def sell():
    return "<p>sell</p>"

@app.route("/settings")
def settings():
    return "<p>settings</p>"


@app.route('/history')
def history():
    # candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "25 May, 2021", "1 Jun, 2021")
    candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "25 May, 2021", "1 Jun, 2021")

    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {
            "time": data[0] / 1000, 
            "open": data[1], 
            "high": data[2], 
            "low": data[3], 
            "close": data[4]
        }

        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)