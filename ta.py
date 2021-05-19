# All the following use the function API:
import numpy
import talib

close = numpy.random.random(100)

print(close)

#Calculate a simple moving average of the close prices:
moving_average = talib.SMA(close, timeperiod=10)

print(moving_average)