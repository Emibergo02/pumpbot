from pyrogram import Client
from pyrogram.handlers import MessageHandler
import configparser
from kucoin.client import Client as ClientKucoin
from datetime import datetime
import discord

config = configparser.ConfigParser()
config.read("config.ini")


clientkucoin = ClientKucoin(config["kucoin"]["kc_api_key"], config["kucoin"]["kc_api_secret"],
                            config["kucoin"]["kc_api_passphrase"])
funds_method1=50


def main():

    telegramclient = Client("telegram_session", config["telegram"]["tg_api_id"], config["telegram"]["tg_api_hash"])
    telegramclient.add_handler(MessageHandler(telegram_msg))
    telegramclient.run()




def symbol_from_social(symbolo):
    start=datetime.now()
    clientkucoin.create_market_order(symbolo, ClientKucoin.SIDE_BUY, funds=funds_method1)


    tickersymbolo=clientkucoin.get_ticker(symbolo)
    klinesymbol=clientkucoin.get_kline_data(symbolo, kline_type='1min')
    price5mago=float(klinesymbol[5][2])
    limitprice=price5mago * 1.5
    print(limitprice)
    symbolonousdt=symbolo.split("-")[0]
    boughtvalue=clientkucoin.get_accounts(symbolonousdt, 'trade')[0]["balance"]

    #prendo prezzo attuale e lo moltiplico per i fondi usati
    #clientkucoin.create_limit_order(symbolo, ClientKucoin.SIDE_SELL, limitprice, round(float(boughtvalue), 1))

    index=1
    for l in klinesymbol[0:15]:
        print(str(index)+" minuti fa: ", l[2])
        index+=1

    print("prezzo ora ", tickersymbolo["price"])
    stop = datetime.now()
    elapsed = stop-start
    print(elapsed.microseconds//1000," millisecondi")


def telegram_msg(client, message):
    if message.text is not None:
        kucoinindex = message.text.find("kucoin.com/") + len("kucoin.com/")

        usdtindex = message.text.find("-USDT") + 5
        if kucoinindex != -1 and usdtindex != -1:
            symbolo = message.text[kucoinindex:usdtindex]
            if symbolo != "":
                print(symbolo)
                symbol_from_social(symbolo)


def prepareds():
    clientds = discord.Client()
    @clientds.event
    async def on_ready():
        print('We have logged in as {0.user}'.format(clientds))

    @clientds.event
    async def on_message(message):
        if message.content.startswith('BASIC-USDT'):
            symbol_from_social(message.content)

    clientds.run('NDk2Njk4OTY2MTA5NTg1NDEw.YaIIQg.LGcIl2iyUSeFSdL0S2u1Rh9_dWs')

if __name__ == '__main__':
    main()