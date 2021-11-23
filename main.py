from pyrogram import Client
from pyrogram.handlers import MessageHandler

def dump(client, message):
    if message.text is not None:
        print(message.text[message.text.find("kucoin.com/")+10:])

app = Client("WeArePoor")

app.add_handler(MessageHandler(dump))

app.run()