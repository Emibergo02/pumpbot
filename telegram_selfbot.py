from pyrogram import Client
from pyrogram.handlers import MessageHandler
from main import symbol_from_social

session_name = "WeArePoor"
api_id = 12021011
api_hash = "4f747c1fbcad3bbae7dcd03676c9b153"

def dump(client, message):
    if message.text is not None:
        kucoinindex=message.text.find("kucoin.com/")+12
        usdtindex=message.text.find("-USDT")+5
        if kucoinindex != -1 and usdtindex != -1:
            symbolo=message.text[kucoinindex:usdtindex]
            if symbolo != "":
                print(symbolo)
                symbol_from_social(symbolo)

def startTelegram():
    app = Client(session_name, api_id, api_hash)

    app.add_handler(MessageHandler(dump))

    app.run()
