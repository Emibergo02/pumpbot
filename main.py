from pyrogram import Client
from pyrogram.handlers import MessageHandler
from kucoin.client import Client as ClientKucoin
from datetime import datetime
import discord_selfbot
import telegram_selfbot

api_key = '619d3516a198580001b81a36'
api_secret = '726efe1d-127c-4b20-948f-4553c176fcc7'
api_passphrase = 'allora_adesso_scopo'

clientkucoin = ClientKucoin(api_key, api_secret, api_passphrase)
discord_selfbot.startDiscord()
telegram_selfbot.startTelegram()
# or connect to Sandbox
# client = Client(api_key, api_secret, api_passphrase, sandbox=True)

# get currencies
#print(clientkucoin.get_currencies())

# get market depth
#depth = clientkucoin.get_order_book('KCS-BTC')
#
## get symbol klines
#print(clientkucoin.get_kline_data('KCS-BTC', kline_type='1min'))
#
## get list of markets
#markets = clientkucoin.get_markets()

# place a market buy order
#order = client.create_market_order('NEO', Client.SIDE_BUY, size=20)

# get list of active orders
#orders = clientkucoin.get_active_orders('KCS-BTC')

def symbol_from_social(symbolo):
    start=datetime.now()
    #clientkucoin.create_market_order(symbolo, ClientKucoin.SIDE_BUY, funds=50)

    tickersymbolo=clientkucoin.get_ticker(symbolo)
    clientkucoin.get_
    klinesymbol=clientkucoin.get_kline_data(symbolo, kline_type='1min')
    print(float(klinesymbol[5]) * 2)
    #clientkucoin.create_limit_order(symbolo, ClientKucoin.SIDE_SELL, str(float(klinesymbol[5])*2))
    index=1
    for l in klinesymbol[0:15]:
        print(str(index)+" minuti fa: ", l[2])
        index+=1

    print("prezzo ora ", tickersymbolo["price"])
    stop = datetime.now()
    elapsed = stop-start
    print(elapsed.microseconds//1000," millisecondi")
