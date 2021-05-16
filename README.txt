By
Part Time Larry


############# Binance API Tutorial (Part 1) - Crypto Trading Bot Design - Jun 20, 2020 #############

https://www.youtube.com/watch?v=rvhnz1yBHgQ

Hey everyone and welcome back to another video, today I'm going to be discussing cryptocurrency. 

Now I'm not typically a crypto trader I only bought it a couple times in my life, but I'm getting more and more requests to cover Binance, specifically whenever I'm covering topics like WEBSOCKETS* and TRADING BOTS. 

(
    Websocket* is a computer communications protocol, providing full-duplex communication channels over a single TCP connection. The WebSocket protocol was standardized by the IETF as RFC 6455 in 2011, and the WebSocket API in Web IDL is being standardized by the W3C. WebSocket is distinct from HTTP.

    cf. WebSockets in 100 Seconds & Beyond with Socket.io by Fireship Youtube channel https://www.youtube.com/watch?v=1BfCnjr_Vjg
)

There a lot of crypto traders out there, they're interested in applying technical analysis, and some of the same technics I'm covering on this channel.
    
I'm currently apply it to stocks and options, but a lot of people are interested in trading crypto. So I thought I will give it a try today, and hopefully learn something in the process myself. 

So, it's about ten thirty - eleven AM on sunday morning, and yeah, one thing I like about cryptos is that the market is always open so while I'm making this videos, I can actually get real time data whenever I want. 

So, the reason I'm doing this particular video is such been request on the youtube video I posted. 
And also there's a forum, if you have any other requests discuss on hackingthemarket.com, if you have anything you want to ask, or a request just for (this) videos, please make an account here and sign up because I'm just getting more and more emails and direct messages on Twitter email and Youtube, and I just need to get them all in one place. 

And also I think it's better to not have all this conversation privately, I want to have a public forum that way it's stock (committed) for the entire community because that's the goal of this channel. 

So, since I've been noticing a lot of request for Binance, I thought I would sign up for an account and check it out. 

So, let's talk about it. 
So, I created a Binance account recently, and I deposit a (wapping) eight dollars and ninety three cents into the account.
So, you know, it's not a lot of money right, but it's you know, the price of a few cups of coffee. 
We can learn some lessons, you know, trade this eight dollars around, and let's see how we can make happen all right?

So, I have this account here, and what are we gonna do, so I've outlined the topic.
So, I thought about what can I build with this thing in about a day, and I thought I would do another multi-part series, where we build a kind of a full stack Tradingview-like platform. It's going to be a very simple and lightweight. 

Obviously Tradingview has tons of features, but I thought I (would do) a hook up, a frontend and a backend, and fullfill some of the other request I'm getting. 
A lot of people want to see a fullstack example, and also want to see things like TAlib which is a technical analysis library, and so I thought I will hook that up as well. 

And so I'm going to do a quick rundown before I get into the code of the entire project we're going to be building. 

So I have writeness down in an markdown file, and this is the start of the repository I'm going to be making for this lesson. 

So here a quick guideline, right: 

So we have a part one, so for this first video when I get started, it's one I will quickly talk about what this Binance is, and how it compares to other exchanges. 
Honeslty, I don't know how to compare to other exchanges. I bought crypto on Coinbase a few times and that's it. 
But It seems like Binance is the leading cryptocurrency exchange, and I think the fees are probably lower. 
And so a part of making this video is I learn about it myself right. 
And one of the reason I mention before why I want to learn more about crypto is that the market is always open, and I can build a lot of these demos and apply to crypto, when I have free time a lot time sets on nights and weekends. 
So, it's good to use cryptos as an example becasue I always get a real time data right. 
So the first thing I'm going to do is so you how to connect to Binance websockets, and get a bunch of incoming data in real-time using websockets, both from the command line.
And I'm also show you how to do it using Python. 
I'm going to show you how to capture that data to a file, and then we're going to also visualize that data with a frontend using javascript. 
And I going to be using this library calls 'lightweight-charts'.

        https://www.tradingview.com/lightweight-charts/

And 'tradingview' actually open sourced a charting library. 
So it's very powerful, and it's very specific unlike other charting library out there for the web, this one is very specific to a financial data so you get a lot of that power of a site like Tradingview.
So you can do things like building this candlesticks charts, there's custom themes, you can see, watermark the charts, and add more advanced features they have different price scales, and you can do this real-time data emulation. 
So I'm going to show you how to visualize the websocket data in real-time. 
And maybe we're going to adding some overlays and some of the indicators and so forth. 
So very powerful charting library we're going to use here, and I'm going show you how to get Binance data from websockets and display a real-time candlestick charts on the web, right. 

So the second thing we're going to do is try to hook up some technical analysis indicators to this, and it's been a lot of request so I'll cover TAlib which is a library for technical analysis, and so what I want to do is on the UI on the web as similar as a site like Tradingview I want to be able to just check and say I'm interested in a particular technical indicator, so as such RSI, and I also want to use Python to analyse the candlesticks that are coming in, and check on particular indicators.
So let's say we want to check whether a cryptocurrency is overbought or oversold, or we want to do something with Bollanger bands, or any of the number of indicators that are available in TAlib. 
I'm also going to write a lib that websocket data to a CSV file to capture for anaylsis.
And also I'm going to try downloading some historical data using the Binance REST API which I haven't explore yet, so I'm going to learn this as I go. 
And then we're going to see if we can apply TALib to historical cryptocurrency data, right.

The third thing we're going to do is, I've covered 'Backtrader' which is a backtesting framework in the past.
And I'll apply that to stocks but I'm going to attempt to apply Backtrader to cryptocurrency, and it looks like Backtrader actually has a TAlib indicators a way to integrate those indicators into Backtrader, in addition to the indicators that Backtrader itself has.
And so what I want to do is get the historical data set of cryptocurrency data that I download using the REST API or capture from websockets.
And I want to apply Backtrader and TAlib indicators to that historical data set and test some different strategies using those indicators, and plot some nice looking charts with a buy/sell entry points,
and see how much an account balance would have grown if we apply a particular strategy historically. 
So one we're satisfy with those results we're going to actually try to hook this all up and see if we can build an API that hooks the frontend, javascript part, and saved the settings for our charts and our notification settings.
So what I'll do here is try to create a few endpoints or either use AWS (chartless) to do a serverless backend, or I might use 'Flask' which is pretty popular as well.
So I'm going to build a WEB API for this charting framework we're building, and so we're going to save some (learning) and indicators settings as similar as how you do in Tradingview.
And then we're going to have some Python code process the (UI) web sockets, the websockets data from Binance, and when we detect any of the indicators that the user is interested in (in), we'll actually call an API endpoint that execute a buy order. 
And we'll aslo process the notification settings and send an email or text notification.

And then to wrap it all up in the final video I'll just as we go I'm going to think to some ideas that we can add to the web UI.
So we're probably add some orders history or intersting visualization to the web UI, and make some improvments and just wrap it up, and have a conclusion.
So I think it's going to be a five parts series. It may grow or be a little less depending on how much I get down.

So yeah it's eleven AM I'm going to do a couple of videos now, and then take a break for a bit. Maybe I'll do an update in the middle (out).
I thought I'll try something different with this series. I filming in outdoors in the backyard at this moment, because you know it's a nice sunny day, the weather's nice in San-Franscico so I thought I'll do some outdoors, and also maybe take you along with me do a walk real quick, take a break, and then come back, and then finish the video at night. 

So yeah that's what we'll making, so fall along with me, I'm going to be posting this source code in the github repository which is at github.com/hackingthemarkets and there also the hackingthemarket's discussion forum if you want to join the discussion, and also make sure you follow me on Youtube or Twitter, and the name is @PartTimeLarry, and yeah follow along and we're going to continue building things and growing this community and (yours) ahead.

So thanks a lot for watching and stay tuned in the next video we're going to get started and jumping in writing the code.





##### Binance API Tutorial (Part 2) - Real-Time Crypto Price Data over Websockets- Jun 20, 2020 ####

https://www.youtube.com/watch?v=d-2GoqQbagI&list=LL&index=344


All right so I'm logged in to my Binance account and I have point zero zero one bitcoins worth about eight dollars and ninety three cents in US dollars.
And I'm interested in figuring out you know how to make some trades how to analyze some data sets and figure out some kind of automated trading system.

So the first step I'm going to take is finding some data. 

And the way, the first method I'm going to use to obtain crypto data is using Binance WebSockets. 

So as we've covered in other videos WebSockets are a way to stream data in real-time, and you can connect WebSockets in a variety of ways.
You can use either a command line tool like WS (cat), you can use a JavaScript to connect to websockets from a web UI for instance, or you can use Python web socket clients in order to connect to these web sockets, and respond to messages based on what you receive in these WebSocket streams.

So I'm in the Binance documentation, the official API Doc's here :

        https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md

        Offcial docs for binance APIS and Streams
        https://github.com/binance/binance-spot-api-docs 

and this gives me the information that I need in order to connect to the Binance WebSockets. 

So it looks like we have a base endpoint, here at wssstream Binance dot com and its port nine four four three, right. 

        wss://stream.binance.com:9443

So I have that, and I'm gonna put this at the top here. I'm just jotting some things down as I go that way I can copy and paste them into my terminal or into my code.
So I have my base URL here and then it looks like you can subscribe to a raw stream by appending this slash ws and then the name of a stream.

        /ws/<streamName>

And so the name of the stream is just like, like a ticker. It looks like this so if you want to subscribe to the Bitcoin USDT stream, you can you can subscribe to that stream but you need to specify if you want the trade stream for instance which will show you all the raw trade information. 
But there's also this K line this candlestick stream here 

        Kline/Candlestick Streams

where you can specify you're only interested in a particular time frame rather than just seeing each individual trade.

So we're gonna try both of those methods, and so the first way I'm gonna connect to the stream is using WS cat which I've covered in some of my previous videos.
So to do this if you want to follow along make sure you have node installed, if you don't have or haven't already, you can just download and install it.
I'm using Mac OS X, so I already have it installed, and you can install the package WS cat. (cf. https://npmjs.com/package/wscat)

        $ npm install -g wscat

so you can use the NPM command, the node package manager and you want to install WS cat.
And so I'll just show you how that looks real quick I already have it installed and up-to-date, so I have that, and so on my command line here if I type wscat 

        $ wscat

you'll see a variety of parameters including this -c that lets you connect to a web socket server.

So what I'm going to want to do is to WS cat -c 

        $ wscat -c <url>

and I am going to connect to this WebSocket server : 

        wss://stream.binance.com:9443
    
and I'm also going to append this particular stream here,
and so what I will do is take this WSS colon slash slash stream binance and then I want all the trade data for Bitcoin,

        wss://stream.binance.com:9443/ws/btcusdt@trade

and it looks like there's no special authentication required here, you can just, this is just wide open, anyone can subscribe to this, and just get a real-time feed of bitcoins trade data.

So I'm gonna do that :

        $ wscat -c wss://stream.binance.com:9443/ws/btcusdt@trade

and you can see just like that, I get a stream of messages coming in.
It's kind of hard to see because it's blue on my command line but you see we have all these traits coming in :

        < {"e":"trade","E":1621016790053,"s":"BTCUSDT","t":833199005,"p":"50405.91000000","q":"0.16428200","b":5914640655,"a":5914640620,"T":1621016790053,"m":false,"M":true}
        < {"e":"trade","E":1621016790070,"s":"BTCUSDT","t":833199006,"p":"50405.91000000","q":"0.39359700","b":5914640665,"a":5914640620,"T":1621016790069,"m":false,"M":true}
        < {"e":"trade","E":1621016790079,"s":"BTCUSDT","t":833199007,"p":"50405.91000000","q":"0.11027100","b":5914640670,"a":5914640620,"T":1621016790079,"m":false,"M":true}
        < {"e":"trade","E":1621016790084,"s":"BTCUSDT","t":833199008,"p":"50405.91000000","q":"0.00120800","b":5914640673,"a":5914640632,"T":1621016790084,"m":false,"M":true}
        < {"e":"trade","E":1621016790087,"s":"BTCUSDT","t":833199009,"p":"50405.91000000","q":"0.53241000","b":5914640675,"a":5914640668,"T":1621016790086,"m":false,"M":true}
        < {"e":"trade","E":1621016790091,"s":"BTCUSDT","t":833199010,"p":"50405.90000000","q":"0.00231900","b":5914640634,"a":5914640678,"T":1621016790090,"m":true,"M":true}
        < {"e":"trade","E":1621016790091,"s":"BTCUSDT","t":833199011,"p":"50405.90000000","q":"0.00768100","b":5914640659,"a":5914640678,"T":1621016790090,"m":true,"M":true}
        < {"e":"trade","E":1621016790093,"s":"BTCUSDT","t":833199012,"p":"50405.90000000","q":"0.01000000","b":5914640659,"a":5914640680,"T":1621016790092,"m":true,"M":true}
        < {"e":"trade","E":1621016790096,"s":"BTCUSDT","t":833199013,"p":"50405.90000000","q":"0.05900000","b":5914640659,"a":5914640684,"T":1621016790095,"m":true,"M":true}
        < {"e":"trade","E":1621016790102,"s":"BTCUSDT","t":833199014,"p":"50407.68000000","q":"0.00531900","b":5914640690,"a":5914640635,"T":1621016790100,"m":false,"M":true}
        < {"e":"trade","E":1621016790103,"s":"BTCUSDT","t":833199015,"p":"50407.68000000","q":"0.00024700","b":5914640691,"a":5914640635,"T":1621016790102,"m":false,"M":true}
        < {"e":"trade","E":1621016790135,"s":"BTCUSDT","t":833199016,"p":"50405.90000000","q":"0.00476000","b":5914640659,"a":5914640711,"T":1621016790134,"m":true,"M":true}
        < {"e":"trade","E":1621016790147,"s":"BTCUSDT","t":833199017,"p":"50405.90000000","q":"0.00100000","b":5914640659,"a":5914640723,"T":1621016790146,"m":true,"M":true}
        < {"e":"trade","E":1621016790152,"s":"BTCUSDT","t":833199018,"p":"50405.90000000","q":"0.00100000","b":5914640659,"a":5914640726,"T":1621016790151,"m":true,"M":true}
        < {"e":"trade","E":1621016790184,"s":"BTCUSDT","t":833199019,"p":"50405.91000000","q":"0.00793000","b":5914640737,"a":5914640697,"T":1621016790183,"m":false,"M":true}
        < {"e":"trade","E":1621016790232,"s":"BTCUSDT","t":833199020,"p":"50405.91000000","q":"0.00100600","b":5914640756,"a":5914640697,"T":1621016790231,"m":false,"M":true}
        < {"e":"trade","E":1621016790246,"s":"BTCUSDT","t":833199021,"p":"50405.90000000","q":"0.04951000","b":5914640659,"a":5914640761,"T":1621016790245,"m":true,"M":true}
        < {"e":"trade","E":1621016790246,"s":"BTCUSDT","t":833199022,"p":"50405.90000000","q":"0.00600000","b":5914640720,"a":5914640761,"T":1621016790245,"m":true,"M":true}
        < {"e":"trade","E":1621016790246,"s":"BTCUSDT","t":833199023,"p":"50405.90000000","q":"0.04386300","b":5914640736,"a":5914640761,"T":1621016790245,"m":true,"M":true}
        < {"e":"trade","E":1621016790246,"s":"BTCUSDT","t":833199024,"p":"50405.90000000","q":"0.10193300","b":5914640759,"a":5914640761,"T":1621016790245,"m":true,"M":true}
        < {"e":"trade","E":1621016790304,"s":"BTCUSDT","t":833199025,"p":"50405.91000000","q":"0.00116600","b":5914640777,"a":5914640697,"T":1621016790303,"m":false,"M":true}
        < {"e":"trade","E":1621016790384,"s":"BTCUSDT","t":833199026,"p":"50403.68000000","q":"0.00763800","b":5914640037,"a":5914640799,"T":1621016790383,"m":true,"M":true}
        < {"e":"trade","E":1621016790398,"s":"BTCUSDT","t":833199027,"p":"50401.48000000","q":"0.00200000","b":5914640703,"a":5914640804,"T":1621016790397,"m":true,"M":true}
        < {"e":"trade","E":1621016790432,"s":"BTCUSDT","t":833199028,"p":"50401.49000000","q":"0.00484800","b":5914640824,"a":5914640801,"T":1621016790431,"m":false,"M":true}
        < {"e":"trade","E":1621016790435,"s":"BTCUSDT","t":833199029,"p":"50401.49000000","q":"0.00648400","b":5914640827,"a":5914640801,"T":1621016790434,"m":false,"M":true}
        < {"e":"trade","E":1621016790435,"s":"BTCUSDT","t":833199030,"p":"50401.49000000","q":"0.00648500","b":5914640828,"a":5914640801,"T":1621016790434,"m":false,"M":true}
        < {"e":"trade","E":1621016790437,"s":"BTCUSDT","t":833199031,"p":"50401.78000000","q":"0.00648400","b":5914640830,"a":5914640818,"T":1621016790437,"m":false,"M":true}
        < {"e":"trade","E":1621016790449,"s":"BTCUSDT","t":833199032,"p":"50401.78000000","q":"0.17009800","b":5914640839,"a":5914640818,"T":1621016790448,"m":false,"M":true}
        < {"e":"trade","E":1621016790462,"s":"BTCUSDT","t":833199033,"p":"50405.64000000","q":"0.04001500","b":5914640852,"a":5914640823,"T":1621016790461,"m":false,"M":true}
        < {"e":"trade","E":1621016790476,"s":"BTCUSDT","t":833199034,"p":"50405.90000000","q":"0.00763800","b":5914640857,"a":5914640870,"T":1621016790475,"m":true,"M":true}
        < {"e":"trade","E":1621016790568,"s":"BTCUSDT","t":833199035,"p":"50409.75000000","q":"0.00509600","b":5914640898,"a":5914640925,"T":1621016790567,"m":true,"M":true}
        < {"e":"trade","E":1621016790625,"s":"BTCUSDT","t":833199036,"p":"50409.75000000","q":"0.02960000","b":5914640898,"a":5914640939,"T":1621016790624,"m":true,"M":true}
        < {"e":"trade","E":1621016790636,"s":"BTCUSDT","t":833199037,"p":"50409.75000000","q":"0.00966900","b":5914640898,"a":5914640942,"T":1621016790635,"m":true,"M":true}
        < {"e":"trade","E":1621016790649,"s":"BTCUSDT","t":833199038,"p":"50409.75000000","q":"0.00500000","b":5914640898,"a":5914640946,"T":1621016790648,"m":true,"M":true}
        < {"e":"trade","E":1621016790649,"s":"BTCUSDT","t":833199039,"p":"50409.75000000","q":"0.00100000","b":5914640898,"a":5914640947,"T":1621016790649,"m":true,"M":true}
        < {"e":"trade","E":1621016790727,"s":"BTCUSDT","t":833199040,"p":"50409.75000000","q":"0.01642400","b":5914640898,"a":5914640972,"T":1621016790726,"m":true,"M":true}
        < {"e":"trade","E":1621016790749,"s":"BTCUSDT","t":833199041,"p":"50408.34000000","q":"0.02868600","b":5914640902,"a":5914640975,"T":1621016790749,"m":true,"M":true}
        < {"e":"trade","E":1621016790749,"s":"BTCUSDT","t":833199042,"p":"50408.30000000","q":"0.01878800","b":5914640948,"a":5914640975,"T":1621016790749,"m":true,"M":true}
        < {"e":"trade","E":1621016790749,"s":"BTCUSDT","t":833199043,"p":"50406.25000000","q":"0.00039600","b":5914640911,"a":5914640975,"T":1621016790749,"m":true,"M":true}
        < {"e":"trade","E":1621016790749,"s":"BTCUSDT","t":833199044,"p":"50401.50000000","q":"0.01000000","b":5914640894,"a":5914640975,"T":1621016790749,"m":true,"M":true}
        < {"e":"trade","E":1621016790749,"s":"BTCUSDT","t":833199045,"p":"50400.50000000","q":"0.13918500","b":5914638335,"a":5914640975,"T":1621016790749,"m":true,"M":true}
        < {"e":"trade","E":1621016790749,"s":"BTCUSDT","t":833199046,"p":"50400.50000000","q":"0.00326100","b":5914638344,"a":5914640975,"T":1621016790749,"m":true,"M":true}
        < {"e":"trade","E":1621016790820,"s":"BTCUSDT","t":833199047,"p":"50406.02000000","q":"0.00202500","b":5914641020,"a":5914641013,"T":1621016790819,"m":false,"M":true}
        < {"e":"trade","E":1621016790824,"s":"BTCUSDT","t":833199048,"p":"50406.01000000","q":"0.07217200","b":5914641010,"a":5914641023,"T":1621016790823,"m":true,"M":true}
        < {"e":"trade","E":1621016790899,"s":"BTCUSDT","t":833199049,"p":"50406.02000000","q":"0.00043200","b":5914641037,"a":5914641013,"T":1621016790899,"m":false,"M":true}
        < {"e":"trade","E":1621016790902,"s":"BTCUSDT","t":833199050,"p":"50406.02000000","q":"0.01795900","b":5914641039,"a":5914641013,"T":1621016790901,"m":false,"M":true}
        < {"e":"trade","E":1621016790919,"s":"BTCUSDT","t":833199051,"p":"50403.49000000","q":"0.00039600","b":5914640996,"a":5914641044,"T":1621016790918,"m":true,"M":true}
        < {"e":"trade","E":1621016790919,"s":"BTCUSDT","t":833199052,"p":"50401.38000000","q":"0.00460400","b":5914641018,"a":5914641044,"T":1621016790918,"m":true,"M":true}
        < {"e":"trade","E":1621016790979,"s":"BTCUSDT","t":833199053,"p":"50403.48000000","q":"0.00072600","b":5914641083,"a":5914641063,"T":1621016790978,"m":false,"M":true}
        < {"e":"trade","E":1621016790985,"s":"BTCUSDT","t":833199054,"p":"50403.48000000","q":"0.05900000","b":5914641087,"a":5914641063,"T":1621016790985,"m":false,"M":true}
        < {"e":"trade","E":1621016790996,"s":"BTCUSDT","t":833199055,"p":"50406.01000000","q":"0.00039600","b":5914641090,"a":5914641042,"T":1621016790994,"m":false,"M":true}
        < {"e":"trade","E":1621016791003,"s":"BTCUSDT","t":833199056,"p":"50407.28000000","q":"0.04310800","b":5914641099,"a":5914641068,"T":1621016790999,"m":false,"M":true}
        < {"e":"trade","E":1621016791003,"s":"BTCUSDT","t":833199057,"p":"50409.75000000","q":"0.01589200","b":5914641099,"a":5914641094,"T":1621016790999,"m":false,"M":true}
        < {"e":"trade","E":1621016791131,"s":"BTCUSDT","t":833199058,"p":"50409.74000000","q":"0.00079200","b":5914641175,"a":5914641118,"T":1621016791130,"m":false,"M":true}
        < {"e":"trade","E":1621016791131,"s":"BTCUSDT","t":833199059,"p":"50409.76000000","q":"0.00548500","b":5914641175,"a":5914640622,"T":1621016791130,"m":false,"M":true}
        < {"e":"trade","E":1621016791131,"s":"BTCUSDT","t":833199060,"p":"50411.61000000","q":"0.00067300","b":5914641175,"a":5914640642,"T":1621016791130,"m":false,"M":true}
        < {"e":"trade","E":1621016791141,"s":"BTCUSDT","t":833199061,"p":"50409.73000000","q":"0.00476000","b":5914641154,"a":5914641177,"T":1621016791139,"m":true,"M":true}
        < {"e":"trade","E":1621016791144,"s":"BTCUSDT","t":833199062,"p":"50409.73000000","q":"0.01646200","b":5914641154,"a":5914641180,"T":1621016791139,"m":true,"M":true}
        < {"e":"trade","E":1621016791149,"s":"BTCUSDT","t":833199063,"p":"50411.60000000","q":"0.00090000","b":5914641183,"a":5914641188,"T":1621016791149,"m":true,"M":true}
        < {"e":"trade","E":1621016791150,"s":"BTCUSDT","t":833199064,"p":"50411.60000000","q":"0.00734100","b":5914641183,"a":5914641189,"T":1621016791149,"m":true,"M":true}
        < {"e":"trade","E":1621016791164,"s":"BTCUSDT","t":833199065,"p":"50411.61000000","q":"0.02932700","b":5914641193,"a":5914640642,"T":1621016791163,"m":false,"M":true}
        < {"e":"trade","E":1621016791237,"s":"BTCUSDT","t":833199066,"p":"50417.73000000","q":"0.05301000","b":5914641202,"a":5914641225,"T":1621016791232,"m":true,"M":true}
        < {"e":"trade","E":1621016791238,"s":"BTCUSDT","t":833199067,"p":"50417.74000000","q":"0.00066300","b":5914641227,"a":5914640450,"T":1621016791236,"m":false,"M":true}
        < {"e":"trade","E":1621016791257,"s":"BTCUSDT","t":833199068,"p":"50417.74000000","q":"0.00051400","b":5914641235,"a":5914640450,"T":1621016791254,"m":false,"M":true}
        < {"e":"trade","E":1621016791280,"s":"BTCUSDT","t":833199069,"p":"50417.73000000","q":"0.00088400","b":5914641202,"a":5914641238,"T":1621016791278,"m":true,"M":true}
        < {"e":"trade","E":1621016791281,"s":"BTCUSDT","t":833199070,"p":"50417.73000000","q":"0.20012200","b":5914641202,"a":5914641239,"T":1621016791280,"m":true,"M":true}
        < {"e":"trade","E":1621016791285,"s":"BTCUSDT","t":833199071,"p":"50417.74000000","q":"0.00120300","b":5914641241,"a":5914640450,"T":1621016791284,"m":false,"M":true}
        < {"e":"trade","E":1621016791327,"s":"BTCUSDT","t":833199072,"p":"50415.21000000","q":"0.00024100","b":5914641262,"a":5914641246,"T":1621016791327,"m":false,"M":true}
        < {"e":"trade","E":1621016791336,"s":"BTCUSDT","t":833199073,"p":"50413.45000000","q":"0.00151900","b":5914641264,"a":5914641266,"T":1621016791333,"m":true,"M":true}
        < {"e":"trade","E":1621016791352,"s":"BTCUSDT","t":833199074,"p":"50415.21000000","q":"0.00292900","b":5914641271,"a":5914641246,"T":1621016791351,"m":false,"M":true}
        < {"e":"trade","E":1621016791394,"s":"BTCUSDT","t":833199075,"p":"50413.44000000","q":"0.00039600","b":5914641251,"a":5914641287,"T":1621016791392,"m":true,"M":true}
        < {"e":"trade","E":1621016791394,"s":"BTCUSDT","t":833199076,"p":"50410.48000000","q":"0.00876500","b":5914641204,"a":5914641287,"T":1621016791392,"m":true,"M":true}
        < {"e":"trade","E":1621016791400,"s":"BTCUSDT","t":833199077,"p":"50410.48000000","q":"0.00075000","b":5914641204,"a":5914641290,"T":1621016791399,"m":true,"M":true}
        < {"e":"trade","E":1621016791403,"s":"BTCUSDT","t":833199078,"p":"50409.67000000","q":"0.00085000","b":5914641160,"a":5914641291,"T":1621016791403,"m":true,"M":true}
        < {"e":"trade","E":1621016791407,"s":"BTCUSDT","t":833199079,"p":"50409.67000000","q":"0.03000000","b":5914641160,"a":5914641293,"T":1621016791407,"m":true,"M":true}
        < {"e":"trade","E":1621016791481,"s":"BTCUSDT","t":833199080,"p":"50404.76000000","q":"0.19322000","b":5914641344,"a":5914641337,"T":1621016791481,"m":false,"M":true}
        < {"e":"trade","E":1621016791500,"s":"BTCUSDT","t":833199081,"p":"50404.76000000","q":"0.00782300","b":5914641360,"a":5914641337,"T":1621016791498,"m":false,"M":true}
        < {"e":"trade","E":1621016791573,"s":"BTCUSDT","t":833199082,"p":"50409.28000000","q":"0.00039600","b":5914641397,"a":5914641349,"T":1621016791572,"m":false,"M":true}
        < {"e":"trade","E":1621016791573,"s":"BTCUSDT","t":833199083,"p":"50409.28000000","q":"0.03943500","b":5914641397,"a":5914641378,"T":1621016791572,"m":false,"M":true}
        < {"e":"trade","E":1621016791574,"s":"BTCUSDT","t":833199084,"p":"50409.27000000","q":"0.12000000","b":5914641370,"a":5914641398,"T":1621016791573,"m":true,"M":true}
        < {"e":"trade","E":1621016791576,"s":"BTCUSDT","t":833199085,"p":"50409.27000000","q":"0.13000000","b":5914641370,"a":5914641399,"T":1621016791575,"m":true,"M":true}
        < {"e":"trade","E":1621016791576,"s":"BTCUSDT","t":833199086,"p":"50404.77000000","q":"0.03073200","b":5914641393,"a":5914641399,"T":1621016791575,"m":true,"M":true}
        < {"e":"trade","E":1621016791576,"s":"BTCUSDT","t":833199087,"p":"50404.75000000","q":"0.00039600","b":5914641322,"a":5914641399,"T":1621016791575,"m":true,"M":true}
        < {"e":"trade","E":1621016791576,"s":"BTCUSDT","t":833199088,"p":"50403.48000000","q":"0.22187200","b":5914641387,"a":5914641399,"T":1621016791575,"m":true,"M":true}
        < {"e":"trade","E":1621016791585,"s":"BTCUSDT","t":833199089,"p":"50403.47000000","q":"0.05900000","b":5914641153,"a":5914641403,"T":1621016791584,"m":true,"M":true}
        < {"e":"trade","E":1621016791587,"s":"BTCUSDT","t":833199090,"p":"50403.47000000","q":"0.02600000","b":5914641153,"a":5914641412,"T":1621016791585,"m":true,"M":true}
        < {"e":"trade","E":1621016791599,"s":"BTCUSDT","t":833199091,"p":"50403.47000000","q":"0.04000000","b":5914641153,"a":5914641427,"T":1621016791598,"m":true,"M":true}
        < {"e":"trade","E":1621016791612,"s":"BTCUSDT","t":833199092,"p":"50403.47000000","q":"0.03300000","b":5914641153,"a":5914641435,"T":1621016791611,"m":true,"M":true}
        < {"e":"trade","E":1621016791615,"s":"BTCUSDT","t":833199093,"p":"50403.47000000","q":"0.82059600","b":5914641153,"a":5914641439,"T":1621016791614,"m":true,"M":true}

it's just scrolling down my screen and I'm gonna copy this to another window real quick but yeah just tons of trade data coming.
And then I'm just gonna stop that, right :

        ctrl c

So let's let's look at that for a bit.
Let's see what we get. 
So in a WebSocket you send it some kind of message or subscribe to the stream and then you get messages back from the WebSocket in JSON format, and so you see we have this JavaScript object that has a bunch of keys and values, see you see our symbol :

        "BTCUSDT"

and it looks like we have this :

        "T" 
        
I think is a UNIX timestamp, so if I were to put this into UNIX timestamp dot com for instance.
I'll do that just so you see. This is a timestamp on the price, and so I'm gonna go to UNIX timestamp dot com :

        https://www.unixtimestamp.com/

and let's just see the utility you can use to see what a UNIX timestamp. Which time it refers to you
And so it gives me the milliseconds as well, so I'm going to delete the last few digits

        1621016791614

and you see that trade occurred on (May 24th which is today at 6:42 p.m. UTC and since I'm in Pacific time it's actually 11:42 a.m. when this occurred, right)  
 
        Fri May 14 2021 20:26:31 GMT+0200 (Central European Summer Time)

So we have a timestamp and then we have a price.
So it looks like a Bitcoin at that time was (trading at eight thousand one hundred sixty four dollars and 63 cents) 

        "50403.47000000" (usd)

and then we have some other some other data here, so if you look at the documentation you can see, you have an event type, it's a trade ...

        Payload:

                {
                  "e": "aggTrade",  // Event type
                  "E": 123456789,   // Event time
                  "s": "BNBBTC",    // Symbol
                  "a": 12345,       // Aggregate trade ID
                  "p": "0.001",     // Price
                  "q": "100",       // Quantity
                  "f": 100,         // First trade ID
                  "l": 105,         // Last trade ID
                  "T": 123456785,   // Trade time
                  "m": true,        // Is the buyer the market maker?
                  "M": true         // Ignore
                }

you have your timestamp which is your trade time, you have a buyer order ID, and seller order ID, and you have a price, quantity, and so forth.

So that's how you get real-time data over WebSockets from Binance, right.

All right so usually I'm not as interested in getting every single trade, some people might have the strategy that uses every single trade for some reason but usually I'm interested in a candlestick, if you're a day trader, right, you might be interested in let's say the 15-minute time frame, or the hourly time frame, right, and if you're a swing trader maybe you're only interested in candlesticks for the day or the week or the month, right, because your time frame is a little bit longer.

So since we're doing a real-time stream right now, I'm going to do a time frame, let's just do five minutes to start, and see how that looks.

So I'm gonna try this Candlestick Stream. 

So it looks like you just pass a symbol ...

        Kline/Candlestick chart intervals:

            Stream Name: <symbol>@kline_<interval>

instead of @trade, you give it Kline, I think, I usually don't use that term Kline, I usually just say Candlestick, so you give it a Kline and an interval, and I think kline is just 
another name for candlestick charts, and so let's give it a five-minute interval.

So I'm gonna do that, all right, and I'll do that, and then I'll put this (@kline) and then underscore five M, right.

        wss://stream.binance.com:9443/ws/btcusdt@kline_5m

and I'm going to run this one more time, and so I'm going to do WS cat dash SC and then subscribe to that stream :

        $ wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m

and see what happens right, and then look at that, so I'm getting some data, but it's coming
in a little bit slower, and you'll see that I have a different format, right : 


        < {"e":"kline","E":1621109661790,"s":"BTCUSDT","k":{"t":1621109400000,"T":1621109699999,        "s":"BTCUSDT","i":"5m","f":835570074,"L":835575605,"o":"48364.48000000","c":"48364.80000000",       "h":"48461.73000000","l":"48325.00000000","v":"200.92067000","n":5532,"x":false,"q":"9725079.   25195099","V":"106.52648500","Q":"5155591.37065720","B":"0"}}
        < {"e":"kline","E":1621109663839,"s":"BTCUSDT","k":{"t":1621109400000,"T":1621109699999,        "s":"BTCUSDT","i":"5m","f":835570074,"L":835575628,"o":"48364.48000000","c":"48373.68000000",       "h":"48461.73000000","l":"48325.00000000","v":"201.77948200","n":5555,"x":false,"q":"9766621.   80940916","V":"106.56816100","Q":"5157607.19260893","B":"0"}}
        < {"e":"kline","E":1621109665930,"s":"BTCUSDT","k":{"t":1621109400000,"T":1621109699999,        "s":"BTCUSDT","i":"5m","f":835570074,"L":835575653,"o":"48364.48000000","c":"48364.80000000",       "h":"48461.73000000","l":"48325.00000000","v":"203.08149100","n":5580,"x":false,"q":"9829601.   08583875","V":"106.59331200","Q":"5158823.61594524","B":"0"}}
        < {"e":"kline","E":1621109668158,"s":"BTCUSDT","k":{"t":1621109400000,"T":1621109699999,        "s":"BTCUSDT","i":"5m","f":835570074,"L":835575673,"o":"48364.48000000","c":"48364.95000000",       "h":"48461.73000000","l":"48325.00000000","v":"203.48707500","n":5600,"x":false,"q":"9849217.   34691895","V":"106.92130900","Q":"5174687.22495024","B":"0"}}

So we have a timestamp, and you see we have more data coming in, but you'll notice this timestamp isn't changing and I think that's because I specified a five minute time frame, and so we're just seeing five minutes of data, and so if I take that timestamp for instance, we'll
know what bar we're on, and so let's go back to Unix timestamp, right

Right, and so you see this is for 6:45 p.m. UTC, right and, so this isn't going to change for a while, it's not going to change until we change minute bars, and so this data is just going to keep coming in, and whenever we change to 650 for instance you'll see a new timestamp there and so I'm going to go ahead and copy this, and look at it here, and just so we can see the structure for the candlestick data, and how it's a little bit different so you see we have this extra dictionary or object, nested inside, and then we also have, let me put this in a new notepad just so we can prettify it a little bit, so I have this little prettify JSON thing, and let's see if, yep there we go :

        {
            "e":"kline",
            "E":1621109668158,
            "s":"BTCUSDT",
            "k":{
                "t":1621109400000,
                "T":1621109699999,
                "s":"BTCUSDT",
                "i":"5m",
                "f":835570074,
                "L":835575673,
                "o":"48364.48000000",
                "c":"48364.95000000",       
                "h":"48461.73000000",
                "l":"48325.00000000",
                "v":"203.48707500",
                "n":5600,       
                "x":false,
                "q":"9849217.34691895",
                "V":"106.92130900",
                "Q":"5174687.22495024",
                "B":"0"
            }
        }


So for this you see we have our symbol for a Bitcoin, right 
and then we have our time stamp here, and so this is a 5-minute time interval, 
and then we can see the ohlc data so for that particular candlestick we know the current open high low and close, so that candle opened at 48364 and 48 cents and it's not closed yet but I
think it updates this closing time as we get more and more data you'll see this closing candlestick what's it actually closest we'll know the final closing value and then a high and low are going to be adjusted as we get more data so you'll see if I scroll down, right 
I look here unless see what the current values are for that exact data right 

So I'm going to paste another one of these in and then prettify that, and there we go, and let's
just compare like what we're getting now versus a second ago so we're still on the same timestamp the same 5-minute candlestick and then the open should stay the same because it's still the same candlestick so we have the open of 8 9 6.6 right, so the opening price is the same but you'll see the high is still the same but you'll notice the low for that candlestick went from 89 6007 to 89 45 so we're updating the highs and lows as we go it still hasn't went above 80 nine eight eight thousand hundred sixty nine dollars and forty cents so the high that's still the high points and the closes is getting adjusted as we get more and more data 

So eventually this candlestick is kind of close and then we'll have the final value for the open high and low and close for that particular five-minute candlestick 

So that's all good now what so maybe I don't want to just stream this to my console maybe I want to capture this output to a file so I can save it for analysis later, and so what I can do here
is rerun this command, and then I can pipe it with this pipe and then I'll do it to the tee  command which will output it to my console but also save it to a file

        $ wscat -c wss://stream.binance.com:9443/ws/btcusdt@kline_5m | tee dataset.txt

so I'm gonna save it to dataset dot txt, right, and so this will stream it and you'll notice it continues to output the information to the console but then whenever I end this command line program you'll see that we have a file called dataset dot text, that where we've captured all these all of this candlestick data to a file that way if we want to use a program later to analyze this data set we can do so, and so a lot of people have been asking me 'do you know where I can get historical option data or historical future data or any historical data sets?'
and a lot of companies charge a lot of money for all this historical data but if you can use your own tools, and just capture them day by day you know maybe snapshot your own historical data set, and just build that up over time I'll leave something like this running for days or
whatever time frame you're interested in and you know capture and save your own data to a file, you know it's not that, it's not that complicated.

So now that that's done you can see we've rolled over to a new five minute candlestick so I wanted to show that and so you can see this timestamp it's updated right, and so if I type this
timestamp in, and that includes the milliseconds so what I've been doing is taking off those last three digits and I'll show you it's rolled over to the 50 minute mark there and we've rolled over to a new candlestick and now when I stop this program, control c, I look and I have this dataset dot text, and so now if I look in my directory, there's this dataset.txt with tons of data and we can use it later so we could capture as much of the state as we want, and then
process it later if we want to, if we don't want to deal with it in real time at the moment.

All right, now that I've shown you how to connect to a WebSocket from the command line you might be wondering how you can connect to it from your favorite programming language, so the first one I'm going to use is JavaScript, so we can include this WebSocket data and stream it on to the web and create some charts from it

So let's create, so I have this directory called coinview, which I'm using for this project, and I'll publish the source code later, so if you see I'm in this coinview directory here and I also have Visual Studio code open and I just open the coinview directory, which is pretty empty, it has my readme about what we're going to do, and it has this dataset that I just saved, so let's just create an index.html, just to start super basic right, and so I can do HTML right and I'll do a coinview is what I'll call this app, because it's like kind of a tradingview for crypto, and it's just a little small lightweight UI, right

So we have a head and, right, I need a title, now you don't need one but I'm just going to do it since it's quick, right, and I'm gonna do a body right and I'll just say hello, and let's just open this file in our browser to make sure we're good, so, I'll do that, and so, let's go to projects 
we got coinview, and we have an index.html, and it's just a 'hello' website, right, and so now what we want to do is connect a WebSocket, so I'm going to open the JavaScript console, I'm using Chrome, and let's see how we use WebSockets from JavaScript, it's actually very easy so writing 
websocket applications, right 

        https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications  

So JavaScript has this WebSocket object that's built in and you can instantiate it and connect to a WebSocket :

        webSocket = new WebSocket(url, protocols);
   
So let's try this example right, so open that index.html and then in my head here let's just do, actually I'll do it at the bottom, at the end of the body, it's a process right, and I'll do a script tag, let's do an example socket, and I am going to take the web socket address that I copied
earlier, for the kline, or the trade data, right


All right, so I get that and I copy it, and instead of this address I'm going to use binance, and I don't need this second parameter : 

        <script>
            // Create WebSocket connection.
            var exampleSocket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade');
            console.log(exampleSocket); 
        </script>

it's just something optional, and let's see if we can log that, and see if this runs, right, 

So I'm going to reload the page and you see I logged this to the console, and it looks like we have some kind of WebSocket, we have an object here,and so yeah what's happening I don't know yet

So we we have this WebSocket connection, right, so what do we do next?
We need to actually receive the messages from the WebSocket, so let's go back to the mozilla documentation for instance, and you can send data to the server or you can receive messages from the server, and, so you need to do is define an on-message function, and so that function just says what do you want to do when you receive a message

So I'm going to rename this I'm gonna call it binanceSocket and I'll say, when I receive a message, so binanceSocket.onmessage we want to execute this function right :

        <script>
            // Create WebSocket connection.
            var binanceSocket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade');
            console.log(binanceSocket); 

            binanceSocket.onmessage = function (event) {
                console.log(event.data)
            }
        </script>

so I'm going to execute that function and log it to the console, so let's see what our data looks like 
So i refresh it, now exampleSocket is not defined because I'm not using that anymore, I renamed it, all right, so I refreshed it and now look at that, we have a web page already that's using Javascript to connect to a Binance WebSocket, and we're streaming trades from Binance to the web

Awesome! that was really quick, we started from scratch from an empty file, right, so let's pretend we don't want those in the console, we could actually make a div here, and then we could do, we
could call this, trades div ID equals trades 

        <div id="trades"></div>

and let's just start that empty, and then instead of 'hello' let's just type H little heading here h2 we'll just type it 'Trades' and then instead of just console outing it we can do, here we can
do a div we can do a document dot getElementById, and then we'll do 'trades'

        <body>
            <h1>Trades</h1>
    
            <div id="charts"></div>

            <script>
                // Create WebSocket connection.
                var binanceSocket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade');

                var tradeDiv = document.getElementById('trades')
       
                binanceSocket.onmessage = function (event) {
                    console.log(event.data)

        

                }
            </script>
        </body>

and then so we'll create a variable called 'tradeDiv', and then that's going to be equal to this particular element on the page, we're going to get a reference to it
So now in our on message event we're going to process this 'event.data' so we have this, this is actually a JSON string but we want to access it as an object that way we can pull out individual attributes like the price and the timestamp, 

So what I'll do is, I'll create a new variable and I'm going to call it 'messageObject' and I'm going to set it equal to JSON.parse (event.data) 

                binanceSocket.onmessage = function (event) {
                    console.log(event.data)

                    var messageObject = JSON.parse(event.data)
                
                }

and then we'll be able to access this like an object, and we'll be able to type things like messageObject dot P for instance, to access this price attribute, right 


                binanceSocket.onmessage = function (event) {
                    console.log(event.data)

                    var messageObject = JSON.parse(event.data)
                    messageObject.p
                }

So now what we'll do is take this trade div and then we'll just append messageObject dot P, right 

        <body>
            <h1>Trades</h1>
    
            <div id="charts"></div>

            <script>
                // Create WebSocket connection.
                var binanceSocket = new WebSocket('wss://stream.binance.com:9443/ws/btcusdt@trade');

                var tradeDiv = document.getElementById('trades')
       
                binanceSocket.onmessage = function (event) {
                    console.log(event.data)

                    var messageObject = JSON.parse(event.data)
                    //messageObject.p
                    
                    tradeDiv.append(messageObject.p)
                }
            </script>
        </body>

and it should just append it to the div, so I'll reload the page and look at that
I have real-time price data, and it's just getting appended to the web page over and over again which is great!

So we already have at the start of a UI, we have a way to connect from WebSockets using javascript and a way to append those to a web page 

So I think this video has gone on, quite a bit, so we've learned how to connect to Binance WebSocket data from the command-line, and also connected to it from the web and show show it, and
we're able to show that price data on a web page now

So I think I'll do a quick break here, and take a break, I'm gonna go outside, bike around, walk around, and then when we come back, I'll actually hook up this real time price data to this lightweight charts 

        https://www.tradingview.com/lightweight-charts/

and we're going to try to do this a real-time WebSocket candlestick chart here using Binance data So stay tuned for the next video and thanks for watching!





########### Binance API Tutorial (Part 3) - Candelstick Chart UI with Lightweight Charts ###########


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







