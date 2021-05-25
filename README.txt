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
if you'll remember last time i mentioned that we're going to try to use this lightweight charts library to add a candlestick chart to our u, and just start sketching out the ui a little bit, i'm just going to start very simple in this video and then we'll add on to it over time, i don't want to spend too much time on ui yet, but i want to figure out how to add this chart library to our web page.

So you remember last time we had a file here, an index.html and all we're doing is connecting to websockets, and we're streaming out this price data, and then we're displaying and appending the bitcoin prices to our webpage 

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

and then you'll have lightweight charts included and it's just hosted on another on another host it's already hosted here, and ready to go, right, and then we have this chart.js here which where we'll put our javascript that's custom, and you'll see they provided an example here, of
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

so it's using document.body here, which will erase our other stuff in the body,
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
let's say the user wants to configure some indicators they're interested in on their custom, on this custom trading platform, right

and so under the trades div let's do an id for 'settings' and this will be a place to store all of our settings right, and so i'll do an h3, and just say 'settings' right and then here let's just put some options the user can configure, and let's say this thing it's going to hold some indicators that the user is interested in

so i'm going to say input type equals text and let's say label and let's say you know we have a simple RSI indicator right, so that's RSI um and we can let's just add another div there just to give it a little bit of room right, so we have an rsi setting right, and so let's see what the settings look like in trading view for instance and we can just make this kind of work similarly, so i'm going to go to markets on trading view, i'm going to go to bitcoin, and then let's click this guy and then let's look at the full featured chart

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
that we can run through whatever software we want, we can load it to later into the (appendix)?(panda)  data frame, or use backtrader, or whatever we want, all right 

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


and so I'm gonna install that, and you'll see it's installed,
and now I'll notice this if I run Python 3 and try to import it, 

        $ python3
        $ import talib

it gives me this error, it says image not found, so it throws some errors here
so one thing there's actually a dependency, so if you scroll down here on OSX you should have something called 'homebrew' right
homebrew for OSX and so if you have that installed it's a package manager for OSX, and there's actually a dependency here, so you want to make sure you have this installed 
so if you type 
        
        $ brew install ta-lib 

like this using homebrew, this will install a ta Lib dependency so you see it that's look quick download for the Mac OSX version that I'm on, and installs it right, and so now I'm gonna rerun python 3 and import talib and you'll see there's no error there, so it looks like I've successfully installed it 

so let's see what we can do with that ok 

so I'm gonna close up some of this stuff that already had open so close that, that, and yeah we have a bunch of difference no (pads)? that I have to open, so I'm going to start a little more fresh here,
so we have our chart and we have our read me, and I won't save that 

alright cool so let's try ta dot py 

        $ touch ta.py

and let's see if we can use this library now 

so let's see if we can find like a 'hello world' example using TALib, so it looks like it imports numpy 

        https://mrjbq7.github.io/ta-lib/

        import numpy

so let's go ahead and add a requirements dot text here to this project

        $ touch requirements.txt

and it looks like I've used a python-binance so far, and I've used a TALib, and that is TA-Lib like that, so I'll add that in there, and also it looks like we need numpy,
so I'll put that in there

        python-binance 
        TA-Lib
        numpy

I believe I already have numpy installed but just in case, I'll do pip3 install numpy right 

        $ pip3 install numpy

and until numpy is just a library, scientific computing library, so it looks like TALib accepts numpy arrays 
okay so now that I know all my packages are installed, I'm going to close that, and look at my ta dot py 

        $ nano ta.py

and let's just take this little example here, and make sure we can import numpy and ta lib right 

        import numpy
        import talib

        close = numpy.random.random(100)

so we're setting a value called close, where a variable called close equal to numpy dot random 100, and let's see what that does right, 
I'm going to print close 

        print(close)

so I'm going to run that 

        $ python3 ta.py

        [0.86983193 0.78960432 0.65126663 0.38216547 0.30000493 0.74326948
         0.27342276 0.17967592 0.02305641 0.67419051 0.53690503 0.6964192
         0.51874032 0.82510687 0.46878464 0.8827212  0.92533801 0.67661258
         0.74881267 0.28539529 0.13401968 0.22480298 0.37472739 0.79024145
         0.76800599 0.79347149 0.72225872 0.76785194 0.15443234 0.45835669
         0.90212719 0.95250666 0.03703968 0.62363581 0.14944983 0.56289757
         0.71214539 0.91349061 0.46822946 0.27004871 0.78782475 0.27558914
         0.4567252  0.40144626 0.31568156 0.9471158  0.61515842 0.1936563
         0.45193616 0.54640122 0.22023052 0.96629215 0.20665873 0.45142079
         0.6891244  0.32406061 0.16649167 0.18035352 0.58037465 0.25673302
         0.17526001 0.26620237 0.95846434 0.28796741 0.73924312 0.06602095
         0.95363059 0.27278343 0.39568007 0.81573064 0.53066213 0.76869594
         0.66947651 0.87028089 0.62642289 0.15642658 0.69264091 0.04660276
         0.60741515 0.41142797 0.47354743 0.87973504 0.30326609 0.58433482
         0.9256456  0.67370802 0.8983113  0.25412395 0.65907143 0.64277622
         0.61716781 0.74397234 0.73531434 0.44293829 0.40455724 0.29964488
         0.92820265 0.74606829 0.72048463 0.63194907]

and you see it generates this list structure with a bunch of random numbers, and it looks like it's just numbers between zero and one there's all decimals 

so well is this a list or is this an array, or what's a numpy array? 

so let's let's look that up 'what is the difference between a numpy array and a list'? (google search) 

        https://www.google.com/search?channel=fs&client=ubuntu&q=what+is+the+difference+between+a+numpy+array+and+a+list

so a numpy array it says it's a grid of values and it's indexed by a tuple of non-negative integers, 
a list in Python it's equivalent array but as resizable and contained elements 

so what is the real difference here? 

        https://webcourses.ucf.edu/courses/1249560/pages/python-lists-vs-numpy-arrays-what-is-the-difference

so it looks like numpy arrays are actually optimized for memory consumption and have a bunch of optimizations for spaced memory speed, and calculations
so looks like numpy is just faster for some scientific computing so if you're multiplying these huge lists or these huge arrays of millions of numbers, and performing all this floating-point arithmetic and matrix operations, and so forth it's designed for the scientific computing purposes 

so looks like TALibs since it's for technical analysis chose to use numpy arrays as it's for all of the data types that it operates on 

so we have a number array here of 100 random numbers here

all right so an array of 100 numbers it's not that interesting, but what is interesting is that we can build up a numpy array of closing prices for Bitcoin for instance,
or closing prices for the S&P 500 and we can have those in a numpy array as a sequence, and then we can use TALib to operate on that sequence of values, and apply all the different built-in functions and indicators that ta lib has, and let it perform calculations for us

so that's an example right, so let's pretend we have a sequence, yeah let's still do it on this random number first, and so let's look at the docs,
and looks like the simplest example right is a moving average, 

        #Calculate a simple moving average of the close prices:
        output = talib.SMA(close)

everyone understands that, it just gets the average of the previous, you know X periods right, and so if I paste that in, right, 

        #Calculate a simple moving average of the close prices:
        moving_average = talib.SMA(close)

we have our moving average equals talib, and it has dot SMA, 

so there's a bunch of indicators, built in, so I could do talib dot RSI for instance 

        talib.RSI

and that's one of the built-in functions, right 
and so yeah, let's see what the simple moving average is of this numpy array which is, just an array of closing values right

and so if I print moving average here 

        print(moving_average)

and I run this again 

        $ python3 ta.py

        [0.4908118  0.4117389  0.9272756  0.48106401 0.29615135 0.95439097
         0.61335399 0.83540937 0.76146143 0.75053812 0.69522358 0.93450378
         0.08171487 0.30119878 0.06826764 0.64119444 0.52722561 0.82042657
         0.53471451 0.49604001 0.62911228 0.49355365 0.68792848 0.64062527
         0.22534901 0.82479685 0.29158492 0.46186203 0.91489757 0.38166769
         0.88112368 0.82711708 0.73921489 0.73045963 0.27527696 0.26592356
         0.76499957 0.90410937 0.26632848 0.81132224 0.46002123 0.60079466
         0.03391452 0.62580068 0.97497397 0.00579673 0.31380193 0.11840322
         0.04289408 0.42244889 0.95889203 0.70536468 0.91989002 0.77949014
         0.75854475 0.51891425 0.25684758 0.13002586 0.22011752 0.29088586
         0.083216   0.42126499 0.67565837 0.21554984 0.7022949  0.59154706
         0.78704013 0.10677738 0.24592596 0.25991086 0.85680665 0.50089351
         0.09303239 0.17540168 0.61774748 0.98547769 0.23842184 0.84061914
         0.48887153 0.57917432 0.52486426 0.66200814 0.95308389 0.1701595
         0.39763226 0.02204815 0.31606821 0.62479518 0.61602481 0.45982162
         0.36493536 0.97547631 0.63942344 0.92012467 0.75239025 0.5726532
         0.63423718 0.16702716 0.41308506 0.71992151]

        [       nan        nan        nan        nan        nan        nan
                nan        nan        nan        nan        nan        nan
                nan        nan        nan        nan        nan        nan
                nan        nan        nan        nan        nan        nan
                nan        nan        nan        nan        nan 0.57246944
         0.58547983 0.59932577 0.59305708 0.60137027 0.60067445 0.57772554
         0.58278039 0.58507039 0.56856596 0.5705921  0.56275202 0.55162838
         0.55003504 0.5608551  0.59107865 0.56989872 0.5627846  0.53938382
         0.52298981 0.52053677 0.53152943 0.5385898  0.54632185 0.55095068
         0.56872387 0.55852778 0.55736987 0.54630866 0.52314933 0.52012327
         0.49352635 0.47999794 0.47787939 0.46071573 0.47494966 0.48580378
         0.48653847 0.45996073 0.45928065 0.44090027 0.45412645 0.45079641
         0.45276701 0.43775371 0.42584616 0.45850219 0.45598952 0.48006338
         0.4949293  0.50015348 0.48568589 0.48424067 0.48534713 0.46503611
         0.45300569 0.43644349 0.43841751 0.45490982 0.46810673 0.47373792
         0.48312857 0.50160228 0.50039445 0.52388028 0.52555012 0.52492033
         0.5198269  0.52183522 0.52740719 0.54274088]


you'll see previously if we have this array of 100 numbers, and then if you look at the second array which is the moving average
you can see a bunch of note a numbers here
so there's 1 2 3 4 5 6, 24, 29, so there's not a number a value here until the 30th a slot in this array
and so what that means is by default it uses the 30 day SMA, so there's not an average to take until 30 elements in, and then at the 31st element you know, it does the previous 30 before those, so it's just an average that rolls through this entire sequence, right 

and so let's see how we might adjust that a little bit, 

        https://mrjbq7.github.io/ta-lib/doc_index.html

        https://mrjbq7.github.io/ta-lib/funcs.html

so let's see indicators, momentum indicators, and so SMA if we're correct, it's yeah so it's on overlap studies here 

        https://mrjbq7.github.io/ta-lib/func_groups/overlap_studies.html

and so if we look at 30 day at SMA here, you can see the time period as we thought by default based on our analysis,

        SMA - Simple Moving Average

        eal = SMA(close, timeperiod=30)

that's the default time period is 30 

but let's say we wanted the 10 day moving average for instance, so we'll do time period equals 10 

        moving_average = talib.SMA(close, timeperiod=10)

and I'll run it again

        $ python3 ta.py

        [       nan        nan        nan        nan        nan        nan
                nan        nan        nan 0.68180449 0.70288098 0.66949703
         0.62371054 0.58328548 0.5172058  0.52543254 0.55868137 0.56807102
         0.53092741 0.49038641 0.49742848 0.46408997 0.41331903 0.35525749
         0.37493918 0.28509121 0.24832163 0.2627829  0.24389292 0.22702523
         0.19552195 0.26248713 0.30987607 0.37704371 0.34856607 0.35395896
         0.32645993 0.30678188 0.35203824 0.35686266 0.39097902 0.40566962
         0.37851984 0.39759511 0.43385128 0.46408071 0.45714316 0.53768064
         0.45540943 0.4662932  0.47928554 0.40341021 0.41357963 0.4089608
         0.4301564  0.44675975 0.51915312 0.47917479 0.52022834 0.56618624
         0.55716699 0.56270402 0.59347141 0.53968688 0.48225206 0.51327344
         0.47834174 0.48719851 0.50900309 0.47848372 0.44750252 0.47297568
         0.47685429 0.53230957 0.58112017 0.5312171  0.56279951 0.53446843
         0.53720634 0.56437187 0.61700998 0.60106851 0.62008311 0.56067823
         0.55567776 0.5486292  0.53353717 0.50260893 0.49494553 0.48723012
         0.48845722 0.53082141 0.47158383 0.51464998 0.53811827 0.58165925
         0.57422962 0.57340474 0.6035598  0.62087756]

and you'll see the first nine slots are not a number and then we have an average of the first 10 values 

so that's how you calculate a moving average using TALib

so you might not care moving average very simple, you don't need a special library for that, it's just an average

so let's start getting more and more complex
a lot of these are actually very simple, even you know RSI very simple calculation

so let's go to momentum indicators here and let's go to relative strength index
                        
        https://mrjbq7.github.io/ta-lib/func_groups/momentum_indicators.html

        RSI - Relative Strength Index

        NOTE: The RSI function has an unstable period.

        real = RSI(close, timeperiod=14)
 
and so this is a way to calculate the RSI, and so what we can do now is do RSI equals talib.RSI close, and then looks like the time period by default is 14 

        rsi = talib.RSI(close, timeperiod=14)

so I like that value and so let's just print the RSI, so I run again 

        print(rsi)

        $ python3 ta.py

        [        nan         nan         nan         nan         nan         nan
                 nan         nan         nan         nan         nan         nan
                 nan         nan 49.15116931 48.5148285  46.30064555 43.91875642
         51.235748   49.49845073 46.93671353 48.78303959 45.99238084 51.38381529
         45.76246125 46.41642298 45.92999962 52.47483859 48.20046702 49.96261854
         49.64689877 44.74006661 45.74441499 45.53812963 54.51625655 51.85039112
         49.24396984 52.40741181 50.81286063 46.51621182 47.41116346 53.76554484
         52.80516301 49.06107699 46.81978198 47.71636609 51.2380484  54.91694031
         53.22630083 49.80967993 48.50815582 46.09493198 42.81316553 46.20552675
         51.14691182 49.15306392 53.52682028 53.98740774 45.15724421 50.76924105
         49.56607725 47.50882851 44.21875529 45.30049368 54.06816925 56.36502396
         55.20850541 51.39127933 55.30163684 46.16969598 47.48543224 53.06721634
         52.82261371 45.51692377 50.03811045 44.18008233 47.49253746 54.66551825
         45.20628325 51.56617675 48.78836559 49.67224089 54.44196644 48.85761312
         46.0645709  50.28722883 54.62006064 50.64783911 47.76644097 48.25920954
         47.3804159  48.04353134 50.95373216 50.08723491 53.40239874 51.92434551
         47.04373181 54.31729252 49.49618373 47.08393676]

and you see we have a bunch of varying values, there random numbers, and so the RSI 14, and it looks like, it's you know, this is just some random numbers,
so the it's never really overbought or oversold, we just have some values that are like 40 or 50, so if we use that with some real price data, we'll probably be able to see some overbought
or oversold values, so overbought is usually over 70 and oversold is below 30

so these random numbers aren't very interesting, so let's see if we can use some of the Bitcoin price data that we downloaded in the last video
so I have this 15-minute.csv

        15minutes.csv

I already forgot what time period that was for, let me see let's get that real quick, and we can just see if there's some overbought or oversold values, so we can calculate the
RSI for this particular time period of prices so this is from May 20th until let's see maybe we have May 20th through May 25th 

        https://www.unixtimestamp.com/

        1614084300000 > Convert > Tue Feb 23 2021 12:45:00 GMT+0000

        1614533400000 > Convert > Sun Feb 28 2021 17:30:00 GMT+0000

so we should get be able to pull out some overbought and oversold values from there, and so let's figure out how we can load this 15-minute CSV data, and to get the open high low close
let's see if we can get the closing prices into a numpy array and run this RSI indicator on that 

so let's see how we do that
so I will use Google and I type 'build numpy array from CSV' 

        https://www.google.com/search?channel=fs&client=ubuntu&q=build+numpy+array+from+CSV

and
        https://intellipaat.com/community/9398/how-do-i-read-csv-data-into-a-record-array-in-numpy

let's see what it gives me

        To read CSV data into a record array in NumPy you can use NumPy modules genfromtxt() function, In this function’s argument, you need to set the delimiter to a comma.

                from numpy import genfromtxt
                my_data = genfromtxt('my_file.csv', delimiter=',')

        You can also use the pandas read_csv function to read CSV data into a record array in NumPy.

                import pandas as pd
                df=pd.read_csv('myfile.csv', sep=',',header=None)
                df.values array([[ 1. , 2. , 3. ], [ 4. , 5.5, 6. ]])


so it looks like there's this genfromtxt() function

so I will import that and I'll say my data equals genfromtxt(), and I'll try this 15 minutes dot CSV, and we give it a delimiter of comma

        from numpy import genfromtxt

        my_data = genfromtxt('15minutes.csv', delimiter=',')

        print(my_data)

and yeah let's print that out, and see how it works, let's see if that gives us what we need 

so I'm going to comment out some stuff here 

        #close = numpy.random.random(100)

        # print(close)

        # #Calculate a simple moving average of the close prices:
        # moving_average = talib.SMA(close, timeperiod=10)

        # print(moving_average)

        # rsi = talib.RSI(close, timeperiod=14)

        # print(rsi)

and print just that my data there, all right, so I'm gonna run it again 

        $ python3 ta.py

        [
         [1.61408430e+12 4.76862400e+04 4.94555300e+04 ... 2.07375702e+03
          1.01062795e+08 0.00000000e+00]
         [1.61408520e+12 4.86705400e+04 4.93223800e+04 ... 1.16145442e+03
          5.66780029e+07 0.00000000e+00]
         [1.61408610e+12 4.92540700e+04 4.96000000e+04 ... 1.21149016e+03
          5.93137781e+07 0.00000000e+00]
         ...
         [1.61453160e+12 4.35147700e+04 4.37305200e+04 ... 4.28064209e+02
          1.86070359e+07 0.00000000e+00]
         [1.61453250e+12 4.36034600e+04 4.39426200e+04 ... 3.89522200e+02
          1.70398295e+07 0.00000000e+00]
         [1.61453340e+12 4.35449200e+04 4.35820500e+04 ... 6.82783060e+01
          2.97135217e+06 0.00000000e+00]
        ]

all right so look at that, so we have a lot of, so it looks like an array of arrays which is good, and this first index from each list is the timestamp, and then we have some prices 
so that's like nine thousand six hundred twenty three because you see that exponent, it's like e to the third, ten to the third, 

and then, yeah, so it looks like that worked
we're able to pull in an array of numpy arrays using this genfromtxt() function, right 

so the next thing I want to do, I want just the closing value from here, 

        15minutes.csv

        1614084300000,  47686.24000000,  49455.53000000,  47672.46000000,  48670.21000000, .......
        timestamp       open             high             low              close      

so we have timestamp, open high/low, close, and so I want the 0 1 2 3, the 4th 4th value here, I don't, I'm not really that interested, and all these other ones I want to use, 
the closing price, so I want to extract, you know this value, this value, this value, all the way down like this entire column of data, 
and so let's look up how we do that right so

        'how to import a CSV file as numpy.array in python' 
        
        import numpy as np
        csv = np.genfromtxt('file.csv', delimiter=",")
        second = csv[:,1]
        third = csv[:,2]

and it looks like you can access this sequence like this, so let's try that syntax just like accessing a list like that 

so we're gonna say the 0 1 2 3 4, all right cool, 

        close = my_data[:,4]

        print(close)

so we want the closing price (low)? so let's see if we say the closing price is 'mydata', 
and then we have a colon and a 4 there and let's print the close 

I run that, and spell it correctly, and look at that 

        $ python3 ta.py

        [48670.21 49264.95 48680.01 48122.79 48750.   48915.53 48489.87 46667.72
         46978.18 47920.6  48615.1  48949.62 48602.03 48530.37 48185.95 47429.07
         47365.61 46952.38 47834.83 47309.43 47175.27 46525.06 47313.23 47507.11
         46881.49 47057.34 46913.78 45668.94 45523.   45866.17 46871.85 47269.48
         47814.5  47941.48 48045.96 48418.26 47937.33 48308.23 48187.51 48136.35
         48589.69 48749.99 48407.39 48252.12 48891.   48115.61 47216.63 47713.91
         48456.58 48723.21 49166.12 49719.52 50191.6  50286.16 50008.52 50055.72
         50160.42 50367.19 50243.7  50405.6  50874.99 51246.79 50673.73 50353.33
         50617.29 50620.01 50399.72 50406.5  50247.4  49736.62 49666.93 50055.59
         50109.21 49552.56 49703.96 50100.   50090.57 50491.91 50626.76 50406.83
         50634.36 50545.63 50717.02 51229.02 50847.51 50606.28 50404.42 50539.14
         50075.   50387.83 50714.89 50366.22 50360.02 50818.7  51131.05 50891.81
         50739.94 50431.67 49590.82 49453.55 49481.61 49428.22 49460.03 48774.57
         49404.04 48914.08 49144.43 49222.17 49819.5  49741.63 49479.04 49577.25
         49308.28 49740.36 49703.24 49842.78 50041.8  49618.18 49632.21 49855.7
         49570.   49348.81 49405.57 48969.46 48959.93 49170.76 48864.96 48629.66
         49101.18 48500.51 48152.16 48449.09 48707.72 48124.12 48686.94 48556.13
         48811.63 49351.71 49309.66 49555.1  49676.2  49554.86 50316.84 50757.21
         50507.25 50851.26 50832.65 50726.75 50504.71 50736.61 50490.37 50790.02
         50650.95 50502.07 50117.23 50333.77 50206.97 50066.57 50287.94 49982.06
         49627.34 49763.7  49701.93 50002.21 50388.6  50422.2  50280.78 50432.38
         50453.54 50335.23 50485.   50466.71 50395.99 50155.1  50069.98 50037.94
         49700.   49253.07 48935.78 48773.8  48977.03 49254.52 49077.05 49214.77
         49551.51 49769.26 49606.17 49761.78 50294.8  50274.01 50366.31 50511.54
         51487.06 51745.02 51430.06 51465.33 51347.6  51445.97 50851.58 50712.08
         50830.88 51036.33 50927.95 50867.47 50849.99 51071.27 51074.8  50980.82
         50630.66 50095.31 49716.41 49633.59 49550.95 49800.63 49740.38 49684.24
         49544.14 49485.98 49527.09 49669.58 49443.86 48872.55 49099.99 48818.39
         49152.75 49043.93 48905.54 48650.47 48101.99 47902.26 48697.68 48342.59
         48235.85 47947.9  48265.5  47335.08 47073.73 47491.61 46752.35 46184.09
         46801.05 46988.91 47153.56 47079.16 46480.48 46810.   47270.15 47756.44
         47343.51 46728.53 47377.63 47235.96 47330.24 47439.79 47486.42 47098.34
         47025.06 46700.01 46650.9  46223.88 45517.53 46107.44 45828.47 46048.53
         46093.07 46046.82 45381.11 44397.85 44973.68 45434.57 45655.11 45694.47
         45727.74 46334.34 45922.1  46092.24 46410.76 46411.45 46628.33 46579.39
         46706.85 46409.55 46207.53 45783.26 46427.65 46427.71 47085.06 47067.59
         46823.39 46531.1  46166.14 46182.55 45958.41 46072.31 46799.95 47356.81
         46868.98 46571.96 46340.3  47486.16 47594.65 47735.77 47862.29 47722.01
         48127.26 48061.74 47815.39 47746.74 47660.98 47768.68 47381.2  47738.15
         47317.09 47256.71 47210.29 46641.27 46959.17 46821.43 46178.09 46588.57
         46270.   46384.69 46773.99 46465.84 45677.46 45157.49 45746.23 45865.03
         45476.3  45991.32 46214.23 46274.58 46276.87 46674.94 46720.95 47150.01
         47525.07 47453.79 47565.15 47789.72 47761.97 47692.63 47739.43 47494.52
         47375.34 47673.9  47487.24 47622.56 47423.08 47384.38 47746.29 47743.81
         47657.47 47700.94 47573.28 47724.35 47803.71 47701.12 47708.31 48332.2
         47566.6  47187.04 47359.38 47069.62 47158.53 47162.23 46552.38 46732.19
         46620.5  46478.19 46566.89 46363.12 46671.04 46727.07 46832.04 46925.83
         46775.51 46799.01 47274.79 47446.72 47299.99 47378.01 47017.04 47554.47
         47429.99 47378.35 47559.73 47517.47 47441.91 47469.98 47254.51 46883.89
         47079.64 47199.52 47060.84 46556.51 46528.64 46755.93 46944.39 46842.61
         46883.19 46876.95 46997.11 46909.47 47042.53 46972.84 47042.11 47251.98
         47136.3  47397.89 47184.17 47256.95 47405.39 47260.85 47324.96 46997.19
         47081.07 47114.99 47048.75 46728.01 46825.3  46589.57 46337.28 46551.04
         45828.43 45425.79 45170.47 45710.38 46106.43 46142.23 46255.95 46128.2
         46345.94 46458.13 46469.65 46277.27 46442.5  46181.35 45845.7  45511.99
         45397.23 45449.53 45388.83 44673.14 44629.17 44597.39 44644.48 44823.05
         44384.14 44875.61 45075.05 44850.02 44791.27 43905.71 44875.53 44636.92
         44372.43 44358.16 44545.56 44326.13 44400.83 44686.68 45095.79 44944.99
         44856.61 45287.18 45103.2  45187.26 45067.61 45147.87 45346.76 45152.69
         45177.2  45347.82 45359.22 45388.55 45284.86 45284.93 45039.61 44649.99
         44756.99 44673.48 44452.55 44601.3  44178.8  43749.67 44176.88 44377.91
         44561.92 44323.76 43744.47 43316.54 43391.14 43411.61 43334.35 43632.98
         43514.78 43603.46 43544.92 43481.66]

so let's see is that correct, yeah nine thousand six hundred fourteen dot eighty seven, nine thousand four fourteen dot five,  nine sixteen eighty seven nine four four fourteen fifty 9470


        48670.21 = 48670.21000000 
                   close             

so that's great, so we have a sequence of this closing price in these 15-minute candles, and we have it in a single numpy array, which is great!
so and then this was the 15-minute charts, and so let's see if we apply our RSI indicator to that 

so talib.RSI for the close of our Bitcoin data 

        rsi = talib.RSI(close)

        print(rsi)

        $ python3 ta.py

        [        nan         nan         nan         nan         nan         nan
                 nan         nan         nan         nan         nan         nan
                 nan         nan 46.90490373 42.47891146 42.12004002 39.76425923
         46.6291435  43.45379552 42.6550255  38.92087424 45.18515002 46.63503022
         42.70931501 44.13288622 43.18937331 36.00190747 35.26104172 38.46758864
         46.78587721 49.68225514 53.4242737  54.27741914 55.00769046 57.60606525
         53.32211526 56.03742249 54.91765749 54.42134636 58.04006642 59.27143143
         55.52127029 53.85808625 59.26517164 51.39358744 44.083058   48.45117547
         54.20490488 56.09942278 59.12448389 62.59286434 65.2979426  65.83095192
         62.78184328 63.09479335 63.82150161 65.27572514 63.63068619 64.88029779
         68.28285682 70.7040151  62.75273306 58.7730507  60.96916003 60.99221898
         58.00342633 58.07152679 55.78549333 49.1024959  48.25312625 53.12319647
         53.76962449 46.58723137 48.59834949 53.52764679 53.39634314 58.10645465
         59.58448219 56.10771055 58.78697954 57.31760465 59.42713983 64.99332906
         58.54786684 54.84424672 51.88642018 53.68181373 47.15341401 51.43991633
         55.50355567 50.63849406 50.55363822 56.3775385  59.84591115 56.16258926
         53.89493908 49.52387191 39.99543133 38.68681597 39.12528135 38.56024272
         39.12433843 32.25254076 42.27874851 37.61270745 40.91428283 42.02928255
         49.85890053 48.93109415 45.8337281  47.18040946 43.9571294  49.88073377
         49.39767423 51.30670287 53.97374741 47.95311235 48.1593633  51.45920556
         47.31309358 44.3348313  45.28661177 39.67363105 39.55824792 43.4748232
         39.47884068 36.68475028 45.07389588 38.14090123 34.79806276 39.65320127
         43.59308137 37.62391338 45.39007987 44.01831985 47.36436432 53.6683526
         53.1347636  55.89137858 57.22817885 55.41591236 63.27986171 66.91220952
         63.09690961 65.97257061 65.67442308 63.90458281 60.23905993 62.64876093
         58.58843455 61.83038657 59.50217919 57.02655659 51.10735048 54.00056992
         52.05793779 49.91667292 53.18626143 48.47700137 43.65020702 45.88099774
         45.01170263 49.9738011  55.53419342 55.99226675 53.49437731 55.77216826
         56.09540412 53.73090837 56.24525129 55.8461343  54.24335358 49.07661166
         47.35997178 46.69783614 40.29822967 33.71721577 29.974703   28.25072816
         33.42443705 39.80672863 37.3411877  40.42492298 47.25963804 51.16145305
         48.28041862 51.10937358 59.31789811 58.90249584 60.23395368 62.30339687
         72.61314026 74.59200837 68.1200286  68.45015242 65.99359408 67.0574198
         55.71565801 53.43153882 55.11898932 57.95634639 55.94699535 54.80510822
         54.45914372 58.06778511 58.12479061 55.94422272 48.62472697 40.00658969
         35.24525828 34.28476709 33.30933199 38.95988137 38.12053243 37.31386378
         35.30599605 34.47660318 35.62771761 39.58920465 35.82780193 28.45789102
         34.25589605 30.91518311 38.57495224 37.13197268 35.32236184 32.2068803
         26.7443528  25.07642305 40.88754093 37.12141203 36.04657737 33.24966407
         38.88251833 30.7072917  28.87102496 35.51137725 30.14910039 26.79915738
         35.2155921  37.56940295 39.63938612 39.00996577 34.2914424  38.68738575
         44.29205072 49.54151105 45.61113465 40.46255498 47.23295923 46.00335629
         46.99233016 48.17999256 48.70679989 44.63943139 43.89405014 40.65150639
         40.16870065 36.14848922 30.67887222 38.98256386 36.74118544 39.68712031
         40.29318611 39.84543722 33.9905432  27.55111151 35.28352211 40.73563107
         43.20145265 43.65206017 44.05607428 50.9600994  46.73868203 48.63005891
         52.06215646 52.06962711 54.47133376 53.81601913 55.32351284 51.13118105
         48.44474379 43.29949532 51.69164284 51.69235979 58.89076621 58.64067386
         55.1171486  51.15509528 46.64624082 46.87298738 44.11520819 45.85844591
         55.4245706  61.090545   54.54909821 50.97044118 48.3084556  59.55901712
         60.43700137 61.60468919 62.66850927 60.66161175 64.2257782  63.22833379
         59.48750005 58.44970487 57.10934316 58.39953269 52.30359365 56.77933954
         50.73176764 49.91081301 49.25095495 41.93258161 46.69789982 44.97566939
         37.93793658 43.96305666 40.66359684 42.34133772 47.74259702 44.21211347
         36.72881339 32.78712252 40.56479052 42.02270628 38.67933977 44.93064467
         47.42870364 48.11493018 48.14259147 52.84840933 53.3750569  58.07747897
         61.71265884 60.63652949 61.75847468 63.98761468 63.4950785  62.20657955
         62.75592795 58.00435285 55.7906182  59.91759194 56.37433215 58.29957084
         54.48257101 53.747363   59.28115006 59.22885568 57.33264971 58.06065756
         55.08798445 57.83894729 59.25098849 56.61144851 56.75684655 67.06904997
         50.99739246 45.21291398 48.0919135  43.91361373 45.4788833  45.54698992
         37.28063703 40.69805943 39.26683401 37.45924706 39.33378023 36.61839974
         43.01975134 44.12558269 46.23094208 48.11222581 45.37218828 45.89099594
         55.17323906 57.97857176 54.82517252 56.18963022 48.83965304 57.70936476
         55.3171605  54.31135514 57.2514624  56.34173785 54.66906086 55.20114935
         50.3185986  43.23490346 47.44330324 49.89327604 47.1547884  38.81185436
         38.40745046 43.57135941 47.5016073  45.65229232 46.54584129 46.41945662
         49.2756651  47.29537596 50.54502128 48.8462833  50.62266016 55.64795369
         52.47765098 58.26757303 52.62619152 54.25060096 57.45488141 53.52378469
         54.99465146 46.83388621 48.92275795 49.78200555 48.08097044 40.8095369
         43.59601947 38.82660225 34.47906047 40.55280895 30.32047162 26.33336459
         24.16349198 36.14575574 43.23143941 43.83810787 45.8188602  43.94388455
         47.86024226 49.80609923 50.01239355 46.57019073 49.76800273 45.1667705
         40.04255876 35.70536559 34.3283286  35.54827982 34.74162777 26.97058968
         26.57726128 26.27895998 27.57609838 32.43127547 27.54366539 38.68648191
         42.54771368 39.52333572 38.74892452 29.39839089 45.03999627 42.54267884
         39.90165907 39.75825103 42.67217554 40.21902946 41.45296594 46.04264946
         51.85934601 49.73120358 48.47565173 54.50222319 51.71856565 52.90216837
         50.98620807 52.23585177 55.27870333 51.81033456 52.2180907  55.068263
         55.26028915 55.78386529 53.40443234 53.40587725 47.81037587 40.54468589
         43.10197098 41.59813083 37.83697092 41.66160114 35.06288619 29.88529451
         39.46827117 43.38924893 46.78702003 43.17508076 35.91275577 31.6742718
         33.15535418 33.58080781 32.73395937 39.1242724  37.60161738 39.50390202
         38.66590577 37.73436833]

        [ ...... 29.974703   28.25072816 ....... 29.88529451 .........]

        (oversold = below 30)

        oversold 15 data points back the price close at 43749.67000000 $ and so if you look before that you would expect prices to be decrease rapidly, so there was probably a lot of momentum leading to an oversold state,

and then we print the RSI, I'm gonna run it, 
so you have a lot of different values here that are between 0 and 100, so these are RSI values, and let's see if we can find any points at which the price was overbought or oversold 

so you'll see here near the end there's a case where the RSI was above 70 which would be overbought 
so let's see if we can verify that using the data, so we'll go, one, two, three, four, five data points back, so if you go back five data points, so from the end,
so you'll see that the value, one two three four five, so 8950 here was when it was overbought, and so if you look before that you would expect prices to be rising rapidly
so there was probably a lot of momentum leading to an overbought state, 

and so let's see if those numbers rose, and if that's correct, right
so you'll, look at that, so we have you'll see it was eighty seven fifty five, eight seven sixty nine, eight 789, and so it was rising until it's eighty eight hundred, 
then kept rising into eighty eight hundreds, and then went all the way to eighty nine fifty, so there was a lot of momentum upward there leading to an overbought state

and also let's see if we can validate that, let's try something like a trading view right, and then let's see what date and time that corresponds to 
so that was May 25th which is today, and that was around 12:15 p.m. Pacific, so I'm going to pull up the cryptocurrency data for Bitcoin, right
and let's see Bitcoin USDT, and I'm gonna go to the fully featured chart here, and let's try to pull up the RSI, and compare so what we got from TALib just to verify we're doing this
correctly 

        29.88529451 
        Sun Feb 28 2021 15:00:00 GMT+0100 (Central European Standard Time)

        https://fr.tradingview.com/chart/oTAPdW86/


so I'm going to look at the 15-minute chart, and then I already have the RSI pulled up, and if you look here
sure enough at 12:15 here, it looks like this is where that overbought condition occurred which was when Bitcoin was about eighty nine fifty,
so you see this run here, this led to the overbought, and so you see this RSI at the bottom, and then it rose, and briefly went above seventy 

okay, so I think I'm going to end the video here, this one's running a bit long, I'm trying to keep every video between ten and fifteen minutes or so
this one's already over fifteen minutes, and I feel pretty good about what we covered so far, 

we showed how to install the TALib library as a Python package
we showed how to read in some data using an numpy arrays
so we read in our Bitcoin historical price data into a numpy array, 
and then we were able to run some TALib indicators against this numpy array, 
so we were able to calculate a simple moving average using TALib and we're also able to calculate the RSI, and determine a point at which Bitcoin price was overbought today
and we compared that against this graph this RSI indicator in trading view just to confirm our analysis was correct, and we were able to detect when this price rose here from 8702 to 8950 and confirm that the RSI went above 70 at that point in time

so it looks like we have a pretty good idea of how to use TA lib indicators

so I'm gonna stop it here and in the next video, we're gonna continue our discussion of TALib and try to combine it with backtrader for back testing and maybe we'll cover some more indicators and see what happens when we buy and sell Bitcoin based on these indicators, and see what our results would be when initializing an account with a certain balance of say $100,000 

so stay tuned for the next video and thanks for watching!










Binance API Tutorial (Part  6) - Setting up a Flask Backend (15:38)

https://www.youtube.com/watch?v=o95Rl1OEkBg





hey everyone welcome back to another video 

today i'm going to be continuing the series on cryptocurrency and binance 

if you'll remember i started recording this series on binance around memorial day weekend, and i didn't post the videos because i wasn't finished
i got a little bit bummed out after what happened after memorial day, and um everything that happened in the country for the past, a little over a month now
so i got a little bit burns out and wasn't quite in the mood to continue the series, but now that i'm in a little bit in better spirits, i'm going to try and pick up where we left off here 
since there's a lot of demand for crypto content, i'm going to post a little bit more of that on this particular channel

um so if you'll remember, last time we had started making this ui, so the plan was to make kind of a tradingview like a system, where we have a user interface has a chart, and some indicators on this user
interface, and then we also explored receiving candlestick data using the binance api, and also explored using websockets to stream, real-time data both from javascript and also from python

and so then after that we explored using talib so we installed ta lib in order to try different indicators against the candlestick that we got, so that we can tell whether the price for bitcoin is overbought or oversold as just a simple example

so now, what we want to do, now that we have this ui, and also we have you know some simple scripts to parse csv data with 15 minute candlesticks, and you know run a talib rsi indicator for instance on 
this dataset, i want to start hooking up a back end to this web ui, so we have a web ui that's written in javascript, and we have the ability to stream bitcoin price data to the console, and i believe we showed
that last time, so that's all inside of an index.html file, so we included lightweight charts, we included these simple text fields for our rsi settings, and then also we have this chart.js that we wrote which is a javascript file that configures our charts, and right now we just have hard-coded price data to demonstrate the chart, and we also know how to stream binance data over websockets using javascript so we showed how to do that, and so now let's start hooking up this front end to a back end that gets a real data, and kind of tie it all together

so to do that i'm going to introduce a framework called flask, so a lot of people that program python are probably familiar with this

        https://flask.palletsprojects.com/en/2.0.x/

it's a web framework that makes it very easy to make a little web application, and so you can build a front end using these html templates, with some placeholders for variables, and then you can also define some api endpoints and routes, to run some logic, access a database, call other services and things like that

and so we're going to use flask here, and hook that up

so to do that let's go ahead and just dive in 

so we have our requirements.txt here

        requirements.txt

and i've already installed python-binance, talib, numpy and backtrader??,

        https://www.backtrader.com/

        How to install Backtrader?
        
        https://algotrading101.com/learn/backtrader-for-backtesting/

        The easiest way to install Backtrader is by command line. Simply type in pip install backtrader.
                
                
        If you plan to use the charting functionality, you should have matplotlib installed. The minimum version requirement for matplotlib is 1.4.1.

        You can confirm it is installed on your system by typing in pip list from the command line to show installed Python packages.

        If you need to install it, you can do so either via pip install backtrader[plotting] or pip install matplotlib.


        $ pip install backtrader

and i'm going to add flask as a requirement here, and so we can just install flask into our virtual environment here 

        ($ pip install flask => gives me an error when using flask)

        so use this instead :

        $ sudo apt isntall python3-flask 

and then we'll have flask as a web application framework, and then let's just copy the quick start example to create a flask app

        https://flask.palletsprojects.com/en/2.0.x/quickstart/

and i'll demonstrate how that works, and then we'll start filling in the simple endpoints with more specific ones for our application

so here's the minimal application in the quick start section of the flask documentation, and so if you just copy this in, let's create a new file and we're going to call it app.py
and this will contain our web application

        $ touch app.py

if i paste that in, 

        from flask import Flask

        app = Flask(__name__)

        @app.route("/")
        def hello_world():
            return "<p>Hello, World!</p>"

you'll see we import flask from the flask package, and then the first thing you need to do is you create a new application, which is a new flask object
and then all you need to do in flask really is to find some routes, and then some function, a function to call when that route is accessed in the browser

and if you don't know what that means, i'm going to show you real quick, so let's run this flask application

so it looks like you have to export a variable, an environment variable, so this export FLASK_APP equals hello.py ($ export FLASK_APP=hello)

so we're going to export from our command line, export flask app equals and then our app is called app.py, so we'll say app.python

        $ export FLASK_APP=app.py

and that creates the environment variable, and then we just say flask run

        $ flask run

and what you'll see that happens is a small web server has a web server built in
and it says the web server is running on localhost 127.0.0.1 and port 5000, so if you copy that to your browser, and you put that in you get 'hello world' on the screen

so you have a web address, and at the base route which is just slash right, it just returns 'hello world' that's all it does, so this is the route 

        @app.route("/")
        def hello_world():
            return "<p>Hello, World!</p>"

and the function, it means when this route is accessed in the browser, it calls this function hello_world() and whatever you return from the function is what's displayed, rendered, in the browser as a response 

so let's modify this a little bit, with another example
so instead of hello_world() let's just call this the index() and then i'll just call this the 'index' page, right 

        def index():
            return "<p>The index page</p>"

and so if i rerun it, i'll rerun the app, and i reload

        $ CTRL-C (to quit)
        $ flask run 

you see it just returns index so that's how you change that, right, and then let's say we wanted to create another route, that where the the url is slash buy 

        @app.route("/buy")

so maybe it's a buy endpoint, so let's call that function 'buy' and we'll return the string by, 

        @app.route("/buy")
        def buy():
            return "<p>buy</p>"

and let's create one called 'sell' and we'll create that function and then return 'sell'

        @app.route("/sell")
        def sell():
            return "<p>sell</p>"

and let's create one more function called settings, where we can just save our indicator settings to a database for instance 
so i'll call that one settings, right, and let's do that

        @app.route("/settings")
        def settings():
            return "<p>settings</p>"

okay and then another thing we'll do, you'll notice i had to restart the web server, in order for the changes to take effect, this web server actually can automatically reload if you set the debug mode on, and so let's see how you do that

        https://flask.palletsprojects.com/en/2.0.x/quickstart/

        Debug mode
        $ export FLASK_ENV=development
        $ flask run

so debug mode all you have to do is do another export, and say you're in development mode, so i'm going to do that, so i'm going to stop this web server with control c, and i'm going to export that flask environment equals development

        $ CTRL-C 
        $ export FLASK_ENV=development
        $ flask run

and then do run and you'll see now it says 'debugger is active!' and so what that means is it will reload the application automatically, so let me show you what that means 

so you see we defined a base route, that's 'index', but also now we have a slash 'buy', so slash 'buy' returns buy 
slash 'sell' returns 'sell', and slash 'settings' return 'settings' right

        http://127.0.0.1:5000/buy
        http://127.0.0.1:5000/sell
        http://127.0.0.1:5000/settings

and so if i change this for instance is settings 2 now 

        http://127.0.0.1:5000/settings2

i don't have to reload the server you see how it reloaded automatically
and so now i'll get a 404 not found when i hit settings, because i changed the route to settings 2.

but if i go to settings 2 i automatically see it, so i'll change that back, i just want to show you how that reloads automatically

and also note in debug mode if i make a mistake, so let's say my home page i leave that out like that, 

        @app.route("/")
        def index():
            return "<p>The index 

and it tries to reload, and then i try to hit my endpoint, the base url, here i see a syntax error, so it shows me some debugging information in the browser to help me know where the error is 
so it says 'end of line (EOL) scanning string literal' and it points to that exact point
so i just took out the quote there so that's the error 

        @app.route("/")
        def index():
            return "<p>The index page</p>"

so now it reloads, and now if i reload it everything's fine

so that's good, all right, so we're not just going to be returning a simple string right, what we really want it to do, is we want it to look like this 

        http://127.0.0.1:5500/Trading/Coinview/index.html

if we want to have a chart, we want to have, you know a user interface so we already have this index.html file created, and so what we want to do is use that in our flask application

so to do that, we're going to want to use flask templates, which are 'Jinja 2' templates, and so if you look in the documentation here

        https://flask.palletsprojects.com/en/2.0.x/

        https://jinja.palletsprojects.com/en/3.0.x/

for 'Jinja' right, so all these are basically some html like this, 

        <!DOCTYPE html>
        <html lang="en">
        <head>
            <title>My Webpage</title>
        </head>
        <body>
            <ul id="navigation">
            {% for item in navigation %}
                <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
            {% endfor %}
            </ul>
        
            <h1>My Webpage</h1>
            {{ a_variable }}
        
            {# a comment #}
        </body>
        </html>

but it has some nice syntax for like looping through a list,

        {% for item in navigation %}

some placeholders like if you  want to change the title

        <title>{% block title %}{% endblock %} - My Webpage</title>

and so there's a bunch of different tags that you can embed in, so it just basically is a templating language that we use, but the baseline it's really just some html, but with ways of looping through python lists, and displaying variables dynamically and so forth 
so it's like some html with an extra layer of programming on top of it, so what we can do is this index.html that we had saved in the previous lesson right 
all that was is we had been opening this as a file, but we don't want to actually open it as a file, we want this to run as a web application right 
so that we can deploy this to some domain, our own domain, and then have this template load and display our ui 

so in flask what you want to do, is you can create a folder called 'templates'

        $ mkdir templates

just like that, and then we want all of our flask templates, our jinja templates to go in this 'templates' folder, and so let's move, so i'm going to move index.html to this templates folder

        $ mv index.html templates/

so i move that there, and then inside of templates, now i have that index.html,

and then our chart.js we can also, we're going to make another directory, and i'm going to create a directory called the base, called 'static', and that'll just be our static javascript and css files

        $ mkdir static

and so i'll move chart.js to static 

        $ mv chart.js static/

and that's in there, and so now we're getting the structure of an application

we have our javascript and css and static, we have our html templates in templates, we'll probably make a 'data' directory, so let's make a 'data' directory just in case we need the csv files later, so we'll make a directory called 'data' and let's just move our csv files into there

        $ mkdir data

        $ mv 15minutes.csv 2012-2020.csv data/

and we're just going to gradually organize our application more and more right 
so data has some csv files that we downloaded, we probably don't need these later we're going to obtain these dynamically, but i'm just saving them for now

so we have our app, we have our backtrader_talib.py 
so i have this prepared for later but we're not going to go into this quite yet, we're going to make some modifications to this

        backtrader_talib.py

and then we have ta.py that we ran earlier, and so any python code we have here, we're going to gradually add that into modules, and then pull them into our web application here
so import them in, and then make it where these endpoints actually call the technical analysis functions from talib, and also called the binance api

and let me see this dataset.txt here, i'll go ahead and move that also into 'data'

        $ mv dataset.txt data/

so do that, and then, yeah so we're going to clean this up more and more so that our project is well organized into a structure 

we just started with the basic html file, and some simple python scripts where we're going to organize this into a full stack web application all right

so here's our app, and then we have an index now, 

        app.py

an index() function that returns the string 'index', but we what we want to do is actually display a template, an html template
so to do that flask has this render template function

        from flask import Flask, render_ template

so i'm going to, from flask import flask and render_template, and this is all in the documentation, but i have enough familiarity where i know the names of these now 
so we're importing 'render_template', and we're going to say return render template index.html

        @app.route("/")
        def index():
            return render_template('index.html')

and i believe it'll automatically know to look in a folder called 'templates', so let's see what happens

so i'm going to reload this and i'm

going to do flask

run to run the server again

and you'll see right it rendered the

index.html template

that we had so you'll notice we have the

html part from

our index template here but we don't

have our chart anymore

and any color or anything like that so

what happened there right we did

we have this template rendering but this

chart.js is in a different location now

and our application doesn't know where

it's at so to fix that

we're going to go back here to the flask

quickstart here

and i believe there's a static yeah so

there's a static files

function here and so we need this little

url for

to generate a url to a particular asset

so a css or javascript file and so if we

copy this where it says script source

equals chart.js instead of

putting just chart start chart js just

like that what we need to do

is do these little placeholders here and

then we're calling this function url for

and saying look in static

for file name chart.js

and then at that point no matter where

we deploy it

when we refresh it it will have

a way to reference that static so it

does slash static charge a s

but if we had this in another folder and

defined our static folder

then it would know where that chart.js

lives all right so now we have our

javascript we have our ui

it's being rendered as a template in

inside of flask all right so the next

step here

is what were those little curly braces i

just used so that's

used to display a variable um in flask

or in ginger two templates

and so we can do is for instance let's

say we want to change the title

of this application we could do title

equals coinview so we define a variable

in our python function

and then we just pass these variables

so we can do title equals title and that

will go to our template here instead of

hard coding trades here

we can do this place folder and just do

title just like that

and you'll see it says coin view and so

if we want to save settings to a

database for instance

um like this 14 70 and 30

then what we could do is when the page

loads we retrieve those default settings

from the database

and then we send them over to the

template and then display them in the

template

that way different users of this

application could have different

settings of their own

alright so we're coming up at about 15

minutes here on this video

so i'm pretty happy with what we've

accomplished we took our

fixed html file that we created in the

earlier lessons

and we installed flask and used it in as

a template

for our flask application and we've also

defined some simple routes even though

they don't have much logic in them yet

so i'm going to start the video here in

the next video i'm going to continue on

and add some logic to actually inter

interact with cryptocurrency data and

binance api

from flask and so we'll gradually start

hooking up our front and back end and

bring it all together

into a full stack application all right

thanks a lot for watching and stay tuned

for the next video
