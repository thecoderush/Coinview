By
Part Time Larry

https://www.youtube.com/watch?v=rvhnz1yBHgQ

Binance API Tutorial (Part 1) - Crypto Trading Bot Design - Jun 20, 2020

Hey everyone and welcome back to another video 
Today I'm going to be discussing cryptocurrency 
Now I'm not typically a crypto trader I only bought it a couple times in my life but 
I'm getting more and more request to cover Binance specifically whenever I'm covering topics like websockets and trading bot. There're a lot of crypto traders out there, they're interested
in (applying) technical analysis and some of the same technics I'm covering on this channel.
I'm currently apply it to stocks and options but a lot of people are intersted in trading crypto, so I thought I will give it a try today and hopefully learn something in the process myself. So, it's about ten thiry eleven AM on sunday moring and yeah, one thing I like about cryptos is that the market is always open So while I'm making this video I can actually get real time data whenever I want. So, the reason I'm making this particular video is (search) been request on the youtube video I posted, so, there's a form, if you have any other request discuss on Hackingthemarket.com if you have anything you want to ask or a request just for this videos, please make an account here and sign up because I'm just getting more and more emails and direct messages on Twitter email and Youtube and I just need to get them all in one place, and also I think it's better to not have all this conversation privately, I want to have a public forum that way it stock (?) for the entire community because that's the goal of this channel. So, since I've been noticing a lot of request for Binance I thought I would sign up for an account and check it out. So, let's talk about it. So, I created a Binance account recently and I deposit a wapping eight dollars and ninety three cents into the account so, you know it's not a lot of money right but it's you know the price of a few cups of coffee, you can learn some lessons you know trade this eight dollars around and let's see how we can make happen alright?
So I have this account here and what are we gonna do so I've outlined the topic So I thought about what can I build with this thing in about a day and I thought I would do another multi-part series where we build a kind of a full stack Tradingview-like platform. It's going to be a very simple and lightweight. Obviously Tradingview has tons of features but I thought a hook-up a frontend and a backend and fullfill some of the other request I'm getting. A lot of people want to see a fullstack example and also want to see things like TAlib wich is a technical analysis library and so I thought I will hook that up as well. And so I'm going to do a quick rundown before I get into the code of the entire project we're getting to beb building. So I have writeness down in an markdown file and this is the start of the repository I'm going to be making for this lesson So here a quick guideline right So we have a part one so for this first video when I get started () talk about what this Binance is and how it compares to other exchanges. Honeslty I don't know how to compare to other exchanges I bought crypto on Coinbase a few times and that's it. But It seems like Binance is the leading cryptocurrency exchange and I think the fees are probably lower and so a part of making this video is I learn about it myself right. And one of the reason I mention before why I want to learn more about crypto is that the market is always open I can build a lot of this demos apply to crypto when I have free time a lot time () some nights and weekend It's good to use cryptos becasue I always get a real time data right. So the first thing I'm going to do is so you how to connect to Binance websockets and get a bunch of incoming data in real-time using websockets both from the command line and I'm also show you how to do it using Python. I'm going to show you how to capture these data to a file and then we're going to also visualize that data with a frontend using Javascript. And I going to be using this library calls Lightweight Charts and Tradingview actually open sourced a charting library so it's very powerful and it's very specific unlike other charts library out there for the web this one is very specific to a financial data so you get a lot of that power of a site like Tradingview So you can do things like building this candlesticks charts (there's) custom themes, you can watermark the charts and add more advanced features, they have different price (scales) and you can do this real-time data emulation. So I'm going to show you how to visualize the websocket data in real-time. And maybe we're going to add it some overlays and some of the indicators and so forth. So very powerful charting library we're going to use here, and I'm going show you how to get Binance data from websockets and display a real-time candlestick charts on the web right. So the second thing we're going to do is try to hook up some technical analysis indicators to this and it's been a lot of request I'll cover which is TAlib is a library for technical analysis and so what I want to do is on the UI on the web as similar as a site like Tradingview I want to be able to check and say I'm interested in a particualr indicator so as such RSI, and I also want to use Python to analyse the candlestick that are coming in and check oin particular indicators so let's say we want to check wether a cryptocurrency is overbought or oversold, or we want to do something with Ballanger bands and so forth any of the number of the indicators that are available, and TAlib. I'm also going to write a lib that the websocket to a CSV file capture for anaylsis, and also I'm going to try downloading some historical data using the Binance REST API wich I haven't explore yet so I'm going to learn this as I go. And then we're going to apply some TALib to historical cryptocurrency data right.
The third thing we're going to do is I've cover 'Backtrader' which is a backtesting framework in the past I'll apply to stocks but I'm going to attend to apply Backtrader to cryptocurrency and it's looks like Backtrader actually has a TAlib indicators a way to integrate thlose indicators into Backtrader in addition to the indicators that Backtrader itself has, and so what I want to do is get this historical data set of historical data that I download using the REST API or capture from websockets and I want to apply Backtrader and TAlib indicators to that historical data set and test some different strategies using those indicators and (plot) some nice looking charts (bind self) entry points and see how much an account (balance) would have grown if we apply a particular strategy  historically. So one we're satisfy with those results we're going to actually try to hook this all up and see if we can build an API that hooks the frontend, javascvript part and saved the settings for our charts and our notification settings so what I'll do here is to create a few endpoints or either use (ADBS) (challes) to do a serverless backend or I might use 'Flask' which is popular as well So I'm going to build a WEB API for this charting framework we're building and we're going to save some (learning) and indicators settings as similar as how you do in Tradingview and then we're going to have some Python code process the (US) sockets the websockets data from Binance and when we detect any of the indicators that the user is interseted in () we'll actually call an API endpoint that execute a buy order, we'll aslo process the notification settings and send an email or text notification.
And then to wrap it all up in the final video I'll just () as we go () I'm going to think to some ideas that we can add to the web UI so we're going to add some orders history or intersting visualization to the web UI and make some improvments and just wrap it up and have a conclusion so I think it's going to be five part series it may grow or be a little less depending on how much I get down so yeah it's eleven AM I'm going to do a couple of videos now and then take a break for a bit maybe I'll do an update in the middle () I try something different with this series I filming in outdoors in the backyard at this moment because you know it's a nice sunny day, the weather's nice in San-Franscico so I thought I'll do some outdoors and also maybe take along with me do a walk real quick take a break and then come back and then finish the video at night. So yeah that's what we're making fall along with me I'm going to be posting this source code in the github repository wich is at github.com/hackingthemarkets and there also hackingthemarket's discussion forum if you want to join the discussion and also make sure you follow me on Youtube or Twitter and the name is @PartTimeLarry and yeah follow along and we're going to continue building things and growing this community and you () ahead so thanks for watching and stay tune next video we're going to started in and jumping around 

https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md

wss://stream.binance.com:9443
wss://stream.binance.com:9443/ws/btcusdt@trade

https://www.unixtimestamp.com/

Offcial docs for binance APIS and Streams
https://github.com/binance/binance-spot-api-docs 



Binance API Tutorial (Part 3) - Candelstick Chart UI with Lightweight Charts

TradingView library Lightweight-Charts
https://www.tradingview.com/lightweight-charts/

https://github.com/tradingview/lightweight-charts



Binance API Tutorial (Part  4) - Historical candlestick Data and the Python Binance Package

https://www.binance.com/fr/my/settings/api-management

https://python-binance.readthedocs.io/en/latest/

pip install python-binance

python3 get_data.py

https://python-binance.readthedocs.io/en/latest/market_data.html

https://binance-docs.github.io/apidocs/spot/en/#old-trade-lookup

python write csv 
https://docs.python.org/3/library/csv.html







