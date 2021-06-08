import backtrader as bt
import datetime

class RSIStrategy(bt.Strategy):

    def __init__(self):
        self.rsi = bt.talib.RSI(self.data, period=14)
    
    def next(self):
        if self.rsi < 20 and not self.position:
            self.buy(size=1)

        if self.rsi > 80 and self.position:
            self.close()

        # if self.rsi > 70 and not self.position:
        #     self.buy(size=1)
        
        # if self.rsi < 30 and self.position:
        #     self.close


cerebro = bt.Cerebro()

fromdate = datetime.datetime.strptime('2020-06-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2020-06-12', '%Y-%m-%d')

# data = bt.feeds.GenericCSVData(dataname='daily.csv', dtformat=2)
# data = bt.feeds.GenericCSVData(dataname='2020_15minutes.csv', dtformat=2)
data = bt.feeds.GenericCSVData(dataname='2020_15minutes.csv', dtformat=2, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)


cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)
 
cerebro.run()

cerebro.plot()