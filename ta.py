# All the following use the function API:
import numpy
import talib
from numpy import genfromtxt

my_data = genfromtxt('15minutes.csv', delimiter=',')

print(my_data)

close = my_data[:,4]

print(close)

# close = numpy.random.random(100)

# print(close)

# #Calculate a simple moving average of the close prices:
# moving_average = talib.SMA(close, timeperiod=10)

# print(moving_average)

# rsi = talib.RSI(close, timeperiod=14)

# print(rsi)

rsi = talib.RSI(close)

print(rsi)