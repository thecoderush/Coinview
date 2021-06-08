import config, csv

from binance.client import Client 

client = Client(config.API_KEY, config.API_SECRET)


# get all symbol prices
# prices = client.get_all_tickers()

# # print(prices)
# for price in prices:
#   print(price)


# # csvfile = open('15minutes.csv', 'w', newline='')
# csvfile = open('2012-2020.csv', 'w', newline='')
# candlestick_writer = csv.writer(csvfile, delimiter=',')

# csvfile = open('daily.csv', 'w', newline='')
# csvfile = open('all_time_daily.csv', 'w', newline='')
csvfile = open('2020_15minutes.csv', 'w', newline='')
# csvfile = open('2021_15minutes.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')


# # get Kline/Candlesticks
# candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# for candlesticks in candles:
#   print(candlesticks)
#   candlestick_writer.writerow(candlesticks)


# fetch 5 minute klines interval for the 1st january of 2012 day to May 24th 2020
# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "24 May, 2020")

# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2021", "7 Jun, 2021")

# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2017", "7 Jun, 2021")

candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 Jan, 2020", "12 Jun, 2020")

# candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_15MINUTE, "1 May, 2020", "7 Jun, 2020")

# for candlestick in candlesticks:
#   candlestick_writer.writerow(candlesticks)

# csvfile.close()

# print(len(candles))

for candlestick in candlesticks:
    candlestick[0] = candlestick[0] / 1000
    candlestick_writer.writerow(candlestick)

csvfile.close()