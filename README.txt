By 
Part Time Larry










Binance API Tutorial (Part 1) - Crypto Trading Bot Design - Jun 20, 2020 

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











Binance API Tutorial (Part 2) - Real-Time Crypto Price Data over Websockets- Jun 20, 2020 

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










Binance API Tutorial (Part 3) - Candelstick Chart UI with Lightweight Charts 

https://www.youtube.com/watch?v=6PnCr14chcY





all right that was great so now that i'm back inside, i wanted to continue where we left off,
if you'll remember last time i mentioned that we're going to try to use this lightweight charts library to add a candlestick chart to our u, and just start sketching out the ui a little bit, uh i'm just going to start very simple in this video and then we'll add on to it over time, i don't want to spend too much time on ui yet, but i want to figure out how to add this chart library to our web page.

So you remember last time we had a file here, an index.html and all we're doing is uh connecting to websockets, and we're streaming out this price data, and then we're displaying and appending the bitcoin prices to our webpage 

So in addition to that, let's see if we can go ahead and include some type of chart here
So i am going to stop this stream for a bit, so i'm going to comment this out for a minute,
all this websocket stuff, and let's just focus on the charting aspect 

So what we'll do here is i'm going to include a new javascript at the end here, and i'm going to say source equals chart.js

        <script src="chart.js"></script>

and we're going to create a new file called chart dot js, just so because i know we're gonna have a lot of javascript i want to include it in a separate file

so i'll do a new file and i'll call it chart.js, right, and here we'll just put all of our 
javascript for lightweight charts, and we're gonna include it at the bottom of the page 

all right so i'm going to look at lightweight charts here, and see how we get the library, and learn more

        https://www.tradingview.com/lightweight-charts/

so it links to a github page right 

        https://github.com/tradingview/lightweight-charts

it looks like you can install it as a node package to access these imports, or there's a CDN which is 'content distribution network' and so you can just include this URL straight up,

        https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js

so just to make it simple for everyone, i'm going to use use it in this fashion
so what you can do is add a script tag, so script in your head, you just do script source equals and then just include that script :

        <head>
            <title>Coinview</title>
            <script src="https://unpkg.com/lightweight-charts/dist/lightweight-charts.standalone.production.js"></script>
        </head>

and then you'll have lightweight charts included and it's just hosted on another uh on another host it's already hosted here, and ready to go, right, and then we have this chart.js here which where we'll put our javascript that's custom, and you'll see uh they provided an example here, of
how to initialize this chart :

        const chart = LightweightCharts.createChart(document.body, { width: 400, height: 300 });
        const lineSeries = chart.addLineSeries();
        lineSeries.setData([
            { time: '2019-04-11', value: 80.01 },
            { time: '2019-04-12', value: 96.63 },
            { time: '2019-04-13', value: 76.64 },
            { time: '2019-04-14', value: 81.89 },
            { time: '2019-04-15', value: 74.43 },
            { time: '2019-04-16', value: 80.01 },
            { time: '2019-04-17', value: 96.63 },
            { time: '2019-04-18', value: 76.64 },
            { time: '2019-04-19', value: 81.89 },
            { time: '2019-04-20', value: 74.43 },
        ]);

so i'm going to take that, let's see, yeah let's take that, and let's just put it in our chart.js so i'm going to paste that in there, and so we have chart equals, so it looks like you create a new
chart, and you give it a width and a height, and you choose where it's added on the page

so it's using document.body here, uh which will erase our other stuff in the body,
so what i want to do is create a new div just for the chart and i'll call it id equals chart 

        <div id="charts"></div>

and let's see if i can just say instead of document.body i'm going to do document.getelementbyid 'chart'
and i'll just pass it the id of our 'chart' element

        const chart = LightweightCharts.createChart(document.getElementById('chart'), { width: 400, height: 300 });

and then yeah let's just add this default line series that they include out of the box
and then later we'll replace this data with our data from binance 

so let's just see if this renders and see if we have any errors
all right so i'm gonna refresh that, and look at that, we already have this line chart here with some data it doesn't look exactly like we want it to look yet, but very promising we've already included the
charting library 'lightweight charts', it's already on our web page and it's already displaying some price data which is great, that's a great great start 

so let's see if we can change this up a little bit
um see if we can add it as a candlestick chart, so let's look at our examples here, and let's see what a candlestick chart looks like 

so i'm going to click their examples for candlestick chart 

        https://www.tradingview.com/lightweight-charts/
        
        Candlestick chart       </> 

and it'll look a little bit different, and it looks like you can do, yeah so i'm going to copy this :

        https://jsfiddle.net/TradingView/eaod9Lq8/

        var chart = LightweightCharts.createChart(document.body, {
	    width: 600,
            height: 300,
	    layout: {
		backgroundColor: '#000000',
		textColor: 'rgba(255, 255, 255, 0.9)',
	    },
	    grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
	        },
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	     },
	    crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	    },
	    rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	    },
	    timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	    },
        });

        var candleSeries = chart.addCandlestickSeries({
            upColor: 'rgba(255, 144, 0, 1)',
            downColor: '#000',
            borderDownColor: 'rgba(255, 144, 0, 1)',
            borderUpColor: 'rgba(255, 144, 0, 1)',
            wickDownColor: 'rgba(255, 144, 0, 1)',
            wickUpColor: 'rgba(255, 144, 0, 1)',
        });

        candleSeries.setData([
	    { time: '2018-10-19', open: 180.34, high: 180.99, low: 178.57, close: 179.85 },
	    { time: '2018-10-22', open: 180.82, high: 181.40, low: 177.56, close: 178.75 },
	    { time: '2018-10-23', open: 175.77, high: 179.49, low: 175.44, close: 178.53 },
	    { time: '2018-10-24', open: 178.58, high: 182.37, low: 176.31, close: 176.97 },
	    { time: '2018-10-25', open: 177.52, high: 180.50, low: 176.83, close: 179.07 },
	    { time: '2018-10-26', open: 176.88, high: 177.34, low: 170.91, close: 172.23 },
	    { time: '2018-10-29', open: 173.74, high: 175.99, low: 170.95, close: 173.20 },
	    { time: '2018-10-30', open: 173.16, high: 176.43, low: 172.64, close: 176.24 },
	    { time: '2018-10-31', open: 177.98, high: 178.85, low: 175.59, close: 175.88 },
	    { time: '2018-11-01', open: 176.84, high: 180.86, low: 175.90, close: 180.46 },
	    { time: '2018-11-02', open: 182.47, high: 183.01, low: 177.39, close: 179.93 },
	    { time: '2018-11-05', open: 181.02, high: 182.41, low: 179.30, close: 182.19 },
	    { time: '2018-11-06', open: 181.93, high: 182.65, low: 180.05, close: 182.01 },
	    { time: '2018-11-07', open: 183.79, high: 187.68, low: 182.06, close: 187.23 },
	    { time: '2018-11-08', open: 187.13, high: 188.69, low: 185.72, close: 188.00 },
	    { time: '2018-11-09', open: 188.32, high: 188.48, low: 184.96, close: 185.99 },
	    { time: '2018-11-12', open: 185.23, high: 186.95, low: 179.02, close: 179.43 },
	    { time: '2018-11-13', open: 177.30, high: 181.62, low: 172.85, close: 179.00 },
	    { time: '2018-11-14', open: 182.61, high: 182.90, low: 179.15, close: 179.90 },
	    { time: '2018-11-15', open: 179.01, high: 179.67, low: 173.61, close: 177.36 },
	    { time: '2018-11-16', open: 173.99, high: 177.60, low: 173.51, close: 177.02 },
	    { time: '2018-11-19', open: 176.71, high: 178.88, low: 172.30, close: 173.59 },
	    { time: '2018-11-20', open: 169.25, high: 172.00, low: 167.00, close: 169.05 },
	    { time: '2018-11-21', open: 170.00, high: 170.93, low: 169.15, close: 169.30 },
	    { time: '2018-11-23', open: 169.39, high: 170.33, low: 168.47, close: 168.85 },
	    { time: '2018-11-26', open: 170.20, high: 172.39, low: 168.87, close: 169.82 },
	    { time: '2018-11-27', open: 169.11, high: 173.38, low: 168.82, close: 173.22 },
	    { time: '2018-11-28', open: 172.91, high: 177.65, low: 170.62, close: 177.43 },
	    { time: '2018-11-29', open: 176.80, high: 177.27, low: 174.92, close: 175.66 },
	    { time: '2018-11-30', open: 175.75, high: 180.37, low: 175.11, close: 180.32 },
	    { time: '2018-12-03', open: 183.29, high: 183.50, low: 179.35, close: 181.74 },
	    { time: '2018-12-04', open: 181.06, high: 182.23, low: 174.55, close: 175.30 },
	    { time: '2018-12-06', open: 173.50, high: 176.04, low: 170.46, close: 175.96 },
	    { time: '2018-12-07', open: 175.35, high: 178.36, low: 172.24, close: 172.79 },
	    { time: '2018-12-10', open: 173.39, high: 173.99, low: 167.73, close: 171.69 },
	    { time: '2018-12-11', open: 174.30, high: 175.60, low: 171.24, close: 172.21 },
	    { time: '2018-12-12', open: 173.75, high: 176.87, low: 172.81, close: 174.21 },
	    { time: '2018-12-13', open: 174.31, high: 174.91, low: 172.07, close: 173.87 },
	    { time: '2018-12-14', open: 172.98, high: 175.14, low: 171.95, close: 172.29 },
	    { time: '2018-12-17', open: 171.51, high: 171.99, low: 166.93, close: 167.97 },
	    { time: '2018-12-18', open: 168.90, high: 171.95, low: 168.50, close: 170.04 },
	    { time: '2018-12-19', open: 170.92, high: 174.95, low: 166.77, close: 167.56 },
	    { time: '2018-12-20', open: 166.28, high: 167.31, low: 162.23, close: 164.16 },
	    { time: '2018-12-21', open: 162.81, high: 167.96, low: 160.17, close: 160.48 },
	    { time: '2018-12-24', open: 160.16, high: 161.40, low: 158.09, close: 158.14 },
	    { time: '2018-12-26', open: 159.46, high: 168.28, low: 159.44, close: 168.28 },
	    { time: '2018-12-27', open: 166.44, high: 170.46, low: 163.36, close: 170.32 },
	    { time: '2018-12-28', open: 171.22, high: 173.12, low: 168.60, close: 170.22 },
	    { time: '2018-12-31', open: 171.47, high: 173.24, low: 170.65, close: 171.82 },
	    { time: '2019-01-02', open: 169.71, high: 173.18, low: 169.05, close: 172.41 },
	    { time: '2019-01-03', open: 171.84, high: 171.84, low: 168.21, close: 168.61 },
	    { time: '2019-01-04', open: 170.18, high: 174.74, low: 169.52, close: 173.62 },
	    { time: '2019-01-07', open: 173.83, high: 178.18, low: 173.83, close: 177.04 },
	    { time: '2019-01-08', open: 178.57, high: 179.59, low: 175.61, close: 177.89 },
	    { time: '2019-01-09', open: 177.87, high: 181.27, low: 177.10, close: 179.73 },
	    { time: '2019-01-10', open: 178.03, high: 179.24, low: 176.34, close: 179.06 },
	    { time: '2019-01-11', open: 177.93, high: 180.26, low: 177.12, close: 179.41 },
	    { time: '2019-01-14', open: 177.59, high: 179.23, low: 176.90, close: 178.81 },
	    { time: '2019-01-15', open: 176.08, high: 177.82, low: 175.20, close: 176.47 },
	    { time: '2019-01-16', open: 177.09, high: 177.93, low: 175.86, close: 177.04 },
	    { time: '2019-01-17', open: 174.01, high: 175.46, low: 172.00, close: 174.87 },
	    { time: '2019-01-18', open: 176.98, high: 180.04, low: 176.18, close: 179.58 },
	    { time: '2019-01-22', open: 177.49, high: 178.60, low: 175.36, close: 177.11 },
	    { time: '2019-01-23', open: 176.59, high: 178.06, low: 174.53, close: 176.89 },
	    { time: '2019-01-24', open: 177.00, high: 177.53, low: 175.30, close: 177.29 },
	    { time: '2019-01-25', open: 179.78, high: 180.87, low: 178.61, close: 180.40 },
	    { time: '2019-01-28', open: 178.97, high: 179.99, low: 177.41, close: 179.83 },
	    { time: '2019-01-29', open: 178.96, high: 180.15, low: 178.09, close: 179.69 },
	    { time: '2019-01-30', open: 180.47, high: 184.20, low: 179.78, close: 182.18 },
	    { time: '2019-01-31', open: 181.50, high: 184.67, low: 181.06, close: 183.53 },
	    { time: '2019-02-01', open: 184.03, high: 185.15, low: 182.83, close: 184.37 },
	    { time: '2019-02-04', open: 184.30, high: 186.43, low: 183.84, close: 186.43 },
	    { time: '2019-02-05', open: 186.89, high: 186.99, low: 184.69, close: 186.39 },
	    { time: '2019-02-06', open: 186.69, high: 186.69, low: 184.06, close: 184.72 },
	    { time: '2019-02-07', open: 183.74, high: 184.92, low: 182.45, close: 184.07 },
	    { time: '2019-02-08', open: 183.05, high: 184.58, low: 182.72, close: 184.54 },
	    { time: '2019-02-11', open: 185.00, high: 185.42, low: 182.75, close: 182.92 },
	    { time: '2019-02-12', open: 183.84, high: 186.40, low: 183.52, close: 185.52 },
	    { time: '2019-02-13', open: 186.30, high: 188.68, low: 185.92, close: 188.41 },
	    { time: '2019-02-14', open: 187.50, high: 188.93, low: 186.00, close: 187.71 },
	    { time: '2019-02-15', open: 189.87, high: 192.62, low: 189.05, close: 192.39 },
	    { time: '2019-02-19', open: 191.71, high: 193.19, low: 191.28, close: 192.33 },
	    { time: '2019-02-20', open: 192.39, high: 192.40, low: 191.11, close: 191.85 },
	    { time: '2019-02-21', open: 191.85, high: 192.37, low: 190.61, close: 191.82 },
	    { time: '2019-02-22', open: 191.69, high: 192.54, low: 191.62, close: 192.39 },
	    { time: '2019-02-25', open: 192.75, high: 193.42, low: 189.96, close: 189.98 },
	    { time: '2019-02-26', open: 185.59, high: 188.47, low: 182.80, close: 188.30 },
	    { time: '2019-02-27', open: 187.90, high: 188.50, low: 183.21, close: 183.67 },
	    { time: '2019-02-28', open: 183.60, high: 185.19, low: 183.11, close: 185.14 },
	    { time: '2019-03-01', open: 185.82, high: 186.56, low: 182.86, close: 185.17 },
	    { time: '2019-03-04', open: 186.20, high: 186.24, low: 182.10, close: 183.81 },
	    { time: '2019-03-05', open: 184.24, high: 185.12, low: 183.25, close: 184.00 },
	    { time: '2019-03-06', open: 184.53, high: 184.97, low: 183.84, close: 184.45 },
	    { time: '2019-03-07', open: 184.39, high: 184.62, low: 181.58, close: 182.51 },
	    { time: '2019-03-08', open: 181.49, high: 181.91, low: 179.52, close: 181.23 },
	    { time: '2019-03-11', open: 182.00, high: 183.20, low: 181.20, close: 182.44 },
	    { time: '2019-03-12', open: 183.43, high: 184.27, low: 182.33, close: 184.00 },
	    { time: '2019-03-13', open: 183.24, high: 183.78, low: 181.08, close: 181.14 },
	    { time: '2019-03-14', open: 181.28, high: 181.74, low: 180.50, close: 181.61 },
	    { time: '2019-03-15', open: 182.30, high: 182.49, low: 179.57, close: 182.23 },
	    { time: '2019-03-18', open: 182.53, high: 183.48, low: 182.33, close: 183.42 },
	    { time: '2019-03-19', open: 184.19, high: 185.82, low: 183.48, close: 184.13 },
	    { time: '2019-03-20', open: 184.30, high: 187.12, low: 183.43, close: 186.10 },
	    { time: '2019-03-21', open: 185.50, high: 190.00, low: 185.50, close: 189.97 },
	    { time: '2019-03-22', open: 189.31, high: 192.05, low: 188.67, close: 188.75 },
	    { time: '2019-03-25', open: 188.75, high: 191.71, low: 188.51, close: 189.68 },
	    { time: '2019-03-26', open: 190.69, high: 192.19, low: 188.74, close: 189.34 },
	    { time: '2019-03-27', open: 189.65, high: 191.61, low: 188.39, close: 189.25 },
	    { time: '2019-03-28', open: 189.91, high: 191.40, low: 189.16, close: 190.06 },
	    { time: '2019-03-29', open: 190.85, high: 192.04, low: 190.14, close: 191.89 },
	    { time: '2019-04-01', open: 192.99, high: 195.90, low: 192.85, close: 195.64 },
	    { time: '2019-04-02', open: 195.50, high: 195.50, low: 194.01, close: 194.31 },
	    { time: '2019-04-03', open: 194.98, high: 198.78, low: 194.11, close: 198.61 },
	    { time: '2019-04-04', open: 199.00, high: 200.49, low: 198.02, close: 200.45 },
	    { time: '2019-04-05', open: 200.86, high: 203.13, low: 200.61, close: 202.06 },
	    { time: '2019-04-08', open: 201.37, high: 203.79, low: 201.24, close: 203.55 },
	    { time: '2019-04-09', open: 202.26, high: 202.71, low: 200.46, close: 200.90 },
	    { time: '2019-04-10', open: 201.26, high: 201.60, low: 198.02, close: 199.43 },
	    { time: '2019-04-11', open: 199.90, high: 201.50, low: 199.03, close: 201.48 },
	    { time: '2019-04-12', open: 202.13, high: 204.26, low: 202.13, close: 203.85 },
	    { time: '2019-04-15', open: 204.16, high: 205.14, low: 203.40, close: 204.86 },
	    { time: '2019-04-16', open: 205.25, high: 205.99, low: 204.29, close: 204.47 },
	    { time: '2019-04-17', open: 205.34, high: 206.84, low: 205.32, close: 206.55 },
	    { time: '2019-04-18', open: 206.02, high: 207.78, low: 205.10, close: 205.66 },
	    { time: '2019-04-22', open: 204.11, high: 206.25, low: 204.00, close: 204.78 },
	    { time: '2019-04-23', open: 205.14, high: 207.33, low: 203.43, close: 206.05 },
	    { time: '2019-04-24', open: 206.16, high: 208.29, low: 205.54, close: 206.72 },
	    { time: '2019-04-25', open: 206.01, high: 207.72, low: 205.06, close: 206.50 },
	    { time: '2019-04-26', open: 205.88, high: 206.14, low: 203.34, close: 203.61 },
	    { time: '2019-04-29', open: 203.31, high: 203.80, low: 200.34, close: 202.16 },
	    { time: '2019-04-30', open: 201.55, high: 203.75, low: 200.79, close: 203.70 },
	    { time: '2019-05-01', open: 203.20, high: 203.52, low: 198.66, close: 198.80 },
	    { time: '2019-05-02', open: 199.30, high: 201.06, low: 198.80, close: 201.01 },
	    { time: '2019-05-03', open: 202.00, high: 202.31, low: 200.32, close: 200.56 },
	    { time: '2019-05-06', open: 198.74, high: 199.93, low: 198.31, close: 199.63 },
	    { time: '2019-05-07', open: 196.75, high: 197.65, low: 192.96, close: 194.77 },
	    { time: '2019-05-08', open: 194.49, high: 196.61, low: 193.68, close: 195.17 },
	    { time: '2019-05-09', open: 193.31, high: 195.08, low: 191.59, close: 194.58 },
	    { time: '2019-05-10', open: 193.21, high: 195.49, low: 190.01, close: 194.58 },
	    { time: '2019-05-13', open: 191.00, high: 191.66, low: 189.14, close: 190.34 },
	    { time: '2019-05-14', open: 190.50, high: 192.76, low: 190.01, close: 191.62 },
	    { time: '2019-05-15', open: 190.81, high: 192.81, low: 190.27, close: 191.76 },
	    { time: '2019-05-16', open: 192.47, high: 194.96, low: 192.20, close: 192.38 },
	    { time: '2019-05-17', open: 190.86, high: 194.50, low: 190.75, close: 192.58 },
	    { time: '2019-05-20', open: 191.13, high: 192.86, low: 190.61, close: 190.95 },
	    { time: '2019-05-21', open: 187.13, high: 192.52, low: 186.34, close: 191.45 },
	    { time: '2019-05-22', open: 190.49, high: 192.22, low: 188.05, close: 188.91 },
	    { time: '2019-05-23', open: 188.45, high: 192.54, low: 186.27, close: 192.00 },
	    { time: '2019-05-24', open: 192.54, high: 193.86, low: 190.41, close: 193.59 },
        ]);

i'm going to put it in a temporary file real quick just so i can study it
so it looks like they do time open high low and close, and then also it has a lot of scale information, we should probably just take this one actually instead as our example

so i'm gonna go back to chart.js and let's try this one, 

createChart, and then we'll do document.getelementbyid again, and we'll use chart there, and let's just
use the actual style that we're using right, and there you go, i refreshed it and now i have a zoomable candlestick chart, which is in our webpage, and then i can also refresh our page,

and let's say i want to reconnect to this websocket and i also want to append price data to my trade div
and i can get that going again and then what we're going to want to do is start interacting with our chart and we're going to append this price data to this candlestick series

and we're going to gradually hook that up, um i'm not quite ready to do that, i don't really feel like doing that yet so, i'm going to comment this back out, and i'm not as much in the ui mode at the moment so i just want to get this started so that we can move on to the python portion

okay next let's put in some placeholders on the ui to accept some user input,
let's say the user wants to configure some indicators they're interested in uh on their custom, on this uh custom trading platform, right

and so under the trades div let's do an id for 'settings' and this will be a place to store all of our settings right, and so i'll do an h3, and just say 'settings' right and then here let's just put some options the user can configure, and let's say this thing it's going to hold some indicators that the user is interested in

so i'm going to say input type equals text and let's say label and let's say you know we have a simple RSI indicator right, so that's RSI um and we can let's just add another div there just to give it a little bit of room right, so we have an rsi setting right, and so let's see what the settings look like in trading view for instance and we can just uh make this kind of work similarly, so i'm going to go to markets on trading view, i'm going to go to bitcoin, and then let's click this guy and then let's look at the full featured chart

so you see, i have this RSI indicator already up so i'm going to close it real quick, and then i'm going to add it back so i'm going to click f of x here
or this, yeah indicators and strategies button, and then if i do relative strength index right
that'll add it to my chart and you see we have this rsi oscillator on the chart and maybe we'll figure out how to add that to the chart visually 

but i'm mainly interested in the settings they let you configure,  and so let's see so over here, i hover
click little gear and it looks like they let you set a couple inputs you can do the length or the source

so i'll just let it let's do the length, right, so i'll do name equals 'rsi length' and then id oops
and then i'll give it an id to id equals 'rsi length' right, and that'll just be a setting and
let's say we also need want a checkbox to say we're interested in using this indicator so

i'll just do input type equals checkbox and i'm going to save a lot of the details for a bit
for a little bit later i just want to sketch out the baseline for a ui right, so we got a checkbox here and i'm just going to put them all in one line

so i'm just going to do rsi and then i'll put next to it the check box so i'll put check box then i'll put the rsi and then i'll put the text box right next to it like that and then let's just do it all
in one line right

so i'm interested in the rsi right and i can type like a 14 there, so i can do like a placeholder equals 14. right 

so that'll be a setting for the period right, and i believe there should be an overbought oversold so they're using 30 and 70 so also make a little input for type equals text, and i'll call this id equals 'rsi oversold' and then i'll do name equals 'rsi oversold' and then i'll do placeholder equals 30 and that'll be like a threshold this below 30 is when it's oversold and then i'll also do input type equals
text id equals 'rsi overbought' right and then placeholder equals 70. so let's say we just have this configurable rsi indicator component that's on our ui, the user can tweak whether or not they want to use it, what the period is and the overbought and oversold thresholds, right 

and let's put a label there 'Oversold' and 'Overbought' and i will put i want to put 'Overbought' on top
let's see that 

all right cool so we have a few settings here and we have a chart, and so i'm feeling pretty good about that, so i'm not going to hook this all up yet, 
what i want to do is start working on a backend for this, so i'm going to use python and do the same thing try to connect to the web sockets
but also i'm going to explore the rest api for binance in the next video, download some historical data and actually use rsi and some other indicators from TAlib

and then you hook that up into Backtrader to backtest those indicators against some historical data

and then we're gonna tie that all together by hooking up this ui to the real data and to the binance api to place some trades 

so i think that's it for this video so stay tuned for the next one and we're going to dive into some python











Binance API Tutorial (Part  4) - Historical candlestick Data and the Python Binance Package

https://www.youtube.com/watch?v=FmfTK5dFOZk&t=8s





hey everyone welcome back to another video and happy Memorial Day 

today we're going to continue the series on Binance by using the Python binance package, in order to retrieve current and historical candlestick data 
Using the Python binance package, we're going to start by figuring out how to authenticate using our API key and API secret, and then we'll see if we can retrieve some current candlesticks
So that we can use those to initialize our lightweight charts that we created in our last video

and then we'll see about downloading some historical candlestick data that we can use to get maybe data for the past year, 
so and run that through some technical analysis libraries, such as TAlib right and so we want to try running some of these TALib indicators against this data set,
and also try to hook up this TALib to Backtrader and it's back tests those indicators against our historical data set 

so let's get started before we jump too far ahead, let's just start with the basics
so what I'm gonna do is, when you google user type by python binance right, that'll bring you to this Python package, and I'm going to go to this read the docs page here 

        https://python-binance.readthedocs.io/en/latest/

and this is just a Python package like any other, it's a wrapper for the binance API, and it makes it very easy for you to call the binance API using just basic Python functions and objects 

so just like any other package we've covered in the channel, all you have to do is pip install the name of the package :

        $ sudo apt install python3-pip

        $ pip install python-binance

so it's python - binance, pip install python-binance and you can see I've installed it already, and then the second thing you need to do is go to your dashboard, for binance, and what you can do is click
settings here and there'll be a sub tab here that says API information or something along those lines actually I'll go ahead and click it and type API management ya and I can delete this key later so it's not that big of a deal so what you want to do yeah let's go ahead and create one and it looks like I can just show you I can just show you it 

so Binance, and I just give it a name, I send myself an SMS text 

all right so I got my API key and my API secret after I verified an SMS text message and I also had to do a verification via my email address in order to make sure the API key was going to me
and so now that I have that API key, what I do is create a file in my directory called config dot py 

        config.py

here's a sample_config dot py just to show you and all you need to do is paste your API key and we're just going to create a variable called API key and API secret, and put our actual keys in there, and so I've already done that, I've placed it in a file called config dot py, and then what I'll be able to do is create a new script also called, let's just call it
get_data 

        get_data.py 

and we're gonna just test out the Binance API, and make sure we can connect so let's go back to this Python Binance package, and I'm going to scroll down a bit, and so you see we've already installed Python binance and so it looks like the first step you need to take, is you got to import the package:

        from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
        client = Client(api_key, api_secret)

after its installed, so you have from binance import Client and then you just make a new instance of Client, a Client object, and let's see

so it takes an API key an API secret, so what I want to do is import my config, very simple, and since my config has an API key and API secret,
I will just plug that in, so config dot API key and config dot API secret,

        client = Client(config.API_KEY, config.API_SECRET)

and so I should have a client, and so let's test that we can actually successfully authenticate, and retrieve some information 

so it looks like the first method that give us, is an example, is this get all tickers, and so let's see what that looks like 

        # get all symbol prices
        prices = client.get_all_tickers()

prices equals client dot get_all_tickers, ok and so, yeah let's just print prices, let's see if this returns anything 

        print(prices)

all right, so I will hit play, or type python get data dot py:

        $ python3 get_data.py

and look at that, we have a whole bunch of data and it looks like it's in a list,
so I can just do for price in prices, right, and we'll just traverse that list and display them each on a line

        for price in prices:
          print(price)

so I'll clear that out, and let's run it again

        $ python3 get_data.py

and look at that, all kinds of, yeah, all kinds of crypto coins that I've never even heard of,
so yeah, we're gonna take something simple here, like, the Bitcoin US dollar one, and we're gonna use that, but just see you know,
there's tons of priced it in here about look 'Ethereum' and maybe 'rubles', all kinds of currencies that I've never used here

so that's great, so this package has many different endpoints available, you see there's 'General endpoints' 'Market Data Endpoints' 'Account Endpoints',
a lot of different stuff that's provided, but for this tutorial what I'm mainly interested in, is the 'market data', specifically we want to get some candlestick data, both
the current days candlestick data, so we could initialize our lightweight charts, but also some historical data so that we can use it to do back testing and things like that

        https://python-binance.readthedocs.io/en/latest/market_data.html

So looks like there's this historical candlestick function here 

        'Get Kline/Candledsticks'
        'Get Historical Kline/Candlesticks'

        https://python-binance.readthedocs.io/en/latest/market_data.html#id6

and so let's see what that does.

so get, get Klines here, 

        'Get Kline/Candlesticks'

        candles = client.get_klines(symbol='BNBBTC', interval=Client.KLINE_INTERVAL_30MINUTE)

so let's see that, let's try this first one, for candles, so I'm going to do, and get Klines,
so candles equals clients like get_klines and I believe if we wanted Bitcoin USDT is what we've been using, and then looks like this is a they have a variety of constants here,
so I could do Client dot Kline you can see I can use any of these constants to get data about whatever interval I'm interested in 

so if I want a day-by-day candlesticks, or hourly candlesticks, or the meet up-to-the-minute I could do that
but let's say I just want 15 minutes for instance

        # get Kline/Candlesticks
        candles = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

all right, and for that particular symbol, and let's see, let's try that, let's see what we get 

So we print the candles there, 

        print(candles)

and let's run it, all right that was pretty fast, so this is a bit hard to read, so let's try to break this down a little bit, and see what we have
So the first thing I'll do is print the length of candles just to see how many this returns by default 

        print(len(candles))

and then I'm also going to print them a line by line, 

        for candlesticks in candles:
          print(candlesticks)

so for candlestick in candles, let's print the candlestick, right
and when I run that, you see we have them line by line
so quite a bit of them and so I'm gonna print the length at the end, and then we'll just look at the format

let's see in the documentation what this a data format is 
so I'm gonna do that, I'm gonna run it one more time

all right, so it looks like it gave us 500 x 15-minute candlesticks, and so this isn't a dictionary that has any kind of labels
so it looks like they're just, it's just a list of lists 

so I want to know which one of these numbers correspond to what, just by glance, this looks like a UNIX timestamp, and then some of these are probably open high low and close, so let's go ahead and check the documentation, to see what all of these are 

so I'm going to go over here and then in the Binance documentation, the official Doc's here on github,

        'binance-docs github'
        https://binance-docs.github.io/apidocs/futures/en/#change-log

        'Market Data Endpoints'
        https://binance-docs.github.io/apidocs/futures/en/#market-data-endpoints

        'Kline/Candlestick Data'
        https://binance-docs.github.io/apidocs/futures/en/#kline-candlestick-data


you can see there's this Kline/Candlestick Data endpoint,
and then the response here:

        Response:

        [
          [
            1499040000000,      // Open time
            "0.01634790",       // Open
            "0.80000000",       // High
            "0.01575800",       // Low
            "0.01577100",       // Close
            "148976.11427815",  // Volume
            1499644799999,      // Close time
            "2434.19055334",    // Quote asset volume
            308,                // Number of trades
            "1756.87402397",    // Taker buy base asset volume
            "28.46694368",      // Taker buy quote asset volume
            "17928899.62484339" // Ignore.
          ]
        ]


they actually have it documented, and so it's a list of lists, and then yeah as we suspected, there is a timestamp and that looks like it just goes in order,
so open high/low close, and then yeah we have some information about the volume

so now that we know the structure of the candlesticks, what we'll do is write that information to a file, that we can use in Backtrader or another system,
so let's remind ourselves, I always forget, so let's look up Python, the csv module, right 

        'python write csv'

        https://docs.python.org/3/library/csv.html


and let's just see how we write to a csv file right 
so we just import the CSV package which is built into Python 

        import csv

and let's open a file for writing right 

        open('eggs.csv', 'w', newline='')

so we can take this and we just want to open a file, and we'll call it 15 minutes dot CSV, and we're writing it to a file, and so we're gonna define the file as f right 

        f = open('15minutes.csv', 'w', newline='')

and then all we got to do is write a row, so let's write a row, so we want a csv writer, and the ability to write a row right 

        spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

so it's a csv writer, so we're gonna call this a candlestick writer right, a candlestick writer, and that's a csv writer, we give it a reference to our file,
So yeah we'll just call this csv file just like that 

        csvfile = open('15minutes.csv', 'w', newline='')

so we're writing to the CSV file the delimiter, we'll use a comma 
we don't need any of this quoting stuff because we're not using quotes these are just numbers 

so I think we just need a file handle and a writer and then we just need to specify the delimiter,
and then looks like we just write rows right 

so let's see what right row looks like, it looks like you can just set, passing a list and it'll convert that to a CSV file 

        csvfile = open('15minutes.csv', 'w', newline='')
        candlestick_writer = csv.writer(csvfile, delimiter=',')

so let's do a candlestick writer right row and then

        for candlesticks in candles:
          print(candlesticks)

          candlestick_writer.writerow(candlesticks)
        
        print(len(candles))

we'll do candlestick right, yeah we could specify them individually too, we could do like candlestick[0], candlestick[1] right, 
or we can just pass the entire list 
so let's try it this way, let's just pass the entire candlestick and let's see what we get 

so I'm gonna do that right, and look at that, so we have this 15minute.csv appeared, right 

        15minutes.csv

and so we have a CSV file from Binance there right

so that looks pretty good and that gives us the timestamp, open high, low, and close
that we can run through whatever software we want, we can load it to later into the (appendix)? data frame, or use backtrader, or whatever we want, all right 

so let's go ahead and get a much larger data set, 
so let's say I want all the 5-minute candlesticks from the past year or so 
so let's do that 
so we have this Kline's function but there's also this historical data, 

        https://binance-docs.github.io/apidocs/futures/en/#recent-trades-list

        Old Trades Lookup (MARKET_DATA)
        
        GET /fapi/v1/historicalTrades

        Get older market historical trades.

            Response:

            [
              {
                "id": 28457,
                "price": "4.00000100",
                "qty": "12.00000000",
                "quoteQty": "8000.00",
                "time": 1499865549590,
                "isBuyerMaker": true,
              }
            ]

so let's go here  historical data 

        https://python-binance.readthedocs.io/en/latest/market_data.html#id7

        Get Historical Kline/Candlesticks

        Fetch klines for any date range and interval

        # fetch 1 minute klines for the last day up until now
        klines = client.get_historical_klines("BNBBTC", Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")

        # fetch 30 minute klines for the last month of 2017
        klines = client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_30MINUTE, "1 Dec, 2017", "1 Jan, 2018")

        # fetch weekly klines since it listed
        klines = client.get_historical_klines("NEOBTC", Client.KLINE_INTERVAL_1WEEK, "1 Jan, 2017")

and yeah, we can get a lot of candlesticks, so let's comment out some stuff, 
so let's go candlesticks equals a client get historical kay lines and then we'll also get Bitcoin USDT and then we can get, past it and interval, or we can pass it the state range here,
so grab that part, I'll just do five minute I don't think I need one minute, and then let's go from December of 2017, now let's go even further than that, let's go January of 2012 to May 24th 2020,

        # fetch 5 minute klines interval for the 1st january of 2012 day to May 24th 2020
        candlesticks = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "24 May, 2020")

and let's see how it handles that, that's a lot of data, right, five minute data for like eight years (worth)? of data, so let's try that again
and then I'll do you for candlestick in candles, and let's create a new file

I'm going to get rid of this 

        # csvfile = open('15minutes.csv', 'w', newline='')

        # for candlesticks in candles:
        #   print(candlesticks)

        #   candlestick_writer.writerow(candlesticks)

        # print(len(candles))

and then I'm gonna write it to a file called 2012 to 2020 dot CSV 

        csvfile = open('2012-2020.csv', 'w', newline='')

and that'll be my candlestick writer, and then we can just write we can write this to the file, 
candlestick_writer and candlesticks 

        for candlestick in candlesticks:
          candlestick_writer.writerow(candlesticks)

and we'll writerow, and then, we can also close the file as well

so CSV file dot close right 

        csvfile.close()

all right so let's run that, and that might take a little while to run for candlestick and candlesticks, and let me close those parentheses right 
I'm gonna run that and let it run for a while, let's see how quick this happens

all right so I took a quick break and came back, I think that ran for a minute or two, and then now if I come back, you see I have this 2012 to 2020 CSV file right 
and it looks like there's tons of data in here, like what, almost a few hundred thousand lines here, a few hundred thousand candlesticks, 
so those are 5-minute candlesticks and let's just double check on the range it gave me, 

so if I go to UNIX timestamp right, and let's display what that looks like 
we have looks like it gave me data starting at AUGUST 17 2017 which is you know about, yeah we've got, nearly three years worth of data

I'm not sure we asked for from the year 2012 but it looks like I only gave us a few years, so I'm not sure if that's due to, there being some maximum number of data points you can request at one time
or if it it's due to just the symbol we use, to maybe there's not a data going back that far in Binance at least and so
yeah I'm not sure the reason that yet for that yet, but you know we had three years of data, three years of five minute candlestick data which, 
you know if you can't do anything with that then, you know what's the point, so yeah, we have a few hundred thousand data points to work with 
so that that should be good enough for what we want to do

so I think it's been, it's been at least 10 or 15 minutes, so I'm hearing the ideal length for a YouTube video is around 10 or 15 minutes
so I'm gonna stop it there

We showed you how to use the Binance Python package in order to connect to the Binance API
and we're able to download some historical data to a file, and so we have this historical data set in a CSV file of all this five-minute candlestick data 

so in the next video, let's try to process these candlestick files, and try to run them through some TAlib indicators 
so the next video I think I'm gonna focus on using TAlib 
so I'm going to install that, and try some of the built-in indicators to see what I think about it, and also maybe explore some other packages as well, 
there might be some newer Python packages for technical analysis that I'm not aware of,
so I'd like to try that as well 

so thanks a lot for watching and stay tuned for the next video










Binance API Tutorial (Part  5) - Python TALib RSI indicator (16:36)

https://www.youtube.com/watch?v=0XQjgmChtE4&t=50s




All right let's keep going

So in the last video we downloaded some historical Bitcoin data using the by Binance API 

so in this video we're gonna see if we can apply some technical analysis to that data using a package called TALib 
 
so I think TALib is actually written in C or C++, but there's actually a Python 'wrapper' for TALib, so I have it pulled up here 

        https://mrjbq7.github.io/ta-lib/

so if you go to ta - lib dot org, 

        https://ta-lib.org/

it will pull up the technical analysis library, so this is actually I believe written in C or C++ originally, but there's a Python wrapper around it, that allows you to use the same functions

        https://ta-lib.org/function.html

so if you browse through this website you'll see it has a variety of indicators that are built in, including you know Bollinger Bands, you can detect various candlestick patterns,
there's some volume, on beyond balance volume, a relative strength index RSI, a whole bunch of different indicators that you can use in your own programs

and although this library is fairly old, you know these indicators are nothing new, many of them are invented many decades ago so they still apply today 
so now

I've searched for Python TALib and you'll see we get the Python wrapper for TALib 

        https://mrjbq7.github.io/ta-lib/

and it has some installation instructions here, and so, here's how you install it, so you click this 

        Install TA-Lib

        https://mrjbq7.github.io/ta-lib/install.html

and I'm installing this on Mac OSX, so if you're following along, you should be able to do what I'm doing 
I can't install it on every operating system, but there should be installation instructions for whatever operating system you're on 

I've heard it can be a little bit tricky depending on your OS, but I verified that this works
so I'm gonna I'm going to go to visual studio code for instance, and there's this just like any other Python package there's pip install TA-Lib 
so I'm gonna do that TA Lib right 

        Installing TA-Lib on Ubuntu

        https://artiya4u.medium.com/installing-ta-lib-on-ubuntu-944d8ca24eae

        # Installing TA-Lib on Ubuntu

                $ sudo apt install build-essential wget -y

        # Download and extract the source code

                $ wget https://artiya4u.keybase.pub/TA-lib/ta-lib-0.4.0-src.tar.gz
                $ tar -xvf ta-lib-0.4.0-src.tar.gz

        # Config and build from source.

                $ tar -xvf ta-lib-0.4.0-src.tar.gz
                $ ./configure --prefix=/usr
                $ make
        
        # Install to system

                $ sudo make install

        # sudo make install

                $ sudo pip install TA-Lib

        or

        # All in one script

                #!/usr/bin/env bash
                sudo apt install build-essential wget -y
                wget https://artiya4u.keybase.pub/TA-lib/ta-lib-0.4.0-src.tar.gz
                tar -xvf ta-lib-0.4.0-src.tar.gz
                cd ta-lib/
                ./configure --prefix=/usr
                make
                sudo make install


and so I'm gonna

install that and you'll see it's

installed and now I'll notice this if I

run Python 3 and try to import it it

gives me this error it says image not

found so it throws some errors here so

one thing there's actually a dependency

so if you scroll down here on OSX you

should have something called homebrew

right

homebrew for OSX and so if you have that

installed it's a package manager for OSX

and there's actually a dependency here

so you want to make sure you have this

installed so if you type brew install ta

live like this

using homebrew this will install a ta

Lib dependency so you see it that's look

quick download for the Mac OSX version

that I'm on and installs it right and so

now I'm gonna rerun python 3 and import

TALib and you'll see there's no error

there so it looks like I've successfully

installed it so let's see what we can do

with that ok so I'm gonna close up some

of this stuff that already had open so

close that that and yeah we have a bunch

of difference no pads that I have to

open so I'm going to start a little more

fresh here so we have our chart and we

ever read me and I won't save that's

alright cool so let's let's let's try ta

PI and let's see if we can use this

library now so let's see if we can find

like a hello world example using TALib

so it looks like it imports numpy so

let's go ahead and add a requirements

text here to this project

and it looks like I've used a Python

finance so far and I've used a TALib

and that is TALib like that so I'll add

that in there and also it looks like we

need numpy so I'll put that in there I

believe I already have numpy installed

but just in case I'll do pip3 install

numpy right and so numpy is just a

library scientific computing library so

it looks like TALib accepts numpy

arrays okay so now that I know all my

packages are installed I'm going to

close that and look at my ta PI and

let's just take this little example here

and make sure we can import numpy and ta

lib right so we're setting a value

called close where a variable called

close equal to num PI dot random 100 and

let's see what that does right

I'm going to print close so I'm going to

run that and you see it generates this

list structure with a bunch of random

numbers and it looks like it's just

numbers between zero and one there's all

decimals so well is this a list or is it

an array or what's it what's a numpy

array so let's let's look that up what

is the difference between a numpy array

and a list so a numpy array it says it's

a grid of values and it's indexed by a

tuple of non-negative integers a list in

Python it's equipment array but as

resizable and contained elements so what

is the real difference here so it looks

like numpy arrays are actually optimized

for memory consumption and have a bunch

of optimizations for spaced memory speed

and calculations so looks like numpy is

just faster for some scientific

computing so if you're multiplying these

huge lists or these huge arrays of

millions of numbers and performing all

this floating-point arithmetic and

matrix operations and so forth it's

designed for the scientific computing

purposes so looks like TALibs since

it's for technical analysis chose to use

numpy arrays as it's for all of the data

types that it operates on so we have a

number array here of 100 random numbers

here

all right so an array of 100 numbers

it's not that interesting

but what is interesting is that we can

build up a numpy array of closing prices

for Bitcoin for instance or closing

prices for the S&P 500 and we can have

those in a numpy array as a sequence and

then we can use TALib to operate on

that sequence of values and apply all

the different built-in functions and

indicators that ta lip has and let it

perform calculations for us so what's an

example right so let's pretend we have a

sequence

yeah let's still do it on this random

number first and so let's look at the

docs and looks like the simplest example

right is a moving average everyone

understands that it just gets the

average of the previous you know ex

periods right and so if I paste that in

right we have our moving average equals

TALib and it has dot s ma so there's a

bunch of indicators built in so I could

do TALib RSI for instance and that's

one of the built-in functions right and

so yeah let's see what the simple moving

average is of this numpy array which is

just an array of closing values right

and so if I print moving average here

and I run this again you'll see

previously if we have this array of 100

numbers and then if you look at the

second array which is the moving average

you can see a bunch of nada numbers here

so there's 1 2 3 4 5 6

24:29 so there's not a number a value

here until the 30th a slot in this array

and so what that means is by default it

uses the 30 day SMA so there's not an

average to take until 30 elements in and

then at the 31st element you know it

does the previous 30 before those so

it's just an average that rolls through

this entire sequence right and so let's

see how we might adjust that a little

bit so let's see indicators momentum

indicators and so SMA if we're correct

it's yeah so it's on overlap studies

here and so if we look at 30 day at SMA

here you can see the time period as we

thought

by default based on our analysis that's

the default time period is 30 but let's

say we wanted the 10 10 day moving

average for instance so we'll do time

period equals 10 and I'll run it again

and you'll see the first nine slots are

not a number and then we have an average

of the first 10 values so that's how you

calculate a moving average using TALib

so you might not care moving average

very simple you don't need a special

library for that it's just an average so

let's let's start getting more and more

complex a lot of these are actually very

simple even you know RSI very simple

calculation so let's go to momentum

indicators here and let's go to relative

strength index and so this is a way to

calculate the RSI and so what we can do

now is do RSI equals t a lift RSI close

and then looks like the time period by

default is 14 so I like that value and

so let's just print the RSI so I run

again and you see we have a bunch of

varying values there random numbers

and so the RSI 14 and it looks like it's

you know this is just some random

numbers so the it's never really

overbought or oversold we just have some

values that are like 40 or 50 so if we

use that with some real price data we'll

probably be able to see some overbought

or oversold values so overbought is

usually over 70 and oversold is below 30

so these random numbers aren't very

interesting so let's see if we can use

some of the Bitcoin price data that we

downloaded in the last video so I have

this 15-minute CSV I already forgot what

time period that was for let me see

let's get that real quick and we can

just see if there's some overbought or

oversold values so we can calculate the

RSI for this particular time period of

prices so this is from May 20th until

let's see maybe we have May 20th through

May 25th so we should get be able to

pull out some overbought and oversold

values from there and so let's figure

out how we can load this 15-minute CSV

data and to get the open high low close

let's see if we can get the closing

prices into a numpy array and run this

RSI indicator on that so let's see how

we do that so I will use Google and I

type build numpy array from CSV and

let's see what it gives me so it looks

like there's this Jen from text function

so I will import that and I'll say my

data equals Jen from text and I'll try

this 15 minutes dot CSV and we give it a

delimiter of comma and yeah let's print

that out and see how it works let's see

if that gives us what we need so I'm

going to comment out some stuff here and

print just that my data there all right

so I'm gonna run it again all right so

look at that so we have a lot of so it

looks like an array of arrays which is

good and this first index from each list

is the timestamp and then we have some

prices so that's like nine thousand six

hundred twenty three because you see

that exponent it's like

e to the third ten to the third and then

yeah so it looks like that worked

we're able to pull in an array of numpy

arrays using this Jen from TechSoup

function right so the next thing I want

to do I want just with the closing value

from here so we have time stamp open

high/low close and so I want the 0 1 2 3

the 4th 4th value here I don't I'm not

really that interested and all these

other ones I want to use the closing

price so I want to extract you know this

value this value this value all the way

down like this entire column of data and

so let's look up how we do that right so

how to import a CSV file it's numpy

array and it looks like you can access

this sequence like this so let's try

that syntax just like accessing a list

like that so we're gonna say the 0 1 2 3

4 0 1 2 3 4 all right cool so we want

the closing price low so let's see if we

say the closing price is my data and

then we have a colon and a 4 there and

let's print the close I run that and

spell it correctly and look at that so

let's see is that correct yeah nine

thousand six hundred fourteen eighty

seven nine thousand four 14.5 nine

sixteen eighty seven nine four four

fourteen fifty 9470 so that's great so

we have a sequence of this closing price

in these 15-minute candles and we have

it in a single numpy array which is

great so and then this was the 15-minute

sharks and so let's see if we apply our

RSI indicator to that so tle RSI for the

close of our Bitcoin data and then we

print the RSI I'm gonna run it so you

have a lot of different values here that

are between 0 and 100 so these are RSI

values and let's see if we can find any

points at which the price was overbought

or oversold so you'll see here near the

end there's a case where the RSI was

above 70 which would be overbought

so let's see if we can verify that using

the data so we'll go one two

three four or five data points back so

if you go back five data points so from

the end so you'll see that the value is

Duke one two three four five so 8950

here was when it was overbought and so

if you look before that you would expect

prices to be rising rapidly so there was

probably a lot of momentum leading to an

overbought State and so let's see if

those numbers rose and if that's correct

right so you'll look look at that so we

have you'll see it was eighty seven

fifty five a seven sixty nine a 789 and

so it was rising until it's eighty eight

hundred then kept rising into eighty

eight hundreds and then went all the way

to eighty nine fifty so there was a lot

of momentum upward there leading to an

overbought state and also let's see if

we can validate that let's try something

like a trading view right and then let's

see what date and time that corresponds

to so that was May 25th which is today

and that was around 12:15 p.m. Pacific

so I'm going to pull up the

cryptocurrency data for Bitcoin right

and let's see Bitcoin UST et and I'm

gonna go to the fully featured chart

here and let's try to pull up the RSI

and compare so what we got from TALib

just to verify we're doing this

correctly so I'm going to look at the

15-minute chart and then I already have

the RSI pulled up and if you look here

sure enough at 12:15 here it looks like

this is where that overbought condition

occurred which was when Bitcoin was

about eighty nine fifty so you see this

run here this led to the overbought and

so you see this RSI at the bottom and

then it rose and briefly went above

seventy okay so I think I'm going to end

the video here this one's running a bit

long I'm trying to keep every video

between ten and fifteen minutes or so

this one's already over fifteen minutes

and I feel pretty good about what we

covered so far we showed how to install

the TALib library as a Python package

we showed how to read in some data using

an umpire arrays so we read in our

Bitcoin historical price data into a

numpy array and then we were able to run

some TALib indicators against this

numpy array so we were able to calculate

a simple moving average using TALib and

we're also able to calculate the RSI and

determine a point at which Bitcoin price

was overbought today and we compared

that against this graph this RSI

indicator in trading view just to

confirm our analysis was correct and we

were able to detect when this price rose

here from 8702 8950 and confirm that the

RSI went above 70 at that point in time

so it looks like we have a pretty good

idea of how to use CA lib indicators so

I'm gonna stop it here and in the next

video we're gonna continue our

discussion of TALib and try to combine

it with back trader for back testing and

maybe we'll cover some more indicators

and see what happens when we buy and

sell Bitcoin based on these indicators

and see what our results would be when

initializing an account with a certain

balance of say $100,000 so stay tuned

for the next video and thanks for

watching










