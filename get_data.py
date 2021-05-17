import config, csv

from binance.client import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

client = Client(config.API_KEY, config.API_SECRET)

# get all symbol prices
# prices = client.get_all_tickers()

# # print(prices)
# for price in prices:
#   print(price)

# csvfile = open('15minutes.csv', 'w', newline='')
csvfile = open('2012-2020.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# get Kline/Candlesticks
candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

# for candlesticks in candles:
#   print(candlesticks)

#   candlestick_writer.writerow(candlesticks)

# fetch 1 minute klines for the last day up until now
candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "24 May, 2020")

for candlestick in candlesticks:
  candlestick_writer.writerow(candlesticks)

csvfile.close()

print(len(candles))